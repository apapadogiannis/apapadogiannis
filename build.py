#!/usr/bin/env python3
"""Writes README.md, the profile page, and llms.txt, the index for AI agents and programs, from papers.toml.

    python3 build.py           # rewrite README.md and llms.txt
    python3 build.py --check   # exit 1 if either is out of date (used by the automated check)
    python3 build.py --fetch   # first read the tools' latest figures from their data files into live.json

Standard library only (Python 3.11+).
"""
import html
import json
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).parent
GH = "https://github.com/apapadogiannis"
QUESTIONS = [  # key, name, what it asks
    ("creation", "Value creation", "where value comes from"),
    ("returns", "Returns", "required and expected"),
    ("valuation", "Valuation", "the dual-risk framework"),
    ("capture", "Value capture", "what the holder actually keeps"),
]
MAP_ALT = ("Two overlapping circles. Value creation: where value comes from, with the risk in the cash flows. "
           "Returns: required and expected, with the risk in the required return. Their overlap is valuation, "
           "the dual-risk framework. An arrow leads to a band below: value capture, what the holder actually keeps.")


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

    m = get("crypto-observatory/main/api/data.json")["months"][-1]
    live = {"crypto-observatory": {"month_end": m["month_end"], "required": m["required"],
                                   "terms_at_midpoint": m["terms_at_midpoint"]}}
    funds = [f for f in get("covered-call-monitor/main/api/funds.json")["funds"]
             if f["role"] == "fund" and f["still_reporting"]]
    pairs = [f["against_benchmark"]["last_12_months"] for f in funds
             if f.get("against_benchmark") and f["against_benchmark"].get("last_12_months")]
    periods = {(p["from"], p["to"]) for p in pairs}
    if len(periods) != 1:
        sys.exit("the funds set beside an index fund do not cover the same twelve months")
    gaps = sorted(p["fund"] - p["benchmark"] for p in pairs)
    live["covered-call-monitor"] = {"funds": len(funds), "from": pairs[0]["from"], "to": pairs[0]["to"],
                                    "beside_an_index_fund": len(pairs), "returned_less": sum(g < 0 for g in gaps),
                                    "smallest_gap": gaps[-1], "largest_gap": gaps[0]}
    (HERE / "live.json").write_text(json.dumps(live, indent=1) + "\n", encoding="utf-8")
    print("wrote live.json")


def latest(repo, live):
    """One sentence with the tool's latest figures, or nothing if live.json has none for it."""
    d = live.get(repo)
    if not d:
        return ""
    if repo == "crypto-observatory":
        r, t = d["required"], d["terms_at_midpoint"]
        return (f'<b>Latest, {month(d["month_end"])}:</b> Bitcoin\'s required return is {r["midpoint"]:.1f}% a year '
                f'(band {r["lower"]:.1f}% to {r["upper"]:.1f}%). Of the midpoint: risk-free {t["risk_free"]:.1f}, '
                f'market {t["market"]:.1f}, concentration {t["concentration"]:.1f}, mortality {t["mortality"]:.1f}.')
    if repo == "covered-call-monitor":
        n, less = d["beside_an_index_fund"], d["returned_less"]
        who = f"all {n}" if less == n else f"{less} of the {n}"
        text = (f'<b>Latest, 12 months to {month(d["to"])}:</b> {who} funds that have an index fund on the same market '
                f'beside them returned less than it')
        if less == n:
            text += f', by {-d["smallest_gap"]:.1f} to {-d["largest_gap"]:.1f} percentage points'
        return text + ", distributions reinvested."
    return ""


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
        f'<a href="{url}"><img src="{p["figure"]}" alt="{html.escape(p["figure_alt"])}"></a>',
        f'<p><img src="assets/q-{q}-tag.svg" height="22" alt="{name}"></p>',
        f'<p><b><a href="{url}">{esc(p["title"])}</a></b></p>',
        f'<p>{p["summary"]}</p>',
        f'<p>{badges(p, live_only=True)}</p>',
        '</td>'])


def line(p):
    """One paper in a question's list: title, venue, then the links that exist."""
    text = f'<b>{esc(p["title"])}</b>' + ("" if p["title"].endswith("?") else ".")
    if "venue" in p:
        text += f' {esc(p["venue"])}.'
    links = []
    if "ssrn" in p:
        links.append(f'<a href="https://ssrn.com/abstract={p["ssrn"]}">SSRN</a>')
    if "published" in p:
        links.append(f'<a href="{p["published"]}">Published version</a>')
    if "repo" in p:
        wf = f'{GH}/{p["repo"]}/actions/workflows/replicate.yml'
        links.append(f'<a href="{GH}/{p["repo"]}">Replication package</a> '
                     f'<a href="{wf}"><img src="{wf}/badge.svg" alt="replication"></a>')
    if "demo" in p:
        links.append(f'<a href="{p["demo"]}">Interactive demo</a>')
    if "tool" in p:
        links.append(f'<a href="{p["tool_page"]}">Live tool</a>')
    if links:
        text += " " + " · ".join(links)
    return f"<li>{text}</li>"


