"""Lead judgments 8 (2026-10-06): flags made stale by the merges."""
import judge_lib as jl
lines = [
    jl.cls("newview-technologies", clear=["identity_conflated"], note="Merged with the row e-steel at the final rebuild (one company)."),
    jl.cls("vibrant-solutions", clear=["identity_conflated"], note="Merged with the row informationview-solutions at the final rebuild (one company)."),
]
jl.write("lead8", lines)
