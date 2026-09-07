#!/usr/bin/env python3
"""Battery's people pages, enumerated from people-sitemap.xml.

Same shape as pull-site-companies.py and for the same reason: the `people`
post type is not REST-exposed. Each profile carries the firm's own title,
office, LinkedIn and -- unusually -- a first-party "Joined Battery in <year>",
which dates a tenure START better than a CDX snapshot span can. The archive
still owns the DEPARTED partners and the end dates; this layer is the current
roster and the joined-year, unioned into partner-roster.py via team.json.

Output: sources/site/team-pages.json (a file_list source for site-portfolio.py)
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
SITEMAP = "https://www.battery.com/people-sitemap.xml"
P = Paths("battery-ventures")
OUT = P.site / "team-pages.json"
RAW = P.scratch / "people-raw"

H1 = re.compile(r'<h1 class="h1-2 nm">\s*(?P<name>[^<]+?)\s*</h1>', re.S)
META = re.compile(r'<div class="hp1-bio-meta">(.*?)</div>\s*</div>', re.S)
CELL = re.compile(r"<div>([^<]+?)</div>")
LI = re.compile(r'href="(https://www\.linkedin\.com/in/[^"]+)"')
X = re.compile(r'href="(https://(?:twitter\.com|x\.com)/(?!batteryventures)[^"]+)"')
JOINED = re.compile(r"Joined Battery in (\d{4})")


def txt(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def fetch(url: str, tries: int = 4) -> str:
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
    m = H1.search(html)
    if not m:
        return None
    row = {"slug": url.rstrip("/").rsplit("/", 1)[-1],
           "name": txt(m.group("name")), "url": url}
    blocks = META.findall(html)
    if blocks:
        cells = [txt(c) for c in CELL.findall(blocks[0])]
        cells = [c for c in cells if c]
        if cells:
            row["title"] = cells[0]
        if len(cells) > 1:
            row["office"] = cells[1]
    j = JOINED.search(html)
    if j:
        row["joined"] = j.group(1)
    focus = re.search(r"Focus Areas:\s*([^<]+)", html)
    if focus:
        row["focus_areas"] = txt(focus.group(1))
    li = LI.search(html)
    if li:
        row["linkedin_url"] = li.group(1)
    x = X.search(html)
    if x:
        row["x_url"] = x.group(1)
    return row


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    urls = sorted(set(re.findall(
        r"<loc>(https://www\.battery\.com/people/[^<]+)</loc>", fetch(SITEMAP))))
    print(f"sitemap: {len(urls)} people URLs")

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
    write_atomic(OUT, json.dumps({
        "_readme": ("Battery's own people pages, one fetch per URL in "
                    "people-sitemap.xml, parsed by scratch/pull-site-people.py "
                    "(raw cached under scratch/people-raw/). Carries the firm's "
                    "title, office, joined-year, focus areas and socials. This "
                    "is the CURRENT roster only; departed partners come from "
                    "the Wayback CDX people namespace."),
        "_source": SITEMAP,
        "_pulled": time.strftime("%Y-%m-%d"),
        "rows": rows}, indent=1))
    from collections import Counter
    print(f"wrote {OUT}: {len(rows)} people")
    print("  titles:", dict(Counter(r.get("title", "-") for r in rows).most_common(12)))
    print("  offices:", dict(Counter(r.get("office", "-") for r in rows).most_common(10)))
    print("  with joined-year:", sum(1 for r in rows if r.get("joined")))


if __name__ == "__main__":
    main()
