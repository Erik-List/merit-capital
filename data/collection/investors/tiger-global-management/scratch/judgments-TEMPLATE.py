#!/usr/bin/env python3
"""TEMPLATE (do not run): the pattern for judgments-<N>.py. Copy it, replace
the example lines with your batch's rows, run with NQ_TAG=b<N>.

Every citation comes from a helper or from a URL a tool printed; the examples
below show each helper once. Illustrative values only.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS, SEC

N = 0            # your batch number
L = []           # the lines

# 1. A listed member (verdict already seeded as site_listing): classification only.
L.append(cls("example-co",
             status="acquired", rng="below_1b",
             stage="undetermined",                      # the record names no round
             country="US", city="Palo Alto", focus="Data Infrastructure",
             note="Acquired by ExampleCorp 2004 ("
                  "ExampleCorp's 8-K names the deal). Tiger's entry round is not on record."))

# 2. A public $1B+ member: market cap cited, as-of date, web_verified band.
# L.append(cls("example-public-co", status="public", rng="10b_plus", usd=25_000_000_000,
#              val_src="web_verified", val_cite="https://stockanalysis.com/stocks/xxx/market-cap/",
#              asof="2026-09-28", extra={"valuation_range_source": "web_verified"},
#              stage="Series A", stage_src="web_verified", stage_cite=SEC("example-public-co", "edgar"),
#              stage_conf="high", entry_date="1993",
#              rounds=[rnd("1993-04", "Series A", 2_000_000, "Sutter Hill Ventures", True,
#                          "https://www.sec.gov/...S-1...", "filing")],
#              country="US", city="Santa Clara", focus="Industrial & Robotics",
#              note="..."))

# 3. A Form D-only row: membership first.
#    member (two lines):
# L.append(verdict("example-formd-co", "member",
#                  "Mike Speiser (Tiger managing director, in tenure) is director and executive officer on the "
#                  "2015 Form D, filing from 755 Page Mill Road; the company is an Tiger incubation (D3)",
#                  ec="formd_adjudicated", conf="medium", cite=SEC("example-formd-co")))
# L.append(cls("example-formd-co", status="acquired", rng="below_1b", stage="undetermined",
#              country="US", city="Palo Alto", focus="AI & Applied AI", note="..."))
#    not a member (one line):
# L.append(verdict("example-homonym-co", "not_member",
#                  "James White on this Form D files from Birmingham, AL, a bank's address: a homonym of "
#                  "Tiger's Jim White; no Tiger listing or filing names the company",
#                  ec="formd_adjudicated", conf="high", cite=SEC("example-homonym-co")))

if __name__ == "__main__":
    raise SystemExit("template only")
    jl.write(f"batch-{N:03d}", L)
