"""PRO-75 grind, judge j15: queue batch 15 (45 member rows, none classified before). Every citation below is a URL a
tool printed or a page read in this pass (TechCrunch's own WordPress search, the firm's CMS posts on disk, SEC filings,
company pages, Google News decodes through NEWS()). Stages follow COLLECTION.md s6: a round is cited only where the
source names the round AND ties GV (Google Ventures) to it; otherwise the stage is undetermined and the rounds found are
kept in funding_rounds."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
WV = {"valuation_range_source": "web_verified"}
GRAD_LEFT = "Graduation left for the graduation pass."


def post_exact(slug):
    """The firm's own post by exact slug (POST() is substring-based and cannot isolate a slug that prefixes another)."""
    m = [p["url"] for p in jl._POSTS if p.get("slug") == slug]
    if len(m) != 1:
        raise SystemExit(f"post_exact({slug!r}) matched {len(m)}")
    return m[0]


# ---------------------------------------------------------------- live list (tier A)

# Waymo: GV's first position is the Feb-2026 $16B round (decisions D4: an Alphabet company, minority financing).
WAYMO = "https://waymo.com/blog/2026/02/waymo-raises-usd16-billion-investment-round/"
L.append(cls("waymo", status="private", rng="100b_plus", usd=126000000000, val_src="web_verified", val_cite=WAYMO,
             asof="2026-02-02", extra=WV, country="US", city="Mountain View", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=WAYMO, entry_date="2026-02-02",
             note="Autonomous driving (Alphabet company, Mountain View). Waymo's own post of 2026-02-02: a $16B "
                  "investment round at $126B post-money, led by Dragoneer, DST Global and Sequoia, with GV named among "
                  "the investors. The firm's own post the same day (" + POST("waymo-gv") + ") calls it GV 'officially "
                  "starting a new ride, participating in Waymo's latest funding round', so this is the entry: a "
                  "late-stage round after Waymo's 2020, 2021 and 2024 raises, read Growth. Private at that mark "
                  "(decisions D4); aligned with a16z and Sequoia ($126B, 2026-02).",
             rounds=[rnd("2026-02-02", "Investment round ($16B at $126B post-money)", 16000000000,
                         "Dragoneer Investment Group, DST Global, Sequoia Capital", True, WAYMO, "company")]))

# Wealth.com: Anthos-led seed without GV; GV led the Series A (the /ai list's first 'Invested' month is 2024-09).
WEALTH_SEED = ("https://www.prnewswire.com/news-releases/wealth-launches-out-of-stealth-with-16m-in-seed-funding-to-"
               "bring-innovation-to-estate-planning-301507779.html")
WEALTH_A = ("https://www.wealth.com/resources/articles/wealth-com-secures-30-million-series-a-to-further-modernize-"
            "estate-planning-for-advisors/")
WEALTH_B = ("https://www.wealth.com/resources/press/wealth-com-raises-65-million-series-b-to-power-ai-future-of-wealth-"
            "management/")
L.append(cls("wealth-com", status="private", rng="below_1b", country="US", city="Tempe", focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=WEALTH_A,
             entry_date="2024-09-16", extra={"valuation_range_source": "web_verified", "valuation_citation": WEALTH_B},
             note="AI estate-planning platform for wealth advisors (offices in Tempe and New York; the 2022 seed release "
                  "and the Series B dateline place it in the Phoenix area). Seed $16M led by Anthos Capital (2022-03-22, "
                  "no GV). GV led the $30M Series A on 2024-09-16 (the company's own post), matching the firm's /ai list "
                  "('Invested' 2024-09). GV followed in the $65M Series B of 2026-04-16 led by Titanium Ventures, Pruven "
                  "Capital, The K Fund and Dynasty. Momentum check 2026-09-28 (Google News + the company's newsroom): "
                  "the Series B disclosed no valuation and no $1B+ priced round was found, so below_1b.",
             rounds=[rnd("2022-03-22", "Seed", 16000000, "Anthos Capital", False, WEALTH_SEED, "company"),
                     rnd("2024-09-16", "Series A", 30000000, "GV", True, WEALTH_A, "company"),
                     rnd("2026-04-16", "Series B", 65000000,
                         "Titanium Ventures, Pruven Capital, The K Fund, Dynasty Financial Partners", True, WEALTH_B,
                         "company")]))

# Weaveworks: Accel-led Series A (no GV); GV led the Series B; shut 2024-02.
WW_A = "https://techcrunch.com/2014/12/03/weaveworks-raises-5m/"
WW_B = ("https://techcrunch.com/2016/05/11/weaveworks-grabs-15-million-series-b-from-gv-to-bring-order-to-container-"
        "management/")
WW_SHUT = NEWS("weaveworks", "Weaveworks shuts its doors")
L.append(cls("weaveworks", status="defunct", rng="below_1b", focus="DevTools & APIs", country="GB",
             country_src="web_verified", country_cite=WW_A, city="London",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=WW_B, entry_date="2016-05-11",
             note="Kubernetes/GitOps tooling (Flux). Accel led the $5M Series A (TechCrunch 2014-12-03; GV not named). "
                  "GV led the $15M Series B (TechCrunch 2016-05-11: 'GV had not invested before'; Accel followed), so "
                  "the entry is Growth. Weaveworks announced on 2024-02-05 that it was shutting down commercial "
                  "operations after an acquisition fell through (TechCrunch), hence defunct; the Flux project lives on "
                  "at the CNCF. Sibling Accel still reads private: the shutdown is fresher cited evidence. London HQ: the Series A coverage "
                  "has the money expanding a US organization 'to complement its team in London'; aligned with Accel.",
             rounds=[rnd("2014-12-03", "Series A", 5000000, "Accel", False, WW_A, "press"),
                     rnd("2016-05-11", "Series B", 15000000, "GV", True, WW_B, "press"),
                     rnd("2020", "Funding round ($36M, end of 2020)", 36000000, None, None, WW_SHUT, "press")]))

# Wingu: Google Ventures invested in the stealth company by July 2011; no round named.
WINGU = "https://techcrunch.com/2011/07/07/google-invests-in-stealth-startup-that-aims-to-accelerate-science/"
L.append(cls("wingu", status="acquired", rng="below_1b", country="US", city="Cambridge", focus="Healthcare & Bio",
             stage="undetermined", entry_date="2011",
             note="Research-collaboration cloud software for pharma R&D (Cambridge MA). TechCrunch 2011-07-07: 'Google "
                  "Ventures has quietly invested in a stealth startup called Wingu', no amount or round named; no other "
                  "source read names the round, so the stage is undetermined. Acquired by PerkinElmer in 2014 (the "
                  "firm's own exit line, 'Acquired by PerkinElmer, 2014').",
             rounds=[rnd("2011-07", "Undisclosed (stealth)", None, None, True, WINGU, "press")]))

# Wonder: the firm's own post (Dave Munichiello, the partner on the row) says he backed Marc Lore at the Series A.
RD_WONDER = "https://www.restaurantdive.com/news/wonder-valuation-9-billion-latest-650m-funding/825417/"
BLUE = post_exact("blue-water-autonomy")
L.append(cls("wonder", status="private", rng="1b_plus", usd=9000000000, val_src="web_verified", val_cite=RD_WONDER,
             asof="2026-07-16", extra=WV, city="New York", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=BLUE, entry_date="2020",
             flags=["stage_disputes_band"],
             note="Marc Lore's food halls and delivery company (Wonder Group, New York). Stage disputes the Form D band: "
                  "the band read Wonder Group, Inc.'s first Form Ds (filed from 2024, rounds of $100M to $1.66B) as a "
                  "Growth entry, but the firm's own post by Dave Munichiello, the GV partner on the row, "
                  "says 'Founders whom I've backed at the Series A include ... Marc Lore (Wonder)'. Entry dated 2020 from "
                  "Wonder's 2023 tender-offer filing (" + FTS("Wonder Group", "SC TO-T") + "): 'Mr. Munichiello has served "
                  "as a director of Wonder since 2020'; the Series A's own amount and month are not on record. GV was an "
                  "existing investor in the May 2025 $600M round (with NEA, Accel, Forerunner) and the July 2026 $650M "
                  "Series D at a $9B pre-money valuation (Restaurant Dive, 2026-07-16). Mark aligned with BCV and "
                  "General Catalyst ($9B, 2026-07-16); Accel's below_1b carries no mark.",
             rounds=[rnd("2020", "Series A", None, None, True, BLUE, "firm"),
                     rnd("2025-05", "Funding round ($600M at $7B)", 600000000,
                         "New Enterprise Associates, Accel, Google Ventures, Forerunner", True, W("Wonder Group"),
                         "press"),
                     rnd("2026-07-16", "Series D", 650000000, None, True, RD_WONDER, "press")]))

