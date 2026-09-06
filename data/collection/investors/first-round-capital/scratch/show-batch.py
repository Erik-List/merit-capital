#!/usr/bin/env python3
"""Render one queue batch compactly for judging, with the investor's own
per-row evidence merged in (the archived WordPress accordion and the live
Sanity CMS), so the judge sees one line per row instead of 45 JSON blobs."""
import json, sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
n = sys.argv[1]
batch = json.loads((INV / f"scratch/queue/batch-{int(n):03d}.json").read_text())
skip = set(json.loads((INV / "scratch/skip-slugs.json").read_text()))
skipped = [i["slug"] for i in batch if i["slug"] in skip]
batch = [i for i in batch if i["slug"] not in skip]
arch = json.loads((INV / "sources/site/archived-rows.json").read_text())
site = {}
for r in json.loads((INV / "sources/site/companies.json").read_text()):
    rows = r if isinstance(r, dict) else {}
site_rows = json.loads((INV / "sources/site/companies.json").read_text())
if isinstance(site_rows, dict):
    site_rows = site_rows.get("companies") or site_rows.get("rows") or []
for r in site_rows:
    s = (r.get("slug") or "").lower()
    if s:
        site[s] = r

if skipped:
    print(f"# skipped (disappear at the rebuild): {len(skipped)} -> {', '.join(skipped)}")
for i in batch:
    s = i["slug"]
    a = arch.get(s, {})
    ay = a.get("years", {})
    last = ay.get(sorted(ay)[-1]) if ay else {}
    cms = site.get(s, {})
    bits = [f"[{i['tier']}] {s}", f"name={i['name']!r}", f"need={','.join(i['need'])}"]
    if i.get("first_seen"): bits.append(f"first={i['first_seen']}")
    if i.get("wayback_years"): bits.append(f"wb={i['wayback_years']}")
    if i.get("evidence_class"): bits.append(f"ev={i['evidence_class']}")
    if i.get("sector"): bits.append(f"sector={i['sector']}")
    if i.get("partners_site"): bits.append(f"psite={i['partners_site']}")
    if i.get("partners_formd"): bits.append(f"pformd={i['partners_formd']}")
    if i.get("formd_span"): bits.append(f"fdspan={i['formd_span']}")
    if i.get("rounds"):
        bits.append("rounds=" + ",".join(f"{r['q'][:6]}:{(r['usd'] or 0)/1e6:.2f}M" for r in i["rounds"][:7]))
    if i.get("issuer_city"): bits.append(f"city={i['issuer_city']},{i.get('issuer_state','')}")
    if i.get("year_inc"): bits.append(f"inc={i['year_inc']}")
    if i.get("former_unicorn"): bits.append("FORMER_UNICORN")
    if i.get("known"): bits.append(f"known={i['known']}")
    if i.get("edgar_forms"): bits.append(f"edgar={i['edgar_forms']}")
    if i.get("site_url"): bits.append(f"url={i['site_url']}")
    fr = []
    if last.get("stage"): fr.append(f"firmStage={last['stage']}")
    if cms.get("initialPartnership"): fr.append(f"cmsStage={cms['initialPartnership']}")
    if last.get("location"): fr.append(f"firmLoc={last['location']}")
    if cms.get("locations"): fr.append(f"cmsLoc={cms['locations']}")
    if last.get("category"): fr.append(f"firmCat={last['category']}")
    if cms.get("categories"): fr.append(f"cmsCat={cms['categories']}")
    if last.get("status_text"): fr.append(f"firmStatus={last['status_text']}")
    if last.get("desc"): fr.append(f"desc={last['desc'][:110]}")
    elif cms.get("statement"): fr.append(f"desc={str(cms['statement'])[:110]}")
    if last.get("founders") or cms.get("founders"): fr.append(f"founders={last.get('founders') or cms.get('founders')}")
    print(" | ".join(bits))
    if fr:
        print("      " + " | ".join(fr))
