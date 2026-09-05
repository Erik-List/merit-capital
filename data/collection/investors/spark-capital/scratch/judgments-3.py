import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge-lib.py")); jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
row, verdict = jl.row, jl.verdict
TC = "https://techcrunch.com/"
J = {}
def put(r): J[r["slug"]] = r
put(row("goji", "acquired", "Boston", "US", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "duplicate"],
        note="IDENTITY for the rebuild: Consumer United (listed 2013) renamed Goji in 2015 — one company, merge queued; Spark entered at a 2013 round of the eight-year-old insurance agency (Growth); acq. by Seeman Holtz, 2021"))
put(row("gowalla", "private", "Austin", "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited", "censored"],
        note="the 2022 relaunch of Gowalla (Josh Williams); Spark in the seed; too young for the graduation test"))
put(row("grammarly", "private", "San Francisco", "US", "Growth", "model", "AI & Applied AI", stage_conf="medium", flags=["needs_web_value", "cite_pending"], rng=None,
        note="Spark joined the $110M round of May 2017 (General Catalyst led, with IVP) — the company's first outside capital, Growth by scale; $13B mark (Nov 2021) to be pinned; rebranded Superhuman in 2025 after acquiring Superhuman"))
put(row("handshake", "private", "San Francisco", "US", "Growth", "web_verified", "Consumer & Marketplaces", stage_cite=TC+"2016/11/17/handshake-nabs-another-20m-to-end-geographic-advantages-in-recruiting/", stage_conf="high", flags=["stage_disputes_band", "needs_web_value"], rng=None,
        note="Spark led the $20M Series B (Nov 2016, Quinn board) — Growth; the band's Series A reads the $22M size; $3.5B mark (Jan 2022) to be pinned"))
put(row("harmonix", "acquired", "Boston", "US", "Growth", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["stage_disputes_band"],
        note="Rock Band studio (founded 1995); the 2015 $15M investment by Spark and Foundry (Hyatt board) is a minority growth round into a 20-year-old company — at-scale entry, Growth; acq. by Epic Games, Nov 2021"))
put(row("haven", "unknown", "San Francisco", "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited"],
        note="Haven Inc., freight booking platform; Spark led the Series A (2015); listed 2016-2019, company dark since ~2019"))
put(row("helaina", "private", "New York", "US", "Seed", "model", "Healthcare & Bio", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified", "graduation_disagree"],
        note="precision-fermentation infant nutrition; Spark in the 2020 seed (Thau board) and led the $20M Series A (Nov 2021) — graduated (the Form D layer's False misses the 2021 A)"))
put(row("hello-alfred", "private", "New York", "US", "Seed", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/Hello_Alfred", stage_conf="high", grad=True, grad_src="web_verified", grad_conf="high",
        note="$2M seed (Nov 2014, Spark, SV Angel, CrunchFund) and $10.5M Series A (Apr 2015, NEA led, Spark) — graduated; now a resident-services platform"))
put(row("heyday", "private", "San Francisco", "US", "Seed", "model", "AI & Applied AI", stage_conf="low", flags=["stage_uncited"],
        note="AI research assistant; Spark led the $6.5M seed (2022); no A on the record — graduation undetermined"))
put(row("higharc", "private", "Durham", "US", "Series A", "model", "Industrial & Robotics", stage_conf="medium",
        note="home-building design platform; Spark led the $21M Series A (2021)"))
put(row("hivemapper", "private", "Burlingame", "US", "Seed", "model", "Crypto & Web3", stage_conf="medium", grad=True, grad_conf="medium", flags=["cohort_unverified"],
        note="decentralized mapping network (HONEY token); Spark led the seed (2015); $18M Series A (2022, Multicoin led) — graduated late"))
put(row("homeis", "unknown", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="social network for immigrants (New York / Tel Aviv); Spark led the $12M Series A (Jan 2019); product discontinued ~2022, no documented exit"))
put(row("homelike", "acquired", "Cologne", "DE", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="furnished-apartment marketplace; Spark led the $14M Series A (2019); insolvency 2024, brand and platform to Spacest (acquired with a successor note, Cherry-run convention)"))
put(row("iex", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="medium",
        note="stock exchange; Spark led the $75M Series C (2014, Finkelstein board; firm news); below $1B"))
put(row("inform-technologies-inc", "unknown", "New York", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="news-aggregation technology; listed from 2008, the 2010 $6M filing (Politi board) is a follow-on; company dark after 2012"))
put(row("instabase", "private", "San Francisco", "US", "Growth", "web_verified", "AI & Applied AI", stage_cite="https://en.wikipedia.org/wiki/Instabase", stage_conf="high", rng="1b_plus", usd=2000000000, asof="2023-06", val_src="unicorn_list", val_conf="medium",
        note="Spark joined the $105M Series B (Oct 2019, Index led); $2B mark per the unicorn list, re-pinned in the A/B pass"))
put(row("instawork", "private", "San Francisco", "US", "Growth", "model", "Consumer & Marketplaces", stage_conf="medium", flags=["needs_web_value"], rng=None,
        note="hourly-work marketplace; Spark led the $18M Series B (Aug 2019); 2023 Series D valuation to be checked"))
