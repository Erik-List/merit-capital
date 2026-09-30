"""PRO-100 NEA, judge m3, second half (38 rows): Form D name-match rows, judged cluster-first.
Run: NQ_TAG=m3 python3 judgments-m3b.py"""
import judge_lib as jl

verdict, cls, rnd = jl.verdict, jl.cls, jl.rnd
FD = "formd_adjudicated"
SEC = "https://www.sec.gov/Archives/edgar/data/"
L = []


def out(slug, basis, conf="high", cite=None, ec=FD):
    L.append(verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=cite))


# ---------------- Mark Perry: NEA's Mark Perry was an IT general partner; the filer is a biotech executive ----------------
MP = ("NEA's Mark Perry was a general partner in Menlo Park with the investment area IT (the firm's team pages 2008-2013); the "
      "Mark Perry on this filing is a biotech executive")
out("aerovance-inc", f"{MP}, Aerovance's own executive officer and director (Berkeley, 2009), and no NEA listing, post or filing "
    "names Aerovance (T4 homonym).")
out("myokardia-inc", f"{MP} on MyoKardia's 2014-2015 board; EDGAR full-text search finds no MyoKardia filing naming NEA, and "
    "no NEA listing or post names it (T4 homonym).")
out("pathway-therapeutics-inc", f"{MP} on Pathway Therapeutics' 2012-2013 board beside GBS Venture Partners, and no NEA listing, "
    "post or filing names Pathway (T4 homonym).")

# ---------------- Scott Gottlieb: NEA venture partner (team pages 2008-2017), special partner from 2020 ----------------
SG = ("Scott Gottlieb was an NEA venture partner at the time (team pages 2008-2017); a venture partner's seat counts only where an "
      "NEA fund held the position (D4)")
out("aseko-inc", f"{SG}, and nothing ties NEA money to Aseko (Glytec, Greenville, SC): no NEA listing in any era, post, fund "
    "filing or round names NEA (T4 personal seat).")
out("kure-corp", f"{SG}; Kure Corp. is a Mooresville, NC chain of vapor lounges whose 2015 filing lists him among its directors, "
    "and no NEA listing, post or filing names it (T4 personal seat).")
out("medavante-inc", f"{SG}, and nothing ties NEA money to MedAvante (Hamilton, NJ): no NEA listing in any era, post, fund filing "
    "or round names NEA (T4 personal seat).")

# ---------------- Greg Raleigh: NEA venture advisor only from 2018 ----------------
GR = ("Greg Raleigh joined NEA only as a venture advisor in 2018 (team pages 2018-2023)")
out("headwater-partners-i-llc", f"{GR}; on Headwater Partners I's 2009-2012 filings he is its own executive officer, the patent "
    "holding company he founded beside ItsOn, a founder seat years before, and an IP vehicle (T4, D5).")
out("headwater-partners-ii-llc", f"{GR}; on Headwater Partners II's 2011 filing he is its own executive officer, a founder seat "
    "years before, and an IP vehicle (T4, D5).")
out("itson-inc", f"{GR}; he founded ItsOn and is its executive officer on the 2009-2014 filings, a founder seat years before his "
    "NEA role, and no NEA listing, post or filing names ItsOn (T4).")
out("triaxis-medical-devices-inc", f"{GR}; his 2009 TriAxis Medical Devices seat is years before that, and no NEA listing, post or "
    "filing names TriAxis (T4).")

# ---------------- Tiffany Luck: GGV Capital partner until she joined NEA in January 2024 ----------------
TL = jl.POST("nea-welcomes-tiffany-luck")
out("mindee-inc", "Tiffany Luck joined NEA from GGV Capital in January 2024 and the firm's own release says she led Mindee at GGV; "
    "Mindee's 2023 filing lists her at GGV's 3000 Sand Hill Road address, a seat from her earlier firm (T4).", cite=TL)
out("stream-io-inc", "Tiffany Luck joined NEA from GGV Capital in January 2024 and the firm's own release says she led Stream at "
    "GGV; the 2020-2021 filing seats are GGV's (T4).", cite=TL)
