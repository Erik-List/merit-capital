"""Lead judgments 6 (2026-10-06): the flag debts the in-flight verify named."""
import judge_lib as jl
lines = [
    jl.cls("capsule8", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
           note="Stage flagged stage_uncited: the seed round is named from knowledge, no page read names it; the cited later round decides the graduation."),
    jl.cls("plenful", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
           note="Stage flagged stage_uncited: TechCrunch reports the first round without naming it; the cited Series A decides the graduation."),
    jl.cls("abacus", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
           note="Stage flagged stage_uncited: no page read names the 2014 round; the cited sale to Certify decides the graduation."),
    jl.cls("docusign", flags=["cite_pending"],
           note="cite_pending: no page read names the round the firm entered in 2011."),
    jl.cls("domain", grad="undetermined", note="S2A undetermined: the company cannot be named."),
    jl.cls("fg-wireless", grad="undetermined", note="S2A undetermined: the company cannot be named."),
]
jl.write("lead6", lines)
