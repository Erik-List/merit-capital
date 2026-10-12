#!/usr/bin/env python3
"""List a company's EDGAR filings of one type through the shared SEC throttle: edgar_list.py <company name or CIK> [type]"""
import re, subprocess, sys, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle
UA = "Merit Capital research erik@meritcapit.al"
def get(url):
    shared_throttle.wait("sec")
    r = subprocess.run(["curl", "-sL", "-m", "60", "-H", f"User-Agent: {UA}", url], capture_output=True)
    return r.stdout.decode("utf-8", "replace")
q, typ = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "S-1")
key = "CIK" if q.isdigit() else "company"
t = get(f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&{key}={urllib.parse.quote(q)}&type={urllib.parse.quote(typ)}&dateb=&owner=include&count=40&output=atom")
names = re.findall(r"<conformed-name>(.*?)</conformed-name>|<title>(.*?)</title>", t)
print("names/titles:", [a or b for a, b in names][:6])
for e in re.findall(r"<entry>(.*?)</entry>", t, re.S)[:25]:
    d = re.search(r"<filing-date>(.*?)</filing-date>", e); ty = re.search(r"<filing-type>(.*?)</filing-type>", e)
    h = re.search(r"<filing-href>(.*?)</filing-href>", e); c = re.search(r"<cik>(.*?)</cik>|<name>(.*?)</name>", e)
    print("  ", d and d.group(1), ty and ty.group(1), h and h.group(1), c and (c.group(1) or c.group(2)))
if len(sys.argv) > 3:
    idx = get(sys.argv[3])
    for m in re.findall(r'href="(/Archives/edgar/data/[^"]+)"', idx):
        print("   doc:", "https://www.sec.gov" + m)
