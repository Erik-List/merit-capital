#!/usr/bin/env python3
"""Compact Google News checks for the judge: nq.py 'query|regex' ...  -> up to 4 headlines matching regex (case-insensitive),
cached in scratch/nq-cache.json with the Google id so judge_lib.nqurl() can decode a citation."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
C = H / "nq-cache.json"
db = json.loads(C.read_text()) if C.exists() else {}
for a in argv:
    q, _, rx = a.partition("|")
    if q not in db:
        r = gs.googlenews(q, q.split('"')[1] if '"' in q else q)
        if r["status"] != "ok":
            print("FAILED", q); continue
        db[q] = [{"date": i["date"], "source": i["source"], "title": i["title"][:220], "gid": i["gid"]} for i in r["items"]]
        C.write_text(json.dumps(db, indent=1, ensure_ascii=False))
    hits = [i for i in db[q] if re.search(rx or ".", i["title"], re.I)]
    print(f"## {q} [{len(db[q])}/{len(hits)}]")
    for i in sorted(hits, key=lambda i: i["date"])[:4]:
        print(f"   {i['date']} {i['source'][:16]}: {i['title'][:150]}")
