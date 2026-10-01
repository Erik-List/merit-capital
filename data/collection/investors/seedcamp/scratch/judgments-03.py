"""PRO-83 grind, batch-003 (fluttr .. klump)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's 2018-2021 list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"


def fp(slug, stage, url, date, country, city, **kw):
    """Stage from the firm's own post that names the round and ties Seedcamp to it."""
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, stage_conf="high", entry_date=date,
             **loc(country, city), **kw)


L = []
L.append(pc("fluttr", "Fluttr", "GB", None, status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["city_unknown"], note="User-curated music events discovery (announced with the Seedcamp Week Berlin 2014 investments); no later trace found"))
L.append(pc("fractal", "Fractal", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="HTML-to-email design conversion (Mini Seedcamp London 2011); a different company from Fractal Labs (2015; PARSED_RENAMES in scratch/cc-parse.py); no later trace found"))
L.append(sc("fractal-labs", "Fractal Labs", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="SME financial marketplace, later Fractal (askfractal.com, open-banking APIs for SME finance); on the firm's Fund III seed list (2015-09-21); askfractal.com does not answer"))
L.append(c("fraugster", status="unknown", **loc("DE", "Berlin"), rng="below_1b", focus="Security", stage="undetermined", entry_date="2016",
    note="AI payment fraud prevention (Berlin and London); fraugster.com returns a Cloudflare error and the UK entity was converted/closed in 2020; the 2016 entry round is not named"))
L.append(fp("fullview", "Pre-Seed", "fullview-doubles-down-on-redesigning-customer-support-with-7-5-million-seed-round/", "2021-11",
    "DK", "Copenhagen", status="private", rng="below_1b", focus="SaaS",
    note="Co-browsing and session replay for customer support; the firm's post of 2022-05-11: 'excited to participate in Fullview's seed round, six months after we invested in their pre-seed' ($1.8M pre-seed Nov 2021, ArcticStartup; $7.5M seed May 2022)"))
L.append(pc("futurelytics", "Futurelytics", "CZ", "Brno", status="unknown", rng="below_1b", focus="Data Infrastructure",
    note="Customer analytics (Seedcamp Budapest 2012); no later trace found"))
L.append(c("gaia", status="private", **loc("GB", "London"), rng="below_1b", focus="Healthcare & Bio", stage="undetermined", entry_date="2020",
    flags=["model_disputes_source"],
    note="IVF financing and fertility care (London); $20M Series A led by Atomico Feb 2022 (TechCrunch); the pre-filled public/BE float is a name collision; the 2020 entry round is not named"))
