"""PRO-83 grind, batch-010 (hack-your-closet .. medefer), plus the rows five renames fold together
(homeshift -> homehero, api-changelog -> hitch, krack-ex-wodd -> krak, garmz -> lookk, koia -> mava)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
FII14 = ("first listed on the firm's /companies/ list captured 2014-03-12, inside the Fund II years, when the programme's "
         "standard cheque was the firm's only instrument (decisions.md D3)")
FII = ("first listed on the firm's 2012-2014 /companies/ list, inside the Fund II years, when the programme's standard cheque "
       "was the firm's only instrument (decisions.md D3)")


def fp(slug, stage, url, date, country, city, cite=None, **kw):
    kw.setdefault("stage_conf", "high")
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, entry_date=date,
             **loc(country, city, cite), **kw)


def und(slug, year, country, city, note, cite=None, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city, cite), note=note, **kw)


L = []
L.append(und("hack-your-closet", 2018, "SE", "Stockholm", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Second-hand fashion subscription with a personal shopper (Stockholm; 'not active anymore', Tracxn); hackyourcloset.com does not answer; "
         "on the firm's lists from 2019 (logo 2018-04), no round named"))
L.append(fp("heresy", "Seed", "2017-year-in-review/", "2017", "GB", "London", status="defunct", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Sales performance analytics (founder Dimitar Stanimiroff, ex-Stack Overflow); the firm's 2017 review: 'GBP 755k seed for Heresy' among "
         "its portfolio's raises, the year the firm listed it (logo 2017-08), hence medium; HERESY SOFTWARE LTD 10309713 dissolved 2025-09-30"))
L.append(fp("hiphops", "Pre-Seed", "hiphops-raises-650k-to-automate-release-management-for-modern-tech-teams/", "2022-06-14", "GB", "London",
    status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Release management automation; the firm's post of 2022-06-14: 'a $650K pre-seed round we co-led alongside First Minute Capital'; "
         "no later trace found"))
for s in ("hitch", "api-changelog"):
    L.append(pc(s, "API Changelog", "ES", "Barcelona", status="unknown", rng="below_1b", focus="DevTools & APIs",
        note="API change notifications and developer engagement (API Changelog, London and Barcelona, September 2015 cohort; renamed Hitch, "
             "'Hitch (Spain)', the firm's post of 2016-04-19; same 2015-09 logo on the firm's list); hitchhq.com does not answer"
             + ("" if s == "hitch" else "; duplicate of hitch (identity-merges.json)")))
for s in ("homehero", "homeshift"):
    L.append(pc(s, "Homeshift", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
        note="Home moving service (Homeshift, Seedcamp Week London 2014; renamed HomeHero, the firm's 2020-2024 lists carry 'Homeshift makes moving "
             "fun' under the 2014-09 logo); homehero.co.uk does not answer"
             + ("" if s == "homehero" else "; duplicate of homehero (identity-merges.json)")))
L.append(fp("homie", "Seed", "renters-rejoice-homie-is-here-to-save-the-day/", "2018-02", "GB", "London",
    V + "renters-rejoice-homie-is-here-to-save-the-day/", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["model_disputes_source"],
    note="Rental concierge ('The London-based PropTech company'); the firm's post of 2018-03-12: 'Last month we announced our investment in Homie as "
         "part of their $4m seed round'; homie.rent answers with an empty page; the pre-filled US is a one-word Wikidata join and is corrected"))
L.append(c("hooplo", prog_at="2011", **loc("GB", "London"), status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    stage_conf="medium",
    note="Hooplo Media, social video advertising ('our own companies Hooplo and Finance A Car', the firm's post of 2011-09-08); no later trace found; " + FII))
L.append(und("hubflo", 2022, "FR", "Paris", status="private", rng="below_1b", focus="SaaS",
    note="Client portal for service businesses (Paris; HUBFLO LTD, its UK company, dissolved 2024); site live; the 2022 entry round is not named"))
L.append(und("humanity", 2019, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Healthy-ageing tracking app (humanity.health, live); the 2019 entry round is not named"))
L.append(und("inovia-bio", 2022, "GB", "London", cite=CH + "13828401", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="AI to de-risk drug development ('one of our portfolio companies', 2022); site live; the 2022 entry round is not named"))
L.append(fp("integration-app", "Seed", "integration-app-raises-3-5-million-to-develop-the-worlds-first-llm-powered-integration-platform/",
    "2023-11-07", "US", None, status="private", rng="below_1b", focus="DevTools & APIs", flags=["city_unknown"],
    note="AI integration framework for SaaS (Integration.app, now Membrane; a Delaware company, founder Daniil Bratchenko); the firm's post of "
         "2023-11-07: 'excited to participate in Integration.app's $3.5 million Seed funding round led by ... Crew Capital'"))
L.append(c("interact-io", prog_at="2014-03", **loc("DE", "Berlin"), status="unknown", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Phone and CRM sales assistant (interact.io, Berlin; 'co-founder of interact.io (SC 2014)', the firm's post of 2014-08-12); interact.io "
         "shows a no-index page; " + FII14))
L.append(c("isidor", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://nordic9.com/news/isidor-raised-a-pre-seed-capital-round-with-gradient-ventures-googles-ai-focused-fund-seedcamp-and-future-present",
    entry_date="2025", **loc("GB", "London"), status="private", rng="below_1b", focus="AI & Applied AI",
    note="Reinforcement-learning data for enterprise AI, starting in finance; a $3.6M pre-seed with Gradient Ventures, Seedcamp and Future Present "
         "(Nordic9); Crunchbase places it in London, CB Insights in San Francisco"))
L.append(und("james-finance", 2012, "PT", "Lisbon", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Machine-learning credit risk for lenders (James); the firm's live list says 2012 but no archived list before 2018 carries it, so the "
         "year does not date an entry (decisions.md D3); james.finance now shows a MarkMonitor holding page"))
L.append(c("kara-ai", stage="undetermined", entry_date="2022", status="private", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="Sales management layer over Pipedrive and HubSpot (kara.ai, live); on the firm's lists from 2022 (logo 2022-02), on no post read; "
         "the country is not established"))
L.append(fp("kerys", "Pre-Seed", "kerys-software-raises-e6-2-million-in-pre-seed-funding-for-its-virtualisation-solution/", "2025-07-01",
    "FR", "Paris", status="private", rng="below_1b", focus="Security",
    note="Bare-metal hypervisor ('la start-up francilienne', Le Monde Informatique); the firm's post of 2025-07-01: 'KERYS Software raises EUR 6.2 "
         "million in pre-seed funding', joined by the firm alongside Daphni and Kima"))
L.append(und("kiko", 2020, "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Lettings without agency fees (kiko.homes, which answers with a server error); on the firm's lists from 2020 (logo 2020-01), no round named"))
L.append(fp("knostic", "Pre-Seed", "knostic-raises-3-3m-to-enable-enterprise-genai-access-control/", "2024-04-22", "US", None,
    status="private", rng="below_1b", focus="Security", flags=["city_unknown"],
    note="Need-to-know access control for enterprise LLMs (co-founders Gadi Evron and Sounil Yu); the firm's post of 2024-04-22: 'excited to participate "
         "in Knostic's $3.3M pre-seed financing round'; $11M Mar 2025 (SiliconANGLE)"))
L.append(c("knowable-org", prog_at="2012-12", **loc("DE", "Berlin", "https://thenextweb.com/news/seedcamp-invests-in-knowable-org-tldr-and-unifyo-after-its-paris-event"),
    status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Collaborative DIY and maker platform (Berlin); 'Seedcamp invests in Knowable.org, tl;dr and Unifyo after its Paris event' (TNW, 2012-12-19); "
         "no later trace found"))
for s in ("mava", "koia"):
    L.append(fp(s, "Pre-Seed", "why-were-leading-alternative-investment-app-koias-1-4m-pre-seed-round/", "2022-01-13", "GB", "London",
        "https://www.mava.app/about", status="private", rng="below_1b", focus="SaaS", flags=["model_disputes_source"] if s == "mava" else [],
        note="Koia (alternative-assets investing app; the firm's post of 2022-01-13: 'Why we're leading ... Koia's $1.4M pre-seed round'), which pivoted "
             "to Mava, a customer support platform for community-driven companies ('Goodbye, Koia ... hello Mava', co-founder Iris ten Teije; "
             "Crunchbase's organization/koia-5e28 is Mava; London)"
             + ("; the pre-filled CZ is a one-word Wikidata join and is corrected" if s == "mava" else "; duplicate of mava (identity-merges.json)")))
L.append(fp("koios", "Pre-Seed", "koios-raises-pre-seed-funding-to-enable-leaders-and-organisations-to-manage-and-develop-their-talent-with-voice-driven-psychometric-insights/",
    "2023-09-06", "GB", "London", status="unknown", rng="below_1b", focus="AI & Applied AI",
    note="Voice-driven psychometric insights ('a UK-based voice-driven AI platform', co-founded by the firm's former Head of Talent); the firm's post of "
         "2023-09-06: 'We are thrilled to lead Koios's $550k Pre-Seed funding round'; on the firm's lists only 2023-2024"))
L.append(und("koyo-loans", 2018, "GB", "London", cite=V + "koyo-raises-4-9m-for-open-banking-powered-loans-to-support-newcomers-to-the-uk/",
    status="private", rng="below_1b", focus="Fintech & Payments",
    note="Open-banking loans for thin-file borrowers ('While Koyo is based in London'); 'We first invested in Tom over a year ago' (the firm's post of "
         "2019-10-28, no round word), then the $4.9M round led by Forward Partners"))
for s in ("krak", "krack-ex-wodd"):
    L.append(c(s, prog_at="2014-03", **loc("FR", "Paris"), status="private", rng="below_1b", focus="Consumer & Marketplaces", stage_conf="medium",
        flags=["model_disputes_source"] if s == "krak" else [],
        note="Skateboarding community and products (Krak, formerly Wodd; founder Kevin Straszburger; 'Krak - the social network for skateboarders', "
             "the firm's post of 2014-12-13); skatekrak.com live; " + FII14
             + ("; the pre-filled DK is a one-word Wikidata join and is corrected" if s == "krak" else "; duplicate of krak (identity-merges.json)")))
L.append(und("kraka", 2024, "DE", "Berlin", cite="https://gokraka.com/impressum", status="private", rng="below_1b", focus="AI & Applied AI",
    note="VR training for factory workers (Kraka Technologies GmbH, Berlin); the 2024 entry round is not named"))
L.append(fp("kubeark", "Pre-Seed", "kubeark-raises-2-8m-pre-seed-to-scale-software-products-and-speed-up-cloud-adoption/", "2023-02-01",
    "US", "New York", V + "kubeark-raises-2-8m-pre-seed-to-scale-software-products-and-speed-up-cloud-adoption/", status="private",
    rng="below_1b", focus="DevTools & APIs",
    note="Kubernetes-as-a-service platform ('Based in New York and Bucharest', founded by ex-UiPath people); the firm's post of 2023-02-01: 'raised $2.8 "
         "million in a pre-seed funding round led by Credo Ventures, with our participation'; the firm's investment year is 2022"))
L.append(sc("kukimi", "Kukimi", "DE", "Berlin", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Healthy diet-food delivery; on the firm's Fund III seed list (2015-09-21); insolvent Dec 2016 (Deutsche Startups)"))
L.append(und("kuula", 2020, "GB", "London", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Video streaming for health and wellness creators (Kuula, Inc. with a London UK establishment); kuula.tv does not answer; no round named"))
L.append(und("la-fraise-pro", 2025, "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI agents for dentists' quotes, payments and treatment plans (lafraise.pro, live); the 2025 entry round is not named"))
L.append(fp("light", "Pre-Seed", "light-secures-13m-scale-the-first-ai-powered-general-ledger-for-automating-global-company-finances/", "2022",
    "DK", "Copenhagen", V + "light-secures-13m-scale-the-first-ai-powered-general-ledger-for-automating-global-company-finances/",
    status="private", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="AI general ledger and ERP for multi-entity companies ('The Copenhagen-based AI-driven platform'); the firm's post of 2024-06-12: 'We partnered "
         "up with Light as part of their pre-seed', then its $13M seed led by Atomico; the pre-filled JP is a one-word Wikidata join; the 2026 'Light "
         "raises $46 Million' (embedded electricity) is a namesake"))
L.append(und("limbo", 2020, "GB", "London", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Performance coach monitoring vital signs (the firm's 2021 healthcare post lists it as 'VIV' with the same line); limborevolution.com answers "
         "with an empty page; no round named"))
L.append(c("line-up", prog_at="2014-03", **loc("GB", "London"), status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    stage_conf="medium",
    note="Event ticketing tools (line-up.tickets, live; raised on Seedrs 2014); " + FII14))
L.append(und("linkup", 2024, "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Web search API for AI agents; the firm's post of 2024-11-18: 'partner with Linkup from day one and lead its EUR 3 million funding round' "
         "(no round word); $10M seed led by Gradient, Feb 2026 (Yahoo Finance)"))
L.append(fp("liveblocks", "Pre-Seed", "our-investment-in-liveblocks-1-4m-pre-seed-round-to-make-any-product-collaborative-in-minutes/", "2021-09-16",
    "US", None, status="private", rng="below_1b", focus="DevTools & APIs", flags=["city_unknown"],
    note="Realtime collaboration APIs (Liveblocks Inc.; founders Steven Fabre and Guillaume Salles, a remote team started from New York and Montreal); the firm's post of 2021-09-16: 'Our $1.4M pre-seed investment in "
         "Liveblocks'; $5M seed Mar 2022 (FrenchWeb)"))
for s in ("lookk", "garmz"):
    L.append(pc(s, "Garmz", "AT", "Vienna", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
        note="Community marketplace for fashion designers (Garmz, Seedcamp Week 2010 winner; renamed LOOKK, 'LOOKK (Garmz)', the firm's post of "
             "2011-09-08); on the firm's lists 2012-2014 only; LOOKK closed in 2013"
             + ("" if s == "lookk" else "; duplicate of lookk (identity-merges.json)")))
L.append(und("lua", 2019, "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note=f"Voice guidance for frontline workers (lua.work); {EXIT} (2022-2024, acquirer not named there); lua.work does not answer; the 2026 'Lua' "
         "seed led by Norrsken22 is a namesake; no round named"))
L.append(fp("lupin-holmes", "Pre-Seed", "seedcamp-co-leads-lupin-holmes-5-9m-pre-seed-to-defend-against-software-supply-chain-attacks/",
    "2026-03-17", "FR", "Paris", status="private", rng="below_1b", focus="Security",
    note="Upstream software supply-chain security (Lupin & Holmes, product Depi; founder Roni Carta); the firm's post of 2026-03-17: 'Seedcamp co-leads "
         "Lupin & Holmes $5.9m pre-seed' with 20VC"))
L.append(c("madebymedics", prog_at="2013-12", status="unknown", rng="below_1b", focus="Healthcare & Bio", stage_conf="medium",
    flags=["city_unknown"],
    note="Madebymedics; on the firm's lists only 2013-2014, on no post read; no later trace found; the country is not established; " + FII))
L.append(c("maily", prog_at="2013-05", **loc("BE", "Brussels", V + "seedcamp-london-meet-the-teams/"), status="unknown", rng="below_1b",
    focus="Consumer & Marketplaces", stage_conf="medium",
    note="Safe messaging for young children ('Maily, Brussels, Belgium', Seedcamp London Jan 2013); $600k on Seedrs with Faber Ventures, 2014; "
         "maily.com does not answer; " + FII))
L.append(pc("make-works", "Make Works", "GB", "Glasgow", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Directory connecting designers with local manufacturers (Seedcamp Week London 2014); no later trace found"))
L.append(fp("manara", "Pre-Seed", "manara-raises-3m-to-train-female-engineers-across-mena-and-diversify-talent-in-global-tech-companies/", "2022-05-09",
    "US", "San Francisco", V + "manara-raises-3m-to-train-female-engineers-across-mena-and-diversify-talent-in-global-tech-companies/",
    status="private", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Trains MENA software engineers and places them with global employers ('The San Francisco-based social impact startup'); the firm's post of "
         "2022-05-09: 'We are delighted to participate in Manara's $3M pre-seed round led by Stripe'; the pre-filled MA is a one-word Wikidata join"))
L.append(und("martie", 2019, "US", "San Francisco", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online discount grocer for surplus food ('SF-born', NBC Bay Area); site live; the 2019 entry round is not named"))
L.append(fp("massive-dynamic", "Pre-Seed", "massive-dynamic-raises-e3m-pre-seed-round-to-build-the-ai-orchestration-layer-for-global-advertising/",
    "2025-07-03", "FR", "Paris", V + "massive-dynamic-raises-e3m-pre-seed-round-to-build-the-ai-orchestration-layer-for-global-advertising/",
    status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI agents for paid media teams ('Massive Dynamic based in Paris'); the firm's post of 2025-07-03: 'We are excited to lead Massive Dynamic's "
         "EUR 3M pre-seed round'"))
L.append(pc("medefer", "Medefer", "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Virtual outpatient consultant care for the NHS (Seedcamp Week London 2014); site live"))

if __name__ == "__main__":
    jl.write("batch-010", L)