# Wonder Workshop (Play-i): Google Ventures in the $1M seed (2013); a named Series B followed in 2016.
PLAYI = NEWS("wonder-workshop", "Play-i want to bring a robot")
WW_SERIES_B = NEWS("wonder-workshop", "Wonder Workshop announces Series B")
L.append(cls("wonder-workshop", status="acquired", rng="below_1b", city="San Mateo", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PLAYI, entry_date="2013",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=WW_SERIES_B,
             note="Educational coding robots Dash and Dot (Play-i, renamed Wonder Workshop; Silicon Valley, San Mateo). "
                  "Robohub 2013-10-29: Play-i came out of stealth 'after receiving a $1million seed fund round from "
                  "investors like Google Ventures', so the entry is that 2013 seed. Graduated: the company later raised "
                  "a named Series B, $20M co-led by WI Harper and Idea Bulb (ZDNet 2016-07-28), after a $6.9M 2015 round "
                  "(WI Harper, Madrona, CRV), and a $41M round led by Tencent in 2017. Acquired: the Wonder Workshop "
                  "brand and its Dash robots now sell under 'MORAVIA Education, Inc' of Celebration, Florida "
                  "(makewonder.com, read 2026-09-28); the acquisition date and price were not found, so the note keeps "
                  "the successor only. City is the company's own last HQ, San Mateo.",
             rounds=[rnd("2013", "Seed", 1000000, None, True, PLAYI, "press"),
                     rnd("2015-05", "Funding round ($6.9M)", 6900000, "WI Harper, Madrona, CRV", None,
                         NEWS("wonder-workshop", "Edtech company Wonder Workshop raises"), "press"),
                     rnd("2016-07-28", "Series B", 20000000, "WI Harper Group, Idea Bulb Ventures", None, WW_SERIES_B,
                         "press"),
                     rnd("2017-10-30", "Funding round ($41M)", 41000000, "Tencent", None,
                         NEWS("wonder-workshop", "Wonder Workshop raises $41M for its chatty"), "press")]))

# Wonderbly (Lost My Name): GV led the $9M Series A; Graphite Capital bought it in 2021, Penguin Random House in 2025.
GUARD = NEWS("wonderbly", "tells a $9m funding tale")
L.append(cls("wonderbly", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=GUARD, city="London", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Wonderbly"),
             entry_date="2015-06-25",
             note="Personalised children's books (Lost My Name, renamed Wonderbly; London). The Guardian 2015-06-25: the "
                  "London firm's $9M round was 'led by Google Ventures with ... Greycroft and The Chernin Group'; "
                  "Wikipedia names it the Series A. Earlier money was small angel funding and a Dragons' Den deal, "
                  "without GV. Ravensburger led an $8.5M Series B in July 2017. Graphite Capital bought the company in "
                  "July 2021 (the firm's own exit line) and Penguin Random House acquired it in June 2025 (Wikipedia).",
             rounds=[rnd("2015-06-25", "Series A", 9000000, "Google Ventures", True, GUARD, "press"),
                     rnd("2017-07", "Series B", 8500000, "Ravensburger", None, W("Wonderbly"), "press")]))

# Xilis: GV joined the Mubadala-led $70M Series A (a new investor), per Duke's own release.
DUKE_XILIS = NEWS("xilis", "Cancer treatment startup started by Duke")
L.append(cls("xilis", status="private", rng="below_1b", city="Durham", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=DUKE_XILIS,
             entry_date="2021-07-08",
             note="MicroOrganoSphere precision-oncology platform (Duke spin-out, Durham NC). Duke's release 2021-07-08: a "
                  "$70M Series A led by Mubadala Capital, 'joined by new investors GV (formerly Google Ventures)', LSP, "
                  "Catalio and others; Felicis, Two Sigma and Pear were existing investors. The Series A was extended to "
                  "over $89M in July 2022; a $19.4M Form D followed in 2025. The 2022 Form D names Wesley Chan, "
                  "Felicis's partner, not a GV seat. Entry date from the round's own release, not the Form D anchor.",
             rounds=[rnd("2021-07-08", "Series A", 70000000, "Mubadala Capital", True, DUKE_XILIS, "press"),
                     rnd("2022-07-13", "Series A extension (total over $89M)", None, None, None,
                         NEWS("xilis", "Xilis Announces Series A Extension"), "company")]))

# Yellowbrick Data: Google Ventures in the Series A (announced at the July 2018 stealth exit).
YB_A = "https://siliconangle.com/2018/07/31/yellowbrick-data-exits-stealth-44m-flash-data-warehouse/"
YB_B = "https://siliconangle.com/2018/10/23/flash-data-warehouse-startup-yellowbrick-data-raises-48m/"
YB_C = "https://techcrunch.com/2019/06/05/yellowbrick-data-raises-81m-series-c-for-hybrid-data-warehouse/"
L.append(cls("yellowbrick-data", status="private", rng="below_1b", country="US", city="Mountain View",
             focus="Data Infrastructure", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=YB_A, entry_date="2018-07",
             note="Hybrid-cloud data warehouse (Mountain View). SiliconANGLE 2018-07-31, at the stealth exit with $44M: "
                  "'Draper Fisher Jurvetson, Google Ventures, Menlo Ventures, Samsung Ventures and Third Point Ventures "
                  "all participating in the Series A'. Menlo dates its own Series A entry to 2015, so the round may have "
                  "closed in parts before its announcement; the entry date is the announcement's (medium confidence). "
                  "Next47 led the $48M Series B (October 2018); DFJ Growth led the $81M Series C with GV as an existing "
                  "investor (June 2019); a $75M Series C1 followed in November 2021. No priced round at $1B+ found; "
                  "aligned with Menlo and IVP (private, below_1b, Mountain View).",
             rounds=[rnd("2018-07-31", "Series A", None, None, True, YB_A, "press"),
                     rnd("2018-10-23", "Series B", 48000000, "Next47", None, YB_B, "press"),
                     rnd("2019-06-05", "Series C", 81000000, "DFJ Growth", True, YB_C, "press"),
                     rnd("2021-11-03", "Series C1", 75000000, None, None,
                         "https://siliconangle.com/2021/11/03/data-warehouse-startup-yellowbrick-data-lands-75m-series-"
                         "c1-funding/", "press")]))

# Yesware: seed (Form D band, prefilled) confirmed by press; a named Series A followed with GV again.
YW_SEED = ("https://techcrunch.com/2011/09/27/google-ventures-foundry-group-put-1m-in-email-tracking-and-productivity-"
           "platform-for-salespeople-yesware/")
YW_A = ("https://techcrunch.com/2012/06/20/yeswares-email-platform-for-salespeople-rasies-4-million-from-idg-google-"
        "ventures-foundry-group-others/")
