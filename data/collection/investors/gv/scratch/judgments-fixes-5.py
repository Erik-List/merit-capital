#!/usr/bin/env python3
"""Lead's fixes (PRO-75, 2026-09-29): two classified rows the grind left without a focus value."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

jl.write("fixes-5", [jl.cls("spinlaunch", focus="Industrial & Robotics"),
                     jl.cls("spruce-finance", focus="Climate & Energy")])
