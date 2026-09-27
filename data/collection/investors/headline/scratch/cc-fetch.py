#!/usr/bin/env python3
"""Fetch Common Crawl captures of one Headline domain (argv[1]) list surfaces by WARC range
request (data.commoncrawl.org), from the records in sources/wayback/cc-index-raw.json.
Raw bodies land in data/filings/commoncrawl/balderton-capital/<crawl>/<timestamp>-<path>.html with a
manifest (url, timestamp, crawl, capture_url in the index.commoncrawl.org form).
A record that does not answer is listed as FAILED in the manifest, never skipped silently.
Usage: python3 cc-fetch.py <domain> <regex on the path>"""
import gzip, json, re, subprocess, sys, time
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
DOM = sys.argv[1]
IDX = HERE.parent / "sources" / "wayback" / f"cc-index-{DOM}.json"
# Raw captures are re-downloadable from Common Crawl: they live under data/filings/ (gitignored);
# the manifest with each capture's URL and digest is tracked as sources/wayback/cc-manifest.json.
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "headline" / DOM
MAN = HERE.parent / "sources" / "wayback" / f"cc-manifest-{DOM}.json"
pat = re.compile(sys.argv[2])
RAW.mkdir(parents=True, exist_ok=True)
man = json.loads(MAN.read_text()) if MAN.exists() else {}
idx = json.loads(IDX.read_text())
n = 0
for cid, v in sorted(idx.items()):
    for r in v.get("records", []):
        path = re.sub(r"https?://(www\.)?" + re.escape(DOM), "", r["url"])
        if not pat.search(path) or "html" not in (r.get("mime") or "html"):
            continue
        key = f"{cid}/{r['timestamp']}-{re.sub(r'[^A-Za-z0-9._-]+', '_', path.strip('/')) or 'root'}.html"
        if man.get(key, {}).get("status") == "ok":
            continue
        a, ln = int(r["offset"]), int(r["length"])
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a+ln-1}",
                            f"https://data.commoncrawl.org/{r['filename']}"], capture_output=True)
        time.sleep(0.3)
        try:
            rec = gzip.decompress(p.stdout)
            if rec.startswith(b"WARC/"):
                head, _, rest = rec.partition(b"\r\n\r\n")
                http, _, body = rest.partition(b"\r\n\r\n")
            else:                      # ARC (the 2008-2012 crawls): one header line, then the HTTP response
                head, _, body = rec.partition(b"\r\n\r\n")
                if not body:
                    head, _, body = rec.partition(b"\n\n")
        except Exception:
            man[key] = {"status": "FAILED", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid}
            continue
        (RAW / cid).mkdir(exist_ok=True)
        (RAW / key).write_bytes(body)
        man[key] = {"status": "ok", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid, "bytes": len(body),
                    "digest": r.get("digest"),
                    "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}
        n += 1
write_atomic(MAN, json.dumps(man, indent=1) + "\n")
print(n, "fetched;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total")
