"""PRO-80 Bessemer, judge jm, file g: members, second half, and the five Bessemer-vehicle filing rows (batches 21 to 25).

Eight rows are listed companies reached a second time through their legal name (flagged `identity_conflated`, the
listed base row named). Three are not on the firm's list: FlexFactor and CozyKin are corroborated by a press source
naming Bessemer in the round; Strala rests on the director-of-record pattern alone and is flagged for review.
"""
import judge_lib as jl

M = "member"
lines = []
FD = {
    "relish": "https://www.sec.gov/Archives/edgar/data/1756582/000175658220000001/0001756582-20-000001-index.htm",
    "tiz": "https://www.sec.gov/Archives/edgar/data/1688204/000168820423000004/0001688204-23-000004-index.htm",
    "t3c": "https://www.sec.gov/Archives/edgar/data/1345021/000134502109000003/0001345021-09-000003-index.htm",
    "t3c10": "https://www.sec.gov/Archives/edgar/data/1345021/000134502110000001/0001345021-10-000001-index.htm",
    "mural": "https://www.sec.gov/Archives/edgar/data/1936452/000193645222000001/0001936452-22-000001-index.htm",
    "birch": "https://www.sec.gov/Archives/edgar/data/2041284/000204128424000001/0002041284-24-000001-index.htm",
    "flex": "https://www.sec.gov/Archives/edgar/data/2029727/000117891324002181/0001178913-24-002181-index.htm",
    "strala": "https://www.sec.gov/Archives/edgar/data/2065647/000206564726000001/0002065647-26-000001-index.htm",
    "dyn19": "https://www.sec.gov/Archives/edgar/data/1727596/000172759619000001/0001727596-19-000001-index.htm",
}
PROVI_PR = jl.NEWS("tiz-inc", "$750M Valuation")
CENTS_B = jl.NEWS("make-cents-technologies-inc", "Announces $40M Series B")
CENTS_C = jl.NEWS("make-cents-technologies-inc", "raises $140m in Series C")
R365_A = jl.NEWS("dyn365-inc", "Turning Up The Heat")
R365_C = jl.NEWS("dyn365-inc", "Receives $88M")
R365_D = jl.NEWS("dyn365-inc", "Announces $135M")
ZEN_SEED = jl.NEWS("evolve-bits-inc", "Bessemer leads $3.5 Mn seed")
ZEN_A = jl.NEWS("evolve-bits-inc", "raises $15m Series A")
FERN_POST = jl.POST("meet-the-founders-of-fern")
FERN_ACQ = jl.NEWS("birch-solutions-inc", "Postman snaps up Fern")
FLEX_PR = "https://www.prnewswire.com/news-releases/flexfactor-raises-16-8m-series-a-from-bessemer-venture-partners-to-tackle-the-500-billion-ecommerce-problem-checkout-failures-due-to-payment-declines-302273131.html"
COZY = "https://www.edsurge.com/news/2019-05-20-nanny-service-startup-cozykin-raises-6m-to-expand-into-new-markets"
STRALA = jl.NEWS("strala-group-inc", "Strala raises $51")
TELOCITY_424 = "https://www.sec.gov/Archives/edgar/data/1102448/0000891618-00-001807.txt"
FCO_424 = "https://www.sec.gov/Archives/edgar/data/1024441/0000912057-96-029342.txt"
PROMEDCO_424 = "https://www.sec.gov/Archives/edgar/data/1011630/0000950133-97-000772.txt"

# ---- HelloRelish, Inc. = Relish
lines.append(jl.verdict("hellorelish-inc", M, "HelloRelish, Inc. is the legal name of Relish, the relationship-coaching app, "
    "which the firm listed in 2020 to 2022; Rob Stavis is the director on the April 2020 filing of its $5M round. The same "
    "company as base row relish, a duplicate pair.", ec="site_listing", cite=jl.ARCH("relish")))
lines.append(jl.cls("hellorelish-inc", status="unknown", rng="below_1b", city="New York", focus="Consumer & Marketplaces",
    flags=["identity_conflated"],
    rounds=[jl.rnd("2020-04", "unnamed round ($5M)", 5000000, None, True, FD["relish"], "filing")],
    note="Same company as base row relish. The firm dropped Relish from its list after 2022 and no report of a sale, a "
         "later round or a shutdown was found (Google News, 2026-10-01), so the status reads unknown. The Form D address is "
         "a founder's (Mamaroneck, New York); the company worked from New York. Graduation left for the graduation pass."))

