import json,sys
c=json.load(open('companies/classification.json'))
r=json.load(open('companies/resolved.json'))
q=json.load(open('scratch/queue/ab1.json'))[:37]
keys=['status','valuation_range','valuation_usd','valuation_source','valuation_range_source','valuation_citation','valuation_asof','entry_stage','entry_stage_source','entry_stage_citation','entry_date','flags','hq_country','hq_city','focus','funding_rounds','note','seed_to_a_graduation']
for s in q:
    m=dict(r.get(s,{})); m.update(c.get(s,{}))
    print('=====',s, m.get('name',''))
    for k in keys:
        if k in m and m[k] not in (None,[],''):
            v=m[k]
            if k=='funding_rounds': v=json.dumps(v)
            print(f'  {k}: {v}')
