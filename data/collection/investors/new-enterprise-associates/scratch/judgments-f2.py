"""Fix brief F2 (PRO-100 NEA): boundary cases. R1 control positions, D8 sale consideration, R3 incubator vehicles.

Every verdict line carries a citation read in this pass. caremark-rx-inc is not written here: F1 already recorded it
as a member on the same MedPartners S-4 (Series A, September 1993), and a second record of its note would trip the
record note-join bug.
"""
import judge_lib as jl
from judge_lib import cls, rnd, verdict, SITE, ARCH, W, NEWS, POST, FTS

CTRL = {"exclusion": "control_position"}
L = []

# ---------------------------------------------------------------- R1: control positions
L.append(verdict("american-pathology-partners", "not_member",
    "R1 control test: American Pathology Partners was incorporated in February 2008 by three laboratory and hospital "
    "executives and in April 2008 secured a $75M equity commitment from NEA, the only investor named, then bought UniPath "
    "(Denver, December 2008), Eastern Carolina Pathology (2009) and Palm Beach Pathology's technical operation (2011) "
    "(Wikipedia). A single sponsor's equity commitment to a company formed to buy operating labs is a "
    "control position, not a minority financing. NEA's own percentage is not published, hence medium; flagged.",
    ec="web", conf="medium", cite=W("American Pathology Partners"), extra=CTRL))

SNN = NEWS("curana-health", "AllyAlign Health Snags")
L.append(verdict("curana-health", "member",
    "R1 control test: NEA's 2021 entry was leading a $300M investment in AllyAlign Health beside Oak HC/FT, Town Hall "
    "Ventures and existing investors Heritage Group and Ziegler, reported as a new investment that brought in Mark Price "
    "as CEO (Skilled Nursing News, 2021-06-10). In May 2022 AllyAlign, Elite Patient Care and Provider Health Services "
    "combined as Curana Health, which the firm's own post calls an NEA company formation. The record shows a syndicated "
    "financing, not a purchase of the company from its owners, and no record gives NEA a majority, so NEA holds a "
    "minority from a financing and the row is a member at Growth. Flagged: the firm's 'company formation' wording also "
    "covers Radiology Partners and Strive Health.",
    ec="web", conf="medium", cite=SNN))
L.append(cls("curana-health", entry_date="2021-06",
    rounds=[rnd("2021-06-10", "unnamed", 300000000, "NEA", True, SNN, "press")],
    note="Senior-living primary care and Medicare Advantage company. NEA entered in June 2021 by leading a $300M "
         "investment in AllyAlign Health with Oak HC/FT, Town Hall Ventures, Heritage Group and Ziegler, which brought in "
         "Mark Price as CEO (Skilled Nursing News); in May 2022 AllyAlign, Elite Patient Care and Provider Health Services "
         "united as Curana Health (the firm's post of 2022-05-04). Growth on the firm's own card."))

L.append(verdict("comprehensive-pharmacy-services", "not_member",
    "R1 control test: Frazier Healthcare Partners bought Comprehensive Pharmacy Services from NexPhase Capital, closing in "
    "March 2019 (NexPhase's exit to a financial sponsor, March 2019; Middle Market Growth). The firm gives its own first "
    "investment as 2019 with Mohamad Makhzoumi on the board, and the Private Equity Stakeholder Project's June 2022 table "
    "names Frazier Healthcare Partners and New Enterprise Associates among the owners when Trellis Rx bought the company. "
    "NEA entered beside Frazier in the buyout (the Frazier and NEA pairing of DSI Renal, Elements and RevSpring), so its "
    "co-investor group acquired control. No record gives NEA's own share, hence medium.",
    ec="web", conf="medium", cite=NEWS("comprehensive-pharmacy-services", "Private Equity Healthcare Acquisitions"),
    extra=CTRL))