L.append(cls("yesware", status="acquired", rng="below_1b", city="Boston", focus="SaaS",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=YW_A,
             note="Email tracking and sales engagement (Boston). The prefilled Seed is borne out by TechCrunch "
                  "2011-09-27: $1M 'from Google Ventures, Foundry Group and other investors'. Graduated: IDG Ventures led "
                  "a named $4M Series A with 'seed investors Google Ventures, Foundry Group' (TechCrunch 2012-06-20; the "
                  "article also has the company moving from Cambridge to Boston); the Form D layer agrees (a $14.7M "
                  "raise in 2013). Acquired by Vendasta (the firm's own exit line; Battery's row dates it 2022); "
                  "aligned with Battery on status and city.",
             rounds=[rnd("2011", "Seed", 1000000, "Google Ventures, Foundry Group", True, YW_SEED, "press"),
                     rnd("2012-06-20", "Series A", 4000000, "IDG Ventures", True, YW_A, "press")]))

# Yieldify: Hoxton-backed seed without GV; SoftBank Capital and Google Ventures in the $11.5M Series A.
YF_A = ("https://techcrunch.com/2015/06/25/uk-martech-startup-yieldify-raises-11-5m-from-softbank-and-google-"
        "ventures/")
L.append(cls("yieldify", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
             country_cite=YF_A, city="London", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=YF_A, entry_date="2015-06-25",
             note="Conversion and on-site marketing software (London). TechCrunch 2015-06-25: the London company's $11.5M "
                  "Series A came from SoftBank Capital and Google Ventures, Avid Larizadeh Duggan leading GV's side; the "
                  "earlier ~$1.2M (Hoxton Ventures, Robin Klein) did not include GV. A further $6M followed in May 2017. "
                  "Acquired by Publicis Groupe in 2023 (the firm's own exit line).",
             rounds=[rnd("2014", "Seed (~$1.2M)", 1200000, None, False, YF_A, "press"),
                     rnd("2015-06-25", "Series A", 11500000, "SoftBank Capital, Google Ventures", True, YF_A, "press"),
                     rnd("2017-05-03", "Funding round ($6M)", 6000000, None, None,
                         "https://techcrunch.com/2017/05/03/yieldify-raises-another-6m-appoints-adtech-vet-john-"
                         "giuliani-as-chairman/", "press")]))

# Yieldmo: Series A prefilled (Form D band, Rich Miner a director); Multiply took a stake in 2020, company still private.
YM_MULTIPLY = NEWS("yieldmo", "Multiply acquires stake in US digital advertising")
L.append(cls("yieldmo", status="private", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
             note="Mobile ad formats and attention analytics (New York, per Wikipedia). Still private: Abu Dhabi's "
                  "Multiply (an IHC subsidiary) bought a stake in September 2020 to finance growth, which Campaign "
                  "Middle East reports as an investment alongside Google Ventures and Union Square Ventures, not a "
                  "takeover; no exit line on the firm's list. No priced round at $1B+ on record. Aligned with USV "
                  "(private, below_1b, New York).",
             rounds=[rnd("2014-10", "Series C (as Wikipedia names it)", None, "Time Warner Investments", None, W("Yieldmo"), "press"),
                     rnd("2020-09-15", "Strategic stake (Multiply)", None, "Multiply", None, YM_MULTIPLY, "press")]))

# Yuga Labs: on the firm's live list since 2022, but no source read ties GV to a round.
YUGA_SEED = "https://techcrunch.com/2022/03/22/bored-apes-nft-startup-yuga-labs-raises-at-monster-4-billion-valuation/"
L.append(cls("yuga-labs", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified", val_cite=YUGA_SEED,
             asof="2022-03", extra=WV, flags=["stale"], country="US", city="Miami", focus="Crypto & Web3",
             stage="undetermined",
             note="Bored Ape Yacht Club studio (Miami). The only priced round on record is the $450M seed at $4B led by "
                  "Andreessen Horowitz (TechCrunch 2022-03-22), whose investor list (Animoca, LionTree, Sound Ventures, "
                  "Thrive, FTX, MoonPay) does not name GV; the firm has listed Yuga since 2022 (David Krane, Tom Hulme) "
                  "but no post, filing or press item read names the round GV bought, so the stage is undetermined. "
                  "Mark aligned with a16z and Lightspeed ($4B, 2022-03), stale; Lightspeed's row notes a reported 2026 "
                  "secondary near half that, still above $1B and not a primary mark.",
             rounds=[rnd("2022-03-22", "Seed", 450000000, "Andreessen Horowitz", None, YUGA_SEED, "press")]))

# ZappRx: SR One-led Series A without GV; GV in the Qiming-led Series B.
ZX_A = "https://techcrunch.com/2015/04/02/zapprx-raises-5-6-million-in-series-a-funding-to-expand-the-company/"
ZX_B = ("https://techcrunch.com/2017/04/20/zapprx-gets-25-million-from-chinese-vcs-hoping-to-tap-into-the-u-s-drug-"
        "prescription-market/")
L.append(cls("zapprx", status="acquired", rng="below_1b", city="Boston", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=ZX_B, entry_date="2017-04-20",
             note="Specialty-medication prescribing platform (Boston). SR One led the $5.6M Series A with Atlas (TechCrunch "
                  "2015-04-02, GV not named); 'GV (formerly Google Ventures) and ... SR One were also in' the $25M Series "
                  "B led by Qiming US (TechCrunch 2017-04-20), matching the firm's first listing in 2017, so the entry "
                  "is Growth. Acquired by Allscripts in 2019 (Wikipedia's Allscripts/Veradigm history; the firm's exit "
                  "line).",
             rounds=[rnd("2013-09-05", "Seed", 1000000, None, None,
                         "https://techcrunch.com/2013/09/05/zapprx-lands-1m-to-rethink-prescription-processing-with-a-"
                         "pharmacy-agnostic-mobile-checkout-platform/", "press"),
                     rnd("2015-04-02", "Series A", 5600000, "SR One", None, ZX_A, "press"),
                     rnd("2017-04-20", "Series B", 25000000, "Qiming US", True, ZX_B, "press")]))

# Zencoder: YC company, a ~$2M Series A in April 2011; bought by Brightcove for $30M in July 2012. GV's round not named.
ZC_ACQ = "https://techcrunch.com/2012/07/26/brightcove-q2-2012-earnings/"
L.append(cls("zencoder", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs", stage="undetermined",
             note="Cloud video-encoding API and the VideoJS player (Y Combinator, San Francisco). TechCrunch 2012-07-26: "
                  "Brightcove paid $30M for Zencoder, which had 'raised just $2 million, mostly through a Series A round "
                  "raised in April 2011'. No source read names GV in that or any round (Google News and TechCrunch's own "
                  "search), so the stage is undetermined; the firm lists it as exited ('Acquired by Brightcove, 2012'). "
                  "The 2024-26 AI coding company named Zencoder is unrelated. Aligned with a16z and YC.",
             rounds=[rnd("2011-04", "Series A", None, None, None, ZC_ACQ, "press")]))

# Zephyr Health: Kleiner/Jafco co-led $15M (2014, GV not named); Anju bought it in October 2018.
ANJU = "https://www.anjusoftware.com/about/all-news/press-releases/1921"
ZH_2014 = ("https://techcrunch.com/2014/01/08/zephyr-health-lands-15m-from-kleiner-to-help-life-sciences-navigate-big-"
           "data-bring-therapies-to-market-faster/")
L.append(cls("zephyr-health", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Healthcare & Bio", stage="undetermined",
             note="Life-sciences data and insights platform. Anju Software's release of 2018-10-02 (linked from the "
                  "firm's own listing) announces the acquisition of 'San Francisco-based Zephyr Health', 'venture backed "
                  "by Kleiner Perkins Caufield & Byers, Icon Ventures, and Google Ventures'. The $15M round of January "
                  "2014 was co-led by Kleiner Perkins and Jafco without naming GV (TechCrunch); the firm first lists the "
                  "company in 2015 (Blake Byers), and no source read names the round GV joined, so undetermined.",
             rounds=[rnd("2014-01-08", "Funding round ($15M)", 15000000, "Kleiner Perkins, Jafco Ventures", None,
                         ZH_2014, "press"),
                     rnd("2018-10-02", "Acquired by Anju Software", None, "Anju Software", True, ANJU, "company")]))

