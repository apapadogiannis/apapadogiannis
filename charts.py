"""The two pictures of the live tools on the profile page, drawn as SVG from live.json.

Called by build.py. Standard library only. Each picture is written twice, for a light and a dark page;
the colours are those of the tools' own pages.
"""
import math

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
THEMES = {
    "light": dict(ink="#0b0b0b", ink2="#52514e", mut="#898781", line="#e1e0d9", axis="#c3c2b7",
                  blue="#2a78d6", band="#cde2fb", orange="#eb6834", page="#ffffff"),
    "dark": dict(ink="#f0efec", ink2="#c3c2b7", mut="#898781", line="#2e2e2b", axis="#52514e",
                 blue="#3987e5", band="#173a66", orange="#d95926", page="#0d1117"),
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
    """Bitcoin's required return: the band and its midpoint by month, and each period's required and delivered average."""
    months, periods = d["months"], d["periods"]
    left, right, top, bottom = 62, 918, 64, 378
    x0, x1 = int(months[0]["month_end"][:4]), ym(months[-1]["month_end"])
    lo, hi = math.log(5), math.log(500)
    X = lambda t: left + (t - x0) / (x1 - x0) * (right - left)
    Y = lambda v: bottom - (math.log(min(max(v, 5), 500)) - lo) / (hi - lo) * (bottom - top)
    out = []
    # legend
    lx = 20
    out += [f'<rect x="{lx}" y="9" width="14" height="10" rx="2" fill="{c["band"]}"/>', text(lx + 20, 19, "required band", 12, c["ink2"]),
            f'<line x1="{lx + 118}" y1="14" x2="{lx + 134}" y2="14" stroke="{c["blue"]}" stroke-width="2"/>',
            text(lx + 140, 19, "required, midpoint", 12, c["ink2"]),
            f'<line x1="{lx + 262}" y1="14" x2="{lx + 278}" y2="14" stroke="{c["blue"]}" stroke-width="5" stroke-linecap="round"/>',
            text(lx + 286, 19, "required, average of the period", 12, c["ink2"]),
            f'<circle cx="{lx + 484}" cy="14" r="5" fill="{c["page"]}" stroke="{c["ink"]}" stroke-width="2"/>',
            text(lx + 495, 19, "delivered, average of the period", 12, c["ink2"])]
    # grid
    for v in (5, 10, 20, 50, 100, 200, 400):
        out += [f'<line x1="{left}" y1="{Y(v):.1f}" x2="{right}" y2="{Y(v):.1f}" stroke="{c["line"]}" stroke-width="1"/>',
                text(left - 8, Y(v) + 4, f"{v}%", 11, c["mut"], anchor="end")]
    for year in range(x0, int(x1) + 1, 2):
        out.append(text(X(year), bottom + 16, str(year), 11, c["mut"], anchor="middle" if year > x0 else "start"))
    # band and midpoint
    pts = [(X(ym(m["month_end"])), m) for m in months]
    area = " ".join(f"{x:.1f},{Y(m['upper']):.1f}" for x, m in pts) + " " + \
           " ".join(f"{x:.1f},{Y(m['lower']):.1f}" for x, m in reversed(pts))
    out.append(f'<polygon points="{area}" fill="{c["band"]}"/>')
    out.append(f'<polyline points="{" ".join(f"{x:.1f},{Y(m["midpoint"]):.1f}" for x, m in pts)}" fill="none" '
               f'stroke="{c["blue"]}" stroke-width="1.6" stroke-linejoin="round"/>')
    # periods
    for i, p in enumerate(periods):
        a, b = ym(p["from"]) - 1 / 24, ym(p["to"]) + 1 / 24
        xa, xb, mid = X(a), min(X(b), right), (X(a) + min(X(b), right)) / 2
        if i:
            out.append(f'<line x1="{xa:.1f}" y1="{top - 22}" x2="{xa:.1f}" y2="{bottom}" stroke="{c["axis"]}" '
                       f'stroke-width="1" stroke-dasharray="2 4"/>')
        label = p["period"] + ("" if p["months"] == 36 else f' ({p["months"]} months)')
        out.append(text(mid, top - 16, label, 12, c["ink2"], 600, "middle"))
        yr, yd = Y(p["required_mid"]), Y(p["delivered"])
        out += [f'<line x1="{xa + 6:.1f}" y1="{yr:.1f}" x2="{xb - 6:.1f}" y2="{yr:.1f}" stroke="{c["page"]}" stroke-width="9" stroke-linecap="round"/>',
                f'<line x1="{xa + 6:.1f}" y1="{yr:.1f}" x2="{xb - 6:.1f}" y2="{yr:.1f}" stroke="{c["blue"]}" stroke-width="5" stroke-linecap="round"/>',
                f'<text x="{xb - 10:.1f}" y="{yr + 18:.1f}" font-size="12" font-weight="600" fill="none" text-anchor="end" '
                f'stroke="{c["band"]}" stroke-width="4" stroke-linejoin="round">{whole(p["required_mid"])}%</text>',
                text(xb - 10, yr + 18, f'{whole(p["required_mid"])}%', 12, c["ink"], 600, "end"),
                f'<line x1="{mid:.1f}" y1="{yd + 6:.1f}" x2="{mid:.1f}" y2="{yr - 4:.1f}" stroke="{c["ink"]}" stroke-width="1.2" stroke-dasharray="3 3"/>',
                f'<circle cx="{mid:.1f}" cy="{yd:.1f}" r="6" fill="{c["page"]}" stroke="{c["ink"]}" stroke-width="2"/>',
                text(mid + 11, yd + 4, f'{whole(p["delivered"])}%', 12.5, c["ink"], 700)]
    # now
    m = months[-1]
    xn, r = X(ym(m["month_end"])), m
    out += [f'<circle cx="{xn:.1f}" cy="{Y(r["midpoint"]):.1f}" r="4.5" fill="{c["blue"]}" stroke="{c["page"]}" stroke-width="2"/>',
            f'<line x1="{xn + 14:.1f}" y1="{Y(r["upper"]):.1f}" x2="{xn + 14:.1f}" y2="{Y(r["lower"]):.1f}" stroke="{c["ink2"]}" stroke-width="1.5"/>',
            f'<line x1="{xn + 10:.1f}" y1="{Y(r["upper"]):.1f}" x2="{xn + 18:.1f}" y2="{Y(r["upper"]):.1f}" stroke="{c["ink2"]}" stroke-width="1.5"/>',
            f'<line x1="{xn + 10:.1f}" y1="{Y(r["lower"]):.1f}" x2="{xn + 18:.1f}" y2="{Y(r["lower"]):.1f}" stroke="{c["ink2"]}" stroke-width="1.5"/>',
            text(xn + 24, Y(r["upper"]) - 4, f'{r["upper"]:.1f}%', 11, c["mut"]),
            text(xn + 24, Y(r["midpoint"]) - 6, f'now, {MONTHS[int(m["month_end"][5:7]) - 1]} {m["month_end"][:4]}', 11.5, c["ink2"]),
            text(xn + 24, Y(r["midpoint"]) + 12, f'{r["midpoint"]:.1f}%', 15, c["ink"], 700),
            text(xn + 24, Y(r["lower"]) + 13, f'{r["lower"]:.1f}%', 11, c["mut"])]
    return frame("Bitcoin's required return", d["alt"], out)


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
             (f'{r["c_eff"] * 100:.1f}%', "Effective rate", f'the one rate that would hide the gap, against {i["c"] * 100:.0f}%'))
    for k, (big, name, note) in enumerate(tiles):
        x = 20 + k * 340
        out += [text(x, 262, big, 44, c["ink"], 700), text(x, 296, name, 15, c["ink"], 600), text(x, 318, note, 12.5, c["ink2"])]
    out.append(text(20, 372, f'Solved on the yearly amounts and not in closed form, the effective rate is {r["c_eff_stream"] * 100:.1f}%. '
                             'The calculator shows both.', 12.5, c["mut"]))
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
