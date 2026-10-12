#!/usr/bin/env python3
"""EDGAR full-text search (2001+) through the shared SEC throttle; prints hits, no disk cache.
Usage: python3 scratchpad/d3/fts.py '"WaterCove"' [startdt enddt]"""
import json, subprocess, sys, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle
UA = "Merit Capital research erik@meritcapit.al"
q = sys.argv[1]
u = "https://efts.sec.gov/LATEST/search-index?q=" + urllib.parse.quote(q)
if len(sys.argv) > 3:
    u += f"&dateRange=custom&startdt={sys.argv[2]}&enddt={sys.argv[3]}"
shared_throttle.wait("sec")
r = subprocess.run(["curl", "-sL", "-m", "60", "-H", f"User-Agent: {UA}", u], capture_output=True, text=True).stdout
try:
    d = json.loads(r)
except Exception:
    print("ERR", r[:300]); sys.exit(1)
hits = d.get("hits", {}).get("hits", [])
print(q, "total", d.get("hits", {}).get("total", {}).get("value"))
hs = sorted(hits, key=lambda h: h["_source"].get("file_date", ""))
n = int(sys.argv[4]) if len(sys.argv) > 4 else 8
seen = set()
sel = []
for h in hs:
    k = (h["_source"].get("display_names") or [""])[0] + h["_source"].get("form", "")
    if k in seen:
        continue
    seen.add(k); sel.append(h)
for h in sel[:n] + (sel[-n:] if len(sel) > 2 * n else sel[n:]):
    s = h["_source"]
    adsh = s.get("adsh", ""); cik = (s.get("ciks") or [""])[0].lstrip("0")
    fn = h["_id"].split(":")[-1]
    print(f"  {s.get('file_date')} | {s.get('form')} | {'; '.join(s.get('display_names') or [])[:70]} | https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}")
