#!/usr/bin/env python3
"""Pull IVP's own site (ivp.com, Nuxt 3) into file_list sources.

ivp.com is a prerendered Nuxt 3 site. Every route ships its data as a static
`<route>/_payload.json?<buildId>` in devalue form, served without auth, so the
whole site reads without the CMS API (cms.ivp.com, which the page config
fronts with a shared basic-auth pair we deliberately do not use).

Writes, under data/collection/investors/ivp/sources/site/:
  company-pages.json  every /portfolio/<slug> the sitemap lists: the firm's own
                      investmentDate, "moments" (Founded / Partnered lines),
                      status, sectors, deal team, website, leadership, and the
                      funding-announcement link
  posts.json          every /content/<slug>: title, date, category, the linked
                      company, and the body text (announcements name rounds)
  team-pages.json     every /team/<slug>: title, group, socials, bio

Raw payloads are cached under scratch/site-raw/ so a re-run is offline.
Usage: python3 data/collection/investors/ivp/scratch/pull-site-ivp.py [--refresh]
"""
from __future__ import annotations

import html
import json
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/ivp"
RAW = INV / "scratch/site-raw"
OUT = INV / "sources/site"
BASE = "https://www.ivp.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
REFRESH = "--refresh" in sys.argv

sys.setrecursionlimit(1_000_000)


def get(url: str) -> bytes:
    for attempt in range(4):
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            time.sleep(0.4)
            return body
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url} rc={r.returncode} code={code!r}")


def cached(name: str, url: str) -> bytes:
    p = RAW / name
    if p.exists() and not REFRESH:
        return p.read_bytes()
    b = get(url)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b)
    return b


def devalue(arr):
    memo = {}

    def rev(i):
        if i in memo:
            return memo[i]
        v = arr[i]
        if isinstance(v, list):
            if v and isinstance(v[0], str) and v[0] in (
                    "Reactive", "ShallowReactive", "Ref", "ShallowRef", "EmptyRef",
                    "EmptyShallowRef", "Set", "Map", "Date", "NuxtError", "Island", "undefined"):
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


def payload(route: str, build: str) -> dict:
    name = (route.strip("/").replace("/", "__") or "home") + ".json"
    url = f"{BASE}/{route.strip('/')}/_payload.json?{build}" if route.strip("/") else f"{BASE}/_payload.json?{build}"
    d = devalue(json.loads(cached(name, url)))
    data = d.get("data") or {}
    merged = {}
    for v in data.values():
        if isinstance(v, dict):
            merged.update(v)
    return merged


def text_of(s: str | None) -> str:
    if not s:
        return ""
    s = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\xa0]+", " ", s)
    return re.sub(r"\n\s*\n+", "\n", s).strip()


