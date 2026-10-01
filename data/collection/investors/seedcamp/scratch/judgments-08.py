"""PRO-83 grind, batch-008 (wave .. catch), plus the two acquirer-page scrape artifacts and three duplicates."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
CLS = json.loads((Path(__file__).resolve().parent.parent / "companies/classification.json").read_text())


def fp(slug, stage, url, date, country, city, cite=None, **kw):
    kw.setdefault("stage_conf", "high")
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, entry_date=date,
             **loc(country, city, cite), **kw)


def und(slug, year, country, city, note, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city), note=note, **kw)


def dup(slug, canonical, name):
    """A duplicate slug judged exactly as its canonical row (identity-merges.json folds it at the rebuild)."""
    r = {k: v for k, v in CLS[canonical].items() if k not in ("slug", "who")}
    r.update({"slug": slug, "who": jl.WHO})
    r["note"] = r.get("note", "") + f"; duplicate of {canonical} ({name}; identity-merges.json)"
    return r


L = []
# scrape artifacts: the /acquirer/ page template's footer headings, read as a company before the cc-parse.py fix
for s, h in (("social", "Social"), ("address", "Address")):
    L.append(jl.verdict(s, "not_member",
        f"not a company: the footer heading '{h}' of the firm's /acquirer/<name>/ page template, read as the acquired "
        "company's name before scratch/cc-parse.py was fixed to take only a heading before 'This company has been acquired'; "
        "the re-parse yields no such row"))

L.append(fp("wave", "Seed", "thewavevr-investment/", "2016-08-05", "US", "Los Angeles", status="private", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["model_disputes_source"],
    note="Virtual concerts (TheWaveVR, renamed Wave); the firm's post of 2016-08-05: 'Seedcamp joins $2.5m seed investment in TheWaveVR'; "
         "$30M Jun 2020 (The Hollywood Reporter), Tencent investment Nov 2020; the VR app closed in 2021 and the new Wave opened a closed beta "
         "in Oct 2024 (mixed-news.com); the pre-filled acquired/public float is a weak CIK name join and is disputed"))
L.append(c("wealthkernel", stage="undetermined", entry_date="2015", **loc("GB", "London", CH + "09686970"), status="acquired",
    rng="below_1b", focus="Fintech & Payments",
    note="Investment infrastructure API (wealth management as a service); a Seedcamp Week London attendee (2015-02-03) with the firm's "
         "investment year 2015 and on no cohort post read, so the entry round is not named; GBP 6M Series A Jan 2024 (Crowdfund Insider); "
         "acq. by Alpaca, agreed Jul 2025, completed Apr 2026 (Business Wire)"))
L.append(c("weavr", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finextra.com/newsarticle/37015/embedded-banking-startup-weavr-raises-4-million-in-seed-funding",
    entry_date="2020-11", **loc("GB", "London"), status="private", rng="below_1b", focus="Fintech & Payments",
    note="Embedded finance for B2B SaaS; the firm's post of 2020-12-07 'Weavr raises $4m' names no round, Finextra of 2020-11-25: "
         "'Weavr raises $4 million in seed funding'; the firm's investment year is 2020"))
L.append(c("wefox", prog_at=None, stage="undetermined", entry_date="2015",
    **loc("DE", "Berlin", V + "wefox-group-europes-leading-insurtech-company-raises-125m-series-b/"), status="private",
    focus="Fintech & Payments",
    note="Insurtech (FinanceFox, Zurich, folded into wefox Group, Berlin); the firm lists it with investment year 2015 and names Finance Fox "
         "in its January 2016 cohort post, but its own post of 2016-04-19 says Finance Fox 'raised a $5.5M Series A led by Salesforce "
         "Ventures in 2015', so the standard cheque is not shown and the entry round is not named; $125M Series B 2019 (the firm's post); "
         "the band stays as pre-filled"))
L.append({**L[-1], "slug": "finance-fox", "note": L[-1]["note"] + "; duplicate of wefox (wefox; identity-merges.json)"})
L.append(pc("wevat", "Wevat", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Digital VAT refunds for tax-free shopping (January 2017 cohort; 'pre-seed investment into ... WeVat', the firm's 2017 review); site live"))
L.append(pc("winnow", "Winnow", "GB", "London", status="private", rng="below_1b", focus="Climate & Energy",
    note="AI food-waste metering for commercial kitchens (Winnow Solutions, Seedcamp Week London 2013); $20M 2019 (Hotelier Middle East), "
         "ABC Impact investment Mar 2024 (PR Newswire)"))
L.append(pc("wise", "Wise", "GB", "London", status="public", focus="Fintech & Payments", flags=["needs_web_value"],
    note="International money transfer (TransferWise, renamed Wise 2021; Mini Seedcamp London Aug 2011, 'Straight out of Mini Seedcamp London'); "
         "LSE direct listing Jul 2021 (the firm's post); the hq_country_claim (GB) is confirmed from the cohort post; the cap is pinned in the A/B pass"))
L.append(pc("wordy", "Wordy", "DK", "Copenhagen", status="private", rng="below_1b", focus="SaaS",
    note="Human proofreading and copy-editing (Seedcamp Week 2010 winner, Copenhagen; later London, WORDY LIMITED 07443366 active); wordy.com live"))
L.append(pc("wriggle", "Wriggle", "GB", "Bristol", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Last-minute deals at local restaurants and bars (Seedcamp Week London 2014); 'Bristol restaurant app Wriggle closes down for good' (Bristol Post, 2022-07-31)"))
L.append(c("yavin", stage="undetermined", entry_date="2021", **loc("FR", "Paris"), status="private", rng="below_1b", focus="Fintech & Payments",
    note="Android payment terminals for merchants; the firm's post of 2022-02-24: 'Just six months after leading their initial EUR 1.2M round' "
         "(no round word), then the EUR 5M round alongside New Wave"))
L.append(pc("yodeltalk", "YodelTalk", "AT", "Vienna", status="unknown", rng="below_1b", focus="SaaS",
    note="Business phone numbers inside team chat (June 2016 cohort; YODELTALK LIMITED 10230818 still registered in London); yodel.io does not answer"))
L.append(fp("yonder", "Pre-Seed", "yonder-launches-with-20m-seed-round-to-rebuild-peoples-relationship-with-credit/", "2021-02",
    "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Rewards credit card (London); the firm's post of 2022-03-31: 'a pre-seed round we led of GBP 850k in February 2021'; GBP 20M seed 2022, "
         "GBP 23.4M Sep 2024 (Finextra); the pre-filled US is a one-word Wikidata join and is corrected"))
L.append(c("zamna", stage="undetermined", entry_date="2017", **loc("GB", "London"), status="private", rng="below_1b", focus="Security",
    note="Passenger identity and document verification for airlines; $5M Oct 2019 (City A.M.), SITA partnership 2023, Iberojet 2025 (eTurboNews); "
         "the 2017 entry round is not named"))
L.append(pc("zemanta", "Zemanta", "SI", "Ljubljana", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note=f"Content recommendation and native ads (Seedcamp 2007 winner); acq. by Outbrain, 2017; {EXIT}"))
L.append(pc("zercatto", "Zercatto", "PT", "Porto", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Social investing: follow the best traders (Seedcamp Week Berlin 2013); on the firm's lists only 2013-2014; no later trace found"))
L.append(c("zin-gl", prog_at=jl.coh("Zin.gl")["post_date"][:7], cohort=jl.coh("Zin.gl")["url"], country="RU", country_src="web_verified",
    country_cite=jl.coh("Zin.gl")["url"], flags=["city_unknown"], status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Social-graph online dating ('Hailing from Russia, and having their eyes set on the US market', Seedcamp New York 2011); no later trace found"))
L.append(c("zinc", stage="undetermined", entry_date="2021", **loc("GB", "London"), status="private", rng="below_1b", focus="Security",
    note="Automated reference and background checks (zincwork.com, live); not Zinc VC, the London venture builder the firm's posts also name; "
         "the 2021 entry round is not named"))
L.append(c("acasa", stage="undetermined", entry_date="2018", **loc("GB", "London"), status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Household bill splitting and management (helloacasa.com, live); on the firm's lists from 2018, on no post read"))
L.append(fp("adia", "Pre-Seed", "welcome-adia-on-a-mission-to-revolutionise-reproductive-health-for-women/", "2018-09-27", "GB", "London",
    status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Women's reproductive health platform (Adia Health, founded 2018 through Zinc); the firm's post of 2018-09-27: 'we are delighted to invest "
         "in their pre-seed round'; on the firm's lists only 2018-2020, adiahealth.com does not answer"))
L.append(c("agamon-health", stage="undetermined", entry_date="2019", country="IL", country_src="web_verified",
    country_cite=V + "founder-qa-with-michal-meiri-ceo-of-health-tech-company-agamon/", city="Tel Aviv", city_src="model_knowledge",
    status="private", rng="below_1b", focus="Healthcare & Bio",
    note="NLP on unstructured medical reports ('an Israeli health tech company', the firm's Q&A of 2020-07-06); site live; the 2019 entry round is not named"))
L.append(pc("albia", "Albia", "BA", "Sarajevo", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Testadon automated software testing (Seedcamp Week 2010 winner); no later trace found"))
L.append(c("amiqa", stage="undetermined", entry_date="2020", **loc("GB", "London"), status="private", rng="below_1b", focus="DevTools & APIs",
    note="Autonomous web testing (the firm's 2021 devtools post), since repositioned as automation for small hotels (amiqa.io, live); "
         "AMIQA LIMITED 12129420 dissolved 2023; the 2020 entry round is not named"))
L.append(c("andel", stage="undetermined", entry_date="2025", **loc("US", "New York", "https://www.alleywatch.com/2025/10/andel-prescription-drug-pharmacy-benefit-cooperative-employer-medication-platform-glp/"),
    status="private", rng="below_1b", focus="Healthcare & Bio", flags=["model_disputes_source"],
    note="Employer-backed medication marketplace (GLP-1s); the firm's post of 2025-10-20: 'thrilled to participate in Andel's $4.5 million funding round' "
         "(no round word); the pre-filled DK is a one-word Wikidata join and is corrected"))
L.append(pc("anvajo", "Anvajo", "DE", "Dresden", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Handheld molecular diagnostics (June 2016 cohort); EUR 17.7M 2022 (Deutsche Startups), clinical study press 2025 (PresseBox)"))
L.append(pc("api-changelog", "API Changelog", "GB", "London", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="API change notifications for developers (September 2015 cohort, London and Barcelona); apichangelog.com does not answer"))
L.append(c("apoha", stage="undetermined", entry_date="2023", **loc("GB", "London", CH + "13344316"), status="private", rng="below_1b",
    focus="AI & Applied AI", note="Neuromorphic sensing ('liquid brain'); site live; the 2023 entry round is not named"))
leg = CLS.get("legal-tender", {})
L.append(pc("apperio", "Legal Tender", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="Legal spend analytics (Legal Tender, Seedcamp Week London 2013, renamed Apperio 2014); now part of PERSUIT (apperio.com redirects: "
         "'Apperio is now part of PERSUIT')"))
L.append(pc("legal-tender", "Legal Tender", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="Legal spend analytics (renamed Apperio 2014); now part of PERSUIT; duplicate of apperio (Apperio; identity-merges.json)"))
L.append(fp("appwrite", "Seed", "an-open-source-alternative-to-googles-firebase-our-investment-in-appwrites-10m-seed-round/", "2021-09-28",
    "IL", "Tel Aviv", status="private", rng="below_1b", focus="DevTools & APIs", stage_conf="medium",
    note="Open-source backend server; the firm's post of 2021-09-28: 'a $10 million seed round led by Bessemer Venture Partners and Flybridge, "
         "with participation from us at Seedcamp'; the firm's investment year reads 2020 (the round closed before its announcement), hence medium"))
L.append(fp("arcjet", "Seed", "arcjet-raises-3-6m-seed-funding-to-help-developers-protect-their-apps-in-production/", "2024-09-10",
    "GB", "London", status="private", rng="below_1b", focus="Security", stage_conf="medium",
    note="Security SDK for developers (David Mytton, formerly Server Density); the firm's post of 2024-09-10: 'Arcjet raises $3.6M seed funding ... "
         "why we invested in Arcjet'; the firm's investment year reads 2023, hence medium; ARCJET LTD 14882009"))
L.append(fp("argil", "Pre-Seed", "argil-raises-e4-9-million-to-empower-everyone-to-become-a-creator-using-their-own-ai-video-clone/", "2023",
    "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI video clones for creators; the firm's post of 2024-11-29: 'having led their EUR 1 million Pre-Seed round in 2023 alongside Axeleo'; "
         "EUR 3.9M seed led by EQT Ventures 2024"))
L.append(pc("avalio", "Avalio", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Find and meet local freelancers (June 2016 cohort); no later trace found"))
L.append(c("baserow", stage="undetermined", entry_date="2020", **loc("NL", "Amsterdam"), status="private", rng="below_1b", focus="DevTools & APIs",
    note="Open-source no-code database (Baserow B.V.); the hq_country_claim (NL) is confirmed from the company's own record; the 2020 entry round is not named"))
L.append(c("beagle", stage="undetermined", entry_date="2017", **loc("CA", "Ottawa"), status="unknown", rng="below_1b", focus="AI & Applied AI",
    flags=["model_disputes_source"],
    note="AI contract review (Beagle.ai); 'we have welcomed into our Seedcamp portfolio HubbleHQ, Opensensors.io, and Beagle.ai' (the firm's post "
         "of 2017-03-30 launching Concrete, its proptech initiative); beagle.ai answers with an empty page; the pre-filled acquired/public float "
         "is a weak CIK name join and is disputed"))
L.append(fp("bioorbit", "Seed", "bioorbit-raises-13-2m-in-the-worlds-largest-seed-round-for-space-manufacturing/", "2026-04-30",
    "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Drug crystallisation in microgravity; the firm's post of 2026-04-30: 'BioOrbit raises $13.2m in the world's largest seed round' and "
         "'we're deeply proud to back BioOrbit in their $13.2m raise'; BIOORBIT LTD 15035829; the hq_country_claim (GB) is confirmed"))
L.append(c("bookend", stage="undetermined", entry_date="2023", **loc("US", "Bellevue"), status="private", rng="below_1b", focus="Healthcare & Bio",
    note="AI autopilot for specialty medical practices (Bellevue, WA), which began as generative-AI security for developers (the firm's "
         "2024 posts name it among its Fund VI security investments); the 2023 entry round is not named"))
L.append(fp("botika", "Seed", "botika-launches-ai-generated-fashion-model-mobile-app-with-8m-in-seed-funding/", "2023",
    "IL", "Tel Aviv", V + "botika-launches-ai-generated-fashion-model-mobile-app-with-8m-in-seed-funding/",
    status="private", rng="below_1b", focus="AI & Applied AI", stage_conf="medium",
    note="AI fashion model imagery for apparel e-commerce ('the Tel Aviv-based company'); the firm's post of 2025-01-17: 'part of Botika's journey "
         "from Day One and participate in their $8 million seed funding round'; the firm's investment year is 2023, hence medium"))
L.append(dup("boxed-ice", "server-density", "Server Density"))
L.append(c("buffalogrid", stage="undetermined", entry_date="2018-12", **loc("GB", "London"), status="defunct", rng="below_1b",
    focus="Climate & Energy",
    note="Solar phone charging and connectivity for off-grid users; the firm's post of 2018-12-12: 'our investment ... as part of their GBP 3.4m round' "
         "led by LocalGlobe (no round word); BUFFALOGRID LTD 07858813 dissolved 2025-07-26 (Companies House)"))
L.append(fp("bunkerex", "Pre-Seed", "2017-year-in-review/", "2017", "GB", "London", status="unknown", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Online marketplace for ship fuel; the firm's 2017 review: 'a new pre-seed investment in BunkerEx'; the domain now serves unrelated content"))
L.append(fp("buynomics", "Seed", "our-investment-in-buynomics-2-6m-seed-round-to-build-the-leading-global-solution-for-commercial-insights/",
    "2021-08-02", "DE", "Cologne", status="private", rng="below_1b", focus="SaaS",
    note="Pricing and assortment simulation; the firm's post of 2021-08-02: 'backed ... from buynomics' seed round' ($2.6M); EUR 13M Series A "
         "Nov 2022 (PR Newswire), $30M Mar 2025"))
L.append(pc("carbon-voyage", "Carbon Voyage", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Logistics efficiency software (Seedcamp Week London 2014); the site sits behind a bot check"))
L.append(c("cargoflip", stage="undetermined", entry_date="2021", **loc("GB", "London"), status="unknown", rng="below_1b", focus="SaaS",
    note="Digital trade assistant for SME importers and exporters (Entrepreneur First; the firm's Q&A of 2021-01-08); cargoflip.com does not answer; "
         "the entry round is not named"))
L.append(fp("catch", "Seed", "catch-ai-raises-5m-to-build-the-ai-agent-for-busy-executives/", "2026-09-02",
    "IL", "Tel Aviv", "https://dealroom.co/news/148442-ex-entr-e-investor-raises-5m-seed-for-ai-admin-agent-catch/",
    status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI executive assistant (Catch AI, Tel Aviv, Dealroom); the firm's post of 2026-09-02: 'backing Catch AI ... in their $5 million seed round'"))
L = [x for x in L if x]

if __name__ == "__main__":
    jl.write("batch-008", L)
