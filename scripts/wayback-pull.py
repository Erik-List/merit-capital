#!/usr/bin/env python3
"""Pull annual Wayback snapshots of Sequoia's portfolio pages (2006-2026)
and parse them into per-year company lists.

Eras:
  A 2006-2009  /company/<slug>   (paginated listing)
  B 2010-2014  /us/<slug>        (via /sitemap + homepage scroller)
  C 2015-2021  /companies/       (single page, _name divs + data-filters)
  D 2021-2026  /our-companies/   (JS-era page)

Raw HTML -> data/aggregation/sources/wayback/raw/
Parsed   -> data/aggregation/sources/wayback/parsed/<year>.json
            rows: {slug, name?, path, filters?, snapshot_ts}
"""
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "data" / "aggregation" / "sources" / "wayback"
RAW = BASE / "raw"
PARSED = BASE / "parsed"
UA = {"User-Agent": "MeritCapitalResearch/1.0 (erik@meritcapit.al)"}

# Non-company /us/ and /company/ paths to exclude (sector/nav/people handled separately)
NON_COMPANY = {
    "news", "contact", "about", "team", "people", "jobs", "legal", "sitemap",
    "map", "ideas", "early", "seed", "venture", "growth", "energy", "financial",
    "healthcare", "internet", "mobile", "outsourcing", "advertising", "software",
    "hardware", "services", "technology", "search",
    # further era-B (2010-2014) category/navigation pages under /us/
    "fund", "funds", "companies", "company", "portfolio", "index", "home",
    "stories", "story", "press", "events", "careers", "privacy", "terms",
    "systems", "consumer", "enterprise", "infrastructure", "crypto",
}


def curl(url: str) -> bytes:
    for attempt in range(3):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "90", "-H", f"User-Agent: {UA['User-Agent']}", url],
                capture_output=True, check=True).stdout
        except subprocess.CalledProcessError as e:
            print(f"    retry {attempt+1} {url}: rc={e.returncode}", file=sys.stderr, flush=True)
            time.sleep(3)
    return b""


def fetch(url: str, dest: Path) -> str:
    if dest.exists():
        return dest.read_text(encoding="utf-8", errors="replace")
    html = curl(url).decode("utf-8", errors="replace")
    if html:
        dest.write_text(html, encoding="utf-8")
        time.sleep(1.0)
    return html


def cdx(url_pattern: str, **params) -> list[list[str]]:
    qs = "&".join([f"url={url_pattern}", "output=json", "filter=statuscode:200",
                   *[f"{k}={v}" for k, v in params.items()]])
    data = json.loads(curl(f"http://web.archive.org/cdx/search/cdx?{qs}") or b"[]")
    return data[1:] if data else []


def wb(ts: str, original: str) -> str:
    return f"http://web.archive.org/web/{ts}/{original}"


def yearly(rows, y0, y1):
    """Pick one snapshot per year (first available)."""
    out = {}
    for row in rows:
        ts, orig = row[0], row[1]
        y = int(ts[:4])
        if y0 <= y <= y1 and y not in out:
            out[y] = (ts, orig)
    return out


def era_a():  # 2006-2009 /company/<slug> pages, enumerated straight from the CDX index
    print("== Era A: /company/ 2006-2009")
    rows = cdx("sequoiacap.com/company/*", collapse="urlkey",
               fl="timestamp,original", to="2009", limit="2000")
    results = {}
    for ts, orig in [(r[0], r[1]) for r in rows]:
        m = re.search(r"/company/([a-z0-9_-]+)/?(?:\?|$)", orig)
        if not m:
            continue
        slug = m.group(1)
        if slug in NON_COMPANY:
            continue
        y = int(ts[:4])
        results.setdefault(y, {})[slug] = {
            "slug": slug, "path": f"/company/{slug}", "snapshot_ts": ts}
    out = {}
    for y, comps in sorted(results.items()):
        out[y] = sorted(comps.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(comps)} companies (from CDX index)")
    return out


