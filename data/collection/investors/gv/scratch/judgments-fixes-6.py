#!/usr/bin/env python3
"""Lead's fixes (PRO-75, 2026-09-29): two cities judge d3 found in its S2A pass but did not emit (Cord: New York,
Variety; Airy Labs: Palo Alto, the Mercury News). The note carries only the new sentence (record appends notes)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

jl.write("fixes-6", [
    jl.cls("cord", city="New York", note="City: New York (Variety, read by the graduation pass 2026-09-29)."),
    jl.cls("airy-labs", city="Palo Alto", note="City: Palo Alto (the Mercury News, read by the graduation pass "
                                             "2026-09-29).")])
