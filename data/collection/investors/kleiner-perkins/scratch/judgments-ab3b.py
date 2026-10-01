#!/usr/bin/env python3
"""A/B pass ab3 (PRO-99), part b: the rest of the float rows re-pinned to the 2026-09-30 cap in scratch/caps.json, and
the rows caps.py could not price (ticker changes, non-US listings, an OTC quote), priced from the stockanalysis pages
fetched into scratchpad/ab3/caps-ab3.json. Only the valuation keys and a one-sentence note."""
import json
import subprocess
from pathlib import Path
import judge_lib as jl

HERE = Path(__file__).resolve().parent
CAPS = json.loads((HERE / "caps.json").read_text())
MINE = json.loads((HERE / "scratchpad/ab3/caps-ab3.json").read_text())
RES = json.loads((jl.INV / "companies/resolved.json").read_text())
RES = RES.get("kleiner-perkins", RES)
ASOF = "2026-09-30"


def band(u):
    return "100b_plus" if u >= 1e11 else "10b_plus" if u >= 1e10 else "1b_plus" if u >= 1e9 else "below_1b"


def money(u):
    return f"${u / 1e12:.2f}T" if u >= 1e12 else f"${u / 1e9:.2f}B" if u >= 1e9 else f"${u / 1e6:.1f}M"


def edge_note(usd):
    for edge, name in ((1e9, "$1B"), (1e10, "$10B"), (1e11, "$100B")):
        if abs(usd - edge) / edge <= 0.05 + 1e-9:
            return f" (within 5% of the {name} band edge)"
    return ""


def cap_line(slug):
    """A row caps.py priced: usd, citation and date from caps.json; the band from the cap."""
    c = CAPS[slug]
    assert c["status"] == "ok" and c["asof"] == ASOF and c["stored_src"] == "sec_public_float", (slug, c)
    usd = int(round(c["usd"]))
    old = RES.get(slug, {})
    was, now = band(c["stored_usd"]), band(usd)
    move = ("band unchanged" if was == now else f"the band moves from {was} to {now}") + edge_note(usd)
    note = (f"A/B pass: market cap {money(usd)} on {c['asof']} (stockanalysis, {c['ticker']}) replaces the SEC public "
            f"float of {money(c['stored_usd'])} dated {old.get('valuation_asof')}; {move}.")
    return jl.cls(slug, rng=now, usd=usd, val_src="web_verified", val_cite=c["url"], asof=c["asof"], note=note)


def page(path, title_has, ccy):
    """One fetched stockanalysis cap page: its title must name the company and its date must be today's."""
    p = MINE[path]
    assert title_has.lower() in p["title"].lower(), (path, p["title"])
    assert p["date"] == "September 30, 2026", (path, p["date"])
    amt = float(p["sentence"].split("market cap or net worth of ")[1].split(" as of ")[0]
                .replace("$", "").replace("billion", "e9").replace("million", "e6").replace(" ", ""))
    assert (p["ccy"] == "$") == (ccy == "USD"), (path, p["ccy"])
    return amt, p["url"]


def us_line(slug, path, title_has, ticker, what):
    """A US-quoted row caps.py had no ticker for (renamed registrant, CIK miss, OTC quote)."""
    usd, url = page(path, title_has, "USD")
    usd = int(round(usd))
    old = RES.get(slug, {})
    now = band(usd)
    if old.get("valuation_source") == "sec_public_float" and old.get("valuation_usd"):
        was = band(old["valuation_usd"])
        move = ("band unchanged" if was == now else f"the band moves from {was} to {now}") + edge_note(usd)
        tail = f" replaces the SEC public float of {money(old['valuation_usd'])} dated {old.get('valuation_asof')}; {move}."
    else:
        tail = f"; {now}."
    note = f"A/B pass: {what}market cap {money(usd)} on {ASOF} (stockanalysis, {ticker}){tail}"
    return jl.cls(slug, rng=now, usd=usd, val_src="web_verified", val_cite=url, asof=ASOF, note=note)


def fx_line(slug, path, title_has, ccy, listing):
    """A non-US listing: the local-currency cap converted at the ECB reference rate of its date (COLLECTION.md s6)."""
    amt, url = page(path, title_has, ccy)
    r = subprocess.run(["python3", "scripts/fx-convert.py", str(int(round(amt))), ccy, ASOF], cwd=jl.ROOT,
                       capture_output=True, text=True)
    out = r.stdout.strip().splitlines()
    assert r.returncode == 0 and len(out) == 2, (slug, r.stdout, r.stderr)
    usd = int(out[0].replace(",", ""))
    note = f"A/B pass: the {listing} market cap is now the row's value (stockanalysis, {ASOF}): {out[1]}; {band(usd)}."
    return jl.cls(slug, rng=band(usd), usd=usd, val_src="web_verified", val_cite=url, asof=ASOF, note=note)


if __name__ == "__main__":
    L = [cap_line(s) for s in ["sagimet-biosciences", "teladoc", "transmedics", "uipath", "upstart",
                               "vera-therapeutics", "veracyte", "zai-lab"]]
    L += [
        us_line("chargepoint", "stocks/chpt", "ChargePoint", "CHPT", ""),
        us_line("flextronics-international", "stocks/flex", "Flex Ltd", "FLEX", "Flextronics is Flex Ltd.; "),
        us_line("groupon", "stocks/grpn", "Groupon", "GRPN", ""),
        us_line("neuropace", "stocks/npce", "NeuroPace", "NPCE", ""),
        us_line("square", "stocks/xyz", "Block", "XYZ", "Square is Block, Inc.; "),
        us_line("symantec", "stocks/gen", "Gen Digital", "GEN", "Symantec is Gen Digital; "),
        us_line("synaptics", "stocks/syna", "Synaptics", "SYNA", ""),
        us_line("neomagic", "quote/otc/NMGC", "NeoMagic", "NMGC",
                "NeoMagic is quoted over the counter, no longer on Nasdaq; "),
        fx_line("arrail-dental", "quote/hkg/6639", "Arrail Group", "HKD", "HKEX (6639)"),
        fx_line("kejingyuan", "quote/she/301372", "Beijing Sys Science", "CNY", "Shenzhen (301372)"),
        fx_line("kindstar-global", "quote/hkg/9960", "Kindstar", "HKD", "HKEX (9960)"),
        fx_line("map-my-india", "quote/nse/MAPMYINDIA", "C. E. Info Systems", "INR", "NSE (MAPMYINDIA)"),
    ]
    # Aleees: TWD is not an ECB reference currency, so the helper cannot convert it; the band is recorded as checked.
    amt, url = page("quote/tpex/5227", "Advanced Lithium Electrochemistry", "TWD")
    assert amt == 2.14e9
    L.append(jl.cls("aleees", extra={"valuation_range_source": "web_verified", "valuation_citation": url,
                                     "valuation_asof": ASOF},
                    note="A/B pass: the Taipei Exchange cap of TWD 2.14B on 2026-09-30 (stockanalysis) is recorded as the "
                         "band's check; TWD is not an ECB reference currency, so no USD figure is stored, and the cap is "
                         "far below $1B at any recent rate."))
    for x in L:
        print(x["slug"], x.get("valuation_range"), x.get("valuation_usd"), "|", x["note"])
    import sys
    jl.write("ab3b", L, record="--dry" not in sys.argv)
