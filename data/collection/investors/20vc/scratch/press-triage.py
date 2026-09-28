#!/usr/bin/env python3
"""Sort the press layer for the judge (decisions.md D7: a sentence naming 20VC
as a platform is never membership evidence).

For every article (scratch/press/items.json) and every targeted check
(scratch/recall/candidates.json) with sentences naming the firm, each sentence
is tagged:
  investor  names 20VC / Harry Stebbings in a funding context (led by,
            participation from, backed by, investors include, co-led, ...)
  podcast   names the podcast, an interview or a quote (told 20VC, on the
            20VC podcast, speaking to Harry Stebbings, ...)
  other     neither
and the headline's company is guessed ("X raises ...", "X secures ...").
Output: scratch/press/triage.json and a compact listing on stdout, investor
articles first, grouped by guessed company.

Usage: python3 press-triage.py [--all]
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = re.compile(r"led by|co-led|lead investor|participation (?:from|of)|backed by|backers? (?:include|such as)|"
                 r"investors? (?:include|including|such as|like)|joined by|with (?:support|backing) from|"
                 r"alongside|existing investors?|new investors?|round (?:was |is )?(?:led|backed)|"
                 r"(?:20\s?VC|Stebbings)[^.]{0,60}\b(?:led|invested|backed|joined|participated|co-led|"
                 r"invests|leads)|\braises?\b|\braised\b|\bsecures?\b|\bfunding\b|\bseed\b|series [a-e]|"
                 r"pre-seed|investment from|invested in|portfolio", re.I)
POD = re.compile(r"podcast|\btold\b|interview|episode|said on|speaking (?:to|with)|in conversation|"
                 r"\bhost\b|20VC x SaaStr|appearance|\bshow\b|conversation with|asked by|on 20VC", re.I)
CO = re.compile(r"^(?:Exclusive:\s*)?([A-Z0-9][\w.&'’\- ]{1,40}?)\s+(?:raises|raised|secures|secured|lands|nabs|bags|"
                r"gets|closes|announces|sammelt|erhält|bekommt|lève|levée|emerges|launches|scores|snags|picks up|"
                r"attracts|receives|banks|hauls|pulls in|debuts|unveils|reels in)\b", re.I)


def tag(s: str) -> str:
    if POD.search(s) and not re.search(r"led by|participation|backed by|investors include|co-led", s, re.I):
        return "podcast"
    if INV.search(s):
        return "investor"
    return "other"


def company(title: str) -> str:
    m = CO.search(title.strip())
    if m:
        return m.group(1).strip(" -–:")
    return ""


def main():
    rows = []
    items = json.loads((HERE / "press" / "items.json").read_text())
    for r in items.values():
        sents = r.get("sentences") or []
        if not sents:
            continue
        tags = [tag(s) for s in sents]
        rows.append({"company": company(r.get("title") or ""), "date": r.get("date"), "title": r.get("title"),
                     "source": r.get("source"), "link": r.get("link"), "layer": "sweep",
                     "sentences": [{"tag": t, "s": s} for t, s in zip(tags, sents)]})
    cf = HERE / "recall" / "candidates.json"
    if cf.exists():
        for name, rec in json.loads(cf.read_text()).items():
            for it in rec.get("items", []):
                sents = it.get("sentences") or []
                if not sents:
                    continue
                tags = [tag(s) for s in sents]
                rows.append({"company": company(it.get("title") or "") or name, "query_name": name,
                             "date": it.get("date"), "title": it.get("title"), "source": it.get("source"),
                             "link": it.get("link"), "layer": "targeted",
                             "sentences": [{"tag": t, "s": s} for t, s in zip(tags, sents)]})
    for r in rows:
        r["kind"] = "investor" if any(x["tag"] == "investor" for x in r["sentences"]) else \
            "podcast" if any(x["tag"] == "podcast" for x in r["sentences"]) else "other"
    (HERE / "press" / "triage.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    by = defaultdict(list)
    for r in rows:
        if r["kind"] == "investor" or "--all" in sys.argv:
            by[(r["company"] or "?").lower()].append(r)
    print(f"{len(rows)} articles with firm sentences; investor-context {sum(1 for r in rows if r['kind'] == 'investor')}, "
          f"podcast {sum(1 for r in rows if r['kind'] == 'podcast')}, other {sum(1 for r in rows if r['kind'] == 'other')}")
    for k in sorted(by):
        print(f"== {k}")
        for r in sorted(by[k], key=lambda x: x["date"] or "")[:4]:
            best = next((x["s"] for x in r["sentences"] if x["tag"] == "investor"), r["sentences"][0]["s"])
            print(f"   {r['date']} {r['source']}: {r['title'][:90]}")
            print(f"      > {best[:260]}")


if __name__ == "__main__":
    main()
