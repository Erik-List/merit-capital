#!/usr/bin/env python3
"""Rule 6 fix (PRO-167): NSE's India head office with a citation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls, W
jl.WHO = "agent-review-pro167"
L = [cls("nse", country="IN", country_src="web_verified", country_cite=W("National Stock Exchange of India"), city="Mumbai")]
for x in L:
    x["who"] = jl.WHO
jl.write("review-004", L)