# Zest: GV led the $4M seed (2022); New York company; the Wikidata GB was a wrong one-word join.
ZEST_TC = "https://techcrunch.com/2022/11/15/zest-wants-to-make-buying-and-sending-gifts-online-delightful/"
ZEST_PP = "https://www.zest.co/legal/privacy-policy"
L.append(cls("zest", status="private", rng="below_1b", country="US", country_src="web_verified", country_cite=ZEST_PP,
             city="New York", city_src="web_verified", focus="SaaS", flags=["model_disputes_source"],
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=ZEST_TC, entry_date="2022-11-15",
             note="Gifting checkout and storefront software for e-commerce brands (zest.co), founded 2022 by Alex Ingram "
                  "and Jeremy Feinstein, ex-Flatiron Health. TechCrunch 2022-11-15: '$4 million in seed funding led by "
                  "GV' with BoxGroup, Character, Operator Partners, Bungalow and Company Ventures. Country and city from "
                  "the company's own privacy policy (an East 49th Street, New York NY 10017 address; Manhattan venue in "
                  "its terms), so the Wikidata GB was a one-word join to another Zest and is disputed. No later round "
                  "found. " + GRAD_LEFT,
             rounds=[rnd("2022-11-15", "Seed", 4000000, "GV", True, ZEST_TC, "press")]))

# BridgeBio Oncology Therapeutics: Series A bought only by BridgeBio Pharma; GV in the $200M Series B (2024).
BBIO_8K = "https://www.sec.gov/Archives/edgar/data/1743881/000095017024051573/bbio-ex99_1.htm"
BBOT_S1 = FTS("BridgeBio Oncology", "S-1")
BBOT_CAP = "https://stockanalysis.com/stocks/bbot/market-cap/"
L.append(cls("bridgebio-oncology-therapeutics", rng="below_1b", usd=305460000, val_src="web_verified",
             val_cite=BBOT_CAP, asof="2026-09-28", extra=WV, country="US", city="South San Francisco",
             city_src="web_verified", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BBIO_8K, entry_date="2024-05",
             note="RAS-pathway oncology company spun out of BridgeBio Pharma (South San Francisco, per its S-1). The S-1's "
                  "related-party section: the Series A preferred (2023 to April 2024, $79.2M) went only to a BridgeBio "
                  "Pharma subsidiary, and the Series B preferred ($200M, April to May 2024) went to outside investors. "
                  "BridgeBio Pharma's release of 2024-05-02 names GV among the participants in that $200M financing (led "
                  "by Cormorant, co-led by Omega), so GV entered at the Series B: Growth. Listed through the August 2025 "
                  "merger with Helix Acquisition Corp. II; GV 2023, L.P. holds 2,823,126 shares in the S-1's selling "
                  "holder table. Value is the market cap, $305.46M on 2026-09-28 (stockanalysis.com), replacing the "
                  "2025 float as the canonical figure; the band is unchanged.",
             rounds=[rnd("2023-01", "Series A", 79200000, "BridgeBio Pharma", False, BBOT_S1, "filing"),
                     rnd("2024-05-02", "Series B", 200000000, "Cormorant Asset Management", True, BBIO_8K, "filing")]))

# Airware: a16z led the $10.7M Series A 'backed by Google Ventures' (2013); shut 2018, Delair took software and IP.
AW_A = "https://techcrunch.com/2013/05/15/airware-raises-10-7m-to-build-brains-for-unmanned-drones/"
AW_END = "https://techcrunch.com/2018/10/29/fresh-drones-of-delair/"
L.append(cls("airware", rng="below_1b", city="San Francisco", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AW_A, entry_date="2013-05-15",
             note="Commercial drone operating system and analytics (Y Combinator W13, San Francisco). TechCrunch "
                  "2013-05-15: the $10.7M Series A 'is led by Andreessen Horowitz, and backed by Google Ventures', after "
                  "a small seed that does not name GV. Kleiner led a $25M round in 2014 and Next World Capital a $30M "
                  "Series C in 2016. Airware shut in September 2018; Delair bought its Redbird analytics software and IP "
                  "and took 26 staff while the hardware went to auction (TechCrunch 2018-10-29), so the prefilled "
                  "acquired stands (a16z and Felicis read acquired; First Round and YC read defunct).",
             rounds=[rnd("2013-05-15", "Series A", 10700000, "Andreessen Horowitz", True, AW_A, "press"),
                     rnd("2014-07-23", "Funding round ($25M)", 25000000, "Kleiner Perkins", None,
                         "https://techcrunch.com/2014/07/23/airware-drone-operating-system/", "press"),
                     rnd("2016-03", "Series C", 30000000, "Next World Capital", None, W("Airware"), "press")]))

# Abundant Robotics: GV led the $10M Series A (2017) after a $2M seed; shut 2021, Wavemaker bought the IP.
AB_A = "https://techcrunch.com/2017/05/03/abundant-robotics-rakes-in-10-million-for-apple-harvesting-robots/"
AB_END = ("https://techcrunch.com/2022/02/02/abundants-new-owner-looks-to-revive-the-apple-picking-robot-through-equity-"
          "crowdfunding/")
L.append(cls("abundant-robotics", status="acquired", rng="below_1b", country="US", city="Hayward",
             focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AB_A, entry_date="2017-05-03",
             note="Apple-harvesting robots (SRI International spin-out). TechCrunch 2017-05-03: 'GV ... is leading a $10 "
                  "million investment', the Series A, after $2M of seed funding (SRI Ventures spin-out, GV not named). "
                  "The Hayward company closed in summer 2021; Wavemaker Labs bought its IP in October 2021 and revived "
                  "it under new leadership (TechCrunch 2022-02-02), so the row reads acquired out of the shutdown, with "
                  "Wavemaker as successor.",
             rounds=[rnd("2016", "Seed", 2000000, None, None, AB_A, "press"),
                     rnd("2017-05-03", "Series A", 10000000, "GV", True, AB_A, "press"),
                     rnd("2021-10", "IP sold to Wavemaker Labs", None, "Wavemaker Labs", None, AB_END, "press")]))

# BackOps: angel seed (no GV); Google Ventures in the $7M Series A co-led by Sherpa and e.ventures.
BO_SEED = ("https://techcrunch.com/2012/11/30/backops-raises-1-5m-to-outsource-your-startups-back-office-and-"
           "eventually-any-back-office/")
BO_A = ("https://techcrunch.com/2013/07/11/backops-raises-7m-to-build-an-army-of-moms-for-managing-startups-and-small-"
        "businesses-with-leading-saas-tools/")
L.append(cls("backops", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=BO_A, entry_date="2013-07-11",
             note="Back-office-as-a-service for startups and small businesses. TechCrunch 2013-07-11: the $7M Series A "
                  "was co-led by Sherpa Ventures and e.ventures 'and includes Google Ventures', the existing seed "
                  "investors being CrunchFund and Mark Pincus (the $1.5M seed of November 2012 names no GV). Status "
                  "aligned with Headline's row: merged in 2016 with the founder's Scalus into HireAthena.",
             rounds=[rnd("2012-11-30", "Seed", 1500000, None, False, BO_SEED, "press"),
                     rnd("2013-07-11", "Series A", 7000000, "Sherpa Ventures, e.ventures", True, BO_A, "press")]))

