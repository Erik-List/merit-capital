#!/usr/bin/env python3
"""Read indexventures.com's portfolio (Wagtail): the /companies/ listing (one
page, every card carries data-backed / data-regions / data-sectors and an
optional ticker-or-acquirer span) and every /companies/<slug>/ page in
sitemap-companies.xml. A company page carries the firm's own fields: tagline,
Founders/CEOs, Index Team, Sector, Website and the related Perspectives posts.
Raw pages go to data/filings/index-ventures/site-raw/ (gitignored). Writes
sources/site/companies.json (everything read) and sources/site/companies-list.json
(the flat file_list source for site-portfolio.py)."""
import html as H
import json
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT.parents[2] / "filings" / "index-ventures" / "site-raw"
RAW.mkdir(parents=True, exist_ok=True)
BASE = "https://www.indexventures.com"
UA = "Mozilla/5.0 (MeritCapitalResearch; erik@meritcapit.al)"


def get(url, dest, refresh=False):
    if dest.exists() and dest.stat().st_size > 0 and not refresh:
        return dest.read_text()
    for i in range(3):
        r = subprocess.run(["curl", "-sS", "-L", "--max-time", "40", "-A", UA,
                            "-w", "\n%{http_code}", url], capture_output=True)
        out = r.stdout.decode("utf-8", "replace")
        body, _, code = out.rpartition("\n")
        if r.returncode == 0 and code == "200":
            dest.write_text(body)
            time.sleep(0.35)
            return body
        if code == "404":
            return None
        print("retry", url, r.returncode, code, file=sys.stderr)
        time.sleep(3 * (i + 1))
    raise SystemExit(f"failed {url}")


def clean(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def text_lines(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", h, flags=re.S)
    t = re.sub(r"<[^>]+>", "\n", t)
    return [H.unescape(l.strip()) for l in t.split("\n") if l.strip()]


CARD = re.compile(
    r'<li\s+class="companies__relationships__list__item js-company"\s+'
    r'data-backed="([^"]*)"\s+data-regions="([^"]*)"\s+data-sectors=\'([^\']*)\'\s*>\s*'
    r'<a href="([^"]+)"[^>]*>(.*?)</a>', re.S)

refresh = "--refresh" in sys.argv

# 1. the listing (the four filter variants serve the same 329 cards; keep "all")
listing = get(f"{BASE}/companies/backed/all/", RAW / "list-all.html", refresh)
cards = {}
for backed, regions, sectors, href, inner in CARD.findall(listing):
    span = re.search(r'<span class="ticker-symbol">(.*?)</span>', inner, re.S)
    name = clean(re.sub(r"<span.*?</span>", "", inner, flags=re.S))
    cards[href] = {
        "name_list": name,
        "backed": json.loads(H.unescape(backed)),
        "regions": json.loads(H.unescape(regions)),
        "sectors_list": json.loads(H.unescape(sectors)),
        "list_tag": clean(span.group(1)) if span else None,
    }
print("listing cards", len(cards))

# 2. the sitemap
sm = get(f"{BASE}/sitemap-companies.xml", RAW / "sitemap-companies.xml", refresh)
locs = [l for l in re.findall(r"<loc>([^<]+)</loc>", sm)
        if re.fullmatch(rf"{re.escape(BASE)}/companies/[^/]+/", l)]
lastmod = dict(re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", sm))
paths = sorted(set(l[len(BASE):] for l in locs) | set(cards))
print("sitemap company pages", len(locs), "union", len(paths))

LABELS = ["Founders/CEOs", "Founder/CEO", "Founders", "Founder", "CEO", "Index Team",
          "Sector", "Sectors", "Website", "Location", "Status"]
rows = []
for p in paths:
    slug = p.strip("/").split("/")[-1]
    h = get(BASE + p, RAW / f"company-{slug}.html", refresh)
    if h is None:
        rows.append({"path": p, "slug_site": slug, "missing_page": True, **cards.get(p, {})})
        continue
    main = h[h.find('<article role="main"'):] if '<article role="main"' in h else h
    main = main.split('<footer')[0]
    title = re.search(r"<title>(.*?)</title>", h, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    lines = text_lines(main)
    # labelled blocks
    fields = {}
    cur = None
    for l in lines:
        if l in LABELS:
            cur = l
            fields.setdefault(cur, [])
            continue
        if cur:
            if l.startswith("Opens in a new window") or l.startswith("This link opens") or l == "View all":
                cur = None
                continue
            fields[cur].append(l)
    # trim: a labelled block ends at the next label; the Website block is one line
    web = re.search(r'href="(https?://[^"]+)"[^>]*class="[^"]*company[^"]*website[^"]*"', main) \
        or re.search(r'Website\s*</[^>]+>\s*(?:<[^>]+>\s*)*<a[^>]+href="(https?://[^"]+)"', main, re.S)
    persp = sorted(set(re.findall(r'href="(/perspectives/[^"#?]+/)"', main)))
    team_links = sorted(set(re.findall(r'href="(/team/[^"#?]+/)"', main)))
    desc = re.search(r'<meta name="description" content="([^"]*)"', h)
    row = {
        "path": p,
        "url": BASE + p,
        "slug_site": slug,
        "name": clean(h1.group(1)) if h1 else None,
        "title_tag": clean(title.group(1)) if title else None,
        "description": H.unescape(desc.group(1)) if desc else None,
        "founders": fields.get("Founders/CEOs") or fields.get("Founder/CEO") or fields.get("Founders") or fields.get("Founder") or fields.get("CEO") or [],
        "partners": [x.rstrip(",").strip() for x in fields.get("Index Team", []) if x.strip(", ")],
        "team_links": team_links,
        "sectors_page": fields.get("Sector") or fields.get("Sectors") or [],
        "website": web.group(1) if web else None,
        "website_text": (fields.get("Website") or [None])[0],
        "perspectives": persp,
        "lastmod": lastmod.get(BASE + p),
        "listed": p in cards,
        **cards.get(p, {}),
    }
    rows.append(row)

out = {
    "_readme": "indexventures.com portfolio, read by scratch/site-scrape.py on %s: "
               "the /companies/backed/all/ listing (cards with data-backed, data-regions, "
               "data-sectors and a ticker-or-acquirer tag) and every /companies/<slug>/ page "
               "in sitemap-companies.xml. Raw pages under data/filings/index-ventures/site-raw/ "
               "(gitignored). listed=false marks a page the sitemap serves and the listing "
               "does not carry." % date.today().isoformat(),
    "rows": rows,
}
(ROOT / "sources" / "site" / "companies-wagtail.json").write_text(json.dumps(out, indent=1, ensure_ascii=True))
print("rows", len(rows), "listed", sum(1 for r in rows if r.get("listed")),
      "missing", sum(1 for r in rows if r.get("missing_page")))
