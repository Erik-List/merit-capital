"""Recall probe (COLLECTION.md s3): Google News headlines naming Project A as an
investor, per year window 2012-2026, so the 100-item cap of one query does not
hide older rounds. Writes scratch/recall-news.json {title: {date, gid, q, source}}.
Headlines whose company is not in the base are the recall candidates."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; INV = H.parent; ROOT = INV.parents[3]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
TERMS = ['"Project A Ventures"', '"Project A" (leads OR led OR "led by" OR backed OR invests OR raises OR "seed round" OR "Series A")',
         '"Project A" (Finanzierungsrunde OR investiert OR Seed OR "Series A" OR Millionen)']
out_p = H / "recall-news.json"
out = json.loads(out_p.read_text()) if out_p.exists() else {}
for y in range(2012, 2027):
    for t in TERMS:
        q = f"{t} after:{y}-01-01 before:{y+1}-01-01"
        r = gs.googlenews(q, "Project A")
        if r.get("status") != "ok":
            print("ERR", q, r.get("status")); continue
        for i in r["items"]:
            out.setdefault(i["title"], {"date": (i.get("date") or "")[:10], "gid": i.get("gid"), "q": q,
                                        "source": i.get("source"), "names": i.get("names")})
        print(y, t[:30], r["n"], flush=True)
    out_p.write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "headlines")
