#!/usr/bin/env python3
"""Companies the Views posts name as Seedcamp investments -> candidate rows.

Reads sources/site/views-posts.json (every post's text) and writes
scratch/views-candidates.json: one entry per (company, post) with the kind of
claim the post makes. Three kinds, strongest first:

  cohort   a post announcing the teams the firm INVESTED in ("Seedcamp Week
           2009 winners ... will all receive a EUR50k investment", "11 New
           Seedcamp Investments", "the teams joining Seedcamp", "latest
           additions to the Seedcamp portfolio"); list items read as
           "Name (City, Country) - description" or "Name, City, Country - ...".
           Attendee, finalist and Mini Seedcamp winner posts are NOT cohorts
           (decisions.md D2) and are skipped by title.
  invest   a post whose title says the firm invested: "our investment in X",
           "why we led / are leading X", "Seedcamp leads / co-leads / joins X",
           "X joins Seedcamp", "welcome X".
  news     "X raises ..." posts whose text names Seedcamp as an investor of X.

The script only proposes; the judge reads each candidate that is not already a
base row (decisions.md D2, D10). Usage: python3 views-extract.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
POSTS = json.loads((INV / "sources" / "site" / "views-posts.json").read_text())["rows"]
OUT = HERE / "views-candidates.json"

COHORT_T = re.compile(r"(?i)(new (seedcamp )?investments|new teams|teams? (join|joining)|startups? join|"
                      r"join(ing)? (the )?seedcamp|joining our family|additions to the seedcamp|newest teams|"
                      r"seedcamp (week )?(20\d\d )?winners|week 20\d\d winners|winners are|seedcamp companies|"
                      r"meet the new|latest teams|welcome to the (seedcamp )?(family|portfolio)|family grows|"
                      r"new companies|pre-seed investments?|portfolio (update|additions))")
NOT_COHORT_T = re.compile(r"(?i)(attending|finalists|mini[- ]seedcamp|applications|apply|tips|details for|"
                          r"preparing|meet & greet|on tour|us trip|podcast|operator|investor days)")
INVEST_T = [
    re.compile(r"(?i)(?:our|announcing our|seedcamp'?s?) investment in (?P<n>[^:,–\-!?$]+?)(?:'s?\b|[,:–\-!?]| to | as | in | for |$)"),
    re.compile(r"(?i)why (?:we|we're|we are|seedcamp) (?:led|leading|lead|backed|backing|invested in|investing in|co-led|co-leading)(?: the)?(?: pre-seed| seed)?(?: round)?(?: into| in)? (?P<n>[^:,–\-!?$]+?)(?:'s?\b|[,:–\-!?]| to | as | in | for |$)"),
    re.compile(r"(?i)seedcamp (?:co-)?leads? (?:[^ ]+ )?(?:funding round for |round for |seed round for |pre-seed round for |investment in )?(?P<n>[A-Z][^:,–\-!?$]+?)(?:'s?\b|[,:–\-!?]| to | as | in | for |$)"),
    re.compile(r"(?i)seedcamp joins .*? (?:investment|round) in (?P<n>[^:,–\-!?$]+?)(?:'s?\b|[,:–\-!?]| to | as | in | for |$)"),
    re.compile(r"(?i)^(?P<n>[^:,–!?]+?) joins seedcamp"),
    re.compile(r"(?i)^welcome(?:,)? (?P<n>[^:,–\-!?]+?)(?:[,:–\-!?]| to | the | on | out | a | an |$)"),
    re.compile(r"(?i)^welcoming (?P<n>[^:,–\-!?]+?) to"),
]
RAISES_T = re.compile(r"(?i)^(?:seedcamp[- ]backed |portfolio (?:company )?)?(?P<n>[^:,–!?]+?) (?:raises|secures|closes|lands|announces|bags|nets|completes|gets)\b")
SC_IN_TEXT = re.compile(r"(?i)(seedcamp (?:led|leads|co-led|co-leads|participat|invest|joined|backed|is an investor|was an early)|"
                        r"(?:led|co-led|backed) by seedcamp|from seedcamp|including seedcamp|with seedcamp|and seedcamp|"
                        r"seedcamp[- ]backed|seedcamp portfolio|existing investors?[^.]{0,80}seedcamp)")
ITEM = re.compile(r"(?:^|\s)(?P<n>[A-Z0-9][\w.&'’+\-]*(?: [A-Z0-9][\w.&'’+\-]*){0,3})\s*(?:\((?P<loc1>[^)]{2,60})\)|,\s*(?P<loc2>[A-Z][A-Za-z .]+(?:,\s*[A-Z][A-Za-z .]+)?))\s*[–—-]\s")


def clean_name(n: str) -> str:
    n = re.sub(r"\s+", " ", n).strip(" .'’\"")
    n = re.sub(r"(?i)^(the )?(startup|company|team) ", "", n)
    return n


def main() -> None:
    out = []
    for p in POSTS:
        title, text = p["title"], p.get("text") or ""
        date = p["date"][:10]
        kind = None
        if COHORT_T.search(title) and not NOT_COHORT_T.search(title):
            kind = "cohort"
            body = text.split(title, 1)[-1]
            for m in ITEM.finditer(body):
                loc = (m.group("loc1") or m.group("loc2") or "").strip()
                out.append({"name": clean_name(m.group("n")), "kind": "cohort", "date": date,
                            "post": p["link"], "title": title, "loc": loc,
                            "snippet": body[max(0, m.start() - 20): m.end() + 140]})
        for rx in INVEST_T:
            m = rx.search(title)
            if m:
                out.append({"name": clean_name(m.group("n")), "kind": "invest", "date": date,
                            "post": p["link"], "title": title})
                break
        m = RAISES_T.search(title)
        if m:
            sm = SC_IN_TEXT.search(text)
            out.append({"name": clean_name(m.group("n")), "kind": "news" if sm else "news-unattributed",
                        "date": date, "post": p["link"], "title": title,
                        "snippet": text[max(0, sm.start() - 160): sm.end() + 160] if sm else ""})
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    from collections import Counter
    print(len(out), "candidates", Counter(x["kind"] for x in out))
    print(len({x["name"].lower() for x in out}), "distinct names")


if __name__ == "__main__":
    main()