TRIV_S1 = "https://www.sec.gov/Archives/edgar/data/1432732/000119312514091651/d638780ds1.htm"
L.append(verdict("trivascular", "not_member",
    "R1 control test, carve-out purchase: TriVascular was sold to Boston Scientific in 2005, and in March 2008 TV2 Holding "
    "Company 'acquired BSSR from Boston Scientific Corporation', paying partly with a $3.5M note (2014 S-1). The TV2 "
    "Series A that funded the purchase was about half NEA 12's (32.4M of 64.9M Series A shares in the S-1 holder table), "
    "and NEA's Jake Nunn joined the board in March 2008. The investor group bought the business outright, a control "
    "purchase rather than a minority financing. Flagged: if a venture syndicate's carve-out of a pre-revenue device "
    "business is ruled a venture entry, the row is a member at Series A (March 2008). Same company as the member row "
    "tv2-holding-co, which should follow this verdict.",
    ec="fund_filing", conf="medium", cite=TRIV_S1, extra=CTRL))

XCEL_S1 = "https://www.sec.gov/Archives/edgar/data/1139665/000095010902000119/ds1.htm"
L.append(verdict("xcel", "not_member",
    "R1 control test, carve-out purchase: Xcel Pharmaceuticals was founded in January 2001 to buy Elan's Diastat "
    "(worldwide) and Mysoline (US) product lines, acquired in March and April 2001 for a net $149.7M, $99M of it lent by "
    "Elan and the rest from its own equity, the Series A of March 2001 (IPO registration, January 2002). Domain Partners V (5.1M "
    "shares) and NEA 10 (5.0M) together held about 54% of the 18.7M shares outstanding, so the Series A investors, NEA "
    "among them, controlled a company formed to buy an operating product business. Flagged: if a venture-syndicated "
    "purchase of a product line is read as a financing, the row is a member at Series A (2001-03-30), as its "
    "classification already reads.",
    ec="fund_filing", conf="medium", cite=XCEL_S1, extra=CTRL))

GOLUB = "https://www.sec.gov/Archives/edgar/data/1476765/000114420414028416/v376994_10q.htm"
L.append(verdict("eci-acquisition-holdings", "uncertain",
    "R1 control test not decidable. The firm lists ECI Acquisition Holdings (ECi Software Solutions, Fort Worth business "
    "software for distributors and manufacturers, operating since the early 1980s) with a 2006 first investment and the "
    "label Early, and the page first appears in the Common Crawl of early 2014 (CC-MAIN-2014-10), around when Carlyle bought "
    "ECi (Carlyle release, 2014-03-12). ECI Acquisition Holdings, Inc. is that buyout's holding company: Golub Capital BDC's 10-Q for the "
    "quarter to March 2014 carries its one-stop loans maturing 03/2019 and a common stock position. What NEA bought in "
    "2006 (a minority growth round, or a stake later rolled into Carlyle's holding company) is in no record read. If the "
    "position is a rollover into the buyout it is out under control_position; if a 2006 minority round, a member at "
    "Growth. Left for review.",
    ec="web", conf="low", cite=GOLUB))

L.append(verdict("revspring", "not_member",
    "R1 control test: Frazier Healthcare Partners bought RevSpring from GTCR in March 2024, and 'Frazier was joined in the "
    "deal by NEA, 22C Capital, and RevSpring's senior leadership team' (Pulse 2.0, 2024-03-13). NEA was part of the "
    "buyer group that acquired the company, a control transaction, not a minority financing.",
    ec="web", conf="high", cite=NEWS("revspring", "Completes Acquisition Of RevSpring"), extra=CTRL))

