#!/usr/bin/env python3
"""Batch 2 of the Sutter Hill Ventures grind (PRO-77). Run: NQ_TAG=b2 python3 judgments-2.py

Every citation comes from a helper (SEC, NEWS, W, ARCH) or from a URL a tool
printed in this session (EDGAR submissions listings, stockanalysis pages fetched
with curl, WebSearch results, sibling notes)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS, SEC

N = 2
L = []
WV = {"valuation_range_source": "web_verified"}
CLR = {"entry_date": None, "entry_stage_source": None}   # a band's date and source leave with its stage

# ---- S-1 / F-1 index pages (printed by the EDGAR submissions listing)
S1_PRAECIS = "https://www.sec.gov/Archives/edgar/data/1033025/000091205700004383/0000912057-00-004383-index.htm"
S1_THERMA = "https://www.sec.gov/Archives/edgar/data/828119/000092962499000662/0000929624-99-000662-index.htm"
S1_VIRAGE = "https://www.sec.gov/Archives/edgar/data/1101147/000089161800000573/0000891618-00-000573-index.htm"
S1_VITRIA = "https://www.sec.gov/Archives/edgar/data/1050808/000101287099002032/0001012870-99-002032-index.htm"
S1_VIROBAY = "https://www.sec.gov/Archives/edgar/data/1374261/000119312514337978/0001193125-14-337978-index.htm"
S1_ADEXA = "https://www.sec.gov/Archives/edgar/data/1119691/000091205700039247/0000912057-00-039247-index.htm"
F1_YOUKU = "https://www.sec.gov/Archives/edgar/data/1442596/000119312510260191/0001193125-10-260191-index.htm"
S1_RESTO = "https://www.sec.gov/Archives/edgar/data/1409269/000119312517275553/0001193125-17-275553-index.htm"
S1_THRESHOLD = "https://www.sec.gov/Archives/edgar/data/1183765/000119312504059933/0001193125-04-059933-index.htm"
S1_SHUTTERFLY = "https://www.sec.gov/Archives/edgar/data/1125920/000095014906000362/0000950149-06-000362-index.htm"
S1_QUIN = "https://www.sec.gov/Archives/edgar/data/1117297/000095012309064388/0000950123-09-064388-index.htm"
S1_YEXT = "https://www.sec.gov/Archives/edgar/data/1614178/000104746917001510/0001047469-17-001510-index.htm"
S1_PURE = "https://www.sec.gov/Archives/edgar/data/1474432/000119312515287576/0001193125-15-287576-index.htm"
S1_SNOW = "https://www.sec.gov/Archives/edgar/data/1640147/000162828020013010/0001628280-20-013010-index.htm"
S1_ACCEL = "https://www.sec.gov/Archives/edgar/data/1280600/000104746913008148/0001047469-13-008148-index.htm"
FD_SILVERRAIL_2023 = "https://www.sec.gov/Archives/edgar/data/1470328/000110465923042439/0001104659-23-042439-index.htm"
# ---- market caps and other pages fetched with curl in this session
MC_AAC = "https://stockanalysis.com/quote/hkg/2018/market-cap/"
PROF_AAC = "https://stockanalysis.com/quote/hkg/2018/company/"
MC_SNOW = "https://stockanalysis.com/stocks/snow/market-cap/"
MC_PURE = "https://stockanalysis.com/stocks/p/market-cap/"
UPI_AIDA = "https://www.upi.com/Archives/1987/11/03/Teradyne-to-acquire-AIDA-Corp/1450562914000/"
EISAI_AKARX = ("https://www.prnewswire.com/news-releases/eisai-completes-acquisition-of-akarx-inc-and-continues-"
               "development-of-akr-501-for-thrombocytopenia-80845092.html")
LOLA_ROOM77 = "https://medium.com/@lola.com/lola-to-acquire-hotel-search-site-room-77-55f9404cf675"
USV_RETURNPATH = "https://www.usv.com/writing/2008/10/return-path/"
RDX_PROSTOR = "https://www.rdxworks.com/prostor-sells-rdx-technology-tandberg.aspx"

# ======================================================================
# Membership: two listed rows leave the base.
# ======================================================================
L.append(verdict(
    "acacia-venture-partners", "not_member",
    "The firm's own 1999 table lists Acacia as a 'Health services investment partnership', outcome 'Private "
    "partnership', and its 2008 to 2016 pages file Acacia Venture Partners under 'Investment Partnerships': an LP "
    "interest in another venture firm, not an operating company (D6, T5).",
    ec="site_listing", conf="high", cite=ARCH("acacia-venture-partners")))

v = verdict(
    "thermawave-inc", "not_member",
    "Control position (T3, D4): SHV's holding came from the May 1997 recapitalization in which 'Bain Capital, Inc., "
    "Sutter Hill Ventures and our senior management team collectively acquired securities representing "
    "approximately 88% of our outstanding voting power' (Therma-Wave S-1, 1999), buying the company from Toray and "
    "Shimadzu, which had owned it since fiscal 1992; Bain Capital Funds held 61% and SHV 18.1%. A majority recap by "
    "the firm's co-investor group is not a venture entry. The firm's 1999 table lists it as 'Private company', "
    "the post-recap holding.",
    ec="web", conf="high", cite=S1_THERMA)
v["exclusion"] = "control_position"
L.append(v)

# ======================================================================
# Classification lines (members; the verdicts are seeded as site_listing).
# ======================================================================

L.append(cls(
    "praecis-pharmaceuticals", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_PRAECIS, stage_conf="medium", entry_date="1994-03",
    country="US", city="Waltham", city_src="web_verified", focus="Healthcare & Bio",
    rounds=[rnd("1994", "Series A", 10500000, None, True, S1_PRAECIS, "filing")],
    note="Peptide drugs (abarelix), Waltham, Massachusetts (EDGAR registrant address; the 2000 S-1 still gave "
         "Cambridge). GlaxoSmithKline bought it in early 2007 (Praecis deregistered on 2007-02-16), so acquired, "
         "below_1b; agrees with the Greylock row. The firm's 1999 table: 'Private company'. Entry: the 2000 S-1 "
         "shows Series A convertible preferred ($10.5M liquidation preference) as the first financing of a company "
         "that began operations in January 1994, and G. Leonard Baker of SHV on the board since March 1994; SHV's "
         "1.29M common-equivalent shares far exceed its only later purchase in the S-1's table (84,409 Series E "
         "shares), so the entry reads as the Series A, dated to Baker's arrival (medium)."))

L.append(cls(
    "prostor-systems", status="acquired", rng="below_1b",
    stage="undetermined", city="Boulder", city_src="formd_address", focus="Data Infrastructure",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("2010-06-25", "Form D, round not named", 5500000, None, None, SEC("prostor-systems"), "filing")],
    note="Removable-disk backup and archive (RDX, InfiniVault), Boulder, Colorado. In 2011 it sold its RDX business "
         "to Tandberg Data (May) and InfiniVault to Imation (August) and wound down (ProStor's own release, "
         f"{RDX_PROSTOR}; eWeek, 'Imation Acquires InfiniVault From ProStor Systems'): an asset sale out of a "
         "wind-down, so acquired, below_1b. DISPUTE of the Seed band: the band read the June 2010 $5.5M Form D, but "
         "that filing says ProStor was incorporated over five years before (the firm's page: founded May 2004), and "
         "its director Ron Bernal had left SHV (Sequel from 2006, NEA from 2010; D5), so the filing dates neither "
         "the company's first round nor SHV's entry (the PRO-157 withholding rule). SHV's round is not on record. "
         "No Seed entry, so no graduation."))

L.append(cls(
    "pure-storage", status="public", rng="10b_plus", usd=43120000000, val_src="web_verified", val_cite=MC_PURE,
    asof="2026-09-28", extra=dict(WV),
    stage="Series A", stage_src="web_verified", stage_cite=S1_PURE, stage_conf="high", entry_date="2009-11-04",
    city="Santa Clara", focus="Data Infrastructure", flags=["stage_disputes_band", "model_disputes_source"],
    rounds=[rnd("2009-10-10", "founders' common", 3050, None, False, SEC("pure-storage", i=2), "filing"),
            rnd("2009-11-04", "Series A", 5075000, "Sutter Hill Ventures", True, S1_PURE, "filing"),
            rnd("2010-07-23", "Series B", 20000000, None, None, S1_PURE, "filing"),
            rnd("2011-05-26", "Series C", 30444000, None, None, S1_PURE, "filing"),
            rnd("2012-08-07", "Series D", 39916000, None, None, S1_PURE, "filing"),
            rnd("2013-08-22", "Series E", 171187000, None, None, S1_PURE, "filing")],
    note="All-flash storage, incorporated October 2009 as OS76, Inc. inside SHV's office (Wikipedia; the S-1), "
         "now named Everpure, headquartered in Santa Clara. DISPUTE of the Pre-Seed band (D3): the band read the "
         "$3,050 founders' filing of October 2009 (Mike Speiser and John Colgrove filing from Palo Alto); the round "
         "SHV's fund bought is the first preferred round, which the 2015 S-1 names Series A ($5.075M; the $5M Form D "
         "of 2009-11-04), with Speiser as SHV's board designee. Valuation: market cap $43.12B on 2026-09-28 "
         "(stockanalysis.com, ticker P), replacing the prefilled 2025 public float of $17.0B, which is corroboration "
         "only; 10b_plus either way, agreeing with the Greylock, IVP and Redpoint rows."))

L.append(cls(
    "quinstreet-inc", stage="Series A", stage_src="web_verified", stage_cite=S1_QUIN, stage_conf="high",
    entry_date="1999-07", country="US", city="Foster City", focus="Media, Gaming & Advertising",
    rounds=[rnd("1999-07", "Series A", None, None, True, S1_QUIN, "filing")],
    note="Performance marketing (online lead generation), Foster City. Entry: the 2009 S-1 says 'The holders of a "
         "majority of our Series A preferred stock ... have designated Gregory Sands and James Simons' for the board, "
         "the investor rights agreement gives one of those seats to a nominee of Sutter Hill Ventures, and Sands "
         "(SHV since 1998) has been a director since July 1999, three months after the April 1999 incorporation: "
         "SHV bought the Series A. Public (Nasdaq QNST), below_1b as prefilled (market cap $811M on 2026-09-28). "
         "Not a Seed entry, so no graduation."))

L.append(cls(
    "redseal-inc", status="private", rng="below_1b", stage="undetermined",
    city="Menlo Park", city_src="web_verified", focus="Security",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("2009-09-23", "Form D, equity, round not named", 12000000, None, None,
                "https://www.sec.gov/Archives/edgar/data/1305683/000130568309000003/0001305683-09-000003-index.htm",
                "filing"),
            rnd("2019-04", "equity investment by STG Partners", None, "STG Partners", None,
                NEWS("redseal-inc", "RedSeal Receives Equity Investment from STG"), "press")],
    note="Network security posture and exposure management, founded 2004 as RedSeal Systems. STG Partners made an "
         "equity investment in April 2019 (FinSMEs) and the company still trades under its own name (product "
         "launches through August 2025); its contact page gives 'RedSeal, Inc. c/o Symphony Technology Group, 1300 "
         "El Camino Real, Menlo Park' as headquarters. Whether STG holds control is not on record, so private; no "
         "priced round at $1B or more found, below_1b. DISPUTE of the Pre-Seed band: it read a $2,088 option filing "
         "of December 2010; the first e-filed round was the $12M equity round of September 2009, whose Form D says "
         "the company was incorporated over five years before, and SHV listed it from 2008 with Tench Coxe as its "
         "director. SHV's entry round is not on record."))

L.append(cls(
    "restoration-robotics", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_RESTO, stage_conf="high", entry_date="2005-07",
    city="San Jose", city_src="formd_address", focus="Healthcare & Bio",
    rounds=[rnd("2005-07", "Series A", 11292000, None, True, S1_RESTO, "filing"),
            rnd("2014", "Series C", 114874000, None, True, S1_RESTO, "filing")],
    note="Robotic hair restoration (ARTAS), San Jose (the later Form Ds). Merged with Venus Concept in November 2019, "
         "the combined company taking the Venus Concept name: acquired as prefilled, below_1b. Entry: the 2017 S-1's "
         "voting agreement gives Sutter Hill Ventures the right to elect 'the other Series A designee' (Alloy "
         "Ventures the first), and Jeffrey Bird of SHV has been a director since July 2005; the Series A ($11.3M "
         "liquidation preference) was the first preferred round of a company incorporated in November 2002, so SHV "
         "entered at the Series A, dated to Bird's arrival. SHV also bought 4,450,948 Series C shares from 2014. The "
         "June 2011 Form D the prefill dated from was a later round. No Seed entry, so no graduation."))

L.append(cls(
    "return-path", status="acquired", rng="below_1b", stage="undetermined",
    city="New York", city_src="formd_address", focus="SaaS",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("1999", "first venture round", None, "Flatiron Partners", None, USV_RETURNPATH, "firm"),
            rnd("2008-10", "later-stage round (USV)", None, None, None, USV_RETURNPATH, "firm"),
            rnd("2009-07-24", "Form D, round not named", 5499999, None, None, SEC("return-path", i=0), "filing")],
    note="Email deliverability and certification data, New York. Validity bought it in May 2019 (MediaPost, 'Email "
         "Vendor Return Path Being Sold To Validity'), so acquired, below_1b; agrees with the USV row. DISPUTE of the "
         "Seed band: Return Path dates from 1999 (Flatiron invested in its first venture round that year) and USV's "
         f"own post of 2008-10-30 ({USV_RETURNPATH}) names 'our good friends Sutter Hill' as an existing investor "
         "when USV made a later-stage investment, so the July 2009 $5.5M Form D (Greg Sands of SHV a director; the "
         "filing says incorporated over five years before) is neither the company's first round nor SHV's entry. "
         "SHV's round is not on record. No Seed entry, so no graduation."))

L.append(cls(
    "right-hemisphere", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Ramon", city_src="web_verified", focus="SaaS",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("2009-03-27", "Form D, round not named", 9999969, None, None, SEC("right-hemisphere"), "filing")],
    note="3D product-graphics and visualization software. SAP agreed to buy it on 2011-09-06, describing it as "
         "'based in San Ramon, California, and Auckland, New Zealand' (SAP's release, "
         f"{NEWS('right-hemisphere', 'SAP to Acquire 3-D Visualization Software Maker')}), so acquired, below_1b; "
         "US and San Ramon agree with Sequoia's row (the 2009 Form D gave Pleasanton). DISPUTE of the Series A band: "
         "the March 2009 $10M Form D the band read says the company was incorporated over five years before, and SHV "
         "already listed it in 2008 (Jim White of SHV its director), so that filing does not date SHV's entry. SHV's "
         "round is not on record."))

L.append(cls(
    "room77", status="acquired", rng="below_1b", city="Mountain View", city_src="formd_address",
    focus="Consumer & Marketplaces",
    note="Hotel search (metasearch) site, Mountain View (the Form Ds). Lola, Paul English's travel-agent app, "
         f"acquired Room 77 in November 2016 (Lola's own post, {LOLA_ROOM77}; PhocusWire, 'Travel startup Lola "
         "acquires Room 77, the hotel metasearch platform'; Skift, 'Lola Travel Agent App Acquires Room 77 "
         "Technology') and kept it running as a hotel search tool, so the business continued under a buyer: "
         "acquired, below_1b. This disputes the Felicis and General Catalyst rows (defunct) with cited evidence; "
         "Felicis's own note records the Lola deal. The prefilled Growth entry (the $30.3M round from December "
         "2012, James White of SHV a director) stands."))

L.append(cls(
    "satmetrix-systems", status="acquired", rng="below_1b", stage="undetermined",
    city="San Mateo", city_src="formd_address", focus="SaaS",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("2009-09-04", "bridge notes (debt)", 1000000, None, None, SEC("satmetrix-systems", i=0), "filing"),
            rnd("2010-09-15", "Form D, equity, round not named", 4537559, None, None, SEC("satmetrix-systems", i=1),
                "filing"),
            rnd("2011-08-09", "Form D, equity, round not named", 16750001, None, None, SEC("satmetrix-systems", i=2),
                "filing")],
    note="Customer loyalty and Net Promoter software, San Mateo (the Form Ds). NICE bought it: it trades as NICE "
         "Satmetrix by June 2018 (PR Newswire, 'Kaiser Permanente Again Tops Annual Consumer Loyalty Study'; CX "
         f"Today, {NEWS('satmetrix-systems', 'NICE Satmetrix Review')}), so acquired, below_1b. DISPUTE of the Seed "
         "band: the September 2009 filing it read is a $1.0M debt offering (bridge notes) by a company its own Form "
         "D says was incorporated over five years before, followed by equity rounds of $4.5M (2010) and $16.8M "
         "(2011); a note is not a seed round. SHV's entry round is not on record (Jim White of SHV a director from "
         "the first e-filing). No Seed entry, so no graduation."))

L.append(cls(
    "seesaw", status="defunct", rng="below_1b", stage="undetermined",
    city="San Francisco", city_src="formd_address", focus="Media, Gaming & Advertising",
    extra=dict(CLR),
    rounds=[rnd("2009-05-06", "convertible notes", 1000000, None, None, SEC("seesaw", i=0), "filing"),
            rnd("2010-04-27", "Form D, equity, round not named", 6088876, None, None, SEC("seesaw", i=3), "filing"),
            rnd("2011-06-15", "notes", 1000000, None, None, SEC("seesaw", i=5), "filing")],
    note="SeeSaw Networks, media planning and buying for out-of-home digital video networks, San Francisco (100 Bush "
         "Street; the Form Ds), incorporated 2005. Its filings end with 2011 bridge notes, its domain "
         "seesawnetworks.com is now for sale, and data vendors list it as closed with no acquirer; no buyer was "
         "found, so defunct (a quiet shutdown; no dated notice), below_1b. Entry: the first e-filed Form Ds (2009) "
         "are convertible notes with Jim Gaither and Tench Coxe of SHV as directors; vendors date a first round to "
         "November 2006 with SHV as its main institutional investor, but no citable source names SHV's round, so "
         "undetermined. NAME COLLISION: First Round Capital's 'seesaw' row is Seesaw the classroom learning journal, "
         "a different company; do not align."))

L.append(cls(
    "shutterfly", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=S1_SHUTTERFLY, stage_conf="high", entry_date="2005-11",
    city="San Jose", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    rounds=[rnd("2005-11", "Series F", 20000000, "Sutter Hill Ventures", True, S1_SHUTTERFLY, "filing")],
    note="Photo books, cards and prints, now headquartered in San Jose (Wikipedia); IPO 2006, taken private by "
         "Apollo in 2019: acquired as prefilled, below_1b. DISPUTE of the band's date: the 2006 S-1 says 'In November "
         "2005, we sold 1,353,730 shares of our Series F preferred stock to Sutter Hill Ventures and affiliated "
         "persons and entities at a purchase price of $14.774 per share' (about $20.0M), with a voting agreement "
         "giving SHV a board seat (James White); SHV also bought common from former officers in 2005 and 2006. The "
         "entry is that Series F, Growth; the 2011 $222M Form D the prefill used was stock issued for the Tiny "
         "Prints acquisition, not a financing SHV joined."))

L.append(cls(
    "sifive", status="private", rng="1b_plus", usd=3650000000, val_src="web_verified",
    val_cite=NEWS("sifive", "SiFive raises $400m Series G at $3.65bn"), asof="2026-04-09", extra=dict(WV),
    stage="Series A", stage_src="web_verified",
    stage_cite=NEWS("sifive", "Design your own RISC-V SoC with SiFive"), stage_conf="high", entry_date="2015-09",
    city="Santa Clara", focus="Industrial & Robotics", flags=["stage_disputes_band"],
    rounds=[rnd("2015-09-04", "Series A", 5062500, "Sutter Hill Ventures", True, W("SiFive"), "press"),
            rnd("2017-05", "Series B", 8500000, "Spark Capital", True,
                NEWS("sifive", "Design your own RISC-V SoC with SiFive"), "press"),
            rnd("2018-02-09", "Series C", 50600000, None, None, W("SiFive"), "press"),
            rnd("2019-06", "Series D", 65400000, "Sutter Hill Ventures (co-lead)", True, W("SiFive"), "press"),
            rnd("2020-08", "Series E", 60000000, "SK Hynix, Saudi Aramco", None, W("SiFive"), "press"),
            rnd("2022-03", "Series F", 175000000, "Coatue", None, W("SiFive"), "press"),
            rnd("2026-04-09", "Series G", 400000000, "Atreides Management", None,
                NEWS("sifive", "SiFive raises $400m Series G at $3.65bn"), "press")],
    note="RISC-V processor IP and chips, Santa Clara (agrees with the Coatue and Spark rows). Private; the Series G "
         "of 2026-04-09 ($400M, led by Atreides, NVIDIA and Apollo joining) valued it at $3.65B (The Next Web), "
         "1b_plus, matching both siblings. DISPUTE of the Seed band: Wikipedia records that 'In September 2015, "
         "SiFive raised $5 million in Series A funding', the company's first round (Form D, first sale 2015-09-04, "
         "$5.06M), and LinuxGizmos (2017-05-08) reports the $8.5M Series B 'led by Spark Capital, and also included "
         "participation from Osage University Partners and earlier investor Sutter Hill Ventures', bringing the "
         "total to $13.5M: the only earlier money was that $5M Series A, so SHV's entry is the Series A. Stefan "
         "Dyckerhoff of SHV is director and executive officer on the Form Ds. SHV later co-led the 2019 Series D. "
         "No Seed entry, so no graduation."))

L.append(cls(
    "sila-nanotechnologies", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
    val_cite=NEWS("sila-nanotechnologies", "Next-gen battery startup Sila raises $300M"), asof="2024-06-27",
    extra={**WV, **CLR}, stage="undetermined", city="Alameda", city_src="web_verified", focus="Climate & Energy",
    flags=["stage_disputes_band", "stale"],
    rounds=[rnd("2018-08-16", "Series D", 70000000, "Sutter Hill Ventures", True,
                NEWS("sila-nanotechnologies", "Announces $70 Million in Series D"), "company"),
            rnd("2021-01-26", "Series F", 590000000, None, None,
                NEWS("sila-nanotechnologies", "Sila Nano Hauls In $590 Million"), "press"),
            rnd("2024-06-27", "Series G", 375000000, "Sutter Hill Ventures", True,
                NEWS("sila-nanotechnologies", "As battery startups fail, Sila snaps up"), "press"),
            rnd("2026-07-21", "financing (Series H)", 300000000, "Atreides Management, Sutter Hill Ventures", True,
                NEWS("sila-nanotechnologies", "Next-gen battery startup Sila raises $300M"), "press")],
    note="Silicon anode battery materials, Alameda ('headquartered in Alameda, California', its 2018 release). "
         "Valuation: GeekWire (2026-07-21) reports that Sila 'was valued at close to $2 billion two years ago', the "
         "June 2024 Series G that SHV led (Bloomberg, 2024-09-24: 'Sila Nanotechnologies Takes $1 Billion Valuation "
         "Haircut With Latest Round', down from the January 2021 Series F mark); the July 2026 $300M round disclosed "
         "no valuation. So 1b_plus at about $2.0B, stale (older than 24 months). This disputes the 8VC row "
         "(below_1b on an assumed repricing, with no figure) with a cited priced mark. DISPUTE of the Growth band: "
         "the band dated SHV's entry to the 2018 Series D, but the firm listed Sila under Mike Speiser in 2013 (a "
         "Common Crawl capture of shv.com/portfolio of December 2013, and the 2013 Wayback page), so SHV held it "
         "about five years before that round; the 2018 release calls SHV the Series D lead and names no earlier SHV "
         "round, so the round SHV first entered is not on record."))

L.append(cls(
    "silverrail-technologies", status="private", rng="below_1b",
    country="GB", country_src="web_verified", country_cite=FD_SILVERRAIL_2023,
    city="London", city_src="web_verified", focus="SaaS", flags=["model_disputes_source"],
    rounds=[rnd("2017", "majority stake sold to Expedia", 148000000, None, None,
                NEWS("silverrail-technologies", "Expedia Spent $148 Million"), "press"),
            rnd("2020-10", "management buyout from Expedia Group", None, None, None,
                NEWS("silverrail-technologies", "SilverRail Technologies in management buyout"), "press"),
            rnd("2023-02-27", "Form D, equity, round not named", 20000000, None, None, FD_SILVERRAIL_2023,
                "filing")],
    note="Rail ticket distribution and booking technology, founded 2009 near Boston. Expedia bought a majority stake "
         "in 2017 (Skift, 'Expedia Spent $148 Million to Buy SilverRail'), and management bought the business back "
         "from Expedia Group in October 2020 (PhocusWire, 'SilverRail Technologies in management buyout from "
         "Expedia Group'); SilverRail then raised again as an independent issuer (Form D, first sale 2023-02-27, "
         "$15M of $20M sold) from 27 Maiden Lane, London. So it is private today: fresher cited evidence than "
         "Accel's row (acquired, Expedia), which should align. No priced round at $1B found, below_1b. Country and "
         "city follow the 2023 Form D (London, United Kingdom), disputing the Woburn-era US prefill. The prefilled "
         "Series A entry (the 2009 round, James White of SHV a director) stands."))

L.append(cls(
    "skyport-systems", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=SEC("skyport-systems", i=0), stage_conf="high",
    entry_date="2013-06-28", city="Mountain View", city_src="formd_address", focus="Security",
    flags=["stage_disputes_band"],
    rounds=[rnd("2013-06-28", "Series A", 7000000, "Sutter Hill Ventures", True, SEC("skyport-systems", i=0),
                "filing"),
            rnd("2014-06-17", "Series B", 29999989, None, True, SEC("skyport-systems", i=1), "filing"),
            rnd("2016-01-19", "Series C", 30000001, "GV", True, SEC("skyport-systems", i=2), "filing")],
    note="Secure hyperconverged infrastructure (SkySecure), Mountain View. Fortune (2016-03-15, "
         f"{NEWS('skyport-systems', 'Alphabet and Cisco Fund Ex-HP Security')}): Stefan Dyckerhoff of SHV "
         "'originally incubated the company at his venture capital firm while serving as interim CEO', and SHV was "
         "an existing investor in the $30M Series C led by GV. Cisco bought it in early 2018, so acquired, below_1b. "
         "DISPUTE of the Seed band (D3): the incubation's first preferred round, which its own Form D names 'Series A "
         "Preferred Stock' ($7.0M, first sale 2013-06-28), is SHV's entry, not the Seed the band read from its size. "
         "No Seed entry, so no graduation."))

L.append(cls(
    "smartsheet", rng="below_1b", city="Bellevue", city_src="formd_address", focus="SaaS",
    note="Work management software, Bellevue, Washington. IPO 2018, taken private by Blackstone and Vista in January "
         "2025 (Wikipedia): acquired as prefilled, so below_1b with no figure; agrees with the Insight row. The "
         "prefilled Growth entry (the $35M round of 2014, Jim White of SHV a director) stands."))

L.append(cls(
    "snowflake-inc", status="public", rng="100b_plus", usd=115650000000, val_src="web_verified", val_cite=MC_SNOW,
    asof="2026-09-28", extra=dict(WV),
    stage="Series A", stage_src="web_verified",
    stage_cite=NEWS("snowflake-inc", "How Low-Profile VC Firm Sutter Hill"), stage_conf="medium",
    entry_date="2013-03-08", city="Menlo Park", city_src="web_verified", focus="Data Infrastructure",
    flags=["stage_disputes_band", "model_disputes_source"],
    rounds=[rnd("2012-08-24", "Series Seed", 899999, None, None, SEC("snowflake-inc", i=1), "filing"),
            rnd("2013-03-08", "Series A", 4999111, "Sutter Hill Ventures", True, SEC("snowflake-inc", i=2), "filing"),
            rnd("2014-04-02", "Series B", 19949670, None, None, SEC("snowflake-inc", i=3), "filing"),
            rnd("2015-02-27", "Series C", 78834305, None, None, SEC("snowflake-inc", i=4), "filing"),
            rnd("2017-03-24", "Series D", 104999963, None, None, SEC("snowflake-inc", i=0), "filing")],
    note="Cloud data platform. HQ: the FY2026 10-K (filed 2026-03-20) gives principal executive offices at 135 "
         "Constitution Drive, Menlo Park (Snowflake moved back from Bozeman), fresher than the Bozeman on the "
         "Coatue, General Catalyst and Sequoia rows. Valuation: market cap $115.65B on 2026-09-28 "
         "(stockanalysis.com), 100b_plus, replacing the prefilled 2025 public float ($73.5B, 10b_plus), which "
         "disagreed with all three siblings. DISPUTE of the Pre-Seed band (D3): Crunchbase News (2020-10-14): "
         "'Sutter Hill led Snowflake's $5 million Series A in August 2012, and Managing Director Mike Speiser served "
         "as the company's founding CEO'; Business Insider (2020-09-21) likewise; the S-1 has Speiser's seat "
         "'elected by the holders of a majority of our Series A convertible preferred stock ... as the designee of "
         "Sutter Hill Ventures'. The Series A Form D gives first sale 2013-03-08 ($5.0M at about $0.35). Open point: "
         "the S-1 and a retroactive Form D also show a Series Seed ($0.9M at $0.1719, first sale 2012-08-24, while "
         "Speiser was CEO) whose buyer the record does not name; if SHV's fund bought it, the entry is that Seed and "
         "the named Series A of March 2013 graduates it."))

L.append(cls(
    "sumo-logic-software", rng="below_1b",
    stage="Growth", stage_src="web_verified",
    stage_cite=NEWS("sumo-logic-software", "How Low-Profile VC Firm Sutter Hill"), stage_conf="medium",
    entry_date="2012-01", city="Redwood City", city_src="formd_address", focus="Data Infrastructure",
    flags=["stage_disputes_band"],
    rounds=[rnd("2012-01", "Series B", 15000000, None, True,
                NEWS("sumo-logic-software", "How Low-Profile VC Firm Sutter Hill"), "press")],
    note="Cloud log management and analytics, Redwood City. IPO 2020, taken private by Francisco Partners in May 2023 "
         "for $1.7B (Wikipedia): acquired as prefilled, below_1b. Entry: Crunchbase News (2020-10-14): 'Sutter Hill "
         "began investing in Sumo Logic around the time of its $15 million Series B round in January 2012', which "
         "fits the firm's 2012 listing; Growth, as the band read, but dated 2012-01 instead of the band's 2015 Form "
         "D."))

L.append(cls(
    "swift-financial", status="acquired", rng="below_1b", stage="undetermined",
    city="Wilmington", city_src="formd_address", focus="Fintech & Payments", extra=dict(CLR),
    rounds=[rnd("2009-02-04", "Series A1 and Series A1-1 preferred", 6239907, None, None,
                SEC("swift-financial", i=0), "filing"),
            rnd("2011-07-08", "Series A2 preferred", 15000000, None, None, SEC("swift-financial", i=1), "filing")],
    note="Small-business lending (Swift Capital), Wilmington, Delaware (the Form Ds). PayPal bought it in August 2017 "
         f"(The News Journal, {NEWS('swift-financial', 'PayPal buys Wilmington startup Swift Financial')}), so "
         "acquired, below_1b. Entry: the first e-filed Form D (a 2010 amendment of a 2009 paper filing) covers "
         "'Series A1 and Series A1-1 Preferred Stock' sold from 2009-02-04 ($6.24M), with Tench Coxe of SHV a "
         "director; the company was incorporated in 2006 and the A1 name implies an earlier Series A, so the round "
         "SHV entered is not on record (the band was withheld). Later: Series A2 (2011, $12.8M of $15M sold), "
         "secured notes (2012), equity (2014)."))

L.append(cls(
    "thousand-eyes", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=W("ThousandEyes"), stage_conf="high", entry_date="2014-03",
    city="San Francisco", city_src="formd_address", focus="Data Infrastructure",
    rounds=[rnd("2011", "Series A", 5500000, "Sequoia Capital", False, W("ThousandEyes"), "press"),
            rnd("2014-03-07", "Series B", 20000000, "Sutter Hill Ventures", True, W("ThousandEyes"), "press"),
            rnd("2019-02", "Series D", 50000000, "GV", True, W("ThousandEyes"), "press")],
    note="Network intelligence and monitoring, San Francisco. Cisco completed its purchase on 2020-08-07 (Cisco "
         f"newsroom, {NEWS('thousand-eyes', 'Cisco Completes Acquisition of ThousandEyes')}), so acquired, "
         "below_1b; agrees with Sequoia's row. Entry: Wikipedia: 'In 2014, Sutter Hill Ventures led a Series B round, "
         "joined by Sequoia Capital and Salesforce.com, to invest $20M' after Sequoia's 2011 Series A; the $20M Form "
         "D gives first sale 2014-03-07 with Stefan Dyckerhoff of SHV a director. Series B reads Growth; not a Seed "
         "entry, so no graduation."))

L.append(cls(
    "threshold-pharmaceuticals", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_THRESHOLD, stage_conf="high", entry_date="2002-08",
    country="US", city="South San Francisco", focus="Healthcare & Bio", flags=["stage_disputes_band"],
    rounds=[rnd("2002-08-15", "Series A", 9000000, None, True, S1_THRESHOLD, "filing"),
            rnd("2003-11-17", "Series B", 41000000, None, True, S1_THRESHOLD, "filing")],
    note="Cancer drugs (evofosfamide), South San Francisco; merged with Molecular Templates in 2017 (the prefill's "
         "acquired), below_1b. DISPUTE of the Growth band: the band read a $35M 2009 private placement, made after "
         "the 2005 IPO. The 2004 S-1 lists entities affiliated with Sutter Hill Ventures among the Series A buyers "
         "(1,589,079 shares) and the Series B buyers (2,140,175 shares). The Series A ($9M at $1.00 after a "
         "reverse split) closed from October 2001 to 2002-08-15; SHV's stake exceeds everything sold before the "
         "August 2002 close (750,000 shares), so the entry is the Series A, dated to that close."))

L.append(cls(
    "toa-technologies", rng="below_1b", city="Beachwood", city_src="formd_address", focus="SaaS",
    note="Cloud field-service management software (ETAdirect), Beachwood, Ohio (the Form Ds). Oracle bought it in "
         "2014: acquired as prefilled, below_1b. The prefilled Series A entry (the $17.2M round of April 2011, Andy "
         "Sheehan of SHV a director) stands."))

L.append(cls(
    "tower-cloud", status="acquired", rng="below_1b", city="St. Petersburg", city_src="formd_address",
    focus="Data Infrastructure",
    note="Fiber backhaul for wireless carriers, St. Petersburg, Florida (the firm's own page and the Form Ds). CS&L, "
         "now Uniti, completed its purchase in 2016 (Telecom Ramblings, "
         f"{NEWS('tower-cloud', 'CS&L Completes Tower Cloud Buy')}), so acquired, below_1b. The prefilled Growth "
         "entry (the $74M round of September 2009, Tench Coxe of SHV a director) stands."))

L.append(cls(
    "vera-security-inc", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=W("Vera Security"), stage_conf="high", entry_date="2016-02",
    city="Palo Alto", city_src="formd_address", focus="Security", flags=["stage_disputes_band"],
    rounds=[rnd("2014-11", "Series A", 14000000, None, False, W("Vera Security"), "press"),
            rnd("2016-02", "Series B", 17000000, "Sutter Hill Ventures", True, W("Vera Security"), "press")],
    note="Data security and rights management, Palo Alto (the Form Ds). HelpSystems (now Fortra) bought it in 2020 "
         "(Wikipedia), so acquired, below_1b. DISPUTE of the Series A band: Wikipedia records the $14M Series A of "
         "November 2014 (its Form D lists only the CEO) and 'In February 2016, Vera announced a $17 million Series B "
         "round, led by Sutter Hill Ventures', and Stefan Dyckerhoff of SHV first appears on the $21.8M Form D filed "
         "in March 2016 (first sale given as 2015-03-10). SHV entered at the Series B: Growth."))

L.append(cls(
    "verinata-health", status="acquired", rng="below_1b", city="Redwood City", city_src="formd_address",
    focus="Healthcare & Bio",
    note="Non-invasive prenatal testing, Redwood City (the 2011 and 2012 Form Ds). Illumina bought it in January 2013 "
         f"(GEN, {NEWS('verinata-health', 'Illumina Acquires Verinata Health')}), so acquired, below_1b. The "
         "prefilled Series A entry (the $10M round of October 2009, Jeff Bird of SHV a director) stands."))

L.append(cls(
    "virage", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_VIRAGE, stage_conf="medium", entry_date="1995-04",
    country="US", country_src="web_verified", country_cite=S1_VIRAGE, city="San Mateo", city_src="web_verified",
    focus="SaaS", flags=["model_disputes_source"],
    rounds=[rnd("1995", "Series A", 3048788, None, True, S1_VIRAGE, "filing"),
            rnd("1997-01-06", "Series B", 3961200, None, True, S1_VIRAGE, "filing"),
            rnd("1998-03-30", "Series C", 6000000, None, True, S1_VIRAGE, "filing")],
    note="Video indexing and cataloging software (VideoLogger), San Mateo, California (177 Bovet Road; its 2000 S-1 "
         "and EDGAR record); Autonomy bought it in 2003 (its last EDGAR filings), so acquired, below_1b. DISPUTE of "
         "the prefilled country RU, a wrong Wikidata join on a one-word name: the company was US. Entry: the 2000 S-1 "
         "shows Series A preferred (about 4.1M shares at roughly $0.75, most outstanding by March 1996) as the first "
         "financing after the March 1995 Delaware reincorporation, and William Younger of SHV a director since April "
         "1995; the S-1's recent-sales table shows SHV buying Series B to E, yet SHV and its affiliates held 3.18M "
         "shares against 1.61M bought in B to E, so the rest predates 1997: the entry reads as the Series A "
         "(medium)."))

L.append(cls(
    "virobay-inc", status="unknown", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_VIROBAY, stage_conf="high", entry_date="2006-08",
    city="Menlo Park", city_src="formd_address", focus="Healthcare & Bio",
    rounds=[rnd("2006-08", "Series A", 30500001, None, True, S1_VIROBAY, "filing"),
            rnd("2010-05-18", "Series B", 10000001, None, True, S1_VIROBAY, "filing")],
    note="Cathepsin and protease inhibitors, Menlo Park (the Form Ds and the 2014 S-1). It withdrew its $50M IPO in "
         "October 2014 (Renaissance Capital, 'TPG-backed biotech Virobay withdraws $50 million IPO'); no later "
         "financing, filing, deal or shutdown notice was found (a vendor profile calls it inactive, which is not a "
         "citable fate), so unknown, below_1b. Entry: the S-1 says the company 'issued 30,500,001 shares of Series A "
         "Stock from 2006 through December 31, 2008' at $1.00, and Jeffrey Bird of SHV has been a director since "
         "August 2006, three months after the May 2006 incorporation, together with TPG's director: SHV entered at "
         "the Series A. SHV also bought $2M of the Series B."))

L.append(cls(
    "vitria-technology", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=S1_VITRIA, stage_conf="high", entry_date="1997-10",
    country="US", city="Sunnyvale", city_src="web_verified", focus="Data Infrastructure",
    rounds=[rnd("1997-10", "Series B", 9499970, None, True, S1_VITRIA, "filing"),
            rnd("1998-10", "Series C", 11431003, None, True, S1_VITRIA, "filing")],
    note="Business-process integration middleware (BusinessWare), Sunnyvale (EDGAR registrant address; Mountain View "
         "at its 1999 IPO). Its founders' company took it private in 2007 (Vitria deregistered on 2007-03-19), so "
         "acquired, below_1b. The firm's 1999 table: 'Public company'. Entry: the 1999 S-1's table of preferred "
         "purchases shows Sutter Hill Ventures (like Brentwood) buying no Series A or A1 and 2,481,327 shares of "
         "the Series B sold in October 1997 at $1.81, then Series C and D; William Younger of SHV a director since "
         "1997. Series B reads Growth."))

L.append(cls(
    "webvisible", status="defunct", rng="below_1b", stage="undetermined",
    country="US", city="Irvine", city_src="formd_address", focus="Media, Gaming & Advertising", extra=dict(CLR),
    rounds=[rnd("2010-02-05", "Form D, equity, round not named", 20000000, None, None, SEC("webvisible"), "filing")],
    note="Online advertising for small businesses, Irvine (the Form D). TechCrunch (2011-12-28, "
         f"{NEWS('webvisible', 'Bank Shuts Down Local Online Advertising Company WebVisible')}): Silicon Valley Bank "
         "foreclosed on its loan and took the assets, with no buyer for the business: defunct, below_1b; agrees with "
         "Redpoint's row. Funded by SHV, Redpoint and Adams Street (over $17M per TechCrunch). The only e-filed Form "
         "D (February 2010, $20M, James White of SHV a director from the firm's address) is not the first round of "
         "a company founded in 2001, and the round SHV entered is not on record."))

L.append(cls(
    "xios-therapeutics", status="defunct", rng="below_1b", city="Waltham", city_src="formd_address",
    focus="Healthcare & Bio",
    note="Small-molecule immuno-oncology drug discovery, Waltham, Massachusetts (100 Beaver Street; the Form Ds). Its "
         "last filing is a 2018 Form D ($1.0M of $1.5M sold), its domain no longer resolves, and data vendors list "
         "it as closed; no acquirer or later round was found, so defunct (a quiet wind-down, not a dated notice), "
         "below_1b. The prefilled Seed entry (the $6.0M first round of December 2015, Jeff Bird of SHV a director) "
         "stands; the 2018 $1M raise is not a later priced round at twice the entry. Graduation left for the "
         "graduation pass."))

L.append(cls(
    "xoft-inc", status="acquired", rng="below_1b", stage="undetermined",
    city="Sunnyvale", city_src="formd_address", focus="Healthcare & Bio",
    flags=["stage_disputes_band"], extra=dict(CLR),
    rounds=[rnd("2009-06-12", "convertible notes", 17501750, None, None, SEC("xoft-inc", i=0), "filing")],
    note="Electronic brachytherapy (miniature x-ray source), Sunnyvale (the Form Ds). iCAD bought it at the end of "
         "2010 and sold the Xoft business to Elekta in 2023 (DOTmed, "
         f"{NEWS('xoft-inc', 'Elekta acquires iCAD')}), so acquired, below_1b. DISPUTE of the Series A band: the "
         "June 2009 filing it read is a debt offering (notes with warrants) by a company its own Form D says was "
         "incorporated over five years before (the firm's page: established 1998), and SHV listed it from 2008. "
         "SHV's entry round is not on record."))

L.append(cls(
    "yext", stage="Series A", stage_src="web_verified", stage_cite=S1_YEXT, stage_conf="medium",
    entry_date="2008-05", city="New York", focus="SaaS", flags=["stage_disputes_band"],
    rounds=[rnd("2008-05", "Series A", 1820000, None, True, S1_YEXT, "filing"),
            rnd("2008-09", "Series B", 2070000, None, None, S1_YEXT, "filing"),
            rnd("2009-10", "Series C", 25145000, None, None, S1_YEXT, "filing"),
            rnd("2016", "Series F", 3000004, None, True, S1_YEXT, "filing")],
    note="Brand knowledge and listings software, New York. Public (NYSE YEXT), below_1b as prefilled (market cap "
         "$636M on 2026-09-28, agreeing with the Insight and IVP rows). DISPUTE of the Growth band (it read a 2014 "
         "$50M Form D): the 2017 S-1's preferred stock table gives the Series A an issue date of May 2008 ($0.317 a "
         "share, $1.82M), and Andrew Sheehan of SHV has been a director since May 2008; SHV was listed from 2010 and "
         "also bought Series F. The entry reads as the Series A, dated to Sheehan's arrival (medium). Not a Seed "
         "entry, so no graduation."))

L.append(cls(
    "youku-tudou", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=F1_YOUKU, stage_conf="high", entry_date="2007-01",
    city="Beijing", focus="Media, Gaming & Advertising",
    rounds=[rnd("2005-11-04", "Series A", 3000000, None, False, F1_YOUKU, "filing"),
            rnd("2007-01", "Series B1", 6030000, None, True, F1_YOUKU, "filing"),
            rnd("2007-07", "Series B2", 6020000, None, True, F1_YOUKU, "filing"),
            rnd("2007-11", "Series C", 25050000, None, True, F1_YOUKU, "filing")],
    note="Online video (Youku, merged with Tudou in 2012), Beijing. Alibaba bought it (agreed November 2015, closed "
         "2016), so acquired, below_1b. Entry: the 2010 F-1 says the Series A of November 2005 went to Chengwei and "
         "Farallon, and 'The investors in our Series B1 and B2 preferred share private placements included Chengwei "
         "Funds, Farallon Funds and certain Sutter Hill Funds'; the B1 was issued in January 2007, and SHV holds "
         "B1, B2, C, D and E but no A. Series B reads Growth. G. Leonard Baker of SHV a director since 2007."))

L.append(cls(
    "aac", status="public", rng="1b_plus", usd=5741391472, val_src="web_verified", val_cite=MC_AAC,
    asof="2026-09-28", extra=dict(WV), stage="undetermined",
    country="CN", country_src="web_verified", country_cite=PROF_AAC, city="Shenzhen", city_src="web_verified",
    focus="Industrial & Robotics",
    note="AAC Technologies, miniature acoustic, haptic and optical components for phones, listed in Hong Kong "
         "(2018.HK) since August 2005; 'founded in 1993 and is headquartered in Shenzhen' (stockanalysis profile; "
         "Cayman-registered). Market cap HKD 45.04B on 2026-09-28 (stockanalysis), HKD 45.04B @ ECB 2026-09-28 "
         "(HKD/EUR 8.9258, EUR/USD 1.1378) = $5.74B, 1b_plus. The firm listed 'AAC' on its networking pages in "
         "captures from 2010 to 2016; a vendor profile names SHV an institutional investor, but no source dates "
         "SHV's entry or names a round, so undetermined. Worth a check: if SHV bought after the 2005 listing, the "
         "position is a post-IPO purchase and the row leaves under T3."))

L.append(cls(
    "acceleron-pharma", rng="below_1b", stage="undetermined", city="Cambridge", focus="Healthcare & Bio",
    rounds=[rnd("2011-12-22", "Series F", None, None, None, S1_ACCEL, "filing")],
    note="TGF-beta superfamily biopharmaceuticals (luspatercept, sotatercept), Cambridge, Massachusetts. Merck bought "
         "it in November 2021: acquired as prefilled, below_1b. SHV signed Acceleron's amended investor rights and "
         "co-sale agreements of 2011-12-22 (the Series F financing) as an existing preferred holder (the 2013 DRS "
         "exhibits) and listed the company from 2008; the 2013 S-1 names SHV neither as a 5% holder nor as a buyer "
         "of any series, so the round SHV entered is not on record."))

L.append(cls(
    "actiance", status="acquired", rng="below_1b", stage="undetermined",
    city="Redwood City", focus="Security",
    note="Formerly FaceTime Communications (the firm's 1999 table: 'FaceTime Communications, Web customer interaction, "
         "Private company'): security and compliance for instant messaging, unified communications and social "
         "media, Redwood City (Wikipedia). K1 Investment Management bought it in November 2017 and combined it with "
         f"Smarsh (Law.com, {NEWS('actiance', 'K1 Investments to Merge Smarsh and Actiance')}), so acquired, "
         "below_1b. SHV held it by 1999 (Tench Coxe its director); the round SHV entered is not on record."))

L.append(cls(
    "activision", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Santa Monica", focus="Media, Gaming & Advertising",
    rounds=[rnd("1979", "founding capital (round not named)", 1000000, "Sutter Hill Ventures", True,
                W("Activision"), "press")],
    note="Video game publisher, founded 1 October 1979, Santa Monica. Wikipedia: Jim Levy 'helped the four to secure "
         "about $1 million in capital from Sutter Hill Ventures' at the founding; the firm's 1999 table: "
         "'Entertainment software, Public company'. Activision merged with Vivendi Games in 2008 to form Activision "
         "Blizzard, which Microsoft bought in October 2023, so acquired, below_1b. The record does not name the "
         "founding round, so the stage is undetermined (the entry itself dates to 1979)."))

L.append(cls(
    "adexa", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=S1_ADEXA, stage_conf="high", entry_date="1997-08",
    country="US", city="Los Angeles", city_src="web_verified", focus="SaaS",
    rounds=[rnd("1997-08-04", "Series A", 4870000, "Sutter Hill Ventures", True, S1_ADEXA, "filing"),
            rnd("1998-07", "Series B", 8225000, None, True, S1_ADEXA, "filing"),
            rnd("2000-08-24", "Series C", 20000000, None, True, S1_ADEXA, "filing")],
    note="Supply-chain planning software, Los Angeles (its 2000 S-1). The 2000 IPO was withdrawn and FreeMarkets' "
         "2001 agreement to buy it did not close; Adexa stayed independent until Eyelit Technologies bought it in "
         "January 2025 (Business Wire, 'Eyelit Technologies Acquires Adexa to Expand Smart Factory and Supply Chain "
         "Solutions'; adexa.com now redirects to eyelit.com), so acquired, below_1b. Entry: the S-1 says Adexa sold "
         "4,130,170 Series A shares at $1.18 from 1997-08-04 to February 1998, of which entities associated with "
         "Sutter Hill Ventures bought 3,160,750 (all but 55,000 shares were issued in 1997); William Younger of SHV "
         "a director from January 1998. SHV also bought Series B (1998) and C (2000)."))

L.append(cls(
    "aepona", status="acquired", rng="below_1b", stage="undetermined",
    country="GB", country_src="web_verified",
    country_cite=NEWS("aepona", "Speculation that Belfast tech firm Aepona"), city="Belfast", city_src="web_verified",
    focus="SaaS",
    note="Service-delivery and network API software for telecom operators, Belfast (Silicon Republic: 'Belfast tech "
         "firm Aepona'). Intel bought it in April 2013 (Amadeus Capital, its largest investor: 'Amadeus' Aepona "
         "Acquired by Intel'), so acquired, below_1b. Amadeus's release names Irish and French venture investors, "
         "BlackBerry Partners and SAP but not SHV; the firm listed Aepona in 2010 and 2012 and no source names the "
         "round SHV joined."))

L.append(cls(
    "aida", status="acquired", rng="below_1b", stage="undetermined",
    country="US", country_src="web_verified", country_cite=UPI_AIDA, city="Santa Clara", city_src="web_verified",
    focus="Industrial & Robotics", flags=["model_disputes_source"],
    note="AIDA Corp., computer-aided engineering tools for large system designers, 'based in Santa Clara, Calif.' "
         f"(UPI, 1987-11-03, {UPI_AIDA}): Teradyne agreed to buy it for about 1.8M Teradyne shares, and the firm's "
         "1999 table says 'Acquired by Teradyne', so acquired, below_1b. DISPUTE of the prefilled country AT, a wrong "
         "Wikidata join on a one-word name. Focus follows the EDA precedent in this book (Avant!, Mentor Graphics). "
         "SHV's round is not on record."))

L.append(cls(
    "akarx-inc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Bridgewater", city_src="web_verified", focus="Healthcare & Bio",
    note="Thrombocytopenia drugs (AKR-501, later avatrombopag, Doptelet). Eisai completed its purchase of AkaRx, "
         f"'Headquarters: Bridgewater, New Jersey', on 2010-01-06 for about $255 million ({EISAI_AKARX}), exercising "
         "the option it gained with MGI Pharma; acquired, below_1b. SHV listed it from 2008 to 2016; the round SHV "
         "entered is not on record."))

L.append(cls(
    "allbusiness", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", focus="Media, Gaming & Advertising",
    rounds=[rnd("2004-07", "Series B", 10000000, None, None, W("AllBusiness.com"), "press"),
            rnd("2006-02", "Series C", 12400000, None, None, W("AllBusiness.com"), "press")],
    note="Small-business information and media site, San Francisco, co-founded 1999 by Richard Harroch. NBCi bought "
         "the first company in March 2000; after that entity was broken up in 2002 Harroch bought back the core "
         "assets, raised a Series B (July 2004, $10M) and a Series C (February 2006, $12.4M), and Dun & Bradstreet "
         "bought AllBusiness for $55M in December 2007 (Wikipedia: AllBusiness.com), so acquired, below_1b. SHV "
         "listed it from 2010; which round it bought is not on record."))

if __name__ == "__main__":
    jl.write(f"batch-{N:03d}", L)
