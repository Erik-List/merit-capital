"""Cross-book pass cx2 (PRO-99, rule 10): Kleiner Perkins rows only. Plan: cross-plan-cx2.json."""
import judge_lib as jl

# Read 2026-09-30 with secget.py (the URL is the EDGAR full-text hit for "Spatial Photonics"): Himax's annual report
# for 2012 says "on July 3, 2012, our subsidiary, Himax Display, Inc. ... acquired all of the outstanding shares of
# capital stock of Spatial Photonics, Inc."
HIMAX_20F = "https://www.sec.gov/Archives/edgar/data/1342338/000114420413024864/v339709_20f.htm"

lines = [
    # Note only: the status (acquired) stands; the row's note left the buyer unnamed and half of it read unknown.
    jl.cls("spatial-photonics-inc",
           note="Cross-book 2026-09-30 (rule 10, Khosla): the buyer is Himax Display, a subsidiary of Himax "
                "Technologies, which acquired all outstanding shares of Spatial Photonics on 2012-07-03 (Himax's "
                f"annual report for 2012, {HIMAX_20F}). Acquired stands, with the buyer now named and cited; the "
                "earlier sentence calling the state unknown is withdrawn, and the Khosla row's defunct is the stale "
                "side."),
]
jl.write("cx2", lines)
