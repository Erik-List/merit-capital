"""PRO-162 grind, batch-009 (lightsource .. oratomic). Evidence: show.py rows, the firm's archived company pages (Common
Crawl captures under data/filings/commoncrawl/bain-capital-ventures/), the firm's posts, Google News (nq.py, tag b9) and
twelve web searches on 2026-09-27 (URLs they printed are cited as printed). Three verdict lines: MAXM Systems is a
heritage position (acquired January 1997, before any venture vehicle), OneSource was a 1993 management buy-out by
Information Partners Capital Fund (Bain Capital, David Dominik) with William Blair (44% each), and M|C Communications
was bought outright by Bain Capital in 2004 (with its acquisition vehicle m-c-acquisition-corp). Onbe folds into
davinci-payments (identity-merges.json) and is aligned with it; MagazineRadar is MediaRadar (row media-radar), aligned."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []
V = {"valuation_range_source": "web_verified"}
_B = {r["slug"]: r for r in json.loads((Path(__file__).resolve().parent.parent / "companies" / "base.json").read_text())}


def WB(slug):
    """The row's own archived-listing link, read from base.json."""
    return _B[slug]["wayback_first_link"]


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


TAG = "[bain_capital_heritage] "

# ---- verdict lines (membership problems) ----
L.append(verdict("maxm-systems", "not_member",
    TAG + "Another desk (decisions.md D2, R1): 'MAXM Systems was acquired by Boole & Babbage in January 1997' (the firm's own 2012 "
    "company page), so Bain Capital's position predates 1997, before any Bain Capital venture vehicle existed (Bain Capital Venture "
    "Fund, L.P. dates from 1999). A position of Bain Capital's generalist funds, which the firm's 2003-2013 listings carry as history.",
    ec="site_listing", conf="high", cite=CCPAGE("/portfolio/company/maxm-systems")))
L.append(verdict("onesource-information-services", "not_member",
    TAG + "OneSource's S-1 (1999): 'In connection with the management buy-out from Lotus in 1993, each of William Blair Venture "
    "Partners III Limited Partnership and Information Partners Capital Fund, L.P. ... purchased' the same stake, and each held 44.0% "
    "before the IPO; Information Partners Capital's general partner, David Dominik, was a managing director at Bain Capital. A 1993 "
    "buy-out in which the Bain Capital fund and its co-investor took 88%: a control acquisition, not a venture round (COLLECTION.md s1 "
    "T3 control positions; decisions.md D4), made before any Bain Capital venture vehicle existed (D2, R1). The firm's 2006 listing "
    "files it under 'Expansion/Growth Buyout'.",
    ec="site_listing", conf="high",
    cite="https://www.sec.gov/Archives/edgar/data/0001079880/000095013599001196/0000950135-99-001196.txt")
    | {"exclusion": "control_position"})
MC_CITE = "https://tradeshowexecutive.com/mooney-and-partners-agree-to-sell-m-c-communications-to-bain-capital/"
L.append(verdict("m-c-communications", "not_member",
    "M|C Communications (Pri-Med medical education conferences, Boston): 'Mooney and Partners Agree to Sell M/C Communications to "
    "Bain Capital' (Trade Show Executive, 2004; expected price about $400M, 12 times EBITDA, closing August 2004). The founders sold "
    "the company; the vehicle was M|C Acquisition Corp. (Delaware, incorporated 2004; its 2009 Form D is a business-combination filing "
    "at the company's own address with John Connolly on the board), and the firm's 2006-2013 listings file it under 'Expansion/Growth "
    "Buyout'. An outright purchase of the company is a control acquisition, not a venture round (COLLECTION.md s1 T3 control "
    "positions; decisions.md D4).",
    ec="site_listing", conf="high", cite=MC_CITE) | {"exclusion": "control_position"})
