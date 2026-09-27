#!/usr/bin/env python3
"""Pull coatue.com (Next.js 13 on Contentful) into file_list sources.

coatue.com renders every page server-side with its Contentful data inside
`__NEXT_DATA__`, and the portfolio grid and the blog lists page through two
Next API routes the site's own JS calls (escalation ladder step 3):

  GET /api/portfolio?id=<PortfolioGrid sys.id>&skip=N[&types[]=..&statuses[]=..]
      -> {total, items[{name, url, type, status, logo, logoWithColor, sys}]}
      `type` is the grid's "Initial investment" filter (Venture | Growth);
      `status` is Active | Exit. 48 rows per page.
  GET /api/articles?skip=N[&blogCategorySlug=..]   -> {total, items}
  GET /api/quick-takes?skip=N                       -> {total, items} (bodies inline)

Writes, under data/collection/investors/coatue/sources/site/:
  portfolio-2026.json   every row of /portfolio, the firm's own type and status
  posts.json            every /blog/<category>/<slug> page: title, date, category,
                        authors, body text (the announcement archive)
  quick-takes.json      every /c/takes/<slug>: title, date, body text
Raw payloads are cached under scratch/site-raw/ so a re-run is offline.
Usage: python3 data/collection/investors/coatue/scratch/pull-site-coatue.py [--refresh]
"""
from __future__ import annotations
import json, re, subprocess, sys, time
from datetime import date
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/coatue"
RAW = INV / "scratch/site-raw"
OUT = INV / "sources/site"
BASE = "https://www.coatue.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36 MeritCapitalResearch/1.0 (erik@meritcapit.al)"
REFRESH = "--refresh" in sys.argv
TODAY = date.today().isoformat()


def get(url: str) -> bytes:
    last = None
    for attempt in range(4):
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True)
        body, _, code = r.stdout.rpartition(b"\n")
        if r.returncode == 0 and code == b"200":
            time.sleep(0.35)
            return body
        last = (r.returncode, code)
        time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"fetch failed: {url} {last}")


def cached(name: str, url: str) -> bytes:
    p = RAW / name
    if p.exists() and not REFRESH:
        return p.read_bytes()
    b = get(url)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(b)
    return b


