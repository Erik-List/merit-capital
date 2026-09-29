#!/usr/bin/env python3
"""Lead's fixes before rebuild 5 (PRO-75, 2026-09-29): MixBit absorbs AVOS Systems (one company; sweep judge s1), so
the canonical row takes AVOS's cited Series A (FinSMEs, 2012-04-27: NEA and Google Ventures)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

av = json.loads((jl.INV / "companies/classification.json").read_text())["avos-systems"]
jl.write("fixes-15", [jl.cls("mixbit", stage="Series A", stage_src="web_verified", stage_conf="high",
                             stage_cite=av["entry_stage_citation"], entry_date=av["entry_date"],
                             rounds=av.get("funding_rounds"),
                             note="AVOS Systems, the company behind MixBit (it turned into a single company working only "
                                  "on MixBit in 2014), is one row with it since rebuild 5; its Series A of April 2012, "
                                  "led by NEA and Google Ventures (FinSMEs, 2012-04-27), is GV's entry.")])