L.append(verdict("elements-behavioral-health", "not_member",
    "R1 control test: Elements Behavioral Health (incorporated in 2007 as Subacute Holdings) sold $62.8M of an $80M "
    "offering from 2008-01-30 with NEA's Chip Linehan and Mohamad Makhzoumi and two Frazier Healthcare Ventures partners "
    "as directors (Form D), and in 2008 bought Promises Treatment Centers for about $30M, a purchase Frazier Healthcare "
    "Ventures and New Enterprise Associates 'helped cover' (Los Angeles Business Journal, 2010). A company the two "
    "sponsors funded to buy an operating business, the DSI Renal pattern, so out as a control position. Same company as "
    "the member row ebh-holding-company-inc, which should follow this verdict.",
    ec="web", conf="medium", cite=NEWS("elements-behavioral-health", "Remaking Promises"), extra=CTRL))

L.append(verdict("paladina-health", "not_member",
    "R1 control test: on 2018-06-01 NEA funds acquired, through NEAPH Holdings (later Everside Health Holdings), all of "
    "the outstanding equity interests of DaVita's direct primary care business, Paladina, for about $60.0M in cash "
    "(Everside Health's 2021 draft S-1, Certain Relationships). A buyout of the whole company, not a round. Same position "
    "as everside-health (already not_member) and marathon-health.",
    ec="fund_filing", conf="high", cite=FTS("Everside", "DRS"), extra=CTRL))

L.append(verdict("marathon-health", "not_member",
    "R1 control test: the firm's Marathon Health page (2018, Growth) is the Paladina position. Paladina, renamed Everside "
    "Health, merged with Marathon Health on 2024-02-08 under the Marathon name, with existing shareholders including "
    "General Atlantic, New Enterprise Associates and Oak HC/FT backing the combined company (PR Newswire). NEA never "
    "financed Marathon itself, which General Atlantic bought in 2019; its Marathon stock came from combining a "
    "company it bought outright from DaVita in 2018, so the row is out as that control position.",
    ec="web", conf="medium", cite=NEWS("marathon-health", "Demand for Advanced Primary Care Services - PR"), extra=CTRL))

# ---------------------------------------------------------------- D8: sale consideration
HIST = "https://historyofcomputercommunications.info/section/9.9/Robert-Metcalfe-and-the-Founding-of-3Com/"
L.append(verdict("3com-corporation", "member",
    "Not D8. Mayfield, New Enterprise Associates and Melchor Venture put $1.1M into 3Com on 1981-02-27, its first "
    "venture financing (History of Computer Communications), and the firm's own 2012 post names 'the funding of Bob "
    "Metcalfe and 3Com' as its nominee for NEA's most consequential tech investment. The firm's year 1996 is when 3Com "
    "bought OnStream Networks (the onstream row, NEA 1991), whose 3Com stock was sale consideration, but NEA had funded "
    "3Com itself fifteen years earlier, so the row is a member on the 1981 round.",
    ec="web", conf="high", cite=HIST))
L.append(cls("3com-corporation", entry_date="1981-02-27",
    rounds=[rnd("1981-02-27", "first venture financing (series not named)", 1100000, None, True, HIST, "press")],
    note="Networking company acquired by Hewlett-Packard in 2010, Marlborough by then (as the Sequoia row reads). NEA, "
         "Mayfield and Melchor Venture put $1.1M into 3Com on 1981-02-27, its first venture financing, and the firm's "
         "2012 post calls the funding of Bob Metcalfe and 3Com its most consequential tech investment. The firm's year "
         "1996 is 3Com's purchase of OnStream Networks (the onstream row). The 1981 round is not named in the record, so "
         "the stage stays undetermined."))

L.append(verdict("the-spectranetics-corporation", "not_member",
    "D8: NEA's Cornelius Bond sat on the board of Advanced Interventional Systems (LAIS) from 1986 until June 1994, when "
    "LAIS merged into Spectranetics, and joined Spectranetics' board at that merger (2001 proxy). No record shows an NEA "
    "fund in Spectranetics before the merger, and the firm's 2013 historical page gives no year, so the holding is stock "
    "received for LAIS. Advanced Interventional Systems is the member; it is not in base.json (a recall gap).",
    ec="fund_filing", conf="medium",
    cite="https://www.sec.gov/Archives/edgar/data/789132/000095013401500835/d86429ddef14a.txt"))

