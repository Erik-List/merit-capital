#!/usr/bin/env python3
"""Recall probe, press layer (COLLECTION.md §3): Google News headlines naming
Atomico per year window, diffed against the base. Prints the headlines that
name no base company, for the judge to read; writes scratch/press-sweep.json.

Usage: python3 press-sweep.py [first_year] [last_year]
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)

y0 = int(argv[0]) if argv else 2006
y1 = int(argv[1]) if len(argv) > 1 else 2026
base = json.loads((HERE.parent / "companies" / "base.json").read_text())
names = set()
for r in base:
    for n in (r["name"], r["slug"].replace("-", " ")):
        n = re.sub(r"(?i)\b(inc|ltd|llc|limited|holdings?|technologies|n v)\b\.?", "", n).strip().lower()
        if len(n) >= 3:
            names.add(n)
EXTRA = {"messagebird", "gympass", "goeuro", "memphis meats", "quit genius", "wunderlist",
         "6wunderkinder", "weatherbill", "mygengo", "sheeldmarket", "aliph", "iboxpay",
         "wonder", "angry birds", "mytaxi", "stubhub"}
names |= EXTRA
QUERIES = ['"Atomico" leads', '"Atomico" invests', '"led by Atomico"', '"Atomico" backed raises']
out = []
for y in range(y0, y1 + 1):
    seen = set()
    for q in QUERIES:
        res = gs.googlenews(f"{q} after:{y}-01-01 before:{y + 1}-01-01", "Atomico")
        if res["status"] != "ok":
            print("ERR", y, q, res.get("status"))
            continue
        for i in res["items"]:
            t = i["title"]
            if t in seen:
                continue
            seen.add(t)
            low = t.lower()
            hit = sorted(n for n in names if re.search(r"(?<![a-z])" + re.escape(n) + r"(?![a-z])", low))
            out.append({"year": y, "date": i["date"], "source": i["source"], "title": t,
                        "gid": i["gid"], "base_names": hit})
    new = [o for o in out if o["year"] == y and not o["base_names"]]
    print(f"== {y}: {len(seen)} headlines, {len(new)} naming no base company")
    for o in new:
        print(f"   {o['date']} | {o['source'][:22]:22} | {o['title'][:140]}")
(HERE / "press-sweep.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
