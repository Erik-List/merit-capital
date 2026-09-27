#!/usr/bin/env python3
"""Pull General Catalyst's own site into sources/site/ (PRO-166).

generalcatalyst.com is Webflow. Three first-party company surfaces:

1. /portfolio: a Finsweet list over server pagination (?f75a35e2_page=N,
   100 rows a page). Each card carries the firm's own flags (active, ipo,
   acquired, creation, cvf, seed), sector, region, the deal investors and
   the /companies/<slug> link. Direct fetches of the page parameter work.
2. /companies/<slug>: one page per company (the sitemap lists them): the
   description, website, LinkedIn, X, investors, industry, "Backed since"
   year and region.
3. /list: the marketing-rule list of investments "made by General Catalyst"
   as of a stated date, legal entity names, with a declared exclusion for
   confidentiality provisions.

Also enumerated from the sitemap: /stories/<slug> (the firm's posts) and
/team/<slug> (people). Raw responses are cached under scratch/site-raw/ so a
re-run re-parses without re-fetching (--refetch forces the network).

Writes:
  sources/site/company-pages.json   rows for site_api file_list (portfolio card + company page)
  sources/site/all-companies.json   the /list entries, verbatim, with the list's own caveat
  sources/site/stories.json         every story: title, date, text, company links
  sources/site/team-pages.json      every team page: name, title, group, socials, companies
"""
import html
import json
import re
import sys
import time
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
RAW = HERE / "site-raw"
SITE = INV / "sources" / "site"
BASE = "https://www.generalcatalyst.com"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
REFETCH = "--refetch" in sys.argv
sys.path.insert(0, str(INV.parents[3] / "scripts"))
from paths import write_atomic  # noqa: E402


def fetch(url: str, cache: Path) -> str:
    if cache.exists() and cache.stat().st_size > 0 and not REFETCH:
        return cache.read_text(errors="replace")
    # curl, as the shared scripts do: this Python's certificate store is not
    # set up, and urllib refuses every TLS handshake.
    for attempt in range(4):
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.decode("utf-8", errors="replace").rpartition("\n")
        if code == "200" and body:
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text(body)
            time.sleep(0.25)
            return body
        if code == "404":
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_text("")
            return ""
        time.sleep(2 + 3 * attempt)
    raise RuntimeError(f"fetch failed: {url}")


