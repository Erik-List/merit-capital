#!/usr/bin/env python3
"""Atomico's own announcement archive (/insights/<slug>), read from the archive.

The firm's posts are the class-1 source for the round each one NAMES
(COLLECTION.md §6: an announcement asserts an ENTRY only where it says so in
words). The Next.js site migrated the whole post history into /insights/<slug>
(a 2013 Klarna post sits there beside the 2025 IPO post), each page carrying
the CMS record in __NEXT_DATA__: title, published date, type ("Partnerships"
for investment posts), the related companies and the body.

Enumerated from the CDX index; the newest readable capture per slug is parsed.
Writes sources/site/insights.json.

Usage: python3 insights-pull.py [--limit N]
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
sys.path.insert(0, str(HERE))
import ia_fetch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

P = Paths("atomico")
RAW = HERE / "insights-raw"


def cdx_rows(pattern: str) -> list[list[str]]:
    url = ("https://web.archive.org/cdx/search/cdx?url=" + pattern +
           "&output=json&fl=timestamp,original,statuscode&filter=statuscode:200&limit=20000")
    body, code = ia_fetch.get(url)
    if code != "200":
        raise SystemExit(f"CDX {pattern}: {code} — rerun later (never read as empty)")
    data = json.loads(body or b"[]")
    return data[1:] if data else []


def rich(node) -> str:
    if isinstance(node, dict):
        if "text" in node and isinstance(node["text"], str):
            return node["text"]
        return " ".join(rich(v) for k, v in node.items() if k in ("children", "content", "raw", "json"))
    if isinstance(node, list):
        return " ".join(rich(c) for c in node)
    return ""


def walk_strings(o, depth=0):
    """Every string in the page props: a fallback body when the shape moves."""
    if depth > 12:
        return
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("globalSettings", "trackingParams", "labels"):
                continue
            if k == "text" and isinstance(v, str):
                yield v
            else:
                yield from walk_strings(v, depth + 1)
    elif isinstance(o, list):
        for v in o:
            yield from walk_strings(v, depth + 1)


def parse(d: dict, slug: str) -> dict:
    pp = d.get("props", {}).get("pageProps", {})
    hero = pp.get("hero") or pp.get("header") or {}
    title = (hero.get("title") or pp.get("title") or "")
    if isinstance(title, dict):
        title = rich(title)
    date = hero.get("publishedDate") or pp.get("publishedDate") or ""
    kind = hero.get("type") or pp.get("type") or ""
    meta = ((pp.get("globalSettings") or {}).get("metadata") or {})
    text = " ".join(" ".join(walk_strings({k: v for k, v in pp.items()
                                          if k not in ("latestNews", "relatedNews", "moreNews")})).split())
    partners = sorted({m.group(1) for m in re.finditer(r'"/partners/([a-z0-9-]+)"', json.dumps(pp))})
    return {"slug": slug, "title": str(title).strip() or meta.get("title") or "",
            "date": date, "type": kind, "description": meta.get("description") or "",
            "partners_linked": partners, "text": text[:6000]}


def sidebar_kind(pp: dict) -> str:
    for it in (pp.get("sidebar") or {}).get("items", []):
        if (it.get("title") or "").lower() in ("category", "type"):
            c = it.get("content")
            return (c.get("label") if isinstance(c, dict) else str(c or "")) or ""
    return ""


def build_local() -> None:
    cc = json.loads((RAW / "cc-captures.json").read_text()) if (RAW / "cc-captures.json").exists() else {}
    by_slug: dict[str, list] = {}
    for f in RAW.glob("*.html"):
        m = re.match(r"^(.*)-(cc)?(\d{14})\.html$", f.name)
        if not m:
            continue
        slug, is_cc, ts = m.group(1), bool(m.group(2)), m.group(3)
        cite = (cc.get(slug) or {}).get("citation") if is_cc else \
            f"https://web.archive.org/web/{ts}/https://atomico.com/insights/{slug}"
        by_slug.setdefault(slug, []).append((ts, f, cite or ""))
    out, misses = [], []
    for slug, caps in sorted(by_slug.items()):
        rec = None
        for ts, f, cite in sorted(caps, reverse=True):
            html = f.read_text(encoding="utf-8", errors="replace")
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json"[^>]*>(.*?)</script>', html, re.S)
            if not m:
                continue
            try:
                d = json.loads(m.group(1))
            except ValueError:
                continue
            rec = parse(d, slug)
            rec["type"] = rec.get("type") or sidebar_kind(d.get("props", {}).get("pageProps", {}))
            rec.update({"url": f"https://atomico.com/insights/{slug}", "capture": cite,
                        "capture_ts": ts})
            break
        (out.append(rec) if rec else misses.append(slug))
    write_atomic(P.site / "insights.json", json.dumps({
        "_readme": ("atomico.com /insights/<slug> posts (the firm's announcement archive, migrated "
                    "into the Next.js site), read from the newest capture on disk (Common Crawl, cited "
                    "as the index query, or the Internet Archive) by scratch/insights-pull.py --local "
                    + time.strftime("%Y-%m-%d") + ". Class 1 for the round a post NAMES; an entry "
                    "only where the post says so in words (COLLECTION.md §6)."),
        "misses": misses, "rows": out}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(out)} posts from local captures; {len(misses)} unreadable")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--local", action="store_true")
    args = ap.parse_args()
    if args.local:
        build_local()
        return
    RAW.mkdir(parents=True, exist_ok=True)
    rows = cdx_rows("atomico.com/insights/*")
    by_slug: dict[str, list] = {}
    for ts, orig, _ in rows:
        m = re.search(r"/insights/([a-z0-9][a-z0-9-]*)/?(?:[?#].*)?$", orig)
        if m:
            by_slug.setdefault(m.group(1), []).append((ts, orig))
    print(f"/insights/<slug>: {len(by_slug)} slugs", flush=True)
    out, misses = [], []
    for i, (slug, caps) in enumerate(sorted(by_slug.items()), 1):
        if args.limit and i > args.limit:
            break
        caps.sort(reverse=True)
        rec = None
        for ts, orig in caps[:2]:
            f = RAW / f"{slug}-{ts}.html"
            if f.exists():
                html = f.read_text(encoding="utf-8", errors="replace")
            else:
                body, code = ia_fetch.get(f"https://web.archive.org/web/{ts}id_/{orig}")
                if code != "200" or not body:
                    continue
                html = body.decode("utf-8", errors="replace")
                write_atomic(f, html)
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json"[^>]*>(.*?)</script>', html, re.S)
            if not m:
                continue
            try:
                rec = parse(json.loads(m.group(1)), slug)
            except ValueError:
                continue
            rec.update({"url": f"https://atomico.com/insights/{slug}",
                        "capture": f"https://web.archive.org/web/{ts}/{orig}"})
            break
        (out.append(rec) if rec else misses.append(slug))
        if i % 25 == 0:
            print(f"  {i}/{len(by_slug)} parsed {len(out)}", flush=True)
    write_atomic(P.site / "insights.json", json.dumps({
        "_readme": ("atomico.com /insights/<slug> posts (the firm's announcement archive, migrated "
                    "into the Next.js site), read from the Internet Archive by scratch/insights-pull.py "
                    + time.strftime("%Y-%m-%d") + ". Class 1 for the round a post NAMES; an entry only "
                    "where the post says so in words (COLLECTION.md §6)."),
        "misses": misses, "rows": out}, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {len(out)} posts; {len(misses)} unreadable")


if __name__ == "__main__":
    main()
