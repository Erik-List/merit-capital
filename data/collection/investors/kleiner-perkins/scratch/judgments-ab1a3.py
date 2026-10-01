"""A/B pass ab1a, part 3 (PRO-99 Kleiner Perkins), 2026-09-30: the stage pass (sta) flagged cognition and databricks
cite_pending in the same minutes this pass cited their entry rounds (judgments-ab1a1.py: Cognition's own Series E
post, The Information on the Series J). The citations are on the rows, so the flag is cleared.
Run as NQ_TAG=ab1a python3 judgments-ab1a3.py."""
import json

import judge_lib as jl
from judge_lib import cls

C = json.loads((jl.INV / "companies/classification.json").read_text())
L = []
for slug, what in (("cognition", "Cognition's own Series E post names Kleiner Perkins in the round"),
                   ("databricks", "The Information names Kleiner Perkins in the Series J fundraising")):
    r = C[slug]
    if r.get("entry_stage_source") != "web_verified" or not (r.get("entry_stage_citation") or "").startswith("http"):
        raise SystemExit(f"{slug}: the stage is not cited on disk, the flag stays")
    L.append(cls(slug, clear=["cite_pending"],
                 note=f"A/B 2026-09-30: cite_pending cleared, the entry round is cited ({what})."))
jl.write("ab1a3", L)
