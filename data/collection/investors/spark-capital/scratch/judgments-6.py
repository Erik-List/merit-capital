import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put(row("tray-io", "private", "San Francisco", "US", "Growth", "model", "DevTools & APIs", stage_conf="medium",
        note="integration platform; Spark led the $37M Series B (2019, Clayton board while at Spark); ~$600M mark (2021), below $1B"))
put(row("trello", "acquired", "New York", "US", "Series A", "web_verified", "SaaS", stage_cite=TC+"2014/07/24/trello-series-a/", stage_conf="high",
        note="$10.3M Series A (Jul 2014, Spark and Index; Sabet board); acq. by Atlassian, Jan 2017 ($425M)"))
put(row("tumblr", "acquired", "New York", "US", "Seed", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/Tumblr", stage_conf="high", grad=True, grad_src="web_verified", grad_conf="high",
        note="$750K seed (Oct 2007, Spark and USV), $4.5M Series B (Dec 2008) and later rounds — graduated; acq. by Yahoo, June 2013 ($1.1B)"))
put(row("twitter", "acquired", "San Francisco", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite="https://blog.twitter.com/en_us/a/2008/welcoming-bijan-and-jeff", stage_conf="high",
        note="Spark joined the Series B (2008; Sabet board); NYSE: TWTR 2013; taken private by Elon Musk, Oct 2022 ($44B) — acquired"))
put(row("uncommon", "unknown", "San Francisco", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="recruiting software; Spark led the $18M Series A (2018); listed 2018-2019, company dark since 2019"))
put(row("unleash", "private", "Oslo", "NO", "Growth", "model", "DevTools & APIs", stage_conf="low", flags=["stage_uncited"],
        note="open-source feature management; Spark led the 2023 round (Series B), listed from 2023"))
put(row("upworthy", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="Spark led the $8M Series A (Sept 2013); merged into GOOD Worldwide, 2017"))
put(row("velocity", "acquired", "London", "GB", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited", "model_disputes_source"],
        note="Velocity (later Velocity Black), restaurant payments turned luxury concierge; Spark led the $12M Series A (2015); acq. by Capital One, 2023; Wikidata's BR is a homonym"))
put(row("verana-networks", "private", "Waltham", "US", "Series A", "model", "Data Infrastructure", stage_conf="medium",
        note="5G RAN; Spark led the $10M Series A (2020, Politi board)"))
put(row("verivue", "acquired", "Westford", "US", "Series A", "model", "Data Infrastructure", stage_conf="low", flags=["stage_uncited"],
        note="video delivery infrastructure; Spark in the 2008 Series A (listed from 2008; Dagres board 2009); acq. by Akamai, Dec 2012"))
put(row("verse", "acquired", "Barcelona", "ES", "Series A", "model", "Fintech & Payments", stage_conf="medium", flags=["model_disputes_source"], country_src="model_knowledge",
        note="P2P payments app (Barcelona; the Form D address is the US entity); Spark led the $8.3M Series A (2016) and the $20.5M Series B (2017, Finkelstein board); acq. by Square, June 2020"))
put(row("videahealth", "private", "Boston", "US", "Series A", "model", "Healthcare & Bio", stage_conf="medium",
        note="dental AI; Spark led the $20M Series A (Jan 2022, Finkelstein board)"))
put(row("vinyl-equity", "private", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited"],
        note="modern transfer agent; Spark Capital VII investor with Finkelstein on the board from May 2024 (TA-1/A); Series A 2024"))
put(row("vivareal", "acquired", "São Paulo", "BR", "Growth", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="Brazilian real-estate marketplace; Spark led the $41.7M Series C (2014) — Growth; merged into Grupo ZAP (2017), acquired by OLX Brasil (2020)"))
put(row("warby-parker", "public", "New York", "US", "Growth", "web_verified", "Consumer & Marketplaces", public=True, stage_cite="https://news.crunchbase.com/retail/warby-parker-investment-history-public-debut/", stage_conf="medium", rng="1b_plus", usd=2174041230, val_src="sec_public_float",
        note="NYSE: WRBY (direct listing Sept 2021); Spark's first position is the January 2013 Series B tranche — Growth; market cap re-pinned in the A/B pass"))
put(row("wealthfront", "public", "Palo Alto", "US", "Growth", "web_verified", "Fintech & Payments", public=True, stage_cite="https://www.businesswire.com/news/home/20141028005968/en/Wealthfront-Raises-64-Million-in-Round-Led-by-Spark-Capital-Growth", stage_conf="high", flags=["needs_web_value"], rng=None,
        note="NASDAQ IPO Dec 2025 (the $0 SEC float predates the listing); Spark Capital Growth led the $64M Series D (Oct 2014); market cap pinned in the A/B pass"))
put(row("wesper", "private", "New York", "US", "Seed", "model", "Healthcare & Bio", stage_conf="medium", flags=["duplicate", "cohort_unverified"],
        extra={"seed_to_a_graduation": None}, note="IDENTITY for the rebuild: Wesper is Tatch rebranded (2021) — merged with the 'tatch' row at the rebuild; Spark led the $5.6M seed (2020)"))
put(row("wildtype", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["stage_disputes_band"],
        note="cultivated salmon; Spark led the $12.5M Series A (Oct 2019), joined the $100M Series B (2022, Hyatt board) — the band's Growth reads the B"))
put(row("wordware", "private", "San Francisco", "US", "Seed", "model", "AI & Applied AI", stage_conf="medium", flags=["censored"],
        note="AI agent IDE; Spark led the $30M seed (Nov 2024); too young for the graduation test"))
