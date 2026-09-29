#!/usr/bin/env python3
"""Common Crawl captures of gv.com and googleventures.com WITHOUT the index server.

Adapted from bain-capital-ventures/scratch/cc-cluster.py (itself from Insight's):
Common Crawl is the archive layer while the Internet Archive's machine-wide
firewall cooldown is set (Erik 2026-09-26; the cooldown stood at its 8-hour
ceiling until about 06:38 UTC on 2026-09-29 when this run started).

index.commoncrawl.org is one heavily limited machine, but the index itself is a
set of static files on data.commoncrawl.org: per crawl one sorted `cluster.idx`
(SURT key, cdx file, offset, length) over ~300 gzip-block cdx files. A binary
search over cluster.idx with HTTP range requests finds the blocks that can hold
the key, and one range request per block returns the index lines.

GV's two domains: googleventures.com (2009 to 2015; the firm renamed itself GV
in 2015) and gv.com (2015 on). Both keys are read per crawl. The old ARC
collections (CC-MAIN-2008-2009, 2009-2010, 2012) are read too, since they exist
and are readable on the data host (Balderton, 2026-09-27).

Output: cc-index-raw.json  {crawl: {key: {"status": ok|failed, "records": [...]}}}
Usage: python3 cc-cluster.py [crawl-id ...]
"""
import gzip
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = HERE / "cc-index-raw.json"
HOST = "https://data.commoncrawl.org"
KEYS = ["com,googleventures)", "com,gv)"]
# Everything under the two domains except static assets: the listing, the people pages, the firm's
# posts and library (the counterparty-side evidence for entry rounds) all matter here.
ASSET = re.compile(r"\.(css|js|png|jpe?g|gif|svg|ico|woff2?|ttf|eot|mp4|webp|pdf|xml|json|txt)(\?|$)", re.I)
# The collection list as the data host publishes it (cc-index/collections/index.html, saved beside this script
# as cc-collections.html on 2026-09-29: 125 crawls from CC-MAIN-2008-2009 to CC-MAIN-2026-39).
CRAWLS = sorted(set(re.findall(r"CC-MAIN-\d{4}(?:-\d{2,4})?", (HERE / "cc-collections.html").read_text())))


def rng(url, a, b):
    for attempt in range(4):
        r = subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, "-r", f"{a}-{b}", "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code in (b"206", b"200"):
            time.sleep(0.2)
            return body
        if code == b"404":
            return None
        time.sleep(3 * (attempt + 1))
    return None


def size(url):
    r = subprocess.run(["curl", "-sI", "--max-time", "40", "-A", UA, url], capture_output=True, text=True)
    if " 404" in (r.stdout.splitlines() or [""])[0]:
        return 0
    for line in r.stdout.splitlines():
        if line.lower().startswith("content-length:"):
            return int(line.split(":")[1])
    return None


def blocks(cid, key):
    url = f"{HOST}/cc-index/collections/{cid}/indexes/cluster.idx"
    n = size(url)
    if not n:
        return n  # 0 = no such crawl, None = not readable
    lo, hi = 0, n
    while hi - lo > 200_000:                      # binary search on byte offsets
        mid = (lo + hi) // 2
        chunk = rng(url, mid, mid + 4000)
        if chunk is None:
            return None
        lines = chunk.decode("utf-8", "replace").split("\n")
        if len(lines) < 3:
            return None
        k = lines[1].split(" ")[0]              # first whole line after mid
        if k < key:
            lo = mid
        else:
            hi = mid
    chunk = rng(url, max(0, lo - 4000), hi + 400_000)
    if chunk is None:
        return None
    rows = [ln.split("\t") for ln in chunk.decode("utf-8", "replace").split("\n")[1:-1]]
    rows = [r for r in rows if len(r) >= 4]
    out = []
    for i, r in enumerate(rows):
        k = r[0].split(" ")[0]
        nxt = rows[i + 1][0].split(" ")[0] if i + 1 < len(rows) else None
        # block i holds keys from its own first key up to the next block's first key
        if k <= key + "\xff" and (nxt is None or nxt >= key):
            out.append((r[1], int(r[2]), int(r[3])))
        if k > key + "\xff":
            break
    return out


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for cid in (sys.argv[1:] or CRAWLS):
        for key in KEYS:
            slot = data.setdefault(cid, {})
            if slot.get(key, {}).get("status") in ("ok", "absent"):
                continue
            bl = blocks(cid, key)
            if bl == 0:
                slot[key] = {"status": "absent", "records": []}
                print(cid, key, "no such crawl", flush=True)
                continue
            if bl is None:
                print(cid, key, "FAILED (cluster.idx not readable)", flush=True)
                slot[key] = {"status": "failed", "records": []}
                continue
            recs, bad = [], False
            for f, off, ln in bl:
                b = rng(f"{HOST}/cc-index/collections/{cid}/indexes/{f}", off, off + ln - 1)
                if b is None:
                    bad = True
                    break
                for line in gzip.decompress(b).decode("utf-8", "replace").splitlines():
                    if line.startswith(key):
                        surt, ts, js = line.split(" ", 2)
                        try:
                            d = json.loads(js)
                        except ValueError:
                            continue
                        d["timestamp"] = ts
                        u = d.get("url") or ""
                        if d.get("status") == "200" and not ASSET.search(u):
                            recs.append({k: d.get(k) for k in ("url", "timestamp", "status", "mime", "digest",
                                                                "filename", "offset", "length")})
            if bad:
                print(cid, key, "FAILED (a cdx block did not answer)", flush=True)
                slot[key] = {"status": "failed", "records": []}
            else:
                slot[key] = {"status": "ok", "records": recs, "via": "cluster.idx", "blocks": len(bl)}
                print(cid, key, len(recs), "captures in", len(bl), "block(s)", flush=True)
            write_atomic(OUT, json.dumps(data, indent=1) + "\n")


if __name__ == "__main__":
    main()