out("yac-inc", "Tiffany Luck's seat on Yac's January 2021 filing dates from her GGV Capital years; she joined NEA in January 2024 "
    "(the firm's own release), and no NEA listing, post or filing names Yac (T4).", cite=TL)

# ---------------- Hugh Panero: NEA venture partner 2008-2011; Tony Florence on Popdust ----------------
out("alarm-com-holdings-inc", "Hugh Panero was an NEA venture partner from 2008 to 2011 (Alarm.com's registration statement), "
    "and his Alarm.com seat from August 2010 is an independent directorship: the statement names NEA only in his biography and "
    "lists no NEA fund among holders, and the 2012 filing comes after his NEA years (D4).", cite=jl.FTS("Alarm.com", "DRS"))
L.append(verdict("popdust-inc", "member",
    "Tony Florence, an NEA partner in 2012 (team pages), is a director of record on Popdust's May 2012 filing at NEA's own Chevy "
    "Chase office (5425 Wisconsin Avenue, Suite 800), beside founder-CEO Hugh Panero, himself an NEA venture partner to 2011. "
    "Popdust resolves to the New York music and pop-culture publisher; the in-tenure seat at the firm's address is the adjudicated "
    "pattern, flagged for the A/B pass.", ec=FD, conf="medium",
    cite=SEC + "1551043/000155104312000002/0001551043-12-000002-index.htm"))
L.append(cls("popdust-inc", status="private", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
    note="Pop-culture and music publisher; popdust.com still publishes under Popdust Inc. (site footer, 2026). Graduation left for "
         "the graduation pass."))

# ---------------- Forest Baskett ----------------
L.append(verdict("azuray-technologies-inc", "member",
    "Two in-tenure NEA partners, Forest Baskett (general partner) and Rohini Chakravarthy (partner), are directors and promoters of "
    "record on Azuray Technologies' June 2010 filing ($5M); Azuray resolves to the Durham, Oregon solar power electronics company "
    "beside Oregon State's Terri Fiez. The in-tenure seat is the adjudicated pattern, flagged for the A/B pass.",
    ec=FD, conf="medium", cite=SEC + "1438165/000143816510000004/0001438165-10-000004-index.htm"))
L.append(cls("azuray-technologies-inc", status="unknown", rng="below_1b", stage="undetermined", entry_date="2010-06",
    city="Durham", city_src="formd_address", focus="Climate & Energy", rounds=[],
    note="Solar power electronics (Durham, OR). The 2010 filing (first sale 2010-06-16) names no round, and nothing after it is on "
         "record: no later filing or press item."))
L.append(verdict("fusion-multisystems-inc", "member",
    "Same company as the listed member 'fusion-io': Fusion Multisystems, Inc. is Fusion-io's legal name (same EDGAR registrant, "
    "CIK 1383729), and the 2009-2010 filings list Forest Baskett and Scott Sandell at NEA's 2855 Sand Hill Road office. Recorded as a "
    "member so the row is not left unjudged; identity-merges.json should fold it into 'fusion-io'.",
    ec="site_listing", conf="high", cite=jl.SITE("fusion-io")))
FIO = jl.W("Fusion-io")
L.append(cls("fusion-multisystems-inc", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=FIO,
    stage_conf="high", entry_date="2008-03", city="Salt Lake City", focus="Data Infrastructure",
    rounds=[rnd("2008-03", "Series A", 19000000, "New Enterprise Associates", True, FIO, "press")],
    note="Fusion-io (flash storage), acquired by SanDisk in 2014. NEA led the $19M Series A in March 2008 (Wikipedia); the firm's "
         "own year field says 2007, a close year."))

# ---------------- Sheila Marcelo: NEA venture partner 2021-2023 ----------------
SM = "Sheila Marcelo was an NEA venture partner from 2021 to 2023 (team pages); a venture partner's seat counts only where an NEA fund held the position (D4)"
out("catalyte-inc", f"{SM}, and she is one of eight directors on Catalyte's 2023 filing (Baltimore) with no NEA listing, post, fund "
    "filing or round naming NEA (T4 personal seat).")
