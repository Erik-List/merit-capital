#!/usr/bin/env python3
"""Pull every usv.com WordPress post (the firm's writing archive since 2003) via the open
REST API into sources/site/wp-posts.json: id, date, slug, link, title, excerpt, plain-text
content, categories, tags, Company/Topic/Thesis term ids. First-party announcement layer
(entry-stage citations, 'Read the Post' targets). Paced at ~1 request/s."""
import json, re, subprocess, sys, time, html
from pathlib import Path
OUT = Path("data/collection/investors/union-square-ventures/sources/site/wp-posts.json")
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
def get(url):
    for a in range(5):
        r = subprocess.run(["curl", "-s", "--max-time", "90", "-A", UA, "-w", "\n%{http_code}", url], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code == "200":
            try: return json.loads(body)
            except json.JSONDecodeError: pass
        time.sleep(3 * (a + 1))
    raise SystemExit(f"failed {url}")
def text(s):
    s = re.sub(r"<script.*?</script>|<style.*?</style>", " ", s or "", flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()
posts = []
page = 1
while True:
    d = get(f"https://www.usv.com/wp-json/wp/v2/posts?per_page=100&page={page}&orderby=date&order=asc")
    if not isinstance(d, list) or not d: break
    for p in d:
        posts.append({"id": p["id"], "date": p["date"], "slug": p["slug"], "link": p["link"],
                      "title": text(p["title"]["rendered"]), "excerpt": text(p["excerpt"]["rendered"]),
                      "text": text(p["content"]["rendered"]), "categories": p.get("categories"),
                      "tags": p.get("tags"), "company_terms": p.get("Company"), "topic": p.get("Topic"),
                      "thesis": p.get("Thesis"), "author": p.get("author"),
                      "external_post_link": p.get("external_post_link")})
    print(f"page {page}: {len(posts)} posts", flush=True)
    if len(d) < 100: break
    page += 1
    time.sleep(1.0)
OUT.write_text(json.dumps({"_readme": "usv.com WordPress REST /wp-json/wp/v2/posts, pulled " + time.strftime("%Y-%m-%d") + "; every post since 2003 with plain-text content; the firm's own announcement archive (COLLECTION.md §5 first-party surfaces).", "pulled": time.strftime("%Y-%m-%dT%H:%M"), "count": len(posts), "posts": posts}, ensure_ascii=False, indent=1))
print("wrote", OUT, len(posts))
