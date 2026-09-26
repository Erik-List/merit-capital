#!/usr/bin/env python3
"""Atomico's current CMS (Hygraph behind a Next.js site), read from the archive.

atomico.com sits behind a Vercel bot checkpoint, so the live pages are not
read here; the Internet Archive holds the site's own server-rendered pages,
each carrying the CMS record in __NEXT_DATA__ (COLLECTION.md §5 escalation
ladder, step 3). Two surfaces:

  /partners/<slug>   one page per company, current and exited: name, the
                     sidebar's "Investment year", "Investment lead",
                     "Stage" (Venture | Growth), "Status" (Current | Exited),
                     "Location", "Areas of interest", the company's website,
                     the hero description and founders line.
  /partners          the listing (40 per page plus the 16 prioritised rows),
                     read only to confirm names and the exit marker.

Every capture of every /partners/<slug> URL is enumerated from the CDX index;
the NEWEST 200 capture of each is parsed (the CMS record as it last stood),
and every capture's year is kept as `years_listed` (the listing-era evidence
for first_seen). A slug whose newest capture cannot be read falls back to the
next newest.

Writes sources/site/cms-partners.json (a file_list source for
scripts/site-portfolio.py).

Usage: python3 cms-pull.py [--limit N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
RAW = HERE / "cms-raw"
NON_COMPANY = {"[slug]", "--navy", "--section-padding", "--navy80", "--text-color"}


def cdx_rows(pattern: str) -> list[list[str]]:
    url = ("https://web.archive.org/cdx/search/cdx?url=" + pattern +
           "&output=json&fl=timestamp,original,statuscode&filter=statuscode:200&limit=20000")
    body, code = ia_fetch.get(url)
    if code != "200":
        raise SystemExit(f"CDX {pattern}: {code} — rerun later (never read as empty)")
    data = json.loads(body or b"[]")
    return data[1:] if data else []


def next_data(html: str) -> dict | None:
    m = re.search(r'<script id="__NEXT_DATA__" type="application/json"[^>]*>(.*?)</script>',
                  html, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def rich(node) -> str:
    if isinstance(node, dict):
        if "text" in node:
            return node["text"]
        return " ".join(rich(c) for c in node.get("children", []))
    if isinstance(node, list):
        return " ".join(rich(c) for c in node)
    return ""


def parse_company(d: dict) -> dict:
    pp = d.get("props", {}).get("pageProps", {})
    hero = pp.get("hero") or {}
    side = {}
    for it in (pp.get("sidebar") or {}).get("items", []):
        c = it.get("content")
        if isinstance(c, dict):
            v = c.get("label")
        elif isinstance(c, list):
            v = [x.get("label") for x in c if isinstance(x, dict)]
        else:
            v = c
        side[it.get("title")] = v
    socials = (pp.get("sidebar") or {}).get("socials") or {}
    web = (socials.get("website") or {}).get("url")
    lead = side.get("Investment lead")
    if isinstance(lead, list):
        lead = "; ".join(x for x in lead if x)
    body = " ".join(rich(b.get("content")) for b in pp.get("pageContent") or []
                    if isinstance(b, dict) and b.get("type") == "Text")
    news = [{"slug": n.get("slug"), "title": n.get("title"), "date": n.get("publishedDate")}
            for n in (pp.get("latestNews") or {}).get("list", [])]
    return {
        "name": (hero.get("title") or "").strip(),
        "pretitle": (hero.get("pretitle") or "").strip(),
        "subtitle": " ".join(rich(hero.get("subtitle")).split())[:600],
        "invest_year": str(side.get("Investment year") or "").strip() or None,
        "lead": lead or None,
        "stage_site": side.get("Stage"),
        "status_site": side.get("Status"),
        "location_site": side.get("Location"),
        "themes": side.get("Areas of interest") if isinstance(side.get("Areas of interest"), list)
        else ([side["Areas of interest"]] if side.get("Areas of interest") else []),
        "website": web,
        "body": " ".join(body.split())[:1500],
        "news": news,
    }


def build_local() -> None:
    """Parse every capture already on disk (archive and Common Crawl alike),
    newest first per slug, and write the source file. The Common Crawl
    captures (scratch/cc-pull.py) carry their index-query citation."""
    cc = json.loads((RAW / "cc-captures.json").read_text()) if (RAW / "cc-captures.json").exists() else {}
    by_slug: dict[str, list[tuple[str, Path, str]]] = {}
    for f in RAW.glob("*.html"):
        m = re.match(r"^(.*)-(cc)?(\d{14})\.html$", f.name)
        if not m:
            continue
        slug, is_cc, ts = m.group(1), bool(m.group(2)), m.group(3)
        if is_cc:
            cite = (cc.get(slug) or {}).get("citation") or ""
        else:
            cite = f"https://web.archive.org/web/{ts}/https://atomico.com/partners/{slug}"
        by_slug.setdefault(slug, []).append((ts, f, cite))
    out, misses = [], []
    for slug, caps in sorted(by_slug.items()):
        rec = None
        for ts, f, cite in sorted(caps, reverse=True):
            d = next_data(f.read_text(encoding="utf-8", errors="replace"))
            if not d:
                continue
            r = parse_company(d)
            if r["name"]:
                rec = {**r, "slug": slug, "url": f"https://atomico.com/partners/{slug}",
                       "capture": cite, "capture_ts": ts,
                       "capture_source": "commoncrawl" if "commoncrawl" in cite else "wayback"}
                break
        if rec:
            rec["partners"] = [x.strip() for x in (rec.get("lead") or "").split(";") if x.strip()]
            out.append(rec)
        else:
            misses.append(slug)
    write_atomic(P.site / "cms-partners.json", json.dumps({
        "_readme": ("atomico.com /partners/<slug> pages (Next.js over the Hygraph CMS). The live site "
                    "sits behind a Vercel bot checkpoint, so each row is read from the newest capture "
                    "of the firm's own page: Common Crawl (34 crawls 2021-39..2026-04, cited as the "
                    "index query) or the Internet Archive (scratch/cc-pull.py, scratch/cms-pull.py "
                    "--local, " + time.strftime("%Y-%m-%d") + "). Sidebar fields: Investment year (an "
                    "anchor, never a round), Investment lead (-> partners), Stage (Venture | Growth, "
                    "scored before it may label: decisions.md D10), Status (Current | Exited), "
                    "Location, Areas of interest."),
        "misses": misses, "rows": out}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(out)} rows from local captures; unreadable: {misses}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--local", action="store_true", help="parse captures on disk only")
    args = ap.parse_args()
    if args.local:
        build_local()
        return
    RAW.mkdir(parents=True, exist_ok=True)
    rows = cdx_rows("atomico.com/partners/*")
    by_slug: dict[str, list[tuple[str, str]]] = {}
    for ts, orig, _st in rows:
        m = re.search(r"/partners/([^/?#]+)/?(?:[?#].*)?$", orig)
        if not m:
            continue
        slug = m.group(1).lower()
        if slug in NON_COMPANY or slug.startswith("--"):
            continue
        by_slug.setdefault(slug, []).append((ts, orig))
    print(f"/partners/<slug>: {len(by_slug)} slugs from {len(rows)} captures", flush=True)
    out, misses = [], []
    for i, (slug, caps) in enumerate(sorted(by_slug.items()), 1):
        if args.limit and i > args.limit:
            break
        caps.sort(reverse=True)
        rec = None
        for ts, orig in caps[:3]:
            f = RAW / f"{slug}-{ts}.html"
            if f.exists():
                html = f.read_text(encoding="utf-8", errors="replace")
            else:
                body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
                if code != "200" or not body:
                    continue
                html = body.decode("utf-8", errors="replace")
                write_atomic(f, html)
            d = next_data(html)
            if not d:
                continue
            rec = parse_company(d)
            if rec["name"]:
                rec.update({"slug": slug, "url": f"https://atomico.com/partners/{slug}",
                            "capture": f"https://web.archive.org/web/{ts}/{orig}",
                            "capture_ts": ts,
                            "years_listed": sorted({int(t[:4]) for t, _ in caps})})
                break
            rec = None
        if rec:
            out.append(rec)
        else:
            misses.append(slug)
        if i % 20 == 0:
            print(f"  {i}/{len(by_slug)} parsed {len(out)} misses {len(misses)}", flush=True)
    write_atomic(P.site / "cms-partners.json", json.dumps({
        "_readme": ("atomico.com /partners/<slug> pages (Next.js over the Hygraph CMS), read from "
                    "the Internet Archive because the live site sits behind a Vercel bot "
                    "checkpoint (scratch/cms-pull.py, " + time.strftime("%Y-%m-%d") + "). One row per "
                    "slug from the newest readable capture: the sidebar's Investment year (an anchor, "
                    "never a round), Investment lead, Stage (Venture | Growth: scored before it may "
                    "label, decisions.md D10), Status (Current | Exited), Location and Areas of "
                    "interest; years_listed = every capture year of the page."),
        "misses": misses,
        "rows": sorted(out, key=lambda r: r["slug"])}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(out)} rows; {len(misses)} unreadable: {misses[:20]}")


if __name__ == "__main__":
    main()
