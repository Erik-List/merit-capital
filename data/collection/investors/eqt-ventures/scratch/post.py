#!/usr/bin/env python3
"""Every round or money sentence about a company in the firm's own posts (stories + 2017-2020 articles).
Usage: post.py "Name" [--all]"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
S = HERE.parent / "sources" / "site"
name = sys.argv[1]; allp = "--all" in sys.argv
pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])", re.I)
money = re.compile(r"(?i)(series|seed|round|raise|rais|led|lead|invest|million|billion|€|\$|£|valuation|acqui|exit|IPO)")
rows = [(r["url"], r["title"], r["date_text"], r["text"].split("More to read")[0]) for r in json.loads((S / "stories.json").read_text())["rows"]]
rows += [(r["capture_url"], r["title"], r["date_text"], r["text"]) for r in json.loads((S / "articles-2017-2020.json").read_text())["rows"]]
for url, title, date, text in sorted(rows, key=lambda x: str(x[2])):
    if not pat.search(text) and not pat.search(title or ""):
        continue
    focal = pat.search(title or "") is not None
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", text) if pat.search(s) or (focal and money.search(s))]
    sents = [s for s in sents if money.search(s) or allp]
    if not sents and not focal:
        continue
    print(f"== {date} | {title[:100]} | {url}")
    for s in list(dict.fromkeys(sents))[:8 if focal else 3]:
        print("   >", s[:350])
