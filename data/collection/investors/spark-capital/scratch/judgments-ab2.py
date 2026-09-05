WHO = "agent-judge-pro85"
def priv(slug, usd, asof, url, note, rng, flags=(), clear=("needs_web_value","stale")):
    return {"slug": slug, "who": WHO, "status": "private", "is_public": False, "valuation_usd": usd, "valuation_asof": asof, "valuation_source": "web_verified",
            "valuation_range": rng, "valuation_range_source": "web_verified", "valuation_citation": url, "valuation_confidence": "high", "clear_flags": list(clear), "flags": sorted(set(flags)), "note": note}
J = {}
J["plaid"] = priv("plaid", 8000000000, "2026-02", "https://en.wikipedia.org/wiki/Plaid_Inc.", "$8B employee share sale (Feb 2026), up from $6.1B (Apr 2025), below the $13.4B 2021 peak — Wikipedia; aligned with the a16z and Thrive bases' 1b_plus band", "1b_plus")
J["andela"] = {"slug": "andela", "who": WHO, "hq_city": None, "clear_flags": [], "flags": ["stale", "city_unknown"], "note": "$1.5B Series E (Sept 2021) is the last mark — stale; the company has been fully remote since 2020 with no headquarters (hq_city null)"}
J["andela"].pop("hq_city")
J["instabase"] = priv("instabase", 2000000000, "2023-06", "https://en.wikipedia.org/wiki/Instabase", "$2B Series C (June 2023) — Wikipedia; stale beyond 24 months", "1b_plus", flags=["stale"], clear=("needs_web_value",))
J["getyourguide"] = priv("getyourguide", 2000000000, "2023-05", "https://en.wikipedia.org/wiki/GetYourGuide", "$194M round at a $2B valuation (May 2023) — Wikipedia; stale beyond 24 months", "1b_plus", flags=["stale"], clear=("needs_web_value",))
J["rapyd"] = priv("rapyd", 15000000000, "2022-07", "https://en.wikipedia.org/wiki/Rapyd", "$15B (July 2022) — Wikipedia; no later primary mark (PayU acquisition Mar 2025) — stale", "10b_plus", flags=["stale"], clear=("needs_web_value","cite_pending"))
if __name__ == "__main__": print(len(J))
