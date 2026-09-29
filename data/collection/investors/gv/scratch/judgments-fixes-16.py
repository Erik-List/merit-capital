#!/usr/bin/env python3
"""Lead's fixes before rebuild 5 (PRO-75, 2026-09-29): the rename sweep (duty 9 on the duplicate class) merges four
more pairs; two canonical rows carry the undetermined stage while the absorbed row holds the cited seed, so they
take the absorbed row's answers: Jetify (from Jetpack Technologies) and Crews by Core (from Core)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

cls = json.loads((jl.INV / "companies/classification.json").read_text())


def take(dst, src, note):
    s = cls[src]
    return jl.cls(dst, stage=s["entry_stage"], stage_src=s["entry_stage_source"], stage_conf=s.get("entry_stage_confidence"),
                  stage_cite=s.get("entry_stage_citation"), entry_date=s.get("entry_date"),
                  grad=s.get("seed_to_a_graduation"), grad_src=s.get("graduation_source"),
                  grad_cite=s.get("graduation_citation"), grad_conf=s.get("graduation_confidence"),
                  grad_asof=s.get("graduation_asof"), surfaces=s.get("graduation_surfaces"),
                  city=s.get("hq_city") if not cls[dst].get("hq_city") else None,
                  city_src=s.get("hq_city_source") or "model_knowledge",
                  rounds=s.get("funding_rounds"), note=note)


L = [take("jetify", "jetpack-technologies",
          "Rename sweep 2026-09-29: Jetpack Technologies is this company under its first name and one row with it since "
          "rebuild 5; its $10M seed, co-led by Coatue and GV (TechCrunch, 2023-02-01), is GV's entry, and GC AI's 2026 "
          "purchase ended it without a later round: not graduated."),
     take("crews-by-core", "core",
          "Rename sweep 2026-09-29: Core is this company under its first name and one row with it since rebuild 5; its $4M "
          "seed of September 2020 with John Lyman of GV (the company's release, Palo Alto) is GV's entry, and the WakeCap "
          "sale of 2024 ended it without a later round: not graduated.")]
for x in L:
    for k in [k for k, v in x.items() if v is None]:
        x.pop(k)
jl.write("fixes-16", L)
