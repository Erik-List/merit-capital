"""PRO-75 GV, judge j5: classification of queue batch 5 (45 member rows, eqrx .. gravity).

Pattern copied from judgments-pilot.py: one cls() per row, citations read from disk through the judge_lib helpers
(POST, CASE, W, FTS, NEWS, SITE) or taken from a page a tool printed and the judge read (WebFetch/WebSearch/curl).
Rounds found are persisted as funding_rounds (COLLECTION.md s6, PRO-143). Run: NQ_TAG=j5 python3 judgments-j5.py
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, CASE, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.CASE, jl.SITE,
                                                           jl.ARCH, jl.W, jl.NEWS, jl.FTS)
L = []
WV = {"valuation_range_source": "web_verified"}
TODAY = "2026-09-28"


def mcap(t):
    return f"https://stockanalysis.com/stocks/{t}/market-cap/"


# ---------------------------------------------------------------- eqrx
EQRX_S1 = FTS("EQRx", "S-1")
L.append(cls(
    "eqrx", country="US", city="Cambridge", focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=EQRX_S1, entry_date="2019-10-02",
    note="Lower-cost medicines (Cambridge, MA). GV 2019, L.P. bought a $5.0M convertible note on 2019-10-02 that "
         "converted into Series A preferred on 2020-01-10, when EQRx sold $218.0M of Series A for cash plus the "
         "conversion of the $22.0M of October 2019 notes (the S-1 of 2021-12-21, certain transactions); the record "
         "counts the notes inside the Series A, and the firm's own post says 'GV invested straight away' at the January "
         "2020 launch. Series B revealed 2021-01-11 (the firm's post). Public through the CM Life Sciences III merger "
         "(December 2021), then acquired by Revolution Medicines in an all-stock deal in 2023 (the firm's exit line; "
         "decisions D11 keeps Revolution Medicines out and EQRx the member). The a16z row reads Growth (model) though "
         "a16z's AH Bio Fund II bought the same notes.",
    rounds=[rnd("2019-10-02", "Convertible notes (converted into Series A)", 22000000, None, True, EQRX_S1, "filing"),
            rnd("2020-01-10", "Series A", 218000000, None, True, EQRX_S1, "filing"),
            rnd("2021-01-11", "Series B", None, None, None, POST("eqrx-affordable-medicine"), "firm")]))

# ---------------------------------------------------------------- ethos
L.append(cls(
    "ethos", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    rng="1b_plus", usd=2180000000, val_src="web_verified", val_cite=mcap("life"), asof=TODAY, extra=WV,
    flags=["model_disputes_source"],
    note="Life insurance platform. Principal executive offices at 90 New Montgomery Street, San Francisco (the 10-K for "
         "2025, filed 2026-03-17: https://www.sec.gov/Archives/edgar/data/1788451/000119312526108887/life-20251231.htm, "
         "and the S-1 of 2025-09-26); the Accel and General Catalyst rows read Austin, the Sequoia row San Francisco. "
         "Value disputed: the prefilled $351.8M is the S-1 cover's float, not a value; public on Nasdaq (LIFE) since "
         "the January 2026 IPO, market cap $2.18B on 2026-09-28 (stockanalysis), fresher than the siblings' $2.42B of "
         "2026-09-03 (same band)."))

# ---------------------------------------------------------------- evelo-biosciences
EVELO_B = NEWS("evelo-biosciences", "Series B Financing and Expansion")
EVELO_S1 = "https://www.sec.gov/Archives/edgar/data/1694665/000119312518116927/d568134ds1.htm"
L.append(cls(
    "evelo-biosciences", status="defunct", country="US", city="Cambridge", focus="Healthcare & Bio", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=EVELO_B, entry_date="2017-07-11",
    flags=["model_disputes_source"],
    note="Microbiome medicines (Cambridge, MA; Flagship Pioneering founded it). The company's release of 2017-07-11 "
         "names GV among the investors in the $50M Series B beside founder Flagship, Celgene, Mayo Clinic and "
         "Alexandria; the S-1 shows Flagship bought 93% to 100% of each earlier series (Series A to A-3, 2015-2016) and "
         "dates the Series B sales 2017-01-05 to 2018-01-30, and GV 2016 and GV 2017 sign its 2018 investors' rights "
         "agreement, so the Series B is GV's entry. Nasdaq IPO in 2018 (EVLO). Status disputed: the prefill read "
         "acquired, but on 2023-11-22 the board found dissolution the only viable option and the company wound down "
         "with no buyer (Fierce Biotech: " + NEWS("evelo-biosciences", "dissolution is only viable") + "), so defunct.",
    rounds=[rnd("2016-06-16", "Series A-3", 10500000, None, False, EVELO_S1, "filing"),
            rnd("2017-07-11", "Series B", 50000000, None, True, EVELO_B, "company"),
            rnd("2018-02-09", "Series C", 81500000, None, None, EVELO_S1, "filing")]))

# ---------------------------------------------------------------- everyone-medicines
L.append(cls(
    "everyone-medicines", status="defunct", country="US", city="Boston", city_src="web_verified",
    focus="Healthcare & Bio", rng="below_1b", stage="undetermined",
    note="Personalized genetic medicines for ultra-rare disease, Boston-based (BioSpace, 2026-04-30: "
         + NEWS("everyone-medicines", "6 biotechs that called it quits") + "). Shut down in early March 2026 "
         "(Endpoints News, 2026-03-04: " + NEWS("everyone-medicines", "EveryOne Medicines shuts down") + "). "
         "Khosla Ventures was a founding investor (BioSpace, 2024-08-07); no source read names GV's round (the WSJ "
         "profile of 2024-04-25 and the July 2024 CEO release could not be read), so the stage is undetermined; the "
         "firm lists it from 2024 with Anthony Philippakis and Issi Rozen. The Khosla row still reads private in South "
         "San Francisco; the shutdown and Boston are the fresher cited facts.",
    rounds=[]))

# ---------------------------------------------------------------- evident-io
EVIDENT_VB = NEWS("evident-io", "raises $22 million led by GV")
L.append(cls(
    "evident-io", status="acquired", country="US", city="Pleasanton", city_src="web_verified", focus="Security",
    rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=EVIDENT_VB,
    entry_date="2017-02-09",
    note="Cloud infrastructure security (Pleasanton, CA). GV led the $22M round of February 2017 as a new investor, "
         "with existing investors Bain Capital, True Ventures and Venrock following; total funding $49M since 2013 "
         "(VentureBeat, 2017-02-09); ReadITQuik's headline names it the Series C. Palo Alto Networks bought it for "
         "$300M in cash, announced 2018-03-14 ('a privately held company based in Pleasanton, Calif.', "
         "https://paloaltonetworks.com/company/press/2018/palo-alto-networks-announces-intent-to-acquire-evident-io). "
         "The BCV row reads Dublin from knowledge; the acquirer's release gives Pleasanton.",
    rounds=[rnd("2017-02-09", "Series C", 22000000, "GV", True, EVIDENT_VB, "press")]))

# ---------------------------------------------------------------- farmwise
FW_B = NEWS("farmwise", "haul in $45m Series B")
L.append(cls(
    "farmwise", status="acquired", country="US", city="San Francisco", focus="Industrial & Robotics", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FW_B, entry_date="2022-04",
    note="AI weeding robots (San Francisco). GV came in as a new investor in the $45M Series B co-led by Fall Line "
         "Capital and Middleland Capital (AgFunderNews, 2022-06-01); the firm's own /ai list dates the investment April "
         "2022 (the entry date, decisions D7) and a re-investment April 2023. FarmWise announced a restructuring and "
         "wind-down in March 2025 and Taylor Farms bought FarmWise's business on 2025-04-04 (Taylor Farms' release: "
         + NEWS("farmwise", "Taylor Farms Announces Acquisition of FarmWise") + "), so acquired, a sale out of a "
         "wind-down. The Felicis row also reads acquired but names Toro; Taylor Farms is the buyer on record.",
    rounds=[rnd("2022-06-01", "Series B", 45000000, "Fall Line Capital; Middleland Capital", True, FW_B, "press")]))

# ---------------------------------------------------------------- flatiron-health
L.append(cls(
    "flatiron-health", status="acquired", city="New York", rng="below_1b", focus="Healthcare & Bio",
    note="Oncology data platform (New York; 291 Broadway on its 2014 Form D). Roche bought it for $1.9B in 2018 "
         "(the firm's exit line, 'Acquired by Roche, 2018'), so acquired and no figure."))

# ---------------------------------------------------------------- forty-seven
FS_S1 = FTS("Forty Seven", "S-1")
FS_PR = ("https://www.prnewswire.com/news-releases/forty-seven-inc-completes-75m-series-a-financing-and-licenses-"
         "technology-from-stanford-university-to-advance-next-generation-immuno-oncology-programs-300225001.html")
L.append(cls(
    "forty-seven", country="US", city="Menlo Park", focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FS_S1, entry_date="2016-02-24",
    note="Anti-CD47 immuno-oncology (Menlo Park; 1490 O'Brien Drive on the S-1). The company's release of 2016-02-24 "
         "names GV among the participants in the $75M Series A led by Lightspeed and Sutter Hill (" + FS_PR + "); the "
         "S-1 (2018-06-01) lists GV's purchases of 4,000,000 Series A-1 shares (sold November 2015 and February to "
         "April 2016; the December 2015 share count is taken up by Lightspeed, Sutter Hill and Clarus, so GV's came in "
         "the 2016 closings), 4,016,666 Series A-2 and 3,964,575 Series B. Status acquired as prefilled (the Sutter Hill "
         "and Lightspeed rows cite Gilead's 2020 purchase); the firm's exit line 'NASDAQ: FTSV' is the pre-acquisition "
         "state (decisions D8).",
    rounds=[rnd("2015-11", "Series A-1", 34400000, "Lightspeed Venture Partners; Sutter Hill Ventures", True, FS_S1,
                "filing"),
            rnd("2017-02", "Series A-2", 40400000, None, True, FS_S1, "filing"),
            rnd("2017-10", "Series B", 75000000, None, True, FS_S1, "filing")]))

# ---------------------------------------------------------------- foundation-medicine
L.append(cls(
    "foundation-medicine", city="Boston", city_src="web_verified", rng="below_1b", focus="Healthcare & Bio",
    note="Cancer genomic profiling. Roche bought the remaining 42.5% in 2018 and runs it as a subsidiary; in 2024 the "
         "company moved its headquarters from Cambridge to a new tower in Boston's Seaport District (Wikipedia: "
         + W("Foundation Medicine") + "), so Boston is the current HQ. Acquired, no figure."))

# ---------------------------------------------------------------- freenome
FN_TC = "https://techcrunch.com/2017/03/01/in-liquid-biopsy-race-freenome-lands-65-million-led-by-andreessen-horowitz"
L.append(cls(
    "freenome", status="public", country="US", city="South San Francisco", focus="Healthcare & Bio",
    rng="1b_plus", usd=1740000000, val_src="web_verified", val_cite=mcap("frnm"), asof=TODAY, extra=WV,
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FN_TC, entry_date="2017-02",
    note="Blood-based cancer screening (South San Francisco). GV joined the $65M Series A led by Andreessen Horowitz "
         "(TechCrunch, 2017-03-01); the earlier $5.5M seed was a16z-led, with Data Collective and Founders Fund the "
         "named earlier backers, not GV. The firm's own /ai list dates GV's first investment February 2017 (the entry "
         "date, decisions D7) and re-investments in 2019, 2020 and 2021. Public on Nasdaq (FRNM) after its 2026 listing "
         "(The Business Journals, 2026-07-27: 'Freenome went public for $300 million'); market cap $1.74B on 2026-09-28 (stockanalysis), fresher than "
         "the a16z row's $1.5B of August 2026 (same band).",
    rounds=[rnd("2016", "Seed", 5500000, "Andreessen Horowitz", False, FN_TC, "press"),
            rnd("2017-03-01", "Series A", 65000000, "Andreessen Horowitz", True, FN_TC, "press")]))

# ---------------------------------------------------------------- gametime
GT_W = W("Gametime")
GT_SI = NEWS("gametime", "raises $20 million in Series B")
L.append(cls(
    "gametime", status="private", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GT_SI,
    entry_date="2016-09-23",
    note="Mobile ticket marketplace (Gametime United, San Francisco). Accel led the 2014 seed and the $13.3M Series A "
         "of May 2015 (Wikipedia); GV came in as a new investor, with Evolution Media Partners and the StartX fund, in "
         "the $20M Series B, Accel following (Sports Illustrated, 2016-09-23; Wikipedia agrees). GV also joined the $30M "
         "round of May 2022 (Wikipedia); no $1B mark on record, so below_1b.",
    rounds=[rnd("2015-05", "Series A", 13300000, "Accel", False, GT_W, "press"),
            rnd("2016-09-23", "Series B", 20000000, None, True, GT_SI, "press"),
            rnd("2022-05", "Unnamed", 30000000, None, True, GT_W, "press")]))

# ---------------------------------------------------------------- firsthand
L.append(cls(
    "firsthand", status="private", city="New York", city_src="formd_address", rng="below_1b",
    focus="Healthcare & Bio",
    note="Serious mental illness care (FirstHand Health, New York; 205 Hudson Street on its 2021 and 2023 Form Ds). "
         "GV put $28.1M into the Series B of February 2023, and the company raised $10M of a $32M round in 2026 after "
         "cutting staff in March 2025 (Behavioral Health Business, 2026-07-22: "
         + NEWS("firsthand", "Secures Portion of $30M+") + "); operating, so private and below_1b. Not the "
         "Y Combinator row's firsthand, a different company."))

# ---------------------------------------------------------------- fyto
L.append(cls(
    "fyto", status="private", city="Petaluma", city_src="formd_address", rng="below_1b",
    focus="Industrial & Robotics",
    note="Robotic farming of aquatic plants for feed protein (FYTO, Inc.; 121 H Street, Petaluma on its 2023 Form D). "
         "GV led the $15M Series A (AgFunderNews, 2022-07-07: " + NEWS("fyto", "Fyto lands $15m") + "), which agrees "
         "with the prefilled Series A; the 2023 Form D ($18M, first sale 2022-04-06) is the latest filing and its site "
         "still operates, so private and below_1b."))

# ---------------------------------------------------------------- genomics-medicine-ireland
GMI_A = NEWS("genomics-medicine-ireland", "GMI Raises $40 Million in Series A")
L.append(cls(
    "genomics-medicine-ireland", status="acquired", country="IE", country_src="web_verified", country_cite=GMI_A,
    city="Dublin", city_src="web_verified", focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GMI_A, entry_date="2016-10-27",
    note="Population genomics research company (Dublin). Its $40M (EUR 36M) Series A came from the Ireland Strategic "
         "Investment Fund, ARCH Venture Partners, Polaris Partners and GV (Technology Networks, 2016-10-27). The firm's exit line reads 'Acquired by Wuxi Nextcode, 2018'; acquired, "
         "no figure.",
    rounds=[rnd("2016-10-27", "Series A", 40000000, None, True, GMI_A, "press")]))

# ---------------------------------------------------------------- grail
GRAIL_PR = ("https://grail.com/press-releases/grail-hires-google-executive-jeff-huber-as-ceo-to-lead-development-for-"
            "early-cancer-detection/")
GRAIL_B = ("https://grail.com/press-releases/grail-closes-over-900-million-initial-investment-in-series-b-financing-to-"
           "develop-blood-tests-to-detect-cancer-early/")
L.append(cls(
    "grail", country="US", city="Sunnyvale", city_src="web_verified", focus="Healthcare & Bio",
    rng="1b_plus", usd=5920000000, val_src="web_verified", val_cite=mcap("gral"), asof=TODAY, extra=WV,
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GRAIL_PR, entry_date="2016-02-10",
    flags=["model_disputes_source"],
    note="Multi-cancer early detection. GRAIL's own release of 2016-02-10: 'The company secured over $100 million in "
         "Series A financing from Illumina, Inc. and ARCH Venture Partners, with participating investors including "
         "Bezos Expeditions, Bill Gates, Sutter Hill Ventures, and GV'; GV 2015, L.P. also signs the 2019 investors' "
         "rights agreement. The Series B release (2017-03-01) names no GV. Illumina bought GRAIL in 2021 and spun it off "
         "in June 2024 (Nasdaq: GRAL). Value updated: market cap $5.92B on 2026-09-28 (stockanalysis) replaces the "
         "prefilled $1.9B, aligned with the Sutter Hill row. HQ Sunnyvale: EDGAR's business address is 250 S. Mathilda "
         "Avenue, Sunnyvale, and the 10-Q for the quarter to 2026-06-30 describes the lease for the 'new corporate "
         "headquarters in Sunnyvale, California' (the cover still gives Menlo Park).",
    rounds=[rnd("2016-01", "Series A", 100000000, "Illumina; ARCH Venture Partners", True, GRAIL_PR, "company"),
            rnd("2017-03-01", "Series B", 900000000, "ARCH Venture Partners", None, GRAIL_B, "company")]))

# ---------------------------------------------------------------- fullstory
FS_17 = "https://www.sec.gov/Archives/edgar/data/1614167/000161416717000002/0001614167-17-000002-index.htm"
FS_D = NEWS("fullstory", "$100 Million Investment at $1.8 Billion Valuation")
FS_C = NEWS("fullstory", "Closes $32M Series C")
L.append(cls(
    "fullstory", status="private", city="Atlanta", focus="SaaS",
    rng="1b_plus", usd=1800000000, val_src="web_verified", val_cite=FS_D, asof="2021-08-04", extra=WV,
    stage="Growth", stage_src="formd_structural", stage_conf="high", stage_cite=FS_17, flags=["stale"],
    note="Digital experience analytics (Atlanta). GV's first seat is Karim Faris as a director on the Form D for the "
         "$15.0M round first sold 2017-05-04, the company's third filing after the 2014 ($1.5M) and 2015 ($10.7M) "
         "rounds; Hypepotamus (2019-04-24) names those rounds 'a Series A of $10 million and a Series B of $15 million' "
         "and lists GV as an existing investor in the $32M Series C led by Stripes. So the entry is the 2017 Series B, "
         "Growth (two earlier filings; the withheld Series A band read the round size). Mark: the $103M Series D led by "
         "Permira at a $1.8B valuation (the company's release, 2021-08-04, GV participating), stale past 24 months; no "
         "later priced round or collapse evidence found.",
    rounds=[rnd("2015-05-04", "Series A", 10000000, None, False, jl.FORMD_CITE("fullstory", 3), "filing"),
            rnd("2017-05-04", "Series B", 15000000, None, True, FS_17, "filing"),
            rnd("2019-04-24", "Series C", 32000000, "Stripes", True, FS_C, "press"),
            rnd("2021-08-04", "Series D", 103000000, "Permira", True, FS_D, "company")]))

# ---------------------------------------------------------------- flock-freight
FF_D = NEWS("flock-freight", "reaches unicorn status with Series D")
FF_B = NEWS("flock-freight", "Announces $50M Series B")
L.append(cls(
    "flock-freight", status="private", country="US", city="Encinitas", city_src="web_verified",
    focus="Industrial & Robotics",
    rng="1b_plus", usd=1300000000, val_src="web_verified", val_cite=FF_D, asof="2021-10-20", extra=WV,
    stage="undetermined", flags=["stale"],
    note="Shared-truckload freight (Encinitas, CA per Business of San Diego, 2025-07-10; Solana Beach in 2020). The "
         "firm first lists it in 2020. The $50M Series B release led by SignalFire and GLP (2020-02-25) calls the "
         "company 'backed by SignalFire, GLP, Google Ventures', and FreightWaves names GV an existing investor in the "
         "$215M Series D led by SoftBank Vision Fund 2 'that landed it a $1.3 billion valuation' (2021-10-20); no "
         "source read names the round GV entered, so the stage is undetermined. Mark $1.3B (Series D), stale: the $60M "
         "Series E led by O'Neil Strategic Capital (FreightWaves, 2025-05-14) disclosed no valuation, and the PitchBook "
         "figure quoted by Business of San Diego is a vendor estimate (Rule A).",
    rounds=[rnd("2020-02-25", "Series B", 50000000, "SignalFire; GLP Capital Partners", None, FF_B, "company"),
            rnd("2020-12-01", "Series C", 113500000, "SoftBank", True, NEWS("flock-freight", "completes $113.5M Series C"), "press"),
            rnd("2021-10-20", "Series D", 215000000, "SoftBank Vision Fund 2", True, FF_D, "press"),
            rnd("2025-05-14", "Series E", 60000000, "O'Neil Strategic Capital", None,
                NEWS("flock-freight", "hauls in $60M Series E"), "press")]))

# ---------------------------------------------------------------- gate-bioscience
GATE_A = ("https://www.prnewswire.com/news-releases/gate-bioscience-emerges-from-stealth-and-introduces-molecular-"
          "gates-a-new-class-of-small-molecule-therapeutics-301972954.html")
GATE_B = ("https://www.gatebio.com/gate-bioscience-announces-65-million-oversubscribed-series-b-financing-to-advance-"
          "oral-molecular-gate-medicines-into-the-clinic")
L.append(cls(
    "gate-bioscience", status="private", country="US", city="Brisbane", city_src="web_verified",
    focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GATE_A, entry_date="2023-11-01",
    note="Small-molecule 'molecular gate' medicines (Brisbane, CA: the dateline and its site's address). GV "
         "participated in the $60M Series A led by Versant Ventures and a16z Bio + Health with ARCH (the company's "
         "release on emerging from stealth, 2023-11-01), and in the $65M Series B led by Forbion (2025-11-13). The a16z "
         "row reads South San Francisco from knowledge.",
    rounds=[rnd("2023-11-01", "Series A", 60000000, "Versant Ventures; a16z Bio + Health", True, GATE_A, "company"),
            rnd("2025-11-13", "Series B", 65000000, "Forbion", True, GATE_B, "company")]))

# ---------------------------------------------------------------- genesis
GEN_SA = NEWS("genesis", "raises $45M to expand globally")
L.append(cls(
    "genesis", status="private", country="GB", country_src="web_verified", country_cite=GEN_SA, city="London",
    city_src="web_verified", focus="SaaS", rng="below_1b",
    extra={**WV, "valuation_citation": "https://genesis.global/company/", "is_public": False, "public_since": None,
           "valuation_asof": None, "valuation_source": None, "valuation_confidence": None},
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GEN_SA, entry_date="2021-03-15",
    flags=["model_disputes_source"],
    note="Genesis Global (genesis.global), a low-code platform for financial markets firms. Status disputed: the "
         "prefilled acquired, and the public-float fields cleared here, came from another company's filings (a weak "
         "CIK join); the company's own page (https://genesis.global/company/) shows it "
         "independent, headquartered at 36 Leadenhall Street, London, with offices in New York and Bangalore, and "
         "SiliconANGLE (2021-03-15) calls it U.K.-based, which confirms GB. GV's entry is the $45M Series B led by "
         "Accel with GV, Salesforce Ventures, Citi, Illuminate Financial and Tribeca (SiliconANGLE); the earlier Series "
         "A (GBP 3M, 2019) and A+ ($1.8M, 2020) do not name GV. The Business Journals (2022-06-01) called it "
         "Miami-based, the Accel row's city; the company's own page gives London. Momentum check 2026-09-28: Google News shows no priced round after the $200M Series C of "
         "2022, which disclosed no valuation; below_1b.",
    rounds=[rnd("2019", "Series A", None, None, False, "https://genesis.global/company/", "company"),
            rnd("2020", "Series A+", 1800000, None, False, "https://genesis.global/company/", "company"),
            rnd("2021-03-15", "Series B", 45000000, "Accel", True, GEN_SA, "press"),
            rnd("2022", "Series C", 200000000, None, None, "https://genesis.global/company/", "company")]))

# ---------------------------------------------------------------- genie-ai
GENIE_A = NEWS("genie-ai", "raises £13.3m Series A led by Google Ventures")
GENIE_EU = NEWS("genie-ai", "London-based Genie AI raises")
L.append(cls(
    "genie-ai", status="private", country="GB", country_src="web_verified", country_cite=GENIE_EU, city="London",
    city_src="web_verified", focus="AI & Applied AI", rng="below_1b", extra={**WV, "valuation_citation": GENIE_A},
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GENIE_A, entry_date="2024-02",
    note="AI legal assistant (London: EU-Startups' headline 'London-based Genie AI raises EUR 16 million'). GV led the "
         "GBP 13.3M Series A ($17.8M) with Khosla Ventures joining (Legal IT Insider, 2024-10-23); the earlier GBP 2M "
         "of 2019 included a UKRI grant and does not name GV. The firm's own /ai list dates GV's investment February "
         "2024 (the entry date, decisions D7); the round was announced in October. Momentum check 2026-09-28: Google "
         "News finds no round after the October 2024 Series A; below_1b.",
    rounds=[rnd("2019", "Seed", None, None, False, GENIE_A, "press"),
            rnd("2024-10-23", "Series A", 17800000, "GV", True, GENIE_A, "press")]))

# ---------------------------------------------------------------- genome-medical
GM_C = NEWS("genome-medical", "Completes $60M Series C")
L.append(cls(
    "genome-medical", status="private", country="US", city="South San Francisco", city_src="web_verified",
    focus="Healthcare & Bio", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GM_C, entry_date="2021-08-31",
    note="Genetics care and telegenomics practice (South San Francisco). Casdin Capital led the $60M Series C 'joined "
         "by new investors GV (formerly Google Ventures) and Amgen Ventures' (Inside Precision Medicine, 2021-08-31), "
         "with the GeneMatters acquisition; the earlier Series A (2017) and $14M round (2020) do not name GV. Operating "
         "(its own site, copyright 2026), so private; no $1B mark.",
    rounds=[rnd("2021-08-31", "Series C", 60000000, "Casdin Capital", True, GM_C, "press")]))

# ---------------------------------------------------------------- gitlab
L.append(cls(
    "gitlab", country="US", city="San Francisco", city_src="web_verified", focus="DevTools & APIs",
    rng="1b_plus", usd=7700000000, val_src="web_verified", val_cite=mcap("gtlb"), asof=TODAY, extra=WV,
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=CASE("gitlab"), entry_date="2017-09",
    flags=["model_disputes_source"],
    note="DevOps platform. The S-1 says it is remote-only and keeps no headquarters; EDGAR's business and mailing "
         "address is 268 Bush Street, San Francisco, the siblings' reading too. The firm's own "
         "case study gives GitLab's first round with GV as the Series C (Date Invested 2017), and its IPO post says GV "
         "led the $20M Series C (TechCrunch, 2017-10-09); the /ai list dates the investment September 2017. GV 2017, "
         "L.P. also bought Series D preferred in 2018 (the 2021 DRS, certain transactions). Value updated: market cap "
         "$7.7B on 2026-09-28 (stockanalysis) replaces the prefilled $6.37B float; the Coatue and General Catalyst rows "
         "carry $7.81B at 2026-09-25 (same band).",
    rounds=[rnd("2017-10-09", "Series C", 20000000, "GV", True, NEWS("gitlab", "GitLab raises $20M Series C round led by GV"),
                "press"),
            rnd("2018-09", "Series D", 100000000, None, True, FTS("Gitlab", "DRS"), "filing")]))

# ---------------------------------------------------------------- glass-imaging
GL_TC = "https://techcrunch.com/2024/02/08/glass-supercharges-smartphone-cameras-with-ai-minus-the-hallucinations/"
GL_A = NEWS("glass-imaging", "AI Imaging Technologies - PR Newswire")
L.append(cls(
    "glass-imaging", status="private", country="US", city="Los Altos", city_src="web_verified",
    focus="AI & Applied AI", rng="below_1b", extra={**WV, "valuation_citation": GL_A},
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GL_TC, entry_date="2023-06",
    grad="graduated", grad_src="web_verified", grad_cite=GL_A, grad_conf="high",
    note="AI image processing for smartphone cameras (Los Altos, CA: its site and The Next Web). GV led the $9.3M "
         "'extended seed' with Future Ventures, Abstract Ventures and LDV Capital (TechCrunch, 2024-02-08; the seed "
         "itself was 2021); the firm's own /ai list dates the investment June 2023 (the entry date, decisions D7). "
         "Graduated: Insight Partners led the $20M Series A with GV, Future Ventures and Abstract Ventures as earlier "
         "investors (the company's release, 2025-05-12). The WSJ reported on 2026-09-14 that OpenAI bought the company "
         "for more than $300M; neither company had announced it (The Next Web, 2026-09-15: "
         + NEWS("glass-imaging", "WSJ reports") + "), so the row stays private until the sale is confirmed. "
         "Momentum check 2026-09-28: no $1B round; the reported price and the 2025 round's reported $100M value are "
         "below $1B.",
    rounds=[rnd("2021", "Seed", None, None, False, GL_TC, "press"),
            rnd("2024-02-08", "Seed extension", 9300000, "GV", True, GL_TC, "press"),
            rnd("2025-05-12", "Series A", 20000000, "Insight Partners", True, GL_A, "company")]))

# ---------------------------------------------------------------- gocardless
GOC_BI = NEWS("gocardless", "How Hiroki Takeuchi Built")
L.append(cls(
    "gocardless", status="acquired", city="London", rng="below_1b", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=GOC_BI, entry_date="2019-02",
    note="Bank payments network (London). Mollie completed its purchase of GoCardless on 2026-09-01 (Demócrata: "
         + NEWS("gocardless", "Mollie closes the purchase") + "), agreed in December 2025 for about EUR 1.05B, "
         "mostly in stock (Wikipedia), so acquired and no figure; aligned with the Balderton and BCV rows (the Accel and "
         "Y Combinator rows still read private at $2.1B). Entry re-dated, stage unchanged: the prefilled Growth dated "
         "2020-12-15 reads Tom Hulme's first Form D seat, but 'GoCardless' recent $75 million raise included backing "
         "from GV' (Business Insider, 2019-03-30), the round of the February 2019 Form D (first sale 2019-02-07), the "
         "company's fifth filing after the 2012, 2013, 2016 and 2017 rounds, so Growth. Wikipedia's line that Google "
         "Ventures joined the 2012 round is not borne out: Balderton's post on the $7M Series B (2014-01-28) names only "
         "Accel and Passion as existing investors, and the firm's own listings carry GoCardless only from 2019.",
    rounds=[rnd("2014-01-28", "Series B", 7000000, "Balderton Capital", False,
                "https://www.balderton.com/news/gocardless-raises-7m-from-balderton-capital-to-expand-development-team/",
                "press"),
            rnd("2019-02-07", "Series E", 75499981, None, True, GOC_BI, "press"),
            rnd("2020-12-15", "Series F", 95000018, None, True, jl.FORMD_CITE("gocardless", 7), "filing")]))

# ---------------------------------------------------------------- flexport
FX_BI = NEWS("flexport", "Uber for the Oceans")
FX_A = NEWS("flexport", "Peter Thiel Leads $20M Series A")
FX_E = "https://www.flexport.com/blog/flexport-raises-935-million-to-boost-resilience-and-visibility-in-supply-chains/"
L.append(cls(
    "flexport", city="San Francisco", focus="Industrial & Robotics",
    rng="1b_plus", usd=8000000000, val_src="web_verified", val_cite=FX_E, asof="2022-02-07", extra=WV,
    flags=["stale", "model_disputes_source"], clear=["unicorn_name_match"],
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FX_BI, entry_date="2015-05",
    grad="graduated", grad_src="web_verified", grad_cite=FX_A, grad_conf="high",
    note="Freight forwarding platform (San Francisco; Y Combinator). 'Flexport has raised $6.6 million in funding, some "
         "of which has come from the likes of Google Ventures' (Business Insider, 2015-05-11, citing Bloomberg): the "
         "seed, all of the company's capital before its Series A. Graduated: Peter Thiel of Founders Fund led the $20M "
         "Series A with 'existing investors ... First Round Capital ... Google Ventures ... Y Combinator' joined by new "
         "ones (the company's post, 2015-08-07; $26.6M raised in all). Mark re-sourced from the unicorn list (an "
         "aggregator, Rule A) to the company's own post: the $935M Series E led by Andreessen Horowitz and MSD Partners "
         "'at a new valuation of $8 billion' (2022-02-07), stale past 24 months; The Loadstar's headline (2025-04-01) "
         "says Flexport is 'losing value', but no priced tender or secondary below the mark was found. Aligned with the "
         "Felicis and 8VC rows.",
    rounds=[rnd("2015-05", "Seed", 6600000, None, True, FX_BI, "press"),
            rnd("2015-08-07", "Series A", 20000000, "Founders Fund", True, FX_A, "company"),
            rnd("2022-02-07", "Series E", 935000000, "Andreessen Horowitz; MSD Partners", None, FX_E, "company")]))

# ---------------------------------------------------------------- firefly
FFY_A = NEWS("firefly", "Firefly raises $30M To Place Digital Ads")
FFY_Y = NEWS("firefly", "Launch in Colombia")
L.append(cls(
    "firefly", status="private", country="US", country_src="web_verified", country_cite=FFY_Y, city="New York",
    city_src="web_verified", focus="Media, Gaming & Advertising", rng="below_1b",
    extra={"valuation_source": None, "valuation_confidence": None},
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FFY_A, entry_date="2019-05-30",
    flags=["model_disputes_source"],
    note="Firefly Systems (fireflyon.com), digital out-of-home screens on rideshare and taxi roofs. GV led the $30M "
         "Series A, $51.5M raised in all after a seed on leaving stealth in December 2018 (Crunchbase News, "
         "2019-05-30; San Francisco then). Status and country disputed: the prefilled acquired and MY came from a name "
         "match on 'Firefly' (the Malaysian airline); the company's own release of 2026-08-25 describes an independent "
         "company based in New York City with offices in Los Angeles, Chicago, Las Vegas, London and Istanbul "
         "(Yahoo Finance), so private, US, New York. IHC's Multiply Marketing Consultancy took a minority stake in 2021 "
         "(Arab News). The a16z row's Firefly is unresolved; the a16z firefly-health row is another company.",
    rounds=[rnd("2018-12", "Seed", 21500000, None, False, FFY_A, "press"),
            rnd("2019-05-30", "Series A", 30000000, "GV", True, FFY_A, "press")]))

# ---------------------------------------------------------------- farmers-business-network
FBN_B = NEWS("farmers-business-network", "Seals $15M Funding Deal")
FBN_G = NEWS("farmers-business-network", "valued at $3.9 bln")
FBN_25 = NEWS("farmers-business-network", "raises $50 million to expand AI")
L.append(cls(
    "farmers-business-network", status="private", country="US", city="San Carlos", city_src="web_verified",
    focus="Consumer & Marketplaces",
    rng="1b_plus", usd=3900000000, val_src="web_verified", val_cite=FBN_G, asof="2021-11-18", extra=WV,
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FBN_B, entry_date="2015-05-19",
    flags=["stale"],
    note="Farmer network, input marketplace and farm finance (San Carlos, CA). Google Ventures led the $15M Series B as "
         "a new investor, after a $6M Series A from Kleiner Perkins and a $3M+ A-1 from DBL (AgFunderNews, "
         "2015-05-19). Mark: Reuters' headline 'Farmers Business Network valued at $3.9 bln after Fidelity-led "
         "investment' (2021-11-18, the Series G), stale past 24 months; the $50M raised in July 2025 from backers "
         "including GV and Temasek disclosed no valuation (Digital Commerce 360, 2025-07-28), and no collapse evidence "
         "was found.",
    rounds=[rnd("2015-05-19", "Series B", 15000000, "Google Ventures", True, FBN_B, "press"),
            rnd("2021-11-18", "Series G", None, "Fidelity", None, FBN_G, "press"),
            rnd("2025-07-28", "Unnamed", 50000000, None, True, FBN_25, "press")]))

# ---------------------------------------------------------------- evox-therapeutics
EVX = NEWS("evox-therapeutics", "Partners with Rett Syndrome")
L.append(cls(
    "evox-therapeutics", status="private", country="GB", country_src="web_verified", country_cite=EVX,
    city="Oxford", city_src="web_verified", focus="Healthcare & Bio", rng="below_1b", stage="undetermined",
    note="Exosome-based gene editing medicines (OXFORD, England dateline, BioSpace, 2026-02-26); operating in 2026 "
         "(that partnership release; a board appointment in November 2025), so private, no $1B mark. The firm lists it "
         "from 2018 with Tom Hulme and Vidu Shanmugarajah. No source read names the round GV entered (Google News "
         "searches for its Series B and C found no investor list), so the stage is undetermined.",
    rounds=[]))

# ---------------------------------------------------------------- giphy
GPH_D = NEWS("giphy", "Has Almost No Revenue But Is Worth $600 Million")
L.append(cls(
    "giphy", status="acquired", country="US", city="New York", focus="Media, Gaming & Advertising", rng="below_1b",
    stage="Growth", stage_src="model", stage_conf="medium",
    note="GIF search (New York; Betaworks incubated it in 2013). GV is not in the $2.4M Series A of May 2014 "
         "(Wikipedia lists Quire, CAA, RRE, Lerer Hippeau and Betaworks) nor in the $72M-75M Series D of October 2016 "
         "led by DFJ with IVP and China Media Capital (Fortune, 2016-10-31). Forbes' headline of 2016-10-26 'Giphy "
         "Passes 100 Million Daily Users ... Reveals GV As Investor' (https://www.forbes.com/sites/alexkonrad/2016/10/"
         "26/giphy-passes-100-million-users-reveals-gv-as-investor/; the body could not be read) and a search snippet "
         "of it say GV joined the $55M Series C of February 2016, led by Lightspeed, late. Every round GV could have "
         "joined after the Series A is a Series B or later, so Growth at medium confidence (model). Facebook bought "
         "Giphy in 2020 and sold it to Shutterstock, which completed the purchase on 2023-06-23 (Wikipedia); acquired.",
    rounds=[rnd("2014-05", "Series A", 2400000, None, False, W("Giphy"), "press"),
            rnd("2016-02", "Series C", 55000000, "Lightspeed Venture Partners", None, W("Giphy"), "press"),
            rnd("2016-10-31", "Series D", 72000000, "Draper Fisher Jurvetson", False, GPH_D, "press")]))

# ---------------------------------------------------------------- flapping-airplanes
FA_TC = NEWS("flapping-airplanes", "research-driven AI - TechCrunch")
L.append(cls(
    "flapping-airplanes", status="private", country="US", city="San Francisco", focus="AI & Applied AI",
    rng="below_1b", extra={**WV, "valuation_citation": NEWS("flapping-airplanes", "research-driven AI - TechCrunch")},
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FA_TC, entry_date="2026-01-28",
    grad="censored",
    note="Research-first AI lab (founders Ben and Asher Spector). It launched with a $180M seed from Google Ventures, "
         "Sequoia and Index (TechCrunch, 2026-01-29); the firm's own post of 2026-01-28 says GV co-led 'the initial "
         "funding rounds' with Sequoia, Index and Menlo participating, and its /ai list dates the investment January "
         "2026. Momentum check 2026-09-28: no priced round at $1B or more with a citable figure; Dealroom's $1.5B is a "
         "vendor figure (Rule A) and Forbes (2026-07-31) reports only talks at $5B; below_1b, aligned with the Sequoia "
         "row. City from knowledge (the Menlo row reads San Francisco). Censored: entry under 24 months old.",
    rounds=[rnd("2026-01-28", "Seed", 180000000, "GV; Sequoia Capital", True, FA_TC, "press")]))

# ---------------------------------------------------------------- fathom
FTH = ("https://www.fathomhealth.com/insights/fathom-secures-strategic-investment-from-cvs-health-ventures-to-"
       "accelerate-enterprise-wide-autonomous-coding")
FTH_B = NEWS("fathom", "Fathom Secures $46M for AI Medical Coding")
L.append(cls(
    "fathom", status="private", rng="below_1b", city="San Francisco", city_src="web_verified",
    extra={"is_public": False, "public_since": None, "valuation_asof": None, "valuation_source": None,
           "valuation_range_source": None, "valuation_confidence": None},
    focus="Healthcare & Bio", stage="undetermined", flags=["model_disputes_source"],
    note="Fathom Health (fathomhealth.com), autonomous medical coding, San Francisco. Status disputed: the prefilled "
         "public row and its $21.9M figure are Fathom Holdings (NASDAQ: FTHM), a real estate brokerage; this Fathom is "
         "private and operating, 'backed by ... 8VC, Alkeon Capital, Cedars-Sinai, CVS Health Ventures, Founders Fund, "
         "GV, Lightspeed Venture Partners, and Tarsadia' (its own release, San Francisco, 2026-05-04). GV is not named "
         "in the $46M Series B co-led by Alkeon and Lightspeed ($61M raised in all; HIT Consultant, 2022-11-09) and no "
         "source read names the earlier round GV entered (the firm lists it from 2019), so the stage is undetermined. "
         "Not the AI notetaker Fathom of the Y Combinator row.",
    rounds=[rnd("2022-11-09", "Series B", 46000000, "Alkeon Capital; Lightspeed Venture Partners", False, FTH_B,
                "press"),
            rnd("2026-05-04", "Strategic", None, "CVS Health Ventures", None, FTH, "company")]))

# ---------------------------------------------------------------- fitstar
L.append(cls(
    "fitstar", status="acquired", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    rng="below_1b", stage="undetermined",
    note="Personalized video fitness apps (San Francisco). Fitbit announced it would acquire FitStar on 2015-03-06 "
         "(Pulse 2.0: " + NEWS("fitstar", "Fitbit To Acquire FitStar") + "; Forbes' headline puts the price at "
         "$17.8M), and the firm's exit line reads 'Acquired by Fitbit, 2015'. The firm lists it from 2013 (Kevin Rose, "
         "then Krishna Yeshwant); no source read names the round GV entered (Google News finds no funding coverage), "
         "so the stage is undetermined.",
    rounds=[]))

# ---------------------------------------------------------------- framed
L.append(cls(
    "framed", status="acquired", country="US", city="New York", focus="Data Infrastructure", rng="below_1b",
    stage="undetermined",
    note="Framed Data (framed.io), predictive churn analytics. The firm's exit line reads 'Acquired by Square, 2016'; "
         "Finextra's headline (2016-03-14) reads 'Team behind predictive analytics firm Framed Data join Square "
         "Capital' (the body could not be read), so acquired stands on the exit line and a later pass may test it "
         "against the acqui-hire rule. The firm lists it from 2015 (M.G. Siegler); no source read names GV's round, so "
         "the stage is undetermined. City from knowledge.",
    rounds=[]))

# ---------------------------------------------------------------- freshplum
L.append(cls(
    "freshplum", status="acquired", country="US", city="San Francisco", focus="Data Infrastructure",
    rng="below_1b", stage="undetermined",
    note="Data-driven online pricing (Freshplum, San Francisco; in Y Combinator's book; Reuters profiled it "
         "2012-06-26). The "
         "firm's exit line reads 'Acquired by TellApart, 2014'; acquired. The firm lists it from 2013 (Shanna "
         "Tellerman); no source read names GV's round (Google News returns only the 2012 profile), so the stage is "
         "undetermined.",
    rounds=[]))

# ---------------------------------------------------------------- gowalla
GW_TC = "https://techcrunch.com/2021/01/28/gowalla-raises-4-million-from-gv-and-spark-for-its-ar-social-app/"
L.append(cls(
    "gowalla", status="private", country="US", city="Austin", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GW_TC, entry_date="2021-01-28",
    note="The 2021 relaunch of Gowalla by co-founder Josh Williams (the original, bought by Facebook in 2011, is the "
         "Greylock row's company). GV and Spark Capital co-led the $4M seed (TechCrunch, 2021-01-28); the app "
         "relaunched in March 2023 (TechCrunch, 2023-03-10). No later round or exit found in Google News as of "
         "2026-09-28; aligned with the Spark row (private, Austin). Graduation left for the graduation pass.",
    rounds=[rnd("2021-01-28", "Seed", 4000000, "GV; Spark Capital", True, GW_TC, "press")]))

# ---------------------------------------------------------------- granata-bio
GR_A = ("https://www.granata.bio/news-press/womens-health-innovator-granata-bio-raises-14m-series-a-led-by-gv-to-"
        "accelerate-fertility-biopharma-pipeline")
GR_AP = ("https://www.prnewswire.com/news-releases/womens-health-innovator-granata-bio-raises-15m-series-a-to-further-"
         "develop-and-expand-reproductive-health-pipeline-302350977.html")
L.append(cls(
    "granata-bio", status="private", country="US", city="Boston", city_src="web_verified", focus="Healthcare & Bio",
    rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GR_A,
    entry_date="2024-01-16",
    note="Fertility medicines (Boston: the dateline of its 2025 release). GV led the $14M Series A with CooperSurgical, "
         "Gedeon Richter, Alumni Ventures, Amboy Street Ventures and Vibe Bio (the company's release, 2024-01-16); a "
         "$15M Series A+ from existing investors followed (2025-01-15). Operating (Phase III news, July 2026).",
    rounds=[rnd("2024-01-16", "Series A", 14000000, "GV", True, GR_A, "company"),
            rnd("2025-01-15", "Series A+", 15000000, None, None, GR_AP, "company")]))

# ---------------------------------------------------------------- granular
GRN_W = W("Granular Inc.")
L.append(cls(
    "granular", status="acquired", country="US", city="San Francisco", focus="SaaS", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=GRN_W, entry_date="2014",
    note="Farm management software (San Francisco), spun out of Solum in 2014. 'After the split, Granular raised $4.2 "
         "million in Series A round funding from Andreessen Horowitz, Khosla Ventures and Google Ventures' "
         "(Wikipedia); Tao Capital led the $18.7M Series B in July 2015 with earlier backers. DowDuPont bought it in "
         "September 2017 (Wikipedia; the firm's exit line 'Acquired by DuPont, 2017'). Medium confidence: the article "
         "gives the year only.",
    rounds=[rnd("2014", "Series A", 4200000, None, True, GRN_W, "press"),
            rnd("2015-07", "Series B", 18700000, "Tao Capital", True, GRN_W, "press")]))

# ---------------------------------------------------------------- gravity
GV_CB = NEWS("gravity", "Google Ventures Leads Seed Funding Round In Gravity")
L.append(cls(
    "gravity", status="private", country="US", country_src="web_verified", country_cite=GV_CB, city="New York",
    city_src="web_verified", focus="Climate & Energy", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GV_CB, entry_date="2023-11-16",
    flags=["model_disputes_source"],
    note="Ultra-fast EV charging (New York; flagship charging center in Midtown Manhattan, opened March 2024). GV led "
         "the seed (citybiz, 2023-11-16, quoting GV's Erik Nordlander). The prefilled JP came from a Wikidata match on "
         "the one-word name; disputed, as citybiz places the company in New York. The Redpoint row's 'Gravity' (JP, "
         "media) is another company. No later priced round found in "
         "Google News as of 2026-09-28 (2025 coverage is of the Los Angeles rollout). Graduation left for the "
         "graduation pass.",
    rounds=[rnd("2023-11-16", "Seed", None, "GV", True, GV_CB, "press")]))

# ---------------------------------------------------------------- flutterflow
FF_TC = NEWS("flutterflow", "FlutterFlow attracts cash")
L.append(cls(
    "flutterflow", status="private", country="US", city="San Francisco", focus="DevTools & APIs", rng="below_1b",
    extra={**WV, "valuation_citation": FF_TC},
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FF_TC, entry_date="2023-10",
    note="Low-code mobile app builder (Y Combinator; founded by former Google engineers). GV led the $25.5M Series A, "
         "with Gradient Ventures, Xoogler Ventures and Y Combinator, at about $170M (TechCrunch, 2024-01-11); the "
         "earlier funding does not name GV. The firm's own /ai list dates the investment October 2023 (the entry date, "
         "decisions D7) and its post welcomed the company on 2024-01-11. Momentum check 2026-09-28: Google News finds "
         "no round after the Series A; below_1b.",
    rounds=[rnd("2024-01-11", "Series A", 25500000, "GV", True, FF_TC, "press")]))

# ---------------------------------------------------------------- flourish
FL_CB = NEWS("flourish", "Emerges With Funding from Bezos")
L.append(cls(
    "flourish", status="private", country="US", focus="AI & Applied AI",
    rng="1b_plus", usd=2500000000, val_src="web_verified", val_cite=FL_CB, asof="2026-06-05", extra=WV,
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FL_CB, entry_date="2026-06-05",
    grad="censored", flags=["city_unknown"],
    note="Neuro-AI lab (flourishlabs.ai) co-founded with Catalio Capital, led by Rob Williams and Thomas Reardon. It "
         "emerged from stealth with a $500M seed at a $2.5B valuation from Jeff Bezos, Google Ventures, Lux Capital "
         "and Catalio (citybiz, 2026-06-05; Pulse 2.0, 2026-06-06), with Lux Capital and GV reported as the expected "
         "leads (The Next Web, 2026-05-01); the firm's own /ai list dates the investment June 2026. The mark is the entry round itself. Not the 2021 bank-engagement Flourish in TechCrunch. No source read "
         "places the company in a city (city_unknown). Censored: entry under 24 months old.",
    rounds=[rnd("2026-06-05", "Seed", 500000000, None, True, FL_CB, "press")]))

# ---------------------------------------------------------------- fabric
FAB_SEED = ("https://www.prnewswire.com/news-releases/florence-launches-modern-healthcare-experience-with-20m-seed-"
            "round-led-by-thrive-capital-gv-and-salesforce-ventures-301785372.html")
FAB_A = NEWS("fabric", "Fabric Raises $60M for its AI Platform")
L.append(cls(
    "fabric", status="private", city="New York", focus="Healthcare & Bio", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FAB_SEED, entry_date="2023-03-30",
    grad="graduated", grad_src="web_verified", grad_cite=FAB_A, grad_conf="high",
    note="Fabric Health (fabrichealth.com), virtual care and clinical intake software; founded in 2021 as Florence and "
         "renamed Fabric in 2024 (its own about page: 'Florence becomes Fabric', 'Fabric (FKA Florence)', "
         "https://www.fabrichealth.com/about). GV co-led Florence's $20M seed with Thrive Capital and Salesforce "
         "Ventures (the company's release, NEW YORK, 2023-03-30). Graduated: General Catalyst led the $60M Series A with "
         "Thrive, GV, Salesforce Ventures, Vast, BoxGroup and Atento, $80M raised in all (AlleyWatch, February 2024; "
         "General Catalyst's post of 2024-02-21). Aligned with the Thrive (Seed) and General Catalyst (Series A) rows; "
         "the Redpoint and Y Combinator 'Fabric' rows are other companies. No $1B mark; below_1b.",
    rounds=[rnd("2023-03-30", "Seed", 20000000, "Thrive Capital; GV; Salesforce Ventures", True, FAB_SEED, "company"),
            rnd("2024-02-26", "Series A", 60000000, "General Catalyst", True, FAB_A, "press")]))

# ---------------------------------------------------------------- flick
FLK = NEWS("flick", "Flick: $6 Million Raised")
L.append(cls(
    "flick", status="private", city="San Francisco", city_src="web_verified", focus="AI & Applied AI",
    rng="below_1b", extra={**WV, "valuation_citation": FLK},
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FLK,
    entry_date="2026-05-14", grad="censored",
    note="AI-native filmmaking platform (flick.art, San Francisco; founders Zoey Zhang and Ray Wang; Y Combinator). "
         "True Ventures led the $6M seed with GV, Y Combinator, Lightspeed and others (Pulse 2.0, 2026-05-14); the "
         "firm's own /ai list dates the investment May 2026. Censored: entry under 24 months old. Momentum check "
         "2026-09-28: Google News finds no round after the seed; below_1b.",
    rounds=[rnd("2026-05-14", "Seed", 6000000, "True Ventures", True, FLK, "press")]))

# ---------------------------------------------------------------- good-eggs
GE_R = NEWS("good-eggs", "Announces $100 Million In Funding")
GE_TC = NEWS("good-eggs", "GrubMarket has acquired Good Eggs")
L.append(cls(
    "good-eggs", status="acquired", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GE_R,
    entry_date="2021-02-03",
    note="Online grocery delivery (San Francisco). GV came in as a new investor in the $100M round of February 2021 led "
         "by Glade Brook Capital, beside Tao Invest, Finistere and Rich's, with existing investors Benchmark, Index, "
         "S2G, DNS Capital and Obvious (the company's release, 2021-02-03); a round after its $21M raise of 2014 and "
         "the $50M Benchmark-led round of 2018 (headlines in the news sweep), so Growth. GrubMarket acquired Good Eggs in an all-stock deal valuing it slightly above "
         "its $22M marked-down value (TechCrunch, 2024-08-06: " + GE_TC + "); acquired, no figure.",
    rounds=[rnd("2021-02-03", "Unnamed", 100000000, "Glade Brook Capital Partners", True, GE_R, "company")]))

# ---------------------------------------------------------------- graft
GRF_TC = NEWS("graft", "building an AI development platform for the masses")
GRF_YOU = NEWS("graft", "You.com Buying Graft")
L.append(cls(
    "graft", status="acquired", country="US", focus="AI & Applied AI", rng="below_1b",
    stage="Pre-Seed", stage_src="model", stage_conf="medium", entry_date="2021-04", flags=["city_unknown"],
    note="AI platform for multimodal enterprise data (founders Adam Oliner, formerly head of AI at Slack, and Eric "
         "Schkufza). Rounds: a $4.5M pre-seed announced in 2022, then a $10M seed led by Radical Ventures 'with "
         "participation from GV' (TechCrunch, 2023-07-26). The firm's own /ai list dates GV's first investment April "
         "2021 and a re-investment February 2023 (the seed); the only round before the seed is the pre-seed, so the "
         "entry is the Pre-Seed, named from the record at medium confidence (no page names GV in that round). You.com "
         "acquired 'the Graft team and technology' (Pulse 2.0, 2025-10-22), a purchase of the technology, not only a "
         "hire, so acquired; graft.com is now a domain for sale. No source read places the company in a city.",
    rounds=[rnd("2022", "Pre-Seed", 4500000, None, None, GRF_TC, "press"),
            rnd("2023-07-26", "Seed", 10000000, "Radical Ventures", True, GRF_TC, "press")]))

# ---------------------------------------------------------------- found
FND_A = ("https://techcrunch.com/podcast/weight-health-startup-found-comes-out-of-stealth-with-32m-in-funding-former-"
         "bumble-exec-as-new-ceo/")
FND_B = NEWS("found", "Weight Loss Startup Found Raises $100M")
L.append(cls(
    "found", status="private", country="US", city="San Francisco", city_src="web_verified",
    focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FND_A, entry_date="2021",
    note="Weight care clinic and app (Found Health, San Francisco; incubated at the Atomic studio in 2020). It came out "
         "of stealth on 2021-09-30 with $32M: an $8M seed in 2020 'largely from Atomic in addition to Define Ventures', "
         "and a $24M Series A earlier in 2021 'led by GV (formerly Google Ventures) and Atomic' (TechCrunch). WestCap "
         "led the $100M Series B with 'earlier investors GV, Define Ventures, and Atomic' (Crunchbase News, "
         "2021-12-16), reported at a $600M valuation (TechCrunch's headline). Operating (its site), so private and "
         "below_1b. The Lightspeed and Sequoia 'Found' rows are the banking app Found, another company.",
    rounds=[rnd("2020", "Seed", 8000000, "Atomic", False, FND_A, "press"),
            rnd("2021", "Series A", 24000000, "GV; Atomic", True, FND_A, "press"),
            rnd("2021-12-16", "Series B", 100000000, "WestCap", True, FND_B, "press")]))

jl.write("j5", L)
