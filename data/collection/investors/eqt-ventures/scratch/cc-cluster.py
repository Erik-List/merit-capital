#!/usr/bin/env python3
"""Common Crawl captures of an EQT Ventures domain WITHOUT the index server
(adapted from the Balderton run's cc-cluster.py). index.commoncrawl.org
refused every crawl from 2020 back on 2026-09-27; the index is also a set of
static files on data.commoncrawl.org, and a binary search over each crawl's
cluster.idx with range requests finds the cdx blocks for the domain's SURT
prefix (the prefix without ")" so subdomains such as jobs. are included).
Records merge into ../sources/wayback/cc-index-raw.json under the domain,
marked "via": "cluster.idx"; a crawl that does not answer is FAILED.

Usage: cc-cluster.py <domain> [crawl-id ...]   (default: the domain's crawls not yet ok)
"""
import gzip, json, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
HOST = "https://data.commoncrawl.org"
DOMAIN = sys.argv[1]
KEY = ",".join(reversed(DOMAIN.split(".")))

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
    allj = json.loads(OUT.read_text()) if OUT.exists() else {}
    data = allj.setdefault(DOMAIN, {})
    coll = json.loads(subprocess.run(["curl", "-s", "--max-time", "60", "https://index.commoncrawl.org/collinfo.json"],
                                     capture_output=True, text=True).stdout or "[]")
    default = [c["id"] for c in coll if c["id"][8:12].isdigit() and 2016 <= int(c["id"][8:12]) <= 2026]
    for cid in (sys.argv[2:] or default):
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
                if line.startswith(KEY + ")") or line.startswith(KEY + ","):
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
        write_atomic(OUT, json.dumps(allj, indent=0) + "\n")

if __name__ == "__main__":
    main()
