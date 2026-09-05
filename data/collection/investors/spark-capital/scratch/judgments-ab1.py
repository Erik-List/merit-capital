"""A/B pass, part 1: public market caps (companiesmarketcap.com / stockanalysis.com, as of 2026-09-04) and the first private pins (Wikipedia)."""
WHO = "agent-judge-pro85"
CMC = "https://companiesmarketcap.com/{}/marketcap/"
SA = "https://stockanalysis.com/stocks/{}/market-cap/"
def pub(slug, usd, url, note, rng, extra=None):
    r = {"slug": slug, "who": WHO, "status": "public", "is_public": True, "valuation_usd": usd, "valuation_asof": "2026-09-04",
         "valuation_source": "web_verified", "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_citation": url,
         "valuation_confidence": "high", "clear_flags": ["needs_web_value", "cite_pending"], "flags": [], "note": note}
    if extra: r.update(extra)
    return r
def priv(slug, usd, asof, url, note, rng, flags=(), extra=None):
    r = {"slug": slug, "who": WHO, "status": "private", "is_public": False, "valuation_usd": usd, "valuation_asof": asof,
         "valuation_source": "web_verified", "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_citation": url,
         "valuation_confidence": "high", "clear_flags": ["needs_web_value", "stale"], "flags": sorted(set(flags)), "note": note}
    if extra: r.update(extra)
    return r
J = {}
for s, usd, url, note, rng in [
 ("affirm", 24410000000, CMC.format("affirm"), "NASDAQ: AFRM market cap $24.41B as of 2026-09-04", "10b_plus"),
 ("coinbase", 48710000000, CMC.format("coinbase"), "NASDAQ: COIN market cap $48.71B as of 2026-09-04", "10b_plus"),
 ("braze", 3590000000, CMC.format("braze"), "NASDAQ: BRZE market cap $3.59B as of 2026-09-04", "1b_plus"),
 ("flywire", 2250000000, CMC.format("flywire"), "NASDAQ: FLYW market cap $2.25B as of 2026-09-04", "1b_plus"),
 ("marqeta", 1720000000, CMC.format("marqeta"), "NASDAQ: MQ market cap $1.72B as of 2026-09-04", "1b_plus"),
 ("warby-parker", 3000000000, CMC.format("warby-parker"), "NYSE: WRBY market cap $3.00B as of 2026-09-04", "1b_plus"),
 ("wayfair", 13610000000, CMC.format("wayfair"), "NYSE: W market cap $13.61B as of 2026-09-04", "10b_plus"),
 ("snap", 9250000000, CMC.format("snap"), "NYSE: SNAP market cap $9.25B as of 2026-09-04 (aligned with the Lightspeed base's 2026-09-02 cap)", "1b_plus"),
 ("etoro", 2580000000, CMC.format("etoro"), "NASDAQ: ETOR market cap $2.58B as of 2026-09-04", "1b_plus"),
 ("clover-health", 2260000000, CMC.format("clover-health-investments"), "NASDAQ: CLOV market cap $2.26B as of 2026-09-04", "1b_plus"),
 ("wealthfront", 1430000000, SA.format("wlth"), "NASDAQ: WLTH (IPO Dec 2025) market cap $1.43B as of 2026-09-04", "1b_plus"),
 ("teamshares", 454490000, SA.format("tms"), "NASDAQ: TMS (Live Oak Acquisition Corp. V SPAC, June 2026) market cap $454M as of 2026-09-04", "below_1b"),
 ("securitize", 1270000000, SA.format("secz"), "SECZ (Cantor Equity Partners II SPAC, 2026) market cap $1.27B as of 2026-09-04", "1b_plus"),
]:
    J[s] = pub(s, usd, url, note, rng)
J["anthropic"] = priv("anthropic", 965000000000, "2026-05", "https://en.wikipedia.org/wiki/Anthropic", "$965B post-money, Series H (May 2026; Series G $380B in Feb 2026) — Wikipedia", "100b_plus")
J["discord"] = priv("discord", 15000000000, "2021-09", "https://en.wikipedia.org/wiki/Discord", "$15B (Sept 2021, $500M round) is the last primary mark; confidential IPO filing reported Jan 2026, still private — stale by the 24-month rule", "10b_plus", flags=["stale"])
J["discord"]["clear_flags"] = ["needs_web_value"]
J["ramp"] = priv("ramp", 44000000000, "2026-06", "https://en.wikipedia.org/wiki/Ramp_(company)", "$44B valuation, $750M round led by ICONIQ Growth, GIC and OTPP (June 2026) — Wikipedia", "10b_plus")
J["scale-ai"] = priv("scale-ai", 14800000000, "2025-06", "https://en.wikipedia.org/wiki/Scale_AI", "Meta's June 2025 purchase of a 49% non-voting stake for $14.8B; the company stays an independent private entity — the unicorn list's $29B reads the implied whole, the cited transaction value is used", "10b_plus")
J["deel"] = priv("deel", 17300000000, "2025-10", "https://en.wikipedia.org/wiki/Deel_(company)", "$17.3B, $300M Series E co-led by Ribbit and a16z (Oct 2025) — Wikipedia", "10b_plus")
J["kalshi"] = priv("kalshi", 22000000000, "2026-05", "https://en.wikipedia.org/wiki/Kalshi", "$22B after a TCV-led round (May 2026) — Wikipedia", "10b_plus")
J["cyera"] = priv("cyera", 12000000000, "2026-06", "https://en.wikipedia.org/wiki/Cyera", "$12B, $600M Series G (June 2026); HQ New York City — Wikipedia", "10b_plus")
J["carta"] = {"slug": "carta", "who": WHO, "status": "private", "valuation_usd": 7400000000, "valuation_asof": "2021-08", "valuation_source": "unicorn_list", "valuation_range": "1b_plus", "valuation_range_source": "web_verified", "valuation_range_citation": "https://en.wikipedia.org/wiki/Carta_(software_company)", "valuation_confidence": "medium", "flags": ["stale"], "note": "last primary $7.4B (Aug 2021); 2024 reports put the valuation under $2B (a ~75% fall from the 2022 peak) — collapse evidence keeps the row in 1b_plus but the mark is stale"}
J["niantic"] = {"slug": "niantic", "who": WHO, "status": "acquired", "is_public": False, "valuation_usd": None, "valuation_asof": None, "valuation_source": None, "valuation_range": "below_1b", "valuation_range_source": "web_verified", "valuation_range_citation": "https://en.wikipedia.org/wiki/Niantic,_Inc.", "valuation_confidence": "high", "clear_flags": ["stale"], "flags": [], "note": "acq.: the games business (Pokémon Go) sold to Scopely for $3.5B, completed May 2025; the geospatial remainder spun out as Niantic Spatial Inc. — the standalone Niantic Spark backed no longer exists (Series B lead 2017)"}
if __name__ == "__main__": print(len(J), "A/B records")
