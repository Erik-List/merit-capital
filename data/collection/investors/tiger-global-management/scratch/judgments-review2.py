#!/usr/bin/env python3
"""Post-rebuild review 2 (PRO-167): the TeachersPayTeachers merge group resurfaced because its canonical is
not_member (COLLECTION.md 8: every slug of the group needs its own verdict)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict
jl.WHO = "agent-review-pro167"
L = [verdict("tpt-investor-llc", "not_member", "TPT Investor, LLC is one of the three 2014 holding entities of TeachersPayTeachers; the group's only evidence is Lee Fixel's director seat, and Erik's 2026-09-28 ruling puts a board-seat-only position out (as ruled on tpt-holdco-llc and teacher-synergy-llc).", ec="formd_adjudicated", conf="medium", cite=jl.SEC("tpt-investor-llc"))]
for x in L:
    x["who"] = jl.WHO
jl.write("review-002", L)
