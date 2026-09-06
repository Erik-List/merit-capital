#!/usr/bin/env python3
"""Read the columns the 2007-2026 site eras publish out of the captures that
wayback-pull.py already stored, into one file_list source per era.

The wayback layer keeps only {slug, name, path, year} — enough for listing
years and survivorship. These eras publish far more, and it is classification
evidence: 2007-2012 a description, a location and a status; 2015-2020 the
firm's own sector and stage taxonomies, an active_state and THE DEAL
PARTNER's author slug per card; 2021-2026 data-filter name, sectors and stage.
Nothing here fetches: it re-reads sources/wayback/raw, so it is safe to re-run
after wayback-pull lands more years.

Usage: python3 scratch/build-late-eras.py
"""
import json
import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths, write_atomic     # noqa: E402
import parse_eras as PE                   # noqa: E402

P = Paths("redpoint-ventures")
RAW = P.wayback / "raw"


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def merge(store: dict, key: str, year: int, row: dict) -> None:
    cur = store.setdefault(key, {"listing_years": []})
    for k, v in row.items():
        if v and not cur.get(k):
            cur[k] = v
        elif isinstance(v, list) and v:
            cur[k] = sorted(set((cur.get(k) or []) + v))
    if year not in cur["listing_years"]:
        cur["listing_years"].append(year)
        cur["listing_years"].sort()


def era_2007_2012() -> dict:
    """The Current Investments table: alt-text name + description/location/status."""
    out: dict = {}
    for f in sorted(RAW.glob("*-portfolio-current-investments.html")):
        year = int(f.name[:4])
        html = f.read_text(errors="replace")
        sections = PE.split_sections(html) or {"current": html}
        body = sections.get("current") or html
        for r in PE.parse_rows(body):
            name = r["name_alt"] or r["name_text"]
            if not name:
                continue
            merge(out, slug_of(name), year, {
                "name": name, "slug": slug_of(name), "url": r["url"],
                "description": r["description"], "site_location": r["site_location"],
                "site_status": r["site_status"], "ticker": r["ticker"],
                "acquirer": r["acquirer"], "era": "2007-2012"})
    return out


def era_2015_2020() -> dict:
    """WordPress cards: the class list is the firm's own taxonomy plus the
    deal partner's author slug; iso-company-name is its rendering of the name."""
    out: dict = {}
    for f in sorted(RAW.glob("*-companies.html")):
        year = int(f.name[:4])
        html = f.read_text(errors="replace")
        for m in re.finditer(r'<article class="([^"]*rpv_companies[^"]*)"[^>]*'
                             r'iso-company-name="([^"]*)"(.*?)</article>', html, re.S):
            classes, name, body = m.group(1), unescape(m.group(2)).strip(), m.group(3)
            if not name:
                continue
            sectors = sorted({c.split("rpv_company_sectors-")[1]
                              for c in classes.split() if c.startswith("rpv_company_sectors-")})
            stages = sorted({c.split("rpv_company_stages-")[1]
                             for c in classes.split() if c.startswith("rpv_company_stages-")})
            state = sorted({c.split("rpv_company_active_state-")[1]
                            for c in classes.split() if c.startswith("rpv_company_active_state-")})
            # bare tokens that are neither a taxonomy class nor WP plumbing are
            # the sector shorthands and the deal partners' author slugs
            bare = [c for c in classes.split()
                    if not c.startswith(("rpv_", "post-", "type-", "status-", "has-", "hentry"))]
            partners = [b for b in bare if re.match(r"^[a-z]-[a-z-]+$|^[a-z]+-[a-z-]+$", b)
                        and b not in set(sectors) | set(stages) | set(state)]
            url = ""
            mu = re.search(r'<a href="(https?://[^"]+)"', body)
            if mu:
                url = mu.group(1)
            merge(out, slug_of(name), year, {
                "name": name, "slug": slug_of(name), "url": url,
                "sectors": sectors, "site_stage": stages[0] if stages else "",
                "site_active_state": state[0] if state else "",
                "partners": partners, "era": "2015-2020"})
    return out


def era_2021_2026() -> dict:
    """Gatsby cards: data-filter-name / -sectors / -stage."""
    out: dict = {}
    for f in sorted(RAW.glob("*-companies.html")):
        year = int(f.name[:4])
        html = f.read_text(errors="replace")
        for m in re.finditer(r'data-filter-sectors="([^"]*)"\s+data-filter-stage="([^"]*)"'
                             r'\s+data-filter-name="([^"]*)"', html):
            sectors = [s.strip() for s in unescape(m.group(1)).split(",") if s.strip()]
            stage, name = unescape(m.group(2)).strip(), unescape(m.group(3)).strip()
            if not name:
                continue
            merge(out, slug_of(name), year, {
                "name": name, "slug": slug_of(name), "sectors": sectors,
                "site_stage": stage, "era": "2021-2026"})
    return out


README = ("Built by scratch/build-late-eras.py out of sources/wayback/raw, with no "
          "network access: the columns each site era published beyond the name the "
          "wayback layer keeps. 2007-2012 is the Current Investments table (description, "
          "location, status, ticker, acquirer). 2015-2020 is the WordPress card grid, "
          "whose <article> class list carries the firm's own sector and stage taxonomies, "
          "an active_state and the deal partner's author slug (the same slugs as "
          "/author/<slug>, so they join to the roster). 2021-2026 is the Gatsby grid's "
          "data-filter attributes. Every stage field here is the FIRM'S OWN LABEL and is "
          "scored on the golden set before it is trusted (COLLECTION.md 4).")

for fname, fn in [("companies-2007-2012.json", era_2007_2012),
                  ("companies-2015-2020.json", era_2015_2020),
                  ("companies-2021-2026.json", era_2021_2026)]:
    rows = sorted(fn().values(), key=lambda r: r.get("slug") or r.get("name", ""))
    write_atomic(P.site / fname, json.dumps({"_readme": README, "rows": rows}, indent=1) + "\n")
    print(f"{fname}: {len(rows)} rows")
