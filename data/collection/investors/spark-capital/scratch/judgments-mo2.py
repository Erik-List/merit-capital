WHO = "agent-judge-pro85"
def mo(slug, stage, year, stage_url, band_url, note, rng="below_1b", usd=None, asof=None, flags=(), clear=(), status=None, conf="high", extra=None):
    r = {"slug": slug, "who": WHO, "entry_stage": stage, "entry_year": year, "entry_stage_source": "web_verified", "entry_stage_citation": stage_url, "entry_stage_confidence": conf,
         "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_range_citation": band_url, "valuation_confidence": conf, "clear_flags": sorted(set(clear) | {"stage_uncited", "web_check", "needs_web_value"}), "flags": sorted(set(flags)), "note": note}
    if usd: r.update({"valuation_usd": usd, "valuation_asof": asof, "valuation_source": "web_verified", "valuation_citation": band_url})
    if status: r["status"] = status
    if extra: r.update(extra)
    return r
J = {}
J["cimulate"] = {"slug": "cimulate", "who": WHO, "status": "acquired", "status_source": "web_verified", "status_citation": "https://cimulate.ai/press/", "clear_flags": [], "flags": [],
    "note": "AI commerce search (Boston); Spark led the $28M Series A (Dec 2024); acq.: Salesforce signed a definitive agreement to acquire Cimulate — the company site now reads 'Cimulate is now part of Salesforce' (2026)"}
J["heyday"] = mo("heyday", "Seed", 2022, "https://www.businesswire.com/news/home/20220628005293/en/Heyday-Raises-%246.5M-for-AI-Powered-Research-Assistant-that-Makes-Knowledge-Workers-Smarter", "https://www.businesswire.com/news/home/20220628005293/en/Heyday-Raises-%246.5M-for-AI-Powered-Research-Assistant-that-Makes-Knowledge-Workers-Smarter",
    "AI research assistant; Spark led the $6.5M seed (Jun 2022; Kevin Thau board); no priced A on the record — below $1B", extra={"seed_to_a_graduation": False, "seed_to_a_graduation_source": "web_verified", "seed_to_a_graduation_confidence": "medium"})
J["latent-technology"] = mo("latent-technology", "Seed", 2023, "https://www.finsmes.com/2023/02/latent-technology-raises-2-1m-in-pre-seed-funding.html", "https://siliconcanals.com/latent-technology-secures-e6-9m/",
    "generative-physics game animation (London); Root and Spark led the $2.1M pre-seed (Feb 2023), Spark co-led the $8M seed with AlbionVC (2025) — still seed, below $1B", extra={"hq_city": "London", "hq_city_source": "web_verified", "hq_country": "GB", "hq_country_source": "web_verified"})
J["lumafield"] = mo("lumafield", "Growth", 2023, "https://www.lumafield.com/article/lumafield-announces-75-million-series-c-funding-and-bill-cronin-as-head-of-revenue", "https://www.lumafield.com/article/lumafield-announces-75-million-series-c-funding-and-bill-cronin-as-head-of-revenue",
    "industrial CT scanning; Spark is named an existing investor at the $75M Series C led by IVP (Mar 2025), so the entry predates it (Series B era, 2023); valuation undisclosed — below $1B", conf="medium")
J["nuvo"] = mo("nuvo", "Series A", 2025, "https://techcrunch.com/2025/04/30/nuvo-a-network-for-b2b-trade-has-nabbed-34m-from-a-whos-who-list-of-investors/", "https://techcrunch.com/2025/04/30/nuvo-a-network-for-b2b-trade-has-nabbed-34m-from-a-whos-who-list-of-investors/",
    "B2B trade-credit network; $34M Series A led by Sequoia with Spark (Apr 2025), $45M raised in total — below $1B")
J["piston-technologies-inc"] = mo("piston-technologies-inc", "Seed", 2025, "https://fintech.global/2025/06/11/fleet-payments-platform-piston-secures-6-1m-seed-funding/", "https://fintech.global/2025/06/11/fleet-payments-platform-piston-secures-6-1m-seed-funding/",
    "fleet fuel payments; Spark led the $6.1M seed (Jun 2025; $7.5M with the PearX pre-seed) — below $1B, too young for the graduation test", flags=["censored"])
