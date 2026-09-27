"""PRO-162 heritage pass: archive-only rows that are positions of Bain Capital's generalist funds
(decisions.md D2, run-time ruling R1, flagged for Erik), plus the plainly non-venture rows of the
same listings (control acquisitions, public-company placements, a venture firm).

Evidence per row: the firm's own 2002-2010 listings (sources/wayback/parsed/, the outcome lines and
IPO dates it printed) and the firm's 2006 statement that "Bain Capital's history of investing in
early stage companies dates back to 1984 ... In 2001, we formed Bain Capital Ventures as a separate
arm" (HISTORY below). The dates are the companies' own public record (IPO dates as the firm's
listing prints them; the buyout years as their own histories give them)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
verdict = jl.verdict
HISTORY = ("https://web.archive.org/web/20060615151520/http://www.baincapitalventures.com:80/"
           "portfolio/index.asp?viewType=All&Section=3,0,0")
TAG = "[bain_capital_heritage] "
L = []


def heritage(slug, why, conf="high"):
    L.append(verdict(slug, "not_member",
        TAG + "Another desk (decisions.md D2, R1): " + why + " A position of Bain Capital's generalist funds "
        "(Bain Capital Fund I onward, today the private-equity family under CRD 145652's sister adviser CRD 145653), "
        "made before any Bain Capital venture vehicle existed; the firm's own 2006 page files these deals under "
        "'Bain Capital's history of investing ... since 1984' and dates BCV itself to 2001.",
        ec="site_listing", conf=conf, cite=HISTORY))


def control(slug, why, conf="high"):
    L.append(verdict(slug, "not_member",
        TAG + why + " A control acquisition is not a venture round (COLLECTION.md s1 T3 control positions; decisions.md D4), "
        "and it was made by Bain Capital's generalist buyout funds, not a venture vehicle (D2).",
        ec="site_listing", conf=conf, cite=HISTORY) | {"exclusion": "control_position"})


heritage("staples", "Staples was founded in 1986 with Bain Capital's investment (IPO 1989; the firm's listing prints 'IPO 03/26/90 (NASDAQ: SPLS)').")
heritage("bright-horizons", "Bain Capital backed Bright Horizons at its 1986 founding; IPO 1997 (the firm's listing: 'IPO 11/07/97 (NASDAQ: BFAM)').")
heritage("course-technology", "Course Technology (founded 1989) was a Bain Capital venture investment of 1990, sold to International Thomson in 1994.")
heritage("doubleclick", "Bain Capital invested in DoubleClick in 1997, ahead of its February 1998 IPO (the firm's listing: 'IPO 02/20/98').")
heritage("aspect-development", "Aspect Development went public in April 1996 (the firm's listing: 'IPO 04/26/96'); Bain Capital's position predates it.")
heritage("mercator-software-inc", "Mercator Software (then TSI International Software) went public in 1997 (the firm's listing: 'IPO 05/16/97'); Bain Capital's position predates it.")
heritage("oacis-healthcare-systems", "Oacis Healthcare Systems went public in 1996 (the firm's listing: 'IPO 05/01/96'); Bain Capital's position predates it.")
heritage("sports-authority", "The Sports Authority, a Bain Capital investment of the early 1990s (the firm's listing prints an IPO date of 1998 for it).")
heritage("babbages", "Babbage's, the software retailer Bain Capital backed in the 1980s (later GameStop; the firm's listing prints 'IPO 02/14/02 (NYSE: GME)').")
heritage("key-airlines", "Key Airlines, a Bain Capital investment of the 1980s.")
heritage("jostens-learning", "Jostens Learning, a 1992 Bain Capital acquisition from Jostens.")
heritage("the-learning-company", "The Learning Company, a Bain Capital investment of the 1990s.", conf="medium")
heritage("calumet-coach", "Calumet Coach, a Bain Capital investment of the 1980s.", conf="medium")
heritage("stericycle", "Stericycle, a 1989 Bain Capital venture investment (IPO 1996).")
heritage("abry-communications", "ABRY Communications, a television-station holding company Bain Capital backed in the 1980s and 1990s.", conf="medium")
heritage("blue-ridge-pharmaceuticals", "Blue Ridge Pharmaceuticals, a 1990s Bain Capital position.", conf="medium")
heritage("mediqual", "MediQual Systems, a Bain Capital position of the 1990s (IPO 1996).", conf="medium")
heritage("physicians-quality-care", "Physicians Quality Care, a 1990s Bain Capital physician-practice investment.", conf="medium")
heritage("vivra-specialty-partners", "Vivra Specialty Partners, a Bain Capital position of the late 1990s.", conf="medium")
heritage("dataware-technologies", "Dataware Technologies went public in 1993; Bain Capital's position predates it.", conf="medium")
heritage("fresh-samantha", "Fresh Samantha, the Maine juice maker Bain Capital backed in 1998 (sold to Odwalla in 2000).", conf="medium")
heritage("wefa-associates", "WEFA (Wharton Econometric Forecasting Associates), a Bain Capital position of the 1990s.", conf="medium")
heritage("frucor", "Frucor, the New Zealand beverage company Bain Capital owned in the late 1990s (sold to Danone in 2001).", conf="medium")
control("gartner-group", "Gartner Group was bought from Saatchi & Saatchi in a 1990 Bain Capital-led buyout and went public in 1993 (the firm's listing: 'IPO 10/05/93 (NYSE: IT)').")
control("experian-corporation", "Experian was TRW's credit-information business, bought by Bain Capital and Thomas H. Lee in 1996 and sold to Great Universal Stores the same year.")
control("waters-corporation", "Waters Corporation was bought from Millipore in Bain Capital's 1994 buyout.")
control("dade-behring", "Dade International (later Dade Behring) was bought from Baxter in Bain Capital's 1994 buyout.")
control("physio-control", "Physio-Control was bought from Eli Lilly in Bain Capital's 1994 buyout (the firm's listing: 'IPO 12/95').")
control("wesley-jessen-visioncare", "Wesley-Jessen was bought from Schering-Plough in Bain Capital's 1995 buyout.")
control("stage-stores-specialty-retailers", "Specialty Retailers (Stage Stores) was a 1988 Bain Capital buyout.")
control("nutraceutical-international", "Nutraceutical International was formed in a 1993 Bain Capital recapitalisation (the firm's listing: 'IPO 02/20/98 (NASDAQ: NUTR)').")
control("ddi-corp", "DDI (Dynamic Details) was acquired in Bain Capital's 1997 buyout (the firm's listing: 'IPO 04/11/00').")
control("stats-chippac-inc", "ChipPAC was bought from Hyundai Electronics in 1999 by Bain Capital and SXI Group.")
control("smtc-corp-hi-tech-man", "SMTC was formed in 1999 when Bain Capital's Hi-Tech Manufacturing combined with Surface Mount Technology.")
control("integrated-circuit-systems", "Integrated Circuit Systems was taken private in 1999 by Bain Capital and management and re-listed in 2000 (the firm's listing: 'IPO 05/22/00 (ICST)').", conf="medium")
L.append(verdict("village-ventures", "not_member",
    "Village Ventures is a venture capital firm (a network of regional seed funds, Williamstown, Massachusetts), not an "
    "operating company: a fund-shaped list entry (COLLECTION.md s1 T5, fund-shaped list entries; decisions.md D6).",
    ec="site_listing", conf="high", cite=HISTORY))
L.append(verdict("open-text", "not_member",
    "Open Text was listed on NASDAQ from 1996, before any position the firm's 2003 listing can reflect; a position in a "
    "listed company with no venture round in a private company is not a venture entry (COLLECTION.md s1 T3, post-RIA "
    "public purchases; decisions.md D4), and any pre-1996 position was the generalist funds' (D2).",
    ec="site_listing", conf="medium", cite=HISTORY))

if __name__ == "__main__":
    jl.write("heritage", L)
