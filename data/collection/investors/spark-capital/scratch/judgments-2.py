import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
J["verdict:cnet"] = verdict("cnet", "not_member", "The Spark funds' Forms 3/4 on CNET Networks (Jan 2008) are the activist stake taken beside JANA Partners and Sandell in the 2008 CNET proxy contest (JANA/Spark 13D group), sold into the CBS acquisition; CNET was public since 1996 and never raised a venture round from the firm — a public purchase with no venture entry (T3, decisions.md D6, ruling 14). The 2021-2025 Webflow alumni card records that stake, not a portfolio position.", "fund_filing", "high", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1015577&type=SC%2013D&dateb=&owner=include&count=40")
put(row("coach-me", "private", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited"],
        note="Lift (2012) renamed Coach.me (2015); Spark in the seed (site label 'seed'); no priced A on the record — graduation undetermined; still operating as a small company"))
put(row("coinbase", "public", None, "US", "Growth", "web_verified", "Crypto & Web3", public=True, stage_cite=TC+"2017/08/10/coinbase-raises-100m-at-a-1-6b-valuation-amid-explosive-growth/", stage_conf="high", flags=["needs_web_value", "city_unknown"], rng=None,
        note="NASDAQ: COIN (direct listing Apr 2021); Spark joined the $100M Series D (Aug 2017, IVP led) — Growth entry; the company declared itself remote-first with no headquarters in 2021 (hq_city null); market cap pinned in the A/B pass"))
put(row("colu", "private", "Tel Aviv", "IL", "Seed", "model", "Fintech & Payments", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified"],
        note="city-currency / municipal rewards platform; Spark and Aleph in the $2.5M seed (Jan 2015) and the $9.6M Series A (2016); operating in Israel"))
put(row("common", "private", None, "US", "Series A", "model", "Crypto & Web3", stage_conf="low", flags=["stage_uncited", "city_unknown"],
        note="common.xyz token-community platform; listed from 2026, Spark's 2026 round unnamed"))
put(row("comulate", "private", "San Francisco", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited"],
        note="insurance revenue automation; Spark-led 2024 round (Series A), listed from 2024"))
put(row("convertmedia", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="outstream video ads (Israel/New York); Spark led the Series A (2013); acq. by Taboola, 2016 (~$100M)"))
put(row("convex", "private", "San Francisco", "US", "Growth", "model", "DevTools & APIs", stage_conf="low", flags=["stage_uncited"],
        note="reactive backend platform (a16z-led 2022 Series A); Spark's position is a 2025-2026 round, listed from 2026"))
put(row("cosuno", "private", "Berlin", "DE", "Growth", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited", "web_check"],
        note="construction procurement SaaS; Spark led the $30M Series B (Jan 2022); operating status to be re-checked (German construction downturn)"))
put(row("cover-genius", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium", flags=["needs_web_value", "identity_uncertain", "duplicate"], rng=None,
        note="IDENTITY DEFECT for the scheduled rebuild: the build's word-prefix rule folded 'Cover' (the 2014-2015 listed restaurant-payments app) into 'Cover Genius' (the 2026-listed insurtech whose $80M Series E, Sept 2024, Spark led); never_merge pair queued in identity-merges.json; this row is judged as Cover Genius"))
put(row("covestor", "acquired", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium", flags=["stage_disputes_band"],
        note="acq. by Interactive Brokers, 2015; Spark in the 2008 Series A (listed from 2008, Dagres board 2010-2013); the band's Growth reads a mis-keyed 2010 filing amount"))
put(row("crowdrise", "acquired", "Los Angeles", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="acq. by GoFundMe, Jan 2017; Spark led the 2014 Series A (Sabet board), the 2015 $5M is a follow-on"))
put(row("cruise", "acquired", "San Francisco", "US", "Series A", "web_verified", "Industrial & Robotics", stage_cite=TC+"2015/09/18/cruise-2/", stage_conf="high",
        note="acq. by General Motors, Mar 2016 (~$1B); $12.5M Series A co-led by Spark and Sam Altman, Sept 2015"))
put(row("ctrl-labs", "acquired", "New York", "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited"],
        note="neural interfaces; Spark in the $28M Series A (Feb 2018); acq. by Facebook, Sept 2019 (~$500M-1B)"))
