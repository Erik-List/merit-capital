#!/usr/bin/env python3
"""Compact judge view for Tiger Global (PRO-167): queue item + evidence pack per slug.
Usage: show.py slug [slug ...] | --batch N"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())} \
    if (HERE / "queue" / "queue.json").exists() else {}
base = {r["slug"]: r for r in json.loads((HERE.parent / "companies" / "base.json").read_text())}
pk = json.loads((HERE / "evidence-pack.json").read_text())
args = sys.argv[1:]
if args and args[0] == "--batch":
    b = json.loads((HERE / "queue" / f"batch-{int(args[1]):03d}.json").read_text())
    args = [i["slug"] for i in (b if isinstance(b, list) else b.get("items", []))]
for s in args:
    i, p, r = q.get(s, {}), pk.get(s, {}), base.get(s, {})
    print(f"\n### {s} | {i.get('name') or r.get('name')} | need={','.join(i.get('need', []))} | fs={i.get('first_seen') or r.get('first_seen')} "
          f"ec={i.get('evidence_class')} tier={r.get('tier')} known={i.get('known')}")
    if r.get("site_url"):
        print("  site: tigerglobal.com/ourstory names it (D4: a position, not proof of a private round)")
    if i.get("rounds"):
        print("  formd rounds:", [(x.get('date'), x.get('amount') or x.get('total_sold'), x.get('position')) for x in i["rounds"]][:6],
              "| grad:", i.get("formd_graduation"))
    if i.get("former_unicorn") or i.get("acquirer") or i.get("formd_band_withheld"):
        print("  unicorn/acq/band:", i.get("former_unicorn"), i.get("acquirer"), i.get("formd_band_withheld"))
    if p.get("recall_basis"):
        print("  RECALL:", p["recall_basis"])
    for k in ("sec", "formd", "press", "wiki", "param"):
        for x in (p.get(k) or []):
            print(f"  {k}: {x}")
    for k in ("edgar", "13f"):
        if p.get(k):
            print(f"  {k}: {p[k]}")
    for x in p.get("sib", []):
        print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) "
              f"{x['city']},{x['country']} {x['focus']} v={x['verdict']}")
