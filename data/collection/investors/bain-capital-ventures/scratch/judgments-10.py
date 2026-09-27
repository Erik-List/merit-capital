"""PRO-162 grind, batch-010 (orb-labs .. skyhook-wireless). Evidence: the firm's live CMS and posts, its archived
company pages (Common Crawl captures, CCPAGE), Wikipedia extracts, Google News (nq.py, NQ_TAG=b10) and web checks
run 2026-09-27 (URLs as the tools printed them). Two rows are left out on the lead judge's instruction: seed-cx
(folded into zero-hash by identity-merges.json) and signify-health (now not_member, sale consideration from the
Remedy Partners merger). Verdict lines: publishing-group-of-america and pgoa-media are one company, bought by BCV
and Shamrock Capital Growth from its majority owner (a control position); risk-management-solutions is the
Risk Management Software position of the heritage book (sold to DMGT in 1998, before any venture vehicle)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []
_HERE = Path(__file__).parent
_SIB = json.loads((_HERE / "siblings.json").read_text())
_LEDGER = json.loads((_HERE.parent / "companies/membership-ledger.json").read_text())["bain-capital-ventures"]["verdicts"]
_BASE = {r["slug"]: r for r in json.loads((_HERE.parent / "companies/base.json").read_text())}


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


def SIBCITE(slug, investor, key="val_cite"):
    """A citation a sibling investor's row already carries, read from siblings.json (never typed)."""
    m = [s for s in _SIB.get(slug, []) if s.get("investor") == investor and s.get(key)]
    if len(m) != 1:
        raise SystemExit(f"SIBCITE({slug!r}, {investor!r}) matched {len(m)}")
    return m[0][key]


def WB(slug):
    """The row's own first archive capture of the firm's listing (base.json wayback_first_link)."""
    u = _BASE[slug].get("wayback_first_link") or ""
    if not u:
        raise SystemExit(f"WB({slug!r}): no capture on the row")
    return u


# The firm's 2006 history page, as the heritage pass cites it (read from the ledger, not typed).
HISTORY = _LEDGER["physicians-quality-care"]["citation"]
# Printed by the web check of 2026-09-27 (WebSearch) for the Publishing Group of America buyout.
EP_PGA = "https://www.editorandpublisher.com/stories/bain-shamrock-buy-relish-and-american-profile,127872"
NP_PGA = "https://www.nashvillepost.com/home/bain-capital-buys-franklin-based-publisher/article_2cb61ceb-476b-5271-87c1-142de300d5e8.html"
# Printed by the web checks of 2026-09-27 (WebSearch results).
PALETTE_PR = ("https://www.prweb.com/releases/palette-raises-6m-led-by-bain-capital-ventures-to-help-finance-and-operations-"
              "teams-design-manage-and-automate-sales-commissions-889823331.html")
SENSE_CD = "https://www.coindesk.com/markets/2021/08/03/sense-finance-raises-52m-to-bring-yield-trading-to-defi"
NUCLEO_TB = "https://www.theblock.co/post/188613/bain-6th-man-ventures-lead-nucleo-round"
PROPERLY_BK = "https://betakit.com/properly-founders-exit-as-company-and-tech-are-sold-in-separate-transactions/"
SCROLL_CB = "https://www.crunchbase.com/organization/scroll-tech"


def control(slug, why, cite, conf="medium"):
    L.append(verdict(slug, "not_member",
        why + " A control acquisition is not a venture round (COLLECTION.md s1 T3 control positions; decisions.md D4): the firm "
        "with its co-investor group took 50% or more.", ec="site_listing", conf=conf, cite=cite) | {"exclusion": "control_position"})


L.append(cls("orb-labs", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("orb-labs", "Raises $4.5M Seed, Led by"), entry_date="2023-02",
    note="Cross-chain messaging protocols (Orb Stack), on Bain Capital Crypto's list. 'Orb Labs Raises $4.5M Seed, Led by Bain Capital "
         "Crypto' (Business Wire, 2023-02-14); the last news read is an Orb Stack audit (December 2023), and no source read gives its "
         "later fate or places the company. Graduation left for the graduation pass. Siblings Greylock and Menlo hold Orb, the "
         "usage-billing company Adyen bought: a name collision, not aligned."))
