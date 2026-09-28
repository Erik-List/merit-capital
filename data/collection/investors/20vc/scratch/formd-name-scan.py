"""Scan the local Form D bulk zips (data/filings/form-d) for issuers whose name
matches a pattern; print accession, quarter, issuer, city/state, offering and
sold amounts, first-sale date. For the S2A absence test's formd: line.
Usage: python3 formd-name-scan.py '<regex>' [--from 2019]"""
import csv, io, re, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
pat = re.compile(sys.argv[1], re.I)
start = int(sys.argv[sys.argv.index('--from') + 1]) if '--from' in sys.argv else 2019
csv.field_size_limit(10**9)
for z in sorted((ROOT / 'data' / 'filings' / 'form-d').glob('*.zip')):
    if int(z.name[:4]) < start: continue
    with zipfile.ZipFile(z) as zf:
        names = {Path(n).name.upper(): n for n in zf.namelist()}
        def rows(fn):
            with zf.open(names[fn]) as fh:
                yield from csv.DictReader(io.TextIOWrapper(fh, 'utf-8', errors='replace'), delimiter='\t')
        hits = {}
        for r in rows('ISSUERS.TSV'):
            if pat.search(r.get('ENTITYNAME', '')):
                hits[r['ACCESSIONNUMBER']] = r
        if not hits: continue
        off = {r['ACCESSIONNUMBER']: r for r in rows('OFFERING.TSV') if r['ACCESSIONNUMBER'] in hits}
        sub = {r['ACCESSIONNUMBER']: r for r in rows('FORMDSUBMISSION.TSV') if r['ACCESSIONNUMBER'] in hits} if 'FORMDSUBMISSION.TSV' in names else {}
        for acc, r in hits.items():
            o = off.get(acc, {}); s = sub.get(acc, {})
            print(z.name[:6], acc, r.get('ENTITYNAME'), r.get('CITY'), r.get('STATEORCOUNTRY'), 'CIK', r.get('CIK'),
                  'offered', o.get('TOTALOFFERINGAMOUNT'), 'sold', o.get('TOTALAMOUNTSOLD'), 'first sale', o.get('SALE_DATE') or o.get('DATEOFFIRSTSALE'), 'filed', s.get('FILING_DATE'))
