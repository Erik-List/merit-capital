#!/usr/bin/env python3
"""Parse Kleiner Perkins' archived portfolio pages (kpcb.com, Common Crawl) into
sources/wayback/parsed/<year>.json, the shape build-company-base.py reads.

Eras (each parsed row carries its own capture_url, the index.commoncrawl.org form,
used verbatim as the row's wayback_first_link; COLLECTION.md s1):
  portfolio-php   2008-2011: /portfolio/portfolio.php[?view] and /portfolio/index.html, rows
                  <p class="company"><a href=URL>Name</a><br>description<br>City, ST</p>; the
                  view (private a-z, public, a sector or initiative) is kept as `list`.
  china-php       the separate KPCB China listing, /china/english/portfolio/ (X1): the same
                  markup, every row tagged team "China" and list "china".
  company-page    2012 on: /companies/<slug>, one row per slug per year in which the index holds
                  a 200 capture; content (Status, Teams, Initiative, URL, description, Partners,
                  Categories) from that year's fetched capture, else the nearest fetched one.
  kp-tiles        kleinerperkins.com /partnerships/[view]/ (2018 on), three shapes: 2018-20 Rails logo tiles
                  (<div class="tile ..."> with the name in the img alt, a /case-study/<slug> link), 2021-24 Gatsby
                  logo grid (<div class="company company-tiny"><a id="<site slug>" href="<company website>">, no
                  name rendered: the name is resolved through the website domain against the live CMS and the
                  other eras, else left empty so the row is named by the judge), 2025 on WordPress archive (img
                  alt, company website). The view (all, alumni, consumer, enterprise, fintech, hardtech,
                  health-care) is kept as `lists`; the page's og:title ("Alumni Partnerships") too.

`filters` carries the site's category tags and the partner slugs (build-company-base.py
reads roster slugs out of it as partners_site). A catch-all shell (one digest served for
more than two slugs) is dropped (COLLECTION.md s5).
Usage: python3 kp-parse.py
"""
import collections
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

IDX = HERE / "cc-index-raw.json"
MAN = HERE.parent / "sources" / "wayback" / "cc-manifest.json"
RAW = ROOT / "data" / "filings" / "commoncrawl" / "kleiner-perkins"
OUT = HERE.parent / "sources" / "wayback" / "parsed"
DOM = r"^https?://(?:www\.)?(?:kpcb|kleinerperkins)\.com(?::\d+)?"
COMPANY_PAGE = re.compile(DOM + r"/(china/)?compan(?:ies|y)/([^/?#]+)/?$", re.I)
KP_LIST = re.compile(DOM + r"/+partnerships(?:/([a-z-]+))?/?$", re.I)
PHP_LIST = re.compile(DOM + r"/+(portfolio/(?:portfolio\.php|index\.html)?|china/english/portfolio/?)(?:\?(.*))?$", re.I)
NOT_COMPANY = {"index", "all", "page", "search", "feed", "category"}


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", " and ")).strip("-")
    return s


def read(key):
    b = (RAW / key).read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return b.decode("latin-1")


def parse_php_list(body):
    rows = []
    for m in re.finditer(r'<p class="company">\s*(?:<a [^>]*href="([^"]*)"[^>]*>([\s\S]*?)</a>|([^<]+))'
                         r'\s*<br\s*/?>([\s\S]*?)</p>', body, re.I):
        url, name_a, name_t, rest = m.group(1), m.group(2), m.group(3), m.group(4)
        name = clean(name_a or name_t)
        parts = [clean(x) for x in re.split(r"<br\s*/?>", rest, flags=re.I)]
        parts = [p for p in parts if p]
        desc = parts[0] if parts else ""
        loc = parts[-1] if len(parts) > 1 else ""
        if name:
            rows.append({"name": name, "company_site": url or "", "about": desc, "location": loc})
    return rows


def field_block(t, label, stops):
    """Text lines after `label` up to the next stop label, in the de-tagged page."""
    m = re.search(r"\n" + re.escape(label) + r"\n([\s\S]*?)\n(?:" + "|".join(map(re.escape, stops)) + r")\n", t)
    return m.group(1) if m else ""


