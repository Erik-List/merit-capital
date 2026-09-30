#!/usr/bin/env python3
"""The firm's own posts, as text: every `blog` entry of NEA's Statamic content
collection fetched from nea.com and reduced to its visible text, plus the
`article` entries (NEA's own index of press coverage: the entry carries the
external article's link and source, no body) and the press releases (their
Bard text is already in the pull).

Output: sources/site/news-text.json {"rows": [{kind, title, date, url, slug,
related_companies, article_link, article_source, body}]}
Usage: python3 fetch-posts.py
"""
import html
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402

ST = HERE.parent / "sources" / "site" / "statamic"
OUT = HERE.parent / "sources" / "site" / "news-text.json"
BASE = "https://www.nea.com"


def fetch(url):
    for attempt in range(3):
        r = subprocess.run(["curl", "-sL", "-m", "60", "-A", "Mozilla/5.0", url], capture_output=True)
        if r.returncode == 0 and r.stdout:
            return r.stdout.decode("utf-8", "replace")
        time.sleep(2 * (attempt + 1))
    return ""


def visible(h):
    # The page is Next.js: the article body is server-rendered inside <main>; the RSC payload repeats it.
    m = re.search(r"<main[\s\S]*?</main>", h)
    s = m.group(0) if m else h
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>|<svg[\s\S]*?</svg>|<nav[\s\S]*?</nav>", " ", s)
    s = re.sub(r"<(br|/p|/h\d|/li|/div)[^>]*>", "\n", s)
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in s.split("\n")]
    return "\n".join(ln for ln in lines if ln)


def main():
    old = {r["url"]: r for r in json.loads(OUT.read_text())["rows"]} if OUT.exists() else {}
    rows = []
    for r in json.load(open(ST / "content.json"))["rows"]:
        url = BASE + (r.get("url") or "")
        kind = (r.get("url") or "/").split("/")[1]
        rec = {"kind": kind, "title": html.unescape(r.get("title") or ""), "date": (r.get("date") or "")[:10],
               "url": url, "slug": r.get("slug"),
               "related_companies": [x["title"] for x in (r.get("related_companies") or [])],
               "article_link": r.get("article_link") or "", "article_source": r.get("article_source") or "",
               "body": ""}
        if kind == "blog":
            if old.get(url, {}).get("body"):
                rec["body"] = old[url]["body"]
            else:
                rec["body"] = visible(fetch(url))
                time.sleep(0.4)
        rows.append(rec)
    for r in json.load(open(ST / "press-releases.json"))["rows"]:
        body = "\n".join(re.sub(r"<[^>]+>", " ", html.unescape(x.get("text") or x.get("html") or x.get("text_content")
                                                                 or x.get("quote_text") or ""))
                         for x in (r.get("content") or []))
        rows.append({"kind": "press_release", "title": html.unescape(r.get("title") or ""),
                     "date": (r.get("date") or "")[:10], "url": BASE + (r.get("url") or ""), "slug": r.get("slug"),
                     "related_companies": [], "article_link": "", "article_source": "",
                     "body": re.sub(r"[ \t]+", " ", body).strip()})
    write_atomic(OUT, json.dumps({"_readme": "NEA's own posts (blog bodies fetched from nea.com), its index of press "
                                              "coverage (article entries: link and source only) and its press releases, "
                                              f"read {time.strftime('%Y-%m-%d')} by scratch/fetch-posts.py.",
                                  "rows": rows}, indent=1, ensure_ascii=False))
    print(len(rows), "rows;", sum(1 for r in rows if r["body"]), "with a body")


if __name__ == "__main__":
    main()
