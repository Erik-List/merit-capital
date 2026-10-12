import importlib.util, sys, json
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("gs", HERE.parents[4] / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
for name in argv:
    for svc, base in (("techcrunch","https://techcrunch.com"),("crunchbase_news","https://news.crunchbase.com")):
        r = gs.wordpress(svc, base, name)
        print(f"== {name} [{svc}] {r.get('status')} {r.get('n')}")
        for i in [x for x in (r.get("items") or []) if x.get("names") or name.split()[0].lower() in (x.get("title") or "").lower()][:40]:
            print("  ", i.get('date'), '|', (i.get('title') or '')[:140], '|', i.get('link'))
