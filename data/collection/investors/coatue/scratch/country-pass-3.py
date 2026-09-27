#!/usr/bin/env python3
"""Country pass 3 (rule 6): for each non-US $1B+ row, open candidate pages and record the first that names the city."""
import html, json, re, subprocess, time, urllib.parse
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
D = json.load(open(INV / "companies/classification.json")); D = D.get("coatue", D)
W = "https://en.wikipedia.org/wiki/"
T = {"abogenbio": (["Suzhou", "苏州"], [W + "Abogen_Biosciences"]), "alan": (["Paris"], [W + "Alan_(company)"]), "choco": (["Berlin"], []), "cloudwalk": (["São Paulo", "Sao Paulo"], [W + "CloudWalk_(company)"]),
     "dapper-labs": (["Vancouver"], [W + "Dapper_Labs"]), "dayone": (["Singapore"], []), "fiture": (["Chengdu", "成都"], []), "kuaikan-comics": (["Beijing", "北京"], [W + "Kuaikan_Manhua"]),
     "mafengwo": (["Beijing", "北京"], [W + "Mafengwo"]), "mech-mind": (["Beijing"], ["https://stockanalysis.com/quote/hkg/9615/company/"]), "pingpong": (["Hangzhou", "杭州"], [W + "PingPong_(company)"]),
     "pleo": (["Copenhagen"], [W + "Pleo_(company)"]), "rapyd": (["London"], [W + "Rapyd"]), "tamara": (["Riyadh"], [W + "Tamara_(company)"]), "weidan": (["Beijing", "北京"], []), "zuoyebang": (["Beijing", "北京"], [W + "Zuoyebang"]),
     "firmus": (["Sydney", "Launceston", "Singapore"], ["https://www.mingtiandi.com/real-estate/data-centres/aussie-ai-data-centre-startup-firmus-raises-505m-in-coatue-led-equity-round/", "https://www.abc.net.au/news/2025-07-02/firmus-ai-factory-launceston-tasmania/105481780"])}
out = []
for k, (cities, extra) in T.items():
    r = D.get(k, {}); urls = [u for u in [r.get("valuation_citation")] + extra if u]; done = False
    for u in urls:
        p = subprocess.run(["curl", "-sL", "-m", "40", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True)
        body = p.stdout.decode("utf-8", "replace"); code = body.rsplit("\n", 1)[-1]; time.sleep(0.7)
        if code != "200": print(f"{k:16s} HTTP {code} {u}"); continue
        t = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", body, flags=re.S | re.I))); t = re.sub(r"\s+", " ", t)
        for c in cities:
            m = re.search(re.escape(c), t)
            if m:
                ctx = t[max(0, m.start() - 90):m.start() + 60]
                print(f"{k:16s} OK  {c} | {u}\n      ...{ctx}...")
                out.append({"slug": k, "city_found": c, "url": u, "context": ctx}); done = True; break
        if done: break
    if not done: print(f"{k:16s} NOT FOUND")
(INV / "scratch/country-pass-3.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
