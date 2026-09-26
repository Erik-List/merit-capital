#!/usr/bin/env python3
"""Parse the Common Crawl captures of ivp.com into file_list sources.

Reads scratch/cc-raw/<crawl>/<hash>.{html,json} (written by pull-cc-ivp.py)
and writes, under sources/site/:

  cc-listings.json  one row per company named on any archived ivp.com
                    portfolio surface, 2013-2022, with the firm's own fields:
                    Gen A (2013 to mid-2016, the /assets/ CMS): the listing
                      pages' <div class="detail"> cards (name, one-line
                      description, an outcome line such as "IPO (TIVO)" or
                      "Acquired by Thoma Bravo", website), per listing page
                      (/portfolio, /portfolio/all, the sector pages, recent
                      investments);
                    Gen B (mid-2016 to 2022, WordPress): the per-company pages
                      (/portfolio/<slug>/: Leadership, Location, Year Invested,
                      Status, company-type class) and the portfolio_nav slider
                      every such page carries, which is the whole list;
                    the earliest and latest capture naming each company, and
                    the capture that is its citation (COLLECTION.md 1: a CC
                    capture cites itself when the live page is gone; decisions
                    R1).
  cc-posts.json     the archived news pages (Gen A /news/press-release/*,
                    Gen B /news/*): title, capture date, body text, companies
                    linked, as round-word evidence.

Usage: python3 data/collection/investors/ivp/scratch/parse-cc-ivp.py
"""
from __future__ import annotations

import glob
import html
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/ivp"
RAW = INV / "scratch/cc-raw"
OUT = INV / "sources/site"


