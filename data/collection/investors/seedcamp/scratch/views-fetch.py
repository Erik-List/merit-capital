#!/usr/bin/env python3
"""Read every seedcamp.com 'Views' post page and keep its text.

The WordPress REST API lists all posts (id, date, link, title, categories)
but serves an empty `content` field: the theme renders the body from custom
fields. So each post page is fetched once, the <main class="main--singlepost">
block is reduced to text, and the text is written back onto the REST rows in
sources/site/views-posts.json. Raw pages are cached under data/filings/
(gitignored, re-downloadable). One request per PACE seconds, resumable.

Usage: python3 views-fetch.py
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = HERE.parents[4]
SRC = INV / "sources" / "site" / "views-posts.json"
CACHE = ROOT / "data" / "filings" / "seedcamp-views"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
PACE = 1.0


def fetch(url: str) -> str | None:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (hashlib.sha1(url.encode()).hexdigest()[:20] + ".html")
    if f.exists() and f.stat().st_size > 1000:
        return f.read_text(encoding="utf-8", errors="replace")
    for attempt in range(3):
        time.sleep(PACE)
        r = subprocess.run(["curl", "-sL", "--max-time", "60", "-A", UA, "-w", "\n%{http_code}", url],
                           capture_output=True)
        body, _, code = r.stdout.decode("utf-8", errors="replace").rpartition("\n")
        if r.returncode == 0 and code == "200":
            f.write_text(body, encoding="utf-8")
            return body
        if code == "404":
            return None
        time.sleep(5 * (attempt + 1))
    return None


def main_text(page: str) -> tuple[str, list[str]]:
    i = page.find("main--singlepost")
    j = page.find("</main>", i)
    seg = page[i:j] if i >= 0 else page
    seg = re.sub(r"<script.*?</script>|<style.*?</style>", "", seg, flags=re.S)
    links = sorted(set(re.findall(r'href="(https?://[^"#]+)"', seg)))
    txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", seg))).strip()
    txt = re.sub(r'^main--singlepost">\s*', "", txt)
    return txt, links


def main() -> int:
    d = json.loads(SRC.read_text())
    rows = d["rows"]
    todo = [r for r in rows if not r.get("text")]
    print(f"{len(todo)} of {len(rows)} posts to read", flush=True)
    failed = 0
    for n, r in enumerate(todo, 1):
        page = fetch(r["link"])
        if page is None:
            r["text_status"] = "failed"
            failed += 1
            continue
        r["text"], r["links"] = main_text(page)
        r.pop("text_status", None)
        if n % 50 == 0:
            SRC.write_text(json.dumps(d, indent=0, ensure_ascii=False))
            print(f"  {n}/{len(todo)}", flush=True)
    SRC.write_text(json.dumps(d, indent=0, ensure_ascii=False))
    print(f"done, {failed} failed", flush=True)
    return 3 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
