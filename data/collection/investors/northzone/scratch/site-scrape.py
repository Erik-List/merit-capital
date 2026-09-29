#!/usr/bin/env python3
"""Read northzone.com's portfolio: the Webflow list (two pages of 100 cards,
?d42057d9_page=N) and every /portfolio/<slug> page from the sitemap. Each
company page carries the firm's own fields: founders, status (Active /
Acquired / IPO), a hidden stage (Early / Growth), a Unicorn tag, category,
location, Founded year, Partnered year, the Northzone team member(s), the
company website and related news. Writes sources/site/companies.json."""
import json, re, sys, time, html as H
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT.parents[2] / "filings" / "northzone" / "site-raw"
RAW.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (MeritCapitalResearch; erik@meritcapit.al)"}

def get(url, dest=None, refresh=False):
    if dest and dest.exists() and not refresh:
        return dest.read_text()
    for i in range(3):
        try:
            import subprocess
            r = subprocess.run(["curl", "-sS", "-f", "-L", "--max-time", "30", "-A", UA["User-Agent"], url],
                               capture_output=True)
            if r.returncode:
                raise RuntimeError(r.stderr.decode()[:200])
            body = r.stdout.decode("utf-8", "replace")
            if dest:
                dest.write_text(body)
            time.sleep(0.4)
            return body
        except Exception as e:
            print("retry", url, e, file=sys.stderr); time.sleep(3)
    raise SystemExit(f"failed {url}")

def text_lines(h):
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = re.sub(r"<[^>]+>", "\n", t)
    return [H.unescape(l.strip()) for l in t.split("\n") if l.strip()]

# 1. the list pages
cards = []
for page in (1, 2, 3):
    h = get(f"https://northzone.com/portfolio?d42057d9_page={page}", RAW / f"list-{page}.html")
    items = h.split('class="filters5_company-list-item w-dyn-item"')[1:]
    for it in items:
        f = lambda k: (re.search(rf'fs-cmsfilter-field="{k}"[^>]*>([^<]*)<', it) or [None, None])[1]
        cards.append({
            "url": "https://northzone.com" + re.search(r'href="(/portfolio/[^"]+)"', it).group(1),
            "name": H.unescape(f("name") or ""),
            "stage_list": f("stage"),
            "status_list": f("status"),
            "industry": [H.unescape(x) for x in re.findall(r'fs-cmsfilter-field="industry" class="text-size-regular text-color-secondary">([^<]*)<', it)],
            "location": [H.unescape(x) for x in re.findall(r'fs-cmsfilter-field="industry" class="text-size-regular">([^<]*)<', it)],
            "list_page": page,
        })
    if not items:
        break
print("list cards", len(cards))

# 2. every company page in the sitemap
sm = get("https://northzone.com/sitemap.xml", RAW / "sitemap.xml")
urls = sorted(set(u for u in re.findall(r"<loc>([^<]+)</loc>", sm) if re.match(r"https://northzone.com/portfolio/[^/]+$", u)))
bycard = {c["url"]: c for c in cards}
rows = []
LABELS = {"Category", "Location", "Founded", "Partnered", "Northzone Team", "About"}
for u in sorted(set(urls) | set(bycard)):
    slug = u.rsplit("/", 1)[1]
    h = get(u, RAW / f"company-{slug}.html")
    L = text_lines(h)
    title = re.search(r"<title>([^<]*)</title>", h)
    name = H.unescape(title.group(1)).rsplit(" - Northzone", 1)[0].strip() if title else slug
    try:
        i0 = L.index(name, 5)
    except ValueError:
        i0 = 6
    def after(label, n=1):
        try:
            j = L.index(label, i0)
            return L[j + 1:j + 1 + n]
        except ValueError:
            return []
    # the block between the name and 'Category' holds founders, status, stage, tags
    try:
        jc = L.index("Category", i0)
    except ValueError:
        jc = i0 + 1
    head = L[i0 + 1:jc]
    status = next((x for x in head if x in ("Active", "Acquired", "IPO", "Exited", "Closed")), None)
    stage = next((x for x in head if x in ("Early", "Growth", "Seed")), None)
    tags = [x for x in head if x in ("Unicorn",)]
    founders = [x for x in head if x not in (status, stage) and x not in tags]
    # team: lines between 'Northzone Team' and the next 'About'
    team = []
    try:
        jt = L.index("Northzone Team", i0); ja = L.index("About", jt)
        team = L[jt + 1:ja]
    except ValueError:
        pass
    about = []
    try:
        ja = L.index("About", jc); je = L.index("company website", ja) if "company website" in L[ja:] else ja + 4
        about = L[ja + 1:je]
    except ValueError:
        pass
    web = re.search(r'<a[^>]+href="(https?://[^"]+)"[^>]*>\s*(?:<[^>]+>\s*)*company website', h, flags=re.I)
    news = []
    for m in re.finditer(r'href="([^"]+)"[^>]*>(?:(?!</a>).)*?</a>', h, flags=re.S):
        pass
    related = []
    try:
        jr = L.index("Related news")
        k = jr + 1
        while k + 2 < len(L) and L[k] in ("Press", "Perspective", "News", "Portfolio news", "Insight", "Podcast", "Announcement"):
            related.append({"kind": L[k], "title": L[k + 1], "date": L[k + 2]}); k += 3
    except ValueError:
        pass
    links = re.findall(r'<a[^>]+href="(/insights/[^"]+|https?://[^"]+)"', h)
    rows.append({
        "name": name, "url": u, "slug_site": slug,
        "status_site": status, "stage_site_word": stage, "tags": tags, "founders": founders,
        "category": after("Category")[:1] and after("Category")[0],
        "location_page": after("Location")[:1] and after("Location")[0],
        "founded_year": (after("Founded") or [None])[0],
        "partnered_year": (after("Partnered") or [None])[0],
        "team": team, "about": " ".join(about),
        "website": web.group(1) if web else None,
        "related": related,
        "insight_links": sorted(set(l for l in links if l.startswith("/insights/"))),
        "in_list": u in bycard, "list": bycard.get(u),
    })
out = ROOT / "sources" / "site" / "companies-webflow.json"
out.write_text(json.dumps({
    "_readme": "northzone.com portfolio, read by scratch/site-scrape.py on " + time.strftime("%Y-%m-%d") +
               ": the Webflow list (?d42057d9_page=1..2) and every /portfolio/<slug> page in sitemap.xml. "
               "Raw pages under data/filings/northzone/site-raw/ (gitignored).",
    "rows": rows}, indent=1, ensure_ascii=False))
print("company pages", len(rows), "in list", sum(r["in_list"] for r in rows))
