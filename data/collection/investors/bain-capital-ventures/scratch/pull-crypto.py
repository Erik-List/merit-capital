#!/usr/bin/env python3
"""Pull Bain Capital Crypto's own portfolio and people from its WordPress REST
API (baincapitalcrypto.com, post types `portfolio` and `people`), into
sources/site/crypto-*.json. Bain Capital Crypto's funds sit under Bain Capital
Ventures' own adviser (CRD 145652; decisions.md D1), so this is a second list
surface of the same firm (COLLECTION.md 5, "enumerate every list surface").
The rendered archive page also splits current from exited companies
(`js-exited-list`), which the REST rows do not carry, so the page is read too.
"""
import json, re, subprocess, html, datetime
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "sources" / "site"
BASE = "https://baincapitalcrypto.com"


def get(url):
    return subprocess.run(["curl", "-sL", "-m", "90", "-A", "Mozilla/5.0", url],
                          capture_output=True, check=True).stdout.decode("utf-8", "replace")


def paged(rest):
    out, page = [], 1
    while True:
        batch = json.loads(get(f"{BASE}/wp-json/wp/v2/{rest}?per_page=100&page={page}") or "[]")
        if not isinstance(batch, list) or not batch:
            break
        out += batch
        if len(batch) < 100:
            break
        page += 1
    return out


port = paged("portfolio")
people = paged("people")
page = get(f"{BASE}/portfolio/")
# the exited list is the second grid; split the page at its marker
cur_html, _, ex_html = page.partition("js-exited-list")
def names(h):
    return [html.unescape(re.sub(r"<[^>]+>", "", m)).strip()
            for m in re.findall(r'class="portfolio-piece">(.*?)</(?:li|div|a)>', h, re.S)]
rows = []
for p in port:
    title = html.unescape(p["title"]["rendered"]).strip()
    rows.append({"name": title, "slug": p["slug"], "id": p["id"], "url": p.get("link") or "",
                 "published": (p.get("date") or "")[:10], "modified": (p.get("modified") or "")[:10],
                 "acf": p.get("acf") or {}, "class_list": p.get("class_list") or [],
                 "content": html.unescape(re.sub(r"<[^>]+>", " ", (p.get("content") or {}).get("rendered") or "")).strip()})
stamp = datetime.date.today().isoformat()
(SITE / "crypto-portfolio.json").write_text(json.dumps({
    "_readme": f"Pulled {stamp} from baincapitalcrypto.com/wp-json/wp/v2/portfolio (every row), "
               "plus the rendered /portfolio/ page, whose second grid (js-exited-list) is the firm's exited list.",
    "rows": rows, "page_exited_html_len": len(ex_html)}, indent=1) + "\n")
(SITE / "crypto-portfolio-page.html").write_text(page)
(SITE / "crypto-people.json").write_text(json.dumps({
    "_readme": f"Pulled {stamp} from baincapitalcrypto.com/wp-json/wp/v2/people.",
    "rows": [{"name": html.unescape(x["title"]["rendered"]).strip(), "slug": x["slug"],
              "url": x.get("link"), "acf": x.get("acf") or {},
              "content": html.unescape(re.sub(r"<[^>]+>", " ", (x.get("content") or {}).get("rendered") or "")).strip()[:2000]}
             for x in people]}, indent=1) + "\n")
print(len(rows), "crypto portfolio rows;", len(people), "people")
print([r["name"] for r in rows])
print(json.dumps(rows[0], indent=1)[:1500])
