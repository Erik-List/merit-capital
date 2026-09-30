#!/usr/bin/env python3
"""Targeted Internet Archive pass for visionaries.vc (the firm's own eras only).

Common Crawl carried the WordPress era (2023-2025) but not the Gatsby era:
its HTML shell is empty and the portfolio rides in
/page-data/index/page-data.json and the page-component JS bundle, which only
the Internet Archive captured. This pass asks the CDX once per namespace,
keeps captures from 2020 on (the domain was a Toastmasters club before), one
per distinct digest, and fetches them through scripts/ia_fetch.py (paced and
status-aware, machine-wide cooldown respected). A fetch that fails is logged,
never written as an empty capture.

Writes sources/wayback/raw/{page-data,portfolio,team,js,sitemap}/<ts>.<ext> and
sources/wayback/raw/ia-pass.json (what was asked, what answered).
Usage: python3 ia-pass.py
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "sources" / "wayback" / "raw"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import ia_fetch  # noqa: E402
from paths import write_atomic  # noqa: E402

# Order matters: the IA blocked this machine twice on 2026-09-30 after a few
# requests, so the one layer no other source holds (the Gatsby page component,
# which hard-codes the 2020-2022 portfolio: page-data.json carries no query
# data, staticQueryHashes is empty) goes first. The WordPress /portfolio/
# captures are also in Common Crawl and come last.
QUERIES = [
    ("js", "visionaries.vc/component---src-pages", "prefix"),
    ("sitemap", "visionaries.vc/portfolio-sitemap.xml", "exact"),
    ("page-data", "visionaries.vc/page-data/", "prefix"),
    ("team", "visionaries.vc/team", "prefix"),
    ("portfolio", "visionaries.vc/portfolio", "prefix"),
]


def main() -> None:
    log = {"queries": [], "fetched": []}
    for kind, url, mt in QUERIES:
        q = (f"https://web.archive.org/cdx/search/cdx?url={url}&matchType={mt}&output=json"
             f"&fl=timestamp,original,statuscode,mimetype,digest&from=2020&filter=statuscode:200")
        body, code = ia_fetch.get(q)
        entry = {"kind": kind, "url": url, "code": code}
        if code != "200":
            entry["error"] = "cdx failed"
            log["queries"].append(entry)
            print(kind, url, "CDX FAILED", code, flush=True)
            continue
        rows = json.loads(body)[1:] if body.strip() else []
        entry["captures"] = len(rows)
        log["queries"].append(entry)
        seen = set()
        (RAW / kind).mkdir(parents=True, exist_ok=True)
        for ts, orig, st, mime, dig in rows:
            if (orig.split("?")[0], dig) in seen:
                continue
            seen.add((orig.split("?")[0], dig))
            ext = "json" if orig.endswith(".json") else "js" if orig.endswith(".js") else \
                "xml" if orig.endswith(".xml") else "html"
            name = orig.split("visionaries.vc", 1)[1].strip("/").replace("/", "_") or "root"
            f = RAW / kind / f"{ts}-{name[:120]}.{ext}"
            if f.exists() and f.stat().st_size > 0:
                continue
            b, c = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
            rec = {"kind": kind, "ts": ts, "url": orig, "code": c, "bytes": len(b)}
            if c == "200" and b:
                f.write_bytes(b)
                rec["file"] = str(f.relative_to(RAW))
            log["fetched"].append(rec)
            print(kind, ts, orig[:100], c, len(b), flush=True)
        write_atomic(RAW / "ia-pass.json", json.dumps(log, indent=1) + "\n")
    write_atomic(RAW / "ia-pass.json", json.dumps(log, indent=1) + "\n")


if __name__ == "__main__":
    main()
