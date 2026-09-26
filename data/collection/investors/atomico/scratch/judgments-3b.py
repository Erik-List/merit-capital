"""PRO-79 grind, batch-003 part b (teralytics .. callosum; research agent B,
citations re-fetched by verify-urls.py)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
INS = "https://atomico.com/insights/"

L = []
L.append(cls("teralytics", status="private", rng="below_1b", country="CH", city="Zurich",
             focus="Data Infrastructure", stage="undetermined",
             note="Mobility insights from telecom data (Zurich); Atomico was an investor by Sep 2017 ('Along with Niklas Zennstrom's Atomico fund, investors include Swiss VC firm Lakestar and Hong Kong-based Horizons Ventures', TechCrunch) and an existing investor in the Aug 2019 $17.5M round led by Bosch (the company's release); the entry round (CMS year 2016) is unnamed on every surface; Bentley Systems invested 2022; still operating",
             rounds=[rnd("2019-08", "unnamed", 17500000, "Robert Bosch Venture Capital", True, "https://teralytics.net/teralytics-raises-17-5-million-to-improve-human-mobility-worldwide/", "company")]))
L.append(cls("testgorilla", status="private", rng="below_1b", country="NL", city="Amsterdam",
             focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.testgorilla.com/blog/testgorilla-secures-70m-series-a-funding-to-help-companies-eliminate-hiring-bias/",
             note="Pre-employment skills testing; 'TestGorilla has secured $70m in Series A funding, co-led by the London-based venture capital firms Atomico and Balderton Capital' (the company's release, Jun 2022; the firm's own post; Luca Eisenstecken to the board); Atomico was not in the earlier Notion/Partech rounds",
             rounds=[rnd("2022-06-14", "Series A", 70000000, "Atomico; Balderton", True, "https://www.testgorilla.com/blog/testgorilla-secures-70m-series-a-funding-to-help-companies-eliminate-hiring-bias/", "company")]))
L.append(cls("the-climate-corporation", rng="below_1b", city="San Francisco",
             stage="Series A", stage_src="model", stage_conf="medium", flags=["stage_disputes_band"],
             note="Weather insurance, then farm data (WeatherBill until 2011; co-founded 2006 by David Friedberg and Siraj Khaliq, later an Atomico partner); 'Skype founder Niklas Zennstrom (through his Atomico fund)' joined the company's first outside round, Jan 2007 (TechCrunch, size undisclosed), and followed in the Oct 2007 $12.5M round TechCrunch names the Series B - so the Jan 2007 entry was the Series A; the Form D band read the 2011 filing, where Khaliq sits as the company's own officer, as a Growth entry (overridden); acquired by Monsanto Oct 2013 ($930M headline) -> acquired, as Felicis, First Round and Khosla record",
             rounds=[rnd("2007-01-15", "first outside round (the Series A by sequence)", None, None, True, "https://techcrunch.com/2007/01/15/weatherbill-launches-announces-all-star-investors/"),
                     rnd("2007-10-17", "Series B", 12500000, "NEA; Index Ventures", True, "https://techcrunch.com/2007/10/17/an-interesting-bet-weatherbill-takes-125-million-series-b/")]))
L.append(cls("travelperk", status="private", rng="1b_plus", usd=2700000000, val_src="web_verified", asof="2025-01-28",
             val_cite="https://www.cnbc.com/2025/01/28/softbank-backed-travelperk-doubles-valuation-plans-fintech-push.html",
             val_conf="high", country="US", city="Boston", focus="SaaS",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://eqtgroup.com/news/eqt-co-leads-travelperks-usd-200-million-series-e",
             note="Business travel and spend management (renamed Perk in Nov 2025, with dual headquarters in Boston and London; founded in Barcelona); Atomico co-led the $200M Series E of Jan 2025 with EQT Growth (EQT; the firm's own post: 'leading this $200m Series E'; Hillary Ball on the board) at a $2.7B valuation (CNBC) - Atomico's first round",
             rounds=[rnd("2025-01-28", "Series E", 200000000, "Atomico; EQT Growth", True, "https://eqtgroup.com/news/eqt-co-leads-travelperks-usd-200-million-series-e")]))
L.append(cls("truecaller", status="public", rng="below_1b", usd=690000000, val_src="web_verified", asof="2026-09-25",
             val_cite="https://companiesmarketcap.com/truecaller/marketcap/", val_conf="high",
             country="SE", city="Stockholm", focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2014/10/08/confirmed-truecaller-scores-60-million-in-series-c-from-kpcb-atomico-and-sequoia",
             note="Caller ID and spam blocking; 'a $60 million in Series C led by Atomico, Kleiner Perkins Caufield & Byers, and Sequoia Capital' (TechCrunch, Oct 2014; Atomico was not in the Feb 2014 Series B); Nasdaq Stockholm IPO Oct 2021 at about SEK 19.4bn; market cap ~$0.69B in Sep 2026 (companiesmarketcap) -> public, below $1B today",
             rounds=[rnd("2014-10-08", "Series C", 60000000, "Atomico; KPCB; Sequoia", True, "https://techcrunch.com/2014/10/08/confirmed-truecaller-scores-60-million-in-series-c-from-kpcb-atomico-and-sequoia")]))
L.append(cls("uniplaces", status="private", rng="below_1b", country="PT", city="Lisbon",
             focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.cgd.pt/English/Institutional/News/Pages/Atomico-and-Caixa-Capital-invest-in-Uniplaces.aspx",
             note="Student accommodation marketplace (Lisbon; London-registered, register seats for Ljungman, Wass, Blume 2015-2020); 'raised a $24 million series A, led by Atomico with Caixa Capital as co-investor' (the co-investor's release, Nov 2015; the firm's own post, dated Nov 2016 on the migrated site, says the same: 'leading the company's $24 million Series A') - the date conflict does not touch the round; still operating 2026",
             rounds=[rnd("2015-11-03", "Series A", 24000000, "Atomico", True, "https://www.cgd.pt/English/Institutional/News/Pages/Atomico-and-Caixa-Capital-invest-in-Uniplaces.aspx")]))
L.append(cls("upside-foods", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2022-04-21",
             val_cite="https://www.prnewswire.com/news-releases/upside-foods-raises-a-400m-series-c-round-to-commercialize-cultivated-meat-at-scale-301529998.html",
             val_conf="medium", country="US", city="Berkeley", focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://venturebeat.com/entrepreneur/lab-grown-meat-startup-memphis-meats-raises-17-million-from-dfj-cargill-bill-gates-richard-branson-others",
             flags=["stale"],
             note="Cultivated meat (Memphis Meats until May 2021); 'Leading the $17 million series A round was venture capital (VC) firm DFJ', with 'European VC giant Atomico' among the investors (VentureBeat, Aug 2017; the firm's own post); the $400M Series C of Apr 2022 'places the company's valuation at over $1 billion' (the company's release) - the floor of a stated figure, stale; layoffs 2024-2025 are not collapse evidence under COLLECTION.md 6",
             rounds=[rnd("2017-08-23", "Series A", 17000000, "DFJ", True, "https://venturebeat.com/entrepreneur/lab-grown-meat-startup-memphis-meats-raises-17-million-from-dfj-cargill-bill-gates-richard-branson-others"),
                     rnd("2022-04-21", "Series C", 400000000, "Temasek; Abu Dhabi Growth Fund", None, "https://www.prnewswire.com/news-releases/upside-foods-raises-a-400m-series-c-round-to-commercialize-cultivated-meat-at-scale-301529998.html", "company")]))
L.append(cls("vaayu", status="acquired", rng="below_1b", country="DE", city="Berlin",
             focus="Climate & Energy",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.vaayu.tech/press-releases/climate-tech-start-up-vaayu-raises-11-5-million-in-funding-round-led-by-atomico",
             entry_date="2022-04-20",
             note="Carbon measurement for retailers; 'has closed an $11.5 million seed funding round led by Atomico' (the company's release, Apr 2022; the firm's own post: 'the very first company that we have invested in following earlier investment from the Atomico Angel Programme' - the Angel Programme's Jul 2021 pre-seed cheque is not the fund entry, decisions.md D3); acquired by Carbonfact May 2026 (ESG Today); graduation decided in the S2A pass",
             rounds=[rnd("2022-04-20", "Seed", 11500000, "Atomico", True, "https://www.vaayu.tech/press-releases/climate-tech-start-up-vaayu-raises-11-5-million-in-funding-round-led-by-atomico", "company")]))
L.append(cls("varjo", status="private", rng="below_1b", country="FI", city="Helsinki",
             focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://varjo.com/news/varjo-raises-31m-series-b-from-atomico-to-transform-heavy-industry-with-worlds-first-human-eye-resolution-vr-product",
             note="Human-eye-resolution VR/XR headsets; 'Varjo Raises $31m Series B from Atomico' (the company's release, Oct 2018; Atomico was not in the EQT/Lifeline Series A); Atomico followed in the $40M Series D of Sep 2022; no valuation disclosed",
             rounds=[rnd("2018-10-08", "Series B", 31000000, "Atomico", True, "https://varjo.com/news/varjo-raises-31m-series-b-from-atomico-to-transform-heavy-industry-with-worlds-first-human-eye-resolution-vr-product", "company")]))
L.append(cls("vay", status="private", rng="below_1b", country="DE", city="Berlin",
             focus="Industrial & Robotics",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://vay.io/press-release/vay-raises-95m-series-b-round-becomes-highest-funded-startup-in-europe-to-pursue-self-driving-car-technology/",
             note="Teledriven car rental (Ree Technology GmbH until 2021, merged in from the 2020 listing); 'Niall Wass, board member at Vay since Atomico led the company's Series A round' (Vay's own release, Dec 2021; deutsche-startups, Jun 2019: Atomico and Creandum put about EUR 10M into Ree Technology); existing investor in the $95M Series B; Grab's strategic investment Nov 2025; aligned with Creandum's row",
             rounds=[rnd("2019-06-17", "Series A", None, "Atomico", True, "https://www.deutsche-startups.de/2019/06/17/dealmonitor-17-06-2019/"),
                     rnd("2021-12-14", "Series B", 95000000, None, True, "https://vay.io/press-release/vay-raises-95m-series-b-round-becomes-highest-funded-startup-in-europe-to-pursue-self-driving-car-technology/", "company")]))
L.append(cls("viagogo", status="public", rng="1b_plus", usd=2080000000, val_src="web_verified", asof="2026-09-25",
             val_cite="https://stockanalysis.com/stocks/stub/market-cap/", val_conf="medium",
             country="US", city="New York", focus="Consumer & Marketplaces", flags=["cite_pending"],
             note="Ticket resale (founded London 2006 by Eric Baker); on the firm's 2007-2012 listings and CMS (Stage Growth), but no source names Atomico's round (TechCrunch's 2009 round names Index, Arnault, Kloiber, Rothschild); viagogo bought StubHub in Feb 2020 and both are owned by StubHub Holdings, NYSE-listed Sep 2025 - the company is public through its parent, market cap $2.08B on 2026-09-25 (StockAnalysis); stage waits on the site-label score"))
L.append(cls("wellhub", status="private", rng="1b_plus", usd=2400000000, val_src="web_verified", asof="2023-08-23",
             val_cite="https://www.prnewswire.com/news-releases/gympass-raises-85-million-in-series-f-funding-at-2-4-billion-valuation-strengthens-position-as-the-leading-global-corporate-wellness-platform-301907492.html",
             val_conf="high", city="New York", focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite=INS + "rethinking-employee-wellness-models-atomicos-investment-in-pelago",
             flags=["stage_disputes_band", "stale"],
             note="Corporate wellness (Gympass until 2024; founded Sao Paulo, now New York); the firm's own 2021 post counts it among the companies it has worked with 'since Series A' (CMS year 2015; Hillary Ball on the board) - the Series A itself is undated in press, hence medium; the Form D band's Seed rests on a 2021 US subsidiary filing (overridden); $85M Series F at $2.4B Aug 2023 (the company's release) is the last priced mark, stale"))
L.append(cls("wolt", rng="below_1b", city="Helsinki",
             stage="undetermined",
             note="Food delivery (Helsinki); the firm's CMS files Wolt at 2016 with Zennstrom as investment lead (Exited), but the only round press, the EUR 10M round of Apr 2016 led by EQT Ventures, names 'Skype founder Niklas Zennstrom' beside Ilkka Paananen and Risto Siilasmaa as individuals (ArcticStartup), and the 2019 round's investor list names neither - kept a member on the firm's own listing, flagged as possibly a personal position (decisions.md ruling 15); acquired by DoorDash 2022 -> acquired",
             rounds=[rnd("2016-04-15", "unnamed", 11000000, "EQT Ventures", True, "https://arcticstartup.com/finnish-foodtech-startup-wolt-announces-raising-11-million-2/")]))
L.append(verdict("wolt", "member",
                 "The firm's own CMS lists Wolt (2016, investment lead Niklas Zennstrom, Exited) and a 2023 firm post counts it among its early investments: a site listing suffices (COLLECTION.md 1). Open (decisions.md ruling 15): the only round press names Zennstrom beside other individual angels, so the position may be personal (D2 would put it out)",
                 "site_listing", "medium", "https://atomico.com/partners/wolt"))
L.append(cls("wonder-studios", status="private", rng="below_1b", country="GB", city="London",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://sifted.eu/articles/wonder-ai-movie-studio-atomico-localglobe",
             entry_date="2025-10-23", grad="censored",
             note="AI-native film studio; 'AI movie studio Wonder raises $12m seed round led by Atomico' (Sifted, Oct 2025; UKTN: $12M / GBP 9M with LocalGlobe and Blackbird following; Ben Blume lead); censored",
             rounds=[rnd("2025-10-23", "Seed", 12000000, "Atomico", True, "https://sifted.eu/articles/wonder-ai-movie-studio-atomico-localglobe")]))
L.append(cls("xobni", status="acquired", rng="below_1b", city="San Francisco",
             focus="SaaS", stage="undetermined",
             note="Email and contacts add-in (Xobni, 'inbox' backwards); 'In March 2007, Xobni raised US$4.26 million from Vinod Khosla, First Round Capital, and Atomico' (Wikipedia; its GigaOM source is gone, and the round is unnamed) -> undetermined; acquired by Yahoo Jul 2013 for more than $60M (TechCrunch, which names Atomico among the backers)",
             rounds=[rnd("2007-03", "unnamed", 4260000, None, True, "https://en.wikipedia.org/wiki/Xobni")]))
L.append(cls("y42", status="private", rng="below_1b", country="DE", city="Berlin",
             focus="Data Infrastructure",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2021/10/25/data-platform-y42-raises-31m/",
             note="Low-code data platform; 'raised a $31 million Series A funding round co-led by Atomico and Insight Partners' (TechCrunch, Oct 2021; the firm's own post); no later round; operating (live site, 2025)",
             rounds=[rnd("2021-10-25", "Series A", 31000000, "Atomico; Insight Partners", True, "https://techcrunch.com/2021/10/25/data-platform-y42-raises-31m/")]))
L.append(cls("zapp", status="private", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Quick-commerce delivery (London, 2020); Atomico was an investor in the $100M raised by Aug 2021 ('from various investors like Lightspeed, Atomico, 468 Capital, and Burda', UK Tech News) and joined by the Jan 2022 $200M Series B; the Mar 2021 round is unnamed -> undetermined; heavy cuts 2024, still trading Oct 2025",
             rounds=[rnd("2021-03", "unnamed", 100000000, None, True, "https://www.uktech.news/news/londons-online-grocery-service-zapp-zooms-to-manchester-20210803"),
                     rnd("2022-01-31", "Series B", 200000000, "Lightspeed; 468 Capital; BroadLight", True, "https://www.uktechnews.info/2022/01/31/quick-commerce-t-a-zapp-secures-149-million-series-b-investment-led-by-lightspeed-468-capital-and-broadlight-capital/")]))
L.append(cls("zocdoc", status="private", rng="1b_plus", usd=1800000000, val_src="web_verified", asof="2015-08-20",
             val_cite="https://www.healthcaredive.com/news/new-zocdoc-funding-raises-value-to-18b/404422/",
             val_conf="high", city="New York", focus="Healthcare & Bio",
             flags=["stale", "cite_pending"], clear=["unicorn_name_match"],
             note="Doctor-booking marketplace (New York); 'The funding round was led by Baillie Gifford and Atomico' - the $130M round of Aug 2015 at $1.8B (Healthcare Dive; WSJ; the firm's own post), unnamed in every source; Francisco Partners' $150M of Feb 2021 disclosed no price, so the 2015 mark stands, stale; stage waits on the site-label score",
             rounds=[rnd("2015-08-20", "unnamed", 130000000, "Baillie Gifford; Atomico", True, "https://www.healthcaredive.com/news/new-zocdoc-funding-raises-value-to-18b/404422/")]))
L.append(cls("ashby", status="private", rng="below_1b", country="US", city="San Francisco",
             focus="SaaS", stage="undetermined",
             note="Recruiting software (ashbyhq.com); only on the firm's job board (careers.atomico.com), and the press for every Ashby round (F-Prime's 2022 Series B, Alkeon's 2025 Series D) omits Atomico - kept a member on the board listing (decisions.md D11), flagged as the one board-only row nothing corroborates (ruling 16); no priced valuation disclosed"))
L.append(verdict("ashby", "member",
                 "Listed on the firm's own job board careers.atomico.com (decisions.md D11: a first-party list surface); 13 of the board's 14 board-only companies are corroborated by the firm's posts or press, Ashby is the one that is not - open (ruling 16)",
                 "site_listing", "medium", "https://careers.atomico.com/companies/ashby"))
L.append(cls("bebestore", status="unknown", rng="below_1b", country="BR", city="São Paulo",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Online baby-products retailer (Bebe Store, Brazil); the firm's first Brazil deals (Dec 2011 / Feb 2012 release: 'US$2.9m in Bebe Store') made it the first outside investor, round unnamed; followed with W7 Brazil Capital in a $10M round (Mar 2013) and led $12.3M in 2014; bought rival Baby 2014; no news since and the domain no longer resolves, but no shutdown source -> status unknown",
             rounds=[rnd("2011-12", "unnamed", 2900000, "Atomico", True, INS + "atomico-announces-first-investments-in-brazil", "firm"),
                     rnd("2013-03-26", "unnamed", 10000000, None, True, INS + "w7-and-atomico-invest-dollar10m-in-bebe-store", "firm")]))
L.append(cls("betable", status="private", rng="below_1b", city="London",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://en.wikipedia.org/wiki/Betable",
             entry_date="2010-07-22",
             grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite="http://allthingsd.com/20131105/real-money-gaming-platform-betable-raises-18-5-million/",
             note="Real-money gaming platform (Christopher Griffin, London); 'In July 2010 the company raised $3 million in seed funding from Atomico Ventures' (Wikipedia, citing TechCrunch: 'the first company selected for Atomico Ventures II fund'); 'In November 2013, Betable raised an $18.5 million Series A funding round led by Venture51' (Wikipedia; AllThingsD) = graduation; operating as a B2B iGaming platform 2026",
             rounds=[rnd("2010-07-22", "Seed", 3000000, "Atomico", True, "https://techcrunch.com/2010/07/22/betable-secures-3-million-to-become-the-twitter-for-betting/"),
                     rnd("2013-11-05", "Series A", 18500000, "Venture51", None, "http://allthingsd.com/20131105/real-money-gaming-platform-betable-raises-18-5-million/")]))
L.append(cls("callosum", status="private", rng="below_1b", country="GB", city="London",
             focus="AI & Applied AI",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.siliconrepublic.com/start-ups/uk-ai-start-up-callosum-secures-100m-seed-funding-round",
             entry_date="2026-08-20", grad="censored",
             note="Software that routes AI workloads to the best-fit models and chips (Danyal Akarca, Jascha Achterberg); the $100M seed of Aug 2026 led by Atomico with the UK Sovereign AI Fund, Plural and DCVC (Silicon Republic; the firm's own post 'Our investment in Callosum'); Atomico was not in Plural's Feb 2026 round; censored",
             rounds=[rnd("2026-08-20", "Seed", 100000000, "Atomico", True, "https://www.siliconrepublic.com/start-ups/uk-ai-start-up-callosum-secures-100m-seed-funding-round")]))

if __name__ == "__main__":
    jl.write("batch-003b", L)
