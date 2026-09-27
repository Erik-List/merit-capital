#!/usr/bin/env python3
"""Parse Common Crawl captures of insightpartners.com into sources/wayback/parsed/<year>.json
(the same shape wayback-pull.py writes; parsed year files MERGE keyed slug+path, COLLECTION.md §5).

Two kinds of rows:
  listing rows   the firm's full portfolio listings, which carry the site's own rendering of each
                 name: 2010-03 and 2012-02 /portfolio (div.portfolio_logo_box: href slug, img alt,
                 title 'Name :: description', Active/Inactive class), 2013-05 /portfolio/ (div.item
                 id=slug, span.name, 'active' class), 2017-07 and 2018-01 /companies/ (li.grid-item
                 data-filter-text=name, href slug, current-/prior-investment class).
  page rows      one per company page in the Common Crawl index (/portfolio/<slug> 2010-2012 and
                 2018-2026, /companies/<slug> 2017-2018), dated by the capture, with no body read;
                 a page whose digest is shared by 3+ slugs in one crawl is a catch-all shell and is
                 dropped. The name comes from a listing of the same slug where one exists.
Every row carries capture_url in the index.commoncrawl.org form (§1: a valid citation).
Usage: python3 cc-parse.py"""
import html, json, re, sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402
I = HERE.parent
RAW = HERE.parents[4] / "data" / "filings" / "commoncrawl" / "insight-partners"
PARSED = I / "sources" / "wayback" / "parsed"
man = json.loads((I / "sources" / "wayback" / "cc-manifest.json").read_text())
idx = json.loads((HERE / "cc-index-raw.json").read_text())
cfg = json.loads((I / "config.json").read_text())
JUNK = set(cfg["wayback"].get("non_company_slugs") or [])
DOM = re.compile(r"https?://(www\.)?insightpartners\.com(:\d+)?", re.I)


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def cap_url(cid, url):
    return f"https://index.commoncrawl.org/{cid}-index?url={quote(url, safe='')}&output=json"


rows = defaultdict(list)          # year -> rows
names = {"era3": {}, "era4": {}}    # slug -> site rendering, per URL namespace era (a slug is not an identity across eras)
LISTINGS = [("20100311", "/portfolio", "era3"), ("20120204", "/portfolio", "era3"),
            ("20130518", "/portfolio/", "era2013"), ("20170723", "/companies/", "era4"),
            ("20180120", "/companies/", "era4")]
for ts, path, kind in LISTINGS:
    key, v = next((k, v) for k, v in man.items() if v["timestamp"].startswith(ts) and v["path"] == path)
    b = (RAW / key).read_bytes().decode("utf-8", "replace")
    year = ts[:4]
    got = []
    if kind == "era3":
        for m in re.finditer(r'<div class="portfolio_logo_box ([^"]*)">\s*<a href="[^"]*/portfolio/([A-Za-z0-9_\-]+)"><img alt="([^"]*)"[^>]*?title="([^"]*)"', b):
            cls, slug, alt, title = m.groups()
            nm, _, desc = html.unescape(title).partition(" :: ")
            got.append({"slug": slug.lower(), "name": clean(alt) or clean(nm), "description": desc.strip()[:600],
                        "listing_status": "inactive" if "Inactive" in cls.split() else "active"})
    elif kind == "era2013":
        for m in re.finditer(r'<div class="item clickable portfolio ([^"]*)"[^>]*id="([^"]+)">(.*?)<span class="name">(.*?)</span>', b, re.S):
            cls, slug, _, nm = m.groups()
            got.append({"slug": slug.lower(), "name": clean(nm),
                        "listing_status": "active" if "active" in cls.split() else "not marked active"})
    else:
        for m in re.finditer(r'<li class="grid-item company ([^"]*)" data-filter-text="([^"]*)">\s*<a href="[^"]*/companies/([A-Za-z0-9_\-]+)/?"', b):
            cls, nm, slug = m.groups()
            got.append({"slug": slug.lower(), "name": clean(nm),
                        "listing_status": "prior investment" if "prior-investment" in cls.split() else
                                          "current investment" if "current-investment" in cls.split() else ""})
    for g in got:
        if g["slug"] in JUNK:
            continue
        names["era3" if kind == "era3" else "era4"].setdefault(g["slug"], g["name"])
        rows[year].append({**g, "path": path, "snapshot_ts": v["timestamp"], "source": "commoncrawl-listing",
                           "capture_url": v["capture_url"]})
    print(ts, path, len(got), "listing rows")

def era_name(path, year):
    """The listing name for a company page, from the listing of its own URL era only:
    /portfolio/<name_with_underscores> up to 2012, /companies/<slug> 2013-2018. The 2019+
    /portfolio/<slug> pages share the namespace with era 3 but not its slugs' meaning."""
    slug = path.rstrip("/").rsplit("/", 1)[-1]
    if path.startswith("/portfolio/") and year <= 2012:
        return names["era3"].get(slug)
    if path.startswith("/companies/"):
        return names["era4"].get(slug)
    return None


# page rows from the index
per_crawl_digest = defaultdict(lambda: defaultdict(set))
recs = []
for cid, v in idx.items():
    for r in v.get("records", []):
        p = DOM.sub("", r["url"]).split("?")[0]
        m = re.match(r"^/(portfolio|companies)/([A-Za-z0-9_\-]+)/?$", p)
        if not m:
            continue
        slug = m.group(2).lower()
        if slug in JUNK:
            continue
        per_crawl_digest[cid][r.get("digest")].add(slug)
        recs.append((cid, r, m.group(1), slug))
seen = set()
shells = 0
for cid, r, ns, slug in sorted(recs, key=lambda x: x[1]["timestamp"]):
    if len(per_crawl_digest[cid][r.get("digest")]) >= 3:
        shells += 1
        continue
    year = r["timestamp"][:4]
    path = f"/{ns}/{slug}"
    if (year, path) in seen:
        continue
    seen.add((year, path))
    row = {"slug": slug, "path": path, "snapshot_ts": r["timestamp"], "source": "commoncrawl-page",
           "capture_url": cap_url(cid, r["url"])}
    nm = era_name(path, int(year))
    if nm:
        row["name"] = nm
    rows[year].append(row)
print(shells, "shell captures dropped;", len(seen), "page rows")

for f in sorted(PARSED.glob('*.json')):
    rows.setdefault(f.stem, [])
for year, new in sorted(rows.items()):
    f = PARSED / f"{year}.json"
    old = json.loads(f.read_text()) if f.exists() else []
    have = {(r["slug"], r["path"]) for r in old}
    add = [r for r in new if (r["slug"], r["path"]) not in have]
    # a listing's own rendering names a slug-only row of the same year
    for r in old:
        if r.get("source") == "commoncrawl-listing":
            continue
        nm = era_name(r["path"], int(year))
        if nm and not r.get("name"):
            r["name"] = nm
        elif not nm and r.get("name_from") == "cc-listing":
            r.pop("name", None)
    write_atomic(f, json.dumps(old + add, indent=1, ensure_ascii=False) + "\n")
    print(year, "+", len(add), "rows, file holds", len(old) + len(add))
