#!/usr/bin/env python3
"""Build the historical partner roster with tenure windows.

Modern /people/ listing pages are JS-rendered and under-report the team, so
this enumerates every individual profile page from the Wayback **CDX index** —
the archive's own URL listing, which records each page that was ever captured
regardless of how the listing page rendered.

Tenure comes from the span of archived snapshots per person. That is a proxy,
not an employment record: it under-reports people archived rarely and
over-reports the end date when a stale profile page lingers.

The CDX patterns, the profile-slug regex and the non-person slug list live in
the investor's config.json under "roster".

Output: <investor>/sources/wayback/partner-roster.json
  {slug, name, years_seen[], first_seen, last_seen, snapshots, sources[]}

Usage: python3 scripts/partner-roster.py <investor-slug>
"""
import argparse
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic  # noqa: E402
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"

# asset / artefact suffixes seen in the archive
ASSET_RE = re.compile(r"\.(gif|jpe?g|png|svg|css|js|ico)$|document\.|_ro$", re.I)


def curl(url: str) -> str:
    for attempt in range(3):
        shared_throttle.wait("ia")
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "90", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
        except subprocess.CalledProcessError:
            time.sleep(2 * (attempt + 1))
    return ""


def cdx_people(cfg: dict) -> dict[str, list[str]]:
    """Every archived profile page -> the years it was captured."""
    slug_re = re.compile(cfg["slug_re"])
    not_a_person = set(cfg["not_a_person"])
    per: dict[str, list[str]] = defaultdict(list)
    for pattern in cfg["cdx_patterns"]:
        txt = curl(f"https://web.archive.org/cdx/search/cdx?url={pattern}"
                   f"&output=text&filter=statuscode:200&fl=original,timestamp&limit=20000")
        for line in txt.splitlines():
            parts = line.split()
            if len(parts) != 2:
                continue
            orig, ts = parts
            orig = orig.split("?")[0]                     # drop utm_/ref query strings
            m = slug_re.search(orig)
            if not m:
                continue
            slug = m.group(1)
            if slug in not_a_person or ASSET_RE.search(slug) or "-" not in slug:
                continue                                  # require first-last shape
            per[slug].append(ts[:4])
        time.sleep(0.5)
    return per


def from_listing_pages(cfg: dict, raw_dir: Path) -> dict[str, list[str]]:
    """Names parsed from cached listing snapshots (reliable for the early eras)."""
    href_re = re.compile(cfg["listing_href_re"])
    not_a_person = set(cfg["not_a_person"])
    per: dict[str, list[str]] = defaultdict(list)
    for f in sorted(raw_dir.glob("*-people.html")):
        year = f.name[:4]
        html = f.read_text(encoding="utf-8", errors="replace")
        for slug in set(href_re.findall(html)):
            if slug not in not_a_person and "-" in slug:
                per[slug].append(year)
    return per


def site_team_rows(p: Paths) -> list[dict]:
    """team.json rows with a usable slug (taken verbatim, or derived from
    the profile URL when the collector left it null).

    The roster exists to attribute Form D related persons — people who sit
    on issuer boards for the firm — so when the site team carries a group
    taxonomy, config's roster.site_team_groups keeps only board-relevant
    groups (a16z: 469 of 572 current staff are operations/marketing/HR,
    whose homonyms only add sweep noise, never attributions)."""
    site_team = p.site / "team.json"
    if not site_team.exists():
        return []
    keep_groups = set(p.config()["roster"].get("site_team_groups") or [])
    rows = []
    for r in json.load(open(site_team)):
        if keep_groups and r.get("group") and r["group"] not in keep_groups:
            continue
        slug = r.get("slug")
        if not slug and r.get("url"):
            slug = r["url"].rstrip("/").rsplit("/", 1)[-1]
        if slug and r.get("name"):
            rows.append({**r, "slug": slug})
    return rows


def from_site_team(p: Paths) -> dict[str, list[str]]:
    """The site CMS team roster (site-portfolio.py's team.json), as
    current-year evidence: the one source that cleanly separates the team
    from mere content authors when the two share a URL namespace."""
    from datetime import date
    y = str(date.today().year)
    return {r["slug"]: [y] for r in site_team_rows(p)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    cfg = p.config()["roster"]

    print("== enumerating individual profile pages from the CDX index")
    cdx = cdx_people(cfg)
    print(f"   {len(cdx)} people slugs")

    print("== parsing cached listing snapshots")
    listing = from_listing_pages(cfg, p.wayback / "raw")
    print(f"   {len(listing)} people slugs")

    print("== site CMS team roster (current)")
    site = from_site_team(p)
    print(f"   {len(site)} people slugs")

    site_names = {r["slug"]: r["name"] for r in site_team_rows(p)}

    merged: dict[str, dict] = {}
    for src, batch in (("cdx-profile-page", cdx), ("listing-page", listing),
                       ("site-team", site)):
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
            "name": site_names.get(slug) or " ".join(
                w.capitalize() for w in slug.split("-")),
            "years_seen": years,
            "first_seen": years[0],
            "last_seen": years[-1],
            "snapshots": e["snapshots"],
            "sources": sorted(e["sources"]),
        })
    rows.sort(key=lambda r: r["slug"])
    p.wayback.mkdir(parents=True, exist_ok=True)
    write_atomic(p.wayback / "partner-roster.json", json.dumps(rows, indent=1) + "\n")

    from collections import Counter
    span = Counter()
    for r in rows:
        span[r["last_seen"]] += 1
    print(f"\nwrote partner-roster.json — {len(rows)} people")
    print(f"  coverage: {min(r['first_seen'] for r in rows)}–{max(r['last_seen'] for r in rows)}")
    print(f"  last-seen distribution: {dict(sorted(span.items()))}")


if __name__ == "__main__":
    main()
