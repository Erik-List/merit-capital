"""Open rows after pass 1 (non-visible) and the first graduation decisions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, rnd, write, gn, hq, EXPORT, surfaces_lines, ASOF  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


def no(slug, finding, entry_date, firm_line=None):
    """A complete absence test: past the window, dated, the named surfaces."""
    return dict(grad="not_graduated", grad_src="absence_check", grad_asof=ASOF, entry_date=entry_date,
                surfaces=surfaces_lines(slug, finding, firm_line))


L.append(cls("cello", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2023/07/21/munich-based-saas-referrals-platform-cello-has-raised-3-1-million/",
             focus="SaaS", **geo("cello"),
             **no("cello", "the July 2023 seed only; every later hit is a namesake (Cello World, BIC Cello, Cello Group)",
                  "2023-07"),
             note="User-referral platform for SaaS, Munich (founded 2022). 'A preempted Seed round led by HV Capital' of "
                  "EUR 3.1M ($3.5M), July 2023 (tech.eu; Business Insider). No later round on any surface.",
             rounds=[rnd("2023-07-21", "Seed", 3_500_000, "HV Capital", True,
                         "https://tech.eu/2023/07/21/munich-based-saas-referrals-platform-cello-has-raised-3-1-million/")]))
L.append(cls("charles", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("charles"),
             note="Conversational commerce on WhatsApp, Berlin (founded 2019). HV entered 2021-03 (Fund VIII), the month of "
                  "the $6.5M seed Accel led (Accel's own page); no source read here names HV in that round. The $20M Series "
                  "A of July 2022 (Salesforce Ventures; the firm-name search) followed.",
             rounds=[rnd("2022-07-20", "Series A", 20_000_000, "Salesforce Ventures", True, gn("charles", "kE1a0dxOUE"))]))
L.append(cls("coachhub", status="private", rng="below_1b", stage="undetermined", focus="SaaS", **geo("coachhub"),
             note="Digital coaching platform, Berlin (founded 2018). HV entered 2019-06 (Fund VII); the round is not named on "
                  "the surfaces read. $30M in Dec 2020 and the $80M 'B2' of Sept 2021 with HV; $200M Series C (Sofina, "
                  "SoftBank) in June 2022, no priced valuation published.",
             rounds=[rnd("2020-12-18", None, 30_000_000, None, True, gn("coachhub", "a1RGUU5BWQ")),
                     rnd("2022-06-14", "Series C", 200_000_000, "Sofina, SoftBank Vision Fund 2", True, gn("coachhub", "X1hvZXFiaw"))]))
L.append(cls("delli", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("delli"),
             note="Marketplace for independent food makers (Depop's founder Simon Beckerman), London (founded 2020). HV "
                  "entered 2021-01 (Fund VIII), in the GBP 2.5M launch funding announced Dec 2021 (Tech Funding News, found "
                  "by the firm-name search), not named as a series; Balderton's GBP 6M seed of Sept 2022 followed.",
             rounds=[rnd("2021-12-16", None, 3_300_000, None, True, gn("delli", "UzRGWTJ1Sw")),
                     rnd("2022-09-06", "Seed", 7_200_000, "Balderton Capital", True, gn("delli", "l9IWVRVVnM"))]))
L.append(cls("dialogue", status="acquired", rng="below_1b", stage="undetermined", focus="Healthcare & Bio",
             **geo("dialogue"),
             note="Virtual care for employers, Montreal (founded 2016). HV entered 2017-12 (Fund VI); the round is not named. "
                  "$40M in June 2019, Sun Life led $43M in 2020; TSX IPO March 2021; acq. by Sun Life, 2023 (the firm's "
                  "export: acquired).",
             rounds=[rnd("2019-06-17", None, 40_000_000, None, True, gn("dialogue", "ekh5U0xiMw")),
                     rnd("2020-07-29", None, 43_000_000, "Sun Life", True, gn("dialogue", "Ut5X2N6Vnc"))]))
L.append(cls("ecoplanet", status="private", rng="below_1b", stage="undetermined", focus="Climate & Energy",
             flags=["model_disputes_source"], **geo("ecoplanet"),
             note="AI energy procurement and management for industry, Munich (founded 2022). HV entered 2023-03 (Fund IX "
                  "Ventures); that round is not named. EQT Ventures led the EUR 16M Series A of Jan 2025 with HV. The "
                  "Wikidata country CZ belongs to a namesake and is disputed.",
             rounds=[rnd("2025-01-20", "Series A", 16_600_000, "EQT Ventures", True, gn("ecoplanet", "3BnZ2h4Sjc"))]))
L.append(cls("everdrop", status="private", rng="below_1b", stage="undetermined", focus="Consumer & Marketplaces",
             **geo("everdrop"),
             note="Refill cleaning tablets, Munich (founded 2019). HV entered 2020-09 (Fund VII), before the $21.8M Series A "
                  "Felix Capital led in Feb 2021 (TechCrunch); HV's round is not named.", rounds=[]))
L.append(cls("feld-energy", status="private", rng="below_1b", stage="undetermined", focus="Climate & Energy",
             **geo("feld-energy"),
             note="Agrivoltaic solar systems, Munich (founded 2024). HV entered at the EUR 1.7M round of Nov 2024 (the firm's "
                  "own news feed links EU-Startups' report), not named as a series; a EUR 10M+ seed followed in Sept 2025 "
                  "(tech.eu).",
             rounds=[rnd("2024-11", None, 1_800_000, None, True,
                         "https://www.eu-startups.com/2024/11/munich-based-feld-energy-raises-e1-7-million-to-drive-agricultural-photovoltaics-in-germany/"),
                     rnd("2025-09-15", "Seed", 11_000_000, None, True, gn("feld-energy", "cnhQbEw0Zw"))]))
L.append(cls("felmo", status="private", rng="below_1b", stage="undetermined", focus="Healthcare & Bio", **geo("felmo"),
             note="Mobile vets and pet-health clinics, Berlin (founded 2019). HV entered 2020-07 (Fund VII); tech.eu's report "
                  "of the Jan 2021 Series A (Redalpine led) names 'previous backers HV Capital and 468 Capital', so HV's round "
                  "came before it and is not named.",
             rounds=[rnd("2021-01-14", "Series A", None, "Redalpine", True, "https://tech.eu/2021/01/14/felmo-series-a/")]))
L.append(cls("fleek", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://wwd.com/sourcing-journal/industry-news/fleek-funding-wholesale-resale-secondhand-vintage-artificial-intelligence-1238843400/",
             entry_date="2024-11", focus="Consumer & Marketplaces", **geo("fleek"),
             note="Wholesale marketplace for secondhand clothing (YC Winter 2022; the firm's HQ field San Francisco). 'HV "
                  "Capital led the Series A' of $14.8M, announced with a $5.6M a16z-led seed in Nov 2024 (WWD, TechCrunch, "
                  "businesscloud); a $25M Series B followed in July 2026.",
             rounds=[rnd("2024-11-12", "Seed", 5_600_000, "Andreessen Horowitz", False, None),
                     rnd("2024-11-12", "Series A", 14_800_000, "HV Capital", True,
                         "https://wwd.com/sourcing-journal/industry-news/fleek-funding-wholesale-resale-secondhand-vintage-artificial-intelligence-1238843400/"),
                     rnd("2026-07-08", "Series B", 25_000_000, None, None, gn("fleek", "Z01kajhyUQ"))]))
L.append(cls("flank", status="private", rng="below_1b", stage="undetermined", focus="AI & Applied AI", **geo("flank"),
             note="Autonomous legal agents (Legal OS, renamed Flank), Berlin (founded 2018). HV led Legal OS's $2.2M round of "
                  "June 2019 ('led by HV Holtzbrinck Ventures', Artificial Lawyer), not named as a series; Insight Partners "
                  "led a $10M round of June 2025. The old 'LEGAL OS' row is this company (merge at the rebuild).",
             rounds=[rnd("2019-06-20", None, 2_200_000, "HV Holtzbrinck Ventures", True,
                         "https://www.artificiallawyer.com/2019/06/20/germanys-legal-os-contract-template-builder-bags-2-2m-funding/"),
                     rnd("2025-06", None, 10_000_000, "Insight Partners", None,
                         "https://www.insightpartners.com/ideas/flank-raises-10m-to-scale-autonomous-legal-agents-embedded-invisible-and-built-for-the-enterprise/", "firm")]))
L.append(cls("green-fusion", status="private", rng="below_1b", stage="undetermined", focus="Climate & Energy",
             country="DE", country_cite=EXPORT, city="Berlin", city_src="model_knowledge",
             note="Heating-system optimisation software for housing companies, Berlin (founded 2021; the firm's HQ field "
                  "names the state, Brandenburg). HV's entry (HV Entry 2024; the archived list's date 2025-10-25 is a data "
                  "error, later than the capture that carries it) is the EUR 12M round of Jan 2025 (EU-Startups, found by "
                  "the firm-name search), not named as a series in the headline.",
             rounds=[rnd("2021-10-11", "Pre-Seed", 225_000, None, False, gn("green-fusion", "YXc2ZkJhSQ")),
                     rnd("2025-01-21", None, 13_000_000, None, True, gn("green-fusion", "SVdfQk1VUQ"))]))
L.append(cls("igent", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://tech.eu/2024/10/30/igent-ai-emerges-from-stealth-with-6-3m-for-engineering-ai/",
             entry_date="2024-10", grad="censored", focus="AI & Applied AI", **geo("igent"),
             note="AI software-engineering agent, London (founded 2023). 'A GBP 6.3M Seed round led by HV Capital' (tech.eu, "
                  "2024-10-30). Entered 2024-10: inside the 24-month window.",
             rounds=[rnd("2024-10-30", "Seed", 8_200_000, "HV Capital", True,
                         "https://tech.eu/2024/10/30/igent-ai-emerges-from-stealth-with-6-3m-for-engineering-ai/")]))
L.append(cls("yapily", status="private", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             **geo("yapily"),
             note="Open-banking API, London (founded 2017). HV entered 2018-07 (Fund VII), before the $5.4M round of May 2019 "
                  "(TechCrunch); HV's round is not named. $13M Series A (Apr 2020, Lakestar), $51M Series B (July 2021, "
                  "Sapphire) with HV.",
             rounds=[rnd("2020-04-06", "Series A", 13_000_000, "Lakestar", True, gn("yapily", "b3lhN1dJTA")),
                     rnd("2021-07-21", "Series B", 51_000_000, "Sapphire Ventures", True, gn("yapily", "mI0dWZRWUE"))]))
L.append(cls("archlet", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://www.startupticker.ch/en/news/procurement-software-company-archlet-raises-10-million",
             entry_date="2021-09", focus="SaaS", **geo("archlet"),
             note="AI sourcing software for procurement, Zurich (founded 2018, an ETH spin-off). HV led the $10M round of Sept "
                  "2021 ('The funding round led by HV Capital', Startupticker; the page names it the Series A; the firm's "
                  "entry year 2021).",
             rounds=[rnd("2021-09-30", "Series A", 10_000_000, "HV Capital", True,
                         "https://www.startupticker.ch/en/news/procurement-software-company-archlet-raises-10-million")]))
L.append(cls("payrails", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2022/03/17/payrails-emerges-from-stealth-with-6-4m-led-by-a16z-to-build-the-os-for-payments/",
             entry_date="2022-03-17", grad="graduated", grad_src="web_verified", grad_cite=gn("payrails", "JGbUVrMnJO"),
             focus="Fintech & Payments", **geo("payrails"),
             note="Payment operations platform, Berlin (founded 2021). HV is named in the $6.4M seed led by a16z (TechCrunch, "
                  "2022-03-17, the firm's own entry date); EUR 13.5M seed extension June 2023; the $32M Series A of June "
                  "2025 (tech.eu) graduates the row.",
             rounds=[rnd("2022-03-17", "Seed", 6_400_000, "Andreessen Horowitz", True,
                         "https://techcrunch.com/2022/03/17/payrails-emerges-from-stealth-with-6-4m-led-by-a16z-to-build-the-os-for-payments/"),
                     rnd("2023-06-07", "Seed extension", 14_400_000, None, True, gn("payrails", "SGQzV0lXRQ")),
                     rnd("2025-06-12", "Series A", 32_000_000, None, True, gn("payrails", "JGbUVrMnJO"))]))
L.append(cls("musicplayr", status="unknown", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low",
             flags=["stage_uncited"], focus="Media, Gaming & Advertising", **geo("musicplayr"),
             **no("musicplayr", "the Oct 2012 EUR 500K seed only, no later round", "2012-10"),
             note="Web music-playlist app, Cologne (founded 2011). HV's entry 2012-08-29 matches the EUR 500K seed reported in "
                  "Oct 2012 (TechCrunch headline: 'Musicplayr Grabs EUR 500,000 In Seed Funding'); the article naming HV was "
                  "not read. No later round on any surface; its later state was not found.",
             rounds=[rnd("2012-10-19", "Seed", 650_000, None, None, None)]))
# ---- graduation decisions for Seed rows recorded in pass 1
for slug, finding, ed in (
        ("floy", "the Nov 2023 EUR 5.4M seed only, no later round", "2023-11"),
        ("hadrian", "the June 2022 EUR 10.5M seed only; every later round in the results is the US machining company "
                    "Hadrian, a namesake", "2022-06"),
        ("kennek", "the Oct 2023 GBP 10M seed only (reported again Jan 2024), no later round", "2023-10"),
        ("kipu-quantum", "the Dec 2023 EUR 10.5M seed only; the 2024 PlanQK purchase is not a financing", "2023-12"),
        ("timberhub", "the Sept 2022 EUR 5.8M seed only, no later round", "2022-09"),
        ("wasp", "the Oct 2021 $1.5M seed only; the rest of the results are namesakes (insects, films)", "2021-10")):
    L.append(cls(slug, **no(slug, finding, ed)))
L.append(cls("klima", grad="graduated", grad_src="web_verified",
             grad_cite="https://tech.eu/2022/04/21/heres-how-pitch-blinkist-wooga-and-tier-mobility-founders-backed-klima-is-encouraging-teams-to-participate-in-fight-against-climate-change-with-eur10-million/",
             entry_date="2020-08",
             note="Consumer carbon-offsetting app, Berlin (founded 2019). HV's entry 2019-12 closed into the $5.8M seed "
                  "announced 2020-08-12 (Crunchbase News). 'The Series A round was led by Keen Venture Partners and saw the "
                  "participation of HV Capital, Headline, 468 Capital and Adjacent' (EUR 10M, tech.eu 2022-04-21) graduates "
                  "the row. The Wikidata status 'defunct' dated 2004 belongs to a namesake and is disputed."))
write("batch-open1", L)
