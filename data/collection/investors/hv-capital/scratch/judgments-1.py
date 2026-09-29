"""Batch 1 (PRO-104 grind, pass 1): rows the evidence closes now. Citations are
resolved from the surfaces file by item id (judge_lib.gn), never typed."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, name=None, city=None, country=None, note_city=None):
    c, ci, cite = hq(slug, name)
    return dict(country=country or c, country_cite=cite, city=city or ci)


# again: HV entered at the $43M round of July 2024 (the firm's entry date 2024-07-01);
# GV's book cites the $10M seed of Feb 2023, so this round is the Series A (ArcticStartup).
L.append(cls("again", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="medium", stage_cite=gn("again", "G1yYmdZZ2M"), entry_date="2024-07",
             focus="Climate & Energy", **geo("again"),
             note="CO2-to-chemicals gas fermentation, Copenhagen. HV joined the $43M (EUR 39.4M) round of "
                  "July 2024 (Tech.eu, EU-Startups, the firm-name search), the round after GV's $10M seed of "
                  "Feb 2023 and called the Series A by ArcticStartup; the firm's own entry date 2024-07-01. "
                  "Bought Genomatica in Aug 2026 and remains private.",
             rounds=[rnd("2023-02", "Seed", 10_000_000, None, False, "https://techcrunch.com/2023/11/30/again-bios-bacteria-eats-exhaust-and-spits-vinegar-for-the-climate/"),
                     rnd("2024-07-17", "Series A", 43_000_000, None, True, gn("again", "G1yYmdZZ2M"))]))

L.append(cls("agreena", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
             stage_conf="medium", stage_cite=gn("agreena", "hXNmltYUlr"), entry_date="2023-03-30",
             focus="Climate & Energy", **geo("agreena"),
             note="Soil-carbon platform, Copenhagen. HV entered at the EUR 46M round of 2023-03-30 (Business "
                  "Wire; the firm's own entry date is the same day; export 'Stage at Entry: growth', Fund IX "
                  "Growth), after the $4.7M seed of Oct 2021 and the EUR 20M Series A of Feb 2022.",
             rounds=[rnd("2021-10-14", "Seed", 4_700_000, "Giant Ventures", False, "https://techcrunch.com/2021/10/14/agreena-a-regenerative-farming-carbon-market-raises-4-7m-seed-from-giant-vc/"),
                     rnd("2022-02-16", "Series A", None, None, False, gn("agreena", "pzWkJSaUZ4")),
                     rnd("2023-03-30", "Series B", 50_000_000, None, True, gn("agreena", "hXNmltYUlr"))]))

L.append(cls("aitme", status="acquired", rng="below_1b", stage="undetermined", focus="Industrial & Robotics",
             **geo("aitme"),
             note="Cooking-robot kitchens, Berlin. HV entered 2021-06 (Fund VIII, 'early'); no announcement names "
                  "the round. acq. by Circus SE, 2023 (EU-Startups 2023-08-29).",
             rounds=[], extra={"status_citation": gn("aitme", "FNOEpKWkFj")}))

L.append(cls("alasco", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("alasco", "QwSHV0Ymow"), entry_date="2018-10",
             grad="graduated", grad_src="web_verified",
             grad_cite="https://www.insightpartners.com/ideas/real-estate-disruptor-alasco-announces-40m-in-series-b-funding/",
             focus="SaaS", **geo("alasco"),
             note="Financial controlling software for real-estate projects, Munich. HV's entry 2018-08 (Fund VII) is "
                  "the 'seven-digit seed' of Oct 2018 (EU-Startups, found by the firm-name search); a later round "
                  "named Series B ($40M, Jan 2022, Insight Partners' own post) graduates the row.",
             rounds=[rnd("2018-10-08", "Seed", None, None, True, gn("alasco", "QwSHV0Ymow")),
                     rnd("2022-01-11", "Series B", 40_000_000, "Insight Partners", None,
                         "https://www.insightpartners.com/ideas/real-estate-disruptor-alasco-announces-40m-in-series-b-funding/", "firm")]))

L.append(cls("alphin", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("alphin"),
             note="Marketing automation for local businesses, Berlin. HV entered 2018-05 (Fund VII, 'early'); the "
                  "surfaces carry no announcement of any round.", rounds=[]))

L.append(cls("beyond-presence", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("beyond-presence", "WXdaQlBYRQ"), entry_date="2024-10",
             focus="AI & Applied AI", **geo("beyond-presence"),
             note="Real-time AI avatars, Munich. HV's entry 2024-10 is the $3.1M pre-seed of Oct 2024 (FinSMEs; "
                  "TechCrunch 2024-10-14), both found by the firm-name search.",
             rounds=[rnd("2024-10-15", "Pre-Seed", 3_100_000, None, True, gn("beyond-presence", "WXdaQlBYRQ"))]))

# bioniq: member on HV's own financing of the acquirer (D4): the VAHA sale of Dec 2022 is not the entry.
L.append(cls("bioniq", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://businesscloud.co.uk/news/bioniq-used-by-manchester-united-nba-stars-raises-series-b-round/",
             entry_date="2024-07", focus="Healthcare & Bio", **geo("bioniq"),
             note="Personalised supplements from blood biomarkers, London. HV first held Bioniq stock as "
                  "consideration when Bioniq bought HV's VAHA (Dec 2022), which is not an entry (decisions.md D4); "
                  "HV then co-led Bioniq's $15M Series B of July 2024 at $75M ('led by principal investors HV "
                  "Capital and Unbound', businesscloud), a financing of its own. acq. by Herbalife, 2026 (up to "
                  "$150M, TNW 2026-03).",
             rounds=[rnd("2024-07-16", "Series B", 15_000_000, "HV Capital, Unbound", True,
                         "https://businesscloud.co.uk/news/bioniq-used-by-manchester-united-nba-stars-raises-series-b-round/")],
             extra={"status_citation": gn("bioniq", "mlvYUl1dVE")}))

L.append(cls("bux", status="acquired", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             **geo("bux"),
             note="Neobroker, Amsterdam. HV entered in Feb 2016 with $6.9M beside existing shareholders Orange Growth "
                  "Capital and Velocity (Wikipedia, BUX), the company's third round, never named; HV followed on in "
                  "Oct 2017 (EUR 10.6M). acq. by ABN AMRO, 2024 (announced 2023-12, completed 2024-07).",
             rounds=[rnd("2016-02", None, 6_900_000, None, True, "https://en.wikipedia.org/wiki/BUX_(brokerage)"),
                     rnd("2017-10", None, None, None, True, "https://en.wikipedia.org/wiki/BUX_(brokerage)")],
             extra={"status_citation": gn("bux", "U3eGZaX2lR")}))

L.append(verdict("cabify", "not_member",
                 "Sale consideration (decisions.md D4): HV's Cabify line carries Easy Taxi's entry (export: HV Entry "
                 "2014, Fund V and Fund Coco; Storyblok entry 2014-09, partner Christian Saller, Easy Taxi's deal "
                 "partner on the 2015 site). Cabify absorbed Easy Taxi in 2017; no financing of Cabify naming HV was "
                 "found (the firm-name search returns nothing for Cabify). Easy Taxi is the member.",
                 ec="site_listing", conf="medium", cite=EXPORT))

L.append(cls("caronsale", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_conf="medium", stage_cite=EXPORT, entry_date="2021-10", focus="Consumer & Marketplaces",
             **geo("caronsale"),
             note="B2B used-car trading marketplace, Berlin. The firm's export labels its entry 'growth' (HV Entry "
                  "2021, Funds VIII and IX Growth; Storyblok entry 2021-10-01); the 2021 round is not in the "
                  "surfaces. HV followed on in the EUR 70M Series C of July 2025 (Northzone led).",
             rounds=[rnd("2025-07-07", "Series C", None, "Northzone", True,
                         "https://tech.eu/2025/07/07/caronsale-secures-70m-in-series-c-for-cross-border-used-car-trading/")]))

L.append(cls("caterwings", status="acquired", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("caterwings"),
             note="Corporate catering marketplace (a Rocket Internet company), Berlin. HV entered 2016-12 (Fund VI). "
                  "The firm's export lists it as acquired and exited ('Stage: acquired', 'Past'); the acquirer was "
                  "not found on the surfaces read.", rounds=[]))

L.append(cls("caya", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("caya"),
             note="Digital mailroom, Berlin. HV entered 2018-12 (Fund VII, 'early'); no announcement names that round. "
                  "A EUR 6M round in June 2023 (VC Magazin).", rounds=[]))

L.append(cls("ceezer", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://cleantechnica.com/2024/02/16/ai-driven-carbon-credits-platform-ceezer-secures-e10-3-million-in-series-a-funding/",
             entry_date="2024-01", focus="Climate & Energy", **geo("ceezer"),
             note="Carbon-credit procurement platform, Berlin. HV led the EUR 10.3M Series A announced 2024-01-25 "
                  "(CleanTechnica: 'led by HV Capital'; the firm's own entry date 2024-01-25).",
             rounds=[rnd("2024-01-25", "Series A", 11_200_000, "HV Capital", True,
                         "https://cleantechnica.com/2024/02/16/ai-driven-carbon-credits-platform-ceezer-secures-e10-3-million-in-series-a-funding/")]))

L.append(cls("certifaction", status="private", rng="below_1b", stage="undetermined", focus="SaaS",
             **geo("certifaction"),
             note="Privacy-preserving e-signature infrastructure, Zurich. HV entered 2021-12 (Fund VIII, 'early'); no "
                  "announcement names the round.", rounds=[]))

L.append(cls("comet", status="private", rng="below_1b", stage="undetermined", focus="AI & Applied AI",
             flags=["model_disputes_source"], **geo("comet"),
             note="AI micro-stores for e-commerce campaigns, Berlin (comet.rocks, founded 2022). The Wikidata country "
                  "FR belongs to a namesake (Comet Meetings, Paris); the firm's own HQ field gives Berlin. HV entered "
                  "2022-11; the one-word name defeats the press surfaces and no round is named.", rounds=[]))

L.append(cls("dance", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2020/10/22/dance-series-a/", entry_date="2020-10",
             focus="Consumer & Marketplaces", **geo("dance"),
             note="E-bike subscription from the SoundCloud founders, Berlin. 'HV Holtzbrinck Ventures led the round' "
                  "of EUR 15M, the Series A of Oct 2020 (tech.eu). acq. by Swapfiets, 2026 (Zag Daily, 2026-05).",
             rounds=[rnd("2020-10-22", "Series A", None, "HV Holtzbrinck Ventures", True, "https://tech.eu/2020/10/22/dance-series-a/")],
             extra={"status_citation": gn("dance", "9rM0thTVYt")}))

L.append(cls("dealflo", status="acquired", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             **geo("dealflo"),
             note="Onboarding and document automation for lenders, London (founded 2009). HV entered 2017-03 (Fund VI); "
                  "the round is not named. acq. by OneSpan (then VASCO Data Security), 2018: the share purchase "
                  "agreement filed with VASCO's 8-K of 2018-06-01 lists the sellers.",
             rounds=[], extra={"status_citation": "https://www.sec.gov/Archives/edgar/data/1044777/000155837018005091/ex-2d1.htm"}))

L.append(verdict("deel", "not_member",
                 "Sale consideration (decisions.md D4): HV's Deel line carries Zeitgold's entry (export: HV Entry 2016, "
                 "Fund VI, the vintage of HV's Zeitgold position). Deel bought Zeitgold in Aug 2021 (01net / Business "
                 "Wire, 2021-08-04; Storyblok entry 2021-07-01); no financing of Deel naming HV was found. Zeitgold is "
                 "the member.", ec="site_listing", conf="medium", cite=gn("deel", "OFlzMmNqSQ")))

L.append(cls("desci-labs", status="private", rng="below_1b", stage="undetermined", focus="Crypto & Web3",
             **geo("desci-labs"),
             note="Decentralised open-science publishing (DeSci Nodes), Wollerau. HV entered 2023-03 (Fund VIII); no "
                  "announcement names the round.", rounds=[]))

L.append(cls("entyre", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=EXPORT, entry_date="2024-10", focus="Healthcare & Bio", **geo("entyre"),
             note="Home-care coordination platform, Berlin (founded 2018). The firm's export labels its entry 'growth' "
                  "(Fund IX Growth, Storyblok entry 2024-10-25); the round is not in the surfaces.", rounds=[]))

L.append(cls("flip", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=gn("flip", "QlQ0VE1CTQ"), entry_date="2022-02", focus="SaaS", **geo("flip"),
             note="Employee app for frontline workers, Stuttgart. HV entered at the $30M round of Feb 2022 (TechCrunch, "
                  "found by the firm-name search; the firm's own entry date 2021-12-01 is the close; export 'growth'), "
                  "after the company's earlier rounds. Not the US beauty, sneaker or real-estate namesakes other books hold.",
             rounds=[rnd("2022-02-02", None, 30_000_000, None, True, gn("flip", "QlQ0VE1CTQ")),
                     rnd("2025-05-21", None, None, None, None, gn("flip", "a3F5QWhVZQ"))]))

L.append(cls("flowdesk", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("flowdesk", "FwZWhXQTVB"), entry_date="2024-05", focus="Crypto & Web3", **geo("flowdesk"),
             note="Crypto market maker and liquidity provider, Paris. HV joined the $52M Series B extension closed in "
                  "2024-25 and announced 2025-03-04 with the credit line as a $102M financing 'with BlackRock and HV "
                  "Capital' (Fortune); the $50M Series B of Jan 2024 put the company at $250M (The Block).",
             rounds=[rnd("2024-01-18", "Series B", 50_000_000, "Cathay Innovation", False, gn("flowdesk", "d2FweUpSdw")),
                     rnd("2025-03-04", "Series B extension", 52_000_000, None, True, gn("flowdesk", "FwZWhXQTVB"))]))

L.append(cls("floy", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("floy", "zhteWFHTE0"), entry_date="2023-11", focus="Healthcare & Bio", **geo("floy"),
             note="AI radiology diagnostics, Munich. HV's entry is the EUR 5.4M seed of Nov 2023 (tech.eu, found by "
                  "the firm-name search; the firm's own entry date 2023-11-11).",
             rounds=[rnd("2023-11-24", "Seed", None, None, True, gn("floy", "zhteWFHTE0"))]))

L.append(cls("greator", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("greator"),
             note="Personal-development education and events platform, Cologne (founded 2012 as Gedankentanken). HV "
                  "entered 2019-05 (Fund VII); no announcement names the round.", rounds=[]))

L.append(verdict("groupon", "not_member",
                 "Sale consideration (decisions.md D4; config trap): Groupon Inc. bought HV's CityDeal GmbH in May 2010. "
                 "The firm's own 2011 page files the position under 'Groupon' and says so: 'CityDeal GmbH was founded in "
                 "2009 ... Groupon Inc. acquired all shares in the company in May 2010'. CityDeal is the member.",
                 ec="site_listing", conf="high",
                 cite="https://web.archive.org/web/20110111165949/http://www.holtzbrinck-ventures.com:80/index.php?portfolio-aktuell_en"))

L.append(cls("hadrian", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("hadrian", "Z3RVMXAtaw"), entry_date="2022-06", focus="Security", **geo("hadrian"),
             note="Offensive-security / attack-surface management (hadrian.io), Amsterdam. HV's entry 2022-05 is the "
                  "EUR 10.5M seed announced 2022-06-24 (TechCrunch, found by the firm-name search), after a EUR 2.5M "
                  "pre-seed of Nov 2021 (Village Global). Not the US machining company a16z holds under the same name.",
             rounds=[rnd("2021-11-16", "Pre-Seed", None, "Village Global", False, gn("hadrian", "JUa0NpVDRJ")),
                     rnd("2022-06-24", "Seed", None, None, True, gn("hadrian", "Z3RVMXAtaw"))]))

L.append(cls("heartbeat-medical", status="private", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("heartbeat-medical"),
             note="Patient-reported outcomes platform, Berlin (founded 2014). HV entered 2017-11 (Fund VI); no "
                  "announcement names the round.", rounds=[]))

L.append(cls("holidu", status="private", rng="below_1b", stage="Growth", stage_src="first_party", stage_conf="medium",
             stage_cite=EXPORT, entry_date="2022-01", focus="Consumer & Marketplaces", **geo("holidu", city="Munich"),
             note="Holiday-rental marketplace and host software, Munich. The firm's export labels its entry 'growth' "
                  "(HV Entry 2022, Fund VIII); by then Holidu had raised a Series A (2016), a Series C (2019) and a "
                  "Series D (2021), and it closed a $98M Series E in Oct 2022.",
             rounds=[rnd("2016-01-07", "Series A", None, None, False, "https://techcrunch.com/2016/01/07/holidu/"),
                     rnd("2019-09-17", "Series C", None, None, False, "https://techcrunch.com/2019/09/17/holidu-raises-e40m-series-c/"),
                     rnd("2021-05-12", "Series D", 45_000_000, None, False, "https://techcrunch.com/2021/05/12/holidu-books-45m-after-growing-its-vacation-rentals-business-50-yoy-during-covid-19/")]))

write("batch-001", L)
