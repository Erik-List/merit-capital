import importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put(row("1stdibs", "public", "New York", "US", "Growth", "model", "Consumer & Marketplaces", public=True, stage_conf="medium",
        note="NASDAQ: DIBS since June 2021 (market cap a few hundred $M, below $1B); Spark led the 2012/2013 $15M round (Series B/C, Todd Dagres board seat) — the 2019 filing is a later round"))
put(row("5min-media", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="high",
        note="acq. by AOL, 2010; $5M Series A from Spark Nov 2007 (TechCrunch); founded in Israel, HQ New York by 2010"))
put(row("8d-world", "defunct", "Woburn", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="Wiz World Online English-learning game; listed from 2008, the 2010 $5.25M filing is a follow-on ('$5.25M more'), entry was the 2008 round; shut down ~2012"))
put(row("9fin", "private", "London", "GB", "Series A", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited"],
        note="leveraged-finance data platform; Spark led the 2022 Series A extension (~$23M), listed from 2023; later rounds below $1B"))
put(row("academia-edu", "private", "San Francisco", "US", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite=TC+"2011/11/30/academia-edu-raises-4-5-million-to-help-researchers-share-their-scholarly-papers/", stage_conf="high",
        note="$4.5M Series A led by Spark, Nov 2011"))
put(row("accelera-mobile-broadband-inc", "unknown", "Santa Clara", "US", "Growth", "model", "Data Infrastructure", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="small-cell / mobile broadband networks; Spark's seat first on the 2014 $14M round (Series B) after a 2012 $7M round without the firm; company dark since ~2016"))
put(row("ada", "private", "Toronto", "CA", "Growth", "model", "AI & Applied AI", stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=1200000000, asof="2021-05", val_src="unicorn_list", val_conf="medium",
        note="Spark led the $130M Series C at $1.2B, May 2021 (Growth entry); $1B+ mark to be web-pinned in the A/B pass"))
put(row("adap-tv", "acquired", "San Mateo", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["stage_disputes_band", "model_disputes_source"],
        extra={"seed_to_a_graduation": None}, note="acq. by AOL, Aug 2013 ($405M) — the site card's 'Acquired by AOL in 2010' is wrong (that is 5min); Spark in the 2007 $10M Series A (Politi board), the 2010-2011 filings are follow-ons"))
put(row("adept", "acquired", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="medium",
        note="Series B $350M co-led by General Catalyst and Spark Capital, Mar 2023; June 2024 licensing deal with Amazon took the founders and team (acqui-hire), the company wound down its independent business"))
put(row("admeld", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="high",
        note="acq. by Google, 2011 (~$400M); $7M Series A June 2008 with Spark and Foundry (golden key)"))
put(row("affirm", "public", "San Francisco", "US", "Growth", "web_verified", "Fintech & Payments", public=True, stage_cite=TC+"2015/05/06/max-levchins-lending-startup-affirm-raises-275m-in-equity-and-debt", stage_conf="high",
        rng="10b_plus", usd=20800000000, val_src="sec_public_float", note="NASDAQ: AFRM (IPO Jan 2021); Spark Capital Growth led the $275M Series B, May 2015"))
put(row("airspace-intelligence", "private", "Seattle", "US", "Series A", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="AI flight-operations software; Spark led the ~$20M Series A (2021), listed from 2022"))
put(row("allstripes", "acquired", "San Francisco", "US", "Series A", "model", "Healthcare & Bio", stage_conf="medium",
        note="RDMD renamed AllStripes; Spark led the $9.5M Series A (Jan 2020, Hyatt board); acq. by PicnicHealth, Dec 2022"))
put(row("alpaca", "private", "San Mateo", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium",
        note="brokerage API; Spark joined the $50M Series B (Nov 2021, Tribe Capital led); below $1B"))
put(row("anthropic", "private", "San Francisco", "US", "Growth", "web_verified", "AI & Applied AI", stage_cite="https://www.anthropic.com/news/anthropic-series-c", stage_conf="high",
        rng="100b_plus", usd=965000000000, asof="2026-05", val_src="unicorn_list", val_conf="medium", note="Spark led the $450M Series C, May 2023 (Razavi board); $965B Series H mark (May 2026) per the unicorn list, web-pinned in the A/B pass"))
