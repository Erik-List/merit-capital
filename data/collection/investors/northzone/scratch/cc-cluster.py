#!/usr/bin/env python3
"""Common Crawl captures of northzone.com WITHOUT the index server (copied from the Balderton run, PRO-106).

index.commoncrawl.org answered nothing for a whole evening (every crawl FAILED
in cc-index.py), but the index itself is a set of static files on
data.commoncrawl.org: per crawl one sorted `cluster.idx` (SURT key, cdx file,
offset, length) over ~300 gzip-block cdx files. A binary search over
cluster.idx with HTTP range requests finds the blocks that can hold
`com,northzone)`, and one range request per block returns the index lines.
About 30 small requests per crawl, on the static host (not the index server).

Output: ../sources/wayback/cc-index-raw.json  {crawl: {"status": ok|failed, "records": [...], "via": "cluster.idx"}}
Usage: python3 cc-cluster.py [crawl-id ...]
"""
import gzip, json, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
HOST = "https://data.commoncrawl.org"
KEY = "com,northzone)"
CRAWLS = ['CC-MAIN-2013-20', 'CC-MAIN-2013-48', 'CC-MAIN-2014-23', 'CC-MAIN-2014-52', 'CC-MAIN-2015-27', 'CC-MAIN-2015-48', 'CC-MAIN-2016-30', 'CC-MAIN-2016-50', 'CC-MAIN-2017-30', 'CC-MAIN-2017-51', 'CC-MAIN-2018-30', 'CC-MAIN-2018-51', 'CC-MAIN-2019-30', 'CC-MAIN-2019-51', 'CC-MAIN-2020-29', 'CC-MAIN-2020-50', 'CC-MAIN-2021-25', 'CC-MAIN-2021-49', 'CC-MAIN-2022-27', 'CC-MAIN-2022-49', 'CC-MAIN-2023-23', 'CC-MAIN-2023-50', 'CC-MAIN-2024-30', 'CC-MAIN-2024-51', 'CC-MAIN-2025-30', 'CC-MAIN-2025-51']

def rng(url, a, b):
    for attempt in range(4):
        r = subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, "-r", f"{a}-{b}", "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code in (b"206", b"200"):
            time.sleep(0.25)
            return body
        time.sleep(3 * (attempt + 1))
    return None

def size(url):
    r = subprocess.run(["curl", "-sI", "--max-time", "40", "-A", UA, url], capture_output=True, text=True)
    for l in r.stdout.splitlines():
        if l.lower().startswith("content-length:"):
            return int(l.split(":")[1])
    return None

def blocks(cid):
    url = f"{HOST}/cc-index/collections/{cid}/indexes/cluster.idx"
    n = size(url)
    if not n:
        return None
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
        if k < KEY:
            lo = mid
        else:
            hi = mid
    chunk = rng(url, max(0, lo - 4000), hi + 400_000)
    if chunk is None:
        return None
    rows = [l.split("\t") for l in chunk.decode("utf-8", "replace").split("\n")[1:-1]]
    rows = [r for r in rows if len(r) >= 4]
    out = []
    for i, r in enumerate(rows):
        k = r[0].split(" ")[0]
        nxt = rows[i + 1][0].split(" ")[0] if i + 1 < len(rows) else None
        # block i holds keys from its own first key up to the next block's first key
        if k <= KEY + "\xff" and (nxt is None or nxt >= KEY):
            out.append((r[1], int(r[2]), int(r[3])))
        if k > KEY + "\xff":
            break
    return out

def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for cid in (sys.argv[1:] or CRAWLS):
        if data.get(cid, {}).get("status") == "ok":
            continue
        bl = blocks(cid)
        if bl is None:
            print(cid, "FAILED (cluster.idx not readable)")
            data[cid] = {"status": "failed", "records": []}
            continue
        recs, bad = [], False
        for f, off, ln in bl:
            b = rng(f"{HOST}/cc-index/collections/{cid}/indexes/{f}", off, off + ln - 1)
            if b is None:
                bad = True
                break
            for line in gzip.decompress(b).decode("utf-8", "replace").splitlines():
                if line.startswith(KEY):
                    surt, ts, js = line.split(" ", 2)
                    try:
                        d = json.loads(js)
                    except ValueError:
                        continue
                    d["timestamp"] = ts
                    if d.get("status") == "200":
                        recs.append({k: d.get(k) for k in ("url", "timestamp", "status", "mime", "digest", "filename", "offset", "length")})
        if bad:
            print(cid, "FAILED (a cdx block did not answer)")
            data[cid] = {"status": "failed", "records": []}
        else:
            data[cid] = {"status": "ok", "records": recs, "via": "cluster.idx", "blocks": len(bl)}
            print(cid, len(recs), "captures in", len(bl), "block(s)")
        write_atomic(OUT, json.dumps(data, indent=1) + "\n")

if __name__ == "__main__":
    main()