L.append(verdict("pharmos", "not_member",
    "D8: NEA 10 received 1,880,824 Pharmos shares on 2006-10-25 in exchange for its Series D preferred and notes of Vela "
    "Pharmaceuticals under the merger agreement of March 2006 (NEA's 13D, 2006-11-06); Pharmos was already listed on "
    "Nasdaq. Vela Pharmaceuticals is the member; it is not in base.json (a recall gap). NEA's later own money went into "
    "Pharmos' 10% convertible debentures (January 2008) and a common stock private placement (April 2009), both into a "
    "listed company, so they are X1 listed purchases rather than a separate venture entry. Flagged with X1: if PIPEs are "
    "ruled venture entries, Pharmos enters at Growth in January 2008.",
    ec="fund_filing", conf="high",
    cite="https://www.sec.gov/Archives/edgar/data/713275/000101297506000430/e8897702.txt"))

L.append(verdict("websidestory-inc", "not_member",
    "D8: WebSideStory, already listed, bought Avivo Corporation under a merger agreement of 2005-02-08 in which NEA's "
    "Charles Linehan was the Avivo holders' representative; NEA 10's 13G (event 2005-05-04) reports 1,340,766 "
    "WebSideStory shares, 7.15%, counted with the 3,123,149 shares issued under that merger. The stake is sale "
    "consideration for Avivo. Avivo Corporation is the member; it is not in base.json (a recall gap). The 2006 purchase "
    "of Visual Sciences, LLC gave NEA nothing (visual-sciences is already not_member).",
    ec="fund_filing", conf="high",
    cite="https://www.sec.gov/Archives/edgar/data/1091158/000107261305001192/sch13g_13532.txt"))

L.append(verdict("letgo", "not_member",
    "D8, a share swap at a combination: NEA invested in Wallapop in 2015 (the wallapop row), and in May 2016 Letgo merged "
    "with Wallapop's US operations, the merged company majority-owned by Letgo, with $100M of new money from Letgo's "
    "existing investors (Global Venturing, 2016-05-13), which names no NEA money. The firm's own posts call the holding "
    "'Letgo (Wallapop)', its listing gives 2016 as the year, and Letgo's 2017 backer list carries Wallapop's investors (Accel, "
    "Eight Roads, Insight, Mangrove, NEA, Northzone; FashionNetwork, 2017-10-04). NEA's Letgo interest is consideration "
    "for Wallapop's US business, not a round it bought (the Point Nine madvertise precedent); no record read shows NEA money "
    "in a Letgo round. Wallapop is the member and is in base.json (row wallapop).",
    ec="web", conf="medium", cite="https://globalventuring.com/blog/2016/05/13/letgo-gets-100m-with-a-wallapop/"))

GW18 = "https://www.sec.gov/Archives/edgar/data/1552345/000155234518000001/0001552345-18-000001-index.htm"
GW16 = "https://www.sec.gov/Archives/edgar/data/1552345/000155234516000002/0001552345-16-000002-index.htm"
GW12 = "https://www.sec.gov/Archives/edgar/data/1552345/000155234512000002/0001552345-12-000002-index.htm"
GOATV = NEWS("grubwithus", "GOAT valuation doubles")
L.append(verdict("grubwithus", "member",
    "Not D8: no sale took place. GrubWithUs, Inc. (EDGAR CIK 1552345) is the corporation that became GOAT: it filed a "
    "Series A-7 preferred Form D from Culver City in 2016 under the GrubWithUs name and was renamed 1661, Inc., GOAT's "
    "operating company, before its February 2018 Series C filing ($58.75M, Index's Danny Rimer on the board). NEA's 2011 "
    "seed stock is stock of the company that pivoted, so the listing, which now links goat.com, is a member.",
    ec="site_listing", conf="high", cite=GW18))
