import importlib.util, sys, json, re
from pathlib import Path
ROOT=Path('/Users/erik/Developer/merit-capital')
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
for q in argv:
    r=gs.wordpress("techcrunch","https://techcrunch.com",q)
    print('##',q,r.get('status'),r.get('n'))
    for i in sorted(r.get('items',[]),key=lambda i:i.get('date') or '')[:8]:
        print('   ',(i.get('date') or '')[:10],'|',i.get('title','')[:100],'|',i.get('link'))