# ---- TIZ, Inc. = Provi
lines.append(jl.verdict("tiz-inc", M, "TIZ, Inc. is the legal name of Provi, the Chicago alcohol-ordering marketplace (chief "
    "executive Taylor Katzman on the filings), which the firm lists (partnered 2019, Kent Bennett); Kent Bennett is the "
    "director on the 2023 and 2026 filings, and Provi's own release names Bessemer in its 2021 rounds. The same company as "
    "base row provi, a duplicate pair.", ec="site_listing", cite=jl.SITE("provi")))
lines.append(jl.cls("tiz-inc", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
    entry_date="2019", city="Chicago", focus="Consumer & Marketplaces", flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2019", "Series A", None, "Bessemer Venture Partners", True, None, "press"),
            jl.rnd("2021", "Series B", 25000000, "CPMG", True, PROVI_PR, "company"),
            jl.rnd("2021-09", "Series C", 75000000, "D1 Capital Partners", True, PROVI_PR, "company"),
            jl.rnd("2023-10", "unnamed round ($32.5M sold)", 32500000, None, None, FD["tiz"], "filing")],
    note="Same company as base row provi. The firm's list dates the partnership to 2019, the year of Provi's Series A, "
         "which Bessemer led; model, the 2019 announcement was not retrieved, and Provi's 2021 release confirms Bessemer "
         "as an existing investor in the Series B and C. This disputes the Form D band, which read the 2023 filing. The "
         "Series C of September 2021 was priced at a $750M valuation (the company's release), below $1B."))

# ---- Make Cents Technologies Inc = Cents
lines.append(jl.verdict("make-cents-technologies-inc", M, "Make Cents Technologies Inc is the legal name of Cents, the New "
    "York laundry-software company (chief executive Alex Jekowsky on the filing), which the firm lists (partnered 2020, "
    "Kent Bennett); Kent Bennett is the director on the 2024 filing, and the Series B release names Bessemer as an "
    "existing investor. The same company as base row cents, a duplicate pair.", ec="site_listing", cite=jl.SITE("cents")))
lines.append(jl.cls("make-cents-technologies-inc", status="private", rng="below_1b", stage="undetermined", entry_date="2020",
    city="New York", focus="SaaS", flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2024-08", "Series B", 40000000, "Camber Creek", True, CENTS_B, "company"),
            jl.rnd("2026-03", "Series C", 140000000, "Sumeru Equity Partners", None, CENTS_C, "press")],
    note="Same company as base row cents. The firm's list dates the partnership to 2020, four years before the Series B "
         "filing the Form D band read as a Growth entry, so the band is disputed; Bessemer led one of the earlier rounds "
         "(AlleyWatch, 2024-08-07: Bessemer and Tiger Global were 'lead investors of our previous rounds'), but no page "
         "retrieved names which, so the stage reads undetermined. No valuation was stated at the $140M Series C of March "
         "2026 (FinTech Global, read 2026-10-01), so the row stays below $1B."))

# ---- DYN365, Inc. = Restaurant365
lines.append(jl.verdict("dyn365-inc", M, "DYN365, Inc. is the legal name of Restaurant365 (Irvine; founders Tony Smith, Morgan "
    "Harris and John Moody on the filings), which the firm lists (partnered 2017, Brian Feinstein); Brian Feinstein and Ben "
    "Mathews are the directors on the 2018 filing, and the company's own releases name Bessemer in its Series A and B. The "
    "same company as base row restaurant365, a duplicate pair.", ec="site_listing", cite=jl.SITE("restaurant365")))
lines.append(jl.cls("dyn365-inc", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=R365_D,
    asof="2023-05-19", stage="Series A", stage_src="web_verified", stage_cite=R365_A, stage_conf="high",
    entry_date="2018-01", city="Irvine", focus="SaaS", flags=["identity_conflated", "stale"],
    extra={"valuation_range_source": "web_verified"},
    rounds=[jl.rnd("2018-01", "Series A", 20000000, "Bessemer Venture Partners", True, R365_A, "company"),
            jl.rnd("2019-01", "Series B", 19500001, None, True, R365_C, "company"),
            jl.rnd("2019-06", "Series C", 88000000, "ICONIQ Capital", True, FD["dyn19"], "filing"),
            jl.rnd("2023-05", "unnamed growth round", 135000000, "KKR and L Catterton", True, R365_D, "company")],
    note="Same company as base row restaurant365. The company's own release: 'In January 2018, Restaurant365 closed $20 "
         "million in Series A financing with a minority investment from Bessemer Venture Partners', which agrees with the "
         "band's Series A and corrects its date (the band read the Series B filing of December 2018; the firm's own invest "
         "date is 2017-12-27). The $135M round of May 2023 crossed '$1B in value' (the company's release), the mark the "
         "ICONIQ and Tiger Global books carry; older than 24 months, so stale."))

