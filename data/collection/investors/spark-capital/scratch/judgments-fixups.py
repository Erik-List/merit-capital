"""Fix-ups outside the queue: the 14 rows prepare resolved deterministically (pre-fill is not judgment, §8),
homonym public floats quarantined (duty 8), band stages re-judged, and cross-investor alignments."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row = jl.row
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put(row("abridge", "private", "Pittsburgh", "US", "Growth", "web_verified", "Healthcare & Bio", stage_cite="https://www.businesswire.com/news/home/20231026850279/en/Abridge-raises-%2430M-to-Accelerate-Adoption-of-its-Proven-Generative-AI-Solution-across-U.S.-Healthcare-Systems", stage_conf="high", rng="1b_plus", usd=2750000000, asof="2025-02", val_src="unicorn_list", val_conf="medium",
        note="Spark led the $30M Series B (Oct 2023; Will Reed board from the 2024 C); HQ Pittsburgh; $2.75B mark (Feb 2025 Series D) per the unicorn list, re-pinned in the A/B pass"))
put(row("andela", "private", "New York", "US", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://www.pehub.com/2015/06/spark-leads-series-a-for-andela/", stage_conf="high", flags=["stage_disputes_band", "stale"], rng="1b_plus", usd=1500000000, asof="2021-09", val_src="unicorn_list", val_conf="medium",
        note="global talent marketplace (New York; founded Lagos); Spark led the $10M Series A (June 2015) — the band's Growth reads the 2017 filing; $1.5B mark (Sept 2021, SoftBank) is stale, re-checked in the A/B pass"))
put(row("carta", "private", "San Francisco", "US", "Series A", "web_verified", "Fintech & Payments", stage_cite="https://www.finsmes.com/2015/01/eshares-raises-series-a-funding.html", stage_conf="high", flags=["stage_disputes_band", "stale"], rng="1b_plus", usd=7400000000, asof="2021-08", val_src="unicorn_list", val_conf="medium",
        note="eShares renamed Carta; Spark in the $7M Series A (Jan 2015, USV led) and led the $17M Series B (Aug 2015; Parker board 2017-2019) — the band's Growth reads the later filings; $7.4B mark (Aug 2021) is stale, re-checked in the A/B pass"))
put({"slug": "co-star", "who": jl.WHO, "status": "private", "is_public": False, "valuation_range": "below_1b", "valuation_usd": None, "valuation_asof": None, "valuation_source": None, "valuation_confidence": "high",
     "entry_stage": "Series A", "entry_stage_source": "web_verified", "entry_stage_confidence": "high", "entry_stage_citation": "https://en.wikipedia.org/wiki/Co%E2%80%93Star",
     "hq_city": "New York", "hq_city_source": "model_knowledge", "hq_country": "US", "hq_country_source": "model_knowledge", "focus": "Consumer & Marketplaces", "focus_source": "model",
     "flags": ["model_disputes_source", "cik_weak"], "note": "Co-Star Astrology Society: Spark led the $15M Series A (Apr 2021; Thau board); the SEC float layer matched CoStar Group (NASDAQ: CSGP) — a name collision, quarantined (duty 8)"})
put(row("deel", "private", "San Francisco", "US", "Growth", "web_verified", "SaaS", stage_cite=TC+"2020/09/09/deel-nabs-30m-more-for-payroll-compliance-and-other-tools-to-run-global-workforces/", stage_conf="high", rng="10b_plus", usd=17300000000, asof="2025-10", val_src="unicorn_list", val_conf="medium",
        note="Spark led the $30M Series B (Sept 2020; Razavi board); $17.3B mark (Oct 2025) per the unicorn list, re-pinned in the A/B pass"))
put(row("flywire", "public", "Boston", "US", "Series A", "web_verified", "Fintech & Payments", public=True, stage_cite=TC+"2011/08/15/peertransfer-raises-7-5-million-from-spark-accel-and-maveron-to-help-students-save-money-on-payments/", stage_conf="high", flags=["stage_disputes_band"], rng="1b_plus", usd=1351794027, asof="2025-06-30", val_src="sec_public_float",
        extra={"seed_to_a_graduation": None}, note="peerTransfer renamed Flywire; Spark led the $7.5M Series A (Aug 2011; Finkelstein board) — the band's Seed reads the 2013 filing size; NASDAQ: FLYW (IPO May 2021); market cap re-pinned in the A/B pass"))
put(row("granola", "private", "London", "GB", "Series A", "model", "AI & Applied AI", stage_conf="medium", flags=["cite_pending", "model_disputes_source"], rng="1b_plus", usd=1500000000, asof="2026", val_src="unicorn_list", val_conf="medium",
        note="AI meeting notes (London); Spark led the $20M Series A (Oct 2024; Hyatt board) — the US Form D address is the Delaware entity; $1.5B mark (2026) per the unicorn list, re-pinned in the A/B pass"))
put(row("headway", "private", "New York", "US", "Growth", "model", "Healthcare & Bio", stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=2300000000, asof="2024-07", val_src="unicorn_list", val_conf="medium",
        note="TherapyMatch, Inc. / Headway (mental-health network); Spark led the $70M Series C (Oct 2021) — Growth; $2.3B mark (July 2024 Series D) per the unicorn list, re-pinned in the A/B pass"))
put(row("niantic", "private", "San Francisco", "US", "Growth", "web_verified", "Media, Gaming & Advertising", stage_cite=TC+"2017/11/24/pokemon-go-creator-raises-200-million-ahead-of-harry-potter-game-launch/", stage_conf="high", flags=["stale"], rng="1b_plus", usd=3950000000, asof="2019-01", val_src="unicorn_list", val_conf="medium",
        note="Spark led the $200M Series B (Nov 2017; Quinn board); the $3.95B mark (Jan 2019 Series C) is stale — the 2025 sale of the games business to Scopely ($3.5B) and the Niantic Spatial spin-out are re-checked in the A/B pass"))
put({"slug": "oculus", "who": jl.WHO, "status": "acquired", "is_public": False, "valuation_range": "below_1b", "valuation_usd": None, "valuation_asof": None, "valuation_source": None, "valuation_confidence": "high",
     "entry_stage": "Series A", "entry_stage_source": "web_verified", "entry_stage_confidence": "high", "entry_stage_citation": "https://thenextweb.com/news/oculus-rift-raises-16m-from-spark-capital-to-bring-its-virtual-reality-platform-to-the-masses",
     "hq_city": "Irvine", "hq_city_source": "model_knowledge", "hq_country": "US", "hq_country_source": "model_knowledge", "focus": "Consumer & Marketplaces", "focus_source": "model",
     "flags": ["model_disputes_source", "cik_weak", "stage_disputes_band"], "note": "Oculus VR: $16M Series A co-led by Spark and Matrix (June 2013; Politi board); acq. by Facebook, March 2014 ($2B); the SEC float layer matched an unrelated public 'Oculus' registrant (CIK 1107280) — quarantined (duty 8)"})
put(row("pendo", "private", "Raleigh", "US", "Growth", "web_verified", "SaaS", stage_cite="https://www.pendo.io/news/pendo-raises-20-million-series-b-funding-led-by-spark-capital-to-accelerate-the-consumerization-of-enterprise-software/", stage_conf="high", flags=["stage_disputes_band", "stale"], rng="1b_plus", usd=2600000000, asof="2021-07", val_src="unicorn_list", val_conf="medium",
        note="Spark led the $20M Series B (Dec 2016; Quinn board) — Growth, the band's Series A reads the size; $2.6B mark (July 2021) is stale, re-checked in the A/B pass"))
put(row("smartrent", "public", "Scottsdale", "US", "Growth", "model", "SaaS", public=True, stage_conf="medium", rng="below_1b", usd=116100000, asof="2025-06-30", val_src="sec_public_float",
        note="NYSE: SMRT (SPAC Aug 2021); Spark Growth in the $60M Series C (Mar 2020; Will Reed board 2021) — Growth"))
put(row("talkspace", "public", "New York", "US", "Series A", "model", "Healthcare & Bio", public=True, stage_conf="medium", rng="below_1b", usd=393200000, asof="2025-06-30", val_src="sec_public_float",
        note="Groop Internet Platform Inc.; Spark led the $9.5M Series A (2015; Finkelstein board 2016-2019); NASDAQ: TALK (SPAC June 2021)"))
put(row("wayfair", "public", "Boston", "US", "Growth", "web_verified", "Consumer & Marketplaces", public=True, stage_cite="https://en.wikipedia.org/wiki/Wayfair", stage_conf="high", flags=["cite_pending"], rng="1b_plus", usd=5200000000, asof="2025-06-30", val_src="sec_public_float",
        note="CSN Stores renamed Wayfair; Spark in the $165M June 2011 round (Finkelstein board 2012) — at-scale entry keyed Growth (label-vs-scale question raised for Erik); NYSE: W (IPO Oct 2014); market cap re-pinned in the A/B pass"))
# ---- cross-investor alignments and corrections found in later batches
put(row("behalf", "private", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium",
        note="Zazma renamed Behalf (2014); Spark and Sequoia in the $10M Series A (2014, firm news 'zazma comes out of stealth') — entry corrected from the 2015 debt-and-equity round to the Series A; below $1B"))
put(row("quantopian", "acquired", "Boston", "US", "Seed", "web_verified", "Fintech & Payments", stage_cite="https://www.crunchbase.com/funding_round/quantopian-seed--de420055", stage_conf="high",
        extra={"seed_to_a_graduation": True, "graduation_source": "formd", "graduation_confidence": "high"}, note="Spark led the $2.15M seed (Jan 2012; Parker board), the 2013 A with Khosla — graduated; wound down Nov 2020 with the team hired by Robinhood — acquired (acqui-hire), aligned with the a16z base"))
put(row("priceonomics", "unknown", "San Francisco", "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="medium", grad=False, grad_conf="medium", flags=["cohort_unverified"],
        note="Spark and a16z in the $1.5M seed (2012); pivoted to content marketing on seed capital, no priced A; quiet since — status unknown, aligned with the a16z base"))
put(row("glossier", "private", "New York", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite="https://www.prnewswire.com/news-releases/glossier-inc-raises-100-million-to-build-the-future-beauty-company-300814345.html", stage_conf="high", extra={"clear_flags": ["needs_web_value"]},
        note="Spark joined the $100M Series D (Mar 2019, Sequoia led); the $1.8B 2021 mark did not hold — the 2025 raise was sought at under $1B (collapse evidence carried by the Sequoia and Thrive bases) — below_1b, aligned"))
if __name__ == "__main__": print(len(J), "fix-ups")
