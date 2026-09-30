#!/usr/bin/env python3
"""Score Project A's own entry-round fields blind against the book's documented
entry rounds (COLLECTION.md s5: measure a layer before it labels; D10).

Documented = a row whose recorded entry_stage rests on web_verified or formd
evidence naming the round (never the firm field itself, never a model guess).
Fields scored, each collapsed onto the taxonomy through scripts/stage_words.py:
  cms   live Sanity projectInvestedAt (pre_seed / seed / series_a / series_b / private_equity)
  cf    2020-2024 Contentful `investment`
  page  2015-2019 per-company page "Investment" line
A field value that does not collapse onto one stage is an anchor, not a label,
and is counted apart. Prints agreement per field and the misses by name.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
INV = HERE.parent
ROOT = INV.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(HERE))
from stage_words import earliest_round  # noqa: E402
import judge_lib as J  # noqa: E402

CMS_WORD = {"pre_seed": "Pre-Seed", "seed": "Seed", "series_a": "Series A", "series_b": "Series B",
            "private_equity": None}


def main():
    base = {r["slug"]: r for r in json.loads((INV / "companies/base.json").read_text())}
    cls = json.loads((INV / "companies/classification.json").read_text())
    doc = {s: c for s, c in cls.items() if s in base and c.get("entry_stage") not in (None, "", "undetermined")
           and c.get("entry_stage_source") in ("web_verified", "formd_structural", "formd")}
    res = {}
    for field in ("cms", "cf", "page"):
        hit, miss, anchor = [], [], []
        for s, c in sorted(doc.items()):
            if field == "cms":
                lv = J.live(s, base[s]["name"]) or {}
                raw = CMS_WORD.get(lv.get("stage_at_entry_site")) if lv.get("stage_at_entry_site") else None
                raw_disp = lv.get("stage_at_entry_site")
            else:
                vals = [v for v, _ in J.fields(s, "cf_investment" if field == "cf" else "page_investment")]
                raw_disp = vals[0] if vals else None
                raw = raw_disp
            if not raw_disp:
                continue
            lab = earliest_round(raw) if raw else None
            if lab in ("Series B", "Series C", "Series D"):
                lab = "Growth"
            if not lab:
                anchor.append((s, raw_disp, c["entry_stage"]))
                continue
            (hit if lab == c["entry_stage"] else miss).append((s, raw_disp, c["entry_stage"]))
        n = len(hit) + len(miss)
        res[field] = {"scored": n, "agree": len(hit), "rate": round(len(hit) / n, 3) if n else None,
                      "misses": miss, "anchors": anchor}
        print(f"{field}: {len(hit)}/{n} agree ({res[field]['rate']}), {len(anchor)} anchors")
        for s, raw, st in miss:
            print(f"   miss {s:26} field={raw!s:22} documented={st}")
    (HERE / "field-score.json").write_text(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
