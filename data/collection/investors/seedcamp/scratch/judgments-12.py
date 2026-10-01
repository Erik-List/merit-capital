"""PRO-83 grind, batch-012 (rock-pamper-scissors .. trait-perception); social was judged in batch-008.
Taxfix is the acquirer of TaxScouts (decisions.md D5), and Teleportd renamed itself Totems."""
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
L.append(pc("rock-pamper-scissors", "Rock Pamper Scissors", "GB", "London", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Hairdresser and salon booking (January 2016 cohort); 'Rock Pamper Scissors, the hairdresser booking app backed by Seedcamp and 500 Startups, "
         "shutters' (TechCrunch, 2017-03-16)"))
L.append(und("rodeo", 2021, "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Super-app for gig-economy riders (gorodeo.app, which now offers career planning); the pre-filled acquired/JP is a one-word Wikidata join "
         "and is disputed; the 2021 entry round is not named"))
L.append(und("runwhen", 2023, "US", "San Francisco", status="private", rng="below_1b", focus="DevTools & APIs",
    note="AI assistants for cloud troubleshooting (founder Kyle Forster); site live; the 2023 entry round is not named"))
L.append(und("ryders", 2021, "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="On-demand riders for last-mile delivery (Ryders, renamed Ryde; GBP 2.5M seed 2021 led by Forward Partners and Triple Point with the firm as "
         "an existing investor, UKTN); ryders.team does not answer; the entry round is not named"))
L.append(fp("sable-bio", "Pre-Seed", "sable-bio-raises-1-5m-pre-seed-round-to-make-drug-discovery-safer-and-more-efficient/", "2024-02-06",
    "GB", "London", V + "sable-bio-raises-1-5m-pre-seed-round-to-make-drug-discovery-safer-and-more-efficient/", status="private",
    rng="below_1b", focus="Healthcare & Bio",
    note="Target safety assessment for drug discovery ('a London-based tech bio startup'); the firm's post of 2024-02-06: 'Sable Bio raises GBP 1.5m "
         "pre-seed round', which the firm joined with Episode1; $3.75M seed Feb 2026 (Pulse 2.0)"))
L.append(und("safara", 2020, "US", "Los Angeles", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Hotel booking with cashback (Safara, founders Maya Poulton and Joey Kotkins); the original company shut down during COVID and the Resy founders "
         "bought its remnants in 2021 (Safara Travel, Inc., Los Angeles; $14M Dec 2024); whether the firm's holding carried over is not shown; "
         "no round named"))
L.append(und("se3", 2024, "DE", "Munich", status="private", rng="below_1b", focus="AI & Applied AI",
    note="3D spatial AI (SE3 Labs, founders from TU Munich and ETH Zurich); site live; the 2024 entry round is not named"))
L.append(und("sense-street", 2020, "GB", "London", cite="https://sensestreet.com", status="private", rng="below_1b", focus="Fintech & Payments",
    note="GenAI for capital markets communications (1 Phipp Street, London, and Krakow); the 2020 entry round is not named"))
L.append(und("sherpa", 2026, "DE", "Munich", cite=V + "sherpa-raises-2-2m-to-build-the-ai-operating-system-for-tomorrows-workforce/",
    status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI agents for external workforce management ('a Munich-based startup'); the firm's post of 2026-07-09: 'We're proud to lead their round' "
         "($2.2M, no round word)"))
L.append(und("sidekick", 2022, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Active investment management for retail investors ('the UK-based company'; sidekickmoney.com live); the firm's post of 2022-10-27: 'Sidekick "
         "raises GBP 3.33M ... we are excited to back Sidekick' (no round word)"))
L.append(c("simpo", stage="undetermined", entry_date="2016", status="unknown", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="SaaS growth platform (simpo.io, which does not answer); on the firm's lists 2018-2024 under a 2016-06 logo, on no post read; the country "
         "is not established"))
L.append(fp("singulate", "Pre-Seed", "singulate-raises-2-3-million-to-create-the-future-of-large-scale-communication-with-ai/", "2024-10-08",
    "US", "Baltimore", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Generative-AI email personalisation (founders ex-Hopin; Baltimore, MD); the firm's post of 2024-10-08: 'excited to participate in Singulate's "
         "$2.3 million pre-seed round led by Bowery Capital'"))
L.append(c("sitejam", prog_at="2014-03", status="unknown", rng="below_1b", focus="SaaS", stage_conf="medium", flags=["city_unknown"],
    note="SiteJam; on the firm's list only in 2014, on no post read; no later trace found; the country is not established; " + FII14))
L.append(und("skyflow", 2023, "DE", None, status="private", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="Automated drone networks for fire-brigade situation reconnaissance (flyskyflow.com, German-language, live); the Skyflow privacy API company in "
         "the news pack is a namesake; the 2023 entry round is not named"))
L.append(und("source-dev", 2024, "GB", "London", cite="https://source.dev", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Software updates for smart devices (85 Great Portland Street, London, the site's footer); the 2024 entry round is not named"))
L.append(und("spacious", 2014, "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online marketplace for renting office space ('raised their seed round', the firm's newsletter of 2014-10-29); first on the firm's list in "
         "Dec 2014, after Seedcamp III began, so no programme terms; no round tied to the firm"))
L.append(und("spektr", 2023, "DK", "Copenhagen", cite=V + "spektr-launches-with-e5m-in-funding-to-streamline-ongoing-due-diligence/",
    status="private", rng="below_1b", focus="Fintech & Payments",
    note="Compliance automation for financial services ('The Copenhagen-based fintech'); the firm's post of 2024-02-21: 'spektr launches with EUR 5M "
         "in funding' (no round word); $20M Series A led by NEA, Apr 2026 (Finextra)"))
L.append(und("splash", "2016-07", "DE", "Berlin", cite=V + "announcing-our-investment-in-splashvr/", status="unknown", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="360 video camera app and VR community ('an ambitious Berlin-based team'); the firm's post of 2016-07-01: 'its investment into Splash, who this "
         "week announced their $2.5m fundraise' (no round word); splashapp.co does not answer; the pre-filled acquired is a one-word Wikidata join"))
L.append(sc("splittable", "Splittable", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Shared household bills and expenses; on the firm's Fund III seed list (2015-09-21); no later trace found"))
L.append(und("spotlock", 2022, "US", "New York", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Commodity price risk management for industrial buyers (founded Jun 2022; New York with an office in Israel); site live; no round named"))
L.append(fp("stackfix", "Seed", "stackfix-raises-3m-to-build-the-ultimate-software-comparison-platform-for-smbs/", "2024-12-03",
    "GB", "London", V + "stackfix-raises-3m-to-build-the-ultimate-software-comparison-platform-for-smbs/", status="private", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="AI software comparison for SMBs ('the London-based company'); the firm's post of 2024-12-03: 'partner with Paddy and Camin from Day One and "
         "participate in Stackfix's $3 million Seed funding round'"))
L.append(und("streambased", 2023, "GB", "London", cite=CH + "14709247", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Kafka and Iceberg in one real-time view; the firm's post of 2024-01-08: 'Streambased raises $800K ... excited to back Streambased' "
         "(no round word)"))
L.append(pc("subscrib", "Subscrib", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Subscription billing (SeedPeek, April 2013); no later trace found"))
L.append(und("sunrise", 2023, "SI", "Ljubljana", cite=V + "sunrise-robotics-raises-8-5m-to-transform-the-future-of-industrial-manufacturing-with-simulation-trained-robots/",
    status="private", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="Simulation-trained industrial robot cells (Sunrise Robotics, 'based in Ljubljana, Slovenia'; founder Tomaz Stolfa); the firm's post of "
         "2025-06-13 covers the $8.5M raise without naming its entry round; the pre-filled acquired/JP is a weak CIK and one-word Wikidata join"))
L.append(und("supercede", 2019, "GB", "London", cite="https://supercede.com", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Reinsurance data and deal platform (Supercede Technology Ltd, 68 King William Street, London); the 2019 entry round is not named"))
L.append(c("tab", prog_at="2012", **loc("GB", "London"), status="defunct", rng="below_1b", focus="Fintech & Payments", stage_conf="medium",
    note="Pay-by-phone bar and restaurant tabs (founder Shawn Zvinis); 'Shawn and the Tab team joined the Seedcamp family ... Tab shutdown' (the firm's "
         "post of 2014-06-12); " + FII))
L.append(c("tano", stage="undetermined", entry_date="2025-11", **loc("GB", "London", V + "tano-announces-their-angel-round-to-enable-end-to-end-influencer-marketing-automation-for-fmcg-brands/"),
    status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI influencer-marketing engine for FMCG brands ('The London-based company'); the firm's post of 2025-11-24: 'a Day One investor ... lead their "
         "round', titled an 'inception round' (an angel round in the link), which is not a stage the book uses"))
L.append(fp("tattvam", "Pre-Seed", "tattvam-raises-1-7m-to-bring-software-speed-agility-to-chip-design/", "2026-02-25", "GB", "London",
    V + "tattvam-raises-1-7m-to-bring-software-speed-agility-to-chip-design/", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI for chip design ('London-based Tattvam AI', with a team in Chennai); the firm's post of 2026-02-25: '$1.7 million in pre-seed funding, led "
         "by Seedcamp'; the firm's investment year is 2025"))
L.append(jl.verdict("taxfix", "not_member",
    "the acquirer of a portfolio company (decisions.md D5; Erik 2026-09-22 sale-consideration ruling): the live list's Taxfix card, investment year "
    "2018, carries TaxScouts's own line 'Digital tax advisor that offers online tax preparation services' (the firm's 2020-2024 lists, TaxScouts) and "
    "taxscouts' site now reads 'Taxfix (formerly TaxScouts)'; no post or filing shows a separate investment in Taxfix, so the holding is the "
    "consideration for TaxScouts, which is the member", ec="site_listing", cite="https://seedcamp.com/our-companies/#taxfix"))
L.append(fp("taxscouts", "Seed", "1-2m-for-taxscouts-making-fears-around-filing-your-tax-return-a-thing-of-the-past/", "2019-01-22",
    "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Online tax returns with accountants; the firm's post of 2019-01-22: 'We're delighted to invest in the GBP 1.2m seed round alongside Speedinvest "
         "and Finch Capital'; GBP 5M Series A Aug 2020 (Yahoo Finance); acq. by Taxfix (taxscouts now redirects: 'Taxfix (formerly TaxScouts)')"))
L.append(und("taxtris", 2022, "GB", "London", status="unknown", rng="below_1b", focus="Crypto & Web3",
    note="Tax automation and reporting API for digital-asset platforms; on the firm's lists 2022-2024, on no post read; no round named"))
L.append(c("telemachus", stage="undetermined", entry_date="2026", status="private", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="Builds AI-native competitors to poorly run incumbents (telemachus.io, live); the 2026 entry round is not named; the country is not established"))
for s in ("totems", "teleportd"):
    L.append(c(s, prog_at="2011", **loc("FR", "Paris", "https://thenextweb.com/news/can-instagram-analytics-be-a-business-teleportd-lands-1m-to-give-it-a-shot-with-nitrogram"),
        status="acquired", rng="below_1b", focus="Media, Gaming & Advertising", stage_conf="medium",
        note="Teleportd (Paris; real-time photo search), then Nitrogram and TOTEMS, Instagram marketing analytics ('TOTEMS, a marketing tools and data "
             f"analytics company which we invested in back in 2011, and which was eventually acquired by Stripe in 2014', the firm's 2026 Dust post); {EXIT}; "
             + FII + ("" if s == "totems" else "; duplicate of totems (identity-merges.json)")))
L.append(und("the-engineering-company", 2017, "GB", None, status="unknown", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="AI-driven engineering design ('Radically faster, cheaper engineering design'); on the firm's lists 2018-2022 under a 2017-08 logo, on no post "
         "read; no round named"))
L.append(und("thirdeye", 2016, "GB", "London", status="defunct", rng="below_1b", focus="AI & Applied AI",
    note="Computer vision for retail (ThirdEye Labs; the firm's 2016-2017 AI posts); THIRDEYE LABS LIMITED 09864208 dissolved 2024-02-01 "
         "(Companies House); thirdeye.io answers with an empty page; no round named"))
L.append(fp("tick", "Pre-Seed", "tick-investment-done/", "2019-04-01", "GB", "London", status="unknown", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="How-to micro-video platform (from Zinc, London); the firm's post of 2019-04-01: 'We are incredibly excited to invest in the team and lead their "
         "pre-seed round'; tick.co does not answer; the pre-filled SK is a one-word Wikidata join"))
L.append(und("tilt", 2021, "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Live shopping and auctions app (Revolut alumni; tilt.app live, UK and Europe); the firm's post of 2022-09-22: 'participate in Tilt's $3m "
         "funding round' (no round word); $18M Series A Aug 2024 (TechCrunch); the pre-filled acquired/US is a weak CIK and one-word Wikidata join "
         "(other Tilts: the crowdfunding site Airbnb bought, the Brazilian credit Tilt)"))
L.append(und("timetrace-labs", 2025, "GB", "London", cite=CH + "16471610", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="AI for data-scarce real-world systems (TimeTrace Labs Ltd, London); the 2025 entry round is not named"))
L.append(c("tl-dr", prog_at="2012-12", **loc("FR", "Paris", "https://thenextweb.com/news/seedcamp-invests-in-knowable-org-tldr-and-unifyo-after-its-paris-event"),
    status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Crowdsourced summaries of web pages (Paris); 'Seedcamp invests in Knowable.org, tl;dr and Unifyo after its Paris event' (TNW, 2012-12-19); "
         "no later trace found"))
L.append(und("tomato-pay", 2019, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="QR-code payments and invoicing for small businesses and sole traders; on the firm's lists from 2021 (logo 2019-08); no round named"))
L.append(fp("topograph", "Seed", "seedcamp-leads-topographs-e2m-seed-to-fix-the-broken-infrastructure-behind-global-kyb/", "2026-03-20",
    "FR", "Paris", status="private", rng="below_1b", focus="Fintech & Payments",
    note="KYB data and documents from official registers (founded 2024 in Paris; Fintech Global); the firm's post of 2026-03-20: 'Seedcamp leads "
         "Topograph's EUR 2M seed'; the firm's investment year is 2025"))
L.append(c("tph", stage="undetermined", entry_date="2018", status="unknown", rng="below_1b", focus="Consumer & Marketplaces", flags=["city_unknown"],
    note="Vintage clothing marketplace (tph.co, empty page); on the firm's lists 2018-2019 only, on no post read; the country is not established"))
L.append(pc("trait-perception", "Trait Perception", "ES", "Madrid", status="unknown", rng="below_1b", focus="SaaS",
    note="Personality insights from social data (Mini Seedcamp Berlin 2012 winner, 'Berlin '12 - Meet the 2 winners'); no later trace found"))

if __name__ == "__main__":
    jl.write("batch-012", L)
