#!/usr/bin/env python3
"""Query-aware copy of cc-fetch.py (the ?id=N pages of the 2010-13 site). Fetch Common Crawl captures of googleventures.com and gv.com by WARC/ARC range request
(data.commoncrawl.org), from the records in scratch/cc-index-raw.json (cc-cluster.py).

Raw bodies land in data/filings/commoncrawl/gv/<crawl>/<timestamp>-<domain>-<path>.html
(gitignored, re-downloadable); the manifest sources/wayback/cc-manifest.json keeps url,
timestamp, crawl, digest and capture_url (the index.commoncrawl.org form, the citation,
COLLECTION.md s1: a capture URL is a valid citation when the live page is gone).
A record that does not answer is listed FAILED in the manifest, never skipped silently.

Usage: python3 cc-fetch.py <regex on domain+path> [--first-per-path | --first-per-path-year]
  e.g. python3 cc-fetch.py '^(gv|gve):/(portfolio|companies)/?$'
       python3 cc-fetch.py '^(gv|gve):/team/[a-z]' --first-per-path-year
Adapted from bain-capital-ventures/scratch/cc-fetch.py (BCV run, 2026-09-27)."""
import gzip
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = HERE / "cc-index-raw.json"
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "new-enterprise-associates"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
DOM = re.compile(r"https?://(www\.)?nea\.com(:\d+)?", re.I)


def dom_of(url):
    return "nea"


def path_of(url):
    # query-aware (cc-fetch-q.py): the 2010-13 ASP.NET site keys each company and person on ?id=N
    return DOM.sub("", url).split("#")[0] or "/"


def key_of(cid, r):
    p = re.sub(r"[^A-Za-z0-9._-]+", "_", path_of(r["url"]).strip("/")) or "root"
    return f"{cid}/{r['timestamp']}-{dom_of(r['url'])}-{p}.html"


def fetch(cid, r, man):
    key = key_of(cid, r)
    if man.get(key, {}).get("status") == "ok":
        return key
    a, ln = int(r["offset"]), int(r["length"])
    body = None
    for attempt in range(3):
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a+ln-1}", "-w", "\n%{http_code}",
                            f"https://data.commoncrawl.org/{r['filename']}"], capture_output=True)
        raw, _, code = p.stdout.rpartition(b"\n")
        time.sleep(0.15)
        if code == b"503":
            time.sleep(10)
            continue
        try:
            rec = gzip.decompress(raw)
        except Exception:
            time.sleep(2)
            continue
        if rec.startswith(b"WARC/"):
            _, _, rest = rec.partition(b"\r\n\r\n")
            _, _, body = rest.partition(b"\r\n\r\n")
        else:  # ARC (the 2008-2012 crawls): one header line, then the HTTP response
            _, _, body = rec.partition(b"\r\n\r\n")
            if not body:
                _, _, body = rec.partition(b"\n\n")
        break
    if body is None:
        man[key] = {"status": "FAILED", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid}
        return None
    (RAW / cid).mkdir(parents=True, exist_ok=True)
    (RAW / key).write_bytes(body)
    man[key] = {"status": "ok", "url": r["url"], "domain": dom_of(r["url"]), "path": path_of(r["url"]),
                "timestamp": r["timestamp"], "crawl": cid, "bytes": len(body), "digest": r.get("digest"),
                "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}
    return key


def main():
    pat = re.compile(sys.argv[1])
    mode = sys.argv[2] if len(sys.argv) > 2 else ""
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    idx = json.loads(IDX.read_text())
    todo, seen = [], set()
    # identical bodies (same digest) are fetched once: the dozens of daily captures of one listing in a crawl
    # carry one digest; a changed page carries a new one, so every distinct version still lands
    have = {v.get("digest") for v in man.values() if v.get("status") == "ok" and v.get("digest")}
    for cid, slots in sorted(idx.items()):
        for _key, v in sorted(slots.items()):
            for r in sorted(v.get("records", []), key=lambda r: r["timestamp"]):
                dp = f"{dom_of(r['url'])}:{path_of(r['url'])}"
                if not pat.search(dp):
                    continue
                norm_p = dp.rstrip("/")
                k = norm_p if mode == "--first-per-path" else (norm_p, r["timestamp"][:4]) \
                    if mode == "--first-per-path-year" else None
                if k is not None:
                    if k in seen:
                        continue
                    seen.add(k)
                if r.get("digest") and r["digest"] in have:
                    continue
                have.add(r.get("digest"))
                todo.append((cid, r))
    print(len(todo), "captures to fetch", flush=True)
    n = 0
    for i, (cid, r) in enumerate(todo):
        if fetch(cid, r, man):
            n += 1
        if i % 50 == 49:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(i + 1, "done", flush=True)
    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    print(n, "fetched;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total")


if __name__ == "__main__":
    main()
