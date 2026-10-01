"""PRO-83 grind, batch-009 (cauldron .. habitual); finance-fox was judged in batch-008."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
FII = ("first listed on the firm's 2013-2014 /companies/ list, inside the Fund II years, when the programme's standard cheque "
       "was the firm's only instrument (decisions.md D3)")


def fp(slug, stage, url, date, country, city, cite=None, **kw):
    kw.setdefault("stage_conf", "high")
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, entry_date=date,
             **loc(country, city, cite), **kw)


def und(slug, year, country, city, note, cite=None, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city, cite), note=note, **kw)


L = []
L.append(und("cauldron", "2022-02", "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Web3 sci-fi games studio; the firm's post of 2022-02-02: 'back this exceptional team in an oversubscribed $1.4M round' (no round word); "
         "cauldron.co does not answer; the hq_country_claim (GB) is kept (a London studio)"))
L.append(und("ciao", 2024, "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Members' home swaps and flexible rentals (meetciao.com, live; London listed first); the 2024 entry round is not named; "
         "the pre-filled acquired/public float is a weak CIK name join and is disputed"))
L.append(und("clearago", 2018, "DE", "Berlin", cite="https://www.clearago.de/impressum", status="private", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Online marketplace for waste containers (Clearago GmbH, Ackerstr. 3, Berlin; site live); named among the companies the firm backed in 2018 "
         "(its 2018 review), no round named"))
L.append(pc("clowdy", "Clowdy", "GB", "Manchester", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Music and creative portfolio platform (February 2015 cohort); no later trace found"))
L.append(und("cnc24", 2021, "DE", "Berlin", cite="https://cnc24.com/impressum", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for custom CNC and metal parts (CNC24 GmbH, Berlin); EUR 8.25M Aug 2022 (Deutsche Startups); the 2021 entry round is not named"))
L.append(und("cofide", 2024, "GB", "London", status="private", rng="below_1b", focus="Security",
    note="Workload identity for multi-cloud and AI agents (Cofide Limited 15443303); site live; the 2024 entry round is not named; "
         "the Peruvian development bank COFIDE in the news pack is a namesake"))
L.append(fp("contingent", "Pre-Seed", "founder-qa-with-contingent-co-founder-ceo-tai-alegbe/", "2019-11", "GB", "London",
    status="unknown", rng="below_1b", focus="SaaS",
    note="Supplier risk and compliance monitoring; the firm's post of 2020-12-01: 'Having backed the team at pre-seed in late 2019', then the "
         "GBP 1.7M seed; contingenton.com does not answer"))
L.append(und("creative-labs", 2017, "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Company builder for media and entertainment (creativelabs.co); on the firm's lists 2018-2024 (logo uploaded 2017-08), on no post read; "
         "creativelabs.co does not answer"))
L.append(pc("crowd", "Crowd", "FR", "Paris", status="unknown", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Real-time location sharing ('Crowd from Paris, France', Mini Seedcamp London Aug 2011; one of '4 new Seedcamp Teams' at Seedcamp Week 2011); "
         "no later trace found; crowd.dev (2022) is a different company, and the pre-filled JP is a one-word Wikidata join"))
L.append(fp("crowd-dev", "Pre-Seed", "crowd-dev-raises-e2-2m-to-fuel-community-led-growth-for-open-source-companies/", "2022-10-28",
    "DE", "Berlin", V + "crowd-dev-raises-e2-2m-to-fuel-community-led-growth-for-open-source-companies/", status="acquired", rng="below_1b",
    focus="DevTools & APIs",
    note="Developer community data platform ('the Berlin-based company'); the firm's post of 2022-10-28: 'We are excited to co-lead crowd.dev's "
         "EUR 2.2 million pre-seed round'; acq. by the Linux Foundation (crowd.dev now redirects to the LFX Community Data Platform repository)"))
L.append(fp("cupclub", "Pre-Seed", "meet-cupclub-the-startup-out-to-tackle-the-global-plastics-epidemic/", "2019-02-13", "GB", "London",
    status="private", rng="below_1b", focus="Climate & Energy",
    note="Returnable food and drink packaging (CupClub, now CLUBZERO, clubzero.co live); the firm's post of 2019-02-13: 'our investment in CupClub ... "
         "as part of their $460k pre-seed round'"))
L.append(und("customeros", 2023, "GB", "London", cite="https://customeros.ai", status="private", rng="below_1b", focus="SaaS",
    note="Customer-driven growth platform (107 Cheapside, London, the site's footer); on the firm's lists from Dec 2023 (logo 2023-10), on no post read"))
L.append(fp("dala", "Pre-Seed", "why-were-leading-dalas-1-4m-pre-seed-to-add-much-needed-context-to-search/", "2021-10-27", "GB", "London",
    status="unknown", rng="below_1b", focus="AI & Applied AI",
    note="Contextual workplace search; the firm's post of 2021-10-27: 'We are delighted to lead Dala's $1.4M pre-seed round'; dala.ai shows only "
         "'Coming Soon'"))
L.append(fp("dalton", "Seed", "daltontx-raises-4-million-seed-round-to-build-adaptive-ai-enabled-drug-discovery-platforms/", "2025-09-23",
    "GB", "London", V + "daltontx-raises-4-million-seed-round-to-build-adaptive-ai-enabled-drug-discovery-platforms/", status="private",
    rng="below_1b", focus="Healthcare & Bio", stage_conf="medium",
    note="AI-enabled drug discovery platforms (DaltonTx, King's Cross, London); the firm's post of 2025-09-23: 'partner with Dalton Tx from Day One ... "
         "join their GBP 4 million seed funding round'; the firm's investment year reads 2024, hence medium; the hq_country_claim (GB) is confirmed"))
L.append(und("davinci", 2019, "CZ", "Prague", cite="https://davincits.com", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Group accommodation booking at wholesale prices (Davinci Travel System, 'Based in Prague, the Czech Republic'); named among 2019's new "
         "companies (the firm's 2019 review), no round named"))
L.append(pc("devicehub", "DeviceHub", "PL", "Krakow", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="IoT device cloud (DeviceHub.net, September 2015 cohort); no later trace found"))
L.append(fp("digital-iron", "Pre-Seed", "digital-iron-raises-2m-to-automate-order-processing-for-the-heavy-machinery-industry/", "2024-06-26",
    "GB", "Belfast", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Parts ordering automation for heavy machinery dealers (Digital Iron Ltd, Belfast); the firm's post of 2024-06-26: 'We are excited to lead "
         "Digital Iron's $2 million pre-seed round'"))
L.append(und("digital-risks", "2018-07", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Insurance for digital businesses (Digital Risks, renamed Superscript; gosuperscript.com live); the firm's post of 2018-07-17: 'our latest "
         "investment ... as part of a GBP 2.25M round' (no round word)"))
L.append(und("doczen", 2024, "GB", "London", cite=CH + "15287136", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI platform for commodity operators and traders; the firm's post of 2025-12-01: 'excited to lead Doczen's first funding round' (no round word)"))
L.append(und("dust", 2023, "FR", "Paris", status="private", focus="AI & Applied AI", flags=["needs_web_value"],
    note="Enterprise AI agents (Dust, Paris; founders previously built TOTEMS, a 2011 Seedcamp company); the firm's investment year is 2023 and its post "
         "of 2026-05-21 covers its part in the $40M Series B led by Abstract and Sequoia; the 2023 entry round is not tied to the firm; the band is "
         "pinned in the A/B pass"))
L.append(und("edmund", 2018, "SI", "Ljubljana", status="unknown", rng="below_1b", focus="Crypto & Web3", flags=["model_disputes_source"],
    note="Custody for digital assets; 'In 2018, we backed Tomaz again to build Edmund' (the firm's post of 2025-06-13, Tomaz Stolfa of Vox.io and "
         "Sunrise Robotics, Ljubljana); edmundhq.com does not answer; the pre-filled GB is a one-word Wikidata join"))
L.append(fp("embedd", "Pre-Seed", "embedd-raises-2-7m-to-cut-chip-integration-time-by-6x/", "2023", "GB", "London", CH + "14618092",
    status="private", rng="below_1b", focus="DevTools & APIs", stage_conf="medium",
    note="ML-generated drivers for embedded software; the firm's post of 2026-08-24 covers the '$2.7 million pre-seed round' it joined; the firm's "
         "investment year is 2023, so the round may have closed in stages, hence medium"))
L.append(fp("emma", "Pre-Seed", "edailabs-raises-e5m-for-emma-its-ai-powered-english-learning-tutor/", "2023", "FR", "Paris",
    status="private", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="AI English tutor with 3D avatars (Edailabs); the firm's post of 2025-12-19: 'Since leading his pre-seed', then the EUR 5 million round "
         "alongside Educapital and Breega; emma-learn.com is suspended; the pre-filled DE is a one-word Wikidata join"))
L.append(fp("enapi", "Pre-Seed", "enapi-secures-e2-5m-pre-seed-funding-to-accelerate-ev-charging-interoperability/", "2024-03-19",
    "DE", "Berlin", V + "enapi-secures-e2-5m-pre-seed-funding-to-accelerate-ev-charging-interoperability/", status="private", rng="below_1b",
    focus="Climate & Energy",
    note="EV charging clearing house ('a Berlin-based connectivity platform'); the firm's post of 2024-03-19: 'excited to participate in Enapi's "
         "EUR 2.5 million pre-seed round'"))
L.append(fp("eversettled", "Seed", "eversettled-raises-5m-to-automate-the-painful-process-of-probate/", "2026-07-16",
    "US", "San Francisco", "https://eversettled.com", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI copilot for settling an estate (Kempster Berger Inc., 501 Folsom St., San Francisco); the firm's post of 2026-07-16: 'their $5M Seed round "
         "... led by Emergence Capital, with participation from us at Seedcamp'"))
L.append(und("factmata", 2018, "GB", "London", cite=CH + "10574955", status="acquired", rng="below_1b", focus="AI & Applied AI",
    note="AI content scoring and misinformation detection; acq. by Cision, 2022; factmata.com now serves unrelated content; the 2018 entry round "
         "is not named"))
L.append(und("fiat-republic", 2021, "GB", "London", cite=CH + "13466461", status="private", rng="below_1b", focus="Crypto & Web3",
    note="Banking and payments API for crypto firms; $3.5M Feb 2022, $7M seed extension Dec 2023 (Finextra); the 2021 entry round is not tied to the firm"))
L.append(c("fina", stage="undetermined", entry_date="2022", status="unknown", rng="below_1b", focus="Crypto & Web3",
    flags=["model_disputes_source", "city_unknown"],
    note="Beginner crypto app (heyfina.com, now for sale); on the firm's lists 2022-2024 (logo 2022-10), on no post read; the pre-filled "
         "acquired/SA is a one-word Wikidata join and is disputed; the country is not established"))
for s in ("flow-ai", "flowrite"):
    L.append(fp(s, "Pre-Seed", "making-writing-flow-right-and-fast-our-investment-in-flowrite/", "2020-12-01", "FI", "Helsinki",
        status="acquired", rng="below_1b", focus="AI & Applied AI",
        note="Flowrite (AI email writing, Helsinki; the firm's post of 2020-12-01: 'the EUR 550,000 pre-seed funding', 'one of our first investments "
             "from Fund V'), which sold the Flowrite product to Maestro Labs in Jan 2025 and continued as Flow AI (LLM evaluation); Flow AI was "
             "acquired by Aiven, 2026 ('Flow AI has been acquired by Aiven', flow-ai.com/blog/flow-ai-is-joining-aiven)"
             + ("" if s == "flow-ai" else "; duplicate of flow-ai (identity-merges.json)")))
L.append(jl.verdict("foreword-fund", "not_member",
    "an LP commitment, not a company: the firm's live list carries 'Foreword Fund ... An early-stage micro fund led by Declan Kelly' (foreword.vc); "
    "LP stakes are OUT (decisions.md D4)", ec="site_listing", cite="https://seedcamp.com/our-companies/#foreword-fund"))
L.append(fp("freqens", "Pre-Seed", "freqens-raises-3m-to-bring-transparency-to-indirect-purchases/", "2024-11-21", "FR", "Paris",
    V + "freqens-raises-3m-to-bring-transparency-to-indirect-purchases/", status="unknown", rng="below_1b", focus="SaaS",
    note="Cost benchmarking for indirect purchases ('a Paris-based fintech company'); the firm's post of 2024-11-21: 'excited to participate in "
         "Freqens' $3 million pre-seed funding'; freqens.com now returns a Framer 'Site Not Found'"))
L.append(und("fuel", 2022, "GB", "London", status="unknown", rng="below_1b", focus="Crypto & Web3",
    note="No-code NFT platform for creators (onfuel.io, last dated 2023); on the firm's lists 2022-2024 (logo 2022-04), on no post read"))
L.append(c("function-health", stage="Growth", stage_src="first_party", stage_conf="high",
    stage_cite=V + "seedcamps-investment-in-function-healths-298m-series-b-via-our-select-fund/", entry_date="2025-11-20",
    **loc("US", "Austin"), status="private", rng="1b_plus", usd=2500000000, val_src="web_verified", asof="2025-11-19",
    val_cite="https://techcrunch.com/2025/11/19/function-health-closes-298m-series-b-at-a-2-5b-valuation-launches-medical-intelligence/",
    focus="Healthcare & Bio",
    note="Membership health testing and MRI; the firm's post of 2025-11-20: 'Seedcamp's investment in Function Health's $298M Series B via our Select "
         "Fund' (decisions.md D5: a separate entry after Ezra merged into Function Health); $298M Series B at $2.5B (TechCrunch), as in the a16z, "
         "Battery, Menlo and Redpoint books"))
L.append(und("futures-factory", 2021, "FR", "Paris", cite="https://futures-factory.com", status="private", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Sneaker design platform pairing NFTs with physical shoes ('Based in Paris & Barcelona'); named among 2021's new companies (the firm's 2021 "
         "review), no round named"))
L.append(und("gameplan", "2019-11", "GB", "London", cite=V + "gameplan-raises-half-a-million-to-empower-businesses-with-integrated-workforce-management-system/",
    status="unknown", focus="SaaS", rng="below_1b", flags=["model_disputes_source"],
    note="Workforce management for frontline teams ('London-based Gameplan'); the firm's post of 2019-11-29: 'as part of their GBP 500,000 round' "
         "(no round word); gameplanteam.com does not answer; the pre-filled public float ($49.4M) is a weak CIK name join and is disputed"))
L.append(und("gardin", 2020, "GB", "Abingdon", cite=CH + "12423953", status="private", rng="below_1b", focus="Climate & Energy",
    note="Photosynthesis sensors and crop analytics ('In 2020 we also invested in Gardin', the firm's 2021 post, no round word); $10.8M 2021, "
         "$4.5M May 2025 (Newswire)"))
L.append(pc("garmz", "Garmz", "AT", "Vienna", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Community marketplace for fashion designers (Seedcamp Week 2010 winner; later LOOKK); no later trace found"))
L.append(c("gateme", prog_at="2013-02", **loc("EE", "Tallinn", "https://arcticstartup.com/estonianmafia-is-going-strong-gate-me-wins-at-seedcamp-london/"),
    status="unknown", rng="below_1b", focus="Consumer & Marketplaces", stage_conf="medium",
    note="Event and table booking for nightclubs ('GateMe Wins At SeedCamp London', ArcticStartup 2013-02-04; the firm's Jan 2013 teams post); "
         "no later trace found; " + FII))
L.append(und("gdevelop", 2021, "GB", "London", cite=CH + "13354928", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note="No-code 2D game engine (GDevelop Ltd; open source, founder Florian Rival); site live; the 2021 entry round is not named"))
L.append(und("graphy", 2019, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Data visualisation and collaboration (Graphy Technologies Ltd; site live); co-invested with La Famiglia (the firm's 2021 post), "
         "no round named"))
L.append(pc("greenhouse", "Greenhouse", "EE", "Tallinn", status="private", rng="below_1b", focus="DevTools & APIs", flags=["model_disputes_source"],
    note="Mobile CI/CD (Greenhouse CI, Tallinn; a Slush 2015 finalist, January 2016 cohort), renamed Nevercode, maker of Codemagic; the pre-filled "
         "acquired/CZ is a weak CIK and one-word Wikidata join and is disputed; not Greenhouse Software"))
L.append(und("gyant", 2017, "US", "San Francisco", status="acquired", rng="below_1b", focus="Healthcare & Bio",
    note="AI symptom triage and care navigation (named among 'Seedcamp AI Healthcare companies', 2017-06-27); acq. by Fabric (Fabric Health; "
         "gyant.com now redirects to fabrichealth.com); the entry round is not named"))
L.append(fp("habitual", "Pre-Seed", "founder-qa-with-habitual-co-founders-napala-pratini-and-ian-braithwaite/", "2020-12-10", "GB", "London",
    status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Type 2 diabetes remission and GLP-1 programmes (tryhabitual.com, live); the firm's post of 2020-12-10: 'thrilled to back Ian and Napala "
         "alongside MMC Ventures in their GBP 325k pre-seed round'"))

if __name__ == "__main__":
    jl.write("batch-009", L)
