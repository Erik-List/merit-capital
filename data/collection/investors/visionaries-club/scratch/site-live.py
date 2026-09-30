#!/usr/bin/env python3
"""Parse the live visionaries.vc portfolio into sources/site/companies-2026.json.

visionaries.vc (2026) is a Kirby CMS single page (media under /media/pages/home/,
Alpine.js `portfolioWrapper`). The whole portfolio ships server-rendered in the
page: one `div.portfolio__item` per company with the name, a one-line claim, a
paragraph description, a website button and the firm's own "Our Thesis" text.
`data-spotlight="true"` marks the twelve companies shown before "show all"; the
flag is kept, it is not an evidence class. The page gives no year, no stage and
no fund, so the rows carry no round word (COLLECTION.md s5: nothing to promote).

Usage: python3 site-live.py   (reads sources/site/home.html, fetched 2026-09-30)
"""
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "sources" / "site"
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
from paths import write_atomic  # noqa: E402


def txt(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def main() -> None:
    h = (SITE / "home.html").read_text(encoding="utf-8", errors="replace")
    rows = []
    for it in re.split(r'<div\s+class="portfolio__item"\s', h)[1:]:
        name = txt(re.search(r'portfolio__item-title-text">(.*?)</div>', it, re.S).group(1))
        claim = re.search(r'portfolio__item-claim">(.*?)</div>', it, re.S)
        desc = re.search(r'portfolio__item-testimonial-content[^>]*>(.*?)</div>', it, re.S)
        thesis = re.search(r'portfolio__item-text[^>]*>(.*?)</div>', it, re.S)
        links = re.findall(r'<a class="btn[^"]*" href="([^"]+)"', it)
        rows.append({
            "name": name,
            "url": "https://www.visionaries.vc/#portfolio",
            "website": links[0] if links else "",
            "claim": txt(claim.group(1)).strip(" -–") if claim else "",
            "description": txt(desc.group(1)) if desc else "",
            "thesis": re.sub(r"^Our Thesis\s*", "", txt(thesis.group(1))) if thesis else "",
            "spotlight": re.search(r'data-spotlight="true"', it) is not None,
            "index": int(re.search(r'data-portfolio-index="(\d+)"', it).group(1)),
        })
    out = {
        "_readme": __doc__,
        "source_url": "https://www.visionaries.vc/",
        "read": "2026-09-30",
        "rows": rows,
    }
    write_atomic(SITE / "companies-2026.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(len(rows), "rows")


if __name__ == "__main__":
    main()
