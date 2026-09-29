#!/usr/bin/env python3
"""Market caps for TCV's public rows (PRO-169; adapted from ICONIQ's and Coatue's caps.py) from stockanalysis.com (the cap source the
landed runs already cite, COLLECTION.md 6). Writes scratch/caps/caps.json:
slug -> {usd, asof, url, sentence}. Raw pages cached under scratch/caps/."""
import html, json, re, subprocess, sys, time
from datetime import datetime
from pathlib import Path
D = Path(__file__).resolve().parent / "caps"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
T = {'airbnb': 'stocks/abnb', 'alarm-com': 'stocks/alrm', 'ccc-intelligent-solutions': 'stocks/cccs', 'green-dot': 'stocks/gdot', 'groupon': 'stocks/grpn', 'grupa-pracuj': 'quote/wse/GPP', 'nerdy': 'stocks/nrdy', 'netflix': 'stocks/nflx', 'payoneer': 'stocks/payo', 'rapid7': 'stocks/rpd', 'siteminder': 'quote/asx/SDR', 'sportradar': 'stocks/srad', 'zillow': 'stocks/z', 'klook': 'stocks/klk', 'exlservice': 'stocks/exls', 'rent-the-runway': 'stocks/rent', 'oak-pacific-interactive': 'stocks/mtbl', 'techtarget': 'stocks/ttgt'}
# NOTE: quote/wse and quote/asx pages give the cap in PLN / AUD; convert with fx-convert.py.
UNIT = {"thousand":1e3,"million":1e6,"billion":1e9,"trillion":1e12}
out = {}
for slug, path in (T.items() if len(sys.argv) < 2 else [(s, T[s]) for s in sys.argv[1:]]):
    url = f"https://stockanalysis.com/{path}/market-cap/"
    f = D / f"{slug}.html"
    if not f.exists():
        r = subprocess.run(["curl","-sL","-m","40","-A",UA,"-o",str(f),"-w","%{http_code}",url], capture_output=True, text=True)
        time.sleep(1.0)
        if r.stdout != "200":
            print(slug, "HTTP", r.stdout); f.unlink(missing_ok=True); continue
    t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", f.read_text(errors="replace"), flags=re.S)))
    t = re.sub(r"\s+", " ", t)
    m = re.search(r"has a market cap or net worth of ([A-Z]{0,3}\$|[^\d\s]{0,3})\s?([\d.,]+) (thousand|million|billion|trillion) as of ([A-Z][a-z]+ \d{1,2}, \d{4})", t)
    if not m:
        print(slug, "no sentence"); continue
    cur, num, unit, d = m.groups()
    usd = float(num.replace(",", "")) * UNIT[unit]
    asof = datetime.strptime(d, "%B %d, %Y").date().isoformat()
    out[slug] = {"usd": round(usd), "asof": asof, "url": url, "currency": cur, "sentence": m.group(0)}
    print(f"{slug:22s} {cur}{usd/1e9:8.2f}B  {asof}")
prev = {}
p = D / "caps.json"
if p.exists():
    prev = json.load(open(p))
prev.update(out)
json.dump(prev, open(p, "w"), indent=1)
