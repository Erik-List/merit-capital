#!/usr/bin/env python3
"""Fetch Common Crawl captures of EQT Ventures' own surfaces by WARC range
request (data.commoncrawl.org), from the records in
sources/wayback/cc-index-raw.json. Adapted from the Balderton run's helper.
Raw bodies land in data/filings/commoncrawl/eqt-ventures/<crawl>/ (gitignored)
with a tracked manifest (url, timestamp, crawl, digest, capture_url in the
index.commoncrawl.org form, COLLECTION.md s1). A record that does not answer is
FAILED in the manifest, never skipped silently. Only status-200 HTML records.

Usage: cc-fetch.py <domain> <regex on host+path>
"""
import gzip, json, re, subprocess, sys, time
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "eqt-ventures"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
DOMAIN, pat = sys.argv[1], re.compile(sys.argv[2])
RAW.mkdir(parents=True, exist_ok=True)
man = json.loads(MAN.read_text()) if MAN.exists() else {}
idx = json.loads(IDX.read_text())[DOMAIN]
n = 0
for cid, v in sorted(idx.items()):
    for r in v.get("records", []):
        hp = re.sub(r"^https?://(www\.)?", "", r["url"])
        if r.get("status") != "200" or not pat.search(hp) or "html" not in (r.get("mime") or "html"):
            continue
        key = f"{cid}/{r['timestamp']}-{re.sub(r'[^A-Za-z0-9._-]+', '_', hp.strip('/'))[:180]}.html"
        if man.get(key, {}).get("status") == "ok":
            continue
        a, ln = int(r["offset"]), int(r["length"])
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a+ln-1}",
                            f"https://data.commoncrawl.org/{r['filename']}"], capture_output=True)
        time.sleep(0.2)
        try:
            rec = gzip.decompress(p.stdout)
            head, _, rest = rec.partition(b"\r\n\r\n")
            http, _, body = rest.partition(b"\r\n\r\n")
            if b"content-encoding: gzip" in http.lower():
                try: body = gzip.decompress(body)
                except Exception: pass
        except Exception:
            man[key] = {"status": "FAILED", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid}
            continue
        (RAW / cid).mkdir(exist_ok=True)
        (RAW / key).write_bytes(body)
        man[key] = {"status": "ok", "url": r["url"], "timestamp": r["timestamp"], "crawl": cid, "bytes": len(body),
                    "digest": r.get("digest"),
                    "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json"}
        n += 1
        if n % 50 == 0:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n"); print(n, flush=True)
write_atomic(MAN, json.dumps(man, indent=1) + "\n")
print(n, "fetched;", sum(1 for x in man.values() if x["status"] != "ok"), "failed in manifest;", len(man), "total")
