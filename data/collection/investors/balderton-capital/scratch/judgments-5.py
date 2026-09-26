"""PRO-106 grind, batch-005 (rawflow .. vestiaire-collective). Same evidence as batch-001."""
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
def und(slug, **kw):
    return cls(slug, stage="undetermined", **kw)

L.append(und("rawflow", status="defunct", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Peer-to-peer live streaming technology; on Benchmark's worldwide list 2006-08 (Europe lineage); the entry round is not named on any surface read; no trace after 2009, status low confidence"))
L.append(fp("recorded-future", "Growth", status="acquired", city="Somerville", rng="below_1b", focus="Security",
    note="Threat intelligence; card 'Series C in 2012'; acq. by Insight Partners, 2019 ($780M; the firm's post), then Mastercard, 2024"))
L.append(fp("rentify", "Series A", status="unknown", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online letting agent; card 'Series A in 2012' (Bunting director from 2012-12); the card says Exited and the event is not on any surface read; Companies House 07723819 shows the company active"))
L.append(wv("request-finance", "Seed", NEWS + "request-finance-raises-5-5m-to-simplify-enterprise-crypto-payments/", status="private", country="FR", city="Paris",
    entry_date="2022-06-09", rng="below_1b", focus="Crypto & Web3", note="Crypto invoicing and payroll; the firm's post of 2022-06-09 announces the $5.5M seed Balderton led"))
L.append(wv("reson8", "Pre-Seed", NEWS + "reson8-raises-e5m-to-build-hyper-customised-europe-first-speech-ai/", status="private", country="NL", city="Amsterdam",
    rng="below_1b", focus="AI & Applied AI", note="Customised speech recognition; the firm's post of 2026-03-19 announces the EUR 5M pre-seed"))
L.append(cls("revolut", status="private", country="GB", country_src="web_verified", country_cite=LIST, city="London",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS + "revolut-raise-1-5m-in-round-led-by-balderton-capital/",
    entry_date="2015-07-20", rng="100b_plus", usd=115000000000, val_src="web_verified", asof="2026-07-22",
    val_cite="https://www.bloomberg.com/news/articles/2026-07-22/revolut-confirms-115-billion-valuation-in-secondary-share-sale",
    focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Digital bank; Balderton led the GBP 1.5M seed of Jul 2015 (the firm's post; card 'Seed in 2015'; Waterhouse director 2016-20) and the Series A of Jul 2016; mark: the company-run secondary of Jul 2026 at $115B (Bloomberg), as in Point Nine's book; the a16z and Greylock books still carry the $75B mark of Nov 2025, the stale side for the wave alignment; the Wikidata country LT is the Lithuanian bank entity",
    rounds=[rnd("2015-07-20", "Seed", 2300000, "Balderton Capital", True, NEWS + "revolut-raise-1-5m-in-round-led-by-balderton-capital/", "firm"),
            rnd("2016-07-11", "Series A", 10000000, "Balderton Capital", True, NEWS + "investment-update-balderton-lead-up-to-7-75m-round-in-revolut/", "firm")]))
L.append(und("ricall", status="unknown", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Online music licensing marketplace; on the Benchmark Europe desk page 2006-08; neither the entry round nor the company's fate is on any surface read"))
L.append(wv("riff", "Seed", NEWS + "riff-raises-1-5m-to-make-working-from-home-feel-more-like-being-in-the-office/", status="private", country="GB", city="London",
    entry_date="2020-08-20", rng="below_1b", focus="SaaS",
    note="Voice chat for remote teams; the firm's post of 2020-08-20 announces the $1.5M seed (Chandratillake director of Riff Technologies 2020-06 to 2026-03); Companies House 12611399 shows the company active"))
L.append(wv("roli", "Series A", NEWS + "revolutionary-music-keyboard-firm-roli-raises-12-8m-from-leading-investment-houses-to-scale-production-and-develop-new-products/",
    status="acquired", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Expressive music keyboards; the firm's post of 2014-05-21 announces the $12.8M Series A Balderton led (Waterhouse director 2014-19); ROLI Ltd went into administration in 2021 and the business continued in a successor company (acquired out of insolvency); Companies House 07044888 dissolved"))
L.append(wv("sava", "Seed", NEWS + "sava-raises-8m-to-build-preventative-personalised-precision-health-monitoring-at-scale/", status="private", country="GB",
    country_src="web_verified", country_cite=LIST, city="London", entry_date="2024-06-21", rng="below_1b", focus="Healthcare & Bio",
    flags=["model_disputes_source"],
    note="Continuous health biosensors; the firm's post of 2024-06-21 announces the $8M seed Balderton led; $19M Series A Jul 2025; the pre-filled status and country are a wrong Wikidata join",
    rounds=[rnd("2024-06-21", "Seed", 8000000, "Balderton Capital", True, NEWS + "sava-raises-8m-to-build-preventative-personalised-precision-health-monitoring-at-scale/", "firm"),
            rnd("2025-07-31", "Series A", 19000000, None, True, NEWS + "sava-raises-19m-series-a-amid-world-first-clinical-results-for-next-gen-biosensing-technology/", "firm")]))
L.append(wv("scalable-capital", "Growth", NEWS + "scalable-capital-raises-e60m-in-growth-funding/", status="private", country="DE", city="Munich",
    focus="Fintech & Payments", flags=["needs_web_value"],
    note="Digital investment platform; Balderton led the EUR 60M Series E extension of Dec 2023 (the firm's post; card 'Series E in 2024'), at an unchanged $1.4B valuation (Wikipedia); EUR 155M round Jun 2025; mark pinned in the A/B pass"))
L.append(und("scansafe", status="acquired", city="London", rng="below_1b", focus="Security",
    note="Web security as a service; on the Benchmark Europe desk page 2005-08; the entry round is not named on any surface read; acq. by Cisco, 2009 ($183M)"))
L.append(und("scytl", status="acquired", city="Barcelona", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Electronic voting software; the desk entered in the $9M round of 2006 with Nauta Capital (Wikipedia), a round no surface names, so the card's 'Series B in 2010' is not the entry; Scytl filed for bankruptcy in 2020 and the business was sold to Paragon Group (acquired out of insolvency); the card says Live"))
L.append(cls("setanta", status="defunct", country="IE", city="Dublin", stage="Growth", stage_src="model", stage_conf="low", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["stage_uncited"],
    note="Sports broadcaster (founded 1990); on Benchmark's worldwide list 2006-08 (Europe lineage); the desk bought into a sixteen-year-old company, a growth entry; the British business went into administration in June 2009 and the group was broken up"))
L.append(wv("simple-feast", "Series A", NEWS + "simple-feast-raises-12m-to-fight-climate-change-with-plant-based-food/", status="defunct", country="DK", city="Copenhagen",
    rng="below_1b", focus="Consumer & Marketplaces", note="Plant-based meal boxes; the firm's post of 2018-08-23 announces the $12M Series A Balderton led; $33M Series B 2019; declared bankrupt in 2023 (the card says Exited)"))
L.append(und("smol", status="private", country="GB", city="London", rng="below_1b", focus="Consumer & Marketplaces",
    note="Subscription laundry and dishwasher products, founded 2018; the card says 'Series A in 2018', but the Series A Balderton led was July 2020 (the firm's post) and Chandratillake joined the board in Nov 2018, so the first position predates the A and its round is not named on any surface read"))
L.append(fp("soundtrack-your-brand", "Growth", status="private", country="SE", city="Stockholm", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Music streaming for businesses; card 'Series C in 2016' (the firm's post of 2017-02-17, $22M); the card says Exited (the firm sold), the company remains private as in Creandum's book"))
L.append(und("splashpower", status="acquired", country="GB", city="Cambridge", rng="below_1b", focus="Industrial & Robotics",
    note="Wireless charging pads; on the Benchmark Europe desk page 2004-08; the entry round is not named on any surface read; administration in 2008, the assets bought by Fulton Innovation (acquired out of insolvency)"))
L.append(fp("stream", "Series A", status="private", country="GB", country_src="web_verified", country_cite=LIST, city="London", rng="below_1b",
    focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Wagestream, renamed Stream in 2024: earned wage access and workplace finance; card 'Series A in 2019' (Moffat director of Stream Group Holdings from 2019-05); $90M Series D Jan 2026; the pre-filled status and country are a wrong Wikidata join; band re-checked in the A/B pass"))
L.append(und("sulake", status="acquired", country="FI", city="Helsinki", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Habbo Hotel; on the Benchmark Europe desk page 2005-06; the entry round is not named on any surface read; Balderton sold with 3i in 2012 (Wikipedia); acq. by Elisa, 2013, later Azerion"))
L.append(wv("sweep", "Series A", NEWS + "sweep-raises-22m-series-a-to-help-enterprises-lower-their-carbon-emissions/", status="private", country="FR", city="Paris",
    rng="below_1b", focus="Climate & Energy", note="Carbon management software; the firm's post of 2021-12-14 announces the $22M Series A Balderton led; $73M Series B Apr 2022"))
L.append(wv("sylvera", "Growth", NEWS + "sylvera-raises-57-million-series-b-to-incentivise-investment-in-real-climate-impact/", status="private", country="GB",
    city="London", rng="below_1b", focus="Climate & Energy", note="Carbon credit ratings; the firm's post of 2023-07-18 announces the $57M Series B Balderton led (Waterhouse director)"))
L.append(wv("taktile", "Growth", NEWS + "taktile-secures-54m-to-enable-risk-experts-to-take-control-of-ai-adoption-for-decision-making/", status="private", country="DE",
    city="Berlin", rng="below_1b", focus="AI & Applied AI", note="Decision automation for financial institutions; the firm's post of 2025-02-27 announces the $54M Series B Balderton led"))
L.append(fp("taptap-send", "Growth", status="private", country="GB", city="London", rng="below_1b", focus="Fintech & Payments",
    note="Remittances for immigrant communities; card 'Series B in 2025'; band re-checked in the A/B pass"))
L.append(wv("tempow", "Series A", NEWS + "tempow-announces-series-a-to-enable-bluetooth-as-a-platform-for-chipmakers-and-device-manufacturers/", status="acquired",
    country="FR", city="Paris", rng="below_1b", focus="Industrial & Robotics", note="Bluetooth audio software; the firm's post of 2018-05-23 announces the Series A Balderton led; acq. by Google, 2021 (status medium confidence; the card says Exited)"))
L.append(wv("tessian", "Series A", "https://techcrunch.com/2018/06/18/tessian/", status="acquired", country="GB", city="London", rng="below_1b",
    focus="Security", note="Email security; Balderton and Accel led the $13M Series A of Jun 2018 (TechCrunch; Chandratillake director 2018-23); acq. by Proofpoint, 2023"))
L.append(wv("testgorilla", "Series A", NEWS + "testgorilla-secures-70m-series-a-to-help-companies-eliminate-hiring-bias/", status="private", country="NL", city="Amsterdam",
    rng="below_1b", focus="SaaS", note="Pre-employment skills tests; the firm's post of 2022-06-14 announces the $70M Series A (Atomico and Balderton)"))
L.append(cls("the-exploration-company", status="private", city="Munich", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS + "the-exploration-company-raises-160-million-to-build-the-first-european-space-capsule/",
    rng="1b_plus", usd=2000000000, val_src="web_verified", asof="2026-07-27", val_conf="low",
    val_cite="https://thenextweb.com/news/exploration-company-300m-raise-spacex-rival", focus="Industrial & Robotics",
    note="Reusable space capsules; Balderton co-led the $160M Series B of Nov 2024 (the firm's post; card 'Series B in 2024'); the $450M Series C closed Sep 2026 with no price disclosed; the $2B figure is the press report of Jul 2026 on that round (FT via The Next Web), aligned to Atomico's book at low confidence (a $450M primary round cannot sit under a $1B valuation); Cherry's book reads below_1b, for the wave alignment"))
L.append(wv("the-org", "Series A", NEWS + "the-org-raises-8-5m-series-a-to-make-organisations-more-transparent/", status="private", country="US", city="New York",
    rng="below_1b", focus="SaaS", note="Public org charts; the firm's post of 2020-02-20 announces the $8.5M Series A; New York HQ (founded in Copenhagen)"))
L.append(fp("the-tab", "Series A", status="acquired", country="GB", city="London", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Student news network (Tab Media; Chandratillake director 2015-20); card 'Series A in 2015'; acq. by Digitalbox, 2020; Companies House 08125470 dissolved"))
L.append(fp("thg-the-hut-group", "Series A", status="public", country="GB", city="Manchester", focus="Consumer & Marketplaces", flags=["needs_web_value"],
    note="Online health and beauty retailer; card 'Series A in 2010' (Liautaud director of THG 2017-20); LSE IPO Sep 2020; market cap pinned in the A/B pass"))
L.append(wv("tibber", "Growth", NEWS + "tibber-closes-65m-funding-to-help-more-customers-lower-their-energy-bills-and-consumption/", status="private", country="NO",
    city="Førde", rng="below_1b", focus="Climate & Energy", note="Digital electricity supplier; the firm's post of 2020-11-17 announces the $65M Series B Balderton co-led; $100M Series C 2022"))
L.append(fp("tictail", "Seed", status="acquired", city="New York", entry_date="2011", rng="below_1b", focus="Consumer & Marketplaces",
    note="Storefronts for independent brands; card 'Seed in 2011'; $8M Series A Feb 2014 led by Thrive; acq. by Shopify, 2018"))
L.append(wv("tinybird", "Growth", NEWS + "tinybird-secures-30-million-series-b-to-expand-real-time-data-analytics-platform/", status="private", country="ES",
    city="Madrid", rng="below_1b", focus="Data Infrastructure", note="Real-time data platform; the firm's post of 2024-06-17 announces the $30M Series B Balderton led"))
L.append(fp("toucan-toco", "Series A", status="private", country="FR", city="Paris", rng="below_1b", focus="SaaS",
    note="Data storytelling software; card 'Series A in 2019' (the firm's post of 2019-11-28, EUR 12M led by Balderton)"))
L.append(fp("trademark-now", "Growth", conf="low", status="acquired", country="FI", city="Helsinki", rng="below_1b", focus="SaaS",
    note="Trademark search and management; card 'Series B in 2014' (the firm's post of 2014-05-07: a $3.5M investment led by Balderton, the round unnamed, so the label is low confidence); acq. by Corsearch, 2020"))
L.append(fp("traefik-labs", "Series A", status="private", country="FR", city="Lyon", rng="below_1b", focus="DevTools & APIs",
    note="Cloud-native networking (Containous until 2020); card 'Series A in 2020' (the firm's post of 2020-01-13, 'why we invested in Containous')"))
L.append(wv("trawa", "Seed", NEWS + "cleantech-trawa-raises-e10-million-to-cut-sme-energy-costs-and-emissions/", status="private", country="DE", city="Berlin",
    entry_date="2024-05-15", rng="below_1b", focus="Climate & Energy",
    note="Renewable electricity for industrial SMEs; the firm's post of 2024-05-15 announces the EUR 10M seed Balderton led; EUR 24M Series A May 2025",
    rounds=[rnd("2024-05-15", "Seed", 10800000, "Balderton Capital", True, NEWS + "cleantech-trawa-raises-e10-million-to-cut-sme-energy-costs-and-emissions/", "firm"),
            rnd("2025-05-22", "Series A", 27100000, None, True, NEWS + "trawa-raises-e24m-to-power-europes-industrial-comeback/", "firm")]))
L.append(wv("treasuryspring", "Growth", NEWS + "treasuryspring-raises-29-million-to-transform-the-future-of-cash-investment-for-businesses/", status="private",
    country="GB", city="London", rng="below_1b", focus="Fintech & Payments", note="Cash investment platform; the firm's post of 2023-06-26 announces the $29M Series B Balderton led (Yared director)"))
L.append(cls("truecaller", status="public", country="SE", city="Stockholm", stage="Growth", stage_src="first_party", stage_cite=LIST, stage_conf="medium",
    rng="below_1b", usd=690000000, val_src="web_verified", asof="2026-09-25", val_cite="https://companiesmarketcap.com/truecaller/marketcap/",
    focus="Consumer & Marketplaces",
    note="Caller ID and spam blocking; card 'Secondary in 2019' (Liquidity I; D5); Nasdaq Stockholm IPO Oct 2021; market cap about $0.69B on 2026-09-25, aligned to Atomico's book (same figure, same citation)"))
L.append(wv("uncommon", "Series A", NEWS + "uncommon-raises-30m-to-pave-the-way-for-scalable-cultivated-meat-utilising-rna-technologies/", status="private", country="GB",
    city="Cambridge", rng="below_1b", focus="Healthcare & Bio", note="Cultivated meat using RNA technology; the firm's post of 2023-06-09 announces the $30M Series A Balderton co-led (Waterhouse director from 2022-03)"))
L.append(fp("vanmoof", "Series A", status="acquired", city="Amsterdam", rng="below_1b", focus="Consumer & Marketplaces",
    note="E-bikes; card 'Series A in 2020' (the firm's post of 2020-05-13, EUR 12.5M led by Balderton); declared bankrupt Jul 2023, the business bought by McLaren Applied's Lavoie (acquired out of insolvency)"))
L.append(fp("vestiaire-collective", "Growth", status="private", country="FR", city="Paris", focus="Consumer & Marketplaces", flags=["needs_web_value"],
    note="Marketplace for pre-owned luxury fashion; card 'Series B in 2011'; the 2021 unicorn mark is pinned or killed in the A/B pass"))
jl.write("batch-005", L)