put(row("aura-frames", "private", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="Pushd, Inc.; digital picture frames; Spark's seat on the 2017 $5.5M round after the 2016 $6M Series A — entry Series A 2016/2017, the band's 'Seed' reads a small later round"))
put(row("autogenai", "private", "London", "GB", "Growth", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="bid-writing language engines; Spark led the $39.5M Series B (2024), listed from 2025"))
put(row("aviary", "acquired", "New York", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite="https://www.finsmes.com/2009/10/aviary-raises-7m-series-b-financing.html", stage_conf="high",
        note="acq. by Adobe, Sept 2014; Spark led the $7M Series B, Oct 2009 (Koyfman board) — entry at the B"))
put(row("axis-security", "acquired", "San Mateo", "US", "Growth", "model", "Security", stage_conf="medium",
        note="acq. by HPE, 2023 (~$500M); Spark led the $100M Series C, Mar 2021"))
put(row("badi", "unknown", "Barcelona", "ES", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="room-rental marketplace; Spark led the $10M Series A (Jan 2018) and the $30M Series B (2019); operations wound down ~2023, no announcement found — status unknown"))
put(row("baseten", "private", "San Francisco", "US", "Growth", "model", "Data Infrastructure", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="ML inference infrastructure; Spark's first position is the 2026 round (Will Reed board, Form D 2026); valued well above $1B — figure pinned in the A/B pass"))
put(row("beam", "unknown", "Paris", "FR", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited", "model_disputes_source"], country_src="model_knowledge",
        note="beamapp.co, the browser/notes app by Dom Leca (Sparrow founder), listed 2021-2025; Wikidata's 'acquired' and 'US' belong to a homonym; the product was discontinued (2023) without a documented acquisition — status unknown; seed 2021 with Spark"))
put(row("behalf", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium",
        note="SMB purchase financing (New York / Israel); Spark joined the 2015 round (Series C equity within the $119M debt-and-equity raise); below $1B"))
put(row("benchling", "private", "San Francisco", "US", "Growth", "model", "Healthcare & Bio", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="R&D cloud for biotech; Spark entered at a late round (2019-2020 Series C/D); $6.1B mark (Series F, Nov 2021) to be pinned"))
put(row("benu", "private", "Billerica", "US", "Series A", "model", "Data Infrastructure", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="Benu Networks (fixed/mobile broadband edge software); Spark's first seat on the 2013 $5M round = Series A (the band's 'Seed' is the size band, not the round); still operating"))
put(row("bloomnation", "private", "Santa Monica", "US", "Seed", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/BloomNation", stage_conf="high",
        grad=True, grad_src="web_verified", grad_conf="high", note="Spark in the $1.65M seed (2013, a16z led) and the $5.55M Series A (Oct 2014) — graduated"))
put({"slug": "bond-street", "who": jl.WHO, "valuation_range": "below_1b", "valuation_usd": None, "valuation_confidence": "high", "flags": [], "note": "acq. by Goldman Sachs (team and technology), 2017; David Haber's founder seat — member via the 2015-2017 site listing (decisions.md D8)"})
put(row("boosted-ai", "private", "Toronto", "CA", "Growth", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="LLM tools for investment managers; listed from 2025 — Spark's entry round unnamed (Growth by the company's 2024-2025 stage); below $1B"))
put(row("boxee", "acquired", "New York", "US", "Series A", "web_verified", "Media, Gaming & Advertising", stage_cite=TC+"2008/11/18/boxee-raises-4-million-for-socially-networked-content-aggregator/", stage_conf="high", flags=["stage_disputes_band"],
        extra={"seed_to_a_graduation": None}, note="acq. by Samsung, 2013; $4M first round Nov 2008 split Spark/USV (Series A per the record; the band's 'Seed' reads the size)"))