def tool(t):
    """One application: its picture beside its name, what it does and where it runs."""
    repo = f'{GH}/{t["repo"]}'
    check = f'{repo}/actions/workflows/{t["workflow"]}'
    return "\n".join([
        "<table>", "<tr>",
        '<td width="45%" valign="top">',
        f'<a href="{t["page"]}"><img src="{t["figure"]}" alt="{html.escape(t["figure_alt"])}"></a>',
        "</td>",
        '<td valign="top">',
        f'<p><b><a href="{t["page"]}">{esc(t["title"])}</a></b></p>',
        f'<p>{esc(t["summary"])}</p>',
        *([f'<p>{t["latest"]}</p>'] if t.get("latest") else []),
        f'<p><a href="{t["page"]}">Open the page</a> · <a href="{repo}">Code and data</a> '
        f'<a href="{check}"><img src="{check}/badge.svg" alt="check"></a></p>',
        f'<p><sub>{t.get("paper_role", "Method")}: {t["paper_link"]}</sub></p>',
        "</td>", "</tr>", "</table>"])


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
        if t["paper"] not in titles:
            sys.exit(f'tool "{t["title"]}" names a paper that is not listed: {t["paper"]}')
        src = by_title[t["paper"]]
        t["paper_link"] = (f'<a href="https://ssrn.com/abstract={src["ssrn"]}">{esc(t["paper"])}</a>' if "ssrn" in src else esc(t["paper"]))
    for p in papers:
        if "tool" in p:
            if p["tool"] not in pages:
                sys.exit(f'unknown tool "{p["tool"]}" for: {p["title"]}')
            p["tool_page"] = pages[p["tool"]]
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
    counts["rest"] = counts["papers"] - counts["packages"]
    words = "zero one two three four five six seven eight nine ten eleven twelve".split()
    for key in ("tools", "packages"):  # as words, for the sentence under the name
        counts[key + "_word"] = words[counts[key]] if counts[key] < len(words) else str(counts[key])
    counts["Tools_word"] = counts["tools_word"].capitalize()
    out = [f'## {prof["name"]}', "", f'**{prof["position"].format(**counts)}**', "",
           " · ".join(f'<a href="{url}">{esc(label)}</a>' for label, url in prof["links"]), "",
           prof["checked"].format(**counts), ""]

    if tools:
        out += ["### Live tools", "",
                "Research that keeps running: each page rebuilds itself from current public data, and only after an "
                "automated check has reproduced a fixed set of reference results. The figures below are read from "
                "the tools' own data files every month.", ""]
        for t in tools:
            out += [tool(t), ""]

    out += ["### The research", ""]
    for para in prof["intro"]:
        out += [para.format(**counts), ""]
    out += ['<p align="center">', '<picture>',
            '<source media="(prefers-color-scheme: dark)" srcset="assets/map-dark.svg">',
            '<source media="(prefers-color-scheme: light)" srcset="assets/map-light.svg">',
            f'<img src="assets/map-light.svg" width="720" alt="{MAP_ALT}">',
            '</picture>', '</p>', ""]

    out += ["### Four papers, one per question", "",
            "Each has a replication package, with one script that regenerates every table and figure.", "", "<table>"]
    out += ["<tr>"] + [card(p) for p in featured] + ["</tr>"]
    out += ["</table>", ""]

    out += ["### All papers by question", "",
            "Click a line to open its list. A green badge is live: it turns red if any stored result of that "
            "package is not reproduced to nine significant digits.", ""]
    for k, name, what in QUESTIONS:
        mine = [p for p in papers if p["question"] == k]
        mine.sort(key=lambda p: "repo" not in p)  # papers with a replication package first; order otherwise as in papers.toml
        n_pk = sum("repo" in p for p in mine)
        count = f'{len(mine)} paper{"s" if len(mine) != 1 else ""}'
        if n_pk:
            count += f', {n_pk} with a replication package'
        out += ["<details>",
                f'<summary><img src="assets/q-{k}-dot.svg" width="12" height="12" alt=""> <b>{name}</b>: {what} ({count})</summary>',
                "<ul>"] + [line(p) for p in mine] + ["</ul>", "</details>", ""]

    out += ["### For AI agents and programs", "", prof["agents"], "", "### About", "", prof["about"], ""]

    return "\n".join(out), index(prof, papers, tools), skill(prof, papers, tools)


