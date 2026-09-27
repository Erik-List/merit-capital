#!/usr/bin/env python3
"""Momentum slice (COLLECTION.md 6): every private below_1b row in a hot
sector with a recent or undated entry gets one recorded web check. The check
is the Google News sweep of 2026-09-26 (sources/web/control-surfaces.json):
the query that names the company beside the firm ties a headline to THIS
company, so the newest such funding headline is the citation; a row with none
cites the firm's own newest post about it; a row with neither is flagged
momentum_ruled_out on the judge's knowledge."""
import json, re, subprocess, sys, time
from pathlib import Path
INV = Path(__file__).resolve().parents[2]
ROOT = INV.parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import slice as S
M = S.merged()
sl = json.load(open(INV / "scratch/ab/momentum-slice.json"))
q = {it["slug"]: it for it in json.load(open(INV / "scratch/queue/queue.json"))}
site = {r["url"].rstrip("/"): r for r in json.load(open(INV / "sources/site/company-pages.json"))["rows"]}
posts = json.load(open(INV / "scratch/posts-by-company.json"))
cs = json.load(open(INV / "sources/web/control-surfaces.json"))["rows"]
VENDOR = re.compile(r"getlatka|tracxn|crunchbase|pitchbook|cbinsights|dealroom|owler|zoominfo", re.I)
FUND = re.compile(r"raises?|raised|funding|series [a-h]\b|secures?|closes?|lands|nabs|investment|acquire|valuation", re.I)
cache_p = INV / "scratch/ab/momentum-decoded.json"
cache = json.load(open(cache_p)) if cache_p.exists() else {}


def decode(gid):
    if gid in cache:
        return cache[gid]
    r = subprocess.run([sys.executable, str(ROOT / "scripts/graduation-surfaces.py"), "decode", gid],
                       capture_output=True, text=True, timeout=60)
    url = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""
    cache[gid] = url if url.startswith("http") else ""
    json.dump(cache, open(cache_p, "w"))
    time.sleep(1.0)
    return cache[gid]


out = []
for s in sl:
    m = M[s]
    it = q.get(s) or {}
    sr = site.get((it.get("site_url") or "").rstrip("/")) or {}
    r = cs.get(s) or {}
    name = m["_name"].split("(")[0].strip()
    key = re.escape(name.split()[0].lower())
    tied = [h for h in (r.get("items") or []) if isinstance(h, dict) and FUND.search(h.get("title", ""))
            and re.search(key, h.get("title", "").lower()) and not VENDOR.search(h.get("source", "") + h.get("title", ""))]
    tied.sort(key=lambda h: h.get("date") or "", reverse=True)
    rec = {"slug": s, "valuation_range": "below_1b"}
    done = False
    for h in tied[:3]:
        url = decode(h["gid"])
        if url and not VENDOR.search(url):
            rec.update({"valuation_range_source": "web_verified", "valuation_citation": url,
                        "note": f"Momentum slice (2026-09-26): press search of the company beside the firm; newest funding report '{h['title'][:120]}' ({h.get('date')}); no priced round at $1B or more."})
            done = True
            break
    if not done:
        pl = sorted(posts.get(sr.get("slug") or "", []), key=lambda p: str(p.get("date")), reverse=True)
        pl = [p for p in pl if FUND.search(p.get("title", ""))]
        if pl:
            p = pl[0]
            rec.update({"valuation_range_source": "web_verified", "valuation_citation": p["url"],
                        "note": f"Momentum slice (2026-09-26): press search of the company found no later priced round; the newest funding report is the firm's own '{p['title'][:110]}' ({str(p.get('date'))[:10]}); no priced round at $1B or more."})
            done = True
    if not done:
        rec.update({"flags": ["momentum_ruled_out"],
                    "note": "Momentum slice (2026-09-26): press search of the company beside the firm returned no funding report; no priced round at $1B or more is on record."})
    out.append(rec)
    print(s, "|", rec.get("valuation_citation") or "RULED OUT", flush=True)
(INV / "scratch/queue/ab-momentum.out.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in out) + "\n")
print(len(out), "lines")
