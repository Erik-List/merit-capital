#!/usr/bin/env python3
"""Parse the Common Crawl captures of ICONIQ's growth portfolio (scratch/cc-raw,
written by cc-fetch.py) into the archive layer's year files,
sources/wayback/parsed/<year>.json, in wayback-pull.py's row shape plus the
capture that cites the row (COLLECTION.md 1: a Common Crawl capture is a valid
citation). One row per company per year per surface, from the earliest capture
of that surface in the year. Four page shapes, one per site generation:

  A. iconiqgrowth.com/companies/ (WordPress, 2020-11 to 2022-01): a logo grid.
     Each entry is <div class="company-wrap <category>"><a href="<company URL>">
     <img src=".../<Name>_color.png">. The name is read from the firm's own
     upload filename (COLLECTION.md 5: a logo-only era is readable through the
     firm's own filenames), then replaced by the firm's own rendering where the
     same company URL or slug appears on a later surface that renders names.
  B. iconiqgrowth.com/company/<slug>/ (WordPress, 2022): one page per holding,
     the name in <h1>. The page's date is the CMS post date (the site's build,
     "September 4, 2020" on most), not an investment date, and is not read.
  C. iconiqcapital.com/growth/companies (Next.js on DatoCMS, 2022-08 to
     2024-02): __NEXT_DATA__ carries the whole grid (info_grid.gridItems): name,
     slug, region, sector, a third label, description, company URL.
  D. iconiqcapital.com/growth/companies and iconiq.com/growth/companies
     (Webflow, 2024-07 on): the grid pull-site-iconiq.py reads live.

Merges with what wayback-pull.py writes for the same years (rows keyed
slug+path), so the Wayback pull can land later and add years.
Usage: python3 data/collection/investors/iconiq-growth/scratch/parse-cc-iconiq.py
"""
from __future__ import annotations

import html as H
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

INV = ROOT / "data/collection/investors/iconiq-growth"
RAW = HERE / "cc-raw"
OUT = INV / "sources/wayback/parsed"
sys.path.insert(0, str(HERE))
from importlib import import_module  # noqa: E402
parse_grid = import_module("pull-site-iconiq").parse_grid  # the live Webflow grid parser


