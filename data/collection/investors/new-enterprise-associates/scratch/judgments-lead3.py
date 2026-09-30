"""Lead ruling on delta judge g4's flag (PRO-100 NEA): Platinum Software rests only on a post-listing ownership
filing. Read in this pass."""
import judge_lib as jl

PLAT_13G = "https://www.sec.gov/Archives/edgar/data/891178/0001047469-99-005789.txt"
L = [jl.verdict("platinum-software-corp", "not_member",
    "X1: the firm has never listed Platinum Software, and NEA's only filing on it is the 13G/A (Amendment No. 3, "
    "1999-02-16) by New Enterprise Associates VI, reporting that the funds had fallen below 5% of a company listed "
    "since 1992. No NEA private round before the listing is on record (the stage pass found none in Google News, "
    "TechCrunch or EDGAR full text), so the position is a purchase into a listed company. If Erik rules such a "
    "purchase a venture entry, the row enters at Growth.", ec="fund_filing", conf="medium", cite=PLAT_13G)]
jl.write("lead3", L)
