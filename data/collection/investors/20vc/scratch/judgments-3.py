"""PRO-76 grind, batch-003: membership verdicts for the 27 press recall additions
(companies/membership-ledger.json) and the Form D homonym Crosstown Brewing, then
the first-pass classification of every member in the batch (status, country,
city, focus, band, entry round, funding history; S2A in its own pass). Every
citation was fetched and its sentence read (verify-url.py). Rulings cited:
decisions.md D1-D9, R1; COLLECTION.md T4 (person-level attribution).
Also re-records Nex Health's note: TechCrunch 2020-07-17 names it one of the
twelve investments made out of Fund I."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
L = []
W = "web_verified"
U = "undetermined"
NOSTAGE = {"entry_stage_source": None, "entry_stage_confidence": None, "entry_stage_citation": None}
FORTUNE = "https://fortune.com/2021/06/16/harry-stebbings-podcaster-vc-20vc-mit-spotify/"
TC_FUND1 = "https://techcrunch.com/2020/07/17/from-twenty-minute-vc-to-20vc-harry-stebbings-launched-a-micro-vc-off-the-back-of-his-popular-podcast/"


def member(slug, basis, cite, conf="high"):
    L.append(verdict(slug, "member", basis, ec="web", conf=conf, cite=cite))


# ======================= membership =======================
member("clubhouse", "Fund I, the $8.3M micro fund begun in April 2020, 'has made investments in several companies that experienced runaway growth during the COVID-19 pandemic, including Hopin and social media app Clubhouse' (Fortune, 2021-06-16): 20VC's own fund.", FORTUNE)
member("revenuecat", "Fund I 'has made investments in ... Hopin and social media app Clubhouse, as well as RevenueCat' (Fortune, 2021-06-16): 20VC's own fund; the $15M Series A of August 2020 names Harry Stebbings among its participants (Crunchbase News, 2020-08-11).", FORTUNE)
member("spiketrap", "'some 12 investments have already been made out of it (Nex Health and Spiketrap are the only two that are public so far)' (TechCrunch, 2020-07-17, on Fund I): 20VC's own fund.", TC_FUND1)
member("shoppinggives", "'raised $5.5 million in seed funding led by Caffeinated Capital and a group of investors that includes Tuesday Capital, SciFi VC, Background Capital, Red Dog Capital and 20VC' (Crunchbase News, 2020-09-18).", "https://news.crunchbase.com/startups/startups-to-watch-finch-grin-zuper-shoppinggives/")
L.append(verdict("bukuwarung", "not_member",
    "'raised new funding from a roster of high-profile investors, including partners of DST Global, Soma Capital and 20VC' (TechCrunch, 2020-09-28) names partners of those firms, that is people, and in September 2020 the partner of 20VC was Harry Stebbings; the firm never lists BukuWarung on any surface. Person-level attribution alone admits nothing (COLLECTION.md T4; decisions.md R1).",
    ec="web", conf="medium", cite="https://techcrunch.com/2020/09/28/indonesian-fintech-startup-bukuwarung-gets-new-funding-to-add-financial-services-for-small-merchants/"))
member("pomelo", "'U.S.-based Index Ventures and Brazil's monashees co-led the funding round, which also included participation from ... 20VC' in Pomelo's $9M seed (TechCrunch, 2021-05-12).", "https://techcrunch.com/2021/05/12/argentinas-pomelo-raises-9m-to-build-a-new-payments-infrastructure-for-latam-fintechs/")
member("airlift", "'The investment was co-led by Harry Stebbings' 20 VC Explorer and Josh Buckley's Buckley Ventures' (MENAbytes, 2021-08-18, the $85M Series B): Explorer Fund II is 20VC's (decisions.md D1).", "https://www.menabytes.com/airlift-series-b/")
member("polywork", "'Bungalow Capital and 20VC were among the other participants' in the $13M Series A led by Andreessen Horowitz (Silicon Republic, 2021-08-06).", "https://www.siliconrepublic.com/start-ups/polywork-series-a")
member("digits", "'SoftBank's Vision Fund is leading the funding, with U.K. investor Harry Stebbings' 20VC Growth, GV and Benchmark also participating' (TechCrunch, 2022-03-24): '20VC Growth' is the Explorer growth fund (decisions.md D1).", "https://techcrunch.com/2022/03/24/digits-books-65m-on-a-565m-valuation-to-bring-a-more-dynamic-automated-approach-to-legacy-accounting-tools/")
member("atlantic-money", "'The round led by Amplo and Ribbit Capital alongside participation from Kleiner Perkins, Index Ventures ..., Harry Stebbings' 20VC, Elefund' (Tech Funding News, 2022-03-09, the $4.5M seed).", "https://techfundingnews.com/founded-by-rohinhood-alumni-atlantic-money-takes-on-wise-paypal-picks-4-5m/")
member("cycle", "'Base Case, The 20VC Fund, SV Angel, BoxGroup, Hummingbird Ventures and 60 angels also invested in the company' (TechCrunch, 2023-02-28).", "https://techcrunch.com/2023/02/28/cycle-is-a-new-product-management-hub-that-centralizes-all-customer-feedback/")
member("noded-ai", "'Today's $4 million investment was led by Boldstart Ventures with participation from Bessemer Venture Partners, 20VC and First Hand Ventures' (TechCrunch, 2024-07-23).", "https://techcrunch.com/2024/07/23/noded-ai-wants-to-make-your-notes-the-center-of-your-work-world/")
member("11x", "'Other investors in the round included 20VC, Project A, Lux Capital, and SV Angel' (TechCrunch, 2024-09-16, the $24M Series A led by Benchmark); 20VC's own boilerplate names 11x among its companies (UK Tech Investment News, 2025-03-17).", "https://techcrunch.com/2024/09/16/ai-digital-employee-startup-11xai-raises-24m-led-by-benchmark/")
member("archy", "'$15M Series A funding in a round led by Entree Capital with participation from Bessemer Venture Partners, CRV, Alven, 20VC Growth fund' (HIT Consultant, 2024-10-23): the Explorer growth fund (decisions.md D1).", "https://hitconsultant.net/2024/10/23/archy-raises-15m-to-optimize-dental-practices-with-ai-powered-automation/")
member("bounce", "'Bounce's Series B was led by Sapphire Sport, with participation from existing investors including Andreessen Horowitz and General Catalyst, as well as new investors 20VC Growth, FJ Labs' (TechCrunch, 2024-11-12).", "https://techcrunch.com/2024/11/12/bounce-grabs-19m-to-expand-its-traveller-convenience-network/")
member("orreco", "'Existing investors include True Ventures, Jason Calacanis, 20VC and professional golfer Padraig Harrington' (Silicon Republic, 2025-12-15; Think Business the same day): the firm by name. No source dates its entry, so a pre-April-2020 personal check by Harry Stebbings (decisions.md D3) cannot be ruled out: medium.", "https://www.siliconrepublic.com/business/mark-cuban-backs-galway-sports-tech-orreco-in-4m-raise", conf="medium")
member("denki", "'Base10 Partners and Shine Capital co-led the raise, which included participation from Y Combinator, 20VC and others' (Crunchbase News, 2026-03-05, $4.1M).", "https://news.crunchbase.com/venture/yc-backed-denki-raise-financial-audit-automation-ai/")
member("zalos", "'Other investors include Cohen Circle, Harry Stebbings' 20VC and several angels' in the $3.6M seed led by 14Peaks Capital (Tech.eu, 2026-03-24).", "https://tech.eu/2026/03/24/agents-for-finance-startup-zalos-raises-3-6m-to-transform-finance-departments/")
member("lua", "'Norrsken22 led the seed round. Flourish Ventures, 20VC, P1 Ventures, Phosphor Capital and Y Combinator also participated' (SiliconANGLE, 2026-04-16).", "https://siliconangle.com/2026/04/16/lua-lands-5-8m-help-businesses-build-manage-ai-agent-workforces/")
member("uplane", "'The seed round was led by Play Ventures, with participation from Y Combinator, 20VC, Rebel Fund and Multimodal Ventures' (The American Bazaar, 2026-09-04; jawlah, 2026-04-19).", "https://americanbazaaronline.com/2026/09/04/uplane-to-work-with-ag1-and-kalshi-to-replace-marketing-agencies-487603/")
member("corvera", "'£3 million ($4.2 million) in seed funding ... led by 6 Degrees Capital, with participation from over 20 venture capital and angel investors including 20VC, Rebel Fund' (Retail Technology Innovation Hub, 2026-05-05).", "https://retailtechinnovationhub.com/home/2026/5/5/agentic-supply-chains-specialist-corvera-lands-3-million-in-seed-funding-to-scale-its-platform")
member("moritz", "'raised $9 million in a seed round through its MSO Parlai, led by startup incubator Y Combinator and venture capital fund 20VC' (Law.com, 2026-05-05).", "https://www.law.com/legaltechnews/2026/05/05/mso-parlai-and-its-hybrid-law-firm-moritz-announce-9m-in-seed-funding/")
member("prelude", "'French digital onboarding startup Prelude has raised $20m in a Series A funding round led by Harry Stebbings' 20VC, which is investing in the startup for the first time' (Tech.eu, 2026-05-20).", "https://tech.eu/2026/05/20/20vc-leads-20m-series-a-investment-in-onboarding-startup-prelude/")
member("archastro", "'ArchAstro is backed by venture capital firms 20VC - the London-based firm led by Harry Stebbings - and Kyber Knight', with 'pre-seed funding of $6.2 million' (GeekWire, 2026-06-09).", "https://www.geekwire.com/2026/ex-stripe-microsoft-vets-launch-archastro/")
member("archestra-ai", "'$10m in a seed funding round, led by Harry Stebbings' 20VC, a new investor in the startup' (Tech.eu, 2026-06-02).", "https://tech.eu/2026/06/02/archestraai-raises-10m-to-unlock-next-gen-agentic-use-case/")
member("fonio-ai", "'fonio.ai has closed a $17 million seed round at a $140 million valuation, led by 20VC' (Tech Funding News, 2026-06-09).", "https://techfundingnews.com/fonio-ai-17m-20vc-austria-seed-round/")
member("theker", "'The round was led by CRV, with participation from Samsung, LVMH, Cathay, 20VC, Henkel' in THEKER's $85M Series A (Cathay Capital's post, 2026-06-11).", "https://www.cathaycapital.com/theker-raises-85m-in-europes-largest-ever-robotics-series-a-led-by-crv-with-backing-from-samsung-and-lvmh/")
L.append(verdict("crosstown-brewing-co-llc", "not_member",
    "A Form D homonym (decisions.md D9): Crosstown Brewing Co LLC (Memphis, 2016) matched on the related person 'Will Goodwin', a namesake of William Goodwin, the LLP member of 2021-2025; the offering predates every 20VC vehicle (the first dates from April 2020) and no surface of the firm lists a brewery.",
    ec="formd_adjudicated", conf="high"))

# ======================= classification =======================
L.append(cls("clubhouse", status="private", country="US", city="San Francisco", focus="Consumer & Marketplaces", rng="1b_plus", usd=4000000000, val_src=W,
    asof="2021-04-18", val_cite="https://voicebot.ai/2021/04/19/clubhouse-closes-new-financing-at-4-billion-valuation/",
    stage=U, extra=NOSTAGE, flags=["stale", "model_disputes_source", "identity_homonym"], clear=["needs_web_value", "unicorn_name_match"],
    note="Social audio app (Clubhouse, Alpha Exploration Co., San Francisco). A Fund I position (Fortune, 2021-06-16). Every Clubhouse round from April 2020 (the $12M Series A a16z led in May 2020, the Series B of January 2021, the Series C of April 2021) could have been Fund I's and no source names it: undetermined. Mark: a Series C that 'brings Clubhouse's valuation to $4 billion' (Voicebot.ai, 2021-04-19, after Reuters), as in the a16z row; older than 24 months (stale). Not Greylock's Clubhouse (the project tracker renamed Shortcut; ruled distinct) and not the Wikidata GB (disputed).",
    rounds=[rnd("2020-05", "Series A", 12000000, "Andreessen Horowitz", None, None),
            rnd("2021-01", "Series B", 100000000, "Andreessen Horowitz", None, None),
            rnd("2021-04", "Series C", None, "Andreessen Horowitz", None, "https://voicebot.ai/2021/04/19/clubhouse-closes-new-financing-at-4-billion-valuation/")]))

L.append(cls("revenuecat", status="private", country="US", city="San Francisco", focus="DevTools & APIs", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2020-08",
    stage_cite="https://news.crunchbase.com/startups/revenuecat-secures-15m-series-a-for-app-subscription-platform/",
    note="In-app subscription infrastructure (San Francisco). A Fund I position (Fortune, 2021-06-16); the $15M Series A of August 2020: 'Adjacent, SaaStr, Oakhouse Partners, Josh Buckley, Harry Stebbings, Nicolas Dessaigne and Tobi Balling also participated in the investment' (Crunchbase News, 2020-08-11), inside Fund I's life (decisions.md R1). Below $1B: the Series C priced it at $500M post-money (May 2025, as in the Bain Capital Ventures row).",
    rounds=[rnd("2020-08", "Series A", 15000000, None, True, "https://news.crunchbase.com/startups/revenuecat-secures-15m-series-a-for-app-subscription-platform/"),
            rnd("2025-05", "Series C", 50000000, "Bain Capital Ventures", None, None)]))

L.append(cls("spiketrap", status="acquired", country="US", city="San Francisco", focus="Media, Gaming & Advertising", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2020", flags=["stage_uncited"],
    note="Contextual AI for audience and ad analytics (San Francisco). One of the twelve investments made out of Fund I by July 2020 (TechCrunch, 2020-07-17). 'Spiketrap raised $3.5 million in a seed round in 2020 ... led by Susa, 645, Pathbreaker and Anorak' (TechCrunch, 2022-09-01), its only round, so the entry is that seed (model, low: no source names 20VC in it). 'Reddit acquires Spiketrap' (TechCrunch, 2022-09-01): acquired.",
    rounds=[rnd("2020", "seed", 3500000, "Susa Ventures, 645 Ventures, Pathbreaker, Anorak", None, "https://techcrunch.com/2022/09/01/reddit-acquires-contextualization-company-spiketrap-to-boost-its-ads-business/"),
            rnd("2022-09", "acquisition by Reddit", None, "Reddit", None, "https://techcrunch.com/2022/09/01/reddit-acquires-contextualization-company-spiketrap-to-boost-its-ads-business/")]))

L.append(cls("shoppinggives", status="acquired", country="US", city="Chicago", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2020-09",
    stage_cite="https://news.crunchbase.com/startups/startups-to-watch-finch-grin-zuper-shoppinggives/",
    note="Cause-based commerce platform for online retailers (ShoppingGives, Chicago). 'The Chicago-based startup raised $5.5 million in seed funding led by Caffeinated Capital and a group of investors that includes ... 20VC' (Crunchbase News, 2020-09-18). 'CPGIO ... has announced its acquisition of ShoppingGives' (PR Newswire, 2025-01-21): acquired.",
    rounds=[rnd("2020-09", "seed", 5500000, "Caffeinated Capital", True, "https://news.crunchbase.com/startups/startups-to-watch-finch-grin-zuper-shoppinggives/"),
            rnd("2025-01", "acquisition by CPGIO", None, "CPGIO", None, "https://www.prnewswire.com/news-releases/cpgio-expands-market-reach-with-shoppinggives-acquisition-and-strategic-leadership-appointment-302355666.html")]))

L.append(cls("pomelo", status="private", country="AR", city="Buenos Aires", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2021-05",
    stage_cite="https://techcrunch.com/2021/05/12/argentinas-pomelo-raises-9m-to-build-a-new-payments-infrastructure-for-latam-fintechs/",
    note="Card-issuing and payments infrastructure for Latin American fintechs (Buenos Aires). 'Pomelo ... has raised $9 million in a seed round of funding'; 'Index Ventures and Brazil's monashees co-led the funding round, which also included participation from ... 20VC' (TechCrunch, 2021-05-12). $55M Series C co-led by Kaszek and Insight Partners (January 2026, the Insight row).",
    rounds=[rnd("2021-05", "seed", 9000000, "Index Ventures, monashees", True, "https://techcrunch.com/2021/05/12/argentinas-pomelo-raises-9m-to-build-a-new-payments-infrastructure-for-latam-fintechs/"),
            rnd("2026-01", "Series C", 55000000, "Kaszek, Insight Partners", None, None)]))

L.append(cls("airlift", status="defunct", country="PK", city="Lahore", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2021-08",
    stage_cite="https://www.menabytes.com/airlift-series-b/",
    note="Quick-commerce and mass-transit startup (Lahore). The $85M Series B of August 2021 'was co-led by Harry Stebbings' 20 VC Explorer and Josh Buckley's Buckley Ventures' (MENAbytes, 2021-08-18; TechCrunch, 2021-08-17): Growth. Shut down in July 2022, as in the First Round row.",
    rounds=[rnd("2021-08", "Series B", 85000000, "20VC Explorer, Buckley Ventures", True, "https://www.menabytes.com/airlift-series-b/")]))

L.append(cls("polywork", status="defunct", country="US", city="New York", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2021-08",
    stage_cite="https://www.siliconrepublic.com/start-ups/polywork-series-a",
    note="Professional social network (Polywork, New York; founder Peter Johnston). The $13M Series A led by Andreessen Horowitz: 'Bungalow Capital and 20VC were among the other participants' (Silicon Republic, 2021-08-06; Business Insider lists Harry Stebbings among its angels). 'Stripe-backed Irish LinkedIn-challenger Polywork to close' (Business Post, 2024-12-31): defunct, as in the a16z row.",
    rounds=[rnd("2021-08", "Series A", 13000000, "Andreessen Horowitz", True, "https://www.siliconrepublic.com/start-ups/polywork-series-a"),
            rnd("2025-01", "shut down", None, None, None, "https://www.businesspost.ie/article/stripe-backed-irish-linkedin-challenger-polywork-to-close/")]))

L.append(cls("digits", status="private", country="US", city="San Francisco", focus="Fintech & Payments", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2022-03",
    stage_cite="https://techcrunch.com/2022/03/24/digits-books-65m-on-a-565m-valuation-to-bring-a-more-dynamic-automated-approach-to-legacy-accounting-tools/",
    note="Automated accounting and finance for small businesses (San Francisco). The $65M Series C at a $565M valuation: 'SoftBank's Vision Fund is leading the funding, with U.K. investor Harry Stebbings' 20VC Growth, GV and Benchmark also participating' (TechCrunch, 2022-03-24): Growth.",
    rounds=[rnd("2022-03", "Series C", 65000000, "SoftBank Vision Fund 2", True, "https://techcrunch.com/2022/03/24/digits-books-65m-on-a-565m-valuation-to-bring-a-more-dynamic-automated-approach-to-legacy-accounting-tools/")]))

L.append(cls("atlantic-money", status="acquired", country="GB", city="London", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2022-03",
    stage_cite="https://techfundingnews.com/founded-by-rohinhood-alumni-atlantic-money-takes-on-wise-paypal-picks-4-5m/",
    note="Low-cost international money transfer (London; founded by Robinhood alumni). The $4.5M seed: 'The round led by Amplo and Ribbit Capital alongside participation from Kleiner Perkins, Index Ventures ..., Harry Stebbings' 20VC, Elefund' (Tech Funding News, 2022-03-09). 'Deel has acquired international funds transfer company Atlantic Money' (Finovate, 2024-12-02): acquired, as in the Ribbit row.",
    rounds=[rnd("2022-03", "seed", 4500000, "Amplo, Ribbit Capital", True, "https://techfundingnews.com/founded-by-rohinhood-alumni-atlantic-money-takes-on-wise-paypal-picks-4-5m/"),
            rnd("2024-12", "acquisition by Deel", None, "Deel", None, "https://finovate.com/deel-acquires-atlantic-money-for-undisclosed-sum/")]))

L.append(cls("cycle", status="private", country="FR", city="Paris", focus="SaaS", rng="below_1b",
    stage=U, extra=NOSTAGE, entry_date="2022",
    note="Product-feedback hub for product teams (Cycle, from the eFounders studio). 'The company raised a total of $6 million across two funding rounds, including a recent funding round led by Boldstart that closed late last year ... Base Case, The 20VC Fund, SV Angel, BoxGroup, Hummingbird Ventures and 60 angels also invested' (TechCrunch, 2023-02-28): the article does not say which of the two rounds 20VC joined: undetermined. City from the studio's base (model).",
    rounds=[rnd("2022", "two rounds totalling $6M, the later led by Boldstart", 6000000, "Boldstart Ventures", True, "https://techcrunch.com/2023/02/28/cycle-is-a-new-product-management-hub-that-centralizes-all-customer-feedback/")]))

L.append(cls("noded-ai", status="private", country="US", focus="AI & Applied AI", rng="below_1b",
    stage=U, extra=NOSTAGE, entry_date="2024-07", flags=["city_unknown"],
    note="AI note-taking hub for work (Noded AI). 'Today's $4 million investment was led by Boldstart Ventures with participation from Bessemer Venture Partners, 20VC and First Hand Ventures' (TechCrunch, 2024-07-23); the article names no round: undetermined.",
    rounds=[rnd("2024-07", "unnamed round", 4000000, "Boldstart Ventures", True, "https://techcrunch.com/2024/07/23/noded-ai-wants-to-make-your-notes-the-center-of-your-work-world/")]))

L.append(cls("11x", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="medium", entry_date="2024-09",
    stage_cite="https://techcrunch.com/2024/09/16/ai-digital-employee-startup-11xai-raises-24m-led-by-benchmark/",
    note="AI sales agents ('digital workers'; 11x, founded in London, now San Francisco). The $24M Series A led by Benchmark: 'Other investors in the round included 20VC, Project A, Lux Capital, and SV Angel' (TechCrunch, 2024-09-16; Estadao's copy of the release adds 20Growth and 20Sales). Medium: whether 20VC was also in the 2023 seed is not stated. $50M Series B led by a16z (TechCrunch, 2024-09-30).",
    rounds=[rnd("2024-09", "Series A", 24000000, "Benchmark", True, "https://techcrunch.com/2024/09/16/ai-digital-employee-startup-11xai-raises-24m-led-by-benchmark/"),
            rnd("2024-09", "Series B", 50000000, "Andreessen Horowitz", None, "https://techcrunch.com/2024/09/30/11x-ai-a-developer-of-ai-sales-reps-has-raised-50m-series-b-led-by-a16z-sources-say/")]))

L.append(cls("archy", status="private", country="US", focus="Healthcare & Bio", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2024-10",
    stage_cite="https://hitconsultant.net/2024/10/23/archy-raises-15m-to-optimize-dental-practices-with-ai-powered-automation/",
    flags=["city_unknown"], extra={"hq_country_confidence": "low"},
    note="Cloud practice software for dental offices (Archy). '$15M Series A funding in a round led by Entree Capital with participation from Bessemer Venture Partners, CRV, Alven, 20VC Growth fund' (HIT Consultant, 2024-10-23; Pulse 2.0): the Explorer growth fund (decisions.md D1). No source read gives the HQ; US is a model read at low confidence.",
    rounds=[rnd("2024-10", "Series A", 15000000, "Entree Capital", True, "https://hitconsultant.net/2024/10/23/archy-raises-15m-to-optimize-dental-practices-with-ai-powered-automation/")]))

L.append(cls("bounce", status="private", country="US", city="San Francisco", focus="Consumer & Marketplaces", rng="below_1b",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2024-11",
    stage_cite="https://techcrunch.com/2024/11/12/bounce-grabs-19m-to-expand-its-traveller-convenience-network/",
    flags=["identity_homonym"],
    note="Luggage-storage network for travellers (San Francisco). 'Bounce's Series B was led by Sapphire Sport, with participation from existing investors including Andreessen Horowitz and General Catalyst, as well as new investors 20VC Growth, FJ Labs' (TechCrunch, 2024-11-12; $19M): Growth. Same company as the a16z and General Catalyst rows; not Accel's Bounce (the Bangalore scooter company; ruled distinct).",
    rounds=[rnd("2024-11", "Series B", 19000000, "Sapphire Sport", True, "https://techcrunch.com/2024/11/12/bounce-grabs-19m-to-expand-its-traveller-convenience-network/")]))

L.append(cls("orreco", status="private", country="IE", city="Galway", focus="Healthcare & Bio", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="AI performance science for elite athletes (Orreco, Galway). At the $4M round of December 2025: 'Existing investors include True Ventures, Jason Calacanis, 20VC and professional golfer Padraig Harrington' (Silicon Republic, 2025-12-15). No source says when or in which round 20VC entered: undetermined.",
    rounds=[rnd("2025-12", "round", 4000000, None, True, "https://www.siliconrepublic.com/business/mark-cuban-backs-galway-sports-tech-orreco-in-4m-raise")]))

L.append(cls("denki", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2026-03", flags=["stage_uncited"],
    note="Financial-audit automation (Denki, YC F25; 'San Francisco-based Denki', founded by two brothers who studied in London). 'Base10 Partners and Shine Capital co-led the raise, which included participation from Y Combinator, 20VC and others' (Crunchbase News, 2026-03-05, $4.1M); FinSMEs' headline calls it seed funding, but the page did not load, so the stage is model-sourced.",
    rounds=[rnd("2026-03", "seed", 4100000, "Base10 Partners, Shine Capital", True, "https://news.crunchbase.com/venture/yc-backed-denki-raise-financial-audit-automation-ai/")]))

L.append(cls("zalos", status="private", country="GB", city="London", focus="Fintech & Payments", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-03",
    stage_cite="https://tech.eu/2026/03/24/agents-for-finance-startup-zalos-raises-3-6m-to-transform-finance-departments/",
    note="AI agents for finance teams (Zalos, London and San Francisco; YC F25). '$3.6m in a seed funding round ... led by Swiss VC 14Peaks Capital'; 'Other investors include Cohen Circle, Harry Stebbings' 20VC and several angels' (Tech.eu, 2026-03-24).",
    rounds=[rnd("2026-03", "seed", 3600000, "14Peaks Capital", True, "https://tech.eu/2026/03/24/agents-for-finance-startup-zalos-raises-3-6m-to-transform-finance-departments/")]))

L.append(cls("lua", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-04",
    stage_cite="https://siliconangle.com/2026/04/16/lua-lands-5-8m-help-businesses-build-manage-ai-agent-workforces/",
    note="Operating system for human and AI-agent teams (Lua; 'Irish co-founded and London-based', Silicon Republic). 'Norrsken22 led the seed round. Flourish Ventures, 20VC, P1 Ventures, Phosphor Capital and Y Combinator also participated' (SiliconANGLE, 2026-04-16; $5.8M).",
    rounds=[rnd("2026-04", "seed", 5800000, "Norrsken22", True, "https://siliconangle.com/2026/04/16/lua-lands-5-8m-help-businesses-build-manage-ai-agent-workforces/")]))

L.append(cls("uplane", status="private", country="US", city="San Francisco", focus="Media, Gaming & Advertising", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-04",
    stage_cite="https://americanbazaaronline.com/2026/09/04/uplane-to-work-with-ag1-and-kalshi-to-replace-marketing-agencies-487603/",
    note="AI performance-marketing platform replacing agencies (Uplane, San Francisco; YC F25). 'The seed round was led by Play Ventures, with participation from Y Combinator, 20VC, Rebel Fund and Multimodal Ventures' (The American Bazaar, 2026-09-04; first reported by jawlah, 2026-04-19, $4.5M).",
    rounds=[rnd("2026-04", "seed", 4500000, "Play Ventures", True, "https://americanbazaaronline.com/2026/09/04/uplane-to-work-with-ag1-and-kalshi-to-replace-marketing-agencies-487603/")]))

L.append(cls("corvera", status="private", country="US", city="San Francisco", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-05",
    stage_cite="https://retailtechinnovationhub.com/home/2026/5/5/agentic-supply-chains-specialist-corvera-lands-3-million-in-seed-funding-to-scale-its-platform",
    note="Agentic supply-chain operations for consumer brands (Corvera, founded in London, 'based in San Francisco'; YC W26). 'GBP 3 million ($4.2 million) in seed funding ... led by 6 Degrees Capital, with participation from ... 20VC, Rebel Fund' (Retail Technology Innovation Hub, 2026-05-05).",
    rounds=[rnd("2026-05", "seed", 4200000, "6 Degrees Capital", True, "https://retailtechinnovationhub.com/home/2026/5/5/agentic-supply-chains-specialist-corvera-lands-3-million-in-seed-funding-to-scale-its-platform")]))

L.append(cls("moritz", status="private", country="US", city="San Francisco", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-05",
    stage_cite="https://www.law.com/legaltechnews/2026/05/05/mso-parlai-and-its-hybrid-law-firm-moritz-announce-9m-in-seed-funding/",
    note="AI-native law firm (Moritz, formerly Arcline; YC W26). 'San Francisco-based startup Moritz ... raised $9 million in a seed round through its MSO Parlai, led by startup incubator Y Combinator and venture capital fund 20VC' (Law.com, 2026-05-05; Tech Funding News the same day).",
    rounds=[rnd("2026-05", "seed", 9000000, "Y Combinator, 20VC", True, "https://www.law.com/legaltechnews/2026/05/05/mso-parlai-and-its-hybrid-law-firm-moritz-announce-9m-in-seed-funding/")]))

L.append(cls("prelude", status="private", country="FR", city="Paris", focus="Security", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2026-05",
    stage_cite="https://tech.eu/2026/05/20/20vc-leads-20m-series-a-investment-in-onboarding-startup-prelude/",
    flags=["identity_homonym", "model_disputes_source"],
    note="User verification and anti-fraud onboarding replacing CAPTCHAs and SMS codes (Prelude, Paris; founded by ex-Zenly engineers). 'French digital onboarding startup Prelude has raised $20m in a Series A funding round led by Harry Stebbings' 20VC, which is investing in the startup for the first time' (Tech.eu, 2026-05-20). Not Insight's Prelude (Seattle security control monitoring; ruled distinct) and not the Wikidata US (disputed).",
    rounds=[rnd("2026-05", "Series A", 20000000, "20VC", True, "https://tech.eu/2026/05/20/20vc-leads-20m-series-a-investment-in-onboarding-startup-prelude/")]))

L.append(cls("archastro", status="private", country="US", city="Seattle", focus="AI & Applied AI", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="medium", entry_date="2026-06",
    stage_cite="https://www.geekwire.com/2026/ex-stripe-microsoft-vets-launch-archastro/",
    note="Cross-company AI agents for enterprise software integration (ArchAstro, Seattle area; ex-Microsoft, Stripe and Meta engineers). 'pre-seed funding of $6.2 million from a marquee list of investors'; 'ArchAstro is backed by venture capital firms 20VC ... and Kyber Knight' (GeekWire, 2026-06-09). Medium: the article lists 20VC as a backer beside the pre-seed rather than inside a named round line.",
    rounds=[rnd("2026-06", "pre-seed", 6200000, None, True, "https://www.geekwire.com/2026/ex-stripe-microsoft-vets-launch-archastro/")]))

L.append(cls("archestra-ai", status="private", country="GB", city="London", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-06",
    stage_cite="https://tech.eu/2026/06/02/archestraai-raises-10m-to-unlock-next-gen-agentic-use-case/",
    note="Secure data access for enterprise AI agents (Archestra.AI, London; founded 2025 by Grafana Labs alumni). '$10m in a seed funding round, led by Harry Stebbings' 20VC, a new investor in the startup' (Tech.eu, 2026-06-02; $13.5M raised to date).",
    rounds=[rnd("2026-06", "seed", 10000000, "20VC", True, "https://tech.eu/2026/06/02/archestraai-raises-10m-to-unlock-next-gen-agentic-use-case/")]))

L.append(cls("fonio-ai", status="private", country="AT", city="Vienna", focus="AI & Applied AI", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-06",
    stage_cite="https://techfundingnews.com/fonio-ai-17m-20vc-austria-seed-round/",
    note="AI phone agents for small businesses (fonio.ai, Vienna). 'fonio.ai has closed a $17 million seed round at a $140 million valuation, led by 20VC' (Tech Funding News, 2026-06-09), six months after a EUR 3M angel round.",
    rounds=[rnd("2025-12", "angel round", None, None, None, None),
            rnd("2026-06", "seed", 17000000, "20VC", True, "https://techfundingnews.com/fonio-ai-17m-20vc-austria-seed-round/")]))

L.append(cls("theker", status="private", country="ES", city="Barcelona", focus="Industrial & Robotics", rng="below_1b",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="2026-06",
    stage_cite="https://www.cathaycapital.com/theker-raises-85m-in-europes-largest-ever-robotics-series-a-led-by-crv-with-backing-from-samsung-and-lvmh/",
    note="AI-native generalist robots for industrial production (THEKER, Barcelona). 'THEKER raises $85M in Europe's largest ever robotics Series A, led by CRV'; 'with participation from Samsung, LVMH, Cathay, 20VC, Henkel, Korelya, Sonae and Mercadona alongside existing investors Inditex' (Cathay Capital's post, 2026-06-11); 20VC is not among the existing investors named.",
    rounds=[rnd("2025", "seed", None, None, None, None),
            rnd("2026-06", "Series A", 85000000, "CRV", True, "https://www.cathaycapital.com/theker-raises-85m-in-europes-largest-ever-robotics-series-a-led-by-crv-with-backing-from-samsung-and-lvmh/")]))

# ---- the four firm-list rows
L.append(cls("xo-market", status="private", country="US", focus="Crypto & Web3", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2026-04",
    stage_cite="https://www.coindesk.com/business/2026/04/30/xo-market-bets-on-user-generated-prediction-markets-to-rival-polymarket-and-kalshi",
    flags=["city_unknown"], extra={"hq_country_confidence": "low"},
    note="User-generated prediction markets (XO Market; co-founders Ali Habbabeh and Walid Al Habboul). 'The startup, which just closed a $6 million seed round led by 20VC, Picus Capital, Coinbase Ventures, Venture Together and a group of angels' (CoinDesk, 2026-04-30); a $500K pre-seed of July 2025 names no 20VC. No source read gives an HQ (reports place the team in San Francisco, the CEO in Switzerland): US at low confidence.",
    rounds=[rnd("2025-07", "pre-seed", 500000, None, None, None),
            rnd("2026-04", "seed", 6000000, "20VC, Picus Capital, Coinbase Ventures", True, "https://www.coindesk.com/business/2026/04/30/xo-market-bets-on-user-generated-prediction-markets-to-rival-polymarket-and-kalshi")]))

L.append(cls("zekju", status="private", country="DE", city="Augsburg", focus="SaaS", rng="below_1b",
    stage="Seed", stage_src=W, stage_conf="high", entry_date="2024-09",
    stage_cite="https://www.taylorwessing.com/en/insights-and-events/news/media-centre/press-releases/2024/09/taylor-wessing-beraet-zekju-bei-seed-finanzierungsrunde",
    note="Messaging and document exchange between shippers, forwarders and truck drivers (ZeKju, Augsburg). 'Augsburg-based ZeKju GmbH has raised capital from investors including 20VC, Prequel Ventures, Combination Ventures and SDAC as part of its seed financing round' (Taylor Wessing, 2024-09-13); the company's own announcement called the round 'led by 20VC'.",
    rounds=[rnd("2024-09", "seed", None, "20VC", True, "https://www.taylorwessing.com/en/insights-and-events/news/media-centre/press-releases/2024/09/taylor-wessing-beraet-zekju-bei-seed-finanzierungsrunde")]))

L.append(cls("zero", status="private", country="FI", city="Helsinki", focus="SaaS", rng="below_1b",
    stage="Pre-Seed", stage_src=W, stage_conf="medium", entry_date="2024",
    stage_cite="https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-helsinkis-zero-raises-10-3-million-in-seed-round-led-by-primary-venture-partners/",
    flags=["model_disputes_source"],
    note="CRM (Zero, zero.inc, Helsinki). At the $10.3M seed led by Primary Venture Partners the founders thank 'the people who backed us at pre-seed, when there genuinely was nothing to look at: Kieran Hill, Harry Stebbings' (ArcticToday, 2026-09-15): 20VC's partners by name, dating the entry of a company the firm lists since 2024-09 (decisions.md R1). Helsinki, not the Wikidata JP (disputed).",
    rounds=[rnd("2024", "pre-seed", None, None, True, "https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-helsinkis-zero-raises-10-3-million-in-seed-round-led-by-primary-venture-partners/"),
            rnd("2026-09", "seed", 10300000, "Primary Venture Partners", None, "https://www.arctictoday.com/%F0%9F%87%AB%F0%9F%87%AE-helsinkis-zero-raises-10-3-million-in-seed-round-led-by-primary-venture-partners/")]))

L.append(cls("zml", status="private", country="FR", city="Paris", focus="AI & Applied AI", rng="below_1b",
    stage=U, extra=NOSTAGE,
    note="Inference framework running models across AI chips (ZML, Paris; founder Steeve Morin, ex-Zenly). 'Morin raised $20 million from venture firms including Harry Stebbings' 20VC, >commit, AALVC, Drysdale Ventures, Xavier Niel's Kima Ventures, Kindred Capital, LocalGlobe, and Puzzle Ventures' (TechCrunch, 2026-07-08): a total, not a round; the firm listed ZML by 2024-09, and no source names the round 20VC joined: undetermined.",
    rounds=[rnd("2026-07", "total raised to date", 20000000, None, True, "https://techcrunch.com/2026/07/08/hot-french-startup-zml-releases-free-product-to-speed-inference-across-lots-of-ai-chips/")]))

# ---- Nex Health: note re-recorded with the Fund I evidence
L.append(cls("nex-health",
    note="Patient-experience platform and healthcare API (NexHealth, San Francisco). One of the twelve investments made out of Fund I by July 2020: 'Nex Health and Spiketrap are the only two that are public so far' (TechCrunch, 2020-07-17), so the position is Fund I's, entered between April and July 2020; TechCrunch (2020-06-30) lists Harry Stebbings among the backers on $12 million raised by then. Neither article names the round (the 2020 round follows the September 2019 seed Point Nine led): undetermined. Mark: 'NexHealth Raises $125M Series C at $1B Valuation' (the company, 2022-04-21), as in the Point Nine row; older than 24 months (stale)."))

if __name__ == "__main__":
    jl.write("batch-003", L)
