#!/usr/bin/env python3
"""Patiently fetch the listing captures wayback-pull.py could not get.

web.archive.org has been flapping all through this run: a CDX query or a
replay fetch answers, then the next connection is refused outright, for
minutes at a time (COLLECTION.md §5's outage pattern, third variant --
neither a clean CDX refusal nor a clean outage, but intermittent). The
puller's three retries per URL are sized for a healthy archive and give up
long before this clears, so the 2011, 2012 and 2013 listing years came back
empty while 2014-2019 landed.

Empty is not the same as absent, and the difference matters: those three
years are the whole /portfolio/ era before it settles down, and reading
their absence as "Felicis listed nothing" would silently drop the book.

So this retries just those years, for as long as it takes, on the shared
Internet Archive budget (scripts/shared_throttle.py, 1 rps machine-wide
across every sibling run), writing into wayback-pull.py's own
raw/<year>-portfolio.html shape so a later `wayback-pull.py felicis` parses
them with the era's configured pattern and converges. It fetches nothing
that is already on disk.

Usage:  fetch-missing-listing-years.py [--rounds N] [--years 2011,2012,2013]
"""
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths  # noqa: E402
import shared_throttle  # noqa: E402

UA = "merit-capital research (erik@meritcapit.al)"
# Hand-picked captures. The puller's own probe picks the capture NEAREST a
# year boundary, which for 2013 is 20130224045636 -- a 2.8KB skeleton that
# carries no <img> at all. The 2013 page only fills out later in the year, so
# the largest capture of the year is seeded here instead (COLLECTION.md §5:
# "a known capture timestamp can be seeded by hand when the probe's nearest
# capture is the wrong era").
SEEDS = {
    "2011": ["20111018084644/http://www.felicis.com/fund/portfolio/",
             "20110925061841/http://www.felicis.com/portfolio",
             "20111201000000/http://www.felicis.com/portfolio/"],
    "2012": ["20120125002607/http://www.felicis.com/portfolio",
             "20120601000000/http://www.felicis.com/portfolio/",
             "20121201000000/http://www.felicis.com/all-portfolio/"],
    "2013": ["20131230021033/http://www.felicis.com/portfolio/",
             "20131201000000/http://www.felicis.com/portfolio/",
             "20130307202728/http://www.felicis.com/all-portfolio/"],
}


def fetch(url: str) -> str | None:
    shared_throttle.wait("ia")
    r = subprocess.run(
        ["curl", "-sS", "-L", "--max-time", "75", "-A", UA, url],
        capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout:
        return None
    return r.stdout


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=40)
    ap.add_argument("--years", default="2011,2012,2013")
    args = ap.parse_args()

    p = Paths("felicis")
    raw = p.wayback / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    memo_path = raw / "portfolio.snapshots.json"
    want = [y for y in args.years.split(",") if y.strip()]

    for rnd in range(1, args.rounds + 1):
        todo = [y for y in want if not (raw / f"{y}-portfolio.html").exists()]
        if not todo:
            print("all requested years on disk")
            break
        print(f"== round {rnd}: still missing {todo}")
        for y in todo:
            for stamp in SEEDS.get(y, []):
                body = fetch(f"https://web.archive.org/web/{stamp.split('/')[0]}id_/"
                             + stamp.split("/", 1)[1])
                if not body or len(body) < 1500:
                    continue
                # A capture with no logo markup is the empty-skeleton case the
                # 2013 probe hit; keep looking rather than banking it.
                if "images/logos/" not in body and "logo-container" not in body:
                    print(f"   {y} {stamp.split('/')[0]}: {len(body)}B but no listing markup")
                    continue
                out = raw / f"{y}-portfolio.html"
                out.write_text(body)
                n = body.count("images/logos/")
                print(f"   {y}: WROTE {out.name} ({len(body)}B, {n} logo refs) "
                      f"from {stamp.split('/')[0]}")
                memo = json.loads(memo_path.read_text()) if memo_path.exists() else {}
                memo[y] = [stamp.split("/")[0], stamp.split("/", 1)[1]]
                memo_path.write_text(json.dumps(memo, indent=1))
                break
        if [y for y in want if not (raw / f"{y}-portfolio.html").exists()]:
            time.sleep(min(20 + rnd * 10, 120))

    got = [y for y in want if (raw / f"{y}-portfolio.html").exists()]
    print(f"\nlanded: {got}   still missing: {sorted(set(want) - set(got))}")


if __name__ == "__main__":
    main()
