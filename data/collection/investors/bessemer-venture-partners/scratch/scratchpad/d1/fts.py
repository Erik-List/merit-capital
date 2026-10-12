#!/usr/bin/env python3
"""EDGAR full-text search through secget's throttled, cached get(): python3 scratchpad/d1/fts.py '"K2 Optronics"' [start end]"""
import json, sys, urllib.parse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import secget
q = sys.argv[1]
u = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q)
if len(sys.argv) > 3:
    u += f"&dateRange=custom&startdt={sys.argv[2]}&enddt={sys.argv[3]}"
d = json.loads(secget.get(u))
hits = d.get("hits", {}).get("hits", [])
print(q, "->", d.get("hits", {}).get("total", {}).get("value"), "hits")
for h in sorted(hits, key=lambda h: h["_source"].get("file_date", ""))[:int(sys.argv[4]) if len(sys.argv) > 4 else 14]:
    s = h["_source"]
    adsh, fn = h["_id"].split(":")
    cik = (s.get("ciks") or ["0"])[0].lstrip("0")
    print(f"  {s.get('file_date')} {s.get('form'):8} {'; '.join(s.get('display_names') or [])[:70]} | https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}")
