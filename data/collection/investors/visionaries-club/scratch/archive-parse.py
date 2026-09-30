#!/usr/bin/env python3
"""Parse the firm's archived portfolio listings into sources/wayback/parsed/<year>.json.

visionaries.vc has four generations (config.json wayback._eras_note):

  - before 2020: a Japanese Toastmasters club on the same domain; never read.
  - 2020-2023 Gatsby: the HTML shell is empty ("Back to top"), the portfolio
    rides in /page-data/index/page-data.json (Internet Archive captures).
  - 2023-2025 WordPress: /portfolio/ ("Portfolio Links Archive") lists every
    company as `a.portfolio__list__link` with a modal carrying the company's
    site, a description and the firm's thesis (Common Crawl captures).
  - 2026 Kirby: the live single page, read through site_api, not here.

Every row carries its exact capture URL: the Common Crawl index form for a CC
capture, the web.archive.org form for an Internet Archive one (COLLECTION.md s1:
a capture URL is a valid citation). A year file is the union of that year's
captures; a company's first capture in the year supplies its citation.
Parsed files merge rather than replace (keyed slug+path), per COLLECTION.md s5.

Usage: python3 archive-parse.py
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

WB = INV / "sources" / "wayback"
PARSED = WB / "parsed"
CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "visionaries-club"
IA_RAW = WB / "raw"


def slug_of(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def txt(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def wp_rows(body: str) -> list[dict]:
    """One row per `portfolio__list__link` on a WordPress /portfolio/ page."""
    out = []
    for m in re.finditer(r'portfolio__list__link js-portfolio-link"[^>]*>(.*?)</a>(.*?)(?=portfolio__list__link js-portfolio-link"|</ul>)',
                         body, re.S):
        name = txt(m.group(1))
        modal = m.group(2)
        site = re.search(r'<a href="(https?://[^"]+)" target="_blank">', modal)
        desc = re.search(r'<p class="t-base@sm t-14 t-center mb-2">(.*?)</p>', modal, re.S)
        if name:
            out.append({"name": name, "website": site.group(1) if site else "",
                        "description": txt(desc.group(1)) if desc else ""})
    return out


def gatsby_rows(data: dict) -> list[dict]:
    """Company entries from a Gatsby page-data.json: any object carrying a
    name/title and a company url, found under the page's result tree. The
    shape is read, not assumed: every dict with a 'name' or 'title' plus a
    link-like field is a candidate, filtered to the portfolio section."""
    out = []

    def walk(o, path):
        if isinstance(o, dict):
            keys = set(o)
            nm = o.get("name") or o.get("title") or o.get("companyName")
            link = o.get("url") or o.get("link") or o.get("website") or o.get("companyUrl")
            if isinstance(nm, str) and isinstance(link, str) and "portfolio" in path.lower():
                out.append({"name": nm.strip(), "website": link, "description": o.get("description") or ""})
            for k, v in o.items():
                walk(v, path + "/" + k)
        elif isinstance(o, list):
            for v in o:
                walk(v, path)

    walk(data, "")
    return out


def main() -> None:
    years: dict[int, dict[str, dict]] = {}

    def add(year: int, rows: list[dict], path: str, ts: str, capture_url: str, era: str) -> None:
        bucket = years.setdefault(year, {})
        for r in rows:
            key = slug_of(r["name"]) + "|" + path
            if key in bucket:
                continue
            bucket[key] = {"slug": slug_of(r["name"]), "name": r["name"], "path": path,
                           "snapshot_ts": ts, "capture_url": capture_url, "era": era,
                           "website": r.get("website", ""), "description": r.get("description", "")}

    # Common Crawl: WordPress /portfolio/
    man = json.loads((WB / "cc-manifest.json").read_text())
    for key, v in sorted(man.items(), key=lambda kv: kv[1]["timestamp"]):
        if v.get("status") != "ok":
            continue
        path = re.sub(r"https?://(www\.)?visionaries\.vc", "", v["url"]).split("?")[0]
        if path != "/portfolio/":
            continue
        body = (CC_RAW / key).read_text(encoding="utf-8", errors="replace")
        rows = wp_rows(body)
        add(int(v["timestamp"][:4]), rows, path, v["timestamp"], v["capture_url"], "wordpress")

    # Internet Archive: WordPress /portfolio/ and Gatsby page-data, where fetched
    for f in sorted((IA_RAW / "portfolio").glob("*.html")) if (IA_RAW / "portfolio").exists() else []:
        ts = f.stem
        body = f.read_text(encoding="utf-8", errors="replace")
        add(int(ts[:4]), wp_rows(body), "/portfolio/", ts,
            f"https://web.archive.org/web/{ts}/https://visionaries.vc/portfolio/", "wordpress")
    for f in sorted((IA_RAW / "page-data").glob("*.json")) if (IA_RAW / "page-data").exists() else []:
        ts = f.stem
        try:
            data = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except ValueError:
            continue
        add(int(ts[:4]), gatsby_rows(data), "/page-data/index/page-data.json", ts,
            f"https://web.archive.org/web/{ts}/https://visionaries.vc/page-data/index/page-data.json", "gatsby")

    PARSED.mkdir(parents=True, exist_ok=True)
    for year, bucket in sorted(years.items()):
        f = PARSED / f"{year}.json"
        old = {r["slug"] + "|" + r["path"]: r for r in json.loads(f.read_text())} if f.exists() else {}
        old.update(bucket)
        rows = sorted(old.values(), key=lambda r: (r["slug"], r["path"]))
        write_atomic(f, json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
        print(year, len(rows), "rows")


if __name__ == "__main__":
    main()
