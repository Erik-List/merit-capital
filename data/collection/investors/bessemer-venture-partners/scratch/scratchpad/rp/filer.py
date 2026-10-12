#!/usr/bin/env python3
"""filer.py <cik>...: fetch (through secget's throttle+cache) the EDGAR filer page and print the filing table compactly."""
import sys, re, importlib.util
from pathlib import Path
H = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("secget", H / "secget.py"); sg = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
try: spec.loader.exec_module(sg)
except SystemExit: pass
for c in argv:
    t = sg.get(f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={c}&type=&dateb=&owner=include&count=40")
    if not t: print(c, "FETCH FAILED"); continue
    t = re.sub(r"\s+", " ", t)
    nm = re.search(r"914-833-9100 (.*?) CIK #", t) or re.search(r"([^»]{0,80}) CIK #", t)
    print("===", c, (nm.group(1).strip()[-70:] if nm else ""))
    i = t.find("Filings Format Description")
    body = t[i:] if i > 0 else t[-3000:]
    for m in re.finditer(r"(\S+(?:/A)?) Documents (.{0,160}?)Acc-no: (\d{10}-\d\d-\d{6}).{0,60}?(\d{4}-\d\d-\d\d)", body):
        print("  ", m.group(4), m.group(1), m.group(3), "|", m.group(2)[:90])
