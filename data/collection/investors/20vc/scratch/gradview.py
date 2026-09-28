import json, sys, re
g = json.load(open('scratch/graduation-surfaces.json'))
c = json.load(open('companies/classification.json'))
for slug in sys.argv[1:]:
    r = g.get(slug); cr = c.get(slug, {})
    if not r: print('??', slug); continue
    ed = str(cr.get('entry_date') or '')
    print(f"######## {slug} | entry {ed} {cr.get('entry_stage')} | status {cr.get('status')} | {r.get('country')}")
    for s in r.get('siblings', [])[:4]:
        print('   SIB', json.dumps(s)[:300])
    seen = set()
    for sname, sv in (r.get('surfaces') or {}).items():
        if sv.get('status') == 'error' or 'error' in str(sv.get('status', '')):
            print(f'   [{sname}] ERROR')
        for it in sv.get('items', []):
            if not it.get('names'): continue
            if (it.get('date') or '') < ed[:7]: continue
            key = it['title'][:80]
            if key in seen: continue
            seen.add(key)
            if it.get('rounds') or re.search(r'acqui|shut|closes|raises|funding|series|seed|round|bought|merge', it['title'], re.I):
                print(f"   [{sname}] {it.get('date')} {it['title'][:150]} {it.get('rounds')} {it.get('amounts')}")
                if it.get('link'): print(f"        {it['link'][:160]}")
