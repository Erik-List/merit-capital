"""PRO-162 heritage pass 2 (decisions.md D2, R1): archive-only rows that Bain Capital Private Equity's own portfolio list carries
(sources/web/bain-pe-portfolio.json, read 2026-09-27) and that no record ties to a Bain Capital venture vehicle. The list carries
the generalist funds' positions and leaves out the venture funds' own of the same years (Taleo, Vonage, Tengion, aPriori); where a
venture vehicle is on record beside it (SquareTrade's 2012 agreement, TravelClick on the live 2007-vintage list), the row stays.
Medium confidence throughout: several are 1999-2002 deals, when the first venture fund could in principle have co-invested,
and no filing read names the holder. Flagged for Erik with R1 (COLLECTION.md s9 trigger 2)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
PE = "https://www.baincapitalprivateequity.com/portfolio/current-and-former-portfolio-companies"
L = []
ROWS = [
    ("closings-ltd", "Closings, Ltd. (the firm's 2006 page, 'Early', Acquired)", "Closings, Ltd."),
    ("cmc", "CMC (the firm's 2006 page, 'Early', Acquired)", "CMC"),
    ("convey-software", "Convey Software, formerly eTranslate (San Francisco; the firm's 2006 page, Acquired)", "Convey Software (Formerly eTranslate)"),
    ("etranslate", "eTranslate (San Francisco; the firm's 2003 page), later Convey Software", "Convey Software (Formerly eTranslate)"),
    ("environmental-data-resources-inc", "Environmental Data Resources (Milford, CT; the firm's 2003-2010 pages, Acquired)", "Environmental Data Resources"),
    ("imagitas", "Imagitas (Waltham, MA; the firm's 2006 page, Acquired; Pitney Bowes bought it in 2005)", "Targeted Marketing Solutions (Formerly Imagitas)"),
    ("iwon-com", "iWon (Irvington, NY; the firm's 2003-2010 pages), later part of Ask Jeeves", "AskJeeves (Formerly Bulldog, iWon)"),
    ("jtech", "JTECH Communications (Boca Raton, FL; the firm's 2003 and 2006 pages, Acquired)", "Jtech"),
    ("market-metrics", "Market Metrics (Quincy, MA; the firm's 2003 and 2006 pages, Acquired)", "Market Metrics"),
    ("medivision", "MediVision (Houston; the firm's 2003 and 2006 pages, Acquired)", "MediVision"),
    ("netlibrary", "NetLibrary (Boulder; the firm's 2006 page; OCLC bought its assets in 2002)", "NetLibrary"),
    ("oasis-asset-management", "Oasis Asset Management (North Sydney; the firm's 2006 page, Acquired)", "Oasis Asset Management"),
    ("professional-advantage-financial", "Professional Advantage (New York; the firm's 2006 page, Acquired; a vendor record dates its sale to March 2000)", "Professional Advantage"),
    ("profitlogic", "ProfitLogic (Cambridge, MA; the firm's 2003-2013 pages; Oracle bought it in July 2005)", "ProfitLogic"),
    ("shopping-com", "Shopping.com, formerly DealTime (the firm's 2003-2013 pages, 'Midstage'; IPO 2004, eBay 2005)", "Shopping.com (Formerly Dealtime.com)"),
    ("strategic-mapping", "Strategic Mapping (Santa Clara; the firm's 2006 page, Acquired; Claritas bought it in 1996)", "Strategic Mapping"),
    ("t-r-a-d-e-inc", "T.R.A.D.E., Inc. (Tampa; the firm's 2003 and 2006 pages, Acquired)", "T.R.A.D.E., Inc."),
]
for slug, what, entry in ROWS:
    L.append(jl.verdict(slug, "not_member",
        "[bain_capital_heritage] Another desk (decisions.md D1, D2, R1): " + what + ". Bain Capital Private Equity's own portfolio list "
        f"carries it ('{entry}'), beside the generalist-fund names (Staples, Bright Horizons, DoubleClick, Ameritrade), while the venture "
        "funds' positions of the same years (Taleo, Vonage, Tengion, aPriori) are absent from it; the firm never listed it on its live "
        "2007-vintage list, and no filing or release read names a Bain Capital venture vehicle as a holder.",
        ec="site_listing", conf="medium", cite=PE))
if __name__ == "__main__":
    jl.write("heritage-2", L)
