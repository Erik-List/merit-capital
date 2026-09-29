#!/usr/bin/env python3
"""Write the selected recall candidates into the membership ledger as recall additions
(PRO-167), in the shape build-company-base.py injects (name, slug, basis, citation,
first_seen, on_site_now, sector, source), so each lands as a base row carrying its
evidence in the row note ("recall addition: <basis> (<citation>)").

Only grades A to D with a citation are written; every X (rejected) and pending candidate
stays in recall/additions-plan.json for the report. Idempotent: an addition already in the
ledger (same slug) is replaced, never duplicated; additions from other sources (the
recall probe after the grind) are kept.
"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("tiger-global-management")
SLUG = "tiger-global-management"
plan = json.loads((HERE / "recall/additions-plan.json").read_text())


def slug_of(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower().replace("&", "and")).strip("-")
    return s or "x"


from shared_throttle import exclusive  # noqa: E402
_LOCK = exclusive(f"record-{SLUG}")      # record's own lock: never race a judge's record
_LOCK.__enter__()
L = json.loads(P.ledger.read_text()) if P.ledger.exists() else {}
inv = L.setdefault(SLUG, {"recall_additions": [], "verdicts": {}})
inv.setdefault("verdicts", {})
# APPEND ONLY (2026-09-29: the first version replaced every "recall layer" addition with the
# current plan, and the plan no longer lists candidates that are already base rows, so it
# dropped 516 additions; they were restored from the base notes). An addition, once written,
# stays until a judge rules its row not_member; the rebuild re-injects every one of them.
keep = list(inv.get("recall_additions", []))
have = {a["slug"] for a in keep}
added, skipped = [], []
for k, v in sorted(plan.items(), key=lambda x: x[1]["name"].lower()):
    if v["grade"] not in ("A", "B", "C", "D") or not v.get("url"):
        continue
    name = v["name"].strip()
    s = slug_of(name)
    if s in have:
        skipped.append(s)
        continue
    if v["grade"] == "A":
        basis = v["basis"]
        src = "recall layer: EDGAR full-text (prospectus or merger filing naming a Tiger vehicle)"
    elif v["grade"] == "B":
        basis = f"'{v['title']}' ({v.get('source')}, {v.get('date')})"
        if v.get("sentences"):
            basis += f": \"{v['sentences'][0][:300]}\""
        src = "recall layer: Google News press sweep (a headline naming Tiger Global and the company)"
    elif v["grade"] == "C":
        basis = f"Wikipedia, {v['title']}: \"{v['basis'][:350]}\""
        src = "recall layer: Wikipedia insource sweep"
    else:
        basis = f"'{v['title']}' ({v.get('source')}, {v.get('date')}): \"{v['sentences'][0][:300]}\""
        src = "recall layer: Google News press sweep (the article's own sentence names Tiger Global)"
    add = {"name": name, "slug": s, "basis": basis, "citation": v["url"],
           "first_seen": v.get("first_seen") or "", "on_site_now": False, "sector": "",
           "source": src, "grade": v["grade"], "candidate_key": k}
    keep.append(add)
    have.add(s)
    added.append(s)
inv["recall_additions"] = keep
write_atomic(P.ledger, json.dumps(L, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
_LOCK.__exit__(None, None, None)
print(f"recall additions written: {len(added)} (total in ledger {len(keep)}); slug collisions skipped: {skipped[:20]}")