J["polar-signals"] = mo("polar-signals", "Seed", 2024, "https://www.businesswire.com/news/home/20240312380887/en/Polar-Signals-Announces-Strategic-Milestones-Secures-$10.8M-in-Funding-Expands-Board-and-Launches-AI-Driven-Performance-Optimizations", "https://www.businesswire.com/news/home/20240312380887/en/Polar-Signals-Announces-Strategic-Milestones-Secures-$10.8M-in-Funding-Expands-Board-and-Launches-AI-Driven-Performance-Optimizations",
    "continuous profiling; Spark led the $6.8M seed extension (Mar 2024; $10.8M seed in total with GV and Lightspeed) — below $1B", flags=["censored", "model_disputes_source"])
J["profluent"] = mo("profluent", "Series A", 2024, "https://www.synbiobeta.com/read/profluent-secures-35m-funding-led-by-spark-capital-to-advance-ai-first-protein-design", "https://www.businesswire.com/news/home/20251119356889/en/Profluent-Raises-$106M-to-Scale-Frontier-AI-Models-for-Programmable-Biology",
    "AI protein design; Spark led the $35M Series A (2024); $106M round co-led by Altimeter and Bezos Expeditions (Nov 2025), ~$150M raised, valuation undisclosed — below $1B", conf="medium")
J["ridwell"] = mo("ridwell", "Growth", 2025, "https://pitchbook.com/profiles/company/267836-95", "https://pitchbook.com/profiles/company/267836-95",
    "recycling pickup service (Seattle); Spark invested in the $15M Series C (Dec 2025); valuation undisclosed — below $1B", conf="medium")
J["sonera"] = mo("sonera", "Seed", 2023, "https://www.businesswire.com/news/home/20230912431509/en/Sonera-Introduces-Breakthrough-Sensing-Technology-to-Make-Neural-Data-More-Accessible", "https://www.businesswire.com/news/home/20230912431509/en/Sonera-Introduces-Breakthrough-Sensing-Technology-to-Make-Neural-Data-More-Accessible",
    "neural sensing chips (Berkeley); $11M seed led by Amplify with Spark (Sep 2023; Nabeel Hyatt quoted) — below $1B", flags=["censored"], extra={"hq_city": "Berkeley", "hq_city_source": "web_verified", "hq_country": "US", "hq_country_source": "web_verified"})
J["sourgum"] = mo("sourgum", "Series A", 2025, "https://www.sourgum.com/the-sour-scoop/sourgum-raises-series-a/", "https://www.sourgum.com/the-sour-scoop/sourgum-raises-series-a/",
    "waste-services marketplace; Spark led the $12.5M Series A (Apr 2025) — below $1B", flags=["city_unknown"])
J["midas"] = mo("midas", "Seed", 2022, "https://www.prnewswire.com/news-releases/meet-midas-turkeys-first-retail-investing-startup-which-has-raised-11m-spark-capital-earlybird-digital-east-and-nigel-morris-301476124.html", "https://www.prnewswire.com/news-releases/midas-secures-80-million-series-b-marking-turkeys-largest-ever-fintech-investment-302533516.html",
    "Turkish retail investing app (Istanbul); Spark and Earlybird led the $11M seed (Feb 2022); $45M Series A (Apr 2024) and $80M Series B (Aug 2025), valuation undisclosed — below $1B", clear=["cohort_unverified"],
    extra={"seed_to_a_graduation": True, "seed_to_a_graduation_source": "web_verified", "seed_to_a_graduation_confidence": "high", "graduation_citation": "https://fintech.global/2024/04/22/midas-secures-record-45m-in-series-a-funding-to-enhance-fintech-offerings-in-turkey/", "hq_city": "Istanbul", "hq_city_source": "web_verified", "hq_country": "TR", "hq_country_source": "web_verified"})
if __name__ == "__main__": print(len(J))
