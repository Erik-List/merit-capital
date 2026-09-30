"""Fix pass F5: membership checks raised by the stage pass (PRO-100 NEA). Every citation below was read in this pass
(SEC documents through secget.py, the one web page through a fetch). arca-biopharma-inc was already ruled not_member
under X1 by pass ab3 with the same facts, so it is not re-recorded here."""
import judge_lib as jl

S1_HELIOGEN_F3 = "https://www.sec.gov/Archives/edgar/data/1840292/000110465922076977/0001104659-22-076977-index.htm"
SATSUMA_8K = "https://www.sec.gov/Archives/edgar/data/1692830/000119312521094589/d160344dex991.htm"
NURO_8K = "https://www.sec.gov/Archives/edgar/data/1289850/000110465909054426/a09-26244_3ex99d1.htm"
DURA_COURT = "https://case-law.vlex.com/vid/in-re-dura-pharmaceuticals-888255891"
PREMIER_SB2 = "https://www.sec.gov/Archives/edgar/data/878543/0000912057-96-010533.txt"
PCORDER_424 = "https://www.sec.gov/Archives/edgar/data/1068726/0001012870-99-000660.txt"
AMISYS_424 = "https://www.sec.gov/Archives/edgar/data/1003202/0000928385-96-000671.txt"
TEMPEST_S4 = "https://www.sec.gov/Archives/edgar/data/1544227/000119312521114415/d150774ds4.htm"
ARYX_RRA = "https://www.sec.gov/Archives/edgar/data/1410064/000110465908070034/a08-28250_1ex4d9.htm"
CENSTOR_10K = "https://www.sec.gov/Archives/edgar/data/932094/0000891618-96-002187.txt"
GZ_424 = "https://www.sec.gov/Archives/edgar/data/1015446/0000912057-96-012539.txt"
OPTA_PROXY = "https://www.sec.gov/Archives/edgar/data/883326/0000927016-97-001116.txt"
CTRL = {"exclusion": "control_position"}

L = []

L.append(jl.verdict("heliogen-inc", "not_member",
    "D4 (T4), a person's seat at his next firm: every Heliogen Form 3 and 4 behind this row (July and August 2022) is "
    "filed by Krishna Kolluri, NeoTribe Ventures I, NeoTribe Partners I and NeoTribe Associates I, the shares held "
    "directly by NeoTribe Ventures I. Kolluri was an NEA general partner on the firm's archived people pages to 2016 and "
    "is the managing member of NeoTribe's general partner, his firm after NEA. No NEA entity is a reporting person, EDGAR full text finds no mention of New Enterprise "
    "Associates in any Heliogen filing (NeoTribe returns 50), and the firm has never listed Heliogen. The row came in "
    "only because Kolluri's own filer number was among NEA's filers.",
    ec="fund_filing", conf="high", cite=S1_HELIOGEN_F3))

L.append(jl.verdict("satsuma-pharmaceuticals-inc", "not_member",
    "X1 and R2: NEA's entry is the $80M private placement of common stock Satsuma closed in March 2021, led by Commodore "
    "Capital and NEA (company release), bought through Growth Equity Opportunities 17 into a company listed on Nasdaq "
    "since its September 2019 IPO. The August 2019 S-1 holder table names RA Capital, TPG, Shin Nippon Biomedical, "
    "Wellington, Osage, CAM, Cormorant, Citadel and Eventide and no NEA fund, and EDGAR full text finds no mention of "
    "NEA in any Satsuma filing before March 2021. No earlier NEA private round. If Erik rules a PIPE a venture entry, "
    "the row enters at Growth in March 2021.",
    ec="fund_filing", conf="high", cite=SATSUMA_8K))

L.append(jl.verdict("neurometrix-inc", "not_member",
    "X1 and R2: NEA's entry is NeuroMetrix's September 2009 private placement of common stock and warrants ($18.7M, led "
    "by Deerfield, New Enterprise Associates participating; company release), held through Growth Equity Opportunities "
    "(NEA 12), into a company listed on Nasdaq since its July 2004 IPO. The 2004 IPO prospectus names its pre-IPO "
    "holders (J.H. Whitney, Delphi, Harris & Harris, BancBoston and others) and no NEA fund, and EDGAR full text finds "
    "no mention of NEA in any NeuroMetrix filing before September 2009. No earlier NEA private round. If Erik rules a "
    "PIPE a venture entry, the row enters at Growth in September 2009.",
    ec="fund_filing", conf="high", cite=NURO_8K))

