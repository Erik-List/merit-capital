#!/usr/bin/env python3
"""Planned Common Crawl fetches for bvp.com (one process at a time: two cc-fetch.py runs overwrote each other's
manifest on 2026-10-01). Selects from scratch/cc-index-raw.json and fetches through cc-fetch.py's own fetch():
  listings   per year and listing path (no query string): the first and the last capture of the year
  anti       per year and anti-portfolio path: the first capture
  teamlist   per year: the first capture of /team (no query)
  forge      every distinct bvp.com/forge page, the last capture
  people     one capture (the last) per /team/<slug> not yet fetched
  companies  one capture (the first) per company-page slug listed in scratch/cc-company-need.json
Usage: python3 cc-plan.py listings anti teamlist forge people companies
"""
import importlib.util, json, re, sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ccf", HERE / "cc-fetch.py"); ccf = importlib.util.module_from_spec(spec); spec.loader.exec_module(ccf)
idx = json.loads(ccf.IDX.read_text())
man = json.loads(ccf.MAN.read_text()) if ccf.MAN.exists() else {}
recs = []
for cid, slots in idx.items():
    for v in slots.values():
        for r in v.get("records", []):
            p = re.sub(r"https?://(www\.)?bvp\.com(:\d+)?", "", r["url"])
            recs.append((cid, r, p.split("?")[0].rstrip("/") or "/", "?" in p))
recs.sort(key=lambda x: x[1]["timestamp"])
todo, modes = [], sys.argv[1:]
def first_last(sel, key, both=True):
    groups = collections.defaultdict(list)
    for x in sel:
        groups[key(x)].append(x)
    out = []
    for g in groups.values():
        out.append(g[0])
        if both and g[-1][1].get("digest") != g[0][1].get("digest"):
            out.append(g[-1])
    return out
if "listings" in modes:
    sel = [x for x in recs if not x[3] and (re.match(r"^/(in/)?(portfolio|companies|Portfolio)$", x[2]) or
                                           re.match(r"^/Portfolio/(Portfolio|Report_Frame|report)\.aspx$", x[2], re.I) or
                                           re.match(r"^/(portfolio/)?top-?exits$", x[2], re.I))]
    todo += first_last(sel, lambda x: (x[1]["timestamp"][:4], x[2]))
if "anti" in modes:
    sel = [x for x in recs if re.search(r"anti-?portfolio|/port/anti", x[2], re.I) and "atlas" not in x[2] and not re.search(r"[,<%]", x[2])]
    todo += first_last(sel, lambda x: (x[1]["timestamp"][:4], x[2].lower()), both=False)
if "teamlist" in modes:
    sel = [x for x in recs if not x[3] and re.match(r"^/(in/)?[Tt]eam$", x[2])]
    todo += first_last(sel, lambda x: (x[1]["timestamp"][:4], x[2].lower()), both=False)
if "forge" in modes:
    sel = [x for x in recs if not x[3] and re.match(r"^/forge(/|$)", x[2])]
    todo += [g for g in first_last(list(reversed(sel)), lambda x: x[2].lower(), both=False)]
if "people" in modes:
    have = {re.sub(r"\.aspx$", "", v["path"].rstrip("/").rsplit("/", 1)[-1].lower()) for v in man.values()
            if v.get("status") == "ok" and re.match(r"^/(in/)?[Tt]eam/[A-Za-z]", v.get("path", ""))}
    sel = [x for x in recs if not x[3] and re.match(r"^/(in/)?team/[a-z0-9-]+$", x[2]) and x[2].rsplit("/", 1)[-1] not in have]
    todo += first_last(list(reversed(sel)), lambda x: x[2].lower(), both=False)
if "companies" in modes:
    need = set(json.loads((HERE / "cc-company-need.json").read_text()))
    sel = [x for x in recs if not x[3] and x[2].lower().lstrip("/") in need]
    todo += first_last(sel, lambda x: x[2].lower(), both=False)
seen, plan = set(), []
for cid, r, p, q in todo:
    k = ccf.key_of(cid, r)
    if k in seen or man.get(k, {}).get("status") == "ok":
        continue
    seen.add(k); plan.append((cid, r))
print(len(plan), "captures to fetch", flush=True)
n = 0
for i, (cid, r) in enumerate(plan):
    if ccf.fetch(cid, r, man):
        n += 1
    if i % 25 == 24:
        ccf.write_atomic(ccf.MAN, json.dumps(man, indent=1) + "\n")
        print(i + 1, "done", flush=True)
ccf.write_atomic(ccf.MAN, json.dumps(man, indent=1) + "\n")
print(n, "fetched;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total", flush=True)
