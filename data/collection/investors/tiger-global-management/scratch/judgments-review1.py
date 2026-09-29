#!/usr/bin/env python3
"""Post-grind review 1 (PRO-167): Erik's 2026-09-28 ruling (board-seat-only rows are not
members, memory unverified-venture-positions-out) applied to the Harry's group, whose only
evidence is Lee Fixel's director seat on its Form Ds (no round naming Tiger on Bing or Google)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict
B = ("Only evidence is Lee Fixel's director seat on the company's Form Ds (filed as {n}); no round naming Tiger "
     "Global is on record (Bing and Google News searched 2026-09-29). Erik's ruling of 2026-09-28: a board-seat-only "
     "position is not a verified venture position, so the row is not a member.")
L = [verdict("harry-s-inc", "not_member", B.format(n="Harry's, Inc."), ec="formd_adjudicated", conf="medium", cite=jl.SEC("harry-s-inc")),
     verdict("hf-global-inc", "not_member", B.format(n="HF Global, Inc., Harry's earlier filing name"), ec="formd_adjudicated", conf="medium", cite=jl.SEC("hf-global-inc")),
     verdict("adkm-inc", "not_member", B.format(n="ADKM, Inc., the same CIK 1556308"), ec="formd_adjudicated", conf="medium", cite=jl.SEC("adkm-inc"))]
jl.WHO = "agent-review-pro167"
for x in L:
    x["who"] = jl.WHO
jl.write("review-001", L)
