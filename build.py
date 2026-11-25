#!/usr/bin/env python3
"""Writes README.md, the profile page, llms.txt, the index for AI agents and programs, and tools.json, the
live tools as data for the tools page (apapadogiannis.github.io), from papers.toml.

    python3 build.py           # rewrite README.md and llms.txt
    python3 build.py --check   # exit 1 if either is out of date (used by the automated check)
    python3 build.py --fetch   # first read the tools' latest figures from their data files into live.json

Standard library only (Python 3.11+).
"""
import html
import json
import math
import statistics
import re
import sys
import tomllib
from pathlib import Path

import charts

HERE = Path(__file__).parent
GH = "https://github.com/apapadogiannis"
QUESTIONS = [  # key, name, what it asks
    ("creation", "Value creation", "where value comes from"),
    ("returns", "Returns", "required and expected"),
    ("valuation", "Valuation", "the dual-risk framework"),
    ("capture", "Value capture", "what the holder actually keeps"),
]
MAP_ALT = ("Two overlapping circles. Value creation: where value comes from, through cash flows, scarcity, desirability "
           "and adoption. Returns: required and expected, what an asset must earn and is expected to earn. Their overlap is valuation, the "
           "dual-risk framework: a valuation carries two risks, in what the asset delivers and in the return it must "
           "earn. An arrow leads to a band below: value capture, what the holder actually keeps.")


RAW = "https://raw.githubusercontent.com/apapadogiannis"
MONTHS = "January February March April May June July August September October November December".split()


def month(ym):
    """'2026-06' or '2026-06-30' as 'June 2026'."""
    return f"{MONTHS[int(ym[5:7]) - 1]} {ym[:4]}"


def fetch():
    """The latest figures of each tool, from the data file the tool publishes. Written to live.json."""
    from urllib.request import urlopen

    def get(path):
        with urlopen(f"{RAW}/{path}", timeout=60) as r:
            return json.load(r)

    obs = get("crypto-observatory/main/api/data.json")
    m = obs["months"][-1]
    live = {"crypto-observatory": {"month_end": m["month_end"], "required": m["required"],
                                   "terms_at_midpoint": m["terms_at_midpoint"]}}
    lt = get("crypto-observatory/main/api/latest.json")
    key = lambda x, k: x[k + "_pct_per_year"]
    terms = lambda x: [key(x, k) for k in ("risk_free", "market_term", "concentration_term", "mortality_term")]
    assets = [{"name": a["asset_name"], "required": key(a, "required_midpoint"), "low": key(a, "required_lower"),
               "high": key(a, "required_upper"), "terms": terms(a), "sharpe": a["sharpe_ratio"],
               "volatility": a["volatility_pct_annualised"], "compound": key(a, "required_compound")} for a in lt["assets"]]
    bench = [{"name": b["name"], "required": key(b, "required"), "terms": terms(b), "sharpe": b["sharpe_ratio"],
              "volatility": b["volatility_pct_annualised"], "compound": key(b, "required_compound")} for b in lt["benchmarks_for_comparison"]]
    rec = lt.get("bitcoin_delivered_against_required") or {}
    live["crypto-observatory"].update({
        "assets": assets, "benchmarks": bench,
        "record": {k: rec[k] for k in ("period", "share_of_excess_return_explained_by_mcm_pct", "share_explained_by_capm_pct") if k in rec}})
    rows = [assets[0]] + sorted(assets[1:], key=lambda a: -a["required"]) + sorted(bench, key=lambda b: -b["required"])
    live["crypto-observatory"]["picture"] = {
        "alt": "The required return of Bitcoin, Ether, BNB, Solana and Tron, each as a bar made of the risk-free rate, market "
               "risk, concentration risk and mortality risk, with three equity series and gold below for scale",
        "when": month(m["month_end"]), "crypto": len(assets),
        "rows": [{"name": r["name"], "total": r["required"], "terms": r["terms"],
                  **({"band": [r["low"], r["high"]]} if "low" in r else {})} for r in rows]}
    funds = [f for f in get("covered-call-monitor/main/api/funds.json")["funds"]
             if f["role"] == "fund" and f["still_reporting"]]
    pairs = [f["against_benchmark"]["last_12_months"] for f in funds
             if f.get("against_benchmark") and f["against_benchmark"].get("last_12_months")]
    periods = {(p["from"], p["to"]) for p in pairs}
    if len(periods) != 1:
        sys.exit("the funds set beside an index fund do not cover the same twelve months")
    gaps = sorted(p["fund"] - p["benchmark"] for p in pairs)
    index_returns = sorted({round(p["benchmark"], 4) for p in pairs})
    live["covered-call-monitor"] = {"funds": len(funds), "from": pairs[0]["from"], "to": pairs[0]["to"],
                                    "beside_an_index_fund": len(pairs), "returned_less": sum(g < 0 for g in gaps),
                                    "smallest_gap": gaps[-1], "largest_gap": gaps[0],
                                    "median_gap": statistics.median(gaps),
                                    "index_funds_returned": [index_returns[0], index_returns[-1]]}
    detail, years = get("covered-call-monitor/main/api/data.json")["detail"], 3
    to = min(f["months"][-1]["month"] for f in detail)
    bars = []
    for f in detail:
        span = [x for x in f["months"] if x["month"] <= to][-12 * years:]
        grow = lambda key: (math.prod(1 + x[key] / 100 for x in span) - 1) * 100
        if len(span) == 12 * years:
            bars.append({"ticker": f["ticker"], "index_fund": f["benchmark"], "fund": grow("fund"),
                         "benchmark": grow("benchmark"), "from": span[0]["month"]})
    if len({b["from"] for b in bars}) != 1:
        sys.exit("the funds in the picture do not cover the same months")
    live["covered-call-monitor"]["picture"] = {
        "alt": f"Total return over {years} years of {len(bars)} large covered-call funds, each beside the index fund "
               "on the same market",
        "years": years, "from": bars[0]["from"], "to": to,
        "bars": [{k: b[k] for k in ("ticker", "index_fund", "fund", "benchmark")} for b in bars]}
    ex = get("dual-risk-calculator/main/api/example.json")
    live["dual-risk-calculator"] = {"inputs": ex["inputs"], "results": ex["results"], "picture": {
        "alt": "Two bars: the value of a benchmark forecast and of a forecast 10% lower, both discounted at the same "
               "benchmark rate, with the valuation ratio K, the gain of capital and the effective rate",
        "inputs": {"c": ex["inputs"]["c"]}, "results": ex["results"]}}
    paper = get("bitcoin-required-return/main/outputs/results.json")["headline"][0]
    live["crypto-observatory"]["paper"] = {"what": paper["what"], "value": paper["value"], "range": paper["range"]}
    live["crypto-observatory"]["data_to"] = obs["meta"]["data_to"]
    live["covered-call-monitor"]["reports_to"] = get("covered-call-monitor/main/api/index.json")["reports_to"]
    from datetime import date
    live["read_on"] = date.today().isoformat()
    (HERE / "live.json").write_text(json.dumps(live, indent=1) + "\n", encoding="utf-8")
    print("wrote live.json")


