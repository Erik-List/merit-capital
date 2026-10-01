"""Recall probe (COLLECTION.md s3): Google News headlines naming Speedinvest as an
investor, per half-year window 2011-2026 (the 100-item cap of one query would hide
older rounds), in English, German and French. Writes scratch/recall-news.json
{title: {date, gid, q, source}}. Headlines whose company is not in the base are
the recall candidates. Adapted from Project A PRO-102."""
import importlib.util, json, sys
from pathlib import Path
H = Path(__file__).resolve().parent; INV = H.parent; ROOT = INV.parents[3]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
TERMS = [('"Speedinvest" (leads OR led OR "led by" OR backed OR raises OR "seed round" OR "pre-seed" OR "Series A" OR "Series B")', "en-US", "US"),
         ('"Speedinvest" (Finanzierungsrunde OR investiert OR Seed OR Millionen OR Investment)', "de", "AT"),
         ('"Speedinvest" (levée OR lève OR millions OR "seed")', "fr", "FR")]
out_p = H / "recall-news.json"
out = json.loads(out_p.read_text()) if out_p.exists() else {}
done_p = H / "recall-news-done.json"
done = set(json.loads(done_p.read_text())) if done_p.exists() else set()
for y in range(2011, 2027):
    for a, b in ((f"{y}-01-01", f"{y}-07-01"), (f"{y}-07-01", f"{y+1}-01-01")):
        for t, hl, gl in TERMS:
            q = f"{t} after:{a} before:{b}"
            if q in done:
                continue
            r = gs.googlenews(q, "Speedinvest", hl=hl, gl=gl)
            if r.get("status") != "ok":
                print("ERR", q, r.get("status"), flush=True); continue
            for i in r["items"]:
                out.setdefault(i["title"], {"date": (i.get("date") or "")[:10], "gid": i.get("gid"), "q": q,
                                            "source": i.get("source")})
            done.add(q)
            print(a, gl, r["n"], flush=True)
        out_p.write_text(json.dumps(out, indent=1, ensure_ascii=False))
        done_p.write_text(json.dumps(sorted(done)))
print(len(out), "headlines")
