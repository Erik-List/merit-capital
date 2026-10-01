#!/usr/bin/env python3
"""Index the firm's own archived news posts by the companies they name.

Reads every /news/... capture (Common Crawl and Internet Archive manifests,
through archive_listings.captures) and writes sources/site/press-archive.json:
  posts      one per distinct post slug (the latest capture wins): title, date,
             category, external link, the text, the capture URL
  by_company company slug -> the posts whose title or text name it
so the grind reads the firm's own words about a round before any outside
source (COLLECTION.md s6: an announcement is class 1 for the round it NAMES).
"""
import html as htmlmod
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
sys.path.insert(0, str(HERE))
import archive_listings as A  # noqa: E402

OUT = INV / "sources" / "site" / "press-archive.json"
MONTHS = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}


def text_of(h: str) -> str:
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>", " ", h, flags=re.S)
    t = htmlmod.unescape(re.sub(r"<[^>]+>", " ", t))
    return re.sub(r"\s+", " ", t).strip()


def main() -> None:
    posts: dict[str, dict] = {}
    for cap in A.captures():
        if not cap["path"].startswith("/news/") or "/category/" in cap["path"]:
            continue
        slug = cap["path"].rstrip("/").split("/")[-1]
        if re.fullmatch(r"\d{4}", slug):
            continue
        h = cap["file"].read_text(encoding="utf-8", errors="replace")
        rec = {"slug": slug, "path": cap["path"], "capture_ts": cap["ts"], "capture_url": cap["capture_url"],
               "title": "", "date": "", "category": "", "external": "", "text": ""}
        txt = A.page_json_text(h)
        art = None
        if txt:
            for key, v in A.find_values(txt, "article|entry"):
                if isinstance(v, dict) and v.get("title") and ("postDate" in v or "slug" in v):
                    art = v
                    break
        if art:
            rec["title"] = art.get("title") or ""
            rec["date"] = (art.get("postDate") or "")[:10]
            rec["category"] = ", ".join(c.get("title", "") for c in (art.get("category") or []) if isinstance(c, dict))
            rec["external"] = art.get("externalUrl") or ""
            parts = []

            def strings(o, key=""):
                if isinstance(o, dict):
                    for k, v in o.items():
                        if k in ("sectionImage", "metaImage", "category", "thesis", "portfolioCompanies", "authors"):
                            continue
                        strings(v, k)
                elif isinstance(o, list):
                    for x in o:
                        strings(x, key)
                elif isinstance(o, str) and key in ("title", "subtitle", "excerpt", "introduction", "content",
                                                    "quote", "quoteAuthor", "text", "sectionContent", "heading"):
                    ref = re.fullmatch(r"\$(\w+)", o)
                    if ref:                      # an RSC text chunk: "<id>:T<hex length>,<text>"
                        m2 = re.search(r"(?:^|\n)" + ref.group(1) + r":T([0-9a-f]+),", txt)
                        if m2:
                            o = txt[m2.end():m2.end() + int(m2.group(1), 16)]
                    parts.append(A.strip_tags(o))
            strings(art)
            rec["text"] = " ".join(p for p in parts if p)[:8000]
            rec["companies_linked"] = [c.get("title") for c in (art.get("portfolioCompanies") or [])
                                       if isinstance(c, dict) and c.get("title")]
        else:
            m = re.search(r'<meta property="og:title" content="([^"]+)"', h) or re.search(r"<title>(.*?)</title>", h, re.S)
            rec["title"] = re.sub(r"\s*-\s*Lakestar\s*$", "", htmlmod.unescape(m.group(1)).strip()) if m else slug
            t = text_of(h)
            d = re.search(r"\b(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December) (20\d\d)\b", t)
            if d:
                rec["date"] = f"{d.group(3)}-{MONTHS[d.group(2)]:02d}-{int(d.group(1)):02d}"
            ext = re.search(r'<a href="(https?://(?!www\.lakestar\.com)[^"]+)"[^>]*>\s*(?:Read (?:More|Full)|Read the full)', h)
            rec["external"] = ext.group(1) if ext else ""
            rec["text"] = t[:8000]
        old = posts.get(slug)
        if old is None or len(rec["text"]) > len(old["text"]) or (not old["date"] and rec["date"]):
            if old and old["date"] and not rec["date"]:
                rec["date"] = old["date"]
            posts[slug] = rec
    ev = json.loads((INV / "sources" / "wayback" / "archive-evidence.json").read_text())["companies"]
    names = {s: e["name"] for s, e in ev.items()}
    site = INV / "sources" / "site" / "companies-2026.json"
    if site.exists():
        for r in json.loads(site.read_text())["rows"]:
            names.setdefault(A.slug_of(r["name"]), r["name"])
    by = {}
    for cs, name in names.items():
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])", re.I if len(name) > 5 else 0)
        hits = [p["slug"] for p in posts.values() if pat.search(p["title"]) or pat.search(p["text"])
                or name in (p.get("companies_linked") or [])]
        if hits:
            by[cs] = sorted(hits, key=lambda s: posts[s]["date"])
    OUT.write_text(json.dumps({"_readme": __doc__.strip(), "posts": dict(sorted(posts.items())),
                               "by_company": dict(sorted(by.items()))}, indent=1, ensure_ascii=False) + "\n")
    dated = sum(1 for p in posts.values() if p["date"])
    print(f"{len(posts)} posts ({dated} dated); {len(by)} companies named in at least one")


if __name__ == "__main__":
    main()
