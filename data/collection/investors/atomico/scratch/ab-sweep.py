#!/usr/bin/env python3
"""A/B pass, pass B (COLLECTION.md 7): for every visible row ($1B+ or public),
Google News headlines after the recorded valuation date that name a round,
a valuation, a sale, an IPO or a down round. Reading aid; writes
scratch/ab-sweep.json."""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)

c = json.loads((HERE.parent / "companies" / "classification.json").read_text())
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
EVENT = re.compile(r"(?i)valu|rais|round|series [a-h]\b|acqui|buy|bought|merge|ipo|list|market cap|"
                   r"down round|tender|secondary|shut|layoff|insolv|bankrupt|headquarter|relocat|move")
out = {}
for s, r in sorted(c.items()):
    if s not in base:
        continue
    if not (r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") or r.get("status") == "public"):
        continue
    if argv and s not in argv:
        continue
    asof = str(r.get("valuation_asof") or "2024-01-01")
    after = (asof + "-01-01")[:10] if len(asof) == 4 else (asof + "-01")[:10] if len(asof) == 7 else asof[:10]
    name = base[s]["name"]
    res = gs.googlenews(f'"{name}" after:{after}', name)
    if res["status"] != "ok":
        print("ERR", s, res.get("status"))
        continue
    items = [i for i in res["items"] if i["names"] and EVENT.search(i["title"])]
    out[s] = {"name": name, "after": after, "items": items}
    print(f"== {s} ({name}) after {after}: {len(items)} event headlines")
    for i in items[-12:]:
        print(f"   {i['date']} | {i['source'][:20]:20} | {i['title'][:140]}")
(HERE / "ab-sweep.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
