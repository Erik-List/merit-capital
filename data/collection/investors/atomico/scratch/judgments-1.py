"""PRO-79 grind, batch-001 (6wunderkinder .. healx). Evidence: scratch/evidence-pack.json,
the firm's own posts (sources/site/insights.json), the UK register layer, headlines and
web checks recorded per line."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
INS = "https://atomico.com/insights/"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
TODAY = "2026-09-26"

L = []
L.append(cls("6wunderkinder", status="acquired", rng="below_1b", country="DE", city="Berlin", focus="SaaS",
             stage="Series A", stage_src="model", stage_conf="medium",
             note="Wunderlist maker; Atomico led the $4.2M round of Nov 2011 (EU-Startups), the round before the Nov 2013 $19M Series B (FinSMEs) in which it followed, i.e. the Series A; acquired by Microsoft Jun 2015 (Microsoft blog)",
             rounds=[rnd("2011-11", "Series A", 4200000, "Atomico", True, "https://www.eu-startups.com/2011/11/atomico-invests-4-2-million-in-6wunderkinder/"),
                     rnd("2013-11", "Series B", 19000000, "Sequoia", True, INS + "6wunderkinder-hits-new-milestone-and-crosses-its-next-funding-round-off-its-to-do-list", "firm")]))
L.append(cls("abacum", status="private", rng="below_1b", country="ES", city="Barcelona", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-abacum-empowering-finance-teams-to-make-organisations-thrive",
             flags=["stage_disputes_band", "model_disputes_source"],
             note="FP&A software; the firm's own post (Nov 2021) announces partnering in Abacum's $25M Series A (overrides the formd_band Growth read off the 2025 US filing); Barcelona-based, the Form D address is the US subsidiary Abacum Inc.",
             rounds=[rnd("2021-11-30", "Series A", 25000000, None, True, INS + "our-investment-in-abacum-empowering-finance-teams-to-make-organisations-thrive", "firm")]))
L.append(cls("accurx", status="private", rng="below_1b", country="GB", city="London", focus="Healthcare & Bio",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.finsmes.com/2019/02/accurx-raises-8-8m-in-series-a-funding.html",
             note="NHS patient-messaging platform (Entrepreneur First alumni); Atomico led the GBP 8.8M Series A Feb 2019 (register: Atomico named from the May 2019 statement; Haivas then Blume directors); GBP 27.5M Series B Sep 2021",
             rounds=[rnd("2019-02", "Series A", 11500000, "Atomico", True, "https://www.finsmes.com/2019/02/accurx-raises-8-8m-in-series-a-funding.html"),
                     rnd("2021-09-15", "Series B", 38000000, None, None, "https://www.mobihealthnews.com/news/emea/british-healthcare-platform-accurx-scores-ps275m-series-b-round")]))
L.append(cls("aiven", country="FI", city="Helsinki", focus="Data Infrastructure",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "why-we-invested-in-aiven-the-leading-provider-of-open-source-data-infrastructure",
             note="Open-source data infrastructure cloud; the firm's own post: 'When we first invested into Aiven and led their $100 million Series C in March' 2021; Series D extension 2022 (unicorn); valuation pinned in the A/B pass",
             rounds=[rnd("2021-03-23", "Series C", 100000000, "Atomico", True, INS + "why-we-invested-in-aiven-the-leading-provider-of-open-source-data-infrastructure", "firm")]))
L.append(cls("andercore", status="private", rng="below_1b", city="Berlin", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.eu-startups.com/2026/02/berlins-andercore-secures-e33-5-million-to-scale-industrial-trade-platform-across-europe/",
             note="Industrial-parts trade platform (Berlin, 2021); the firm's own page dates to Feb 2026, the week of the $40M (EUR 33.5M) Series B, which is Atomico's first round (no earlier Atomico round in the press); listed on the job board",
             rounds=[rnd("2026-02-11", "Series B", 40000000, None, True, "https://www.eu-startups.com/2026/02/berlins-andercore-secures-e33-5-million-to-scale-industrial-trade-platform-across-europe/")]))
L.append(cls("ankar", status="private", rng="below_1b", country="GB", city="London", focus="AI & Applied AI",
             stage="undetermined",
             note="AI patent/IP operating system (London, Palantir alumni); Atomico led the $20M (GBP 15M) Series A Dec 2025, but the register already names an Atomico vehicle as a holder in the Oct 2024 confirmation statement (Helbig director from Nov 2025), so the first position predates the A and its round is not named on any surface -> undetermined",
             rounds=[rnd("2025-12-17", "Series A", 20000000, "Atomico", True, "https://www.uktechnews.info/2025/12/17/ankar-secures-15-million-series-a-investment-led-by-atomico/")]))
L.append(cls("aplo", status="acquired", rng="below_1b", country="FR", city="Paris", focus="Crypto & Web3",
             stage="undetermined",
             note="Crypto prime broker (formerly SheeldMarket); the firm's own Oct 2021 post announces the partnership without naming the round; acquired by Coincheck Group Sep 2025 (CoinDesk) - Atomico V SCSp holds Coincheck shares as consideration (decisions.md D6)"))
L.append(cls("arculus", status="acquired", rng="below_1b", country="DE", city="Munich", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-arculus-bringing-modular-production-to-manufacturing",
             flags=["model_disputes_source"],
             note="Modular production / AMR platform; the firm's own post (May 2020) announces its lead role in arculus's Series A; acquired by Jungheinrich AG Nov 2021 (The Robot Report); the SEC-float pre-fill was a weak CIK join to an unrelated registrant (disputed)",
             rounds=[rnd("2020-05-19", "Series A", None, "Atomico", True, INS + "our-investment-in-arculus-bringing-modular-production-to-manufacturing", "firm")]))
L.append(cls("attentive", status="private", country="US", city="New York", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-attentive-personalized-mobile-messaging-for-innovative-brands",
             note="SMS marketing platform; the firm's own post (Nov 2020) announces its participation in Attentive's $230M Series D; valuation pinned in the A/B pass",
             rounds=[rnd("2020-11-23", "Series D", 230000000, None, True, INS + "our-investment-in-attentive-personalized-mobile-messaging-for-innovative-brands", "firm")]))
L.append(cls("automation-hero", status="unknown", rng="below_1b", city="San Francisco", focus="AI & Applied AI",
             note="Intelligent document processing (founded by Stefan Groschupf); Atomico in the $14.5M Series A Mar 2019 with Ben Blume joining the board (the firm's own post; Form D 2019 $15.5M); the firm's page marks it Exited but no sale is reported - last public news 2022; status unknown"))
L.append(cls("beekeeper", status="acquired", rng="below_1b", country="CH", city="Zurich", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-beekeeper-using-saas-to-connect-the-unconnected",
             note="Frontline-worker communication platform; the firm's own post (Sep 2018): 'co-lead Beekeeper's Series A extension' with Keen Ventures; agreed to be acquired by LumApps Jul 2025, completed 2026 (William Blair, unleash.ai)",
             rounds=[rnd("2018-09-10", "Series A extension", None, "Atomico; Keen Venture Partners", True, INS + "our-investment-in-beekeeper-using-saas-to-connect-the-unconnected", "firm")]))
L.append(cls("ben", status="private", rng="below_1b", country="GB", city="London", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2022/08/03/employee-benefits-platform-ben-raises-16m-to-cut-hr-admin/",
             note="Employee-benefits platform; Atomico led the $16M (GBP 13M) Series A Aug 2022 (TechCrunch, BusinessCloud 'Atomico backs Ben in GBP 13m Series A'); GBP 21M Series B Dec 2025",
             rounds=[rnd("2022-08-03", "Series A", 16000000, "Atomico", True, "https://techcrunch.com/2022/08/03/employee-benefits-platform-ben-raises-16m-to-cut-hr-admin/"),
                     rnd("2025-12-17", "Series B", 27500000, None, None, "press")]))
L.append(cls("bird", status="private", city="Amsterdam", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-messagebird-a-european-deep-tech-wunderkind-enabling-truly-global-cloud-communications",
             flags=["stage_disputes_band"],
             note="MessageBird, rebranded Bird 2024 (cloud communications / CRM); the firm's own post (Oct 2017): invited to participate in the $60M Series A (Accel-led) - Series A by the round's name, the site's Growth label notwithstanding; valuation pinned in the A/B pass",
             rounds=[rnd("2017-10-03", "Series A", 60000000, "Accel", True, INS + "our-investment-in-messagebird-a-european-deep-tech-wunderkind-enabling-truly-global-cloud-communications", "firm")]))
L.append(cls("bitmovin", status="private", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-bitmovin-working-to-build-the-webs-new-video-infrastructure",
             note="Video encoding/streaming infrastructure (Austrian founders, SF HQ); the firm's own post: 'we've led Bitmovin's $10.3 million Series A' (Sep 2016), agreeing with the Form D band",
             rounds=[rnd("2016-09-02", "Series A", 10300000, "Atomico", True, INS + "our-investment-in-bitmovin-working-to-build-the-webs-new-video-infrastructure", "firm")]))
L.append(cls("bossa-studios", status="private", rng="below_1b", city="London", focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-bossa-studios-funding-the-next-generation-of-innovative-games",
             note="Games studio (Surgeon Simulator, I Am Bread); the firm's own post: 'leading a $10m Series A' (Sep 2017); register: Atomico named in Bossaco Ltd's Jul 2018 statement, Ljungman director 2017-2019; sold several IPs to tinyBuild 2022, layoffs 2024, still operating",
             rounds=[rnd("2017-09-12", "Series A", 10000000, "Atomico", True, INS + "our-investment-in-bossa-studios-funding-the-next-generation-of-innovative-games", "firm")]))
L.append(cls("caddi", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", asof="2026-09-16",
             val_cite="https://www.businesswire.com/news/home/20260916456307/en/CADDi-Raises-$114-Million-in-Series-D-at-$1.2-Billion-Valuation",
             val_conf="high", city="Tokyo", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-caddi-the-ai-data-platform-transforming-manufacturing",
             note="Manufacturing AI data platform (Tokyo); the firm's own post (Mar 2025): 'Atomico is excited to lead the firm's $38M Series C Extension'; $114M Series D at $1.2B Sep 2026 with Atomico participating (Business Wire)",
             rounds=[rnd("2025-03-27", "Series C extension", 38000000, "Atomico", True, INS + "our-investment-in-caddi-the-ai-data-platform-transforming-manufacturing", "firm"),
                     rnd("2026-09-16", "Series D", 114000000, None, True, "https://www.businesswire.com/news/home/20260916456307/en/CADDi-Raises-$114-Million-in-Series-D-at-$1.2-Billion-Valuation", "company")]))
L.append(cls("channelengine", status="private", rng="below_1b", city="Leiden", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.lw.com/en/news/2022/03/latham-advises-atomico-on-channelengine-series-b",
             note="Marketplace-integration SaaS (Leiden); Atomico led the US$50M (EUR 45.5M) Series B Mar 2022 (Latham & Watkins, counsel to Atomico; EU-Startups)",
             rounds=[rnd("2022-03-15", "Series B", 50000000, "Atomico", True, "https://www.lw.com/en/news/2022/03/latham-advises-atomico-on-channelengine-series-b")]))
L.append(cls("chemist-direct", status="acquired", rng="below_1b", city="London", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Online pharmacy (Direct Healthcare Ltd); Atomico's entry is dated by the register (Ljungman director Feb 2009; Atomico first named in the Dec 2009 statement) but no surface names the round; merged into Pharmacy2U Jul 2016 (the firm's own post), Atomico then a Pharmacy2U holder as consideration (decisions.md ruling 13)"))
L.append(cls("claimsorted", status="private", rng="below_1b", country="GB", city="London", focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-claimsorted-pioneering-the-future-of-claims-administration",
             entry_date="2025-10-13", grad="censored",
             note="AI-native claims administration (London, YC alumni); the firm's own post (Oct 2025): 'our $13.3 million seed investment in ClaimSorted led by Atomico'; censored (entry under 24 months)",
             rounds=[rnd("2025-10-13", "Seed", 13300000, "Atomico", True, INS + "our-investment-in-claimsorted-pioneering-the-future-of-claims-administration", "firm")]))
L.append(cls("cloudnc", status="private", rng="below_1b", country="GB", city="London", focus="AI & Applied AI",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2018/06/07/cloudnc/",
             note="AI CNC-machining software; Atomico led the GBP 9M Series A Jun 2018 (TechCrunch; Khaliq director May 2018; register names Atomico from Nov 2018); $45M 2022, $20M Sep 2026",
             rounds=[rnd("2018-06-07", "Series A", 12000000, "Atomico", True, "https://techcrunch.com/2018/06/07/cloudnc/")]))
L.append(cls("clutter", status="acquired", rng="below_1b", city="Los Angeles", focus="Consumer & Marketplaces",
             note="On-demand storage; Atomico entered at the 2017 $64M round (Form D 2017 $63.8M, Tamura as related person; the filings band Growth); merged with MakeSpace 2022, then taken over by lender Iron Mountain through the foreclosure of Clutter Holdings (Bloomberg Law 2024-2025) -> acquired out of insolvency"))
L.append(cls("commsor", status="private", rng="below_1b", country="US", city="New York", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-commsor-unlocking-the-power-of-community-for-modern-businesses",
             note="Community software; the firm's own post (Mar 2022): 'our Series B investment in Commsor'",
             rounds=[rnd("2022-03-01", "Series B", None, None, True, INS + "our-investment-in-commsor-unlocking-the-power-of-community-for-modern-businesses", "firm")]))
L.append(cls("connect-parts", status="unknown", rng="below_1b", country="BR", city="São Paulo", focus="Consumer & Marketplaces",
             stage="undetermined",
             note="Brazilian online auto-parts retailer (formerly Dakota Parts); the firm's own Feb 2012 post: 'invested US$8.7m in Connect Parts' (round unnamed); the site still lists it Current but no news since - status unknown"))
L.append(cls("corti", status="private", rng="below_1b", country="DK", city="Copenhagen", focus="AI & Applied AI",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-corti-supporting-overburdened-healthcare-professionals-globally",
             note="AI assistants for clinicians; the firm's own post (Sep 2023): 'our newest $60million Series B partnership'",
             rounds=[rnd("2023-09-20", "Series B", 60000000, "Atomico; Prosus", True, INS + "our-investment-in-corti-supporting-overburdened-healthcare-professionals-globally", "firm")]))
L.append(cls("deepl", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2024-05-22",
             val_cite="https://www.prnewswire.co.uk/news-releases/deepl-announces-300-million-investment-at-2-billion-valuation-fueled-by-global-demand-for-ai-language-solutions-302153042.html",
             val_conf="high", country="DE", city="Cologne", focus="AI & Applied AI",
             flags=["stale"],
             note="AI translation; Atomico joined the IVP-led round of Jan 2023 (the firm's own post; round unnamed in the press, ~$1B valuation) - stage left for the site-label scoring; $300M at $2B May 2024 (Index-led, PR Newswire), the last priced mark (stale beyond 24 months)"))
L.append(cls("deeploi", status="private", rng="below_1b", country="DE", city="Hamburg", focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-deeploi-boosting-businesses-through-smarter-it-management",
             entry_date="2024-01-24",
             note="IT-as-a-service for SMEs; after a EUR 3M pre-seed (Mar 2023, TechCrunch) the firm's own post (Jan 2024) announces 'our newest $6.5 million Seed partnership'; graduation decided in the S2A pass",
             rounds=[rnd("2023-03-15", "Pre-Seed", 3300000, None, False, "https://techcrunch.com/2023/03/15/it-as-a-service-startup-deeploi-raises-e3m/"),
                     rnd("2024-01-24", "Seed", 6500000, "Atomico", True, INS + "our-investment-in-deeploi-boosting-businesses-through-smarter-it-management", "firm")]))
L.append(cls("dexory", status="private", rng="below_1b", country="GB", city="London", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-dexory-modernising-warehouses-the-beating-heart-of-the-supply-chain",
             note="Warehouse robotics / digital twins; the firm's own post (Jun 2023): 'our newest $19 million Series A partnership' (Blume director May 2023); Series B 2024, Series C 2025 with a BBB extension Mar 2026, valuations undisclosed",
             rounds=[rnd("2023-06-27", "Series A", 19000000, "Atomico", True, INS + "our-investment-in-dexory-modernising-warehouses-the-beating-heart-of-the-supply-chain", "firm")]))
L.append(cls("digitail", status="private", rng="below_1b", city="Toronto", focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2023/01/12/digitail-raises-11-million-via-atomico/",
             note="Veterinary practice-management software (Romanian founders, US/Toronto HQ); Atomico led the $11M Series A Jan 2023 (Tech.eu; 'Atomico's first investment in Romania' per its own post); $23M Series B Nov 2025 (BetaKit) - the Form D band read that later filing",
             rounds=[rnd("2023-01-12", "Series A", 11000000, "Atomico", True, "https://tech.eu/2023/01/12/digitail-raises-11-million-via-atomico/"),
                     rnd("2025-11-10", "Series B", 23000000, None, None, "press")]))
L.append(cls("drivetribe", status="private", rng="below_1b", country="GB", city="London", focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-drivetribe-backing-the-top-gear-team-to-disrupt-online-media",
             note="Motoring media platform of the Grand Tour presenters; the firm's own post (Aug 2016): 'participating in DRIVETRIBE's $5.5 million Series A round' with Breyer Capital; still publishing 2023",
             rounds=[rnd("2016-08-17", "Series A", 5500000, None, True, INS + "our-investment-in-drivetribe-backing-the-top-gear-team-to-disrupt-online-media", "firm")]))
L.append(cls("evrythng", status="acquired", rng="below_1b", country="GB", city="London", focus="Industrial & Robotics",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://en.wikipedia.org/wiki/EVRYTHNG",
             entry_date="2011-11", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite="https://techcrunch.com/2014/04/30/iot-startup-evrythng-secures-7m-series-a-from-atomico-bhlp-cisco-and-dawn/",
             note="IoT product-identity platform; Atomico led the Nov 2011 seed (Wikipedia, citing the company), then led the $7M Series A Apr 2014 as 'a previous investor' (the firm's own post; TechCrunch) = graduation; acquired by Digimarc Jan 2022 (Atomico II among the sellers, 8-K)",
             rounds=[rnd("2011-11", "Seed", 1000000, "Atomico", True, "https://en.wikipedia.org/wiki/EVRYTHNG"),
                     rnd("2014-04-30", "Series A", 7000000, "Atomico", True, "https://techcrunch.com/2014/04/30/iot-startup-evrythng-secures-7m-series-a-from-atomico-bhlp-cisco-and-dawn/"),
                     rnd("2017-03-14", "Series B", 24800000, None, None, "https://techcrunch.com/2017/03/14/evrythng-series-b/")]))
L.append(cls("fabricnano", status="private", rng="below_1b", country="GB", city="London", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-fabricnano-enabling-the-bioindustrial-revolution",
             flags=["model_disputes_source"],
             note="Cell-free biomanufacturing; the firm's own posts (Jul 2021) announce leading FabricNano's Series A (Form D 2021 $12.5M agrees); London-based, the Form D address is the US entity FabricNano Inc.",
             rounds=[rnd("2021-06-30", "Series A", 12500000, "Atomico", True, INS + "our-investment-in-fabricnano-enabling-the-bioindustrial-revolution", "firm")]))
L.append(cls("factorial", status="private", rng="1b_plus", usd=2500000000, val_src="web_verified", asof="2026-06-03",
             val_cite="https://tech.eu/2026/06/03/factorial-raises-150m-series-d-at-25b-valuation-to-expand-across-europe/",
             val_conf="high", country="ES", city="Barcelona", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.lw.com/en/news/2022/10/latham-advises-atomico-on-factorials-us120-million-series-c",
             note="SMB HR / workforce platform; Atomico led the US$120M Series C Oct 2022 (Latham & Watkins, counsel to Atomico; the firm's own post); $150M Series D at $2.5B Jun 2026 (General Catalyst lead, Atomico participating; Tech.eu)",
             rounds=[rnd("2022-10-11", "Series C", 120000000, "Atomico", True, "https://www.lw.com/en/news/2022/10/latham-advises-atomico-on-factorials-us120-million-series-c"),
                     rnd("2026-06-03", "Series D", 150000000, "General Catalyst", True, "https://tech.eu/2026/06/03/factorial-raises-150m-series-d-at-25b-valuation-to-expand-across-europe/")]))
L.append(cls("farmdrop", status="defunct", rng="below_1b", country="GB", city="London", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=CH + "08111929/filing-history",
             entry_date="2016-02-03",
             note="Online farmers' market grocer; the firm's own post (Feb 2016) announces 'leading FarmDrop's latest investment round, worth GBP 3m'; the register's Aug 2016 annual return lists Atomico IV LP holding SERIES SEED PREFERRED shares -> the Series Seed; administration Dec 2021 (BBC), dissolved 2024; graduation decided in the S2A pass",
             rounds=[rnd("2016-02-03", "Series Seed", 3900000, "Atomico", True, INS + "our-investment-in-farmdrop-on-a-mission-to-fix-the-food-chain", "firm")]))
L.append(cls("fat-llama", status="acquired", rng="below_1b", country="GB", city="London", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-fat-llama-bringing-the-sharing-economy-to-everything-you-own",
             note="Peer-to-peer rental marketplace; the firm's own post (Apr 2018) announces its Series A investment; acquired by Hygglo Aug 2022 for ~$41.5M (EU-Startups)",
             rounds=[rnd("2018-04-25", "Series A", 10000000, None, True, INS + "our-investment-in-fat-llama-bringing-the-sharing-economy-to-everything-you-own", "firm")]))
L.append(cls("fon", status="acquired", rng="below_1b", city="Madrid", focus="Industrial & Robotics",
             stage="undetermined",
             note="Community WiFi network (Martin Varsavsky); on the 2008 listing and under Atomico Ventures I in 2010, so the first position predates the EUR 10M round Atomico led Feb 2011 (the firm's own release); the fund-I round is unnamed on every surface -> undetermined; bought by Agile Content Apr 2021 (Broadband TV News)"))
L.append(cls("framer", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2025-08-28",
             val_cite="https://www.businesswire.com/news/home/20250828901842/en/Framer-Raises-$100-Million-Series-D-at-a-$2-Billion-Valuation-to-Redefine-How-Businesses-Build-Websites",
             val_conf="high", city="Amsterdam", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2018/11/12/framer-series-b/",
             flags=["stage_disputes_band"],
             note="Website design/publishing platform; Atomico led the $24M Series B Nov 2018 (TechCrunch) - the Form D band read that first Atomico filing as a Series A; $100M Series D at $2B Aug 2025 co-led by Meritech and Atomico (Business Wire)",
             rounds=[rnd("2018-11-12", "Series B", 24000000, "Atomico", True, "https://techcrunch.com/2018/11/12/framer-series-b/"),
                     rnd("2025-08-28", "Series D", 100000000, "Meritech; Atomico", True, "https://www.businesswire.com/news/home/20250828901842/en/Framer-Raises-$100-Million-Series-D-at-a-$2-Billion-Valuation-to-Redefine-How-Businesses-Build-Websites", "company")]))
L.append(verdict("free-now", "not_member",
                 "The firm's own page dates Free Now to Hailo's 2011 investment year and calls it 'part of the mobility joint venture' that acquired Hailo in 2016: the Free Now stake is Hailo's sale consideration, Hailo is the member (decisions.md ruling 13; COLLECTION.md §1, Erik 2026-09-22)",
                 "site_listing", "high", "https://atomico.com/partners/free-now"))
L.append(cls("gaia", status="private", rng="below_1b", country="GB", city="London", focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2022/02/14/gaia-a-platform-to-finance-ivf-treatments-closes-20m-series-a-led-by-atomico/",
             flags=["model_disputes_source"],
             note="IVF financing / fertility insurance; Atomico led the $20M Series A Feb 2022 (TechCrunch); $100M credit facility May 2026; the SEC-float pre-fill was Gaia Inc. (a US public company) on a weak CIK join, and Wikidata's Belgium match a homonym (both disputed)",
             rounds=[rnd("2022-02-14", "Series A", 20000000, "Atomico", True, "https://techcrunch.com/2022/02/14/gaia-a-platform-to-finance-ivf-treatments-closes-20m-series-a-led-by-atomico/")]))
L.append(cls("gengo", status="acquired", rng="below_1b", city="Tokyo", focus="AI & Applied AI",
             stage="undetermined",
             note="Crowdsourced translation (myGengo on the 2011 fund-II page); Atomico entered in 2011, but no surface on disk names that round; acquired by Lionbridge Jan 2019 (BRIDGE)"))
L.append(cls("graphcore", status="acquired", rng="below_1b", country="GB", city="Bristol", focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-graphcore-accelerating-the-arrival-of-our-ai-future",
             note="AI chips (IPU); the firm's own post (Jul 2017): 'Atomico is leading Graphcore's $30m Series B'; register: Atomico named from the May 2018 statement, Khaliq director 2017-2024; acquired by SoftBank Jul 2024",
             rounds=[rnd("2017-07-20", "Series B", 30000000, "Atomico", True, INS + "our-investment-in-graphcore-accelerating-the-arrival-of-our-ai-future", "firm")]))
L.append(cls("habito", status="acquired", rng="below_1b", country="GB", city="London", focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-habito-why-using-technology-for-mortgages-is-a-better-deal-for-both-borrowers-and-lenders",
             note="Digital mortgage broker; the firm's own post (Sep 2017): 'we have led Habito's GBP 18.5m Series B'; Monzo's acquisition announced Dec 2025, completed Apr 2026 (Mortgage Strategy)",
             rounds=[rnd("2017-09-04", "Series B", 24000000, "Atomico", True, INS + "our-investment-in-habito-why-using-technology-for-mortgages-is-a-better-deal-for-both-borrowers-and-lenders", "firm")]))
L.append(cls("hailo", status="acquired", rng="below_1b", country="GB", city="London", focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "congratulations-hailo-and-mytaxi",
             entry_date="2011",
             flags=["model_disputes_source"],
             note="Taxi e-hailing app; the firm's own post: 'Atomico has sat on the Board of Hailo since our very first seed investment in 2011'; merged into mytaxi (Daimler/BMW) 2016 - acquired; the unicorn-list $1B 'Hailo' is the Israeli AI-chip company (homonym, disputed); graduation decided in the S2A pass",
             rounds=[rnd("2011", "Seed", None, None, True, INS + "congratulations-hailo-and-mytaxi", "firm")]))
L.append(cls("harbor-lab", status="private", rng="below_1b", country="GR", city="Athens", focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite=INS + "our-investment-in-harbor-lab-modernising-accounting-in-the-dollar14t-global-shipping-industry",
             note="Port-disbursement accounting for shipping; the firm's own post (May 2024) announces leading the $16M Series A",
             rounds=[rnd("2024-05-15", "Series A", 16000000, "Atomico", True, INS + "our-investment-in-harbor-lab-modernising-accounting-in-the-dollar14t-global-shipping-industry", "firm")]))
L.append(cls("healx", status="private", rng="below_1b", country="GB", city="Cambridge", focus="Healthcare & Bio",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.fiercebiotech.com/biotech/healx-raises-56m-to-launch-40-rare-disease-r-d-programs",
             note="AI rare-disease drug discovery; Atomico led the $56M Series B Oct 2019 (FierceBiotech; the firm's own 2024 post recalls leading the B and leads the $47M Series C)",
             rounds=[rnd("2019-10-16", "Series B", 56000000, "Atomico", True, "https://www.fiercebiotech.com/biotech/healx-raises-56m-to-launch-40-rare-disease-r-d-programs"),
                     rnd("2024-08-01", "Series C", 47000000, "Atomico", True, INS + "our-continued-investment-in-healx-leveraging-ai-to-advance-rare-disease-treatments", "firm")]))

if __name__ == "__main__":
    jl.write("batch-001", L)