put(row("cybereason", "private", "Boston", "US", "Growth", "web_verified", "Security", stage_cite=TC+"2015/05/06/cybereason-raises-25m-because-corporate-security-is-broken/", stage_conf="high",
        note="Spark led the $25M Series B, May 2015 (Politi board); the 2021 $3.3B mark collapsed (2023 SoftBank-led recapitalisation at a fraction of it) — below_1b on collapse evidence"))
put(row("cyera", "private", "New York", "US", "Growth", "model", "Security", stage_conf="low", flags=["cite_pending", "stage_uncited", "model_disputes_source"], rng="10b_plus", usd=12000000000, asof="2025-11", val_src="unicorn_list", val_conf="medium",
        note="data security platform (New York / Tel Aviv); Spark's position is the late 2025/2026 round (listed from 2026); the unicorn list's country string was malformed — HQ New York, US"))
put(row("dataplor", "private", None, "US", "Series A", "model", "Data Infrastructure", stage_conf="low", flags=["stage_uncited", "city_unknown"],
        note="global location intelligence; Spark-led 2024 round, listed from 2025"))
put(row("descript", "private", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="medium",
        note="Spark led the $50M Series C (Nov 2022, with the OpenAI Startup Fund; Hyatt board); $553M valuation — below $1B"))
put(row("discord", "private", "San Francisco", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite=TC+"2017/06/07/discord/", stage_conf="medium", rng="10b_plus", usd=15000000000, asof="2021-09", val_src="unicorn_list", val_conf="medium",
        note="Spark's first Discord position is the ~$50M Index-led round of early 2017 (Series C); $15B mark (Sept 2021) per the unicorn list, web-pinned in the A/B pass"))
put(row("dooly", "private", "Vancouver", "CA", "Growth", "model", "SaaS", stage_conf="medium",
        note="Spark led the $80M Series B (May 2021); below $1B"))
put(row("droplette", "private", "Boston", "US", "Series A", "model", "Healthcare & Bio", stage_conf="medium",
        note="micro-infusion skincare / drug delivery (MIT spin-out); Spark led the Series A (2019, Politi board)"))
put(row("durable", "private", "Vancouver", "CA", "Series A", "model", "AI & Applied AI", stage_conf="medium", flags=["model_disputes_source"],
        note="AI website builder for service businesses; Spark led the $14M Series A (Mar 2023); Wikidata's DE is a homonym (durable.co is Vancouver-based)"))
put(row("earnin", "private", "Palo Alto", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium",
        note="earned-wage access; Spark Growth in the $125M Series C (Dec 2018, DST led); below $1B"))
put(row("enfabrica", "private", "Mountain View", "US", "Growth", "model", "Industrial & Robotics", stage_conf="medium", flags=["web_check"],
        note="AI networking silicon; Spark led the $115M Series C (Nov 2024); valuation undisclosed, checked in the momentum slice"))
put(row("etoro", "public", "Limassol", "CY", "Growth", "web_verified", "Fintech & Payments", public=True, stage_cite=TC+"2011/01/26/etoro-funding", stage_conf="high", flags=["needs_web_value", "stage_disputes_band"], rng=None, country_src="formd_address",
        note="NASDAQ: ETOR (IPO May 2025); Spark led the $8.3M round announced Jan 2011 (eToro's Series C; Politi board) — Growth entry, the band's 'Series A' reads the size; registered office Limassol (Form D), operations Tel Aviv; market cap pinned in the A/B pass"))
put(row("everything-but-the-house", "private", "Cincinnati", "US", "Growth", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited"],
        note="online estate-sale marketplace; Spark entered at the 2015 rounds ($13M A / $30M B; Finkelstein board from 2015) — Growth per the band, round to be named"))
put(row("exfm", "defunct", "New York", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["stage_disputes_band", "cohort_unverified"], grad=False, grad_src="formd", grad_conf="medium",
        note="ExtensionFM / exfm music discovery; Spark seeded it (Sabet board 2010-2012; $0.5M, $0.75M, $1.5M rounds — seed money, the band's Pre-Seed reads the size); shut down Jan 2013, no A"))
put(row("feather", "private", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="furniture rental; Spark led the $12M Series A (Aug 2019, Thau board), the 2020 $30M Series B followed"))
put(row("fig", "acquired", "San Francisco", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["stage_disputes_band", "cohort_unverified"],
        note="games crowdfunding platform; Spark seeded Fig (2015; Wikipedia: 'initially backed by seed funding from Spark Capital') — the band's Pre-Seed reads the $73K Fig Productions 1 LLC project vehicle, not the company's round; acq. by Republic, 2020; graduation undetermined"))
