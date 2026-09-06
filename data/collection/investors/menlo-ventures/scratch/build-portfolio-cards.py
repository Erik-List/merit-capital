#!/usr/bin/env python3
"""Parse menlovc.com/portfolio/ into sources/site/portfolio-cards.json.

The WordPress REST collection (`site-portfolio.py`, 322 rows) is the recall
surface; the RENDERED listing carries what REST does not expose (ACF fields
are not published on the endpoint): per company a description, the website,
an exit line ("Acquired by X"), the Menlo deal PARTNERS, and a **Milestones**
list in which the firm states its own entry year and entry round
("2011 - Partnered, Series B" on Uber). Only the 245 listed rows have this
detail; the 77 REST-only rows are unpublished records with a name and a
description and no front-end page.

The Milestones field is a candidate class-1 entry_stage layer and is SCORED
on the golden set before it is allowed to label anything (COLLECTION.md 4).
"""
import json, re, subprocess, sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126 Safari/537.36")
URL = "https://menlovc.com/portfolio/"
CARD = re.compile(r'card-company block js-company-block js-company-card[^>]*?data-title="([^"]*)"')


def txt(s: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def main() -> None:
    p = Paths("menlo-ventures")
    cache = Path(__file__).resolve().parent / "portfolio.html"
    if not cache.exists():
        html = subprocess.run(["curl", "-sL", "--max-time", "180", "-H", f"User-Agent: {UA}", URL],
                              capture_output=True, check=True).stdout.decode("utf-8", "replace")
        write_atomic(cache, html)
    html = cache.read_text(encoding="utf-8", errors="replace")
    html = re.sub(r"<svg.*?</svg>", " ", html, flags=re.S)

    marks = list(CARD.finditer(html))
    rows = []
    for i, m in enumerate(marks):
        seg = html[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(html)]
        name = unescape(m.group(1)).strip()
        desc = re.search(r'<div class="body-small md:w-\[45%\][^"]*">(.*?)</div>', seg, re.S)
        status = re.search(r'<div class="body-small md:w-\[20%\][^"]*wysiwyg-section">(.*?)</div>', seg, re.S)
        site = re.search(r'class="portfolio-details-link eyebrow"\s*>\s*([^<]+?)\s*</a>', seg)
        miles = [(y.strip(), txt(t))
                 for y, t in re.findall(
                     r'<span class="h6 portfolio-details-text[^"]*">\s*(\d{4})\s*</span>\s*'
                     r'<span class="portfolio-details-text body-small[^"]*">(.*?)</span>', seg, re.S)]
        partners, seen = [], set()
        pblock = re.search(r'<h3 class="h6 mb-3">Partners</h3>(.*?)(?:</div>\s*</div>\s*</div>|$)', seg, re.S)
        for href, who in re.findall(r'href="https://menlovc\.com/team/([^"/]+)/"(.*?)</a>',
                                    pblock.group(1) if pblock else "", re.S):
            who = txt(who).lstrip("> ").strip()
            if href not in seen:
                seen.add(href)
                partners.append({"slug": href, "name": who or None})
        entry = next((m for m in miles if txt(m[1]).lower().lstrip("-\u2013\u2014 ").startswith("partnered")), None)
        stage = None
        if entry:
            e = txt(entry[1]).lstrip("-\u2013\u2014 ").strip()
            stage = e.split(",", 1)[1].strip() if "," in e else "Partnered (round unstated)"
        rows.append({
            "invest_year": int(entry[0]) if entry else None,
            "site_entry_stage": stage,
            "name": name,
            "slug": re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-"),
            "description": txt(desc.group(1)) if desc else None,
            "status_line": txt(status.group(1)) if status else None,
            "website": site.group(1).strip() if site else None,
            "milestones": [{"year": int(y), "event": e.lstrip("- –— ").strip()} for y, e in miles],
            "partners": partners,
        })
    out = {
        "_readme": ("Parsed from a saved copy of https://menlovc.com/portfolio/ by "
                    "scratch/build-portfolio-cards.py. The rendered listing is a "
                    "245-row subset of the 322-row wp-json `portfolios` collection; "
                    "it is used for its per-row detail (exit line, deal partners, "
                    "and the firm's own Milestones with entry year and entry round), "
                    "never for recall."),
        "source_url": URL,
        "rows": rows,
    }
    write_atomic(p.site / "portfolio-cards.json", json.dumps(out, indent=1) + "\n")
    withm = sum(1 for r in rows if r["milestones"])
    part = sum(1 for r in rows if r["partners"])
    exits = sum(1 for r in rows if r["status_line"])
    print(f"cards: {len(rows)}   milestones: {withm}   partners: {part}   exit lines: {exits}")
    ent = [m["event"] for r in rows for m in r["milestones"] if m["event"].lower().startswith("partnered")]
    from collections import Counter
    print("  entry events:", Counter(ent).most_common(12))


if __name__ == "__main__":
    main()
