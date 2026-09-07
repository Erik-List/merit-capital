#!/usr/bin/env python3
"""Merge the pre-outage CDX dump into wayback-pull.py's parsed year files.

COLLECTION.md §5: "Parsed year files merge across capture universes (keyed
slug+path): the IA pull and the Common Crawl pull write the same per-year
shape from different capture sets, and each must survive the other's re-runs."
This is a third capture universe of the same kind -- the felicis.com CDX index
as it answered at 22:21 on 2026-09-06, minutes before web.archive.org started
refusing every connection.

The puller ran INTO that outage, so its per-era CDX queries were truncated: it
enumerated 343 distinct /companies/ slugs where the dump holds 461 at
statuscode 200. Rather than read that shortfall as portfolio history, the
missing slugs are merged back in from the dump, each dated by its own first
capture year, in exactly the shape the puller writes. Re-running the puller
after the archive recovers converges over this and is idempotent.

Only the three per-company-page eras are merged (`cdx_company_pages`); the
regex listing eras parse page BODIES, which a CDX index cannot supply.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

DUMP = "cdx-felicis.com-domain-20260906.txt"


def era_of(path: str) -> str:
    """The era prefix of a per-company path: /companies/plaid -> /companies/."""
    return path[:path.rfind("/") + 1] if "/" in path.strip("/") else path


def main() -> None:
    p = Paths("felicis")
    cfg = p.config()["wayback"]
    non_company = set(cfg["non_company_slugs"])
    eras = [e for e in cfg["eras"] if e["parser"] == "cdx_company_pages"]

    dump = (p.wayback / "raw" / DUMP).read_text(errors="replace").splitlines()
    # slug -> (path, earliest year) per era path
    found: dict[str, dict[str, int]] = defaultdict(dict)
    for line in dump:
        parts = line.split()
        if len(parts) < 3 or parts[2] != "200":
            continue
        ts, url = parts[0], parts[1].split("?")[0]
        year = int(ts[:4])
        for era in eras:
            path = era["path"]
            m = re.search(re.escape(path) + r"([^/?#]+)/?$", url)
            if not m:
                continue
            slug = m.group(1).lower().strip()
            if (not slug or slug in non_company or slug.startswith("page-")
                    or "." in slug or "%" in slug or len(slug) < 2):
                continue
            if not (era["from"] <= year <= era["to"]):
                continue
            prev = found[path].get(slug)
            found[path][slug] = year if prev is None else min(prev, year)

    parsed_dir = p.wayback / "parsed"
    existing: dict[int, list] = {}
    for f in sorted(parsed_dir.glob("[0-9][0-9][0-9][0-9].json")):
        existing[int(f.stem)] = json.loads(f.read_text())

    have = {(r["slug"], era_of(r.get("path", ""))) for rows in existing.values() for r in rows}
    added_by_year: dict[int, list] = defaultdict(list)
    for path, slugs in found.items():
        for slug, year in slugs.items():
            if (slug, path) in have:
                continue
            added_by_year[year].append({
                "slug": slug, "name": None, "path": f"{path}{slug}",
                "snapshot_ts": None, "source": "cdx-dump-20260906",
            })

    total = 0
    for year, rows in sorted(added_by_year.items()):
        merged = existing.get(year, []) + rows
        seen, out = set(), []
        for r in merged:
            k = (r["slug"], era_of(r.get("path", "")))
            if k in seen:
                continue
            seen.add(k)
            out.append(r)
        out.sort(key=lambda r: (r.get("path", ""), r["slug"]))
        write_atomic(parsed_dir / f"{year}.json", json.dumps(out, indent=1) + "\n")
        print(f"  {year}: +{len(rows)} from the dump -> {len(out)} rows")
        total += len(rows)

    print(f"\nmerged {total} company-page slugs the outage cost the puller")
    for path, slugs in sorted(found.items()):
        print(f"  {path}: {len(slugs)} distinct slugs in the dump")


if __name__ == "__main__":
    main()
