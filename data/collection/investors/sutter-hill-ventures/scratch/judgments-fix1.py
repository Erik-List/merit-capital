#!/usr/bin/env python3
"""Orchestrator fixes after the first grind (PRO-77): the one uncertain row."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, SEC

L = []
# serviz-inc: the director-of-record pattern (COLLECTION.md s1, a16z 2026-08-29): a current SHV managing
# director on the issuer's Form D, in tenure, identity resolved (Serviz, Los Angeles home services, bought by
# Porch in 2018). The Series B coverage names "Andy Sheehan of Sutter Hill Ventures" among existing investors.
L.append(verdict("serviz-inc", "member",
                 "Director-of-record pattern: Andy Sheehan, an SHV managing director in tenure (2007 to at least 2016), "
                 "is a director on Serviz's February 2014 Form D, the Series A Groupon led; the December 2014 Series B "
                 "coverage lists 'existing investors Andy Sheehan of Sutter Hill Ventures'. Identity resolved: Serviz, "
                 "Los Angeles home services, bought by Porch in 2018. Medium: whether the money was the partnership's or "
                 "Sheehan's own (D2) is not stated; flagged for the A/B pass.",
                 ec="formd_adjudicated", conf="medium", cite=SEC("serviz-inc")))
L.append(cls("serviz-inc", status="acquired", rng="below_1b",
             stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014-02",
             city="Los Angeles", city_src="formd_address", focus="Consumer & Marketplaces",
             flags=["stage_disputes_band"],
             note="Home services marketplace (Sherman Oaks, Los Angeles). Entry: the February 2014 Series A led by Groupon, "
                  "when Andy Sheehan joined the board (socaltech; the $7.5M Form D of 2014-02-18); the Form D band read it as "
                  "a seed. Series B December 2014 ($12.5M, Los Angeles Business Journal). Acquired by Porch 2018. "
                  "https://labusinessjournal.com/technology/serviz-fixes-125-million/"))
if __name__ == "__main__":
    jl.write("fix-001", L)