put(row("inversion", "private", "Los Angeles", "US", "Series A", "model", "Industrial & Robotics", stage_conf="medium",
        note="re-entry capsules; Spark led the $44M Series A (Sept 2023)"))
put(row("invisionapp", "defunct", "New York", "US", "Growth", "model", "SaaS", stage_conf="medium",
        note="design collaboration platform; Spark Capital Growth led the $100M Series E (Nov 2017); wound down its services at the end of 2024 after the $2B 2018 mark"))
put(row("ipwireless", "acquired", "San Francisco", "US", "Growth", "model", "Data Infrastructure", stage_conf="medium", flags=["stage_disputes_band"],
        extra={"seed_to_a_graduation": None}, note="mobile broadband infrastructure carved out of NextWave in 2008; Spark entered at the $15.5M 2009 round (firm news) — a recapitalised mature company, Growth; acq. by General Dynamics, 2012"))
put(row("jam", "unknown", None, "US", "Seed", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="listed once (2018) under 'consumer'; Spark seed; company dark"))
put(row("jamiphy", "unknown", None, "US", "Seed", "model", "Media, Gaming & Advertising", stage_conf="low", flags=["stage_uncited", "city_unknown", "country_prior"],
        note="mini virtual-concert app (2021-2023 listings); Spark seed; dark since 2023"))
put(row("jana", "defunct", "Boston", "US", "Series A", "model", "Media, Gaming & Advertising", stage_conf="medium",
        note="txteagle renamed Jana (2011); Spark led the 2011 Series A ($8.5M), Dagres board through the 2016 Series C; shut down 2020"))
put(row("jelly", "acquired", "San Francisco", "US", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite="https://en.wikipedia.org/wiki/Jelly_(app)", stage_conf="high",
        note="Biz Stone's Q&A app; Series A (May 2013) from Spark, SV Angel and angels; acq. by Pinterest, 2017"))
put(row("jfrog", "public", "Sunnyvale", "US", "Growth", "model", "DevTools & APIs", public=True, stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=4400000000, val_src="sec_public_float",
        note="NASDAQ: FROG (IPO Sept 2020); HQ Sunnyvale (R&D Israel); Spark Growth in the $165M Series D (Oct 2018, Insight led) — citation in the A/B pass"))
put(row("justworks", "private", "New York", "US", "Growth", "model", "SaaS", stage_conf="low", flags=["needs_web_value", "cite_pending", "stage_uncited"], rng=None,
        note="PEO / payroll platform; Spark Growth in a late round (Series D/E, 2017-2020), listed from 2019; IPO withdrawn 2022; $2B mark (Jan 2020) to be checked"))
put(row("kateeva", "private", "Newark", "US", "Series A", "model", "Industrial & Robotics", stage_conf="low", flags=["stage_uncited", "web_check"],
        note="OLED inkjet manufacturing equipment; Spark in the 2009 Series A (listed from 2009); the 2016 ~$1B mark faded after the 2019-2020 restructuring — below_1b, to be web-checked"))
put(row("kickapps", "acquired", "New York", "US", "Series A", "model", "SaaS", stage_conf="medium",
        note="social-media software for publishers; Spark in the 2006 Series A (one of the firm's first deals); acq. by KIT digital, 2011"))
put(row("kik", "acquired", "Waterloo", "CA", "Series A", "web_verified", "Consumer & Marketplaces", stage_cite=TC+"2011/03/07/mobile-messaging-startup-kik-raises-8m-launches-group-chat-and-photo-sharing/", stage_conf="high",
        note="$8M Series A (Mar 2011, RRE, Spark, USV); the messenger was sold to MediaLab in Oct 2019 while Kik Interactive continued as the Kin token company — acquired; the 2015 $1B mark (Tencent) retired at the sale"))
put(row("lexity", "acquired", "Palo Alto", "US", "Series A", "model", "SaaS", stage_conf="low", flags=["stage_uncited", "duplicate"],
        note="IDENTITY for the rebuild: Vurve (listed 2011) rebranded Lexity in 2011 — merge queued; Spark in the 2010/2011 Series A; acq. by Yahoo, 2013"))
put(row("lightmatter", "private", "Boston", "US", "Series A", "web_verified", "Industrial & Robotics", stage_cite="https://www.finsmes.com/2019/02/lightmatter-receives-22m-in-series-a-1-funding.html", stage_conf="high", flags=["needs_web_value"], rng=None,
        note="photonic AI chips; Spark in the Series A (first tranche Dec 2017 with Matrix, the Feb 2019 A-1 led by GV; Politi board); $4.4B mark (Oct 2024) to be pinned"))
put(row("linkwell-health", "private", "Needham", "US", "Seed", "model", "Healthcare & Bio", stage_conf="low", grad=True, grad_src="formd", grad_conf="medium", flags=["cohort_unverified"],
        note="healthcare consumer-engagement content; Spark in the 2009 $3M round (Finkelstein board), the 2010 $7M and 2012 $15M rounds followed — graduated"))
