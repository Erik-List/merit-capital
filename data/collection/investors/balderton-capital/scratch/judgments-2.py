"""PRO-106 grind, batch-002 (attio .. ezoic). Same evidence as batch-001."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
LIST = "https://www.balderton.com/companies/"
NEWS = "https://www.balderton.com/news/"
L = []
def fp(slug, stage, **kw):
    return cls(slug, stage=stage, stage_src="first_party", stage_cite=LIST, stage_conf="medium", **kw)
def wv(slug, stage, cite, **kw):
    return cls(slug, stage=stage, stage_src="web_verified", stage_cite=cite, stage_conf="high", **kw)

L.append(wv("attio", "Seed", NEWS + "attio-raises-a-7-7m-seed-round/", status="private", country="GB", city="London", entry_date="2021-11-24",
    rng="below_1b", focus="SaaS", note="CRM for modern teams; the firm's post of 2021-11-24 announces the $7.7M seed (Balderton led; Point Nine also in); Series A Mar 2023, $52M Series B Aug 2025; band re-checked in the momentum pass"))
L.append(fp("avi-medical", "Growth", status="private", country="DE", city="Munich", rng="below_1b", focus="Healthcare & Bio",
    note="Tech-enabled primary care practices; card 'Series B in 2022' (the firm's post of 2022-04-06: EUR 50M)"))
L.append(fp("axitech", "Series A", status="private", country="GB", city="London", rng="below_1b", focus="SaaS",
    note="Crash detection and accident management for connected cars; card 'Series A in 2010' (Bunting director since 2010-03, Balderton's office as service address); the card says Exited, Companies House 05171643 shows the company active"))
L.append(fp("beauty-pie", "Series A", status="private", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Members' club for luxury beauty products; card 'Series A in 2020' (the firm's post 'Our investment in Beauty Pie', 2020-12-18); $100M Series B Sep 2021"))
L.append(fp("better-origin", "Series A", status="unknown", country="GB", city="Cambridge", rng="below_1b", focus="Climate & Energy",
    note="Insect mini-farms for animal feed; card 'Series A in 2022' (the firm's post of 2022-04-07, $16M Series A); the card says Exited and the event is not on any surface read, so status unknown"))
L.append(fp("bookatable", "Series A", status="acquired", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Restaurant reservations (Livebookings until 2012; Bunting director of Livebookings Holdings 2008-16); card 'Series A in 2008'; acq. by Michelin, 2016 (the firm's post of 2016-01-11), then TheFork, 2019"))
L.append(cls("bridgeco", status="acquired", country="US", city="El Segundo", stage="Growth", stage_src="model", stage_conf="low", rng="below_1b",
    focus="Industrial & Robotics", flags=["stage_uncited"],
    note="Networked-audio chips (founded in Dubendorf, Switzerland; HQ later El Segundo); on the Benchmark Europe desk page from 2003, the year the desk led the company's second round; acq. by SMSC, 2011"))
L.append(fp("brigad", "Growth", status="private", country="FR", city="Paris", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for self-employed hospitality and care staff; card 'Series B in 2023' (the firm's post of 2023-02-16, EUR 33M)"))
L.append(wv("carwow", "Seed", "https://techcrunch.com/2014/02/23/carwow/", status="private", city="London", entry_date="2014-02-23", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    note="New-car buying platform; Balderton led the GBP 1.3M seed of Feb 2014 (TechCrunch; the firm's own post), then the GBP 4.6M Series A of Dec 2014; the card says 'Series A in 2014'",
    rounds=[rnd("2014-02-23", "Seed", 2200000, "Balderton Capital", True, "https://techcrunch.com/2014/02/23/carwow/"),
            rnd("2014-12-14", "Series A", 7200000, "Balderton Capital", True, "https://techcrunch.com/2014/12/14/carwow-fuel-injection/")]))
L.append(cls("cellectivity", status="defunct", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile commerce software; on the Benchmark Europe desk page 2003-04 (Misso briefly a director, 2003-11); Companies House 04153715 dissolved; the entry round is not named on any surface read; Benchmark's book carries the same row"))
L.append(fp("checkly", "Growth", status="private", country="DE", city="Berlin", rng="below_1b", focus="DevTools & APIs",
    note="Code-based monitoring; card 'Series B in 2024' (the firm's post of 2024-07-31, $20M Series B led by Balderton)"))
L.append(wv("cino", "Seed", NEWS + "cino-raises-e3-5m-to-revolutionise-shared-payments-with-the-first-virtual-card-that-splits-payments-in-real-time/", status="private", country="NL", city="Amsterdam",
    entry_date="2025-03-04", rng="below_1b", focus="Fintech & Payments",
    note="Shared payments card; the firm's post of 2025-03-04 announces the EUR 3.5M seed (card 'Seed round in 2025')"))
L.append(cls("circle", status="acquired", country="GB", country_src="web_verified", country_cite=LIST, city="London", stage="undetermined",
    rng="below_1b", focus="Healthcare & Bio", flags=["model_disputes_source"],
    note="Circle Health, the UK hospital operator (Bunting director of Circle International 2008-10 and Circle Holdings 2011-14); card gives the year 2008 only and the round is not named on any surface read; AIM IPO 2011, taken private by Toscafund 2017, later Centene and PureHealth; the Wikidata pre-fill joined Circle Internet Financial and is disputed"))
L.append(fp("citymapper", "Series A", status="acquired", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Transit app; card 'Series A in 2013' (Liautaud director from 2013-12); acq. by Via, 2023 (the firm's post of 2023-03-17)"))
L.append(wv("cleo", "Series A", "https://techcrunch.com/2018/09/20/cleo-meet-balderton/", status="private", country="GB", country_src="web_verified", country_cite=LIST,
    city="London", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="AI money assistant; Balderton led the $10M Series A of Sep 2018 (TechCrunch; Moffat director from 2019-02); $80M Series C Jun 2022; the Wikidata country CA is a wrong join; band re-checked in the momentum pass"))
L.append(fp("clue", "Growth", status="private", country="DE", city="Berlin", rng="below_1b", focus="Healthcare & Bio",
    note="Period and reproductive health app; card 'Series C in 2021' (the firm's post of 2021-12-16, EUR 16M)"))
L.append(wv("cobee", "Series A", NEWS + "cobee-raises-e-14m-series-a-to-continue-improving-employee-compensation/", status="acquired", country="ES", city="Madrid",
    rng="below_1b", focus="SaaS", note="Employee benefits platform; the firm's post of 2021-07-27 announces the EUR 14M Series A; acq. by Pluxee, 2024"))
L.append(wv("complyadvantage", "Series A", NEWS + "investment-update-balderton-lead-8-2m-series-a-investment-into-complyadvantage/", status="private",
    country="GB", city="London", rng="below_1b", focus="Fintech & Payments",
    note="AML screening and monitoring; Balderton led the $8.2M Series A of Oct 2016 (Bunting director of IVXS UK from 2016-03); $70M Series C 2020-21"))
L.append(wv("conveo", "Series A", NEWS + "conveo-raises-50m-to-help-fortune-500-brands-understand-what-consumers-want-next/", status="private", country="BE", city="Antwerp",
    rng="below_1b", focus="AI & Applied AI", note="AI qualitative research platform; the firm's post of 2026-09-02 announces the $50M Series A; band re-checked in the momentum pass"))
L.append(wv("convergence", "Pre-Seed", NEWS + "convergence-raises-12m-to-build-personal-ai-agents-with-long-term-memory/", status="acquired", country="GB",
    country_src="web_verified", country_cite=LIST, city="London", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="Personal AI agents; the firm's post of 2024-09-25 announces the $12M pre-seed; Salesforce signed to acquire it in May 2025 (the firm's post of 2025-05-15); London HQ, the pre-filled US is disputed"))
L.append(fp("coro", "Growth", status="private", city="Chicago", rng="below_1b", focus="Security", flags=["model_disputes_source"],
    note="Cyber security for mid-market companies (founded in Israel, US HQ); card 'Series C in 2022'; $100M Series D Mar 2024; the pre-filled 'defunct' is a wrong Wikidata join; band re-checked in the A/B pass"))
L.append(fp("credit-benchmark", "Growth", status="private", city="London", rng="below_1b", focus="Fintech & Payments",
    note="Consensus credit-risk data; card 'Series B in 2015' (the firm's post of 2015-07-15: $20M Series B led by Balderton; Bunting director)"))
L.append(wv("crowdcube", "Growth", NEWS + "balderton-capital-invests-3-8-million-in-crowdcube-series-b/", status="private", country="GB", city="Exeter",
    rng="below_1b", focus="Fintech & Payments", flags=["stage_disputes_band"],
    note="Equity crowdfunding platform; the firm's own post of 2014-07-17 is titled 'Balderton Capital invests GBP 3.8M in Crowdcube series B' (Bunting director from 2014-08); the card says 'Series A in 2014'"))
L.append(cls("curious-ai-company", status="unknown", country="FI", city="Helsinki", stage="undetermined", rng="below_1b", focus="AI & Applied AI",
    note="AI research company; the card says 'Series B in 2015', the firm's own post of 2015-10-05 reports a EUR 800k raise and the 2017 post $3.675M, neither naming a round, so the label is not used; the card says Exited and the event is not on any surface read"))
L.append(fp("darktrace", "Growth", status="acquired", city="Cambridge", rng="below_1b", focus="Security",
    note="AI cyber security; card 'Secondary in 2018' (Liquidity I; decisions.md D5); LSE IPO 2021; acq. by Thoma Bravo, 2024 ($5.3B)"))
L.append(cls("dash0", status="private", country="US", city="New York", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "dash0-raises-110m-series-b-at-1b-valuation-to-build-the-ai-nervous-system-for-production/",
    rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2026-03-25",
    val_cite=NEWS + "dash0-raises-110m-series-b-at-1b-valuation-to-build-the-ai-nervous-system-for-production/", focus="DevTools & APIs",
    note="OpenTelemetry-native observability; the firm's post of 2026-03-23 announces the $110M Series B at a $1B valuation (card 'Series B in 2026'); the same mark as the Accel and Cherry books",
    rounds=[rnd("2026-03-23", "Series B", 110000000, None, True, NEWS + "dash0-raises-110m-series-b-at-1b-valuation-to-build-the-ai-nervous-system-for-production/", "firm")]))
L.append(wv("davis", "Pre-Seed", NEWS + "davis-raises-5-5-million-pre-seed-to-accelerate-early-stage-real-estate-development-from-months-to-hours/", status="private",
    country="FR", city="Paris", rng="below_1b", focus="AI & Applied AI", note="AI for early-stage real estate development; the firm's post of 2026-05-06 announces the $5.5M pre-seed"))
L.append(fp("deepip", "Series A", status="private", country="FR", city="Paris", rng="below_1b", focus="AI & Applied AI",
    note="AI patent drafting; card 'Series A in 2025'; band re-checked in the momentum pass"))
L.append(wv("deepset", "Growth", "https://en.wikipedia.org/wiki/Deepset", status="private", country="DE", city="Berlin", rng="below_1b",
    focus="AI & Applied AI", flags=["stage_disputes_band"],
    note="LLM application framework (Haystack); Balderton led the $30M Series B of Aug 2023 (Wikipedia, citing the announcement; the Series A was 2022); the card says 'Series A 2023'"))
L.append(fp("defined-ai", "Growth", status="private", country="US", city="Seattle", rng="below_1b", focus="AI & Applied AI",
    note="Training data for AI (DefinedCrowd until 2021); card 'Secondary in 2020' (Liquidity I; D5)"))
L.append(fp("delli", "Seed", status="private", country="GB", city="London", entry_date="2022-09-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for independent food makers (Depop's founder); card 'Seed in 2022' (the firm's post of 2022-09-06, $7.2M; Waterhouse director 2022-08 to 2025-12); $6M extension Sep 2024"))
L.append(wv("demodesk", "Series A", NEWS + "demodesk-raises-8m-to-scale-worlds-first-intelligent-online-sales-meeting-software/", status="private", country="DE",
    city="Munich", rng="below_1b", focus="SaaS", note="Online sales meeting software; the firm's post of 2020-09-03 announces the $8M Series A"))
L.append(fp("depop", "Seed", country="GB", city="London", entry_date="2012", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social shopping app; card 'Seed in 2012' (Bonanzinga director from 2012-12-31, Balderton's office as service address); $8M Series A Jan 2015; acq. by Etsy, 2021 ($1.6B)"))
L.append(wv("detectify", "Growth", NEWS + "detectify-secures-e215-million-to-bring-world-class-cyber-security-to-everyone/", status="private", country="SE",
    city="Stockholm", rng="below_1b", focus="Security", flags=["stage_disputes_band"],
    note="Automated web vulnerability scanning; the firm's post of 2019-11-26 announces the EUR 21.5M round, a Series B (the Series A was 2016-17); the card says 'Series A in 2019'"))
L.append(fp("digital-surgery", "Series A", status="acquired", country="GB", city="London", rng="below_1b", focus="Healthcare & Bio",
    note="Surgical training and AI (Touch Surgery); card 'Series A in 2013'; acq. by Medtronic, 2020"))
L.append(wv("dinghy", "Seed", NEWS + "investment-update-dinghy-raises-1-2m-to-provide-flexible-insurance-geared-to-freelance-professionals/", status="unknown",
    country="GB", city="London", entry_date="2018-01-05", rng="below_1b", focus="Fintech & Payments",
    note="Flexible insurance for freelancers; the firm's post of 2018-01-05 announces the $1.2M seed; the card says Exited and the event is not on any surface read"))
L.append(wv("dream-games", "Seed", "https://techcrunch.com/2019/11/19/dream-games/", status="private", city="Istanbul", entry_date="2019-11-19",
    focus="Media, Gaming & Advertising", flags=["needs_web_value"],
    note="Casual puzzle games (Royal Match); Balderton led the $7.5M seed of Nov 2019 (TechCrunch); Series A Mar 2021, Series B at $1B Jun 2021, $255M at $2.75B Jan 2022; mark pinned in the A/B pass",
    rounds=[rnd("2019-11-19", "Seed", 7500000, "Balderton Capital", True, "https://techcrunch.com/2019/11/19/dream-games/"),
            rnd("2021-03-01", "Series A", 50000000, None, True, NEWS + "dream-games-secures-50m-series-a-and-launches-its-first-game-royal-match/", "firm"),
            rnd("2022-01-18", "Series C", 255000000, None, True, NEWS + "dream-games-raises-255m-and-hits-a-2-75-billion-valuation/", "firm")]))
L.append(cls("drive-diagnostics", status="private", country="US", city="Austin", stage="undetermined", rng="below_1b", focus="SaaS",
    flags=["identity_conflated"],
    note="Driver-behaviour telematics; Drive Diagnostics was renamed GreenRoad Technologies in 2007; on the Benchmark Europe desk page in 2006 under the old name; Benchmark's own book files GreenRoad under its Israel desk from 2008, a second listing of the same company; the entry round is not named on any surface read"))
L.append(cls("dropshop", status="defunct", country="DE", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces", flags=["city_unknown"],
    extra={"hq_city": None},
    note="German chain of eBay drop-off shops (dropshop.de); on the Benchmark Europe desk page 2005-08; closed in the late 2000s; the city and the entry round are not on any surface read"))
L.append(fp("dubsmash", "Growth", status="acquired", country="US", city="New York", rng="below_1b", focus="Consumer & Marketplaces",
    note="Lip-sync video app (founded in Berlin, HQ moved to New York); card 'Series B in 2016'; acq. by Reddit, 2020"))
L.append(cls("elecsnet", status="private", city="Moscow", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Russian payment-kiosk network; on Benchmark's worldwide list in 2007 (Europe lineage); the entry round is not named on any surface read; status low confidence"))
L.append(wv("escape", "Series A", NEWS + "escape-raises-18m-series-a-to-fight-ai-powered-cyberattacks-with-ai-agents/", status="private", country="FR", city="Paris",
    rng="below_1b", focus="Security", note="Automated offensive security; the firm's post of 2026-03-10 announces the $18M Series A"))
L.append(wv("exein", "Growth", NEWS + "exein-raises-e70m-series-c-to-protect-critical-infrastructure-from-back-door-attacks/", status="private", country="IT", city="Rome",
    rng="below_1b", focus="Security", note="Embedded IoT security; the firm's post of 2025-07-16 announces the EUR 70M Series C (card 'Series C in 2025')"))
L.append(cls("ezoic", status="private", country="US", city="Carlsbad", stage="undetermined", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Ad and layout optimisation for publishers; the card says 'Initial investment in 2011', which names no round, and no surface read names the 2011 round"))
jl.write("batch-002", L)