def next_data(html: bytes) -> dict:
    m = re.search(rb'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.S)
    return json.loads(m.group(1)) if m else {}


def rich_text(node) -> str:
    """Contentful rich text -> plain text with paragraph breaks."""
    if node is None:
        return ""
    if isinstance(node, list):
        return "".join(rich_text(n) for n in node)
    t = node.get("nodeType")
    if t == "text":
        return node.get("value", "")
    inner = rich_text(node.get("content", []))
    if t in ("paragraph", "heading-1", "heading-2", "heading-3", "heading-4", "list-item", "blockquote"):
        return inner.strip() + "\n"
    if t == "hyperlink":
        return inner
    return inner


# The published name is the brand in normal capitalisation (COLLECTION.md 8, 2026-09-24). Where the
# firm's page carries a legal name, a misspelling or an odd rendering, the brand is set HERE, at the
# parsed source, and the page's own rendering is kept as site_name (the First Round precedent:
# a merge would keep the junk name on the surviving row).
NAME_FIXES = {
    "Alchemy Insights": "Alchemy", "Snap Group": "Snap", "By Mason": "Mason", "Mei tuan": "Meituan", "Coreweave": "CoreWeave",
    "Dbt Labs": "dbt Labs", "Classin": "ClassIn", "BitDeer": "Bitdeer", "Cloudwalk": "CloudWalk", "Xpeng": "XPeng",
    "Endeavor Group Holdings": "Endeavor", "CHAGEE Singapore": "Chagee", "Weidan": "Weidian", "Valsoft Corporation": "Valsoft",
    "Reliable Robotics (Air)": "Reliable Robotics", "Relativity": "Relativity Space", "Persona Identities": "Persona",
    "Komodo": "Komodo Health", "Wisdom AI": "WisdomAI", "Meticulous Ai": "Meticulous", "PingCap": "PingCAP", "Moonpay": "MoonPay",
    "Decidehq": "DecideHQ", "Tencent Music Entertainment Group": "Tencent Music Entertainment", "Opendoor Technologies": "Opendoor",
    "Infinitus Systems": "Infinitus", "Device Plane": "Deviceplane", "Didi Global": "DiDi", "VIPkid": "VIPKid", "NDEA": "Ndea",
    "ATTAbotics": "Attabotics", "FlexCompute": "Flexcompute", "GuMing": "Guming", "Norm Ai": "Norm Ai", "Jetpack.io": "Jetify",
    "Karat Financial": "Karat", "Juul Labs": "Juul", "Oscar": "Oscar Health", "Lyra": "Lyra Health", "Stability": "Stability AI",
    "Root Insurance": "Root", "Youxinpai": "Uxin", "Kujiale": "Manycore Tech", "Auris": "Auris Health", "Jet": "Jet.com",
}


def portfolio() -> list[dict]:
    html = cached("portfolio.html", f"{BASE}/portfolio")
    d = next_data(html)
    grid = next(s for s in d["props"]["pageProps"]["page"]["sectionsCollection"]["items"]
                if s.get("__typename") == "PortfolioGrid")
    gid = grid["sys"]["id"]
    rows, skip, total = [], 0, None
    while total is None or skip < total:
        b = cached(f"api-portfolio-{skip:04d}.json", f"{BASE}/api/portfolio?{urlencode({'id': gid, 'skip': skip})}")
        j = json.loads(b)
        total = int(j["total"])
        items = j["items"]
        if not items:
            break
        rows.extend(items)
        skip += len(items)
    out = []
    for it in rows:
        logo = (it.get("logoWithColor") or it.get("logo") or {}).get("src")
        site_name = (it.get("name") or "").strip()
        out.append({"cms_id": it["sys"]["id"], "name": NAME_FIXES.get(site_name, site_name), "site_name": site_name, "url": f"{BASE}/portfolio",
                    "company_site": it.get("url"), "initial_investment": it.get("type"), "status_site": it.get("status"),
                    "logo": logo})
    print(f"portfolio: {len(out)} rows (site total {total})", file=sys.stderr)
    return out


def sitemap_urls() -> list[str]:
    xml = cached("sitemap.xml", f"{BASE}/sitemap.xml").decode()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def articles() -> list[dict]:
    listed, skip, total = [], 0, None
    while total is None or skip < total:
        j = json.loads(cached(f"api-articles-{skip:04d}.json", f"{BASE}/api/articles?{urlencode({'skip': skip})}"))
        total = int(j["total"]); items = j["items"]
        if not items:
            break
        listed.extend(items); skip += len(items)
    api_slugs = {(a.get("blogCategory") or {}).get("slug"): None for a in listed}
    urls = {f"{BASE}/blog/{(a.get('blogCategory') or {}).get('slug')}/{a['slug']}" for a in listed}
    urls |= {u for u in sitemap_urls() if "/blog/" in u}
    posts = []
    for u in sorted(urls):
        slug = u.split("/blog/", 1)[1]
        try:
            d = next_data(cached(f"blog/{slug.replace('/', '__')}.html", u))
        except RuntimeError as e:
            print(f"  post failed: {u}: {e}", file=sys.stderr); continue
        pp = d.get("props", {}).get("pageProps", {})
        art = pp.get("article") or pp.get("page") or {}
        body = art.get("content") or art.get("body") or {}
        text = rich_text(body.get("json")) if isinstance(body, dict) else ""
        authors = [a.get("name") for a in ((art.get("authorsCollection") or {}).get("items") or []) if a]
        posts.append({"url": u, "slug": slug, "category": slug.split("/")[0], "title": art.get("heading") or art.get("title"),
                      "subheading": art.get("subheading"), "date": art.get("date"), "author": art.get("author"),
                      "authors": authors, "text": text.strip(), "_keys": sorted(art.keys())[:30]})
    print(f"posts: {len(posts)} ({len(listed)} via API, {len(urls)} urls)", file=sys.stderr)
    return posts


def quick_takes() -> list[dict]:
    rows, skip, total = [], 0, None
    while total is None or skip < total:
        j = json.loads(cached(f"api-quick-takes-{skip:04d}.json", f"{BASE}/api/quick-takes?{urlencode({'skip': skip})}"))
        total = int(j["total"]); items = j["items"]
        if not items:
            break
        rows.extend(items); skip += len(items)
    out = []
    for it in rows:
        authors = [a.get("name") for a in ((it.get("authorsCollection") or {}).get("items") or []) if a]
        out.append({"url": f"{BASE}/c/takes/{it['slug']}", "slug": it["slug"], "title": it.get("heading"),
                    "date": it.get("date"), "authors": authors, "text": rich_text((it.get("content") or {}).get("json")).strip()})
    print(f"quick takes: {len(out)}", file=sys.stderr)
    return out


def write(name: str, rows: list[dict], readme: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps({"_readme": readme, "_source": BASE, "_pulled": TODAY,
                                        "_script": "scratch/pull-site-coatue.py", "rows": rows}, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    write("portfolio-2026.json", portfolio(),
          "Every row of coatue.com/portfolio read through the site's own /api/portfolio route (48 per page, keyed by the PortfolioGrid's Contentful id). initial_investment is the grid's 'Initial investment' filter (Venture | Growth), the firm's own claim about the round it entered; status_site is the grid's Active | Exit. No year, round word beyond the two-way split, or sector is published.")
    write("quick-takes.json", quick_takes(), "Every /c/takes/<slug> quick take via /api/quick-takes, body text flattened from Contentful rich text.")
    write("posts.json", articles(), "Every /blog/<category>/<slug> page (the API's article list unioned with the sitemap), read from each page's __NEXT_DATA__: title, date, category, authors, body text. The announcement archive: partnership and investment posts name rounds.")
