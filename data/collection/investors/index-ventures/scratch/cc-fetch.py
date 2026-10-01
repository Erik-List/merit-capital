#!/usr/bin/env python3
"""Fetch Common Crawl captures of indexventures.com list surfaces by WARC range
request (data.commoncrawl.org), from the records in sources/wayback/cc-index-raw.json.
Raw bodies land in data/filings/commoncrawl/index-ventures/<crawl>/<timestamp>-<path>.html with a
manifest (url, timestamp, crawl, capture_url in the index.commoncrawl.org form).
A record that does not answer is listed as FAILED in the manifest, never skipped silently.
Six workers (the data host's guidance is below 10 small requests per second).
Adapted from the Northzone run (PRO-105).
Usage: python3 cc-fetch.py <regex on the path>"""
import gzip, json, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "index-ventures"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
pat = re.compile(sys.argv[1])
RAW.mkdir(parents=True, exist_ok=True)
man = json.loads(MAN.read_text()) if MAN.exists() else {}
idx = json.loads(IDX.read_text())


def entry(cid, r, nbytes):
    return {"status": "ok", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid, "bytes": nbytes,
            "digest": r.get("digest"),
            "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}


def one(job):
    cid, r, key = job
    dest = RAW / key
    gz = Path(str(dest) + ".gz")
    if gz.exists() or (dest.exists() and dest.stat().st_size > 0):
        return key, entry(cid, r, (gz if gz.exists() else dest).stat().st_size)
    a, ln = int(r["offset"]), int(r["length"])
    for attempt in range(3):
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a+ln-1}",
                            f"https://data.commoncrawl.org/{r['filename']}"], capture_output=True)
        try:
            rec = gzip.decompress(p.stdout)
            if rec.startswith(b"WARC/"):
                head, _, rest = rec.partition(b"\r\n\r\n")
                http, _, body = rest.partition(b"\r\n\r\n")
            else:                      # ARC (the 2008-2012 crawls): one header line, then the HTTP response
                head, _, body = rec.partition(b"\r\n\r\n")
                if not body:
                    head, _, body = rec.partition(b"\n\n")
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes(body)
            return key, entry(cid, r, len(body))
        except Exception:
            time.sleep(2 + 3 * attempt)
    return key, {"status": "FAILED", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid}


jobs = []
for cid, v in sorted(idx.items()):
    if not isinstance(v, dict):
        continue
    for r in v.get("records", []):
        path = re.sub(r"https?://(www\.)?indexventures\.com(:80|:443)?", "", r["url"], flags=re.I)
        if not pat.search(path) or "html" not in (r.get("mime") or "html"):
            continue
        key = f"{cid}/{r['timestamp']}-{re.sub(r'[^A-Za-z0-9._-]+', '_', path.strip('/'))[:150] or 'root'}.html"
        if man.get(key, {}).get("status") == "ok":
            continue
        jobs.append((cid, r, key))
print(len(jobs), "to fetch", flush=True)
n = 0
with ThreadPoolExecutor(6) as ex:
    for key, e in ex.map(one, jobs):
        man[key] = e
        n += 1
        if n % 500 == 0:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(n, flush=True)
write_atomic(MAN, json.dumps(man, indent=1) + "\n")
print(n, "done;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total")
