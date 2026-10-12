import json,sys
from pathlib import Path
INV=Path('..').resolve() if Path('../companies').exists() else Path('../..').resolve()
INV=Path('/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins')
C=json.loads((INV/'companies/classification.json').read_text()); C=C.get('kleiner-perkins',C)
R=json.loads((INV/'companies/resolved.json').read_text()); R=R.get('kleiner-perkins',R)
base={r['slug']:r for r in json.loads((INV/'companies/base.json').read_text())}
slugs=sys.argv[1:] or json.load(open(INV/'scratch/queue/ab2.json'))
for s in slugs:
    m={**R.get(s,{}),**C.get(s,{})}
    b=base.get(s,{})
    print(f"### {s} | {b.get('name')} | fs={b.get('first_seen')} web={b.get('website') or b.get('domain')}")
    for k in ('status','valuation_range','valuation_usd','valuation_source','valuation_range_source','valuation_citation','valuation_asof','entry_stage','entry_stage_source','entry_date','focus','hq_country','hq_city','flags','seed_to_a_graduation'):
        if k in m: print(f"   {k}: {m[k]}")
    for r in m.get('funding_rounds') or []:
        print(f"   rnd: {r.get('date')} {r.get('round')} {r.get('amount_usd')} lead={r.get('lead')} kp={r.get('firm_in_round')} {r.get('source')}")
    print(f"   note: {m.get('note')}")
