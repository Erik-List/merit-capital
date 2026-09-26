"""PRO-79 grind, batch-004 part b: listing-era companies (research agent D,
citations re-fetched by verify-urls.py). ree-technology merges into vay and
hem into fab at the rebuild (identity-merges.json)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd

L = []
L.append(cls("memolane", status="defunct", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Social-media 'digital memory' timeline (born at Startup Weekend Copenhagen); 'raised a $2 million funding round led by August Capital and Atomico' (TechCrunch, Sep 2010; the firm's 2011 fund-II page: 'Atomico co-invested in this deal with August Capital') - the round is unnamed; service and accounts deleted 2013-02-22 with the team joining an unnamed company -> defunct (the acqui-hire rule)",
             rounds=[rnd("2010-09-13", "unnamed", 2000000, "August Capital; Atomico", True, "https://techcrunch.com/2010/09/13/memolane-raises-2-million-to-become-your-digital-memory/")]))
L.append(cls("mydeco", status="defunct", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Online interior-design marketplace (Brent Hoberman); Atomico is named in the launch investor list beside lead SPARK Ventures (TechCrunch, Feb 2008), the 2007 round that Growth Business calls 'seed' and Global Venturing 'series A' - the name conflicts -> undetermined; the site wound down and redirected to Made.com before Monoqi bought its old assets in Jan 2015 (TechCrunch) -> defunct",
             rounds=[rnd("2007", "conflicting (seed / series A)", None, "SPARK Ventures", True, "https://techcrunch.com/2008/02/04/mydeco-launches-assault-on-the-home-front/")]))
L.append(cls("ofo", status="defunct", rng="below_1b", country="CN", city="Beijing",
             focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.chinatravelnews.com/article/112439",
             note="Dockless bike sharing (Beijing); the $450M Series D of Mar 2017 led by DST: 'other investors include Didi Chuxing, CITIC Private Equity Funds, Matrix Partners China, Coatue, Atomico and Macrolink Group' (ChinaTravelNews; the firm's own post 'Our investment in ofo'); debt crisis from Dec 2018, no longer operating bike rentals by 2020 (Wikipedia) -> defunct",
             rounds=[rnd("2017-03-01", "Series D", 450000000, "DST Global", True, "https://www.chinatravelnews.com/article/112439")]))
L.append(cls("ostrovok", status="private", rng="below_1b", country="RU", city="Moscow",
             focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.prnewswire.com/news-releases/ostrovok-russias-fastest-growing-online-travel-company-secures-136-million-in-funding-125408323.html",
             note="Hotel booking (Serge Faguet, Kirill Makharinsky); the $13.6M Series A of Jul 2011 'led by General Catalyst Partners and Accel Partners' lists 'Niklas Zennstrom and Atomico (Skype)' among the investors (the company's release; Wikipedia: 'Niklas Zennstrom and Atomico Ventures'); operating, owned by Emerging Travel Group (Interfax, 2026)",
             rounds=[rnd("2011-07-12", "Series A", 13600000, "General Catalyst; Accel", True, "https://www.prnewswire.com/news-releases/ostrovok-russias-fastest-growing-online-travel-company-secures-136-million-in-funding-125408323.html", "company")]))
L.append(cls("playfire", status="acquired", rng="below_1b", country="GB", city="London",
             focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2009/11/10/confirmed-gamer-social-network-playfire-secures-2-1m-series-a/",
             note="Social network for gamers; 'The round was led by Atomico Ventures' - the $2.1M (GBP 1.3M) Series A of Nov 2009 (TechCrunch; Ljungman director 2009-2012, register); the 2008 seed was angels only; acquired by Green Man Gaming 2012-07-09 (Wikipedia)",
             rounds=[rnd("2009-11-10", "Series A", 2100000, "Atomico", True, "https://techcrunch.com/2009/11/10/confirmed-gamer-social-network-playfire-secures-2-1m-series-a/")]))
L.append(cls("powerreviews", status="acquired", rng="below_1b", city="Chicago",
             focus="SaaS", stage="undetermined",
             note="Ratings-and-reviews software for retailers (founded 2005); on the firm's 2008-2012 listings, but no press names Atomico in any round (2005 A: Menlo, Draper Richards; 2007 $15M: Lehman, Menlo; 2010-2011 rounds) - an unannounced or secondary position, undated -> undetermined; acquired by Bazaarvoice 2012 (TechCrunch), later sold on (Viewpoints 2014, 1WorldSync 2023)"))
L.append(cls("restorando", status="acquired", rng="below_1b", country="AR", city="Buenos Aires",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Restaurant reservations for Latin America; 'Atomico Leads Investment Round for Restorando.com' (LAVCA, Apr 2011: $500K with Kaszek) - the entry, unnamed, before the $3.2M Series A of Feb 2012 led by Emergence (the firm's own release) -> undetermined (the ankar reading); acquired by TheFork (TripAdvisor) 2019 (LatAm List)",
             rounds=[rnd("2011-04-19", "unnamed", 500000, "Atomico", True, "https://www.lavca.org/atomico-leads-investment-round-for-restorando-com/"),
                     rnd("2012-02-22", "Series A", 3200000, "Emergence Capital Partners", True, "https://www.globenewswire.com/en/news-release/2012/02/22/1217385/0/en/Brazil-s-Restorando-Closes-3-2M-Series-A-Round-Led-by-Emergence-Capital-Partners.html", "company")]))
L.append(cls("seesmic", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2008/02/14/seesmic-announces-6-million-series-a-round",
             note="Video conversations, then social-media clients (Loic Le Meur); the '$6 million Series A round of funding' of Feb 2008 led by Atomico (TechCrunch; Wikipedia: 'the primary one being Atomico'); acquired by HootSuite Sep 2012",
             rounds=[rnd("2008-02-14", "Series A", 6000000, "Atomico", True, "https://techcrunch.com/2008/02/14/seesmic-announces-6-million-series-a-round")]))
L.append(cls("siine", status="defunct", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2011/02/11/siine-lands-550000-aims-to-change-the-way-we-type-on-touch-screen-keyboards",
             entry_date="2011-02-11",
             note="Icon-based predictive keyboard (Ed Maklouf, London/Barcelona); 'has raised GBP 550,000 (roughly $880,000) in seed funding from Atomico Ventures' (TechCrunch, Feb 2011); no later round found; Siine Ltd dissolved 2018-12-11 (register) -> defunct; graduation decided in the S2A pass",
             rounds=[rnd("2011-02-11", "Seed", 880000, "Atomico", True, "https://techcrunch.com/2011/02/11/siine-lands-550000-aims-to-change-the-way-we-type-on-touch-screen-keyboards")]))
L.append(cls("silk", status="defunct", rng="below_1b", country="NL", city="Amsterdam",
             focus="SaaS",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2011/05/18/silk-scores-seed-funding-from-atomico-others-for-content-crunching-platform/",
             entry_date="2011-05-18",
             note="Structured-data publishing (silk.co, Amsterdam); 'Silk announced it has completed a EUR 320,000 ($475,000) funding round led by Atomico' (TNW; TechCrunch: 'Silk Scores Seed Funding From Atomico'); the next round, NEA's $1.6M of Aug 2012, is also named a seed and no Series A followed; Palantir's 2016 deal was an acqui-hire with silk.co frozen -> defunct (the acqui-hire rule); graduation decided in the S2A pass",
             rounds=[rnd("2011-05-18", "Seed", 475000, "Atomico", True, "https://thenextweb.com/news/the-tnw-startup-rally-winner-silk-gets-funded-by-atomico"),
                     rnd("2012-08-01", "Seed", 1600000, "NEA", True, "https://techcrunch.com/2012/08/01/content-crunching-app-silk-raises-1-6-million-seed-round/")]))
L.append(cls("technorati", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Blog search, later a publisher ad platform (Dave Sifry); on the firm's 2008-2012 listings, but no press names Atomico in any round (2006 C: DFJ, Mobius; 2008 D; 2009 extension) - an unannounced or secondary position -> undetermined; acquired by Synacor Feb 2016 for $3M (SiliconANGLE)"))
L.append(cls("trialpay", status="acquired", rng="below_1b", city="Mountain View",
             focus="Fintech & Payments",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://globalventuring.com/blog/2012/02/03/visa-judges-promise-in-trialpay/",
             note="Transactional advertising / alternative payments; 'TrialPay raised $12.7m in its February 2008 series B round, receiving funding from VC firms Index Ventures, Atomico and Battery Ventures' (Global Venturing); the 2007 A was Battery and angels; acquired by Visa Feb 2015",
             rounds=[rnd("2008-02", "Series B", 12700000, None, True, "https://globalventuring.com/blog/2012/02/03/visa-judges-promise-in-trialpay/")]))
L.append(cls("woome", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Video speed-dating / live video chat (Woo Media, Stephen Stokols); 'We got funded by Niklas Zennstrom and Atomico, his investment vehicle' (socaltech, Nov 2007) - about $5M before Jun 2008 with Mangrove, unnamed and undated; Index led the $12M second round Jun 2008 (CBS); acquired by Zoosk Nov 2011 (Wikipedia)",
             rounds=[rnd("2007", "unnamed", None, None, True, "https://www.socaltech.com/interview_with_stephen_stokols_woome/s-0012130.html"),
                     rnd("2008-06-13", "unnamed (second round)", 12000000, "Index Ventures", None, "https://www.cbsnews.com/news/video-dater-woome-raises-125-million-second-round/")]))
L.append(cls("wrapp", status="acquired", rng="below_1b", country="SE", city="Stockholm",
             focus="Fintech & Payments",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2011/11/14/skype-co-founder-leads-5-5m-round-in-social-gifting-service-wrapp/",
             note="Social gifting, later card-linked rewards; '$5.5 million in Series A funding ... led by Atomico' (TechCrunch, Nov 2011; Zennstrom to the board; Creandum's seed came earlier); the firm's 2013 release 'Wrapp raises $15m Series B'; acquired by Meniga Jan 2019 (Finovate), as Creandum and Greylock record",
             rounds=[rnd("2011-11-14", "Series A", 5500000, "Atomico", True, "https://techcrunch.com/2011/11/14/skype-co-founder-leads-5-5m-round-in-social-gifting-service-wrapp/")]))
L.append(cls("wunderloop", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
             flags=["identity_unresolved"],
             note="Listed on the firm's 2008-2011 sites (rendered 'wunderLOOP'; its own page /OurPortfolio/wunderLOOP.xml is in the CDX but the Internet Archive refused this machine before it could be read); no press, Wikipedia or register record identifies the company -> undetermined in every outcome column, excluded from every metric"))
L.append(cls("zattikka", status="defunct", rng="below_1b", country="GB", city="London",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Social/casual games group (Zattikka Ltd 2007; Zattikka PLC on AIM 2012, per the firm's own 2012 page); the register dates the position: Zattikka Ltd's annual return to 2009-09-26 lists Atomico Management Limited with 5,333 C ORDINARY shares (transferred 2010-06-24) - no round word; administration Aug 2013 (Game Developer), the PLC dissolved 2019 -> defunct"))

if __name__ == "__main__":
    jl.write("batch-004b", L)