def slug_of(n: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")


def dom(u: str) -> str:
    try:
        h = urlparse(u if "//" in u else "https://" + u).netloc.lower()
    except ValueError:
        return ""
    return re.sub(r"^(www\d?|m)\.", "", h)


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def name_from_file(fn: str) -> str:
    stem = re.sub(r"\.(png|jpe?g|svg|gif|webp)$", "", fn, flags=re.I)
    stem = re.sub(r"(?i)[-_ ]?(colou?r|logo|greyscale|grey|black|white|new|final|\d+x\d+)([-_ ]?\d+)?$", "", stem)
    stem = re.sub(r"(?i)[-_ ]?(colou?r|logo)$", "", stem)
    stem = re.sub(r"[-_]+", " ", stem).strip()
    return stem


# Upload filenames that do not read as the company's name (COLLECTION.md 5: filename
# variants are fixed in the parsed source, not by an identity merge that would keep
# the junk rendering on the surviving row).
FILE_NAME_FIXES = {"Reprise-edited-v5.png": "Reprise"}


def parse_grid_any(h: str) -> list[dict]:
    """Both Webflow generations of the grid: the live one (class 'is-new', name in an
    h3 carrying fs-list-field="name") and the 2024-07 to 2026-01 one (no 'is-new',
    name in an h2 'heading-style-h3 is-companies', tags in fs-cmsfilter-field
    "category", the exit tag among them)."""
    rows = parse_grid(h)
    if rows:
        return rows
    out = []
    for it in re.split(r'class="companies-list_grid-item w-dyn-item"', h)[1:]:
        name = re.search(r'class="heading-style-h3 is-companies[^"]*"[^>]*>(.*?)</h[23]>', it, re.S)
        if not name:
            continue
        url = re.search(r'<a href="([^"]+)" target="_blank" class="companies-list_grid-item-reveal-wrap', it)
        cats = [clean(c) for c in re.findall(r'fs-cmsfilter-field="category"[^>]*>([^<]*)<', it)]
        cats = [c for c in cats if c and c != "All"]
        out.append({"name": clean(name.group(1)), "company_site": url.group(1) if url else "",
                    "categories": [c for c in cats if c != "IPO/Acquired"], "exit_site": "IPO/Acquired" in cats})
    return out


def cite(m: dict) -> str:
    return f"https://index.commoncrawl.org/{m['crawl']}-index?url={m['url']}&output=json"


def surface_of(url: str) -> str | None:
    u = url.lower()
    if re.search(r"iconiqgrowth\.com/companies/?$", u):
        return "A"
    if re.search(r"iconiqgrowth\.com/company/[^/]+/?$", u):
        return "B"
    if re.search(r"(iconiqcapital|iconiq)\.com/growth/companies(\?[0-9a-f]+_page=\d+)?$", u):
        return "CD"
    return None


def main() -> None:
    caps = []
    for meta_p in sorted(RAW.glob("*/*.json")):
        m = json.loads(meta_p.read_text())
        s = surface_of(m["url"])
        if s:
            caps.append((s, m, meta_p.with_suffix(".html")))
    # earliest capture per (year, url)
    best: dict[tuple, tuple] = {}
    for s, m, p in caps:
        k = (m["timestamp"][:4], m["url"].split("#")[0])
        if k not in best or m["timestamp"] < best[k][1]["timestamp"]:
            best[k] = (s, m, p)
    rows_by_year: dict[str, dict] = {}
    names_by_domain: dict[str, str] = {}
    names_by_slug: dict[str, str] = {}
    pending_a = []
    for (y, url), (s, m, p) in sorted(best.items()):
        h = p.read_text("utf-8", "replace")
        out = []
        if s == "A":
            for mm in re.finditer(r'<div class="company-wrap ([^"]*)"><a[^>]*href="([^"]+)"[^>]*><img[^>]*src="([^"]+)"', h):
                cat, href, src = mm.groups()
                pending_a.append((y, m, cat, href, src.rsplit("/", 1)[-1]))
            continue
        if s == "B":
            n = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
            if not n:
                continue
            name = clean(n.group(1))
            site_slug = re.search(r"/company/([^/]+)/?$", m["url"]).group(1)
            names_by_slug[site_slug] = name
            out.append({"name": name, "site_slug": site_slug, "path": "/company/" + site_slug + "/",
                        "surface": "cc:iconiqgrowth.com/company"})
        if s == "CD":
            nd = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
            if nd:
                d = json.loads(nd.group(1))
                content = d["props"]["pageProps"]["data"]["page"]["content"]
                grid = [b for b in content if b.get("_modelApiKey") == "info_grid"]
                for it in (grid[0]["gridItems"] if grid else []):
                    if not isinstance(it, list) or not it or not it[0]:
                        continue
                    name, site_slug = it[0], it[1]
                    region, sector, label, desc, cu = (it + [None] * 9)[4:9]
                    out.append({"name": name, "site_slug": site_slug, "path": "/growth/companies",
                                "surface": "cc:iconiqcapital.com/growth/companies", "region": region,
                                "sector": sector, "label": label, "company_site": cu})
                    if cu:
                        names_by_domain.setdefault(dom(cu), name)
            else:
                for r in parse_grid_any(h):
                    out.append({"name": r["name"], "path": "/growth/companies",
                                "surface": "cc:" + re.sub(r"^https?://(www\.)?", "", m["url"]).split("?")[0],
                                "categories": r["categories"], "exit_site": r["exit_site"],
                                "company_site": r["company_site"]})
                    if r["company_site"]:
                        names_by_domain.setdefault(dom(r["company_site"]), r["name"])
        yr = rows_by_year.setdefault(y, {})
        for r in out:
            slug = slug_of(r["name"])
            if not slug:
                continue
            r.update({"slug": slug, "snapshot_ts": m["timestamp"], "capture_url": cite(m)})
            yr.setdefault((slug, r["path"]), r)
    # the live grid names every company it still lists, by its own URL
    live = json.loads((INV / "sources/site/portfolio-2026.json").read_text())["rows"]
    for r in live:
        if r.get("company_site"):
            names_by_domain.setdefault(dom(r["company_site"]), r["name"])
    for y, m, cat, href, fn in pending_a:
        d = dom(href)
        name = names_by_domain.get(d) or FILE_NAME_FIXES.get(fn) or name_from_file(fn)
        slug = slug_of(name)
        rows_by_year.setdefault(y, {}).setdefault((slug, "/companies/"), {
            "slug": slug, "name": name, "path": "/companies/", "surface": "cc:iconiqgrowth.com/companies",
            "snapshot_ts": m["timestamp"], "capture_url": cite(m), "company_site": href, "category": cat,
            "logo_file": fn, "name_from": "later rendering (same company URL)" if d in names_by_domain else "logo filename"})
    OUT.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(rows_by_year.items()):
        p = OUT / f"{y}.json"
        existing = json.loads(p.read_text()) if p.exists() else []
        keyed = {(r["slug"], r["path"]): r for r in existing}
        for k, r in rows.items():
            keyed[k] = r
        merged = sorted(keyed.values(), key=lambda r: (r["path"], r["slug"]))
        write_atomic(p, json.dumps(merged, indent=1, ensure_ascii=False) + "\n")
        per = {}
        for r in merged:
            per[r["surface"]] = per.get(r["surface"], 0) + 1
        print(f"{y}: {len({r['slug'] for r in merged})} companies {per}")


if __name__ == "__main__":
    main()
