"""PRO-80 Bessemer, second pass s21, file a: three membership verdicts (listed-company purchases, T3 / R3),
the entry stages the firm's own archived sentences name, and old-book statuses and cities settled from the
firm's archive, Wikipedia and EDGAR."""
import json
from pathlib import Path

import judge_lib as jl

A = jl.ARCH
PK = json.loads((Path(__file__).resolve().parent / "evidence-pack.json").read_text())


def HIST(slug):
    """The firm's own 2008 history page, by the capture URL the evidence pack prints for the row."""
    return PK[slug]["history"]["capture_url"]


FU = "http://www.fundinguniverse.com/company-histories/fort-james-corporation-history/"
TULIP_IPO = "https://www.chittorgarh.com/ipo/tulip-it-services-ipo/3072/"
AIT = jl.NEWS("portrait-software", "Founder back in the AIT hotseat")
DKS_S1 = jl.FTS("DICKS SPORTING", "S-1")
HOTJ_S1 = "https://www.sec.gov/Archives/edgar/data/1087728/0001047469-99-023692-index.html"
NTGX_S1 = "https://www.sec.gov/Archives/edgar/data/1004874/0000950135-99-005679-index.html"
VIA_S1 = "https://www.sec.gov/Archives/edgar/data/1098402/0000950109-99-004246-index.html"
MSI_S1 = "https://www.sec.gov/Archives/edgar/data/1086216/0000912057-00-009749-index.html"
BVP = "Bessemer Venture Partners"

