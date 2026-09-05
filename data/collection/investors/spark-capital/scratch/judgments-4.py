import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put(row("mightytv", "acquired", "New York", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=False, grad_src="formd", grad_conf="medium", flags=["cohort_unverified"],
        note="video-discovery app; Spark led the $2.25M seed (2016, Politi board); acq. by Spotify, Mar 2017 — no A"))
put(row("milkrun", "defunct", "Portland", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified"],
        note="farm-direct grocery delivery; Spark seed (2021); ceased operations April 2023"))
put(row("mirror", "acquired", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["model_disputes_source"],
        note="connected home gym; Spark led the $13M Series A (Feb 2018); acq. by lululemon, June 2020 ($500M); Wikidata's IT is a homonym"))
put(row("mountaintop", "defunct", "Palo Alto", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="game studio (Spectre Divide); Spark in the $30M Series A (2022); studio closed March 2025"))
put(row("next-new-networks", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="high",
        note="acq. by Google/YouTube, Mar 2011; $8M launch round Mar 2007 with Spark (golden key)"))
put(row("nift", "private", "Boston", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="gift-based customer acquisition; Spark led the $16.5M Series A (2018, Politi board)"))
put(row("nomad", "private", "São Paulo", "BR", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "web_check", "model_disputes_source"],
        note="Brazilian global banking app; Spark joined a 2024-2025 growth round (listed from 2025); Wikidata's JP is a homonym; valuation checked in the momentum slice"))
put(row("noom", "private", "New York", "US", "Growth", "model", "Healthcare & Bio", stage_conf="low", flags=["cite_pending", "stage_uncited", "stale"], rng="1b_plus", usd=3700000000, asof="2021-05", val_src="unicorn_list", val_conf="medium",
        note="Spark's position is a late round (2021-2022; listed from 2022) — round to be named; the $3.7B Series F mark (May 2021) is stale, re-checked in the A/B pass"))
put(row("north", "acquired", "Kitchener", "CA", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["duplicate"],
        note="IDENTITY for the rebuild: Thalmic Labs (listed 2013-2019) renamed North (2018) — merge queued; Spark and Intel Capital led the $14.5M Series A (June 2013); acq. by Google, June 2020"))
put(row("noyo", "private", "San Francisco", "US", "Series A", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited"],
        note="benefits-data APIs; Spark in the $12.5M Series A (2020)"))
put(row("nuvo", "private", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="trade-credit platform; Spark co-led the $34M Series A (2025) with Sequoia"))
put(row("nylas", "private", "San Francisco", "US", "Growth", "model", "DevTools & APIs", stage_conf="medium", flags=["stage_disputes_band"],
        note="communications APIs; Spark led the $16M Series B (Aug 2018, Parker board) — Growth; the band's Series A reads the size"))
put(row("omgpop", "acquired", "New York", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=True, grad_conf="medium", flags=["stage_disputes_band", "cohort_unverified"],
        note="iminlikewithyou (2007) renamed OMGPOP; Spark seeded it in 2007 (firm news 2009: 'seed funding ... OMGPOP'), the 2010 $10.6M round is a follow-on (Sabet board) — graduated; acq. by Zynga, Mar 2012 ($180M)"))
put(row("oneriot", "acquired", "Boulder", "US", "Growth", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="Me.dium renamed OneRiot (2008); Spark entered at Me.dium's 2007 Series B, the 2009 $7M is the Series C (firm news; Politi board) — Growth; acq. by Walmart Labs, Sept 2011"))
put(row("optimism", "private", None, "US", "Growth", "model", "Crypto & Web3", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited", "city_unknown"], rng=None,
        note="OP Labs / Optimism Foundation (OP token: issuing organization, D7); Spark joined the 2022 Series B round ($150M, a16z and Paradigm led) — to be cited; $1.65B mark to be pinned; no single headquarters"))
put(row("orchard", "acquired", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="Orchard Platform (online-lending analytics); Spark led the $12M Series A (Nov 2014, Politi board); acq. by Kabbage, 2019"))
put(row("outreach", "private", "Seattle", "US", "Growth", "model", "SaaS", stage_conf="medium", flags=["cite_pending", "stale"], rng="1b_plus", usd=4400000000, asof="2021-06", val_src="unicorn_list", val_conf="medium",
        note="Spark Growth joined the $114M Series E (Apr 2019, Lone Pine led); $4.4B mark (June 2021) is stale, re-checked in the A/B pass"))