def parse_company_page(body):
    """The 2012-2017 Rails page: <h1>Name</h1>, a <dl> of Status / Teams / Initiative / URL / Twitter,
    <section class="summary">, and partner figures linking /partner/<slug> with a figcaption name."""
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", body, flags=re.I)
    out = {}
    m = re.search(r'<article>[\s\S]*?<h1[^>]*>([\s\S]*?)</h1>', s) or re.search(r"<h1[^>]*>([\s\S]*?)</h1>", s)
    name = clean(m.group(1)) if m else ""
    if not name or name.lower() in ("partners", "kleiner perkins caufield byers"):
        m = re.search(r"<title>([\s\S]*?)</title>", s, re.I)
        name = re.split(r"\s+[\u2014\-|]\s+(?:Kleiner|KPCB)", clean(m.group(1)) if m else "")[0].strip()
    out["name"] = name
    dl = {}
    for m in re.finditer(r"<dt>([\s\S]*?)</dt>\s*<dd>([\s\S]*?)</dd>", s, re.I):
        dl[clean(m.group(1)).lower()] = m.group(2)
    out["status_site"] = clean(dl.get("status", ""))
    out["team"] = [clean(x) for x in re.findall(r"<a [^>]*>([\s\S]*?)</a>", dl.get("teams", ""))] or \
        [x.strip() for x in clean(dl.get("teams", "")).split(",") if x.strip()]
    out["initiative"] = [clean(x) for x in re.findall(r"<a [^>]*>([\s\S]*?)</a>", dl.get("initiative", ""))] or \
        [x.strip() for x in clean(dl.get("initiative", "")).split(",") if x.strip()]
    m = re.search(r'href="(https?://[^"]+)"', dl.get("url", ""))
    out["company_site"] = m.group(1) if m else clean(dl.get("url", ""))
    m = re.search(r'<section class="summary">([\s\S]*?)</section>', s)
    out["about"] = clean(m.group(1)) if m else ""
    partners = []
    for m in re.finditer(r'href="/(?:china/)?partner/([a-z0-9-]+)"[\s\S]*?<figcaption>([\s\S]*?)</figcaption>'
                         r'(?:[\s\S]*?<strong class="title">([\s\S]*?)</strong>)?', s):
        partners.append((m.group(1), clean(m.group(2)), clean(m.group(3) or "")))
    out["partners"] = sorted({p[1] for p in partners if p[1]})
    out["partner_slugs"] = sorted({p[0] for p in partners})
    out["partner_titles"] = {p[1]: p[2] for p in partners if p[1]}
    m = re.search(r'<[^>]*class="categories"[^>]*>([\s\S]*?)</(?:section|ul|div)>', s)
    out["categories"] = [clean(x) for x in re.findall(r"<a [^>]*>([\s\S]*?)</a>", m.group(1))] if m else []
    return out


