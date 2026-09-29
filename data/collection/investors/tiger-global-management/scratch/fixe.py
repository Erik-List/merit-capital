#!/usr/bin/env python3
"""PRO-167 Tiger Global, verify-gap fix e (2026-09-29): Avant, whose new $1B+ band (fix c) made its uncited stage a
verify gap. Tiger's entry is the Series C it led in July 2014 (the company's release); the mark moves from Crain's
'close to $2 billion' to the stated $1.975B of the 2015 Series E (BuzzFeed News).
Run: NQ_TAG=fx python3 fixe.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402
from judge_lib import cls, rnd, NEWS  # noqa: E402
from fxlib import SRC, BURL, MARK  # noqa: E402

L = []

u = BURL("avant", "AvantCredit Secures $75 Million Series C Funding Led by Tiger Global", "prnewswire")
bf = NEWS("avant", "Online Lender Avant Gets $2 Billion Valuation")
L.append(cls("avant", stage="Growth", stage_src="web_verified", stage_cite=u, stage_conf="high",
             entry_date="2014-07-23", flags=("stale",), **MARK(bf, 1_975_000_000, "2015-09-29"),
             rounds=[rnd("2013-08", "Series B", None, None, False, u, "company"),
                     rnd("2014-07-23", "Series C", 75_000_000, "Tiger Global", True, u, "company"),
                     rnd("2014-12-04", "Series D", 225_000_000, "Tiger Global and August Capital", True,
                         SRC("avant-series-d"), "company"),
                     rnd("2015-09-29", "Series E", 325_000_000, "General Atlantic", True, bf)],
             note="Verify fix 2026-09-29 (second line): entry cited. AvantCredit's release (2014-07-23): a '$75 million "
                  "round of Series C funding led by Tiger Global Management'; 'Subsequent to its contributions to "
                  "AvantCredit's Series B funding in August 2013, Victory Park Capital is joined by Tiger Global', so "
                  "the Series C is Tiger's entry: Growth, web_verified. Tiger co-led the $225M Series D (December "
                  "2014, where DFJ Growth, RRE, KKR and Peter Thiel were the first-time investors) and stayed in the "
                  "Series E. Mark refined: the Series E 'would value the company at $1.975 billion' (BuzzFeed News, "
                  "2015-09-29, naming Tiger among the existing investors), replacing the Crain's 'close to $2 "
                  "billion'; still 1b_plus and stale."))

if __name__ == "__main__":
    jl.write("fix-e", L)
