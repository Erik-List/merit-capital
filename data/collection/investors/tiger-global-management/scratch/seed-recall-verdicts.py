#!/usr/bin/env python3
"""Seed membership verdicts for recall additions whose evidence was verified at selection
(PRO-167), the way prepare seeds a site listing or a fund filing, so the grind's judges
confirm them rather than re-derive them:

  A  a prospectus / IRA / merger filing naming a PIP (private-equity desk) vehicle or the
     adviser as a holder while the company was private -> member, fund_filing, high
     (a filing naming ONLY public-desk vehicles is NOT seeded: delta X1, the judge rules it)
  B  a headline naming Tiger Global and the company with an investment word -> member, web,
     high when it names a round or a lead, else medium
  C  a Wikipedia sentence naming Tiger's investment -> member, web, medium
  D  (an article sentence) is NOT seeded: the sentence may name Tiger for another reason

Every seed carries who "seed-recall-pro167" (agent level: a judge's verdict replaces it) and
the citation the addition carries. Only rows present in base.json and without a verdict
are touched.
"""
import json, re, sys
from datetime import date
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("tiger-global-management")
SLUG = "tiger-global-management"
from shared_throttle import exclusive  # noqa: E402
_LOCK = exclusive(f"record-{SLUG}")
_LOCK.__enter__()
L = json.loads(P.ledger.read_text())
inv = L[SLUG]
ver = inv.setdefault("verdicts", {})
base = {r["slug"] for r in json.loads(P.base_json.read_text())}
plan = json.loads((HERE / "recall/additions-plan.json").read_text())
n = {"A": 0, "B": 0, "C": 0, "skipped_public_desk": 0, "skipped_D": 0, "not_in_base": 0, "had_verdict": 0}
for a in inv.get("recall_additions", []):
    s, g = a["slug"], a.get("grade")
    if s not in base:
        n["not_in_base"] += 1
        continue
    if s in ver:
        n["had_verdict"] += 1
        continue
    pl = plan.get(a.get("candidate_key") or "", {})
    if g == "A":
        if pl.get("desk") == "public":
            n["skipped_public_desk"] += 1
            continue
        ec, conf = "fund_filing", "high"
    elif g == "B":
        ec = "web"
        conf = "high" if re.search(r"(?i)series|seed|round|led by|leads|co-led|funding", a["basis"]) else "medium"
    elif g == "C":
        ec, conf = "web", "medium"
    else:
        n["skipped_D"] += 1
        continue
    ver[s] = {"verdict": "member", "who": "seed-recall-pro167", "evidence_class": ec,
              "basis": f"Recall addition ({a['source'].replace('recall layer: ', '')}): {a['basis'][:600]}",
              "citation": a["citation"], "confidence": conf, "decided": date.today().isoformat()}
    n[g] += 1
write_atomic(P.ledger, json.dumps(L, indent=1, sort_keys=True, ensure_ascii=False) + "\n")
_LOCK.__exit__(None, None, None)
print("seeded:", n)