def text(s: str) -> str:
    s = re.sub(r"<br\s*/?>", " / ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def cite(meta: dict) -> str:
    return (f"https://index.commoncrawl.org/{meta['crawl']}-index?url="
            f"{meta['url']}&output=json")


def path_of(url: str) -> str:
    return re.sub(r"^https?://(www\.)?ivp\.com(:80)?", "", url).split("?")[0].split("#")[0].rstrip("/").lower() or "/"


def norm(name: str) -> str:
    n = html.unescape(name).lower()
    n = re.sub(r"\b(inc|corp|corporation|llc|ltd|co)\b\.?", "", n)
    return re.sub(r"[^a-z0-9]+", "", n)


def devalue(arr):
    """Nuxt 3 devalue payload -> plain objects (same decoder as pull-site-ivp.py)."""
    import sys as _s
    _s.setrecursionlimit(1_000_000)
    memo = {}

    def rev(i):
        if i in memo:
            return memo[i]
        v = arr[i]
        if isinstance(v, list):
            if v and isinstance(v[0], str) and v[0] in ("Reactive", "ShallowReactive", "Ref", "ShallowRef",
                                                        "EmptyRef", "EmptyShallowRef", "Set", "Map", "Date",
                                                        "NuxtError", "Island", "undefined"):
                tag = v[0]
                if tag in ("Reactive", "ShallowReactive", "Ref", "ShallowRef"):
                    r = rev(v[1])
                elif tag == "Set":
                    r = [rev(x) for x in v[1:]]
                elif tag == "Map":
                    r = {str(rev(v[k])): rev(v[k + 1]) for k in range(1, len(v), 2)}
                elif tag == "Date":
                    r = v[1]
                elif tag in ("EmptyRef", "EmptyShallowRef", "undefined"):
                    r = None
                else:
                    r = {"_tag": tag, "v": [rev(x) for x in v[1:]]}
                memo[i] = r
                return r
            out = []
            memo[i] = out
            for x in v:
                out.append(rev(x) if isinstance(x, int) and not isinstance(x, bool) else x)
            return out
        if isinstance(v, dict):
            out = {}
            memo[i] = out
            for k, x in v.items():
                out[k] = rev(x) if isinstance(x, int) and not isinstance(x, bool) else x
            return out
        memo[i] = v
        return v

    return rev(0)


GEN_A_LISTS = re.compile(r"^/portfolio(/all|/category/[a-z-]+|/recent-investments|/enterprise-it(-print)?|"
                         r"/internet-digital-media(-print)?|/mobile-communications(-print)?)?$")


def main() -> None:
    caps = []
    for mf in glob.glob(str(RAW / "*/*.json")):
        meta = json.load(open(mf))
        meta["_html"] = mf[:-5] + ".html"
        meta["_path"] = path_of(meta["url"])
        caps.append(meta)
    caps.sort(key=lambda m: m["timestamp"])

    rows: dict[str, dict] = {}

    def row(name: str) -> dict:
        k = norm(name)
        r = rows.setdefault(k, {"name": html.unescape(name).strip(), "listed_on": set(),
                                "captures": [], "descriptions": set(), "outcomes": set(),
                                "websites": set(), "gen_b": {}})
        return r

    def seen(r: dict, meta: dict, surface: str) -> None:
        r["captures"].append((meta["timestamp"], cite(meta), surface))
        r["listed_on"].add(surface)

    for meta in caps:
        p = meta["_path"]
        try:
            h = open(meta["_html"], encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        # ---- Gen A listing cards
        if GEN_A_LISTS.match(p) and 'class="detail"' in h:
            surface = p.replace("-print", "")
            for m in re.finditer(r'<div class="detail">\s*<h3>(.*?)</h3>\s*(?:<p>(.*?)</p>)?\s*'
                                 r'(?:<a href="([^"]*)")?', h, re.S):
                name = text(m.group(1))
                if not name:
                    continue
                r = row(name)
                seen(r, meta, "gen-a:" + surface)
                para = m.group(2) or ""
                em = re.search(r"<em>(.*?)</em>", para, re.S)
                if em:
                    r["outcomes"].add(text(em.group(1)))
                    para = para[:em.start()]
                d = text(para).rstrip(" /")
                if d:
                    r["descriptions"].add(d)
                if m.group(3):
                    r["websites"].add(m.group(3).strip())
        # ---- Gen B per-company pages
        mm = re.match(r"^/portfolio/([a-z0-9][a-z0-9-]*)$", p)
        if mm and 'type-portfolio' in h:
            t = re.search(r'<h1[^>]*entry-title[^>]*>(.*?)</h1>', h, re.S)
            if t:
                name = text(t.group(1))
                r = row(name)
                seen(r, meta, "gen-b:company-page")
                g = r["gen_b"]
                g.setdefault("slug", mm.group(1))
                g["page_cite"] = g.get("page_cite") or cite(meta)
                sub = re.search(r'<div class="subheader">(.*?)</div>', h, re.S)
                if sub and text(sub.group(1)):
                    r["descriptions"].add(text(sub.group(1)))
                link = re.search(r'<div class="header-links[^"]*">\s*<a href="([^"]+)"', h)
                if link:
                    r["websites"].add(link.group(1))
                for k, v in re.findall(r'<h3 class="h6">([^<]+)</h3>\s*<p>(.*?)</p>', h, re.S):
                    g[k.strip().lower().replace(" ", "_")] = text(v)
                ct = re.search(r'\bcompany-type-([a-z-]+)', h)
                if ct:
                    g["type"] = ct.group(1)
            # the slider on every Gen B company page is the whole list
            for slug, name in re.findall(r'<a href="https?://www\.ivp\.com/portfolio/([a-z0-9-]+)/" class="post_nav-item">.*?'
                                         r'<div class="title">(.*?)</div>', h, re.S):
                r = row(text(name))
                seen(r, meta, "gen-b:portfolio-nav")
                r["gen_b"].setdefault("slug", slug)
        # ---- Gen C (2023 on, Nuxt 3): every page inlines the site-wide search
        # widget's company list in __NUXT_DATA__, i.e. the whole portfolio as
        # it stood on the capture date. Companies the firm has since removed
        # from the live site survive only here.
        if 'id="__NUXT_DATA__"' in h and (p.startswith("/portfolio") or p == "/"):
            nm = re.search(r'<script type="application/json"[^>]*id="__NUXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
            if nm:
                try:
                    st = devalue(json.loads(nm.group(1)))
                    comps = ((st.get("pinia") or {}).get("global") or {}).get("searchWidgetCompanies") or []
                except (ValueError, RecursionError, AttributeError, IndexError, KeyError, TypeError):
                    comps = []
                for c in comps:
                    if isinstance(c, dict) and c.get("name"):
                        r = row(c["name"])
                        seen(r, meta, "gen-c:search-widget")
                        r["gen_b"].setdefault("slug", c.get("slug") or "")
        # ---- Gen B listing page
        if p == "/portfolio" and "Portfolio Items" in h:
            for slug, name in re.findall(r'href="https?://www\.ivp\.com/portfolio/([a-z0-9-]+)/"[^>]*>.*?'
                                         r'(?:<div class="title">|<h\d[^>]*>)(.*?)</', h, re.S):
                if name.strip():
                    r = row(text(name))
                    seen(r, meta, "gen-b:portfolio")
                    r["gen_b"].setdefault("slug", slug)

    out = []
    for k, r in rows.items():
        caps_sorted = sorted(r["captures"])
        g = r["gen_b"]
        first_ts, first_cite, _ = caps_sorted[0]
        years = sorted({ts[:4] for ts, _, _ in caps_sorted})
        out.append({
            "slug": re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-"),
            "name": r["name"],
            "url": g.get("page_cite") or first_cite,
            "cc_first": first_ts[:8],
            "cc_last": caps_sorted[-1][0][:8],
            "cc_years": years,
            "listed_on": sorted(r["listed_on"]),
            "description": sorted(r["descriptions"], key=len)[-1] if r["descriptions"] else "",
            "outcome": "; ".join(sorted(r["outcomes"])),
            "company_site": sorted(r["websites"])[0] if r["websites"] else "",
            "invest_year": (g.get("year_invested") or "")[:4],
            "site_status": g.get("status", ""),
            "leadership": g.get("leadership", ""),
            "location": g.get("location", ""),
            "company_type": g.get("type", ""),
            "cc_slug": g.get("slug", ""),
        })
    out.sort(key=lambda r: r["name"].lower())
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "cc-listings.json").write_text(json.dumps({
        "_readme": ("Every company named on an archived ivp.com portfolio surface, 2013-2022, read from Common Crawl "
                    "captures (the Internet Archive excludes ivp.com; decisions.md D8, R1) by "
                    "scratch/parse-cc-ivp.py. Gen A (2013 to mid-2016): the listing pages' detail cards with the "
                    "firm's own one-line description and outcome line. Gen B (mid-2016 to 2022, WordPress): the "
                    "per-company pages with the firm's own Year Invested, Status, Location and Leadership, and the "
                    "portfolio slider every company page carries. `url` is the CC capture that cites the row: the "
                    "company's own archived page where one was captured, else the first listing capture naming it. "
                    "invest_year is the firm's own 'Year Invested' (an anchor, never a stage label)."),
        "_source": "https://index.commoncrawl.org/ (ivp.com/*, CC-MAIN-2013-20 through CC-MAIN-2022-49)",
        "_pulled": date.today().isoformat(),
        "rows": out,
    }, indent=1, ensure_ascii=False))
    print(f"cc-listings: {len(out)} companies")

    # ---- the archive layer proper: sources/wayback/parsed/<year>.json, one row
    # per company per capture year, citing its own CC capture (capture_url,
    # build-company-base.py 458fcc7). cc-listings.json above is the reference
    # copy with the firm's fields; this is what the build reads, so the capture
    # years date the listing (wayback_years, first_seen) and the layer counts
    # once toward tier.
    per_year: dict[str, dict[str, dict]] = defaultdict(dict)
    for k, r in rows.items():
        slug = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
        iy = (r["gen_b"].get("year_invested") or "")[:4]
        for ts, cite_url, surface in sorted(r["captures"]):
            y = ts[:4]
            # the current year's captures re-state the live site, which the
            # site layer already reads: counting them here would count one
            # listing twice toward tier
            if y >= str(date.today().year):
                continue
            if slug in per_year[y]:
                continue
            per_year[y][slug] = {
                "slug": slug, "name": r["name"],
                "path": "/portfolio/" + (r["gen_b"].get("slug") or slug) if surface.startswith("gen-b")
                        else surface.split(":", 1)[1],
                "snapshot_ts": ts, "capture_url": cite_url, "surface": surface,
                **({"invest_year": iy} if iy.isdigit() else {}),
            }
    pdir = INV / "sources/wayback/parsed"
    pdir.mkdir(parents=True, exist_ok=True)
    for y, rs in sorted(per_year.items()):
        (pdir / f"{y}.json").write_text(json.dumps(sorted(rs.values(), key=lambda x: x["slug"]),
                                                   indent=1, ensure_ascii=False) + "\n")
    print("parsed years:", {y: len(rs) for y, rs in sorted(per_year.items())})
    by = defaultdict(int)
    for r in out:
        for s in r["listed_on"]:
            by[s.split(":")[0]] += 1
    print(dict(by))

    # ---- archived news
    posts = {}
    for meta in caps:
        p = meta["_path"]
        if not re.match(r"^/news/(press-release|blog|podcast|ivp-news|portfolio-company-news)?/?[a-z0-9-]*", p):
            continue
        if p in ("/news", "/news/ivp-news", "/news/portfolio-company-news", "/news/events", "/news/blog",
                 "/news/podcast", "/news/press-release") or p.startswith("/news/category"):
            continue
        try:
            h = open(meta["_html"], encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        t = re.search(r"<title>(.*?)</title>", h, re.S)
        title = text(t.group(1)) if t else ""
        body = h
        for pat in (r'<div class="entry-content">(.*?)</div><!-- \.entry-content -->',
                    r'<article.*?</article>', r'<div id="content".*?<div id="sidebar"'):
            bm = re.search(pat, h, re.S)
            if bm:
                body = bm.group(0) if bm.lastindex is None else bm.group(1)
                break
        body = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S)
        key = p
        if key in posts:
            continue
        posts[key] = {"path": p, "url": cite(meta), "captured": meta["timestamp"][:8], "title": title,
                      "body": text(body)[:6000]}
    (OUT / "cc-posts.json").write_text(json.dumps({
        "_readme": ("IVP's archived news and press-release pages, 2013-2022, read from Common Crawl captures by "
                    "scratch/parse-cc-ivp.py. A post is class 1 for the round it NAMES; it asserts IVP's entry only "
                    "where it says so in words (COLLECTION.md 6). `captured` is the capture date, a ceiling on the "
                    "post's own date, never the round's date."),
        "_pulled": date.today().isoformat(),
        "rows": sorted(posts.values(), key=lambda x: x["path"]),
    }, indent=1, ensure_ascii=False))
    print(f"cc-posts: {len(posts)} pages")


if __name__ == "__main__":
    main()