put(row("overtime", "private", "New York", "US", "Growth", "web_verified", "Media, Gaming & Advertising", stage_cite="https://en.wikipedia.org/wiki/Overtime_(sports_network)", stage_conf="high",
        note="Spark joined the $23M Series B (Feb 2019); the 2018 Series A was a16z's"))
put(row("owl-labs", "private", "Boston", "US", "Growth", "model", "Industrial & Robotics", stage_conf="medium",
        note="360° meeting cameras; Spark led the $15M Series B (Jul 2019)"))
put(row("panorama-education", "private", "Boston", "US", "Series A", "model", "SaaS", stage_conf="medium", flags=["stage_disputes_band"],
        extra={"seed_to_a_graduation": None}, note="K-12 survey software; Spark led the $12M Series A (Feb 2015, Parker board); the band's Seed rests on an unpriced filing"))
put(row("particle", "private", "San Francisco", "US", "Growth", "model", "Data Infrastructure", stage_conf="medium", flags=["stage_disputes_band"],
        note="IoT platform; Spark led the $20M Series B (Jul 2017, Parker board) — Growth; the band's Series A reads the size"))
put(row("perch", "private", "Boston", "US", "Growth", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["web_check"],
        note="Amazon-brand roll-up; Spark led the $123M 'Series A' (Dec 2020) — an at-scale first round into a one-year-old acquirer, keyed Growth like Wayfair (label-vs-scale question raised for Erik); the 2021 SoftBank round's mark did not hold — below_1b, web-checked"))
put(row("picturelife", "acquired", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="photo storage; Spark led the $4.5M Series A (2012, Hyatt board); acq. by StreamNation, 2014 (later shut)"))
put(row("pixie", "unknown", "Los Altos", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="Pixie item tracker; Spark led the $5M Series A (2013, Politi board), the 2016 $25M B followed; company dark since ~2019"))
put(row("plaid", "private", "San Francisco", "US", "Seed", "web_verified", "Fintech & Payments", stage_cite="https://en.wikipedia.org/wiki/Plaid_Inc.", stage_conf="high", grad=True, grad_src="web_verified", grad_conf="high",
        rng="10b_plus", usd=13400000000, asof="2021-04", val_src="unicorn_list", val_conf="medium", note="Spark led the $2.8M seed (Sept 2013); the $12.5M Series A (Nov 2014, NEA) — graduated; the unicorn-list $13.4B (2021) is superseded by the Feb 2026 $8B employee-sale mark — re-pinned in the A/B pass"))
put({"slug": "plume", "who": jl.WHO, "status": "private", "valuation_range": None, "valuation_usd": None, "valuation_confidence": "medium", "flags": ["needs_web_value", "model_disputes_source"],
     "note": "Plume Design (smart home WiFi software); Wikidata's 'acquired' is a homonym — Plume is private; $2.6B mark (Series F, 2021) to be pinned; Spark seeded it in 2016 (Dagres board), the 2017 A followed"})
put(row("poggio", "private", "San Francisco", "US", "Seed", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="AI customer-relationship platform; Spark seed (2022); graduation undetermined"))
put(row("polar-signals", "private", "Berlin", "DE", "Seed", "model", "DevTools & APIs", stage_conf="low", flags=["stage_uncited", "censored", "model_disputes_source"],
        extra={"seed_to_a_graduation": None}, note="continuous profiling (Parca); Spark led the 2024 seed (Vais board); the Form D address is the Delaware registered agent — the company is Berlin-based; too young for the graduation test"))
put(row("postmates", "acquired", "San Francisco", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite=TC+"2014/02/18/postmates-16m-spark-capital", stage_conf="high",
        note="acq. by Uber, Dec 2020 ($2.65B); Spark led the $16M Series B (Feb 2014, Hyatt board)"))
put(row("preveil", "private", "Boston", "US", "Series A", "model", "Security", stage_conf="low", flags=["stage_uncited"],
        note="end-to-end encrypted email and files; Spark led the Series A (2018)"))
put(row("priceonomics", "private", "San Francisco", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=False, grad_conf="medium", flags=["cohort_unverified"],
        note="Spark and a16z in the $1.5M seed (2012); pivoted to content marketing on seed capital, no priced A"))
