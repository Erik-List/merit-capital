#!/usr/bin/env python3
"""EDGAR full-text search through the shared SEC throttle (no file saved): fts.py "<phrase>" [start end]"""
import sys, json, subprocess, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[6] / "scripts"))
import shared_throttle
ph = sys.argv[1]
dates = f"dateRange=custom&startdt={sys.argv[2]}&enddt={sys.argv[3]}" if len(sys.argv) > 3 else "dateRange=all"
url = f"https://efts.sec.gov/LATEST/search-index?q={urllib.parse.quote(chr(34)+ph+chr(34))}&{dates}&from=0"
shared_throttle.wait("sec")
r = subprocess.run(["curl", "-s", "-m", "60", "-A", "Merit Capital research erik@meritcapit.al", "-H", "Accept-Encoding: identity", url], capture_output=True)
j = json.loads(r.stdout)
hits = j.get("hits", {})
print("total", hits.get("total"))
for h in hits.get("hits", [])[:25]:
    s = h["_source"]
    adsh = s.get("adsh"); cik = (s.get("ciks") or [""])[0].lstrip("0")
    fn = h["_id"].split(":")[1]
    print(f"  {s.get('file_date')} | {s.get('form')} | {'; '.join(s.get('display_names') or [])[:70]} | https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}")