L.append(cls("osmo", status="private", rng="below_1b", city="San Francisco", city_src="web_verified", focus="AI & Applied AI",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("osmo", "Osmo Gives Every Storyteller"),
    entry_date="2026-08", grad="censored",
    note="AI-native video studio for storytellers (osmo.inc; San Francisco dateline). 'Osmo is also announcing a $5 million seed round "
         "led by Bain Capital Ventures' (the company's release, 2026-08-05); inside 24 months, so censored. Momentum check "
         "(2026-09-27): no round beyond the $5M seed. Siblings Accel (Osmo, the children's learning toy Byju's bought) and Lux (Osmo, "
         "digital olfaction) are name collisions, not aligned."))
L.append(cls("palette", status="private", rng="below_1b", country="FR", country_src="model_knowledge", city="Paris",
    focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PALETTE_PR, entry_date="2022-05",
    flags=["model_disputes_source"],
    note="Sales-commission software (palettehq.com). 'Palette ... today announced that it has raised $6 million in Seed funding' led "
         "by Bain Capital Ventures (release, San Francisco dateline, 2022-05-18; the firm's listing gives 2021, the close year). "
         "Status and place aligned with YC's row for the same company (palettehq: private, Paris, from YC's directory); the site "
         "still sells the product. The prefilled 'defunct' and Moroccan country came from a wrong join. Graduation left for the "
         "graduation pass. YC's other 'palette' row (an S26 media platform) is a name collision."))
L.append(cls("pallet", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("pallet", "Pallet uses AI to bring logistics"), entry_date="2022",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("pallet", "Pallet uses AI to bring logistics"),
    note="AI workforce for logistics operations (San Francisco). 'Bain also led Pallet's $3 million seed round and decided to double "
         "down by also leading the company's Series A now' (TechCrunch, 2024-10-02, the $18M Series A); a $27M Series B led by "
         "General Catalyst followed in May 2025. Momentum check (2026-09-27): no priced round at $1B or more.",
    rounds=[rnd("2022", "Seed", 3000000, "Bain Capital Ventures", True, NEWS("pallet", "Pallet uses AI to bring logistics"), "press"),
            rnd("2024-10", "Series A", 18000000, "Bain Capital Ventures", True, NEWS("pallet", "Pallet uses AI to bring logistics"), "press"),
            rnd("2025-05", "Series B", 27000000, "General Catalyst", None,
                NEWS("pallet", "Pallet Secures $27M Series B Led by General Catalyst"), "press")]))
L.append(cls("parafi", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Crypto & Web3", stage="Seed", **site_stage("parafi"), entry_date="2019",
    note="ParaFi Capital, a crypto-native asset manager (San Francisco). The position is in the firm itself, not a fund commitment: "
         "Galaxy Digital's 2020 strategic investment made it 'a minority shareholder in the firm', 'joining other ParaFi investors "
         "including Bain Capital Ventures and Henry Kravis' (" + NEWS("parafi", "Announces Strategic Investment from Galaxy") + "). "
         "BCV's listing: 2019, 'Seed, Early' (read as Seed, as on relay-financial). Graduation left for the graduation pass."))
L.append(cls("parative", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Boston",
    focus="SaaS", stage="Seed", **site_stage("parative"), entry_date="2019",
    note="Customer-data scoring for revenue teams (Parlor, renamed Parative; Boston). Totango bought its technology and team in "
         "October 2024 (" + NEWS("parative", "Acquisition of Technology and Team") + "): the product and team as a going concern, so "
         "acquired. BCV's listing: 2019, Seed (Ajay Agarwal). Graduation left for the graduation pass."))
