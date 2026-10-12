import json, re, csv, sys, os
from pathlib import Path
HERE = Path('/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch')
INVS = HERE.parent.parent
def load(book):
    c = json.loads((INVS/book/'companies/classification.json').read_text())
    b = {}
    with open(INVS/book/'companies/base.csv', newline='') as f:
        for r in csv.DictReader(f):
            b[r.get('slug')] = r
    return c, b
cache = {}
pairs = []
for line in (HERE/'cross-list.txt').read_text().splitlines():
    m = re.match(r'(.+?): kleiner-perkins:(\S+) .*? vs (\S+?):(\S+) ', line)
    pairs.append((m.group(1), m.group(2), m.group(3), m.group(4)))
if __name__ == '__main__':
    sel = sys.argv[1:]
    KEYS = ['status','valuation_range','valuation_usd','valuation_asof','valuation_source','valuation_citation','hq_city','hq_country','focus','entry_stage','entry_date','flags','note']
    BK = ['name','first_seen','sector','site_url','status','valuation_range','valuation_usd','valuation_asof','valuation_source','valuation_citation','hq_city','hq_country','focus','entry_stage','entry_date','flags','note']
    seen=set()
    for name, ks, book, ss in pairs:
        if sel and ks not in sel: continue
        for bk, sl in (('kleiner-perkins', ks), (book, ss)):
            if (bk,sl) in seen: continue
            seen.add((bk,sl))
            if bk not in cache: cache[bk] = load(bk)
            c, b = cache[bk]
            row = c.get(sl) or {}
            br = b.get(sl) or {}
            inflight = (INVS/bk/'scratch/in-flight.json').exists()
            print(f"\n=== {bk}:{sl}" + ("  IN-FLIGHT" if inflight and bk!='kleiner-perkins' else ""))
            if bk == 'kleiner-perkins':
                print("  base:", {k: br.get(k) for k in ('name','first_seen','sector','site_url') if br.get(k)})
                print("  cls:", json.dumps({k: row.get(k) for k in KEYS if row.get(k) not in (None,'',[])}, ensure_ascii=False)[:1500])
            else:
                print("  row:", json.dumps({k: br.get(k) for k in BK if br.get(k) not in (None,'',[])}, ensure_ascii=False)[:1500])
