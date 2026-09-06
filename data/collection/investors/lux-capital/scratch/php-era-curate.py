#!/usr/bin/env python3
"""Curate the 2005-2008 PHP-era portfolio into the wayback parsed years.

/portfolio.php renders each company as a table row whose logo is either
images/logo_<slug>.gif with the name in the alt text or images/LOGO_<NAME>.gif
with the name in a <span class="teamName style1"> anchor, so no single
listing_regex reaches every row (COLLECTION.md §5's era-parser rule: a logo-only
sub-era stays unparsed unless another surface brackets it -- here the same page
carries both). The era is six to eight companies wide, so it is curated the way
Spark's 2006 era was, and the page's own "Sector(s):" and "Location:" cells are
kept as entry-time evidence for the oldest rows in the base.

Writes sources/site/php-era-2005-2008.json and merges rows into
sources/wayback/parsed/<year>.json.
"""
import json
import re
import sys
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

SLUG = re.compile(r"[^a-z0-9]+")


def slugify(name: str) -> str:
    n = re.sub(r"\b(inc|llc|corp|corporation|ltd|co)\b\.?", "", name.lower())
    return SLUG.sub("-", n).strip("-")


def parse(html: str) -> list[dict]:
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    rows, order = {}, []
    # Every company row carries a logo image; the name comes from its alt text
    # or from the teamName anchor that follows it.
    for m in re.finditer(r'images/(?:logo|LOGO)_([A-Za-z0-9_]+)\.gif"'
                         r'(?:[^>]*?alt="([^"]*)")?', text):
        raw_slug, alt = m.group(1), m.group(2) or ""
        # The row's own anchor text owns the name: LOGO_ACCELERGY.gif carries
        # alt="Angstrom Publishing - Nanotechnology" (the site's own copy-paste
        # error), and trusting the alt drops Accelergy from the era entirely.
        tail = text[m.end():m.end() + 1200]
        # the class varies across rows (teamName style1 / style4 / style4
        # style5) and nests a second span on some, so match loosely
        t = re.search(r'class="teamName[^"]*"[^>]*>\s*(?:<span[^>]*>\s*)?'
                      r'(?:<a[^>]*>)?\s*([^<]{2,60}?)\s*(?:</a>|</span>)', tail)
        name = unescape(t.group(1)).strip() if t else ""
        if not name and alt:
            name = re.split(r"\s+-\s+", unescape(alt))[0].strip()
        if not name:
            name = raw_slug.replace("_", " ").title()
        slug = slugify(name)
        # the paragraph after the row carries Sector(s) and Location cells
        seg = text[m.end():m.end() + 3000]
        sec = re.search(r'Sector\(s\):</strong>.*?<td class="teamTitle">([^<]*)</td>', seg, re.S)
        loc = re.search(r'Location:</strong>.*?<td class="teamTitle">([^<]*)</td>', seg, re.S)
        desc = re.search(r'<td class="teamBio"[^>]*>(.*?)</td>', seg, re.S)
        if slug in rows:
            continue
        rows[slug] = {
            "slug": slug, "name": name,
            "sector_site": unescape(sec.group(1)).strip() if sec else None,
            "location_site": unescape(loc.group(1)).strip() if loc else None,
            "description": re.sub(r"\s+", " ", unescape(
                re.sub(r"<[^>]+>", " ", desc.group(1)))).strip()[:900] if desc else None,
        }
        order.append(slug)
    return [rows[s] for s in order]


def main():
    p = Paths("lux-capital")
    raw = p.wayback / "raw"
    parsed = p.wayback / "parsed"
    all_rows, per_year = {}, {}
    for year in (2005, 2006, 2007, 2008):
        f = raw / f"{year}-portfolio.php.html"
        if not f.exists():
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        ts = json.loads((raw / "portfolio.php.snapshots.json").read_text())[str(year)][0]
        rows = parse(html)
        per_year[year] = rows
        for r in rows:
            all_rows.setdefault(r["slug"], {**r, "years": []})["years"].append(year)
        print(f"  {year}: {len(rows)} companies -> {[r['name'] for r in rows]}")
        dest = parsed / f"{year}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for r in rows:
            merged.setdefault((r["slug"], "/portfolio.php"),
                              {"slug": r["slug"], "name": r["name"],
                               "path": "/portfolio.php", "snapshot_ts": ts})
        write_atomic(dest, json.dumps(sorted(merged.values(),
                     key=lambda r: (r["slug"], r.get("path") or "")), indent=1))
    write_atomic(p.site / "php-era-2005-2008.json",
                 json.dumps({"_readme": "luxcapital.com /portfolio.php captures 2005-2008, "
                             "curated by scratch/php-era-curate.py; carries the site's own "
                             "sector, location and description per company",
                             "rows": sorted(all_rows.values(),
                                                     key=lambda r: r["slug"])}, indent=1))
    print(f"php era: {len(all_rows)} distinct companies")


if __name__ == "__main__":
    main()
