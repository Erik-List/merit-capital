import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put({"slug": "rover", "who": jl.WHO, "valuation_range": "below_1b", "valuation_usd": None, "valuation_confidence": "high", "flags": [],
     "note": "Spark Growth led the $65M Series F (Jul 2017, Quinn board); SPAC listing Aug 2021 (NASDAQ: ROVR), taken private by Blackstone Feb 2024 ($2.3B) — acquired"})
put(row("runkeeper", "acquired", "Boston", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/Runkeeper", stage_conf="high", flags=["stage_disputes_band"],
        note="FitnessKeeper / Runkeeper; Spark led the $10M Series B (late 2011, Sabet board) — Growth; acq. by ASICS, Feb 2016"))
put(row("rylo", "acquired", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited"],
        note="360° camera; Spark in the Series A (2018); acq. by VSCO, Dec 2019"))
put(row("scale-ai", "private", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="low", flags=["cite_pending", "stage_uncited"], rng="10b_plus", usd=29000000000, asof="2025-06", val_src="unicorn_list", val_conf="medium",
        note="Spark joined the $100M Series C (Aug 2019, Founders Fund led) — to be cited; $29B mark (Meta's June 2025 investment) per the unicorn list, re-pinned in the A/B pass"))
put(row("shepherd", "private", "San Francisco", "US", "Seed", "model", "Fintech & Payments", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified", "model_disputes_source"],
        note="construction insurance MGA; Spark led the $6.2M seed (Oct 2021), the $13.5M Series A (2023) followed — graduated; Wikidata's GB is a homonym"))
put(row("sifive", "private", "Santa Clara", "US", "Growth", "model", "Industrial & Robotics", stage_conf="medium", flags=["stage_disputes_band", "needs_web_value"], rng=None,
        extra={"seed_to_a_graduation": None}, note="RISC-V processors; Spark led the $8.5M Series B (May 2017, Dagres board) — Growth (the band's Seed reads the size); $2.5B mark (2022) to be pinned"))
put(row("sift", "private", "San Francisco", "US", "Growth", "model", "Security", stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=1000000000, asof="2021-04", val_src="unicorn_list", val_conf="medium",
        note="Sift Science renamed Sift; Spark led the $18M Series B (2014) — Growth; $1B+ mark (Apr 2021) per the unicorn list, re-pinned in the A/B pass"))
put(row("sigma-computing", "private", "San Francisco", "US", "Growth", "model", "Data Infrastructure", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="cloud BI; Spark co-led the $200M Series D (May 2024) with Avenir; $1.5B mark to be pinned"))
put(row("signpost", "private", "New York", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="SMB marketing software; Spark led the 2012 Series A (Dagres board), the 2013 and 2015 rounds followed; the band's Seed reads the 2010 pre-Spark round"))
put(row("sincerely", "acquired", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified"],
        note="postcard app; Spark in the $3M 2011 round (firm news); acq. by Provide Commerce, 2013 — no A"))
put(row("skillshare", "private", "New York", "US", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://gigaom.com/2011/08/16/skillshare-raises-3-1m-to-make-every-person-a-teacher/", stage_conf="high",
        note="$3.1M Series A (Aug 2011, USV and Spark), the 2014 and 2016 rounds followed (Finkelstein board 2016); below $1B"))
put(row("slack", "acquired", "San Francisco", "US", "Growth", "web_verified", "SaaS", stage_cite=TC+"2015/04/16/used-daily-by-750k-workers-slack-raises-160m-to-value-collaboration-startup-at-2-8b/", stage_conf="high",
        note="Spark Capital Growth joined the $160M Series E (Apr 2015); NYSE: WORK 2019; acq. by Salesforce, Jul 2021 ($27.7B)"))
put(row("slite", "private", "Paris", "FR", "Series A", "model", "SaaS", stage_conf="medium",
        note="team knowledge base; Spark led the $11M Series A (2020)"))
put(row("smash-gg", "acquired", "San Francisco", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="esports tournament platform; Spark led the $11M Series A (Aug 2017); acq. by Microsoft, Dec 2020"))
put(row("smiledirectclub", "defunct", "Nashville", "US", "Growth", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited", "model_disputes_source"],
        note="Spark Growth joined the 2018 $380M round (Clayton Dubilier led) — Growth; NASDAQ: SDC 2019; Chapter 11 in Sept 2023 and shut down Dec 2023 — defunct (Wikidata's 'acquired' is wrong)"))
put(row("snap", "public", "Santa Monica", "US", "Growth", "model", "Consumer & Marketplaces", public=True, stage_conf="low", flags=["cite_pending", "stage_uncited"], rng="10b_plus", usd=11600000000, asof="2025-06-30", val_src="sec_public_float",
        note="NYSE: SNAP (IPO Mar 2017); Spark's position is a late private-market entry (no round names the firm) — to be cited; market cap re-pinned in the A/B pass (Lightspeed's Sept 2026 cap $9.45B)"))
put(row("socratic", "acquired", "New York", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified", "duplicate"],
        note="IDENTITY for the rebuild: Vespr Inc. is Socratic's legal name (Parker board 2013-2015) — merge queued; Spark led the seed (2013), the $6M Series A (2015, Shasta led) followed — graduated; acq. by Google, Mar 2018"))
put({"slug": "sonder", "who": jl.WHO, "status": "defunct", "valuation_range": "below_1b", "valuation_usd": None, "valuation_confidence": "high", "flags": ["model_disputes_source"],
     "note": "Spark led the $225M Series D (2019, Hyatt board); SPAC listing Jan 2022 (NASDAQ: SOND); Chapter 7 liquidation Nov 2025 — defunct (Wikidata's 'acquired' is wrong)"})
