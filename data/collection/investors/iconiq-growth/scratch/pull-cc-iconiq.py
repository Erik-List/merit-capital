#!/usr/bin/env python3
"""Common Crawl captures of ICONIQ's three domains (iconiqgrowth.com, the growth
desk's own site; iconiqcapital.com, the parent's site; iconiq.com, since 2025):
the archive layer while the Internet Archive is in a machine-wide cooldown
(set 2026-09-28 22:38 UTC for eight hours by an earlier session's block).
Adapted from the Coatue run's puller (pull-cc-coatue.py).

Common Crawl was retired as a SWEEP layer in 2026-09 because it held nothing
the Internet Archive lacked; that is a finding about where we look, and a CC
capture stays a valid citation (COLLECTION.md 1). The Wayback pull runs later
in the run, not at the instant the cooldown ends (archive-availability rule),
and merges with these years.

Two passes, both resumable:
  index   every CC crawl since 2013 is asked for coatue.com/* (status 200); the
          answer, or the failure, is written per crawl under scratch/cc-index/.
          A failed query is recorded as failed and retried on the next run,
          never written as an empty crawl.
  fetch   each distinct (url, digest) on a page we parse is range-read from
          data.commoncrawl.org and its HTTP body cached under scratch/cc-raw/.

Paced through shared_throttle ("ccindex", "ccdata"; 1 request per second
each, the module's default for a service without its own rate).

Usage: python3 data/collection/investors/iconiq-growth/scratch/pull-cc-iconiq.py index|fetch [--only REGEX]
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

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
import shared_throttle  # noqa: E402

INV = ROOT / "data/collection/investors/iconiq-growth"
IDX = INV / "scratch/cc-index"
RAW = INV / "scratch/cc-raw"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
# one capture per URL per year is enough to date a listing and read its fields;
# every crawl re-captures the same page under a new digest
PER_YEAR = "--per-year" in sys.argv
ONCE = "--once" in sys.argv          # one capture per URL: enough for a post

# The pages worth reading: portfolio listings and company pages, people pages,
# the news archive (press releases name rounds), the history page.
KEEP = re.compile(r"(iconiqgrowth\.com|iconiqcapital\.com|iconiq\.com)(:80)?/(growth/?$|growth/(companies|portfolio|team|people|about|approach|news|insights)|portfolio|companies|team|people|our-team|news|insights|about|approach|press|$|index)", re.I)
HOSTS = ("iconiqgrowth.com/*", "www.iconiqgrowth.com/*", "iconiqcapital.com/*", "www.iconiqcapital.com/*",
         "iconiq.com/*", "www.iconiq.com/*")


def curl(args: list[str], service: str, tries: int = 5) -> tuple[bytes, str]:
    last = (b"", "rc-1")
    for attempt in range(tries):
        shared_throttle.wait(service)
        r = subprocess.run(["curl", "-sS", "--max-time", "90", "-A", UA, "-w", "\n%{http_code}"] + args,
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        code = code.decode() if r.returncode == 0 else f"rc{r.returncode}"
        if code in ("200", "206"):
            return body, code
        if code == "404":
            return body, code
        last = (body, code)
        time.sleep(min(60, 3 * 2 ** attempt))
    return last


def crawls() -> list[str]:
    body, code = curl(["https://index.commoncrawl.org/collinfo.json"], "ccindex")
    if code != "200":
        sys.exit(f"collinfo failed: {code}")
    ids = [c["id"] for c in json.loads(body)]
    return [i for i in ids if re.match(r"CC-MAIN-20(1[3-9]|2\d)-", i)]


def index_pass() -> None:
    IDX.mkdir(parents=True, exist_ok=True)
    years = re.compile(sys.argv[sys.argv.index("--years") + 1]) if "--years" in sys.argv else None
    todo = [c for c in crawls() if not (IDX / f"{c}.jsonl").exists()
            and (years is None or years.search(c))]
    print(f"{len(todo)} crawls to query")
    failed = []
    for cid in todo:
        rows = []
        page_fail = False
        for host in HOSTS:
            body, code = curl([f"https://index.commoncrawl.org/{cid}-index?url={host}&output=json&filter=status:200"],
                              "ccindex")
            if code == "404" and b"No Captures found" in body:
                continue
            if code != "200":
                page_fail = True
                break
            for line in body.decode("utf-8", "replace").splitlines():
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    page_fail = True
        if page_fail:
            failed.append(cid)
            (IDX / f"{cid}.failed").write_text(time.strftime("%Y-%m-%dT%H:%M:%S"))
            print(f"  {cid}: FAILED (retry on the next run)")
            continue
        (IDX / f"{cid}.failed").unlink(missing_ok=True)
        (IDX / f"{cid}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
        print(f"  {cid}: {len(rows)} captures")
    print(f"index pass done; {len(failed)} failed: {failed}")


def fetch_pass(only: str | None) -> None:
    sel = re.compile(only) if only else KEEP
    seen = set()
    todo = []
    for f in sorted(IDX.glob("*.jsonl")):
        for line in f.open():
            r = json.loads(line)
            url = r["url"]
            if not sel.search(url):
                continue
            key = (re.sub(r"^https?://(www\.)?", "", url).rstrip("/").lower(),
                   "" if ONCE else r["timestamp"][:4] if PER_YEAR else r.get("digest"))
            if key in seen:
                continue
            seen.add(key)
            todo.append((f.stem, r))
    print(f"{len(todo)} distinct captures to read")
    n = 0
    for cid, r in todo:
        name = hashlib.sha1(f"{r['url']}|{r['digest']}".encode()).hexdigest()[:16]
        out = RAW / cid / f"{name}.html"
        meta = RAW / cid / f"{name}.json"
        if out.exists():
            continue
        off, ln = int(r["offset"]), int(r["length"])
        body, code = curl(["-H", f"Range: bytes={off}-{off + ln - 1}",
                           f"https://data.commoncrawl.org/{r['filename']}"], "ccdata")
        if code not in ("200", "206"):
            print(f"  fetch failed {code}: {r['url']} {cid}")
            continue
        try:
            rec = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
        except OSError:
            print(f"  bad gzip: {r['url']} {cid}")
            continue
        # WARC headers, blank line, HTTP headers, blank line, body
        parts = rec.split(b"\r\n\r\n", 2)
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
                                    "offset": r["offset"], "length": r["length"],
                                    "mime": r.get("mime"), "status": r.get("status")}))
        n += 1
        if n % 50 == 0:
            print(f"  {n} read")
    print(f"fetch pass done: {n} new captures")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "index"
    only = sys.argv[sys.argv.index("--only") + 1] if "--only" in sys.argv else None
    index_pass() if mode == "index" else fetch_pass(only)
