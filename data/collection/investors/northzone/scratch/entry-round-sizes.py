#!/usr/bin/env python3
"""Entry rounds announced in the firm's own posts, for investment_range.median
(COLLECTION.md §11: "investment_range without Form D coverage"; Balderton and
Creandum precedent).

A row counts when its entry_stage_citation is one of the firm's own posts
(northzone.com/insights/<slug>, or an archived northzone.com/YYYY/MM/DD/<slug>
post) and that post states a size: the first amount in the title, else in the
body's first 700 characters. Non-USD sizes convert at the ECB rate of the post
date (scripts/fx-convert.py). Writes sources/site/entry-round-sizes.json.
"""
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
REPO = ROOT.parents[3]
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location("fxc", REPO / "scripts" / "fx-convert.py")
fxc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fxc)

CUR = {"$": "USD", "€": "EUR", "£": "GBP", "usd": "USD", "eur": "EUR", "sek": "SEK",
       "nok": "NOK", "dkk": "DKK", "gbp": "GBP", "dollars": "USD", "euros": "EUR",
       "euro": "EUR", "kronor": "SEK", "pounds": "GBP"}
AMT = re.compile(
    r"(?P<pre>[$€£]|\b(?:USD|EUR|SEK|NOK|DKK|GBP)\s?)(?P<num>\d+(?:[.,]\d+)?)\s?"
    r"(?P<unit>million|mln|mn|m|bn|billion|k)?\b"
    r"|(?P<num2>\d+(?:[.,]\d+)?)\s?(?P<unit2>million|mln|mn|m)\s+(?P<post>dollars|euros|euro|kronor|pounds|USD|EUR|SEK|NOK|DKK|GBP)\b",
    re.I)
UNIT = {"million": 1e6, "mln": 1e6, "mn": 1e6, "m": 1e6, "bn": 1e9, "billion": 1e9, "k": 1e3, None: 1}


ROUND_WORDS = re.compile(r"round|series|seed|a-round|raise|funding|financing|\bled\b|leads|leading|investment", re.I)
NOT_ROUND = re.compile(r"\bmarkets?\b|annual|spent|default|revenue|proceeds|\btrade\b|worth|valu", re.I)


def first_amount(text: str):
    """The first amount that reads as a round: round words within 90
    characters and no market, revenue or proceeds word right beside it (a post
    body can open with the size of the market it is attacking)."""
    for m in AMT.finditer(text):
        near = text[max(0, m.start() - 90):m.end() + 90]
        tight = text[max(0, m.start() - 30):m.end() + 25]
        if not ROUND_WORDS.search(near) or NOT_ROUND.search(tight):
            continue
        if m.group("num"):
            num, unit, cur = m.group("num"), (m.group("unit") or "").lower() or None, m.group("pre").strip()
        else:
            num, unit, cur = m.group("num2"), m.group("unit2").lower(), m.group("post")
        cur = CUR.get(cur.lower(), CUR.get(cur, cur.upper()))
        v = float(num.replace(",", ".")) * UNIT[unit]
        if v < 1e5 or v >= 1e9:  # "$3" without a unit, or a billion, is not a venture round
            continue
        return m.group(0).strip(), cur, v
    return None


def post_slug(url: str):
    m = re.search(r"northzone\.com/(?:insights/|\d{4}/\d{2}/\d{2}/)([^/?#]+)", url or "")
    return m.group(1) if m else None


def main():
    posts = {r["slug"]: r for r in json.loads((ROOT / "sources/site/insights.json").read_text())["rows"]}
    cls = json.loads((ROOT / "companies/classification.json").read_text())
    ledger = json.loads((REPO / "data/collection/shared/membership-ledger.json").read_text()) \
        if (REPO / "data/collection/shared/membership-ledger.json").exists() else None
    base = {r["slug"] for r in json.loads((ROOT / "companies/base.json").read_text())}
    rows, skipped = [], []
    for slug, c in sorted(cls.items()):
        if slug not in base:
            continue
        ps = post_slug(c.get("entry_stage_citation"))
        if not ps:
            continue
        p = posts.get(ps)
        if not p:
            skipped.append((slug, "post not in insights.json", ps))
            continue
        body = re.sub(r"\s+", " ", p.get("body") or "")
        hit = first_amount(p.get("title") or "") or first_amount(body[:700])
        if not hit:
            skipped.append((slug, "no size stated", ps))
            continue
        native, cur, v = hit
        date = p.get("date_wp") or (re.search(r"/(\d{4})/(\d{2})/(\d{2})/", c["entry_stage_citation"]) and
                                    "-".join(re.search(r"/(\d{4})/(\d{2})/(\d{2})/", c["entry_stage_citation"]).groups()))
        if cur == "USD":
            usd, fxnote = v, None
        else:
            usd, det = fxc.to_usd(v, cur, date)
            fxnote = f"{v:,.0f} {cur} at the ECB rate of {det.get('rate_date', date)}"
        rows.append(dict(slug=slug, stage=c.get("entry_stage"), date=date, native=native,
                         usd=int(round(usd, -5)), fx=fxnote, post=p["url"], title=p.get("title")))
    usd = sorted(r["usd"] for r in rows)
    by = {}
    for r in rows:
        by.setdefault(r["stage"], []).append(r["usd"])
    out = {
        "_readme": ("Entry rounds announced in the firm's own posts (sources/site/insights.json) where the post "
                    "is the row's entry_stage_citation and states a size; first amount in the title, else in the "
                    "body's first 700 characters, converted at the ECB rate of the post date. Built by "
                    "scratch/entry-round-sizes.py for investment_range.median."),
        "median_usd": statistics.median(usd) if usd else None,
        "count": len(rows),
        "by_stage": {k: {"median_usd": statistics.median(v), "count": len(v)} for k, v in sorted(by.items(), key=lambda kv: str(kv[0]))},
        "rows": rows,
        "skipped": [dict(slug=s, why=w, post=p) for s, w, p in skipped],
    }
    (ROOT / "sources/site/entry-round-sizes.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    for r in rows:
        print(f"{r['slug']:28} {str(r['stage']):10} {r['date']} {r['native']:>14} {r['usd']:>13,}  {r['title'][:70]}")
    print("median", out["median_usd"], "n", len(rows), out["by_stage"])
    print("skipped", len(skipped))


if __name__ == "__main__":
    main()
