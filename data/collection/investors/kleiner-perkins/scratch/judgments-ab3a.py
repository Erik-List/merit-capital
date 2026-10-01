#!/usr/bin/env python3
"""A/B pass ab3 (PRO-99), part a: public rows whose stored value is an SEC float, re-pinned to the 2026-09-30 market
cap in scratch/caps.json (stockanalysis, fetched by caps.py). Only the valuation keys and a one-sentence note."""
import json
from pathlib import Path
import judge_lib as jl

HERE = Path(__file__).resolve().parent
CAPS = json.loads((HERE / "caps.json").read_text())
RES = json.loads((jl.INV / "companies/resolved.json").read_text())
RES = RES.get("kleiner-perkins", RES)


def band(u):
    return "100b_plus" if u >= 1e11 else "10b_plus" if u >= 1e10 else "1b_plus" if u >= 1e9 else "below_1b"


def money(u):
    return f"${u / 1e12:.2f}T" if u >= 1e12 else f"${u / 1e9:.2f}B" if u >= 1e9 else f"${u / 1e6:.1f}M"


def cap_line(slug):
    """The cap line for one priced row: usd, source, citation and date from caps.json; the band from the cap."""
    c = CAPS[slug]
    assert c["status"] == "ok" and c["asof"] == "2026-09-30", (slug, c)
    usd = int(round(c["usd"]))
    old = RES.get(slug, {})
    was = band(c["stored_usd"]) if c.get("stored_usd") else old.get("valuation_range")
    now = band(usd)
    move = "band unchanged" if was == now else f"the band moves from {was} to {now}"
    for edge, name in ((1e9, "$1B"), (1e10, "$10B"), (1e11, "$100B")):
        if abs(usd - edge) / edge < 0.05:
            move += f" (within 5% of the {name} band edge)"
    note = (f"A/B pass: market cap {money(usd)} on {c['asof']} (stockanalysis, {c['ticker']}) replaces the SEC public "
            f"float of {money(c['stored_usd'])} dated {old.get('valuation_asof')}; {move}.")
    return jl.cls(slug, rng=now, usd=usd, val_src="web_verified", val_cite=c["url"], asof=c["asof"], note=note)


ROWS = ["aeye", "airbnb", "align-technology", "amazon", "amprius", "atara-biotherapeutics", "beyond-meat",
        "boston-scientific", "caredx", "chegg", "geron-corporation", "inspire-medical-systems", "intuit",
        "lendingclub", "neurocrine-biosciences", "nextdoor", "pacific-biosciences-of-california", "peloton",
        "power-integrations", "progyny", "pulmonx", "quantumscape", "rambus", "rapid-micro-biosystems",
        "rent-the-runway"]

if __name__ == "__main__":
    lines = [cap_line(s) for s in ROWS]
    for x in lines:
        assert CAPS[x["slug"]]["stored_src"] == "sec_public_float", x["slug"]
    jl.write("ab3a", lines)
