#!/usr/bin/env python3
"""Parse Project A's archived portfolio surfaces into the build's shape.

Sources (both captured, both valid citations, COLLECTION.md s1):
  - Common Crawl captures of project-a.com listed in sources/wayback/cc-manifest.json
    (bodies under data/filings/commoncrawl/project-a-ventures/<crawl>/, gitignored,
    re-downloadable by the manifest's filename/offset); capture_url is the
    index.commoncrawl.org form.
  - Internet Archive captures under sources/wayback/raw/ia/<ts>-<path>.html, listed
    in sources/wayback/ia-manifest.json; capture_url is the web.archive.org form.

Four site generations on project-a.com, one parser each:
  2012-2014  WordPress gallery: <a href=".../portfolio/<slug>/"> ... <h3>Name</h3>
  2015-2018  Kirby CMS: <div class="portfoliList__item [--former]" data-investment-themes=...>
             <a href=".../portfolio/<slug>"><img alt="Logo <Name>">
  2019       LogoTile grid: <a class="LogoTile" href=".../portfolio/<slug>"> + optional
             <div class="LogoTile__label">Exited</div>; names from the per-company pages
  2020-2024  Next.js on Contentful: __NEXT_DATA__ 'venture' records with headline,
             status, founded, dateOfInvestment, investment (round word), investmentType
             (VC / PE Co-Investment), location, segment, management, website
Per-company pages (2012-2019): name (h1/title), Founded, Location, Founders,
Investment (round word, exit line), Segment, Website.

Writes sources/wayback/parsed/<year>.json (rows: slug, name, path, snapshot_ts,
capture_url, filters, invest_year?) and sources/wayback/archive-evidence.json (per
company: every field each capture stated, with its capture_url), the judge's pack.

invest_year comes only from a Contentful dateOfInvestment read in a capture taken
before 2021-11 (DATE_TRUST_BEFORE): the late-2021 CMS migration rewrote the field
on every record (Voi read 2019-03-01 in 2020 and 2021-12-26 from 2022; rows created
later carry Sep-Dec 2021 dates whatever their real year).
"""
from __future__ import annotations

import html as H
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

WB = INV / "sources" / "wayback"
CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "project-a-ventures"
IA_RAW = WB / "raw" / "ia"
PLACEHOLDER_DATES = ("2021-12-25", "2021-12-26", "2021-12-24", "2021-12-27")
# The late-2021 CMS migration rewrote dateOfInvestment on every record: old rows
# moved to 2021-12-2x (Voi 2019-03-01 -> 2021-12-26) and rows created from then on
# carry Sep-Dec 2021 dates whatever their real year (Bucket 2021-11-14 against the
# live CMS's 2023). Only a capture taken before the migration states a real date.
DATE_TRUST_BEFORE = "20211101"


