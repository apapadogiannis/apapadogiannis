"""The two pictures of the live tools on the profile page, drawn as SVG from live.json.

Called by build.py. Standard library only. Each picture is written twice, for a light and a dark page;
the colours are those of the tools' own pages.
"""
import math

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
THEMES = {
    "light": dict(ink="#0b0b0b", ink2="#52514e", mut="#898781", line="#e1e0d9", axis="#c3c2b7",
                  blue="#2a78d6", band="#cde2fb", orange="#eb6834", page="#ffffff", rf="#b9b8ae", violet="#6250d6", aqua="#1baf7a"),
    "dark": dict(ink="#f0efec", ink2="#c3c2b7", mut="#898781", line="#2e2e2b", axis="#52514e",
                 blue="#3987e5", band="#173a66", orange="#d95926", page="#0d1117", rf="#6b6a64", violet="#9085e9", aqua="#199e70"),
}
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
W, H = 1040, 400


def text(x, y, s, size=12, fill="", weight=400, anchor="start"):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{s}</text>')


def frame(title, desc, body):
    return "\n".join([f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
                      f'role="img" font-family="{FONT}"><title>{title}</title><desc>{desc}</desc>', *body, "</svg>", ""])


def whole(v):
    """Rounded to a whole number, halves up, as on the tool's page."""
    return math.floor(v + 0.5)


def ym(s):
    """'2026-10-31' or '2026-10' as years since year 0, at the middle of the month."""
    return int(s[:4]) + (int(s[5:7]) - 0.5) / 12


def observatory(d, c):
    """The required return of each cryptoasset as a bar of its four terms, with equities and gold below for scale."""
    rows, n_crypto = d["rows"], d["crypto"]
    x0, x1, top = 186, 800, 46
    step = (H - top - 34 - 14) / len(rows)
    hi = math.ceil(max(sum(r["terms"]) for r in rows) / 5) * 5
    X = lambda v: x0 + v / hi * (x1 - x0)
    out, lx = [], 20
    for name, key in (("risk-free rate", "rf"), ("market risk", "violet"), ("concentration risk", "orange"), ("mortality risk", "aqua")):
        out += [f'<rect x="{lx}" y="9" width="14" height="10" rx="2" fill="{c[key]}"/>', text(lx + 20, 19, name, 12.5, c["ink2"])]
        lx += 44 + 7.2 * len(name)
    out.append(text(W - 20, 19, f'percent a year, {d["when"]}', 12.5, c["mut"], anchor="end"))
    bottom = top + len(rows) * step + 14
    for v in range(0, hi + 1, 5):
        out += [f'<line x1="{X(v):.1f}" y1="{top - 6}" x2="{X(v):.1f}" y2="{bottom:.1f}" stroke="{c["line"]}" stroke-width="1"/>',
                text(X(v), bottom + 17, f"{v}%", 11.5, c["mut"], anchor="middle")]
    for i, r in enumerate(rows):
        y = top + i * step + (14 if i >= n_crypto else 0)
        ref, main = i >= n_crypto, i == 0
        if i == n_crypto:
            out.append(f'<line x1="20" y1="{y - 5:.1f}" x2="{W - 20}" y2="{y - 5:.1f}" stroke="{c["axis"]}" stroke-width="1" stroke-dasharray="3 3"/>')
        bh = step - 14
        out.append(text(x0 - 12, y + bh / 2 + 5, r["name"], 15 if main else 13.5, c["ink2"] if ref else c["ink"], 800 if main else 400 if ref else 600, "end"))
        acc = 0
        for v, key in zip(r["terms"], ("rf", "violet", "orange", "aqua")):
            if v > 0.005:
                w = max(0.0, X(acc + v) - X(acc) - 2)
                out.append(f'<rect x="{X(acc):.1f}" y="{y:.1f}" width="{w:.1f}" height="{bh:.1f}" rx="3" fill="{c[key]}"'
                           + (' opacity="0.7"' if ref else "") + "/>")
                if w > 34:
                    out.append(text(X(acc) + w / 2, y + bh / 2 + 4, f"{v:.1f}", 11, c["ink"] if key == "rf" else "#ffffff", anchor="middle"))
                acc += v
        label = (f'<text x="{X(acc) + 8:.1f}" y="{y + bh / 2 + 5:.1f}" font-size="{15 if main else 13.5}" fill="{c["ink"]}">'
                 f'<tspan font-weight="{800 if main else 700}">{r["total"]:.1f}%</tspan>')
        if r.get("band"):
            label += f'<tspan dx="8" font-size="12" fill="{c["mut"]}">band {r["band"][0]:.1f} to {r["band"][1]:.1f}%</tspan>'
        out.append(label + "</text>")
    return frame("Required returns of five cryptoassets, with equities and gold for scale", d["alt"], out)