L.append(pc("gamewheel", "Gamewheel", "DE", "Berlin", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Branded game creation platform (Seedcamp Week Berlin 2014); no later trace found"))
L.append(fp("gameye", "Seed", "welcome-gameye-the-multiplayer-solution-out-to-revolutionise-the-future-of-online-gaming/", "2019-01-23",
    "NL", "Rotterdam", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Game server orchestration API; the firm's post of 2019-01-23: 'Our investment in Rotterdam-based Gameye as part of their $1.6m seed round'"))
L.append(pc("gaminglive", "GamingLive", "PL", "Warsaw", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Live-streaming for games and eSports (2014); no later trace found"))
L.append(sc("getagent", "GetAgent", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Estate agent comparison; on the firm's Fund III seed list (2015-09-21); GBP 2.2M round 2019 (The Negotiator); site live"))
L.append(pc("gis-cloud", "GIS Cloud", "HR", "Zagreb", status="private", rng="below_1b", focus="SaaS",
    note="Online GIS mapping platform (Seedcamp Week 2010 winner); site live"))
L.append(pc("gopixel", "GoPixel", "GB", "Newcastle upon Tyne", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Image-network marketing campaigns (2013); no later trace found"))
L.append(pc("goworkabit", "GoWorkaBit", "EE", "Tallinn", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Temporary-work marketplace (joined from Seedcamp Week London, Jan 2014); the Estonian site is live"))
L.append(pc("grabcad", "GrabCAD", "US", "Boston", status="acquired", rng="below_1b", focus="SaaS",
    note="CAD community and collaboration (founded in Tallinn, later Boston); acq. by Stratasys, 2014 (~$100M, Forbes)"))
L.append(c("granular", status="private", **loc("FR", "Paris"), rng="below_1b", focus="Climate & Energy", stage="undetermined", entry_date="2022-06-14",
    note="Granular Energy, hourly energy certificates; the firm's post of 2022-06-14 announces EUR 2M in funding without naming the round; EUR 7.5M 2023 (Tech Funding News)",
    rounds=[rnd("2022-06-14", None, None, None, True, V + "granular-energy-launches-the-worlds-first-market-for-hour-by-hour-energy-certificates-with-e2m-in-funding/", "firm")]))
L.append(c("griffin", status="private", **loc("GB", "London"), rng="below_1b", focus="Fintech & Payments", stage="undetermined", entry_date="2018",
    flags=["model_disputes_source"],
    note="Banking-as-a-service bank (UK banking licence); EUR 7.2M 2020, $13.5M Series A 2023; the pre-filled IT is a name collision; the 2018 entry round is not named"))
L.append(c("grover", status="private", **loc("DE", "Berlin"), focus="Consumer & Marketplaces", stage="undetermined", entry_date="2015",
    note="Consumer electronics rental subscription; EUR 60M Series B 2021; the 2015 entry is on no cohort post; the band is pinned in the A/B pass"))
L.append(c("harbr", status="private", **loc("GB", "London"), rng="below_1b", focus="Data Infrastructure", stage="undetermined", entry_date="2018",
    note="External data sharing platform; $38.5M Series A Nov 2020 (FinSMEs); the 2018 entry round is not named"))
L.append(fp("helloflow", "Seed", "digital-client-onboarding-with-no-code-needed-helloflow-raises-1-6m-to-revolutionise-client-onboarding-and-identity-verification/",
    "2021-07-15", "DK", "Copenhagen", status="acquired", rng="below_1b", focus="SaaS",
    note="No-code client onboarding; the firm's post of 2021-07-15: '$1.6m seed round led by Seedcamp and Danish VC PreSeed Ventures'; acq. by Trulioo, Feb 2022 (Business Wire)"))
L.append(c("hi-health", status="acquired", **loc("DE", "Berlin"), rng="below_1b", focus="Fintech & Payments", stage="undetermined", entry_date="2019",
    note="Health-insurance payment cards; acq. by Pliant, Apr 2025 (FinTech Global; hi.health now redirects to Pliant); the 2019 entry round is not named"))
L.append(pc("hoko", "Hoko", "PT", "Lisbon", status="unknown", rng="below_1b", focus="DevTools & APIs", flags=["model_disputes_source"],
    note="Mobile deep-linking (Lisbon and London); the pre-filled JP is a name collision; HOKO LTD (09525857) dissolved 2020, not shown to be this company"))
L.append(pc("hole19", "Hole19", "PT", "Lisbon", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Golf GPS app; site live"))
L.append(pc("holvi", "Holvi", "FI", "Helsinki", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Business banking for freelancers; acq. by BBVA, Mar 2016 (Finextra)"))
L.append(pc("home-on-demand", "Home on Demand", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Landlord-tenant rental platform (2012); no later trace found"))
L.append(pc("homeshift", "Homeshift", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Home moving service (2014); the domain now serves unrelated content"))
L.append(fp("hopin", "Pre-Seed", "hopin-cmo-anthony-kennada-on-how-to-build-a-category-defining-brand/", "2019",
    "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="Virtual events platform; the firm's post: 'Hopin's growth since leading their Pre-Seed raise in 2019'; $6.5M seed Feb 2020, peak valuation $7.75B (2021); events business sold to RingCentral (2023, hopin.com now 'RingCentral Events'), StreamYard to Bending Spoons (2024); HOPIN LTD dissolved May 2026"))
L.append(sc("hubble", "Hubble", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Flexible office space marketplace (hubblehq.com); on the firm's Fund III seed list (2015-09-21); the pre-filled KR and the Hubble Network satellite headlines are name collisions"))
L.append(pc("hype", "Hype", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Real-time local events app (2013); the domain now carries an experiences site last dated 2021"))
L.append(pc("hypernumbers", "Hypernumbers", "GB", "Edinburgh", status="unknown", rng="below_1b", focus="SaaS",
    note="Web spreadsheet platform (Project Playfair; Seedcamp 2007 winner, Scotland); no later trace found"))
L.append(sc("incrediblue", "incrediblue", "GR", "Athens", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Private yacht holiday marketplace; the firm's post of 2015-05-06: joined 'raising $1.8m ... seed round, led by Connect Ventures'; on the Fund III seed list; no later trace found"))
L.append(pc("ineze", "Ineze", "IL", "Tel Aviv", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Product search (Seedcamp Week 2010 winner); no later trace found"))
L.append(pc("intelliment-security", "Intelliment Security", "ES", "Seville", status="defunct", rng="below_1b", focus="Security",
    note="Network security policy automation; INTELLIMENT SECURITY LIMITED (10767991) dissolved 2023-05-28 (Companies House), the domain is for sale"))
L.append(c("itch", status="private", **loc("GB", "London"), rng="below_1b", focus="Consumer & Marketplaces", stage="undetermined", entry_date="2019-07-09",
    note="Pet wellbeing treatments by subscription; launched with GBP 5M (the firm's post of 2019-07-09, no round word)",
    rounds=[rnd("2019-07-09", None, None, None, True, V + "itch-launches-with-5m-to-disrupt-pet-wellbeing-market/", "firm")]))
L.append(c("jelly", status="private", **loc("GB", "London"), rng="below_1b", focus="SaaS", stage="undetermined", entry_date="2020",
    note="Food costing and kitchen management software; site live; the 2020 entry round is not named"))
L.append(pc("jobdoh", "JOBDOH", "HK", "Hong Kong", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Temporary hospitality staffing marketplace; site last dated 2016"))
L.append(c("join", status="private", **loc("FR", "Paris"), rng="below_1b", focus="Media, Gaming & Advertising", stage="undetermined", entry_date="2021",
    note="JOIN (join-stories.com), shoppable video stories for brands; site live; the 2021 entry round is not named"))
L.append(c("julienne-bruno", status="acquired", **loc("GB", "London"), rng="below_1b", focus="Consumer & Marketplaces", stage="undetermined",
    entry_date="2021", note="Plant-based foods; the firm 'doubled down' in the GBP 6M round of 2022 (its post), so that round is a follow-on; JULIENNE BRUNO LTD in administration (Companies House), the business sold out of administration to Harvey & Brockless (Cherry's book); the 2021 entry round is not named"))
L.append(pc("juro", "Juro", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Contract automation; $750K seed Jan 2017, $2M 2018, $23M Series B Jan 2022"))
L.append(pc("kareinn", "KareInn", "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Care home management software; site live"))
L.append(pc("kasko", "Kasko", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Insurance-as-a-service platform; site live; KASKO LTD (09607496) active"))
L.append(c("kelvin", status="private", **loc("FR", "Paris"), rng="below_1b", focus="Climate & Energy", stage="undetermined", entry_date="2024-06-11",
    note="AI sales assistant for home energy renovation; the firm's post of 2024-06-11 announces EUR 5M without naming the round",
    rounds=[rnd("2024-06-11", None, None, None, True, V + "kelvin-raises-e5m-to-ramp-up-home-energy-renovations/", "firm")]))
L.append(fp("kitch", "Pre-Seed", "kitch-launches-to-bring-our-favourite-restaurants-to-our-home/", "2020-05-20",
    "PT", "Lisbon", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Delivery-first virtual food market (Lisbon); the firm's post of 2020-05-20: 'an easy decision for us to lead this EUR 1M pre-seed round'; the domain now serves unrelated content"))
L.append(fp("klasha", "Seed", "our-investment-in-klashas-2-4m-seed-to-enable-seamless-cross-border-commerce-in-africa/", "2021-10-07",
    "NG", "Lagos", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Cross-border payments for African commerce; the firm's post of 2021-10-07: 'Our investment in Klasha's $2.4M seed' (its first investment in Africa)"))
L.append(fp("klump", "Pre-Seed", "klump-launches-to-bring-buy-now-pay-later-to-nigeria/", "2022-03-09",
    "NG", "Lagos", status="private", rng="below_1b", focus="Fintech & Payments",
    note="BNPL infrastructure for Nigeria; the firm's post of 2022-03-09: 'we are excited to lead Klump's $780k pre-seed round'"))

if __name__ == "__main__":
    jl.write("batch-003", L)
