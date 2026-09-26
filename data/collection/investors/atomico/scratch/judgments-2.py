"""PRO-79 grind, batch-002 (hinge-health .. qatalog)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
INS = "https://atomico.com/insights/"

L = []
L.append(cls("hinge-health", status="public", rng="1b_plus", usd=7410000000, val_src="web_verified", asof="2026-09",
             val_cite="https://companiesmarketcap.com/hinge-health/marketcap/", val_conf="high",
             city="San Francisco",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-hinge-health-how-digital-care-for-common-injuries-is-transforming-outcomes",
             note="Digital MSK care; the firm's own post (Jul 2017): 'delighted to be leading in Hinge Health's $8m Series A funding round'; NYSE: HNGE since the May 2025 IPO (Atomico filers on the IPO-time Forms 3 and 4, EDGAR); market cap ~$7.41B Sep 2026 (companiesmarketcap)",
             rounds=[rnd("2017-07-24", "Series A", 8000000, "Atomico", True, INS + "our-investment-in-hinge-health-how-digital-care-for-common-injuries-is-transforming-outcomes", "firm")]))
L.append(cls("iboxchain", status="private", rng="below_1b", country="CN", city="Shenzhen", focus="Fintech & Payments",
             stage="undetermined",
             note="Chinese mobile card-reader and payments company (iBoxPay, now iBoxChain); Atomico entered in 2011-2012 (the 2012 listing; CMS year 2011) but no surface names the round; the site lists it Current"))
L.append(cls("ima", status="acquired", rng="below_1b", country="NL", city="Amsterdam", focus="Media, Gaming & Advertising",
             stage="undetermined",
             note="Fashiolista, the Amsterdam fashion-inspiration community Atomico II backed in 2010-2011, renamed its company IMA (Influencer Marketing Agency) in 2015 when the platform closed; the firm's CMS page 'IMA' links fashiolista.com; IMA later merged into MediaMonks (S4 Capital) -> acquired; the round is unnamed on every surface; the fashiolista row merges into this one at the rebuild (identity-merges.json)"))
L.append(cls("infarm", status="acquired", rng="below_1b", country="DE", city="Berlin", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://agfundernews.com/infarm-joins-vertical-farming-pantheon-with-titanic-100m-series-b",
             note="Urban vertical farming; Atomico led the $100M Series B Jun 2019 (AgFunderNews; the firm's own post, Partner Hiro Tamura joining the board); insolvent 2023-2024, assets and IP sold to the successor InFarm Technologies -> acquired, aligned with Cherry's row",
             rounds=[rnd("2019-06-11", "Series B", 100000000, "Atomico", True, "https://agfundernews.com/infarm-joins-vertical-farming-pantheon-with-titanic-100m-series-b")]))
L.append(cls("jawbone", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Wearables / audio (Aliph, renamed Jawbone 2011); held by Atomico Ventures I (the 2008 and 2010 fund-I listings); the fund-I round is unnamed on every surface; liquidated 2017 (defunct)"))
L.append(cls("jobandtalent", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", asof="2025-04-10",
             val_cite="https://techcrunch.com/2025/04/10/jobandtalent-raises-103m-on-a-down-round-1-5b-valuation-as-it-looks-to-ai-to-recruit-temps/",
             val_conf="medium", city="Madrid", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-jobandtalent-a-world-class-team-revolutionising-the-sme-jobs-market-with-leading-matching-technology-and-an-innovative-transaction-based-mobile-platform",
             note="Temp-staffing marketplace; the firm's own post (Jun 2016): 'we have just led a $42m Series B round for Jobandtalent' (Wass and de Vries directors of the UK holding from May 2016, register); $500M Series E 2021; $103M down round at $1.5B Apr 2025 (TechCrunch) is the last priced mark",
             rounds=[rnd("2016-06-13", "Series B", 42000000, "Atomico", True, INS + "our-investment-in-jobandtalent-a-world-class-team-revolutionising-the-sme-jobs-market-with-leading-matching-technology-and-an-innovative-transaction-based-mobile-platform", "firm"),
                     rnd("2021-12-01", "Series E", 500000000, None, None, "https://www.prnewswire.com/news-releases/jobandtalent-secures-500m-in-series-e-fundraising-round-to-accelerate-expansion-301434496.html"),
                     rnd("2025-04-10", "down round", 103000000, None, None, "https://techcrunch.com/2025/04/10/jobandtalent-raises-103m-on-a-down-round-1-5b-valuation-as-it-looks-to-ai-to-recruit-temps/")]))
L.append(cls("katana", status="private", rng="below_1b", country="EE", city="Tallinn", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2021/02/23/katana-series-a/",
             note="Manufacturing ERP for SMBs; $11M Series A led by Atomico Feb 2021 (Tech.eu; the firm's own post the same day, Ben Blume joining the board); $35M Series B Oct 2022 (Business Wire)",
             rounds=[rnd("2021-02-23", "Series A", 11000000, "Atomico", True, "https://tech.eu/2021/02/23/katana-series-a/"),
                     rnd("2022-10-12", "Series B", 35000000, None, None, "https://www.businesswire.com/news/home/20221012005045/en/Katana-Closes-%2435M-Series-B-to-Scale-an-Industry-Leading-Manufacturing-Ecosystem-for-SMBs")]))
L.append(cls("kheiron-medical", status="acquired", rng="below_1b", country="GB", city="London", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2019/09/23/kheirons-22-million-series-a-funds-early-breast-cancer-detection-for-women-worldwide/",
             note="AI breast-cancer screening (Mia); $22M Series A led by Atomico Sep 2019 (Tech.eu; the firm's own post, Haivas on the board 2019-2024); the register's May 2019 statement lists no Atomico holder and the May 2020 one lists Atomico V SCSp with PREFERRED A shares, so the A is the entry; acquired by DeepHealth (RadNet) 2024, the UK company renamed DeepHealth UK Ltd (register)",
             rounds=[rnd("2019-09-23", "Series A", 22000000, "Atomico", True, "https://tech.eu/2019/09/23/kheirons-22-million-series-a-funds-early-breast-cancer-detection-for-women-worldwide/")]))
L.append(cls("klarna", status="public", rng="1b_plus", usd=7520000000, val_src="web_verified", asof="2026-08",
             val_cite="https://stockanalysis.com/stocks/klar/market-cap/", val_conf="medium", city="Stockholm",
             focus="Fintech & Payments", flags=["cite_pending"],
             note="Buy-now-pay-later; the firm's own post (Dec 2013): 'In 2012 we invested in the outstanding team at Klarna' (round unnamed; the site labels it Growth, pending the label score); NYSE: KLAR since Sep 2025, cap ~$7.5B Aug 2026 as Sequoia's row records"))
L.append(cls("knewton", status="acquired", rng="below_1b", city="New York", focus="SaaS",
             note="Adaptive learning; 'Knewton raised $51 million in a recent round of funding led by new investors GSV and Atomico' (GSV Capital 8-K, Jan 2014; 'since we invested last December', the firm's 2014 post) - the Form D band's Growth stands; acquired by Wiley 2019"))
L.append(cls("koru-kids", status="private", rng="below_1b", city="London", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techround.co.uk/news/koru-kids-raises-10m-series-a/",
             note="Nanny/childcare platform; the GBP 10M Series A of Aug 2019 (TechRound; $12.2M at the ECB rate of 2019-08-30), announced with the firm's own post the same week; Wass director 2019-2024 (register)",
             rounds=[rnd("2019-08-30", "Series A", 12185723, "Atomico", True, "https://techround.co.uk/news/koru-kids-raises-10m-series-a/")]))
L.append(cls("labgenius", status="private", rng="below_1b", country="GB", city="London", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2020/10/29/labgenius-series-a/",
             note="ML-driven antibody discovery; Atomico led the $15M Series A extension of Oct 2020, bringing the Series A to $25M (Tech.eu; the firm's own post; Haivas director 2020-2025, register)",
             rounds=[rnd("2020-10-29", "Series A extension", 15000000, "Atomico", True, "https://tech.eu/2020/10/29/labgenius-series-a/")]))
L.append(cls("lace-lithography", status="private", rng="below_1b", country="NO", city="Bergen", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://arcticstartup.com/lace-lithography-raises-40m-series-a/",
             note="Atom-beam chip lithography (Norway); the firm's page dates to Mar 2026, the $40M Series A (ArcticStartup) - Atomico's first round",
             rounds=[rnd("2026-03-24", "Series A", 40000000, None, True, "https://arcticstartup.com/lace-lithography-raises-40m-series-a/")]))
L.append(cls("lakera", status="acquired", rng="below_1b", country="CH", city="Zurich", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-lakera-securing-genai-applications-in-real-time",
             note="GenAI security; the firm's own post (Jul 2024): 'With this $20M Series A round' as the firm's newest partnership; acquired by Check Point, completed 2025 (MarketScreener)",
             rounds=[rnd("2024-07-24", "Series A", 20000000, "Atomico", True, INS + "our-investment-in-lakera-securing-genai-applications-in-real-time", "firm")]))
L.append(cls("last-fm", status="acquired", rng="below_1b", country="GB", city="London", focus="Media, Gaming & Advertising",
             stage="undetermined",
             note="Music scrobbling service; on the 2008 listing and under Atomico Ventures I in 2010 (CMS year 2006); the 2006 round is unnamed on every surface on disk; acquired by CBS 2007"))
L.append(cls("lendinvest", status="public", rng="below_1b", city="London", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-lendinvest-disrupting-property-finance-through-marketplace-lending",
             note="Property lending platform; the firm's own post (Mar 2016): 'we've completed a GBP 17 million Series B equity investment in LendInvest' ($24.4M at the ECB rate of 2016-03-14; Ljungman director 2016-2019, register); LSE AIM listing Jul 2021, small cap",
             rounds=[rnd("2016-03-14", "Series B", 24412745, None, True, INS + "our-investment-in-lendinvest-disrupting-property-finance-through-marketplace-lending", "firm")]))
L.append(cls("light", status="private", rng="below_1b", country="DK", city="Copenhagen", focus="Fintech & Payments",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-light-the-first-ai-powered-general-ledger-for-global-company-finances",
             entry_date="2024-06-12", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite="https://www.eu-startups.com/2025/09/light-raises-e25-million-to-replace-legacy-finance-systems-with-ai-native-platform/",
             flags=["model_disputes_source"],
             note="AI general ledger (Copenhagen); the firm's own post (Jun 2024): 'our newest $13M Seed partnership with Light'; the EUR 25M Series A of Sep 2025 (EU-Startups) = graduation; Wikidata's Japan match was a homonym (disputed)",
             rounds=[rnd("2024-06-12", "Seed", 13000000, "Atomico", True, INS + "our-investment-in-light-the-first-ai-powered-general-ledger-for-global-company-finances", "firm"),
                     rnd("2025-09-25", "Series A", None, None, None, "https://www.eu-startups.com/2025/09/light-raises-e25-million-to-replace-legacy-finance-systems-with-ai-native-platform/")]))
L.append(cls("lilium", status="defunct", rng="below_1b", city="Wessling", focus="Industrial & Robotics",
             stage="undetermined",
             note="Electric VTOL jet; the firm's Dec 2016 post: 'we made an initial investment to help with their prototype development, ahead of our Series A round' - the entry predates the Series A Atomico led, and that first round is unnamed on every surface -> undetermined (the ankar reading; the 2021 post's 'when we first invested at Series A' is the looser later wording); de-SPAC 2021, insolvent 2024-2025, the tech continued at Archer (TechCrunch: 'defunct') -> defunct",
             rounds=[rnd("2016", "unnamed initial investment", None, "Atomico", True, INS + "the-future-of-sustainable-transportation-why-we-invested-in-lilium-aviation", "firm"),
                     rnd("2016-12-05", "Series A", None, "Atomico", True, INS + "the-future-of-sustainable-transportation-why-we-invested-in-lilium-aviation", "firm")]))
L.append(cls("lime", status="public", rng="1b_plus", usd=1600000000, val_src="web_verified", asof="2026-07-02",
             val_cite="https://mlq.ai/news/lime-raises-174-million-in-nasdaq-ipo-at-16-billion-valuation/",
             val_conf="medium", city="San Francisco", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://venturebeat.com/transportation/lime-raises-335-million-including-from-uber-whose-app-will-now-offer-scooters",
             flags=["cite_pending"],
             note="Micromobility; Atomico joined the $335M round of Jul 2018 led by GV with Uber (VentureBeat: 'The round also includes money from Alphabet's GV, IVP, Atomico, and Fidelity'; the firm's own post the same day); the round is unnamed but follows Lime's 2017 lettered rounds and precedes the Feb 2019 Series D -> Growth; Nasdaq IPO Jul 2026 at ~$1.6B (MLQ); a cited market cap is owed in the A/B pass",
             rounds=[rnd("2018-07-09", "unnamed", 335000000, "GV", True, "https://venturebeat.com/transportation/lime-raises-335-million-including-from-uber-whose-app-will-now-offer-scooters")]))
L.append(cls("mapillary", rng="below_1b", city="Malmö", focus="AI & Applied AI",
             stage="Series A", stage_src="model", stage_conf="medium",
             note="Crowdsourced street-level imagery; the firm's own post (Mar 2016): 'leading Mapillary's latest investment round, worth $8 million, alongside prominent investors Sequoia Capital, LDV Capital and Playfair'; the next round was the $15M Series B of Apr 2018 led by BMW i Ventures (Geospatial World), so the 2016 round was the Series A; acquired by Facebook Jun 2020",
             rounds=[rnd("2016-03-03", "unnamed", 8000000, "Atomico", True, INS + "our-investment-in-mapillary-transforming-photo-mapping-through-crowdsourcing", "firm"),
                     rnd("2018-04-12", "Series B", 15000000, "BMW i Ventures", None, "https://geospatialworld.net/news/mapillary-secures-15-million-series-b-led-by-bmw-i-ventures-to-accelerate-global-map-data-collection/")]))
L.append(cls("masterclass", city="San Francisco",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-masterclass-lifelong-learning-from-the-best-in-the-world",
             note="Online classes by experts; the firm's own post (Sep 2018): 'invited to participate in this $80m Series D round'; valuation pinned in the A/B pass",
             rounds=[rnd("2018-09-07", "Series D", 80000000, None, True, INS + "our-investment-in-masterclass-lifelong-learning-from-the-best-in-the-world", "firm")]))
L.append(cls("mews", rng="1b_plus", usd=2367200000, val_src="web_verified", asof="2026-01-26",
             val_cite="https://nltimes.nl/2026/01/26/dutch-unicorn-tech-firm-mews-gets-eu2-billion-valuation-new-funding-round",
             val_conf="high", country="NL", city="Amsterdam",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.wsgr.com/en/insights/wilson-sonsini-advises-mews-on-dollar300-million-series-d-funding.html",
             flags=["model_disputes_source"],
             note="Hospitality operations/payments platform (Czech-founded, Amsterdam HQ); the firm's page appears Jan 2026, the week of the $300M Series D (Wilson Sonsini) at a EUR 2B valuation (NL Times; $2.37B at the ECB rate of 2026-01-26) - Atomico's first round; Wikidata's Ireland match disputed",
             rounds=[rnd("2026-01-22", "Series D", 300000000, None, True, "https://www.wsgr.com/en/insights/wilson-sonsini-advises-mews-on-dollar300-million-series-d-funding.html")]))
L.append(cls("mondoo", status="private", rng="below_1b", country="DE", city="Berlin", focus="Security",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2021/10/05/bringing-devops-and-security-teams-together-mondoo-raises-12-million-in-atomico-led-round/",
             note="Infrastructure security for DevOps; $12M Series A led by Atomico Oct 2021 (Tech.eu; the firm's own post the same day); $17.5M raise Sep 2025 (Business Wire)",
             rounds=[rnd("2021-10-05", "Series A", 12000000, "Atomico", True, "https://tech.eu/2021/10/05/bringing-devops-and-security-teams-together-mondoo-raises-12-million-in-atomico-led-round/"),
                     rnd("2025-09-30", "unnamed", 17500000, None, None, "https://www.businesswire.com/news/home/20250930352438/en/Mondoo-Raises-%2417.5-Million-to-Pioneer-Agentic-Vulnerability-Management")]))
L.append(cls("neko-health", status="private", rng="1b_plus", usd=7000000000, val_src="web_verified", asof="2026-07-15",
             val_cite="https://mlq.ai/news/neko-health-raises-700m-series-c-at-nearly-7b-valuation-for-us-expansion/",
             val_conf="medium", country="SE", city="Stockholm", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://arcticstartup.com/neko-health-raises-60m-series-a/",
             note="AI full-body health scans (Daniel Ek, Hjalmar Nilsonne); the firm's partnership post (Jul 2023) coincides with the EUR 60M Series A ($65.3M at the ECB rate of 2023-07-05; ArcticStartup); $700M Series C Jul 2026 at nearly $7B (MLQ; TechCrunch)",
             rounds=[rnd("2023-07-05", "Series A", 65274000, None, True, "https://arcticstartup.com/neko-health-raises-60m-series-a/"),
                     rnd("2026-07-15", "Series C", 700000000, None, None, "https://techcrunch.com/2026/07/15/daniel-eks-body-scanning-startup-neko-health-raises-another-700m/")]))
L.append(cls("nftport", status="unknown", rng="below_1b", country="EE", city="Tallinn", focus="Crypto & Web3",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-nftport-building-the-infrastructure-for-digital-ownership",
             note="NFT developer infrastructure (Tallinn); the firm's own post (Jun 2022): 'NFTPort's $26 million Series A funding round, which we have co-led with Taavet + Sten' (Sifted); no news since the 2022 NFT downturn - status unknown",
             rounds=[rnd("2022-06-15", "Series A", 26000000, "Atomico; Taavet+Sten", True, INS + "our-investment-in-nftport-building-the-infrastructure-for-digital-ownership", "firm")]))
L.append(cls("nourish", status="private", rng="1b_plus", usd=1750000000, val_src="web_verified", asof="2026-05-19",
             val_cite="https://www.tradingview.com/news/reuters.com,2026:newsml_L4N41W0X1:0-nutrition-counseling-startup-nourish-raises-100-million-at-1-75-billion-valuation-bloomberg-news/",
             val_conf="medium", country="US", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-nourish-the-leading-nutrition-care-platform-tackling-chronic-disease",
             note="Insurance-covered virtual nutrition care; the firm's own post (Apr 2025): 'Atomico is delighted to be investing in Nourish's $70m Series B round'; $100M raise at $1.75B May 2026 (Reuters/Bloomberg via TradingView)",
             rounds=[rnd("2025-04-23", "Series B", 70000000, None, True, INS + "our-investment-in-nourish-the-leading-nutrition-care-platform-tackling-chronic-disease", "firm"),
                     rnd("2026-05-19", "unnamed", 100000000, None, None, "https://www.tradingview.com/news/reuters.com,2026:newsml_L4N41W0X1:0-nutrition-counseling-startup-nourish-raises-100-million-at-1-75-billion-valuation-bloomberg-news/")]))
L.append(cls("oden-technologies", status="private", rng="below_1b", country="US", city="New York", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-oden-technologies-driving-the-digital-transformation-of-manufacturing",
             note="Industrial analytics for manufacturing (New York; UK entity Oden Technologies Ltd with Zennstrom 2018-2022 then Blume 2022-2024 as directors, register); the firm's own post (Jul 2018): 'so proud to announce our Series A investment'",
             rounds=[rnd("2018-07-02", "Series A", None, None, True, INS + "our-investment-in-oden-technologies-driving-the-digital-transformation-of-manufacturing", "firm")]))
L.append(cls("oh-bibi", status="private", rng="below_1b", country="FR", city="Paris", focus="Media, Gaming & Advertising",
             stage="undetermined",
             note="Mobile games studio; Atomico led the $21M round of Jun 2018 (GamesBeat; TechCrunch; the firm's own post) - the round is unnamed in every source",
             rounds=[rnd("2018-06-27", "unnamed", 21000000, "Atomico", True, "https://gamesbeat.com/atomico-leads-21-million-investment-in-oh-bibi-for-mobile-versions-of-popular-pc-and-console-games/")]))
L.append(cls("omio", status="private", rng="below_1b", city="Berlin", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-goeuro-transforming-the-way-we-travel-in-europe",
             note="Multimodal travel booking (GoEuro, renamed Omio 2019); the firm's own post (Dec 2015): 'participating in GoEuro's $45m Series B round' (led by Goldman Sachs, Skift); joined the $70M 2016 round with Silver Lake and KPCB; no citable priced mark at $1B+ (vendor estimates only, Rule A)",
             rounds=[rnd("2015-12-09", "Series B", 45000000, "Goldman Sachs", True, "https://skift.com/2015/12/08/goeuro-gets-45-million-in-funding-round-led-by-goldman-sachs/"),
                     rnd("2016-10-04", "unnamed", 70000000, None, True, INS + "new-investment-in-goeuro-to-accelerate-their-success", "firm")]))
L.append(cls("onetwotrip", status="private", rng="below_1b", country="RU", city="Moscow", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Russian online travel agency; the firm's own post (Oct 2012): 'Atomico is pleased to announce our $16 million investment in OneTwoTrip' (round unnamed); raised $3M 2017 (PhocusWire); the site lists it Current",
             rounds=[rnd("2012-10-24", "unnamed", 16000000, "Atomico", True, INS + "atomico-invests-dollar16m-in-onetwotrip", "firm")]))
L.append(cls("onna", status="acquired", rng="below_1b", city="New York",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.prnewswire.com/news-releases/onna-raises-27m-series-b-to-scale-worlds-first-knowledge-integration-platform-kip-301078333.html",
             flags=["stage_disputes_band"],
             note="Knowledge-integration / eDiscovery data platform; Atomico led the $27M Series B of Jun 2020 (PR Newswire; the firm's own post, Ben Blume joining the board) - the Form D band read Series A; acquired by Reveal May 2024 (Business Wire)",
             rounds=[rnd("2020-06-17", "Series B", 27000000, "Atomico", True, "https://www.prnewswire.com/news-releases/onna-raises-27m-series-b-to-scale-worlds-first-knowledge-integration-platform-kip-301078333.html")]))
L.append(cls("ontruck", status="private", rng="below_1b", country="ES", city="Madrid", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-ontruck-driving-european-road-freight-into-the-future",
             note="Digital road-freight marketplace; the firm's own post (May 2017): 'The $10m Series A investment we are announcing today'",
             rounds=[rnd("2017-05-11", "Series A", 10000000, None, True, INS + "our-investment-in-ontruck-driving-european-road-freight-into-the-future", "firm")]))
L.append(cls("openfx", status="private", rng="below_1b", country="US", city="San Francisco", focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://ibsintelligence.com/ibsi-news/openfx-raises-94m-series-a-to-scale-cross-border-payments/",
             note="Stablecoin FX / cross-border payments infrastructure (founded 2024); the $94M Series A of Apr 2026 (IBS Intelligence; M13 co-led, Quartz) with the firm's own post - Atomico's first round",
             rounds=[rnd("2026-04-01", "Series A", 94000000, None, True, "https://ibsintelligence.com/ibsi-news/openfx-raises-94m-series-a-to-scale-cross-border-payments/")]))
L.append(cls("opna", status="private", rng="below_1b", country="GB", city="London", focus="Climate & Energy",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-opna-unlocking-the-capital-to-solve-climate-change",
             entry_date="2023-09-05",
             note="Carbon-project financing platform (legal entity Salt Global Tech Ltd: the register's Mar 2024 and Feb 2026 statements list Atomico Venture VI SCSp holding SEED 2 shares; Hougaard director 2023-2025); the firm's own post (Sep 2023): 'Enter Opna, our newest $6.5 million Seed partnership'; graduation decided in the S2A pass",
             rounds=[rnd("2023-09-05", "Seed", 6500000, None, True, INS + "our-investment-in-opna-unlocking-the-capital-to-solve-climate-change", "firm")]))
L.append(cls("pactum", status="private", rng="below_1b", city="Mountain View",
             note="AI contract-negotiation automation (Estonian founders; Form D issuer address Mountain View, CA); Atomico led the Apr 2021 round (the firm's own posts: 'with a total of $15M in funding secured'; Form D 2021 $11M) - the Form D band's Series A stands; Form D $50M 2025"))
L.append(cls("peakon", status="acquired", rng="below_1b", country="DK", city="Copenhagen", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://peakon.com/press/press-releases/peakon-closes-35m-extension-bringing-total-series-b-funding-to-57m-to-scale-the-worlds-leading-employee-retention-platform/",
             note="Employee-engagement platform; Atomico led the $35M Series B extension of Mar 2019 (Peakon's own release: 'Peakon closes $35M Extension, Bringing Total Series B funding to $57M'; the firm's Jan 2020 post: 'We missed Peakon's Series A'); acquired by Workday 2021 ($700M)",
             rounds=[rnd("2019-03-19", "Series B extension", 35000000, "Atomico", True, "https://peakon.com/press/press-releases/peakon-closes-35m-extension-bringing-total-series-b-funding-to-57m-to-scale-the-worlds-leading-employee-retention-platform/", "company")]))
L.append(cls("pedidosya", country="UY", city="Montevideo", focus="Consumer & Marketplaces",
             stage="undetermined", rng="below_1b",
             note="Latin American food delivery (Montevideo, 2009); on the 2011 fund-II page; the 2011 round is unnamed on every surface; acquired by Delivery Hero 2014"))
L.append(cls("pelago", status="private", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-pelago-doubling-down-on-substance-use-management",
             note="Digital substance-use treatment (formerly Quit Genius); the firm's own 2024 post: 'Atomico is once again partnering with Pelago to lead their $58 Million Series C, having co-led their Series B back in 2021' - the $64M round of Jul 2021 (MobiHealthNews); the quit-genius row merges into this one at the rebuild (identity-merges.json)",
             rounds=[rnd("2021-07-19", "Series B", 64000000, "Atomico (co-lead)", True, "https://www.mobihealthnews.com/news/digital-addiction-treatment-company-quit-genius-scores-64m"),
                     rnd("2024-03-28", "Series C", 58000000, "Atomico", True, INS + "our-investment-in-pelago-doubling-down-on-substance-use-management", "firm")]))
L.append(cls("physicsx", status="private", rng="1b_plus", usd=2400000000, val_src="web_verified", asof="2026-06-08",
             val_cite="https://ventureburn.com/physicsx-raises-300m-to-transform-engineering-with-ai/", val_conf="medium",
             country="GB", city="London", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "beyond-human-imagination",
             note="AI for engineering simulation; the firm's own post (Jun 2025): 'we are proud to lead this $135m Series B investment in PhysicsX' (CMS year 2025); $300M round at $2.4B Jun 2026 (Ventureburn)",
             rounds=[rnd("2025-06-22", "Series B", 135000000, "Atomico", True, INS + "beyond-human-imagination", "firm")]))
L.append(cls("pipedrive", status="acquired", rng="below_1b", country="EE", city="Tallinn", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-pipedrive-putting-salespeople-in-the-drivers-seat",
             note="Sales CRM; the firm's own post (Jan 2017): 'partnering with the Pipedrive team by leading their $17 million Series B round'; Vista Equity Partners took majority control Nov 2020 -> acquired",
             rounds=[rnd("2017-01-18", "Series B", 17000000, "Atomico", True, INS + "our-investment-in-pipedrive-putting-salespeople-in-the-drivers-seat", "firm")]))
L.append(cls("plato", status="private", rng="below_1b", country="DE", city="Berlin", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.thesaasnews.com/news/plato-secures-14-5-million-in-seed-round/",
             entry_date="2026-02-19", grad="censored",
             note="AI operating system for wholesale distributors (Berlin, 2023); the firm's page dates to the $14.5M (EUR 12.2M) seed of Feb 2026 (The SaaS News, Tech.eu) - Atomico's first round; censored",
             rounds=[rnd("2026-02-19", "Seed", 14500000, None, True, "https://www.thesaasnews.com/news/plato-secures-14-5-million-in-seed-round/")]))
L.append(cls("pocketlaw", status="private", rng="below_1b", country="SE", city="Stockholm", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "why-we-invested-in-pocketlaw-finally-legal-peace-of-mind-for-smbs",
             note="Legal-work SaaS for SMEs; the firm's own post (May 2022): 'Leading Kira's & Olga's $11m Series A is an absolute privilege'",
             rounds=[rnd("2022-05-19", "Series A", 11000000, "Atomico", True, INS + "why-we-invested-in-pocketlaw-finally-legal-peace-of-mind-for-smbs", "firm")]))
L.append(cls("pomelo-care", status="private", rng="1b_plus", usd=1700000000, val_src="web_verified", asof="2026-01-08",
             val_cite="https://www.mobihealthnews.com/news/pomelo-care-raises-92m-reaches-17b-valuation", val_conf="high",
             country="US", city="New York", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.mobihealthnews.com/news/pomelo-care-raises-92m-reaches-17b-valuation",
             note="Virtual maternity and pediatric care; the firm's page (CMS year 2026, lead partner Hillary Ball) dates to the $92M Series C of Jan 2026 at $1.7B (MobiHealthNews) - Atomico's first round",
             rounds=[rnd("2026-01-08", "Series C", 92000000, None, True, "https://www.mobihealthnews.com/news/pomelo-care-raises-92m-reaches-17b-valuation")]))
L.append(cls("psiquantum", status="private", rng="1b_plus", usd=7000000000, val_src="web_verified", asof="2025-09-10",
             val_cite="https://www.psiquantum.com/news-import/psiquantum-1b-fundraise", val_conf="high",
             city="Palo Alto",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://quantumcomputingreport.com/psiquantum-raises-a-150-million-series-c-round-bringing-total-funding-to-215-million/",
             flags=["stage_disputes_band"],
             note="Photonic quantum computing; the firm's own post (Apr 2020): 'proud to announce its partnership with PsiQuantum by leading the firm's latest funding round' - the $150M Series C (Quantum Computing Report; $215M raised in total, Bloomberg); $1B Series E at $7B Sep 2025 (the company's release); the Form D band read a 2025 filing as a Series A entry (overridden)",
             rounds=[rnd("2020-04-06", "Series C", 150000000, "Atomico", True, "https://quantumcomputingreport.com/psiquantum-raises-a-150-million-series-c-round-bringing-total-funding-to-215-million/"),
                     rnd("2025-09-10", "Series E", 1000000000, None, None, "https://www.psiquantum.com/news-import/psiquantum-1b-fundraise", "company")]))
L.append(cls("qatalog", status="acquired", rng="below_1b", country="GB", city="London", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.maddyness.com/uk/2020/10/16/over-340m-raised-by-uk-startups-across-a-wide-range-of-verticals-this-week/",
             note="Work-graph collaboration software; GBP 11.6M Series A led by Atomico Oct 2020 (Maddyness; $15.0M at the ECB rate of 2020-10-16; the firm's own post, Haivas on the board 2020-2025); the register's 2024 statement lists Atomico V SCSp with SERIES A and A2 PREFERRED shares; acquired by ClickUp Nov 2025 (Business Wire), the UK company dissolved Jul 2026 (register)",
             rounds=[rnd("2020-10-13", "Series A", 14980542, "Atomico", True, "https://www.maddyness.com/uk/2020/10/16/over-340m-raised-by-uk-startups-across-a-wide-range-of-verticals-this-week/")]))

if __name__ == "__main__":
    jl.write("batch-002", L)