out("wag-group-co", f"{SM}; she joined Wag! Group's board as an independent director at its August 2022 listing (its 8-K), the "
    "filings are post-listing offerings, and no NEA fund held Wag (D4, X1).", cite=jl.FTS("Wag", "8-K"))

# ---------------- Michael Albert: NEA associate 2022-2023; the filer is a founder namesake ----------------
MA = "NEA's Michael Albert was an associate in Washington, DC (team pages 2022-2023)"
out("draynow-inc", f"{MA}; the Michael Albert on DrayNow's 2017 filing is its own executive officer and promoter (Pipersville, "
    "PA), a founder namesake (T4 homonym).")
out("pioneer-valley-trading-company-llc", f"{MA}; the Michael Albert on Pioneer Valley Trading Company's 2022 filing is its "
    "executive officer at a Westfield, MA home address, an operator namesake (T4 homonym).")

# ---------------- Charlotte Ross: NEA associate 2018-2019 ----------------
CR = "Charlotte Ross was an NEA associate in New York in 2018-2019 only (team pages)"
out("find-solace-inc", f"{CR}; her seat on Find Solace's 2025 filing comes years after, from her later firm, and no NEA listing, "
    "post or filing names the company (T4).")
out("paytient-technologies-inc", f"{CR}; her seat on Paytient's 2023 filings comes years after, from her later firm, and no NEA "
    "listing, post or filing names Paytient (T4).")

# ---------------- Mark Hawkins: NEA venture partner from 2023 ----------------
MH = "Mark Hawkins became an NEA venture partner in 2023 (team pages)"
out("obsidian-energy-ltd", f"{MH}; the Mark Hawkins on Obsidian Energy's 2021 filing is an officer of a listed Calgary oil "
    "producer, before those years, and no NEA surface names Obsidian (T4, X1).")
out("plex-systems-holdings-inc", f"{MH}; his seat on Plex Systems' 2014 filing, beside Francisco Partners' directors, comes nine "
    "years before, and no NEA listing, post or filing names Plex (T4).")

# ---------------- Tony Florence: duplicates of listed members ----------------
L.append(verdict("refresh-club-inc", "member",
    "Same company as the listed member 'the-wing': Refresh Club, Inc. is The Wing's legal name (founders Audrey Gelman and Lauren "
    "Kassan on the filing, Tony Florence as director), which NEA's archived list carries with a 2017 first investment. Recorded as a "
    "member so the row is not left unjudged; identity-merges.json should fold it into 'the-wing'.",
    ec="site_listing", conf="high", cite=jl.ARCH("the-wing")))
WING = jl.W("The Wing (workspace)")
L.append(cls("refresh-club-inc", status="defunct", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=WING,
    stage_conf="high", entry_date="2017-04", city="New York", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    rounds=[rnd("2017-04", "Series A", None, "New Enterprise Associates", True, WING, "press")],
    note="The Wing (women's coworking, New York), shut in 2022 (aligned with the GV and Sequoia rows). NEA led the Series A in April "
         "2017 (Wikipedia), so the band's Growth reading of the December 2018 filing is a later round."))
L.append(verdict("traina-interactive-corp", "member",
    "Same company as the listed member 'ifonly': Traina Interactive Corp. is IfOnly's legal name (founder Trevor Traina, director "
    "Tony Florence, the NEA deal team on the firm's IfOnly page). Recorded as a member so the row is not left unjudged; "
    "identity-merges.json should fold it into 'ifonly'.", ec="site_listing", conf="high", cite=jl.SITE("ifonly")))
L.append(cls("traina-interactive-corp", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
    note="IfOnly (experiences marketplace, San Francisco), acquired by Mastercard per the firm's own exit line (the Khosla row agrees)."))

