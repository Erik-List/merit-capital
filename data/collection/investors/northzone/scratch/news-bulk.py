#!/usr/bin/env python3
"""Bulk Google News lookups for the grind: per company, '"<name>" Northzone' then '"<name>" raises',
headlines kept when they name the company. Output scratch/news-bulk.json (appended; a failed lookup is
recorded as failed and retried on the next run). Usage: news-bulk.py name1 name2 ..."""
import importlib.util, json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
OUT = H / "news-bulk.json"
db = json.loads(OUT.read_text()) if OUT.exists() else {}
for name in argv:
    if db.get(name, {}).get("status") == "ok":
        continue
    rec = {"status": "ok", "items": []}
    for q in (f'"{name}" Northzone', f'"{name}" raises funding'):
        r = gs.googlenews(q, name)
        if r["status"] != "ok":
            rec = {"status": "failed", "error": str(r)[:200]}; break
        for i in r["items"]:
            if i["names"] and all(i["title"] != x["title"] for x in rec["items"]):
                rec["items"].append({"date": i["date"], "source": i["source"], "title": i["title"][:200], "gid": i["gid"],
                                     "rounds": i.get("rounds"), "amounts": i.get("amounts"), "q": q})
    db[name] = rec
    OUT.write_text(json.dumps(db, indent=1, ensure_ascii=False))
    print(name, rec["status"], len(rec.get("items", [])), flush=True)
