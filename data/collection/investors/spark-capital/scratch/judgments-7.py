import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
def nm(slug, basis, ec="formd_adjudicated", conf="high", cite=None): J["verdict:" + slug] = verdict(slug, "not_member", basis, ec, conf, cite)
def mem(slug, basis, ec="formd_adjudicated", conf="medium", cite=None): J["verdict:" + slug] = verdict(slug, "member", basis, ec, conf, cite)
put(row("kalshi", "private", "New York", "US", "Growth", "web_verified", "Fintech & Payments", stage_cite="https://news.kalshi.com/p/kalshi-hits-5-billion-valuation-amid-international-expansion", stage_conf="medium", rng="10b_plus", usd=22000000000, asof="2026-03", val_src="unicorn_list", val_conf="medium",
        note="prediction-market exchange; Spark joined the $300M Series D (Oct 2025) — Growth; $22B mark (Mar 2026) per the unicorn list, re-pinned in the A/B pass"))
nm("kit-digital", "KIT digital (NASDAQ: KITD) appears on the 2012 listing as the successor of KickApps, which it acquired in January 2011 — Spark's KIT digital shares are sale consideration for the KickApps position (decisions.md D7, ruling 14); the investment row is KickApps.", "site_listing", "high")
put(row("kitchensurfing", "defunct", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited"],
        note="private-chef marketplace; Spark led the 2013 Series A, the $15M Series B (2014, firm news) followed; shut down 2016"))
put(row("kumu", "unknown", None, "US", "Seed", "model", "SaaS", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="2015 listing only ('software-services', California); company dark"))
put(row("latent-technology", "private", "London", "GB", "Seed", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="generative animation for games; Spark led the seed (2023); graduation undetermined"))
put(row("lily", "defunct", "Menlo Park", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="Lily camera drone; Spark led the $14M Series A (Dec 2015); shut down Jan 2017 before shipping"))
nm("mandalay-media", "Mandalay Media (NeuMedia / Mandalay Digital, NASDAQ: APPS) acquired Spark-backed Twistbox in February 2008; the 2008-2011 listing shows the acquirer as the successor of the Twistbox position and Spark Management Partners' 13D on Mandalay Media is the sale consideration — not_member under the consideration rule (decisions.md D7, ruling 14); Twistbox stays the member row.", "fund_filing", "high", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000317788&type=SC%2013D&dateb=&owner=include&count=40")
put(row("medallion", "private", "San Francisco", "US", "Series A", "model", "Healthcare & Bio", stage_conf="medium", flags=["model_disputes_source"],
        note="provider credentialing platform; Spark led the $20M Series A (Jan 2021); Wikidata's SE is a homonym; below $1B"))
put(row("mercury", "private", "San Francisco", "US", "Growth", "web_verified", "Fintech & Payments", stage_cite="https://en.wikipedia.org/wiki/Mercury_(company)", stage_conf="high", flags=["needs_web_value", "model_disputes_source"], rng=None,
        note="business banking platform; Spark joined the $300M Series C (Mar 2025, Sequoia led, $3.5B) — the a16z and Sequoia bases carry $5.2B as of May 2026, re-pinned in the A/B pass; Wikidata's 'acquired / JP' is a homonym"))
put(row("n3", "unknown", None, "US", "Series A", "model", None, stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"], focus_src=None,
        note="2007-2008 static-site listing only; company dark, sector unknown"))
put(row("nimble-commerce", "unknown", "San Francisco", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited"],
        note="commerce software (2014-2015 listing); company dark"))
put(row("onswipe", "acquired", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="tablet publishing platform; Spark led the $5M Series A (Aug 2011; firm news 2011 '$1M' seed preceded); acq. by Beanstock Media, 2014"))
put(row("panjo", "unknown", "Los Angeles", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited"],
        note="enthusiast marketplace; Spark seed (2013); dark since 2018"))
put(row("parallel", "private", "Palo Alto", "US", "Series A", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited", "web_check", "model_disputes_source"],
        note="Parallel Web Systems (Parag Agrawal); Spark's position is the 2025 round (live-site listing); the April 2026 $100M Sequoia-led Series B's valuation checked in the momentum slice; Wikidata's AU is a homonym"))
put({"slug": "post", "who": jl.WHO, "status": "unknown", "is_public": False, "valuation_range": "below_1b", "valuation_usd": None, "valuation_asof": None, "valuation_source": None, "valuation_confidence": "high",
     "entry_stage": "Seed", "entry_stage_source": "model", "entry_stage_confidence": "low", "hq_country": "US", "hq_country_source": "model_knowledge", "focus": None, "focus_source": None,
     "flags": ["model_disputes_source", "cik_weak", "stage_uncited", "city_unknown", "country_prior"],
     "note": "the 2010-2012 listing 'Post' (Start@Spark era); the SEC float layer matched Post Holdings (NYSE: POST, CIK 1530950) — a name collision, quarantined (duty 8); the startup is dark"})
put(row("sendme", "unknown", "San Francisco", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="mobile content; Spark led the 2007 Series A (listed 2007-2011); company dark"))
put(row("sensr-net", "unknown", None, "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified", "city_unknown", "country_prior"],
        note="camera-monitoring service; Spark seed (2012); dark"))
