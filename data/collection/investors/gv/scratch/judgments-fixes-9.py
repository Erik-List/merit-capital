#!/usr/bin/env python3
"""Lead's fixes after the final rebuild (PRO-75, 2026-09-29): eleven rows kept layer A's is_public / public_since from a
weak SEC join to another company (the judges disputed the status and float, not these two keys), and rule 7 read
CacheFlow as public for it. The keys are set to the row's own evidence: none of these companies was ever listed."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

ROWS = ["airware", "cacheflow", "cosmos", "courier", "lattice", "sense", "upbound", "flux", "glimpse", "simply",
        "lucid-software"]
jl.write("fixes-9", [{"slug": s, "who": jl.WHO, "is_public": False, "public_since": None} for s in ROWS])