put(row("sonera", "private", None, "US", "Seed", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited", "censored", "city_unknown"],
        note="neural-signal sensing; Spark seed (2024)"))
put(row("soundhouse", "acquired", None, "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited", "city_unknown"],
        note="music-royalty acquirer; Spark in the 2018 round; acq. by Apollo Global Management, 2021 (site card)"))
put(row("sourcepoint", "private", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="publisher consent / compensation platform; Spark and Foundry led the $10M Series A (2015; Politi board)"))
put(row("sourgum", "private", None, "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited", "city_unknown"],
        note="waste-hauling marketplace; listed from 2026, Spark's 2025-2026 round unnamed"))
put(row("spinn", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="coffee hardware and marketplace; Spark led the $20M round of 2021 (Wikipedia; Thau board)"))
put(row("splash", "acquired", "New York", "US", "Series A", "model", "SaaS", stage_conf="medium",
        note="event marketing software; Spark led the $6M Series A (2015, firm news), joined the $7M Series B (Dec 2016); acq. by Cvent, 2023"))
put(row("spreadsheet-com", "unknown", "Redwood City", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="spreadsheet-database hybrid; Spark led the Series A (2021); listed 2022-2024, service wound down ~2024"))
put(row("stack-overflow", "acquired", "New York", "US", "Growth", "web_verified", "DevTools & APIs", stage_cite=TC+"2011/03/08/stack-overflow", stage_conf="high",
        note="Spark joined the $12M Series B (Mar 2011, Index led; Sabet board); acq. by Prosus, June 2021 ($1.8B)"))
put(row("standard-metrics", "private", "San Francisco", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="portfolio-reporting software for investors; Spark led the Series A (2024)"))
put(row("sternum", "private", "Tel Aviv", "IL", "Growth", "model", "Security", stage_conf="medium",
        note="IoT security; Spark led the $27M Series B (Sept 2021)"))
put(row("stoke-space", "private", "Kent", "US", "Growth", "model", "Industrial & Robotics", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="reusable rockets; Spark joined the $260M Series C (Jan 2025), listed from 2025; valuation to be pinned"))
put(row("storenvy", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="social marketplace; Spark led the $5M Series A (2012); still operating as a small marketplace"))
put(row("studs", "private", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="ear-piercing retail brand; Spark led the $15M Series A (2021)"))
put(row("superpedestrian", "defunct", "Cambridge", "US", "Seed", "model", "Industrial & Robotics", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified"],
        note="Copenhagen Wheel / e-scooters (MIT spin-out); Spark led the $2.1M seed (2013), Series A and B followed — graduated; shut down Dec 2023"))
put(row("synera", "private", "Bremen", "DE", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited"],
        note="ELISE renamed Synera (2023); low-code engineering platform; Spark led the 2023 round (Series A)"))
put(row("taptap-send", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium",
        note="remittances for immigrants; Spark led the $65M Series B (Dec 2021)"))
put(row("tashtego", "unknown", "Boston", "US", "Seed", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "city_unknown"], city_src="model_knowledge",
        note="listed 2010-2012 (Start@Spark era) and again 2018-2019 as fintech; the current tashtegollc.com is a reporting shell — status unknown, seed entry"))
put(row("tatch", "private", "New York", "US", "Seed", "model", "Healthcare & Bio", stage_conf="medium", flags=["duplicate", "cohort_unverified"],
        extra={"seed_to_a_graduation": None}, note="IDENTITY for the rebuild: Tatch rebranded Wesper (2021) — the 'wesper' row is the same company, merge queued; Spark led the $5.6M seed (2020, Politi board)"))
put(row("tenderly", "private", "San Francisco", "US", "Growth", "model", "Crypto & Web3", stage_conf="medium",
        note="blockchain developer platform (Belgrade / San Francisco); Spark led the $40M Series B (Mar 2022)"))
put(row("thalmic-labs", "acquired", "Kitchener", "CA", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["duplicate"],
        note="IDENTITY for the rebuild: renamed North (2018), merged into the 'north' row at the rebuild; Spark and Intel Capital led the $14.5M Series A (June 2013); acq. by Google, June 2020"))
put(row("the-bot-company", "private", "San Francisco", "US", "Growth", "model", "Industrial & Robotics", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="Kyle Vogt's home robots; Spark led the $150M first round (2024, Hyatt board) — an at-scale entry keyed Growth like Wayfair and Perch (label-vs-scale question for Erik); $2B mark (2025) to be pinned"))
put(row("theplatform", "acquired", "Seattle", "US", "Growth", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="online video publishing (founded 2000); Spark's 2006 round into a six-year-old company was one of the firm's first deals; acq. by Comcast, July 2006"))
put(row("tigerbeetle", "private", "San Francisco", "US", "Series A", "model", "Data Infrastructure", stage_conf="medium",
        note="financial transactions database; Spark led the $24M Series A (Sept 2024, Vais board)"))
put(row("tigris-data", "private", "San Francisco", "US", "Series A", "model", "Data Infrastructure", stage_conf="low", flags=["stage_uncited"],
        note="S3-compatible object storage for AI; listed from 2026, Spark-led 2025-2026 round"))
put(row("timehop", "private", "New York", "US", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/Timehop", stage_conf="high",
        note="$3M Series A from Spark (2013); small and private"))
put(row("tourlane", "private", "Berlin", "DE", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="multi-day tour booking; Spark led the Series A (2018) and co-led the $24M Series B (2019) with Sequoia"))
put(row("travelperk", "private", "Barcelona", "ES", "Series A", "model", "SaaS", stage_conf="medium", flags=["needs_web_value"], rng=None,
        note="business travel platform; Spark led the $7M Series A (2016, Finkelstein board); $2.7B mark (2025) to be pinned"))
if __name__ == "__main__": print(len(J), "judgments")
