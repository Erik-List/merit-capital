import json, re, unicodedata
from pathlib import Path
H = Path('.').resolve()
INV = 'bessemer-venture-partners'
uni = json.load(open('../../../shared/unicorns/wikipedia.json'))
base = {r['slug']: r for r in json.loads((H.parent/'companies/base.json').read_text())}
led = json.loads((H.parent/'companies/membership-ledger.json').read_text())
verd = led[INV]['verdicts']
cl = json.loads((H.parent/'companies/classification.json').read_text()); cl = cl.get(INV, cl)
rs = json.loads((H.parent/'companies/resolved.json').read_text()); rs = rs.get(INV, rs)
STOP = {'labs','lab','hq','technologies','technology','inc','llc','ltd','limited','corp','corporation','co','the','group','holdings','company','systems','software','io','ai','com','gmbh','sa','ag','plc','pvt','private','global','international','health','financial','bank','and','of','data','cloud','network','networks','security','medical','therapeutics','pharmaceuticals','capital','solutions','services','digital','mobile','games','media','energy','bio','robotics','pay','payments','tech','app','apps','finance','money','analytics','online','interactive','communications','india','us','usa'}
def toks(n):
    n = unicodedata.normalize('NFKD', n or '').encode('ascii', 'ignore').decode().lower()
    n = re.sub(r'\.(io|ai|com|co|net|org|app|dev|xyz)\b', ' ', n)
    n = re.sub(r'[^a-z0-9 ]+', ' ', n)
    return [t for t in n.split()]
def core(n):
    return [t for t in toks(n) if t not in STOP]
vv = lambda v: v.get('verdict') if isinstance(v, dict) else v
members = [s for s, v in verd.items() if vv(v) == 'member' and s in base]
U = []
for kind in ('current', 'former'):
    for k, v in uni[kind].items():
        U.append((kind, k, v, core(v.get('name') or k), toks(v.get('name') or k)))
print(len(U), 'unicorn entries')
exact = set()
seen = set()
for s in sorted(members):
    r = base[s]
    st = {**(rs.get(s) or {}), **(cl.get(s) or {})}
    rng, status = st.get('valuation_range'), st.get('status')
    settled = rng in ('1b_plus','10b_plus','100b_plus') or status in ('acquired','defunct','public')
    names = [r.get('name') or '', s.replace('-', ' ')]
    for f in ('fka','aka','aliases','former_names','listed_as'):
        x = r.get(f)
        if isinstance(x, str) and x: names.append(x)
        elif isinstance(x, list): names += [str(y) for y in x]
    paren = re.findall(r'\(([^)]+)\)', r.get('name') or '')
    names += paren
    names += [re.sub(r'\(.*?\)', '', r.get('name') or '')]
    for n in names:
        c = core(n); j = ''.join(c)
        if not c: continue
        for kind, k, v, uc, ut in U:
            uj = ''.join(uc)
            if not uj: continue
            m = None
            if j == uj: m = 'exact'
            elif len(j) >= 4 and len(uj) >= 4 and (uj.startswith(j) or j.startswith(uj)): m = 'prefix'
            elif c[0] == uc[0] and len(c[0]) >= 4: m = 'first-token'
            elif len(j) >= 5 and (j in uj or uj in j): m = 'substr'
            elif set(c) & set(uc) and any(len(t) >= 5 for t in set(c) & set(uc)): m = 'token'
            if m and (s, k) not in seen:
                seen.add((s, k))
                print(('OPEN ' if not settled else 'ok   ') + f"[{m}] {s} | {r.get('name')} | {status}/{rng}/{st.get('valuation_usd')} fs={r.get('first_seen')} || {kind}:{v.get('name')} {v.get('valuation_usd') or v.get('last_valuation_usd')} {v.get('asof') or v.get('exit_date') or ''} {v.get('exit_reason') or ''} {v.get('industry') or ''} {v.get('country') or ''}".replace('\n', ' '))