# ---- Evolve Bits, Inc. = Zenskar
lines.append(jl.verdict("evolve-bits-inc", M, "Evolve Bits, Inc. is the legal name of Zenskar (founders Apurv Bansal and "
    "Saurabh Agrawal on the filings), which the firm lists (partnered 2022, Anant Vidur Puri) and whose $3.5M seed it led; "
    "Anant Puri is the director on the filings. The same company as base row zenskar, a duplicate pair.",
    ec="site_listing", cite=jl.SITE("zenskar")))
lines.append(jl.cls("evolve-bits-inc", status="private", rng="below_1b", city="New York", city_src="formd_address",
    focus="SaaS", grad="graduated", grad_src="web_verified", grad_cite=ZEN_A, grad_conf="high",
    flags=["identity_conflated"],
    rounds=[jl.rnd("2022-10", "Seed", 3500000, "Bessemer Venture Partners", True, ZEN_SEED, "press"),
            jl.rnd("2026-04", "Series A", 15000000, "Susquehanna Venture Capital", True, ZEN_A, "press")],
    note="Same company as base row zenskar. Bessemer led the $3.5M seed (Entrackr, 2022-10-04), which agrees with the band. "
         "Graduated: a $15M Series A in April 2026 led by Susquehanna Venture Capital with Bessemer, Shine Capital and Rho "
         "(FinTech Global, 2026-04-20). No valuation was stated at the Series A, so the row stays below $1B (checked "
         "2026-10-01). The company works from New York and Bangalore."))

# ---- T3C Inc = T3Ci, later Retail Solutions
lines.append(jl.verdict("t3c-inc", M, "T3C Inc is T3Ci, renamed Retail Solutions, which the firm lists (partnered 2005, Byron "
    "Deeter; the archived list reads 'Retail Solutions Inc. (fka T3Ci)'); the filings name Byron Deeter as director 'c/o "
    "Bessemer Venture Partners'. The same company as base row retail-solutions, a duplicate pair.", ec="site_listing",
    cite=jl.SITE("retail-solutions")))
lines.append(jl.cls("t3c-inc", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_cite=FD["t3c"], stage_conf="medium", city="Mountain View", focus="SaaS",
    flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2005-11", "Series B", None, "Bessemer Venture Partners", True, FD["t3c"], "filing"),
            jl.rnd("2010-09", "Series C", 15200002, None, True, FD["t3c10"], "filing")],
    note="Same company as base row retail-solutions. Acq. by IRI (the firm's own listing names the acquirer). The filing "
         "itself describes the offering as the 'sale and issuance of Series B preferred stock' with a first sale on "
         "2005-11-01 and Byron Deeter of Bessemer on the board, and the firm's list dates its investment to 2005-10-31, so "
         "the entry is the Series B, Growth, against the band's Series A."))

# ---- Every Neighbor Deserves Kindness, Inc. = Mural Health
lines.append(jl.verdict("every-neighbor-deserves-kindness-inc", M, "Every Neighbor Deserves Kindness, Inc. is the earlier "
    "legal name of Mural Health (co-chief executives Sam Whitaker and Jason Dong on the filing; the same SEC registrant, CIK "
    "1936452, as the listed row's 2024 filing), which the firm lists (partnered 2022, Steve Kraus); Steve Kraus is the "
    "director on the 2022 filing. The same company as base row mural-health, a duplicate pair.", ec="site_listing",
    cite=jl.SITE("mural-health")))
lines.append(jl.cls("every-neighbor-deserves-kindness-inc", status="private", rng="below_1b", stage="Seed",
    stage_src="formd_band", entry_date="2022-06-23", city="Berwyn", city_src="web_verified", focus="Healthcare & Bio",
    flags=["identity_conflated"],
    rounds=[jl.rnd("2022-06-23", "unnamed first round ($7.5M)", 7500000, None, True, FD["mural"], "filing")],
    note="Same company as base row mural-health. The entry is the company's first financing, $7.5M sold from 2022-06-23 by "
         "a company incorporated that year with Steve Kraus on the board (this Form D), which the band rule reads as Seed "
         "(at or under the $8M ceiling for 2022); the row's own filings were keyed to the listed row, so the band is "
         "written here by hand. Headquarters Berwyn, Pennsylvania (Technical.ly, 2023-07-18). Graduation left for the "
         "graduation pass (the listed row's 2024 filing is $12.7M)."))

