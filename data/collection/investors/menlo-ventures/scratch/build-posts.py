#!/usr/bin/env python3
"""menlovc.com/wp-json/wp/v2/posts -> sources/site/posts.json.

The firm's own announcement archive (COLLECTION.md 5: a class-1 layer on
Creandum, and the check that overrides a Form D band on a $1B+ or post-2020
row per 6, entry_stage). 369 posts under /perspective/; the pre-2023 "voice"
and "blog" eras live only in the capture archive and are read from there.
Content is kept as text so a round word and a company name can be matched
without a second fetch.
"""
import json, re, subprocess, sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
API = "https://menlovc.com/wp-json/wp/v2/posts"


def txt(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def main() -> None:
    p = Paths("menlo-ventures")
    rows, page = [], 1
    while True:
        raw = subprocess.run(
            ["curl", "-sL", "--max-time", "90", "-H", f"User-Agent: {UA}",
             f"{API}?per_page=100&page={page}&_fields=id,date,slug,link,title,excerpt,content"],
            capture_output=True, check=True).stdout
        batch = json.loads(raw)
        if not batch:
            break
        for r in batch:
            body = txt(r.get("content", {}).get("rendered", ""))
            rows.append({"date": r["date"][:10], "slug": r["slug"], "url": r["link"],
                         "title": txt(r["title"]["rendered"]),
                         "excerpt": txt(r.get("excerpt", {}).get("rendered", ""))[:400],
                         "body": body[:6000]})
        if len(batch) < 100:
            break
        page += 1
    rows.sort(key=lambda r: r["date"], reverse=True)
    write_atomic(p.site / "posts.json", json.dumps(
        {"_readme": ("The firm's own announcement and essay archive, pulled from the live "
                     "WordPress REST posts collection by scratch/build-posts.py. Used as "
                     "entry-round evidence (a dated post naming the round is class 1 under "
                     "COLLECTION.md 6) and as a recall-probe surface."),
         "source_url": API, "rows": rows}, indent=1) + "\n")
    yrs = {}
    for r in rows:
        yrs[r["date"][:4]] = yrs.get(r["date"][:4], 0) + 1
    print(f"posts: {len(rows)}   by year: {dict(sorted(yrs.items()))}")


if __name__ == "__main__":
    main()
