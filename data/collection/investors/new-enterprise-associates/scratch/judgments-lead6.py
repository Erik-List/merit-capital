"""PRO-131 b on two graduated rows (PRO-100 NEA): the later round is cited, the Seed entry is an inferred reading, so
the row stays decided with stage confidence low and the flag stage_uncited."""
import judge_lib as jl

L = [
    jl.cls("thirdlove", stage_conf="low", flags=["stage_uncited"], extra={"entry_stage_confidence": "low"}),
    jl.cls("tigerdata", stage_conf="low", flags=["cite_pending", "stale", "stage_uncited"],
           extra={"entry_stage_confidence": "low"}),
]
jl.write("lead6", L)