def slug_of(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")


def text(s: str) -> str:
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", H.unescape(s)).strip()


def captures():
    """(year, ts, path, capture_url, body) for every captured page, CC then IA."""
    man = json.loads((WB / "cc-manifest.json").read_text()) if (WB / "cc-manifest.json").exists() else {}
    for key, m in sorted(man.items()):
        if m.get("status") != "ok":
            continue
        f = CC_RAW / key
        if not f.exists():
            continue
        path = re.sub(r"^https?://(www\.)?project-a\.(com|vc)(:\d+)?", "", m["url"]) or "/"
        yield int(m["timestamp"][:4]), m["timestamp"], path, m["capture_url"], f.read_text(errors="replace")
    iam = json.loads((WB / "ia-manifest.json").read_text()) if (WB / "ia-manifest.json").exists() else {}
    for key, m in sorted(iam.items()):
        if m.get("status") != "ok":
            continue
        f = IA_RAW / key
        if not f.exists():
            continue
        path = re.sub(r"^https?://(www\.)?project-a\.(com|vc)(:\d+)?", "", m["url"]) or "/"
        yield int(m["timestamp"][:4]), m["timestamp"], path, m["capture_url"], f.read_text(errors="replace")


def is_listing(path: str) -> bool:
    return re.fullmatch(r"(/(en|de))?/portfolio/?", path.split("?")[0]) is not None


def company_slug(path: str) -> str | None:
    m = re.fullmatch(r"(?:/(?:en|de))?/portfolio/([^/?#]+)/?", path.split("?")[0])
    return m.group(1).lower() if m else None


def parse_wp_gallery(body):
    for m in re.finditer(r'<a href="[^"]*/portfolio/([^/"]+)/?">\s*<img[^>]*>\s*<div class="miniExcerpt">\s*<h3>(.*?)</h3>', body, re.S):
        yield {"slug": m.group(1).lower(), "name": text(m.group(2))}


def parse_kirby(body):
    for m in re.finditer(r'<div class="portfoliList__item([^"]*)"(?: data-investment-themes="([^"]*)")?[^>]*>\s*<a href="[^"]*/portfolio/([^"/?#]+)"[^>]*>\s*<img[^>]*alt="([^"]*)"', body, re.S):
        name = re.sub(r"^Logo\s+", "", H.unescape(m.group(4))).strip()
        yield {"slug": m.group(3).lower(), "name": name, "former": "--former" in m.group(1),
               "themes": [t.strip() for t in H.unescape(m.group(2) or "").split(";") if t.strip()]}


def parse_logotile(body):
    for m in re.finditer(r'<a class="LogoTile[^"]*" href="[^"]*/portfolio/([^"/?#]+)"[^>]*>(.*?)</a>', body, re.S):
        lab = re.search(r'LogoTile__label">(.*?)<', m.group(2))
        yield {"slug": m.group(1).lower(), "name": "", "label": text(lab.group(1)) if lab else ""}


def ventures(body):
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', body, re.S)
    if not m:
        return []
    out = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("contentType") == "venture" and o.get("headline"):
                out.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(json.loads(m.group(1)))
    return out


def rich_text(doc) -> str:
    bits = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("nodeType") == "text":
                bits.append(o.get("value") or "")
            if o.get("nodeType") == "hyperlink":
                bits.append(f" <{(o.get('data') or {}).get('uri', '')}> ")
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(doc)
    return re.sub(r"\s+", " ", "".join(bits)).strip()


def company_page(body) -> dict:
    t = text(body)
    out = {}
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = re.search(r"<title>(.*?)</title>", body, re.S)
    name = text(h1.group(1)) if h1 else ""
    if not name and title:
        tt = text(title.group(1))
        name = tt.split("|")[-1].strip() if tt.startswith("Project A") else tt.split("|")[0].strip()
    out["name"] = name
    for lab, key in (("Founded", "founded"), ("Gegründet", "founded"), ("Location", "location"),
                     ("Standort", "location"), ("Founder", "founders"), ("Gründer", "founders"),
                     ("Investment", "investment"), ("Investition", "investment"),
                     ("Segment", "segment"), ("Website", "website"), ("Webseite", "website")):
        m = re.search(rf"\b{lab}:?\s+(.{{1,160}}?)(?=\s(?:Founded|Gegründet|Location|Standort|Founder|Gründer|Investment|Investition|Segment|Website|Webseite)\b|$)", t)
        if m and key not in out and not m.group(1).startswith(("Themes", "Expertise")):
            out[key] = m.group(1).strip(" :")
    ex = re.search(r"(Exited (?:in|im) [^.]{3,120}?\))|(Exited (?:in|im) [A-Za-zäöü]+ \d{4}[^.]{0,80})", t)
    if ex:
        out["exit_line"] = ex.group(0).strip()
    return out


def main() -> None:
    by_year: dict[int, dict[str, dict]] = defaultdict(dict)
    ev: dict[str, dict] = defaultdict(lambda: {"names": {}, "captures": [], "fields": defaultdict(dict)})
    names_by_slug: dict[str, str] = {}

    def add(year, ts, path, cap, slug, name, **fields):
        slug = slug_of(slug)
        if not slug:
            return
        e = ev[slug]
        if name:
            e["names"].setdefault(name, cap)
            names_by_slug.setdefault(slug, name)
        e["captures"].append({"ts": ts, "path": path, "capture_url": cap})
        for k, v in fields.items():
            if v not in (None, "", [], {}):
                e["fields"][k].setdefault(str(v) if not isinstance(v, (list, dict)) else json.dumps(v, ensure_ascii=False), cap)
        row = by_year[year].get(slug)
        if row is None or ts < row["snapshot_ts"]:
            by_year[year][slug] = {"slug": slug, "name": name or "", "path": path,
                                   "snapshot_ts": ts, "capture_url": cap}
        elif name and not row["name"]:
            row["name"] = name

    pages = list(captures())
    # per-company pages first, so the 2019 logo grid can take their names
    for year, ts, path, cap, body in pages:
        s = company_slug(path)
        if s and not is_listing(path):
            f = company_page(body)
            add(year, ts, path, cap, s, f.pop("name", ""), **{f"page_{k}": v for k, v in f.items()})
    earliest_date: dict[str, tuple[str, str]] = {}
    for year, ts, path, cap, body in pages:
        if not is_listing(path) and path.rstrip("/") not in ("", "/en", "/de"):
            continue
        n = 0
        for r in parse_wp_gallery(body):
            add(year, ts, path, cap, r["slug"], r["name"], era="wp_gallery"); n += 1
        for r in parse_kirby(body):
            add(year, ts, path, cap, r["slug"], r["name"], era="kirby",
                former_flag="former" if r["former"] else "current", themes=r["themes"]); n += 1
        for r in parse_logotile(body):
            add(year, ts, path, cap, r["slug"], "", era="logotile", tile_label=r["label"] or "none"); n += 1
        for v in ventures(body):
            name = (v.get("headline") or "").strip()
            s = slug_of(name)
            d = (v.get("dateOfInvestment") or "")[:10]
            add(year, ts, path, cap, s, name, era="contentful",
                cf_status=v.get("status"), cf_founded=v.get("founded"), cf_investment=v.get("investment"),
                cf_investment_type=v.get("investmentType"), cf_location=(v.get("location") or "").replace("\n", " / "),
                cf_segment=v.get("segment"), cf_business_model=v.get("businessModel"),
                cf_management=(v.get("management") or "").replace("\n", ", "),
                cf_website=(v.get("website") or {}).get("url"), cf_subheadline=v.get("subheadline"),
                cf_text=rich_text(v.get("content"))[:1500], cf_id=v.get("id"), cf_created=v.get("createdAt"))
            if d and d not in PLACEHOLDER_DATES and ts < DATE_TRUST_BEFORE:
                prev = earliest_date.get(s)
                if prev is None or ts < prev[1]:
                    earliest_date[s] = (d, ts, cap)
            n += 1
        print(f"  {ts} {path:22} {n:4} rows", file=sys.stderr)
    # names for nameless rows (logo grid): the per-company page or another era
    for year, rows in by_year.items():
        for s, r in rows.items():
            if not r["name"] and s in names_by_slug:
                r["name"] = names_by_slug[s]
            if s in earliest_date:
                r["invest_year"] = earliest_date[s][0][:4]
    (WB / "parsed").mkdir(parents=True, exist_ok=True)
    for year, rows in sorted(by_year.items()):
        write_atomic(WB / "parsed" / f"{year}.json",
                     json.dumps(sorted(rows.values(), key=lambda r: r["slug"]), indent=1, ensure_ascii=False) + "\n")
        print(f"{year}: {len(rows)} companies")
    out = {}
    for s, e in sorted(ev.items()):
        caps = sorted(e["captures"], key=lambda c: c["ts"])
        out[s] = {"names": e["names"], "first_capture": caps[0], "last_capture": caps[-1],
                  "years": sorted({int(c["ts"][:4]) for c in caps}),
                  "fields": {k: v for k, v in e["fields"].items()}}
        if s in earliest_date:
            out[s]["date_of_investment"] = {"value": earliest_date[s][0], "capture_ts": earliest_date[s][1],
                                            "capture_url": earliest_date[s][2]}
    write_atomic(WB / "archive-evidence.json", json.dumps(
        {"_readme": __doc__.strip().splitlines()[0] + " Per company: names as rendered, first/last capture, years, and every field value with the capture that stated it.",
         "companies": out}, indent=1, ensure_ascii=False) + "\n")
    print(f"archive-evidence: {len(out)} slugs")


if __name__ == "__main__":
    main()
