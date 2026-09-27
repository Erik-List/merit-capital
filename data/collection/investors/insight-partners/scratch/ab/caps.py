#!/usr/bin/env python3
"""Market caps for the public rows, read off stockanalysis.com quote pages.
Writes scratch/ab/caps.json: slug -> {url, cap_text, currency, value, asof}."""
import json, re, html, subprocess, sys, time
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
T = {
    "1stdibs": "stocks/dibs", "3p-learning-pty": "quote/asx/3PL", "chegg-com": "stocks/chgg",
    "delivery-hero": "quote/etr/DHER", "docusign": "stocks/docu", "equipmentshare": "stocks/eqpt",
    "hellofresh": "quote/etr/HFG", "hinge-health": "stocks/hnge", "hometogo": "quote/etr/HTG",
    "jd-com": "stocks/jd", "jfrog": "stocks/frog", "kyverna-therapeutics": "stocks/kytx",
    "monday-com": "stocks/mndy", "ncino": "stocks/ncno", "newegg": "stocks/negg",
    "nextdoor": "stocks/nxdr", "sentinelone": "stocks/s", "shopify": "stocks/shop",
    "shutterstock-com": "stocks/sstk", "tenable": "stocks/tenb", "trivago": "stocks/trvg",
    "wix-com": "stocks/wix", "yext": "stocks/yext", "hawkeye-360": "stocks/hawk",
    "alibaba-com": "stocks/baba",
}
T.update(dict(a.split("=") for a in sys.argv[1:]))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
out_p = INV / "scratch/ab/caps.json"
out = json.load(open(out_p)) if out_p.exists() else {}
MON = {m: i + 1 for i, m in enumerate("January February March April May June July August September October November December".split())}
for slug, path in T.items():
    url = f"https://stockanalysis.com/{path}/market-cap/"
    r = subprocess.run(["curl", "-sL", "-m", "25", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True, text=True)
    body, _, code = r.stdout.rpartition("\n")
    t = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", body)
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))
    m = re.search(r"has a market cap or net worth of ([^\d\s]{0,4})\s?([\d.,]+) (million|billion|trillion) as of (\w+) (\d+), (\d{4})", t)
    title = re.search(r"^\s*(.{0,80}?) Market Cap", t)
    if not m:
        out[slug] = {"url": url, "http": code, "error": "no cap sentence", "title": title.group(1) if title else None}
        print(slug, code, "NO CAP", (title.group(1) if title else "")[:60])
    else:
        cur, num, unit, mon, day, yr = m.groups()
        val = float(num.replace(",", "")) * {"million": 1e6, "billion": 1e9, "trillion": 1e12}[unit]
        out[slug] = {"url": url, "http": code, "title": title.group(1) if title else None, "currency": cur, "value": val,
                     "asof": f"{yr}-{MON[mon]:02d}-{int(day):02d}", "text": m.group(0)}
        print(slug, code, (title.group(1) if title else "")[:40], "|", m.group(0)[30:])
    time.sleep(1.2)
json.dump(out, open(out_p, "w"), indent=1)
