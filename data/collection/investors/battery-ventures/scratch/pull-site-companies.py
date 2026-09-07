#!/usr/bin/env python3
"""Battery's per-company detail pages, enumerated from company-sitemap.xml.

Escalation ladder step 5 with a twist: battery.com is WordPress and answers
/wp-json/wp/v2/types, but the `company` post type is NOT REST-exposed and the
/company/ index loads its cards over admin-ajax. What IS public is the Yoast
company sitemap (351 URLs) plus a per-company detail page whose markup is
regular and unusually rich:

    <h1 class="h1-2 nm"><a href="<company site>">Name</a></h1>
    <div class="comp-writeup">description</div>
    <div class="comp-detail-row"><div class="comp-det-sub">SECTORS|INVESTED|
        STATUS|Location|STAGE</div><div>value</div></div>
    <a href="/people/<slug>/" class="comp-team-row"><div class="part-name">..
        <div class="comp-team-tite">title</div>

So the rows come from 351 detail fetches rather than one listing, which no
site-portfolio.py parser does; this writes the union as a `file_list` source
(COLLECTION.md 5, ladder step 4/5) so the config stays reproducible.

INVESTED is the firm's own investment year and STAGE its own Early / Growth /
Buyout label -- the layer PRO-97's control-position delta turns on. Neither is
trusted as a label until the calibration gate scores it (COLLECTION.md 4).
"""
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = "merit-capital-research/1.0 (list.erik.2005@gmail.com)"
SITEMAP = "https://www.battery.com/company-sitemap.xml"
P = Paths("battery-ventures")
OUT = P.site / "company-pages.json"
RAW = P.scratch / "site-raw"

DETAIL = re.compile(
    r'<div class="comp-det-sub">\s*(?P<k>[^<]+?)\s*</div>\s*<div>\s*'
    r'(?P<v>.*?)\s*</div>', re.S)
TEAM = re.compile(
    r'href="https://www\.battery\.com/people/(?P<slug>[^"/]+)/"[^>]*'
    r'class="comp-team-row.*?<div class="part-name">\s*(?P<name>[^<]+?)\s*</div>'
    r'\s*<div class="comp-team-tite">\s*(?P<title>[^<]*?)\s*</div>', re.S)
H1 = re.compile(r'<h1 class="h1-2 nm">\s*(?:<a href="(?P<site>[^"]*)"[^>]*>)?\s*'
                r'(?P<name>.*?)\s*(?:</a>)?\s*</h1>', re.S)
WRITEUP = re.compile(r'<div class="comp-writeup">(.*?)</div>', re.S)
LINKEDIN = re.compile(r'href="(https://www\.linkedin\.com/company/[^"]+)"')


def txt(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def fetch(url: str, tries: int = 4) -> str:
    """curl, not urlopen: the repo's convention (site-portfolio.py) and the
    only one that gets a verified chain on this machine."""
    for i in range(tries):
        try:
            return subprocess.run(
                ["curl", "-sfL", "--max-time", "60", "-H", f"User-Agent: {UA}", url],
                capture_output=True, check=True).stdout.decode("utf-8", "replace")
        except subprocess.CalledProcessError:
            if i == tries - 1:
                print(f"  FAILED {url}")
                return ""
            time.sleep(1.5 * (i + 1))
    return ""


def parse(url: str, html: str) -> dict | None:
    if not html:
        return None
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    m = H1.search(html)
    if not m:
        return None
    row = {"slug": slug, "name": txt(m.group("name")), "url": url}
    if m.group("site"):
        row["company_site"] = m.group("site")
    w = WRITEUP.search(html)
    if w:
        row["description"] = txt(w.group(1))
    li = LINKEDIN.search(html)
    if li:
        row["linkedin"] = li.group(1)
    for d in DETAIL.finditer(html):
        k, v = d.group("k").strip().lower(), txt(d.group("v"))
        if not v:
            continue
        if k == "sectors":
            row["sectors"] = [s.strip() for s in v.split(",") if s.strip()]
        elif k == "invested":
            row["invest_year"] = v
        elif k == "status":
            row["site_status"] = v
        elif k == "location":
            row["site_location"] = v
        elif k == "stage":
            row["site_stage"] = v
    team = [{"slug": t.group("slug"), "name": txt(t.group("name")),
             "title": txt(t.group("title"))} for t in TEAM.finditer(html)]
    if team:
        row["team"] = team
        row["partners"] = [t["name"] for t in team]
    return row


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    urls = re.findall(r"<loc>(https://www\.battery\.com/company/[^<]+)</loc>",
                      fetch(SITEMAP))
    urls = sorted(set(urls))
    print(f"sitemap: {len(urls)} company URLs")

    def one(u: str):
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        cache = RAW / f"{slug}.html"
        html = cache.read_text(encoding="utf-8", errors="replace") \
            if cache.exists() and cache.stat().st_size > 2000 else ""
        if not html:
            html = fetch(u)
            if html:
                write_atomic(cache, html)
        return parse(u, html)

    with ThreadPoolExecutor(max_workers=4) as ex:
        rows = [r for r in ex.map(one, urls) if r]

    rows.sort(key=lambda r: r["name"].lower())
    payload = {
        "_readme": (
            "Battery's own company pages, one fetch per URL in "
            "https://www.battery.com/company-sitemap.xml, parsed by "
            "scratch/pull-site-companies.py (re-runnable; raw HTML cached "
            "under scratch/site-raw/). Fields are the firm's own: sectors, "
            "invest_year (its INVESTED year), site_status (free text), "
            "site_location, site_stage (Early|Growth|Buyout) and the per-deal "
            "Battery Team with titles. site_stage and invest_year are scored "
            "on the calibration gate before either is trusted as a label."),
        "_source": SITEMAP,
        "_pulled": time.strftime("%Y-%m-%d"),
        "rows": rows,
    }
    write_atomic(OUT, json.dumps(payload, indent=1))
    from collections import Counter
    print(f"wrote {OUT}: {len(rows)} rows")
    print("  stage:", dict(Counter(r.get("site_stage", "-") for r in rows)))
    print("  status:", dict(Counter(r.get("site_status", "-")[:18] for r in rows).most_common(6)))
    print("  with invest_year:", sum(1 for r in rows if r.get("invest_year")))
    print("  with partners:", sum(1 for r in rows if r.get("partners")))


if __name__ == "__main__":
    main()
