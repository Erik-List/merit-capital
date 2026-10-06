"""PRO-80 Bessemer, judge jm, file f: members, first half (batches 21 to 25).

Every row here is a company the firm lists under its brand or later name, reached by the base a second time
through the legal name on a Form D. Each is judged a member on the firm's own listing of the brand (cited) and
flagged `identity_conflated`, with the listed base row named, so the pair can be merged in identity-merges.json.
"""
import judge_lib as jl

M = "member"
lines = []
FD = {
    "2tor": "https://www.sec.gov/Archives/edgar/data/1459417/000145941711000003/0001459417-11-000003-index.htm",
    "adaptive": "https://www.sec.gov/Archives/edgar/data/1278150/000127815013000001/0001278150-13-000001-index.htm",
    "dolores": "https://www.sec.gov/Archives/edgar/data/1477518/000147751810000002/0001477518-10-000002-index.htm",
    "justin": "https://www.sec.gov/Archives/edgar/data/1558564/000155856412000001/0001558564-12-000001-index.htm",
}
ADAPTIVE_S1 = "https://www.sec.gov/Archives/edgar/data/1278150/000119312518166221/d454129ds1.htm"

# ---- 2tor, Inc. = 2U
lines.append(jl.verdict("2tor-inc", M, "2tor, Inc. is the earlier name of 2U, which the firm lists (partnered 2011, Rob "
    "Stavis; the archived 2012 list carries it as '2tor'); Rob Stavis is the director on the 2011 and 2012 filings. The same "
    "company as base row 2u, a duplicate pair.", ec="site_listing", cite=jl.SITE("2u")))
lines.append(jl.cls("2tor-inc", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
    entry_date="2011-03-04", city="Arlington", focus="SaaS", flags=["identity_conflated"],
    rounds=[jl.rnd("2011-03", "Series D ($32.5M)", 32499982, "Bessemer Venture Partners", True, FD["2tor"], "filing")],
    note="Same company as base row 2u (2tor renamed 2U in 2012). Bessemer led the $32.5M round of March 2011 (Form D 2011 Q1, "
         "Rob Stavis joins the board; the firm's own invest date is 2011-03-04), the company's fourth priced round after "
         "three in 2009 and 2010, so Growth; model, the round's press page was not retrieved. Headquarters moved from "
         "Lanham, Maryland to Arlington, Virginia. Graduation not applicable."))

# ---- Adaptive Planning = Adaptive Insights
lines.append(jl.verdict("adaptive-planning-inc", M, "Adaptive Planning, Inc. is the earlier name of Adaptive Insights, which "
    "the firm lists (partnered 2013, Bob Goodman and Byron Deeter; the archived 2013 list carries it as 'Adaptive Planning, "
    "Inc.'), and the company's S-1 names Bessemer Venture Partners VIII as a holder. The same company as base row "
    "adaptive-insights, a duplicate pair.", ec="site_listing", cite=jl.SITE("adaptive-insights")))
lines.append(jl.cls("adaptive-planning-inc", status="acquired", rng="below_1b", stage="Growth", stage_src="model",
    stage_conf="medium", entry_date="2013-05", city="Palo Alto", focus="SaaS", flags=["identity_conflated"],
    rounds=[jl.rnd("2013-05", "unnamed late round ($45M)", 44999984, None, True, FD["adaptive"], "filing"),
            jl.rnd("2015-06", "Series G", 74999994, "JMI Equity", None, ADAPTIVE_S1, "filing")],
    note="Same company as base row adaptive-insights. Acq. by Workday, 2018. Bessemer entered in the $45M round of May 2013 "
         "(Form D 2013 Q2; the S-1 has Byron Deeter on the board since May 2013), a late round of a company founded in 2003 "
         "with a $22M round the year before, so Growth; model, the round's own name was not found (the S-1 lists only the "
         "2015 Series G)."))

# ---- Hyper Labs, Inc. = Hyperscience
lines.append(jl.verdict("hyper-labs-inc", M, "Hyper Labs, Inc. is the legal name of Hyperscience (New York; the filings carry "
    "its $60M, $80M and $100M rounds of 2020 to 2022 with Elliott Robinson as director), which the firm lists (partnered "
    "2020, Elliott Robinson). The same company as base row hyperscience, a duplicate pair.", ec="site_listing",
    cite=jl.SITE("hyperscience")))
