#!/usr/bin/env python3
"""Lead's fixes for the in-flight verify problems after the grind (PRO-75, 2026-09-29): two public $1B+ rows
without a cited market cap, five $1B+ rows whose entry stage is a medium-confidence model reading with no page
naming GV's round (cite_pending: the judges searched and no single page names both), and Doppler's graduation on
an uncited stage (stage_uncited at low confidence, PRO-131 b)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

CHECK = "2026-09-29"
VR = {"valuation_range_source": "web_verified"}
cls_now = json.loads((jl.INV / "companies/classification.json").read_text())


def note_plus(slug, extra):
    return (cls_now.get(slug, {}).get("note") or "").rstrip() + " " + extra


L = []
UPCAP = "https://stockanalysis.com/stocks/upst/market-cap/"
L.append(jl.cls("upstart", rng="1b_plus", usd=2290000000, val_src="web_verified", val_cite=UPCAP, asof=CHECK,
                note=note_plus("upstart", "Market cap $2.29B on " + CHECK + " (stockanalysis.com), replacing the "
                               "pre-filled $5.44B float of 2025-06-30."), extra=VR))
VECAP = "https://stockanalysis.com/stocks/vera/market-cap/"
L.append(jl.cls("vera-therapeutics", rng="1b_plus", usd=2310000000, val_src="web_verified", val_cite=VECAP,
                asof=CHECK, note=note_plus("vera-therapeutics", "Market cap $2.31B on " + CHECK + " (stockanalysis.com), "
                                           "replacing the pre-filled $1.3B float of 2025-06-30."), extra=VR))
for s, why in [("dialpad", "Firespotter's 2011 round is the Series A by position; TechCrunch names GV's $3M, the "
                "company's 2012 release names the Series B, and no page names the 2011 round."),
               ("simply", "the 2020 round is at least the third priced round; no page names it."),
               ("turo", "TechCrunch names GV among the $10M raised (Sept 2011) and calls the financing the Series A "
                "(Oct 2011), on two pages, not one."),
               ("typeface", "the Lightspeed and Menlo pages label the launch round Series A and TechCrunch names GV in "
                "it, on separate pages."),
               ("viz-ai", "Globes names GV in the $21M round and NoCamels names the next round Series B; no page names "
                "the $21M round.")]:
    L.append(jl.cls(s, flags=["cite_pending"],
                    note=note_plus(s, "cite_pending: the stage is a model reading at medium; " + why)))
L.append(jl.cls("doppler", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
                note=note_plus("doppler", "The graduation is cited (TechCrunch, the named Series A); the stage under it "
                               "is uncited (stage_uncited, low, PRO-131 b).")))
jl.write("fixes-1", L)
