"""PRO-161 profile: the entry-round sizes behind investment_range (COLLECTION.md s11). Ribbit invests worldwide, so
Form D covers few entries; the entry round is the first round each judge recorded with the firm in it (the
classification's funding_rounds, cited), and the Form D entry offering where the entry itself rests on the filing.
Rows whose entry round is undetermined, or whose first firm round carries no amount, are left out."""
import json, statistics
cls = json.load(open('companies/classification.json'))
res = json.load(open('companies/resolved.json'))
led = json.load(open('companies/membership-ledger.json'))
base = json.load(open('companies/base.json'))
verd = (led.get('ribbit-capital') or led).get('verdicts', {})
members = [r['slug'] for r in base if verd.get(r['slug'], {}).get('verdict') == 'member'
           or (r.get('status') == 'auto_confirmed' and r['slug'] not in verd)]
members = [s for s in members if s != 'ibod-company-inc']        # merged into root at the rebuild
out = []
for s in members:
    c, rv = cls.get(s, {}), res.get(s, {})
    stage = c.get('entry_stage') or rv.get('entry_stage')
    if not stage or stage == 'undetermined':
        continue
    rounds = sorted((r for r in c.get('funding_rounds') or [] if r.get('firm_in_round')),
                    key=lambda r: str(r.get('date') or '9999'))
    if rounds and rounds[0].get('amount_usd'):
        out.append({'slug': s, 'stage': stage, 'usd': rounds[0]['amount_usd'], 'date': rounds[0].get('date'),
                    'round': rounds[0].get('round'), 'via': 'judged round', 'source': rounds[0].get('source')})
    elif not rounds and rv.get('entry_stage_source') == 'formd_band' and rv.get('entry_offering_usd') \
            and (not c.get('entry_stage') or c.get('entry_stage') == rv.get('entry_stage')):
        out.append({'slug': s, 'stage': stage, 'usd': rv['entry_offering_usd'], 'date': rv.get('entry_date'),
                    'round': rv.get('entry_stage'), 'via': 'Form D entry offering', 'source': None})
vals = sorted(o['usd'] for o in out)
q = statistics.quantiles(vals, n=20)
summ = {'n': len(vals), 'of_members': len(members), 'median': statistics.median(vals), 'p10': q[1], 'p25': q[4],
        'p75': q[14], 'p90': q[17], 'via': {v: sum(1 for o in out if o['via'] == v) for v in {o['via'] for o in out}},
        'by_stage': {st: statistics.median([o['usd'] for o in out if o['stage'] == st])
                     for st in {o['stage'] for o in out}}}
json.dump({'summary': summ, 'rows': out}, open('scratch/entry-rounds.json', 'w'), indent=1)
print(json.dumps(summ, indent=1))