put(row("fireblocks", "private", "New York", "US", "Growth", "model", "Crypto & Web3", stage_conf="medium", flags=["needs_web_value", "cite_pending", "model_disputes_source"], rng=None,
        note="digital-asset custody; Spark co-led the $310M Series D (Jul 2021); HQ New York (R&D Tel Aviv; Wikidata's IL reads the founding country); $8B mark (Jan 2022) to be pinned"))
put(row("fitorbit", "defunct", "Los Angeles", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["cohort_unverified"], grad=True, grad_src="formd", grad_conf="low",
        note="online fitness coaching (Brentwood, Los Angeles); Spark in the 2011 rounds (Dagres and Miller boards), the 2012 $9M follow-on; shut down ~2014"))
put(row("flock-safety", "private", "Atlanta", "US", "Growth", "model", "Security", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="the Form D director seats 2020-2022 are Alex Clayton's Meritech seats (he left Spark in 2019) — membership rests on the 2026 site listing; Spark's own position is a late round (2024-2025), to be named; $7.5B mark (2025) to be pinned"))
put(row("formation-bio", "private", "New York", "US", "Growth", "model", "Healthcare & Bio", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="TrialSpark renamed Formation Bio (2023); Spark joined the 2021 Series C ($156M); valuation after the $372M 2024 round to be pinned"))
put(row("foursquare", "private", "New York", "US", "Growth", "web_verified", "Data Infrastructure", stage_cite=TC+"2011/06/24/foursquare-closes-50m-at-a-600m-valuation/", stage_conf="high",
        note="Spark entered at the $50M Series C (June 2011, a16z led) and later bought ~$50M of employee stock (2013 secondary); merged with Factual 2020, private, below $1B; now a location-data platform"))
put(row("framework", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="repairable laptops; Spark led the $18M Series A (Feb 2022, Thau board)"))
put(row("freight-farms", "private", "Boston", "US", "Series A", "model", "Industrial & Robotics", stage_conf="medium", flags=["stage_disputes_band"],
        extra={"seed_to_a_graduation": None}, note="container farms; Spark led the $3.7M round of late 2014 (firm news 2015; Dagres board) after the 2013 seed without the firm — Series A entry"))
put(row("friends-with-benefits", "private", None, "US", "Series A", "model", "Crypto & Web3", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"], country_src="model_knowledge",
        note="FWB DAO ($FWB token, treasury and governance — an issuing organization, D7); Spark joined the $10M a16z-led round (Oct 2021); no headquarters"))
put(row("full-harvest", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="B2B surplus-produce marketplace; Spark led the $8.5M Series A (2018)"))
put(row("fundbox", "private", "San Francisco", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="SMB credit; Spark Capital Growth led the $50M Series B (Sept 2015); $1.1B mark (Nov 2021) to be pinned"))
put(row("fundersclub", "private", "San Francisco", "US", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited"],
        note="online VC platform; Spark led the $6M Series A (2013)"))
put(row("garden", "private", "New York", "US", "Seed", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited", "model_disputes_source", "censored"],
        note="AI patent discovery; Spark-led seed (2025); Wikidata's JP is a homonym"))
put(row("gdgt", "acquired", "San Francisco", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=False, grad_conf="medium", flags=["cohort_unverified"],
        note="gadget community by the Engadget founders; Spark seeded it (2010 firm news 'raises new financing'); acq. by AOL, 2013 — no A before the exit"))
put(row("generalist", "private", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="embodied foundation models; Spark's first position is the 2026 $400M round (Kelton board) — Growth; valuation to be pinned"))
put(row("getyourguide", "private", "Berlin", "DE", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/GetYourGuide", stage_conf="high", rng="1b_plus", usd=1000000000, val_src="unicorn_list", val_conf="medium",
        note="$14M Series A (Jan 2013) from Spark and Highland (firm news 2014 'getyourguide seals 14m series a'); unicorn-list $1B mark is old (2023 round at ~$2B), re-pinned in the A/B pass"))
put(row("glossier", "private", "New York", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite="https://www.prnewswire.com/news-releases/glossier-inc-raises-100-million-to-build-the-future-beauty-company-300814345.html", stage_conf="high", flags=["needs_web_value"], rng=None,
        note="Spark joined the $100M Series D (Mar 2019, Sequoia led); $1.8B mark (2021) to be pinned"))
if __name__ == "__main__": print(len(J), "judgments")
