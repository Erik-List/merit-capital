#!/usr/bin/env python3
"""Common Crawl index records for EQT Ventures' own domains, while the Internet
Archive is under its machine-wide cooldown (COLLECTION.md s1: a Common Crawl
capture is a valid citation; s5: CC as the archive layer during an IA
cooldown). Adapted from the Balderton run's helper. Every query retries with
backoff and a failed crawl is recorded as FAILED, never as zero captures; a
404 is the index's "no captures in this crawl".

Output: ../sources/wayback/cc-index-raw.json  {domain: {crawl: {"status", "records"}}}
Usage: cc-index.py <domain> [crawl-id ...]   (default: every crawl 2016-2026)
"""
import json, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
DOMAIN = sys.argv[1]
coll = json.loads(subprocess.run(["curl", "-s", "--max-time", "60", "https://index.commoncrawl.org/collinfo.json"],
                                 capture_output=True, text=True).stdout)
ALL = [c["id"] for c in coll]
CRAWLS = sys.argv[2:] or [c for c in ALL if c[8:12].isdigit() and 2016 <= int(c[8:12]) <= 2026]

def query(cid):
    url = (f"https://index.commoncrawl.org/{cid}-index?url={DOMAIN}/*&matchType=domain"
           f"&output=json&fl=url,timestamp,status,mime,digest,filename,offset,length")
    for attempt in range(6):
        r = subprocess.run(["curl", "-s", "--max-time", "120", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
        if code == "404":
            return []
        if r.returncode == 0 and code == "200":
            try:
                return [json.loads(l) for l in body.splitlines() if l.startswith("{")]
            except ValueError:
                pass
        time.sleep(5 * (attempt + 1))
    return None

data = json.loads(OUT.read_text()) if OUT.exists() else {}
dom = data.setdefault(DOMAIN, {})
for cid in CRAWLS:
    if dom.get(cid, {}).get("status") == "ok":
        continue
    recs = query(cid)
    dom[cid] = {"status": "ok" if recs is not None else "failed", "records": recs or []}
    print(cid, dom[cid]["status"], len(dom[cid]["records"]), flush=True)
    write_atomic(OUT, json.dumps(data, indent=0))
    time.sleep(1.5)
