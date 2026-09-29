#!/usr/bin/env python3
"""Duty 7 adjudication (PRO-167): the blind re-judgment (28 rows, 133/140 cells agree) disagreed on these;
the recorded value is kept on the row's own evidence and the row is flagged unstable."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls
jl.WHO = "agent-review-pro167"
L = [cls("invisionapp-inc", flags=["unstable"], note="Blind re-judgment (duty 7) read the entry as Growth; kept Series A: Lee Fixel joined InVision's board on its Q4 2013 Form D, the round of Tiger's entry, before the later Tiger-backed rounds."),
     cls("clicoh", flags=["unstable"], note="Blind re-judgment (duty 7) placed the head office in Buenos Aires; kept Córdoba, the city the grind cited for the company's head office.")]
for x in L:
    x["who"] = jl.WHO
jl.write("review-003", L)