# ---- Birch Solutions, Inc. = Fern
lines.append(jl.verdict("birch-solutions-inc", M, "Birch Solutions, Inc. is the legal name of Fern (chief executive Danny "
    "Sheridan and co-founder Deep Singhvi on the filing), which the firm lists (partnered 2025, Lindsey Li) and whose $9M "
    "Series A the firm's own post says it led; Lindsey Li is the director on the 2024 filing. The same company as base row "
    "fern, a duplicate pair.", ec="site_listing", cite=jl.SITE("fern")))
lines.append(jl.cls("birch-solutions-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=FERN_POST, stage_conf="high", city="New York", focus="DevTools & APIs", flags=["identity_conflated"],
    rounds=[jl.rnd("2024-09-30", "Series A", 9000000, "Bessemer Venture Partners", True, FERN_POST, "firm"),
            jl.rnd("2026-01", "acquisition by Postman", None, None, None, FERN_ACQ, "press")],
    note="Same company as base row fern. Acq. by Postman, 2026 (InfoWorld, 2026-01-12). The firm's own "
         "post: 'Bessemer Venture Partners leads Fern's $9M Series A' (announced April 2025; this Form D dates the first "
         "sale to 2024-09-30 and carries $12.8M with the earlier notes), which agrees with the withheld band."))

# ---- FlexCorp Inc (formerly FlexCharge Inc.) = FlexFactor: not on the firm's list, corroborated by the company's release
lines.append(jl.verdict("flexcorp-inc", M, "FlexCorp Inc (formerly FlexCharge Inc.) is FlexFactor, the payment-decline "
    "recovery company (chief executive Elio Vitucci on the filing): its own release announces a $16.8M Series A led by "
    "Bessemer Venture Partners, the amount on this Form D, on which Charles William Birnbaum is a director. The company is "
    "not on the firm's list; the round is the corroboration.", ec="web", cite=FLEX_PR))
lines.append(jl.cls("flexcorp-inc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=FLEX_PR, stage_conf="high", city="Miami", city_src="web_verified", focus="Fintech & Payments",
    rounds=[jl.rnd("2024-10-10", "Series A", 16800000, "Bessemer Venture Partners", True, FLEX_PR, "company")],
    note="FlexFactor (legal name FlexCorp Inc). The company's release of 2024-10-10: $16.8M Series A led by Bessemer "
         "Venture Partners with the seed investors (this Form D dates the first sale to 2024-06-18). Headquarters Miami "
         "(the release's dateline; the Form D gives a Milpitas, California office). Momentum check: no $1B+ priced round "
         "found (Google News, 2026-10-01)."))

# ---- Strala Group, Inc.: director of record only, flagged for review
lines.append(jl.verdict("strala-group-inc", M, "Director of record (COLLECTION.md s1): Charles Birnbaum, a current Bessemer "
    "partner who co-leads its fintech practice, is a director on the Form D of Strala's $51.3M round (first sale "
    "2026-03-26), inside his tenure, on a named operating company (Strala, a San Francisco insurance-claims platform "
    "founded in 2024). No source names Bessemer in the round (the one press report names Founders Fund and Emergence) and "
    "the company is not yet on the firm's list, so this is an unannounced deal at medium confidence, flagged for review.",
    ec="formd_adjudicated", conf="medium", cite=FD["strala"]))
lines.append(jl.cls("strala-group-inc", status="private", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
    rounds=[jl.rnd("2026-03-26", "unnamed round ($51.3M)", 51342804, None, None, STRALA, "press")],
    note="Strala, an insurance-claims platform (a technology-enabled claims administrator). Member on the director-of-record "
         "pattern only: Bessemer is not named in the round's one press report (Coverager, 2026-04-06, which names Founders "
         "Fund and Emergence and states no valuation). Momentum check: no $1B+ priced round found (Google News and "
         "Coverager, 2026-10-01)."))

# ---- CozyKin, Inc.: not on the firm's list, corroborated by press
lines.append(jl.verdict("cozykin-inc", M, "CozyKin raised a $6M Series A from Bessemer Venture Partners, NextView Ventures "
    "and Primary Venture Partners (EdSurge, 2019-05-20), the round on this Form D, on which Kent Bennett is a director. "
    "The company is not on the firm's list; the round is the corroboration.", ec="web", cite=COZY))
lines.append(jl.cls("cozykin-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=COZY, stage_conf="high", city="Cambridge", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    rounds=[jl.rnd("2018-12-11", "Series A", 6000001, None, True, COZY, "press")],
    note="Acq. by Higher Ground Education, 2020 (Business Wire, 2020-03-12). The press names the $6M round a Series A with "
         "Bessemer among its three investors, against the Form D band's Seed; the Form D dates the first sale to "
         "2018-12-11."))