def era_b():  # 2010-2014 /us/ via sitemap + homepage
    print("== Era B: /us/ 2010-2014")
    site_snaps = yearly(cdx("sequoiacap.com/sitemap", collapse="timestamp:4",
                            fl="timestamp,original"), 2010, 2014)
    home_snaps = yearly(cdx("sequoiacap.com", collapse="timestamp:4",
                            fl="timestamp,original"), 2010, 2014)
    results, people = {}, {}
    for y in range(2010, 2015):
        found = {}
        for src, snaps in (("sitemap", site_snaps), ("home", home_snaps)):
            if y not in snaps:
                continue
            ts, orig = snaps[y]
            html = fetch(wb(ts, orig), RAW / f"{y}-{src}.html")
            # The old CMS rendered sector/category pages with an un-interpolated
            # Ruby object in the alt text ('#<Region:0x..> Gaming'), while company
            # links carry the clean name ('Mixpanel'). That distinguishes the two
            # exactly, and hands us a display name for era B at the same time.
            linked = re.findall(r'href="[^"]*?/us/([a-z0-9_-]+)/?"\s+alt="([^"]*)"', html)
            for slug, alt in linked:
                if "#<" in alt or slug in NON_COMPANY:
                    continue
                found[slug] = {"slug": slug, "name": unescape(alt).strip() or None,
                               "path": f"/us/{slug}", "snapshot_ts": ts}
            if not linked:      # snapshots without alt attributes
                for slug in re.findall(r'href="[^"]*?/us/([a-z0-9_-]+)/?"', html):
                    if slug not in NON_COMPANY:
                        found.setdefault(slug, {"slug": slug, "path": f"/us/{slug}",
                                                "snapshot_ts": ts})
        if found:
            results[y] = sorted(found.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(found)} /us/ paths (companies+people mixed)")
    return results


def era_c():  # 2015-2021 /companies/
    print("== Era C: /companies/ 2015-2021")
    snaps = yearly(cdx("sequoiacap.com/companies", collapse="timestamp:4",
                       fl="timestamp,original"), 2015, 2021)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), RAW / f"{y}-companies.html")
        blocks = re.findall(
            r'data-filters="([^"]*)"[^>]*data-id="([^"]+)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)
        if not blocks:  # attribute order variant
            blocks = [(f, i, n) for i, f, n in re.findall(
                r'data-id="([^"]+)"[^>]*data-filters="([^"]*)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)]
        rows = {}
        for filt, cid, name in blocks:
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            rows[slug] = {"slug": slug, "name": name, "path": f"/companies/{cid}",
                          "filters": filt, "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(rows)} companies")
    return results


def era_d():  # 2021-2026 /our-companies/
    print("== Era D: /our-companies/ 2021-2026")
    snaps = yearly(cdx("sequoiacap.com/our-companies", collapse="timestamp:4",
                       fl="timestamp,original"), 2021, 2026)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), RAW / f"{y}-our-companies.html")
        rows = {}
        for name in re.findall(
                r'class="company-listing-card__company-name">\s*([^<\t\n]+)', html):
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            if slug:
                rows[slug] = {"slug": slug, "name": name, "path": "/our-companies/",
                              "snapshot_ts": ts}
        time.sleep(2.0)
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
    return results


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    PARSED.mkdir(parents=True, exist_ok=True)
    all_years = {}
    for era in (era_a, era_b, era_c, era_d):
        for y, rows in era().items():
            all_years.setdefault(y, []).extend(rows)
    for y, rows in sorted(all_years.items()):
        (PARSED / f"{y}.json").write_text(json.dumps(rows, indent=1) + "\n")
    total = {r["slug"] for rows in all_years.values() for r in rows}
    print(f"\nyears: {sorted(all_years)}\ndistinct slugs across all years: {len(total)}")


if __name__ == "__main__":
    main()
