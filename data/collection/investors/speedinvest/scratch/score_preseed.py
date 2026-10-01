#!/usr/bin/env python3
"""Score the firm's 2018-2020 'Pre-Seed' filter tag (decisions.md D10) blind against
the book's documented entry rounds (COLLECTION.md s5: an invented or first-party
field may label only after it is measured; `high` at >=95% over >=30 scored
rows, `medium` otherwise).

The tag is eligible by semantics only if it is the firm's claim about the round
IT entered. Scored two ways: precision (a tagged row's documented entry is a
Pre-Seed) and the complement (an untagged row listed in the same era whose
documented entry is a Pre-Seed). Writes scratch/preseed-score.json.
"""
import json
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J  # noqa: E402

cls = json.loads((J.INV / "companies/classification.json").read_text())
cls = cls.get("speedinvest", cls)
cls = cls.get("rows", cls) if isinstance(cls, dict) and "rows" in cls else cls
rows = []
for slug, r in J.BASE.items():
    e = J.ev(slug)
    if not e:
        continue
    tags = set(e.get("sections") or [])
    in_grid = bool(tags & {"active", "acquired"})       # the 2018-2020 grid era
    if not in_grid:
        continue
    c = cls.get(slug) or {}
    st, src = c.get("entry_stage"), c.get("entry_stage_source")
    if st in (None, "undetermined") or src not in ("web_verified", "first_party"):
        continue
    if "commoncrawl.org" in (c.get("entry_stage_citation") or "") and "portfolio" in (c.get("entry_stage_citation") or ""):
        continue   # the tag itself: a row labelled by the field cannot score it
    rows.append({"slug": slug, "tagged": "pre_seed" in tags, "documented": st, "cite": c.get("entry_stage_citation")})
tagged = [r for r in rows if r["tagged"]]
hit = [r for r in tagged if r["documented"] == "Pre-Seed"]
untagged_pre = [r for r in rows if not r["tagged"] and r["documented"] == "Pre-Seed"]
out = {"scored_rows": len(rows), "tagged": len(tagged), "tagged_and_preseed": len(hit),
       "precision": round(len(hit) / len(tagged), 3) if tagged else None,
       "untagged_but_preseed": len(untagged_pre),
       "tagged_misses": [(r["slug"], r["documented"]) for r in tagged if r["documented"] != "Pre-Seed"],
       "rows": rows}
(H / "preseed-score.json").write_text(json.dumps(out, indent=1))
print({k: v for k, v in out.items() if k != "rows"})