lines = [
    # ---- membership: first Bessemer money into a company that was already listed (decisions.md D5, R3)
    jl.verdict("james-river", "not_member",
               "Purchase of an already listed company (decisions.md D5, T3): the firm's own archived text says BVP "
               "invested in James River Corp. in 1978 and 'James River was public at the time'; the company went "
               "public on 1973-03-16 (FundingUniverse company history, read 2026-10-06) and the firm lists no "
               "earlier private round. A later version of the firm's text dates the offering to 1980, which the "
               "company history does not support.",
               ec="site_listing", cite=A("james-river"), conf="high",
               extra={"ipo_citation": FU}),
    jl.verdict("portrait-software", "not_member",
               "Financing of an already listed company (decisions.md D5, T3 / R3): AIT Group plc, later Portrait "
               "Software, was a London-listed company whose shares were suspended in 2002; the Evening Standard "
               "reports the rescue loan 'is to be provided by US-based Bessemer Venture Partners and a string of "
               "private investors' beside a rights issue and a move to AIM. The firm lists 2002 and no earlier "
               "private round.",
               ec="web", cite=AIT, conf="high"),
    jl.verdict("tulip-telecom", "not_member",
               "BVP India purchase of an already listed company (decisions.md R3, T3): Tulip IT Services, later "
               "Tulip Telecom, listed on the BSE and NSE on 2006-01-05 after its December 2005 offering "
               "(chittorgarh.com IPO record, read 2026-10-06), and the firm's own list dates its investment to 2007 "
               "with no earlier private round.",
               ec="web", cite=TULIP_IPO, conf="medium"),

    # ---- entry stages named by the firm's own archived sentences
    jl.cls("parametric-technology", stage="Series A", stage_src="first_party", stage_cite=A("parametric-technology"),
           stage_conf="high",
           rounds=[jl.rnd("1987", "First institutional round", lead=BVP, firm_in_round=True,
                          source=A("parametric-technology"), source_type="firm")],
           note="Second pass: the firm's archived listing says Felda Hardymon and Don Feddersen 'led the company's "
                "first institutional round in 1987', read as Series A. The Y Combinator row named Parametric is a "
                "different company, a name collision."),
    jl.cls("u-s-behavioral-health", stage="Series A", stage_src="first_party",
           stage_cite=A("u-s-behavioral-health"), stage_conf="high",
           rounds=[jl.rnd("1987", "First institutional round", firm_in_round=True,
                          source=A("u-s-behavioral-health"), source_type="firm")],
           note="Second pass: the firm's archived listing says Chris Gabrieli 'invested in the first institutional "
                "round' in 1987 and joined two more rounds, read as Series A."),
    jl.cls("magnuson-computer-systems", status="defunct", stage="Series A", stage_src="first_party",
           stage_cite=A("magnuson-computer-systems"), stage_conf="medium",
           city="San Jose",
           rounds=[jl.rnd("1979", "First round", firm_in_round=True, source=A("magnuson-computer-systems"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says Neill Brownstein 'invested in the first round' in "
                "1979, read as Series A since nothing shows an earlier seed. Wikipedia: the maker of IBM-compatible "
                "mainframes declared bankruptcy in March 1983, so defunct. City from memory."),
    jl.cls("veritas", stage="Growth", stage_src="first_party", stage_cite=HIST("veritas"), stage_conf="medium",
           rounds=[jl.rnd("1991", "Turn-around financing of Tolerant Computing", lead=BVP, firm_in_round=True,
                          source=HIST("veritas"), source_type="firm")],
           note="Second pass: the firm's own history page says Neill Brownstein 'led the turn-around financing of "
                "Tolerant Computing, later named Veritas Software'. A turn-around financing recapitalises a "
                "company that had already raised venture rounds, a later round, so Growth at medium confidence."),
    jl.cls("dick-s-sporting-goods", stage="Series A", stage_src="first_party",
           stage_cite=A("dick-s-clothing-sporting-goods"), stage_conf="medium",
           rounds=[jl.rnd("1991", "First institutional round", firm_in_round=True,
                          source=A("dick-s-clothing-sporting-goods"), source_type="firm"),
                   jl.rnd("2002-07-17", "IPO filing; preferred series A to G converted", firm_in_round=True,
                          source=DKS_S1, source_type="filing")],
           note="Second pass: the firm's archived listing of the same company under its older name (base row "
                "dick-s-clothing-sporting-goods) says 'BVP invested in the company's first institutional round'; "
                "the 2002 S-1 shows lettered preferred series A to G, so the first is read as Series A. The retailer "
                "dates from 1948, so this was growth capital in substance."),
    jl.cls("vistacare", stage="Series A", stage_src="first_party", stage_cite=A("vistacare"), stage_conf="medium",
           rounds=[jl.rnd("1995", "First round", lead=BVP, firm_in_round=True, source=A("vistacare"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says Chris Gabrieli 'led the first round in VistaCare', "
                "read as Series A since nothing shows an earlier seed. The 2002 S-1 confirms the Scottsdale "
                "headquarters."),
    jl.cls("data-labs", stage="Series A", stage_src="first_party", stage_cite=A("data-labs"), stage_conf="high",
           rounds=[jl.rnd("1996", "First venture round", lead=BVP, firm_in_round=True, source=A("data-labs"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says David Cowan 'led the first venture round of Data "
                "Labs' in 1996, read as Series A; Yurie Systems bought it in December 1997."),
    jl.cls("webspective", stage="Series A", stage_src="first_party", stage_cite=A("webspective"),
           stage_conf="high", city="Andover",
           rounds=[jl.rnd("1997", "First venture round", lead=BVP, firm_in_round=True, source=A("webspective"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says 'In 1997 BVP led the first venture round of "
                "Webspective', read as Series A. Inktomi bought it in November 1999 for $106M in stock (Wikipedia, "
                "Inktomi). City (Andover, Massachusetts) from memory."),
    jl.cls("hotjobs", stage="Series A", stage_src="first_party", stage_cite=A("hotjobs"), stage_conf="high",
           entry_date="1999-05-10",
           rounds=[jl.rnd("1999-05-10", "Series A", amount_usd=16200000, firm_in_round=True, source=HOTJ_S1,
                          source_type="filing")],
           note="Second pass: the firm's archived listing says David Cowan 'participated in the first "
                "institutional round'; the 1999 S-1 shows that round was the Series A preferred sold effective "
                "1999-05-10 (1,620,000 shares at $10) and names the Bessemer funds as holders, so the entry date "
                "is corrected from 1998."),
    jl.cls("counterpane", stage="Series A", stage_src="first_party", stage_cite=HIST("counterpane"),
           stage_conf="high",
           rounds=[jl.rnd("1999-08-05", "Series A", lead=BVP, firm_in_round=True, source=HIST("counterpane"),
                          source_type="firm")],
           note="Second pass: the firm's own history page says Bruce Schneier 'turned to David Cowan at Bessemer to "
                "lead the Series A round in his startup Counterpane'."),
    jl.cls("ocular-networks", stage="Series A", stage_src="first_party", stage_cite=A("ocular-networks"),
           stage_conf="medium", city="Reston",
           rounds=[jl.rnd("2000-01-11", "First financing round", firm_in_round=True, source=A("ocular-networks"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says 'BVP invested in both of the company's financing "
                "rounds in 2000', so it was in the first round (the firm's date 2000-01-11), read as Series A since "
                "nothing shows an earlier seed. City (Reston, Virginia) from memory."),
    jl.cls("trigo", stage="Series A", stage_src="first_party", stage_cite=A("trigo"), stage_conf="medium",
           city="Brisbane",
           rounds=[jl.rnd("2000-08-08", "First institutional round", firm_in_round=True, source=A("trigo"),
                          source_type="firm")],
           note="Second pass: the firm's archived listing says David Cowan 'participated in all of Trigo's "
                "institutional rounds from its founding in 1999', so the entry is the first institutional round, "
                "read as Series A. City (Brisbane, California) from memory."),

    # ---- entry stages from filings and documented later rounds
    jl.cls("on-technology", stage="Growth", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("1994", "Round to fund the DaVinci Systems acquisition", lead=BVP, firm_in_round=True,
                          source=A("on-technology"), source_type="firm")],
           note="Second pass: the firm's archived listing says David Cowan 'led a round to fund ON's acquisition of "
                "DaVinci Systems' in 1994; ON Technology was founded in 1987 and venture-backed from the start, so "
                "this was a later round, Growth, from knowledge at medium confidence. Wikipedia dates the Symantec "
                "acquisition to October 2003 and the IPO to 1995."),
    jl.cls("netgenesis", stage="Growth", stage_src="web_verified", stage_cite=NTGX_S1, stage_conf="high",
           entry_date="1996-09-18",
           rounds=[jl.rnd("1996-09-18", "Series B", firm_in_round=True, source=NTGX_S1, source_type="filing"),
                   jl.rnd("1997-09-12", "Series C", firm_in_round=True, source=NTGX_S1, source_type="filing"),
                   jl.rnd("1998-06-25", "Series D", firm_in_round=True, source=NTGX_S1, source_type="filing"),
                   jl.rnd("1999-06-10", "Series F", firm_in_round=True, source=NTGX_S1, source_type="filing")],
           note="Second pass: the December 1999 S-1 lists the preferred the Bessemer funds bought, starting with "
                "344,187 shares of Series B on 1996-09-18 beside Charles River, then Series C, D and F. The record "
                "names the entry Series B, so Growth, although it was the first venture round after a small Series "
                "A. The S-1 confirms Cambridge."),
    jl.cls("via-net-works", status="acquired", stage="Growth", stage_src="model", stage_conf="medium",
           rounds=[jl.rnd("1997-08", "Series A", amount_usd=1488657, firm_in_round=None, source=VIA_S1,
                          source_type="filing"),
                   jl.rnd("1998-05", "Series B", amount_usd=51586005, firm_in_round=None, source=VIA_S1,
                          source_type="filing"),
                   jl.rnd("1999-04", "Series C", amount_usd=127857948, firm_in_round=True, source=VIA_S1,
                          source_type="filing")],
           note="Second pass: the 1999 S-1 lists a small Series A (about $1.5M over 1997 and April 1998), a $51.6M "
                "Series B in May 1998 and a Series C in April 1999, and the Bessemer funds signed the 1999 "
                "stockholders agreement. The firm's own year is 1998, which matches the Series B, so Growth at "
                "medium confidence. Interoute bought its European operations in 2005 (Wikipedia, Interoute) and "
                "the company deregistered in November 2005, so acquired with that successor."),
    jl.cls("metapath", city="Bellevue", city_src="web_verified",
           rounds=[jl.rnd("1994-12", "Round at inception", firm_in_round=True, source=MSI_S1, source_type="filing"),
                   jl.rnd("1997-10", "Class E preferred", firm_in_round=True, source=MSI_S1, source_type="filing"),
                   jl.rnd("1998-07", "Class F preferred", firm_in_round=True, source=MSI_S1, source_type="filing")],
           note="Second pass: the March 2000 S-1 of Metapath Software International says Felda Hardymon sat on "
                "Metapath's board 'from its inception in December 1994', names the unit Metapath Software "
                "International (Bellevue) and shows Bessemer buying Class E and F preferred in 1997 and 1998. The "
                "firm says it joined every round from 1994 but no source names the first one (seed or Series A), "
                "so the stage stays undetermined."),

    # ---- old book: statuses and cities
    jl.cls("quantor", city="Mountain View", focus="Industrial & Robotics",
           note="Second pass: the firm's archived text calls it a 'manufacturer of microfiche systems' acquired by "
                "NCR in 1978, and says BVP invested in 1974 where its list says 1970; the list year is kept. City "
                "(Mountain View) from memory. No round named."),
    jl.cls("galileo-electro-optics", status="acquired",
           note="Second pass: EDGAR carries the company as NetOptix Corp, formerly Galileo Corp and Galileo "
                "Electro-Optics Corp of Sturbridge; Corning filed the merger communication on 2000-04-26 and the "
                "company deregistered on 2000-05-12, so acquired by Corning, 2000."),
    jl.cls("circadian", status="defunct", city="San Jose", city_src="web_verified",
           note="Second pass: EDGAR places Circadian Inc (electromedical apparatus) at 3942 North First Street, San "
                "Jose, and shows the SEC revoking its registration on 2011-04-25 with no filings on record, so it "
                "is read as defunct; what became of the business is not on record."),
    jl.cls("gmis", status="acquired", city="Malvern", city_src="web_verified",
           note="Second pass: the firm's archived listing says GMIS went public in 1991 and 'was later acquired by "
                "McKesson'; from knowledge the buyer was HBO & Company in 1997, which McKesson absorbed in 1999. "
                "EDGAR places GMIS Inc in Malvern, Pennsylvania."),
    jl.cls("psinet", status="acquired", city="Ashburn", city_src="web_verified",
           note="Second pass: Wikipedia has PSINet filing for Chapter 11 on 2001-06-01 and Cogent Communications "
                "buying most of its United States assets in April 2002, so acquired with that successor rather "
                "than defunct (asset sale out of insolvency); last headquarters Ashburn, Virginia. Wikipedia names "
                "Matrix, Sigma and Amerindo as its venture investors, not the round Bessemer joined in 1993."),
    jl.cls("itc-holding-company-magnolia-holding", status="acquired", city="West Point",
           note="Second pass: West Corporation's 8-K/A says it completed on 2003-05-09 the purchase of InterCall "
                "by merging a subsidiary into its parent ITC Holding Company, Inc.; Magnolia Holding Company of "
                "Valley, Alabama then appears on EDGAR holding the group's ITC DeltaCom shares. An operating "
                "telecom group, acquired by West Corporation, 2003. City (West Point, Georgia) from memory."),
]

jl.write("s21a", lines)