# Amino (Narvii, New York): USV's own post puts Google Ventures in the 2014 Series A.
USV_AMINO = "https://www.usv.com/writing/2014/07/amino/"
L.append(cls("amino", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=USV_AMINO,
             entry_date="2014-07-08",
             note="Amino Apps (Narvii), mobile interest communities, New York. USV's own post of 2014-07-08 announces its "
                  "Series A investment with co-investors 'Google Ventures, SV Angel, Box Group, Kal Vepuri and Slow "
                  "Ventures'; Wikipedia calls the same 2014 money a $1.65M seed 'primarily from Union Ventures' with "
                  "Google Ventures, so the label rests on the lead's own contemporaneous word (medium). MediaLab bought "
                  "the app (January 2020 per USV's row, January 2021 per Wikipedia) and the platform stopped in December "
                  "2025: acquired, aligned with USV. First Round's 'Amino' is Amino Payments of Philadelphia, a "
                  "different company.",
             rounds=[rnd("2014-07-08", "Series A (Wikipedia: $1.65M seed)", 1650000, "Union Square Ventures", True,
                         USV_AMINO, "firm")]))

# Buttercoin: Google Ventures (via Kevin Rose and Chris Hutchins) in the ~$1M seed of 2013; shut April 2015.
BC_SEED = "https://techcrunch.com/2013/09/18/centralway-fund-buttercoin-seed/"
BC_END = "https://techcrunch.com/2015/04/06/buttercoin-bitcoin-closing/"
L.append(cls("buttercoin", status="defunct", rng="below_1b", country="US", city="New York", focus="Crypto & Web3",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BC_END, entry_date="2013",
             note="Bitcoin exchange (Y Combinator S13). TechCrunch 2015-04-06: 'Google Ventures participated in the seed "
                  "round through Kevin Rose and Chris Hutchins'; TechCrunch 2013-09-18 dates that seed (about $1M "
                  "before Centralway's $250k on the same terms, total ~$1.6M) to 2013. Shut its service on 2015-04-10 "
                  "after failing to raise more (TechCrunch 2015-04-06): defunct. City aligned with YC's directory row "
                  "(New York). " + GRAD_LEFT,
             rounds=[rnd("2013", "Seed", 1600000, None, True, BC_SEED, "press")]))

# Breather (Montreal): Series A to C led by RRE, Valar, Menlo; GV's own round not found; Industrious took the assets.
BR_WIKI = "https://en.wikipedia.org/wiki/Breather_(company)"
L.append(cls("breather", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
             country_cite=BR_WIKI, city="Montreal", focus="Consumer & Marketplaces", stage="undetermined",
             note="On-demand private rooms and flexible workspace, 'based in Montreal, Canada' (Wikipedia), confirming the "
                  "Wikidata country. Rounds read: $6M Series A led by RRE (2014), $20M Series B from Valar (2015), $40M "
                  "Series C led by Menlo (December 2016); none names GV, which the firm first lists in 2017, and the "
                  "$122.5M raised by June 2018 implies a later round not found, so undetermined. Industrious acquired "
                  "key assets of Breather's platform in May 2021 (Wikipedia): acquired.",
             rounds=[rnd("2014-09-04", "Series A", 6000000, "RRE Ventures", None,
                         "https://techcrunch.com/2014/09/04/breather-series-a/", "press"),
                     rnd("2015-09-17", "Series B", 20000000, "Valar Ventures", None,
                         "https://techcrunch.com/2015/09/17/breather-raises-20m-from-peter-thiels-valar-ventures-to-"
                         "expand-its-on-demand-private-room-business/", "press"),
                     rnd("2016-12-07", "Series C", 40000000, "Menlo Ventures", None,
                         "https://techcrunch.com/2016/12/07/breather-raises-40-million-for-stylish-workspaces-on-"
                         "demand/", "press")]))

# AVOS Systems (Chad Hurley, Steve Chen): turned into MixBit in 2014; MixBit stopped in August 2018.
AVOS_TC = ("https://techcrunch.com/2014/06/06/youtube-co-founders-break-up-as-chad-hurley-spins-out-his-own-company-and-"
           "steve-chen-joins-google-ventures/")
L.append(cls("avos-systems", status="defunct", rng="below_1b", city="San Mateo", focus="Media, Gaming & Advertising",
             stage="undetermined",
             note="The YouTube founders' internet company (Delicious, Zeen, MixBit). TechCrunch 2014-06-06: AVOS sold "
                  "Delicious and turned from an incubator into a single company working on MixBit, with offices in San "
                  "Mateo and New Zealand. MixBit ceased operations on 2018-08-21 (Wikipedia's MixBit article), so "
                  "defunct. A Series A closed in April 2012 (FinSMEs headline) but no source read names GV in it, so "
                  "the stage is undetermined.",
             rounds=[rnd("2012-04-27", "Series A", None, None, None,
                         NEWS("avos-systems", "AVOS Systems Closes Series A"), "press")]))

# Agent (Tagstand): YC company that pivoted Tagstand -> Agent -> Status; the founders then started Zeus Living.
ZEUS_TC = "https://techcrunch.com/2019/03/15/zeus-corporate-housing/"
L.append(cls("agent", status="unknown", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Agent, the context-aware Android app on the firm's 2014-19 archived list, was Tagstand's product: "
                  "TechCrunch 2019-03-15 says Kulveer Taggar's Y Combinator-backed 'NFC-triggered task launcher "
                  "Tagstand ... pivoted into app settings configurer Agent, which pivoted into automatic location "
                  "sharing app Status', before he co-founded Zeus Living in 2016. No source read names GV's round or "
                  "gives the company's own end (shutdown or sale), so status is unknown and the stage undetermined.",
             rounds=[]))

# Apportable: Google Ventures in the $2.4M round of July 2013 (unnamed); a $5M round followed in 2014.
AP_TC = ("https://techcrunch.com/2014/02/05/used-by-zynga-pocket-gems-and-more-apportable-lands-5m-to-help-developers-"
         "automatically-convert-ios-games-to-android/")
L.append(cls("apportable", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="DevTools & APIs", stage="undetermined", entry_date="2013-07",
             note="iOS-to-Android cross-compiler (Y Combinator W11, San Francisco). TechCrunch 2014-02-05: in July 2013 "
                  "Apportable raised $2.4M 'from Initialized Capital and Google Ventures, among others', then $5M from "
                  "Initialized, Danhua Capital and Y Combinator. Neither round is named in any source read, so the stage "
                  "is undetermined, dated by the July 2013 round. Status aligned with YC's directory (acquired); no "
                  "sale document was read.",
             rounds=[rnd("2013-07", "Funding round ($2.4M)", 2400000, "Initialized Capital", True, AP_TC, "press"),
                     rnd("2014-02-05", "Funding round ($5M)", 5000000, None, None, AP_TC, "press")]))

# AppStack: $1.5M seed with Google Ventures and Eric Schmidt's Tomorrow Ventures (March 2012).
AS_TC = ("https://techcrunch.com/2012/03/27/appstack-raises-1-5m-from-eric-schmidt-google-ventures-gary-vee-and-"
         "others/")
L.append(cls("appstack", status="unknown", rng="below_1b", country="US", focus="Media, Gaming & Advertising",
             flags=["city_unknown"],
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AS_TC, entry_date="2012-03-27",
             note="Hosted mobile sites plus Google mobile ads for local businesses (founder Steve Espinosa; 'Google's "
                  "biggest reseller of mobile ads'). TechCrunch 2012-03-27: a '$1.5 million seed round' with Google "
                  "Ventures and Eric Schmidt's Tomorrow Ventures involved. No source read gives its fate (the appstack.com "
                  "domain is now for sale) or its city, so status unknown and city_unknown. " + GRAD_LEFT,
             rounds=[rnd("2012-03-27", "Seed", 1500000, None, True, AS_TC, "press")]))

