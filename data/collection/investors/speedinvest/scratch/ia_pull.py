#!/usr/bin/env python3
"""Internet Archive pull for the speedinvest.com years Common Crawl does not hold
(adapted from Project A PRO-102).

Common Crawl crawled only the home page before 2017 (cc-manifest.json), and the
home page is not a list. This fills the 2012-2016 /portfolio/ listing (one
capture per year) and every per-company page of that era (/blog/portfolio/<slug>/,
/portfolio/<slug>/, /portfolio-item/<slug>/), one capture per distinct page, plus
the 2012-2016 /team/ page for the roster.

Probe first: one CDX request; if it is refused the script stops before any bulk
traffic. Everything goes through scripts/ia_fetch.py (the machine-wide IA bucket
and cooldown).

Bodies -> data/filings/wayback/speedinvest/<ts>-<path>.html (gitignored, re-fetchable);
manifest -> sources/wayback/ia-manifest.json {key: {status, url, timestamp, capture_url}}.
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

RAW = ROOT / "data" / "filings" / "wayback" / "speedinvest"
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
    if ia_fetch.blocked():
        sys.exit("Internet Archive cooldown still active on this machine; not starting")
    RAW.mkdir(parents=True, exist_ok=True)
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    rows, st = cdx("speedinvest.com/portfolio/", **{"from": "2011", "to": "2016"})
    if rows is None:
        sys.exit(f"probe refused ({st}); not starting the bulk pull")
    listing = list(rows)
    for u in ("speedinvest.com/portfolio", "speedinvest.com/team/", "speedinvest.com/team",
              "speedinvest.com/", "speedinvest.com/blog/portfolio/"):
        r, st = cdx(u, **{"from": "2011", "to": "2016"})
        if r is None:
            print("cdx failed", u, st)
            continue
        listing += r
    per_year = {}
    for ts, orig, code, dig in listing:
        if code != "200":
            continue
        key = (ts[:4], re.sub(r"^https?://(www\.)?", "", orig).rstrip("/"))
        per_year.setdefault(key, (ts, orig))
    targets = sorted(per_year.values())
    if "--listings-only" not in sys.argv:
        seen = set()
        for prefix in ("speedinvest.com/blog/portfolio/", "speedinvest.com/portfolio/", "speedinvest.com/portfolio-item/"):
            r, st = cdx(prefix, matchType="prefix", **{"from": "2011", "to": "2017"})
            if r is None:
                print("cdx failed", prefix, st)
                continue
            for ts, orig, code, dig in r:
                p = re.sub(r"^https?://(www\.)?[^/]+(:\d+)?", "", orig).split("?")[0].rstrip("/").lower()
                if code == "200" and re.fullmatch(r"/(?:blog/)?portfolio(?:-item)?/[^/.]+", p) and p not in seen:
                    seen.add(p)
                    targets.append((ts, orig))
    print(f"{len(targets)} captures to fetch", flush=True)
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
