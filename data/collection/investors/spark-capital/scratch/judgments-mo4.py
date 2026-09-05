WHO = "agent-judge-pro85"
def mo(slug, stage, year, stage_url, band_url, note, rng="below_1b", usd=None, asof=None, flags=(), clear=(), status=None, conf="high", extra=None, stage_src="web_verified"):
    r = {"slug": slug, "who": WHO, "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_range_citation": band_url, "valuation_confidence": conf,
         "clear_flags": sorted(set(clear) | {"stage_uncited", "web_check", "needs_web_value"}), "flags": sorted(set(flags)), "note": note}
    if stage: r.update({"entry_stage": stage, "entry_year": year, "entry_stage_source": stage_src, "entry_stage_confidence": conf})
    if stage and stage_url: r["entry_stage_citation"] = stage_url
    if usd: r.update({"valuation_usd": usd, "valuation_asof": asof, "valuation_source": "web_verified", "valuation_citation": band_url})
    if status: r.update({"status": status, "status_source": "web_verified", "status_citation": band_url})
    if extra: r.update(extra)
    return r
J = {}
J["clyde"] = mo("clyde", None, None, None, "https://tracxn.com/d/companies/clyde/__OcIm3Eg5JRWRIXa-Uogg_We9qFkIzTvIiBWMdS4b4AU",
    "product-protection platform (New York); acq.: acquired by Cover Genius (Mar 2023), itself a Spark portfolio company — the standalone valuation no longer applies", status="acquired", flags=["stage_disputes_band"], clear=["stage_uncited"])
J["cosuno"] = mo("cosuno", "Series A", 2021, "https://nordic9.com/news/cosuno-in-a-125-million-round-led-by-spark-capital/", "https://tech.eu/2022/02/09/cosuno-brings-in-30-million-to-digitise-construction-industry/",
    "construction procurement software (Berlin); Spark led the €12.5M Series A (2021); $30M Series B led by Avenir at a $150M valuation (Feb 2022) — below $1B", usd=150000000, asof="2022-02", extra={"hq_city": "Berlin", "hq_city_source": "web_verified", "hq_country": "DE", "hq_country_source": "web_verified"})
J["kateeva"] = mo("kateeva", None, None, None, "https://pitchbook.com/profiles/company/52783-75",
    "OLED inkjet manufacturing equipment; still private with $341M raised and no priced mark in the record — below $1B (2009 Series A entry stands on the site's stage class)", status="private", conf="medium")
J["parallel"] = mo("parallel", None, None, None, "https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/",
    "web APIs for AI agents (Parag Agrawal); $100M Series A at $740M co-led by Kleiner Perkins and Index (Nov 2025), $100M Series B at $2B led by Sequoia (Apr 2026) — the momentum check moved the band up; Spark's entry round to be cited", rng="1b_plus", usd=2000000000, asof="2026-04", flags=["cite_pending", "model_disputes_source"])
J["perch"] = mo("perch", "Series A", 2020, "https://news.fintech.io/post/102g4k0/spark-capital-leads-raise-as-perch-creates-new-model-of-consumer-products-company", "https://www.bloomberg.com/news/articles/2024-03-04/arnault-backed-razor-buys-perch-in-amazon-aggregator-shakeout",
    "Amazon brand aggregator; Spark led the $8M Series A (Apr 2020) before the SoftBank-led $775M round at ~$1B (May 2021); acq.: acquired by Razor Group in an all-stock deal (Mar 2024, combined entity ~$1.7B), Perch+ later divested to Levanta (Apr 2026)", status="acquired")
J["remarkable"] = mo("remarkable", "Series A", 2019, "https://techcrunch.com/2019/10/08/with-15m-round-and-100k-tablets-sold-remarkable-ceo-wants-to-make-tech-more-human", "https://techcrunch.com/2022/05/10/remarkable-maker-of-a-focus-friendly-e-paper-tablet-says-it-closed-funding-at-a-1b-valuation-after-selling-1m-devices",
    "paper tablet maker (Oslo); Spark led the $15M Series A (Oct 2019); $1B valuation at the TCV-led $45M round and secondary (May 2022) — last priced mark, stale", rng="1b_plus", usd=1000000000, asof="2022-05", flags=["stale"], conf="medium", extra={"status": "private"})
J["zeller"] = mo("zeller", "Series A", 2021, "https://www.fintechfutures.com/venture-capital-funding/australian-fintech-zeller-lands-73m-series-b-funding", "https://www.fintechfutures.com/venture-capital-funding/australian-fintech-zeller-lands-73m-series-b-funding",
    "Australian business payments (Melbourne); Spark is an existing investor from the 2021 Series A; AUD 100M Series B led by Headline at AUD 1B ≈ US$730M (Mar 2025) — below $1B", usd=730000000, asof="2025-03", conf="medium", extra={"hq_city": "Melbourne", "hq_city_source": "web_verified", "hq_country": "AU", "hq_country_source": "web_verified"})
J["relay"] = mo("relay", "Growth", 2021, "https://www.relaypayments.com/newsroom/43-million-investment-in-transportation-transformation", "https://pitchbook.com/profiles/company/437651-02",
    "trucking payments network (Atlanta); Spark led the $43M Series B (2021); $50M Series C with General Catalyst (May 2026), ~$100M 2025 revenue, valuation undisclosed — below $1B", conf="medium", flags=["model_disputes_source"])
J["producer"] = mo("producer", None, None, None, "https://www.billboard.com/pro/google-acquires-producerai-ai-music-startup/",
    "generative-music platform (formerly Riffusion, $4M seed 2023); acq.: acquired by Google for Google Labs (Feb 2026) shortly after Spark listed it", status="acquired", flags=["city_unknown", "country_prior"], conf="medium")
if __name__ == "__main__": print(len(J))
