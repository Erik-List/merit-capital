import json,re
G='data/collection/investors/general-catalyst'
F={r['slug']:r for r in json.load(open(f'{G}/scratch/research/valuation-findings.json'))}
c=json.load(open(f'{G}/companies/classification.json'))
def band(u): return '100b_plus' if u>=1e11 else '10b_plus' if u>=1e10 else '1b_plus' if u>=1e9 else 'below_1b'
out=[]
hb=F['hi-bob']; m=re.search(r'https://www\.calcalistech\.com/\S+', hb['notes'] or '')
hb_url=m.group(0).rstrip(').,') if m else None
over={
 'hi-bob':(2450000000,'2022-08',hb_url,'high',"the $150M Series D led by General Atlantic at $2.45B (August 2022), the last company-stated figure; Calcalist reported $2.7B from sources for the September 2023 round"),
 'devoted':(16000000000,'2026-01',F['devoted']['citation'],'medium',"$16B at the January 2026 Series F-Prime, as DistilINFO reports Business Insider; the October 2021 Series D was $12.6B and a $25B round is only in talks"),
}
for s,r in F.items():
    old=(c.get(s) or {}).get('note') or ''
    if s in ('cambridge-mobile-telematics','dandy'):
        out.append({"slug":s,"valuation_usd":None,"valuation_source":None,"valuation_citation":None,"valuation_asof":None,"valuation_range":"below_1b","clear_flags":["needs_web_value"],"note":old+"; A/B pass: no priced figure citable (Rule A); "+(r.get('notes') or '')[:160]})
        continue
    if s=='datavant':
        out.append({"slug":s,"status":"acquired","valuation_usd":None,"valuation_source":None,"valuation_citation":None,"valuation_asof":None,"valuation_range":"below_1b","clear_flags":["needs_web_value"],"note":old+"; A/B pass: merged with Ciox Health under New Mountain Capital's control in 2021 at $7B (Wikipedia), a PE-controlled company since, so acquired (as Veeam and Armis)"})
        continue
    if s in over:
        usd,asof,cite,conf,txt=over[s]
    else:
        usd,asof,cite,conf,txt=r['valuation_usd'],r['asof'],r['citation'],'high',(r.get('event') or '')
        if s in ('awardco','teamworks','amperity','lila-sciences','fireflies-ai','beast-industries','upside'): conf='medium'
    if not cite: print('NO CITE', s); continue
    out.append({"slug":s,"status":"private","valuation_usd":int(usd),"valuation_source":"web_verified","valuation_citation":cite,"valuation_asof":asof,"valuation_range":band(usd),"valuation_confidence":conf,"clear_flags":["needs_web_value"],"note":old.replace(', figure to pin','').replace('; figure to pin','')+f"; A/B pass: ${usd/1e9:.2f}B ({asof}), {txt}"})
open(f'{G}/scratch/queue/ab-pins.out.jsonl','w').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
print(len(out), 'hibob url', hb_url)
