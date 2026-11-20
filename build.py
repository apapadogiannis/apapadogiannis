#!/usr/bin/env python3
"""Writes README.md, the profile page, from papers.toml.

    python3 build.py           # rewrite README.md
    python3 build.py --check   # exit 1 if README.md is out of date (used by the automated check)

Standard library only (Python 3.11+).
"""
import html
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
MAP_ALT = ("Two overlapping circles. Value creation: where value comes from. Returns: required and expected. "
           "Their overlap is valuation, the dual-risk framework: a valuation carries two risks, in the cash flows "
           "and in the required return. Both lead to a band below: value capture, what the holder actually keeps.")


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
        f'<p>Implements <i>{esc(t["paper"])}</i>.</p>',
        f'<p><a href="{t["page"]}">Open the page</a> · <a href="{repo}">Code and data</a> '
        f'<a href="{check}"><img src="{check}/badge.svg" alt="check"></a></p>',
        "</td>", "</tr>", "</table>"])


def build():
    data = tomllib.loads((HERE / "papers.toml").read_text(encoding="utf-8"))
    prof, papers, tools = data["profile"], data["paper"], data.get("tool", [])
    titles = {p["title"] for p in papers}
    pages = {t["repo"]: t["page"] for t in tools}
    for t in tools:
        if t["paper"] not in titles:
            sys.exit(f'tool "{t["title"]}" names a paper that is not listed: {t["paper"]}')
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

    out = [f'## {prof["name"]}', "", prof["links"].strip(), ""]
    for para in prof["intro"]:
        out += [para, ""]
    out += ['<p align="center">', '<picture>',
            '<source media="(prefers-color-scheme: dark)" srcset="assets/map-dark.svg">',
            '<source media="(prefers-color-scheme: light)" srcset="assets/map-light.svg">',
            f'<img src="assets/map-light.svg" width="720" alt="{MAP_ALT}">',
            '</picture>', '</p>', ""]

    out += ["### Featured replication packages", "",
            "One per question. Each holds the data and code behind a paper, with one script that regenerates "
            "every table and figure.", "", "<table>"]
    out += ["<tr>"] + [card(p) for p in featured] + ["</tr>"]
    out += ["</table>", ""]

    if tools:
        out += ["### Tools", "",
                "Research that keeps running: each tool applies a paper's method to current public data, on a page that "
                "updates itself. The badge shows the latest automated check, which reruns the paper's stored results "
                "before the page is rebuilt.", ""]
        for t in tools:
            out += [tool(t), ""]

    out += ["### All papers by question", "",
            "Click a line to open its list. Where a paper has a replication package, the green badge is live: "
            "GitHub re-runs the full pipeline on a clean machine at every change and once a month, and the badge "
            "turns red if any stored result is not reproduced to nine significant digits.", ""]
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

    return "\n".join(out)


if __name__ == "__main__":
    page = build()
    target = HERE / "README.md"
    if "--check" in sys.argv[1:]:
        if not target.exists() or target.read_text(encoding="utf-8") != page:
            sys.exit("README.md is out of date: run  python3 build.py")
        print("README.md is up to date")
    else:
        target.write_text(page, encoding="utf-8")
        print(f"wrote {target.name}")