# Airy Labs: $1.5M seed from Google Ventures, Foundation Capital and Rick Thompson (August 2011).
AIRY_TC = ("https://techcrunch.com/2011/08/03/social-learning-game-developer-airy-labs-raises-1-5m-from-google-ventures-"
           "others/")
AIRY_CUTS = "https://techcrunch.com/2012/02/11/airy-labs-big-cuts/"
L.append(cls("airy-labs", status="unknown", rng="below_1b", country="US", focus="Media, Gaming & Advertising",
             flags=["city_unknown"],
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AIRY_TC, entry_date="2011-08-03",
             note="Social learning games for children, founded 2011 by Thiel Fellow Andrew Hsu (StartX). TechCrunch "
                  "2011-08-03: '$1.5 million in seed funding from Google Ventures, Foundation Capital and Playdom founder "
                  "Rick Thompson'. TechCrunch 2012-02-11 reported deep staff cuts; no source read gives the company's "
                  "end or its city, so status unknown and city_unknown. Cherry's 'Airy' (Berlin messaging platform) is a "
                  "different company. " + GRAD_LEFT,
             rounds=[rnd("2011-08-03", "Seed", 1500000, None, True, AIRY_TC, "press")]))

# Backplane: Google Ventures in the $1.8M seed; a named Series A followed in February 2012; assets sold in 2016.
BP_SEED_A = ("https://techcrunch.com/2012/02/16/lady-gaga-backed-backplane-raises-over-4m-from-sequoia-more-acquires-"
             "sharing-platform-cortex/")
BP_JAN = ("https://techcrunch.com/2012/01/20/first-look-backplane-the-lady-gaga-backed-community-platform-with-all-star-"
          "investors-invites/")
BP_END = "https://techcrunch.com/2016/04/11/too-close-to-the-sun/"
L.append(cls("backplane", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BP_SEED_A, entry_date="2012-01",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=BP_SEED_A,
             note="Community-platform startup co-founded by Lady Gaga's manager Troy Carter (Little Monsters). TechCrunch "
                  "2012-02-16: Backplane 'raised an early ... seed round' of $1.8M from investors 'including Google "
                  "Ventures, Founders Fund Angel, Menlo Ventures, SV Angel, i/o Ventures, and Tomorrow Ventures', and "
                  "the same day closed a named Series A of $4-5M (Sequoia, Greylock Discovery, Battery, Formation 8), so "
                  "the seed graduated. Entry dated by TechCrunch 2012-01-20, the first piece naming Google Ventures in "
                  "the round. In April 2016 Backplane ran out of money and sold its assets to a group of previous and "
                  "new investors who meant to restart it (TechCrunch 2016-04-11): acquired out of insolvency.",
             rounds=[rnd("2012-01", "Seed", 1800000, "Tomorrow Ventures", True, BP_JAN, "press"),
                     rnd("2012-02-16", "Series A", 4500000, None, None, BP_SEED_A, "press"),
                     rnd("2016-04-11", "Asset sale to previous and new investors", None, None, None, BP_END, "press")]))

# Carnival Labs (Carnival.io): GV in the $2.4M 2013 round; Sailthru bought it in April 2016. The prefilled public
# $25.1B was Carnival Corporation's float (a cik_weak name join).
CARN_TC = ("https://techcrunch.com/2014/01/10/newly-launched-marketing-platform-carnival-wants-brands-to-stop-treating-"
           "mobile-like-a-billboard/")
CARN_GV = "https://globalventuring.com/gv-celebrates-carnival-io-exit"
CARN_ACQ = "https://www.mediapost.com/publications/article/272959/sailthru-acquires-carnivalio-for-mobile-personali.html"
NOT_PUBLIC = {"is_public": False, "public_since": None, "valuation_source": None, "valuation_asof": None,
              "valuation_range_source": None, "valuation_confidence": None}
L.append(cls("carnival-labs", status="acquired", rng="below_1b", extra=NOT_PUBLIC, flags=["model_disputes_source"],
             country="US", city="New York", focus="SaaS", stage="undetermined", entry_date="2013",
             note="Mobile marketing automation (push, in-app messaging), later Carnival.io. The prefilled public/$25.1B "
                  "is Carnival Corporation's float joined on the name (cik_weak) and is disputed: Global Venturing: "
                  "'The company, then known as Carnival Labs, raised $2.4m in 2013 from GV, then called Google Ventures, "
                  "Lerer Ventures, Flybridge ...', and GV exited when Sailthru bought the 'US-based' company (MediaPost, "
                  "2016-04-07; terms undisclosed). TechCrunch 2014-01-10 has the round led by Gary Vaynerchuk and Lerer "
                  "Ventures and the company 'based in New York and New Zealand'. The round is not named, so the stage is "
                  "undetermined.",
             rounds=[rnd("2013", "Funding round ($2.4M)", 2400000, "Gary Vaynerchuk, Lerer Ventures", True, CARN_GV,
                         "press"),
                     rnd("2016-04-07", "Acquired by Sailthru", None, "Sailthru", True, CARN_ACQ, "press")]))

# Cluster (Cluster Labs): GV among the investors in the $1.6M raised for Cluster; the team joined Google in 2016 while
# the app kept running, now under the makers' own company Fotoloce. The prefilled public/$4,399 was a wrong float join.
LK_GOOGLE = ("https://techcrunch.com/2016/07/27/launchkit-team-heads-to-google-and-open-sources-its-tools-for-helping-"
             "devs-launch-their-apps/")
CLUSTER_ABOUT = "https://cluster.co/about/"
CLUSTER_2014 = ("https://techcrunch.com/2014/05/22/mobile-photo-sharing-app-cluster-now-focused-on-private-groups-adds-"
                "support-for-video-notes-and-tablets/")
L.append(cls("cluster", status="private", rng="below_1b", extra=NOT_PUBLIC, flags=["model_disputes_source"],
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CLUSTER_2014, entry_date="2013",
             note="Private group photo-sharing app (Cluster Labs: Brenden Mulligan, Taylor Hughes, Riz Sattar). The "
                  "prefilled public/$4,399 is another registrant's float joined on the name (cik_weak) and is disputed. "
                  "TechCrunch 2014-05-22: 'the startup raised $1.6 million in seed funding last year from First Round, "
                  "Freestyle, Google Ventures, Sherpa Ventures' and Steve Anderson, so the entry is the 2013 seed. "
                  "TechCrunch 2016-07-27: $600k more went into LaunchKit and the team then joined Google, open-sourcing "
                  "LaunchKit. Status departs from First Round's 'defunct': the Cluster app still runs in 2026, built and "
                  "maintained by its makers under their own small company, Fotoloce ('We built Cluster', cluster.co/about "
                  "read 2026-09-28), so the business operates and the acqui-hire decides nothing (s6). Flagged for "
                  "review. " + GRAD_LEFT,
             rounds=[rnd("2013", "Seed", 1600000, None, True, CLUSTER_2014, "press"),
                     rnd("2015", "Funding for LaunchKit ($600k)", 600000, None, None, LK_GOOGLE, "press")]))

# Beamable (formerly Disruptor Beam, Boston): Series A-B and the 2021 $5M name no GV; Skillz bought it in January 2026.
BEAM_2021 = NEWS("beamable", "Beamable raises $5 million for Unity-based")
L.append(cls("beamable", status="acquired", rng="below_1b", country="US", city="Boston", focus="DevTools & APIs",
             stage="undetermined",
             note="Live-services backend and SDK for game developers, relaunched in 2020 from the 'Boston-based' game "
                  "studio Disruptor Beam (TechCrunch 2017-02-02, 2020-04-21), which went through a Subchapter V "
                  "reorganization. Rounds read: $3.2M Series A (GrandBanks), a 2017 Series B led by GrandBanks and "
                  "Romulus, and a $5M round in February 2021 led by Companyon Ventures and GrandBanks (GamesBeat); none "
                  "names GV, which the firm's archive lists from 2020, so undetermined. Skillz acquired Beamable in "
                  "January 2026 (Wikipedia).",
             rounds=[rnd("2017-02-02", "Series B", 8500000, "GrandBanks Capital, Romulus Capital", None,
                         "https://techcrunch.com/2017/02/02/disruptor-beam-series-b/", "press"),
                     rnd("2021-02-23", "Funding round ($5M)", 5000000, "Companyon Ventures, GrandBanks Capital", None,
                         BEAM_2021, "press"),
                     rnd("2026-01", "Acquired by Skillz", None, "Skillz", None, W("Beamable"), "press")]))

