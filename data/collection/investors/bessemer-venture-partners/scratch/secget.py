#!/usr/bin/env python3
"""Read an SEC document through the machine-wide SEC throttle, cached under scratch/sec-cache/, and print the
paragraphs that match a pattern (default: the firm's names). For triage agents: never call sec.gov with a bare curl.

Usage: python3 secget.py <sec url> [--grep REGEX] [--width N] [--max N]
"""
import argparse
import hashlib
import html
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import shared_throttle  # noqa: E402

CACHE = HERE / "sec-cache"
UA = "Merit Capital research erik@meritcapit.al"


def get(url):
    CACHE.mkdir(exist_ok=True)
    f = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if f.exists():
        return f.read_text()
    for attempt in range(4):
        shared_throttle.wait("sec")
        r = subprocess.run(["curl", "-sL", "-m", "90", "-H", f"User-Agent: {UA}", url], capture_output=True)
        bad = (b"Request Rate Threshold Exceeded", b"<Code>NoSuchKey</Code>", b"<Error><Code>")
        if r.returncode == 0 and r.stdout and not any(x in r.stdout for x in bad):
            t = r.stdout.decode("utf-8", "replace")
            t = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", " ", t)
            t = html.unescape(re.sub(r"<[^>]+>", " ", t))
            t = re.sub(r"[ \t\r\f\v]+", " ", t)
            f.write_text(t)
            return t
        time.sleep(2 * (attempt + 1))
    raise SystemExit(f"fetch failed: {url}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--grep", default=r"Bessemer|\bBVP\b|Bessec|Deer [IVX]+ & Co")
    ap.add_argument("--width", type=int, default=700)
    ap.add_argument("--max", type=int, default=6)
    a = ap.parse_args()
    t = get(a.url)
    n = 0
    for m in re.finditer(a.grep, t, re.I):
        s = max(0, m.start() - a.width // 2)
        print("...", re.sub(r"\s+", " ", t[s:s + a.width]), "...\n")
        n += 1
        if n >= a.max:
            break
    print(f"[{n} match(es) shown; document {len(t)} chars]")


if __name__ == "__main__":
    main()
