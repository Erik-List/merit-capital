import json, re, unicodedata
from pathlib import Path
INV=Path('/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins')
cls=json.load(open(INV/'companies/classification.json')); cls=cls.get('kleiner-perkins',cls)
res=json.load(open(INV/'companies/resolved.json')); res=res.get('kleiner-perkins',res)
base=json.load(open(INV/'companies/base.json'))
led=json.load(open(INV/'companies/membership-ledger.json'))['kleiner-perkins']['verdicts']
dups={d for m in json.load(open(INV/'companies/identity-merges.json'))['kleiner-perkins']['merges'] for d in m['duplicates']}
uni=json.load(open(INV/'../../shared/unicorns/wikipedia.json'))
STOP=('labs','lab','hq','technologies','technology','inc','corp','corporation','ltd','limited','llc','co','the','ai','io','com','group','holdings','systems','software','health','therapeutics','bio','pharmaceuticals','gmbh','sa','plc','ag','networks','network','global','international')
def norm(n):
    n=unicodedata.normalize('NFKD',n or '').encode('ascii','ignore').decode().lower()
    n=re.sub(r"\(.*?\)","",n)
    n=re.sub(r"\.(io|ai|com|co|app|xyz|dev|so|inc)\b","",n)
    n=re.sub(r"[^a-z0-9 ]"," ",n)
    return ' '.join(t for t in n.split() if t not in STOP)
def norm2(n): return norm(n).replace(' ','')
U={}; UN=[]
for kind in ('current','former'):
    for k,v in uni[kind].items():
        for key in {norm2(v['name']), norm2(k)}:
            if key: U.setdefault(key,[]).append((kind,k,v))
        UN.append((norm(v['name']).split(),kind,v))
def names(r):
    out={r['name'], r['slug'].replace('-',' ')}
    for k in ('aliases','former_names','aka','names'):
        v=r.get(k)
        if isinstance(v,str): out|={x.strip() for x in re.split(r'[;|]',v) if x.strip()}
        elif isinstance(v,list): out|={str(x) for x in v}
    m=re.findall(r"\((?:formerly|fka|now)?\s*([^)]+)\)", r['name'])
    out|=set(m)
    return out
hits=set(); loose=set()
for r in base:
    s=r['slug']
    if s in dups or (led.get(s) or {}).get('verdict')!='member': continue
    m={**res.get(s,{}),**cls.get(s,{})}
    row=(m.get('status'),m.get('valuation_range'),m.get('valuation_usd'),m.get('valuation_source'),m.get('valuation_asof'),m.get('focus'),m.get('hq_country'))
    ex=False
    for nm in names(r):
        key=norm2(nm)
        if key and key in U:
            ex=True
            for (kind,k,v) in U[key]:
                hits.add((s,r['name'],kind,v['name'],v.get('valuation_usd') or v.get('last_valuation_usd'),v.get('asof') or v.get('exit_date'),v.get('exit_reason'),v.get('country') or '',v.get('industry') or '')+row)
    if ex: continue
    mt=norm(r['name']).split()
    if not mt: continue
    for ut,kind,v in UN:
        if not ut: continue
        n=min(len(ut),len(mt))
        if ut[:n]==mt[:n] and (len(' '.join(ut[:n]))>=5 or n>=2):
            loose.add((s,r['name'],kind,v['name'],v.get('valuation_usd') or v.get('last_valuation_usd'),v.get('asof') or v.get('exit_date'),v.get('exit_reason'),v.get('country') or '',v.get('industry') or '')+row)
print('EXACT',len(hits))
for h in sorted(hits): print(' | '.join(str(x) for x in h))
print('LOOSE',len(loose))
for h in sorted(loose): print(' | '.join(str(x) for x in h))
