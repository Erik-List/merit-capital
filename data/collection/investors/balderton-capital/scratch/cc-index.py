#!/usr/bin/env python3
"""Common Crawl index records for balderton.com, while the Internet Archive is
under its machine-wide cooldown (COLLECTION.md s1: a Common Crawl capture is a
valid citation; s5 IVP precedent: CC as the archive layer). The index answers
intermittently (empty replies), so every query retries with backoff and a
failed crawl is recorded as FAILED, never as zero captures.

Output: ../sources/wayback/cc-index-raw.json  {crawl: {"status": ok|failed, "records": [...]}}
"""
import json, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
OUT = HERE.parent / "sources" / "wayback" / "cc-index-raw.json"
CRAWLS = ["CC-MAIN-2013-20", "CC-MAIN-2013-48", "CC-MAIN-2014-52", "CC-MAIN-2015-48", "CC-MAIN-2016-50",
          "CC-MAIN-2017-51", "CC-MAIN-2018-51", "CC-MAIN-2019-51", "CC-MAIN-2020-50", "CC-MAIN-2021-49",
          "CC-MAIN-2022-49", "CC-MAIN-2023-50", "CC-MAIN-2024-51"]
EXTRA = sys.argv[1:]          # further crawl ids on the command line

def query(cid: str):
    url = (f"https://index.commoncrawl.org/{cid}-index?url=balderton.com/*&matchType=domain"
           f"&output=json&fl=url,timestamp,status,mime,digest,filename,offset,length")
    for attempt in range(6):
        r = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.decode("utf-8", "replace").rpartition("\n")
        if r.returncode == 0 and code == "200":
            rows = []
            for line in body.splitlines():
                if line.startswith("{"):
                    try:
                        rows.append(json.loads(line))
                    except ValueError:
                        rows = None
                        break
            if rows is not None:
                return rows
        if code == "404":            # the index's way of saying "no captures in this crawl"
            return []
        time.sleep(6 * (attempt + 1))
    return None

data = json.loads(OUT.read_text()) if OUT.exists() else {}
for cid in CRAWLS + EXTRA:
    if data.get(cid, {}).get("status") == "ok":
        continue
    rows = query(cid)
    if rows is None:
        data[cid] = {"status": "failed", "records": []}
        print(cid, "FAILED (index did not answer)")
    else:
        ok = [x for x in rows if x.get("status") == "200"]
        data[cid] = {"status": "ok", "records": ok}
        print(cid, len(ok), "captures")
    write_atomic(OUT, json.dumps(data, indent=1) + "\n")
    time.sleep(2)
