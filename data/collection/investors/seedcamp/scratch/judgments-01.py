"""PRO-83 grind, batch-001 (24symbols .. codility). Evidence: scratch/evidence-pack.py batch-001."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, verdict, rnd = jl.c, jl.loc, jl.verdict, jl.rnd
import re
class _Coh(dict):
    def __getitem__(self, k):
        return dict.__getitem__(self, re.sub(r"[^a-z0-9]", "", k.lower()))
COH = _Coh()
for r in json.loads((Path(__file__).resolve().parent.parent / "sources/site/views-cohorts.json").read_text())["rows"]:
    dict.__setitem__(COH, re.sub(r"[^a-z0-9]", "", r["name"].lower()), r)
V = "https://seedcamp.com/views/"


def pc(slug, name, country, city, **kw):
    """A programme-cohort row: Pre-Seed on its era's terms, location cited to the cohort post."""
    r = COH[name]
    return c(slug, prog_at=r["post_date"][:7], cohort=r["url"], **loc(country, city, r["url"]), **kw)


L = []
L.append(pc("24symbols", "24Symbols", "ES", "Madrid", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Ebook subscription reading service ('Spotify for books'); site live"))
L.append(c("9fin", status="private", **loc("GB", "London"), rng="1b_plus", usd=1300000000, val_src="web_verified",
    asof="2026-03-31", val_cite=V + "on-the-journey-with-9fin-from-day-one-to-their-1-3-billion-valuation/",
    stage="Pre-Seed", stage_src="first_party", stage_cite=V + "on-the-journey-with-9fin-from-day-one-to-their-50m-series-b/",
    stage_conf="high", entry_date="2017-03-17", focus="Fintech & Payments",
    note="AI analytics for debt capital markets; the firm's post: 'We first partnered with Steven and Huss in 2017, when we wrote their pre-seed cheque on St Patrick's Day'; $50M Series B (Highland Europe) Dec 2024; $170M Series C at $1.3B, Mar 2026 (the firm's post, Tech.eu, EU-Startups)",
    rounds=[jl.rnd("2017-03-17", "Pre-Seed", None, "Seedcamp", True, V + "on-the-journey-with-9fin-from-day-one-to-their-50m-series-b/", "firm"),
            jl.rnd("2024-12", "Series B", 50000000, "Highland Europe", True, V + "on-the-journey-with-9fin-from-day-one-to-their-50m-series-b/", "firm"),
            jl.rnd("2026-03-31", "Series C", 170000000, None, True, V + "on-the-journey-with-9fin-from-day-one-to-their-1-3-billion-valuation/", "firm")]))
L.append(pc("actionbar", "ActionBar", "IL", "Tel Aviv", status="unknown", rng="below_1b", focus="SaaS",
    note="In-app feature search for SaaS; site actionbar.io answers a Cloudflare error, no later trace found"))
L.append(pc("ai-build", "AI Build", "GB", "London", status="private", rng="below_1b", focus="Industrial & Robotics",
    note="AI for additive manufacturing; $8.5M Series A Oct 2023 (3D Printing Industry, voxelmatters)"))
L.append(pc("alterest", "Alterest", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Data and tools for private and asset-based credit; site live; Alterest Limited 09919781 active"))
L.append(pc("antavo", "Antavo", "HU", "Budapest", status="private", rng="below_1b", focus="SaaS",
    note="Loyalty program software; EUR 10M Series A Nov 2022 (PR Newswire); founded in Budapest, UK holding company in London"))
L.append(pc("appextras", "Appextras", "CA", None, status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["city_unknown"], note="In-app store for app cross-promotion (Canada/Brazil team, Mini Seedcamp NY 2011); no later trace found"))
L.append(pc("archivme", "Archivme", "FR", "Paris", status="unknown", rng="below_1b", focus="SaaS",
    note="Invoicing and budgeting tool (Seedcamp Paris 2011); no later trace found"))
L.append(c("askui", status="private", **loc("DE", "Karlsruhe"), rng="below_1b", focus="AI & Applied AI",
    stage="Seed", stage_src="first_party", stage_cite=V + "ai-powered-automation-software-askui-raises-e4-3-million-in-seed-funding/",
    stage_conf="high", entry_date="2023-09-04",
    note="AI agents for UI automation and testing; the firm's post of 2023-09-04 announces the EUR 4.3M seed round it backed (the list's investment year is 2023)",
    rounds=[jl.rnd("2023-09-04", "Seed", None, None, True, V + "ai-powered-automation-software-askui-raises-e4-3-million-in-seed-funding/", "firm")]))
L.append(pc("authentiq", "Authentiq", "NL", "Amsterdam", status="unknown", rng="below_1b", focus="Security",
    note="Passwordless authentication; authentiq.com does not answer; no later trace found"))
L.append(c("autone", status="private", **loc("GB", "London"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2022",
    note="AI inventory and operations platform for retail (London and Paris); the firm's post of 2022-06-30 announces the EUR 1.7M round it backed without naming it; $17M Series A (General Catalyst) Oct 2024",
    rounds=[jl.rnd("2022-06-30", None, None, None, True, V + "autone-raises-e1-7m-to-help-retail-cpg-businesses-make-better-operational-decisions/", "firm"),
            jl.rnd("2024-10-16", "Series A", 17000000, "General Catalyst", None, None, "press")]))
L.append(c("back", status="acquired", **loc("DE", "Berlin"), rng="below_1b", focus="SaaS",
    stage="Seed", stage_src="first_party", stage_cite=V + "the-future-of-work-according-to-back/", stage_conf="high", entry_date="2019-11-28",
    note="Employee-experience automation (backhq.com); the firm's post of 2019-11-28: 'excited to invest in Back, alongside our friends at Point Nine, as they announce their seed round'; the firm's 2022-2024 list marks it exited (acquirer not named on the list)"))
L.append(pc("basekit", "Basekit", "GB", "Cardiff", status="private", rng="below_1b", focus="SaaS",
    note="White-label website builder for hosting partners (founded in Chepstow, Wales); site live"))
L.append(pc("beeline", "Beeline", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    flags=["model_disputes_source"], clear=[],
    note="Bike navigation device (beeline.co); raised GBP 1M on Seedrs in 2022; the pre-filled public/JP float is a name collision with another Beeline and is disputed"))
L.append(c("ben", status="private", **loc("GB", "London"), rng="below_1b", focus="Fintech & Payments", stage="undetermined", entry_date="2019",
    note="Flexible employee benefits platform (thanksben.com, Berlin founding, London HQ); GBP 13M Series A (Atomico) 2022, GBP 20.8M Series B Dec 2025; Seedcamp's entry round not named on any surface read"))
L.append(pc("bilbus", "Bilbus", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Working-capital hub for small businesses (London and New York; Seedcamp New York 2011); no later trace found"))
L.append(c("blobr", status="private", **loc("FR", "Paris", V + "blobr-raises-e1-2m-to-empower-companies-to-customise-and-monetise-apis/"),
    rng="below_1b", focus="DevTools & APIs",
    stage="Pre-Seed", stage_src="first_party", stage_cite=V + "blobr-raises-e1-2m-to-empower-companies-to-customise-and-monetise-apis/",
    stage_conf="high", entry_date="2021-01-25",
    note="API monetisation layer, since repositioned as an AI ads assistant; the firm's post: 'We're excited to back Blobr in a EUR 1.2m pre-seed round'; $5.4M more in 2023 (TechCrunch)"))
L.append(c("bloomsbury", status="acquired", **loc("GB", "London"), rng="below_1b", focus="AI & Applied AI", stage="undetermined", entry_date="2017",
    note="Natural-language question answering (Bloomsbury AI); acq. by Facebook, 2018; the firm's 2018-2021 list marks it exited; the programme or seed entry is not named on any surface read"))
L.append(pc("blossom", "Blossom", "AT", "Vienna", status="unknown", rng="below_1b", focus="SaaS",
    note="Kanban project management for product teams (blossom.io, Vienna); site returns 404"))
L.append(pc("bluefields", "Bluefields", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Amateur sports organisation platform; no later trace found"))
L.append(pc("borrowmydoggy", "BorrowMyDoggy", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Dog-sharing community; site live; BorrowMyDoggy Limited 08339960 active"))
L.append(c("boundless", status="private", **loc("IE", "Dublin"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2019",
    flags=["model_disputes_source"],
    note="Employer-of-record platform (Dublin); the pre-filled US is a registrant join, the company is Irish; Seedcamp's entry round not named on any surface read"))
L.append(pc("brainient", "Brainient", "GB", "London", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Interactive video advertising (founded in Bucharest, later London); acq. by Teads, 2016; the firm's 2018-2020 list marks it exited"))
L.append(pc("branchtrack", "Branchtrack", "LV", "Riga", status="private", rng="below_1b", focus="SaaS",
    note="Branching-scenario training simulations; EUR 250K seed 2016 (EU-Startups); site live"))
L.append(pc("brandid", "BRANDiD", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Men's clothing subscription (Seedcamp London 2012); no later trace found"))
L.append(pc("bridgeu", "BridgeU", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="University and careers guidance platform for schools; acq. by Kaplan, 2021 (The PIE News), sold on to Manifest Global 2025"))
L.append(pc("buildcon", "Buildcon", "RS", "Belgrade", status="private", rng="below_1b", focus="SaaS",
    note="Construction management and logistics software (buildcontech.com, site live 2024)"))
L.append(pc("bukit", "Bukit", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Consumer debt settlement platform (2012); no later trace found"))
L.append(pc("buzztale", "BuzzTale", "LV", "Riga", status="unknown", rng="below_1b", focus="SaaS",
    note="Visual real-time stories, pivoted to enterprise (the firm's guest post 2014); no later trace found"))
L.append(pc("byebuy", "ByeBuy", "DE", "Berlin", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Consumer electronics rental (London/Berlin, 2015); no later trace found"))
L.append(c("cakewalk", status="private", **loc("DE", "Berlin"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2022",
    flags=["model_disputes_source"],
    note="Identity and access management for SMBs and AI agents; emerged from stealth with EUR 3M, Jun 2023 (Tech.eu; the firm's post); the round is not named; the pre-filled US is wrong, the company is in Berlin"))
L.append(pc("campalyst", "Campalyst", "LV", "Riga", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social media ROI measurement (Baltic team, moved to New York; 'we received our first investment from Seedcamp', the firm's 2012 post); no later trace found"))
L.append(pc("captini", "Captini", "GB", "London", status="defunct", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social WiFi analytics and monetisation; CAPTINI LIMITED (08628175) in liquidation (Companies House)"))
L.append(pc("car-quids", "Car Quids", "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Advertising on private cars; carquids.com does not answer"))
L.append(pc("cardlife", "Cardlife", "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Subscription management app; CARDLIFE LTD (09913815) dissolved 2018-11-27 (Companies House), cardlifeapp.com only redirects"))
L.append(pc("cashtag", "Cashtag", "PT", "Lisbon", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Mobile payment network (Seedcamp Week Berlin 2013); no later trace found"))
L.append(c("cerbos", status="private", **loc("GB", "London"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2021",
    note="Open-source authorisation layer (co-founder Emre Baran was a Seedcamp Expert in Residence); the firm's post of 2023-04-13 announces the $7.5M seed; the list's investment year is 2021, so that post may describe a follow-on and the entry round is not named"))
L.append(c("certifaction", status="private", **loc("CH", "Zurich"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2020",
    note="Privacy-first e-signatures; site live; Seedcamp's entry round not named on any surface read"))
L.append(c("charlie-hr", status="private", **loc("GB", "London", COH["Charlie HR"]["url"]), rng="below_1b", focus="SaaS",
    stage="Seed", stage_src="first_party", stage_cite=COH["Charlie HR"]["url"], stage_conf="medium", entry_date="2016-04",
    note="HR software for small businesses; the firm's post of 2016-04-08 welcomes CharlieHR noting 'The team recently announced a GBP 1M Seed Round', so the entry is that seed rather than the standard cheque"))
L.append(pc("checkthis", "Checkthis", "BE", "Brussels", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Micro-publishing tool (2012); no later trace found"))
L.append(pc("clause", "Clause", "US", "New York", status="acquired", rng="below_1b", focus="SaaS",
    note="Smart legal contracts (Nextlaw Labs callout, 2016); acq. by DocuSign, 2021"))
L.append(c("clubzero", status="private", **loc("GB", "London"), rng="below_1b", focus="Climate & Energy", stage="undetermined", entry_date="2018",
    note="Reusable food and drink packaging system; site live; Seedcamp's entry round not named on any surface read"))
L.append(c("codacy", status="private", **loc("PT", "Lisbon"), rng="below_1b", focus="DevTools & APIs", stage="undetermined", entry_date="2012",
    note="Automated code review; $15M round Sep 2022 (TechCrunch); the list gives 2012 but the firm's 2012-2017 lists do not carry it, so the entry is not dated and its round is not named"))
L.append(pc("codeship", "Codeship", "US", "Boston", status="acquired", rng="below_1b", focus="DevTools & APIs",
    note="Hosted continuous delivery (founded in Vienna as Railsonfire, later Boston); acq. by CloudBees, 2018; the firm's 2018-2021 list marks it exited"))
L.append(pc("codility", "Codility", "PL", "Warsaw", status="private", rng="below_1b", focus="SaaS",
    note="Technical hiring assessments; $22M Series A (Oxx, Kennet) Jan 2020; HQ London and Warsaw"))

if __name__ == "__main__":
    jl.write("batch-001", L)
