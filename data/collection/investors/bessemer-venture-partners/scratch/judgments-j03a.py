"""PRO-80 Bessemer Venture Partners, judge j03, queue batch 5 part 1 (farther .. fuze): classification of listed
members. Every row here is on the firm's own listing; none is excluded in this file."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, ARCH, POST, W, NEWS

GL = "Graduation left for the graduation pass."
# URLs printed by tools run in this session (stockanalysis curl, secget, NEWS decode, WebFetch reads)
SA_FVRR = "https://stockanalysis.com/stocks/fvrr/market-cap/"
SA_DCOY = "https://stockanalysis.com/stocks/slrx/market-cap/"
TC_FARTHER = NEWS("farther", "banks $15M Series A")
FF_FARTHER = NEWS("farther", "New unicorn Farther")
RB_FARTHER = NEWS("farther", "soars to $1-billion-plus")
SA_FIELDGUIDE = NEWS("fieldguide", "$700M valuation to scale")
RT_FIREBOLT = NEWS("firebolt", "valued at $1.4 bln")
QZ_FIREWORKS = NEWS("fireworks", "qz.com")
TC_FORAGED = NEWS("foraged", "wild foods marketplace")
TC_FOREVR = NEWS("forevr", "raises $10M to grow")
FS_FORMALLY = NEWS("formally", "Pre-Seed")
BJ_FULCRUM = NEWS("fulcrum", "raises $18.8M")
VB_INTERCOM = NEWS("fin", "Intercom grabs")
CB_FIREBOLT = NEWS("firebolt", "Enters Data Warehousing")
GB_FINMARK = NEWS("finmark", "GrepBeat")

L = []

# ---- Farther
L.append(cls("farther", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
             val_cite=RB_FARTHER, asof="2026-05", country="US", city="New York",
             stage="Series A", stage_src="web_verified", stage_cite=TC_FARTHER, stage_conf="medium",
             entry_date="2022-05", focus="Fintech & Payments",
             rounds=[rnd("2021", "unnamed earlier round", None, None, False, TC_FARTHER, "press"),
                     rnd("2022-05", "Series A", 15000000, "Bessemer Venture Partners", True, TC_FARTHER, "press"),
                     rnd("2023-10", "Series B", 31000000, None, None, None, "press"),
                     rnd("2024-10", "Series C", 72000000, "CapitalG", None, None, "press"),
                     rnd("2026-05", "Series D", 150000000, "General Atlantic", None, FF_FARTHER, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Wealth management platform, New York (as in the Lightspeed book, which still reads below_1b). "
                  "TechCrunch (2022-08-11): Bessemer led the $15M Series A closed in May 2022, and the 2021 round "
                  "names Moneta, Context and Cota, not Bessemer, so the Series A is the entry although the firm's "
                  "own year reads 2021. Momentum check 2026-10-01: the $150M Series D of May 2026 led by General "
                  "Atlantic valued the company at $1 billion-plus (RIABiz headline, 2026-05-22; FinTech Futures: "
                  "'new unicorn'); the figure recorded is that floor, at the band edge."))

# ---- Fern
L.append(cls("fern", rng="below_1b", country="US", city="New York", stage="Series A", stage_src="first_party",
             stage_cite=POST("meet-the-founders-of-fern"), stage_conf="high", entry_date="2025-04",
             focus="DevTools & APIs",
             rounds=[rnd("2025-04", "Series A", 9000000, "Bessemer Venture Partners", True,
                         POST("meet-the-founders-of-fern"), "firm")],
             note="SDK and API documentation generator, New York. The firm's own post of 2025-04-10: Bessemer leads "
                  "Fern's $9M Series A, the firm's partnered year. Acquired by Postman in 2026 (the firm's listing)."))

# ---- Fieldguide
L.append(cls("fieldguide", status="private", rng="below_1b", country="US", city="San Francisco", stage="Growth",
             stage_src="first_party", stage_cite=POST("news/fieldguide"), stage_conf="high", entry_date="2024-03",
             focus="SaaS",
             rounds=[rnd("2024-03", "Series B", 30000000, "Bessemer Venture Partners", True, POST("news/fieldguide"),
                         "firm"),
                     rnd("2026-02", "Series C", 75000000, "Goldman Sachs Alternatives", True, SA_FIELDGUIDE, "press")],
             note="Audit and advisory engagement software, San Francisco (as in the 8VC and YC books). The firm's own "
                  "post: Bessemer leads the $30M Series B (March 2024), its partnered year. Momentum check 2026-10-01: "
                  "the $75M Series C of February 2026 valued the company at $700M (SiliconANGLE), below $1B."))

# ---- Fin (Intercom)
L.append(cls("fin", status="acquired", rng="below_1b", city="San Francisco", stage="Growth",
             stage_src="web_verified", stage_cite=VB_INTERCOM, stage_conf="medium", entry_date="2014-01",
             focus="SaaS",
             rounds=[rnd("2013", "earlier rounds ($7M in total)", 7000000, None, False, VB_INTERCOM, "press"),
                     rnd("2014-01", "Series B", 23000000, "Bessemer Venture Partners", True, VB_INTERCOM, "press")],
             note="Intercom, renamed Fin; acq. by Salesforce, 2026 (the firm's listing gives 2026-09-10; the ICONIQ, "
                  "Kleiner Perkins and GV books read the same). VentureBeat (2014-01-22): the $23M round was led by "
                  "Bessemer Venture Partners and brought the total raised to $30M, so it followed $7M of earlier "
                  "rounds and is the Series B (Growth); the firm's archived Intercom listing dates its investment "
                  "2014-01-06. This row and the base row intercom are one company."))

# ---- Finmark
L.append(cls("finmark", status="acquired", rng="below_1b", country="US", city="Raleigh", stage="Seed",
             stage_src="web_verified", stage_cite=GB_FINMARK, stage_conf="high", entry_date="2020-10",
             focus="Fintech & Payments",
             rounds=[rnd("2020-10", "Seed", 5000000, "IDEA Fund Partners", True, GB_FINMARK, "press")],
             note="Financial modeling software for startups, remote-first with its team in Raleigh (as in the YC "
                  "book); acq. by Bill.com, 2022. GrepBeat (2020-10-29): a $5M seed led by IDEA Fund Partners with "
                  "Bessemer Venture Partners and Draper Associates, the firm's partnered year. " + GL))

# ---- Firebolt
L.append(cls("firebolt", status="private", rng="1b_plus", usd=1400000000, val_src="web_verified",
             val_cite=RT_FIREBOLT, asof="2022-01", country="IL", country_src="web_verified",
             country_cite=CB_FIREBOLT, city="Tel Aviv", stage="Series A", stage_src="web_verified",
             stage_cite=CB_FIREBOLT, stage_conf="high", entry_date="2020-12", focus="Data Infrastructure",
             flags=["stale"],
             rounds=[rnd("2020-12", "Series A", 37000000, None, True, CB_FIREBOLT, "press"),
                     rnd("2021-06", "Series B", 127000000, None, None, None, "press"),
                     rnd("2022-01", "Series C", 100000000, None, None, RT_FIREBOLT, "press")],
             extra={"valuation_range_source": "web_verified"},
             note="Cloud data warehouse, Israel-based (Tel Aviv). Crunchbase News (2020-12-09): the $37M Series A "
                  "announced on leaving stealth names Zeev Ventures, TLV Partners, Bessemer Venture Partners and "
                  "Angular Ventures, the firm's partnered year. Mark: the $100M Series C of January 2022 at $1.4B "
                  "(Reuters headline), older than 24 months; layoffs were reported in February 2026 but no lower "
                  "priced event."))

# ---- Fireworks
L.append(cls("fireworks", status="private", rng="10b_plus", usd=17500000000, val_src="web_verified",
             val_cite=QZ_FIREWORKS, asof="2026-07-16", country="US", city="Redwood City", stage="Growth",
             stage_src="first_party", stage_cite=POST("fireworks-the-inference"), stage_conf="high",
             entry_date="2026-07", focus="AI & Applied AI",
             rounds=[rnd("2026-07", "Series D", 1500000000, None, True, POST("fireworks-the-inference"), "firm")],
             extra={"valuation_range_source": "web_verified"},
             note="Inference and training platform for open models. The firm's own post of 2026-07-17: Bessemer joins "
                  "the $1.5B Series D, its partnered year, so the entry is Growth. Mark: the Series D at $17.5B "
                  "(Quartz, 2026-07-16), as in the Insight and Menlo books. City follows those books (Redwood City); "
                  "the firm's listing gives San Mateo."))

# ---- Fiverr
L.append(cls("fiverr", status="public", rng="below_1b", usd=308100000, val_src="web_verified", val_cite=SA_FVRR,
             asof="2026-10-01", country="IL", country_src="web_verified", country_cite=ARCH("fiverr"),
             city="Tel Aviv", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011-01-20",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2010-03", "angel round", 1000000, None, False, POST("memos/fiverr"), "firm"),
                     rnd("2011-01", "$4M round, first institutional investment", 4000000,
                         "Bessemer Venture Partners", True, POST("memos/fiverr"), "firm"),
                     rnd("2012-05", "Series B", 15000000, "Accel", True, None, "press")],
             note="Freelance services marketplace, Tel Aviv; NYSE: FVRR, market cap $308.1M on 2026-10-01 "
                  "(StockAnalysis), fresher than the Accel book's August figure. The firm's memo of 2011-01-10 "
                  "recommends leading a $4M round after a $1M angel round, and its 2019 post calls it Fiverr's first "
                  "institutional investment; neither names the series. Model: the record names the next round, "
                  "Accel's of May 2012, the Series B, so the round Bessemer led is the Series A."))

# ---- Flagler Health
L.append(cls("flagler-health", status="private", rng="below_1b", country="US", city="New York", stage="Growth",
             stage_src="first_party", stage_cite=POST("flagler-health-the"), stage_conf="high", entry_date="2026-08",
             focus="Healthcare & Bio",
             rounds=[rnd("2026-08", "Series B", 50000000, "Bessemer Venture Partners", True,
                         POST("flagler-health-the"), "firm")],
             note="AI workflow platform for musculoskeletal clinics, New York (the firm's listing). The firm's own "
                  "post of 2026-08-12: Bessemer leads the $50M Series B, its partnered year. No valuation was "
                  "reported with the round (Google News, 2026-10-01)."))

# ---- Flarion Technologies
L.append(cls("flarion-technologies", status="acquired", rng="below_1b", country="US", city="Bedminster",
             stage="undetermined", entry_date="2000-02-09", focus="Data Infrastructure", rounds=[],
             note="OFDMA wireless broadband equipment, a Bell Labs spin-out in Bedminster, New Jersey; acq. by "
                  "Qualcomm, 2006. The firm's own listing dates its investment 2000-02-09 and says Bob Goodman led "
                  "BVP's investments, naming no round; a Google News query on 2026-10-01 found no funding report."))

# ---- Flat World Knowledge
L.append(cls("flat-world-knowledge", status="acquired", rng="below_1b", city="Boston",
             focus="Media, Gaming & Advertising",
             note="Publisher of openly licensed college textbooks. Bought in late 2016 by Alastair Adam and John "
                  "Eielson and renamed FlatWorld (Wikipedia), which operates from Boston; under Bessemer it was in "
                  "Irvington, New York, then Washington."))

# ---- Flex Pharma
L.append(cls("flex-pharma-inc", city="Boston", focus="Healthcare & Bio",
             note="Muscle cramp treatments, Boston (800 Boylston Street on its 2014 filings). Flex Pharma merged "
                  "with Salarius Pharmaceuticals in 2019 in a reverse merger and the listed shell is now Decoy "
                  "Therapeutics (DCOY, market cap $1.23M on 2026-10-01, StockAnalysis), so the public status is the "
                  "successor's listing; a later pass may prefer acquired."))

# ---- Flycast
L.append(cls("flycast", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Series A",
             stage_src="first_party", stage_cite=ARCH("flycast"), stage_conf="high", entry_date="1997",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("1997", "Series A", None, "Bessemer Venture Partners", True, ARCH("flycast"), "firm")],
             note="Web advertising network, San Francisco. The firm's own listing: in 1997 BVP's David Cowan led "
                  "Flycast's Series A round; IPO in 1999 (NASDAQ: FCST), then acq. by CMGI, 2000."))

# ---- Folx Health
L.append(cls("folx-health", status="private", rng="below_1b", city="Boston", focus="Healthcare & Bio",
             note="Digital health provider for the LGBTQIA+ community, Boston. Private; the last round found is the "
                  "$30M Series B of October 2022 led by 7wireVentures (Google News, 2026-10-01)."))

# ---- Foraged
L.append(cls("foraged", status="private", rng="below_1b", country="US", city="Washington", stage="Seed",
             stage_src="web_verified", stage_cite=TC_FORAGED, stage_conf="high", entry_date="2023-07",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2022", "pre-seed", 200000, None, None, TC_FORAGED, "press"),
                     rnd("2023-07", "Seed", 2700000, "Bessemer Venture Partners", True, TC_FORAGED, "press")],
             note="Marketplace for foraged and specialty foods, Washington (Business Journals, 2023-07-12). "
                  "TechCrunch (2023-07-12): Bessemer led the $2.7M seed after a $200K pre-seed in 2022; the firm's "
                  "own year reads 2022, the announcement dates the entry. " + GL))

# ---- Forever Oceans
L.append(cls("forever-oceans", status="defunct", rng="below_1b", city="Gainesville", extra={"focus": None},
             note="Offshore aquaculture (kanpachi farmed off Panama), headquartered in Gainesville, Virginia; outside "
                  "the focus taxonomy. Undercurrent News (2024-11-21, headline): liquidation experts took over the "
                  "troubled offshore farmer that once had $170M of backing; no sale of the business was found, so "
                  "the row reads defunct. The firm's listing dropped the company after 2024."))

# ---- ForeVR
L.append(cls("forevr", status="private", rng="below_1b", country="US", city="Los Angeles", stage="undetermined",
             entry_date="2021", focus="Media, Gaming & Advertising",
             rounds=[rnd("2021-08", "unnamed round ($8.5M raised in total)", 7000000, None, None,
                         NEWS("forevr", "racks up"), "press"),
                     rnd("2022-10", "Series A", 10000000, "Lobby Capital", True, TC_FOREVR, "press")],
             note="Virtual reality games studio, Los Angeles. TechCrunch (2022-10-27) names Bessemer in the $10M Series "
                  "A led by Lobby Capital, but the firm's own year is 2021, the year of a $7M round whose page (Venture "
                  "Capital Journal) could not be read for its name or investors, so the entry round is not "
                  "established."))

# ---- Formally
L.append(cls("formally", status="private", rng="below_1b", country="US", city="Palo Alto", stage="Pre-Seed",
             stage_src="web_verified", stage_cite=FS_FORMALLY, stage_conf="high", entry_date="2022-05",
             focus="SaaS",
             rounds=[rnd("2022-05", "Pre-Seed", 2300000, "Bessemer Venture Partners", True, FS_FORMALLY, "press")],
             note="Legal software for immigration applications, Palo Alto. FinSMEs (2022-05-16): a $2.3M pre-seed "
                  "led by Bessemer Venture Partners; the firm's own year reads 2021."))

# ---- Forter
L.append(cls("forter", city="New York", stage="Growth", stage_src="first_party", stage_cite=POST("forter-raises"),
             stage_conf="high", entry_date="2020-11", focus="Security",
             rounds=[rnd("2020-11", "Series E", 125000000, "Bessemer Venture Partners", True, POST("forter-raises"),
                         "firm")],
             note="E-commerce fraud prevention, New York (as in the NEA and Tiger Global books). The firm's own post "
                  "of 2020-11-19: Bessemer leads the $125M Series E, its partnered year."))

# ---- Foxglove
L.append(cls("foxglove", status="private", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
             note="Data and observability platform for robotics developers, San Francisco. Momentum check "
                  "2026-10-01: the $40M Series B of November 2025 led by Bessemer carried no reported valuation and "
                  "no later round was found (Google News)."))

# ---- Fractyl Health
L.append(cls("fractyl-health", city="Burlington", stage="undetermined", entry_date="2011", focus="Healthcare & Bio",
             rounds=[rnd("2013-03", "unnamed (Form D)", 14347541, None, True, None, "filing"),
                     rnd("2017-11", "Series D", 44000000, None, None, None, "press"),
                     rnd("2021-06", "Series F", 100000000, None, True, None, "press")],
             note="Metabolic disease therapies, Burlington, Massachusetts (as in the General Catalyst and GV books). "
                  "The firm's own year is 2011, before the first Form D of 2013 on which Chris Gabrieli is a "
                  "director, so the pre-filled 2013 date is replaced; no source read names the 2011 round (the IPO "
                  "prospectus covers only the Series E and F purchases)."))

# ---- Fulcrum
L.append(cls("fulcrum", status="private", rng="below_1b", country="US", city="Minneapolis", stage="undetermined",
             entry_date="2021", focus="SaaS",
             rounds=[rnd("2022-10", "$18.8M raised in total, announced out of stealth", 18800000, None, None,
                         BJ_FULCRUM, "press")],
             note="Fulcrum (fulcrumpro.com), ERP software for small manufacturers, Minneapolis. The Business Journals "
                  "(2022-10-14) report $18.8M raised on leaving stealth; the page could not be read for the round "
                  "names, so the round Bessemer entered in 2021 is not established. The General Catalyst and YC "
                  "rows named Fulcrum are other companies."))

# ---- Fuze
L.append(cls("fuze", status="acquired", rng="below_1b", city="Boston", stage="Growth", stage_src="web_verified",
             stage_cite=W("Fuze (company)"), stage_conf="medium", entry_date="2012-09-27", focus="SaaS",
             rounds=[rnd("2010-01", "first venture round", 1200000, "Capstone Partners", False, W("Fuze (company)"),
                         "press"),
                     rnd("2012-10", "second round", 16500000, "Advanced Technology Ventures and Bessemer Venture "
                         "Partners", True, W("Fuze (company)"), "press"),
                     rnd("2016-02", "growth round", 112000000, "Summit Partners", True, W("Fuze (company)"), "press")],
             note="Cloud communications, Boston, formerly Thinking Phone Networks; acq. by 8x8, 2022. Wikipedia: the "
                  "first venture round was $1.2M from Capstone in January 2010 and the $16.5M round of October 2012 "
                  "was led by Advanced Technology Ventures and Bessemer, which matches the firm's own date of "
                  "2012-09-27; a later round than the first, so Growth stands and the pre-filled 2016 date (the "
                  "Form D on which Bob Goodman first appears) is replaced. This row and the base row "
                  "thinking-phone-networks are one company."))

jl.write("j03a", L)
