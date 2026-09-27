#!/usr/bin/env python3
"""Narrow CDX queries for generalcatalyst.com's portfolio and people pages, one
prefix at a time (a whole-domain query 504s while the archive is degraded).
Every request goes through scripts/ia_fetch.py (paced, cooldown-aware).
Writes scratch/cdx/<name>.json and prints the path groups by year."""
import json, re, sys, collections
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(INV.parents[3] / "scripts"))
import ia_fetch  # noqa: E402

def cdx(pattern, **kw):
    qs = "&".join([f"url={pattern}", "output=json"] + [f"{k}={v}" for k, v in kw.items()])
    body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?{qs}")
    try:
        data = json.loads(body or b"[]")
    except ValueError:
        data = []
    return (data[1:] if data else []), code

Q = [
    ("root-to-2012", "generalcatalyst.com", dict(fl="timestamp,original,statuscode,digest", to="2012", collapse="timestamp:6")),
    ("portfolio-prefix", "generalcatalyst.com/portfolio*", dict(collapse="urlkey", fl="timestamp,original,statuscode", limit="3000")),
    ("companies-prefix", "generalcatalyst.com/companies*", dict(collapse="urlkey", fl="timestamp,original,statuscode", limit="3000")),
    ("company-prefix", "generalcatalyst.com/company*", dict(collapse="urlkey", fl="timestamp,original,statuscode", limit="3000")),
    ("team-prefix", "generalcatalyst.com/team*", dict(collapse="urlkey", fl="timestamp,original,statuscode", limit="3000")),
    ("people-prefix", "generalcatalyst.com/people*", dict(collapse="urlkey", fl="timestamp,original,statuscode", limit="3000")),
    ("html-to-2012", "generalcatalyst.com/*.htm*", dict(collapse="urlkey", fl="timestamp,original,statuscode", to="2012", limit="3000")),
    ("php-to-2012", "generalcatalyst.com/*.php*", dict(collapse="urlkey", fl="timestamp,original,statuscode", to="2012", limit="3000")),
    ("asp-to-2012", "generalcatalyst.com/*.asp*", dict(collapse="urlkey", fl="timestamp,original,statuscode", to="2012", limit="3000")),
]
only = set(sys.argv[1:])
for name, pattern, kw in Q:
    if only and name not in only:
        continue
    rows, code = cdx(pattern, **kw)
    json.dump(rows, open(INV / f"scratch/cdx/{name}.json", "w"))
    print(name, code, len(rows), flush=True)
    c = collections.Counter(); yrs = collections.defaultdict(set)
    for r in rows:
        u = re.sub(r"^https?://(www\.)?generalcatalyst\.com(:80)?", "", r[1]).split("?")[0]
        p = "/".join(u.split("/")[:2]).lower() or "/"
        c[p] += 1; yrs[p].add(r[0][:4])
    for p, n in c.most_common(15):
        ys = sorted(yrs[p]); print(f"   {n:5d} {p} {ys[0]}-{ys[-1]}", flush=True)
