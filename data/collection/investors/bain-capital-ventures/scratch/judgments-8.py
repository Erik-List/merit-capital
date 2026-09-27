"""PRO-162 grind, batch-008 (etched .. legora). Evidence as in judgments-1.py, plus Google News (nq.py, NQ_TAG=b8,
news-extra-b8.json), Wikipedia extracts (wikifetch.py), the companies' own sites and releases, and 11 WebSearch calls
(Instinet, iPay, Imerica, eTranslate, Gradle, Hi Marley, Laika, Ulvetanna, Hyde, Fuel Labs, Flood).

Two verdicts replace classifications: Instinet (the Bain Capital holders of the listed Instinet Group were the generalist
Fund VII family, with no venture vehicle: another desk, D2, and a listed-company stake, D4) and iPay Technologies (a 2006
recapitalisation that made Spectrum Equity and BCV the majority shareholders: a control position).

Two rows here are companies already in the base under another slug: fingerhut is Bluestem Brands (formerly Fingerhut
Direct Marketing) and futuredontics is 1-800-Dentist (the brand of Futuredontics). Both are classified in line with the
earlier rows and reported for identity-merges.json."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []

HERITAGE = "[bain_capital_heritage] "
BLUESTEM_S1 = "https://www.sec.gov/Archives/edgar/data/1283384/000095012311037906/c62024sv1.htm"
EYETEL_SB2 = "https://www.sec.gov/Archives/edgar/data/1205653/000114420407022935/v073241sb2.htm"


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


def control(slug, why, cite, conf="high"):
    L.append(verdict(slug, "not_member",
        why + " A control acquisition is not a venture round (COLLECTION.md s1 T3 control positions; decisions.md D4): the firm "
        "with its co-investor group took 50% or more.", ec="site_listing", conf=conf, cite=cite) | {"exclusion": "control_position"})


L.append(cls("etched", city="Cupertino", focus="Industrial & Robotics",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("etched", "Customer Contracts Top"), entry_date="2026",
    note="Transformer inference chips (Cupertino, aligned with sibling Sequoia). BCV's listing: 2026, Growth (Merritt Hummer, Abby Meyers); "
         "Pulse 2.0 names Bain Capital Ventures in the $700M round of August 2026 led by Jane Street at $21B, which followed the July "
         "Series C. Every Etched round of 2026 was past Series A, so the entry reads Growth either way."))
L.append(cls("etranslate", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS", stage="undetermined",
    note="Translation software and services (San Francisco), on the firm's 2003 listing only. 'Translations.com merges with software "
         "development company eTranslate' in 2002 (TransPerfect's history, https://www.transperfect.com/about/history). BCV's round "
         "(by 2003) is not named."))
L.append(cls("evenup", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2025-10",
    val_cite=NEWS("evenup", "Doubles Valuation To $2B"), extra={"valuation_range_source": "web_verified"},
    country="US", city="San Francisco", focus="AI & Applied AI",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("leveling-the-legal-playing-field"), entry_date="2023-06",
    note="AI for personal-injury law firms (San Francisco). 'After first investing in EvenUp's Series B' (the firm's post, 2024-10-08; the "
         "$50.5M Series B of June 2023, first published for that round); BCV returned in the $135M Series D. Mark: the October 2025 Series E "
         "at $2B (Crunchbase News), aligned with sibling Lightspeed; momentum check found no later priced round."))
L.append(cls("eyetel-imaging", status="acquired", rng="below_1b", country="US", city="Columbia", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=EYETEL_SB2, entry_date="2004-01",
    note="Diabetic retinopathy screening (DigiScope; Columbia, MD). 'In January 2004, we completed our Series B convertible preferred stock "
         "financing led by Bain Capital Ventures and Radius Ventures' (EyeTel's SB-2, 2007; Bain Capital Venture Fund 2001 signed the "
         "investor rights agreement); a Series B entry reads Growth. The firm's 2010-2013 listings mark it Acquired; no source read names "
         "the buyer."))
L.append(cls("feather", status="acquired", rng="below_1b", country="US", city="New York", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2017", flags=["stage_uncited"],
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("feather", "Feather Raises Another $12M"),
    rounds=[rnd("2019-05", "Series A", 12000000, "Spark Capital", True, NEWS("feather", "Feather Raises Another $12M"), "press")],
    note="Furniture rental subscription (New York). BCV (Salil Deshpande) is on the firm's list from its January 2018 capture, before "
         "the $12M Series A led by Spark Capital with Bain Capital Ventures participating (AlleyWatch, 2019-05-15; $16M across three "
         "rounds), so BCV entered in the seed; no page names that round (stage_uncited). 'Luxury furniture rental company Vesta acquires "
         "Fernish and Feather' (Retail Dive, 2023-11-13, " + NEWS("feather", "Vesta acquires Fernish and Feather") + "): acquired, "
         "fresher than sibling Spark's private and aligned with Y Combinator's row."))
L.append(cls("fidel-api", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=NEWS("fidel-api", "raises $65M led by Bain Capital"), city="London", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("fidel-api", "Fidel API Raises $65 Million Series B"),
    entry_date="2022-04",
    note="Card-linked transaction APIs (London-based, per TechCrunch). 'Fidel API Raises $65 Million Series B' led by Bain Capital "
         "Ventures (businesswire, 2022-04-06); a Series B entry reads Growth. Momentum check (fintech, first seen 2022): no $1B+ priced "
         "round found."))
L.append(cls("fingerhut", status="acquired", rng="below_1b", country="US", city="Eden Prairie", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2004-02",
    note="Fingerhut Direct Marketing, renamed Bluestem Brands (Eden Prairie), the same company as the base row bluestem-brands. "
         "'In February of 2004, Brookside Capital Investors, L.P., funds affiliated with Bain Capital, and funds affiliated with Battery "
         "Ventures ... made the first of their investments in us, and at that time the ownership interest of Thomas Petters and his "
         "affiliates in our company was reduced to a minority position' (Bluestem's S-1, 2011, " + BLUESTEM_S1 + "): an investment in an "
         "operating retailer two years after the 2002 asset purchase, read as Growth. Sold to Capmark Financial in 2014 (the firm's "
         "listing), aligned with bluestem-brands and sibling Battery. OPEN for Erik: Wikipedia counts 'Bain Capital Ventures (2004)' "
         "among Fingerhut's owners, and the sponsor group held about 49% fully diluted in 2011; whether the 2004 group took 50% or more "
         "(a control position, D4) is not stated in any source read."))
L.append(cls("flood", status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.theblock.co/post/276664/bain-capital-crypto-flood-ethereum-funding", entry_date="2023",
    flags=["model_disputes_source"],
    note="DEX aggregator on Ethereum and Arbitrum, on Bain Capital Crypto's list. 'Bain Capital Crypto leads $5.2 million seed round for "
         "Ethereum-focused DEX aggregator Flood' (The Block, announced 2024-02-08; the round, equity with token warrants, closed in summer "
         "2023; the release carries a San Francisco dateline). '0x Acquires Competitor Flood' (CoinDesk, 2025-05-15, "
         + NEWS("flood", "0x Acquires Competitor Flood") + "). The prefilled defunct status and British country came from a wrong join. "
         "Graduation left for the graduation pass."))
L.append(cls("foghorn-systems-johnson-controls", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
    focus="AI & Applied AI", stage="undetermined",
    note="Edge AI software for industrial IoT (Sunnyvale). 'Johnson Controls acquires FogHorn' (EdgeIR, 2022-01-13, "
         + NEWS("foghorn-systems-johnson-controls", "integrates Edge AI platform") + "). The firm's listing gives 2011, three years "
         "before FogHorn's 2014 founding, so the year is not usable; BCV's round is not named."))
L.append(cls("formation-systems", status="acquired", rng="below_1b", country="US", city="Southborough", focus="SaaS",
    stage="undetermined",
    note="Product lifecycle software for process industries (Southborough, MA, in the firm's listings 2003-2013, Michael Krupka). The firm "
         "lists it as acquired (2006 per sibling Lightspeed's row). BCV's round (by 2003) is not named."))
L.append(cls("forus-fka-tandem-health", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified", asof="2026-09-08",
    val_cite=NEWS("forus-fka-tandem-health", "Series C At $3 Billion Valuation Led By Bain"),
    extra={"valuation_range_source": "web_verified"}, country="US", city="New York", city_src="web_verified", focus="Healthcare & Bio",
    stage="Seed", **site_stage("forus-fka-tandem-health"), entry_date="2023",
    grad="graduated", grad_src="web_verified", grad_conf="high",
    grad_cite=NEWS("forus-fka-tandem-health", "Series C At $3 Billion Valuation Led By Bain"),
    rounds=[rnd("2026-09", "Series C", 150000000, "Bain Capital Ventures", True,
                NEWS("forus-fka-tandem-health", "Series C At $3 Billion Valuation Led By Bain"), "press")],
    note="AI network for prescription access (formerly Tandem; New York-based per Pulse 2.0). BCV's listing: 2023, Seed (Kevin Zhang); "
         "the Series C release names BCV as investor since the seed round (as read by sibling Thrive's run). Later rounds: $160M announced "
         "in May 2026 (its Series A, which General Catalyst led, and Series B), then 'Forus Raises $150 Million Series C At $3 Billion Valuation Led By "
         "Bain Capital Ventures' (Pulse 2.0, 2026-09-08). Mark: $3B; siblings Accel, General Catalyst, Redpoint and Thrive still read "
         "below_1b, and this cited round is fresher."))
L.append(cls("fuel", status="private", rng="below_1b", country="CA", country_src="web_verified",
    country_cite="https://tracxn.com/d/companies/fuel-labs/__AO7_6_QETJlySdpmUKZcLIdM6gcRlCkRv3kOcxZnzRM", city="Toronto",
    city_src="web_verified", focus="Crypto & Web3",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2022-09",
    note="Fuel Labs, the modular execution layer (Fuel Network), on Bain Capital Crypto's list. 'Fuel Labs raises $80 million' led by "
         "Blockchain Capital and Stratos with Bain Capital Crypto participating (The Block, 2022-09-06, "
         + NEWS("fuel", "Fuel Labs raises $80 million") + "), after a $1.5M CoinFund-led seed in 2021: its first large institutional "
         "round, read as Series A; the instrument and valuation were not disclosed. The company told The Block it has no headquarters; "
         "Tracxn places it in Toronto (incorporated in the Cayman Islands), a location only. Momentum check: no $1B+ priced round found; "
         "the FUEL token trades far below its launch value."))
L.append(cls("futuredontics", status="acquired", rng="below_1b", country="US", city="Los Angeles", focus="Healthcare & Bio",
    stage="undetermined", entry_date="2010",
    note="Futuredontics, the company behind 1-800-DENTIST (Los Angeles), the same company as the base row 1-800-dentist. The firm's "
         "listing: 2010 (Paul Zurlo), Acquired; by 2021 it was 'CriticalPoint-backed Futuredontics' (PE Hub, 2021-07-21, "
         + NEWS("futuredontics", "CriticalPoint-backed") + "). BCV's 2010 round is not named."))
L.append(cls("gamelogic", status="acquired", rng="below_1b", country="US", city="Waltham", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Online games and promotions (GameLogic, Inc., Waltham, MA, in the firm's listings 2006-2013, Jeff Schwartz, 'Midstage'). The "
         "firm's own listing marks it Acquired, which is fresher cited evidence than sibling General Catalyst's unknown; no source read "
         "names the buyer. BCV's round is not named."))
L.append(cls("gradle", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="DevTools & APIs", stage="undetermined",
    note="Gradle Inc., the company behind the Gradle build tool (San Francisco). On the firm's list from its January 2017 capture (Salil "
         "Deshpande, who names Gradle among his open-source investments); Bain Capital Ventures joined the $27M Series C led by Triangle "
         "Peak Partners (https://www.prweb.com/releases/Gradle_Inc_Raises_27_Million_in_Series_C_Funding/prweb18343348.htm, 2021-11-18). "
         "BCV's entry round, before 2017, is not named."))
L.append(cls("grain", status="private", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("grain", "Grain emerges from stealth"), city="Tel Aviv", city_src="web_verified", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("global-commerce-demands"), entry_date="2025-03",
    note="FX hedging embedded in B2B payments (Tel Aviv-based, per TechCrunch). 'Today, we're excited to announce Grain's BCV-led $33 "
         "million Series A' (the firm's post, 2025-03-05); Aleph led the seed. Momentum check (fintech, 2025): no later priced round "
         "found. Sibling Y Combinator's Grain (San Francisco, a 2020 batch) is a different company."))
L.append(cls("harness-wealth", status="private", rng="below_1b", country="US", city="New York", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("harness-wealth", "Harness Wealth Raises $4M"),
    entry_date="2018-12",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("harness-wealth", "Harness Wealth Raises $15M"),
    rounds=[rnd("2021-07", "Series A", 15000000, "Jackson Square Ventures", True, NEWS("harness-wealth", "Harness Wealth Raises $15M"),
                "press")],
    note="Tax and wealth advice platform (New York). 'Harness Wealth raised a $4M Seed round' with Bain Capital Ventures named first "
         "among its backers (AlleyWatch, 2018-12); the $15M Series A led by Jackson Square Ventures followed with Bain Capital "
         "participating (AlleyWatch, 2021-07)."))
L.append(cls("hera", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("hera", "Series A Led By Bain"), entry_date="2026-06",
    flags=["model_disputes_source"],
    note="Senior care coordination covered by Medicare (Hera Health, New York, aligned with sibling Accel). 'Hera Raises $27 Million Series "
         "A Led By Bain Capital Ventures' (Pulse 2.0, 2026-06-26), a month after Accel's seed. The prefilled Japanese country is a wrong "
         "join; the company serves US states only. Sibling Y Combinator's Hera (Paris, a 2021 batch) is a different company."))
L.append(cls("hi-marley", status="private", rng="below_1b", country="US", city="Boston", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prnewswire.com/news-releases/hi-marley-closes-8-million-series-a1-preferred-financing-to-accelerate-go-to-market-and-product-expansion-301086163.html",
    entry_date="2020-06",
    note="Text messaging platform for insurers (Boston). 'The new funding was led by True Ventures and Underscore VC, along with Bain Capital "
         "Ventures and Greenspring Associates' (the $8M Series A1, PR Newswire, 2020-06-30), BCV's first round, an extension of the "
         "Series A; Emergence led the $25M Series B in March 2021."))
L.append(cls("hyde", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified", focus="AI & Applied AI",
    stage="Seed", **site_stage("hyde"), entry_date="2025", grad="censored", flags=["model_disputes_source"],
    note="Training and inference stack for enterprise specialist models (Campfire). BCV's listing: 2025, Seed (Kevin Zhang); inside 24 "
         "months, so censored. Its site's job listings are mostly in New York City (also Mumbai and London). The prefilled acquired status "
         "and Japanese country are wrong joins (sibling General Catalyst reads the same). Momentum check (AI, 2025): no priced round found."))
L.append(cls("imagemover", status="private", rng="below_1b", country="US", city="Madison", city_src="web_verified",
    focus="Healthcare & Bio", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("imagemover", "ImageMoverMD raises $4 million"), entry_date="2019-02",
    note="ImageMoverMD, clinical image capture into the medical record (Madison, WI). A $4M Series B led by Bain Capital Ventures (BizTimes, "
         "2019-02-11, Yumin Choi quoted); a Series B entry reads Growth. Still operating (its site, copyright 2024)."))
L.append(cls("imagitas", status="acquired", rng="below_1b", country="US", city="Waltham", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Direct marketing through the USPS change-of-address mailings (Waltham, MA). The firm's 2006 listing marks it Acquired (Pitney "
         "Bowes bought it in 2005). BCV's round is not named."))
L.append(cls("imerica", status="acquired", rng="below_1b", country="US", city="Tampa", focus="Healthcare & Bio",
    stage="undetermined", entry_date="2005-04",
    note="Imerica Life and Health Insurance Company, HSA-qualified health plans (Tampa). Announced 'a $13.5 million investment by Bain "
         "Capital Ventures' with a new CEO in April 2005 (https://www.biospace.com/b-imerica-life-and-health-insurance-company-b-"
         "announces-appointment-of-b-rod-farmer-b-as-ceo-and-a-13-5-million-investment-by-bain-capital-vent); the round is not named "
         "and the release does not state the stake. The firm's 2006-2013 listings mark it Acquired."))
L.append(cls("index", status="private", rng="below_1b", country="AU", country_src="web_verified",
    country_cite=NEWS("index", "Canva and Atlassian alumni"), city="Sydney", city_src="web_verified", focus="AI & Applied AI",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("index", "Canva and Atlassian alumni"),
    entry_date="2025-02", grad="censored", flags=["model_disputes_source"],
    note="AI product planning tool (Sydney; founders from Atlassian and Canva). A $3.5M seed led by Blackbird and Bain Capital Ventures "
         "(Startup Daily, 2025-02-12); inside 24 months, so censored. The prefilled acquired status came from a wrong join to the UK "
         "catalogue retailer Index (Littlewoods). Momentum check (AI, 2025): no later priced round found. Siblings Greylock's Index "
         "(Cambridge) and Y Combinator's Index (2019 batch) are different companies."))
L.append(verdict("instinet", "not_member",
    HERITAGE + "Another desk and a listed-company stake (decisions.md D2, D4): Instinet Group was listed on NASDAQ from 2001, and its "
    "Bain Capital holders were Bain Capital Fund VII, Bain Capital VII Coinvestment Fund, BCI Datek Investors and the BCIP employee "
    "vehicles (Schedule 13G/A for 2003), the generalist fund family, with no venture vehicle among them; the shares trace to Bain "
    "Capital's Datek stake (Island ECN merged into Instinet in 2002). The firm's 2006 and 2010 listings filed it under "
    "'Expansion/Growth Buyout'. A position in a listed company is not a venture round (COLLECTION.md s1 T3).",
    ec="site_listing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/0001132327/000119312504022890/dsc13ga.htm"))
control("ipay",
    "iPay Technologies (Elizabethtown, KY) 'completed a recapitalization with Spectrum Equity and Bain Capital Ventures' in December "
    "2006, and its co-founder called them 'our new majority shareholders' (Spectrum Equity's release); the firm's archive filed it under "
    "'Expansion/Growth Buyout'. Jack Henry bought iPay for $300M in 2010.",
    "https://www.spectrumequity.com/news/ipay-technologies-receives-investment-from-spectrum-equity/")
L.append(cls("iron-io", status="private", rng="below_1b", country="US", city="San Francisco", focus="DevTools & APIs",
    stage="undetermined",
    note="Serverless job and message queue services (IronWorker, IronMQ; San Francisco in its venture years). On the firm's 2016-2017 "
         "lists only, no partner named; still operating (its site, copyright 2025). BCV's round is not named."))
L.append(cls("irreducible", status="private", rng="below_1b", country="DE", country_src="web_verified",
    country_cite=NEWS("irreducible", "Paradigm co-leads"), city="Berlin", city_src="web_verified", focus="Crypto & Web3",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite="https://www.theblock.co/post/203568/zk-proof-funding-seed",
    entry_date="2022-06",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("irreducible", "Paradigm co-leads"),
    rounds=[rnd("2025-01", "Series A", 24000000, "Paradigm and Bain Capital Crypto", True, NEWS("irreducible", "Paradigm co-leads"),
                "press")],
    note="Zero-knowledge proof hardware and software (Ulvetanna, renamed Irreducible; Berlin). 'Bain Capital Crypto and Paradigm co-led the "
         "seed round' of $15M, an equity round at $55M that closed in June 2022 (The Block, 2023-01-19); Paradigm and Bain Capital Crypto "
         "co-led the $24M Series A in January 2025 (The Block). Momentum check: no $1B+ priced round found."))
L.append(cls("iwon-com", status="acquired", rng="below_1b", country="US", city="Irvington", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="iWon, the prize-draw web portal (Irvington, NY), on the firm's 2003-2010 lists ('Early'). It combined with Excite and was bought "
         "by Ask Jeeves in 2004, later IAC (Wikipedia: 'last owned by Barry Diller's IAC'); the site closed in 2016. BCV's round is not "
         "named."))
L.append(cls("jadu", status="private", rng="below_1b", country="US", city="Los Angeles", city_src="web_verified",
    focus="Media, Gaming & Advertising", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("jadu", "Jadu Raises $36M"), entry_date="2022-05", flags=["model_disputes_source"],
    note="Augmented-reality games (Jadu AR, Los Angeles), on Bain Capital Crypto's list from 2022-05-27. 'Bain Capital led the Series A "
         "round and was joined by existing investor General Catalyst Partners' ($36M, dot.la, 2022-05-27), an equity round. The prefilled "
         "British country is a wrong join, as sibling General Catalyst also found."))
L.append(cls("jott-networks", status="acquired", rng="below_1b", country="US", city="Seattle", focus="SaaS",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2007-05",
    note="Voice-to-text messaging (Seattle, founded 2006). BCV led the company's first equity financing of $5.4M in May 2007 with Draper "
         "Richards, Ackerley Partners and Atomico (Light Reading, as cited by sibling Atomico's row), read as its Series A. 'Jott Networks "
         "was acquired by Nuance in July 2009' (the firm's own listing)."))
L.append(cls("jtech", status="acquired", rng="below_1b", country="US", city="Boca Raton", focus="Industrial & Robotics",
    stage="undetermined",
    note="On-site paging systems for restaurants and hospitals (JTECH Communications, Boca Raton, FL), on the firm's 2003 and 2006 lists "
         "('Midstage'), marked Acquired; it operates today as part of HM Electronics. BCV's round is not named."))
L.append(cls("jupiterone", status="private", rng="below_1b", country="US", city="Morrisville", focus="Security",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2020-09",
    note="Cyber asset management on a graph data model (Morrisville, NC). BCV's listing: 2020, Early (Enrique Salem). 'JupiterOne Lands $19 "
         "Million Funding Round' (businesswire, 2020-09-17), its first outside round after the LifeOmic spin-out and before Sapphire's "
         "Series B of May 2021, read as its Series A. The June 2022 Series C release claims 'a valuation of over $1B' ("
         + NEWS("jupiterone", "Achieves Valuation of Over") + ") without a figure, so no mark can be recorded (COLLECTION.md s6 Rule A, "
         "as for ShipBob in batch 4)."))
L.append(cls("klutch", status="private", rng="below_1b", country="US", city="Seattle", city_src="web_verified", focus="AI & Applied AI",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("klutch", "Seattle startup Klutch"), entry_date="2025-06",
    grad="censored",
    note="AI agents for construction teams (Seattle). An $8M seed co-led by Bling Capital and Bain Capital Ventures (GeekWire, 2025-06-26); "
         "inside 24 months, so censored. Momentum check (AI, 2025): no later priced round found."))
L.append(cls("krea", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="AI & Applied AI", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("krea", "Krea raises $83M to be"), entry_date="2025-04",
    note="Generative image and video tools for creatives (San Francisco). 'Bain Capital Ventures is leading the latest round', the $47M "
         "Series B, at $500M post-money (TechCrunch, 2025-04-07); a Series B entry reads Growth. Momentum check (AI, 2025): no $1B+ priced "
         "round found; aligned with sibling a16z (below_1b)."))
L.append(cls("laika", status="private", rng="below_1b", country="US", city="New York", focus="Security",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("laika", "Canapi Ventures, Bain Capital"),
    entry_date="2020-09", flags=["model_disputes_source"],
    note="Security compliance automation (Laika, renamed Thoropass in 2023; New York). A $10M Series A 'from Canapi Ventures, Bain Capital, "
         "and NYCA' (Business Insider, 2020-09-23); the firm's list carries it from late 2020 (Matt Harris), which ties the press line to "
         "BCV (D7). J.P. Morgan led the $35M Series B (2021) and Fin Capital the $50M Series C (2022). The prefilled Belgian country is a "
         "wrong join. Sibling Y Combinator's Laika (Bogota pet commerce) is a different company."))
L.append(cls("lala-media", status="acquired", rng="below_1b", country="US", city="Palo Alto", focus="Media, Gaming & Advertising",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2006",
    note="Lala, the music trading and streaming service (La La Media, Palo Alto). It 'was venture funded by Bain Capital and Ignition "
         "Partners' (" + W("Lala (website)") + "), its founding venture backers, read as its Series A; the firm listed it from 2006 (Mike "
         "Krupka). Apple acquired it on 2009-12-04."))
L.append(cls("legacy", status="private", rng="below_1b", country="US", city="Boston", city_src="web_verified", focus="Healthcare & Bio",
    stage="Seed", **site_stage("legacy"), entry_date="2019",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("legacy", "Legacy Raises $10M Series A"),
    rounds=[rnd("2021-04", "Series A", 10000000, "FirstMark Capital", True, NEWS("legacy", "Legacy Raises $10M Series A"), "press")],
    flags=["model_disputes_source"],
    note="At-home sperm testing and freezing (Give Legacy, Boston). BCV's listing: 2019, tagged Seed and Early; the $10M Series A of April "
         "2021 led by FirstMark lists Bain Capital Ventures among existing investors (PR Newswire, dateline Boston, 'headquartered in "
         "Boston'), so BCV entered at the seed. The prefilled Argentine country is a wrong join. Sibling Y Combinator places it in New "
         "York; the release, the firm's listing (Cambridge, MA) and the company's 617 number say Boston."))
L.append(cls("legora", status="private", rng="1b_plus", usd=5550000000, val_src="web_verified", asof="2026-03-10",
    val_cite=NEWS("legora", "Triples Valuation To $5.55B"), extra={"valuation_range_source": "web_verified"},
    city="Stockholm", focus="AI & Applied AI", stage="Growth", **site_stage("legora"), entry_date="2026-03",
    note="Collaborative AI for lawyers (Stockholm). BCV's listing: 2026, Growth (Merritt Hummer, Abby Meyers); the firm's post 'Investing "
         "in Legora' is dated 2026-03-10, the day of the $550M Series D led by Accel at $5.55B (Crunchbase News). Mark: $5.55B, aligned "
         "with the siblings; the September 2026 talks at $8.5B (Bloomberg) are not a closed round."))

if __name__ == "__main__":
    jl.write("batch-008", L)
