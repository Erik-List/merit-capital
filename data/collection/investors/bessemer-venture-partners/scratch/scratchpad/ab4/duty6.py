import json, re, unicodedata
from pathlib import Path
H = Path('.').resolve()
INV = 'bessemer-venture-partners'
uni = json.load(open('../../../shared/unicorns/wikipedia.json'))
base = {r['slug']: r for r in json.loads((H.parent/'companies/base.json').read_text())}
led = json.loads((H.parent/'companies/membership-ledger.json').read_text())
verd = led[INV]['verdicts'] if INV in led else led['verdicts']
cl = json.loads((H.parent/'companies/classification.json').read_text()); cl = cl.get(INV, cl)
rs = json.loads((H.parent/'companies/resolved.json').read_text()); rs = rs.get(INV, rs)

def norm(n):
    n = unicodedata.normalize('NFKD', n or '').encode('ascii', 'ignore').decode().lower()
    n = re.sub(r'\(.*?\)', ' ', n)
    n = re.sub(r'\.(io|ai|com|co|net|org|app|dev|xyz)\b', ' ', n)
    n = re.sub(r'[^a-z0-9 ]+', ' ', n)
    toks = [t for t in n.split() if t not in ('labs','lab','hq','technologies','technology','inc','llc','ltd','limited','corp','corporation','co','the','group','holdings','company','systems','software','io','ai','com','gmbh','sa','ag','plc','pvt','private','global','international','health','financial','bank')]
    return ''.join(toks)

def vv(v):
    return v.get('verdict') if isinstance(v, dict) else v

members = [s for s, v in verd.items() if vv(v) == 'member']
print('members', len(members), 'in base', sum(1 for s in members if s in base))
U = {}
for kind in ('current', 'former'):
    for k, v in uni[kind].items():
        for cand in {norm(v.get('name')), norm(k)}:
            if cand:
                U.setdefault(cand, []).append((kind, k, v))
hits = []
for s in members:
    r = base.get(s)
    if not r: continue
    names = {r.get('name') or '', s.replace('-', ' ')}
    for extra in ('aka', 'fka', 'aliases', 'former_names', 'published_name'):
        x = r.get(extra)
        if isinstance(x, str): names.add(x)
        elif isinstance(x, list): names.update(map(str, x))
    keys = {norm(n) for n in names if n}
    for k in keys:
        if k in U:
            st = {**(rs.get(s) or {}), **(cl.get(s) or {})}
            hits.append((s, r.get('name'), st, U[k]))
            break
print('hits', len(hits))
open_ = []
for s, name, st, us in sorted(hits):
    rng, status = st.get('valuation_range'), st.get('status')
    settled = rng in ('1b_plus','10b_plus','100b_plus') or status in ('acquired','defunct','public')
    if not settled:
        open_.append(s)
    kind, k, v = us[0]
    print(('OPEN ' if not settled else 'ok   ') + f"{s} | {name} | {status}/{rng}/{st.get('valuation_usd')}@{st.get('valuation_asof')} | fs={base[s].get('first_seen')} || {kind}:{v.get('name')} {v.get('valuation_usd') or v.get('last_valuation_usd')} {v.get('asof') or ''} {v.get('exit_date') or ''} {v.get('exit_reason') or ''} {v.get('industry') or ''} {v.get('country') or ''}")
print('OPEN:', open_)
