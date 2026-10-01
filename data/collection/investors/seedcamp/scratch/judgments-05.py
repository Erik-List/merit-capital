"""PRO-83 grind, batch-005 (oratio .. reposit)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"


def fp(slug, stage, url, date, country, city, **kw):
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, stage_conf="high", entry_date=date,
             **loc(country, city), **kw)


def und(slug, year, country, city, note, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city), note=note, **kw)


L = []
L.append(pc("oratio", "Oratio", "AT", "Vienna", status="unknown", rng="below_1b", focus="SaaS",
    note="Customer service over messaging apps (2016); orat.io does not answer"))
for s in ("orbital",):
    L.append(und(s, 2019, "GB", "London", status="private", rng="below_1b", focus="AI & Applied AI",
        note="Orbital (Orbital Witness until its rename), AI for real-estate legal diligence; the firm's post of 2019-05-16 announces a GBP 1.2m round without a round word; GBP 3.3M seed Jul 2020, $60M Series B Jan 2026 (the firm's post)"
             + ("" if s == "orbital" else "; duplicate of orbital (identity-merges.json)"),
        rounds=[rnd("2019-05-16", None, None, None, True, V + "orbital-witness-raises-1-2m-to-fully-automate-legal-risk-assessments-on-land-and-property/", "firm")]))
L.append(pc("oust-me", "Oust.me", "SI", "Ljubljana", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Gaming layer on location check-ins (Mini Seedcamp Ljubljana 2011); no later trace found"))
L.append(und("outverse", 2021, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Community platform turned AI customer support (founded by a Seedcamp investment-team alumnus); the firm's post of 2022-05-27 announces GBP 1m without a round word; $6M Jul 2023 (Tech.eu)"))
L.append(fp("pace", "Seed", "seedcamp-deploys-first-capital-from-fourth-fund-into-pace-matching-hotel-pricing-to-real-time-demand/",
    "2017-12-14", "GB", "London", status="acquired", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="Hotel revenue management; the firm's post of 2017-12-14: 'the first investment from our fourth fund into Pace as part of a GBP 2.5 million seed round'; acq. by FLYR, Sep 2022 (Skift); the pre-filled acquisition year of 2016 is a name collision"))
L.append(und("paid", 2020, "GB", "London", status="private", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Procurement automation (paid.co.uk); the firm backed 'their GBP 2.2M raise, led by ... Crane Venture Partners' (post of 2020-11-17, no round word); the pre-filled public float of $6.9M is a name collision"))
L.append(und("parla", 2018, "GB", "London", status="acquired", rng="below_1b", focus="Healthcare & Bio", flags=["model_disputes_source"],
    note=f"Reproductive health diagnostics; acq. by Holland & Barrett, Jun 2022 (Femtech Insider); {EXIT}; the pre-filled IT is a name collision"))
L.append(fp("passbase", "Pre-Seed", "passbase-the-startup-out-to-reimagine-identity-verification/", "2019-03-15",
    "DE", "Berlin", status="acquired", rng="below_1b", focus="Security",
    note="Identity verification APIs; the firm's post of 2019-03-15: 'We're excited to lead a $600k pre-seed round' (FinTech Global); EUR 3.3M 2019, $13.5M Series A 2021; its assets acquired by Parallel Markets, Mar 2023 (Biometric Update)"))
L.append(und("passfort", 2017, "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="KYC and AML onboarding software; $16.2M Sep 2021 (TechCrunch); acq. by Moody's, Dec 2021; the 2017 entry round is not named"))
L.append(pc("patients-know-best", "Patients Know Best", "GB", "Cambridge", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Patient-controlled health records (Seedcamp Week 2009 winner); PATIENTS KNOW BEST LIMITED active"))
L.append(fp("paua", "Pre-Seed", "paua-accelerates-the-adoption-of-electric-vehicles-through-uks-largest-network-of-chargepoints/",
    "2022-04-26", "GB", "London", status="private", rng="below_1b", focus="Climate & Energy",
    note="EV charging roaming network and fuel card for fleets; the firm's post of 2022-04-26: 'we're excited to lead pre-seed into Paua' (the list's investment year is 2021)"))
L.append(fp("pento", "Seed", "pento-raises-2-8m-to-make-payroll-pains-a-thing-of-the-past/", "2019-09-10", "GB", "London",
    status="acquired", rng="below_1b", focus="SaaS",
    note="Payroll automation; the firm's post of 2019-09-10: 'as we invest in their $2.8M seed round led by Point Nine Capital' (TechCrunch); $15.6M 2021, GBP 26M Series B Dec 2021; acq. by HiBob, Feb 2024 (~$40M, Calcalist)"))
L.append(und("peppy", 2019, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Employee health benefits (menopause, fertility, parenthood); the firm 'lead[s] investment into Peppy' (post of 2019-05-22, no round word); $45M Series B Jan 2023"))
L.append(pc("planvine", "Planvine", "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Events discovery (a Seedcamp Week London winner, January 2013, per the firm's SeedPeek post); no later trace found"))
L.append(pc("platogo", "Platogo", "AT", "Vienna", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note=f"Social browser games, now the Platogo Interactive Entertainment studio (site live); {EXIT} (2018-2020), the company still operates"))
L.append(und("pleo", 2015, "DK", "Copenhagen", status="private", focus="Fintech & Payments",
    note="Company spend cards and expense management; $150M Series C Jul 2021 and a $200M extension at $4.7B Dec 2021 (FinSMEs); the 2015 entry round and the current mark are pinned in the A/B pass"))
L.append(und("plumery", 2023, "NL", "Amsterdam", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Digital banking experience platform; site live; the 2023 entry round is not named"))
L.append(sc("podo-labs", "Podo Labs", "US", "San Francisco", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Stick-and-shoot Bluetooth camera; on the firm's Fund III seed list (2015-09-21); podolabs.com does not serve a page"))
L.append(sc("pointy", "Pointy", "IE", "Dublin", status="acquired", rng="below_1b", focus="SaaS",
    note="Local shop inventory online; on the firm's Fund III seed list (2015-09-21); acq. by Google, Jan 2020 (~$160M, Irish Times)"))
L.append(und("pollen", 2015, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="White-label payments platform (Pollen Technologies; on the firm's 2017 companies page 'Pay and collect funds around the world'); site live; the entry round is not named"))
L.append(pc("popcorn-metrics", "Popcorn Metrics", "PT", "Lisbon", status="defunct", rng="below_1b", focus="SaaS",
    note="No-code web analytics; POPCORN METRICS LTD (09132531) dissolved 2022-02-01 (Companies House)"))
L.append(und("popsink", 2021, "FR", "Paris", status="private", rng="below_1b", focus="Data Infrastructure",
    note="Real-time data replication; site live; the 2021 entry round is not named"))
L.append(pc("poq", "Poq", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="App commerce platform for retailers (poq Studio in 2012); site answers behind a bot check"))
L.append(fp("portalone", "Seed", "unleashing-the-world-of-hybrid-games-our-investment-in-portalone/", "2021-04-30", "NO", "Oslo",
    status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Hybrid live games; the firm's post of 2021-04-30: 'We're thrilled to back Bard Anders Kasin and Stig Olav Kasin in a $15m seed round' (Tech.eu); $60M Jan 2022 (TechCrunch)"))
L.append(fp("prelude", "Seed", "prelude-raises-8m-to-fix-sms-and-mobile-onboarding/", "2024-11-14", "FR", "Paris",
    status="private", rng="below_1b", focus="Security", flags=["model_disputes_source"],
    grad="graduated", grad_src="first_party", grad_cite=V + "prelude-raises-20m-series-a-to-fix-broken-sms-onboarding/",
    note="SMS verification and fraud prevention; the firm's post of 2024-11-14: 'excited to be part of Prelude's journey from Day One and co-lead their $8 million Seed round'; $20M Series A led by 20VC, May 2026 (the firm's post); the pre-filled US is not the company's base"))
L.append(fp("primer", "Pre-Seed", "primer-raises-3-8m-to-take-the-pain-out-of-payments/", "2020-01", "GB", "London",
    status="private", rng="below_1b", focus="Fintech & Payments",
    note="Unified payments API; the firm's post of 2020-05-11: 'At the beginning of this year, we led the pre-seed investment into Paul and Gabriel'; $50M Series B led by ICONIQ Oct 2021"))
L.append(sc("priori-data", "Priori Data", "DE", "Berlin", status="private", rng="below_1b", focus="Data Infrastructure",
    note="App-economy market intelligence; on the firm's Fund III seed list (2015-09-21); site live"))
L.append(pc("profitero", "Profitero", "IE", "Dublin", status="acquired", rng="below_1b", focus="SaaS",
    note="E-commerce analytics for brands (Seedcamp Week 2010 winner, later Boston); acq. by Publicis Groupe, May 2022 (EUR 200M, Silicon Republic)"))
L.append(sc("property-partner", "Property Partner", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Property crowdfunding and trading exchange, now London House Exchange (propertypartner.co redirects there); a seed investment the firm announced 2014-09-18 (the GBP 1.25M seed led by Octopus)"))
L.append(pc("psykosoft", "Psykosoft", "FR", "Tours", status="defunct", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online photo painting (Seedcamp London 2011); PSYKOSOFT LIMITED (07531099) dissolved 2015-04-28 (Companies House)"))
L.append(pc("pult", "Pult", "EE", "Tallinn", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Stream content to any screen from a phone (2012); no later trace found"))
L.append(pc("qamine", "Qamine", "PT", "Lisbon", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Software testing as a service (Seedcamp Lisbon 2012); no later trace found"))
L.append(pc("qminder", "Qminder", "EE", "Tallinn", status="private", rng="below_1b", focus="SaaS",
    note="Queue management (Mini Seedcamp Prague 2011); site live"))
L.append(fp("questdb", "Seed", "our-investment-in-questdb-the-usain-bolt-of-databases/", "2020-09-16", "GB", "London",
    status="private", rng="below_1b", focus="Data Infrastructure",
    note="Open-source time-series database; the firm's post of 2020-09-16 'Our investment in QuestDB' in its $2.3 million seed round (led by Episode 1, 7percent, YC, Kima); $12M Series A 2021"))
L.append(pc("queueco", "Queueco", "GB", "London", status="private", val_conf="low", rng="below_1b", focus="Crypto & Web3",
    note="Algorithmic market making for digital currencies; site live; QUEUECO LIMITED active"))
L.append(und("ramp", 2018, "PL", "Warsaw", status="private", rng="below_1b", focus="Crypto & Web3", clear=["needs_web_value"],
    flags=["model_disputes_source"],
    note="Ramp Network, fiat-to-crypto on-ramp (Warsaw and London); $53M Series A Dec 2021; the unicorn-list match is Ramp (ramp.com), a different US company; the 2018 entry round is not named"))
L.append(pc("rawstream", "Rawstream", "MT", None, status="unknown", rng="below_1b", focus="Security", flags=["city_unknown"],
    note="Cloud web filtering (Malta team, Seedcamp London 2012); the site was last dated 2022"))
L.append(und("rayon", 2021, "FR", "Paris", status="private", rng="below_1b", focus="SaaS",
    note="Collaborative interior design software; the firm's post of 2022-06-15 announces $2m without a round word; EUR 10M Series A Sep 2026 (Tech.eu)"))
L.append(pc("reedsy", "Reedsy", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for publishing professionals (founded in Nottingham); site live"))
L.append(pc("reinfer", "Reinfer", "GB", "London", status="acquired", rng="below_1b", focus="AI & Applied AI",
    note="NLP for business communications; acq. by UiPath, 2022 (REINFER LTD's last address is UiPath's London office)"))
L.append(pc("rentlord", "Rentlord", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Rental market platform (Mini Seedcamp NY 2011); no later trace found"))
L.append(pc("rentmineonline", "RentMineOnline", "NL", "Amsterdam", status="acquired", rng="below_1b", focus="Consumer & Marketplaces",
    note="Peer-to-peer rentals (Seedcamp 2007 winner); acq. by RealPage, 2012 (the firm's /acquirer/real-page page)"))
L.append(pc("repairy", "Repairy", "LV", "Riga", status="unknown", rng="below_1b", focus="SaaS",
    note="Car-repair shop management (Seedcamp Berlin 2012, jointly with 500 Startups); no later trace found"))
L.append(und("reply-ai", 2018, "ES", "Barcelona", status="acquired", rng="below_1b", focus="AI & Applied AI",
    note="Customer-service automation; acq. by Kustomer, May 2020 (PR Newswire); the 2018 entry round is not named"))
L.append(und("reposit", 2016, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Tenancy deposit alternative; site live; the 2016 entry round is not named"))

if __name__ == "__main__":
    jl.write("batch-005", L)
