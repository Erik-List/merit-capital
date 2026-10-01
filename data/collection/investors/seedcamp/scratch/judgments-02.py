"""PRO-83 grind, batch-002 (compilr .. fluidstack)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's 2018-2021 list marks it exited (acquirer not named there)"
L = []
L.append(pc("compilr", "Compilr", "CA", "Halifax", status="acquired", rng="below_1b", focus="DevTools & APIs",
    note=f"Browser IDE (Halifax, Nova Scotia; Seedcamp New York 2011); {EXIT}"))
L.append(pc("countly", "Countly", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Product analytics (founded in Istanbul, Countly Ltd London since 2013); site live"))
L.append(pc("crashpadder", "Crashpadder", "GB", "London", status="acquired", rng="below_1b", focus="Consumer & Marketplaces",
    note="Peer-to-peer accommodation; acq. by Airbnb, 2012 (the firm's /acquirer/airbnb page)"))
L.append(pc("cronofy", "Cronofy", "GB", "Nottingham", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Calendar and scheduling APIs; $1.6M led by Firestartr 2016, EUR 17.8M 2025 (EU-Startups)"))
L.append(pc("crowdprocess", "CrowdProcess", "PT", "Lisbon", status="unknown", rng="below_1b", focus="AI & Applied AI",
    note="Browser-based distributed computing, later AI credit risk (James); the old domain is parked with a registrar"))
L.append(c("cru-kafe", status="private", **loc("GB", "London"), rng="below_1b", focus="Consumer & Marketplaces", stage="undetermined",
    entry_date="2016-10-25",
    note="Organic coffee capsules; the firm's post of 2016-10-25 'Seedcamp leads CRU Kafe GBP 1.25M round' names no round word; CRU KAFE LIMITED 08648796 active",
    rounds=[rnd("2016-10-25", None, None, "Seedcamp", True, V + "seedcamp-leads-cru-kafe-1-25m-round/", "firm")]))
L.append(pc("ctrlio", "Ctrlio", "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Household bills management; CTRLIO LTD (09376911) dissolved 2025-01-14 (Companies House); the domain now serves unrelated content"))
L.append(sc("curve", "Curve", "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Card-consolidating digital wallet; on the firm's list of Seedcamp Fund III seed investments (2015-09-21); acq. by Lloyds Banking Group, completed May 2026 (Finextra; reported ~GBP 120M)"))
L.append(c("cuvva", status="private", **loc("GB", "London"), rng="below_1b", focus="Fintech & Payments", stage="undetermined", entry_date="2016",
    note="Pay-as-you-drive car insurance; EUR 17.5M Series A Dec 2019 (EU-Startups); Seedcamp's entry round not named on any surface read"))
L.append(c("cybersmart", status="private", **loc("GB", "London"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2016",
    note="Automated cyber-security compliance for SMBs; GBP 12.75M Series B Feb 2023 (TechCrunch); Seedcamp's entry round not named on any surface read"))
L.append(sc("cymmetria", "Cymmetria", "IL", "Tel Aviv", status="unknown", rng="below_1b", focus="Security",
    note="Cyber deception platform; on the firm's Fund III seed list (2015-09-21) and its 2015-06-29 post 'Cymmetria exits stealth, having raised a seed round with Seedcamp' (alongside Felicis and Y Combinator); site returns 403"))
L.append(c("cyscale", status="private", **loc("GB", "London"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2022-05-19",
    note="Cloud security posture (Cluj and London); the firm's post of 2022-05-19 announces the EUR 3M round it backed without naming it",
    rounds=[rnd("2022-05-19", None, None, None, True, V + "cloud-security-analysis-start-up-cyscale-raises-e3m/", "firm")]))
L.append(pc("data-smoothie", "Data Smoothie", "GB", "London", status="unknown", rng="below_1b", focus="Data Infrastructure",
    note="Data analysis platform for survey data; datasmoothie.com does not answer"))
L.append(c("dinmo", status="private", **loc("FR", "Paris"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2022-11-22",
    note="Composable customer data platform; the firm's post of 2022-11-22 announces 'EUR 1.6M in initial funding' without naming the round; the pre-filled FR stands",
    rounds=[rnd("2022-11-22", None, 1600000, None, True, V + "dinmo-aims-to-build-a-new-privacy-compliant-standard-for-the-customer-data-platform-industry-with-e1-6m-in-initial-funding/", "firm")]))
L.append(pc("divido", "Divido", "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Buy-now-pay-later white-label platform (formerly Invoice House); DIVIDO LTD (08410307) dissolved 2024-09-03 (Companies House)"))
L.append(c("doctorly", status="acquired", **loc("DE", "Berlin"), rng="below_1b", focus="Healthcare & Bio",
    stage="Pre-Seed", stage_src="first_party", stage_cite=V + "qa-with-doctorly-ceo-co-founder-samir-el-alami/", stage_conf="high", entry_date="2018-02-05",
    note="Cloud practice software for German doctors; the firm's post of 2018-02-05: 'Investing alongside Pioneers Ventures and Target Global in their pre-seed round'; $10M 2023; taken over out of insolvency in a full acquisition, June 2025 (EU-Startups)"))
L.append(c("doorfeed", status="private", **loc("GB", "London"), rng="below_1b", focus="Fintech & Payments", stage="undetermined", entry_date="2021",
    note="Residential real-estate acquisition platform for institutional buyers; EUR 12M 2023 (the firm's post), a later round than the list's 2021 entry, which is not named"))
L.append(pc("doxout", "DoxOut", "MK", "Skopje", status="unknown", rng="below_1b", focus="SaaS",
    note="Word-document collaboration with external teams (2014); no later trace found"))
L.append(c("dreamdata", status="private", **loc("DK", "Copenhagen", V + "welcome-dreamdata-to-the-seedcamp-nation-providing-data-driven-growth-for-b2b-companies/"),
    rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2019-09-04",
    note="B2B revenue attribution; the firm's post of 2019-09-04: 'our investment in Dreamdata as part of their $535,000 round' (no round word); $55M Series B Oct 2025",
    rounds=[rnd("2019-09-04", None, 535000, None, True, V + "welcome-dreamdata-to-the-seedcamp-nation-providing-data-driven-growth-for-b2b-companies/", "firm"),
            rnd("2025-10-14", "Series B", 55000000, None, None, None, "press")]))
L.append(sc("edgefolio", "Edgefolio", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Fund distribution data platform (Norwegian founders, Edgefolio UK Ltd); on the firm's Fund III seed list (2015-09-21); site live"))
for s in ("edited", "editd"):
    L.append(pc(s, "EDITD", "GB", "London", status="private", rng="below_1b", focus="SaaS",
        note="Retail and apparel market intelligence (EDITD, renamed EDITED); Seedcamp Week 2010 winner; site live"
             + ("" if s == "edited" else "; duplicate of edited (identity-merges.json)")))
L.append(c("electric-car-scheme", status="private", **loc("GB", "London"), rng="below_1b", focus="Climate & Energy", stage="undetermined",
    entry_date="2021", note="EV salary-sacrifice scheme; GBP 2.5M round Sep 2022 (the firm's post) after the list's 2021 entry, which is not named"))
L.append(c("elephant-healthcare", status="private", **loc("GB", "London"), rng="below_1b", focus="Healthcare & Bio", stage="undetermined",
    entry_date="2018", note="Digital health records for frontline care in emerging markets; site live; Seedcamp's entry round not named on any surface read"))
L.append(c("elliptic", status="private", **loc("GB", "London"), rng="below_1b", focus="Crypto & Web3", stage="undetermined", entry_date="2014",
    note="Blockchain analytics and crypto compliance; $120M Series D May 2026 (FinSMEs); the 2014 entry is on no cohort post, so programme or seed is not established"))
L.append(sc("emoov", "eMoov", "GB", "Brentwood", status="acquired", val_conf="low", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online estate agent; a seed investment the firm announced 2014-09-18 ('Part of Seedcamp's new fund is dedicated to investing in seed rounds'); entered administration 2019, the emoov.co.uk brand continues under a new owner and EMOOV LIMITED (07118826) was dissolved 2023"))
L.append(c("enzai", status="private", **loc("GB", "Belfast"), rng="below_1b", focus="AI & Applied AI", stage="undetermined", entry_date="2023-09-05",
    note="AI governance and risk platform (Enzai Technologies, Belfast); the firm's post of 2023-09-05 announces $4M without naming the round",
    rounds=[rnd("2023-09-05", None, 4000000, None, True, V + "enzai-secures-4-million-for-its-global-ai-governance-platform/", "firm")]))
L.append(pc("erply", "Erply", "EE", "Tallinn", status="private", rng="below_1b", focus="SaaS",
    note="Cloud point-of-sale and inventory for retailers; Seedcamp Week 2009 winner; site live"))
for s in ("evercontact", "kwaga"):
    L.append(pc(s, "Kwaga", "FR", "Paris", status="acquired", rng="below_1b", focus="SaaS",
        note=f"Kwaga, renamed Evercontact (automatic contact updates); invested from Mini Seedcamp Paris 2009; {EXIT}"
             + ("" if s == "evercontact" else "; duplicate of evercontact (identity-merges.json)")))
L.append(c("ezra", status="acquired", **loc("US", "New York"), rng="below_1b", focus="Healthcare & Bio", stage="undetermined", entry_date="2018",
    note="AI full-body MRI cancer screening; the firm calls itself a 'Day One investor'; $4M round Nov 2018 (AlleyWatch) not named as the firm's entry; merged into Function Health, 2025 (the firm's post of 2025-05-06); the Select fund's Function Health entry is its own row (decisions.md D5)"))
L.append(pc("faballthings", "FabAllThings", "IE", "Dublin", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Customisable design products (2014); no later trace found"))
L.append(c("fabric", status="private", country="US", country_src="model_knowledge", rng="below_1b", focus="SaaS", stage="undetermined",
    entry_date="2022", flags=["city_unknown"], note="AI workspace and file system (fabric.so); site live; Seedcamp's entry round not named on any surface read"))
L.append(c("faks", status="private", **loc("FR", "Paris"), rng="below_1b", focus="Healthcare & Bio", stage="undetermined", entry_date="2023-05-18",
    note="Supplier platform for pharmacies and labs; the firm's post of 2023-05-18 announces EUR 5M without naming the round",
    rounds=[rnd("2023-05-18", None, None, None, True, V + "faks-raises-e5-million-to-digitize-interactions-between-pharmacies-and-their-suppliers/", "firm")]))
L.append(pc("farmeron", "Farmeron", "HR", "Osijek", status="acquired", rng="below_1b", focus="SaaS",
    note=f"Livestock farm management software (Osijek, Croatia); {EXIT}"))
L.append(pc("farmhopping", "Farmhopping", "BG", "Sofia", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for local farms (2014); the domain now serves unrelated content"))
L.append(c("ferry", status="private", **loc("GB", "London"), rng="below_1b", focus="AI & Applied AI", stage="undetermined", entry_date="2023",
    note="AI for industrial workflows (Ferry, a trading name of ThirdRails Ltd, England); site live"))
L.append(c("fifth-dimension", status="private", **loc("GB", "London"), rng="below_1b", focus="AI & Applied AI",
    stage="Pre-Seed", stage_src="first_party", stage_cite=V + "fifth-dimension-ai-raises-2-3-million-pre-seed-round-for-its-ai-partner-for-real-estate-professionals/",
    stage_conf="high", entry_date="2023-10-12",
    note="AI copilot for real estate; the firm's post of 2023-10-12 announces the GBP 2.3M pre-seed round (the list's investment year is 2023)"))
L.append(c("figures", status="private", **loc("FR", "Paris"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2022-01-19",
    note="Compensation benchmarking and pay transparency; the firm's post of 2022-01-19: 'we are delighted to lead investment' in Figures' EUR 1.7M round, no round word",
    rounds=[rnd("2022-01-19", None, None, "Seedcamp", True, V + "our-investment-in-figures-e1-7m-round-to-help-startups-manage-their-salary-policy/", "firm")]))
L.append(pc("finance-a-car", "Finance A Car", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Car finance comparison (Seedcamp Week 2010 winner); no later trace found"))
L.append(sc("findify", "Findify", "SE", "Stockholm", status="acquired", rng="below_1b", focus="SaaS",
    note="E-commerce search and personalisation; on the firm's Fund III seed list (2015-09-21); acq. by Maropost (findify.io now redirects to Maropost's merchandising cloud)"))
L.append(pc("fishbrain", "FishBrain", "SE", "Stockholm", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Fishing app and social network; $8M from Northzone 2015, $13.5M Series B 2018, $31M 2021"))
L.append(c("flagcat", status="private", **loc("FR", "Paris"), rng="below_1b", focus="Media, Gaming & Advertising", stage="undetermined",
    entry_date="2023", note="AI tools and studio for webtoons (Paris studio, per its site); Seedcamp's entry round not named on any surface read"))
for s in ("fleksy", "thingthing"):
    L.append(pc(s, "ThingThing", "ES", "Barcelona", status="unknown", rng="below_1b", focus="DevTools & APIs",
        note="ThingThing (Barcelona keyboard app) acquired the Fleksy keyboard in 2016 and took its name; text-input SDKs; fleksy.com does not answer"
             + ("" if s == "fleksy" else "; duplicate of fleksy (identity-merges.json)")))
L.append(c("flow", status="private", **loc("GB", "London"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2016",
    flags=["model_disputes_source"],
    note="Flow Engineering (flowengineering.com), requirements management for hardware teams; $50M Series B Sep 2026 (the firm's post); the pre-filled acquired/AR is a name collision; the list's 2016 year is not matched by any cohort post and the entry round is not named"))
L.append(c("fluidstack", status="private", **loc("GB", "London"), rng="10b_plus", usd=18000000000, val_src="web_verified", asof="2026-09",
    val_cite="https://valueaddvc.com/blog/fluidstack-1-5b-round-18b-valuation-jane-street-ai-data-centers-2026",
    stage="Seed", stage_src="web_verified", stage_cite="https://nordic9.com/news/fluidstack-raised-a-3m-seed-round-with-participation-from-seedcamp-mercuri-and-7-global-capital/",
    stage_conf="high", entry_date="2019-03", focus="AI & Applied AI",
    note="GPU cloud for AI (founded in London 2017); first outside round a $3M seed, Mar 2019, with Seedcamp, Mercuri and 7 Global (Nordic9); $1.5B led by Jane Street at $18B, Sep 2026; the cap citation is re-pinned in the A/B pass",
    rounds=[rnd("2019-03", "Seed", 3000000, None, True, "https://nordic9.com/news/fluidstack-raised-a-3m-seed-round-with-participation-from-seedcamp-mercuri-and-7-global-capital/", "press"),
            rnd("2026-09", None, 1500000000, "Jane Street", None, "https://valueaddvc.com/blog/fluidstack-1-5b-round-18b-valuation-jane-street-ai-data-centers-2026", "press")]))

if __name__ == "__main__":
    jl.write("batch-002", L)
