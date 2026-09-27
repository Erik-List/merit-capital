#!/usr/bin/env python3
"""S2A cards for the open Seed rows: entry evidence, the Form D verdict, sibling
decisions and the publisher surfaces (scripts/graduation-surfaces.py output).
Usage: python3 s2a-cards.py [start] [count]"""
import json, sys, re
G='data/collection/investors/general-catalyst'
q=json.load(open(f'{G}/scratch/queue/queue.json'))
c=json.load(open(f'{G}/companies/classification.json'))
res=json.load(open(f'{G}/companies/resolved.json'))
gs=json.load(open(f'{G}/scratch/graduation-surfaces.json'))
posts=json.load(open(f'{G}/scratch/posts-by-company.json'))
m=json.load(open(f'{G}/companies/identity-merges.json'))['general-catalyst']['merges']
dups={d for g in m for d in g['duplicates']}
seed=[it for it in q if it['slug'] not in dups and 'seed_to_a_graduation' in it.get('need',[]) and (c.get(it['slug']) or {}).get('entry_stage')=='Seed' and not (c.get(it['slug']) or {}).get('seed_to_a_graduation')]
a=int(sys.argv[1]) if len(sys.argv)>1 else 0; n=int(sys.argv[2]) if len(sys.argv)>2 else 30
print(f"{len(seed)} open Seed rows")
for it in seed[a:a+n]:
    s=it['slug']; r=c.get(s) or {}
    ps=posts.get(s) or []
    pd=[p.get('date') for p in ps if isinstance(p,dict)][:3]
    print(f"## {s} | {it.get('name')} | status={r.get('status') or (res.get(s) or {}).get('status')} | stage_src={r.get('entry_stage_source')} {('cite='+str(r.get('entry_stage_citation'))[:70]) if r.get('entry_stage_citation') else ''}")
    print(f"   entry: grid={it.get('site_invest_year')} formd_entry={it.get('entry_date')} posts={pd} rounds={[(x['q'],x['usd']) for x in (it.get('rounds') or [])][:5]}")
    fg=it.get('formd_graduation')
    if fg: print(f"   formd: {fg.get('seed_to_a_graduation')} entry ${fg.get('entry_offering_usd')} {fg.get('entry_date')} -> next ${fg.get('next_offering_usd')} {fg.get('next_quarter')}")
    g=gs.get(s) or {}
    for sb in (g.get('siblings') or [])[:4]:
        print(f"   sib: {json.dumps(sb)[:220]}")
    for svc,v in (g.get('surfaces') or {}).items():
        if not isinstance(v,dict): continue
        its=[x for x in (v.get('items') or []) if x.get('names') and (x.get('rounds') or x.get('amounts'))]
        print(f"   {svc}: {v.get('status')} n={v.get('n')} naming+round={len(its)}")
        for x in its[:2]:
            print(f"      {x.get('date')} | {x.get('source','')} | {x.get('title','')[:140]} | {x.get('rounds')} {x.get('amounts')}")
    print(f"   note: {(r.get('note') or '')[:200]}")
