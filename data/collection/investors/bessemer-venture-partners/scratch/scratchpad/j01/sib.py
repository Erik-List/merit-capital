import json, sys
from pathlib import Path
INV = Path(__file__).resolve().parents[4]
S = json.load(open(Path(__file__).resolve().parents[2] / 'siblings.json'))
for slug in sys.argv[1:]:
    for sb in S.get(slug, []):
        inv = sb['investor']
        try:
            c = json.load(open(INV / inv / 'companies' / 'classification.json'))
        except Exception as e:
            print(inv, 'no classification', e); continue
        rows = c if isinstance(c, list) else list(c.values()) if isinstance(c, dict) and all(isinstance(v, dict) for v in c.values()) else c.get('rows', [])
        if isinstance(c, dict) and not rows:
            rows = []
        hit = None
        if isinstance(c, dict):
            for k, v in c.items():
                if isinstance(v, dict) and (v.get('name') == sb['name'] or k == slug):
                    hit = (k, v); break
        else:
            for v in rows:
                if v.get('name') == sb['name'] or v.get('slug') == slug:
                    hit = (v.get('slug'), v); break
        print('==', slug, '|', inv, '|', sb.get('name'), sb.get('status'), sb.get('range'), sb.get('usd'), sb.get('asof'), sb.get('stage'), sb.get('city'), sb.get('country'))
        print('   val_cite:', sb.get('val_cite'))
        if hit:
            v = hit[1]
            for k in ('entry_stage_citation', 'entry_date', 'hq_country_citation', 'graduation_citation', 'note', 'notes'):
                if v.get(k): print('   ', k, ':', str(v[k])[:700])