def main():
    idx = json.loads(IDX.read_text())
    man = {}
    for _mf in sorted(MAN.parent.glob("cc-manifest*.json")):
        man.update(json.loads(_mf.read_text()))
    per_year = collections.defaultdict(dict)   # year -> (slug, path) -> row
    stats = collections.Counter()

    # ---- listing eras (every fetched capture is parsed on its own year)
    for key, v in sorted(man.items()):
        if v.get("status") != "ok":
            continue
        m = PHP_LIST.match(v["url"])
        if not m:
            continue
        china = "china" in m.group(1).lower()
        view = (m.group(2) or "").strip() or ("china" if china else "private-a-z")
        body = read(key)
        y = v["timestamp"][:4]
        rows = parse_php_list(body)
        stats[f"{'china' if china else 'php'} {y}"] += len(rows)
        for r in rows:
            slug = slugify(r["name"])
            k = (slug, v["path"])
            if k in per_year[y]:
                per_year[y][k].setdefault("lists", [])
                if view not in per_year[y][k]["lists"]:
                    per_year[y][k]["lists"].append(view)
                continue
            per_year[y][k] = {
                "slug": slug, "name": r["name"], "path": v["path"], "snapshot_ts": v["timestamp"],
                "capture_url": v["capture_url"], "filters": "", "era": "china-php" if china else "portfolio-php",
                "about": r["about"], "location": r["location"], "company_site": r["company_site"],
                "team": ["China"] if china else [], "lists": [view], "content_ts": v["timestamp"]}

    # ---- kleinerperkins.com listings (2018 on)
    dom_name = {}
    live = json.loads((HERE.parent / "sources" / "site" / "company-list.json").read_text())["rows"]
    for r in live:
        d = re.sub(r"^https?://(www\.)?", "", (r.get("company_site") or "").lower()).split("/")[0]
        if d:
            dom_name.setdefault(d, r["name"])
    for yrs in per_year.values():
        for r in yrs.values():
            d = re.sub(r"^https?://(www\.)?", "", (r.get("company_site") or "").lower()).split("/")[0]
            if d and r.get("name"):
                dom_name.setdefault(d, r["name"])
    for key, v in sorted(man.items()):
        if v.get("status") != "ok":
            continue
        m = KP_LIST.match(v["url"].split("?")[0])
        if not m:
            continue
        view = m.group(1) or "all"
        body = read(key)
        y = v["timestamp"][:4]
        og = re.search(r'og:title" content="([^"]*)"', body)
        og = html.unescape(og.group(1)) if og else ""
        rows = []
        # 2018: <div class="tile tile--company"><figure><a href=/case-study/..><img alt=Name>; 2019-20: <a href=site
        # class="tile tile--company"><figure><img alt="Name Logo">
        for m2 in re.finditer(r'<(?:div|a)\b([^>]*class="tile tile--company[^"]*"[^>]*)>([\s\S]*?)</figure>', body):
            opener, t = m2.group(1), m2.group(2)
            a = re.search(r'alt="([^"]*)"', t)
            h = re.search(r'href="([^"]*)"', opener) or re.search(r'href="([^"]*)"', t)
            if a and a.group(1).strip():
                nm = re.sub(r"\s+logo$", "", html.unescape(a.group(1)).strip(), flags=re.I).strip()
                rows.append((nm, (h.group(1) if h else ""), ""))
        for m2 in re.finditer(r'<div class="company company-[a-z]+"><a id="([^"]+)" href="([^"]*)"', body):
            sid, site = m2.group(1), html.unescape(m2.group(2))
            d = re.sub(r"^https?://(www\.)?", "", site.lower()).split("/")[0]
            rows.append((dom_name.get(d, ""), site, sid))
        for t in re.findall(r'<li class="wp-block-post[^"]*company[^"]*">([\s\S]*?)</li>', body):
            a = re.search(r'alt="([^"]*)"', t)
            h = re.search(r'<a href="([^"]*)"', t)
            if a and a.group(1).strip():
                rows.append((html.unescape(a.group(1)).strip(), (h.group(1) if h else ""), ""))
        stats[f"kp-tiles {y}"] += len(rows)
        for name, link, sid in rows:
            slug = sid or slugify(name)
            if not slug:
                continue
            k = (slug, "/partnerships/")
            if k in per_year[y]:
                if view not in per_year[y][k]["lists"]:
                    per_year[y][k]["lists"].append(view)
                continue
            site = link if link.startswith("http") and "kleinerperkins.com" not in link else ""
            per_year[y][k] = {
                "slug": slug, "name": name, "path": "/partnerships/", "snapshot_ts": v["timestamp"],
                "capture_url": v["capture_url"], "filters": "", "era": "kp-tiles", "page_title": og,
                "company_site": site, "case_study": link if "/case-study/" in link else "",
                "site_id": sid, "lists": [view], "content_ts": v["timestamp"]}

    # ---- per-company pages: years from the index, content from the fetched bodies
    caps = collections.defaultdict(dict)
    for cid, slots in idx.items():
        for _k, v in slots.items():
            for r in v.get("records", []):
                m = COMPANY_PAGE.match(r["url"])
                if not m or r.get("status") != "200":
                    continue
                slug = m.group(2).lower().rstrip(".")
                if slug in NOT_COMPANY:
                    continue
                y = r["timestamp"][:4]
                cur = caps[slug].get(y)
                if cur is None or r["timestamp"] < cur[0]:
                    caps[slug][y] = (r["timestamp"], cid, r["url"], r.get("digest"), bool(m.group(1)))
    bodies = collections.defaultdict(dict)   # slug -> year -> (key, manifest row)
    for k, v in man.items():
        if v.get("status") != "ok":
            continue
        m = COMPANY_PAGE.match(v["url"])
        if m:
            bodies[m.group(2).lower().rstrip(".")][v["timestamp"][:4]] = (k, v)
    dig_slugs = collections.defaultdict(set)
    for slug, ys in caps.items():
        for y, c in ys.items():
            if c[3]:
                dig_slugs[c[3]].add(slug)
    shell = {d for d, s in dig_slugs.items() if len(s) > 2}
    parsed_cache = {}
    for slug, ys in sorted(caps.items()):
        for y, (ts, cid, url, dig, china_path) in sorted(ys.items()):
            if dig in shell:
                stats["shell"] += 1
                continue
            have = bodies.get(slug, {})
            pick = have.get(y) or (have[min(have, key=lambda yy: abs(int(yy) - int(y)))] if have else None)
            info = {}
            if pick:
                k, mv = pick
                if mv.get("digest") in shell:
                    stats["shell"] += 1
                    continue
                if k not in parsed_cache:
                    parsed_cache[k] = parse_company_page(read(k))
                info = parsed_cache[k]
                content_ts = mv["timestamp"]
            else:
                content_ts = ""
                stats["no body"] += 1
            path = re.sub(DOM, "", url, flags=re.I).split("?")[0]
            from urllib.parse import quote
            row = {"slug": slug, "name": info.get("name", ""), "path": path, "snapshot_ts": ts,
                   "capture_url": f"https://index.commoncrawl.org/{cid}-index?url={quote(url, safe='')}&output=json",
                   "filters": ",".join(info.get("categories", []) + info.get("partner_slugs", [])),
                   "era": "company-page", "about": info.get("about", ""),
                   "status_site": info.get("status_site", ""), "team": info.get("team", []) + (["China"] if china_path else []),
                   "initiative": info.get("initiative", []), "partners": info.get("partners", []),
                   "partner_titles": info.get("partner_titles", {}),
                   "categories": info.get("categories", []), "company_site": info.get("company_site", ""),
                   "content_ts": content_ts}
            per_year[y][(slug, path)] = row
            stats[f"page {y}"] += 1
    OUT.mkdir(parents=True, exist_ok=True)
    for y, rows in sorted(per_year.items()):
        write_atomic(OUT / f"{y}.json", json.dumps(sorted(rows.values(), key=lambda r: (r["slug"], r["path"])),
                                                   indent=1, ensure_ascii=False) + "\n")
    for k, n in sorted(stats.items()):
        print(k, n)
    print({y: len(r) for y, r in sorted(per_year.items())})


if __name__ == "__main__":
    main()
