#!/usr/bin/env python3
"""Momentum slice (COLLECTION.md s6): every private row first seen in the last five years in a hot
sector gets one dated web check for a round or mark the judge could not know. Google News through
scripts/graduation-surfaces.py (paced by the shared throttle). Output scratch/momentum.json."""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1]; spec.loader.exec_module(gs)
base = {r["slug"]: r for r in json.load(open(HERE.parent / "companies" / "base.json"))}
cl = json.load(open(HERE.parent / "companies" / "classification.json"))
HOT = {"AI & Applied AI", "Fintech & Payments", "Data Infrastructure", "DevTools & APIs"}
EXTRA = {"cleo", "coro", "stream", "taptap-send", "attio", "photoroom", "lassie", "grand-games", "huspy", "housecall-pro", "zego",
         "vestiaire-collective", "scalable-capital", "writer", "lendable", "geordie-ai", "escape", "exein", "gitguardian", "ory", "sylvera",
         "tibber", "light", "lindus-health", "healx", "testgorilla", "proxima-fusion", "quantum-systems", "the-exploration-company", "kong"}
rows = []
for s, c in cl.items():
    b = base.get(s)
    if not b or c.get("status") != "private":
        continue
    fs = str(b.get("first_seen") or "")[:4]
    if (c.get("focus") in HOT and fs.isdigit() and int(fs) >= 2021) or s in EXTRA:
        rows.append((s, b["name"]))
out = json.loads((HERE / "momentum.json").read_text()) if (HERE / "momentum.json").exists() else {}
KEY = re.compile(r"(?i)unicorn|valuation|valued|\$\d[\d.]*\s?(b|bn|billion)|€\d[\d.]*\s?(bn|billion)|series [b-h]|acqui|raises|secures")
for s, name in sorted(rows):
    if s in out and out[s].get("status") == "ok":
        continue
    q = f'"{name}" startup valuation OR raises OR unicorn OR acquired'
    res = gs.googlenews(q, name)
    if res["status"] != "ok":
        out[s] = {"status": "error", "detail": str(res)[:200]}
        print(s, "ERROR"); continue
    items = [i for i in res["items"] if i["names"] and i["date"] >= "2024-01-01" and KEY.search(i["title"])]
    items.sort(key=lambda i: i["date"], reverse=True)
    out[s] = {"status": "ok", "query": q, "asof": "2026-09-26", "n": res["n"],
              "headlines": [{"date": i["date"], "source": i["source"], "title": i["title"], "gid": i["gid"]} for i in items[:6]]}
    print(f"## {s} ({res['n']} items)")
    for i in items[:4]:
        print(f"   {i['date']} | {i['source'][:22]} | {i['title'][:150]}")
    (HERE / "momentum.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(rows), "rows checked")
