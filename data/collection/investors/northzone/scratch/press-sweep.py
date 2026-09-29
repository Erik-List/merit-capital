#!/usr/bin/env python3
"""Recall probe, press layer (COLLECTION.md s3): Google News headlines naming Northzone as lead or backer,
company names pulled from the headline, kept when no base row, archive name or merge covers them.
Output scratch/press-sweep.json."""
import importlib.util, json, re, sys, glob
from pathlib import Path
H = Path(__file__).resolve().parent
ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); argv, sys.argv = sys.argv[1:], sys.argv[:1]; spec.loader.exec_module(gs)
def k(s): return re.sub(r"[^a-z0-9]", "", (s or "").lower())
known = {k(r["name"]) for r in json.load(open(H.parent / "companies" / "base.json"))}
for f in glob.glob(str(H.parent / "sources" / "wayback" / "parsed" / "*.json")):
    known |= {k(r["name"]) for r in json.load(open(f))}
Q = ['"led by Northzone"', '"Northzone leads"', '"Northzone-led"', '"Northzone-backed"', '"backed by Northzone"',
     '"Northzone" seed round', '"Northzone" "Series A"', '"Northzone" "Series B"', '"Northzone" invests',
     '"Northzone" portfolio company acquired', '"Northzone Ventures" invests', '"Northzone" participation round']
out = {}
for q in Q:
    r = gs.googlenews(q, "Northzone")
    if r["status"] != "ok":
        print(q, "FAILED"); continue
    for i in r["items"]:
        t = i["title"]
        m = re.match(r"^(?:[A-Z][\w'’.-]*(?:\s[A-Z][\w'’.-]*){0,3}(?:-based)?\s)?([A-Z0-9][\w.&'’!-]*(?:\s[A-Z0-9][\w.&'’!-]*){0,2})\s+(raises|secures|lands|closes|bags|nabs|scores|gets|snags|grabs|announces|banks|picks up|receives)", t)
        c = m.group(1) if m else None
        if c and k(c) not in known and len(k(c)) > 2:
            out.setdefault(c, []).append({"date": i["date"], "title": t[:180], "source": i["source"], "gid": i["gid"], "q": q})
json.dump(out, open(H / "press-sweep.json", "w"), indent=1, ensure_ascii=False)
for c, v in sorted(out.items(), key=lambda x: x[1][0]["date"]):
    print(v[0]["date"], "|", c, "|", v[0]["title"][:140])
