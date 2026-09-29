#!/usr/bin/env python3
"""Northzone's archived portfolio listings, 2003-2025, into
sources/wayback/parsed/<year>.json (the builder's wayback layer), one row per
company per year with the exact capture URL (`capture_url`), so every row cites
the capture it came from.

Six site generations (config.json wayback._eras_note). Each era below names
its listing URL(s) and a parser; captures are chosen from the CDX index, two
per year (first and second half), status 200 only, and every fetch goes
through scripts/ia_fetch via scratch/ia.py (machine-wide throttle and
cooldown). A failed fetch is recorded as failed in the manifest, never as an
empty year (COLLECTION.md §5).

Usage: python3 scratch/archive-listings.py [era ...]
"""
import html as H
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ia  # noqa: E402

ROOT = HERE.parent
PARSED = ROOT / "sources" / "wayback" / "parsed"
MANIFEST = ROOT / "sources" / "wayback" / "manifest.json"


def slug_of(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", H.unescape(name).lower()).strip("-")
    return s


def text_lines(h: str) -> list[str]:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S | re.I)
    return [H.unescape(x.strip()) for x in re.sub(r"<[^>]+>", "\n", t).split("\n") if x.strip()]


def captures(url: str, y0: int, y1: int, per_year: int = 2) -> list[tuple[str, str]]:
    """(timestamp, original) for up to `per_year` 200-status captures a year."""
    rows = ia.cdx(f"url={url}&output=json&fl=timestamp,original,statuscode,digest"
                  f"&from={y0}&to={y1}&limit=5000")
    by = defaultdict(list)
    for ts, orig, sc, dg in rows[1:]:
        if sc == "200":
            by[ts[:4]].append((ts, orig, dg))
    out = []
    for y, xs in sorted(by.items()):
        xs.sort()
        halves = [[x for x in xs if x[0][4:6] <= "06"], [x for x in xs if x[0][4:6] > "06"]]
        picked = [h[0] for h in halves if h][:per_year] or xs[:1]
        seen = set()
        for ts, orig, dg in picked:
            if dg in seen:
                continue
            seen.add(dg)
            out.append((ts, orig))
    return out


def add(rows_by_year, year, name, path, ts, orig, **extra):
    name = re.sub(r"\s+", " ", H.unescape(name)).strip()
    if not name:
        return
    rows_by_year[year].append(dict(
        name=name, slug=extra.pop("slug", None) or slug_of(name), path=path,
        snapshot_ts=ts, capture_url=f"https://web.archive.org/web/{ts}/{orig}",
        surface="wayback", **extra))


def write(rows_by_year, era):
    PARSED.mkdir(parents=True, exist_ok=True)
    for year, rows in rows_by_year.items():
        f = PARSED / f"{year}.json"
        cur = json.loads(f.read_text()) if f.exists() else []
        keep = {(r["slug"], r["path"]): r for r in cur}
        for r in rows:
            keep.setdefault((r["slug"], r["path"]), r)
        f.write_text(json.dumps(sorted(keep.values(), key=lambda r: (r["path"], r["slug"])),
                                indent=1, ensure_ascii=False) + "\n")
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    man[era] = {y: len(r) for y, r in sorted(rows_by_year.items())}
    MANIFEST.write_text(json.dumps(man, indent=1) + "\n")


ERAS = {}

if __name__ == "__main__":
    for era in (sys.argv[1:] or list(ERAS)):
        ERAS[era]()