# 2nd Address (formerly HomeSuite): GV led a $10M round in February 2019 (unnamed); HomeSuite's 2015 round had no GV.
TWO_A = ("https://techcrunch.com/2019/02/04/2nd-address-picks-up-10m-from-gv-foundation-to-take-on-airbnb-in-business-"
         "travel/")
L.append(cls("2nd-address", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined", entry_date="2019-02-04",
             note="Furnished mid-term rentals for business travellers (formerly HomeSuite, San Francisco). HomeSuite's "
                  "$2.3M of 2015 came from Battery, Foundation and Bessemer (TechCrunch 2015-06-11, no GV). TechCrunch "
                  "2019-02-04: 2nd Address 'picks up $10M from GV, Foundation', GV leading, with $42M raised to date "
                  "including debt-era money; the round is not named, so undetermined. Status aligned with Battery's row "
                  "(acquired by Blueground in 2021); no sale document was read.",
             rounds=[rnd("2015-06-11", "Funding round ($2.3M)", 2300000, None, False,
                         "https://techcrunch.com/2015/06/11/homesuite-raises-2-3m-to-provide-corporate-housing-a-quarter-"
                         "at-a-time/", "press"),
                     rnd("2019-02-04", "Funding round ($10M)", 10000000, "GV", True, TWO_A, "press")]))

# Boxbee: $2.3M from Floodgate, Google Ventures and others (April 2014), unnamed; the service still operates.
BOXBEE_TC = "https://techcrunch.com/2014/04/16/boxbee-2-3m-floodgate-gv/"
L.append(cls("boxbee", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined", entry_date="2014-04-16",
             note="Valet storage and reusable moving boxes (AngelPad 2013, San Francisco). TechCrunch 2014-04-16: $2.3M "
                  "from 'Floodgate Capital, Google Ventures, 500 Startups, Techstars, Jason Calacanis, and Ludlow "
                  "Ventures'; the round is not named, so undetermined. Still operating: boxbee.com (read 2026-09-28) "
                  "takes orders across the Bay Area and Southern California. No sale or later round found.",
             rounds=[rnd("2014-04-16", "Funding round ($2.3M)", 2300000, "Floodgate", True, BOXBEE_TC, "press")]))

# Bento (Bento Labs): $2M seed with Google Ventures (2015). The Wikidata CA was a one-word join.
BENTO_TC = "https://techcrunch.com/2015/03/11/bento-labs/"
L.append(cls("bento", status="unknown", rng="below_1b", country="US", focus="Consumer & Marketplaces",
             flags=["model_disputes_source", "city_unknown"],
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BENTO_TC, entry_date="2015-03-11",
             note="Bento Labs' context-aware Android home screen. TechCrunch 2015-03-11: '$2 million in seed funding from "
                  "investors that include First Round Capital, Social+Capital, Google Ventures, Susa Ventures' and "
                  "Silicon Valley angels. The Wikidata CA is a one-word join (another Bento) and is disputed: the "
                  "company is a US startup on its investors' record, but no source read places its city. No source "
                  "gives its fate after the 2015 beta, so status unknown. First Round's and YC's 'Bento' rows are other "
                  "companies (Bento for Business; a 2020 YC company), though First Round was also in this seed. "
                  + GRAD_LEFT,
             rounds=[rnd("2015-03-11", "Seed", 2000000, None, True, BENTO_TC, "press")]))

# Brandless: Cowboy/Slow seed, Redpoint Series A, then NEA and GV closed the $35M Series B at launch (July 2017).
BRANDLESS_TC = "https://techcrunch.com/2017/07/11/brandless/"
L.append(cls("brandless", status="defunct", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BRANDLESS_TC,
             entry_date="2017-07-11",
             note="Direct-to-consumer $3 essentials (San Francisco, product team in Minneapolis). TechCrunch 2017-07-11: "
                  "seed from Cowboy and Slow, 'Redpoint led the company's Series A round, and NEA and GV just closed a "
                  "$35 million Series B', so GV entered at the Series B: Growth. After SoftBank's $240M round (2018) it "
                  "closed in February 2020 (Fortune headline, 2020-02-11). The brand was later relaunched by new owners "
                  "(Clarke Capital Partners, per Wikipedia); aligned with Redpoint's defunct, the venture-backed company "
                  "having ended, though the asset-sale reading of s6 would make it acquired: flagged.",
             rounds=[rnd("2016-11", "Series A", 16000000, "Redpoint Ventures", None, W("Brandless"), "press"),
                     rnd("2017-07-11", "Series B", 35000000, "NEA, GV", True, BRANDLESS_TC, "press")]))

# Bionic Panda Games: San Francisco Android games studio; seed raised in 2011 with Google Ventures (GamesBeat).
BPG = NEWS("bionic-panda-games", "Bionic Panda raises seed funding for Android")
L.append(cls("bionic-panda-games", status="unknown", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BPG, entry_date="2011",
             note="Android casual games studio of Charles Hudson and Mike Jimenez. GamesBeat 2012-01-17: 'San "
                  "Francisco-based Bionic Panda' raised seed financing, 'raised last year and ... announced for the "
                  "first time today', from Google Ventures, SoftTech VC, Norwest, 500 Startups and angels. No source "
                  "read gives the company's end, so status unknown. " + GRAD_LEFT,
             rounds=[rnd("2011", "Seed", None, None, True, BPG, "press")]))

# BuysideFX: Boston FX workflow start-up; $2M from Google Ventures plus Atlas, FreshTracks, Boston Seed; closed 2014.
BFX = "https://www.fx-markets.com/foreign-exchange/2373135/buysidefx-shuts-up-shop"
L.append(cls("buysidefx", status="defunct", rng="below_1b", country="US", city="Boston", focus="Fintech & Payments",
             stage="undetermined",
             note="FX workflow and liquidity-access tools for institutional money managers. FX Week 2014-10-01: the "
                  "'Boston-based firm' closed before its planned July launch after a key deal with a global FX manager "
                  "fell through, 'despite receiving $2 million from Google Ventures ... as well as investment from Atlas "
                  "Venture, FreshTracks Capital and Boston Seed Capital' (CEO Ty Danco). The round is not named or "
                  "dated, so undetermined; defunct.",
             rounds=[rnd(None, "Funding ($2M from Google Ventures)", 2000000, "Google Ventures", True, BFX, "press")]))

# Zipline: GV an investor by the Nov-2016 Series B (VentureBeat), listed by the firm before it; round not named.
ZL_B = "https://venturebeat.com/business/drone-delivery-startup-zipline-raises-25-million-from-sequoia-andreessen-horowitz/"
ZL_2026 = "https://techcrunch.com/2026/01/21/zipline-charts-drone-delivery-expansion-with-600m-in-new-funding/"
L.append(cls("zipline", usd=7600000000, rng="1b_plus", val_src="web_verified", val_cite=ZL_2026, asof="2026-01-21",
             extra=WV, city="South San Francisco", focus="Industrial & Robotics", stage="undetermined",
             note="Autonomous medical and retail drone delivery (Half Moon Bay in 2016, now South San Francisco). "
                  "VentureBeat 2016-11-09 on the $25M Series B led by Visionnaire (with Sequoia and a16z): 'Google "
                  "Ventures, Sequoia Capital, Andreessen Horowitz ... are investors', total past $40M; the firm's own "
                  "list carried Zipline in spring 2016, before that round, but no source read names the round GV "
                  "bought, so undetermined. Mark: the $600M round of January 2026 at $7.6B (TechCrunch 2026-01-21), "
                  "replacing the unicorn-list figure as the source; aligned with a16z, Felicis and Sequoia.",
             rounds=[rnd("2016-11-09", "Series B", 25000000, "Visionnaire Ventures", None, ZL_B, "press"),
                     rnd("2026-01-21", "Funding round ($600M at $7.6B)", 600000000, None, None, ZL_2026, "press")]))

