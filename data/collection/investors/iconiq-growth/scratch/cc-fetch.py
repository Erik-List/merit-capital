#!/usr/bin/env python3
"""Range-read the Common Crawl captures that scratch/cc-cluster.py indexed.

Reads scratch/cc-index-raw.json (every text/html 200 capture on iconiq.com,
iconiqcapital.com and iconiqgrowth.com, per crawl) and fetches, from
data.commoncrawl.org, each distinct (url, digest) whose URL is a page the
archive layer parses: the portfolio listings (iconiqgrowth.com/companies/,
iconiqcapital.com/growth/companies, iconiq.com/growth/companies), the growth
desk's per-company pages (iconiqgrowth.com/company/<slug>/), team and people
pages, and the growth posts ("updates", "ideas", root-level WordPress posts on
iconiqgrowth.com). iconiq.com captures before 2025 belong to an unrelated agency
that owned the domain ("our-work", "mind-melt") and are skipped.

Each body lands in scratch/cc-raw/<crawl>/<sha1(url|digest)[:16]>.html with a
.json sidecar (crawl, url, timestamp, digest, WARC filename/offset/length), so
a parsed row cites its capture exactly. One capture per URL per year is read (per URL for a post). A failed read is printed and retried on
the next run, never written as an empty page. Paced through shared_throttle
("ccdata").
Usage: python3 data/collection/investors/iconiq-growth/scratch/cc-fetch.py [--only REGEX]
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
    r"^https?://(www\.)?("
    r"iconiqgrowth\.com/(companies|company/|company-type/|team|people|about|our-team|approach|$|[a-z0-9-]{12,}/?$)"
    r"|iconiqcapital\.com/(growth|team|people|about|$)"
    r"|iconiq\.com/(growth|news|team|people))", re.I)


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
            if re.search(r"//(www\.)?iconiq\.com/", url) and r["timestamp"][:4] < "2025":
                continue  # the domain belonged to an unrelated agency before ICONIQ took it
            # one capture per URL per year: enough to date a listing and read its fields
            # (the same page recaptured in the next crawl carries a new digest for
            # trivial markup changes); posts are read once
            year = r["timestamp"][:4]
            is_post = not re.search(r"/(companies|company/|company-type/|growth/?$|growth/companies|team|people)", url)
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
        parts = rec.split(b"\r\n\r\n", 2)          # WARC headers, HTTP headers, body
        http_body = parts[2] if len(parts) == 3 else b""
        hdr = parts[1].decode("latin-1", "replace") if len(parts) > 1 else ""
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
