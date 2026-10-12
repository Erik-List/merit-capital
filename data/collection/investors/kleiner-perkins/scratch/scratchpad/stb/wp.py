import importlib.util, sys, json
from pathlib import Path
ROOT=Path('/Users/erik/Developer/merit-capital')
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
for name in argv:
    for svc,base in (("techcrunch","https://techcrunch.com"),("crunchbase_news","https://news.crunchbase.com")):
        r=gs.wordpress(svc,base,name)
        print('##',name,svc,r.get('status'),r.get('n'))
        for i in sorted(r.get('items',[]),key=lambda i:i.get('date') or '')[:14]:
            print('   ',(i.get('date') or '')[:10],'|',i.get('title','')[:110],'|',i.get('link'))
