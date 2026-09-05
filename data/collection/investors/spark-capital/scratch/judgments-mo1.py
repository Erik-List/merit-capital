WHO = "agent-judge-pro85"
def mo(slug, stage, year, stage_url, band_url, note, rng="below_1b", usd=None, asof=None, flags=(), clear=(), status=None, conf="high", extra=None):
    r = {"slug": slug, "who": WHO, "entry_stage": stage, "entry_year": year, "entry_stage_source": "web_verified", "entry_stage_citation": stage_url, "entry_stage_confidence": conf,
         "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_range_citation": band_url, "valuation_confidence": conf, "clear_flags": sorted(set(clear) | {"stage_uncited", "web_check", "needs_web_value"}), "flags": sorted(set(flags)), "note": note}
    if usd: r.update({"valuation_usd": usd, "valuation_asof": asof, "valuation_source": "web_verified", "valuation_citation": band_url})
    if status: r["status"] = status
    if extra: r.update(extra)
    return r
J = {}
J["9fin"] = mo("9fin", "Growth", 2024, "https://www.fintechfutures.com/venture-capital-funding/9fin-bags-50m-in-series-b-funding-round-led-by-highland-europe", "https://www.9fin.com/insights/9fin-raises-170m-to-lead-ai-transformation-of-debt-markets",
    "debt-markets data; Spark first invested in the $50M Series B led by Highland Europe (Dec 2024); $170M Series C at $1.3B (Mar 2026) — momentum check moved the band up", rng="1b_plus", usd=1300000000, asof="2026-03")
J["autogenai"] = mo("autogenai", "Growth", 2023, "https://venturebeat.com/ai/automated-proposal-writing-startup-autogenai-raises-39-5m-from-salesforce-ventures-and-others", "https://venturebeat.com/ai/automated-proposal-writing-startup-autogenai-raises-39-5m-from-salesforce-ventures-and-others",
    "AI proposal writing (London); Spark co-led the $39.5M Series B with Salesforce Ventures (Oct 2023); valuation undisclosed, ~$70M raised — below $1B")
J["boosted-ai"] = mo("boosted-ai", "Growth", 2022, "https://www.boosted.ai/resources/boosted-ai-raises-35-million-in-series-b-funding", "https://www.businesswire.com/news/home/20241120214172/en/Boosted.ai-Raises-$15-Million-to-Transform-Investment-Management-with-Agentic-and-Generative-AI",
    "AI for investment managers (Toronto); Spark co-led the $35M Series B with Ten Coves (Jan 2022) and followed on in the $15M round (Nov 2024); $61M raised, valuation undisclosed — below $1B")
J["cimulate"] = mo("cimulate", "Series A", 2024, "https://cimulate.ai/press/cimulate-raises-28-million-in-series-a-funding-led-by-spark-capital-to-transform-commerce-with-ai-powered-customergpt/", "https://cimulate.ai/press/cimulate-raises-28-million-in-series-a-funding-led-by-spark-capital-to-transform-commerce-with-ai-powered-customergpt/",
    "AI commerce search (Boston); Spark led the $28M Series A (Dec 2024); valuation undisclosed — below $1B")
J["civilgrid"] = mo("civilgrid", "Series A", 2026, "https://www.businesswire.com/news/home/20260827753660/en/CivilGrid-Raises-$26M-Series-A-Financing-To-Drive-U.S.-Critical-Infrastructure-Modernization", "https://www.businesswire.com/news/home/20260827753660/en/CivilGrid-Raises-$26M-Series-A-Financing-To-Drive-U.S.-Critical-Infrastructure-Modernization",
    "underground-infrastructure data platform; Spark led the $26M Series A (Aug 2026); valuation undisclosed — below $1B")
J["comulate"] = mo("comulate", "Series A", 2024, "https://medium.com/spark-capital/welcome-comulate-246f95ccfff8", "https://www.lifeinsuranceinternational.com/news/comulate-20m-series-b-funding/",
    "insurance revenue automation; Spark's own 'Welcome, Comulate!' post (Natalie Sandman) marks the 2024 entry; $20M Series B led by BOND and Workday Ventures with Spark (Feb 2025), valuation not disclosed — below $1B")
J["convex"] = mo("convex", "Growth", 2026, "https://www.prnewswire.com/news-releases/convex-raises-57m-series-b-led-by-insight-partners-to-scale-the-reliable-backend-for-the-ai-era-302841686.html", "https://www.prnewswire.com/news-releases/convex-raises-57m-series-b-led-by-insight-partners-to-scale-the-reliable-backend-for-the-ai-era-302841686.html",
    "reactive backend platform; Spark joined the $57M Series B led by Insight (Aug 2026), first listed 2026; no valuation disclosed, $110.5M raised — below $1B")
J["dataplor"] = mo("dataplor", "Series A", 2024, "https://www.businesswire.com/news/home/20240418167357/en/dataplor-Announces-Series-A-Funding-Led-by-Spark-Capital-to-Expand-Global-Location-Data-Intelligence", "https://www.businesswire.com/news/home/20250603685452/en/dataplor-Raises-$20.5M-Series-B-to-Scale-Global-Location-Intelligence-and-Accelerate-Product-Growth",
    "location data intelligence; Spark led the $10.6M Series A (Apr 2024) and followed on in the $20.5M Series B led by F-Prime (Jun 2025); valuation undisclosed — below $1B")
J["durable"] = mo("durable", "Series A", 2023, "https://techcrunch.com/2023/12/12/durable-cements-14m-to-build-ai-powered-tools-for-small-businesses-in-service-industries/", "https://techcrunch.com/2023/12/12/durable-cements-14m-to-build-ai-powered-tools-for-small-businesses-in-service-industries/",
    "AI website builder for small businesses (Vancouver); Spark led the $14M Series A (Dec 2023); ~$20M raised, valuation undisclosed — below $1B", extra={"hq_city": "Vancouver", "hq_city_source": "web_verified", "hq_country": "CA", "hq_country_source": "web_verified"})
J["enfabrica"] = mo("enfabrica", "Growth", 2024, "https://news.crunchbase.com/semiconductors-and-5g/enfabrica-ai-networking-chips-startup-funding-nvda-arm/", "https://pitchbook.com/profiles/company/465827-59",
    "AI networking silicon (Mountain View); Spark led the $115M Series C (Nov 2024); PitchBook post-money $445-560M — below $1B", usd=560000000, asof="2024-11", conf="medium")
J["garden"] = mo("garden", "Seed", 2025, "https://www.crunchbase.com/funding_round/garden-01d0-seed--52801eb5", "https://www.crunchbase.com/funding_round/garden-01d0-seed--52801eb5",
    "AI for patent drafting and infringement analysis (New York); $6.8M seed with Spark (2025) — below $1B, too young for the graduation test", conf="medium", flags=["censored"])
if __name__ == "__main__": print(len(J))
