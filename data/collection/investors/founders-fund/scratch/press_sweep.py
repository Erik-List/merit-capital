"""Recall probe, press layer: Google News headlines for '<firm> leads/led' by year window,
minus headlines naming a company already in the base. Writes scratch/recall-press.json."""
import importlib.util, sys, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
H = Path(__file__).resolve().parent
base = json.loads((H.parent / "companies/base.json").read_text())
names = sorted({re.sub(r",? (inc|corp|llc|co)\.?$", "", r["name"], flags=re.I).lower() for r in base if len(r["name"]) > 3}, key=len, reverse=True)
seen, out = set(), []
QS = ['"led by Founders Fund"', '"Founders Fund leads"', '"Founders Fund" leads seed round', '"Founders Fund" leads Series A', '"Founders Fund" leads Series B',
      '"Founders Fund" co-led round', '"backed by Founders Fund" raises'] + [f'"led by Founders Fund" {y}' for y in range(2014, 2027)] + [f'"Founders Fund" leads round {y}' for y in (2022, 2023, 2024, 2025, 2026)]
for q in QS:
    res = gs.googlenews(q, "Founders Fund")
    if res["status"] != "ok": print("ERR", q, res["status"]); continue
    for i in res["items"]:
        t = i["title"]
        if t in seen or "founders fund" not in t.lower(): continue
        seen.add(t)
        tl = t.lower()
        if any(re.search(r"\b" + re.escape(n) + r"\b", tl) for n in names): continue
        out.append({"date": i["date"], "source": i["source"], "title": t, "gid": i["gid"]})
out.sort(key=lambda x: x["date"])
(H / "recall-press.json").write_text(json.dumps(out, indent=1))
print(len(seen), "headlines naming the firm;", len(out), "not naming a base company")
for o in out: print(o["date"], "|", o["title"][:118])