def latest(repo, live):
    """One sentence with the tool's latest figures, or nothing if live.json has none for it."""
    d = live.get(repo)
    if not d:
        return ""
    if repo == "crypto-observatory":
        r, t = d["required"], d["terms_at_midpoint"]
        text = (f'<b>Latest, {month(d["month_end"])}:</b> Bitcoin\'s required return is {r["midpoint"]:.1f}% a year: '
                f'risk-free {t["risk_free"]:.1f}, market {t["market"]:.1f}, concentration {t["concentration"]:.1f}, '
                f'mortality {t["mortality"]:.1f}. Across the range of the model\'s inputs it runs from {r["lower"]:.1f}% '
                f'to {r["upper"]:.1f}%.')
        if d.get("assets"):
            others = ", ".join(f'{a["name"]} {a["required"]:.1f}%' for a in d["assets"][1:])
            scale = {b["name"]: b for b in d.get("benchmarks", [])}
            text += f' The same equation gives {others}'
            if "US stock market" in scale and "Gold" in scale:
                text += f', against {scale["US stock market"]["required"]:.1f}% for the US stock market and {scale["Gold"]["required"]:.1f}% for gold'
            text += "."
        return text + two_figures(d)
    if repo == "covered-call-monitor":
        n, less = d["beside_an_index_fund"], d["returned_less"]
        who = f"all {n}" if less == n else f"{less} of the {n}"
        text = (f'<b>Latest, 12 months to {month(d["to"])}:</b> {d["funds"]} covered-call funds are followed. {n} of them '
                f'can be set beside an index fund on the same market, and {who} returned less than it')
        if less == n:
            text += (f', by {-d["smallest_gap"]:.1f} to {-d["largest_gap"]:.1f} percentage points '
                     f'(median {-d["median_gap"]:.1f})')
        text += ", distributions reinvested."
        lo, hi = d["index_funds_returned"]
        if lo > 10:
            text += (f' The index funds returned {lo:.0f}% to {hi:.0f}% over these months: a market that rises this '
                     f'fast is where a cap on the upside costs most.')
        return text
    if repo == "dual-risk-calculator":
        r, c = d["results"], d["inputs"]["c"]
        return (f'<b>Worked example:</b> a forecast {(1 - r["v_own"] / r["v_fair"]) * 100:.0f}% below the benchmark, at a '
                f'benchmark rate of {c * 100:.0f}% over {r["horizon"]:.0f} years, gives a valuation ratio K of {r["K"]:.3f} and a '
                f'gain of capital of {r["gain"]:+.3f}. One discount rate would have to fall to {r["c_eff_stream"] * 100:.1f}% '
                f'to hide the gap ({r["c_eff"] * 100:.1f}% by the article\'s closed form, which is exact for a single payoff).')
    return ""