put(row("braze", "public", "New York", "US", "Growth", "model", "SaaS", public=True, stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=2700000000, val_src="sec_public_float",
        note="NASDAQ: BRZE (IPO Nov 2021); Spark Capital Growth joined the $80M Series E (Oct 2018, Meritech led) — Growth entry, citation in the A/B pass"))
put(row("brud", "acquired", "Los Angeles", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="virtual-influencer studio (Lil Miquela); Spark led the ~$20M Series A (early 2019, Thau board); acq. by Dapper Labs, Oct 2021"))
put(row("bug-labs", "unknown", "New York", "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="modular open-source hardware (BUG), later IoT tools (dweet.io); Spark and USV in the 2007 first round, the 2010 $5M is a follow-on; company dark since ~2016"))
put(row("cameo", "private", "Chicago", "US", "Growth", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["model_disputes_source"],
        note="Wikidata's IT is a homonym — Cameo is Chicago-based; Spark joined the $50M Series B (June 2019, Kleiner led); the 2021 $1B mark collapsed (2023 down round at ~$100M) — below_1b on collapse evidence"))
put(row("capella-space", "acquired", "San Francisco", "US", "Series A", "model", "Industrial & Robotics", stage_conf="medium",
        note="SAR satellites; Spark led the $12M Series A (2017, Hyatt board); acq. by IonQ, 2025 (the IonQ 424B7 lists the Spark funds as selling stockholders)"))
put(row("capitolis", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="capital-markets technology; Spark led the $40M Series B (Nov 2019); $1.6B mark (Series D, Mar 2022) to be pinned"))
put(row("careship", "unknown", "Berlin", "DE", "Series A", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited"],
        note="home-care marketplace; Spark led the Series A (2017); operations ceased ~2022 without a documented exit — status unknown"))
put(row("catalyst", "acquired", "New York", "US", "Growth", "model", "SaaS", stage_conf="medium", flags=["stage_disputes_band"],
        note="customer-success software; Spark led the $25M Series B (Sept 2020), the 2022 filing is the Series C — Growth entry (the band's 'Series A' reads the 2022 size); merged into Totango, Feb 2024"))
put(row("chainguard", "private", "Kirkland", "US", "Growth", "web_verified", "Security", stage_cite="https://www.prnewswire.com/news-releases/chainguard-raises-61-million-series-b-round-as-enterprises-move-to-fortify-open-source-software-301973663.html", stage_conf="high", flags=["needs_web_value"], rng=None,
        note="Spark led the $61M Series B, Nov 2023; $3.5B mark (2025) to be pinned"))
put(row("chronosphere", "private", "New York", "US", "Growth", "model", "Data Infrastructure", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="observability; Spark joined a late round (2022-2023), listed from 2023; $1.6B mark (Jan 2022) to be pinned"))
put(row("cimulate", "private", "Boston", "US", "Series A", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="generative AI for e-commerce (MIT spin-out); Spark-led 2025 round, listed from 2025"))
put(row("civilgrid", "private", "San Francisco", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="infrastructure-permitting data; listed from 2026, Spark-led 2026 round"))
put(row("clarify", "private", "San Francisco", "US", "Growth", "model", "Healthcare & Bio", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="Clarify Health Solutions; Spark Growth in the $150M Series D (Apr 2022, Will Reed board); $1.4B mark to be pinned"))
put(row("clora", "private", "Boston", "US", "Seed", "model", "Healthcare & Bio", stage_conf="low", flags=["stage_uncited"],
        note="life-science expert marketplace; Spark-led seed (2018); graduation undetermined"))
put(row("clover-health", "public", "Franklin", "US", "Growth", "model", "Healthcare & Bio", public=True, stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="NASDAQ: CLOV (SPAC, Jan 2021); Spark Growth in the $160M Series C (2016); market cap to be pinned in the A/B pass"))
put(row("clyde", "acquired", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium", flags=["stage_disputes_band", "web_check"],
        note="product-protection platform; Spark led the $25M Series B (Nov 2021, Finkelstein board) — Growth entry; acquired by Cover Genius (2024), to be confirmed in the momentum web check"))
if __name__ == "__main__": print(len(J), "judgments")