# ---------------- Suzanne King ----------------
APPROVA_SALE = jl.NEWS("approva-corp", "sale to Infor")
L.append(verdict("approva-corp", "member",
    "Suzanne King, an NEA partner in Chevy Chase with the investment area IT (team pages 2008-2023), is a director of record on "
    "Approva's 2009 filing beside the directors of Novak Biddle, Sierra Ventures and Columbia Capital; Approva resolves to the "
    "Reston, VA controls-automation software company. The in-tenure seat is the adjudicated pattern, flagged for the A/B pass.",
    ec=FD, conf="medium", cite=SEC + "1163995/000116399509000003/0001163995-09-000003-index.htm"))
L.append(cls("approva-corp", status="acquired", rng="below_1b", country="US", city="Reston", focus="SaaS",
    note="Approva (controls-automation software, Reston, VA) was sold to Infor in 2011 (the deal announcement of DC Advisory, "
         "which advised on the sale, dated 2011-09-01 in Google News: " + APPROVA_SALE + ")."))

# ---------------- Tak Cheung: NEA partner to 2023 ----------------
out("cagent-vascular-inc", "Tak Cheung appears on NEA's team pages only to 2023 and not on the live team; his seat on Cagent "
    "Vascular's May 2026 filing came with the $41M Series D from U.S. Venture Partners and Astoria Health Investors, which names no "
    "NEA fund, and no NEA listing, post or filing names Cagent (T4, next-firm seat).",
    cite="https://projectstartups.com/startups/cagent-vascular-cagentvascularcom-2026-05-19/")

# ---------------- Mohamad Makhzoumi and Richard Whitney: duplicate of the listed Elements Behavioral Health ----------------
EBH_SALE = jl.NEWS("elements-behavioral-health", "Advanced Recovery Systems Acquires Promises")
EBH_BK = jl.NEWS("elements-behavioral-health", "Files for Bankruptcy")
L.append(verdict("ebh-holding-company-inc", "member",
    "Same company as the listed member 'elements-behavioral-health': EBH Holding Company is the Long Beach holding company of "
    "Elements Behavioral Health (CEO David Sack on the filing), with Mohamad Makhzoumi listed c/o New Enterprise Associates beside "
    "Frazier Healthcare's directors. Recorded as a member so the row is not left unjudged; identity-merges.json should fold it "
    "into 'elements-behavioral-health'.", ec="site_listing", conf="high", cite=jl.ARCH("elements-behavioral-health")))
L.append(cls("ebh-holding-company-inc", status="acquired", rng="below_1b", city="Long Beach", focus="Healthcare & Bio",
    note="Elements filed for Chapter 11 in May 2018 (" + EBH_BK + ") and BlueMountain Capital bought its assets out of the "
         "bankruptcy that year, relaunching them as Promises Behavioral Health (Behavioral Health Business, 2026: " + EBH_SALE +
         "): a sale out of insolvency, so acquired with that successor."))

# ---------------- single-person rows ----------------
out("faraday-future-intelligent-electric-inc", "The Xiao Jiang on Faraday Future's 2026 filings is a director of a listed EV "
    "maker, not Xiaodong Jiang of NEA (Beijing), who appears on NEA's team pages only in 2013; no NEA fund held Faraday Future "
    "(T4 homonym, X1).")
L.append(verdict("l18-holdings-inc", "member",
    "Same company as the listed member 'lot18': L18 Holdings is Lot18's holding company (founder Philip James on the filing), with "
    "NEA's Tom Grossi listed at the firm's 1954 Greenspring Drive, Timonium address; NEA's archived list carries Lot18 from 2011. "
    "Recorded as a member so the row is not left unjudged; identity-merges.json should fold it into 'lot18'.",
    ec="site_listing", conf="high", cite=jl.ARCH("lot18")))
LOT = jl.W("Lot18")
L.append(cls("l18-holdings-inc", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=LOT,
    stage_conf="high", entry_date="2011-05", city="New York", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    rounds=[rnd("2011-05", "Series B", 10000000, "New Enterprise Associates", True, LOT, "press"),
            rnd("2011-11", "Series C", 30000000, "Accel Partners", True, LOT, "press")],
    note="Lot18 (wine flash sales, New York). NEA led the $10M Series B in May 2011 (Wikipedia), the entry, so the band's Series A "
         "reading is disputed; status defunct aligned with the Accel row."))