put(row("liquidity", "private", "Tel Aviv", "IL", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited", "needs_web_value"], rng=None,
        note="Liquidity Group, AI-driven growth credit (Tel Aviv / New York / Abu Dhabi); Spark joined a 2021-2022 growth round; reported ~$1.4B mark to be checked"))
put(row("lithic", "private", "New York", "US", "Growth", "model", "Fintech & Payments", stage_conf="low", flags=["stage_uncited"],
        note="card-issuing API (ex Privacy.com); Spark joined a 2021-2022 round (listed from 2022); $800M mark (2021), below $1B"))
put(row("lola", "private", "New York", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="medium",
        note="reproductive-health products brand; Spark led the $7M Series A (Dec 2016)"))
put(row("lumafield", "private", "Boston", "US", "Growth", "model", "Industrial & Robotics", stage_conf="medium",
        note="industrial CT scanners; Spark led the $35M Series B (Nov 2023); below $1B"))
put(row("lumi", "acquired", "Los Angeles", "US", "Series A", "model", "Consumer & Marketplaces", stage_conf="low", flags=["stage_disputes_band", "stage_uncited"],
        extra={"seed_to_a_graduation": None}, note="packaging supply-chain platform; Spark led the 2019 Series A (~$9M; Thau board, the $4M filing is one tranche) — the band's Seed reads the size; acq. by Narvar, 2021"))
put({"slug": "mark43", "who": jl.WHO, "status": "private", "valuation_range": "below_1b", "valuation_usd": None, "valuation_confidence": "high",
     "entry_stage": "Seed", "entry_stage_source": "web_verified", "entry_stage_confidence": "high", "entry_stage_citation": "https://www.prnewswire.com/news-releases/mark43-secures-195-million-from-lead-investors-spark-capital-and-general-catalyst-215500431.html",
     "hq_city": "New York", "hq_city_source": "model_knowledge", "hq_country": "US", "hq_country_source": "model_knowledge", "focus": "SaaS", "focus_source": "model", "flags": [],
     "note": "public-safety software; $1.95M seed (Jul 2013) led by Spark and General Catalyst, $10.8M Series A (2015) — graduated (Form D)"})
put(row("marqeta", "public", "Oakland", "US", "Growth", "web_verified", "Fintech & Payments", public=True, stage_cite=TC+"2019/05/21/payment-card-startup-marqeta-confirms-260m-round-at-close-to-2b-valuation/", stage_conf="high", rng="1b_plus", usd=2300000000, val_src="sec_public_float",
        note="NASDAQ: MQ (IPO June 2021); Spark joined the $260M Series E (May 2019, Coatue led)"))
put(row("materia", "acquired", "New York", "US", "Seed", "model", "AI & Applied AI", stage_conf="low", grad=False, grad_conf="low", flags=["stage_uncited", "cohort_unverified"],
        note="AI for accounting firms; Spark led the seed (2024); acq. by Thomson Reuters, 2025 (site card) — no A before the exit"))
put(row("matx", "private", "Mountain View", "US", "Series A", "web_verified", "Industrial & Robotics", stage_cite=TC+"2024/11/22/ai-chip-startup-matx-founded-by-google-alums-raises-series-a-at-300m-valuation-sources-say/", stage_conf="high", flags=["stage_disputes_band", "needs_web_value"], rng=None,
        note="AI chips; Spark led the ~$80M Series A (Nov 2024, Razavi board) — the band's Growth reads the $95M size; the Feb 2026 $558M round's valuation to be pinned"))
put(row("medium", "private", "San Francisco", "US", "Growth", "model", "Media, Gaming & Advertising", stage_conf="medium", flags=["identity_uncertain"],
        note="Ev Williams' publishing platform: Spark Capital Growth led the $50M Series C (Apr 2016) — the row's 2007-2010 listing years belong to an unrelated early Spark company also named Medium (same name, no separable slug); the row is judged as the 2016 position; ~$600M mark, below $1B"))
put(row("menara-networks", "acquired", "Dallas", "US", "Series A", "model", "Data Infrastructure", stage_conf="medium",
        note="optical transport modules; Spark in the 2007 Series A (listed from 2007, Dagres board); acq. by IPG Photonics, 2016"))
put(row("messagebird", "private", "Amsterdam", "NL", "Growth", "model", "DevTools & APIs", stage_conf="medium", flags=["cite_pending"], rng="1b_plus", usd=3000000000, asof="2021-04", val_src="unicorn_list", val_conf="medium",
        note="Spark Capital led the $200M Series B (Oct 2020); renamed Bird (2024); $3B mark per the unicorn list, re-pinned in the A/B pass"))
put(row("midas", "private", "Istanbul", "TR", "Seed", "model", "Fintech & Payments", stage_conf="low", grad=True, grad_conf="medium", flags=["stage_uncited", "cohort_unverified", "model_disputes_source"],
        note="Turkish retail-investing app; Spark in the $11M seed (Nov 2022) and led the $45M Series A (Aug 2024) — graduated; Wikidata's 'acquired / ZA' is a homonym"))
if __name__ == "__main__": print(len(J), "judgments")
