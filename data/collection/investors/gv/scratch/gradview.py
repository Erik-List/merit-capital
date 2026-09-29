#!/usr/bin/env python3
"""Graduation view per row for the delta judges (PRO-75): the row's stage and entry as recorded, its Form D sequence,
the Form D layer's verdict, the publisher surfaces' headlines that name the company (scratch/graduation-surfaces.json,
all dates), and what sibling books decided. Usage: gradview.py slug [slug ...]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
q = {i["slug"]: i for i in json.loads((HERE / "queue" / "queue.json").read_text())}
cls = json.loads((INV / "companies" / "classification.json").read_text())
res = json.loads((INV / "companies" / "resolved.json").read_text())
gs = json.loads((HERE / "graduation-surfaces.json").read_text()) if (HERE / "graduation-surfaces.json").exists() else {}
fir = json.loads((INV / "sources" / "edgar" / "formd-issuer-rounds.json").read_text())
for s in sys.argv[1:]:
    i, c, r, g = q.get(s, {}), cls.get(s, {}), res.get(s, {}), gs.get(s, {})
    m = {**r, **c}
    print(f"\n### {s} | {i.get('name')} | need={','.join(i.get('need', []))}")
    print(f"  stage={m.get('entry_stage')} src={m.get('entry_stage_source')} conf={m.get('entry_stage_confidence')} "
          f"cite={m.get('entry_stage_citation')} entry_date={m.get('entry_date')} flags={m.get('flags')}")
    print(f"  status={m.get('status')} band={m.get('valuation_range')} usd={m.get('valuation_usd')} country={m.get('hq_country')} "
          f"S2A now={m.get('seed_to_a_graduation')} site_invest_year={i.get('site_invest_year')!r}")
    print("  note:", (m.get("note") or "")[:1200])
    for rr in (fir.get(s) or {}).get("rounds") or []:
        print(f"  formd: sale {rr.get('sale_date')} filed {rr.get('filing_date')} offering ${rr.get('offering_usd') or 0:,} "
              f"sold ${rr.get('sold_usd') or 0:,} {rr.get('accession')}")
    if i.get("formd_graduation"):
        print("  formd_graduation:", i["formd_graduation"])
    for sb in g.get("siblings") or []:
        print("  sibling:", {k: sb.get(k) for k in ("investor", "name", "seed_to_a_graduation", "graduation_source",
                                                   "graduation_citation", "entry_stage", "entry_stage_citation")})
    for surf, v in (g.get("surfaces") or {}).items():
        its = [x for x in v.get("items", []) if x.get("names")]
        print(f"  [{surf}] status={v.get('status')} query={v.get('query')!r} results={len(v.get('items', []))} naming={len(its)}")
        for x in sorted(its, key=lambda x: x.get("date") or ""):
            print(f"     {x.get('date')} | {x.get('source') or ''} | {x.get('title')[:150]} | {(x.get("link") or "google-news")[:90]}")
