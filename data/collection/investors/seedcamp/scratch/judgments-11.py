"""PRO-83 grind, batch-011 (membrane .. robot-media), plus the renames it surfaced
(integration-app -> membrane, nanoget -> propoly, milkster -> milk-ly, replay -> stupeflix)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
CLS = json.loads((Path(__file__).resolve().parent.parent / "companies/classification.json").read_text())
FII = ("first listed on the firm's 2012-2014 /companies/ list, inside the Fund II years, when the programme's standard cheque "
       "was the firm's only instrument (decisions.md D3)")


def fp(slug, stage, url, date, country, city, cite=None, **kw):
    kw.setdefault("stage_conf", "high")
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, entry_date=date,
             **loc(country, city, cite), **kw)


def und(slug, year, country, city, note, cite=None, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city, cite), note=note, **kw)


def dup(slug, canonical, extra=""):
    """A duplicate slug judged exactly as its canonical row (identity-merges.json folds it at the rebuild)."""
    r = {k: v for k, v in CLS[canonical].items() if k not in ("slug", "who")}
    r.update({"slug": slug, "who": jl.WHO})
    r["note"] = r.get("note", "") + extra + f"; duplicate of {canonical} (identity-merges.json)"
    return r


L = []
for s in ("membrane", "integration-app"):
    L.append(fp(s, "Seed", "integration-app-raises-3-5-million-to-develop-the-worlds-first-llm-powered-integration-platform/",
        "2023-11-07", "US", None, status="private", rng="below_1b", focus="DevTools & APIs", flags=["city_unknown"],
        note="AI integration infrastructure for SaaS (Integration.app, renamed Membrane, getmembrane.com; a Delaware company, founder Daniil Bratchenko); "
             "the firm's post of 2023-11-07: 'excited to participate in Integration.app's $3.5 million Seed funding round led by ... Crew Capital'"
             + ("" if s == "membrane" else "; duplicate of membrane (identity-merges.json)")))
L.append(und("memories", 2025, "US", "San Francisco", status="private", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="Visual memory models for video understanding (Memories.ai, founders Shawn Shen and Enmin Zhou; began at Cambridge); the firm's post of "
         "2025-07-24: 'partnered with Memories.ai from Day One' and the '$8 million funding round' (no round word); the pre-filled CH is a one-word "
         "Wikidata join"))
L.append(dup("milkster", "milk-ly", "; Milk.ly renamed Milkster (the firm's /companies/milk-ly/ page is titled Milkster from Aug 2014)"))
L.append(und("mimo", 2022, "GB", "London", cite=V + "mimo-raises-15-5m-and-launches-its-global-b2b-payments-platform/", status="private",
    rng="below_1b", focus="Fintech & Payments",
    note="B2B payments and cash flow for SMBs ('the London and Stockholm-based company'); the firm's investment year is 2022 and its post of 2024-04-11 "
         "covers its part in the GBP 15.5M round led by Northzone; the entry round is not named"))
L.append(fp("miru-labs", "Pre-Seed", "miru-labs-raises-2-7m-round-to-shape-the-future-of-cybersecurity-investigations/", "2024",
    "US", "San Francisco", status="private", rng="below_1b", focus="Security", stage_conf="medium",
    note="AI investigation platform for threat hunting ('Founded in 2024 in the Bay Area'); the firm's post of 2025-09-10: 'We are excited to lead the "
         "pre-seed round of Miru Labs from day one'; the firm's investment year is 2024, hence medium"))
L.append(fp("motley", "Pre-Seed", "motley-raises-1-5m-to-build-the-worlds-first-ai-business-reporting-platform/", "2025-11-06",
    "CH", "Zurich", V + "motley-raises-1-5m-to-build-the-worlds-first-ai-business-reporting-platform/", status="private", rng="below_1b",
    focus="AI & Applied AI",
    note="AI business reporting for customer success teams ('The Zurich-based company'); the firm's post of 2025-11-06: 'We are excited to lead "
         "Motley's 1.5 million pre-seed round'"))
L.append(und("motormia", 2023, "US", "Scottsdale", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="AI platform for car enthusiasts and the aftermarket (founder Isaac Bunick; Scottsdale, AZ); the firm's post of 2024-10-30: 'participate in "
         "MOTORMIA's $8 million funding round' (no round word)"))
L.append(fp("murphy", "Pre-Seed", "murphy-raises-15m-to-fix-the-broken-industry-of-debt-servicing-with-ai/", "2025", "ES", "Barcelona",
    V + "murphy-raises-15m-to-fix-the-broken-industry-of-debt-servicing-with-ai/", status="private", rng="below_1b",
    focus="Fintech & Payments", stage_conf="medium",
    note="AI agents for debt collection ('Murphy based in Barcelona'); the firm's post of 2025-07-14: 'investing in Murphy's $15 million funding across "
         "their pre-seed and seed rounds' and 'double down', so the firm entered at the pre-seed, hence medium"))
for s in ("propoly", "nanoget"):
    L.append(pc(s, "Nanoget", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
        note="Online rental management (Nanoget, January 2016 cohort, 'Online rental management platform'; the firm's 2018+ lists carry Propoly with "
             "the same line); propoly.com live" + ("" if s == "propoly" else "; duplicate of propoly (identity-merges.json)")))
L.append(und("nopan", 2024, "NL", "Amsterdam", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Account and wallet payment infrastructure ('Dutch startup Nopan', Finextra; founders ex-Netflix payments); the firm's post of 2026-07-14: "
         "'a new funding round led by Newion, with follow-on investment from Seedcamp'; the 2024 entry round is not named"))
L.append(pc("now-native", "Now Native", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Local experiences marketplace (Seedcamp Week Berlin, Dec 2014 cohort); no later trace found"))
L.append(fp("nurture", "Pre-Seed", "nurture-raises-2-8-million-to-create-the-future-of-early-childhood-learning/", "2024-09-19",
    "US", "Mercer Island", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Story-based learning for young children (CEO Roger Egan; Mercer Island, WA); the firm's post of 2024-09-19: 'We are excited to co-lead "
         "Nurture's $2.8 million pre-seed round'; the firm's investment year is 2023"))
L.append(c("offset-options", prog_at="2011", **loc("ES", "Barcelona"), status="unknown", rng="below_1b", focus="Climate & Energy",
    stage_conf="medium",
    note="Carbon offsets at the online point of sale (Mini Seedcamp Barcelona 2010 winner; 'we already have two awesome Barcelona based teams ... "
         "Offset Options and Robot Media', the firm's post of 2011-10-04); no later trace found; " + FII))
L.append(und("omniscient", 2025, "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Real-time reputation and risk intelligence for executives (founders Arnaud d'Estienne and Mehdi; Bpifrance support); the firm's post of "
         "2026-04-02: 'lead Omniscient's latest $4.1 million funding round' (no round word)"))
L.append(fp("opereit", "Seed", "opereit-raises-2-5m-to-fix-logistics-e1-billion-blind-spot/", "2026-06-03", "ES", "Barcelona",
    "https://techfundingnews.com/barcelona-startup-opereit-raises-2-5m-to-tackle-logistics-trillion-euro-problem-with-ai-agents/",
    status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI agents that audit logistics invoices and file carrier claims ('Barcelona startup', TFN); the firm's post of 2026-06-03: 'we're proud to "
         "lead their $2.5m seed round, alongside Yellow'"))
L.append(pc("opinion", "Opinion", "SE", "Stockholm", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["model_disputes_source"],
    note="Podcast recording and editing app (February 2015 cohort); no later trace found; the pre-filled NO is a one-word Wikidata join"))
L.append(c("opio", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://techfundingnews.com/opio-raises-4m-seed-ai-financial-due-diligence-audit/", entry_date="2025",
    **loc("FR", "Paris"), status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI for financial due diligence (founded in Paris in 2025 by Tristan Fulchiron and Olivier Chance); the firm's post of 2026-09-21: 'taking part "
         "in Opio's EUR 4 million first round', which the press calls a seed (TFN, The SaaS News); the firm's investment year is 2025, hence medium"))
L.append(und("orchest", 2020, "NL", "Amsterdam", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Open-source data science pipelines ('Earlier this year, we invested in Rick and Yannick', the firm's post of 2020-09-03, no round word); "
         "$3.5M Oct 2021 (Yahoo Finance); orchest.io sits behind a Cloudflare block"))
L.append(fp("outpost-bio", "Pre-Seed", "outpost-bio-raises-3-5m-pre-seed-to-make-human-microbiology-computable/", "2026-03-02",
    "GB", "London", CH + "16594666", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Foundation model for microbiome-drug interactions; the firm's post of 2026-03-02: 'Outpost Bio raises $3.5m pre-seed', with its partner's "
         "quote on the investment; the firm's investment year is 2025"))
L.append(fp("pair", "Seed", "pair-raises-seed-round-to-drive-enterprise-ai-adoption/", "2025", "GB", "London", status="private",
    rng="below_1b", focus="AI & Applied AI", stage_conf="medium",
    note="Enterprise AI adoption and upskilling (PAIR, formerly Inversity; London); the firm's post of 2026-01-27: 'We're thrilled to have taken part "
         "in their latest seed round, alongside Venrex and FJ Labs'; the firm's investment year is 2025, hence medium"))
L.append(fp("papaya", "Seed", "papaya-raises-3-5m-to-build-europes-largest-ev-ecosystem-and-decarbonise-european-fleets/", "2022-09-27",
    "GB", "London", V + "papaya-raises-3-5m-to-build-europes-largest-ev-ecosystem-and-decarbonise-european-fleets/", status="private",
    rng="below_1b", focus="Climate & Energy",
    note="EV fleet sourcing and management software ('a UK-based company'); the firm's post of 2022-09-27: 'Papaya has raised a $3.5M seed round led by "
         "Giant Ventures, with our participation', as in the 20VC book; papayadash.com live; not the Papaya in the Sequoia book"))
L.append(und("peer-medical", 2020, "GB", "London", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Treatment histories shared by cancer patients; on the firm's lists from 2020, on no post read; the domain now serves unrelated content"))
L.append(und("pelikan-mobility", 2023, "FR", "Paris", status="private", rng="below_1b", focus="Climate & Energy",
    note="EV-native leasing for commercial fleets ('a UK and France-based deeptech platform'); the firm's post of 2024-03-21: 'participate in Pelikan's "
         "EUR 4 million funding round' (no round word)"))
L.append(und("penelope-health", 2025, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Payer policy intelligence for US medical payments (Sohum Patel and Mattijs De Paepe, 'building out of Seedcamp HQ'); the firm's post of "
         "2026-09-18: 'backed Penelope Health since their first round' (no round word) and the $100M commitment led by Thoreau"))
L.append(und("peony", 2018, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Notes and knowledge base, now the Peony data room (peony.ink, live; San Francisco and London); on the firm's live list with year 2018, "
         "no round named"))
L.append(und("picnic", 2020, "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Group chat and shared photos for close friends (Picnic Ventures Ltd; picnic.photos live); the pre-filled NL is a one-word Wikidata join "
         "with the Dutch grocer, and GeekWire's robot-pizza Picnic is another namesake; the 2020 entry round is not named"))
L.append(fp("pixie", "Seed", "the-all-in-one-operating-system-for-accountants-our-2-25m-seed-investment-in-pixie/", "2021-11-18",
    "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Practice management for small accounting firms (usepixie.com, live; founder Celso Pinto, also of GoSimpleTax); the firm's post of 2021-11-18: "
         "'our GBP 2.25M seed investment in Pixie'; not the Pixie in the Spark book"))
L.append(fp("plakar", "Pre-Seed", "plakar-launches-encrypted-and-queryable-open-source-backup-platform-with-3m-in-funding/", "2025-05-15",
    "FR", "Paris", V + "plakar-launches-encrypted-and-queryable-open-source-backup-platform-with-3m-in-funding/", status="private",
    rng="below_1b", focus="Security",
    note="Open-source encrypted backup ('a Paris-based open-source backup and restore solution'); the firm's post of 2025-05-15: 'We are excited to "
         "lead Plakar's $3 million pre-seed funding round'"))
L.append(fp("popup", "Pre-Seed", "popup-secures-3-5m-pre-seed-round-to-launch-game-changing-no-code-e-commerce-platform-for-entrepreneurs-of-all-sizes/",
    "2022-11-23", "US", None, status="unknown", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="No-code e-commerce builder; the firm's post of 2022-11-23: 'Popup raised $3.5M in pre-seed round funding led by Accel, joined by us', as in "
         "the Accel and 20VC books (US); on the firm's lists only 2022-2024"))
L.append(fp("porters", "Pre-Seed", "porters-raise-e2-7m-pre-seed-to-fill-the-e3bn-black-hole-in-financial-services/", "2026-02-11",
    "CH", "Zurich", status="private", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="AI back office for banks, starting with garnishments (Porters Group AG, Zurich); the firm's post of 2026-02-11: 'we're backing Porters in their "
         "EUR 2.7m raise in pre-seed funding' (led by Earlybird, Tech.eu); the pre-filled GB is a one-word Wikidata join; the firm's investment year is 2025"))
L.append(fp("powernaut", "Pre-Seed", "powernaut-raises-e2-4-million-to-decentralise-the-energy-sector/", "2024-12-11",
    "BE", "Ghent", status="private", rng="below_1b", focus="Climate & Energy",
    note="Virtual power plant software ('a Belgium-based startup'; 'la start-up gantoise'); the firm's post of 2024-12-11: 'support Powernaut from Day "
         "One and participate in their EUR 2.4 million pre-seed round'"))
L.append(sc("pronto", "Pronto", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces", entry_date="2015-05",
    flags=["model_disputes_source"],
    note="On-demand home-cooked food delivery ('Pronto became a Seedcamp-backed company in May 2015', the firm's post of 2015-08-28); on the firm's "
         "Fund III seed list (2015-09-21); no later trace found; the pre-filled acquired is a name collision (the AV maker Pronto, India's Pronto)"))
L.append(und("protagonist", 2021, "GB", "London", status="private", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Collaboration space for the purpose economy (protagon.ist, live); named among 2021's new companies (the firm's 2021 review), no round named; "
         "the pre-filled public float ($2.9B) is Protagonist Therapeutics, a name collision, and is disputed"))
L.append(und("quarterone", "2019-06", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Sales forecasting from live CRM data (co-founders Richard Mann and Michael Foulkes); the firm's post of 2019-06-13: 'Our investment in "
         "QuarterOne' (no round word); quarterone.com answers with an empty page"))
L.append(und("rasayel", 2021, "US", None, status="private", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="WhatsApp for B2B sales teams (Rasayel, Inc., a remote team; CEO Tarek Khalil); site live; the entry round is not named"))
L.append(pc("real-funds", "Real Funds", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Property investment platform (June 2016 cohort); no later trace found"))
L.append(und("receeve", 2019, "DE", "Berlin", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Debt-servicing automation (receeve, Berlin; CEO Paul Jozefak); acq. by InDebted (receeve.com now lands on indebted.co's 'Receive' product); "
         "no round named"))
L.append(dup("replay", "stupeflix", "; the firm's 2017 list shows Stupeflix's card under its app's name, Replay (site slug stupeflix)"))
L.append(c("resolyst", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://digitalhealth.london/resolyst-wins-hlth-europe-2026-startup-pitch-with-vision-for-continuous-specialty-care",
    entry_date="2026", **loc("GB", "London"), status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Specialty care for chronic conditions (founder Dr Molly Gilmartin); 'raised $3 million in pre-seed funding with backing from firms including "
         "Seedcamp, AlbionVC' (DigitalHealth.London); the firm's post of 2026-07-07: 'Why We Invested in Resolyst'"))
L.append(fp("revox", "Pre-Seed", "seedcamp-leads-3m-funding-round-for-revox-developing-reliable-voice-ai-at-scale/", "2026-01-15",
    "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="Voice AI agents for outbound calls (FrenchWeb, 2026-01-15); the firm's post of 2026-01-15: 'excited to lead Revox's latest $3M pre-seed "
         "funding round'; the pre-filled acquired/CH is a one-word name join and is disputed; the firm's investment year is 2025"))
L.append(fp("riff", "Seed", "riff-raises-1-5m-to-revolutionise-remote-team-communication-through-voice-first-chat-tool/", "2020-08-20",
    "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Voice-first chat for remote teams (CEO Isabel Bescos); the firm's post of 2020-08-20: 'back Isabel and Matthew ... as part of a $1.5M seed "
         "round led by our friends at Balderton', as in the Balderton book; getriff.co answers; not the Riff in the Northzone book"))
L.append(fp("riskbook", "Pre-Seed", "riskbook-raises-2m-for-its-hyperconnected-marketplace-for-reinsurance-placement/", "2020",
    "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments", stage_conf="medium",
    note="Digital reinsurance marketplace; the firm's post of 2020-09-30: 'Since the pre-seed round we led', then the GBP 2m seed it backed with "
         "Episode 1 and MMC; riskbook.com does not answer; the pre-seed's date is not stated, hence medium"))
L.append(c("ritually", stage="undetermined", entry_date="2022", status="acquired", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["city_unknown"],
    note=f"Daily audio rituals for communities; {EXIT} (2022-2024, acquirer not named there); on no post read; the country is not established"))
L.append(c("robot-media", prog_at="2011", **loc("ES", "Barcelona"), status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    stage_conf="medium",
    note="Mobile apps and games studio (Barcelona; a Seedcamp Week 2010 finalist, one of the firm's 'two awesome Barcelona based teams' by 2011-10-04); "
         "no later trace found; " + FII))

if __name__ == "__main__":
    jl.write("batch-011", L)
