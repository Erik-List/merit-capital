"""PRO-162 grind, batches 012-014 (one file, recorded as batch-012). Evidence as in judgments-1.py, plus Google News
(nq.py, NQ_TAG=b12, news-extra-b12.json), Wikipedia (wikifetch.py) and WebSearch on 2026-09-27 (VMLogix, WebPutty,
Work 'N Gear). Rows not classified here because they merge at the rebuild (identity-merges.json):
factor-systems-inc and btrs-holdings-inc (billtrust), thorley-industries-llc (4moms), cellular-longevity-inc (loyal),
material-technologies-corp (material-bank), shop-my-shelf-inc (shopmy), m-c-acquisition-corp (m-c-communications),
scryer-inc (reonomy-altus-group), groupay-inc (gocardless) and zenreach (adentro). seed-cx folds into zero-hash, so the
zero-hash line carries the Seed CX history."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


# ---- batch 012
L.append(cls("viso-trust-protecht", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="San Francisco", focus="Security", stage="undetermined", entry_date="2021",
    note="AI-driven third-party security risk management (San Francisco). BCV's listing: 2021, Early (Rak Garg, Enrique Salem); "
         "Bain Capital Ventures was an existing investor when the company raised $7M in November 2024, $24M in total ("
         + NEWS("viso-trust-protecht", "Secures $7M to Accelerate") + "). Protecht acquired it in April 2026 ("
         + NEWS("viso-trust-protecht", "Protecht Acquires Leading") + "). The 2021 round is not named, and the Early tag "
         "never mints a stage (decisions.md R2)."))
L.append(cls("vmlogix", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Santa Clara",
    focus="DevTools & APIs", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.infoworld.com/article/2298149/vmlogix-receives-funding-from-bain-capital-ventures.html",
    entry_date="2006-10",
    note="Virtual lab management for development and test (Santa Clara, per the firm's archived listing). 'VMLogix Receives Funding "
         "from Bain Capital Ventures' (InfoWorld, 2006-10): a $3.5M Series A from BCV (Ajay Agarwal). 'VMLogix was acquired by "
         "Citrix Systems in August 2010' (the firm's archived page)."))
L.append(cls("webputty", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Jose",
    focus="DevTools & APIs", stage="undetermined", entry_date="2003",
    note="E-business applications and internet frameworks (San Jose). The firm listed it from its 2003 page, "
         "'Early', and as acquired by 2006; no source read names the acquirer. BCV held it by 2003; the round is not named."))
L.append(cls("whop", status="private", rng="1b_plus", usd=1600000000, val_src="web_verified", asof="2026-02-25",
    val_cite=NEWS("whop", "Tether Investment Values Whop"), extra={"valuation_range_source": "web_verified"},
    city="New York", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Whop.com"), entry_date="2024-06",
    note="Marketplace and tools for digital creators (Brooklyn, New York). 'In June 2024, Whop raised US$50 million in a Series B "
         "round led by Bain Capital Ventures at a valuation of US$800 million' (Wikipedia); a Series B entry reads Growth, "
         "matching the listing's Growth tag (Merritt Hummer). Mark: Tether's $200M investment at $1.6B (February 2026), aligned "
         "with Insight."))
L.append(cls("wisetack", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Fintech & Payments", stage="undetermined",
    note="Point-of-sale consumer financing for service businesses (San Francisco). Greylock led the 2019 seed and Series A; "
         "'Existing backers Greylock Partners and Bain Capital Ventures also participated' in the $45M Series B Insight led "
         "(TechCrunch, 2021-09-09, " + NEWS("wisetack", "Wisetack closes on $45M") + "), so BCV entered before September "
         "2021 in a round no source names (the firm's 2022 archive: Matt Harris). Momentum check (fintech): no priced round at "
         "$1B or more since the 2021 Series B; the 2025 Group 1001 deal is a lending capital partnership. Aligned with Greylock "
         "and Insight."))
L.append(cls("wonder", status="private", rng="1b_plus", usd=9000000000, val_src="web_verified", asof="2026-07-16",
    val_cite=NEWS("wonder", "Wonder tops $9B valuation"), extra={"valuation_range_source": "web_verified"},
    city="New York", focus="Consumer & Marketplaces", stage="undetermined", entry_date="2020",
    note="Marc Lore's food delivery and fast-casual food hall company (New York). BCV's listing: 2020, Early (Scott Friend); the "
         "2020 round is not named. Mark: the $650M round of July 2026 at a $9B pre-money valuation (Restaurant Dive, 2026-07-16). "
         "Sibling Accel (same company, Sameer Gandhi) reads below_1b with no mark; this cited round is fresher evidence. The "
         "EQT Ventures (wonder.me, Berlin) and First Round (research service) rows named Wonder are different companies."))
L.append(cls("work-n-gear", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Weymouth",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="Work apparel and footwear retail chain (Weymouth, MA in the firm's 2006-2013 listings, 'Expansion/Growth Buyout'). Its "
         "CEO bought it out of bankruptcy in 2002 and raised about $40M from venture investors (Wikipedia, Anthony DiPaolo); no "
         "source read gives BCV's round or stake, so the listing bucket stays context. It filed for Chapter 11 in July 2025, "
         "moved to liquidate and closed its stores in February 2026 (" + NEWS("work-n-gear", "closes in West Springfield")
         + "); a family office-backed operator bought its assets in April 2026 (" + NEWS("work-n-gear", "Assets Acquired")
         + "): an asset sale out of a wind-down reads acquired (COLLECTION.md s6)."))
L.append(cls("zenlytic", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Data Infrastructure", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("zenlytic", "Zenlytic Raises $4.4M"), entry_date="2021",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("zenlytic", "Raises $9 Million (Series A)"),
    note="Self-serve business intelligence for commerce brands (New York). BCV led the $4.4M seed (AlleyWatch, announced "
         "2022-12-20; the firm's listing: 2021, Seed, Scott Friend), after a $1M pre-seed Primary led in 2021 without BCV. M13 "
         "led the $9M Series A with BCV participating (Pulse 2.0, 2024-10-01).",
    rounds=[rnd("2024-09", "Series A", 9000000, "M13", True, NEWS("zenlytic", "Raises $9 Million (Series A)"), "press")]))
L.append(cls("zero-hash", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", asof="2025-09-23",
    val_cite=NEWS("zero-hash", "Leads $104M Zerohash Round"), extra={"valuation_range_source": "web_verified"},
    country="US", country_src="model_knowledge", city="Chicago", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("zero-hash", "Bain Capital Invests $15 Million"),
    entry_date="2018-09",
    note="Crypto and stablecoin settlement infrastructure (Chicago), formerly the Seed CX exchange (the 2022 archive renders Zero Hash "
         "at /portfolio/seed-cx; the seed-cx row folds in here). BCV led Seed CX's $15M Series B in September 2018 (CryptoSlate; the "
         "firm's 2018 listing, Salil Deshpande); a Series B entry reads Growth. Renamed Zero Hash with a Series C in 2020; 'Bain "
         "Capital' joined the $105M Series D of January 2022. Mark: the $104M Series D-2 Interactive Brokers led in September 2025 "
         "at $1B (CoinDesk). Mastercard's reported $2B takeover talks ended without a deal in January 2026 ("
         + NEWS("zero-hash", "Zerohash walked away") + "), so private."))

if __name__ == "__main__":
    jl.write("batch-012", L)
