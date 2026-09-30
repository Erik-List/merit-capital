"""Lead reversal of judge x1c's two X1 calls (PRO-100 NEA). The 13Gs were read in this pass. Before the 1998 passive
investor rule, a holder that was not an institution could file Schedule 13G instead of 13D only if it acquired the
shares before the class was registered or bought no more than 2% in any 12 months; a 5% stake reported at the first
year-end after the IPO therefore predates the listing."""
import judge_lib as jl

GM = "https://www.sec.gov/Archives/edgar/data/907111/0001029869-97-000137.txt"
PD = "https://www.sec.gov/Archives/edgar/data/858876/0001029869-97-000237.txt"
L = [
    jl.verdict("genemedicine-inc", "member",
        "A pre-listing holding shown by the filing route: New Enterprise Associates V filed on Schedule 13G, not 13D and "
        "not as an institution (Item 3 unchecked), and its Amendment No. 1 of February 1997 means NEA V reported 5% or "
        "more by the end of 1995, 18 months after the July 1994 IPO. Under the pre-1998 rules that route was open only "
        "to a holder that acquired before registration or bought at most 2% a year, which cannot reach 5% in that time; "
        "NEA V (1990) held the stake before the listing. No round is named.", ec="fund_filing", conf="medium", cite=GM),
    jl.verdict("penederm-inc", "member",
        "A pre-listing holding shown by the filing route: New Enterprise Associates IV filed on Schedule 13G (with ONSET, "
        "not as an institution), and its Amendment No. 3 of February 1997 means NEA IV first reported at the end of "
        "1993, weeks after the November 1993 IPO. Under the pre-1998 rules that route was open only to a holder that "
        "acquired before registration or bought at most 2% a year, so NEA IV (1988) held Penederm before the listing. "
        "No round is named.", ec="fund_filing", conf="medium", cite=PD),
]
jl.write("lead7", L)