def main() -> None:
    home = get(f"{BASE}/portfolio/").decode("utf-8", "replace")
    build = re.search(r'buildId:"([0-9a-f-]+)"', home).group(1)
    sitemap = cached("sitemap.xml", f"{BASE}/sitemap.xml").decode()
    locs = [re.sub(r"^https?://[^/]+", "", u) for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)]
    companies = sorted({u.strip("/").split("/")[1] for u in locs
                        if u.startswith("/portfolio/") and u.strip("/").count("/") == 1})
    posts = sorted({u.strip("/").split("/")[1] for u in locs
                    if u.startswith("/content/") and u.strip("/").count("/") == 1})
    people = sorted({u.strip("/").split("/")[1] for u in locs
                     if u.startswith("/team/") and u.strip("/").count("/") == 1})
    print(f"build {build}: {len(companies)} companies, {len(posts)} posts, {len(people)} people")

    # the listing carries hideFromPortfolioLanding and the listing order
    listing = payload("portfolio", build).get("paginatedItems", {}).get("items", [])
    listed = {c["slug"]: c for c in listing}

    rows = []
    for slug in companies:
        c = payload(f"portfolio/{slug}", build).get("company") or {}
        lc = listed.get(slug, {})
        moments = [m.strip() for m in (c.get("moments") or "").splitlines() if m.strip()]
        rows.append({
            "slug": slug,
            "name": c.get("name") or lc.get("name"),
            "url": f"{BASE}/portfolio/{slug}/",
            "company_site": c.get("websiteUrl") or "",
            "headline": c.get("headline") or lc.get("headline") or "",
            "description": text_of(c.get("body"))[:1200],
            "invest_date": c.get("investmentDate") or lc.get("investmentDate"),
            "invest_year": (c.get("investmentDate") or lc.get("investmentDate") or "")[:4],
            "moments": moments,
            "site_status": (c.get("status") or lc.get("status") or {}).get("name"),
            "sectors": [s.get("name") for s in (lc.get("sectors") or []) if isinstance(s, dict)],
            "partners": [t.get("fullName") for t in (c.get("teamMembers") or []) if isinstance(t, dict)],
            "leadership": c.get("leadership") or "",
            "announcement_url": (BASE + c["linkUrl"]) if (c.get("linkUrl") or "").startswith("/") else (c.get("linkUrl") or ""),
            "linkedin": c.get("linkedinLinkUrl") or "",
            "twitter": c.get("twittterLinkUrl") or "",
            "listed_on_landing": slug in listed and not lc.get("hideFromPortfolioLanding"),
            "cms_created": lc.get("createdAt"),
        })
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "company-pages.json").write_text(json.dumps({
        "_readme": ("IVP's own company pages: every /portfolio/<slug> in https://www.ivp.com/sitemap.xml, read from "
                    "the prerendered Nuxt payload (<route>/_payload.json, devalue form, no auth) by "
                    "scratch/pull-site-ivp.py. Fields are the firm's own: investmentDate (a year, stored as "
                    "YYYY-01-01), the 'moments' lines (Founded / Partnered / IPO / Acquired), the status filter "
                    "(Active | Public | Acquired), the sector filter, the per-company IVP team, the company "
                    "website and the link to IVP's own funding announcement."),
        "_source": f"{BASE}/sitemap.xml",
        "_pulled": date.today().isoformat(),
        "_build": build,
        "rows": rows,
    }, indent=1, ensure_ascii=False))

    prow = []
    for slug in posts:
        p = payload(f"content/{slug}", build)
        post = p.get("contentPost") or p.get("post") or next((v for v in p.values() if isinstance(v, dict) and v.get("slug") == slug), {})
        comp = post.get("company") or {}
        comps = [x.get("slug") for x in (post.get("companies") or []) if isinstance(x, dict)]
        body = "\n".join(text_of(b) for b in [post.get("body"), post.get("introduction"), post.get("description")] if b)
        # page-builder blocks: pageComponents[].instance.{heading, body, quote, ...}
        for blk in post.get("pageComponents") or []:
            inst = (blk or {}).get("instance") if isinstance(blk, dict) else None
            if not isinstance(inst, dict):
                continue
            for kk in ("largeHeading", "heading", "body", "text", "content", "copy", "quote", "attribution"):
                if isinstance(inst.get(kk), str) and inst[kk].strip():
                    body += "\n" + text_of(inst[kk])
        if post.get("featuredExcerpt"):
            body = text_of(post["featuredExcerpt"]) + "\n" + body
        prow.append({
            "slug": slug,
            "url": f"{BASE}/content/{slug}/",
            "title": post.get("title") or "",
            "date": post.get("publishDate") or post.get("date") or post.get("publishedAt") or post.get("createdAt"),
            "category": ((post.get("contentCategory") or {}).get("name")),
            "company": comp.get("slug") if isinstance(comp, dict) else None,
            "companies": comps,
            "external_url": post.get("externalLinkUrl") or "",
            "body": body.strip(),
            "_keys": sorted(post.keys()),
        })
    (OUT / "posts.json").write_text(json.dumps({
        "_readme": ("IVP's own content archive: every /content/<slug> in the sitemap, read from the Nuxt payload "
                    "by scratch/pull-site-ivp.py. Announcements name the round IVP led, which is regularly a "
                    "follow-on, so a post is class 1 for the round it NAMES and asserts an entry only where it "
                    "says so in words (COLLECTION.md 6)."),
        "_source": f"{BASE}/sitemap.xml",
        "_pulled": date.today().isoformat(),
        "rows": prow,
    }, indent=1, ensure_ascii=False))

    # the team landing page carries each person's category (Investors |
    # Operators) and sub-categories; the person pages carry title and socials
    landing = payload("team", build).get("teamMembersPage", {}).get("items", [])
    cats = {}
    for it in landing:
        subs = [s for s in (it.get("teamSubcategories") or []) if isinstance(s, dict)]
        cats[it.get("slug")] = {
            "group": sorted({(s.get("teamCategory") or {}).get("name") for s in subs} - {None}),
            "subgroups": sorted({s.get("name") for s in subs} - {None, "All"}),
        }
    trow = []
    for slug in people:
        p = payload(f"team/{slug}", build)
        m = p.get("teamMember") or next((v for v in p.values() if isinstance(v, dict) and v.get("slug") == slug), {})
        c = cats.get(slug, {})
        trow.append({
            "slug": slug,
            "name": m.get("fullName") or m.get("name"),
            "url": f"{BASE}/team/{slug}/",
            "title": m.get("fullTitle") or m.get("abbreviatedTitle") or "",
            "abbreviated_title": m.get("abbreviatedTitle") or "",
            "group": "; ".join(c.get("group") or []),
            "subgroups": c.get("subgroups") or [],
            "on_landing": slug in cats,
            "focus_areas": m.get("focusAreas") or "",
            "linkedin_url": m.get("linkedinProfileUrl") or "",
            "x_url": m.get("twitterProfielUrl") or "",
            "companies": [x.get("slug") for x in (m.get("companies") or []) if isinstance(x, dict)],
            "bio": text_of(m.get("bio") or m.get("introduction"))[:1500],
        })
    (OUT / "team-pages.json").write_text(json.dumps({
        "_readme": "IVP's own team pages: every /team/<slug> in the sitemap, from the Nuxt payload (scratch/pull-site-ivp.py).",
        "_source": f"{BASE}/sitemap.xml",
        "_pulled": date.today().isoformat(),
        "rows": trow,
    }, indent=1, ensure_ascii=False))
    print(f"wrote {len(rows)} companies, {len(prow)} posts, {len(trow)} people")


if __name__ == "__main__":
    main()