def two_figures(d):
    """Why the tool's figure and the paper's differ: one sentence, or nothing if the paper's is not on file."""
    p = d.get("paper")
    if not p:
        return ""
    return (f' Each figure is the midpoint of its range. The paper\'s {p["value"]:.1f}% for Bitcoin in {p["what"][-4:]} is '
            f'another measure of the same model: the median when all inputs are varied together.')


def headline(repo, live):
    """For a tool's card on the profile page: (what the figure is, the figure, one line under it)."""
    d = live.get(repo)
    if not d:
        return None
    if repo == "crypto-observatory":
        r = d["required"]
        return (f'Bitcoin\'s required return, {month(d["month_end"])}', f'{r["midpoint"]:.1f}% a year',
                f'The midpoint of a range from {r["lower"]:.1f}% to {r["upper"]:.1f}% across the model\'s inputs. '
                + (f'The paper\'s {d["paper"]["value"]:.1f}% is the median over the same inputs. ' if d.get("paper") else "")
                + 'Recomputed every month.')
    if repo == "covered-call-monitor":
        n, less = d["beside_an_index_fund"], d["returned_less"]
        who = f"all {n}" if less == n else f"{less} of the {n}"
        return ('Covered-call funds followed, each from its SEC filings', f'{d["funds"]} funds',
                f'{n} of them can be set beside an index fund on the same market. Over the 12 months to '
                f'{month(d["to"])}, {who} returned less than it, by {-d["median_gap"]:.1f} percentage points at the '
                f'median, distributions reinvested. Rebuilt every quarter.')
    if repo == "dual-risk-calculator":
        r, c = d["results"], d["inputs"]["c"]
        return (f'Example: a forecast {(1 - r["v_own"] / r["v_fair"]) * 100:.0f}% too low, valued at {c * 100:.0f}% over {r["horizon"]:.0f} years',
                f'K = {r["K"]:.2f}',
                f'One discount rate would have to fall to {r["c_eff_stream"] * 100:.1f}% to hide the gap. Enter your own forecasts or prices.')
    return None


def esc(text):
    return html.escape(text, quote=False)


def badges(p, live_only=False):
    """Live replication badge, then (unless live_only) Zenodo and SSRN, for a paper with a package."""
    wf = f'{GH}/{p["repo"]}/actions/workflows/replicate.yml'
    out = [f'<a href="{wf}"><img src="{wf}/badge.svg" alt="replication"></a>']
    if live_only:
        return out[0]
    if "zenodo" in p:
        out.append(f'<a href="https://doi.org/{p["zenodo"]}"><img src="https://img.shields.io/badge/Zenodo-'
                   f'{p["zenodo"].replace("/", "%2F")}-007ec6" alt="Zenodo"></a>')
    if "ssrn" in p:
        out.append(f'<a href="https://ssrn.com/abstract={p["ssrn"]}"><img src="https://img.shields.io/badge/SSRN-'
                   f'{p["ssrn"]}-1f4e79" alt="SSRN"></a>')
    return " ".join(out)


def card(p):
    """One featured package: colour band, figure, question tag, title, one-sentence summary, live badge."""
    q = p["question"]
    name = next(n for k, n, _ in QUESTIONS if k == q)
    url = f'{GH}/{p["repo"]}'
    return "\n".join([
        '<td width="25%" valign="top">',
        f'<p><img src="assets/q-{q}-band.svg" width="100%" alt=""></p>',
        f'<img src="{p["figure"]}" alt="{html.escape(p["figure_alt"])}">',
        f'<p><img src="assets/q-{q}-tag.svg" height="22" alt="{name}"></p>',
        f'<p><b><a href="{url}">{esc(p["title"])}</a></b></p>',
        f'<p>{p["summary"]}</p>',
        f'<p><sub>{"Peer-reviewed: " + esc(p["venue"]) if "venue" in p else "Working paper"}</sub></p>',
        f'<p><img src="{url}/actions/workflows/replicate.yml/badge.svg" alt="replication check"></p>',
        '</td>'])


