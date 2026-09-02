#!/usr/bin/env python3
"""Pull annual Wayback snapshots of an investor's portfolio pages and parse
them into per-year company lists.

Everything investor-specific — the domain, the era map (which path pattern the
site used in which years, and which parser understands that era's markup), and
the non-company slug list — lives in the investor's config.json under
"wayback". The parsers themselves are named strategies in code; an investor's
era entry picks one:

  cdx_company_pages   per-company pages enumerated straight from the CDX index
  sitemap_home_links  hrefs on archived sitemap + homepage snapshots
  companies_listing   single listing page, `_name` divs + data-filters
  company_cards       JS-era listing page, company-name card markup
  listing_regex       one listing page per year; era config carries the
                      markup regex (named groups name and/or slug)
  js_array_listing    listing page embedding a JSON array in a JS
                      assignment (era config: var, name_field)

Raw HTML -> <investor>/sources/wayback/raw/
Parsed   -> <investor>/sources/wayback/parsed/<year>.json
            rows: {slug, name?, path, filters?, snapshot_ts}

Usage: python3 scripts/wayback-pull.py <investor-slug>
"""
import argparse
import json
import re
import subprocess
import sys
import time
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths  # noqa: E402

UA = {"User-Agent": "MeritCapitalResearch/1.0 (erik@meritcapit.al)"}


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
    if not data:
        # Degraded-CDX fallback (observed in the 2026-08-29 IA outage): the
        # statuscode-filtered query times out while the unfiltered one
        # answers. Replay follows redirects, so the worst case of an
        # unfiltered pick is a snapshot that parses to zero rows.
        qs = "&".join([f"url={url_pattern}", "output=json",
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


def seg_of(era: dict) -> str:
    return era["path"].strip("/")


def cdx_company_pages(era, cfg, raw_dir):
    """Per-company pages enumerated straight from the CDX index."""
    seg = seg_of(era)
    non_company = set(cfg["non_company_slugs"])
    print(f"== era {era['path']} {era['from']}-{era['to']} (CDX index)")
    rows = cdx(f"{cfg['cdx_domain']}{era['path']}*", collapse="urlkey",
               fl="timestamp,original", to=str(era["to"]), limit="2000")
    results = {}
    for ts, orig in [(r[0], r[1]) for r in rows]:
        m = re.search(rf"/{seg}/([a-z0-9_-]+)/?(?:\?|$)", orig)
        if not m:
            continue
        slug = m.group(1)
        if slug in non_company:
            continue
        y = int(ts[:4])
        if not era["from"] <= y <= era["to"]:
            continue
        results.setdefault(y, {})[slug] = {
            "slug": slug, "path": f"/{seg}/{slug}", "snapshot_ts": ts}
    out = {}
    for y, comps in sorted(results.items()):
        out[y] = sorted(comps.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(comps)} companies (from CDX index)")
    return out


def sitemap_home_links(era, cfg, raw_dir):
    """Company hrefs on archived sitemap + homepage snapshots."""
    seg = seg_of(era)
    non_company = set(cfg["non_company_slugs"])
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (sitemap + home)")
    site_snaps = yearly(cdx(f"{cfg['cdx_domain']}/sitemap", collapse="timestamp:4",
                            fl="timestamp,original"), y0, y1)
    home_snaps = yearly(cdx(cfg["cdx_domain"], collapse="timestamp:4",
                            fl="timestamp,original"), y0, y1)
    results = {}
    for y in range(y0, y1 + 1):
        found = {}
        for src, snaps in (("sitemap", site_snaps), ("home", home_snaps)):
            if y not in snaps:
                continue
            ts, orig = snaps[y]
            html = fetch(wb(ts, orig), raw_dir / f"{y}-{src}.html")
            # Old CMSes render sector/category pages with an un-interpolated
            # template object in the alt text ('#<Region:0x..> Gaming'), while
            # company links carry the clean name ('Mixpanel'). That
            # distinguishes the two exactly, and hands us a display name too.
            linked = re.findall(
                rf'href="[^"]*?/{seg}/([a-z0-9_-]+)/?"\s+alt="([^"]*)"', html)
            for slug, alt in linked:
                if "#<" in alt or slug in non_company:
                    continue
                found[slug] = {"slug": slug, "name": unescape(alt).strip() or None,
                               "path": f"/{seg}/{slug}", "snapshot_ts": ts}
            if not linked:      # snapshots without alt attributes
                for slug in re.findall(rf'href="[^"]*?/{seg}/([a-z0-9_-]+)/?"', html):
                    if slug not in non_company:
                        found.setdefault(slug, {"slug": slug, "path": f"/{seg}/{slug}",
                                                "snapshot_ts": ts})
        if found:
            results[y] = sorted(found.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(found)} /{seg}/ paths (companies+people mixed)")
    return results


def companies_listing(era, cfg, raw_dir):
    """Single listing page: `_name` divs + data-filters attributes."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (listing page)")
    snaps = yearly(cdx(f"{cfg['cdx_domain']}/{seg}", collapse="timestamp:4",
                       fl="timestamp,original"), y0, y1)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), raw_dir / f"{y}-{seg}.html")
        blocks = re.findall(
            r'data-filters="([^"]*)"[^>]*data-id="([^"]+)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)
        if not blocks:  # attribute order variant
            blocks = [(f, i, n) for i, f, n in re.findall(
                r'data-id="([^"]+)"[^>]*data-filters="([^"]*)"[^>]*>\s*<div class="_name">([^<]+)</div>', html)]
        rows = {}
        for filt, cid, name in blocks:
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            rows[slug] = {"slug": slug, "name": name, "path": f"/{seg}/{cid}",
                          "filters": filt, "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
            print(f"  {y}: {len(rows)} companies")
    return results


def company_cards(era, cfg, raw_dir):
    """JS-era listing page: company-name card markup."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (card listing)")
    snaps = yearly(cdx(f"{cfg['cdx_domain']}/{seg}", collapse="timestamp:4",
                       fl="timestamp,original"), y0, y1)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), raw_dir / f"{y}-{seg}.html")
        rows = {}
        for name in re.findall(
                r'class="company-listing-card__company-name">\s*([^<\t\n]+)', html):
            name = unescape(name).strip()
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            if slug:
                rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                              "snapshot_ts": ts}
        time.sleep(2.0)
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
    return results


