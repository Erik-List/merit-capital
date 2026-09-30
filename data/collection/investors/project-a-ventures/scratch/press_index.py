#!/usr/bin/env python3
"""Index Project A's own press-release archive (project-a.com /media|press|presse/
press-releases|pressemitteilungen[-news]/<post>, 2012-2019, captured by Common Crawl)
plus the live Sanity articles, one record per post (EN and DE captures of one
post fold on the post slug), with the date the page states, the title, the body
text and the base rows the text names.

Writes sources/site/press-archive.json: {post_slug: {title, date, capture_url,
original_url, lang, text, companies: [base slugs]}}. The judge reads it as the
firm's own announcement layer: class 1 for the round a post NAMES (COLLECTION.md
s6: an announcement asserts an entry only where the post says so in words).
"""
import html as H
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

CC_RAW = ROOT / "data" / "filings" / "commoncrawl" / "project-a-ventures"
MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                      "september", "october", "november", "december"], 1)}
MONTHS.update({m[:3]: i for m, i in list(MONTHS.items())})
MONTHS.update({"sept": 9, "januar": 1, "februar": 2, "märz": 3, "maerz": 3, "mai": 5, "juni": 6, "juli": 7, "oktober": 10,
               "dezember": 12})


def text_of(body: str) -> str:
    m = re.search(r"<main.*?</main>|<article.*?</article>", body, re.S)
    s = m.group(0) if m else body
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<nav.*?</nav>|<header.*?</header>|<footer.*?</footer>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", H.unescape(s)).strip()


def date_of(t: str) -> str:
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\.(20\d\d)\b", t)
    if m:
        return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    m = re.search(r"\b(\d{1,2})\.? ([A-Za-zä]+) (20\d\d)\b", t)
    if m and m.group(2).lower() in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
    m = re.search(r"\b([A-Za-zä]+) (\d{1,2}),? (20\d\d)\b", t)
    if m and m.group(1).lower() in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1).lower()]:02d}-{int(m.group(2)):02d}"
    return ""


def main():
    man = json.loads((INV / "sources/wayback/cc-manifest.json").read_text())
    base = json.loads((INV / "companies/base.json").read_text())
    names = {r["slug"]: r["name"] for r in base}
    posts = {}
    for key, m in sorted(man.items()):
        if m.get("status") != "ok":
            continue
        path = re.sub(r"^https?://(www\.)?project-a\.com(:\d+)?", "", m["url"])
        mm = re.fullmatch(r"/(en|de)/(?:media|press|presse)/(?:press-releases|pressemitteilungen)(?:-news)?/([^/?#]+)/?", path)
        if not mm:
            continue
        lang, post = mm.groups()
        body = (CC_RAW / key).read_text(errors="replace")
        t = text_of(body)
        title = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = text_of(title.group(1)) if title else post
        rec = posts.get(post)
        # prefer the English capture, then the earliest
        if rec and (rec["lang"] == "en" or lang != "en"):
            continue
        cos = sorted({s for s, n in names.items()
                      if len(n) >= 3 and re.search(rf"(?<![A-Za-z0-9]){re.escape(n)}(?![A-Za-z0-9])", t, re.I)})
        posts[post] = {"title": title, "date": date_of(t[:600]) or date_of(t), "lang": lang,
                       "capture_url": m["capture_url"], "original_url": m["url"], "capture_ts": m["timestamp"],
                       "text": t[:6000], "companies": cos}
    sa = json.loads((INV / "sources/site/articles.json").read_text())["rows"]
    for a in sa:
        t = a.get("body") or ""
        cos = sorted({s for s, n in names.items()
                      if len(n) >= 3 and re.search(rf"(?<![A-Za-z0-9]){re.escape(n)}(?![A-Za-z0-9])", t + " " + a["title"], re.I)})
        posts["vc:" + (a.get("slug") or a["_id"])] = {
            "title": a["title"], "date": str(a.get("publishedAt") or a.get("date") or a["_createdAt"])[:10],
            "lang": "en", "capture_url": f"https://www.project-a.vc/blog/{a.get('slug')}",
            "original_url": f"https://www.project-a.vc/blog/{a.get('slug')}", "text": t[:6000], "companies": cos}
    write_atomic(INV / "sources/site/press-archive.json", json.dumps(
        {"_readme": __doc__.strip().splitlines()[0], "posts": posts}, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for p in posts.values() if p["companies"])
    print(f"{len(posts)} posts, {n} naming a base row")


if __name__ == "__main__":
    main()
