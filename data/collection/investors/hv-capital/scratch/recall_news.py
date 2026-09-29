"""Recall probe: Google News sweeps naming the firm as investor; companies not in the base."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; INV = H.parent; ROOT = INV.parents[3]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
base = json.loads((INV / "companies/base.json").read_text())
def k(s): return re.sub(r"[^a-z0-9]", "", s.lower())
known = {k(r["name"]) for r in base} | {k(r["slug"]) for r in base}
QUERIES = ['"HV Capital" leads', '"HV Capital" led round', '"led by HV Capital"', '"HV Capital" seed round',
           '"HV Capital" Series A', '"HV Capital" Series B', '"HV Holtzbrinck" leads', '"led by HV Holtzbrinck"',
           '"HV Holtzbrinck Ventures" investiert', '"Holtzbrinck Ventures" investiert', '"Holtzbrinck Ventures" invests',
           '"HV Capital" investiert', '"HV Capital" Finanzierungsrunde', '"HV Holtzbrinck" Finanzierungsrunde',
           '"Holtzbrinck Ventures" Finanzierungsrunde', '"HV Capital" funding round participation']
out = {}
for q in QUERIES:
    r = gs.googlenews(q, "HV")
    if r.get("status") != "ok":
        print("ERR", q); continue
    for i in r["items"]:
        out.setdefault(i["title"], {"date": i.get("date", "")[:10], "gid": i.get("gid"), "q": q, "source": i.get("source")})
    print(q, r["n"])
(H / "recall-news.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "headlines")
