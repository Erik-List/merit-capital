"""Recall probe, press leg (COLLECTION.md s3): Google News for the firm's name with round words, one query per quarter,
to catch deals the firm's list does not carry yet. Headlines are kept with their Google id (decoded on demand);
company names are NOT extracted here: the judge reads the unmatched headlines (scratch/press-sweep.json)."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
OUT = H / "press-sweep.json"
db = json.loads(OUT.read_text()) if OUT.exists() else {}
Q = [(f"{y}-{m:02d}-01", f"{y + (m + 3 > 12)}-{(m + 3 - 1) % 12 + 1:02d}-01") for y in range(int(argv[0]), int(argv[1]) + 1) for m in (1, 4, 7, 10)]
for a, b in Q:
    for words in ('(led OR leads OR "co-led" OR "led by")', '(raises OR raised OR backs OR invests OR seed OR "series a" OR "series b")'):
        q = f'"Index Ventures" {words} after:{a} before:{b}'
        if q in db and db[q].get("status") == "ok": continue
        r = gs.googlenews(q, "Index Ventures")
        db[q] = {"status": r["status"], "n": len(r.get("items", [])), "items": [{"date": i["date"], "source": i["source"], "title": i["title"][:240], "gid": i["gid"]} for i in r.get("items", [])]}
        OUT.write_text(json.dumps(db, indent=1, ensure_ascii=False))
        print(a, words[:12], db[q]["status"], db[q]["n"], flush=True)
