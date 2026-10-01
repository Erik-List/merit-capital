"""PRO-83 grind, batch-007 (swiftshift .. wanna), plus two corrections to batch 002/004 (Fund II-era listings)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
L14 = "https://index.commoncrawl.org/CC-MAIN-2014-10-index?url=http%3A%2F%2Fwww.seedcamp.com%2Fcompanies&output=json"
FII14 = ("first listed on the firm's /companies/ list captured 2014-03-12, inside the Fund II years, when the programme's "
         "standard cheque was the firm's only instrument (decisions.md D3)")


def fp(slug, stage, url, date, country, city, **kw):
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, stage_conf="high", entry_date=date,
             **loc(country, city), **kw)


def und(slug, year, country, city, note, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city), note=note, **kw)


L = []
L.append(c("swiftshift", prog_at=jl.coh("SwiftShift")["post_date"][:7], cohort=jl.coh("SwiftShift")["url"],
    country="IL", country_src="web_verified", country_cite=jl.coh("SwiftShift")["url"], flags=["city_unknown"],
    status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Shift staffing software (Israel, January 2016 cohort), since repositioned as caregiver-managed paediatric home care; site live"))
L.append(fp("sylvera", "Pre-Seed", "from-our-pre-seed-to-a-7-8m-seed-led-by-index-sylvera-brings-much-needed-clarity-to-carbon-offset-markets/",
    "2020", "GB", "London", status="private", rng="below_1b", focus="Climate & Energy",
    note="Carbon credit ratings; the firm's post of 2021-05-13: 'From our pre-seed to a $7.8M seed led by Index'; $32M Series A Jan 2022, $57M Series B Jul 2023"))
L.append(c("synthesia", status="private", **loc("GB", "London", "https://find-and-update.company-information.service.gov.uk/company/10933652"),
    rng="1b_plus", usd=4000000000, val_src="web_verified", asof="2026-01-26",
    val_cite=V + "synthesia-raises-200m-series-e-at-4b-valuation-to-continue-the-next-era-of-video-creation/",
    stage="Seed", stage_src="model", stage_conf="low", entry_date="2019-04-25", flags=["stage_uncited", "cite_pending", "model_disputes_source"],
    grad="graduated", grad_src="web_verified", grad_cite="https://globalventuring.com/university/synthesia-visualises-12-5m-series-a/",
    focus="AI & Applied AI",
    note="AI video generation; the firm's post of 2019-04-25 names Synthesia 'our latest investment' in the $3.1m round led by LDV Capital with Mark Cuban (no round word; UKTN called it a Series A, but the company's Series A was the $12.5M of 2021, so the 2019 round was the seed); $200M Series E led by GV at $4B, Jan 2026 (the firm's post), as in the Accel, GV and NEA books; the pre-filled acquired/CZ is a name collision"))
L.append(und("synthesized", 2018, "GB", "London", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Synthetic test data for software QA; 'Last year we invested in the team at Synthesized' (the firm's 2019 post, no round word); GBP 14.9M Series A Sep 2025 (Fortune)"))
L.append(pc("tablefinder", "Tablefinder", "SE", "Stockholm", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Restaurant table booking (Seedcamp 2007 winner, Swedish team); tablefinder.com does not answer"))
L.append(pc("talasim", "Talasim", "JO", "Amman", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Arabic online comedy channel (Seedcamp Week 2009 winner); acq. by Jeeran, 2010 (Ammon News; the firm's /acquirer/jeeran page)"))
L.append(pc("talkpush", "Talkpush", "HK", "Hong Kong", status="private", rng="below_1b", focus="SaaS",
    note="Recruitment automation over chat and messaging; site live"))
L.append(c("tanaza", prog_at="2014-03", **loc("IT", "Milan"), status="private", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Cloud management for Wi-Fi access points (Milan); site live; " + FII14))
L.append(pc("teddy-the-guardian", "Teddy The Guardian", "HR", "Zagreb", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Plush toy with medical sensors (the firm's first hardware team, 2013); no later trace found"))
L.append(sc("teleport", "Teleport", "US", "Palo Alto", status="acquired", rng="below_1b", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note=f"Search engine for where to live and work (Palo Alto and Tallinn, Sten Tamkivi); a seed investment the firm announced 2014-09-18; acq. by MoveGuides (Topia), 2017 (the firm's /acquirer/moveguides page); {EXIT}; the pre-filled AT is a name collision"))
L.append(pc("telleroo", "Telleroo", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Bulk payments and payouts API (January 2017 cohort); site live"))
L.append(pc("the-efficient-cloud", "The Efficient Cloud", "AT", "Vienna", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Platform-as-a-service for hosting providers (Mini Seedcamp Berlin 2011); no later trace found"))
L.append(fp("this", "Seed", "this-raises-1m-seed-round-to-bring-delicious-plant-based-meat-alternatives-to-uk-consumers/", "2019-05-13",
    "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Plant-based meat (THIS); the firm's post of 2019-05-13: 'THIS raises $1m seed round', naming it 'our latest investment'; GBP 4.7M 2020 (Tech.eu)"))
L.append(und("those-beyond", 2022, "GB", "Bath", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Immersive online games publisher; site live; the 2022 entry round is not named"))
L.append(pc("thriva", "Thriva", "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="At-home blood testing; $7.3M Series A 2019 (Forbes), EUR 4.4M extension 2020"))
L.append(fp("tickitto", "Pre-Seed", "why-we-led-pre-seed-into-travel-tech-startup-tickitto/", "2020-06-15", "GB", "London",
    status="acquired", rng="below_1b", focus="SaaS",
    note="Event and attraction ticketing API; the firm's post of 2020-06-15: 'Why we led pre-seed into travel tech startup Tickitto'; $4.5M 2021 (Tech.eu); acq. by InteleTravel, Mar 2025 (PhocusWire)"))
L.append(und("tl-dv", 2020, "DE", "Aachen", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI meeting notetaker (tl;dv); EUR 4.3M Jun 2022 (EU-Startups); the 2020 entry round is not named"))
L.append(pc("toksta", "toksta", "DE", "Berlin", status="acquired", rng="below_1b", focus="SaaS",
    note=f"Chat and IM for social networks (Seedcamp Week 2008 winner); {EXIT} (2018-2020, acquirer not named there); today's toksta.com is an unrelated influencer platform"))
L.append(und("tooth-fairy", 2020, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="On-demand dentistry app (Toothfairy); site live; the 2020 entry round is not named"))
L.append(pc("traderion", "Traderion", "RO", "Bucharest", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Trading simulation and assessment (September 2015 cohort); site last dated 2021"))
L.append(und("trail", 2016, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Operations checklists for hospitality (trailapp.com, live); first on the firm's lists in Dec 2016, on no cohort post read"))
L.append(pc("trdata", "TRData", "UA", "Kyiv", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Financial data and communication platform for emerging-market traders; trdata.com live"))
L.append(pc("trebax", "Trebax", "GB", "London", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Mobile advertising and games (Trebax Innovations; Seedcamp Week 2010 winner); no later trace found"))
L.append(und("treecard", 2021, "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Wooden debit card funding reforestation; $23M Dec 2022 (Finextra); treecard.org now carries a 'Treecard Closing Notice'; the 2021 entry round is not named"))
L.append(und("trezy", 2023, "FR", "Paris", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Cash-flow forecasting for SMEs; the firm's post of 2023-06-15 announces EUR 3 million without a round word"))
L.append(pc("trucktrack", "TruckTrack", "RS", "Belgrade", status="unknown", rng="below_1b", focus="SaaS",
    note="Trucking business management SaaS (Mini Seedcamp Belgrade 2013); site behind a Cloudflare check"))
L.append(sc("trussle", "Trussle", "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note="Online mortgage broker; on the firm's Fund III seed list (2015-09-21); acq. by Better, Jul 2021, then OneDome, 2025 (trussle.com redirects to better.co.uk)"))
L.append(und("twig", 2022, "GB", "London", status="private", rng="below_1b", focus="Climate & Energy",
    note="Bioengineered sustainable ingredients; the firm's post of 2023-09-11 announces GBP 3 million without a round word"))
L.append(pc("ubervu", "uberVU", "RO", "Bucharest", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Social media analytics (Seedcamp Week 2008 winner, later Boston); acq. by Hootsuite, Jan 2014 (the firm's /acquirer/hootsuite page)"))
L.append(sc("uipath", "UiPath", "US", "New York", status="public", focus="AI & Applied AI",
    stage_cite=V + "uipath-ipo-a-monumental-moment-for-european-tech-and-for-seedcamp/", entry_date="2015",
    grad="graduated", grad_src="first_party", grad_cite=V + "another-european-unicorn-uipath-raises-153m-eclipses-1-1bn-valuation/",
    note="Robotic process automation (founded in Bucharest, HQ New York); on the firm's Fund III seed list (2015-09-21) and its IPO post: 'In 2015, when we first invested, UiPath was ... fighting to galvanise investors to raise its $500k seed round'; follow-on in the $153M Series B led by Accel, Mar 2018; NYSE IPO Apr 2021; the cap is pinned in the A/B pass"))
L.append(und("uncapped", 2019, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Revenue-based growth financing; the firm's post of 2019-12-02 announces GBP 10m without a round word; GBP 200M debt facility 2023"))
L.append(pc("unifyo", "Unifyo", "GB", "Cambridge", status="unknown", rng="below_1b", focus="SaaS",
    note="360-degree customer profiles in the browser (2013); no later trace found"))
L.append(und("vanilla-steel", 2020, "DE", "Berlin", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for non-prime steel; $4M Jul 2021 (Tech.eu); the 2020 entry round is not named"))
L.append(pc("vchain", "Vchain", "GB", "London", status="defunct", rng="below_1b", focus="Security",
    note="Identity verification for airlines on blockchain (January 2017 cohort); VCHAIN LTD (10431793) dissolved 2026-03-24 (Companies House)"))
L.append(fp("veratrak", "Pre-Seed", "introducing-veratrak-blockchain-based-collaboration-for-pharmaceutical-supply-chain-companies/",
    "2018-04-16", "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="Pharmaceutical supply-chain collaboration; the firm's post of 2018-04-16: 'we're thrilled to lead their pre-seed round of GBP 175k'; site live"))
L.append(und("verax", 2023, "GB", "London", status="private", rng="below_1b", focus="Security",
    note="Trust and security for enterprise generative AI (Verax AI); site live; the 2023 entry round is not named"))
L.append(und("verisian", 2023, "GB", "London", status="private", rng="below_1b", focus="Healthcare & Bio",
    note="AI for clinical trial traceability; the firm's post of 2023-09-07 announces GBP 1M without a round word"))
L.append(und("vidjet", 2021, "FR", "Paris", status="private", rng="below_1b", focus="SaaS",
    note="Shoppable video for online stores; site live; the 2021 entry round is not named"))
L.append(pc("vinterior", "Vinterior", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Vintage and design furniture marketplace; site live"))
L.append(und("vitrolabs", 2018, "US", None, status="unknown", rng="below_1b", focus="Climate & Energy", flags=["city_unknown"],
    note="Lab-grown leather (VitroLabs Inc); the site no longer resolves; the 2018 entry round is not named"))
L.append(c("viz-ai", prog_at=jl.coh("Viz.ai")["post_date"][:7], cohort=jl.coh("Viz.ai")["url"], **loc("US", "San Francisco"),
    status="private", focus="Healthcare & Bio", flags=["needs_web_value"],
    note="AI stroke and care-coordination platform (October 2016 cohort); the band is pinned in the A/B pass (a $100M Series D of 2022 was reported at a $1.2B valuation)"))
L.append(pc("vox-io", "Vox.io", "SI", "Ljubljana", status="unknown", rng="below_1b", focus="SaaS",
    note="Browser voice and video calls (Seedcamp London 2011, later San Francisco); no later trace found"))
L.append(fp("vyne", "Pre-Seed", "vyne-raises-uks-largest-open-banking-seed-round-of-15-5m-with-its-full-stack-payments-solution-for-merchants-and-consumers/",
    "2019-11", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Open banking payments; the firm's post of 2021-09-28: 'resulting in us leading their pre-seed round in November 2019'; $15.5M seed Sep 2021; payvyne.com now serves unrelated content"))
L.append(pc("wanna", "Wanna", "IL", "Tel Aviv", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Local parenting marketplace (Seedcamp Week Berlin 2015); no later trace found"))
# corrections: Fund II-era listings (first on the 2014-03-12 capture)
L.append(c("lodgify", prog_at="2014-03", **loc("ES", "Barcelona"), status="private", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Vacation rental websites and software; EUR 600K seed May 2015 (FinSMEs), $30M Series B 2022; " + FII14))
L.append(c("elliptic", prog_at="2014-03", **loc("GB", "London"), status="private", rng="below_1b", focus="Crypto & Web3", stage_conf="medium",
    note="Blockchain analytics and crypto compliance; $120M Series D May 2026 (FinSMEs); " + FII14))

if __name__ == "__main__":
    jl.write("batch-007", L)