def monitor(d, c):
    """Total return of a few large covered-call funds, each beside the index fund on the same market."""
    rows = d["bars"]
    top, step = 44, (H - 52) / len(rows)
    x0, x1 = 182, 880
    scale = (x1 - x0) / max(max(r["fund"], r["benchmark"]) for r in rows)
    out = [f'<rect x="20" y="10" width="14" height="10" rx="2" fill="{c["blue"]}"/>',
           text(40, 20, "Covered-call fund, total return with distributions reinvested", 12.5, c["ink2"]),
           f'<rect x="440" y="10" width="14" height="10" rx="2" fill="{c["orange"]}"/>',
           text(460, 20, "Its index fund, total return with distributions reinvested", 12.5, c["ink2"])]
    span = f'{MONTHS[int(d["from"][5:7]) - 1]} {d["from"][:4]} to {MONTHS[int(d["to"][5:7]) - 1]} {d["to"][:4]}'
    for i, r in enumerate(rows):
        y = top + i * step
        if i:
            out.append(f'<line x1="0" y1="{y - 6:.1f}" x2="{W}" y2="{y - 6:.1f}" stroke="{c["line"]}" stroke-width="1"/>')
        out += [text(20, y + 16, r["ticker"], 15, c["ink"], 700), text(20, y + 34, span, 11.5, c["mut"]),
                text(20, y + 50, f'{d["years"]} years', 11.5, c["mut"])]
        for k, (key, colour, name) in enumerate((("fund", "blue", r["ticker"]), ("benchmark", "orange", r["index_fund"]))):
            by, w = y + 6 + k * 30, max(r[key], 0) * scale
            out += [f'<rect x="{x0}" y="{by:.1f}" width="{w:.1f}" height="12" rx="4" fill="{c[colour]}"/>',
                    f'<text x="{x0 + w + 9:.1f}" y="{by + 11:.1f}" font-size="12.5" fill="{c["ink2"]}">'
                    f'<tspan font-weight="700" fill="{c["ink"]}">{r[key]:+.1f}%</tspan> {name}</text>']
    return frame("Covered-call funds beside their index funds", d["alt"], out)


def calculator(d, c):
    """The calculator's worked example: the two present values as bars, then K, the gain and the effective rate."""
    r, i = d["results"], d["inputs"]
    x0, x1 = 250, 800
    scale = (x1 - x0) / max(r["v_fair"], r["v_own"])
    below = (1 - r["v_own"] / r["v_fair"]) * 100
    out = [text(20, 30, f'Benchmark rate {i["c"] * 100:.0f}% a year, {r["horizon"]:.0f} years. '
                        f'The examined forecast is {below:.0f}% below the benchmark forecast in every year.', 14, c["ink2"])]
    for k, (label, key, colour) in enumerate((("Benchmark fair value", "v_fair", "blue"), ("Valuation examined", "v_own", "orange"))):
        y = 66 + k * 54
        out += [text(20, y + 21, label, 15, c["ink"], 600),
                f'<rect x="{x0}" y="{y}" width="{r[key] * scale:.1f}" height="30" rx="5" fill="{c[colour]}"/>',
                text(x0 + r[key] * scale + 12, y + 21, f'{r[key]:.2f}', 15, c["ink"], 700)]
    out.append(f'<line x1="20" y1="196" x2="{W - 20}" y2="196" stroke="{c["line"]}" stroke-width="1"/>')
    tiles = ((f'{r["K"]:.3f}', "Valuation ratio K", "fair value divided by the valuation examined"),
             (f'{r["gain"]:+.3f}', "Gain of capital g", f'per unit invested, over the {r["horizon"]:.0f} years'),
             (f'{r["c_eff_stream"] * 100:.1f}%', "Effective rate", f'the one rate that would hide the gap, against {i["c"] * 100:.0f}%'))
    for k, (big, name, note) in enumerate(tiles):
        x = 20 + k * 340
        out += [text(x, 262, big, 44, c["ink"], 700), text(x, 296, name, 15, c["ink"], 600), text(x, 318, note, 12.5, c["ink2"])]
    out.append(text(20, 372, f"Solved on the yearly amounts. The article's closed form, exact for a single payoff at the horizon, "
                             f'gives {r["c_eff"] * 100:.1f}%. The calculator shows both.', 12.5, c["mut"]))
    return frame("Dual-Risk DCF Calculator: a worked example", d["alt"], out)


DRAW = {"crypto-observatory": observatory, "covered-call-monitor": monitor, "dual-risk-calculator": calculator}


def pictures(live):
    """{file name: SVG text} for every tool in live.json that carries the data of a picture."""
    out = {}
    for repo, draw in DRAW.items():
        d = live.get(repo, {}).get("picture")
        if d:
            for theme, colours in THEMES.items():
                out[f"assets/{repo}-{theme}.svg"] = draw(d, colours)
    return out
