"""Pin the four verified namesakes before any base can inherit their filings."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / 'scripts'))
from paths import Paths, write_atomic
p = Paths('founders-fund')
reasons = {
    '1494301': 'Minnetonka real-estate vehicle, Founders Properties GP and Andrew Deckas, formed 2010. SEC Form D 0001494301-10-000001. Not the San Francisco adviser.',
    '1008311': 'Salt Lake City entity, 421 Wakara Way, filing dated 1997-02-14, before Founders Fund formation in 2005.',
    '1004705': 'Greenville SC entity, NationsBank Plaza, filing dated 2003-07-16, before Founders Fund formation in 2005.',
    '2038138': 'Digital Irish Ventures series, 20 Robinson Drive Middlesex MA, Martin Loughlin, 2024-09-19 filing. Independent adviser.'
}
rows = json.loads(p.entities.read_text())
for row in rows:
    if row['cik'] in reasons:
        row.update(desk='external', confirmed=True, basis=reasons[row['cik']])
        row['sources'].append(f"https://data.sec.gov/submissions/CIK{int(row['cik']):010d}.json")
write_atomic(p.entities, json.dumps(rows, indent=2)+'\n')
print('Pinned four namesake exclusions')