L.append(jl.verdict("dura-pharmaceuticals", "not_member",
    "X1: the firm's own page gives 1993 as the year of NEA's first investment, and Dura became a publicly traded "
    "company in 1992 (In re Dura Pharmaceuticals Securities Litigation, S.D. Cal. 2006). Dura's 1997 proxy shows no NEA holder and no NEA director, EDGAR "
    "carries no NEA filing on Dura, and no source shows an NEA private round before the listing, so the 1993 purchase "
    "was into the listed company. The page's 'Early' label and its description (synthetic peptides for allergies and "
    "asthma, not Dura's respiratory products business) do not match the record, hence medium. If Erik rules a PIPE a "
    "venture entry, the row enters at Growth in 1993.",
    ec="web", conf="medium", cite=DURA_COURT))

L.append(jl.verdict("premier-laser-systems-inc", "member",
    "Not X1: NEA's position predates the listing. Premier Laser listed through its December 1994 IPO; its 1996 SB-2 "
    "lists an Amended and Restated Registration Rights Agreement of June 17, 1994 among the company, Onset Enterprise "
    "Associates, New Enterprise Associates IV and Franklin Capital Associates, the three venture firms that received "
    "$1.5M of secured notes in December 1993, exchanged them for convertible debentures in June 1994, and took 321,099 "
    "units for them at the IPO. NEA IV's 13G/A of February 1997 reports it has ceased to hold more than 5%. Flagged: "
    "the notes were issued in connection with Premier's purchase of Proclosure's laser technology, and the filings do "
    "not say whether they were new money or part of the price for Proclosure's assets; if the latter, D8 applies and "
    "Proclosure (not in base.json) is the member. Hence medium.",
    ec="fund_filing", conf="medium", cite=PREMIER_SB2))
L.append(jl.cls("premier-laser-systems-inc", entry_date="1993-12",
    rounds=[jl.rnd("1993-12", "Secured notes, exchanged for convertible debentures (June 1994), converted into IPO units "
                   "(December 1994)", 1500000, None, True, PREMIER_SB2, "filing")],
    note="Fix pass F5: NEA IV entered before the December 1994 IPO, as one of three venture holders (with Onset "
         "Enterprise Associates and Franklin Capital) of $1.5M of secured notes issued in December 1993 with the "
         "Proclosure technology purchase, exchanged for convertible debentures in June 1994 and converted into IPO "
         "units (1996 SB-2). Not a listed purchase; no round is named, so the stage stays undetermined."))

L.append(jl.verdict("pcorder", "not_member",
    "D2 and D4, a partner's seat without fund money: pcOrder was a wholly owned Trilogy subsidiary until its February "
    "1999 IPO. The IPO prospectus has Trilogy holding 98.3% before the offering and the rest in management options; "
    "Peter Barris, a director since June 17, 1998, is listed with no shares, and no NEA fund appears. The later "
    "ownership filings on pcOrder (1999-2000) are by Janus, FMR, Trilogy, West Highland and Gabelli, none by an NEA "
    "entity, and Trilogy took pcOrder private in its 2000 tender offer. No NEA fund held pcOrder; if the firm's "
    "money sat anywhere it was in Trilogy, which is not established and is not this row.",
    ec="fund_filing", conf="high", cite=PCORDER_424))

L.append(jl.verdict("amisys-managed-care", "not_member",
    "R1 control test: AMISYS (then American International Healthcare) was bought from AIG on May 26, 1994 for $10.0M "
    "cash through AIH Systems, Inc., which merged into it. All 4,800,000 Class A shares issued for the acquisition went "
    "to Greylock Equity (2,000,000), New Enterprise Associates VI and affiliates (2,000,000) and ABS Capital Partners "
    "(800,000), against 450,000 Class B shares, so the co-investor group acquired control of the whole "
    "company (May 1996 offering prospectus, Certain Transactions). A control acquisition, not a minority financing. "
    "Flagged: Greylock's row for the same company reads member, a cross-investor pair for rule 10.",
    ec="fund_filing", conf="high", cite=AMISYS_424, extra=CTRL))

L.append(jl.verdict("tempest-therapeutics", "not_member",
    "D8, the Battery reverse-merger reading: in 2021 private Tempest merged into listed Millendo, which took the "
    "Tempest name. The merger S-4 shows NEA's stake on the Millendo side (1,766,407 shares held by New Enterprise "
    "Associates 15 and 372 by NEA Ventures 2015, 8.8% of Millendo), while Legacy Tempest's 5% holders are the Versant "
    "entities, F-Prime, Quan Venture Fund, LYFE Capital and LAV Regulus, and the Series B buyers the S-4 names include no NEA fund. "
    "Mike Raab, a Legacy Tempest director, holds personally and left NEA for Ardelyx by 2009. NEA's Tempest stock is Millendo stock "
    "carried through the merger, not an investment in Tempest; Millendo (row millendo, acquired) is the member.",
    ec="fund_filing", conf="high", cite=TEMPEST_S4))