put(row("work-market", "acquired", "New York", "US", "Series A", "model", "SaaS", stage_conf="medium",
        note="freelance management platform; Spark and USV led the 2010/2011 Series A (Koyfman board per Wikipedia); acq. by ADP, Jan 2018"))
put(row("wunderite", "private", "Boston", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="insurance underwriting software; Spark led the $8M Series A (2023, Finkelstein board)"))
put(row("x1", "acquired", "San Francisco", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium", flags=["model_disputes_source"],
        note="X1 Card; Spark led the $12M Series A (2021); acq. by Robinhood, July 2023 ($95M); Wikidata's JP is a homonym"))
put(row("zeal", "private", "San Francisco", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="Puzzl Group / Zeal payroll API; Spark led the $13M Series A (2021, Sandman board)"))
put(row("zeller", "private", "Melbourne", "AU", "Series A", "model", "Fintech & Payments", stage_conf="medium", flags=["web_check"],
        note="Australian business payments; Spark led the A$25M Series A (Mar 2021) and joined the A$50M Series B (2021, ~A$1B valuation ≈ US$0.7B) — checked in the momentum slice"))
put(row("zum", "private", "Redwood City", "US", "Growth", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["stage_disputes_band", "needs_web_value"], rng=None,
        extra={"seed_to_a_graduation": None}, note="student transportation; Spark led the $19M Series B (2018) — Growth (the band anchors on a 2024 $4M filing); $1.3B mark (2024 Series E) to be pinned"))
put(row("4thmedia", "unknown", None, "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="2007 static-site listing only; entry round unnamed; company dark"))
put(row("adkeeper", "defunct", "New York", "US", "Series A", "web_verified", "Media, Gaming & Advertising", stage_cite="https://en.wikipedia.org/wiki/AdKeeper", stage_conf="medium",
        note="$8M first round (Mar 2010) from DCM, True, Spark, First Round, Betaworks; shut down 2012"))
put(row("altius-education", "defunct", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="online higher education (Ivy Bridge College); $8M Series A (2009, firm news 'altius education raises 8 million series a', Spark and Charles River), $18.6M Series B (2011); wound down 2013"))
put(row("base-power", "private", "Austin", "US", "Growth", "model", "Climate & Energy", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="distributed battery storage; Spark's position is a 2025 growth round (live-site listing only) — to be cited; valuation to be pinned"))
put(row("bumpers", "defunct", "New York", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified"],
        note="podcast-creation app; Spark seed (2016); shut down 2017"))
put(row("buzzwire", "defunct", "Denver", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="mobile video; Spark led the 2007 Series A; wound down 2009"))
put(row("close-io", "private", "San Francisco", "US", "Seed", "model", "SaaS", stage_conf="low", grad=False, grad_conf="medium", flags=["stage_uncited", "cohort_unverified"],
        note="Close.io sales CRM (Elastic Inc.); Spark and SV Angel in a small 2013/2016 round (firm news); no priced A — the company grew on revenue"))
put(row("coin", "acquired", "San Francisco", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "model_disputes_source"],
        note="Coin smart card; Spark in the 2014 Series A; acquired (acqui-hire) by Fitbit, May 2016; Wikidata's IT is a homonym"))
put(row("consumer-united", "acquired", "Boston", "US", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "duplicate"],
        note="IDENTITY for the rebuild: Consumer United renamed Goji (2015) — merged into the 'goji' row at the rebuild; acq. by Seeman Holtz, 2021"))
put(row("contextin", "unknown", "Tel Aviv", "IL", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited", "city_unknown"], city_src="model_knowledge",
        note="Israeli ad-tech; Spark in the 2011 Series A (listed 2011-2013); company dark"))
put(row("crusoe", "private", "San Francisco", "US", "Growth", "model", "Data Infrastructure", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="AI cloud infrastructure; Spark's position is a 2024-2025 growth round (live-site listing) — to be cited; $10B+ mark (2025) to be pinned"))
put(row("diy", "acquired", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="medium", grad=False, grad_conf="medium", flags=["cohort_unverified", "duplicate"],
        note="IDENTITY for the rebuild: DIY.org relaunched as JAM (2016) — the 'jam' row is the same company, merge queued; Spark led the $1M seed (2012), the $4.8M 2013 round is under the $5M graduation bar; acq. by littleBits, 2019"))
put(row("doctorsdirect", "unknown", None, "US", "Series A", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="2007 static-site listing only; company dark"))
put(row("drop-messages", "unknown", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified"],
        note="messaging app; Spark seed (2014); dark since 2017"))
put(row("edison-scientific", "private", "San Francisco", "US", "Series A", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="AI for scientific R&D; Spark-led 2025 round, listed from 2025"))
put(row("eqal", "acquired", "Los Angeles", "US", "Series A", "web_verified", "Media, Gaming & Advertising", stage_cite="https://en.wikipedia.org/wiki/EQAL", stage_conf="medium",
        note="lonelygirl15 studio; Spark among the initial investors (2008 Series A); acq. by Everyday Health, 2012"))
put(row("frontier-strategy-group", "unknown", "Washington", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="emerging-markets intelligence; Spark in the 2011 Series A; later ownership not documented"))
put(row("group-commerce", "unknown", "New York", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="e-commerce platform for publishers; Spark in the 2011 Series A; acquired Dealised's European operations (2016), later status not documented"))
put(row("hey", "unknown", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited", "city_unknown"], city_src="model_knowledge",
        note="2014-2016 listing under 'seed'; company dark"))
put(row("intune", "defunct", "Dublin", "IE", "Series A", "model", "Data Infrastructure", stage_conf="low", flags=["stage_uncited"],
        note="Intune Networks (optical packet transport); Spark in the 2007 Series A (listed from 2007); wound down ~2016"))
if __name__ == "__main__": print(len(J), "judgments")
