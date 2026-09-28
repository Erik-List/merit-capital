"""PRO-76 grind, batch-001 part B (first pass). Same evidence and rules as
judgments-1.py; every citation was fetched and its 20VC sentence read
(scratch/research/url-checks.json) or read in the browser pane (Medium, EU-Startups)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
L = []
W = "web_verified"
U = "undetermined"

L.append(cls("papaya", status="private", country="GB", city="London", focus="Climate & Energy", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2022-09",
    note="Software to source and run electric and light-electric delivery fleets (Papaya, London; papayadash.com). Its first institutional money, 'the company's new $3.5 million investment ushered in a host of backers including Giant Ventures, Seedcamp, 20VC, FJ Labs, Flexport' (TechCrunch, 2022-09-27), seven months after the soft launch: a seed-sized first round the article does not name, so the stage is model-read (medium). 20VC's own page for Papaya dates from 2022-08. A different company from Sequoia's Papaya (Los Angeles bill pay): ruled distinct.",
    flags=["identity_homonym"],
    rounds=[rnd("2022-09", "seed (unnamed first round)", 3500000, None, True, "https://techcrunch.com/2022/09/27/papaya-wants-to-help-electrify-last-mile-logistics-in-europe/")]))

L.append(cls("asklio", status="private", country="US", city="New York", focus="AI & Applied AI", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2026-03",
    stage_cite="https://pulse2.com/lio-30-million-raised-for-agentic-ai-enterprise-procurement-platform/",
    note="Agentic AI for enterprise procurement (Lio, formerly askLio; founded in Munich 2023, headquartered at 524 Broadway, New York per its own site). The $30M Series A of March 2026 'was led by Andreessen Horowitz (a16z) with participation from SV Angels, Harry Stebbings, and Y Combinator' (Pulse 2.0, 2026-03-05); the firm added Lio to its list the same month (decisions.md R1: the line dates the entry of a company the firm lists).",
    rounds=[rnd("2026-03", "Series A", 30000000, "Andreessen Horowitz", True, "https://www.prnewswire.com/news-releases/lio-raises-30m-series-a-to-bring-agentic-ai-to-enterprise-procurement-302705236.html", "company")]))

L.append(cls("athenian", status="acquired", country="ES", city="Madrid", focus="DevTools & APIs", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-03",
    stage_cite="https://techcrunch.com/2022/03/02/athenian-gives-you-metrics-about-your-engineering-team-without-focusing-on-individuals/",
    note="Engineering-metrics platform founded by Eiso Kant (later a co-founder of Poolside). $6M seed led by Point Nine: 'Frst, Xavier Niel, 20VC, Abstraction Capital and Air Street Capital also participated in the round' (TechCrunch, 2022-03-02). Acquired by the Linux Foundation (Point Nine's card; the Point Nine row agrees). 20VC's 2026 card reads 'Athenian (now Poolside)': Poolside is judged as its own row. Country and city from the company's Madrid registration (low confidence).",
    extra={"hq_country_confidence": "low", "hq_city_confidence": "low"},
    rounds=[rnd("2022-03", "seed", 6000000, "Point Nine", True, "https://techcrunch.com/2022/03/02/athenian-gives-you-metrics-about-your-engineering-team-without-focusing-on-individuals/")]))

L.append(cls("bereal", status="acquired", country="FR", city="Paris", focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="Photo-sharing social app (Paris). In 20VC's portfolio per its own pages of 2022-2023 and Business Insider ('20VC's portfolio includes companies like Hopin ...; Sorare ...; and BeReal', 2024-06-13), but no source names 20VC in a round (the $30M Series A of June 2021 co-led by a16z and Accel; the $60M Series B of 2022 led by DST): round undetermined. acq. by Voodoo, 2024 (EUR 500M), as the a16z, Accel and Coatue rows read.",
    rounds=[rnd("2021-06", "Series A", 30000000, "Andreessen Horowitz, Accel", None, None),
            rnd("2022", "Series B", 60000000, "DST Global", None, "https://techcrunch.com/2022/10/20/sources-bereal-raised-60m-in-its-series-b-earlier-this-year-now-has-20m-daus/")]))

L.append(cls("bottlecap", status="private", country="CZ", city="Prague", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2026-01", flags=["stage_uncited"],
    note="Efficient large language models (BottleCap AI, Prague; founders Tomas Mikolov, Jaroslav Beck, David Herel). A $7.5M seed led by 20VC, January 2026 (reported by Dealroom's news feed and the founders' posts; no fetchable press page was found, so the stage is model-read at medium pending a citation); Julien Codorniou names it an investment ('20VC (investor)', TechCrunch, 2026-05-02).",
    rounds=[rnd("2026-01", "seed", 7500000, "20VC", True, None)]))

L.append(cls("bridgelinx", status="private", country="PK", city="Lahore", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2021-09",
    stage_cite="https://techcrunch.com/2021/09/13/digital-freight-marketplace-bridgelinx-raises-10-million-in-pakistans-largest-seed-funding/",
    note="Digital freight marketplace (Lahore). 'Harry Stebbings' 20 VC, Josh Buckley's Buckley Ventures and Indus Valley Capital co-led the startup's financing round' (TechCrunch, 2021-09-13), $10M, 'Pakistan's largest seed funding'.",
    rounds=[rnd("2021-09", "seed", 10000000, "20VC, Buckley Ventures, Indus Valley Capital", True, "https://techcrunch.com/2021/09/13/digital-freight-marketplace-bridgelinx-raises-10-million-in-pakistans-largest-seed-funding/")]))

L.append(cls("buena", status="private", country="DE", city="Berlin", focus="SaaS", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="AI-run property management, buying and digitising property managers (Berlin). 20VC participated in the Series A led by GV (July 2025; 'a Series A funding round led by GV, with participation from 20VC, Stride, and Capnamic', Tech.eu, 2025-07-23), but the firm listed Buena from September 2024, so its entry was an earlier round no source names: undetermined.",
    rounds=[rnd("2025-07", "Series A", 26500000, "GV", True, "https://tech.eu/2025/07/23/gv-and-20vc-back-buenas-vision-to-reinvent-property-management-through-ai-powered-rollups-with-58m-investment/")]))

L.append(cls("cadensys", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage=U, flags=["stage_uncited"],
    note="Human-AI collaboration tool ('Made in London', its own site). The firm added it in March 2026; vendor profiles list 20VC, Accel and angels from Revolut and Trade Republic over about $5M, but no press names a round: undetermined."))

L.append(cls("cognition", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="10b_plus", usd=48000000000, val_src=W,
    asof="2026-09-08", val_cite="https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/",
    stage="Growth", stage_src="model", stage_conf="medium", flags=["cite_pending"],
    note="AI software engineer Devin (Cognition AI, San Francisco). The firm added Cognition in March 2026; no source names 20VC's round, and every Cognition round since 20VC could have entered is a growth round at $2B or more (the S-series vehicles of 2025-2026 are the likely channel), so Growth (cite_pending). Mark: the Series E at $48B (TechCrunch, 2026-09-08), the Bain Capital Ventures row's; the 8VC, General Catalyst, Khosla and Lux rows carry the older $10.2B, same band.",
    rounds=[rnd("2025-09", "growth", 400000000, "Founders Fund", None, None),
            rnd("2026-09", "Series E", 2000000000, None, None, "https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/")]))

L.append(cls("comstruct", status="private", country="DE", city="Munich", focus="SaaS", rng="below_1b",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2025-02",
    note="Procurement platform for construction materials (Munich). 'the startup is announcing a EUR 12.5 million round ($13 million ...) led by GV and 20VC, with existing investors Booom and Puzzle Ventures investing once again' (TechCrunch, 2025-02-06; PropTech Connect names Paul Bonnet); the first round after the seed from Booom and Puzzle, so Series A (the article names no series: model, medium).",
    rounds=[rnd("2025-02", "Series A", 13000000, "GV, 20VC", True, "https://techcrunch.com/2025/02/06/comstruct-a-platform-to-digitize-the-construction-industry-raises-135-million/")]))

L.append(cls("context", status="acquired", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage=U, flags=["stage_uncited", "identity_homonym"],
    note="LLM product analytics (Context.ai, London; founders Henry Scott-Green and Alex Gamble). Its $3.5M seed of August 2023 was led by GV and Theory Ventures (Business Wire) with no 20VC named; the firm's 2026 card flags the exit. acq. by OpenAI, April 2025 (the team joined OpenAI and the product was wound down). A different company from YC's Context (San Francisco): ruled distinct.",
    rounds=[rnd("2023-08", "seed", 3500000, "GV, Theory Ventures", None, None)]))

L.append(cls("datalane", status="private", country="US", city=None, focus="Data Infrastructure", rng="below_1b",
    stage=U, flags=["stage_uncited", "city_unknown"],
    note="Identity graph for local businesses (DataLane). The $22.5M Series A of December 2025 was led by Amplify Partners 'with participation from Harry Stebbings, founder of 20VC' (citybiz, 2025-12-16), and 'DataLane has raised $27 million to date from Amplify Partners, Harry Stebbings, founder of 20VC, Mischief, Basis Set' (same): the founder is named in the seed and the Series A alike, so the fund's entry round is undetermined (decisions.md R1).",
    rounds=[rnd("2025", "seed", 4500000, None, None, None),
            rnd("2025-12", "Series A", 22500000, "Amplify Partners", True, "https://www.citybiz.co/article/784668/datalane-raises-22-5m-series-a-led-by-amplify-partners/")]))

L.append(cls("dataware", status="private", country="GB", city=None, focus="Data Infrastructure", rng="below_1b",
    stage=U, flags=["stage_uncited", "city_unknown"],
    extra={"hq_country_confidence": "low"},
    note="In-memory data layer for AI-era applications (dataware.dev). The firm added it in March 2026; vendor profiles list 20VC, Felicis, SV Angel and Project Europe over about $7.75M, with no dated round: undetermined. 20VC's own position is distinct from Project Europe's (decisions.md D5). Country low confidence; city not found."))

L.append(cls("deblock", status="private", country="FR", city="Paris", focus="Crypto & Web3", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022",
    stage_cite="https://sifted.eu/articles/20vc-deblock-raise-news",
    extra={"hq_city_confidence": "low"},
    note="Crypto wallet merged with a current account (Deblock, founded August 2022 by Revolut and Ledger alumni). 20VC has backed it from the start: its Kieran Hill was a director of Deblock Ltd from 2022-10-04 to 2025-11-10 (Companies House), the first seed closing at the end of 2022; Sifted's '20VC-backed crypto wallet Deblock raises GBP 13.3m' (2024-11-21) names 20VC among the lead investors of the second seed ('Headline, Hoxton, 20VC and Chalfen were lead investors in the round'). Both rounds are seeds, so the entry stage is Seed, dated 2022. $35M Series A led by Speedinvest, CommerzVentures and Latitude (November 2025, DL News). City low confidence.",
    rounds=[rnd("2022", "seed", 12000000, None, True, "https://find-and-update.company-information.service.gov.uk/officers/vBMg9N819DZ57iGwX_aTvwXuNeg/appointments", "filing"),
            rnd("2024-11", "seed (second)", 17500000, "Headline, Hoxton, 20VC, Chalfen", True, "https://sifted.eu/articles/20vc-deblock-raise-news"),
            rnd("2025-11", "Series A", 35000000, "Speedinvest, CommerzVentures, Latitude", True, "https://www.dlnews.com/articles/deals/revolut-alumni-raise-funds-to-fuel-expansion-of-crypto-neobank-deblock/")]))

L.append(cls("delos", status="private", country="FR", city="Paris", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2025-04",
    note="AI employees for business operations (Delos, French). 'French startup Delos landed $2.5 million in a round led by 20VC, with participation from Kima Ventures and Inovia' (Business Insider, 2025-04-24): its first round, seed-sized, not named by the article (model, medium). EUR 10M followed in September 2026 (Dealroom news).",
    rounds=[rnd("2025-04", "seed (unnamed)", 2500000, "20VC", True, "https://www.businessinsider.com/pitch-decks-ai-startups-qevlar-honeyhive-solve-intelligence-delos-vcs-2025-4"),
            rnd("2026-09", "funding round", 11700000, None, None, None)]))

L.append(cls("district", status="private", country="US", city=None, focus="Consumer & Marketplaces", rng="below_1b",
    stage=U, flags=["stage_uncited", "city_unknown"],
    note="AI commerce platform for independent sellers (District, formerly ISO; founded by Snap alumni). Its $14.7M seed announced May 2026 was led by Andreessen Horowitz and Kindred Ventures with 20VC participating (Business Wire, 2026-05-06), but 20VC listed District from September 2024, so the firm's money went in before that announcement: undetermined. Same company as the a16z row.",
    rounds=[rnd("2026-05", "seed", 14700000, "Andreessen Horowitz, Kindred Ventures", True, "https://www.businesswire.com/news/home/20260506903958/en/District-Raises-$14.7M-in-Seed-Funding-to-Unlock-the-Next-Generation-of-Online-Commerce")]))

if __name__ == "__main__":
    jl.write("batch-001b", L)
