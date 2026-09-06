#!/usr/bin/env python3
"""Compact judge view of a queue batch: the queue item's own evidence plus the
site card's exit line, description and sector tags, which the base build does
not carry but which decide `status` and `focus` for most listed rows."""
import json, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
cards = {r["slug"]: r for r in json.loads((D/"sources/site/portfolio-cards.json").read_text())["rows"]}
cardn = {r["name"].lower(): r for r in cards.values()}
jobs  = {r["name"].lower(): r for r in json.loads((D/"sources/site/jobboard.json").read_text())["rows"]}
for n in sys.argv[1:]:
    b = json.loads((D/f"scratch/queue/batch-{int(n):03d}.json").read_text())
    print(f"===== BATCH {int(n):03d}  ({len(b)} rows)")
    for it in b:
        c = cards.get(it["slug"]) or cardn.get((it.get("name") or "").lower()) or {}
        j = jobs.get((it.get("name") or "").lower()) or {}
        bits = [f"[{it['slug']}] {it.get('name')}",
                f"tier={it.get('tier')} ev={it.get('evidence_class')} first={it.get('first_seen')}"]
        if it.get("site_entry_stage"): bits.append(f"SITE_ENTRY={it['site_entry_stage']} @{it.get('site_invest_year')}")
        if c.get("status_line"): bits.append(f"EXIT={c['status_line']}")
        if it.get("wayback_years"): bits.append(f"wb={it['wayback_years']}")
        if it.get("edgar_forms"): bits.append(f"edgar={it['edgar_forms']}")
        if it.get("formd_span"): bits.append(f"formd={it['formd_span']} max={it.get('formd_max_round_usd')}")
        if it.get("partners_site"): bits.append(f"P.site={it['partners_site']}")
        if it.get("partners_formd"): bits.append(f"P.formd={it['partners_formd']}")
        if it.get("issuer_city") or it.get("issuer_state"): bits.append(f"issuer={it.get('issuer_city')},{it.get('issuer_state')}")
        if it.get("year_inc"): bits.append(f"inc={it['year_inc']}")
        if j.get("founded"): bits.append(f"founded={j['founded']}")
        if it.get("former_unicorn"): bits.append("FORMER_UNICORN")
        if it.get("known"): bits.append(f"known={json.dumps(it['known'])}")
        bits.append(f"NEED={','.join(it.get('need') or [])}")
        print("  " + " | ".join(bits))
        d = (c.get("description") or "")[:150]
        tags = ",".join((j.get("sectors") or [])[:6])
        if d or tags: print(f"      {d}{('  «'+tags+'»') if tags else ''}")