# WitnessAI: incubated by Ballistic; GV co-led the $27.5M Series A (May 2024); Sound Ventures led $58M in Jan 2026.
WAI_A = NEWS("witness-ai", "WitnessAI Raises $27.5 Million to Enable")
WAI_B = NEWS("witness-ai", "WitnessAI Raises $58 Million for Global")
L.append(cls("witness-ai", status="private", rng="below_1b", country="US", city="Mountain View", focus="Security",
             extra={"valuation_range_source": "web_verified", "valuation_citation": WAI_B},
             stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=WAI_A, entry_date="2024-05-21",
             note="Security and governance platform for enterprise AI use and AI agents (Mountain View, per its site and "
                  "the 2026 release; the 2024 release was datelined San Mateo). The company's release of 2024-05-21: a "
                  "'$27.5 million Series A round, co-led by GV and Ballistic Ventures', Ballistic having incubated it "
                  "since 2023; matches the firm's /ai list ('Invested' 2024-05). Sound Ventures led a $58M round on "
                  "2026-01-13 (Fin Capital, Qualcomm Ventures, Samsung Ventures, Forgepoint; GV not named). Momentum "
                  "check 2026-09-28 (Google News, both releases): no valuation disclosed and no $1B+ priced round found, "
                  "so below_1b.",
             rounds=[rnd("2024-05-21", "Series A", 27500000, "GV, Ballistic Ventures", True, WAI_A, "company"),
                     rnd("2026-01-13", "Funding round ($58M)", 58000000, "Sound Ventures", None, WAI_B, "company")]))

# Chroma Medicine: GV led the $135M Series B as a new investor (March 2023); merged with Nvelop into nChroma Bio (2024).
CHROMA_B = NEWS("chroma-medicine", "Chroma Medicine Secures $135M in Series B")
CHROMA_M = NEWS("chroma-medicine", "Chroma, Nvelop merge to marry genetic")
L.append(cls("chroma-medicine", status="acquired", rng="below_1b", country="US", city="Cambridge",
             focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CHROMA_B, entry_date="2023-03-01",
             note="Epigenetic editing therapeutics (Cambridge MA). The Series B release of 2023-03-01 (Sixth Street's "
                  "copy): $135M, 'Financing led by GV', with ARCH, DCVC Bio, Mubadala and Sixth Street as new investors "
                  "and an existing-investor list (Atlas, Newpath, Cormorant, Omega and others) that does not include "
                  "GV, so GV entered at the Series B: Growth. The firm's own post (" + POST("chroma-medicine") + ") "
                  "names the same GV-led Series B. On 2024-12-11 Chroma and Nvelop Therapeutics combined as nChroma "
                  "Bio, led by Nvelop's CEO Jeff Walsh, with $75M of new money; the two already shared ARCH, Atlas and "
                  "GV as investors (BioPharma Dive). Read as acquired: the company folded into the combined nChroma "
                  "Bio, which the firm lists as its own row (nchroma-bio), as it listed Nvelop (nvelop-therapeutics).",
             rounds=[rnd("2023-03-01", "Series B", 135000000, "GV", True, CHROMA_B, "company"),
                     rnd("2024-12-11", "Merger with Nvelop Therapeutics into nChroma Bio ($75M financing)", 75000000,
                         "Cormorant, ARCH Venture Partners, Atlas Venture, Newpath Partners", None, CHROMA_M,
                         "press")]))

# Copious: $2M seed with Google Ventures (spring 2011); a named $5M Series A in July 2012 with GV; pivoted into
# Distiller, which CircleCI acquired in 2014.
CP_A = "https://techcrunch.com/2012/07/12/copious-raises-5-million-series-a/"
CP_ROSE = NEWS("copious", "Interview with Jim Rose, CEO of CircleCI")
L.append(cls("copious", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CP_A, entry_date="2011",
             grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=CP_A,
             note="Social marketplace built on Facebook ('a San Francisco startup', co-founded by Jim Rose). TechCrunch "
                  "2012-07-12: Foundation Capital led a $5M Series A 'with Google Ventures and Relay Ventures "
                  "participating', all three having invested in the '$2 million seed funding round that closed in the "
                  "spring of 2011', so the entry is that seed and the named Series A graduates it. Jim Rose's own "
                  "account (interview, 2021): after the Facebook traffic fell the company pivoted to mobile tooling as "
                  "'Distiller', and 'In 2014, Distiller was acquired by CircleCI': acquired.",
             rounds=[rnd("2011", "Seed", 2000000, "Foundation Capital", True, CP_A, "press"),
                     rnd("2012-07-12", "Series A", 5000000, "Foundation Capital", True, CP_A, "press"),
                     rnd("2014", "Acquired by CircleCI (as Distiller)", None, "CircleCI", None, CP_ROSE, "press")]))

# Core (bycore.com, later 'Crews by Core'): $4M seed with John Lyman of Google Ventures (release of 2020-09-21).
CORE_PR = ("https://www.globenewswire.com/news-release/2020/09/21/2096350/0/en/Core-Launches-Construction-Marketplace-"
           "to-Grow-Jobs-Help-Solve-Labor-Shortage.html")
L.append(cls("core", status="unknown", rng="below_1b", country="US", city="Palo Alto", city_src="web_verified",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CORE_PR, entry_date="2020-09-21",
             note="Construction labor marketplace matching trades workers to contractors (co-founded by Di-Ann Eisnor, "
                  "ex-Waze). The company's release of 2020-09-21, datelined Palo Alto: $4M 'in its seed funding round "
                  "from investors including Pete Flint (NFX), John Lyman (Google Ventures)', Rob Hayes and Caterina "
                  "Fake; John Lyman is the GV partner on the firm's listing. bycore.com now forwards to a parked page "
                  "and no source read gives the company's later state, so status unknown. YC's 'Core' (Bangalore, "
                  "S23) is a different company. " + GRAD_LEFT,
             rounds=[rnd("2020-09-21", "Seed", 4000000, None, True, CORE_PR, "company")]))

# Cinch (Nifti's polling app): Google Ventures among the backers (PRWeb, March 2015, Boston dateline); round unnamed.
CINCH_PR = "http://www.prweb.com/releases/2015/03/prweb12574614.htm"
CINCH_TC = ("https://techcrunch.com/2014/09/25/price-tracking-service-nifti-switches-gears-launches-social-polling-"
            "app-cinch/")
L.append(cls("cinch", status="unknown", rng="below_1b", country="US", city="Boston", city_src="web_verified",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Cinch Polls, the social photo-polling app spun out of the price-tracker Nifti (Nathan Sharp). Nifti's "
                  "$1.2M additional seed of December 2013 came from Otto Capital and angels, without GV (TechCrunch "
                  "2014-09-25); the company's March 2015 release, datelined Boston, cites 'backing from a group of "
                  "investors including Google Ventures'. No source read names or dates GV's round, so undetermined; no "
                  "source gives the company's later state, so status unknown.",
             rounds=[rnd("2013-12", "Seed (additional, $1.2M)", 1200000, "Otto Capital", False, CINCH_TC, "press"),
                     rnd(None, "Funding with Google Ventures (unnamed)", None, None, True, CINCH_PR, "company")]))

jl.write("j15", L)
