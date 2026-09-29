#!/usr/bin/env python3
"""Fetch one EDGAR full-text hit and print the sentences naming a company (PRO-169 legacy rows).
Usage: efts-read.py <slug> <hit-index> [needle]"""
import json, re, subprocess, sys, html
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
d = json.load(open(INV / "scratch/legacy-efts.json"))
slug, k = sys.argv[1], int(sys.argv[2])
v = d[slug]; needle = sys.argv[3] if len(sys.argv) > 3 else v["name"]
disp, form, date, _id = v["hits"][k]
adsh, fn = _id.split(":")
m = re.search(r"CIK (\d+)", disp)
cik = int(m.group(1)) if m else int(adsh.split("-")[0])
url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-','')}/{fn}"
r = subprocess.run(["curl", "-s", "-A", "merit-capital research erik@meritcapit.al", url], capture_output=True, text=True)
t = html.unescape(re.sub(r"<[^>]+>", " ", r.stdout)); t = re.sub(r"\s+", " ", t)
print(url, form, date)
for mm in list(re.finditer(r"[^.]{0,400}" + re.escape(needle.split(",")[0].replace(" Inc.", "").replace(", Inc", "")) + r"[^.]{0,400}\.", t, re.I))[:4]:
    print("  ..", mm.group(0).strip()[:700])