def listing_regex(era, cfg, raw_dir):
    """One listing page per year; companies via the era's own markup regex
    (named groups (?P<name>...) and/or (?P<slug>...)). Markup specifics stay
    in config, mirroring site-portfolio.py's regex_list."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    non_company = set(cfg["non_company_slugs"])
    print(f"== era {era['path']} {y0}-{y1} (regex listing)")
    snaps = yearly(cdx(f"{cfg['cdx_domain']}/{seg}", collapse="timestamp:4",
                       fl="timestamp,original"), y0, y1)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), raw_dir / f"{y}-{seg.replace('/', '-')}.html")
        rows = {}
        for m in re.finditer(era["pattern"], html):
            d = m.groupdict()
            name = unescape((d.get("name") or "")).replace("\xa0", " ").strip() or None
            slug = d.get("slug") or (
                re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") if name else "")
            if not slug or slug in non_company:
                continue
            rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                          "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
    return results


def extract_js_array(html: str, var: str):
    """The array assigned to `var`, via bracket matching (JSON-safe)."""
    m = re.search(re.escape(var) + r"\s*=\s*\[", html)
    if not m:
        return []
    start = m.end() - 1
    depth, i, instr, esc = 0, start, False, False
    while i < len(html):
        c = html[i]
        if instr:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                instr = False
        else:
            if c == '"':
                instr = True
            elif c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
                if depth == 0:
                    break
        i += 1
    try:
        return json.loads(html[start:i + 1])
    except json.JSONDecodeError:
        return []


def js_array_listing(era, cfg, raw_dir):
    """Listing page embedding the portfolio as a JSON array in a JS
    assignment (era config: var, name_field)."""
    seg = seg_of(era)
    y0, y1 = era["from"], era["to"]
    print(f"== era {era['path']} {y0}-{y1} (embedded JS array)")
    snaps = yearly(cdx(f"{cfg['cdx_domain']}/{seg}", collapse="timestamp:4",
                       fl="timestamp,original"), y0, y1)
    results = {}
    for y, (ts, orig) in sorted(snaps.items()):
        html = fetch(wb(ts, orig), raw_dir / f"{y}-{seg}.html")
        rows = {}
        for entry in extract_js_array(html, era["var"]):
            name = unescape(str(entry.get(era.get("name_field", "title")) or "")).strip()
            if not name:
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            if slug:
                rows[slug] = {"slug": slug, "name": name, "path": era["path"],
                              "snapshot_ts": ts}
        if rows:
            results[y] = sorted(rows.values(), key=lambda c: c["slug"])
        print(f"  {y}: {len(rows)} entries")
        time.sleep(1.0)
    return results


PARSERS = {
    "cdx_company_pages": cdx_company_pages,
    "sitemap_home_links": sitemap_home_links,
    "companies_listing": companies_listing,
    "company_cards": company_cards,
    "listing_regex": listing_regex,
    "js_array_listing": js_array_listing,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    args = ap.parse_args()

    p = Paths(args.investor)
    cfg = p.config()["wayback"]
    raw, parsed = p.wayback / "raw", p.wayback / "parsed"
    raw.mkdir(parents=True, exist_ok=True)
    parsed.mkdir(parents=True, exist_ok=True)

    all_years = {}
    for era in cfg["eras"]:
        # A firm that changed domains keeps one config: an era may carry its
        # own cdx_domain (Lightspeed: lightspeedvp.com 2000-2012, lsvp.com
        # after), falling back to the investor-level domain.
        era_cfg = {**cfg, "cdx_domain": era.get("cdx_domain", cfg["cdx_domain"])}
        for y, rows in PARSERS[era["parser"]](era, era_cfg, raw).items():
            all_years.setdefault(y, []).extend(rows)
    for y, rows in sorted(all_years.items()):
        # Merge with what the year file already holds rather than replacing:
        # the Common Crawl layer (commoncrawl-pull.py) writes the same
        # per-year shape from a different capture universe (per-company
        # pages vs listing snapshots), and each source must survive the
        # other's re-runs. Keyed by (slug, path); existing rows win.
        dest = parsed / f"{y}.json"
        merged = {(r["slug"], r.get("path")): r
                  for r in (json.loads(dest.read_text()) if dest.exists() else [])}
        for r in rows:
            merged.setdefault((r["slug"], r.get("path")), r)
        (parsed / f"{y}.json").write_text(json.dumps(
            sorted(merged.values(), key=lambda r: (r["slug"], r.get("path") or "")),
            indent=1) + "\n")
    total = {r["slug"] for rows in all_years.values() for r in rows}
    print(f"\nyears: {sorted(all_years)}\ndistinct slugs across all years: {len(total)}")


if __name__ == "__main__":
    main()
