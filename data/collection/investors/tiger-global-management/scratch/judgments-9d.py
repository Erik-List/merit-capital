#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 9, chunk d: the valuation line nuvemshop still needed. Run: NQ_TAG=b9 python3 judgments-9d.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls

TC_NUV = "https://techcrunch.com/2021/08/17/brazils-nuvemshop-raises-500m-at-a-3-1b-valuation-months-after-last-raise/"
L = [cls("nuvemshop", rng="1b_plus", usd=3_100_000_000, val_src="web_verified", val_cite=TC_NUV, asof="2021-08-17",
         extra={"valuation_range_source": "web_verified"}, flags=["stale"],
         note="Valuation: the $500M Series E Tiger co-led valued Nuvemshop at $3.1B (TechCrunch, 2021-08-17); no later "
              "priced round or collapse evidence found, so the mark stands, stale. Aligned with the Accel row.")]

if __name__ == "__main__":
    jl.write("batch-009d", L)