L.append(verdict("m-c-acquisition-corp", "not_member",
    "M|C Acquisition Corp. is the 2004 acquisition vehicle of M|C Communications (merges into 'm-c-communications'), which Bain "
    "Capital bought outright from its founders in 2004 (Trade Show Executive): a control acquisition (COLLECTION.md s1 T3; "
    "decisions.md D4). This replaces the membership recorded for the merge.",
    ec="site_listing", conf="high", cite=MC_CITE) | {"exclusion": "control_position"})

# ---- classification lines ----
L.append(cls("lightsource", status="private", rng="below_1b", city="San Francisco", city_src="web_verified", focus="SaaS",
    stage="Seed", **site_stage("lightsource"), entry_date="2021",
    grad="graduated", grad_src="web_verified", grad_conf="medium", grad_cite=NEWS("lightsource", "From Stealth to Series A"),
    note="AI-native sourcing and procurement software (San Francisco; CNBC). BCV's listing: 2021, Seed (Ajay Agarwal). It emerged from "
         "stealth in March 2025 with $33M 'led by Bain Capital Ventures and Lightspeed Venture Partners' (CNBC, "
         + NEWS("lightsource", "big business for supply chain software") + "), the Series A ('From Stealth to Series A', Procurement "
         "Magazine), aligned with Lightspeed's Series A row. Momentum check 2026-09-27 (Google News): no $1B+ round found.",
    rounds=[rnd("2025-03", "Series A", None, "Bain Capital Ventures and Lightspeed Venture Partners", True,
                NEWS("lightsource", "big business for supply chain software"), "press")]))
L.append(cls("lithos-carbon", status="private", rng="below_1b", country="US", city="Seattle", focus="Climate & Energy",
    stage="Seed", **site_stage("lithos-carbon"), entry_date="2022",
    note="Enhanced rock weathering for carbon removal on farms (Seattle, the firm's listing; founded 2022); operating in 2026 (Microsoft "
         "and Climeworks offtake deals). BCV's listing: 2022, Seed (Kevin Zhang, Aaref Hilaly), aligned with USV. Graduation left for "
         "the graduation pass."))
L.append(cls("lolli", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified", focus="Crypto & Web3",
    stage="undetermined",
    note="Bitcoin rewards for online shopping (New York; 'Headquarters: New York City', CNBC Upstart 100, 2019, which names Bain Capital "
         "Ventures among its top investors). The firm listed it from 2018 (Scott Friend). Rounds on record: a $3M seed in 2020, a 2021 "
         "Series A led by Seven Seven Six and an $8M Series B led by BITKRAFT in December 2023 (Business Insider, "
         + NEWS("lolli", "Lolli Overcomes Tough Crypto") + "); it bought Slice in 2025. BCV's 2018 round is not named.",
    rounds=[rnd("2020", "Seed", 3000000, None, None, NEWS("lolli", "Lolli Overcomes Tough Crypto"), "press"),
            rnd("2021-07", "Series A", 10000000, "Seven Seven Six", None, NEWS("lolli", "Lolli raises $10 million in Series A"), "press"),
            rnd("2023-12", "Series B", 8000000, "BITKRAFT Ventures", None, NEWS("lolli", "Lolli Overcomes Tough Crypto"), "press")]))
L.append(cls("loyal", status="private", rng="below_1b", city="San Francisco", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("loyal", "Loyal: $45 Million Raised"),
    entry_date="2024-03",
    note="Dog lifespan-extension drugs (Cellular Longevity, Inc.; San Francisco). 'Bain Capital Ventures led the funding round', the "
         "$45M Series B of March 2024, with BCV a new investor (Pulse 2.0): a Series B entry reads Growth. A $22M Series B-2 (2025) and "
         "a $100M Series C led by age1 (February 2026) followed with no published valuation; aligned with First Round and Khosla.",
    rounds=[rnd("2024-03", "Series B", 45000000, "Bain Capital Ventures", True, NEWS("loyal", "Loyal: $45 Million Raised"), "press")]))
