"""PRO-75 GV grind, judge j17: queue batches 17, 18 and 19 (the member rows not yet classified; the four legal-name
twins rosa-foods-inc, denver-technologies-inc, noho-dental-inc and asset-blue-pharmacy-services-inc are skipped).

Research order per row: the firm's own posts and listings, S-1 holder tables (FTS), the company's own pages and
releases, TechCrunch's own archive (its WordPress search), Google News via nq.py (NQ_TAG=j17), EDGAR Form D filings,
and archived copies of pages that no longer load. Every citation below is a URL a tool printed and that was read.
Two rows here are one company with another base row: vectorized = redpanda, trucode = vera-therapeutics; omni =
omni-analytics and ready = mylaurel likewise. Each is classified on its own evidence, aligned with the twin's facts.
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
WEBV = {"valuation_range_source": "web_verified"}
GP = "Graduation left for the graduation pass."

# ---------------------------------------------------------------- Omni (omni.co, the /ai row)
OMNI_A = "https://omni.co/blog/series-a-press-release"
OMNI_B = "https://omni.co/blog/omni-series-b-funding"
OMNI_C = "https://omni.co/blog/press-release-omni-series-c-funding"
L.append(cls(
    "omni", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", val_cite=OMNI_C,
    asof="2026-04-23", country="US", city="San Francisco", focus="Data Infrastructure",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=OMNI_A, entry_date="2022-04",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=OMNI_A,
    note="Omni Analytics, the BI and AI analytics platform (San Francisco); the same company as the base row "
         "omni-analytics (exploreomni.com was its earlier domain). Omni's own release of 2022-08-16 names GV in the "
         "$9.4M Seed led by First Round and in the $17.5M Series A led by Redpoint; the firm's /ai list dates its "
         "first investment 2022-04 and a re-investment 2022-08, so GV entered at the Seed (entry date from the /ai "
         "list, decisions D7) and the named Series A graduates it. Momentum check 2026-09-28: Omni's own release of "
         "2026-04-23 reports a $120M Series C at a $1.5B valuation led by ICONIQ with GV participating, so 1b_plus. "
         "The First Round and Redpoint rows still read below_1b; ICONIQ's row carries the same $1.5B mark. The "
         "y-combinator row named Omni is a different company (a YC batch company).",
    rounds=[rnd("2022-04", "Seed", 9400000, "First Round Capital", True, OMNI_A, "company"),
            rnd("2022-08-16", "Series A", 17500000, "Redpoint Ventures", True, OMNI_A, "company"),
            rnd("2025-03-13", "Series B", 69000000, "ICONIQ Growth", True, OMNI_B, "company"),
            rnd("2026-04-23", "Series C", 120000000, "ICONIQ", True, OMNI_C, "company")],
    extra=WEBV))

# ---------------------------------------------------------------- Vectorized (renamed Redpanda Data)
VEC_TC = "https://techcrunch.com/2021/01/26/vectorized-announces-15-5m-investment-to-build-simpler-streaming-data-tool/"
VEC_CO = "https://www.redpanda.com/blog/redpanda-announces-series-a-lightspeed-venture-partners-gv"
RP_D = "https://www.redpanda.com/press/data-health-security-and-defense-startups-among-the-new-unicorns-in-april"
L.append(cls(
    "vectorized", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=RP_D,
    asof="2025-04-03", country="US", city="San Francisco", focus="Data Infrastructure",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=VEC_TC, entry_date="2020-11",
    note="Vectorized is Redpanda Data under its first name (streaming data platform, San Francisco); the same company "
         "as the base row redpanda. TechCrunch (2021-01-26) splits the $15.5M announcement into a $3M seed led by "
         "Lightspeed and a $12.5M Series A from Lightspeed with Google Ventures, and the firm's own posts say GV has "
         "led or co-led every round 'since the Series A' (" + POST("redpanda-performance-ai-revolution") + "); the "
         "firm's /ai list dates GV's first investment 2020-11 (decisions D7). Mark: the $100M Series D led by GV in "
         "April 2025 at a $1 billion valuation (Redpanda's own press page), aligned with the Lightspeed row. "
         "Momentum check 2026-09-28: no later priced round in the news search through September 2026.",
    rounds=[rnd(None, "Seed", 3000000, "Lightspeed Venture Partners", False, VEC_TC, "press"),
            rnd("2021-01-26", "Series A", 12500000, "Lightspeed Venture Partners", True, VEC_TC, "press"),
            rnd("2025-04-03", "Series D", 100000000, "GV", True, RP_D, "company")],
    extra=WEBV))

# ---------------------------------------------------------------- TruCode (renamed Vera Therapeutics, NASDAQ: VERA)
VERA_S1 = FTS("Vera Therapeutics", "S-1")
VERA_CAP = "https://stockanalysis.com/stocks/vera/market-cap/"
TRU_FIERCE = NEWS("trucode", "Kleiner, GV drive gene editing startup Trucode")
L.append(cls(
    "trucode", status="public", rng="1b_plus", usd=2340000000, val_src="web_verified", val_cite=VERA_CAP,
    asof="2026-09-28", country="US", city="Brisbane", city_src="web_verified", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=VERA_S1, entry_date="2019-09",
    note="Trucode Gene Repair is Vera Therapeutics under an earlier name: the S-1's corporate history says it was "
         "incorporated as CDF Therapeutics in May 2016, renamed Trucode Gene Repair in October 2017 and Vera "
         "Therapeutics in April 2020, at the same 170 Harbor Way, South San Francisco office the archived trucodegene.com "
         "shows; the same company as the base row vera-therapeutics. The S-1's principal-stockholder table shows GV's "
         "first shares are Series B preferred held by GV 2017, L.P. (Series C through GV 2019, L.P.; no GV Seed or "
         "Series A shares), bought in the financing Kleiner Perkins and GV drove in September 2019 (Fierce Biotech, "
         "the $34M round at launch): Growth. Public since May 2021: market cap $2.34B on 2026-09-28 (stockanalysis). "
         "HQ Brisbane, California, the current SEC business address.",
    rounds=[rnd("2019-09-10", "Series B", None, None, True, TRU_FIERCE, "press"),
            rnd("2020-10", "Series C", 80000000, "Abingworth", True, VERA_S1, "filing")]))

# ---------------------------------------------------------------- SideCar
SC_A = "https://techcrunch.com/2012/10/10/sidecar-10m-new-markets/"
SC_GM = "https://techcrunch.com/2016/01/19/whos-driving/"
L.append(cls(
    "sidecar", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=SC_A, entry_date="2012-10-10",
    flags=["model_disputes_source"],
    note="Ridesharing marketplace (San Francisco). GV co-led the $10M Series A with Lightspeed (TechCrunch, "
         "2012-10-10); the late-2011 seed's investors listed there do not include GV. Sidecar stopped rides and "
         "deliveries at the end of December 2015, and in January 2016 General Motors acquired certain assets and IP "
         "and hired about 20 staff (TechCrunch 2016-01-19; " + W("Sidecar (company)") + "): a sale of the business's "
         "assets after it ceased operating reads acquired, so the prefilled defunct (a Wikidata dissolution) is "
         "disputed. Aligned with the Lightspeed and USV rows.",
    rounds=[rnd("2011", "Seed", None, None, False, SC_A, "press"),
            rnd("2012-10-10", "Series A", 10000000, "Lightspeed Venture Partners and Google Ventures", True, SC_A,
                "press")]))

# ---------------------------------------------------------------- Stitch (stitchapp.com)
ST_SEED = "https://techcrunch.com/2014/04/24/stitch-raises-3-25m-from-google-ventures-and-others-to-help-salespeople-close-more-deals/"
ST_ACQ = "https://techcrunch.com/2015/03/08/sugarcrm-buys-mobile-startup-stitch-shuts-it-down/"
L.append(cls(
    "stitch", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=ST_SEED, entry_date="2014-04-24",
    note="Mobile email and sales productivity app (San Francisco, per SugarCRM's release). $3.25M seed from Google "
         "Ventures, SoftTech, Freestyle, Foundation Capital, ENIAC and angels (TechCrunch, 2014-04-24). SugarCRM "
         "acquired its IP and other assets and hired its engineers in March 2015, shutting the app (" + ST_ACQ + "). "
         "The other books' Stitch rows (a16z, General Catalyst, y-combinator's London Stitch Technologies, Ribbit's "
         "Cape Town fintech) are different companies. " + GP,
    rounds=[rnd("2014-04-24", "Seed", 3250000, None, True, ST_SEED, "press")]))

# ---------------------------------------------------------------- Rumble (Rumble Entertainment, not Rumble Inc.)
RUM_A = "https://techcrunch.com/2011/12/01/rumble-to-build-and-publish-games-using-15m-series-a-from-google-ventures-and-khosla/"
RUM_ACQ = NEWS("rumble", "Plarium acquires Alliance")
RUM_END = NEWS("rumble", "Forte shuts down Rumble Entertainment")
L.append(cls(
    "rumble", status="defunct", rng="below_1b", country="US", city="San Mateo",
    focus="Media, Gaming & Advertising",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=RUM_A, entry_date="2011-12-01",
    flags=["model_disputes_source"],
    note="Rumble Entertainment (Rumble Games, rumblegames.com), the free-to-play games developer and publisher, not "
         "Rumble Inc. (NASDAQ: RUM): the prefilled public status and $1.73B float are a name join onto the video "
         "platform and are disputed. Rumble closed a $15M Series A from Google Ventures and Khosla Ventures "
         "(TechCrunch, 2011-12-01; the company was founded that year on a few million dollars of seed money, investors "
         "not named). Plarium acquired Rumble in September 2017 (" + RUM_ACQ + ", terms undisclosed); in July 2024 its "
         "later owner Forte shut the studio, by then called R Studios (" + RUM_END + "). Status is the last known "
         "state, the 2024 closure: defunct, aligned with the Khosla row.",
    rounds=[rnd("2011", "Seed", None, None, None, RUM_A, "press"),
            rnd("2011-12-01", "Series A", 15000000, "Google Ventures and Khosla Ventures", True, RUM_A, "press")],
    extra={"is_public": False, "public_since": None, "valuation_source": None, "valuation_range_source": None,
           "valuation_asof": None, "valuation_confidence": None}))

# ---------------------------------------------------------------- 2011-2014 seeds with a TechCrunch round report
SHOP = "https://techcrunch.com/2011/06/16/price-tracking-service-shopobot-raises-funding-from-google-ventures-aol-and-others/"
L.append(cls(
    "shopobot", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SHOP, entry_date="2011-06-16",
    flags=["city_unknown"],
    note="Retail price-tracking site from AngelPad's second class. Undisclosed seed round from Google Ventures, AOL "
         "Ventures, Jump Ventures and others (TechCrunch, 2011-06-16). Fate unknown: no source read reports a sale or "
         "shutdown, and shopobot.com is a domain for sale (checked 2026-09-28). No source read places the company in "
         "a city. " + GP,
    rounds=[rnd("2011-06-16", "Seed", None, None, True, SHOP, "press")]))

ORDR = "https://techcrunch.com/2011/10/18/ordr-in-raises-seed-funding-from-google-ventures-for-its-food-api/"
L.append(cls(
    "ordr-in", status="unknown", rng="below_1b", country="US", city="New York", focus="DevTools & APIs",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=ORDR, entry_date="2011-10-18",
    note="Restaurant-ordering API from the 2011 TechStars NYC class. Its CEO announced a seed round from Google "
         "Ventures led by Rich Miner at the TechStars New York demo day (TechCrunch, 2011-10-18). Fate unknown: no "
         "source read reports a sale or shutdown, and ordr.in answers 410 Gone (checked 2026-09-28). " + GP,
    rounds=[rnd("2011-10-18", "Seed", None, "Google Ventures", True, ORDR, "press")]))

STICK = "https://techcrunch.com/2011/10/12/mobile-learning-platform-slickery-raises-325k-from-google-ventures-500-startups-and-others/"
L.append(cls(
    "stickery", status="unknown", rng="below_1b", country="US", focus="Media, Gaming & Advertising",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=STICK, entry_date="2011-10-12",
    flags=["city_unknown"],
    note="Mobile learning games for preschool children. $325K seed from Google Ventures, 500 Startups and other "
         "investors (TechCrunch, 2011-10-12). Fate unknown: no source read reports a sale or shutdown, and "
         "stickeryapp.com no longer answers (checked 2026-09-28). No source read places the company in a city. " + GP,
    rounds=[rnd("2011-10-12", "Seed", 325000, None, True, STICK, "press")]))

TRIP_A = "https://techcrunch.com/2012/03/08/triptrotting-series-a/"
TRIP_W = "https://techcrunch.com/2013/11/22/travel-startup-triptrotting-relaunches-as-wist-a-local-recommendations-app-for-iphone/"
L.append(cls(
    "triptrotting", status="unknown", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TRIP_A, entry_date="2012-03-08",
    note="Traveler-to-local matching site, home base San Francisco. TechCrunch names its $1M round a Series A with "
         "Google Ventures, GRP Partners, Launchpad LA, 500 Startups and Idealab among investors (2012-03-08; $1.3M "
         "raised in total, so a smaller earlier raise exists whose investors are not named), and repeats 'its $1 "
         "million Series A ... from Google Ventures' when the team relaunched as the Wist app in November 2013 "
         "(" + TRIP_W + "). The firm's own posts show nothing earlier. Fate after the Wist relaunch unknown: no "
         "source read reports a sale or shutdown, and triptrotting.com is parked (checked 2026-09-28).",
    rounds=[rnd("2012-03-08", "Series A", 1000000, None, True, TRIP_A, "press")]))

WANT = "https://techcrunch.com/2012/08/09/wantworthy-is-wanted-the-instapaper-for-shopping-raises-1-million-from-google-ventures-and-others/"
L.append(cls(
    "wantworthy", status="unknown", rng="below_1b", country="US", city="New York",
    city_src="formd_address", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WANT, entry_date="2012-08-09",
    note="Online shopping wish-list tool from the 2011 TechStars NYC class (its December 2011 Form D, $859,998 sold of "
         "$999,999, was filed from 8 Spruce Street, New York). $1M seed led by RRE Ventures with Google Ventures, "
         "Quotidian Ventures and New York angels (TechCrunch, 2012-08-09). In 2013 it launched the Fresh app; by "
         "2014 its CTO and creative director had joined Nifti (TechCrunch, 2014-09-25). Fate unknown: no source read "
         "reports a sale or shutdown, and wantworthy.com is parked (checked 2026-09-28). " + GP,
    rounds=[rnd("2012-08-09", "Seed", 1000000, "RRE Ventures", True, WANT, "press")]))

WITT = "https://techcrunch.com/2013/05/13/wittlebee-needs-a-wittle-more-money/"
L.append(cls(
    "wittlebee", status="unknown", rng="below_1b", country="US", city="Los Angeles",
    focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WITT,
    note="Kids' clothing subscription launched out of Los Angeles's Science incubator in January 2012. 'Wittlebee "
         "raised a $2.5 million seed round from Google Ventures, Matt Coffin, Crosslink Capital, and Rincon Venture "
         "Partners' (TechCrunch, 2013-05-13); no source read dates the seed itself, so no entry date is written. The "
         "same article reports the co-founder CEO stepping down after it could not raise a Series A. Fate unknown: no "
         "source read reports a sale or shutdown, and wittlebee.com no longer answers (checked 2026-09-28). " + GP,
    rounds=[rnd(None, "Seed", 2500000, None, True, WITT, "press")]))

NIFTI = NEWS("nifti", "An Idea Born at Business School")
NIFTI_C = "https://techcrunch.com/2014/09/25/price-tracking-service-nifti-switches-gears-launches-social-polling-app-cinch/"
L.append(cls(
    "nifti", status="unknown", rng="below_1b", country="US", city="Boston", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NIFTI, entry_date="2013-07",
    note="Price-tracking shopping tool founded by Tuck MBA graduates, with an office in Boston's North End. Tuck's "
         "article of 2013-07-24 says the founders secured $800,000 from Google Ventures and angel investors (the "
         "seed; seed investors also named). TechCrunch (2014-09-25) reports $1.2M more in seed funding in December "
         "2013 and the Cinch polling app spun out in 2014 (" + NIFTI_C + "). Fate unknown: no source read reports a "
         "sale or shutdown, and nifti.com shows an empty directory (checked 2026-09-28). " + GP,
    rounds=[rnd("2013-07", "Seed", 800000, None, True, NIFTI, "press"),
            rnd("2013-12", "Seed", 1200000, None, None, NIFTI_C, "press")]))

OSITO = "https://techcrunch.com/2013/03/25/sherpa-location-seed-funding-google-andreessen/"
OSITO_R = "https://techcrunch.com/2013/04/18/goodbye-sherpa-hello-osito-predictive-intelligence-ios-app-rebrands-and-graduates-from-beta/"
L.append(cls(
    "osito", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=OSITO, entry_date="2013-03-25",
    flags=["city_unknown"],
    note="Predictive personal-assistant iPhone app, launched as Sherpa and renamed Osito in April 2013 (" + OSITO_R +
         "). $1.1M seed from Andreessen Horowitz, Google Ventures, InterWest, Merus, Innovation Endeavors and "
         "AngelPad (TechCrunch, 2013-03-25). Fate unknown: no source read reports a sale or shutdown; getosito.com "
         "shows a placeholder page (checked 2026-09-28). No source read places the company in a city. " + GP,
    rounds=[rnd("2013-03-25", "Seed", 1100000, None, True, OSITO, "press")]))

SHELF = "https://techcrunch.com/2016/01/27/shelf-helps-you-find-the-best-products-people-actually-use/"
L.append(cls(
    "shelf", status="unknown", rng="below_1b", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SHELF, entry_date="2014",
    note="Shelf.com, a product-cataloguing and resale site from San Francisco, founded by Dayo Esho and Chris Kline. "
         "'Shelf is backed by $1.2 million in seed funding led by Google Ventures back in 2014' (TechCrunch, "
         "2016-01-27). Fate unknown: no source read reports a sale or shutdown, and shelf.com shows an empty page "
         "(checked 2026-09-28). The insight-partners row named Shelf is a different company (Shelf.io, the Stamford "
         "knowledge-management firm). " + GP,
    rounds=[rnd("2014", "Seed", 1200000, "Google Ventures", True, SHELF, "press")]))

TINY = "https://techcrunch.com/2015/11/17/tinyrx-gets-5-million-in-seed-to-take-on-pillpack-and-other-prescription-delivery-services/"
L.append(cls(
    "tinyrx", status="unknown", rng="below_1b", country="US", focus="Healthcare & Bio",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TINY, entry_date="2015-11-17",
    flags=["city_unknown"],
    note="Same-day prescription delivery covering the Bay Area in 2015. $5M seed from 8 Partners, Google Ventures, "
         "StartX and angels (TechCrunch, 2015-11-17). Fate unknown: no source read reports a sale or shutdown; "
         "tinyrx.com now serves a telehealth prescription business, and no source read ties it to this company "
         "(checked 2026-09-28). The article names the Bay Area, not a city. " + GP,
    rounds=[rnd("2015-11-17", "Seed", 5000000, None, True, TINY, "press")]))

WEOTTA = "https://techcrunch.com/2013/05/30/weotta-social-update-google-ventures/"
L.append(cls(
    "weotta", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
    stage="undetermined", flags=["city_unknown"],
    note="Activity-planning app that launched at TechCrunch Disrupt in 2011. GV's round: an undisclosed amount led by "
         "Google Ventures with Slow Ventures and TenOneTen, all new investors (TechCrunch, 2013-05-30); no source "
         "names the round, so the stage is undetermined. Fate unknown: no source read reports a sale or shutdown, "
         "and weotta.com refuses the request (checked 2026-09-28). No source read places the company in a city.",
    rounds=[rnd("2013-05-30", "unnamed", None, "Google Ventures", True, WEOTTA, "press")]))

# ---------------------------------------------------------------- SynapDx
SYN_TC = "https://techcrunch.com/2013/07/22/synapdx/"
SYN_FD13 = "https://www.sec.gov/Archives/edgar/data/1492969/000149296913000002/0001492969-13-000002-index.htm"
SYN_FD10 = "https://www.sec.gov/Archives/edgar/data/1492969/000149296910000001/0001492969-10-000001-index.htm"
L.append(cls(
    "synapdx", status="unknown", rng="below_1b", country="US", city="Lexington", city_src="formd_address",
    focus="Healthcare & Bio",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2013-07",
    note="Autism blood-test developer (Massachusetts). Google Ventures led a $15.4M round in July 2013, joined by "
         "Foundation Medical Partners and earlier investors North Bridge and General Catalyst (TechCrunch, "
         "2013-07-22). The record does not name the round, but the company's own Form Ds show it was its second "
         "priced round: $9.35M sold from 2010-05-26 (" + SYN_FD10 + ", the round the BCV and General Catalyst rows "
         "entered) and then $15.35M sold from 2013-07-18 (" + SYN_FD13 + "), above the era's $15M Series A band: a "
         "Series B by position, so Growth (model, medium). HQ Lexington, Massachusetts, the 2013 filing address "
         "(the siblings' Waltham is the 2010 address). Fate unknown: no source read reports a sale or shutdown after "
         "2014, aligned with the BCV and General Catalyst rows.",
    rounds=[rnd("2010-05-26", "unnamed", 9350000, None, False, SYN_FD10, "filing"),
            rnd("2013-07-22", "unnamed", 15400000, "Google Ventures", True, SYN_TC, "press")]))

# ---------------------------------------------------------------- Objective Logistics
OL_FS = NEWS("objective-logistics", "Objective Logistics Raises $1.5M")
OL_END = NEWS("objective-logistics", "Bit9 acqui-hires Objective Logistics")
L.append(cls(
    "objective-logistics", status="defunct", rng="below_1b", country="US", city="Boston", focus="SaaS",
    stage="undetermined",
    note="Restaurant staff-performance software (MUSE), Boston. GV's round on record: $1.5M in November 2011 led by "
         "Atlas Venture with Google Ventures, NextView, Canary and angels (FinSMEs, read from its archived copy); the "
         "report names no round, and Fortune says the company raised about $9M of equity and debt from 2010, so the "
         "stage is undetermined. In June 2015 Bit9 hired about a dozen of its staff in an acqui-hire; the core IP "
         "was not included, the CEO retired and the company began winding down its customers (" + OL_END + "). An "
         "acqui-hire decides nothing; the company wound down, so defunct.",
    rounds=[rnd("2011-11-30", "unnamed", 1500000, "Atlas Venture", True, OL_FS, "press")]))

# ---------------------------------------------------------------- Ready (Ready Responders, now myLaurel)
READY_C = NEWS("ready", "Home-Based Care Startup Ready Lands $54 Million")
MYL_24 = NEWS("ready", "myLaurel Positioned to Save")
MYL_25 = NEWS("ready", "SteelSky Ventures Leads Investment in myLaurel")
L.append(cls(
    "ready", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=READY_C,
    city="New York", city_src="web_verified", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=READY_C, entry_date="2020-09-16",
    flags=["model_disputes_source"],
    note="Ready (Ready Responders, readyresponders.com), in-home urgent care founded in New Orleans in 2016; the "
         "prefilled GB is a one-word name match and is disputed. GV was among the investors in its $54M Series C "
         "(Home Health Care News, 2020-09-16; valuation above $350M per Bloomberg as quoted there); the article says "
         "GV, Deerfield and City Light invested over $100M across two rounds in under a year, so GV may already "
         "have been in the preceding round, also Growth. It now operates as myLaurel: readyresponders.com serves "
         "myLaurel's site, the firm's own listing replaced Ready with myLaurel in 2023 under the same partner, and "
         "myLaurel's November 2025 round names Deerfield and GV as previous investors (" + MYL_25 + "). myLaurel "
         "gives its headquarters as New York (" + MYL_24 + "); it still operates in New Orleans. The same company as "
         "the base row mylaurel. The y-combinator row named Ready is a different company (a fintech).",
    rounds=[rnd("2020-09-16", "Series C", 54000000, None, True, READY_C, "press"),
            rnd("2025-11-06", "unnamed", None, "SteelSky Ventures", True, MYL_25, "company")]))

# ---------------------------------------------------------------- Rooser
ROO_TC = "https://techcrunch.com/2022/04/24/fishy-business-rooser-raises-23m-for-its-seafood-trading-platform/"
ROO_EU = NEWS("rooser", "nets $23 million from GV and Index")
L.append(cls(
    "rooser", status="defunct", rng="below_1b", country="GB", country_src="web_verified", country_cite=ROO_EU,
    city="Edinburgh", city_src="web_verified", focus="Consumer & Marketplaces",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ROO_TC, entry_date="2022-04-24",
    note="Seafood trading marketplace, headquartered in Edinburgh (Tech.eu, Insider). Index Ventures led the $23M "
         "Series A with GV and Point Nine participating (TechCrunch, 2022-04-24; before it, Point Nine and Eos "
         "Advisory funded the seed), so GV entered at the Series A. Status aligned with the Point Nine row, whose "
         "firm lists the company as closed; rooser.eu no longer resolves (checked 2026-09-28).",
    rounds=[rnd("2022-04-24", "Series A", 23000000, "Index Ventures", True, ROO_TC, "press")]))

# ---------------------------------------------------------------- Studio (Studio of America, Inc., s-tud.io)
STU_TC = "https://techcrunch.com/2022/09/29/studios-private-group-camcorder-app-lets-friends-create-episodes-by-combining-10-second-videos/"
STU_SITE = "http://web.archive.org/web/20260211220909/https://s-tud.io/"
L.append(cls(
    "studio", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=STU_TC,
    city="New York", city_src="web_verified", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=STU_TC, entry_date="2022-09-29",
    flags=["model_disputes_source"],
    note="Studio of America, Inc. (s-tud.io), a New York maker of a group video app and, by 2026, a creative "
         "studio; the prefilled DK is a one-word name match and is disputed. $3.3M seed led by GV's M.G. Siegler, "
         "with Mercury Fund and Pareto (TechCrunch, 2022-09-29, 'New York-based Studio'; the same three co-founders "
         "appear on the company's own team page). Private: its site was live in the 2026-02-11 capture ("
         + STU_SITE + "); the domain did not resolve on 2026-09-28. The y-combinator row named Studio is a "
         "different company. " + GP,
    rounds=[rnd("2022-09-29", "Seed", 3300000, "GV", True, STU_TC, "press")]))

# ---------------------------------------------------------------- Zeus Living
ZEUS_END = "https://techcrunch.com/2023/11/08/proptech-startup-zeus-living-which-was-backed-by-airbnb-reportedly-shuts-down/"
ZEUS_21 = "https://techcrunch.com/2021/10/14/zeus-living-closes-on-55m-to-offer-flexible-furnished-rentals-as-it-expands-beyond-corporate-housing/"
L.append(cls(
    "zeus-living", status="defunct", rng="below_1b", country="US", city="San Francisco",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="Furnished flexible-rental operator, San Francisco (Dogpatch). It was winding down operations in November "
         "2023 (TechCrunch 2023-11-08, citing The Information; the San Francisco Chronicle reported the same). No "
         "source read ties GV to a round: TechCrunch names Initialized (seed and Series A leads), Airbnb in the 2019 "
         "$55M Series B at $205M, and SIG leading the October 2021 $55M round, without GV; the firm's listing runs "
         "2019 to 2023. Stage undetermined.",
    rounds=[rnd("2019-12", "Series B", 55000000, None, None, ZEUS_END, "press"),
            rnd("2021-10-14", "unnamed", 55000000, "SIG", None, ZEUS_21, "press")]))

# ---------------------------------------------------------------- Superplastic
SP_GV = NEWS("superplastic", "Raises $6M Led By GV")
SP_21 = "https://techcrunch.com/2021/10/20/superplastic-guggimon-janky-virtual-celebrities-series-a/"
SP_23 = "https://techcrunch.com/2023/02/15/superplastic-a-creator-of-synthetic-influencers-raises-20m-led-by-amazon-in-deal-to-make-tv-shows-and-more/"
L.append(cls(
    "superplastic", status="private", rng="below_1b", country="US", city="Burlington", city_src="formd_address",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Character-driven toys, animation and synthetic-influencer company founded by Paul Budnitz; its Form Ds are "
         "filed from 47 Maple Street, Burlington, Vermont. GV led a $6M round in October 2020 (VirtualHumans.org, "
         "2020-10-22), but the sources disagree on what came before and after: that article calls the July 2019 $10M "
         "round a Series A, while TechCrunch calls the October 2021 $20M round the Series A (" + SP_21 + "). The GV "
         "round is unnamed and cannot be placed on either side of a Series A, so the stage is undetermined. Later: a "
         "$20M round led by Amazon in February 2023 (" + SP_23 + "). No priced mark near $1B is reported.",
    rounds=[rnd("2019-07", "Series A", 10000000, None, None, SP_GV, "press"),
            rnd("2020-10-22", "unnamed", 6000000, "GV", True, SP_GV, "press"),
            rnd("2021-10-20", "Series A", 20000000, None, None, SP_21, "press"),
            rnd("2023-02-15", "unnamed", 20000000, "Amazon", None, SP_23, "press")]))

# ---------------------------------------------------------------- Patina (Patina Health)
PAT_BI = NEWS("patina", "Patina Health Raises $57M From Andreessen Horowitz, GV")
PAT_END = "https://patinahealth.com"
PAT_FD = "https://www.sec.gov/Archives/edgar/data/1891732/000189173221000002/0001891732-21-000002-index.htm"
L.append(cls(
    "patina", status="defunct", rng="below_1b", city="Bala Cynwyd", city_src="formd_address",
    focus="Healthcare & Bio",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PAT_BI, entry_date="2020-10",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=PAT_BI,
    note="Primary care for adults over 65 in the Philadelphia area (Form D address 150 Monument Road, Bala Cynwyd). "
         "'Andreessen Horowitz and Alphabet's GV co-led Patina's seed and Series A funding', $57M in total (Business "
         "Insider, 2021-10-26); the company's Form Ds date the $7M seed from 2020-10-08 (two investors) and the $50M "
         "Series A from 2021-10-22 (" + PAT_FD + "). The named Series A graduates the seed. The practice closed: its "
         "own site now carries the records custodian's notice that Patina Medical Group stopped providing care on "
         "2025-09-30 'due to unforeseen business challenges' (" + PAT_END + "). The a16z row still reads private.",
    rounds=[rnd("2020-10-08", "Seed", 7000000, "Andreessen Horowitz and GV", True, PAT_BI, "press"),
            rnd("2021-10-22", "Series A", 50000000, "Andreessen Horowitz and GV", True, PAT_BI, "press")]))

# ---------------------------------------------------------------- Tome Biosciences
TOME_L = "https://www.globenewswire.com/news-release/2023/12/12/2794660/0/en/tome-biosciences-launches-with-over-200-million-in-funding-to-advance-programmable-genomic-integration-platform.html"
TOME_END = NEWS("tome-biosciences", "files notice to lay off virtually entire staff - STAT")
L.append(cls(
    "tome-biosciences", status="defunct", rng="below_1b", country="US", city="Watertown", city_src="web_verified",
    focus="Healthcare & Bio", stage="undetermined",
    note="Programmable genomic integration (gene insertion) company in Watertown, Massachusetts (its launch release's "
         "dateline). It launched in December 2023 having raised $213M 'in Series A and B funding' from a16z, ARCH, "
         "GV, Longwood, Polaris and others (" + TOME_L + "); neither the release nor BioSpace says which of the two "
         "rounds GV joined, so the stage is undetermined. In August 2024 it filed notice to lay off virtually its "
         "entire staff from November 1, planning to wind down and seek a buyer (" + TOME_END + "); no sale is "
         "reported, so defunct, aligned with the a16z row (whose Cambridge city is not what the company's own "
         "releases give).",
    rounds=[rnd("2023-12-12", "Series A and Series B (combined $213M)", 213000000, None, True, TOME_L, "company")]))

# ---------------------------------------------------------------- Ribon Therapeutics
RIB_65 = NEWS("ribon-therapeutics", "Peregrine Ventures invests")
RIB_END = NEWS("ribon-therapeutics", "Shuts Down Business Operations")
L.append(cls(
    "ribon-therapeutics", status="defunct", rng="below_1b", country="US", city="Cambridge",
    focus="Healthcare & Bio", stage="undetermined",
    note="Small-molecule cancer and inflammation biotech, Cambridge, Massachusetts. Its Form Ds show rounds from 2015 "
         "onward; the July 2021 $65M round was led by Deerfield and US Venture Partners with existing investors named "
         "(Globes, 2021-07-15), and no source read names GV in any round (the firm lists it from 2021), so the stage "
         "is undetermined. Ribon discontinued all material operations and auctioned substantially all of its assets "
         "(its IP) in 2024, with no buyer named (" + RIB_END + "): defunct.",
    rounds=[rnd("2021-07-15", "unnamed", 65000000, "Deerfield Management and US Venture Partners", None, RIB_65,
                "press")]))

# ---------------------------------------------------------------- Next Autoworks (formerly V-Vehicle)
NA_GTM = "http://web.archive.org/web/20250817115321/https://www.greentechmedia.com/articles/read/next-autoworks-the-curse-of-the-doe-loan-guarantee"
NA_AN = "http://web.archive.org/web/20200308025243/https://www.autonews.com/article/20111219/OEM/111219864/startup-next-autoworks-scales-back-after-failing-to-secure-u-s-loan"
NA_NS = NEWS("next-autoworks", "Davison at crossroad")
L.append(cls(
    "next-autoworks", status="defunct", rng="below_1b", country="US", city="San Diego",
    focus="Industrial & Robotics", stage="undetermined",
    note="Next Autoworks (formerly V-Vehicle), a San Diego car startup backed by Kleiner Perkins, T. Boone Pickens and "
         "Google Ventures, with about $100M from investors (Greentech Media, " + NA_GTM + "). The DOE refused its "
         "$320M loan in November 2011; it closed its San Diego headquarters and cut staff in December 2011 "
         "(Automotive News, " + NA_AN + "), and the local paper of its planned Louisiana plant wrote in 2014 that the "
         "deal died with the loan (" + NA_NS + "). No later activity is reported: defunct. No source read names the "
         "round GV joined, so the stage is undetermined.",
    rounds=[]))

# ---------------------------------------------------------------- Predilytics
PRED_ACQ = NEWS("predilytics", "Welltok Acquires Leading Healthcare Analytics")
L.append(cls(
    "predilytics", status="acquired", rng="below_1b", country="US", city="Burlington",
    city_src="formd_address", focus="Healthcare & Bio", stage="undetermined",
    note="Machine-learning analytics for health plans, Burlington, Massachusetts (its 2013 and 2014 Form D address). "
         "Welltok acquired it in May 2015 (" + PRED_ACQ + "). Its Form Ds show rounds of $6.07M (from 2012-08-16), "
         "$4.5M (from 2013-09-18) and $8.9M (from 2014-11-24), none naming a GV person, and no source read names the "
         "round GV joined (the firm lists it 2013 to 2015), so the stage is undetermined.",
    rounds=[]))

# ---------------------------------------------------------------- Nvelop Therapeutics (merged into nChroma Bio)
NV_GEN = NEWS("nvelop-therapeutics", "Cloaking Device: Liu, Joung Launch")
NV_M = NEWS("nvelop-therapeutics", "Chroma, Nvelop merge to marry")
L.append(cls(
    "nvelop-therapeutics", status="acquired", rng="below_1b", country="US", focus="Healthcare & Bio",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NV_GEN, entry_date="2022",
    flags=["city_unknown"],
    note="In vivo delivery platforms for genetic medicines from the Liu and Joung labs. At its April 2024 launch GEN "
         "reported '$100 million in seed funding, raised two years ago' from Newpath, Atlas, F-Prime and 5AM 'with "
         "participation from GV (Google Ventures) and ARCH', so GV entered at the Seed (entry year 2022). In "
         "December 2024 it merged with Chroma Medicine into nChroma Bio, led by Nvelop's CEO, with $75M of new "
         "funding (" + NV_M + "): a merger into a successor reads acquired. Fierce calls both 'Boston-area "
         "biotechs'; no source read gives Nvelop's own municipality. " + GP,
    rounds=[rnd("2022", "Seed", 100000000, None, True, NV_GEN, "press")]))

# ---------------------------------------------------------------- Rally (Rally.org, formerly Piryx)
RALLY_S = "https://techcrunch.com/2011/06/16/social-fundraising-platform-piryx-is-reborn-as-rally-org-with-top-investors-in-tow/"
RALLY_A = "http://web.archive.org/web/20240812214329/https://www.forbes.com/sites/jjcolao/2013/02/13/8m-in-two-weeks-the-inside-story-of-the-largest-crowdfunded-series-a-round-of-all-time/"
L.append(cls(
    "rally", status="unknown", rng="below_1b", country="US", city="San Francisco", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=RALLY_A, entry_date="2012-05-25",
    note="Rally.org (formerly Piryx), a social fundraising and payments platform headquartered in San Francisco's "
         "SoMa. Its 2011 seed came from Floodgate, Greylock Discovery and Ron Conway (" + RALLY_S + "), no GV. Forbes "
         "(2013-02-13, read from its archived copy) tells how the May 2012 Series A came together: Floodgate, Reid "
         "Hoffman and Eric Ries leading with $3.5M and 18 more backers adding $4.4M; Kevin Rose, then a new Google "
         "Ventures partner, said yes, the CEO met 'Kevin Rose and Google Ventures in Mountain View' on May 24, and the "
         "round closed on May 25. The firm lists Rally from 2013 with Kevin Rose as its partner. Series A at medium "
         "confidence (the article does not list the round's final investors). Fate unknown: no source read reports "
         "a sale or shutdown, and rally.org is parked (checked 2026-09-28). The accel and battery-ventures rows named "
         "Rally are different companies.",
    rounds=[rnd("2011-06-16", "Seed", None, "Floodgate", False, RALLY_S, "press"),
            rnd("2012-05-25", "Series A", 7900000, "Floodgate, Reid Hoffman and Eric Ries", True, RALLY_A, "press")]))

# ---------------------------------------------------------------- Rabbit (rabb.it)
L.append(cls(
    "rabbit", status="acquired", rng="below_1b", country="US", city="Redwood City", city_src="formd_address",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="Rabbit (rabb.it), the co-watching and video chat service, based in California; its 2015 Form D ($3.8M sold "
         "from 2015-02-09) was filed from 822 Winslow Street, Redwood City. After a failed round it shut down in "
         "July 2019 and on 2019-07-31 its remaining assets (IP, software stack and patents) were acquired by Kast ("
         + W("Rabb.it") + "): an asset sale after the shutdown reads acquired, with Kast as successor. No source read "
         "names the round GV joined (the firm lists it from 2013), so the stage is undetermined. The a16z and "
         "General Catalyst Rabbit rows are identity-unresolved; if either is rabb.it it should read acquired too.",
    rounds=[]))

# ---------------------------------------------------------------- Oncologic
ONC_SITE = "https://www.oncologic.ai"
L.append(cls(
    "oncologic", status="private", rng="below_1b", country="US", city="Orlando", city_src="web_verified",
    focus="Healthcare & Bio", stage="undetermined",
    note="AI oncology practice-workflow platform (therapy selection, insurance pre-approval, care coordination); its own "
         "site gives 7300 Sandlake Commons Blvd, Orlando (" + ONC_SITE + "). On the firm's live list with partner "
         "David Reshef. No source read names a round or ties GV to one, so the stage is undetermined. Momentum check "
         "2026-09-28 (Google News for the company's name with 'raises'; the results are the common word, not the "
         "company): no priced round near $1B reported, so below_1b.",
    rounds=[]))

# ---------------------------------------------------------------- Synapse Health (Form D seat, medium membership)
SYNH_BW = NEWS("synapse-health-inc", "to Lead Medtrade 2026 Panel")
L.append(cls(
    "synapse-health-inc", status="private", rng="below_1b", city="Evanston", city_src="formd_address",
    focus="Healthcare & Bio",
    note="Synapse Health, the durable-medical-equipment ordering platform, 1603 Orrington Avenue, Evanston, Illinois "
         "(both Form Ds). Its Form Ds show $15M sold from 2022-12-20 (14 investors) and $25M sold of a $45M offering "
         "from 2023-09-11 (one investor); Ben Robbins of GV is a director on both, the second filed from GV's "
         "Mountain View address. Operating in 2026 (Business Wire, 2026-02-17: " + SYNH_BW + "). No priced mark "
         "near $1B is reported. Membership stays medium (a seat, not a listing).",
    rounds=[]))

# ---------------------------------------------------------------- The Wing
WING_GV = NEWS("the-wing", "WeWork sells Teem and its stake in The Wing")
WING_IWG = NEWS("the-wing", "IWG CEO Mark Dixon Confirms Majority Stake")
WING_END = NEWS("the-wing", "Women-Only Club the Wing Shuts Down")
WING_C = NEWS("the-wing", "just raised $75 million led by Sequoia")
L.append(cls(
    "the-wing", status="defunct", rng="below_1b", country="US", city="New York", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=WING_GV, entry_date="2020-01-22",
    note="Women-focused coworking clubs, New York. GV was not in the $75M Series C of December 2018 (led by Sequoia "
         "with Upfront, Airbnb, NEA and WeWork: " + WING_C + "). In January 2020 WeWork sold its minority stake to a "
         "consortium of new and existing investors including GV (CNBC, 2020-01-22; Business Insider says the group was "
         "led by GV, at a $165M valuation plus a $15M convertible note: " + NEWS("the-wing", "took a huge valuation cut") + "): "
         "a secondary, so Growth. IWG bought a majority "
         "stake in February 2021 (" + WING_IWG + ") and The Wing closed on 2022-08-31 (" + WING_END + "). Status is "
         "the last known state: defunct, aligned with the Sequoia row.",
    rounds=[rnd("2018-12-19", "Series C", 75000000, "Sequoia Capital", False, WING_C, "press"),
            rnd("2020-01-22", "secondary (WeWork's stake)", None, "GV", True, WING_GV, "press")]))

# ---------------------------------------------------------------- Place (Place.xyz, Backplane's pivot)
BP_GV = NEWS("place", "Backplane goes down after $19m")
BP_VF = NEWS("place", "Lady Gaga’s Start-Up Meets an Untimely End")
L.append(cls(
    "place", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BP_GV, entry_date="2011",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=BP_GV,
    note="Place (place.xyz) is the community-network product Backplane pivoted to in 2015; the same company as the base "
         "row backplane (listed 2012 to 2015 under the same partner, David Krane). 'GV, then called Google Ventures, "
         "was among the investors in the company's 2011 seed round ... The seed investors returned for a $12.1m "
         "series A round the following year' (Global Venturing, 2016-04-15), so Seed, graduated by the named Series "
         "A. In April 2016 Backplane went out of business and sold its assets through Dorsey & Whitney while some "
         "Series A investors set up a new company to relaunch the business (same source; " + BP_VF + "): an asset "
         "sale out of insolvency with a successor reads acquired.",
    rounds=[rnd("2011", "Seed", None, None, True, BP_GV, "press"),
            rnd("2012", "Series A", 12100000, None, True, BP_GV, "press")]))

# ---------------------------------------------------------------- Seedling: not a GV venture position (merger stock)
SEED_M = "https://techcrunch.com/2014/10/29/p-s-xo-merges-with-toy-and-crafts-company-seedling-raises-7-million/"
L.append(verdict(
    "seedling", "not_member",
    "Merger consideration, not an investment (COLLECTION.md s1, the share-swap reading of the sale-consideration "
    "rule): GV's company here was Moonfrye (listed 2013 to 2014, a row of its own), renamed P.S. XO, which merged "
    "with the New Zealand toy and craft company Seedling in October 2014; the combined company kept the Seedling name, "
    "Seedling had never taken outside money, and the $7M raised with the merger came from Upfront Ventures and "
    "Greycroft, not GV (TechCrunch, 2014-10-29). The firm lists Seedling from 2015, right after its Moonfrye listing "
    "ends. Moonfrye stays the member. Flagged for Erik: the parties called it a merger of equals.",
    ec="web", conf="medium", cite=SEED_M))

# ---------------------------------------------------------------- Wearable Intelligence
L.append(cls(
    "wearable-intelligence", status="unknown", rng="below_1b", country="US", city="San Francisco",
    city_src="formd_address", focus="SaaS", stage="undetermined",
    note="Hands-free enterprise software for Google Glass and other wearables. Its only Form D (2014-08-20: $7.87M "
         "sold from 2014-08-06, ten investors, Barry Eggers of Lightspeed a director) was filed from 217 2nd Street, "
         "San Francisco; no source read names the round GV joined (the firm lists it 2014 to 2019, partner Blake "
         "Byers), so the stage is undetermined. Fate unknown: no source read reports a sale or shutdown. The First "
         "Round row says it 'became Proxy', but Proxy was incorporated separately as Martians Inc. (TechCrunch, "
         "2016-08-22), so that reading is not followed; the a16z row also reads unknown.",
    rounds=[]))

# ---------------------------------------------------------------- rumr
RUMR = "https://techcrunch.com/2014/03/25/rumr/"
L.append(cls(
    "rumr", status="defunct", rng="below_1b", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=RUMR, entry_date="2013-10",
    note="Anonymous group-chat app. 'Raising an $800,000 seed back in October, led by Khosla Ventures' Ben Ling. "
         "Google Ventures' MG Siegler also participated in the round' (TechCrunch, 2014-03-25); the firm lists rumr "
         "2014 to 2015 with Siegler as partner. Status and city aligned with the Khosla row (the app shut down; "
         "rumrapp.com is a domain for sale, checked 2026-09-28). " + GP,
    rounds=[rnd("2013-10", "Seed", 800000, "Khosla Ventures", True, RUMR, "press")]))

# ---------------------------------------------------------------- Pocket Change
L.append(cls(
    "pocket-change", status="defunct", rng="below_1b", country="US", city="San Francisco",
    focus="Media, Gaming & Advertising", stage="undetermined",
    note="Token-based monetization platform for mobile game developers (the firm's own 2012 listing). No source read "
         "names a round or ties GV to one; Google News returns only the common phrase. Status and city aligned with "
         "the First Round row (defunct, San Francisco); pocketchange.com no longer answers (checked 2026-09-28).",
    rounds=[]))

# ---------------------------------------------------------------- Puddle
L.append(cls(
    "puddle", status="unknown", rng="below_1b", country="US", city="San Francisco", focus="Fintech & Payments",
    stage="undetermined",
    note="Crowd-sourced credit circles ('a new way to access credit', the firm's 2015 listing). No source read names a "
         "round or the company's fate; Google News returns only the common word. Status and city aligned with the "
         "a16z row; puddle.com no longer answers (checked 2026-09-28).",
    rounds=[]))

# ---------------------------------------------------------------- Scout (Scout launcher)
SCOUT_AB = "http://web.archive.org/web/2016id_/http://www.scoutlauncher.com:80/about.html"
L.append(cls(
    "scout", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
    stage="undetermined", flags=["city_unknown", "model_disputes_source"],
    note="Scout, a contextual Android home-screen launcher (scoutlauncher.com). Its own About page names founders "
         "Nikhil Chandhok (nine years at Google, then Entrepreneur in Residence at Google Ventures) and Kunal Punera "
         "(RelateIQ, Yahoo) and no UK tie; the prefilled GB is a one-word Wikidata match and is disputed (US, from "
         "the founders' record; the page gives no city). No source read names a round or the company's fate; "
         "scoutlauncher.com is a domain for sale (checked 2026-09-28).",
    rounds=[]))

# ---------------------------------------------------------------- Super.cc
SUPER = "https://techcrunch.com/2014/02/10/super-cc/"
L.append(cls(
    "super-cc", status="unknown", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
    flags=["city_unknown"],
    note="Super.cc, an email-to-calendar service built by Michael Galpert (a founder of Aviary), launched in February "
         "2014 (" + SUPER + "); its parent Superhuman had 'raised some seed capital' by May 2013 (TechCrunch), no "
         "investors named, so the stage is undetermined. No source read gives its fate or city; super.cc is a "
         "domain for sale (checked 2026-09-28).",
    rounds=[]))

# ---------------------------------------------------------------- WUT
L.append(cls(
    "wut", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces", stage="undetermined",
    flags=["city_unknown"],
    note="WUT (WUT, Inc., wutwut.com), a 2014 app for anonymous, disappearing messages to Facebook friends' lock "
         "screens. No source read names a round, the company's city or its fate; wutwut.com no longer serves the "
         "app (checked 2026-09-28).",
    rounds=[]))

# ---------------------------------------------------------------- The Orange Chef Co.
OC_IP = NEWS("the-orange-chef-co", "Perfect Company Acquires Orange Chef")
L.append(cls(
    "the-orange-chef-co", status="acquired", rng="below_1b", country="US", focus="Consumer & Marketplaces",
    stage="undetermined", flags=["city_unknown"],
    note="Maker of the Prep Pad smart kitchen scale. Its founder and former CEO says in Perfect Company's release of "
         "2016-12-22 that the company had been 'acquired by Yummly', after which Perfect Company bought the Prep Pad "
         "IP (" + OC_IP + "): acquired. No source read names a round GV joined (the firm lists it 2014 to 2015) or "
         "the company's city.",
    rounds=[]))

# ---------------------------------------------------------------- Nettle (MovieGoer)
NET = "https://techcrunch.com/2012/02/08/google-ventures-backed-nettle-wants-to-make-watching-movies-social-with-moviegoer/"
L.append(cls(
    "nettle", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces", stage="undetermined",
    flags=["city_unknown"],
    note="Maker of the MovieGoer social moviegoing iPhone app (co-founder Brian Dear). TechCrunch (2012-02-08) says it "
         "'has raised funding from Google Ventures, 500 Startups and others' without naming the round, so the stage "
         "is undetermined. No source read gives its city or fate.",
    rounds=[rnd("2012", "unnamed", None, None, True, NET, "press")]))

# ---------------------------------------------------------------- NewHound
NH = "http://web.archive.org/web/20160130073452/https://newhound.com/"
L.append(cls(
    "newhound", status="unknown", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
    flags=["city_unknown"],
    note="Lead-generation and free mobile web pages for local businesses (its own site in a January 2016 capture, "
         + NH + "). No source read names a round, the company's city or its fate; Google News finds nothing for it "
         "and newhound.com no longer answers (checked 2026-09-28).",
    rounds=[]))

jl.write("j17", L)
