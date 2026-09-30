#!/usr/bin/env python3
"""Market caps of the non-US listings (COLLECTION.md s6: a listing outside SEC registration takes a web-cited market
cap, the local-currency figure converted at the ECB reference rate of its own date via scripts/fx-convert.py). Reads
stockanalysis.com's quote page (its stats block marketCap and the "as of" date), appends to scratch/caps.json with
the original figure, currency, rate and rate date kept for the note.
Usage: python3 caps-nonus.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
BROWSER = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
           "Chrome/128.0 Safari/537.36")
ROWS = {  # slug: (stockanalysis path, currency)
    "semiconductor-manufacturing-international-corporation-smic": ("quote/hkg/0981", "HKD"),
    "sasken-communications": ("quote/nse/SASKEN", "INR"),
    "firstcry": ("quote/nse/FIRSTCRY", "INR"),
    "cathay-industrial-biotech": ("quote/sha/688065", "CNY"),
    "desire2learn": ("quote/tsx/DTOL", "CAD"),
    "didi-chuxing": ("quote/otc/DIDIY", "USD"),
    "hygeia-medical-services-group": ("quote/hkg/6078", "HKD"),
    "lianlian": ("quote/hkg/2598", "HKD"),
    "linekong": ("quote/hkg/8267", "HKD"),
    "yubico": ("quote/sto/YUBICO", "SEK"),
    "boku": ("quote/lon/BOKU", "GBP"),
}
MULT = {"T": 1e12, "B": 1e9, "M": 1e6, "K": 1e3}


def main():
    out_p = HERE / "caps.json"
    out = json.loads(out_p.read_text())
    import datetime
    for slug, (path, ccy) in ROWS.items():
        url = f"https://stockanalysis.com/{path}/market-cap/"
        p = subprocess.run(["curl", "-sL", "-m", "40", "-A", BROWSER, url], capture_output=True).stdout.decode("utf-8", "replace")
        m = re.search(r'stats:\{marketCap:"([\d.]+)([TBMK])"', p)
        d = re.search(r"as of ([A-Z][a-z]+ \d{1,2}, \d{4})", p)
        if not m or not d:
            out[slug] = {"url": url, "status": "unparsed", "currency": ccy}
            print(slug, "UNPARSED")
            continue
        local = float(m.group(1)) * MULT[m.group(2)]
        asof = datetime.datetime.strptime(d.group(1), "%B %d, %Y").strftime("%Y-%m-%d")
        if ccy == "USD":
            usd, note = local, f"USD {local/1e9:.2f}B"
        else:
            r = subprocess.run([sys.executable, str(ROOT / "scripts" / "fx-convert.py"), "--json", str(local), ccy, asof],
                               capture_output=True, text=True)
            j = json.loads(r.stdout)
            usd, note = j.get("usd"), j.get("note") or r.stdout.strip()
        out[slug] = {"ticker": path, "url": url, "usd": usd, "asof": asof, "status": "ok" if usd else "fx_failed",
                     "local": local, "currency": ccy, "fx_note": note}
        print(slug, ccy, local, "->", usd, "|", note)
    out_p.write_text(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
