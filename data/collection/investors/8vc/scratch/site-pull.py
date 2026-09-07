#!/usr/bin/env python3
"""Pull 8vc.com's four first-party people/company surfaces into file_list sources.

www.8vc.com is Webflow with no public read API (COLLECTION.md §5 ladder step 5:
the .wf_graphql endpoint is the site editor's, not a public query API), so this
fetches the sitemap's own URLs and parses the server-rendered CMS bindings.

Four surfaces, three of them people:
  /companies/<slug>  -> sources/site/webflow-companies.json   (the portfolio)
  /team/<slug>       -> sources/site/team-webflow.json        (the firm's roster)
  /advisors/<slug>   -> sources/site/advisors.json            (Advisor Upside network)
  /fellows/<slug>    -> sources/site/fellows.json             (8VC Fellowship)

The last two are NOT roster input (config.json roster._note): they are outside
people who are related persons on their own companies' Form Ds. They are pulled
because read the other way round they are first-party company lists.

Usage: python3 site-pull.py [companies|team|advisors|fellows|all]
"""
import gzip
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
P = Paths("8vc")
SITE = P.root / "sources" / "site"
RAW = P.root / "scratch" / "site-raw"


def get(url: str, tries: int = 3) -> str:
    for i in range(tries):
        r = subprocess.run(["curl", "-sfL", "--max-time", "45", "-A", UA, url],
                           capture_output=True)
        if r.returncode == 0:
            return r.stdout.decode("utf-8", errors="replace")
        time.sleep(1.0 * (i + 1))
    return ""


