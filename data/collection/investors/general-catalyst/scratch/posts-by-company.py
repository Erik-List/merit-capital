#!/usr/bin/env python3
"""Index the firm's own posts by company (scratch/posts-by-company.json).

For every portfolio-grid company: the /stories posts that link its
/companies/<slug> page or name it in the title, each with its date and the
sentences that carry a round word or an investment verb near the company's
name. The judge reads these as the firm's own record (class 1 for the round
a post NAMES; an entry only where the post says so in words, COLLECTION.md 6).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
sys.path.insert(0, str(INV.parents[3] / "scripts"))
from paths import write_atomic  # noqa: E402

ROUND = re.compile(r"\b(pre-seed|seed|series [a-h]\b|series [a-h][0-9]?|growth|incubat|hatch|co-?found|"
                   r"led|lead|co-led|first investment|first invested|backed|invest(?:ed|ment)|"
                   r"customer value fund|CVF|acqui|buyout|majority|round|raise[ds]?|funding)", re.I)
SPLIT = re.compile(r"(?<![0-9])(?<!\b[A-Z])[.!?]\s+(?=[A-Z])")


def main() -> None:
    stories = json.load(open(INV / "sources/site/stories.json"))["rows"]
    grid = json.load(open(INV / "sources/site/company-pages.json"))["rows"]
    out = {}
    for c in grid:
        name = c["name"]
        pat = re.compile(r"\b" + re.escape(name) + r"\b", re.I) if len(name) > 3 else None
        hits = []
        for s in stories:
            linked = c["slug"] in (s.get("companies") or [])
            titled = bool(pat and pat.search(s.get("title") or ""))
            if not (linked or titled):
                continue
            sents = [x.strip() for x in SPLIT.split(s.get("text") or "") if x.strip()]
            keep = [x[:400] for x in sents if (pat is None or pat.search(x)) and ROUND.search(x)][:6]
            hits.append({"url": s["url"], "date": s.get("date") or "", "title": s.get("title") or "",
                         "linked": linked, "titled": titled, "sentences": keep})
        if hits:
            out[c["slug"]] = sorted(hits, key=lambda h: (not h["titled"], h["date"]))
    write_atomic(HERE / "posts-by-company.json", json.dumps(out, indent=1, ensure_ascii=False) + "\n")
    print(f"posts-by-company: {len(out)} of {len(grid)} grid companies have a post; "
          f"{sum(1 for v in out.values() if any(h['titled'] for h in v))} with a post naming them in the title")


if __name__ == "__main__":
    main()
