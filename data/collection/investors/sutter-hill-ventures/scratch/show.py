#!/usr/bin/env python3
"""Compact judge view: queue item + evidence pack per slug.
Usage: show.py slug [slug ...] | --batch N"""
import json, re, sys
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
    if i.get("rounds"):
        print("  formd rounds:", [(x.get('date'), x.get('amount') or x.get('total_sold'), x.get('position')) for x in i["rounds"]][:6],
              "| grad:", i.get("formd_graduation"))
    if r.get("partners_formd") or r.get("partners_site"):
        print("  partners: formd", r.get("partners_formd"), "| site", r.get("partners_site"), "| links", (r.get("formd_links") or "")[:150])
    if r.get("edgar_forms"):
        print("  edgar:", r.get("edgar_forms"), r.get("edgar_span"), "| cik", r.get("edgar_cik"))
    if i.get("former_unicorn") or i.get("acquirer") or i.get("formd_band_withheld"):
        print("  unicorn/acq/band:", i.get("former_unicorn"), i.get("acquirer"), i.get("formd_band_withheld"))
    if "archive" in p:
        a = p["archive"]
        print("  archive:", ",".join(a["years"]), "|", a.get("site_sector") or "", "|", ("OUTCOME 1999: " + a["site_outcome"]) if a.get("site_outcome") else "",
              ("MD: " + a["site_md"]) if a.get("site_md") else "")
        if a.get("description"):
            print("      desc:", a["description"][:300])
    for k, v in (p.get("formd_persons") or {}).items():
        print(f"  person {k[:26]:26} {','.join(v['roles'])[:40]:40} {'FIRM ADDR' if v['firm_address'] else ''} {v['streets'][0][:60]}")
    for x in p.get("edgar_fulltext", [])[:2]:
        print("  fts:", x["registrant"], x["forms"], x["first"], (x["snippets"] or [""])[0][:300])
    for x in p.get("wikipedia", [])[:2]:
        print("  wiki:", x["article"], [y[:200] for y in x["sentences"][:2]])
    for h in p.get("press", [])[:5]:
        print("  press:", h)
    for x in p.get("siblings", []):
        print(f"  sib {x['investor']}: {x['status']}/{x['range']}/{x['usd'] or '-'}@{x['asof'] or '-'} stage={x['stage']}({x['stage_src']}) "
              f"{x['city']},{x['country']} {x['focus']} v={x['verdict']}")