LUMI = NEWS("lumilens", "Lumilens Emerges From Stealth With Over $900 Million")
L.append(cls("lumilens", status="private", rng="1b_plus", usd=5510000000, val_src="web_verified", asof="2026-08-06", val_cite=LUMI,
    extra=V, country="US", city="San Francisco", focus="Industrial & Robotics",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LUMI, entry_date="2026-08",
    note="Photonic interconnects for AI data centers (San Francisco, as Redpoint's row). It emerged from stealth with more than $700M "
         "in new financing 'co-led by Atreides Management, Bain Capital Ventures, Meritech, Seligman Ventures and Spark Capital'; 'The "
         "round values Lumilens at $5.51 billion' (Pulse 2.0, 2026-08-06; the Series C, AI Insider). BCV's listing: 2026, Growth. "
         "Redpoint's row reads below_1b from before this round; this mark is fresher.",
    rounds=[rnd("2026-08", "Series C", 700000000, "Atreides, Bain Capital Ventures, Meritech, Seligman Ventures, Spark Capital", True,
                LUMI, "press")]))
L.append(cls("lumina", status="acquired", rng="below_1b", country="US", country_src="web_verified",
    country_cite=CCPAGE("/portfolio/lumina"), city="San Francisco", city_src="web_verified", focus="Crypto & Web3",
    stage="undetermined", flags=["model_disputes_source"],
    note="Digital-asset prime dealer and portfolio platform for hedge funds and family offices (lumina.app, San Francisco, the firm's "
         "2019 page, Salil Deshpande). BitGo acquired it in 2020 ('the tax reporting and portfolio tools of Lumina, a company it "
         "acquired in April', The Block, " + NEWS("lumina", "BitGo launches BitGo Prime") + "). The prefilled 'defunct' and Romanian "
         "country came from a wrong join; YC's 'Lumina' (Singapore, AI) is a different company. BCV's round is not named."))
L.append(cls("m-qube", status="acquired", rng="below_1b", country="US", city="Watertown", focus="Media, Gaming & Advertising",
    stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=CCPAGE("/portfolio/company/m-qube"), entry_date="2002-05",
    note="Mobile content delivery, messaging and billing across carriers (Watertown, MA). 'Bain Capital Ventures led the series A "
         "funding of m-Qube in May 2002' and 'm-Qube was acquired by VeriSign in May 2006' (the firm's own company page, 2012 capture).",
    rounds=[rnd("2002-05", "Series A", None, "Bain Capital Ventures", True, CCPAGE("/portfolio/company/m-qube"), "firm")]))
L.append(cls("m0", status="private", rng="below_1b", country="CH", country_src="web_verified",
    country_cite="https://dealroom.co/companies/m0-1/", city="Zug", city_src="web_verified", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("m0", "Bain Capital Crypto leads $35 million Series A for stablecoin"), entry_date="2024-06",
    note="Stablecoin issuance platform (M^0 Labs; 'legally domiciled in Zug, Switzerland', Dealroom), on Bain Capital Crypto's list. "
         "'M^0 ... has raised $35 million in a Series A funding round led by Bain Capital Crypto', structured as equity plus tokens (The "
         "Block, 2024-06-05), after Pantera's $22.5M seed of April 2023; a priced equity round, so not token-funded. Momentum check "
         "2026-09-27: the $40M Series B of August 2025 (Polychain and Ribbit, with Bain Capital Crypto in) disclosed no valuation (CoinDesk); Dealroom's "
         "$100M-250M range is a vendor estimate (Rule A), so below_1b.",
    rounds=[rnd("2023-04", "Seed", 22500000, "Pantera Capital", None,
                NEWS("m0", "Bain Capital Crypto leads $35 million Series A for stablecoin"), "press"),
            rnd("2024-06", "Series A", 35000000, "Bain Capital Crypto", True,
                NEWS("m0", "Bain Capital Crypto leads $35 million Series A for stablecoin"), "press"),
            rnd("2025-08", "Series B", 40000000, "Polychain and Ribbit Capital", True,
                NEWS("m0", "Stablecoin News: Startup M0 Raises"), "press")]))
