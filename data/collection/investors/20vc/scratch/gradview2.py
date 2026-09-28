import json, sys, re
g = json.load(open('scratch/graduation-surfaces.json'))
c = json.load(open('companies/classification.json'))
ALIAS = {"agent-sync": "AgentSync", "noh-payments": "Noh", "cryptotax-calculator": "CryptoTaxCalculator|Summ", "lottielabs": "Lottielab", "slay": "Slay|Born", "junction": "Junction", "atlantic-money": "Atlantic Money"}
for slug in sys.argv[1:]:
    r = g.get(slug); cr = c.get(slug, {})
    if not r: print('??', slug); continue
    ed = str(cr.get('entry_date') or '')
    name = ALIAS.get(slug, r.get('name') or slug)
    pat = re.compile(r'(?<![\w-])(' + name + r')(?![\w-])', re.I)
    print(f"######## {slug} | entry {ed} | {cr.get('status')} | {r.get('country')} | surfaces: " + ", ".join(f"{k}:{v.get('status','?')}:{len(v.get('items',[]))}" for k,v in (r.get('surfaces') or {}).items()))
    for s in r.get('siblings', [])[:4]:
        gr = {k: s.get(k) for k in ('investor','seed_to_a_graduation','graduation_citation','entry_stage') if s.get(k)}
        print('   SIB', json.dumps(gr)[:260])
    seen = set(); n = 0
    for sname, sv in (r.get('surfaces') or {}).items():
        for it in sv.get('items', []):
            t = it['title']
            if not pat.search(t): continue
            if (it.get('date') or '') < ed[:7]: continue
            if not re.search(r'series [a-f]|seed|acqui|shut|raises|raised|funding|round|valuation|lands|secures|closes|bags', t, re.I): continue
            k = t[:70]
            if k in seen: continue
            seen.add(k); n += 1
            if n > 8: break
            print(f"   [{sname[:10]}] {it.get('date')} {t[:140]}")
            if it.get('link'): print(f"        {it['link'][:150]}")
