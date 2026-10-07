#!/usr/bin/env python3
"""Second surface for the status check outside Europe: TechCrunch's own search (its WordPress API, through
scripts/graduation-surfaces.py) for each row that reads private or unknown, keeping posts whose title or excerpt has
the company as the one bought or closed. Writes scratch/status-tc.json. Leads for the judge."""
import csv, importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
EU = {'GB','FR','DE','NL','SE','FI','BE','CH','CZ','DK','ES','IT','IE','NO','PT','AT','PL','EE','LT','LU','RO','HU','GR','IS','LV','SK','BG','HR','SI','MT','CY','TR','UA'}
OUT = H / "status-tc.json"; out = json.loads(OUT.read_text()) if OUT.exists() else {}
rows = [r for r in csv.DictReader(open(R / "companies/base.csv")) if r["hq_country"] not in EU and r["status"] in ("private", "unknown")]
for r in rows:
    s, n = r["slug"], r["name"]
    if s in out: continue
    res = gs.wordpress("techcrunch", "https://techcrunch.com", n)
    if res["status"] != "ok": print("FAILED", s, res.get("http")); continue
    nm = re.escape(n)
    pats = [rf"(acquires?|acquiring|buys|to buy|bought|snaps up|scoops up|takes over|acquisition of|takeover of|acqui-?hires?|to acquire|is acquiring|has acquired)\s+(?:[\w\-\.&']+\s){{0,5}}?{nm}\b",
            rf"\b{nm}\b[^.]{{0,70}}?(acquired by|bought by|to be acquired|sold to|sells (itself )?to|is being acquired|has been acquired|is joining|joins\b|shut(s|ting)? down|to shut|is closing|closing down|files for bankruptcy|bankrupt|winds? down|winding down|ceas(es|ing)|folds)"]
    hits = [{"date": i["date"], "title": i["title"][:160], "link": i["link"], "excerpt": i["excerpt"][:220]} for i in res["items"]
            if any(re.search(p, i["title"] + " . " + i["excerpt"], re.I) for p in pats)]
    out[s] = {"name": n, "status": r["status"], "n": res["n"], "hits": hits[-4:]}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    if hits: print(f"{s:20s} {r['status']:8s} | " + " || ".join(f"{h['date']} {h['title'][:100]}" for h in hits[-3:]), flush=True)
print("done", len(out))