L.append(jl.verdict("aryx-therapeutics-inc", "not_member",
    "X1 and R2: NEA's entry is the November 2008 private placement in which Growth Equity Opportunities Fund (member: "
    "New Enterprise Associates 12) bought ARYx common stock under a securities purchase and registration rights "
    "agreement, into a company listed on Nasdaq since its November 2007 IPO. The IPO registration's holder table names "
    "MPM Capital, Nomura Phase4 Ventures and OrbiMed and no NEA fund, and EDGAR full text finds no mention of New "
    "Enterprise Associates in any ARYx filing before November 2008. No earlier NEA private round. If Erik rules a PIPE "
    "a venture entry, the row enters at Growth in November 2008.",
    ec="fund_filing", conf="high", cite=ARYX_RRA))

L.append(jl.verdict("censtor-corp-ca", "member",
    "Not X1: Censtor was never listed. Its 1996 10-K reports no established public trading market for any class of its "
    "equity; it filed with the SEC only because its Series B preferred had 557 holders (registered under 12(g)). New "
    "Enterprise Associates V and Spectra Enterprise Associates (an NEA sleeve, D1) held 1,424,590 shares of Series A "
    "and Series B preferred, 5.86%, and NEA partner James A. Cole, Spectra's managing general partner, sat on the board "
    "from October 1992. A venture preferred position in a private company; NEA's 13G was filed under Rule 13d-1(d).",
    ec="fund_filing", conf="high", cite=CENSTOR_10K))
L.append(jl.cls("censtor-corp-ca", status="defunct",
    note="Fix pass F5, correcting the stage pass note: Censtor was never listed (1996 10-K: no established public "
         "trading market); NEA V and Spectra held Series A and Series B preferred, with NEA's James Cole on the board "
         "from October 1992. Censtor sold its manufacturing and R&D operations to Read-Rite in July 1996, kept only "
         "patent licensing, stopped filing after 1999 and had its registration revoked in 2011, so it is defunct."))

L.append(jl.verdict("graphix-zone-inc-de", "not_member",
    "X1 and D8: the listed Graphix Zone, Inc. (Delaware) is the 1996 holding company that combined Graphix Zone "
    "(California) and StarPress. Graphix Zone had been listed since its June 1994 IPO, and NEA bought its common stock in "
    "a February 1996 private placement, a purchase into a listed company; the rest of NEA V's 900,114 shares (8.5% at "
    "end-1996) came from its 5,370,064 StarPress shares (16.06% of StarPress), exchanged at 0.14666 in the "
    "reorganization, which is merger consideration (1996 joint proxy statement and prospectus). No NEA private round "
    "in Graphix Zone before its listing. StarPress had itself acquired StarPress Multimedia, Inc., the likely venture "
    "position behind NEA's StarPress stock; neither is in base.json and that route is not established.",
    ec="fund_filing", conf="high", cite=GZ_424))

L.append(jl.verdict("opta-food-ingredients-inc-de", "member",
    "Not X1: NEA held Opta before its March 1992 IPO. Opta was incorporated in April 1991 from the food ingredients "
    "division of its predecessor Enzytech (an NEA company), and its 1997 proxy describes director Charles W. Newhall III, on the board "
    "since 1991, as a general partner of NEA Partners IV, the general partner of New Enterprise Associates IV, 'a "
    "venture capital partnership that is an investor in the Company'. NEA IV and NEA VI held 577,500 shares (5.26%) in "
    "1997. NEA VI's larger block (472,500 shares) is not shown to predate the IPO, "
    "so the membership rests on NEA IV's pre-listing position. The filings read do not say whether NEA IV's shares came "
    "from a 1991 formation round or from Enzytech's division, hence medium.",
    ec="fund_filing", conf="medium", cite=OPTA_PROXY))
L.append(jl.cls("opta-food-ingredients-inc-de", entry_date="1991",
    note="Fix pass F5: NEA IV held Opta before the March 1992 IPO, Charles Newhall on the board from 1991, the year Opta "
         "was incorporated from Enzytech's food ingredients division (1997 proxy and 10-K); NEA VI's 472,500 shares are not "
         "shown to predate the listing. No round is named, so the stage stays undetermined."))

jl.write("f5", L)