def text_of(fragment: str) -> str:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", fragment, flags=re.S)
    t = re.sub(r"<br\s*/?>|</p>|</div>|</h\d>|</li>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t).replace("‍", "")
    return re.sub(r"[ \t]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()


def sitemap() -> list[str]:
    x = fetch(f"{BASE}/sitemap.xml", RAW / "sitemap.xml")
    return [re.sub(r"^https?://[^/]+", "", u) for u in re.findall(r"<loc>([^<]+)</loc>", x)]


def portfolio_cards() -> list[dict]:
    cards, page, pages = [], 1, None
    while True:
        h = fetch(f"{BASE}/portfolio?f75a35e2_page={page}", RAW / f"portfolio-p{page}.html")
        main = h[h.find('fs-list-instance="main" role="list"'):]
        end = main.find("w-pagination-wrapper")
        body = main[: end if end > 0 else len(main)]
        blocks = body.split('role="listitem" class="portfolio_collection-item w-dyn-item"')[1:]
        for b in blocks:
            name = re.search(r'<h2 class="heading-style-h2[^"]*">([^<]+)</h2>', b)
            href = re.search(r'href="/companies/([^"#?]+)"', b)
            flags = dict(re.findall(r'<div fs-list-field="(active|ipo|acquired|creation|cvf|seed)">(true|false)</div>', b))
            sector = re.search(r'fs-list-field="sector"[^>]*>([^<]*)<', b)
            region = re.search(r'fs-list-field="location"[^>]*>([^<]*)<', b)
            invs = re.findall(r'fs-list-field="investor">([^<]+)<', b)
            cards.append({
                "name": html.unescape(name.group(1)).strip() if name else "",
                "slug": href.group(1) if href else "",
                "flags": {k: v == "true" for k, v in flags.items()},
                "sector": html.unescape(sector.group(1)).strip() if sector else "",
                "region": html.unescape(region.group(1)).strip() if region else "",
                "investors": [html.unescape(i).strip() for i in invs],
                "page": page,
            })
        m = re.search(r'aria-label="Page \d+ of (\d+)"', main)
        pages = int(m.group(1)) if m else pages or page
        if page >= pages:
            break
        page += 1
    return cards


def company_page(slug: str) -> dict:
    h = fetch(f"{BASE}/companies/{slug}", RAW / "companies" / f"{slug}.html")
    if not h:
        return {"_missing": True}
    main = h[h.find("<main"):]
    main = main[: main.find("</main>")] if "</main>" in main else main
    out = {}
    m = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    out["page_name"] = text_of(m.group(1)) if m else ""
    links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', main, re.S)
    for href, label in links:
        lab = text_of(label).lower()
        if lab == "website" and "company_site" not in out:
            out["company_site"] = href
        elif lab == "linkedin" and "linkedin" not in out:
            out["linkedin"] = href
        elif lab in ("x", "twitter") and "x_url" not in out:
            out["x_url"] = href
    t = text_of(main)
    lines = [ln.strip() for ln in t.split("\n") if ln.strip()]
    # The page reads: name, description, Website, LinkedIn, X, "Investors:",
    # names..., "Industry:", value, "Backed since:", year, "Region:", value.
    def after(label: str, stop: tuple) -> list[str]:
        if label not in lines:
            return []
        i, vals = lines.index(label) + 1, []
        while i < len(lines) and lines[i] not in stop:
            vals.append(lines[i])
            i += 1
        return vals
    labels = ("Investors:", "Industry:", "Backed since:", "Region:")
    out["investors"] = after("Investors:", labels)
    ind = after("Industry:", labels)
    out["industry"] = ind[0] if ind else ""
    bs = after("Backed since:", labels)
    out["backed_since"] = bs[0] if bs else ""
    rg = after("Region:", labels)
    out["region"] = rg[0] if rg else ""
    # description: the text between the name and "Website"/"Investors:"
    try:
        i0 = lines.index(out["page_name"]) + 1 if out["page_name"] in lines else 0
        desc = []
        for ln in lines[i0:]:
            if ln in ("Website", "LinkedIn", "X", "Investors:", "Industry:") or ln.startswith(("WebsiteLinkedIn", "LinkedInX", "Website")):
                break
            desc.append(ln)
        out["description"] = " ".join(desc)[:1200]
    except ValueError:
        out["description"] = ""
    out["stories"] = sorted(set(re.findall(r'href="/stories/([^"#?]+)"', main)))
    return out


def all_companies() -> dict:
    h = fetch(f"{BASE}/list", RAW / "list.html")
    head = re.search(r'c-page-header__subheading">(.*?)</div>', h, re.S)
    i = h.find("c-all-companies__list")
    e = h.find("</div>", i)
    names = [html.unescape(re.sub(r"<[^>]+>", "", x)).replace("‍", "").strip()
             for x in re.findall(r"<p>(.*?)</p>", h[i:e], re.S)]
    names = [n for n in names if n]
    return {"caveat": text_of(head.group(1)) if head else "", "entries": names}


def story(slug: str) -> dict:
    h = fetch(f"{BASE}/stories/{slug}", RAW / "stories" / f"{slug}.html")
    if not h:
        return {"slug": slug, "_missing": True}
    title = re.search(r"<title>([^<]*)</title>", h)
    main = h[h.find("<main"):]
    main = main[: main.find("</main>")] if "</main>" in main else main
    date = re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, (19|20)\d\d", text_of(main))
    return {
        "slug": slug,
        "url": f"{BASE}/stories/{slug}",
        "title": html.unescape(title.group(1)).replace(" | General Catalyst", "").strip() if title else "",
        "date": date.group(0) if date else "",
        "companies": sorted(set(re.findall(r'href="/companies/([^"#?]+)"', main))),
        "text": text_of(main)[:20000],
    }


def team(slug: str) -> dict:
    h = fetch(f"{BASE}/team/{slug}", RAW / "team" / f"{slug}.html")
    if not h:
        return {"slug": slug, "_missing": True}
    main = h[h.find("<main"):]
    main = main[: main.find("</main>")] if "</main>" in main else main
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    lines = [ln for ln in text_of(main).split("\n") if ln.strip()]
    socials = re.findall(r'href="(https?://(?:www\.)?(?:linkedin\.com|x\.com|twitter\.com)/[^"]+)"', main)
    return {
        "slug": slug,
        "url": f"{BASE}/team/{slug}",
        "name": text_of(h1.group(1)) if h1 else "",
        "lines": lines[:40],
        "linkedin_url": next((s for s in socials if "linkedin.com" in s), ""),
        "x_url": next((s for s in socials if "x.com" in s or "twitter.com" in s), ""),
        "companies": sorted(set(re.findall(r'href="/companies/([^"#?]+)"', main))),
    }


def main() -> None:
    paths = sitemap()
    co_slugs = sorted({p.split("/")[2] for p in paths if p.startswith("/companies/")})
    st_slugs = sorted({p.split("/")[2] for p in paths if p.startswith("/stories/") and p.count("/") == 2})
    tm_slugs = sorted({p.split("/")[2] for p in paths if p.startswith("/team/") and p.count("/") == 2})
    print(f"sitemap: {len(co_slugs)} companies, {len(st_slugs)} stories, {len(tm_slugs)} team", flush=True)

    cards = portfolio_cards()
    print(f"portfolio cards: {len(cards)}", flush=True)
    by_slug = {c["slug"]: c for c in cards if c["slug"]}
    rows = []
    for n, slug in enumerate(sorted(set(co_slugs) | set(by_slug)), 1):
        c = by_slug.get(slug, {})
        p = company_page(slug)
        name = c.get("name") or p.get("page_name") or slug
        by = (p.get("backed_since") or "").strip()
        rows.append({
            "slug": slug,
            "name": name,
            "url": f"{BASE}/companies/{slug}",
            "in_grid": bool(c),
            "in_sitemap": slug in co_slugs,
            "page_missing": bool(p.get("_missing")),
            "sectors": [s for s in {c.get("sector") or "", p.get("industry") or ""} if s],
            "partners": list(dict.fromkeys((c.get("investors") or []) + (p.get("investors") or []))),
            "backed_since": by,
            "invest_year": by[:4] if re.fullmatch(r"(19|20)\d\d", by[:4] or "") else "",
            "region": c.get("region") or p.get("region") or "",
            "flag_active": (c.get("flags") or {}).get("active"),
            "flag_ipo": (c.get("flags") or {}).get("ipo"),
            "flag_acquired": (c.get("flags") or {}).get("acquired"),
            "flag_creation": (c.get("flags") or {}).get("creation"),
            "flag_cvf": (c.get("flags") or {}).get("cvf"),
            "flag_seed": (c.get("flags") or {}).get("seed"),
            "company_site": p.get("company_site") or "",
            "linkedin": p.get("linkedin") or "",
            "x_url": p.get("x_url") or "",
            "description": p.get("description") or "",
            "stories": p.get("stories") or [],
        })
        if n % 100 == 0:
            print(f"  company pages {n}", flush=True)
    SITE.mkdir(parents=True, exist_ok=True)
    write_atomic(SITE / "company-pages.json", json.dumps({
        "_readme": ("General Catalyst's live portfolio: every /portfolio card (Webflow + Finsweet, "
                    "server pages ?f75a35e2_page=N) joined to its /companies/<slug> page by "
                    "scratch/pull-site-gc.py. flag_* are the firm's own card flags (Active, IPO, "
                    "Acquired, Creation, CVF, Seed); 'partners' are the deal investors the card and "
                    "page name; 'backed_since' is the firm's own year of first backing (an anchor, "
                    "never a round word). flag_seed is the firm's claim that it backed the company "
                    "at seed: measured against documented rounds before it may label (COLLECTION.md 5)."),
        "_source": f"{BASE}/portfolio",
        "_pulled": time.strftime("%Y-%m-%d"),
        "rows": rows,
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"company-pages: {len(rows)}", flush=True)

    ac = all_companies()
    write_atomic(SITE / "all-companies.json", json.dumps({
        "_readme": "The firm's /list page verbatim: 'a list of investments made by General Catalyst', legal entity names, with the list's own caveat (confidentiality exclusions, as-of date).",
        "_source": f"{BASE}/list",
        "_pulled": time.strftime("%Y-%m-%d"),
        "caveat": ac["caveat"],
        "entries": ac["entries"],
    }, indent=1, ensure_ascii=False) + "\n")
    print(f"all-companies: {len(ac['entries'])}", flush=True)

    stories = [story(s) for s in st_slugs]
    write_atomic(SITE / "stories.json", json.dumps({"_source": f"{BASE}/stories", "_pulled": time.strftime("%Y-%m-%d"), "rows": stories}, indent=1, ensure_ascii=False) + "\n")
    print(f"stories: {len(stories)}", flush=True)
    people = [team(s) for s in tm_slugs]
    write_atomic(SITE / "team-pages.json", json.dumps({"_source": f"{BASE}/team", "_pulled": time.strftime("%Y-%m-%d"), "rows": people}, indent=1, ensure_ascii=False) + "\n")
    print(f"team: {len(people)}", flush=True)


if __name__ == "__main__":
    main()