out("new-relic-inc", "Hilarie Koplow-McAdams is an executive officer of New Relic on its 2015 filing (its president), an operator "
    "role before she became an NEA venture partner in 2018 (team pages), and no NEA fund held New Relic (T4).")
out("qurrent-inc", "Melissa Taunton appears on NEA's team pages only to 2023 and not on the live team; her seat on Qurrent's 2026 "
    "filing came with the $15M Series A led by Cervin Ventures with Streamlined Ventures (Ventureburn, 2026-03-12), which names no "
    "NEA fund, and no NEA listing, post or filing names Qurrent (T4, next-firm seat).",
    cite="https://ventureburn.com/qurrent-raises-15m/")
out("spark-therapeutics-inc", "Elliott Sigal, an NEA venture partner and senior advisor (team pages 2014-2019), is an independent "
    "director of Spark; its registration statement names NEA only in his biography and lists no NEA fund among holders, so no NEA "
    "fund held the position (D4).", cite=jl.FTS("Spark Therapeutics", "S-1"))
L.append(verdict("stable-coin-inc", "member",
    "Same company as the listed member 'brale': Stable Coin Inc. (Des Moines, executives Ben Milne and Jeff Milewski) is Brale's legal "
    "entity, and its 2024 filing lists NEA's Alex Sharata, Brale's NEA deal team on the firm's page, as director. Recorded as a "
    "member so the row is not left unjudged; identity-merges.json should fold it into 'brale'.",
    ec="site_listing", conf="high", cite=jl.SITE("brale")))
LSV = "https://lsvp.com/company/brale/"
L.append(cls("stable-coin-inc", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
    stage_cite=jl.SITE("brale"), stage_conf="medium", entry_date="2022", grad="graduated", grad_src="web_verified",
    grad_cite=LSV, grad_conf="medium", city="Des Moines", focus="Crypto & Web3", flags=["stage_disputes_band"],
    rounds=[rnd("2022", "Seed", None, None, True, jl.SITE("brale"), "firm"),
            rnd("2025", "Series A", None, None, False, LSV, "firm")],
    note="Brale (stablecoin issuance, Des Moines, founded 2022): the firm's own page labels NEA's 2022 entry Seed, so the band's "
         "2024 date is a later filing; Lightspeed's page records a 2025 Series A, which graduates the seed. Momentum check "
         "2026-09-30 (one Google News query): no priced round at $1B or more."))
L.append(verdict("unite-genomics-inc", "member",
    "Pete Sonsini, an NEA general partner in 2018 (team pages 2008-2023), is the one outside director of record on Unite Genomics' "
    "November 2018 financing filing ($5.8M sold of $6.2M); the company resolves to the Foster City, CA genomics data company that filed "
    "again in 2023. The in-tenure seat is the adjudicated pattern, flagged for the A/B pass (vendor profiles also list NEA, a "
    "lead only).", ec=FD, conf="medium", cite=SEC + "1760629/000176062918000001/0001760629-18-000001-index.htm"))
L.append(cls("unite-genomics-inc", status="private", rng="below_1b", stage="undetermined", entry_date="2018-11",
    city="Foster City", city_src="formd_address", focus="Healthcare & Bio",
    rounds=[rnd("2018-11-21", "unnamed (Form D)", 5782499, None, True,
                SEC + "1760629/000176062918000001/0001760629-18-000001-index.htm", "filing")],
    note="Genomics data company in Foster City, CA; the November 2018 filing (first on record) names no round, so the entry stays "
         "undetermined; a 2023 filing shows it still raising."))
out("viuhealth-inc", "Emily Zhen left NEA in 2023 to become a principal at Zeal Capital Partners (Zeal's own team page; the "
    "Business Wire announcement of 2023-08-30); her seat on ViuHealth's October 2023 filing (formerly Drugviu) is Zeal's, and no "
    "NEA listing, post or filing names ViuHealth (T4, next-firm seat).",
    cite="https://www.zealcapitalpartners.com/emily-zhen/")

jl.write("m3b", L)
