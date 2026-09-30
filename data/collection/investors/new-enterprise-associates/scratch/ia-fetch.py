#!/usr/bin/env python3
"""Fetch chosen Internet Archive captures of nea.com (from scratch/ia-cdx.json) through scripts/ia_fetch.py (the
machine-wide throttle and firewall cooldown), into data/filings/wayback/new-enterprise-associates/ and the manifest
sources/wayback/ia-manifest.json (the cc-manifest.json entry shape, capture_url in web.archive.org form).

Usage: python3 ia-fetch.py "<url regex>" [--per-year N] [--from YYYY] [--to YYYY]
  --per-year N   keep at most N captures per distinct URL per year (default 1: the first of the year)
The id_ flag fetches the raw capture without the archive's toolbar.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

CDX = HERE / "ia-cdx.json"
RAW = ROOT / "data" / "filings" / "wayback" / "new-enterprise-associates"
MAN = HERE.parent / "sources" / "wayback" / "ia-manifest.json"
DOM = re.compile(r"^https?://(www\.)?nea\.com(:\d+)?", re.I)


def path_of(url):
    return DOM.sub("", url).split("#")[0] or "/"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern")
    ap.add_argument("--per-year", type=int, default=1)
    ap.add_argument("--from", dest="fy", default="1990")
    ap.add_argument("--to", dest="ty", default="2013")
    a = ap.parse_args()
    pat = re.compile(a.pattern, re.I)
    cdx = json.loads(CDX.read_text())["urls"]
    man = json.loads(MAN.read_text()) if MAN.exists() else {}
    have_dg = {v.get("digest") for v in man.values() if v.get("status") == "ok"}
    todo = []
    for url, caps in cdx.items():
        p = path_of(url)
        if not pat.search(p):
            continue
        by_year = {}
        for ts, dg in sorted(caps):
            y = ts[:4]
            if not (a.fy <= y <= a.ty):
                continue
            by_year.setdefault(y, [])
            if len(by_year[y]) < a.per_year and dg not in have_dg:
                by_year[y].append((ts, dg))
                have_dg.add(dg)
        for y, lst in by_year.items():
            for ts, dg in lst:
                todo.append((url, ts, dg))
    print(len(todo), "captures to fetch", flush=True)
    RAW.mkdir(parents=True, exist_ok=True)
    n = 0
    for i, (url, ts, dg) in enumerate(sorted(todo, key=lambda t: t[1])):
        key = f"{ts}-{re.sub(r'[^A-Za-z0-9._-]+', '_', path_of(url).strip('/'))[:150] or 'root'}.html"
        if man.get(key, {}).get("status") == "ok":
            continue
        body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{url}", tries=3)
        if code != "200" or not body:
            man[key] = {"status": "FAILED", "code": code, "url": url, "timestamp": ts}
            if ia_fetch.blocked():
                print("IA firewall cooldown set; stopping", flush=True)
                break
        else:
            (RAW / key).write_bytes(body)
            man[key] = {"status": "ok", "url": url, "path": path_of(url), "timestamp": ts, "digest": dg,
                        "bytes": len(body), "capture_url": f"https://web.archive.org/web/{ts}/{url}"}
            n += 1
        if i % 20 == 19:
            write_atomic(MAN, json.dumps(man, indent=1) + "\n")
            print(i + 1, "done", flush=True)
    write_atomic(MAN, json.dumps(man, indent=1) + "\n")
    print(n, "fetched;", sum(1 for v in man.values() if v["status"] != "ok"), "failed in manifest;", len(man), "total")


if __name__ == "__main__":
    main()
