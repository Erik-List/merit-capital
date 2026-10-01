#!/usr/bin/env python3
"""Parse the archived seedcamp.com list surfaces into sources/wayback/parsed/<year>.json.

Captures come from Common Crawl (scratch/cc-fetch.py; manifest in
sources/wayback/cc-manifest.json) while the Internet Archive is under its
machine-wide cooldown; wayback-pull.py later merges its own rows into the
same year files (keyed slug+path, COLLECTION.md s5). Every row carries the
capture's `capture_url` (the index.commoncrawl.org form), used verbatim as the
row's wayback_first_link (the IVP precedent).

Surfaces, by site generation:
  2008-2010  /pages/2007winners, /pages/2009winners: "this year's six Seedcamp
             companies", one <h2><a> per company (the programme's invested
             cohort; the finalists pages are NOT parsed: a finalist was not an
             investment, decisions.md D4).
  2012-2017  /companies/ and /companies/page/N/ (Genesis theme, one
             `h2.entry-title` per company, sector classes on the post div) and
             the per-company pages /companies/<slug>(/) (name from <title>).
  2017-2024  /our-startups/: the whole list as a `window.companies` JSON array
             (title, website, categories, exit flag, logo upload path), and
             /acquirer/<x>/ pages ("This company has been acquired by X").
  2024-2025  /company/<slug>/ pages (name from <title>).

Usage: python3 cc-parse.py
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

RAW = ROOT / "data" / "filings" / "commoncrawl" / "seedcamp"
MAN = INV / "sources" / "wayback" / "cc-manifest.json"
OUT = INV / "sources" / "wayback" / "parsed"
NON = set(json.loads((INV / "config.json").read_text())["wayback"]["non_company_slugs"])


def slug_of(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", html.unescape(s).lower()).strip("-")


def clean(s: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", s)).split())


def title_name(t: str) -> str | None:
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    if not m:
        return None
    n = clean(m.group(1))
    n = re.split(r"\s+[:|\-–]\s+Seedcamp\b", n)[0].strip()
    # 2016-2017 per-company pages title themselves "Grover with |" (an empty
    # Yoast variable after the name): the name is what precedes " with".
    n = re.sub(r"\s+with\s*\|?\s*$", "", n).strip(" |")
    return n or None


def parse(path: str, t: str) -> list[dict]:
    rows: list[dict] = []
    if re.match(r"^/pages/20\d\dwinners$", path):
        i = t.find("page_content")
        seg = t[i:t.find("</div>", i + 20)] if i >= 0 else ""
        for m in re.finditer(r"<h2>\s*<a href=\"([^\"]*)\"[^>]*>(.*?)</a>\s*</h2>", seg, re.S):
            rows.append({"name": clean(m.group(2)), "website": m.group(1), "surface": "winners"})
        # 2009 winners page is logo-only: the firm's own image filename is the
        # identity (COLLECTION.md s5, "a logo-only era is recoverable from the
        # image filename"); the row lands under the slug and the judge names it.
        for m in re.finditer(r'<a href="([^"]*)"><img src="[^"]*/images/([a-z0-9]+)_\d+\.(?:png|jpg|gif)"', seg):
            rows.append({"name": None, "slug_only": m.group(2), "website": m.group(1), "surface": "winners"})
    elif re.match(r"^/pages/scw(08|_2009)$", path):
        # the week page carries a Winners box and a Finalists box; only the
        # Winners were invested (decisions.md D2)
        w = re.search(r"<h3>\s*Winners\s*</h3>(.*?)</div>", t, re.S)
        if w:
            for m in re.finditer(r"<a(?: href=\"([^\"]*)\")?[^>]*>(.*?)</a>", w.group(1), re.S):
                if clean(m.group(2)):
                    rows.append({"name": clean(m.group(2)), "website": m.group(1), "surface": "winners"})
    elif re.match(r"^/companies/?(page/\d+/?)?$", path):
        # split on post boundaries: the 2012-2014 theme puts <!-- end --> comments
        # between the closing divs, so a block regex ending on </div></div>
        # swallows several companies at once
        for blk in re.split(r'(?=<div class="post-\d+ companies)', t)[1:]:
            a = re.search(r'<h2 class="entry-title"><a href="https?://(?:www\.)?seedcamp\.com/companies/([^/"]+)/?"[^>]*>(.*?)</a>', blk, re.S)
            if not a:
                continue
            sectors = re.findall(r"sectors-([a-z0-9-]+)", blk.split('"')[1])
            rows.append({"name": clean(a.group(2)), "site_slug": a.group(1), "filters": ",".join(sectors),
                         "surface": "companies-list"})
    elif re.match(r"^/companies/[^/]+/?$", path):
        n = title_name(t)
        if n and slug_of(n) not in NON:
            rows.append({"name": n, "site_slug": path.strip("/").split("/")[-1], "surface": "companies-page"})
    elif re.match(r"^/our-startups/?$", path):
        m = re.search(r"window\.companies\s*=\s*(\[.*?\]);", t, re.S)
        if m:
            for c in json.loads(m.group(1)):
                up = re.search(r"/uploads/(\d{4})/(\d{2})/", c.get("image") or "")
                rows.append({"name": clean(c["title"]), "website": c.get("url"),
                             "filters": ",".join(slug_of(x["name"]) for x in c.get("categories") or []),
                             "exit": bool(c.get("exit")),
                             "logo_upload": f"{up.group(1)}-{up.group(2)}" if up else None,
                             "description": clean(c.get("content") or ""),
                             "surface": "our-startups"})
    elif re.match(r"^/acquirer/[^/]+/?$", path):
        b = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
        acq = re.search(r"This company has been acquired by\s*(.*?)\.\s*<", b, re.S)
        n = title_name(t)
        # the page's <title> is the acquirer; the company is the first heading
        # the company is the first non-empty text <h2> after the header (the
        # first <h2>s hold the logo image or nothing)
        b = b[b.find("</header>"):] if "</header>" in b else b
        # only a heading BEFORE the acquisition sentence names the company: the
        # 2018+ template prints the sentence alone, and the first heading after
        # it is the footer's "Social" (a scrape artifact, ruled not_member)
        cut = b.find("This company has been acquired")
        b = b[:cut] if cut >= 0 else b
        h = next((clean(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", b, re.S) if clean(x)), None)
        if h and acq:      # most /acquirer/ pages are empty taxonomy shells
            rows.append({"name": h, "acquirer": clean(acq.group(1)) if acq else n,
                         "exit": True, "surface": "acquirer"})
    elif re.match(r"^/company/[^/]+/?$", path):
        n = title_name(t)
        if n:
            rows.append({"name": n, "site_slug": path.strip("/").split("/")[-1], "surface": "company-page"})
    return rows


# Curated identity fixes applied to the parsed rows (COLLECTION.md s5: fix a
# source-side variant in the PARSED SOURCE, not by a merge that would keep the
# wrong name on the surviving row). Keyed by (slug, website substring).
PARSED_RENAMES = {
    # two companies under one slug: the 2011 cohort's Fractal (HTML-to-email
    # tool, London; the 2012-2014 /companies list) and Fractal Labs (the 2015
    # Fund III seed investment, later branded Fractal, askfractal.com)
    ("fractal", "askfractal"): ("fractal-labs", "Fractal Labs"),
}


def main() -> None:
    man = json.loads(MAN.read_text())
    by_year: dict[str, dict[tuple, dict]] = defaultdict(dict)
    n_caps = 0
    for key, v in man.items():
        if v.get("status") != "ok":
            continue
        path = re.sub(r"^https?://(www\.)?seedcamp\.com", "", v["url"]).split("?")[0] or "/"
        f = RAW / key
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        rows = parse(path, t)
        if not rows:
            continue
        n_caps += 1
        year = v["timestamp"][:4]
        for r in rows:
            if not r.get("name") and not r.get("slug_only"):
                continue
            s = slug_of(r["name"]) if r.get("name") else r.pop("slug_only")
            if not s or s in NON:
                continue
            for (rs, dom), (ns, nn) in PARSED_RENAMES.items():
                if s == rs and dom in (r.get("website") or ""):
                    s, r["name"] = ns, nn
            row = {"slug": s, **({"name": r["name"]} if r.get("name") else {}), "path": path, "snapshot_ts": v["timestamp"],
                   "capture_url": v["capture_url"], **{k: x for k, x in r.items() if k not in ("name", "slug_only") and x not in (None, "")}}
            k = (s, path)
            prev = by_year[year].get(k)
            if prev is None or row["snapshot_ts"] < prev["snapshot_ts"]:
                by_year[year][k] = row
    OUT.mkdir(parents=True, exist_ok=True)
    for year, rows in sorted(by_year.items()):
        f = OUT / f"{year}.json"
        old = json.loads(f.read_text()) if f.exists() else []
        merged = {(r["slug"], r["path"]): r for r in old}
        merged.update(rows)
        write_atomic(f, json.dumps(sorted(merged.values(), key=lambda r: (r["slug"], r["path"])),
                                   indent=1, ensure_ascii=False) + "\n")
        print(year, len(rows), "rows from CC,", len(merged), "in file")
    print(n_caps, "captures parsed")


if __name__ == "__main__":
    main()
