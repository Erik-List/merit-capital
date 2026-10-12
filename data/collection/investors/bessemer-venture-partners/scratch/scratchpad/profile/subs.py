import sys,json,re
sys.path.insert(0,'.')
import secget
ents=json.load(open('../entities.json'))
pat=re.compile(r'^Bessemer Venture Partners (VI|VII|VIII|IX|X|XI|XII|XIII|Century|India|PR|VS|SG|Co-Inv)|BVP VII SPECIAL|BVP VII E|BVP Forge|BVP FORGE|BVP EUROPE|Bessemer Venture Associates',re.I)
for e in ents:
    if not pat.search(e['name']): continue
    c=e['cik'].zfill(10)
    t=secget.get(f"https://data.sec.gov/submissions/CIK{c}.json")
    t=t[t.index('{'):]
    try: j=json.loads(t)
    except Exception as ex:
        print(e['cik'],e['name'],'PARSEFAIL');continue
    r=j['filings']['recent']
    ds=[(r['filingDate'][i],r['form'][i],r['accessionNumber'][i]) for i in range(len(r['form'])) if r['form'][i].startswith('D')]
    print(e['cik'],e['name'],ds)
