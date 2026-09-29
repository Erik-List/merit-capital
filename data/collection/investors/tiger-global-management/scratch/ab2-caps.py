#!/usr/bin/env python3
"""A/B pass slice 2 (PRO-167): market caps for the slice's public rows from stockanalysis.com
(the cap source the landed runs cite, COLLECTION.md 6). Adapted from Coatue's caps.py.
Writes scratch/ab2-caps.json: slug -> {usd_native, currency, asof, url, sentence}; the raw pages
are cached in the session scratchpad (AB2_CACHE) and re-fetched with --fresh.
    python3 ab2-caps.py [slug ...] [--fresh]"""
import html, json, os, re, subprocess, sys, time
from datetime import datetime
from pathlib import Path
HERE = Path(__file__).resolve().parent
D = Path(os.environ.get("AB2_CACHE", "/tmp/ab2-caps"))
D.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
T = {"freshworks-inc": "stocks/frsh", "gitlab": "stocks/gtlb", "grab": "stocks/grab", "groww": "quote/nse/GROWW",
     "hinge-health": "stocks/hnge", "jd-com": "stocks/jd", "kanzhun-boss-zhipin": "stocks/bz",
     "makemytrip-ltd": "stocks/mmyt", "meesho": "quote/nse/MEESHO", "mercado-libre": "stocks/meli",
     "momo": "stocks/momo", "new-oriental-education-technology-group-inc": "stocks/edu", "nextdoor": "stocks/nxdr",
     "nubank": "stocks/nu", "ola-electric": "quote/nse/OLAELEC", "oscar-health": "stocks/oscr",
     "pagaya-technologies-ltd": "stocks/pgy", "palantir": "stocks/pltr", "peloton": "stocks/pton",
     "policybazaar": "quote/nse/POLICYBZR", "procore-technologies-inc": "stocks/pcor",
     "pure-storage-inc": "stocks/p", "roblox": "stocks/rblx"}
UNIT = {"thousand": 1e3, "million": 1e6, "billion": 1e9, "trillion": 1e12}
args = [a for a in sys.argv[1:] if not a.startswith("--")]
fresh = "--fresh" in sys.argv
extra = {}
for a in args:
    if "=" in a:
        s, p = a.split("=", 1)
        extra[s] = p
todo = extra or ({s: T[s] for s in args} if args else T)
P = HERE / "ab2-caps.json"
prev = json.loads(P.read_text()) if P.exists() else {}
for slug, path in todo.items():
    url = f"https://stockanalysis.com/{path}/market-cap/"
    f = D / f"{slug}.html"
    if fresh or not f.exists():
        r = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-o", str(f), "-w", "%{http_code} %{url_effective}", url],
                           capture_output=True, text=True)
        time.sleep(1.0)
        code, _, eff = r.stdout.partition(" ")
        if code != "200":
            print(slug, "HTTP", r.stdout, url)
            f.unlink(missing_ok=True)
            continue
        (D / f"{slug}.url").write_text(eff.strip())
    if (D / f"{slug}.url").exists():
        url = (D / f"{slug}.url").read_text().strip() or url   # the page actually served (a renamed ticker redirects)
    raw = f.read_text(errors="replace")
    t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)))
    t = re.sub(r"\s+", " ", t)
    m = re.search(r"has a market cap or net worth of ([A-Z]{0,3}\$|[^\d\s]{0,3})\s?([\d.,]+) (thousand|million|billion|trillion) as of ([A-Z][a-z]+ \d{1,2}, \d{4})", t)
    cur_m = re.search(r"(?:Currency is|in) (INR|HKD|USD|EUR|CNY|BRL)", t)
    if not m:
        print(slug, "no sentence", url, t[:300])
        continue
    cur, num, unit, d = m.groups()
    native = float(num.replace(",", "")) * UNIT[unit]
    asof = datetime.strptime(d, "%B %d, %Y").date().isoformat()
    prev[slug] = {"usd_native": round(native), "currency": (cur or "").strip() or (cur_m.group(1) if cur_m else "?"),
                  "asof": asof, "url": url, "sentence": m.group(0)}
    print(f"{slug:45s} {cur}{native/1e9:10.2f}B  {asof}  {url}")
P.write_text(json.dumps(prev, indent=1, ensure_ascii=False) + "\n")
