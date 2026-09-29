#!/usr/bin/env python3
"""Recall probe, third-party side: for each third-party or ownership-form registrant in
sources/edgar/fts-hits.json that is not in the base, print the text around every ICONIQ
mention in up to three of its hit documents (SEC, paced through shared_throttle; cached in
scratch/s1-raw/, the s1-iconiq.py cache). Read-only on the sources; prints to stdout.
Usage: python3 .../scratch/fts-context.py [--only REGEX] [--all]
"""
import html as H, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from importlib import import_module
s1 = import_module("s1-iconiq".replace("-", "_")) if False else None
import runpy
G = runpy.run_path(str(HERE / "s1-iconiq.py"))["get"]
INV = HERE.parent
fts = json.load(open(INV / "sources/edgar/fts-hits.json"))
base = json.load(open(INV / "companies/base.json"))
base = base if isinstance(base, list) else list(base.values())
norm = lambda s: re.sub(r"[^a-z0-9]", "", re.sub(r",? (inc|corp|ltd|llc|holdings|co)\.?.*$", "", s.lower()))
names = {norm(r["name"]) for r in base}
only = re.compile(sys.argv[sys.argv.index("--only") + 1], re.I) if "--only" in sys.argv else None
ALL = "--all" in sys.argv
for r in fts["registrants"]:
    if r.get("bucket") not in ("third_party", "ownership_forms"):
        continue
    n = norm(r["registrant"])
    if not ALL and any(n and len(x) > 3 and (n in x or x in n) for x in names):
        continue
    if only and not only.search(r["registrant"]):
        continue
    print(f"\n===== {r['registrant']} ({r['bucket']}; {r['first_date']}..{r['last_date']})")
    for f in r.get("filings", [])[:3]:
        t = G(f["url"])
        t = H.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)))
        hits = [m.start() for m in re.finditer(r"iconiq", t, re.I)]
        print(f"  -- {f['form']} {f['date']} {f['url']} ({len(hits)} mentions)")
        last = -10**9
        shown = 0
        for h in hits:
            if h - last < 400:
                continue
            last = h
            print("     ...", t[max(0, h - 280): h + 320].strip())
            shown += 1
            if shown >= 3:
                break
