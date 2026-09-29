#!/usr/bin/env python3
"""Lead's fixes before the final rebuild (PRO-75, 2026-09-29). Rockbot absorbs the recall addition Roqbot (the same
company under its first name; judge d1): the canonical row takes Roqbot's cited 2012 seed and its S2A answer.
Voltron Data absorbs Ursa Computing (decisions R2; judge d5): its note records Ursa's seed."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

cls = json.loads((jl.INV / "companies/classification.json").read_text())
rq = cls["roqbot"]
L = [jl.cls("rockbot", stage="Seed", stage_src="web_verified", stage_cite=rq["entry_stage_citation"],
            stage_conf="high", entry_date=rq["entry_date"], grad=rq["seed_to_a_graduation"],
            grad_src=rq["graduation_source"], grad_asof=rq["graduation_asof"], surfaces=rq["graduation_surfaces"],
            grad_conf=rq.get("graduation_confidence") or "medium",
            note="Roqbot was Rockbot's first name (the same CEO, Garrett Dodge, and the same start at San Francisco's "
                 "Bar Basic; TechCrunch 2014 and 2015), so the recall addition roqbot is this row since the final "
                 "rebuild. Google Ventures and Detroit Venture Partners led its $1.2M seed of 2012-06-12 (TechCrunch; "
                 "AllThingsD): GV's entry. S2A: not graduated; the 2014 Universal Music Group round was strategic and "
                 "undisclosed, and the two 2015 Form Ds ($290,000 in notes, $2.71M of equity) do not reach the $5M an "
                 "unnamed round needs over a 2012 seed (absence test 2026-09-29, medium).",
            rounds=rq.get("funding_rounds")),
     jl.cls("voltron-data",
            note="GV's first money in this lineage was Ursa Computing's $4.9M seed, which it led (Ursa's own "
                 "announcement, 2020-12-10; the firm's /ai list dates it October 2020); Ursa folded into Voltron Data "
                 "in 2021 and is one row with it since the final rebuild (decisions R2). The entry is read through "
                 "Voltron's own seed, and either reading graduates on Voltron's named Series A.")]
jl.write("fixes-8", L)
