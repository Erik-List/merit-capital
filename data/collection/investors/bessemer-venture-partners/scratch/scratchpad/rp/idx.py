#!/usr/bin/env python3
"""idx.py <cik> <accession>...: print the parties on a filing index page (Issuer / Reporting / Subject / Filed by)."""
import sys, re, importlib.util
from pathlib import Path
H = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("secget", H / "secget.py"); sg = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
try: spec.loader.exec_module(sg)
except SystemExit: pass
cik = argv[0]
for acc in argv[1:]:
    u = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{acc}-index.htm"
    t = re.sub(r"\s+", " ", sg.get(u) or "")
    print("==", acc, u)
    for m in re.finditer(r"([A-Za-z0-9&.,'\- /]{2,80}) \((Issuer|Reporting|Subject|Filed by|Filer)\) CIK: (\d+)", t):
        print("   ", m.group(2), "|", m.group(1).strip()[-70:], "|", m.group(3))
    pm = re.search(r"Period of Report (\d{4}-\d\d-\d\d)", t)
    if pm: print("    period", pm.group(1))