def skill(prof, papers, tools):
    """skill/SKILL.md: a skill a reader can add to their own AI agent, pointing it at the index."""
    raw = "https://raw.githubusercontent.com/apapadogiannis/apapadogiannis/main/llms.txt"
    packaged = [p for p in papers if "repo" in p]
    lines = ["---", "name: papadogiannis-finance-research",
             "description: Open finance research by Agisilaos Papadogiannis, with replication packages and live tools, on "
             "Bitcoin's required and expected return, the valuation of scarcity and of blockchain networks, covered-call "
             "funds, broad index investing and AI, discount rates and unpriced risk. Use when asked what one of these "
             "papers says or reports, for a number from one of them, or which of them covers a topic. Every published "
             "number comes with data and code.",
             "---", "", f'# Research by {prof["name"]}', "",
             "This skill tells you where the work is and how to reach a paper's numbers. It holds no figures:",
             "fetch them each time.", "",
             "## Steps", "",
             f"1. Fetch the index: {raw}",
             "   It lists every tool, paper and replication package under four questions, with the address of",
             "   each guide.",
             "2. Open the guide of the repository the question is about (an `llms.txt`). It states the headline",
             "   figures, which file holds what, how to read the figures and what they cannot answer.",
             "3. For a number, use the file the guide names, usually `outputs/results.json` in a package.",
             "   Quote it with its unit and date, and cite the paper as the guide says.", "",
             "## What is there", "",
             "Live tools, each with its own skill and guide:", ""]
    lines += [f'- {t["title"]}: {t["page"]}llms.txt' for t in tools]
    lines += ["", "Papers with a replication package:", ""]
    lines += [f'- {p["title"]}' for p in packaged]
    lines += ["", "## Rules", "",
              "- A replication package is a fixed record of one paper. For current figures use the live tool the",
              "  guide points to.",
              "- Several papers are working papers. Say so, and report a figure as that paper's result.",
              "- The results are under CC BY 4.0, whose one condition is credit: cite the paper.",
              "- A published article belongs to its publisher. The packages hold its numbers, not its text.", "",
              f"Page for people: {GH}", ""]
    return "\n".join(lines)


def index(prof, papers, tools):
    """llms.txt: every tool and paper in one list, with the address of its own guide where it has one."""
    raw = "https://raw.githubusercontent.com/apapadogiannis"
    out = [f'# {prof["name"]}: open finance research', "",
           "Every published number is recomputed automatically, with machine-readable results and stated limits.", "",
           "> An index of this account for AI agents and other programs: live tools, papers and replication",
           "> packages. Where an entry has a guide, the guide says what the repository holds, what it adds,",
           "> which file to use, what not to use it for, and how to cite it.", "",
           f"Page for people: {GH}", "",
           "The work follows value through four questions: " +
           "; ".join(f"{name.lower()} ({what})" for _, name, what in QUESTIONS) + ".", "",
           "## Live tools", "",
           "Each recomputes its figures from current public data and publishes them as data files beside its page.", ""]
    for t in tools:
        out += [f'- {t["title"]}', f'  Page: {t["page"]}', f'  Guide: {t["page"]}llms.txt',
                f'  Same guide in the repository: {raw}/{t["repo"]}/main/api/llms.txt',
                f'  Code and data: {GH}/{t["repo"]}', f'  {t.get("paper_role", "Method")}: {t["paper"]}', ""]
    for k, name, what in QUESTIONS:
        out += [f"## {name}: {what}", ""]
        mine = [p for p in papers if p["question"] == k]
        mine.sort(key=lambda p: (not p.get("guide"), "repo" not in p))
        for p in mine:
            out.append(f'- {p["title"]}')
            out.append(f'  {p["venue"]}.' if "venue" in p else "  Working paper.")
            if "published" in p:
                out.append(f'  Published article: {p["published"]}')
            if "ssrn" in p:
                out.append(f'  SSRN: https://ssrn.com/abstract={p["ssrn"]}')
            if "repo" in p:
                out.append(f'  Replication package: {GH}/{p["repo"]}' + (f' (archive: https://doi.org/{p["zenodo"]})' if "zenodo" in p else ""))
            if p.get("guide"):
                out.append(f'  Guide: {raw}/{p["repo"]}/main/llms.txt')
                out.append(f'  Results as data: {raw}/{p["repo"]}/main/outputs/results.json')
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
    files = dict(zip(("README.md", "llms.txt", "skill/SKILL.md"), build()))
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
