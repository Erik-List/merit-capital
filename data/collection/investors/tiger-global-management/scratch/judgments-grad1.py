#!/usr/bin/env python3
"""S2A for Mayfair (PRO-167): Tiger led the $8M seed of April 2022 (TechCrunch 2023-01-13); past the 24-month
window on 2026-09-29; no later round on any surface -> not_graduated by the absence test (COLLECTION.md 6)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls, GRADLINES
jl.WHO = "agent-review-pro167"
surf = GRADLINES("mayfair", name="Mayfair", formd_note="Mayfair's own Form D filings on EDGAR: none found for the business cash-management company -> no later priced round on record",
                 extra=["web: Bing News '\"Mayfair\" business cash fintech funding' and '\"Mayfair\" \"Tiger Global\"' (2026-09-29) -> only the January 2023 launch coverage naming the $2M pre-seed and the $8M seed; no Series A or later round"])
L = [cls("mayfair", grad="not_graduated", grad_src="absence_check", grad_asof="2026-09-29", surfaces=surf,
         entry_date="2022-04", note="S2A: the $8M seed of April 2022 (Tiger led) is the last round on record; the absence test ran 2026-09-29 on the firm, Form D, Google News (two queries), TechCrunch and Crunchbase News surfaces plus Bing, and found no later round.")]
for x in L:
    x["who"] = jl.WHO
jl.write("grad-001", L)
