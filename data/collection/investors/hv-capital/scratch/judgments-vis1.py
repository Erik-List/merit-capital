"""Visible slice (PRO-104): the public, $1B+ and consideration rows, from the research pass of 2026-09-29."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT  # noqa: E402

L = []


def geo(slug):
    c, ci, cite = hq(slug)
    return dict(country=c, country_cite=cite, city=ci)


SA = "https://stockanalysis.com/quote/etr/"
ASOF = "2026-09-29"

# --- public ---------------------------------------------------------------
L.append(cls("delivery-hero", status="public", rng="10b_plus", usd=12_604_050_000, val_src="web_verified",
             val_cite=SA + "DHER/", asof=ASOF, stage="undetermined", entry_date="2012-04",
             focus="Consumer & Marketplaces", **geo("delivery-hero"),
             note="Online food delivery, Berlin (Frankfurt: DHER, IPO 2017). HV reached Delivery Hero through Lieferheld: "
                  "HV and Team Europe gave Lieferheld EUR 1M start capital (2010) and joined its EUR 4M round of spring "
                  "2011 (deutsche-startups, 2011-11-16); Delivery Hero took over Lieferheld in Feb 2012 and 'the "
                  "previous Lieferheld shareholders now receive shares in Delivery Hero' (deutsche-startups, 2012-02-28), "
                  "which is sale consideration (D4). HV then put new money into Delivery Hero itself in the ~EUR 25M "
                  "round of April 2012 (The Next Web, 2012-04-02, names Holtzbrinck Ventures; Focus had reported the "
                  "round with Holtzbrinck among the investors), so the row is a member on that entry; that round is not "
                  "named as a series, so the stage is undetermined. Lieferheld is its own row (acquired, 2012). "
                  "Market cap EUR 11.10B (stockanalysis, 2026-09-29) @ ECB 2026-09-29 (EUR/USD 1.1355) = $12.60B. "
                  "Uber's takeover offer (~$14.8B) is board-backed but has not closed, so the status stays public.",
             rounds=[rnd("2011-11-16", None, None, None, False,
                         "https://www.deutsche-startups.de/2011/11/16/lieferheld-delivery-hero-finanzierung/"),
                     rnd("2012-04-02", None, None, None, True,
                         "https://thenextweb.com/news/hot-berlin-startup-delivery-hero-raises-e25m-expands-online-food-ordering-business-through-acquisitions")],
             extra={"status_citation": SA + "DHER/"}))
L.append(cls("zalando", status="public", rng="1b_plus", usd=5_972_730_000, val_src="web_verified",
             val_cite=SA + "ZAL/", asof=ASOF, stage="undetermined", entry_date="2008",
             focus="Consumer & Marketplaces", **geo("zalando"),
             note="Online fashion retailer, Berlin (Frankfurt: ZAL, IPO Oct 2014). 'Zalando was financially kick-started by "
                  "Rocket Internet ... and Holtzbrinck Ventures' (deutsche-startups, 2010-03-30); HV was an existing investor "
                  "by Sept 2009. HV's round is not named (the export says 'early', an anchor), so the stage is undetermined. "
                  "Market cap EUR 5.26B (stockanalysis, 2026-09-29) @ ECB 2026-09-29 (EUR/USD 1.1355) = $5.97B.",
             rounds=[rnd("2008", None, None, None, True,
                         "https://www.deutsche-startups.de/2010/03/30/auf-den-spuren-von-zappos-mirapodo-shoepassion-zalando-und-co-bringen-schuhe-ins-netz/")],
             extra={"status_citation": SA + "ZAL/"}))
L.append(cls("westwing", status="public", rng="below_1b", usd=258_519_285, val_src="web_verified",
             val_cite=SA + "WEW/", asof=ASOF, stage="undetermined", entry_date="2011",
             focus="Consumer & Marketplaces", **geo("westwing"),
             note="Home and living e-commerce, Munich (Frankfurt: WEW, IPO 2018). Before launch HV already held 16% after "
                  "the just-closed capital increase with the angels Christoph Janz and Klaus Neuhaus (deutsche-startups, "
                  "2011-08-01); the round is not named, so the stage is undetermined. Market cap EUR 227.7M "
                  "(stockanalysis, 2026-09-29) @ ECB 2026-09-29 (EUR/USD 1.1355) = $258.5M.",
             rounds=[rnd("2011-08-01", None, None, None, True,
                         "https://www.deutsche-startups.de/2011/08/01/westwing-shoppingclub-holtzbrinck/")],
             extra={"status_citation": SA + "WEW/"}))
L.append(cls("hellofresh", status="public", rng="below_1b", usd=392_814_870, val_src="web_verified",
             val_cite=SA + "HFG/", asof=ASOF, stage="undetermined", entry_date="2011",
             focus="Consumer & Marketplaces", **geo("hellofresh"),
             note="Meal kits, Berlin (Frankfurt: HFG, IPO Nov 2017). HV is an 'Altinvestor' in the $7.5M Series C of Sept "
                  "2013 led by Phenomen Ventures (Gruenderszene, 2013-09-30), after the $10M round of Dec 2012; HV's own "
                  "entry round (export: 2011, 'early') is not named on a non-vendor source, so the stage is undetermined. "
                  "Market cap EUR 345.9M (stockanalysis, 2026-09-29) @ ECB 2026-09-29 (EUR/USD 1.1355) = $392.8M.",
             rounds=[rnd("2012-12", None, 10_000_000, None, True, None, "vendor"),
                     rnd("2013-09-30", "Series C", 7_500_000, "Phenomen Ventures", True,
                         "https://www.businessinsider.de/gruenderszene/allgemein/hellofresh-phenomen-vc/")],
             extra={"status_citation": SA + "HFG/"}))
L.append(cls("ozon-ru", status="public", rng="1b_plus", usd=7_590_000_000, val_src="web_verified",
             val_cite="https://companiesmarketcap.com/ozon/marketcap/", asof="2026-09",
             stage="Growth", stage_src="model", stage_conf="medium",
             stage_cite="https://venturebeat.com/ai/cisco-begins-vc-investing-in-russia-announces-deal-18m-in-e-commerce-site-ozon",
             entry_date="2007-04", focus="Consumer & Marketplaces", **geo("ozon-ru"),
             note="Russian e-commerce marketplace, Moscow (founded 1998; Nasdaq IPO Nov 2020, now traded on the Moscow "
                  "Exchange). HV entered at the $18M round of April 2007 led by Index Ventures with Cisco ('Holtzbrinck "
                  "Ventures also invested', VentureBeat 2007-04-03), nine years after founding and after 'a period of "
                  "strong expansion and investment by Baring Vostok'; the round carries no series word, so Growth rests on "
                  "that history (model, medium). HV has since exited. Market cap $7.59B (companiesmarketcap, Sept 2026, "
                  "quoted in USD: the ECB has published no RUB reference rate since March 2022, so the aggregator's own "
                  "conversion stands).",
             rounds=[rnd("2007-04-03", None, 18_000_000, "Index Ventures", True,
                         "https://venturebeat.com/ai/cisco-begins-vc-investing-in-russia-announces-deal-18m-in-e-commerce-site-ozon")],
             extra={"status_citation": "https://companiesmarketcap.com/ozon/marketcap/"}))

# --- private, $1B+ ----------------------------------------------------------
TNY = "https://www.einpresswire.com/article/921546417/finn-raises-140-million-and-achieves-unicorn-status"
L.append(cls("finn", status="private", rng="1b_plus", usd=1_134_000_000, val_src="web_verified", val_cite=TNY,
             asof="2026-06-24", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.munich-startup.de/en/55750/seed-financing-for-finn-car/", entry_date="2019-12",
             grad="graduated", grad_src="web_verified", grad_cite="https://tech.eu/2020/12/07/finnauto-series-a/",
             focus="Consumer & Marketplaces", country="DE", country_cite=TNY, city="Munich",
             clear=["needs_web_value"],
             note="Car subscription, Munich (founded 2019). HV led the EUR 8.8M seed closed in Dec 2019 (Munich Startup, "
                  "2019-12-13); the EUR 20M Series A of Dec 2020 (tech.eu, 'all existing investors joined in again') "
                  "graduates the row. Series D of nearly EUR 100M led by Portage, HV named among existing investors, "
                  "'FINN's valuation has surpassed EUR 1 billion' (company release, 2026-06-24): EUR 1.00B @ ECB 2026-06-24 "
                  "(EUR/USD 1.134) = $1.13B, a floor. The company release gives Munich as HQ (a US layer had set US).",
             rounds=[rnd("2019-12-13", "Seed", None, "HV Holtzbrinck Ventures", True,
                         "https://www.munich-startup.de/en/55750/seed-financing-for-finn-car/"),
                     rnd("2020-12-07", "Series A", None, "White Star Capital", True,
                         "https://tech.eu/2020/12/07/finnauto-series-a/"),
                     rnd("2026-06-24", "Series D", None, "Portage", True, TNY, "company")]))
VPR = ("https://www.prnewswire.com/news-releases/verbit-the-worlds-leading-voice-ai-platform-raises-250-million-series-e-"
       "achieving-a-2-billion-valuation-in-less-than-5-years-301429352.html")
VA = "https://techcrunch.com/2019/01/29/verbit-raises-23m-for-its-transcription-service/"
L.append(cls("verbit", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=VPR,
             asof="2021-11-23", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2018/03/29/verbit-funding/", entry_date="2018-03",
             grad="graduated", grad_src="web_verified", grad_cite=VA, flags=["stale"],
             focus="AI & Applied AI", **geo("verbit"),
             note="AI transcription and captioning, New York and Tel Aviv (founded 2017). HV's entry is the $11M seed of "
                  "March 2018 'from HV Holtzbrinck Ventures, Vertex Ventures, and Orzyn Capital' (tech.eu, 2018-03-29); "
                  "the $23M Series A led by Viola Ventures in Jan 2019, 'HV Ventures' participating (TechCrunch), "
                  "graduates the row. Last priced round: $250M Series E at a $2B valuation (company release, "
                  "2021-11-23), stale past 24 months; no later round, tender or collapse evidence found (still launching "
                  "products in 2026; the 2024 3Play Media merger talks did not produce a deal).",
             rounds=[rnd("2018-03-29", "Seed", 11_000_000, None, True, "https://tech.eu/2018/03/29/verbit-funding/"),
                     rnd("2019-01-29", "Series A", 23_000_000, "Viola Ventures", True, VA),
                     rnd("2021-11-23", "Series E", 250_000_000, None, None, VPR, "company")]))
L.append(cls("enpal", status="private", rng="1b_plus", usd=2_412_740_000, val_src="web_verified",
             val_cite="https://invest-in.berlin/n/enpal-secures-eur110-million-in-fresh-funding/", asof="2025-04-07",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2021/10/17/enpal-closes-out-series-c-with-174m-from-softbank-for-tech-to-make-it-easier-for-homeowners-to-make-the-switch-to-solar-energy/",
             entry_date="2021-07", focus="Climate & Energy", **geo("enpal"),
             note="Residential solar, storage and heat pumps, Berlin (founded 2017). HV led the EUR 100M first close of "
                  "July 2021, which TechCrunch counts in the Series C (HV's own page calls it a Series B; either is "
                  "Growth). Last priced round: EUR 110M equity led by TPG, April 2025, at EUR 2.2B per industry sources "
                  "(Handelsblatt via Berlin Partner): EUR 2.20B @ ECB 2025-04-07 (EUR/USD 1.0967) = $2.41B. The Aug 2026 "
                  "sale of a solar-asset portfolio concerns subsidiaries, not Enpal itself.",
             rounds=[rnd("2021-07-08", "Series C", None, "HV Capital", True, gn("enpal", "Y250LWY3UQ")),
                     rnd("2025-04-07", None, None, "TPG", None,
                         "https://invest-in.berlin/n/enpal-secures-eur110-million-in-fresh-funding/")],
             extra={"status_citation": "https://www.corporate.enpal.com/pressemitteilungen/investment-by-equitix-keppel-mizuho-and-mm-capital-partners-unlocks-up-to-eur-65-million-for-enpals-platform-transition"}))
L.append(cls("isar-aerospace", status="private", rng="1b_plus", usd=2_314_600_000, val_src="web_verified",
             val_cite="https://resiliencemedia.co/isar-aerospace-lands-e270m-as-europe-pushes-for-sovereign-space-launch/",
             asof="2026-06-09", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://isaraerospace.com/press/isar-aerospace-raises-over-usd-90m-in-europes-largest-spacetech-funding-round",
             entry_date="2020-12", focus="Industrial & Robotics", **geo("isar-aerospace"),
             note="Orbital launch vehicles, Munich/Ottobrunn (founded 2018). HV joined the USD 91M Series B of Dec 2020 as a "
                  "new investor (company release) and led its extension to over $165M in July 2021. Series D of EUR 270M "
                  "(June 2026) at 'a post-money valuation of around EUR 2 billion' per sources close to the company "
                  "(Resilience Media; GTAI concurs): EUR 2.00B @ ECB 2026-06-09 (EUR/USD 1.1573) = $2.31B.",
             rounds=[rnd("2019-12-10", "Series A", 17_000_000, None, False, None, "company"),
                     rnd("2020-12-09", "Series B", 91_000_000, "Lakestar", True,
                         "https://isaraerospace.com/press/isar-aerospace-raises-over-usd-90m-in-europes-largest-spacetech-funding-round", "company"),
                     rnd("2021-07-28", "Series B", None, "HV Capital, Porsche SE, Lombard Odier", True,
                         gn("isar-aerospace", "MWdWWXhIaw"), "company"),
                     rnd("2026-06-09", "Series D", None, None, True,
                         "https://isaraerospace.com/press/isar-aerospace-secures-eur-270m-to-provide-sovereign-space-capabilities-globally", "company")]))
L.append(cls("scalable-capital", status="private", rng="1b_plus", usd=1_707_900_000, val_src="web_verified",
             val_cite="https://www.zeit.de/news/2025-06/03/investoren-geben-fintech-scalable-capital-155-millionen-euro",
             asof="2025-06-03", stage="undetermined", entry_date="2015", focus="Fintech & Payments",
             **geo("scalable-capital"),
             note="Digital broker and wealth manager, Munich (founded 2014). HV was in the company's first round of 2015 "
                  "(Finovate: the 2016 investors 'all of whom contributed to the company's first round of funding in "
                  "2015') and led the EUR 7M Series A of April 2016 as an existing investor; the 2015 round is not "
                  "named, so the stage is undetermined. Last priced round: EUR 155M (June 2025, Sofina and Noteus, HV "
                  "participating) at EUR 1.5B per the FT (dpa in Die Zeit): EUR 1.50B @ ECB 2025-06-03 (EUR/USD 1.1386) "
                  "= $1.71B.",
             rounds=[rnd("2015", None, None, None, True, "https://finovate.com/scalable-capital-scores-7-9-million/"),
                     rnd("2016-04-06", "Series A", 7_900_000, None, True, gn("scalable-capital", "bldjU1dEQQ")),
                     rnd("2025-06-03", None, None, "Sofina, Noteus Partners", True,
                         "https://www.zeit.de/news/2025-06/03/investoren-geben-fintech-scalable-capital-155-millionen-euro")]))
SEN = "https://techcrunch.com/2024/07/30/sennder-buys-ch-robinsons-european-business/"
L.append(cls("sennder", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=SEN,
             asof="2021-06", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite="https://www.deutsche-startups.de/2019/09/26/sennder-zahlencheck-2017/", entry_date="2018",
             flags=["stale"], focus="Industrial & Robotics", **geo("sennder"),
             note="Digital road freight forwarder, Berlin (founded 2015). In 2018 'Project A, Holtzbrinck Ventures and the "
                  "Flixbus founders invested an eight-figure sum' (deutsche-startups); the page gives no series word, "
                  "and the spring-2019 Accel round that followed is the Series B (LTO), so HV's 2018 round is the Series A "
                  "(model, medium). The Series D's second close of June 2021 was 'at a valuation of over $1 billion' "
                  "(TechCrunch, 2024-07-30), a floor in USD, stale past 24 months; the 2022 top-up reported only a "
                  "speculative target.",
             rounds=[rnd("2018", None, None, "Project A", True,
                         "https://www.deutsche-startups.de/2019/09/26/sennder-zahlencheck-2017/"),
                     rnd("2019-07-22", "Series C", 70_000_000, None, True, gn("sennder", "LXUyb0ZXUQ")),
                     rnd("2021-01-13", "Series D", 160_000_000, None, True,
                         "https://techcrunch.com/2021/01/13/digital-road-freight-forwarder-sennder-raises-160m-series-plans-european-expansion/")]))
FLX = "https://www.swissinfo.ch/eng/eqt,-german-tycoon-buy-%E2%82%AC1-billion-stake-in-greyhound-owner-flix/82707885"
L.append(cls("flix", status="private", rng="1b_plus", usd=3_240_000_000, val_src="web_verified", val_cite=FLX,
             asof="2024-07-04", stage="undetermined", entry_date="2013-09", focus="Consumer & Marketplaces",
             **geo("flix"),
             note="Long-distance bus and rail (FlixBus, FlixTrain, Greyhound), Munich (founded 2011). HV came in with "
                  "Daimler and the TU Munich fund at a capital increase of Sept 2013 (Stuttgarter Zeitung, archived); the "
                  "round is not named, so the stage is undetermined. The 2024 EQT Future and Kuehne deal (primary plus "
                  "secondary, closed 2024-11-28) valued Flix at 'more than EUR 3 billion' per people with knowledge "
                  "(Bloomberg via swissinfo): EUR 3.00B @ ECB 2024-07-04 (EUR/USD 1.08) = $3.24B, a floor; the June 2021 "
                  "Series G was $650M at $3B (TechCrunch, HV participating).",
             rounds=[rnd("2013-09", None, None, None, True,
                         "https://web.archive.org/web/20141006104351/http://www.stuttgarter-zeitung.de/inhalt.fernbusse-daimler-investiert-in-mobilitaetsdienstleister-flixbus.877e6a4a-4852-420d-98fa-4048b1dfebf2.html"),
                     rnd("2021-06-02", "Series G", 650_000_000, None, True,
                         "https://techcrunch.com/2021/06/02/flixmobility-raises-650m-at-a-3b-valuation-to-double-down-on-buses-and-other-transport-in-the-us/"),
                     rnd("2024-07-04", None, None, "EQT Future, Kuehne Holding", None, FLX)]))

# --- acquired -------------------------------------------------------------
L.append(cls("depop", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.unquote.com/uk/official-record/3013379/h-farm-makes-6x-on-depop-exit",
             entry_date="2012", grad="graduated", grad_src="web_verified",
             grad_cite="https://globalventuring.com/blog/2015/02/02/depop-shops-around-for-8m-series-a/",
             focus="Consumer & Marketplaces", **geo("depop"),
             note="Social resale marketplace, London (founded 2011). 'Balderton Capital, Holtzbrinck Ventures and H-Farm "
                  "took part in a EUR 2m seed round for Depop ... in 2012' (Unquote); the $8M Series A of Feb 2015 "
                  "'featuring Holtzbrinck Ventures' (Global Venturing) graduates the row. acq. by Etsy, 2021 ($1.6B); "
                  "Etsy sold it to eBay in Feb 2026 ($1.2B).",
             rounds=[rnd("2012", "Seed", None, None, True,
                         "https://www.unquote.com/uk/official-record/3013379/h-farm-makes-6x-on-depop-exit"),
                     rnd("2013-10-16", "Seed", 1_000_000, "Red Circle Investments", None,
                         "https://www.the-spin-off.com/news/stories/Rossos-Red-Circle-Investments-and-Luca-Marzotto-invest-in-Depop-app-7442"),
                     rnd("2015-02-02", "Series A", 8_000_000, None, True,
                         "https://globalventuring.com/blog/2015/02/02/depop-shops-around-for-8m-series-a/")],
             extra={"status_citation": gn("depop", "dVMkM3Qm56")}))
L.append(cls("quandoo", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite="https://www.vc-magazin.de/blog/2013/06/27/holtzbrinck-atlantic-capital-und-sixt-investieren-in-quandoo/",
             entry_date="2013-06", focus="Consumer & Marketplaces", **geo("quandoo"),
             note="Restaurant reservations, Berlin (founded 2012). HV Holtzbrinck Ventures, Atlantic Capital Partners and "
                  "the Sixt family financed Quandoo's second round in June 2013, a high seven-figure sum (VC Magazin), "
                  "after Cherry's seed of Feb 2013 and before the $8M round of Jan 2014 that the press calls the Series B "
                  "(FinSMEs), so HV's round is the Series A (model, medium). acq. by Recruit, 2015, for EUR 198.6M "
                  "(deutsche-startups).",
             rounds=[rnd("2013-06-27", None, None, None, True,
                         "https://www.vc-magazin.de/blog/2013/06/27/holtzbrinck-atlantic-capital-und-sixt-investieren-in-quandoo/"),
                     rnd("2014-01-13", "Series B", 8_000_000, "DN Capital", True, None, "vendor")],
             extra={"status_citation": gn("quandoo", "18zTy1VTjY")}))
L.append(cls("solaris", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://newsroom.solarisgroup.com/189970-solarisbank-europe-s-leading-banking-as-a-service-platform-raises-eur-60-million-in-series-c-round-to-further-accelerate-growth",
             entry_date="2020-06", focus="Fintech & Payments", **geo("solaris"),
             note="Banking-as-a-service, Berlin (founded 2016). HV led the EUR 60M Series C of June 2020 as a new investor "
                  "(company release). SBI Group took the majority in the EUR 140M Series G of Feb 2025 and cleared the "
                  "owner-control procedure on 2025-03-25 (Solaris newsroom), so the company is acquired; the round "
                  "reportedly valued it near EUR 90M, against over $1B in 2021-23.",
             rounds=[rnd("2020-06-29", "Series C", 67_500_000, "HV Holtzbrinck Ventures", True,
                         "https://techcrunch.com/2020/06/29/banking-platform-solarisbank-raises-67-5-million-at-360-million-valuation/"),
                     rnd("2025-02-03", "Series G", None, "SBI Group, Boerse Stuttgart Group", None,
                         "https://newsroom.solarisgroup.com/246601-solaris-sichert-sich-140-millonen-eur-finanzierungsrunde/", "company")],
             extra={"status_citation": "https://newsroom.solarisgroup.com/248158-solaris-investor-sbi-schliesst-eigentumerkontrollverfahren-ab/"}))

# --- A/B corrections to rows the grind recorded -------------------------------
L.append(cls("n8n", rng="1b_plus", usd=2_500_000_000, val_src="web_verified", val_cite="https://blog.n8n.io/series-c/",
             asof="2025-10-09",
             note="Workflow automation for technical teams, Berlin (founded 2019). HV joined the EUR 55M ($60M) Series B of "
                  "March 2025 led by Highland Europe (TechCrunch; export 'growth', Fund IX Growth), after the EUR 10M "
                  "Series A of 2021. Last priced primary round: the $180M Series C led by Accel, 'our valuation to $2.5 "
                  "billion' (company blog, 2025-10-09). SAP's investment of May 2026 at $5.2B came through a secondary "
                  "share sale (tech.eu, 2026-05-12), so it goes to the note, not the figure (s7)."))
L.append(cls("neura-robotics", stage="Series A", stage_src="model", stage_conf="medium",
             stage_cite="https://techcrunch.com/2023/07/19/neura-robotics-picks-up-55m-to-ramp-up-in-cognitive-robotics/",
             note="Cognitive and humanoid robots, Metzingen (founded 2019). HV co-led the $55M (EUR 50M) round of July 2023 "
                  "with Lingotto, Vsquared and Primepulse, the company's first round with venture investors after ~$80M "
                  "from its strategic backer Han's Group (TechCrunch). The press gives that round no series word; the "
                  "next, EUR 120M of Jan 2025, is the Series B (Robot Report), so HV's round is the Series A (model, "
                  "medium). The Series C of up to $1.4B led by Tether (June 2026) valued it at around $7B per a source "
                  "familiar (CNBC)."))
L.append(cls("holidu", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://shorttermrentalz.com/news/holidu-seriese-funding-round/", entry_date="2022-10",
             note="Holiday-rental marketplace and host software, Munich. HV came in as a new investor in the $98M Series E "
                  "of Oct 2022 led by 83North (ShortTermRentalz), after a Series A (2016), a Series C (2019) and a "
                  "Series D (2021); no priced valuation is published."))

# --- consideration (D4) ---------------------------------------------------
L.append(verdict("sumup", "not_member",
                 "Sale consideration by share swap (decisions.md D4; COLLECTION.md s1, Point Nine 2026-09-26): HV's "
                 "company was payleven, whose first round of summer 2012 it joined with NEA and ru-Net (TechCrunch, "
                 "2012-06-22) and which merged into SumUp in April 2016 with payleven's investors 'coming in behind the "
                 "merged company' (TechCrunch, 2016-04-27). HV's export files that position as SumUp with payleven's "
                 "year (HV Entry 2012, Fund V, later moved to the Coco continuation fund). No SumUp financing names "
                 "Holtzbrinck or HV (the 2012 Series A, the 2013-15 rounds, the 2022 EUR 590M and the 2023 EUR 285M "
                 "rounds). payleven is the member.", ec="site_listing", conf="high",
                 cite="https://techcrunch.com/2016/04/27/sumup-and-payleven-merge-as-european-square-clones-consolidate/"))

write("vis-001", L)
