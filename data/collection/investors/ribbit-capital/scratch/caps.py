#!/usr/bin/env python3
"""Market caps for the public members (A/B pass, COLLECTION.md s6 public rows):
StockAnalysis's market-cap page, read by curl, the sentence 'has a market cap or
net worth of $X billion as of <date>'. Writes scratch/caps.json
{slug: {ticker, usd, currency, asof, url, sentence}}; a non-USD listing keeps its
native figure for fx-convert. A page that does not carry the sentence is recorded
as failed, never as a value.

Usage: python3 scratch/caps.py slug=path [slug=path ...]
   path is StockAnalysis's path after the host, e.g. robinhood=stocks/hood
"""
import html
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "caps.json"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
MULT = {"thousand": 1e3, "million": 1e6, "billion": 1e9, "trillion": 1e12}


def main() -> None:
    caps = json.loads(OUT.read_text()) if OUT.exists() else {}
    for arg in sys.argv[1:]:
        slug, path = arg.split("=", 1)
        url = f"https://stockanalysis.com/{path.strip('/')}/market-cap/"
        raw = subprocess.run(["curl", "-sL", "--max-time", "40", "-A", UA, url],
                             capture_output=True).stdout.decode("utf-8", "replace")
        text = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S))
        text = re.sub(r"\s+", " ", html.unescape(text))
        m = re.search(r"has a market cap or net worth of ([A-Z]{0,3}\$|[A-Z]{3} |[^\d\s]{1,3})?\s?([\d.,]+) "
                      r"(thousand|million|billion|trillion) as of ([A-Z][a-z]+ \d{1,2}, \d{4})", text)
        if not m:
            caps[slug] = {"url": url, "status": "failed"}
            print(f"{slug}: FAILED ({url})")
            continue
        cur = (m.group(1) or "$").strip()
        val = float(m.group(2).replace(",", "")) * MULT[m.group(3)]
        asof = datetime.strptime(m.group(4), "%B %d, %Y").date().isoformat()
        caps[slug] = {"url": url, "status": "ok", "native": val, "currency_mark": cur, "asof": asof,
                      "sentence": m.group(0)}
        print(f"{slug}: {cur} {val:,.0f} as of {asof}")
    OUT.write_text(json.dumps(caps, indent=1) + "\n")


if __name__ == "__main__":
    main()
