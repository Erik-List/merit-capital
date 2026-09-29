#!/usr/bin/env python3
"""Range-read the Common Crawl captures that scratch/cc-cluster.py indexed.

Reads scratch/cc-index-raw.json (every text/html 200 capture on tcv.com, per
crawl) and fetches, from data.commoncrawl.org, each distinct (url, digest) whose
URL is a page the archive layer parses (PRO-169; adapted from ICONIQ's
cc-fetch.py): the compliance list /all-companies, the 2017-2023 /companies/ grid,
the 2013-2016 /portfolio/ grid, the 2024-2026 /partnerships grid, team pages
(/team/<slug>, /teams/<slug>) and news posts (/news/<slug> and the 2013-2019
root-level press releases).

Each body lands in scratch/cc-raw/<crawl>/<sha1(url|digest)[:16]>.html with a
.json sidecar (crawl, url, timestamp, digest, WARC filename/offset/length), so
a parsed row cites its capture exactly. One capture per URL per year is read (per URL for a post). A failed read is printed and retried on
the next run, never written as an empty page. Paced through shared_throttle
("ccdata").
Usage: python3 data/collection/investors/tcv/scratch/cc-fetch.py [--only REGEX]
"""
from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_throttle  # noqa: E402

IDX = HERE / "cc-index-raw.json"
RAW = HERE / "cc-raw"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
KEEP = re.compile(
    r"^https?://(www\.)?tcv\.com(:\d+)?/("
    r"all-companies/?$|companies/?$|portfolio/?$|partnerships/?$|team/?$|teams/?$"
    r"|portfolio/(index|all-portfolio)\.php4|team/index\.php4|portfolio/alphabetical\.html|companies/[a-z]+\.html"
    r"|teams?/[a-z0-9-]+/?$|news/[a-z0-9-]{12,}/?$|[a-z0-9-]{25,}/?$)", re.I)


def curl(args: list[str], tries: int = 5) -> tuple[bytes, str]:
    last = (b"", "rc-1")
    for attempt in range(tries):
        shared_throttle.wait("ccdata")
        r = subprocess.run(["curl", "-sS", "--max-time", "90", "-A", UA, "-w", "\n%{http_code}"] + args,
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        code = code.decode() if r.returncode == 0 else f"rc{r.returncode}"
        if code in ("200", "206"):
            return body, code
        last = (body, code)
        time.sleep(min(60, 3 * 2 ** attempt))
    return last


def main() -> None:
    only = re.compile(sys.argv[sys.argv.index("--only") + 1]) if "--only" in sys.argv else None
    data = json.loads(IDX.read_text())
    seen, todo = set(), []
    for cid, v in sorted(data.items()):
        for r in v.get("records", []):
            url = r["url"]
            if not KEEP.search(url) or (only and not only.search(url)):
                continue
            # one capture per URL per year: enough to date a listing and read its fields
            # (the same page recaptured in the next crawl carries a new digest for
            # trivial markup changes); posts are read once
            year = r["timestamp"][:4]
            is_post = not re.search(r"/(all-companies|companies/?$|portfolio/?$|partnerships/?$|teams?/?$|portfolio/(index|all-portfolio)\.php4|team/index\.php4|portfolio/alphabetical|companies/[a-z]+\.html)", url)
            key = (re.sub(r"^https?://(www\.)?", "", url).rstrip("/").lower(), "" if is_post else year)
            if key in seen:
                continue
            seen.add(key)
            todo.append((cid, r))
    print(f"{len(todo)} distinct captures to read", flush=True)
    n = fails = 0
    for cid, r in todo:
        name = hashlib.sha1(f"{r['url']}|{r['digest']}".encode()).hexdigest()[:16]
        out, meta = RAW / cid / f"{name}.html", RAW / cid / f"{name}.json"
        if out.exists():
            continue
        off, ln = int(r["offset"]), int(r["length"])
        body, code = curl(["-H", f"Range: bytes={off}-{off + ln - 1}", f"https://data.commoncrawl.org/{r['filename']}"])
        if code not in ("200", "206"):
            print(f"  fetch failed {code}: {r['url']} {cid}", flush=True)
            fails += 1
            continue
        try:
            rec = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
        except OSError:
            print(f"  bad gzip: {r['url']} {cid}", flush=True)
            fails += 1
            continue
        if rec.startswith(b"WARC/"):
            parts = rec.split(b"\r\n\r\n", 2)      # WARC headers, HTTP headers, body
            http_body = parts[2] if len(parts) == 3 else b""
            hdr = parts[1].decode("latin-1", "replace") if len(parts) > 1 else ""
        else:
            # ARC record (the 2008-2012 crawls): one ARC header line, then the HTTP response
            resp = rec.split(b"\n", 1)[1] if b"\n" in rec else b""
            hp = resp.split(b"\r\n\r\n", 1)
            hdr = hp[0].decode("latin-1", "replace")
            http_body = hp[1] if len(hp) == 2 else b""
        if re.search(r"(?im)^content-encoding:\s*gzip", hdr):
            try:
                http_body = gzip.decompress(http_body)
            except OSError:
                pass
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(http_body)
        meta.write_text(json.dumps({"crawl": cid, "url": r["url"], "timestamp": r["timestamp"],
                                    "digest": r.get("digest"), "filename": r["filename"],
                                    "offset": r["offset"], "length": r["length"]}))
        n += 1
        if n % 50 == 0:
            print(f"  {n} read", flush=True)
    print(f"done: {n} new captures, {fails} failed (retry on the next run)", flush=True)


if __name__ == "__main__":
    main()