L.append(cls("grubwithus", status="private", rng="1b_plus", usd=3700000000, val_src="web_verified", val_cite=GOATV,
    asof="2021-06-25", val_conf="medium", flags=["stale"], city="Culver City", city_src="formd_address",
    rounds=[rnd("2012-05-15", "unnamed (Form D)", 7760573, None, None, GW12, "filing"),
            rnd("2016-05-23", "Series A-7", 4874997, None, None, GW16, "filing"),
            rnd("2018-02-05", "Series C", 58750027, None, None, GW18, "filing"),
            rnd("2021-06-24", "Series F", 195000000, "Park West Asset Management", None, GOATV, "press")],
    note="GrubWithUs, Inc. is the corporation that became GOAT (EDGAR: renamed 1661, Inc., GOAT's operating company, "
         "Culver City), so NEA's 2011 seed stock carries into GOAT; the dining product was shut, not the company. GOAT "
         "Group raised a $195M Series F led by Park West at a $3.7B valuation in June 2021 (Retail Dive), the last priced "
         "mark, stale. Stage from the firm's own label Seed. The a16z and First Round rows still read defunct. "
         "Graduation left for the graduation pass."))

# ---------------------------------------------------------------- R3: incubator vehicles
L.append(verdict("exploramed-iv", "not_member",
    "R3 (D5): the firm's own page describes 'a medical device incubator'; the issuer is ExploraMed IV, L.L.C., a Mountain "
    "View LLC run by Josh Makower that sold $6.6M in 2011 (Form D). No source shows it operating as a company of its "
    "own; the device companies ExploraMed forms are judged on their own rows.",
    ec="site_listing", conf="medium", cite=ARCH("exploramed-iv")))
L.append(verdict("exploramed-v", "not_member",
    "R3 (D5): the firm's own page describes a 'premier medical device incubator'; the issuer is ExploraMed V, L.L.C., "
    "which sold $8.8M in 2017 (Form D). No source shows it operating as a company of its own; the numbered NewCos ExploraMed "
    "forms (Willow, Revelle Aesthetics) are judged on their own rows.",
    ec="site_listing", conf="medium", cite=SITE("exploramed-v")))
L.append(verdict("prospex-medical-iii-inc", "not_member",
    "R3 (D5): the firm's own page describes 'a medical device incubator focused on innovating and incubating novel "
    "medical technologies'; Prospex Medical III, Inc. (White Bear Lake, Minnesota; 2011 Form D, $1.5M sold, no revenue) "
    "is one of Robert Atkinson's numbered Prospex vehicles, a name that also appears on the Form D filings of "
    "BridgePoint Medical, Apnex Medical and ClarVista Medical. No source shows it operating as a company of its own.",
    ec="site_listing", conf="medium", cite=ARCH("prospex-medical-iii-inc")))

ALLAY21 = "https://www.sec.gov/Archives/edgar/data/1766366/000176636621000004/0001766366-21-000004-index.htm"
L.append(verdict("foundry-therapeutics-1", "member",
    "R3 exception: the entity is itself an operating company. Foundry Therapeutics 1, Inc. (Menlo Park, CEO Karun Naga, "
    "$15.75M sold from 2019-01-31) was renamed Allay Therapeutics, Inc., the post-surgical pain company, under the same "
    "EDGAR CIK 1766366 (its 2021 Form D names Foundry Therapeutics 1 as the previous name). Same company as the listed "
    "member allay-therapeutics; identity-merges.json should fold this row into it.",
    ec="site_listing", conf="high", cite=ALLAY21))
L.append(cls("foundry-therapeutics-1", flags=["identity_conflated"],
    note="Foundry Therapeutics 1, Inc. is Allay Therapeutics, Inc. renamed (same EDGAR CIK 1766366; the 2021 Form D names "
         "the previous name), the post-surgical pain company NEA also lists as allay-therapeutics; this row should merge "
         "into that one."))

jl.write("f2", L)
