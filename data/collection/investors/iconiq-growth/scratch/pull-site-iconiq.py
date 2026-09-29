#!/usr/bin/env python3
"""ICONIQ Growth's own site, read into sources/site/ (COLLECTION.md 5, layer 1b).

iconiq.com is a Webflow site (site id 65d0d38fc4ec8ce8a8921654; CMS assets on
65e1d7fb19a3e64b5c36fb38). The growth portfolio is the server-rendered grid at
/growth/companies: 100 CMS items per page, paged by the Webflow list parameter
`?03ce0375_page=N` (2 pages, 172 companies on 2026-09-28). Each item carries the
company name (fs-list-field="name"), a one-line description, the company's own
URL, the logo, and one or more category tags (fs-list-field="category"):
Enterprise, Consumer, AI, Fintech, Healthcare, Frontier, and "IPO/Acquired",
the firm's own exit marker. No year, no stage, no partner.

Also read, as evidence rather than list sources:
  * the growth insights (136 posts on 2026-09-28, /growth/insights/<slug>): the
    firm's partnership announcements name rounds ("anthropic-series-h");
  * the news posts (/news/<slug>): fund announcements, hires.

Everything fetched is cached under sources/site/raw/ (the grid pages) and
scratch/site-raw/ (posts), so a re-run parses offline unless --refresh.

Outputs:
  sources/site/portfolio-2026.json   the grid, one row per company (file_list source)
  sources/site/posts.json            growth insights + news: slug, url, title, date, text
Usage: python3 data/collection/investors/iconiq-growth/scratch/pull-site-iconiq.py [--refresh] [--posts]
"""
from __future__ import annotations

import html as H
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

INV = ROOT / "data/collection/investors/iconiq-growth"
RAW = INV / "sources/site/raw"
POSTRAW = INV / "scratch/site-raw"
BASE = "https://www.iconiq.com"
LISTING = BASE + "/growth/companies"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
REFRESH = "--refresh" in sys.argv


def fetch(url: str, dest: Path) -> str:
    if dest.exists() and not REFRESH:
        return dest.read_text(errors="replace")
    for attempt in range(4):
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(body)
            time.sleep(0.5)
            return body.decode("utf-8", "replace")
        if code == b"404":
            return ""
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url}")


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def parse_grid(h: str) -> list[dict]:
    start = h.find("companies-list_grid shuffle-container")
    if start < 0:
        return []
    out = []
    for it in h[start:].split('class="companies-list_grid-item is-new w-dyn-item"')[1:]:
        name = re.search(r'fs-list-field="name"[^>]*>(.*?)</h3>', it, re.S)
        desc = re.search(r'text-style-3lines is-companies[^"]*"[^>]*>(.*?)</div>', it, re.S)
        url = re.search(r'<a href="([^"]*)" target="_blank" class="button-new is-companies', it)
        cats = [clean(c) for c in re.findall(r'fs-list-field="category">(.*?)</div>', it)]
        logo = re.search(r'<img [^>]*src="([^"]+)"[^>]*class="companies-list_logo', it)
        if not name:
            continue
        out.append({"name": clean(name.group(1)),
                    "description": clean(desc.group(1)) if desc else "",
                    "company_site": url.group(1).strip() if url else "",
                    "categories": [c for c in cats if c != "IPO/Acquired"],
                    "exit_site": "IPO/Acquired" in cats,
                    "logo": logo.group(1) if logo else ""})
    return out


def grid() -> None:
    rows, page = [], 1
    while True:
        url = LISTING if page == 1 else f"{LISTING}?03ce0375_page={page}"
        dest = RAW / ("companies.html" if page == 1 else f"companies-p{page}.html")
        items = parse_grid(fetch(url, dest))
        if not items:
            break
        for i, r in enumerate(items):
            r.update({"url": LISTING, "grid_page": page, "grid_position": i + 1})
        rows += items
        page += 1
    seen, uniq = set(), []
    for r in rows:
        k = r["name"].lower()
        if k in seen:
            continue
        seen.add(k)
        uniq.append(r)
    doc = {"_readme": ("Every company on iconiq.com/growth/companies (ICONIQ Growth's portfolio grid), read "
                       f"{time.strftime('%Y-%m-%d')} by scratch/pull-site-iconiq.py from the server-rendered Webflow "
                       "list (2 pages of 100). `url` is the listing page, the citation (the site has no per-company "
                       "pages); `company_site` is the company's own URL; `categories` are the firm's sector tags; "
                       "`exit_site` is the firm's own 'IPO/Acquired' tag (the FIRM's exit marker, not a status: "
                       "the judge decides status from the company's evidence)."),
           "rows": uniq}
    write_atomic(INV / "sources/site/portfolio-2026.json", json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"grid: {len(uniq)} companies ({sum(r['exit_site'] for r in uniq)} tagged IPO/Acquired)")


def posts() -> None:
    sm = fetch(BASE + "/sitemap.xml", RAW / "sitemap.xml")
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    want = [u for u in locs if re.search(r"/(growth/insights|news)/[^/]+$", u)]
    out = []
    for u in want:
        slug = u.rstrip("/").split("/")[-1]
        kind = "insight" if "/growth/insights/" in u else "news"
        h = fetch(u, POSTRAW / kind / f"{slug}.html")
        if not h:
            out.append({"kind": kind, "slug": slug, "url": u, "status": "404"})
            continue
        title = re.search(r"<title>(.*?)</title>", h, re.S)
        date = (re.search(r'post-content_date"><p[^>]*>([^<]+)</p>', h) or
                re.search(r'"datePublished"\s*:\s*"([^"]+)"', h) or
                re.search(r'fs-list-field="date"[^>]*>([^<]+)<', h) or
                re.search(r'class="[^"]*(?:blog-post_date|article-date|date)[^"]*"[^>]*>([^<]{6,40})<', h))
        body = re.search(r'class="[^"]*w-richtext[^"]*"[^>]*>(.*?)</div>\s*</div>', h, re.S)
        text = clean(body.group(1)) if body else ""
        if not text:
            main = re.search(r"<main.*?</main>", h, re.S)
            text = clean(main.group(0))[:20000] if main else ""
        out.append({"kind": kind, "slug": slug, "url": u, "title": clean(title.group(1)) if title else "",
                    "date": clean(date.group(1)) if date else "", "text": text})
    doc = {"_readme": ("ICONIQ's own posts: every /growth/insights/<slug> and /news/<slug> URL in iconiq.com's "
                       f"sitemap, read {time.strftime('%Y-%m-%d')} by scratch/pull-site-iconiq.py. Evidence, not a "
                       "list source: an insight announcing a partnership names the round it announces, which is "
                       "class 1 for THAT round and asserts an entry only where the post says so (COLLECTION.md 6)."),
           "posts": out}
    write_atomic(INV / "sources/site/posts.json", json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print(f"posts: {len(out)} ({sum(1 for p in out if p['kind']=='insight')} insights, "
          f"{sum(1 for p in out if p['kind']=='news')} news)")


if __name__ == "__main__":
    grid()
    if "--posts" in sys.argv:
        posts()
