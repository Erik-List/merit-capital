#!/usr/bin/env python3
"""Delta pass, tag d1, batch 1, one follow-up line (PRO-99): the city the Subject release gives.
Run: NQ_TAG=d1 python3 judgments-d1c.py
"""
import judge_lib as jl
from judge_lib import cls

L = [cls("subject", city="Los Angeles", city_src="web_verified",
         note="City from the company's Series A release of 2022-03-22 (PR Newswire, Los Angeles), the page the "
              "graduation cites.")]

if __name__ == "__main__":
    jl.write("d1c", L)