put(row("sesame", "private", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="voice AI; Spark co-led the $250M Series B (2025) with Sequoia; valuation to be pinned"))
put(row("sidewire", "defunct", "San Francisco", "US", "Seed", "web_verified", "Media, Gaming & Advertising", stage_cite="https://en.wikipedia.org/wiki/Sidewire", stage_conf="high", grad=False, grad_conf="medium", flags=["cohort_unverified"],
        note="political news app; $4.85M seed from Spark (2015); shut down 2017 — no A"))
put(row("standard-intelligence", "private", "San Francisco", "US", "Series A", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="computer-use models; Spark-led 2025 round (live-site listing)"))
put(row("storefront", "acquired", "San Francisco", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="pop-up retail marketplace; Spark led the $7.3M Series A (2014); merged with Oui Open (2016), later acquired"))
put(row("super", "defunct", "San Francisco", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", grad=False, grad_conf="medium", flags=["stage_uncited", "cohort_unverified"],
        note="Biz Stone's Super app; Spark seed (2015); shut down 2017"))
put(row("svpply", "acquired", "New York", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="medium", grad=False, grad_conf="medium", flags=["cohort_unverified"],
        note="social shopping; Spark seed (2010, firm news); acq. by eBay, Sept 2012 — no A"))
put(row("tjet-technologies", "unknown", None, "US", "Series A", "model", None, stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"], focus_src=None,
        note="2008-2012 listing only; company dark, sector unknown"))
put(row("triggit", "acquired", "San Francisco", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="retargeting ad platform; Spark in the 2010 Series A; acq. by Gravity4, 2015"))
put(row("twistbox", "acquired", "Los Angeles", "US", "Growth", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited"],
        note="mobile content (founded 2003); Spark's 2006 round into a three-year-old company; acq. by Mediavest / Mandalay Media, Feb 2008 (the acquirer's listing is consideration, ruling 14)"))
put(row("txteagle", "defunct", "Boston", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["duplicate"],
        note="IDENTITY for the rebuild: txteagle renamed Jana (2011) — merged into the 'jana' row at the rebuild"))
put(row("veoh-networks", "acquired", "San Diego", "US", "Growth", "web_verified", "Media, Gaming & Advertising", stage_cite="https://www.adweek.com/brand-marketing/eisner-time-warner-back-veoh-84899/", stage_conf="high",
        note="online video; Spark in the $12.5M Series B (Apr 2006); Chapter 7 in Feb 2010, assets sold to Qlipso — acquired out of insolvency (Cherry-run convention)"))
put(row("verified-identity-pass", "acquired", "New York", "US", "Growth", "model", "Security", stage_conf="low", flags=["stage_uncited"],
        note="Clear registered-traveler program (Steven Brill); Spark in the 2008 round — a late round into a 2003-founded company; ceased operations June 2009, assets bought by Alclear (2010) — acquired out of insolvency"))