put(row("privlo", "unknown", "Pasadena", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="non-QM mortgage lender; Spark in the 2014 Series A (listed 2014-2015, Finkelstein board 2015); lending wound down ~2018"))
put(row("producer", "private", None, "US", "Seed", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited", "censored", "city_unknown", "country_prior"],
        note="producer.ai music agent; listed from 2026, Spark seed"))
put(row("profluent", "private", "Berkeley", "US", "Series A", "model", "Healthcare & Bio", stage_conf="medium", flags=["web_check"],
        note="AI protein design; Spark led the $35M Series A (Mar 2024); valuation checked in the momentum slice"))
put(row("proletariat", "acquired", "Cambridge", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=True, grad_src="formd", grad_conf="medium", flags=["cohort_unverified"],
        note="Spellbreak studio; Spark in the $2.5M seed (2013, Hyatt board), the $20.9M A (2019) — graduated; acq. by Activision Blizzard, 2022"))
put(row("qriously", "acquired", "London", "GB", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_disputes_band", "stage_uncited", "model_disputes_source"], country_src="model_knowledge",
        extra={"seed_to_a_graduation": None}, note="mobile survey/ad platform (London; the Form D address is the Delaware agent); Spark led the 2014 Series A; acq. by Brandwatch, 2019"))
put(row("quaestor", "unknown", "San Francisco", "US", "Seed", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="startup financial reporting; Spark seed (2021); product folded ~2023"))
put({"slug": "quantopian", "who": jl.WHO, "status": "defunct", "valuation_range": "below_1b", "valuation_usd": None, "valuation_confidence": "high",
     "entry_stage": "Seed", "entry_stage_source": "web_verified", "entry_stage_confidence": "high", "entry_stage_citation": "https://www.crunchbase.com/funding_round/quantopian-seed--de420055",
     "hq_city": "Boston", "hq_city_source": "model_knowledge", "hq_country": "US", "hq_country_source": "model_knowledge", "focus": "Fintech & Payments", "focus_source": "model", "flags": [],
     "note": "Spark led the $2.15M seed (Jan 2012; Parker board), the 2013 A with Khosla — graduated (Form D); shut down Nov 2020 (team hired by Robinhood)"})
put(row("ramp", "private", "New York", "US", "Growth", "web_verified", "Fintech & Payments", stage_cite="https://ramp.com/blog/ramp-series-c", stage_conf="medium", rng="10b_plus", usd=32000000000, asof="2025-11", val_src="unicorn_list", val_conf="medium",
        note="Spark joined the $300M Series C (Aug 2021); $32B mark (Nov 2025) per the unicorn list — the June 2026 $44B round re-pinned in the A/B pass"))
put(row("rapyd", "private", "London", "GB", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["cite_pending", "stage_uncited"], rng="1b_plus", usd=8700000000, asof="2021-08", val_src="unicorn_list", val_conf="medium",
        note="Spark's position is a 2021 growth round (listed from 2021) — to be cited; $8.7B mark (Aug 2021) re-checked in the A/B pass"))
put(row("rare-bits", "defunct", "San Francisco", "US", "Seed", "model", "Crypto & Web3", stage_conf="medium", grad=False, grad_src="formd", grad_conf="medium", flags=["cohort_unverified"],
        note="crypto-collectibles marketplace; Spark led the $6M seed (Mar 2018, Hyatt board); shut down 2019"))
put(row("reggora", "private", "Boston", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="appraisal management for lenders; Spark led the $10M Series A (2019)"))
put(row("relay", "private", "Atlanta", "US", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "web_check", "model_disputes_source"],
        note="Relay Payments (trucking payments); Spark led the Series B (2021); Wikidata's 'acquired / ZA' is a homonym; valuation checked in the momentum slice"))
put(row("remarkable", "private", "Oslo", "NO", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/ReMarkable", stage_conf="high", flags=["web_check"],
        note="paper tablet; Spark led the $15M Series A (Oct 2019); the 2021 ~$1B secondary mark checked in the momentum slice"))
put(row("ridwell", "private", "Seattle", "US", "Series A", "model", "Climate & Energy", stage_conf="medium",
        note="hard-to-recycle pickup service; Spark led the $15M Series A (2025, Hyatt board)"))
if __name__ == "__main__": print(len(J), "judgments")