def line(p):
    """One paper in a question's list: title, venue, then the links that exist."""
    text = f'<b>{esc(p["title"])}</b>' + ("" if p["title"].endswith("?") else ".")
    if "venue" in p:
        text += f' <b>Peer-reviewed:</b> {esc(p["venue"])}.'
    else:
        text += " Working paper."
    links = []
    if "ssrn" in p:
        links.append(f'<a href="https://ssrn.com/abstract={p["ssrn"]}">SSRN</a>')
    if "published" in p:
        links.append(f'<a href="{p["published"]}">Published version</a>')
    if "repo" in p:
        wf = f'{GH}/{p["repo"]}/actions/workflows/replicate.yml'
        links.append(f'<a href="{GH}/{p["repo"]}">Replication package</a> '
                     f'<a href="{wf}"><img src="{wf}/badge.svg" alt="replication"></a>')
    if "record" in p:   # a paper with nothing to compute: its definitions, model and tables as data
        wf = f'{GH}/{p["record"]}/actions/workflows/check.yml'
        links.append(f'<a href="{GH}/{p["record"]}">Paper record</a> '
                     f'<a href="{wf}"><img src="{wf}/badge.svg" alt="check"></a>')
    if "demo" in p:
        links.append(f'<a href="{p["demo"]}">Interactive demo</a>')
    if "tool" in p:
        links.append(f'<a href="{p["tool_page"]}">{p["tool_label"]}</a>')
    if links:
        text += " " + " · ".join(links)
    if "finding" in p:
        text += f'<br><sub>{esc(p["finding"])}</sub>'
    return f"<li>{text}</li>"


def picture(t):
    """The tool's picture: drawn from its data for a light and a dark page, or the stored file if none is drawn."""
    alt = html.escape(t.get("drawn_alt") or t["figure_alt"])
    if not t.get("drawn_alt"):
        return f'<img src="{t["figure"]}" width="100%" alt="{alt}">'
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{t["repo"]}-dark.svg">'
            f'<source media="(prefers-color-scheme: light)" srcset="assets/{t["repo"]}-light.svg">'
            f'<img src="assets/{t["repo"]}-light.svg" width="100%" alt="{alt}"></picture>')


def tool(t, width):
    """One tool as a card in the row of tools: name, the question it answers, one figure, one link."""
    check = f'{GH}/{t["repo"]}/actions/workflows/{t["workflow"]}'
    name = t["title"].partition(": ")[0]
    h = t.get("headline")
    return "\n".join([
        f'<td width="{width}%" valign="top">',
        f'<h4>{esc(name)}</h4>',
        f'<p>{esc(t["question"])}</p>',
        *([f'<p><sub>{esc(h[0])}</sub></p>', f'<h3>{esc(h[1])}</h3>', f'<p><sub>{esc(h[2])}</sub></p>'] if h else []),
        f'<p><b><a href="{t["page"]}">Open the tool</a></b></p>',
        f'<p><img src="{check}/badge.svg" alt="automated check"></p>',
        '</td>'])


def lead(t, live):
    """The lead tool across the full width: the question, the picture, the latest figures and what the tool does."""
    d = live.get(t["repo"], {})
    name = t["title"].partition(": ")[0]
    check = f'{GH}/{t["repo"]}/actions/workflows/{t["workflow"]}'
    out = [f'### {name}', "", f'**{t["question"]}** {t["pitch"]}', "",
           f'<a href="{t["page"]}">{picture(t)}</a>', ""]
    if d.get("assets"):
        cells = d["assets"] + [b for b in d.get("benchmarks", []) if b["name"] in ("US stock market", "Gold")]
        out += ["<table>", "<tr>" + "".join(f'<th>{esc(c["name"])}</th>' for c in cells) + "</tr>",
                "<tr>" + "".join(f'<td align="center"><b>{c["required"]:.1f}%</b></td>' for c in cells) + "</tr>",
                "<tr>" + "".join(f'<td align="center"><sub>Sharpe ratio {c["sharpe"]:.2f}<br>compounds at {c["compound"]:.1f}%</sub></td>' for c in cells) + "</tr>",
                "</table>", "",
                f'<sub>Required return a year at the end of {month(d["month_end"])}, the midpoint of each asset\'s range. A hurdle rate, not a forecast. '
                "Equities and gold are priced the same way for scale. Read from the tool's own data file every month.</sub>", ""]
    points = list(t["points"])
    rec = d.get("record") or {}
    if rec.get("share_of_excess_return_explained_by_mcm_pct") is not None:
        points.append(f'**The record.** Since {rec["period"][:4]} the three risks account for {rec["share_of_excess_return_explained_by_mcm_pct"]:.0f}% of what Bitcoin '
                      f'delivered over the risk-free rate; market risk alone, as in the CAPM, for {rec["share_explained_by_capm_pct"]:.0f}%.')
    out += [f'- {p}' for p in points] + ["",
            f'**<a href="{t["page"]}">Open the {esc(name)}</a>** · <a href="{t["paper_url"]}">the paper behind it</a> ({t["paper_standing"]}) · '
            f'<a href="{t["page"]}latest.json">the figures as one small file</a> · <img src="{check}/badge.svg" alt="automated check">', ""]
    return out


