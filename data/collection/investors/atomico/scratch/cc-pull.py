#!/usr/bin/env python3
"""Atomico's own pages from Common Crawl, while the Internet Archive is blocked.

The Internet Archive refused this machine twice on 2026-09-26 (a 1-hour then a
2-hour machine-wide cooldown), and atomico.com itself sits behind a Vercel bot
checkpoint. Common Crawl captured the same server-rendered Next.js pages
(each carrying the CMS record in __NEXT_DATA__) in 34 crawls from 2021-39 to
2026-04. A Common Crawl capture is a valid citation for a page the firm has
since moved (COLLECTION.md §1; retiring CC as a *sweep layer* did not change
what counts), cited as the index query for that crawl, the Cherry precedent.

For each URL under the requested prefixes the NEWEST 200 capture is fetched
as a WARC byte range from data.commoncrawl.org, the HTTP body saved raw beside
the archive captures (scratch/cms-raw, insights-raw, team-raw) under
<slug>-cc<timestamp>.html, and the citation recorded in <dir>/cc-captures.json.

Usage: python3 cc-pull.py [partners|insights|team ...]
"""
from __future__ import annotations

import gzip
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle  # noqa: E402
from paths import write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/"
           "7d8e9a00-bfd0-4e09-8d4e-1b30f898d60e/scratchpad/atomico/cc-index-records.json")
TARGETS = {"partners": ("atomico.com/partners/*", HERE / "cms-raw"),
           "insights": ("atomico.com/insights/*", HERE / "insights-raw"),
           "team": ("atomico.com/team/*", HERE / "team-raw")}


def records(pattern: str) -> list[dict]:
    """The index records measured at the start (scratchpad), or a fresh query."""
    if IDX.exists():
        return json.loads(IDX.read_text()).get(pattern, [])
    raise SystemExit("no index records; run the coverage measurement first")


def fetch(rec: dict) -> bytes:
    start = int(rec["offset"])
    end = start + int(rec["length"]) - 1
    shared_throttle.wait("ccdata", rate=4.0)
    r = subprocess.run(["curl", "-sS", "--max-time", "90", "-A", UA,
                        "-H", f"Range: bytes={start}-{end}",
                        f"https://data.commoncrawl.org/{rec['filename']}"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError(f"rc={r.returncode}")
    warc = gzip.decompress(r.stdout)
    # WARC headers, blank line, HTTP headers, blank line, body
    parts = warc.split(b"\r\n\r\n", 2)
    if len(parts) < 3:
        raise RuntimeError("short WARC record")
    head, body = parts[1], parts[2]
    if b"content-encoding: gzip" in head.lower():
        try:
            body = gzip.decompress(body)
        except OSError:
            pass
    return body


def main():
    which = sys.argv[1:] or list(TARGETS)
    for key in which:
        pattern, outdir = TARGETS[key]
        outdir.mkdir(parents=True, exist_ok=True)
        newest: dict[str, dict] = {}
        for rec in records(pattern):
            url = re.sub(r"[?#].*$", "", rec["url"]).rstrip("/")
            m = re.search(r"/(?:partners|insights|team)/([^/]+)$", url)
            if not m or m.group(1).startswith("--") or m.group(1) == "[slug]":
                continue
            slug = m.group(1).lower()
            if rec.get("mime", "text/html") not in ("text/html", "unk") and "html" not in rec.get("mime", ""):
                continue
            if slug not in newest or rec["timestamp"] > newest[slug]["timestamp"]:
                newest[slug] = rec
        cites_path = outdir / "cc-captures.json"
        cites = json.loads(cites_path.read_text()) if cites_path.exists() else {}
        ok = fail = 0
        for slug, rec in sorted(newest.items()):
            f = outdir / f"{slug}-cc{rec['timestamp']}.html"
            if not f.exists():
                try:
                    body = fetch(rec)
                except Exception as e:  # noqa: BLE001
                    print(f"  {slug}: {e}")
                    fail += 1
                    continue
                write_atomic(f, body.decode("utf-8", errors="replace"))
            cites[slug] = {"timestamp": rec["timestamp"], "crawl": rec["crawl"], "url": rec["url"],
                           "citation": f"https://index.commoncrawl.org/{rec['crawl']}-index?"
                                       f"url={re.sub(r'^https?://', '', rec['url'])}&output=json",
                           "file": f.name}
            ok += 1
        write_atomic(cites_path, json.dumps(cites, indent=1) + "\n")
        print(f"{key}: {ok} pages ({fail} failed) from {len(newest)} urls")


if __name__ == "__main__":
    main()
