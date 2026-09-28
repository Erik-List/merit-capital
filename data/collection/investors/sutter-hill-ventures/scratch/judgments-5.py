#!/usr/bin/env python3
"""PRO-77 Sutter Hill Ventures, queue batch 5 (45 rows): judgments.

Run: NQ_TAG=b5 python3 judgments-5.py
Every URL below was printed by a tool run in this session (WebSearch results,
EDGAR full-text search output, the sibling record) or comes from a helper."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS

N = 5
L = []

# ---- URLs printed by tools this session
U_NTAP_CAP = "https://stockanalysis.com/stocks/ntap/market-cap/"
U_PACB_CAP = "https://www.wallstreetzen.com/stocks/us/nasdaq/pacb"
U_MENLO_B = "https://www.securityweek.com/menlo-security-emerges-stealth-25-million-series-b-funding/"
U_MNP_A = "https://venturebeat.com/business/mynewplace-gets-funding-for-apartment-leasing"
U_MNP_B = "https://splitrock.com/?p=404"
U_MNP_8K = "https://www.sec.gov/Archives/edgar/data/1286225/000095012311079304/d84324exv99w1.htm"
U_MNP_8KA = "https://www.sec.gov/Archives/edgar/data/1286225/000095012311094963/c23636exv99w1.htm"
U_ADEXA_S4 = "https://www.sec.gov/Archives/edgar/data/949968/000095012801000458/j8660901s-4.txt"
U_PMC_10K = "https://www.sec.gov/Archives/edgar/data/767920/000076792015000004/pmcs-20141227x10k.htm"
U_RUCKUS_S1A = "https://www.sec.gov/Archives/edgar/data/1294016/000119312512428704/d358896ds1a.htm"
U_NIM_8KA = "https://www.sec.gov/Archives/edgar/data/1111665/000095012310014708/w77465exv99w1.htm"
U_STREET_A_VENDOR = "https://www.crunchbase.com/funding_round/streetline-series-a--9d9a783a"
U_STREET_C = "https://techcrunch.com/2013/01/10/streetline-series-c/"
U_STREET_14 = ("https://www.prnewswire.com/news-releases/streetline-closes-10m-financing-to-accelerate-"
               "deployment-of-smart-parking-platform-265351461.html")
U_BUZZ_07 = "https://techcrunch.com/2007/05/24/buzznet-lands-6million"
U_BUZZ_09 = ("https://www.mediapost.com/publications/article/102550/"
             "buzznet-morphs-into-buzz-media-lands-125-millio.html")

UND = "SHV's entry round is not named in any record found, so the stage is undetermined."

# ---- membership: the one fund-shaped listing (decisions D6)
L.append(verdict(
    "makena-capital-management-llc", "not_member",
    "The firm filed Makena Capital Management under its own 'Investment Partnerships' category on every "
    "listing (2008 to 2016), and its page describes Makena as an investment management firm run by the "
    "team that ran the Stanford endowment: the position is a partnership interest in a fund manager, not "
    "equity in a venture-outcome operating company (decisions D6, T5, the LP-stake class)",
    ec="site_listing", conf="high", cite=ARCH("makena-capital-management-llc")))

# ---- rows with a researched entry round
L.append(cls(
    "menlo-security", status="private", rng="below_1b", usd=800_000_000, val_src="web_verified",
    val_cite=NEWS("menlo-security", "reaches $800m valuation"), asof="2020-11-13",
    extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=U_MENLO_B, stage_conf="high", entry_date="2015-06",
    country="US", city="Mountain View", focus="Security", flags=("stale",),
    rounds=[rnd("2014-11", "Series A", 10_500_000, None, False, U_MENLO_B, "press"),
            rnd("2015-06-08", "Series B", 25_000_000, "Sutter Hill Ventures", True, U_MENLO_B, "press"),
            rnd("2017-12", "Series C", 40_000_000, None, None,
                NEWS("menlo-security", "raises $40 million in Series C"), "press"),
            rnd("2019-07", "Series D", 75_000_000, None, None,
                NEWS("menlo-security", "Raises $75 Million"), "press"),
            rnd("2020-11", "Series E", 100_000_000, "Vista Equity Partners", None,
                NEWS("menlo-security", "reaches $800m valuation"), "press")],
    note="SHV entered at the $25M Series B of June 2015, which it led as a new investor (SecurityWeek, "
         "2015-06-08; Stefan Dyckerhoff joined the board); the $10.5M Series A of November 2014 came before "
         "it, so the entry reads Growth. Last priced mark: the $100M Series E led by Vista Equity Partners in "
         "November 2020 at an $800M enterprise valuation (FinTech Global), older than 24 months, so stale; no "
         "later priced round found. Still independent: it bought Votiro in February 2025 and named Bill Robbins "
         "CEO in February 2026. City aligned with General Catalyst's row (Mountain View); the firm's 2017 page "
         "said Menlo Park."))

L.append(cls(
    "ruckus-wireless", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_cite=W("Ruckus Networks"), stage_conf="high", entry_date="2005-09",
    country="US", city="Sunnyvale", focus="Data Infrastructure",
    rounds=[rnd(None, "Series A-1", 1_500_000, None, None, W("Ruckus Networks"), "press"),
            rnd(None, "Series B", 3_500_000, "WK Technology Fund", None, U_RUCKUS_S1A, "filing"),
            rnd("2005-09-19", "Series C", 9_000_000, "Sutter Hill Ventures; Investor Growth Capital", True,
                U_RUCKUS_S1A, "filing")],
    note="SHV and Investor Growth Capital led Ruckus's $9M second round, announced September 19, 2005, "
         "which existing investors Sequoia and WK Technology Fund completed (Wikipedia). The October 2012 "
         "S-1/A names that round Series C (7,835,000 shares at $1.15, $8.96M), after the Series A-1 seed "
         "($1.5M from Sequoia and private investors) and the $3.5M Series B led by WK Technology Fund, so the "
         "entry reads Growth. Brocade bought Ruckus in May 2016 for about $1.5B; last HQ Sunnyvale; aligned "
         "with Sequoia's row (acquired, below_1b)."))

L.append(cls(
    "mynewplace", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=U_MNP_B, stage_conf="high", entry_date="2006-09",
    city="San Francisco", focus="Consumer & Marketplaces",
    rounds=[rnd("2006-03", "Series A", 8_000_000, "Trinity Ventures", False, U_MNP_A, "press"),
            rnd("2006-09-18", "Series B", 12_000_000, "Sutter Hill Ventures; Split Rock Partners", True,
                U_MNP_B, "press"),
            rnd("2008-09", "Series B-1", 3_574_000, None, None, U_MNP_8KA, "filing"),
            rnd("2010-12-21", "Series B-2", 5_000_000, None, None, U_MNP_8KA, "filing")],
    note="SHV entered at the $12M Series B of September 18, 2006, which it co-led with Split Rock Partners "
         "(the release on Split Rock's site). The first round, $8M in March 2006, was led by Trinity Ventures "
         "with REIT backers and does not name SHV (VentureBeat); Wikipedia's 'initially backed by' line merges "
         "the two rounds. RealPage bought the company (Multifamily Technology Solutions, d/b/a MyNewPlace, San "
         "Francisco) for about $74.4M in August 2011 (RealPage 8-K). Preferred ladder in RealPage's 8-K/A: "
         "Series A $8M, Series B $12M, B-1 $3.57M (2008 to 2009), B-2 $5M (December 2010)."))

L.append(cls(
    "paragon-management-systems", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=U_ADEXA_S4, stage_conf="high", entry_date="1997",
    country="US", city="Los Angeles", focus="SaaS",
    rounds=[rnd("1997", "Series A", 4_218_938, None, True, U_ADEXA_S4, "filing"),
            rnd("1998", "Series B", 8_225_000, None, True, U_ADEXA_S4, "filing"),
            rnd("2000-08-24", "Series C", 20_000_000, None, True, U_ADEXA_S4, "filing")],
    note="Paragon Management Systems, Inc. is Adexa: formed in California in 1994 as successor to NP "
         "Complete and later renamed Adexa (supply chain planning software; FreeMarkets' 2001 S-4). The S-4 "
         "shows SHV funds holding 1,978,906 Series A shares (about half of the Series A, financed in 1997) plus "
         "Series B (1998, $3.30 a share) and Series C (August 2000, about $20M) shares, 18.0% of the company, "
         "with William Younger (SHV) a director, so the entry is the 1997 Series A. Adexa stayed independent "
         "after FreeMarkets' 2001 merger agreement and was acquired by Eyelit Technologies in January 2025 "
         "(Business Wire: " + NEWS("paragon-management-systems", "Eyelit Technologies Acquires Adexa") + "). "
         "HQ in the S-4: 5933 W. Century Blvd, Los Angeles. The published name could read Adexa."))

L.append(cls(
    "networks-in-motion", status="acquired", rng="below_1b",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2004",
    country="US", city="Aliso Viejo", focus="SaaS",
    rounds=[rnd("2001-06", "Series A", 250_000, None, None, U_NIM_8KA, "filing"),
            rnd("2003-09", "Series A-1", 1_032_000, None, None, U_NIM_8KA, "filing"),
            rnd("2004-09", "Series B", 3_517_000, None, None, U_NIM_8KA, "filing"),
            rnd("2004-12", "Series B", 2_750_000, None, None, U_NIM_8KA, "filing"),
            rnd("2006-03", "Series C", 10_000_000, "Mission Ventures", None,
                NEWS("networks-in-motion", "Bragging Rights with Buyout"), "press")],
    note="TeleCommunication Systems bought the company (Aliso Viejo, CA) for $170M in cash, stock and notes, "
         "agreed 2009-12-01 (TCS 8-K); SHV received 232,731 TCS shares for its stake and James White (SHV) sat "
         "on the board until the sale (TCS S-3, February 2010). The first venture money was the $6.5M Series B "
         "of late 2004 (closings in September and December 2004), and the $10M Series C of 2006 was led by "
         "Mission Ventures (Orange County Business Journal; ladder in TCS's 8-K/A: Series A $250K in 2001, A-1 "
         "$1.03M in 2003). SHV is named only among the venture investors, so it entered at the 2004 Series B or "
         "the 2006 Series C, Growth either way; the entry date is the earlier of the two. Aligned with "
         "Redpoint's row (acquired, below_1b, Aliso Viejo)."))

# ---- public rows
L.append(cls(
    "netapp", rng="10b_plus", usd=40_150_000_000, val_src="web_verified", val_cite=U_NTAP_CAP,
    asof="2026-09-28", extra={"valuation_range_source": "web_verified"},
    stage="undetermined", city="San Jose", focus="Data Infrastructure", flags=("model_disputes_source",),
    rounds=[rnd("1994", "venture round", None, None, None, W("NetApp"), "press")],
    note="Market cap $40.15B on 2026-09-28 (stockanalysis) replaces the prefilled October 2025 SEC float "
         "($17.1B) as the public mark; same band as Sequoia's row (10b_plus, $39.0B on 2026-08-11). HQ San "
         "Jose. The firm's 1999 table lists Network Appliance as a public company. The 1995 IPO prospectus "
         "predates EDGAR, the 1997 13G filers are Vanguard IV, Advent VII, Sequoia and Pilgrim Baxter, and "
         "Wikipedia names only Sequoia's 1994 funding. " + UND))

L.append(cls(
    "pacific-biosciences", status="public", rng="below_1b", usd=503_550_000, val_src="web_verified",
    val_cite=U_PACB_CAP, asof="2026-09-25", extra={"valuation_range_source": "web_verified"},
    stage="undetermined", city="Menlo Park", focus="Healthcare & Bio", rounds=[],
    note="Public (Nasdaq: PACB, IPO October 2010); market cap $503.55M on 2026-09-25 at $1.62 a share "
         "(WallStreetZen). HQ Menlo Park. The firm listed PacBio from 2012 to 2017 (MD Jeff Bird) with its "
         "startup-era description, but no SEC filing names Sutter Hill with the company (EDGAR full-text "
         "search: zero hits) and Wikipedia's investor list (six rounds, nearly $400M) omits SHV, so SHV's round "
         "cannot be tied and the stage is undetermined. Membership rests on the listing alone; worth a look "
         "whether SHV's position began before the IPO (D4)."))

# ---- prefill disputes (country or status)
L.append(cls(
    "nimsoft", status="acquired", rng="below_1b", stage="undetermined",
    country="US", country_src="web_verified", country_cite=W("Nimsoft"), city="Redwood City",
    focus="Data Infrastructure", flags=("model_disputes_source",),
    rounds=[rnd("2007", "Series A", 10_300_000, "JMI Equity; Northzone Ventures", None, W("Nimsoft"), "press"),
            rnd("2008-10", "venture round", 12_000_000, "Goldman Sachs", None, W("Nimsoft"), "press")],
    note="CA bought Nimsoft for $350M in March 2010 (Wikipedia; CA's 10-K for fiscal 2010 names the legal "
         "parent Nimsoft AS). The prefilled GB is a wrong join: Nimbus Software was founded in Oslo in 1998 "
         "and merged in 2004 with its US distributor, and the combined company's headquarters were established "
         "in Silicon Valley (Wikipedia); 2010 deal coverage places it in Redwood City. Total funding $22.3M "
         "(TechCrunch, 2010): the 2007 $10.3M Series A from JMI Equity and Northzone and the October 2008 $12M "
         "round led by Goldman Sachs. Neither names SHV, so its round is not on record and the stage is "
         "undetermined."))

L.append(cls(
    "pmc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", country_src="web_verified", country_cite=U_PMC_10K, city="Sunnyvale",
    focus="Industrial & Robotics", flags=("model_disputes_source",),
    note="PMC-Sierra (fabless communications and storage chips) was acquired by Microsemi on January 15, "
         "2016 (Wikipedia, PMC-Sierra). The prefilled GB is a wrong join: its last 10-K (February 2015) gives "
         "its principal offices in Sunnyvale, CA, with engineering in Burnaby, Canada. The firm's listing (2010 "
         "to 2016) is the only tie: no SEC filing names Sutter Hill with PMC-Sierra and no listed SHV company "
         "names PMC-Sierra as its acquirer, so no sale-consideration reading was found. " + UND))

L.append(cls(
    "measurex", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cupertino", focus="Industrial & Robotics", flags=("model_disputes_source",),
    note="Acquired by Honeywell in March 1997 for almost $600M (Wikipedia, Measurex); the firm's own 1999 "
         "table says 'Acquired by Honeywell'. The prefilled 'defunct' (a Wikidata dissolution) is disputed: "
         "the business was bought, so it reads acquired. Based in Cupertino (Wikipedia). " + UND))

L.append(cls(
    "prime-computer", status="acquired", rng="below_1b", stage="undetermined",
    city="Natick", focus="Industrial & Robotics", flags=("model_disputes_source",),
    note="The prefilled 'defunct' is disputed: Prime shut its computer business, but its Computervision "
         "subsidiary (bought in 1988) carried on and was acquired by Parametric Technology in 1998 (Wikipedia, "
         "Prime Computer); the firm's 1999 table says 'Merged with Parametric'. So it reads acquired, aligned "
         "with Greylock's row (acquired, below_1b, Natick). " + UND))

# ---- acquired rows, the firm's own outcome lines plus a record
L.append(cls(
    "macusight", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Union City", city_src="web_verified", focus="Healthcare & Bio", rounds=[],
    note="Acquired by Santen Inc. in 2010: Opthea's March 2022 6-K says its new executive was MacuSight's "
         "chief medical officer until the company was acquired by Santen Inc. in 2010. Santen had licensed "
         "MacuSight's sirolimus for Japan and Asia in 2008 ($50M upfront), a license rather than the sale. The "
         "firm's own page (2008, 2012) places the company in Union City, CA. " + UND))

L.append(cls(
    "mentor-graphics", rng="below_1b", stage="undetermined", city="Wilsonville",
    focus="Industrial & Robotics", rounds=[],
    note="Acquired by Siemens in 2017 ($4.5B, announced November 2016; Wikipedia) and kept its headquarters "
         "in Wilsonville, Oregon as a Siemens subsidiary; aligned with Greylock's and Battery's rows (acquired, "
         "below_1b). Founded 1981 by three Tektronix engineers and public from 1984. " + UND))

L.append(cls(
    "merced-systems", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Redwood City", focus="SaaS", rounds=[],
    note="NICE Systems agreed in December 2011 to buy Merced Systems for about $150M plus up to $20M on "
         "performance targets, closing early in 2012 (NICE's 6-K exhibit 99.1); the firm's 2013 page says it "
         "was acquired by NICE Systems. NICE describes it as headquartered in Silicon Valley and London; its "
         "Silicon Valley base was Redwood City. The only financing found is Venture Lending & Leasing III debt "
         "(2002 to 2005). " + UND))

L.append(cls(
    "metaphor-computer", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Mountain View", focus="Data Infrastructure",
    note="Founded 1982 by David Liddle and Donald Massaro after Xerox PARC; IBM, one of its main customers, "
         "acquired it outright in 1991 (Wikipedia, Metaphor Computer Systems); the firm's 1999 table says "
         "'Acquired by IBM'. Decision-support workstations and software for querying corporate databases. "
         + UND))

L.append(cls(
    "metronome-therapeutics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Healthcare & Bio", flags=("city_unknown",),
    note="The firm's own 2013 page says Metronome Therapeutics was acquired by Spectrum Pharmaceuticals. Its "
         "founder and CEO George Tidmarsh ran it from March 2006 to July 2010 and joined Spectrum as chief "
         "scientific officer in July 2010 (Spectrum's 10-K for 2010; La Jolla Pharmaceutical's January 2012 "
         "8-K), consistent with a 2010 sale that Spectrum did not report separately. No filing or press item "
         "found gives its city. " + UND))

L.append(cls(
    "mips-computer", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Sunnyvale", focus="Industrial & Robotics",
    note="MIPS Computer Systems (founded 1984 to commercialise Stanford's RISC work) was acquired by Silicon "
         "Graphics in 1992 for $333M and renamed MIPS Technologies (Wikipedia); the firm's 1999 table says "
         "'Acquired by Silicon Graphic'. Last known HQ Sunnyvale. " + UND))

L.append(cls(
    "mobile-com", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="AtMobile.com, Inc. merged into Software.com on April 11, 2000 (pooling of interests, 6,039,375 "
         "Software.com shares; Openwave's 10-K for fiscal 2001); the firm's 2004 page says '@mobile.com "
         "acquired by Software.com is now Openwave'. Wireless services software for carriers. AtMobile had "
         "preferred up to a Series D, but no record names the round SHV bought, so the stage is undetermined. "
         "No filing found gives its city."))

L.append(cls(
    "nelson-analytical", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cupertino", focus="SaaS",
    note="Laboratory (chromatography data) software; the firm's 1999 table says 'Acquired by Perkin Elmer', "
         "and Perkin-Elmer's successor Applera still listed a Nelson Analytical GmbH subsidiary in 2001 "
         "(Applera's 10-K, exhibit 21). Last known HQ Cupertino (Perkin-Elmer's Nelson division). " + UND))

L.append(cls(
    "neurex", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Menlo Park", focus="Healthcare & Bio",
    note="Pain and hypertension drugs; acquired by Elan in 1998 (the firm's 1999 table: 'Acquired by Elan'; "
         "its 2008 page: 'Neurex is now a part of Elan'). Aligned with Greylock's row (acquired, below_1b, "
         "Menlo Park). " + UND))

L.append(cls(
    "norian", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cupertino", focus="Healthcare & Bio",
    note="Bone substitute materials (Norian SRS); the firm's 1999 table says 'Acquired by Synthes'. Last "
         "known HQ Cupertino. The Wikipedia article titled Norian is the geological stage, not this company. "
         + UND))

L.append(cls(
    "onstream-inc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="The firm's investment is OnStream Networks (formerly T3Plus Networking), listed in its 1999 table "
         "as high speed networking, 'Acquired by 3Com'; 3Com's agreement and plan of reorganization with "
         "OnStream Networks is dated October 5, 1996 (3Com 10-K, 2001). The 2010 to 2016 pages sit in the "
         "firm's networking section but carry the text of a different company, OnStream, Inc. (a 1998 Philips "
         "spin-off making removable storage in Colorado), so the published name and text should read OnStream "
         "Networks. No filing found gives its city. " + UND))

L.append(cls(
    "ontogeny", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Cambridge", focus="Healthcare & Bio",
    note="Induction factor (developmental biology) drugs; merged in 2000 with Creative BioMolecules and "
         "Reprogenesis to form Curis; the firm's 1999 table still read 'Private company'. Aligned with "
         "Greylock's row (acquired, below_1b, Cambridge). " + UND))

L.append(cls(
    "pacific-microsonics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Berkeley", focus="Industrial & Robotics",
    note="Developer of HDCD audio encoding and its decoder chips; in 2000 the company folded and Microsoft "
         "acquired it with all its intellectual property (Wikipedia, High Definition Compatible Digital); the "
         "firm's 1999 table read 'Private company'. Last known HQ Berkeley. " + UND))

L.append(cls(
    "palm-inc", rng="below_1b", stage="undetermined", city="Sunnyvale", focus="Consumer & Marketplaces",
    note="Hewlett-Packard bought Palm, Inc. in July 2010 (Wikipedia); the prefilled acquirer TCL only bought "
         "the Palm trademark from HP in 2014, so HP is this row's acquirer. Headquartered in Sunnyvale. Palm "
         "Computing was founded in 1992, bought by U.S. Robotics in 1995 and spun out of 3Com in 2000. " + UND))

L.append(cls(
    "phycor-management-inc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Nashville", focus="Healthcare & Bio",
    note="Management of independent physician associations; the firm's 1999 table says 'Acquired by Phycor "
         "Inc.'. City aligned with Greylock's row (acquired, below_1b, Nashville, PhyCor's home); the "
         "company's own city before the sale is not on record. " + UND))

L.append(cls(
    "primary-access", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", focus="Data Infrastructure",
    note="Network access (remote access) systems; acquired by 3Com in 1995 (the firm's 1999 table and its "
         "2010 to 2013 pages: acquired by 3Com). Last known HQ San Diego. " + UND))

L.append(cls(
    "pyxis", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", focus="Healthcare & Bio",
    note="Hospital medication dispensing systems; bought by Cardinal Health in 1996 for $867M in stock "
         "(Wikipedia, Pyxis Corporation); the firm's 1999 table says 'Acquired by Cardinal'. Aligned with "
         "Menlo Ventures' row (acquired, below_1b, San Diego). " + UND))

L.append(cls(
    "risk-management-solutions", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Newark", focus="Fintech & Payments",
    note="Catastrophe risk models for insurers (RMS, founded at Stanford). The firm's 1999 table says "
         "'Acquired by Center Reinsurance'; the business later passed to Daily Mail and General Trust, which "
         "sold it to Moody's in 2021. Acquired either way; last HQ Newark, California. " + UND))

L.append(cls(
    "roxro-pharma-inc", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Menlo Park", focus="Healthcare & Bio",
    note="Developer of SPRIX (ketorolac nasal spray, FDA approval May 2010). In December 2010 Luitpold "
         "Pharmaceuticals (a Daiichi Sankyo company) entered a merger agreement with ROXRO Pharma under which "
         "it obtained SPRIX (Egalet's March 2015 8-K/A, exhibit 99.2); FibroGen's 2015 proxy dates ROXRO's "
         "sale to Luitpold to 2011. " + UND))

L.append(cls(
    "sequoia-turner", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Mountain View", focus="Healthcare & Bio",
    note="Hematology instruments. The firm's 1999 table says 'Acquired by Unilever'; Abbott's own history "
         "dates its entry into hematology testing to its 1991 acquisition of Sequoia-Turner Corp (Abbott, "
         "January 2004 filing). Acquired either way; last known HQ Mountain View. " + UND))

L.append(cls(
    "somatix", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Alameda", focus="Healthcare & Bio",
    note="Somatix Therapy Corporation (gene therapy) was acquired by Cell Genesys in 1997, which took over its "
         "GVAX cancer vaccine program (Cell Genesys 10-K for 2000); the firm's 1999 table still read 'Public "
         "company'. Last known HQ Alameda. " + UND))

L.append(cls(
    "spinmedia", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Los Angeles", focus="Media, Gaming & Advertising",
    rounds=[rnd("2007-05", "venture round", 6_000_000, "Redpoint Ventures; Anthem Venture Partners", None,
                U_BUZZ_07, "press"),
            rnd("2008", "venture round", 25_000_000, None, None, U_BUZZ_09, "press"),
            rnd("2009-03-20", "venture round", 12_500_000, None, True, U_BUZZ_09, "press")],
    note="Buzznet, then BuzzMedia and from 2013 SpinMedia (Los Angeles). After a 2014 assignment for the "
         "benefit of creditors M/C Partners became the main owner, and in 2016 the sites were sold off "
         "(Buzznet, Idolator and PureVolume to Hive Media; Spin, Vibe and Stereogum to Eldridge Industries "
         "through the Billboard-Hollywood Reporter group; others to CPX Interactive), so it reads acquired, an "
         "asset sale out of a wind-down (Wikipedia, the SpinMedia section of the MRC article). SHV is not named "
         "in the May 2007 $6M round led by Redpoint and Anthem (TechCrunch) and is an existing investor in the "
         "March 2009 $12.5M round (MediaPost), so it came in between, most likely in the roughly $25M 2008 "
         "round, whose series name is not on record: the stage is undetermined."))

L.append(cls(
    "streetline", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Foster City", focus="Industrial & Robotics",
    rounds=[rnd("2010-07", "Series A", None, None, None, U_STREET_A_VENDOR, "vendor"),
            rnd("2011-06", "Series B", 15_000_000, "Fontinalis Partners; RockPort Capital", None, None, "vendor"),
            rnd("2013-01-10", "Series C", 25_000_000, "True Ventures", True, U_STREET_C, "press"),
            rnd("2014-07-01", "venture round", 10_000_000, None, None, U_STREET_14, "press")],
    note="Parking sensors and data for cities, Foster City (July 2014 release, with Jim White of SHV on the "
         "board). SHV was a past backer in the $25M Series C of January 2013 led by True Ventures (TechCrunch), "
         "so it entered at the Series A or B; only a vendor places it in a July 2010 Series A, which cannot "
         "cite (Rule A), so the stage is undetermined. Kapsch TrafficCom took controlling ownership in 2015 "
         "(ITS International), so it reads acquired; Streetline kept its own CEO until February 2018 (Augmedix "
         "10-K)."))

L.append(cls(
    "symmetricom", rng="below_1b", stage="undetermined",
    country="US", city="San Jose", focus="Data Infrastructure",
    note="Network synchronization and timing equipment for telecom networks, headquartered in San Jose; "
         "acquired by Microsemi in 2013 for $230M (Wikipedia, Symmetricom). The firm's 1999 table lists it as a "
         "public company. " + UND))

L.append(cls(
    "synernetics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="Data Infrastructure", flags=("city_unknown",),
    note="FDDI and Ethernet switching; the firm's 1999 table says 'Acquired by 3Com' (the deal was in 1993). "
         "A Massachusetts company as far as known, but no filing found confirms the municipality. " + UND))

# ---- fate not on record (status unknown)
L.append(cls(
    "naryx-pharma", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="Healthcare & Bio", flags=("city_unknown",),
    note="Private pharmaceutical company developing inhaled, nebulized and intranasal formulations; Michael "
         "Narachi (ex-Amgen) was its executive chairman from August 2004 to April 2008 (Orexigen's 2009 and "
         "Allos's 2011 filings). The firm listed it in 2008 and 2012, not from 2013. No source found gives its "
         "later fate or its city, so status is unknown. " + UND))

L.append(cls(
    "object-reservoir", status="unknown", rng="below_1b", stage="undetermined",
    country="US", city="Austin", focus="Climate & Energy",
    note="Reservoir characterization software and services for oil and gas producers, listed by the firm "
         "2004 to 2012. Still in use in 2011 (Clayton Williams Energy's reserve engineer lists Object Reservoir "
         "training for 2011), but no source found gives its later fate, so status is unknown. " + UND))

L.append(cls(
    "optical-sensors", status="private", rng="below_1b", stage="undetermined",
    country="US", city="Eden Prairie", city_src="web_verified", focus="Healthcare & Bio",
    note="Optical Sensors Inc (blood gas measurement; Nasdaq IPO 1996) traded as VASAMED from 2004 at 7615 "
         "Golden Triangle Drive, Eden Prairie, MN (its August 2004 8-K), deregistered from the SEC in November "
         "2006 (Form 15) and raised privately in 2007. VASAMED was still operating in 2015 (a collaboration with "
         "CorVascular, PR Newswire: " + NEWS("optical-sensors", "CorVascular and Vasamed") + ") and no sale "
         "or shutdown was found, so the last known state is private, below_1b. " + UND))

L.append(cls(
    "ourpictures", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="Consumer & Marketplaces", flags=("city_unknown",),
    note="Listed by the firm only in 2004 (software). OurPictures, Inc. was a private company in 2005 "
         "(RedEnvelope's proxy lists Karen Edwards on its board); no source found gives its fate or city, so "
         "status is unknown. " + UND))

L.append(cls(
    "pivia", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="SaaS", flags=("city_unknown",),
    note="Listed by the firm only in 2004 (software). Pivia was a Plumtree portal technology partner in 2003 "
         "and 2004 and a Venture Lending & Leasing III borrower (loans running to September 2005); no source "
         "found gives its fate or city, so status is unknown. " + UND))

L.append(cls(
    "radiance-technologies", status="unknown", rng="below_1b", stage="undetermined",
    country="US", city="Los Altos", city_src="web_verified", focus="Data Infrastructure",
    note="Internet content delivery technology; the firm's page (2004, 2008) says it is based in Los Altos, "
         "California (not the Huntsville defense contractor of the same name). No source found gives its fate, "
         "so status is unknown. " + UND))

L.append(cls(
    "synapix", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="Media, Gaming & Advertising", flags=("city_unknown",),
    note="SynaPix, Inc. developed software for film and video special effects (Phase Forward's 2004 S-1, its "
         "CFO from May 1999 to December 2000) and was still named as a US competitor in Dynamic Digital "
         "Depth's 2001 F-1; the firm's 1999 table read 'Private company'. No source found gives its fate or "
         "city, so status is unknown. " + UND))

L.append(cls(
    "targeted-marketing-systems", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="SaaS", flags=("city_unknown",),
    note="Targeted Marketing Systems, Inc. was a privately held firm specializing in customer loyalty "
         "programs in 2001 (Sixx Holdings' 10-KSB; Polaris's proxy also lists it among a director's boards); "
         "the firm's 1999 table read 'Private company'. No source found gives its fate or city, so status is "
         "unknown. " + UND))

if __name__ == "__main__":
    jl.write(f"batch-{N:03d}", L)
