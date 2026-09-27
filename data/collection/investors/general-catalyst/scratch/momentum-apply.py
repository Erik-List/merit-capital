import json,re,importlib.util,sys
spec=importlib.util.spec_from_file_location('gs','scripts/graduation-surfaces.py'); gs=importlib.util.module_from_spec(spec); sys.argv=sys.argv[:1]; spec.loader.exec_module(gs)
G='data/collection/investors/general-catalyst'
m=json.load(open(f'{G}/scratch/momentum.json'))
c=json.load(open(f'{G}/companies/classification.json'))
pins={
 'serval':(1000000000,'2025-12','https://www.reuters.com/technology/ai-startup-serval-valued-1-billion-after-sequoia-led-round-expand-it-automation-2025-12-11/','high',"'AI startup Serval valued at $1 billion after Sequoia-led round' (Reuters, December 2025)"),
 'rox':(1200000000,'2026-03','https://techcrunch.com/2026/03/12/sales-automation-startup-rox-ai-hits-1-2b-valuation-sources-say/','medium',"'Sales automation startup Rox AI hits $1.2B valuation, sources say' (TechCrunch, March 2026)"),
 'thatch':(1000000000,'2026-09','https://www.prnewswire.com/news-releases/thatch-raises-108m-at-1b-valuation-as-employers-shift-away-from-traditional-health-plans-302879015.html','high',"'Thatch Raises $108M at $1B Valuation' (PR Newswire, 15 September 2026)"),
}
VERB=re.compile(r'\b(raises|raised|secures|lands|bags|closes|announces|nabs|snags|gets|emerges|launches with|valued|hits|acquires|acquired|buys)\b',re.I)
out=[]
for s,v in m.items():
    old=(c.get(s) or {}).get('note') or ''
    if s in pins:
        usd,asof,url,conf,txt=pins[s]
        out.append({"slug":s,"valuation_usd":usd,"valuation_source":"web_verified","valuation_citation":url,"valuation_asof":asof,"valuation_range":"1b_plus","valuation_confidence":conf,"valuation_range_source":"web_verified","note":old+"; momentum check 2026-09-27: "+txt})
        continue
    name=v['name']
    hits=[x for x in (v.get('items') or []) if re.search(r'\b'+re.escape(name)+r'\b',x.get('title') or '',re.I) and VERB.search(x.get('title') or '') and (x.get('amounts') or x.get('rounds'))]
    hits.sort(key=lambda x:x.get('date') or '')
    if hits:
        x=hits[-1]; url=gs.decode(x['gid']) if x.get('gid') else None
        if url:
            out.append({"slug":s,"valuation_range_source":"web_verified","valuation_citation":url,"valuation_asof":(x.get('date') or '')[:7],"note":old+f"; momentum check 2026-09-27: the latest round in the press is '{(x.get('title') or '')[:110]}' ({x.get('date')}), below $1B"})
            continue
    out.append({"slug":s,"note":old+"; momentum check 2026-09-27: Google News finds no round naming the company"})
open(f'{G}/scratch/queue/momentum.out.jsonl','w').write(''.join(json.dumps(o,ensure_ascii=False)+'\n' for o in out))
print(len(out), sum(1 for o in out if o.get('valuation_citation')))
