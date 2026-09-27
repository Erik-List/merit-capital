#!/usr/bin/env python3
"""CDX exploration for the archive layer: which URL shapes carried the firm's
portfolio in which years. Every request goes through scripts/ia_fetch.py, so
it is paced and serves the machine-wide cooldown. Writes scratch/cdx/*.json.
Usage: python3 .../scratch/cdx-explore.py"""
import json, re, sys, collections
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402


def cdx(pattern, **kw):
    qs = "&".join([f"url={pattern}", "output=json"] + [f"{k}={v}" for k, v in kw.items()])
    body, code = ia_fetch.get(f"https://web.archive.org/cdx/search/cdx?{qs}")
    try:
        data = json.loads(body or b"[]")
    except ValueError:
        data = []
    return (data[1:] if data else []), code


out = {}
for name, pattern, kw in (
    ("all-to-2012", "generalcatalyst.com/*", dict(collapse="urlkey", fl="timestamp,original,statuscode,mimetype", to="2012", limit="8000", filter="mimetype:text/html")),
    ("all-2013-2019", "generalcatalyst.com/*", dict(collapse="urlkey", fl="timestamp,original,statuscode,mimetype", **{"from": "2013"}, to="2019", limit="12000", filter="mimetype:text/html")),
    ("all-2020-2026", "generalcatalyst.com/*", dict(collapse="urlkey", fl="timestamp,original,statuscode,mimetype", **{"from": "2020"}, limit="15000", filter="mimetype:text/html")),
    ("gcpartners", "gcpartners.com/*", dict(collapse="urlkey", fl="timestamp,original,statuscode,mimetype", limit="4000")),
):
    rows, code = cdx(pattern, **kw)
    out[name] = {"code": code, "n": len(rows)}
    json.dump(rows, open(INV / f"scratch/cdx/{name}.json", "w"))
    print(name, code, len(rows), flush=True)
    c = collections.Counter()
    yrs = collections.defaultdict(set)
    for r in rows:
        u = re.sub(r"^https?://(www\.)?generalcatalyst\.com(:80)?", "", r[1]).split("?")[0]
        p = "/".join(u.split("/")[:2]).lower()
        c[p] += 1
        yrs[p].add(r[0][:4])
    for p, n in c.most_common(18):
        ys = sorted(yrs[p])
        print(f"   {n:5d} {p} {ys[0]}-{ys[-1]}")
json.dump(out, open(INV / "scratch/cdx/summary.json", "w"), indent=1)