put(row("vurve", "acquired", "Palo Alto", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited", "duplicate"],
        note="IDENTITY for the rebuild: Vurve rebranded Lexity (2011) — merged into the 'lexity' row at the rebuild; acq. by Yahoo, 2013"))
put(row("xoova", "unknown", None, "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="2007-2008 listing only (local search); company dark"))
put(row("zazma", "private", "New York", "US", "Series A", "model", "Fintech & Payments", stage_conf="medium", flags=["duplicate"],
        note="IDENTITY for the rebuild: Zazma renamed Behalf (2014) — merged into the 'behalf' row at the rebuild; the $10M from Sequoia and Spark (firm news 2015, 'comes out of stealth') is Behalf's Series A, listed from 2014"))
put(row("zeromatter", "private", "San Francisco", "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited"],
        note="simulation platform for training AI systems; Spark-led 2025 round (live-site listing)"))
# ---- membership verdicts on the Form D name-match rows of this batch
nm("adaptiveblue-inc", "Fraser Kelton's 2012 director seat at AdaptiveBlue (GetGlue) is his operator job before joining Spark in 2023 (D8 seat dating); no Spark listing, announcement or vehicle.")
mem("alyk-inc", "ALYK, Inc. is LOLA's legal name (the initials of founders Alex Friedman and Jordana Kier): the Form D rounds ($7M Dec 2016, $24M Jan 2018) are LOLA's Spark-led Series A and Series B with Kevin Thau as director, and LOLA is site-listed 2017-2022 — one company, merge queued for the rebuild.", "formd_adjudicated", "high")
nm("atbash-labs-inc", "'Benjamin Simon' as Executive Officer of a Berkeley startup 2022-2025 is not the Spark team member of that name (a 2022 profile only); founder paper, no Spark listing or vehicle.")
nm("banyan-biomarkers-inc", "'Andrew Parker' director 2020 on a San Diego diagnostics company: homonym — Spark's Andrew Parker left in 2019 and the firm never listed Banyan.")
nm("blaze-bioscience-inc", "'Dennis Miller' Executive Officer 2014-2020 (a Seattle biotech CFO): homonym — Spark's Dennis Miller left in 2011 and the firm never listed Blaze.")
nm("boundless-learning-inc", "Rob Go's 2011 director seat is a NextView Ventures seat (he co-founded NextView after leaving Spark in 2010); Boundless was never Spark-listed.")
nm("breakout-global-technologies-inc", "Arpan Shah's 2022-2024 director seat at a Tampa startup predates his 2025 arrival at Spark (D8); no Spark listing or vehicle.")
mem("cloud-tiger-media-inc", "Cloud Tiger Media, Inc. is Upworthy's legal name: the 2013 $12.2M filing with Andrew Parker as director is Upworthy's Spark-led Series A (Sept 2013), and Upworthy is site-listed 2014-2019 — one company, merge queued for the rebuild.", "formd_adjudicated", "high")
nm("conduit-labs-inc", "Nabeel Hyatt's own company (Executive Officer, 2009 Form D) before he joined Spark in 2012 — founder-era paper (D8); acquired by Zynga 2010, never Spark-listed.")
nm("craft-standard-enterprises-inc", "'Benjamin Simon' officer/director of a Fayetteville, Arkansas company 2021-2023: homonym; no Spark listing or vehicle.")
mem("curiouser-products-inc", "Curiouser Products Inc. is Mirror's legal name: the rounds ($3M 2016, $10M 2017, $25M 2018) are Mirror's seed, Spark-led Series A and Series B with Kevin Thau as director, and Mirror is site-listed 2019-2023 — one company, merge queued for the rebuild.", "formd_adjudicated", "high")
nm("extend-inc", "Alex Clayton's 2020-2022 director seats are his Meritech seats (he left Spark for Meritech in 2019); Extend was never Spark-listed (D8).")
if __name__ == "__main__": print(len(J), "judgments")
