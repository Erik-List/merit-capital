"""Entry-round sizes from the judged notes (the firm's own announcements and press),
converted to USD at the ECB rate of the entry date: the investment_range median (§11,
Creandum precedent: Form D covers only 15 issuers here)."""
import json, re, sys, statistics, importlib.util
spec = importlib.util.spec_from_file_location("fxc", "/Users/erik/Developer/merit-capital/scripts/fx-convert.py")
fxc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fxc)
c = json.load(open('companies/classification.json'))
AM = re.compile(r"(EUR|USD|US\$|\$|€|GBP|£|SEK|DKK|NOK|CHF)\s?([\d.,]+)\s?(m\b|M\b|million|mn\b|bn\b|billion|B\b)|([\d.,]+)\s?(million|m)\s(euros?|EUR|USD|dollars)")
ROUND = re.compile(r"seed|series|round|pre-seed|funding|investment|raise|note|extension|financing|entry", re.I)
SKIP = set(sys.argv[1].split(',')) if len(sys.argv) > 1 else set()
out = []
for s, r in sorted(c.items()):
    note = r.get('note', '')
    pick = None
    for m in AM.finditer(note):
        after = note[m.end():m.end()+60]; before = note[max(0, m.start()-25):m.start()]
        if re.search(r"\bat\s*(a\s*)?(reported\s*)?(about\s*)?(~)?$", before): continue
        if re.search(r"valuation|mark\b", after[:15], re.I): continue
        if not ROUND.search(after) and not ROUND.search(before): continue
        pick = m; break
    if not pick or s in SKIP:
        out.append((s, None, None, '')); continue
    if pick.group(1):
        ccy = {'$': 'USD', 'US$': 'USD', '€': 'EUR', '£': 'GBP'}.get(pick.group(1), pick.group(1))
        num = float(pick.group(2).replace(',', '')); unit = pick.group(3)
    else:
        ccy = 'EUR' if pick.group(6).lower().startswith('euro') or pick.group(6) == 'EUR' else 'USD'
        num = float(pick.group(4).replace(',', '')); unit = 'm'
    mult = 1e9 if unit.lower() in ('bn', 'billion', 'b') else 1e6
    d = r.get('entry_date') or ''
    d = (d + '-06-30' if len(d) == 4 else d + '-15' if len(d) == 7 else d) or '2020-06-30'
    usd = num*mult if ccy == 'USD' else fxc.to_usd(num*mult, ccy, d)[0]
    out.append((s, usd, f"{ccy} {num:g}{'B' if mult == 1e9 else 'M'}", note[max(0, pick.start()-40):pick.end()+40]))
for s, u, a, ctx in out:
    print(s[:24].ljust(24), (f"{u/1e6:8.1f}M" if u else '       -'), (a or '').ljust(12), ctx.replace('\n', ' '))
vals = sorted(u for s, u, a, ctx in out if u)
q = statistics.quantiles(vals, n=20)
print(len(vals), 'median', round(statistics.median(vals)/1e6, 2), 'p25', round(q[4]/1e6, 2), 'p75', round(q[14]/1e6, 2), 'p10', round(q[1]/1e6, 2), 'p90', round(q[17]/1e6, 2))
json.dump([{'slug': s, 'usd': u, 'amount': a, 'context': ctx} for s, u, a, ctx in out], open('scratch/entry-rounds.json', 'w'), indent=1, ensure_ascii=False)
