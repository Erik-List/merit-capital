#!/usr/bin/env python3
"""Compact evidence render for one queue batch: the queue item's needs/known/rounds plus the evidence pack."""
import json, sys
I='/Users/erik/Developer/merit-capital/data/collection/investors/spark-capital/'
pack=json.load(open(I+'scratch/evidence-pack.json'))
for b in sys.argv[1:]:
    items=json.load(open(I+f'scratch/queue/{b}.json'))
    print(f"##### {b}: {len(items)} items")
    for it in items:
        s=it['slug']; e=pack.get(s,{})
        lab=e.get('site_labels') or {}; card=e.get('archive_card') or e.get('live_card') or {}
        print(f"\n## {s} | {it['name']} | need={it['need']} | known={it.get('known')} | tier {it['tier']} | fs {it['first_seen']} | wb {it['wayback_years'][:24]} | ec {it['evidence_class']} | sector {it.get('sector')}")
        if card.get('acquisition_spec') or card.get('description'): print(f"   card: exit={card.get('acquisition_spec')} | {str(card.get('description') or '')[:160]}")
        if lab: print(f"   site labels: stage {lab.get('stage_all')} sectors {lab.get('sectors')} geo {lab.get('geo')} years {lab.get('years')}")
        if it.get('partners_formd') or it.get('rounds'): print(f"   formd: partners={it.get('partners_formd')} span={it.get('formd_span')} rounds={[(r['q'][:6], r['usd']) for r in it.get('rounds',[])][:8]} city={it.get('issuer_city')} state={it.get('issuer_state')} inc={it.get('year_inc')}")
        if e.get('formd_seats'): print(f"   seats: {[(x['q'][:4], x['person'].title(), x['role'], x['issuer'][:30]) for x in e['formd_seats']][:5]}")
        if e.get('news_titles'): print(f"   news: {[n['year']+':'+n['title'][:70] for n in e['news_titles']][:4]}")
        if e.get('wikipedia'): print(f"   wiki: {[x[:170] for w in e['wikipedia'] for x in w['sentences']][:2]}")
        if e.get('edgar_filings'): print(f"   edgar: {e['edgar_filings']}")
        if it.get('former_unicorn'): print(f"   former unicorn: {it['former_unicorn']}")
        if it.get('site_url'): print(f"   site_url: {it['site_url']}")