# ---- the Bessemer-vehicle filing rows (membership prefilled; classification only)
lines.append(jl.cls("directv-broadband-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=TELOCITY_424, stage_conf="high", entry_date="1998-07-08", country="US", city="Cupertino",
    focus="Data Infrastructure", flags=["identity_conflated"],
    rounds=[jl.rnd("1998-07-08", "Series A", 6575000, None, True, TELOCITY_424, "filing"),
            jl.rnd("1999-02-16", "Series B", 14500000, None, True, TELOCITY_424, "filing"),
            jl.rnd("1999-12-13", "Series C", 127500000, None, True, TELOCITY_424, "filing")],
    note="DIRECTV Broadband is Telocity renamed after Hughes Electronics bought it in 2001 (acq. by Hughes, 2001; the "
         "service was shut in 2003): the same SEC registrant and the same company as base row telocity, a duplicate pair. "
         "Telocity's IPO prospectus lists Bessemer Venture Partners IV, Bessec Ventures IV and Bessemer Venture Investors "
         "among the buyers of the series A preferred sold on 1998-07-08 at $0.50 a share, so the entry is the Series A."))
lines.append(jl.cls("factory-card-outlet-corp", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_cite=FCO_424, stage_conf="medium", entry_date="1994-07", country="US", city="Naperville",
    focus="Consumer & Marketplaces",
    rounds=[jl.rnd("1989-07", "Series A", None, None, False, FCO_424, "filing"),
            jl.rnd("1994-07-15", "Series B", None, None, True, FCO_424, "filing")],
    note="A party-goods and greeting-card retailer; acq. by Amscan (AAH Holdings), 2007, after a 1999 to 2002 bankruptcy. "
         "The IPO prospectus has Bessemer Venture Partners FCOA (managed by Bessemer Venture Partners III) at 9.2% and "
         "Bessemer's Robert Barach on the board since July 1994, the month of the Series B stock purchase agreement "
         "(effective 1994-07-15); the Series A dates from 1989, before that fund existed, so the entry "
         "is read as the Series B, Growth, at medium confidence (the prospectus does not list the Series B buyers by name)."))
lines.append(jl.cls("learmonth-burchett-management-systems-plc-england", status="acquired", rng="below_1b",
    stage="undetermined", entry_date="1993", country="US", city="Houston", focus="DevTools & APIs",
    flags=["identity_conflated"], rounds=[],
    note="LBMS, a maker of software-development process tools: the same company as base row lbms, a duplicate pair. Acq. by "
         "Platinum Technology, 1998. Founded in London, it moved its operating headquarters to Houston in fiscal 1995 (its "
         "10-K), so the country reads US. The firm's list dates the investment to 1993; no filing read (the 13Gs of 1997 "
         "and 1998, the fiscal 1997 10-K) names the round Bessemer Venture Partners III bought, so the stage is undetermined."))
lines.append(jl.cls("promedco-management-co", status="defunct", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_cite=PROMEDCO_424, stage_conf="high", entry_date="1995-12", country="US", city="Fort Worth",
    focus="Healthcare & Bio",
    rounds=[jl.rnd("1995-12", "Series A", 3000000, "Bessemer Venture Partners", True, PROMEDCO_424, "filing")],
    note="A physician practice management company. Its IPO prospectus: 'In December 1995 the Company issued an aggregate of "
         "500,000 shares of Series A Redeemable Convertible Preferred Stock at a purchase price of $6.00 per share to "
         "Bessemer Venture Partners', so the entry is the Series A. The company filed for bankruptcy in 2001 and was wound "
         "down (it deregistered in 2003), so defunct."))
lines.append(jl.cls("summagraphics-corp", status="acquired", rng="below_1b", stage="undetermined", country="US",
    city="Austin", focus="Industrial & Robotics", rounds=[],
    note="A maker of digitizing tablets and plotters, incorporated in 1972. Acq. by Lockheed Martin, 1996: in the July 1996 "
         "exchange Summagraphics took in Lockheed Martin's CalComp, Lockheed Martin came to hold 89.7%, and the company "
         "was renamed CalComp Technology. The 1996 proxy has Bessemer Venture Partners I and II among the holders and "
         "Bessemer's Felda Hardymon as a former director, a venture position; no filing read names the round or its "
         "year, so the stage is undetermined and no entry date is given."))

assert sum(1 for x in lines if "verdict" in x) == 11 and len(lines) == 27, len(lines)
jl.write("jmg", lines)