def cached(url: str, key: str) -> str:
    """Fetch once, keep the page gzipped: 744 Webflow pages are 52 MB raw, 13 MB stored."""
    RAW.mkdir(parents=True, exist_ok=True)
    gz, plain = RAW / f"{key}.html.gz", RAW / f"{key}.html"
    if gz.exists() and gz.stat().st_size > 200:
        with gzip.open(gz, "rt", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    if plain.exists() and plain.stat().st_size > 500:
        return plain.read_text(encoding="utf-8", errors="replace")
    t = get(url)
    if t:
        with gzip.open(gz, "wt", encoding="utf-8") as fh:
            fh.write(t)
    return t


def clean(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def sitemap_urls() -> list[str]:
    t = cached("https://www.8vc.com/sitemap.xml", "_sitemap")
    return re.findall(r"<loc>([^<]+)</loc>", t)


def info_cells(t: str) -> dict:
    """The four CMS fields in the details rail. Empty ones carry w-dyn-bind-empty."""
    out = {}
    for m in re.finditer(
            r'<div class="info-cell_small-text">([^<]+)</div>'
            r'<div class="heading-small-h4([^"]*)">([^<]*)</div>', t):
        label, cls, val = m.group(1).strip(), m.group(2), clean(m.group(3))
        if "w-dyn-bind-empty" in cls or not val:
            continue
        out[label.lower()] = val
    return out


def parse_company(t: str, slug: str, url: str) -> dict:
    name = clean(re.search(r"<h1>(.*?)</h1>", t, re.S).group(1)) if re.search(r"<h1>", t) else slug
    tags = [clean(m) for m in re.findall(
        r'<div class="card-tag is-uppercase">.*?<div class="text-size-small">([^<]+)</div>', t, re.S)]
    desc = ""
    m = re.search(r'\[overview\](.*?)(?:<div VC-links-wrapper|<div class="border-line)', t, re.S)
    if m:
        desc = clean(m.group(1))
    if not desc:
        m = re.search(r'<meta name="description" content="([^"]*)"', t)
        desc = html.unescape(m.group(1)) if m else ""
    cells = info_cells(t)
    links = {}
    for lid, key in (("website-link", "url"), ("twitter-link", "twitter"),
                     ("linkedin-link", "linkedin")):
        m = re.search(rf'id="{lid}"[^>]*href="([^"]+)"', t)
        if m:
            links[key] = m.group(1)
    return {
        "slug": slug, "name": name, "url": links.get("url", ""),
        "sectors_site": tags, "description": desc,
        "site_stage": cells.get("stage", ""), "site_founded": cells.get("founded", ""),
        "site_region": cells.get("region", ""), "site_fund": cells.get("fund", ""),
        "twitter": links.get("twitter", ""), "linkedin": links.get("linkedin", ""),
        "source": url,
    }


def parse_person(t: str, slug: str, url: str) -> dict:
    """One /team/ or /advisors/ page.

    The team card renders the site group ("Investment Team", "Operations") and
    the person's office ("Austin, TX") as two `text-size-small` divs inside one
    `card-tag is-grey`; the bio is the [overview] rich-text block. Advisor pages
    are empty shells (robots.txt disallows /advisors and nothing is server
    rendered), so those rows come back name-only — recorded, not hidden.
    """
    m = re.search(r"<h1>(.*?)</h1>", t, re.S)
    name = clean(m.group(1)) if m else slug.replace("-", " ").title()
    tags = [clean(x) for x in re.findall(
        r'<div class="card-tag is-(?:grey|uppercase)">.*?</div>(.*?)</div></div>', t, re.S)]
    card = re.search(r'<div class="card-tag is-grey">(.*?)</div></div></div>', t, re.S)
    parts = [clean(x) for x in re.findall(
        r'<div class="text-size-small">([^<]+)</div>', card.group(1))] if card else []
    bio = ""
    b = re.search(r'\[overview\](.*?)(?:<div class="border-line|<div VC-links-wrapper)', t, re.S)
    if b:
        bio = clean(b.group(1))
    cells = info_cells(t)
    li = re.search(r'href="(https://[^"]*linkedin\.com/[^"]+)"', t)
    tw = re.search(r'href="(https://(?:twitter|x)\.com/[^"]+)"', t)
    return {
        "slug": slug, "name": name, "url": url,
        "group": parts[0] if parts else "", "office": parts[1] if len(parts) > 1 else "",
        "tags": tags, "title": cells.get("title", "") or cells.get("role", ""),
        "company": cells.get("company", ""), "bio": bio,
        "linkedin_url": li.group(1) if li else "", "x_url": tw.group(1) if tw else "",
        "source": url,
    }


def pull(kind: str, prefix: str, parser, outfile: str, listkey: str) -> None:
    urls = [u for u in sitemap_urls() if f"/{prefix}/" in u]
    rows, missing = [], []
    for i, u in enumerate(urls, 1):
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        t = cached(u.replace("https://8vc.com", "https://www.8vc.com"), f"{prefix}-{slug}")
        if not t:
            missing.append(slug)
            continue
        rows.append(parser(t, slug, u))
        if i % 25 == 0:
            print(f"  {prefix}: {i}/{len(urls)}", flush=True)
    payload = {
        "_readme": (f"8vc.com /{prefix}/ pages, fetched from the site's own sitemap.xml "
                    f"by scratch/site-pull.py. {len(rows)} rows"
                    + (f", {len(missing)} unfetchable ({', '.join(missing[:8])})" if missing else "")
                    + ". The list is keyed both as \"rows\" (what site-portfolio.py's file_list "
                      "parser reads) and under its own name, so the file is readable either way."),
        "rows": rows,
        listkey: rows,
    }
    SITE.mkdir(parents=True, exist_ok=True)
    write_atomic(SITE / outfile, json.dumps(payload, indent=1, ensure_ascii=False))
    print(f"wrote {outfile}: {len(rows)} rows ({len(missing)} missing)")


def parse_post(t: str, slug: str, url: str) -> dict:
    """One /resources/ page: the firm's own announcement and essay archive.

    COLLECTION.md §6: an announcement is class 1 for the round it NAMES, and
    asserts an ENTRY only where the post says so in words (the Menlo inversion —
    a firm announces the round it LED, regularly a follow-on). Title, published
    date, author and body are all kept so the judge can tell "Announcing our
    investment in X" from "we first invested in X's seed two years ago".
    """
    m = re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S)
    title = clean(m.group(1)) if m else slug
    tail = t[t.index("</h1>"):] if "</h1>" in t else t
    d = re.search(r'class="created-at-text">([^<]+)</div>', tail)
    fmt = re.findall(r'data-element-(?:format|category)="" class="text-size-small(?: w-condition-invisible)?">([^<]+)<', t)
    author = ""
    a = re.search(r'href="/team/([a-z0-9-]+)"', t)
    if a:
        author = a.group(1)
    body = ""
    b = re.search(r'<div class="insight-rich-text[^"]*w-richtext">(.*?)</div>\s*<div class="(?:border-line|scrolled)', t, re.S)
    if not b:
        b = re.search(r'<div class="insight-rich-text[^"]*w-richtext">(.*?)</section>', t, re.S)
    if b:
        body = clean(b.group(1))[:6000]
    return {"slug": slug, "title": title, "date": d.group(1).strip() if d else "",
            "kinds": [x.strip() for x in dict.fromkeys(fmt)], "author_slug": author,
            "body": body, "url": url}


JOBS = {
    "companies": ("companies", parse_company, "webflow-companies.json", "companies-live"),
    "team": ("team", parse_person, "team-webflow.json", "team"),
    "advisors": ("advisors", parse_person, "advisors.json", "advisors"),
    "fellows": ("fellows", parse_person, "fellows.json", "fellows"),
    "resources": ("resources", parse_post, "resources.json", "posts"),
}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, (prefix, parser, out, listkey) in JOBS.items():
        if which in ("all", k):
            pull(k, prefix, parser, out, listkey)
