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
    ("valuation", "Valuation", "what an asset is worth"),
    ("pricing", "Pricing", "what return it must earn"),
    ("dual-risk", "Dual-risk framework", "where valuation and pricing meet"),
    ("capture", "Capture", "what the holder actually keeps"),
]
MAP_ALT = ("Two overlapping circles. Valuation: what an asset is worth. Pricing: what return it must earn. "
           "Their overlap is the dual-risk framework, in which expected cash flows shift the required return "
           "and the required return sets the value. Both lead to a band below: capture, what the holder actually keeps.")


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
        f'<p><img src="assets/hband-{q}.svg" width="100%" alt=""></p>',
        f'<a href="{url}"><img src="{p["figure"]}" alt="{html.escape(p["figure_alt"])}"></a>',
        f'<p><img src="assets/tag-{q}.svg" height="22" alt="{name}"></p>',
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
    if links:
        text += " " + " · ".join(links)
    return f"<li>{text}</li>"


def build():
    data = tomllib.loads((HERE / "papers.toml").read_text(encoding="utf-8"))
    prof, papers = data["profile"], data["paper"]
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

    out = [f'## {prof["name"]}', ""]
    for para in prof["intro"]:
        out += [para, ""]
    out += ['<p align="center">', '<picture>',
            '<source media="(prefers-color-scheme: dark)" srcset="assets/research-map-dark.svg">',
            '<source media="(prefers-color-scheme: light)" srcset="assets/research-map-light.svg">',
            f'<img src="assets/research-map-light.svg" width="820" alt="{MAP_ALT}">',
            '</picture>', '</p>', ""]

    out += ["### Featured replication packages", "",
            "One per question. Each holds the data and code behind a paper, with one script that regenerates "
            "every table and figure.", "", "<table>"]
    out += ["<tr>"] + [card(p) for p in featured] + ["</tr>"]
    out += ["</table>", ""]

    out += ["### All papers by question", "",
            "Click a line to open its list. Where a paper has a replication package, the green badge is live: "
            "GitHub re-runs the full pipeline on a clean machine at every change and once a month, and the badge "
            "turns red if a single table differs from the published one.", ""]
    for k, name, what in QUESTIONS:
        mine = [p for p in papers if p["question"] == k]
        n_pk = sum("repo" in p for p in mine)
        count = f'{len(mine)} paper{"s" if len(mine) != 1 else ""}'
        if n_pk:
            count += f', {n_pk} with a replication package'
        out += ["<details>",
                f'<summary><img src="assets/dot-{k}.svg" width="12" height="12" alt=""> <b>{name}</b>: {what} ({count})</summary>',
                "<ul>"] + [line(p) for p in mine] + ["</ul>", "</details>", ""]

    out += ["### Elsewhere", "", prof["elsewhere"].strip(), ""]
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
