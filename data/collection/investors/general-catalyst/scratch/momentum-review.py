import json,re
G='data/collection/investors/general-catalyst'
m=json.load(open(f'{G}/scratch/momentum.json'))
for s,v in m.items():
    its=v.get('items') or []
    big=[x for x in its if re.search(r'billion|\$\s?\d+(\.\d+)?\s?B\b|unicorn|valuation',x.get('title') or '',re.I)]
    rnd=[x for x in its if x.get('amounts') or x.get('rounds')]
    last=sorted(rnd,key=lambda x:x.get('date') or '')[-2:]
    flag='**' if big else '  '
    print(f"{flag}{s} n={v.get('n')} naming={len(its)}")
    for x in (big or last):
        print(f"     {x.get('date')} | {x.get('source')} | {(x.get('title') or '')[:130]}")
