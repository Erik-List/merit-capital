#!/usr/bin/env python3
"""Status news check for the rows outside Europe that read private or unknown (the second half of the same check): one Google News query per company with sale,
insolvency and shutdown words (through scripts/graduation-surfaces.py's googlenews, the same reader nq.py uses), and
the headlines that name the company with one of those words. Writes scratch/status-news-row.json. A headline is a
lead for the judge, never a status by itself."""
import csv, importlib.util, json, re, sys, time
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
EU = {'GB','FR','DE','NL','SE','FI','BE','CH','CZ','DK','ES','IT','IE','NO','PT','AT','PL','EE','LT','LU','RO','HU','GR','IS','LV','SK','BG','HR','SI','MT','CY','TR','UA'}
OUT = H / "status-news-row.json"; out = json.loads(OUT.read_text()) if OUT.exists() else {}
WORDS = re.compile(r"acqui|buy|bought|takeover|taken over|merg|bankrupt|insolv|administrat|liquidat|shut|clos(es|ing|ed) down|wind(s|ing)? down|ceas|faillite|redressement|rachat|rach[eè]te|insolvenz|übernahme|übernimmt|konkurs|faillissement|overname", re.I)
rows = [r for r in csv.DictReader(open(R / "companies/base.csv")) if r["hq_country"] not in EU and r["status"] in ("private", "unknown")]
for r in rows:
    s = r["slug"]
    if s in out: continue
    q = f'"{r["name"]}" (acquired OR acquires OR acquisition OR bankruptcy OR insolvency OR administration OR "shuts down" OR takeover)'
    res = gs.googlenews(q, r["name"])
    if res["status"] != "ok":
        print("FAILED", s); continue
    hits = [{"date": i["date"], "source": i["source"], "title": i["title"][:200], "gid": i["gid"]} for i in res["items"]
            if r["name"].lower() in i["title"].lower() and WORDS.search(i["title"])]
    out[s] = {"name": r["name"], "status": r["status"], "country": r["hq_country"], "query": q, "n": len(res["items"]), "hits": sorted(hits, key=lambda h: h["date"])[-6:]}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    if hits: print(f"{s:22s} {r['hq_country']} {r['status']:8s} | " + " || ".join(f"{h['date']} {h['title'][:95]}" for h in out[s]["hits"][-3:]), flush=True)
print("done", len(out))
