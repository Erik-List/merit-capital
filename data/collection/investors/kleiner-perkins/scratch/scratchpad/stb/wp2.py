import importlib.util, sys, json, re
from pathlib import Path
ROOT=Path('/Users/erik/Developer/merit-capital')
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
for a in argv:
    q,_,key=a.partition('::'); key=key or q.split()[0]
    for svc,base in (("techcrunch","https://techcrunch.com"),("crunchbase_news","https://news.crunchbase.com")):
        r=gs.wordpress(svc,base,q)
        its=[i for i in r.get('items',[]) if key.lower() in (i.get('title','')+' '+(i.get('excerpt') or '')).lower()]
        print('##',q,svc,r.get('status'),r.get('n'),len(its))
        for i in sorted(its,key=lambda i:i.get('date') or '')[:10]:
            print('   ',(i.get('date') or '')[:10],'|',i.get('title','')[:100],'|',i.get('link'))
