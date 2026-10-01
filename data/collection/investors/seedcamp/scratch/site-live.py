#!/usr/bin/env python3
"""Parse the live seedcamp.com/our-companies/ list into sources/site/companies-2026.json.

seedcamp.com (2026) is WordPress with a custom theme; the company post type is
not exposed in the REST API, and the whole list ships server-rendered in one
page (mixitup filter): one `div.company__item` per company with the name, the
firm's own "Year of Investment", a one-line description, the company website
and the sector classes of the filter bar (ai, climate, consumer, crypto,
developer-tools, enterprise, fintech, health-bio, marketplaces, security).
There is no per-company page; url is the list anchor. The year is the firm's
own investment year: an anchor for first_seen and the censor clock, never a
round word (COLLECTION.md s6, "a bare year is an anchor, not a label").

Usage: python3 site-live.py   (reads scratch/site-raw/our-companies-2026-09-30.html)
"""
import html, json, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
RAW = HERE / "site-raw" / "our-companies-2026-09-30.html"
OUT = HERE.parent / "sources" / "site" / "companies-2026.json"

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

t = RAW.read_text()
rows = []
for i, it in enumerate(re.split(r'<div class="company__item mix', t)[1:]):
    cls = it[:it.find('"')].split()
    web = re.search(r'<a href="([^"]*)"', it)
    name = re.search(r'company__item__name[^>]*>\s*(.*?)\s*<', it, re.S)
    year = re.search(r'company__item__year[^>]*>\s*(.*?)\s*<', it, re.S)
    desc = re.search(r'company__item__description__content[^>]*>\s*(.*?)\s*</div', it, re.S)
    nm = html.unescape(name.group(1)).strip()
    rows.append({
        "name": nm,
        "url": f"https://seedcamp.com/our-companies/#{slug(nm)}",
        "website": web.group(1) if web else None,
        "invest_year": year.group(1).strip() if year else None,
        "description": html.unescape(re.sub(r"<[^>]+>", "", desc.group(1))).strip() if desc else None,
        "sectors": cls,
        "index": i,
    })
OUT.write_text(json.dumps({
    "_readme": __doc__.strip(),
    "source_url": "https://seedcamp.com/our-companies/",
    "read": "2026-09-30",
    "rows": rows}, indent=1, ensure_ascii=False) + "\n")
print(len(rows), "rows")
