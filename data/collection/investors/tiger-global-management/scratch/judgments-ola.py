#!/usr/bin/env python3
"""Ola (ANI Technologies / Ola Consumer), PRO-167: the row the builder had folded into Ola Electric (never_merge now)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, NEWS, W
jl.WHO = "agent-review-pro167"
add = [a for a in json.load(open("../companies/membership-ledger.json"))["tiger-global-management"]["recall_additions"] if a["slug"] == "ola"][0]
BL = add["citation"]
vg = NEWS("ola", "Vanguard marks Ola valuation down")
L = [verdict("ola", "member", "Tiger Global Management provided Olacabs' Series A (Business Line and The Next Web, April 2012), then joined the 2013 round ($20M with Matrix) and the 2014 Series D ($210M, SoftBank-led).", ec="web", conf="high", cite=BL),
     cls("ola", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=BL, stage_conf="high", entry_date="2012-04",
         country="IN", country_src="web_verified", country_cite=W("Ola Consumer"), city="Bangalore", focus="Consumer & Marketplaces",
         rounds=[rnd("2012-04", "Series A", None, "Tiger Global", True, BL, "press")],
         note=f"Ola Consumer (ANI Technologies), Bangalore ride hailing. Tiger's first money was the April 2012 Series A. No priced round is on record since the 2021-22 marks; holder marks collapsed: Vanguard cut Ola Consumer to about $70M in June 2026, 99% below its peak ({vg}), collapse evidence under COLLECTION.md 6, so the row reads below $1B with no figure minted from the mark. Ola Electric is a separate row.")]
for x in L:
    x["who"] = jl.WHO
jl.write("review-006", L, record=False)
