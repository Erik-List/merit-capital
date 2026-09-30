#!/usr/bin/env python3
"""Internet Archive pull for the project-a.com years Common Crawl does not hold.

Common Crawl carries the portfolio listing in 2013 and 2016-2024 (cc-manifest.json).
This fills 2012, 2014 and 2015 (listing pages) and the 2012-2014 per-company pages
(/portfolio/<slug>/, /en/portfolio/<slug>/), one capture per distinct page (HV
Capital write-back 4: one capture per page, not per year).

Probe first (HV Capital write-back 4): one CDX request; if it is refused the
script stops before any bulk traffic, so a still-active firewall block is not
escalated for every session on the machine.

Bodies -> sources/wayback/raw/ia/<ts>-<path>.html; manifest ->
sources/wayback/ia-manifest.json {key: {status, url, timestamp, capture_url}}.
A fetch that fails is recorded FAILED, never as an empty page.
Usage: python3 ia_pull.py [--listings-only]
"""
import json
import re
import sys
import urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

RAW = INV / "sources" / "wayback" / "raw" / "ia"
MAN = INV / "sources" / "wayback" / "ia-manifest.json"


def cdx(url, **kw):
    params = {"url": url, "output": "json", "fl": "timestamp,original,statuscode,digest"}
    params.update(kw)
    body, st = ia_fetch.get("https://web.archive.org/cdx/search/cdx?" + urllib.parse.urlencode(params))
    if not st.startswith("2"):
        return None, st
    rows = json.loads(body or b"[]")
    return rows[1:], st


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    rows, st = cdx("project-a.com/en/portfolio/", **{"from": "2012", "to": "2016"})
    if rows is None:
        sys.exit(f"probe refused ({st}); not starting the bulk pull")
    targets = []
    listing_rows = list(rows)
    for u in ("project-a.com/portfolio/", "project-a.com/de/portfolio/", "project-a.com/en/portfolio",
              "project-a.com/de/portfolio", "project-a.com/portfolio"):
        r, st = cdx(u, **{"from": "2012", "to": "2016"})
        if r is None:
            print("cdx failed", u, st)
            continue
        listing_rows += r
    per_year = {}
    for ts, orig, code, dig in listing_rows:
        if code != "200":
            continue
        y = ts[:4]
        if y in ("2013",) or y > "2016":
            continue  # Common Crawl holds 2013 and 2016 on
        key = (y, re.sub(r"^https?://(www\.)?", "", orig).rstrip("/"))
        per_year.setdefault(key, (ts, orig))
    targets += sorted(per_year.values())
    if "--listings-only" not in sys.argv:
        cdx_file = HERE / "cdx" / "project-a.com.tsv"
        seen = set()
        for line in cdx_file.read_text().splitlines():
            ts, orig, code = line.split("\t")
            p = re.sub(r"^https?://(www\.)?[^/]+(:\d+)?", "", orig).split("?")[0].rstrip("/").lower()
            m = re.fullmatch(r"(?:/en)?/portfolio/([^/.]+)", p)
            if m and code == "200" and ts[:4] <= "2015" and p not in seen:
                seen.add(p)
                targets.append((ts, orig))
    print(f"{len(targets)} captures to fetch")
    for ts, orig in targets:
        path = re.sub(r"^https?://(www\.)?[^/]+(:\d+)?", "", orig)
        key = f"{ts}-{re.sub(r'[^A-Za-z0-9._-]+', '_', path.strip('/')) or 'root'}.html"
        if man.get(key, {}).get("status") == "ok":
            continue
        url = f"https://web.archive.org/web/{ts}id_/{orig}"
        body, code = ia_fetch.get(url)
        if code == "rc7":
            print("firewall block; stopping")
            break
        if code != "200" or not body:
            man[key] = {"status": "FAILED", "code": code, "url": orig, "timestamp": ts}
            continue
        (RAW / key).write_bytes(body)
        man[key] = {"status": "ok", "url": orig, "timestamp": ts, "bytes": len(body),
                    "capture_url": f"https://web.archive.org/web/{ts}/{orig}"}
        write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    print(sum(1 for v in man.values() if v["status"] == "ok"), "ok;",
          sum(1 for v in man.values() if v["status"] != "ok"), "failed")


if __name__ == "__main__":
    main()