L.append(cls("magazineradar", status="acquired", rng="below_1b", country="US", city="New York", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Ad-sales intelligence for magazines (New York, 252 West 37th Street in the firm's 2010 listing; Scott Friend, Sunny Sethi). "
         "It was renamed MediaRadar: the firm's 2013 software listing already carries 'MediaRadar', which is the base row 'media-radar' "
         "(one company, two rows; aligned with that row's acquired status and city). BCV's round is not named."))
L.append(cls("magical", status="private", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("automation-for-everyone"), entry_date="2020",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("magical", "Magical nabs $35M"),
    note="Browser automation across tabs (San Francisco). BCV 'helped incubate, co-led a seed financing, and committed additional dollars "
         "to a Series A' (the firm's post, 2022-06-06; listing 2020, Seed). Coatue led the $35M Series A with Greylock and Bain, after "
         "a $6M seed (TechCrunch, 2022-06-06). Aligned with Coatue and Greylock.",
    rounds=[rnd("2022-06", "Series A", 35000000, "Coatue", True, NEWS("magical", "Magical nabs $35M"), "press")]))
L.append(cls("maintainx", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("maintainx-is-bringing"), entry_date="2023-12",
    note="Maintenance and operations software for frontline teams (San Francisco). 'We are excited to announce that we are leading "
         "MaintainX's $50 million Series C', which 'brings MaintainX's valuation to $1 billion' (the firm's post, 2023-12-06); BCV "
         "co-led the $150M Series D (2025). Autodesk bought it for about $3.6B and closed on 2026-08-03 ("
         + NEWS("maintainx", "closes MaintainX Inc. acquisition") + ")."))
L.append(cls("market-metrics", status="acquired", rng="below_1b", country="US", city="Quincy", focus="Data Infrastructure",
    stage="undetermined",
    note="Collected and distributed data on customer shopping trends (Quincy, MA; the firm's 2006 listing marks it acquired). The firm "
         "listed it in 2003 and 2006 with no partner, round or date; the acquirer is not named on any surface read."))
L.append(cls("marriage-pact", status="private", rng="below_1b", country="US", city="Palo Alto", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("marriage-pact", "Marriage Pact secures $5 million"),
    entry_date="2022-09",
    note="College matchmaking (founded at Stanford; Palo Alto, the firm's listing). 'Marriage Pact ... received $5 million in seed "
         "funding from Bain Capital Ventures', which led the round, closed in September 2022 (The Stanford Daily). Graduation left for "
         "the graduation pass."))
L.append(cls("medivision", status="acquired", rng="below_1b", country="US", city="Houston", focus="Healthcare & Bio",
    stage="undetermined",
    note="Acquirer and operator of outpatient ophthalmic surgery centers (Houston; the firm's 2006 listing marks it acquired). The firm "
         "listed it in 2003 and 2006 with no partner or date; a web search found neither the round nor the acquirer."))
MEELA = "https://finance.yahoo.com/news/meela-launches-personalized-ai-companion-160000691.html"
L.append(cls("meela", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="AI & Applied AI", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MEELA, entry_date="2025-09-11",
    grad="censored",
    note="AI voice companion for seniors ('NEW YORK, September 11, 2025 (BUSINESS WIRE) ... announced $3.5 million in seed funding led "
         "by Bain Capital Ventures', the company's release). Entry inside the 24-month window, so censored. Momentum check 2026-09-27: "
         "no later round found."))
MIFERIA = "https://www.prnewswire.com/news-releases/miferia-raises-7-million-to-digitalize-inventory-procurement-in-mexico-301601172.html"
L.append(cls("mercanto", status="private", rng="below_1b", country="MX", country_src="web_verified", country_cite=MIFERIA,
    city="Mexico City", city_src="web_verified", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MIFERIA, entry_date="2022-08-08",
    note="B2B wholesale marketplace (Miferia, renamed Mercanto; Mexico City), now supplying restaurants (its site, 2026). 'MEXICO CITY, "
         "Aug. 8, 2022: Miferia ... announced a $7 million seed round co-led by Bain Capital Ventures and Tiger Global' (PR Newswire). "
         "Graduation left for the graduation pass."))
MR_VAL = NEWS("mind-robotics", "valued at $3.4 billion in new funding round - CNA")
MR_A = NEWS("mind-robotics", "Rivian-Backed Mind Robotics Startup Raises $500")
L.append(cls("mind-robotics", status="private", rng="1b_plus", usd=3400000000, val_src="web_verified", asof="2026-05-13",
    val_cite=MR_VAL, extra=V, country="US", city="Palo Alto", focus="Industrial & Robotics",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=MR_A, entry_date="2026-03",
    note="AI industrial robotics, a Rivian spinout (Palo Alto). BCV is named among the investors of the $500M Series A of March 2026 "
         "that Accel and Andreessen Horowitz led at $2B (Orange County Business Journal), after Eclipse's $115M seed. The "
         "Kleiner Perkins-led $400M round of May 2026, with BCV as an existing investor, valued it at $3.4 billion (Reuters via CNA). "
         "a16z, Accel and Redpoint read below_1b from before that round; this mark is fresher.",
    rounds=[rnd("2025-11", "Seed", 115000000, "Eclipse", None, MR_A, "press"),
            rnd("2026-03", "Series A", 500000000, "Accel and Andreessen Horowitz", True, MR_A, "press"),
            rnd("2026-05", "unnamed round", 400000000, "Kleiner Perkins", True, MR_VAL, "press")]))
MINT = NEWS("mintlify", "Mintlify is building a next-gen")
L.append(cls("mintlify", status="private", rng="below_1b", usd=500000000, val_src="web_verified", asof="2026-04",
    val_cite=NEWS("mintlify", "Mintlify Raises $45M in Series B"), extra=V, country="US", city="San Francisco",
    focus="DevTools & APIs", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MINT, entry_date="2022",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=MINT,
    note="Developer documentation platform. The founders 'raised seed capital from Bain' and then 'an $18.5 million Series A funding "
         "round led by Andreessen Horowitz with participation from Bain and Y Combinator' (TechCrunch, 2024-09-05); BCV's listing: 2022, "
         "Seed (Kevin Zhang). Momentum check: the $45M Series B of April 2026 was at $500M (FinSMEs), so below_1b. City aligned with a16z "
         "and YC (San Francisco); the firm's listing says New York and TechCrunch placed it in Ithaca in 2022.",
    rounds=[rnd("2024-09", "Series A", 18500000, "Andreessen Horowitz", True, MINT, "press"),
            rnd("2026-04", "Series B", 45000000, None, None, NEWS("mintlify", "Mintlify Raises $45M in Series B"), "press")]))
L.append(cls("minuteclinic", rng="below_1b", city="Minneapolis", focus="Healthcare & Bio", stage="undetermined",
    note="Retail walk-in clinics run by nurse practitioners (Minneapolis). 'Bain Capital Ventures was the largest institutional investor "
         "in MinuteClinic' and 'MinuteClinic was acquired by CVS Corporation in September 2006' (the firm's own page, 2012 capture, "
         + CCPAGE("/portfolio/company/minuteclinic") + "). The round BCV entered is not named."))
MODAL = NEWS("modal", "Modal Raises $355M as AI Infrastructure")
L.append(cls("modal", status="private", rng="1b_plus", usd=4650000000, val_src="web_verified", asof="2026-05-22",
    val_cite=NEWS("modal", "Post-Money Valuation of $4.65 Billion"), extra=V, city="New York", city_src="web_verified",
    focus="Data Infrastructure", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=MODAL, entry_date="2026-05",
    note="Serverless AI inference and training cloud (Modal Labs, New York City-based). 'Accel, Menlo Ventures and Bain Capital Ventures "
         "also joined the round as new investors', the $355M Series C led by General Catalyst and Redpoint (Ventureburn); post-money "
         "$4.65 billion (FinSMEs, 2026-05-22). The siblings' $1.1B mark (September 2025) is older; this one is fresher.",
    rounds=[rnd("2026-05", "Series C", 355000000, "General Catalyst and Redpoint Ventures", True, MODAL, "press")]))
L.append(cls("momento", status="private", rng="below_1b", country="US", city="Seattle", focus="Data Infrastructure",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=POST("momento-data-retrieval"), entry_date="2022-11",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("momento", "lands $15M"),
    note="Serverless cache and data infrastructure (Seattle). 'Its $15 million seed, led by Bain Capital Ventures' (the firm's post, "
         "2022-11-02); then 'a $15 million Series A round led by Bain Capital Ventures' (GeekWire, 2024-07-18). Momentum check "
         "2026-09-27: no $1B+ round found. YC's 'Momento' (Mexico City, fintech) is a different company.",
    rounds=[rnd("2024-07", "Series A", 15000000, "Bain Capital Ventures", True, NEWS("momento", "lands $15M"), "press")]))
L.append(cls("mpower-auto-inc", status="unknown", rng="below_1b", country="US", focus="SaaS", stage="undetermined",
    flags=["city_unknown"],
    note="Hosted software for used-vehicle inventory management (mpowerauto.com), on the firm's 2006 listing only, 'Early', no partner "
         "or address. Google News finds nothing on the company, so its fate and its city are unknown."))
PAYTRIX = POST("why-we-invested-in-paytrix")
L.append(cls("navro", status="private", rng="below_1b", country="GB", country_src="web_verified", country_cite=PAYTRIX,
    city="London", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PAYTRIX, entry_date="2022",
    grad="graduated", grad_src="first_party", grad_conf="high", grad_cite=PAYTRIX,
    note="Cross-border payments for marketplaces (Paytrix, renamed Navro; London). 'Since we first invested in the London-based firm in "
         "its early 2022 seed round' and 'we co-led Paytrix's $18.3 million Series A' (the firm's post, 2023-04-03). A $14M raise "
         "(2024) and a $41M Series B (April 2025) followed. Momentum check 2026-09-27: no $1B+ round found.",
    rounds=[rnd("2023-03", "Series A", 18300000, "Bain Capital Ventures, Motive Partners and Unusual Ventures", True, PAYTRIX, "firm"),
            rnd("2025-04", "Series B", 41000000, None, None, NEWS("navro", "to expand outside of Europe"), "press")]))
L.append(cls("ndata", status="private", rng="below_1b", country="CZ", country_src="web_verified",
    country_cite="https://www.ndata.cz/en/contact", city="Prague", city_src="web_verified", focus="Healthcare & Bio",
    stage="undetermined", entry_date="2019",
    note="GxP pharmaceutical software (nData Solutions, s. r. o., Prague, its contact page; in business since 2005). BCV's listing: "
         "2019, Enrique Salem, no stage. The round is not named."))
NEB = NEWS("nebulock", "Threat hunting startup Nebulock closes")
L.append(cls("nebulock", status="private", rng="below_1b", country="US", city="Boston", city_src="web_verified", focus="Security",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEB, entry_date="2025-07",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("nebulock", "Nebulock raises $25M to expand"),
    note="Autonomous threat hunting (Boston). 'Bain Capital Ventures led the seed round', $8.5M (SiliconANGLE, 2025-07-29); 'FirstMark "
         "Capital led the Series A round', $25M, with BCV an existing backer (SiliconANGLE, 2026-06-25). Momentum check: no $1B+ round.",
    rounds=[rnd("2026-06", "Series A", 25000000, "FirstMark Capital", True, NEWS("nebulock", "Nebulock raises $25M to expand"),
                "press")]))
L.append(cls("nerati", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    flags=["identity_unresolved"],
    note="Listed on the firm's 2013 portfolio pages only (the software and venture categories, /portfolio/company/nerati, a logo and the "
         "name); no company page was captured, and Google News and a web search on the name find nothing, so the company cannot be "
         "described."))
L.append(cls("netfish", status="acquired", rng="below_1b", country="US", city="Santa Clara", focus="Data Infrastructure",
    stage="undetermined",
    note="XML business-to-business integration software (Netfish Technologies, Santa Clara), on the firm's 2003 listing. IONA "
         "Technologies bought it in 2001, so BCV's position dates from 1999-2000; the round is not named."))
L.append(cls("netlibrary", status="acquired", rng="below_1b", country="US", city="Boulder", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="E-book publishing for libraries (Boulder). OCLC bought its assets out of insolvency in 2002 (the firm's 2006 listing marks it "
         "acquired and gives OCLC's Dublin, OH address): an asset sale reads acquired. BCV's round is not named."))
L.append(cls("network-intelligence", status="acquired", rng="below_1b", country="US", city="Westwood", focus="Security",
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=CCPAGE("/portfolio/company/network-intelligence"),
    entry_date="2005",
    note="Security event and log management (Westwood, MA). 'Bain Capital Ventures led the company's Series C financing' and 'EMC "
         "acquiring the company 18 months after the Bain Capital Ventures investment'; EMC closed in September 2006 (the firm's own "
         "page, 2012 capture), so the entry is early 2005. A Series C entry reads Growth.",
    rounds=[rnd("2005", "Series C", None, "Bain Capital Ventures", True, CCPAGE("/portfolio/company/network-intelligence"), "firm")]))
L.append(cls("network-next", status="unknown", rng="below_1b", country="US", city="Santa Monica", city_src="web_verified",
    focus="Data Infrastructure", stage="undetermined",
    note="Network acceleration for online games (Glenn Fiedler), 'Santa Monica, California', Seed/Early Stage, on the firm's 2019 page ("
         + CCPAGE("/portfolio/network-next") + "). The Albany Business Journal covered Fiedler and the company in 2022; no source read "
         "gives its later fate. BCV's round is not named."))
L.append(cls("nomis-solutions", status="private", rng="below_1b", country="US", city="South San Francisco", city_src="web_verified",
    focus="Fintech & Payments", stage="undetermined",
    note="Pricing and profitability management for banks (San Bruno in the firm's 2006-2012 listings; 'SOUTH SAN FRANCISCO, Calif., Dec. "
         "5, 2023' in its release naming a new CEO, " + NEWS("nomis-solutions", "Appoints Greg Demas as Chief Executive Officer - PR")
         + "); Accenture took a minority stake in 2017. BCV held it by 2006 (Scott Friend); the round is not named."))
NORM = NEWS("norm-ai", "Norm Ai nabs $120M")
L.append(cls("norm-ai", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", asof="2026-07-07", val_cite=NORM,
    extra=V, country="US", city="New York", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("norm-ai-is-using-ai"), entry_date="2024-06",
    note="AI agents for regulatory compliance and legal work (New York). 'We invested in the $27 million Series A with Coatue, "
         "Blackstone, Citi, New York Life, TIAA' (the firm's post, 2024-06-25). Mark: the $120M Series C at $1.2B led by Khosla "
         "(SiliconANGLE, 2026-07-07), aligned with Coatue; Khosla's below_1b row is older.",
    rounds=[rnd("2024-06", "Series A", 27000000, None, True, POST("norm-ai-is-using-ai"), "firm"),
            rnd("2026-07", "Series C", 120000000, "Khosla Ventures", None, NORM, "press")]))
NF = "https://pulse2.com/northflank-developer-workload-platform-company-secures-22-3-million/"
L.append(cls("northflank", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite="https://builtinlondon.uk/articles/northflank-database-funding-22m-20241111", city="London", city_src="web_verified",
    focus="DevTools & APIs", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NF, entry_date="2024-11",
    note="Developer workload and deployment platform (headquartered in London, Built In London). '$22.3 million in new funding, including "
         "a $16 million Series A led by Bain Capital Ventures (BCV) and a $6.3 million seed led by Vertex' (Pulse 2.0, 2024-11-11). "
         "Momentum check 2026-09-27: no $1B+ round found.",
    rounds=[rnd("2024-11", "Seed", 6300000, "Vertex Ventures US", False, NF, "press"),
            rnd("2024-11", "Series A", 16000000, "Bain Capital Ventures", True, NF, "press")]))
L.append(cls("oasis-asset-management", status="acquired", rng="below_1b", country="AU", country_src="web_verified",
    country_cite=WB("oasis-asset-management"), city="North Sydney", focus="Fintech & Payments", stage="undetermined",
    note="Start-up providing administration services to independent financial advisers (Level 4, 60 Miller Street, North Sydney, in the "
         "firm's 2006 listing, which marks it acquired). No partner, round or acquirer on any surface read."))
L.append(cls("obvio", status="private", rng="below_1b", country="US", city="San Carlos", city_src="web_verified",
    focus="AI & Applied AI", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("obvio", "Obvio: $22 Million Secured"), entry_date="2025-06",
    note="AI stop-sign and traffic-safety cameras (a San Carlos, California-based startup, TechCrunch). '$22 million in Series A funding "
         "led by Bain Capital Ventures' (Pulse 2.0, 2025-06-11; Ajay Agarwal). Momentum check 2026-09-27: no later round found.",
    rounds=[rnd("2025-06", "Series A", 22000000, "Bain Capital Ventures", True, NEWS("obvio", "Obvio: $22 Million Secured"), "press")]))
L.append(cls("onbe", status="acquired", rng="below_1b", country="US", city="Chicago", focus="Fintech & Payments", stage="undetermined",
    note="Onbe is the 2021 rebrand of daVinci Payments (formerly Swift Prepaid Solutions, bought by BCV-backed Syncapay) after its merger "
         "with North Lane Technologies, which came 'from a majority equity investment by Centerbridge Partners' (Technical.ly, "
         + NEWS("onbe", "Conshy payment company") + "): a change of control, so acquired. The row folds into 'davinci-payments' "
         "(identity-merges.json) and is aligned with it. BCV's round is not named."))
ORA = NEWS("oratomic", "Oratomic raises $300M to build a viable")
L.append(cls("oratomic", status="private", rng="below_1b", city="Pasadena", city_src="web_verified", focus="Industrial & Robotics",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=ORA, entry_date="2026-07",
    note="Fault-tolerant neutral-atom quantum computers (a Pasadena-based Caltech spinout, Pulse 2.0). The $300M Series A 'was co-led by "
         "ARCH Venture Partners, Spark Capital, and Khosla Ventures, with participation from ... Bain Capital' (TechCrunch, "
         "2026-07-10); the firm's own listing (2026, Rak Garg, Slater Stich) ties the position to BCV (decisions.md D7). Pulse 2.0's "
         "'estimated valuation around $1.5 billion' is not a disclosed figure, so no band (Rule A); aligned with Khosla's below_1b. "
         "Khosla's row gives San Francisco; the round's coverage places the company in Pasadena.",
    rounds=[rnd("2026-07", "Series A", 300000000, "ARCH Venture Partners, Spark Capital and Khosla Ventures", True, ORA, "press")]))

if __name__ == "__main__":
    jl.write("batch-009", L)