def build():
    data = tomllib.loads((HERE / "papers.toml").read_text(encoding="utf-8"))
    prof, papers, tools = data["profile"], data["paper"], data.get("tool", [])
    titles = {p["title"] for p in papers}
    pages = {t["repo"]: t["page"] for t in tools}
    by_title = {p["title"]: p for p in papers}
    live_file = HERE / "live.json"
    live = json.loads(live_file.read_text(encoding="utf-8")) if live_file.exists() else {}
    for t in tools:
        t["latest"] = latest(t["repo"], live)
        t["headline"] = headline(t["repo"], live)
        t["drawn_alt"] = live.get(t["repo"], {}).get("picture", {}).get("alt")
        if t["paper"] not in titles:
            sys.exit(f'tool "{t["title"]}" names a paper that is not listed: {t["paper"]}')
        src = by_title[t["paper"]]
        t["paper_url"] = src.get("published") or f'https://ssrn.com/abstract={src["ssrn"]}'
        t["paper_standing"] = f'peer-reviewed, {src["venue"]}' if "venue" in src else "working paper"
    for p in papers:
        if "tool" in p:
            if p["tool"] not in pages:
                sys.exit(f'unknown tool "{p["tool"]}" for: {p["title"]}')
            p["tool_page"] = pages[p["tool"]]
            p["tool_label"] = next(t.get("link_label", "Live tool") for t in tools if t["repo"] == p["tool"])
    known = {k for k, _, _ in QUESTIONS}
    for p in papers:
        if p["question"] not in known:
            sys.exit(f'unknown question "{p["question"]}" for: {p["title"]}')
    featured = []
    for k, name, _ in QUESTIONS:
        f = [p for p in papers if p["question"] == k and p.get("featured")]
        if len(f) > 1:
            sys.exit(f"more than one featured package for {name}")
        featured += f

    counts = {"papers": len(papers), "packages": sum("repo" in p for p in papers), "tools": len(tools),
              "published": sum("venue" in p for p in papers)}
    words = "zero one two three four five six seven eight nine ten eleven twelve".split()
    counts["rest"] = counts["papers"] - counts["packages"]
    counts["both"] = sum("repo" in p and "venue" in p for p in papers)
    journals = []
    for p in papers:
        name = p.get("venue", "").split(",")[0].strip()
        if name and name not in journals:
            journals.append(name)
    counts["journals"] = ", ".join(journals[:-1]) + " and " + journals[-1]
    for key in ("tools", "packages"):  # as words, for the sentence under the name
        counts[key + "_word"] = words[counts[key]] if counts[key] < len(words) else str(counts[key])
    counts["Tools_word"] = counts["tools_word"].capitalize()
    counts["published_word"] = words[counts["published"]] if counts["published"] < len(words) else str(counts["published"])
    out = [f'## {prof["name"]}', "", f'**{prof["position"]}** {prof["forms"].format(**counts)}', "",
           " · ".join(f'<a href="{url}">{esc(label)}</a>' for label, url in prof["links"]), "",
           ""]
    first = next((t for t in tools if t.get("lead")), None)
    rest = [t for t in tools if t is not first]
    if first:
        out += lead(first, live)
    out += ["| If you want to | Start here |", "|---|---|",
            (f'| get an answer to a question | the [{first["title"].partition(": ")[0]}](#{first["title"].partition(": ")[0].lower().replace(" ", "-")}) above, and [{words[len(rest)]} more tools](#more-tools), free, no account |'
             if first else f'| get an answer to a question | [Tools](#tools): {counts["tools_word"]} pages, free, no account |'),
            "| ask through your own AI assistant | [For your AI assistant](#for-your-ai-assistant): one skill, and a calculator it can call |",
            f'| read the research or check a number | [The research](#the-research-one-corpus-four-questions): {counts["papers"]} papers, '
            f'{counts["published"]} peer-reviewed, {counts["packages"]} with data and code |', ""]

    if rest:
        out += ["### More tools" if first else "### Tools", "",
                "Each answers one question, from current public data or from your own numbers. The figures below are "
                "read from the tools' own data files every month.", "", "<table>", "<tr>"]
        out += [tool(t, 100 // len(rest)) for t in rest]
        out += ["</tr>", "</table>", "",
                f'All {counts["tools_word"]} on one page, each with its chart: **[apapadogiannis.github.io](https://apapadogiannis.github.io/)**', ""]

    rows = [(t["skill_for"], t["skill_ask"]) for t in tools] + [(prof["skill_for"], prof["skill_ask"])]
    one, one_raw = "papadogiannis-finance-research", "apapadogiannis/main/skill/SKILL.md"
    out += ["### For your AI assistant", ""]
    for para in prof["skills"]:
        out += [para.format(**counts), ""]
    out += [f'**One skill covers everything here:** <a href="{GH}/apapadogiannis/blob/main/skill/SKILL.md"><code>{one}</code></a>. '
            "With it your assistant can answer, for example:", "",
            "<table>", "<tr><th>What it answers</th><th>A question to try</th></tr>"]
    out += [f'<tr><td>{esc(what)}</td><td>“{esc(ask)}”</td></tr>' for what, ask in rows]
    out += ["</table>", "", "<details>", "<summary>How to add it</summary>", "",
            "In Claude Code, one file in one folder:", "", "```",
            f"mkdir -p ~/.claude/skills/{one}",
            f"curl -o ~/.claude/skills/{one}/SKILL.md {RAW}/{one_raw}",
            "```", "",
            "In another assistant, add the same file wherever it takes instructions or skills, or give it the "
            "address of [llms.txt](llms.txt). It replaces the separate skills the tools used to publish. "
            "The Bitcoin and Ether price inputs come from Coin Metrics community "
            "data, which are for non-commercial use, as the Observatory's guide states.", "",
            "</details>", "",
            "**The calculator is also an MCP server.** A skill tells an assistant where to read figures. An MCP server "
            "gives it a tool to call: the assistant sends your numbers and gets the result computed, not estimated. "
            f"It runs on your own machine, and the install line is in [its repository]({GH}/dual-risk-calculator#use-it-from-your-own-ai-agent).", "",
            f'<sub>{prof["agents"]}</sub>', ""]

    out += ["### The research: one corpus, four questions", ""]
    for para in prof["intro"]:
        out += [para.format(**counts), ""]
    out += [prof["checked"].format(**counts), ""]
    out += ['<p align="center">', '<picture>',
            '<source media="(prefers-color-scheme: dark)" srcset="assets/map-dark.svg">',
            '<source media="(prefers-color-scheme: light)" srcset="assets/map-light.svg">',
            f'<img src="assets/map-light.svg" width="720" alt="{MAP_ALT}">',
            '</picture>', '</p>', ""]

    out += ["### Four papers, one per question", "",
            "Each comes with its data and code.", "", "<table>"]
    out += ["<tr>"] + [card(p) for p in featured] + ["</tr>"]
    out += ["</table>", ""]

    out += ["### All papers by question", "",
            "Click a line to open its list. A green badge means the package's stored results were reproduced at "
            "the last automated run.", ""]
    for k, name, what in QUESTIONS:
        mine = [p for p in papers if p["question"] == k]
        mine.sort(key=lambda p: ("repo" not in p, "record" not in p))  # papers with a replication package first; order otherwise as in papers.toml
        n_pk = sum("repo" in p for p in mine)
        count = f'{len(mine)} paper{"s" if len(mine) != 1 else ""}'
        if n_pk:
            count += f', {n_pk} with a replication package'
        n_rec = sum("record" in p for p in mine)
        if n_rec:
            count += f', {n_rec} with a paper record'
        out += ["<details>",
                f'<summary><img src="assets/q-{k}-dot.svg" width="12" height="12" alt=""> <b>{name}</b>: {what} ({count})</summary>',
                "<ul>"] + [line(p) for p in mine] + ["</ul>", "</details>", ""]

    out += ["### About", "", prof["about"], ""]

    return {"README.md": "\n".join(out), "llms.txt": index(prof, papers, tools, live, counts),
            "skill/SKILL.md": skill(prof, papers, tools, counts), "tools.json": tools_file(tools),
            **charts.pictures(live)}


def tools_file(tools):
    """tools.json: the live tools as data. The tools page, apapadogiannis.github.io, draws its cards from this file."""
    raw = "https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main"
    rows = []
    for t in tools:
        name, _, rest = t["title"].partition(": ")
        m = re.fullmatch(r"<b>(.*?)</b> (.*)", t["latest"] or "")
        rows.append({
            "name": name, "subtitle": rest, "summary": t["summary"],
            "latest_label": m.group(1) if m else "", "latest": m.group(2) if m else "",
            "caption": t.get("caption", ""), "picture_alt": t.get("drawn_alt") or t.get("figure_alt", ""),
            "picture_light": f'{raw}/assets/{t["repo"]}-light.svg', "picture_dark": f'{raw}/assets/{t["repo"]}-dark.svg',
            "page": t["page"], "code": f'{GH}/{t["repo"]}',
            "paper": t["paper"], "paper_role": t.get("paper_role", "Method"), "paper_url": t["paper_url"],
            "paper_standing": t["paper_standing"]})
    return json.dumps({"tools": rows}, indent=1, ensure_ascii=False) + "\n"


def skill(prof, papers, tools, counts):
    """skill/SKILL.md: a skill a reader can add to their own AI agent, pointing it at the index."""
    raw = "https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main/llms.txt"
    packaged = [p for p in papers if "repo" in p]
    lines = ["---", "name: papadogiannis-finance-research",
             "description: Open finance research by Agisilaos Papadogiannis, with replication packages and live tools, on "
             "Bitcoin's required and expected return, the valuation of scarcity and of blockchain networks, covered-call "
             "funds, broad index investing and AI, discount rates and unpriced risk. Use when asked what one of these "
             "papers says or reports, for a number from one of them, for the latest figure of a live tool, or which of "
             f"them covers a topic. {counts['packages']} of the {counts['papers']} papers come with data and code; the others are papers only.",
             "---", "", f'# Research by {prof["name"]}', "",
             "This one skill covers the whole account: the live tools and every paper. It tells you where the work is",
             "and how to reach a number. It holds no figures: fetch them each time.", "",
             "## Steps", "",
             f"1. Fetch the index: {raw}",
             "   It lists every tool, paper, replication package and paper record under four questions, with the address of",
             "   each guide.",
             "2. Open the guide of the repository the question is about (an `llms.txt`). It states the headline",
             "   figures, which file holds what, how to read the figures and what they cannot answer.",
             "3. For a number, use the file the guide names, usually `outputs/results.json` in a package.",
             "   Quote it with its unit and date, and cite the paper as the guide says.",
             "4. For a paper that has no package, the index gives its venue and its SSRN or published address. Say what",
             "   the paper is and where it is; do not state a number from it unless you have read the paper itself.", "",
             "## What is there", "",
             "Live tools. Read the guide first: it has the reading rules and says which data file to fetch.", ""]
    for t in tools:
        lines += [f'- {t["title"]}', f'  Use for: {t["skill_for"]}', f'  Guide: {t["page"]}llms.txt',
                  f'  Same guide in the repository: {RAW}/{t["repo"]}/main/api/llms.txt']
    lines += ["", "Papers with a replication package, each with its guide:", ""]
    for p in packaged:
        lines += [f'- {p["title"]}', f'  Guide: {RAW}/{p["repo"]}/main/llms.txt']
    recorded = [p for p in papers if "record" in p]
    if recorded:
        lines += ["", "Papers with a paper record (no computation; the definitions, model and tables as data):", ""]
        for p in recorded:
            lines += [f'- {p["title"]}', f'  Guide: {RAW}/{p["record"]}/main/llms.txt']
    rest = [p for p in papers if "repo" not in p and "record" not in p]
    lines += ["", f"The other {len(rest)} papers have no package. They are listed in the index with their addresses."]
    lines += ["", "## Rules", "",
              "- A tool and the paper behind it can give different figures for the same thing, because a tool is",
              "  recomputed and a paper is a fixed record. Give the tool's figure with its date for a question about",
              "  now, and the paper's for what the paper reports. Say which one you are giving.",
              "- A replication package is a fixed record of one paper. For current figures use the live tool the",
              "  guide points to.",
              f"- {counts['published']} of the {counts['papers']} papers are peer-reviewed journal articles, published or accepted; the index marks each one.",
              "  The others are working papers. Say which a paper is, and report a figure as that paper's result.",
              "- For the calculator: if the tools of the MCP server `dual-risk` are available to you, use them and do",
              "  not do the arithmetic yourself.",
              "- The results are under CC BY 4.0, whose one condition is credit: cite the paper.",
              "- A published article belongs to its publisher. The packages hold its numbers, not its text.", "",
              f"Page for people: {GH}", ""]
    return "\n".join(lines)


def index(prof, papers, tools, live, counts):
    """llms.txt: every tool and paper in one list, with the address of its own guide where it has one."""
    raw = "https://raw.githubusercontent.com/apapadogiannis"
    out = [f'# {prof["name"]}: open finance research', "",
           f"In the {counts['tools_word']} tools and the {counts['packages_word']} replication packages, every published number is recomputed "
           "automatically, with machine-readable results and stated limits. "
           f"The other {counts['rest']} of the {counts['papers']} papers are papers only: they are listed here with their addresses. "
           f"{counts['published']} of the {counts['papers']} papers are peer-reviewed journal articles, published or accepted; each entry says which.", "",
           "> An index of this account for AI agents and other programs: live tools, papers and replication",
           "> packages. Where an entry has a guide, the guide says what the repository holds, what it adds,",
           "> which file to use, what not to use it for, and how to cite it.", "",
           f"Page for people: {GH}", "",
           "The work follows value through four questions: " +
           "; ".join(f"{name.lower()} ({what})" for _, name, what in QUESTIONS) + ".", "",
           "## Tools", "",
           "The Observatory and the Monitor recompute their figures from current public data and publish them as data",
           "files beside their pages. The Calculator holds no data: it computes from the numbers it is given, as a page",
           "and as an MCP server.", ""]
    for t in tools:
        out += [f'- {t["title"]}', f'  Page: {t["page"]}', f'  Guide: {t["page"]}llms.txt',
                f'  Same guide in the repository: {raw}/{t["repo"]}/main/api/llms.txt',
                f'  Code and data: {GH}/{t["repo"]}', f'  {t.get("paper_role", "Method")}: {t["paper"]}']
        m = re.fullmatch(r"<b>(.*?)</b> (.*)", t["latest"] or "")
        if m:
            out.append(f'  {html.unescape(m.group(1))} {html.unescape(m.group(2))}')
        out.append("")
    if live.get("read_on"):
        o, cc = live.get("crypto-observatory", {}), live.get("covered-call-monitor", {})
        out += [f"The figures above were read from the tools' own data files on {live['read_on']}"
                + (f" (Observatory: data to {o['data_to']}" if o.get("data_to") else " (")
                + (f"; Monitor: fund reports to {cc['reports_to']}" if cc.get("reports_to") else "")
                + "). They are copies: a tool's guide always has its current figures.", ""]
    out += ["## Skill", "",
            "One instruction file a reader adds to their own AI agent covers the whole account, tools and papers. It",
            "says when to use the work, where the files are and how to read them, and holds no figures.", "",
            f'- papadogiannis-finance-research: {raw}/apapadogiannis/main/skill/SKILL.md', ""]
    for k, name, what in QUESTIONS:
        out += [f"## {name}: {what}", ""]
        mine = [p for p in papers if p["question"] == k]
        mine.sort(key=lambda p: (not p.get("guide"), "repo" not in p, "record" not in p))
        for p in mine:
            out.append(f'- {p["title"]}')
            out.append(f'  Peer-reviewed journal article: {p["venue"]}.' if "venue" in p else "  Working paper, not peer-reviewed.")
            if "finding" in p:
                out.append(f'  In one sentence: {p["finding"]}')
            if "published" in p:
                out.append(f'  Published article: {p["published"]}')
            if "ssrn" in p:
                out.append(f'  SSRN: https://ssrn.com/abstract={p["ssrn"]}')
            if "repo" in p:
                out.append(f'  Replication package: {GH}/{p["repo"]}' + (f' (archive: https://doi.org/{p["zenodo"]})' if "zenodo" in p else ""))
            if "record" in p:
                out.append(f'  Paper record (the paper has no computation; its definitions, model and tables as data): {GH}/{p["record"]}'
                           + (f' (archive: https://doi.org/{p["zenodo"]})' if "zenodo" in p else ""))
            if p.get("guide"):
                out.append(f'  Guide: {raw}/{p.get("repo") or p["record"]}/main/llms.txt')
                out.append(f'  Results as data: {raw}/{p.get("repo") or p["record"]}/main/outputs/results.json')
            elif "repo" in p:
                out.append("  No guide yet: the README of the package describes its files.")
            if "tool_page" in p:
                out.append(f'  Live tool: {p["tool_page"]}')
            out.append("")
    out += ["## Licence and credit", "",
            "Each repository states its own licence. In general the code is under the MIT License and the results",
            "under CC BY 4.0, whose one condition is credit: cite the paper, or the tool, as its guide says.",
            "Published articles belong to their publishers and are not reproduced in these repositories.", ""]
    return "\n".join(out)


if __name__ == "__main__":
    if "--fetch" in sys.argv[1:]:
        fetch()
    files = build()
    for name, text in files.items():
        target = HERE / name
        target.parent.mkdir(exist_ok=True)
        if "--check" in sys.argv[1:]:
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                sys.exit(f"{name} is out of date: run  python3 build.py")
            print(f"{name} is up to date")
        else:
            target.write_text(text, encoding="utf-8")
            print(f"wrote {name}")
