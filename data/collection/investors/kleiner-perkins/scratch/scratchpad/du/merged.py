import json
from pathlib import Path
INV=Path(__file__).resolve().parents[3]
base={r['slug']:r for r in json.load(open(INV/'companies/base.json'))}
ver=json.load(open(INV/'companies/membership-ledger.json'))['kleiner-perkins']['verdicts']
res=json.load(open(INV/'companies/resolved.json')); cl=json.load(open(INV/'companies/classification.json'))
members=sorted(s for s in base if (ver.get(s) or {}).get('verdict')=='member')
def merged(s):
    d=dict(res.get(s) or {}); d.update(cl.get(s) or {}); return d
