"""Cross-book pass, judge cx1 (PRO-80, rule 10): Bessemer rows that change (bvp_stale). Only the keys that change.

One row: sorare. The A/B pass of 2026-10-06 read it below_1b on the 2025 layoffs and the unpriced insider round of
September 2026; Erik ruled on those facts on 2026-09-28 (headline/documentation/decisions.md E2: the September 2021
$4.3B Series B is the last priced mark; layoffs do not band a row), so the row returns to the mark it carried before
the A/B pass and agrees with the 20VC, Accel, Atomico, Headline, IVP and Seedcamp books.

Run once: NQ_TAG=cx1 python3 judgments-cx1.py
"""
import json

import judge_lib as jl
from judge_lib import cls

WV = "web_verified"

# The citation is read from disk: the row's own mark before the A/B pass (Sorare's release on PR Newswire, read
# 2026-10-06: "gives Sorare a new valuation of $4.3 billion").
_OLD = json.loads((jl.INV / "scratch" / "classification-before-rebuild.json").read_text())
_OLD = _OLD.get("bessemer-venture-partners", _OLD)["sorare"]
PRN = _OLD["valuation_citation"]
assert "prnewswire.com" in PRN and _OLD["valuation_usd"] == 4_300_000_000 and _OLD["valuation_asof"] == "2021-09-21"

L = [
    cls("sorare", rng="1b_plus", usd=4_300_000_000, val_src=WV, val_cite=PRN, asof="2021-09-21",
        extra={"valuation_range_source": WV}, flags=["stale"],
        note="Cross-book 2026-10-06 (rule 10): the mark returns to the $680M Series B of September 2021, which "
             "'gives Sorare a new valuation of $4.3 billion' (Sorare's release, read), older than 24 months, so stale. "
             "Erik ruled on 2026-09-28 (Headline decisions.md E2) that this is the last priced mark and that layoffs "
             "do not band a row, with the unpriced insider round of September 2026 already known, so the below_1b "
             "reading of the A/B pass is withdrawn and the row agrees with the six sibling books."),
]

jl.write("cx1", L)
