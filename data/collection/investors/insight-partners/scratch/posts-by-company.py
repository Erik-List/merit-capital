#!/usr/bin/env python3
"""Join the firm's own posts to its companies and keep what each post says
about the deal: the sentences that name a round, an amount or Insight's part
in it, and the sentences that use control wording.

This is the run's first-party evidence for two judged questions:
  entry_stage   an announcement is class 1 for the round it NAMES, and asserts
                an ENTRY only where the post says so in words (COLLECTION.md 6)
  control       decisions.md D3: "to acquire", "majority", "take private",
                "recapitalization" route a row to the control test; "strategic
                growth investment" decides nothing

A post is joined to a company when the company's panel links it (the panel's
own related-ideas list), or when the post's TITLE names the company as a whole
word. Body-only mentions are not joined: a portfolio roundup names forty
companies and says nothing about any one of them.

Output: scratch/posts-by-company.json  {slug: [{date, url, title, link,
        round_words, amounts, control_words, sentences}]}
Usage: python3 data/collection/investors/insight-partners/scratch/posts-by-company.py
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

INV = Path(__file__).resolve().parents[1]

ROUND = re.compile(r"\b(pre-seed|seed|series\s+[a-k]\d?|growth (?:equity |capital )?(?:round|investment|financing|funding)|"
                   r"strategic growth investment|minority (?:growth )?investment|minority stake|"
                   r"funding round|financing round|round of funding|investment round)\b", re.I)
AMOUNT = re.compile(r"(?:US)?[$€£]\s?\d[\d,.]*\s?(?:million|billion|m|mm|bn|b)\b", re.I)
CONTROL = re.compile(r"\b(to acquire|acquires?|acquired by|acquisition of|acquisition by|majority (?:growth )?investment|"
                     r"majority stake|majority interest|majority shareholder|majority owner|controlling (?:stake|interest)|"
                     r"take[- ]private|taken private|going[- ]private|definitive (?:merger )?agreement|"
                     r"recapitali[sz]ation|buyout|buy-out|all-cash transaction|per share in cash)\b", re.I)
FIRM = re.compile(r"\bInsight (?:Venture )?Partners\b|\bInsight\b")
GENERIC = {"the", "and", "for", "inc", "group", "labs", "software", "systems", "technologies", "technology",
           "solutions", "network", "networks", "media", "health", "data", "cloud", "digital", "global",
           "international", "holdings", "company", "fka"}


def sentences(text: str) -> list[str]:
    # keep decimals ("$5.1M") whole: split only on a stop followed by space + capital
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"“])", re.sub(r"\s+", " ", text))
    return [p.strip() for p in parts if p.strip()]


def names_of(row: dict) -> list[str]:
    n = row["name"]
    out = [re.sub(r"\s*\(.*?\)\s*", " ", n).strip()]
    for m in re.finditer(r"\((?:fka|f/k/a|formerly|aka|now)\s+([^)]+)\)", n, flags=re.I):
        for part in re.split(r"/|,| and ", m.group(1)):
            if part.strip():
                out.append(part.strip())
    return [x for x in dict.fromkeys(out) if len(x) >= 2]


def title_names(title: str, name: str) -> bool:
    if name.lower() in GENERIC:
        return False
    pat = r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])"
    flags = 0 if (len(name) <= 4 or name.lower() in {"hour", "divvy", "famous", "jobs", "move", "fabric"}) else re.I
    return re.search(pat, title, flags) is not None


def main() -> None:
    comps = json.load(open(INV / "sources/site/company-pages.json"))["rows"]
    posts = json.load(open(INV / "sources/site/posts.json"))["rows"]
    by_url = {p["url"].rstrip("/"): p for p in posts}
    out: dict[str, list[dict]] = {}
    stats = Counter()
    for c in comps:
        joined: dict[str, str] = {}
        for u in c.get("ideas") or []:
            if u.rstrip("/") in by_url:
                joined[u.rstrip("/")] = "panel"
        nms = names_of(c)
        for p in posts:
            if any(title_names(p["title"], n) for n in nms):
                joined.setdefault(p["url"].rstrip("/"), "title")
        rows = []
        for u, how in joined.items():
            p = by_url[u]
            keep = []
            for s in sentences(p["title"] + ". " + p["body"]):
                if len(s) > 600:
                    s = s[:600]
                hit_round = ROUND.search(s) or AMOUNT.search(s)
                hit_ctrl = CONTROL.search(s)
                # a control sentence is kept whoever it names: "becomes the
                # majority shareholder" often names neither party
                if hit_ctrl or (hit_round and (FIRM.search(s) or any(n.lower() in s.lower() for n in nms))):
                    keep.append(s)
            text = p["title"] + " " + p["body"]
            rows.append({
                "date": p["date"][:10], "url": p["url"], "title": p["title"], "link": how,
                "round_words": sorted({m.group(0).lower() for m in ROUND.finditer(text)})[:8],
                "amounts": sorted({m.group(0) for m in AMOUNT.finditer(text)})[:6],
                "control_words": sorted({m.group(0).lower() for m in CONTROL.finditer(" ".join(keep))})[:8],
                "sentences": keep[:8],
            })
        if rows:
            rows.sort(key=lambda r: r["date"])
            out[c["slug"]] = rows
            stats["companies with posts"] += 1
            if any(r["control_words"] for r in rows):
                stats["companies with control wording"] += 1
            if any(r["round_words"] for r in rows):
                stats["companies with a round word"] += 1
    (INV / "scratch/posts-by-company.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(dict(stats), "of", len(comps))


if __name__ == "__main__":
    main()
