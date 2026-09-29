#!/usr/bin/env python3
"""Lead's fixes (PRO-75, 2026-09-29): Airware's and CacheFlow's status rode a weak SEC join to other companies
(Airware Labs; the 1990s CacheFlow that became Blue Coat); both rows' own evidence gives acquired (Delair, 2018;
HubSpot, 2024), so the status is stated on the classification."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

jl.write("fixes-4", [{"slug": "airware", "who": jl.WHO, "status": "acquired"},
                     {"slug": "cacheflow", "who": jl.WHO, "status": "acquired"}])
