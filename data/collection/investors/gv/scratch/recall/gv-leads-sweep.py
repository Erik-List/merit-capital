#!/usr/bin/env python3
"""Recall probe, press layer (COLLECTION.md s3): Google News headlines that name GV or Google Ventures as a round's
lead or participant, one query per phrase per year window (the RSS search takes after:/before: operators), so the
cap on items per query does not hide a year. Every headline is matched against the base's names; the ones that name
no base company are the candidates, read by the judge.

Output: scratch/recall/gv-leads.json {query: {status, items}} and scratch/recall/gv-leads-unmatched.json
Usage: python3 gv-leads-sweep.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)

OUT = HERE / "gv-leads.json"
PHRASES = ['"led by GV"', '"GV led"', '"from GV"', '"led by Google Ventures"', '"Google Ventures led"',
           '"from Google Ventures"', '"GV (formerly Google Ventures)"']
cache = json.loads(OUT.read_text()) if OUT.exists() else {}
for year in range(2009, 2027):
    for ph in PHRASES:
        if "Google Ventures" in ph and "formerly" not in ph and year > 2017:
            continue
        q = f"{ph} after:{year}-01-01 before:{year + 1}-01-01"
        if (cache.get(q) or {}).get("status") == "ok":
            continue
        res = gs.googlenews(q, "GV")
        cache[q] = {"status": res["status"], "items": [{k: it[k] for k in ("date", "title", "source", "gid")}
                                                       for it in res.get("items", [])]}
        print(year, ph, res["status"], len(cache[q]["items"]), flush=True)
        OUT.write_text(json.dumps(cache, indent=1, ensure_ascii=False) + "\n")

base = json.loads((HERE.parents[1] / "companies" / "base.json").read_text())


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


names = sorted({norm(r["name"]) for r in base if len(norm(r["name"])) > 3}, key=len, reverse=True)
seen, unmatched = set(), []
for q, v in cache.items():
    for it in v.get("items", []):
        t = norm(it["title"])
        if it["title"] in seen:
            continue
        seen.add(it["title"])
        if not re.search(r"\b(gv|google ventures)\b", t):
            continue
        if any(re.search(r"\b" + re.escape(n) + r"\b", t) for n in names):
            continue
        unmatched.append(it)
unmatched.sort(key=lambda i: i["date"])
(HERE / "gv-leads-unmatched.json").write_text(json.dumps(unmatched, indent=1, ensure_ascii=False) + "\n")
print(len(seen), "headlines;", len(unmatched), "name GV and no base company")
