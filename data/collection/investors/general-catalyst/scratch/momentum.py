#!/usr/bin/env python3
"""Momentum slice (COLLECTION.md 6): one press check per private hot-sector row
first seen 2021 on. Google News via scripts/graduation-surfaces.py; writes
scratch/momentum.json {slug: {query, n, items naming the company with amounts}}."""
import importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts/graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); a = sys.argv; sys.argv = a[:1]; spec.loader.exec_module(gs); sys.argv = a
G = ROOT / "data/collection/investors/general-catalyst"
led = json.load(open(G / "companies/membership-ledger.json"))["general-catalyst"]["verdicts"]
c = json.load(open(G / "companies/classification.json")); res = json.load(open(G / "companies/resolved.json"))
b = json.load(open(G / "companies/base.json")); base = {r["slug"]: r for r in (b if isinstance(b, list) else b.get("companies", b.get("rows")))}
F = {"AI & Applied AI", "Fintech & Payments", "Data Infrastructure", "DevTools & APIs"}
out_p = G / "scratch/momentum.json"
out = json.load(open(out_p)) if out_p.exists() else {}
for s, v in led.items():
    if v.get("verdict") != "member" or s not in base or s in out: continue
    rec = {**res.get(s, {}), **{k: x for k, x in (c.get(s) or {}).items() if x is not None}}
    fs = str(base[s].get("first_seen") or base[s].get("site_invest_year") or "")
    y = int(fs[:4]) if fs[:4].isdigit() else 0
    if not (rec.get("status") == "private" and y >= 2021 and rec.get("focus") in F and rec.get("valuation_range") in ("below_1b", None)): continue
    name = gs.clean_name(base[s]["name"]) if hasattr(gs, "clean_name") else base[s]["name"]
    q = f'"{name}" (raises OR raised OR valuation OR "series a" OR "series b" OR "series c" OR acquired OR acquires)'
    r = gs.googlenews(q, name)
    items = [x for x in (r.get("items") or []) if x.get("names")] if r.get("status") == "ok" else []
    out[s] = {"name": name, "query": q, "status": r.get("status"), "n": r.get("n"),
              "items": [{k: x.get(k) for k in ("date", "source", "title", "amounts", "rounds", "gid")} for x in items[-12:]]}
    json.dump(out, open(out_p, "w"), indent=1)
    print(s, r.get("status"), len(items), flush=True)
print("done", len(out))
