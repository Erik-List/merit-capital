#!/usr/bin/env python3
"""A/B pass, pass B (COLLECTION.md s7) for the private $1B+ rows (PRO-100 NEA): one Google News query per row for a
newer round, a sale, a listing or a shutdown, kept to headlines dated after the row's mark. Through the machine-wide
googlenews bucket and NEA's two-slot cap (neaslot.py). A failed query is recorded as an error, never as no news.
Output scratch/ab-news.json {slug: {query, status, asof, items_after_mark}}."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

_s = importlib.util.spec_from_file_location("neaslot", str(HERE / "neaslot.py"))
gvslot = importlib.util.module_from_spec(_s); _s.loader.exec_module(gvslot)
INV = HERE.parent
cls = json.loads((INV / "companies/classification.json").read_text())
res = json.loads((INV / "companies/resolved.json").read_text())
cls = cls.get("new-enterprise-associates", cls)
res = res.get("new-enterprise-associates", res)
led = json.loads((INV / "companies/membership-ledger.json").read_text())["new-enterprise-associates"]["verdicts"]
HOT = {"AI & Applied AI", "Fintech & Payments", "Data Infrastructure", "DevTools & APIs"}
base = json.loads((INV / "companies/base.json").read_text())
OUT = HERE / "ab-news.json"
cache = json.loads(OUT.read_text()) if OUT.exists() else {}
todo = []
for r in base:
    m = {**res.get(r["slug"], {}), **cls.get(r["slug"], {})}
    if led.get(r["slug"], {}).get("verdict") != "member":
        continue
    big = m.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")
    momentum = (m.get("focus") in HOT and str(r.get("first_seen") or "0")[:4] >= "2021")
    if m.get("status") == "private" and (big or momentum):
        if (cache.get(r["slug"]) or {}).get("status") != "ok":
            todo.append((r, m))
print(len(todo), "rows to query", flush=True)
for n, (r, m) in enumerate(todo):
    name = gs.clean_name(r["name"])
    q = f'"{name}" (valuation OR raises OR raised OR funding OR acquires OR acquired OR "to acquire" OR IPO OR "goes public" OR "shuts down" OR layoffs)'
    with gvslot.slot():
        out = gs.googlenews(q, name)
    mark = str(m.get("valuation_asof") or "")[:10]
    keep = [{k: it.get(k) for k in ("date", "title", "source", "gid", "names", "rounds", "amounts")}
            for it in out.get("items", []) if it.get("names") and (it.get("date") or "") >= (mark or "2024-09")]
    cache[r["slug"]] = {"query": q, "status": out["status"], "asof": mark, "usd": m.get("valuation_usd"),
                        "slice": "1b_plus" if m.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") else "momentum",
                        "items_after_mark": keep[-30:]}
    if n % 10 == 9:
        write_atomic(OUT, json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
        print(n + 1, "done", flush=True)
write_atomic(OUT, json.dumps(cache, indent=1, ensure_ascii=False) + "\n")
print("errors:", sum(1 for v in cache.values() if v["status"] != "ok"), "of", len(cache))
