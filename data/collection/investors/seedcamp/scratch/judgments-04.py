"""PRO-83 grind, batch-004 (kublax .. oradian)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
FII = ("its first listing is the firm's 2013 /companies/ list, inside the Fund II years, when the programme's "
       "standard cheque was the firm's only instrument (seedcamp.com/faq 2012-2014; decisions.md D3)")


def fp(slug, stage, url, date, country, city, **kw):
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, stage_conf="high", entry_date=date,
             **loc(country, city), **kw)


def und(slug, year, country, city, note, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city), note=note, **kw)


L = []
L.append(pc("kublax", "Kublax", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Visual personal finance manager (Seedcamp 2007 winner); the domain is listed for sale"))
L.append(pc("kyko", "Kyko", "GB", "Oxford", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Multi-player social gaming (Seedcamp Week 2008 winner); no later trace found"))
L.append(und("labstep", 2017, "GB", "London", status="acquired", rng="below_1b", focus="Healthcare & Bio",
    note="Electronic lab notebook and research data; acq. by STARLIMS, Aug 2023 (Lab Manager); the 2017 entry round is not named"))
L.append(sc("land-insight", "LandInsight", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Development land search, now LandTech (land.tech); on the firm's Fund III seed list (2015-09-21); the Land Insight acquired by PEXA and Envirosite is an Australian namesake"))
L.append(pc("lateral", "Lateral", "DE", "Berlin", status="unknown", rng="below_1b", focus="AI & Applied AI",
    note="Recommendation and discovery API (Berlin; Seedcamp Week Berlin 2014); lateral.io does not answer; the 2026 'Lateral' seed and 'Lateral Labs' sale are namesakes"))
L.append(pc("legal-tender", "Legal Tender", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Legal services tendering (2013); no later trace found"))
L.append(fp("legit-patents", "Seed", "welcoming-legit-patents-to-the-seedcamp-family/", "2016-11-22", "US", None,
    status="private", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="AI-assisted patent filing (legit.ai); the firm's post of 2016-11-22: 'We are thrilled to announce our seed investment in Legit Patents - the US based start-up'"))
L.append(pc("libryo", "Libryo", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="Regulatory compliance software (South African founders, Libryo Ltd London; the Nextlaw Labs callout, 2016); acq. by ERM, Dec 2022"))
L.append(und("lindus-health", 2021, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Clinical trials platform, now Lindus Therapeutics; the firm backed it 'from Day One' (no round named); EUR 16.5M Series A 2023, $55M Series B led by Balderton Jan 2025; its CRO assets sold to Curavit, Aug 2026"))
L.append(und("liv", 2019, "GB", "London", status="private", rng="below_1b", focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Mixed-reality capture and streaming for VR (liv.tv); '$1M from Oculus founder and Seedcamp' Jul 2019 (TechCrunch, no round word), $2.6M Nov 2019; the pre-filled CZ is a name collision"))
L.append(und("liveflow", 2020, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Accounting and financial reporting automation (Copenhagen founders, London); $3.5M seed Dec 2021, $13.5M 2024; the firm's 2021 post 'Our Investment in Liveflow' names no round"))
L.append(und("loc-tax", 2020, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Tax project management (Loctax); the firm's post of 2021-02-18 announces a $3.6M round led by Cavalry, no round word",
    rounds=[rnd("2021-02-18", None, 3600000, "Cavalry Ventures", True, V + "building-the-tax-operating-system-loc-tax-raises-3-6m-to-help-you-handle-tax-on-a-global-scale/", "firm")]))
L.append(und("lodgify", 2014, "ES", "Barcelona", status="private", rng="below_1b", focus="SaaS",
    note="Vacation rental websites and software; EUR 600K seed May 2015 (FinSMEs), $30M Series B 2022; the 2014 entry is on no cohort post"))
L.append(und("machinations", 2019, "RO", "Bucharest", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Game-economy design platform; EUR 580K seed Jun 2020 (Trending Topics) a year after the list's 2019 entry; the entry round is not named"))
L.append(pc("magictab", "MagicTab", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Restaurant ordering tablets; site live; MAGICTAB LTD (07398116) active"))
L.append(sc("mailcloud", "Mailcloud", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Email collaboration app; a seed investment the firm announced 2014-09-18; no later trace found"))
L.append(sc("marcopolo-learning", "MarcoPolo Learning", "GB", "London", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Children's educational media (New York and London); on the firm's Fund III seed list (2015-09-21); $8.5M 2017 (VentureBeat), Seedrs round 2018; the firm's 2015 post gives New York, today MARCOPOLO LEARNING LTD in London"))
L.append(fp("maze", "Pre-Seed", "maze-launches-the-first-quantitative-analytics-tool-for-prototypes-with-350k-pre-seed-funding/", "2018-05-17",
    "FR", "Paris", status="private", rng="below_1b", focus="SaaS",
    note="Product research and testing platform (founded in Paris, fully distributed); the firm's post of 2018-05-17: 'Maze launches ... with GBP 350k pre-seed funding'; $40M Series B Jun 2022 (TechCrunch)"))
L.append(und("medall", 2020, "GB", "Belfast", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Medical training platform (Belfast); the firm backed it 'at the earliest stage' (no round named); $3.4M Jan 2022 (Silicon Republic); the Indian diagnostics chain Medall is a namesake"))
L.append(und("medusa", 2021, "DK", "Copenhagen", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Open-source commerce engine (medusajs.com); site live; the 2021 entry round is not named"))
L.append(und("meilisearch", 2020, "FR", "Paris", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Open-source search engine API; site live; the 2020 entry round is not named"))
L.append(und("metaview", 2018, "GB", "London", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI recruiting and interview intelligence; the firm has backed it 'since day one' (no round named); $35M Series B led by GV Jun 2025, $60M Series C led by Insight Sep 2026 (the firm's posts)"))
L.append(pc("microscaling-systems", "Microscaling Systems", "GB", "London", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Container autoscaling (UK and Spain, 2016); no later trace found"))
L.append(pc("mightyfingers", "MightyFingers", "LV", "Riga", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="HTML5 gaming engine (2012); no later trace found"))
L.append(pc("milk-ly", "Milk.ly", "NL", None, status="unknown", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="The firm's first Netherlands team (Mini Seedcamp Prague 2011); no later trace found"))
L.append(und("millimetric", 2018, "GB", "London", status="private", rng="below_1b", focus="Data Infrastructure",
    note="Anomaly detection, now API analytics (millimetric.ai, live); the 2018 entry round is not named"))
L.append(c("minubo", prog_at="2013", **loc("DE", "Hamburg"), status="private", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="E-commerce business intelligence (Hamburg); site live; " + FII))
L.append(pc("mobclix", "Mobclix", "US", "San Francisco", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile ad exchange (Seedcamp Week 2008 winner); acq. by Velti, Sep 2010 (~$50M, TechCrunch); Velti's 2012 F-3 lists Seedcamp Investments LLP among the selling shareholders of the consideration shares (decisions.md D5)"))
L.append(sc("monese", "Monese", "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Mobile banking for migrants; the firm 'first backed at seed stage in spring 2015' ($1.8M seed, its 2015-05-27 post); $10M Series A 2017; acq. by Pockit, Oct 2024 (GBP 15M, FinTech Global)"))
L.append(pc("mopapp", "Mopapp", "IT", "Bologna", status="unknown", rng="below_1b", focus="Data Infrastructure",
    note="App store revenue analytics (Mini Seedcamp Berlin 2011); no later trace found"))
L.append(pc("much-better-adventures", "Much Better Adventures", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Adventure holiday marketplace; site live"))
L.append(pc("mybuilder", "MyBuilder", "GB", "London", status="acquired", rng="below_1b", focus="Consumer & Marketplaces",
    note=f"Tradesperson marketplace (Buildersite in 2007); acq. by HomeServe, 2017; {EXIT} (2018-2019)"))
L.append(pc("myrecovery", "MyRecovery", "GB", "London", status="acquired", rng="below_1b", focus="Healthcare & Bio",
    note=f"Patient surgical-journey app; {EXIT} (2022-2024, acquirer not named there)"))
L.append(pc("mytips", "myTips", "UA", "Kyiv", status="unknown", rng="below_1b", focus="SaaS",
    note="Interactive on-screen tutorials (2013); no later trace found"))
L.append(und("nevercode", 2015, "EE", "Tallinn", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Mobile CI/CD, now Codemagic (codemagic.io, live); the 2015 entry is on no cohort post read"))
L.append(pc("newsfixed", "Newsfixed", "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Journalism commissioning marketplace (2014); no later trace found"))
L.append(pc("nextchef", "NextChef", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Restaurant operating system (2016); no later trace found"))
L.append(fp("nodes-and-links", "Seed", "our-investment-in-nodes-links-out-to-increase-the-performance-of-complex-projects/", "2019-06-27",
    "GB", "London", status="private", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="AI project risk analytics; the firm's post of 2019-06-27: 'our investment in ... [the] $1.4M seed round, led by our friends at ADV'; the pre-filled CY is a name collision"))
L.append(und("nordigen", 2018, "LV", "Riga", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Open banking data API; the firm's post of 2018-09-24: 'invest in their $1m round alongside our friends at Inventure' (joining pre-seed investor Change Ventures; no round word); acq. by GoCardless, 2022",
    rounds=[rnd("2018-09-24", None, 1000000, None, True, V + "our-investment-in-nordigen-the-latvian-based-startup-out-to-disrupt-credit-bureaus/", "firm")]))
L.append(pc("nuji", "Nuji", "GB", "London", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social shopping (Seedcamp Week 2010 winner); NUJI LTD (07182051) dissolved 2023-10-31 after liquidation (Companies House)"))
L.append(pc("oinky", "Oinky", "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Savings habit app; OINKY LIMITED (09619397) dissolved 2018-10-30 (Companies House)"))
L.append(und("oneshot", 2020, "GB", None, status="private", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="Deep-learning sales prospecting (oneshot.ai, live); the 2020 entry round is not named"))
L.append(pc("open-sensors", "Open Sensors", "GB", "London", status="private", rng="below_1b", focus="Data Infrastructure",
    note="IoT workplace occupancy data (OpenSensors); site live; OPEN SENSORS LTD (08773413) active"))
L.append(pc("oradian", "Oradian", "HR", "Zagreb", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Core banking for microfinance in emerging markets; site live"))

if __name__ == "__main__":
    jl.write("batch-004", L)
