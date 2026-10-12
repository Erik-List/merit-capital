import json, re
from pathlib import Path
H = Path('.').resolve()
slugs = json.loads((H/'queue/ab-momentum.json').read_text())
base = {r['slug']: r for r in json.loads((H.parent/'companies/base.json').read_text())}
cl = json.loads((H.parent/'companies/classification.json').read_text()); cl = cl.get('bessemer-venture-partners', cl)
rs = json.loads((H.parent/'companies/resolved.json').read_text()); rs = rs.get('bessemer-venture-partners', rs)
pat = re.compile(r'(?i)(momentum check|checked)\s*(on\s*)?\(?(20\d\d-\d\d-\d\d)')
pat2 = re.compile(r'(?i)(momentum|\$1B|1B or more|unicorn)')
n=0
for s in slugs:
    st = {**(rs.get(s) or {}), **(cl.get(s) or {})}
    note = str(st.get('note') or '')
    m = pat.search(note)
    tail = ''
    i = note.lower().find('momentum')
    if i < 0: i = note.lower().find('checked 20')
    tail = note[i:i+230] if i >= 0 else '-- NO CHECK IN NOTE --'
    print(f"{s} | {base.get(s,{}).get('name')} | fs={base.get(s,{}).get('first_seen')} | {st.get('status')}/{st.get('valuation_range')}/{st.get('valuation_usd')} | {st.get('focus')} | vrs={st.get('valuation_range_source')}\n     {tail}")
