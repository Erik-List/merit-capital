#!/usr/bin/env python3
"""A/B pass (COLLECTION.md s7), public rows still on a 2025 float (PRO-75, 2026-09-29): market cap at the
2026-09-29 read (stockanalysis.com) replaces the float. Vir Biotechnology crosses into 1b_plus."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

CHECK = "2026-09-29"
VR = {"valuation_range_source": "web_verified"}
cls = json.loads((jl.INV / "companies/classification.json").read_text())


def plus(slug, extra):
    return (cls.get(slug, {}).get("note") or "").rstrip() + " " + extra


L = [jl.cls("vir-biotechnology", rng="1b_plus", usd=1750000000, val_src="web_verified",
            val_cite="https://stockanalysis.com/stocks/vir/market-cap/", asof=CHECK,
            note=plus("vir-biotechnology", "A/B pass: market cap $1.75B on " + CHECK + " (stockanalysis.com), "
                      "replacing the $689M float of 2025-06-30; the row moves to 1b_plus."), extra=VR),
     jl.cls("prime-medicine", rng="below_1b", usd=519480000, val_src="web_verified",
            val_cite="https://stockanalysis.com/stocks/prme/market-cap/", asof=CHECK,
            note=plus("prime-medicine", "A/B pass: market cap $519.48M on " + CHECK + " (stockanalysis.com), "
                      "replacing the $239M float of 2025-06-30."), extra=VR)]
jl.write("ab-1", L)