lines.append(jl.cls("hyper-labs-inc", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
    stage_cite=jl.POST("hyperscience-series-c-investment"), stage_conf="high", entry_date="2020-06", city="New York",
    focus="AI & Applied AI", flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2020-06", "Series C", 60000000, "Bessemer Venture Partners", True, jl.POST("hyperscience-series-c-investment"), "firm"),
            jl.rnd("2020-10", "Series D", 80000000, "Tiger Global", None, jl.NEWS("hyper-labs-inc", "Raises $80M Series D Led by Tiger Global"), "company"),
            jl.rnd("2021-12", "Series E", 100000000, None, True, jl.NEWS("hyper-labs-inc", "Raises $100M in Growth"), "press")],
    note="Same company as base row hyperscience. The firm's own post: Bessemer leads the $60M Series C (June 2020), and its "
         "list dates the partnership to 2020, so the entry is the Series C, Growth; this disputes the Form D band, which "
         "read a 2018 filing with no Bessemer person on it. No valuation was disclosed at the $100M Series E of December "
         "2021 (FinSMEs, read 2026-10-01), so the row stays below $1B."))

# ---- Justin.tv, Inc. = Twitch
lines.append(jl.verdict("justin-tv-inc", M, "Justin.tv, Inc. is the corporate entity of Twitch: the firm's own memo says 'we "
    "would be investing in the Justin.tv corporate entity which includes both Twitch.tv and Justin.tv', and the firm lists "
    "Twitch (partnered 2012). The same company as base row twitch, a duplicate pair.", ec="site_listing",
    cite=jl.POST("memos/twitch")))
lines.append(jl.cls("justin-tv-inc", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
    stage_cite=jl.POST("memos/twitch"), stage_conf="high", entry_date="2012-09-11", city="San Francisco",
    focus="Media, Gaming & Advertising", flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2012-09", "Series B", None, "Bessemer Venture Partners", True, jl.POST("memos/twitch"), "firm")],
    note="Same company as base row twitch. Acq. by Amazon, 2014 (about $970M). The firm's own investment memo of July 2012 is "
         "headed 'Twitch Series B' and recommends $13M at $53M pre-money, so the entry is the Series B, Growth, against the "
         "Form D band's Series A; the firm's own invest date is 2012-09-11."))

# ---- Dolores Labs, Inc. = CrowdFlower (later Figure Eight)
lines.append(jl.verdict("dolores-labs-inc", M, "Dolores Labs, Inc. is the legal name of CrowdFlower (later Figure Eight), which "
    "the firm lists from 2010 with an investment date of 2009-12-08, the first-sale date on this Form D; James Cham, then a "
    "Bessemer vice president, is the director. The same company as base row crowdflower, a duplicate pair.",
    ec="site_listing", cite=jl.ARCH("crowdflower")))
lines.append(jl.cls("dolores-labs-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="model",
    stage_conf="medium", country="US", city="San Francisco", focus="AI & Applied AI",
    flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2009-12", "Series A", 5080471, None, True, FD["dolores"], "filing")],
    note="Same company as base row crowdflower. Acq. by Appen, 2019, as Figure Eight (Finovate, 2019-04-18, names Bessemer "
         "among its investors). The $5.1M round of December 2009 on the Form D was CrowdFlower's Series A, from Trinity "
         "Ventures and Bessemer, after a 2009 seed; model, the announcement page was not retrieved, so this disputes the "
         "band's Seed at medium confidence."))

# ---- PinPT, Inc. = Pinpoint
lines.append(jl.verdict("pinpt-inc", M, "PinPT, Inc. is the legal name of Pinpoint (Jeff Haynie's engineering-analytics "
    "company), which the firm listed in 2019 to 2022 and whose $13.5M Series A the firm's own post says it led; Ethan "
    "Kurzweil is the director on the 2018 filing. The same company as base row pinpoint, a duplicate pair.",
    ec="site_listing", cite=jl.POST("bessemer-series-a-investment-pinpoint")))
lines.append(jl.cls("pinpt-inc", status="unknown", rng="below_1b", city="Austin", focus="DevTools & APIs",
    flags=["identity_conflated"],
    note="Same company as base row pinpoint. The firm dropped Pinpoint from its list after 2022 and its chief executive "
         "Jeff Haynie joined Shopmonkey as chief technology officer in June 2022 (GlobeNewswire), which says nothing of a "
         "sale or a shutdown; no later trace found (Google News, 2026-10-01), so the status reads unknown."))

# ---- Shop My Shelf, Inc. = ShopMy
lines.append(jl.verdict("shop-my-shelf-inc", M, "Shop My Shelf, Inc. is the legal name of ShopMy, which the firm lists "
    "(partnered 2025, Jeremy Levine) and whose $77.5M Series B the firm's own post says it led; Jeremy Levine is the "
    "director on the 2025 filing. The same company as base row shopmy, a duplicate pair.", ec="site_listing",
    cite=jl.SITE("shopmy")))
lines.append(jl.cls("shop-my-shelf-inc", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
    val_cite=jl.NEWS("shop-my-shelf-inc", "ShopMy Raises $70M at $1.5 Billion Valuation to Scale"), asof="2025-10-22",
    city="New York", focus="Media, Gaming & Advertising", flags=["identity_conflated"],
    extra={"valuation_range_source": "web_verified"},
    note="Same company as base row shopmy. ShopMy raised $70M at a $1.5B valuation on 2025-10-22 (the company's release), "
         "the mark the Bain Capital Ventures book also carries. The Form D address is a founder's (Holden, Massachusetts); "
         "the company is in New York."))

