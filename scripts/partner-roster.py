#!/usr/bin/env python3
"""Build the historical partner roster with tenure windows.

The modern /people/ listing pages are JS-rendered: the 2020 snapshot contains
only 16 of Sequoia's partners in its HTML (Pat Grady, a sitting partner, is
absent entirely). Rather than render JS, this enumerates every individual
/people/<slug> page from the Wayback **CDX index** — the archive's own URL
listing, which records each page that was ever captured regardless of how the
listing page rendered. Same technique that took era-A companies from 42 to 284.

Tenure comes from the span of archived snapshots per person. That is a proxy,
not an employment record: it under-reports people archived rarely and
over-reports the end date when a stale profile page lingers.

Output: data/aggregation/sources/wayback/partner-roster.json
  {slug, name, years_seen[], first_seen, last_seen, snapshots, sources[]}
"""
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data" / "aggregation" / "sources" / "wayback"
RAW = BASE / "raw"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"

# Non-person paths that live under /people/ or /us/
NOT_A_PERSON = {
    "index", "people", "team", "ethos", "growth", "specialists", "seed", "early",
    "venture", "scouts", "commons", "search", "jobs", "contact", "legal", "about",
    "news", "stories", "companies", "build", "login", "password",
}
# asset / artefact suffixes seen in the archive
ASSET_RE = re.compile(r"\.(gif|jpe?g|png|svg|css|js|ico)$|document\.|_ro$", re.I)


def curl(url: str) -> str:
    for attempt in range(3):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "90", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
        except subprocess.CalledProcessError:
            time.sleep(2 * (attempt + 1))
    return ""


def cdx_people() -> dict[str, list[str]]:
    """Every archived /people/<slug> page -> the years it was captured."""
    per: dict[str, list[str]] = defaultdict(list)
    for pattern in ("sequoiacap.com/people/*", "sequoiacap.com/us/team/*"):
        txt = curl(f"http://web.archive.org/cdx/search/cdx?url={pattern}"
                   f"&output=text&filter=statuscode:200&fl=original,timestamp&limit=20000")
        for line in txt.splitlines():
            parts = line.split()
            if len(parts) != 2:
                continue
            orig, ts = parts
            orig = orig.split("?")[0]                     # drop utm_/ref query strings
            m = re.search(r"/(?:people|team)/([a-z][a-z0-9-]*[a-z0-9])/?$", orig)
            if not m:
                continue
            slug = m.group(1)
            if slug in NOT_A_PERSON or ASSET_RE.search(slug) or "-" not in slug:
                continue                                  # require first-last shape
            per[slug].append(ts[:4])
        time.sleep(0.5)
    return per


def from_listing_pages() -> dict[str, list[str]]:
    """Names parsed from cached listing snapshots (reliable for 2006-2009)."""
    per: dict[str, list[str]] = defaultdict(list)
    for f in sorted(RAW.glob("*-people.html")):
        year = f.name[:4]
        html = f.read_text(encoding="utf-8", errors="replace")
        for slug in set(re.findall(r'/people/([a-z][a-z0-9-]*[a-z0-9])/?["\']', html)):
            if slug not in NOT_A_PERSON and "-" in slug:
                per[slug].append(year)
    return per


def main() -> None:
    print("== enumerating individual profile pages from the CDX index")
    cdx = cdx_people()
    print(f"   {len(cdx)} people slugs")

    print("== parsing cached listing snapshots")
    listing = from_listing_pages()
    print(f"   {len(listing)} people slugs")

    merged: dict[str, dict] = {}
    for src, batch in (("cdx-profile-page", cdx), ("listing-page", listing)):
        for slug, years in batch.items():
            e = merged.setdefault(slug, {"slug": slug, "years": set(), "sources": [],
                                         "snapshots": 0})
            e["years"].update(years)
            e["snapshots"] += len(years)
            if src not in e["sources"]:
                e["sources"].append(src)

    rows = []
    for slug, e in merged.items():
        years = sorted(int(y) for y in e["years"])
        rows.append({
            "slug": slug,
            "name": " ".join(w.capitalize() for w in slug.split("-")),
            "years_seen": years,
            "first_seen": years[0],
            "last_seen": years[-1],
            "snapshots": e["snapshots"],
            "sources": sorted(e["sources"]),
        })
    rows.sort(key=lambda r: r["slug"])
    (BASE / "partner-roster.json").write_text(json.dumps(rows, indent=1) + "\n")

    from collections import Counter
    span = Counter()
    for r in rows:
        span[r["last_seen"]] += 1
    print(f"\nwrote partner-roster.json — {len(rows)} people")
    print(f"  coverage: {min(r['first_seen'] for r in rows)}–{max(r['last_seen'] for r in rows)}")
    print(f"  last-seen distribution: {dict(sorted(span.items()))}")


if __name__ == "__main__":
    main()
