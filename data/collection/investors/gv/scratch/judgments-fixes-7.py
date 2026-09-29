#!/usr/bin/env python3
"""Lead's fixes (PRO-75, 2026-09-29). Corduro: the Form D band labelled its only filing ($3.3M, first sale
2010-04-30, Joe Kraus a director) Seed by the code's flat $7.5M ceiling, but COLLECTION.md s6's structural rule
uses era-adjusted ceilings (seed / A up to 2010: $1.5M / $12M): no prior filing, a company incorporated in 2010,
so the round reads Series A and the row leaves the S2A cohort (judge d4 flagged it). Appstack: city from its own
Form D (Appstack, Inc., CIK 1562745, 43174 Business Park Drive, Temecula, CA; judge d4)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

FD = "https://www.sec.gov/Archives/edgar/data/1491585/000149158510000001/0001491585-10-000001-index.htm"
jl.write("fixes-7", [
    jl.cls("corduro", stage="Series A", stage_src="formd_structural", stage_cite=FD, stage_conf="medium",
           entry_date="2010-04-30", flags=["stage_disputes_band"],
           note="Stage: Series A by COLLECTION.md s6's era-adjusted band (a $3.3M first round in 2010 is above the "
                "$1.5M seed ceiling and below the $12M Series A ceiling; no prior filing, company incorporated "
                "2010); the flat band had read it Seed. The S2A column does not apply."),
    jl.cls("appstack", city="Temecula", city_src="formd_address",
           note="City: Temecula, the address on Appstack, Inc.'s own Form D (CIK 1562745, filed 2012-12-14).")])
