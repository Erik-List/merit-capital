"""Momentum slice (Erik, 2026-09-04; COLLECTION.md s7): every private row below $1B that the firm first listed in the
last five years gets one mechanical Google News check for a round that would move it over $1B. Headlines naming a
valuation in billions or 'unicorn' are printed for the judge; everything lands in scratch/momentum.json."""
import importlib.util, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
spec = importlib.util.spec_from_file_location("merged", H / "merged.py"); mg = importlib.util.module_from_spec(spec); spec.loader.exec_module(mg)
V = mg.view()
def recent(r):
    fs = str(r["_base"].get("first_seen") or ""); ed = str(r.get("entry_date") or "")
    return (fs[:4].isdigit() and int(fs[:4]) >= 2021) or fs in ("", "?") or (ed[:4].isdigit() and int(ed[:4]) >= 2021)
T = {s: r for s, r in V.items() if r["verdict"] == "member" and r.get("status") == "private" and r.get("valuation_range") == "below_1b" and recent(r)}
OUT = H / "momentum.json"; db = json.loads(OUT.read_text()) if OUT.exists() else {}
for s, r in sorted(T.items()):
    if s in db and db[s]["status"] == "ok": continue
    q = f'"{r["name"]}" (valuation OR unicorn OR "billion") after:2025-06-01'
    x = gs.googlenews(q, r["name"])
    db[s] = {"status": x["status"], "query": q, "items": [{"date": i["date"], "source": i["source"], "title": i["title"][:220], "gid": i["gid"]} for i in x.get("items", [])]}
    OUT.write_text(json.dumps(db, indent=1, ensure_ascii=False))
print(len(T), "rows in the slice;", sum(1 for s in T if db[s]["status"] != "ok"), "failed")
B = re.compile(r"\$\s?\d[\d.]*\s?(b\b|bn|billion)|unicorn|€\s?\d[\d.]*\s?(bn|billion)|£\s?\d[\d.]*\s?(bn|billion)", re.I)
for s in sorted(T):
    nm = T[s]["name"].lower()
    hits = [i for i in db[s]["items"] if nm in i["title"].lower() and B.search(i["title"]) and not re.search(r"tracxn|getlatka|cbinsights|forge|equityzen|hiive", i["title"], re.I)]
    seen = set(); out = []
    for i in sorted(hits, key=lambda i: i["date"], reverse=True):
        if i["title"][:40].lower() in seen: continue
        seen.add(i["title"][:40].lower()); out.append(i)
    if out:
        print("##", s)
        for i in out[:3]: print("    ", i["date"], i["source"][:14], "|", i["title"][:160])
