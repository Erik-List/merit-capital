#!/usr/bin/env python3
"""Fetch the Common Crawl captures of Ribbit's listing and team pages by WARC
range request (data.commoncrawl.org), from scratch/cc-index-raw.json
(cc-cluster.py), into sources/wayback/raw/<era>-<timestamp>.html, and register
each in sources/wayback/captures.json beside the Internet Archive captures, so
scratch/wayback-ribbit.py parses both the same way (Erik 2026-09-26: Common
Crawl is the archive layer while the IA cooldown is set; a Common Crawl
capture is a valid citation, COLLECTION.md s1). capture_url is the
index.commoncrawl.org form. A record that does not answer is listed as failed,
never skipped. Adapted from bain-capital-ventures/scratch/cc-fetch.py.

Usage: python3 scratch/cc-fetch.py
"""
import gzip
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
IDX = HERE / "cc-index-raw.json"
WB = HERE.parent / "sources" / "wayback"
RAW = WB / "raw"
CAPS = WB / "captures.json"
DOM = re.compile(r"https?://(www\.)?ribbitcap\.com(:\d+)?", re.I)
ERA_OF = [(re.compile(r"^/bets/?$"), "bets"), (re.compile(r"^/our-bets/?$"), "our-bets"),
          (re.compile(r"^/team/?$"), "team"), (re.compile(r"^/about/?$"), "about"),
          (re.compile(r"^/rebels/?$"), "rebels-page"),
          (re.compile(r"^/?$"), "home")]


def path_of(url: str) -> str:
    return DOM.sub("", url).split("?")[0] or "/"


def era_of(url: str, ts: str) -> str | None:
    p = path_of(url)
    for rx, era in ERA_OF:
        if rx.match(p):
            # the homepage carried the bets slider only until the 2015 redesign
            return None if era == "home" and ts[:4] > "2014" else era
    return None


def body_of(r: dict) -> bytes | None:
    a, ln = int(r["offset"]), int(r["length"])
    for attempt in range(3):
        p = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-r", f"{a}-{a + ln - 1}",
                            "-w", "\n%{http_code}", f"https://data.commoncrawl.org/{r['filename']}"],
                           capture_output=True)
        raw, _, code = p.stdout.rpartition(b"\n")
        time.sleep(0.2)
        if code == b"503":
            time.sleep(10)
            continue
        try:
            rec = gzip.decompress(raw)
        except Exception:  # noqa: BLE001
            time.sleep(2)
            continue
        _, _, rest = rec.partition(b"\r\n\r\n")      # WARC header
        _, _, body = rest.partition(b"\r\n\r\n")     # HTTP header
        return body
    return None


def main() -> None:
    idx = json.loads(IDX.read_text())
    caps = json.loads(CAPS.read_text())
    have = {(c["era"], c["ts"]) for c in caps["captures"]}
    got = failed = 0
    for cid, v in sorted(idx.items()):
        for r in v.get("records", []):
            era = era_of(r["url"], r["timestamp"])
            ts = r["timestamp"]
            if not era or (era, ts) in have:
                continue
            body = body_of(r)
            if not body:
                caps.setdefault("failed", []).append({"era": era, "ts": ts, "url": r["url"], "crawl": cid,
                                                      "error": "commoncrawl record did not answer"})
                failed += 1
                continue
            dest = RAW / f"{era}-{ts}.html"
            dest.write_bytes(body)
            caps["captures"].append({
                "era": era, "ts": ts, "original": r["url"], "crawl": cid, "source": "commoncrawl",
                "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(r['url'], safe='')}&output=json",
                "raw": str(dest.relative_to(HERE.parent))})
            have.add((era, ts))
            got += 1
    caps["captures"].sort(key=lambda c: (c["era"], c["ts"]))
    write_atomic(CAPS, json.dumps(caps, indent=1) + "\n")
    print(f"commoncrawl captures fetched: {got}, failed: {failed}")


if __name__ == "__main__":
    main()