L.append(cls("periodic-labs", status="private", rng="1b_plus", usd=1300000000, val_src="web_verified", asof="2025-09",
    val_cite=SIBCITE("periodic-labs", "a16z"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="Menlo Park", city_src="web_verified", focus="AI & Applied AI",
    stage="Seed", **site_stage("periodic-labs"), entry_date="2025", grad="censored",
    note="AI for physical science (ex-OpenAI and DeepMind researchers). BCV's listing: 2025, Seed (Slater Stich): the $300M seed at "
         "$1.3B post-money closed in September 2025; mark aligned with a16z, Accel, Felicis and Lightspeed. Reported talks at about "
         "$7B (Bloomberg, March 2026) are unclosed, so they do not mark the row. City: 'plans to build its own lab in Menlo Park, "
         "California' (" + NEWS("periodic-labs", "raise $300 million") + "), agreeing with Felicis; a16z and Lightspeed read San "
         "Francisco. Inside 24 months, so censored."))
L.append(cls("perksy", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=CCPAGE("/portfolio/perksy/"), city="New York", city_src="web_verified", focus="SaaS", stage="undetermined",
    note="Mobile consumer-insights platform (founded in Toronto; the firm's 2019 page places it in New York, NY, 'Seed/Early Stage', "
         "Sarah Smith). The only round on record is the $4M of February 2019 (Forbes), which no page read ties to BCV, so the round "
         "is not named. The firm listed it as Active through 2022 and the product site is live (2026-09-27).",
    rounds=[rnd("2019-02", None, 4000000, None, None, NEWS("perksy", "Just Raised $4 Million"), "press")]))
L.append(cls("polars", status="private", rng="below_1b", country="NL", country_src="web_verified",
    country_cite=NEWS("polars", "raises $21M from Accel"), city="Amsterdam", city_src="web_verified", focus="DevTools & APIs",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("Polars (software)"), entry_date="2023-08",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("polars", "raises $21M from Accel"),
    note="The company behind the Polars DataFrame library ('the Amsterdam-based company', TechCrunch). 'In 2023, Vink and Peters "
         "successfully closed a seed round of approximately $4 million, which was led by Bain Capital Ventures' (Wikipedia); the EUR "
         "18M (about $21M) Series A led by Accel followed in September 2025. Country and city aligned with Accel.",
    rounds=[rnd("2023-08", "Seed", 4000000, "Bain Capital Ventures", True, W("Polars (software)"), "press"),
            rnd("2025-09", "Series A", 21000000, "Accel", None, NEWS("polars", "raises $21M from Accel"), "press")]))
L.append(cls("poolside", status="private", rng="10b_plus", usd=12000000000, val_src="web_verified", asof="2026-08-24",
    val_cite=NEWS("poolside", "Nvidia Pays Poolside $6 Billion"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="San Francisco", focus="AI & Applied AI",
    stage="Seed", **site_stage("poolside"), entry_date="2023",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("poolside", "Raises Massive $500M Series B"),
    note="AI for software development ('headquartered in San Francisco', Wikipedia, with a Paris branch). BCV's listing: 2023, Seed "
         "(the $126M seed Redpoint led); BCV then led the $500M Series B of October 2024 at about $3B. Mark: $12B, the value of the "
         "Nvidia deal of August 2026 (Forbes, 2026-08-24), aligned with Felicis and Point Nine; Redpoint's $3B is the stale side.",
    rounds=[rnd("2024-10", "Series B", 500000000, "Bain Capital Ventures", True, NEWS("poolside", "Raises Massive $500M Series B"), "press")]))
L.append(cls("primitive", status="unknown", rng="below_1b", city="New York", city_src="web_verified", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("primitive", "Primitive raises $9 million"),
    entry_date="2022-08",
    note="AMM liquidity discovery (DeFi), on Bain Capital Crypto's list. 'Primitive announced it has raised $9 million in a Series A "
         "round led by Bain Capital Crypto' (The Block, 2022-08-18), the team 'looking to hire in New York and remotely'. The firm's "
         "crypto list tags it 'exited'; primitive.xyz answers HTTP 402 and no source read gives its fate. YC's 'primitive' (an S26 "
         "agent-communications company) is a name collision, not aligned."))
L.append(cls("professional-advantage-financial", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="New York", city_src="web_verified", focus="Fintech & Payments", stage="undetermined",
    note="Financial services firm at 845 Third Avenue, New York (the firm's 2006 listing: 'Acquired', 'Early', " + WB(
        "professional-advantage-financial") + "). No source read names the round or the buyer (a vendor dates a sale to March "
         "2000, which would put the entry near the D2 boundary; left for Erik if the heritage pass wants it)."))
L.append(cls("profitlogic", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Cambridge",
    city_src="web_verified", focus="SaaS", stage="undetermined",
    note="Markdown and price optimisation for retailers (25 1st Street, Cambridge, MA). 'ProfitLogic was acquired by Oracle in July "
         "2005' (the firm's page, " + CCPAGE("/portfolio/company/profitlogic") + "; Scott Friend, Jeff Schwartz; 'Midstage' in 2003). "
         "The round is not named; aligned with Battery."))
L.append(cls("pronto", status="private", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=NEWS("pronto", "3.6x valuation jump"), city="New Delhi", city_src="web_verified", focus="Consumer & Marketplaces",
    stage="Seed", **site_stage("pronto"), entry_date="2025-05",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("pronto", "3.6x valuation jump"),
    flags=["model_disputes_source"],
    note="Ten-minute home services in India ('A budding startup out of New Delhi', TechCrunch; Livemint later calls it a Bengaluru "
         "startup). BCV's listing: 2025, Seed: the $2M seed of May 2025; 'Existing investor Bain Capital Ventures also participated' "
         "in the $11M Series A co-led by General Catalyst and Glade Brook (TechCrunch, 2025-08-11). A $20M Series B at about $200M "
         "followed in May 2026, still below the band. The prefilled 'acquired' came from YC's Pronto (Mexican ride sharing), a name "
         "collision.",
    rounds=[rnd("2025-05", "Seed", 2000000, None, True, NEWS("pronto", "3.6x valuation jump"), "press"),
            rnd("2025-08", "Series A", 11000000, "General Catalyst and Glade Brook Capital", True, NEWS("pronto", "3.6x valuation jump"), "press"),
            rnd("2026-05", "Series B", 20000000, None, None, NEWS("pronto", "Pronto raises $20 million in Series B round"), "press")]))
L.append(cls("properly", status="acquired", rng="below_1b", country="CA", country_src="web_verified",
    country_cite=CCPAGE("/portfolio/properly/"), city="Toronto", city_src="web_verified", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("bcv-leads-35m-series-b-in-properly"),
    entry_date="2021-07",
    note="Tech-enabled home brokerage ('The company is headquartered in Toronto', the firm's 2021 page). 'BCV is thrilled to announce "
         "that we are leading a CAD$44 million (USD$35 million) Series B investment in Properly' (the firm's post, 2021-07-21); a "
         "Series B entry reads Growth. In September 2023 the brokerage and search portal were sold to a Canadian buyer and the "
         "technology in a separate transaction as the founders left (" + PROPERLY_BK + "): asset sales, so acquired."))
L.append(cls("prophet-security", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Menlo Park",
    city_src="web_verified", focus="Security", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("prophet-security-is-using"), entry_date="2024-04",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("prophet-security", "Raises $30M Series A, Announces"),
    note="AI security-operations analyst, incubated in BCV Labs. 'We are pleased to have led the $11 million seed round' (the firm's "
         "post, 2024-04-23); Accel led the $30M Series A of July 2025 with BCV participating. City: 'The Menlo Park-based company' "
         "(" + NEWS("prophet-security", "Prophet Security raises $30M for AI SOC") + ", 2025-07), fresher than Accel's Palo Alto and "
         "the firm's listing (San Francisco). Momentum check (2026-09-27): only strategic investments since (Amex and Citi, "
         "February 2026), no priced round at $1B or more.",
    rounds=[rnd("2024-04", "Seed", 11000000, "Bain Capital Ventures", True, POST("prophet-security-is-using"), "firm"),
            rnd("2025-07", "Series A", 30000000, "Accel", True, NEWS("prophet-security", "Prophet Security raises $30M for AI SOC"), "press")]))
L.append(cls("puzzle", status="private", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NUCLEO_TB, entry_date="2022-11",
    note="Puzzle (formerly Nucleo), private multisig and wallet infrastructure (Aleo, Aztec), on Bain Capital Crypto's list at "
         "/portfolio/nucleo/. 'Crypto privacy startup Nucleo raised $4 million in seed funding, led by the crypto arm of investment "
         "firm Bain Capital and 6th Man Ventures' (The Block, 2022-11). The Puzzle wallet is live; no source read places the "
         "company. Graduation left for the graduation pass. Felicis' Puzzle (puzzle.io, accounting) is a name collision."))
L.append(cls("pylon", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="SaaS", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("pylon", "$31 Million Series B Funding Secured"), entry_date="2025-08", flags=["model_disputes_source"],
    note="B2B customer support platform (San Francisco). 'The round was co-led by a16z and Bain Capital Ventures (BCV)' (Pulse 2.0, the "
         "$31M Series B of August 2025; the firm's own year-end post: 'we co-led their Series B round'). Momentum check "
         "(2026-09-27): no later priced round found. The prefilled Thai country was a wrong join; aligned with a16z."))
L.append(cls("qwiet", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Santa Clara",
    focus="Security", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017-10",
    note="Application security testing (ShiftLeft, renamed Qwiet AI; Santa Clara). 'In October 2017 ShiftLeft came out of stealth and "
         "announced Bain Capital Ventures as an investor' (" + POST("why-i-invested-in-shiftleft") + "): the round before its $20M "
         "Series B of 2019 (FinSMEs), read as its Series A. Harness acquired Qwiet AI effective 2025-09-26 ("
         + NEWS("qwiet", "Harness Strengthens Its Application Security") + ")."))
L.append(cls("radionomy-azerion", status="acquired", rng="below_1b", country="BE", country_src="web_verified",
    country_cite=W("Radionomy"), city="Brussels", focus="Media, Gaming & Advertising", stage="undetermined", entry_date="2008",
    note="Online radio platform and audio advertising (Radionomy Group, founded in Belgium in 2007 'by four Belgian entrepreneurs'). "
         "Azerion acquired Radionomy in November 2022 (" + NEWS("radionomy-azerion", "enters audio advertising market - GlobeNewswire")
         + "). BCV's listing gives 2008, before Radionomy raised outside money: the position most likely came through TargetSpot "
         "(the base row 'targetspot', New York, on the firm's 2010-2013 listings), which Radionomy bought in December 2012 "
         "(Wikipedia). The round is not named."))
L.append(cls("readia", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    city_src="web_verified", focus=None, extra={"focus": None}, stage="undetermined",
    note="Internet company in New York on the firm's 2006 and 2010 listings ('Acquired', 'Early', " + WB("readia") + "). No source read "
         "says what it did, who bought it or which round BCV entered; focus left outside the taxonomy for want of a description."))
L.append(cls("revenuecat", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="DevTools & APIs", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("revenuecat-lowers"),
    entry_date="2025-05",
    note="In-app subscription infrastructure (San Francisco). 'BCV is leading RevenueCat's $50M Series C-2' (the firm's post, "
         "2025-05-22). Momentum check (2026-09-27): the Series C priced it at $500M (" + NEWS("revenuecat", "Went from a $1.5M Round")
         + "); no later round found, so below the band.",
    rounds=[rnd("2025-05", "Series C", 50000000, "Bain Capital Ventures", True, POST("revenuecat-lowers"), "firm")]))
L.append(cls("ricerca-biosciences", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Concord",
    city_src="web_verified", focus="Healthcare & Bio", stage="undetermined", entry_date="2007",
    note="Preclinical and chemistry contract research (Concord, Ohio). Its chemical division went to Olon and the rest was renamed "
         "Concord Biosciences in 2017, then owned by Main Market Partners (" + NEWS("ricerca-biosciences", "Renamed to Concord")
         + "); Frontage Laboratories acquired Concord Biosciences in April 2018. BCV's listing gives 2007 and 'Acquired'; the round "
         "is not named."))
L.append(cls("rightfoot", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    city_src="web_verified", focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("rightfoot-co-founder"), entry_date="2021-02",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("rightfoot", "Rightfoot raises $15M"),
    note="Embedded debt-payment APIs (Charitize, Inc.; San Francisco on the firm's 2022 page). 'Our firm was thrilled to lead the "
         "company's $5M seed financing round earlier this year' (the firm's post, 2021); 'The Series A was led by ... Blue Lion Global "
         "and Renegade Partners, with participation from Bain Capital Ventures' (Banking Dive, 2023-08, $15M). Momentum check "
         "(2026-09-27): no priced round at $1B or more.",
    rounds=[rnd("2021-02", "Seed", 5000000, "Bain Capital Ventures", True, POST("rightfoot-co-founder"), "firm"),
            rnd("2023-08", "Series A", 15000000, "Blue Lion Global and Renegade Partners", True, NEWS("rightfoot", "Rightfoot raises $15M"), "press")]))
L.append(cls("rillet", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2026-08-19",
    val_cite=NEWS("rillet", "Raises $100M Series C at $1B Valuation to Build"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="New York", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("rillet-closes"), entry_date="2026-08",
    note="AI-native ERP and general ledger (New York). 'We are proud to partner with Nic and the Rillet team as part of the company's "
         "$100M Series C' (the firm's post, 2026-08-18). Mark: the Series C at $1B (Business Wire, 2026-08-19), exactly on the band "
         "edge; fresher than the below_1b rows of a16z, Creandum, First Round and Sequoia, which predate the round."))
L.append(cls("risc-zero", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="Seattle",
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("risc-zero", "RISC Zero raises $40 million"), entry_date="2022-08",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("risc-zero", "RISC Zero raises $40 million"),
    note="Zero-knowledge proving (RISC Zero zkVM, Bonsai), on Bain Capital Crypto's list. 'The $40 million joins the $12 million the "
         "startup raised in a seed round in August 2022 led by Bain Capital Crypto' (Fortune, 2023-07-19, the Series A led by "
         "Blockchain Capital). Momentum check (2026-09-27): no priced round at $1B or more (the Boundless ZKC token belongs to a "
         "separate network).",
    rounds=[rnd("2022-08", "Seed", 12000000, "Bain Capital Crypto", True, NEWS("risc-zero", "RISC Zero raises $40 million"), "press"),
            rnd("2023-07", "Series A", 40000000, "Blockchain Capital", None, NEWS("risc-zero", "RISC Zero raises $40 million"), "press")]))
L.append(cls("risk-harbor", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    city_src="web_verified", focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("announcing-our-seed-investment-in-risk-harbor"), entry_date="2021-06",
    note="Parametric risk marketplace for DeFi (San Francisco on the firm's 2021 page, Stefan Cohen). 'We could not be more thrilled to "
         "participate in Risk Harbor's seed financing' (the firm's post, 2021-06-24; the $3.25M seed co-led by Framework and "
         "Pantera). riskharbor.com now redirects to Subsea ('Risk Management Marketplace'), read as the same business under a new "
         "name. Graduation left for the graduation pass."))
L.append(verdict("risk-management-solutions", "not_member",
    "[bain_capital_heritage] Another desk (decisions.md D2, R1): the firm's 2003 listing names it 'Risk Management Software', the "
    "company's pre-rename name (Wikipedia, Haresh C. Shah), and the 2006 listing files 'Risk Management' (rms.com) under 'Acquired'. "
    "RMS's only sale before Moody's bought it from DMGT in 2021 was to Daily Mail and General Trust in January 1998, so Bain Capital's "
    "position ended before any Bain Capital venture vehicle existed (1999): a position of the generalist funds, filed under 'Bain "
    "Capital's history of investing ... since 1984'.",
    ec="site_listing", conf="medium", cite=HISTORY))
L.append(cls("rollbar", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    city_src="web_verified", focus="DevTools & APIs", stage="undetermined",
    note="Error monitoring for developers (San Francisco on the firm's 2018 page, 'Seed/Early Stage', Salil Deshpande). An $11M Series "
         "B followed in March 2020 (FinSMEs); no page read names the round BCV entered. Still operating (a 2023 breach disclosure, "
         "2026 product comparisons).",
    rounds=[rnd("2020-03", "Series B", 11000000, None, None, NEWS("rollbar", "Rollbar Raises $11M"), "press")]))
L.append(cls("scroll", status="private", rng="below_1b", country="SC", country_src="web_verified", country_cite=SCROLL_CB,
    flags=["city_unknown", "model_disputes_source"], focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("scroll", "raises $30 million from Bain Capital"),
    entry_date="2022-04",
    note="Ethereum zkEVM rollup, on Bain Capital Crypto's list. 'Polychain Capital led the funding, with Bain Capital Crypto, Robot "
         "Ventures ... participating' (The Block, 2022-04-21, the Series A). The $1.8B of March 2023 came from an unnamed source "
         "(" + NEWS("scroll", "reaches $1.8 billion valuation") + ") and is stale; the SCR token's fully diluted value read $25.6M on "
         "2026-09-27 (" + NEWS("scroll", "Scroll Price Today | Live SCR Price") + "), so the collapse rules the lower band "
         "(COLLECTION.md s6). Country: the company's registered address is in Seychelles (Crunchbase, LinkedIn); the team is "
         "distributed and no source places an operating HQ. The prefilled Japan was a wrong join. USV's Scroll (the news "
         "subscription Twitter bought) is a name collision."))
L.append(cls("sense-finance", status="defunct", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    city_src="web_verified", focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=SENSE_CD, entry_date="2021-08",
    note="Fixed-rate and yield-trading DeFi protocol ('San Francisco & NYC' on the firm's 2022 page, Kevin Zhang and Stefan Cohen). "
         "'Sense Finance ... raised $5.2 million in a seed funding round led by Dragonfly Capital' with Bain Capital (CoinDesk, "
         "2021-08-03). The project wound down: 'The Sense Project is winding down and the UI will be deprecated in Q4 2023' "
         "(sense.finance, read 2026-09-27). Graduation left for the graduation pass."))
L.append(cls("servigistics", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Atlanta",
    city_src="web_verified", focus="SaaS", stage="undetermined",
    note="Service parts and service lifecycle software (Atlanta). 'Servigistics was acquired by Marlin Equity Partners in July 2009' "
         "(the firm's page, " + CCPAGE("/portfolio/company/servigistics") + "; James Nahirny; 'Midstage' in 2003); PTC bought it in "
         "2012. The round is not named."))
L.append(cls("shopmy", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", asof="2025-10-22",
    val_cite=NEWS("shopmy", "Raises $70M at $1.5 Billion Valuation to Scale"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="New York", focus="Media, Gaming & Advertising",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-creator-economy-is-breathing"),
    entry_date="2025-01",
    note="Creator commerce and affiliate platform (New York). 'We recently co-led ShopMy's Series B' (the firm's post, 2025-01-24; the "
         "$77.5M round; the listing gives 2024, the close year). Mark: the $70M round of October 2025 at $1.5B, led by Avenir with "
         "BCV participating (PR Newswire, 2025-10-22); fresher than Menlo's below_1b row, which predates it."))
L.append(cls("shopping-com", city="Brisbane", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
    note="Comparison shopping (DealTime, renamed Shopping.com; corporate HQ Brisbane, California). IPO October 2004; eBay acquired it in "
         "June 2005 for about $634M (" + W("Shopping.com") + "). BCV's listings from 2003 file it as 'Midstage'; the round BCV entered "
         "is not named. Aligned with Benchmark."))
L.append(cls("silna", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Healthcare & Bio", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("silna", "Daily Funding Report: 3/26/2025"), entry_date="2025-03",
    note="Prior-authorization automation for providers (New York). 'Silna Health ... has raised $22M in Series A funding led by Accel "
         "and Bain Capital Ventures' (AlleyWatch, 2025-03-26), announced with the seed Accel had led for $27M in all; the firm's "
         "listing gives 2024 (the close year). Aligned with Accel."))
L.append(cls("simile", city="Palo Alto", focus="AI & Applied AI", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("why-we-re-continuing-to-invest-in-simile"), entry_date="2026-02",
    note="AI simulations of human behaviour (Joon Sung Park, Percy Liang, Michael Bernstein; Palo Alto, with a San Francisco office). "
         "'We backed Simile at the Series A' (the firm's post, 2026-07-30): the $100M Series A led by Index Ventures of February 2026 "
         "(" + NEWS("simile", "AI digital twin startup Simile raises $100M") + "); BCV joined the $200M Series B at $2B in July 2026."))
L.append(cls("singleclick-systems", status="unknown", rng="below_1b", country="US", country_src="model_knowledge", city="Eatontown",
    city_src="web_verified", focus="SaaS", stage="undetermined",
    note="Remote access and home-network software for consumers and small businesses (Eatontown, NJ, on the firm's 2012 page, "
         + CCPAGE("/portfolio/company/singleclick-systems") + "; Ben Holzman, Ben Nye). Listed 2011-2013 only; no source read gives "
         "the round or its later fate."))
L.append(cls("skip", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("skip", "Blockchain Infrastructure Company Skip Raises"), entry_date="2022-10",
    note="Cosmos interoperability and blockspace infrastructure (skip.money). 'The round was led by Bain Capital Crypto' (Pulse 2.0, "
         "the $6.5M seed of October 2022). The Interchain Foundation acquired Skip in December 2024 ("
         + NEWS("skip", "Interchain Foundation acquires Skip") + "). No source read places the company. Graduation left for the "
         "graduation pass. YC's Skip (e-scooters) is a name collision."))
L.append(cls("skyhook-wireless", status="acquired", rng="below_1b", city="Boston", focus="Data Infrastructure",
    stage="undetermined",
    note="Wi-Fi positioning (Boston). 'In February 2014, Skyhook Wireless was acquired by True Position Inc.' (" + W("Skyhook Wireless")
         + "); Qualcomm bought it in 2022. The firm lists it from 2006 (Ajay Agarwal, 'Seed/Early Stage'); the round is not named."))

control("publishing-group-of-america",
    "Publishing Group of America (Franklin, TN; American Profile, Relish, Spry): 'Bain, Shamrock Buy Relish And American Profile' "
    "(Editor and Publisher, " + EP_PGA + "; 'Bain Capital buys Franklin-based publisher', Nashville Post, " + NP_PGA + "): Bain "
    "Capital Ventures and Shamrock Capital Growth bought the company from its majority owner, Quadrangle Capital Partners. The firm's "
    "2010 listing files it under 'Expansion/Growth Buyout'.", EP_PGA)
control("pgoa-media",
    "PGOA Media is Publishing Group of America under its later name ('Publishing Group of America (PGOA Media) ... publishes three "
    "magazines - American Profile, Relish, and Spry', the firm's 2012 page, " + CCPAGE("/portfolio/company/pgoa-media") + "), the "
    "company Bain Capital Ventures and Shamrock Capital Growth bought from its majority owner Quadrangle Capital Partners (Editor and "
    "Publisher, " + EP_PGA + ").", EP_PGA)

if __name__ == "__main__":
    jl.write("batch-010", L)
