"""Batch 6 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


def old(slug, status, note, focus, stage="undetermined", rounds=None, extra=None, **kw):
    g = geo(slug)
    g.update(kw.pop("geo", {}))
    return cls(slug, status=status, rng="below_1b", stage=stage, focus=focus, note=note, rounds=rounds or [],
               extra=extra, **{**g, **kw})


def bare(slug, status, note, focus):
    return cls(slug, status=status, rng="below_1b", stage="undetermined", focus=focus, country="DE",
               country_src="model_knowledge", flags=["city_unknown"], note=note, rounds=[])


L.append(old("move24", "defunct", "Relocation services platform, Berlin (founded 2015). HV entered 2015-08, before the EUR 13M "
             "Series B of Oct 2016 (EU-Startups, found by the firm-name search); HV's own round is not named. Filed for "
             "insolvency in Feb 2018 (deutsche-startups).", "Consumer & Marketplaces",
             rounds=[rnd("2016-10-24", "Series B", None, None, True, gn("move24", "RXNKRzd3dw"))],
             extra={"status_citation": gn("move24", "0zZXZWZk5n")}))
L.append(old("mpiriq", "private", "AI platform matching care providers with clinical studies, Munich (founded 2024). HV entered "
             "2024 (Fund IX Ventures); no announcement names the round.", "Healthcare & Bio"))
L.append(bare("my-hammer", "acquired", "MY-HAMMER, the German trades and services auction marketplace (Berlin), on the unit's 2006-07 "
              "portfolio pages. Later majority-owned by IAC's HomeAdvisor. The round is not named.", "Consumer & Marketplaces"))
L.append(cls("n8n", status="private", rng="1b_plus", usd=5_200_000_000, val_src="web_verified",
             val_cite="https://www.bloomberg.com/news/articles/2026-05-12/sap-invests-in-ai-automation-startup-n8n-at-5-2-billion-value",
             asof="2026-05-12", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("n8n", "cWdjQmxRaA"), entry_date="2025-03", focus="AI & Applied AI", **geo("n8n"),
             note="Workflow automation for technical teams, Berlin (founded 2019). HV joined the EUR 55M ($60M) Series B of "
                  "March 2025 led by Highland Europe (TechCrunch, found by the firm-name search; export 'growth', Fund IX "
                  "Growth), after the EUR 10M Series A of 2021. $180M Series C at $2.5B in Oct 2025; SAP's investment of May "
                  "2026 priced it at $5.2B (Bloomberg, the figure Sequoia's and Felicis's books cite).",
             rounds=[rnd("2021-04-29", "Series A", 12_000_000, None, False, gn("n8n", "M1QTdfclJv")),
                     rnd("2025-03-24", "Series B", 60_000_000, "Highland Europe", True, gn("n8n", "cWdjQmxRaA")),
                     rnd("2025-10-09", "Series C", 180_000_000, None, None, gn("n8n", "1pLczZWdVk"))]))
L.append(cls("nabla", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("nabla", "NRRndweVdS"), entry_date="2025-06", focus="Healthcare & Bio", **geo("nabla"),
             note="Ambient clinical AI assistant (founded in Paris 2018; the firm's HQ field: New York). HV entered at the $70M "
                  "Series C of June 2025 (Fierce Healthcare, found by the firm-name search; export 'growth', Fund IX Growth). "
                  "Not Nabla Bio, the antibody-design company.",
             rounds=[rnd("2024-01-05", "Series B", 24_000_000, None, False, gn("nabla", "lMRkhFXzB3")),
                     rnd("2025-06-17", "Series C", 70_000_000, None, True, gn("nabla", "NRRndweVdS"))]))
L.append(old("namshi", "acquired", "Middle East fashion e-commerce (a Rocket Internet company), Dubai (founded 2012). HV entered "
             "2012-12-31; Emaar Malls bought 51% in 2017 and the rest in 2019; noon bought it in 2023. The round is not named.",
             "Consumer & Marketplaces", extra={"status_citation": gn("namshi", "ME0zVDZzbw")}))
L.append(old("newtron", "unknown", "newtron AG, web-based supplier management for industry, Dresden (founded 1998). A "
             "corporate-era holding (entry 2000-05) listed as portfolio 2006-15. Its later state was not found.", "SaaS"))
L.append(old("nimbuzz", "acquired", "Mobile messaging app (Rotterdam, later India; founded 2006). HV entered 2007-05, in the early "
             "rounds of Dec 2005 to July 2008 (Wikipedia names the early investors). acq. by New Call Telecom, 2014 ($250M, "
             "TechCrunch).", "Consumer & Marketplaces"))
L.append(old("omnidock", "private", "E-commerce operating system for marketplace expansion, Berlin (founded 2024; YC Summer 2024). "
             "HV entered in 2024 after the batch (Fund IX Ventures); the round is not named.", "SaaS"))
L.append(old("onlinetours", "unknown", "Online travel agency onlinetours.ru, Moscow (founded 2012). HV entered 2014-03; still on the "
             "2022-25 lists. Its current state was not found.", "Consumer & Marketplaces"))
L.append(old("pamono", "acquired", "Vintage design marketplace, Berlin (founded 2012). HV entered 2012-12. acq. by Chairish, 2021 "
             "(Business of Home). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("pamono", "9tdnhleE5r")}))
L.append(old("pact", "private", "Materials replacing plastics in fashion and textiles, Cambridge UK (founded 2020). HV entered "
             "2025 (Fund IX Ventures); no announcement names the round. Not GymPact, the fitness app Khosla's book holds as "
             "'Pact'.", "Industrial & Robotics"))
L.append(bare("panelbiz", "unknown", "Panelbiz, the online market-research panel operator (Meinungsplatz) the unit listed 2006-07 "
              "and as former in 2011. Its later state was not established.", "SaaS"))
L.append(bare("panfu", "unknown", "Panfu, the children's virtual world (Young Internet GmbH), on the 2011 current list. Its later "
              "state was not established.", "Media, Gaming & Advertising"))
L.append(cls("payleven", status="acquired", rng="below_1b", stage="undetermined", focus="Fintech & Payments",
             country="DE", country_src="model_knowledge", city="Berlin", city_src="model_knowledge",
             note="Mobile card payments (a Rocket Internet company), Berlin (founded 2012). HV was in the funding of Jan 2013 "
                  "(Mobile World Live, found by the firm-name search), not named as a series. Merged into SumUp in 2016 "
                  "(Finovate, 2016-04-28): SumUp continued and payleven's shareholders took SumUp shares.",
             rounds=[rnd("2013-01-22", None, None, None, True, gn("payleven", "R2NjcWV0Yw"))],
             extra={"status_citation": gn("payleven", "ZTJKd3VWcw")}))
L.append(old("paymill", "acquired", "Online payment processing (a Rocket Internet company), Munich (founded 2012). HV entered "
             "2012-08; the firm's own record now links kliknpay.com: sold to Klik & Pay. The round is not named.",
             "Fintech & Payments"))
L.append(old("peakers-ai", "private", "Peakers.ai, US (the archived list: Los Angeles; founded 2017). HV entered 2018-07; still a "
             "seed-stage holding on the 2022-25 lists. The round is not named.", "AI & Applied AI"))
L.append(old("penta", "acquired", "Digital business banking, Berlin (founded 2016). HV entered 2019 (Fund VII), in the EUR 8M "
             "round of Aug 2019 after the EUR 7M Series A of Oct 2018 (finextra, found by the firm-name search), not named as "
             "a series. acq. by Qonto, 2022 (tech.eu 2022-07-22); HV's resulting Qonto stake is not a member (D4).",
             "Fintech & Payments",
             rounds=[rnd("2018-10-15", "Series A", 8_000_000, None, False, None),
                     rnd("2019-08-06", None, 9_000_000, None, True, gn("penta", "05BTjZqN1U"))],
             extra={"status_citation": gn("penta", "Y2FMQmNqcA")}))
L.append(old("pippa-jean", "unknown", "PIPPA&JEAN, fashion jewellery direct sales, Frankfurt (founded 2011). HV entered 2012-06; an "
             "exit on the 2022-25 lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("platinnetz", "unknown", "Community for people over 50, Cologne (founded 2007). HV entered 2007-08; an exit on the "
             "2022-25 lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("praxipal", "private", "AI receptionist for medical practices, Berlin (founded 2024). HV entered at the $6.7M round "
             "of Oct 2025 (tech.eu, found by the firm-name search), not named as a series in the headline.",
             "Healthcare & Bio", rounds=[rnd("2025-10-02", None, 6_700_000, None, True, gn("praxipal", "YzRlU3cUNU"))]))
L.append(old("proximic", "acquired", "Contextual ad targeting (Munich and Palo Alto; founded 2006). HV entered 2006-04 (the firm's "
             "own 2010 post: Proximic secures $4.4M). acq. by comScore, 2015. The entry round is not named.",
             "Media, Gaming & Advertising"))
L.append(cls("qontext", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("qontext", "Ymhrajc2RQ"), entry_date="2026-02", focus="AI & Applied AI", **geo("qontext"),
             note="Context layer for enterprise AI agents, Berlin (founded 2025). HV's entry (HV Entry 2025) is the $2.7M "
                  "pre-seed announced 2026-02-05 (tech.eu, found by the firm-name search).",
             rounds=[rnd("2026-02-05", "Pre-Seed", 2_700_000, None, True, gn("qontext", "Ymhrajc2RQ"))]))
L.append(cls("rabot-energy", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="medium", stage_cite="https://www.energate-messenger.com/news/240766/financial-round-rabot-charge-convinces-investors",
             entry_date="2024-01", focus="Climate & Energy", **geo("rabot-energy"),
             note="Dynamic-tariff electricity supplier (Rabot Charge, renamed rabot.energy), Hamburg (founded 2021). HV's entry "
                  "(Storyblok 2024-01-31; export HV Entry 2023, the close) is the EUR 17.5M Series A announced 2024-01-31 "
                  "(StartingUp; the firm's own news feed links energate's report of the round). The old 'Rabot Charge' row "
                  "is this company (merge at the rebuild).",
             rounds=[rnd("2024-01-31", "Series A", 19_000_000, None, True,
                         "https://www.energate-messenger.com/news/240766/financial-round-rabot-charge-convinces-investors")]))
L.append(old("reiner-ai", "private", "AI productivity for architecture, engineering and construction, Berlin (founded 2024). HV "
             "entered 2025 (Fund IX Ventures); no announcement names the round.", "AI & Applied AI"))
L.append(old("restaurant-kritik", "acquired", "Restaurant reviews site, Hamburg (founded 2008). HV entered 2008-10. acq. by Yelp, "
             "2014 (TechCrunch). The round is not named.", "Consumer & Marketplaces"))
L.append(bare("rumble-media", "unknown", "Rumble Media, on the 2015 current list (the firm's own post of 2013-04-19 on its new "
              "management). Its later state was not established.", "Media, Gaming & Advertising"))
L.append(old("rvvup", "acquired", "Payments and retail finance at checkout, London (founded 2020). HV entered 2021-04 (Fund VIII); "
             "the round is not named. acq. by Zopa, 2025 (Financial IT, 2025-09-02); HV's resulting Zopa stake is not a "
             "member (D4).", "Fintech & Payments", extra={"status_citation": gn("rvvup", "VnF6SFNLZw")}))
L.append(old("seatwave", "acquired", "Secondary ticketing marketplace, London (founded 2007). HV entered 2008-02; the round is not "
             "named. acq. by Ticketmaster, 2014.", "Consumer & Marketplaces"))
L.append(old("semasio", "acquired", "Semantic audience targeting, Hamburg (founded 2010). HV entered 2012 with BDMI and Project A "
             "(the firm's own post of 2012-08-27). acq. by Samba TV, 2024 (AdExchanger). The round is not named.",
             "Media, Gaming & Advertising", extra={"status_citation": gn("semasio", "RCbU5jU2JR")}))
L.append(bare("six-offene-systeme", "unknown", "Six Offene Systeme GmbH, open-source enterprise content management, on the unit's "
              "2006-07 portfolio pages. Its later state was not established.", "SaaS"))
L.append(old("smartlaw", "acquired", "Online legal documents, Berlin (founded 2012). HV entered 2013-05; sold to Wolters Kluwer. "
             "The round is not named.", "SaaS"))
L.append(old("spotcap", "private", "Online SME credit lines (a Rocket Internet company; Berlin, Madrid, later Sydney). HV entered "
             "2014-07, the EUR 13M funding weeks after launch (the firm's own post of 2014-10-29), not named as a series; still "
             "listed 2022-25.", "Fintech & Payments"))
L.append(old("springlane", "unknown", "Kitchenware e-commerce and content, Duesseldorf (founded 2012). HV entered 2013-06; an exit "
             "on the 2022-25 lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("talea", "private", "Home-care network, Berlin (founded 2016). HV entered 2016-10-06, after Cherry's seed of May "
             "2016; HV's round is not named.", "Healthcare & Bio"))
L.append(bare("talentrun", "unknown", "TalentRun, a recruiting startup on the 2011 current list. Its later state was not "
              "established.", "SaaS"))
L.append(cls("the-icon-league", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_conf="high", stage_cite=gn("the-icon-league", "FvNVNhMDFV"), entry_date="2025-11",
             focus="Media, Gaming & Advertising", **geo("the-icon-league"),
             note="Creator-led five-a-side football league (Toni Kroos), Berlin (founded 2023). HV's entry (HV Entry 2025) is "
                  "the EUR 15M Series A of Nov 2025 (FinSMEs, tech.eu, found by the firm-name search).",
             rounds=[rnd("2025-11-03", "Series A", 17_300_000, None, True, gn("the-icon-league", "FvNVNhMDFV"))]))
L.append(old("tingles", "unknown", "Tingles (gettingles.com), San Francisco (YC Winter 2018). HV entered 2018-07 after the batch; "
             "an exit on the 2022-25 lists. Its later state was not found (YC's directory reads it the same way).",
             "Consumer & Marketplaces"))
L.append(old("toptarif", "unknown", "Energy and telecom tariff comparison, Berlin (founded 2007). HV entered 2007-08; former "
             "portfolio from 2011. Its later state was not found.", "Consumer & Marketplaces"))
write("batch-006", L)
