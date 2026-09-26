"""PRO-106 grind, batch-004 (light .. ramp). Same evidence as batch-001."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
LIST = "https://www.balderton.com/companies/"
NEWS = "https://www.balderton.com/news/"
L = []
def fp(slug, stage, conf="medium", **kw):
    return cls(slug, stage=stage, stage_src="first_party", stage_cite=LIST, stage_conf=conf, **kw)
def wv(slug, stage, cite, **kw):
    return cls(slug, stage=stage, stage_src="web_verified", stage_cite=cite, stage_conf="high", **kw)

L.append(wv("light", "Series A", NEWS + "light-raises-30m-series-a-to-replace-legacy-finance-systems-with-ai-native-platform/", status="private", country="DK",
    country_src="web_verified", country_cite=LIST, city="Copenhagen", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="AI-native finance and accounting platform; Balderton led the $30M Series A of Sep 2025 (the firm's post; Wikipedia); the pre-filled country JP is a wrong join; band re-checked in the momentum pass"))
L.append(wv("lindus-health", "Growth", NEWS + "lindus-health-raises-55m-to-transform-the-clinical-trial-landscape/", status="private", country="GB", city="London",
    rng="below_1b", focus="Healthcare & Bio", note="Tech-enabled clinical trials; the firm's post of 2025-01-22 announces the $55M Series B Balderton led (Chandratillake director from 2024-12)"))
L.append(cls("lovable", status="private", city="Stockholm", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "lovable-raises-400m-in-series-c-funding-to-help-people-run-their-businesses/",
    rng="10b_plus", usd=13300000000, val_src="web_verified", asof="2026-08-12",
    val_cite="https://www.bloomberg.com/news/articles/2026-08-12/ai-coding-startup-lovable-raises-400-million-at-13-3-billion-valuation",
    focus="AI & Applied AI",
    note="AI app builder; Balderton joined the $400M Series C of Aug 2026 at a $13.3B valuation (the firm's post; Bloomberg), its entry (card 'Series C in 2026'); the same mark as the Accel, Creandum, Khosla and Menlo books",
    rounds=[rnd("2026-08-12", "Series C", 400000000, "Menlo Ventures", True, NEWS + "lovable-raises-400m-in-series-c-funding-to-help-people-run-their-businesses/", "firm")]))
L.append(fp("lovecrafts", "Series A", status="unknown", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace and community for knitters and makers; card 'Series A in 2014' (Waterhouse director 2014-03 to 2024-09); the card says Exited and the event is not on any surface read"))
L.append(wv("luno", "Growth", "https://techcrunch.com/2017/09/19/luno-raises-9m-bitcoin/", status="acquired", country="GB", city="London", rng="below_1b",
    focus="Crypto & Web3", note="Crypto exchange and wallet; Balderton led the $9M Series B of Sep 2017 (TechCrunch); acq. by Digital Currency Group, 2020"))
L.append(wv("lyst", "Growth", NEWS + "fashion-ecommerce-platform-lyst-announces-14-million-series-b-investment/", status="acquired", country="GB", city="London",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="Fashion search platform; the firm's post of 2014-01-23 announces the $14M Series B Balderton led; acq. by Zozo, 2025 (status medium confidence, re-checked in the A/B pass; the card says Live and Accel's book private)"))
L.append(fp("magic-pony-technology", "Series A", status="acquired", country="GB", city="London", rng="below_1b", focus="AI & Applied AI",
    note="Machine learning for video; card 'Series A in 2015'; acq. by Twitter, 2016 (the firm's post of 2016-06-20)"))
L.append(cls("matillion", status="private", country="GB", city="Manchester", stage="Growth", stage_src="first_party", stage_cite=LIST, stage_conf="medium",
    rng="1b_plus", usd=1500000000, val_src="web_verified", asof="2021-09-16",
    val_cite=NEWS + "matillion-raises-150m-series-e-funding-at-1-5b-valuation/", focus="Data Infrastructure", flags=["stale"],
    note="Cloud data integration; card 'Secondary in 2021' (Liquidity I; D5); last primary mark the $150M Series E at $1.5B, Sep 2021 (the firm's post), stale; the same mark as the Battery and Lightspeed books; attacked in the A/B pass"))
L.append(cls("matrix-semiconductor", status="acquired", country="US", city="Santa Clara", stage="undetermined", rng="below_1b", focus="Industrial & Robotics",
    note="3D memory chips; listed on the Benchmark Europe desk page 2003-07 beside Benchmark's US book (both desks' row); acq. by SanDisk, 2006; the entry round is not named on any surface read"))
L.append(cls("mba-polymers", status="unknown", city="Richmond", stage="undetermined", rng="below_1b", focus="Climate & Energy",
    note="Plastics recycling; card gives the year 2007 only (its 2010-13 Form Ds name the Balderton funds); the round and the company's later ownership are not on any surface read; the card says Exited"))
L.append(fp("mcmakler", "Growth", status="private", city="Berlin", rng="below_1b", focus="Consumer & Marketplaces",
    note="Hybrid estate agent; card 'Secondary in 2019' (the firm's post of 2019-10-23 welcomes Balderton as a new investor; Liquidity I, D5)"))
L.append(fp("miim", "Growth", status="private", country="US", city="Salt Lake City", rng="below_1b", focus="AI & Applied AI",
    note="Computer vision for venues; card 'Series B in 2012'; status from the card (Live), low confidence"))
L.append(fp("mojiworks", "Series A", status="private", country="GB", city="Guildford", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Games for messaging platforms; card 'Series A in 2017' (the firm's post of 2017-11-07, GBP 2.1M; Moffat director from 2017-09)"))
L.append(wv("mozart", "Seed", NEWS + "mozart-ai-scores-6m-from-balderton-to-put-artists-at-the-centre-of-ai-powered-music-making/", status="private", country="GB",
    city="London", entry_date="2026-02-11", rng="below_1b", focus="AI & Applied AI", note="AI music production software; the firm's post of 2026-02-11 announces the $6M seed Balderton led"))
L.append(fp("mytomorrows", "Seed", status="private", country="NL", city="Amsterdam", entry_date="2014", rng="below_1b", focus="Healthcare & Bio",
    note="Access to pre-approval medicines; card 'Seed in 2014'; EUR 10M round Jan 2017 (the firm's post)"))
L.append(cls("neartek", status="unknown", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    flags=["country_prior"],
    note="Storage management software (French-founded, US offices); on the Benchmark Europe desk page 2003-06; neither the entry round nor the company's fate is on any surface read; country and city low confidence"))
L.append(fp("nested", "Series A", conf="low", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Estate agent with an advance on the sale price; card 'Series A in 2018' (the firm's posts of 2018-11-12: the GBP 120M debt-and-equity round); the company had raised earlier rounds from others, so the label is low confidence"))
L.append(cls("nexagent", status="acquired", country="GB", city="Reading", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    note="Network service management software; on the Benchmark desk lists 2003-09; the entry round is not named on any surface read; acq. by EDS, 2008"))
L.append(cls("nlyte-software", status="acquired", country="US", city="Edison", stage="undetermined", rng="below_1b", focus="Data Infrastructure",
    note="Data centre infrastructure management (founded in London as GDCM); the card names no round or year (Bunting director 2008-05, Liautaud 2008-06 to 2021-10); acq. by Carrier, 2021 (the firm's post)"))
L.append(fp("numeral", "Seed", status="acquired", country="FR", city="Paris", entry_date="2021-12-21", rng="below_1b", focus="Fintech & Payments",
    note="Payment operations platform; card 'Seed in 2021' (the firm's post of 2021-12-21, EUR 13M); acq. by Mambu, 2024 (the card says Exited)"))
L.append(fp("nutmeg", "Growth", status="acquired", city="London", rng="below_1b", focus="Fintech & Payments",
    note="Online wealth manager; card 'Series C in 2014' (the firm's post of 2014-06-25: $32M from Balderton and Schroders; Bunting director of what is now J.P. Morgan Personal Investing from 2014-07); acq. by JPMorgan Chase, 2021"))
L.append(verdict("odyssey-therapeutics", "not_member",
    "Sale consideration, not an investment (decisions.md D6; COLLECTION.md s1, Erik 2026-09-22): Odyssey's own registration statement says its Series A preferred shares 'were issued to Balderton Capital VI S.L.P. as partial consideration for the shares of Rahko Limited held by Balderton, pursuant to a share purchase agreement, dated October 6, 2021', with no purchase price beside Balderton's name; the firm's card labels the position 'Acquired Rahko in 2022'. Rahko is the member.",
    ec="fund_filing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1882782/000095012324009534/filename1.htm"))
L.append(fp("omio", "Growth", status="private", city="Berlin", rng="below_1b", focus="Consumer & Marketplaces",
    note="Travel search and booking (GoEuro until 2019); card 'Secondary in 2020' (Liquidity I; D5); below $1B as in the Atomico and Battery books"))
L.append(cls("omprompt", status="unknown", country="GB", city="Abingdon", stage="undetermined", rng="below_1b", focus="SaaS",
    note="Automated order processing; on Benchmark's worldwide list 2005-08 (Europe lineage); neither the entry round nor the company's fate is on any surface read"))
L.append(cls("oncimmune", status="defunct", country="GB", city="Nottingham", stage="undetermined", rng="below_1b", focus="Healthcare & Bio",
    flags=["model_disputes_source"],
    note="Early cancer detection blood tests; card gives the year 2007 only (Bunting director of the holding company 2015-23); AIM IPO 2016; Companies House 09818395 shows Oncimmune Holdings plc in administration, recorded defunct (Erik 2026-09-07); the card says Live"))
L.append(cls("orbian", status="private", country="GB", city="London", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Supply chain finance; on the Benchmark Europe desk page 2005-08; the entry round is not named on any surface read; status low confidence"))
L.append(cls("orchestria", status="acquired", country="US", city="New York", stage="undetermined", rng="below_1b", focus="Security",
    note="Compliance and data-loss prevention software (founded in the UK); on the Benchmark desk lists 2002-09; the entry round is not named on any surface read; acq. by CA, 2009"))
L.append(cls("pageflakes", status="acquired", country="US", city="San Francisco", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Personalised start page; the desk invested an undisclosed amount in May 2006 (Wikipedia), the round unnamed; acq. by LiveUniverse, 2008"))
L.append(fp("patients-know-best", "Series A", status="private", city="Cambridge", rng="below_1b", focus="Healthcare & Bio",
    note="Patient-controlled medical records; card 'Series A in 2015'; the card says Exited (the firm sold), the company still operates"))
L.append(cls("pay-with-my-bank", status="acquired", country="US", city="Redwood City", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Online banking payments; the card names no round or year; merged with Trustly in 2019 (the card still says Live)"))
L.append(wv("payflows", "Series A", NEWS + "payflows-raises-e25m-to-build-the-command-centre-for-finance-teams/", status="private", country="FR", city="Paris",
    rng="below_1b", focus="Fintech & Payments", note="Finance operations platform; the firm's post of 2024-04-22 announces the EUR 25M Series A Balderton led"))
L.append(wv("peakon", "Growth", "https://techcrunch.com/2018/02/27/peakon-secures-another-22m-in-a-series-b-round-led-by-balderton-capital/", status="acquired",
    country="DK", city="Copenhagen", rng="below_1b", focus="SaaS",
    note="Employee engagement analytics; Balderton led the $22M Series B of Feb 2018 (TechCrunch); acq. by Workday, 2021 ($700M)"))
L.append(wv("playplay", "Series A", NEWS + "playplay-raises-e10m-to-help-brands-produce-high-quality-videos-in-minutes/", status="private", country="FR", city="Paris",
    rng="below_1b", focus="SaaS", note="Video creation for communications teams; the firm's post of 2020-05-12 announces the EUR 10M Series A Balderton led; $55M Series B 2022"))
L.append(cls("premialab", status="private", country="FR", city="Paris", stage="undetermined", rng="below_1b", focus="Fintech & Payments",
    note="Analytics on systematic investment strategies; the card says 'Investment in 2021' and the firm's post of 2021-03-31 'a strategic partnership with Balderton', neither naming a round"))
L.append(wv("primer", "Seed", NEWS + "primer-raises-3-2m-seed-to-help-merchants-consolidate-their-payment-stacks/", status="private", country="GB", city="London",
    entry_date="2020-05-11", rng="below_1b", focus="Fintech & Payments",
    note="Payments orchestration; the firm's post of 2020-05-11 announces the GBP 3.2M seed Balderton led; GBP 14M Series A Nov 2020; $50M Series B at $425M Oct 2021",
    rounds=[rnd("2020-05-11", "Seed", 3900000, "Balderton Capital", True, NEWS + "primer-raises-3-2m-seed-to-help-merchants-consolidate-their-payment-stacks/", "firm"),
            rnd("2020-11-30", "Series A", 18700000, None, True, NEWS + "primer-secures-14m-series-a-to-help-merchants-consolidate-their-payment-stacks/", "firm")]))
L.append(wv("prior-labs", "Pre-Seed", NEWS + "prior-labs-raises-e9m-to-revolutionise-how-businesses-interact-with-their-tabular-data/", city="Freiburg", rng="below_1b",
    focus="AI & Applied AI", note="Foundation model for tabular data; the firm's post of 2025-02-05 announces the EUR 9M pre-seed Balderton led; SAP announced its intent to acquire the company in May 2026 (the firm's post of 2026-05-04); closing re-checked in the A/B pass"))
L.append(fp("prodigy-finance", "Growth", status="private", country="GB", city="London", rng="below_1b", focus="Fintech & Payments",
    note="Loans for international postgraduate students; card 'Series B in 2014' (Bunting director of Prodigy Investments from 2014-12; the 2015 announcement: $12.5M of equity from Balderton)"))
L.append(cls("proxima-fusion", status="private", country="DE", city="Munich", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "proxima-fusion-raises-e130m-series-a-to-build-worlds-first-stellarator-based-fusion-power-plant/",
    rng="1b_plus", usd=2743920000, val_src="web_verified", asof="2026-07-07",
    val_cite="https://www.proximafusion.com/press-news/proxima-fusion-raises-eu411-million-to-build-europes-commercial-fusion-champion",
    focus="Climate & Energy",
    note="Stellarator fusion; Balderton co-led the EUR 130M Series A of Jun 2025 (the firm's post); the EUR 411M round of Jul 2026 sets the mark, aligned to the Cherry and Lightspeed books (same figure, same citation)"))
L.append(wv("pusher", "Series A", NEWS + "investment-update-pusher-raises-8m-to-grow-its-platform-of-realtime-apis-for-developers-led-by-balderton/", status="acquired",
    country="GB", city="London", rng="below_1b", focus="DevTools & APIs", note="Realtime APIs; Balderton led the $8M Series A of Apr 2018; acq. by MessageBird, 2020"))
L.append(wv("qargo", "Series A", NEWS + "qargo-raises-11-million-to-build-the-all-in-one-platform-to-streamline-the-logistics-industry/", status="private", country="GB",
    city="London", rng="below_1b", focus="SaaS", note="Transport management software; the firm's post of 2024-06-06 announces the GBP 11M Series A Balderton led (Moffat director)"))
L.append(wv("quantum-systems", "Growth", NEWS + "quantum-systems-raises-e160m-as-it-targets-global-leadership-in-aerial-intelligence-solutions/", status="private",
    country="DE", city="Munich", focus="Industrial & Robotics", flags=["needs_web_value"],
    note="Aerial intelligence drones; Balderton led the EUR 160M Series C of May 2025 (the firm's post; card 'Series C in 2025'); the Nov 2025 extension tripled the valuation (the firm's post of 2025-11-28); figure pinned in the A/B pass"))
L.append(fp("qubit", "Series A", status="acquired", country="GB", city="London", rng="below_1b", focus="SaaS",
    note="Personalisation software for e-commerce; card 'Series A in 2012'; acq. by Coveo, 2021"))
L.append(wv("rahko", "Seed", NEWS + "rahko-raises-1-3m-seed-round-to-expand-the-expert-team-and-break-new-ground-in-quantum-machine-learning/", status="acquired",
    country="GB", city="London", entry_date="2019-10-11", rng="below_1b", focus="AI & Applied AI",
    note="Quantum machine learning for chemistry; the firm's post of 2019-10-11 announces the GBP 1.3M seed Balderton led; acq. by Odyssey Therapeutics, agreement of 2021-10-06 (Odyssey's registration statement), announced Jan 2022; Balderton took Odyssey shares as consideration (D6)"))
L.append(wv("ramp", "Series A", NEWS + "ramp-raises-53m-to-empower-mainstream-adoption-of-decentralized-applications/", status="private", country="PL",
    country_src="web_verified", country_cite=LIST, city="Warsaw", rng="below_1b", focus="Crypto & Web3", flags=["stage_disputes_band"],
    note="Ramp Network, the fiat-to-crypto on-ramp (not Ramp, the US card company in sibling books); Balderton co-led the $53M Series A announced 2021-12-15 (the firm's post) and joined the $70M Series B of Nov 2022; the card says 'Series B in 2022'"))
jl.write("batch-004", L)
