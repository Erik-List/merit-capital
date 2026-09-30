"""Fix pass F6 (lead): corrections from the A/B pass ab3."""
import judge_lib as jl
C13G = "https://www.sec.gov/Archives/edgar/data/906709/000102986997000139/0001029869-97-000139-index.htm"
L = [
    jl.verdict("nektar-therapeutics", "member",
               "Nektar is Inhale Therapeutic Systems renamed (one EDGAR filer, CIK 906709). NEA entities reported 1,888,410 "
               "shares, 16.0% of the class, in their Schedule 13G of February 1997, three years after the 1994 IPO: a "
               "venture-scale holding that predates the firm's own 2011 year for Nektar, so X1 does not apply (the firm's "
               "Public/PIPES label and year fail on the pre-1995 book, fix pass F1).",
               ec="fund_filing", conf="medium", cite=C13G),
    jl.cls("nektar-therapeutics", stage="undetermined", entry_date="1994",
           note="NEA held 16.0% of Inhale Therapeutic Systems (Nektar's former name) by February 1997 (13G); the round it "
                "entered is not named in any record read, so the stage is undetermined and the entry dated no later than "
                "the 1994 listing.",
           rounds=[]),
    jl.verdict("marker-therapeutics", "not_member",
               "NEA's first money went into the private placement that closed with the October 2018 reverse merger of Marker "
               "into listed TapImmune, a purchase at the listing (the Coatue R1 extension of X1: PIPE shares bought at a "
               "merger); no earlier NEA private round in Marker is on record. X1: a listed purchase (decisions.md); if Erik "
               "rules a PIPE a venture entry, this row enters at Growth.",
               ec="site_listing", conf="medium"),
    jl.cls("catalyst-biosciences", city="Winston-Salem",
           note="City is Targacept's (Winston-Salem), the company NEA held; San Diego was its successor's."),
    jl.cls("reneo-pharmaceuticals", city="Irvine",
           note="City is Reneo's (Irvine), the company NEA held; Boulder was OnKure's, which took over the listing."),
]
jl.write("f6", L)