# ---- Tinz Optics, Inc. = Light
lines.append(jl.verdict("tinz-optics-inc", M, "Tinz Optics, Inc. is the legal name of Light, the multi-lens camera company, "
    "which the firm listed from 2014 with an investment date of 2014-05-09; Bob Goodman is the director on the 2014 filing "
    "of its $9M round. The same company as base row light, a duplicate pair.", ec="site_listing", cite=jl.ARCH("light")))
lines.append(jl.cls("tinz-optics-inc", status="acquired", rng="below_1b", city="Palo Alto", focus="Industrial & Robotics",
    flags=["identity_conflated"],
    note="Same company as base row light. John Deere bought Light's patents and intellectual property and hired its team "
         "in May 2022 (Precision Farming Dealer), a sale of the business's core, so acquired (acq. by Deere, 2022), as the "
         "GV book reads it."))

# ---- Recover Together, Inc. = Groups
lines.append(jl.verdict("recover-together-inc", M, "Recover Together, Inc. is the legal name of Groups (Groups Recover "
    "Together), which the firm lists (partnered 2017, Steve Kraus); Steve Kraus is the director on the 2017 and 2021 "
    "filings. The same company as base row groups, a duplicate pair.", ec="site_listing", cite=jl.SITE("groups")))
lines.append(jl.cls("recover-together-inc", status="private", rng="below_1b", stage="Series A", stage_src="first_party",
    stage_cite=jl.POST("our-deep-health-seed-program"), stage_conf="high", entry_date="2017-04-11", city="Burlington",
    focus="Healthcare & Bio", flags=["identity_conflated", "stage_disputes_band"],
    rounds=[jl.rnd("2017-04", "Series A", None, "Bessemer Venture Partners", True, jl.POST("our-deep-health-seed-program"), "firm")],
    note="Same company as base row groups. The firm's own post says 'We led the Series A of ... Groups', and its list dates "
         "the investment to 2017-04-11, so the entry is the Series A, against the Form D band's Seed (a $1.2M filing of "
         "June 2017). Headquarters Burlington, Massachusetts (the 2021 filings)."))

# ---- K2 Global Consulting, Inc. = K2 Intelligence, now K2 Integrity
lines.append(jl.verdict("k2-global-consulting-inc", M, "K2 Global Consulting is the earlier name of K2 Intelligence, now K2 "
    "Integrity, which the firm lists (partnered 2010, Rob Stavis; the archived 2012 list carries it as 'K2 Global "
    "Consulting'); Eric Arnold, then on the firm's team, is the director on the 2010 filings. The same company as base rows "
    "k2-intelligence and k2-integrity, a duplicate group.", ec="site_listing", cite=jl.SITE("k2-integrity")))
lines.append(jl.cls("k2-global-consulting-inc", status="private", rng="below_1b", city="New York",
    flags=["identity_conflated"], extra={"focus": None},
    note="Same company as base rows k2-intelligence and k2-integrity (renamed K2 Integrity in November 2020). An "
         "investigations and risk-advisory firm, outside the focus taxonomy. Graduation left for the graduation pass."))

# ---- ReputationDefender Inc = Reputation (Reputation.com)
lines.append(jl.verdict("reputationdefender-inc", M, "ReputationDefender is the earlier name of Reputation.com, now "
    "Reputation, which the firm lists (partnered 2009, David Cowan; the archived 2010 list carries it as "
    "'ReputationDefender'); David Cowan is the director on the 2010 filing. The same company as base row reputation, a "
    "duplicate pair.", ec="site_listing", cite=jl.SITE("reputation")))
lines.append(jl.cls("reputationdefender-inc", status="private", rng="below_1b", stage="Growth", stage_src="model",
    stage_conf="medium", entry_date="2009-04-17", city="San Ramon", focus="SaaS", flags=["identity_conflated"],
    rounds=[jl.rnd("2009-04", "unnamed round ($5.4M, Form D 2009 Q2)", 5396000, None, True, None, "filing"),
            jl.rnd("2010-05", "unnamed round ($12M, Form D 2010 Q2)", 11990648, None, True,
                   "https://www.sec.gov/Archives/edgar/data/1392955/000149083310000002/0001490833-10-000002-index.htm", "filing")],
    note="Same company as base row reputation. The firm's own invest date is 2009-04-17, the $5.4M round on the company's "
         "2009 Form D; the company, founded in 2006, had already raised two venture rounds (2007 and 2008), so "
         "the entry is a third round, Growth; model, no page naming the 2009 round was retrieved. The consumer business "
         "was sold in 2018 and the enterprise company continues as Reputation, now in San Ramon, California."))

assert sum(1 for x in lines if "verdict" in x) == 11 and len(lines) == 22, len(lines)
jl.write("jmf", lines)
