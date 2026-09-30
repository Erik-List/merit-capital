"""Lead ruling on delta judge g3a's flag (PRO-100 NEA): Aquila Biopharmaceuticals rests only on post-listing 13Gs.
Read in this pass."""
import judge_lib as jl

AQ_13G = "https://www.sec.gov/Archives/edgar/data/704292/0001047469-99-005798.txt"
L = [jl.verdict("aquila-biopharmaceuticals-inc", "not_member",
    "X1: the firm has never listed Aquila, and NEA's only filings on it are 13Gs of 1999 and 2000 by New Enterprise "
    "Associates VI (374,176 shares, 5.4%) on a company listed since its 1996 emergence from Cambridge Biotech's "
    "reorganisation; the judge read the purchase as April 1998. No NEA private round in Aquila is on record. If the "
    "shares were consideration for Aquila's 1998 purchase of VacTex, the reading is D8 instead, with the same "
    "outcome.", ec="fund_filing", conf="medium", cite=AQ_13G)]
jl.write("lead4", L)
