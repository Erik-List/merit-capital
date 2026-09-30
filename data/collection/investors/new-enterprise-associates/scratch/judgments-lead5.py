"""Verify clean-ups (PRO-100 NEA): stale source keys left on two rows whose answer changed. No value changes."""
import judge_lib as jl

L = [
    jl.cls("mode", extra={"entry_stage_source": None, "entry_stage_citation": None, "entry_stage_confidence": None}),
    jl.cls("stash", extra={"valuation_source": None, "valuation_range_source": None, "valuation_asof": None,
                           "valuation_confidence": None}),
]
jl.write("lead5", L)
