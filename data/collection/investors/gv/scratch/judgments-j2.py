"""PRO-75 grind, queue batch 2 (judge j2): the 45 member rows aspire-health to checkr.

Every stage names the round GV entered from a source that ties GV to it (the firm's own post, the company's release,
a filing or press read in this pass); where no source read does, the stage is undetermined and the rounds found are
kept. Public rows carry their stockanalysis market cap of 2026-09-28. Three slugs hold two companies each (basis,
bowery, bloom-institute-of-technology): each is classified as the company its later listings and filings describe,
and the note names the other one.
"""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, ARCH, W, NEWS, FTS = (jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.ARCH, jl.W,
                                                      jl.NEWS, jl.FTS)
L = []
ASOF = "2026-09-28"


def SA(ticker):
    """stockanalysis.com market-cap page (read with curl on 2026-09-28)."""
    return f"https://stockanalysis.com/stocks/{ticker}/market-cap/"


WV = {"valuation_range_source": "web_verified"}
GRAD_LATER = " Graduation left for the graduation pass."

# ---------------------------------------------------------------- aspire-health
HCD = NEWS("aspire-health", "Google bets on palliative care")
L.append(cls(
    "aspire-health", status="acquired", rng="below_1b", city="Nashville", focus="Healthcare & Bio",
    note="Palliative and serious-illness care provider (Nashville; the 2016 Form D address). GV led the $32M round of "
         "October 2016, 'GV's first in Nashville' (Healthcare Dive, 2016-10-04); the story names no series, so the "
         "prefilled Form D band (Growth) stands. Anthem completed the acquisition in June 2018, months ahead of "
         "schedule (Fierce Healthcare, 2018-06-18); the firm's exit line 'Acquired by Anthem, 2018' agrees.",
    rounds=[rnd("2016-10-04", "round (unnamed)", 32000000, "GV", True, HCD, "press")]))

# ---------------------------------------------------------------- astrid
WA = W("Astrid (application)")
L.append(cls(
    "astrid", status="acquired", rng="below_1b", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=WA, entry_date="2011",
    flags=["model_disputes_source"],
    note="Mobile and social to-do list app founded in San Francisco in 2008. After AngelPad in 2011 'they raised a "
         "seed round of venture capital from Google Ventures' (Wikipedia); Yahoo bought the company on 2013-05-01 and "
         "closed the service in August 2013 (Business Insider; the firm's exit line 'Acquired by Yahoo!, 2013'). "
         "Disputed prefill: the entry_date 2023-07-18 came from Form D 0001990492-23-000001 of Astrid Health Inc. "
         "(Rachel Blank, 769 Broadway, New York; Frederique Dame director), which is Allara Health (the firm's own "
         "Allara post names Rachel Blank its CEO), a different company with its own row (allara-health); the entry "
         "date is the 2011 seed instead." + GRAD_LATER,
    rounds=[rnd("2011", "Seed", None, None, True, WA, "press")]))

# ---------------------------------------------------------------- attio
UKA = NEWS("attio", "Google Ventures-led Series B")
L.append(cls(
    "attio", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=POST("interview-with-nicholas-sharp"), city="London", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=UKA, entry_date="2025-08",
    extra={"valuation_range_source": "web_verified", "valuation_citation": UKA, "valuation_asof": ASOF},
    note="AI-native CRM (London; the firm's own interview asks 'Why set up headquarters in London?'). Google Ventures "
         "led the $52M Series B (UKTN, 2025-08-27; the firm's own post: 'I am so excited to lead Attio's Series B'), "
         "the firm's first 'Invested' month on /ai (August 2025); the seed (Point Nine, Balderton, 2021) and the "
         "$23.5M Series A (Redpoint, 2023) do not name GV in the sibling rows. Momentum-slice check 2026-09-28 "
         "(Google News for Attio with valuation): the Series B disclosed no valuation, Attio bought Inconvo in July "
         "2026, no priced round at or above $1B; aligned with the Balderton, Headline, Point Nine and Redpoint rows.",
    rounds=[rnd("2021-11-24", "Seed", 7700000, "Point Nine", None,
                "https://writing.pointnine.com/p/the-business-built-crm", "press"),
            rnd("2023-03-02", "Series A", 23500000, "Redpoint Ventures", None,
                NEWS("attio", "Attio raises $23.5M to build a next-gen CRM platform"), "press"),
            rnd("2025-08-26", "Series B", 52000000, "GV", True, UKA, "press")]))

# ---------------------------------------------------------------- basis
FGB = NEWS("basis", "Series B at $1.15bn valuation - FinTech Global")
L.append(cls(
    "basis", status="private", rng="1b_plus", usd=1150000000, val_src="web_verified", val_cite=FGB, asof="2026-02",
    country="US", city="New York", focus="AI & Applied AI",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=FGB, entry_date="2026-02",
    flags=["model_disputes_source"], extra=WV,
    note="AI agents for accounting firms (getbasis.ai, New York). Accel led the $100M Series B at a $1.15B valuation "
         "with GV participating (FinTech Global, 2026-02-25; Tech Funding News, 2026-02-24), the firm's own first "
         "'Invested' month on /ai (February 2026); the Khosla row records the earlier seed and the $34M Series A of "
         "December 2024, neither naming GV. The Accel and Khosla rows read below_1b; this priced round is fresher "
         "evidence (momentum-slice check 2026-09-28, Google News on Basis with valuation: no later round). The "
         "prefilled JP is a one-word Wikidata join; disputed. This slug holds two companies: the firm's "
         "2018-2019 listings are Basis (basis.io), the algorithmic stablecoin that raised $133M in 2018 and shut in "
         "December 2018 (the a16z and Bain Capital Ventures rows), which needs its own row; classified here as the "
         "live /ai company.",
    rounds=[rnd("2026-02-24", "Series B", 100000000, "Accel", True, FGB, "press")]))

# ---------------------------------------------------------------- bbot
BB8K = FTS("BridgeBio Pharma", "8-K")
BBS1 = FTS("BridgeBio Oncology Therapeutics, Inc.  (BBOT)", "S-1")
L.append(cls(
    "bbot", status="public", rng="below_1b", usd=305460000, val_src="web_verified", val_cite=SA("bbot"), asof=ASOF,
    country="US", city="South San Francisco", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BB8K, entry_date="2024-05", extra=WV,
    note="BridgeBio Oncology Therapeutics, RAS-pathway cancer drugs (South San Francisco, the S-1's principal office). "
         "GV joined the $200M private financing that launched BBOT, led by Cormorant and co-led by Omega (BridgeBio's "
         "8-K exhibit of 2024-05-02 names 'GV (Google Ventures)'); BBOT's S-1 calls that financing its Series B "
         "Preferred Stock ($200.0M at $0.7873 a share, April to May 2024), after a Series A held only by BridgeBio, "
         "so GV entered at the Series B. Listed on Nasdaq in August 2025 through the merger with Helix Acquisition "
         "Corp. II; GV 2023, L.P. holds 2,823,126 shares (S-1). Market cap $305.46M on 2026-09-28 (stockanalysis).",
    rounds=[rnd("2023-01", "Series A (BridgeBio only)", 79200000, "BridgeBio Pharma", False, BBS1, "filing"),
            rnd("2024-04-30", "Series B", 200000000, "Cormorant Asset Management", True, BBS1, "filing")]))

# ---------------------------------------------------------------- beacon-biosignals
BGN = NEWS("beacon-biosignals", "Upsizes Series B Financing to Over $97 Million - GlobeNewswire")
L.append(cls(
    "beacon-biosignals", status="private", rng="below_1b", country="US", city="Boston", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BGN, entry_date="2025-11",
    note="EEG and sleep-data platform for brain-disease trials (Boston, the release's dateline). The company's release "
         "of 2026-04-06 on the upsized Series B ($97M) names GV (Google Ventures) among the investors of the $86M "
         "Series B announced in November 2025, the firm's own first 'Invested' month on /ai; the $27M Series A of "
         "November 2021 was led by General Catalyst. No valuation disclosed (check 2026-09-28, Google News on the "
         "name: no priced round at or above $1B); below_1b, aligned with the General Catalyst row.",
    rounds=[rnd("2021-11-08", "Series A", 27000000, "General Catalyst", None,
                NEWS("beacon-biosignals", "raises $27 Million Series A led by General Catalyst"), "company"),
            rnd("2025-11-13", "Series B", 86000000, None, True,
                NEWS("beacon-biosignals", "Raises $86M in Series B Funding - FinSMEs"), "press"),
            rnd("2026-04-06", "Series B (extension)", 11000000, None, None, BGN, "company")]))

# ---------------------------------------------------------------- beam-therapeutics
GEN = NEWS("beam-therapeutics", "Raises $135M in Series B Financing")
L.append(cls(
    "beam-therapeutics", usd=2420000000, val_src="web_verified", val_cite=SA("beam"), asof=ASOF,
    city="Cambridge", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GEN, entry_date="2019-03", extra=WV,
    note="Base-editing medicines (238 Main Street, Cambridge MA, the company's site). GV came in as a new investor in "
         "the $135M Series B of March 2019 (GEN, 2019-03-06; F-Prime and ARCH had led the 2018 Series A), the year "
         "the firm first listed it; a 2021 resale prospectus shows GV 2019, L.P. holding 469,790 shares beyond the "
         "171,002 it received for Guide Therapeutics (" + FTS("Beam Therapeutics", "424B7") + "), so the position "
         "predates the Guide sale. IPO February 2020 (NASDAQ: BEAM). Market cap $2.42B on 2026-09-28 "
         "(stockanalysis) replaces the prefilled $1.7B.",
    rounds=[rnd("2018", "Series A", None, "F-Prime Capital; ARCH Venture Partners", False, GEN, "press"),
            rnd("2019-03-06", "Series B", 135000000, None, True, GEN, "press")]))

# ---------------------------------------------------------------- benson-hill
L.append(cls(
    "benson-hill", rng="below_1b", city="St. Louis", focus="Climate & Energy",
    note="Crop-genetics and soy-ingredient company (St. Louis; its Form D address). Filed for Chapter 11 on "
         "2025-03-20 (AgWeb) and sold its assets out of bankruptcy to Confluence Genetics (Business Wire, "
         "2025-05-23): an asset sale out of insolvency, so the prefilled acquired stands, Confluence Genetics the "
         "successor. GV co-led the $150M Series D of October 2020 with Wheatsheaf (AgFunderNews); the entry stage "
         "stays the prefilled Form D band (Growth, 2018). The firm's exit line 'NYSE: BHIL' is stale (decisions D8).",
    rounds=[rnd("2020-10-29", "Series D", 150000000, "GV; Wheatsheaf", True,
                NEWS("benson-hill", "GV & Wheatsheaf-led Series D"), "press")]))

# ---------------------------------------------------------------- blacksmith
BS_SEED = NEWS("blacksmith", "led by GV and Y Combinator")
BS_A = NEWS("blacksmith", "Doubles Down on Blacksmith With $10M Series A")
BS_B = NEWS("blacksmith", "valuation jumps almost 10x")
L.append(cls(
    "blacksmith", status="private", rng="below_1b", usd=550000000, val_src="web_verified", val_cite=BS_B,
    asof="2026-08-12", city="San Francisco", focus="DevTools & APIs",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BS_SEED, entry_date="2025-05-01",
    grad="graduated", grad_src="web_verified", grad_cite=BS_A, grad_conf="high",
    flags=["stage_disputes_band"], extra=WV,
    note="Bare-metal CI runners for GitHub Actions (San Francisco; the release and the 2026 Form D). GV and Y "
         "Combinator led the $3.5M seed announced 2025-05-01 (PR Newswire); the firm's own post says it partnered "
         "'at the seed stage' and would 'double down and lead their Series A', the $10M Series A of September 2025 "
         "(The Tech Buzz), which graduates the row. Disputes the prefilled Form D band (Growth, 2026-05-07): that "
         "filing is the $45M Series B led by Peak XV at a $550M valuation (TechCrunch, 2026-08-12). Momentum-slice "
         "check 2026-09-28: that Series B is the latest priced round, below $1B.",
    rounds=[rnd("2025-05-01", "Seed", 3500000, "GV; Y Combinator", True, BS_SEED, "company"),
            rnd("2025-09-17", "Series A", 10000000, "GV", True, BS_A, "press"),
            rnd("2026-08-12", "Series B", 45000000, "Peak XV Partners", True, BS_B, "press")]))

# ---------------------------------------------------------------- blockaid
JPB = NEWS("blockaid", "includes Google Ventures")
L.append(cls(
    "blockaid", status="private", rng="below_1b", country="IL", country_src="web_verified", country_cite=JPB,
    city="Tel Aviv", focus="Security",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=JPB, entry_date="2025-02",
    note="Onchain transaction security ('Israel's Blockaid', The Jerusalem Post; Tel Aviv as in the Greylock, Ribbit "
         "and Sequoia rows). Google Ventures 'was one of several VCs to take part in the series B investment round', "
         "the $50M led by Ribbit Capital (The Jerusalem Post, 2025-02-19), the firm's own first 'Invested' month on "
         "/ai; the 2022 seed and the $27M Series A of October 2023 do not name GV in the sibling rows. Momentum "
         "check 2026-09-28 (Google News on Blockaid with valuation): no round since the Series B, nothing at or "
         "above $1B.",
    rounds=[rnd("2023-10", "Series A", 27000000, "Ribbit Capital; Variant", None,
                "https://www.calcalistech.com/ctechnews/article/skq7n74zp", "press"),
            rnd("2025-02-18", "Series B", 50000000, "Ribbit Capital", True, JPB, "press")]))

# ---------------------------------------------------------------- blockchain
CDB = "https://www.coindesk.com/markets/2017/06/22/bitcoin-startup-blockchain-raises-40-million-series-b"
UKB = NEWS("blockchain", "London-based digital asset platform")
PYB = NEWS("blockchain", "Seeks $6 Billion Valuation in IPO")
CNB = ("https://cryptonews.com/news/blockchaincom-seeks-new-funding-at-4-billion-valuation-70-decline-from-"
       "previous-round/")
L.append(cls(
    "blockchain", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified", val_cite=CNB, asof="2023-11",
    country="GB", country_src="web_verified", country_cite=UKB, city="London", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CDB, entry_date="2017-06",
    flags=["stale"], extra=WV,
    note="Blockchain.com, crypto wallet and exchange ('London-based', UKTN 2021). GV entered in the $40M Series B of "
         "June 2017 (CoinDesk, 2017-06-22: 'Digital Currency Group, GV, Lakestar, Lightspeed ...'), the year the "
         "firm first listed it; the 2014 Series A was Lightspeed's. Later: $120M in February 2021 with GV (UKTN), "
         "$300M at $5.2B in March 2021 (Wikipedia), $14B in 2022, then the $110M Series E of November 2023 led by "
         "Kingsway that 'valued Blockchain.com at less than half the $14 billion it reached in 2022' (PYMNTS, "
         "2026-09-28). Mark aligned with the Lightspeed row, $4B as of November 2023 on its CryptoNews citation, "
         "which returned 403 to this pass; the September 2026 IPO plan targets $4-6B (PYMNTS), so 1b_plus holds. "
         "Older than 24 months: stale.",
    rounds=[rnd("2014", "Series A", None, "Lightspeed Venture Partners", False, "https://lsvp.com/company/blockchain/",
                "press"),
            rnd("2017-06-22", "Series B", 40000000, None, True, CDB, "press"),
            rnd("2021-02-17", "round (unnamed)", 120000000, None, True, UKB, "press"),
            rnd("2021-03", "round (unnamed)", 300000000, None, None, W("Blockchain.com"), "press"),
            rnd("2023-11", "Series E", 110000000, "Kingsway Capital", None, PYB, "press")]))

# ---------------------------------------------------------------- bloom-institute-of-technology
BT = "https://www.bloomtech.com/article/bloomtech-announces-14-million-series-a-led-by-gv"
L.append(cls(
    "bloom-institute-of-technology", status="private", rng="below_1b", city="Austin", focus="Consumer & Marketplaces",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=BT, entry_date="2018-10-08",
    flags=["stage_disputes_band"],
    note="Coding bootcamp, Lambda School until its 2021 rename. GV led the $14M Series A announced 2018-10-08 (the "
         "company's own release; Stripe also in), the year the firm first listed Lambda School; disputes the "
         "prefilled Form D band (Growth, 2020-08-05), which is the $74M Series C. Later the $30M round of January "
         "2019 with Google Ventures again (Wikipedia). Still enrolling students after the 2024 CFPB order "
         "(bloomtech.com, read 2026-09-28). City aligned with the Y Combinator row (Austin); the 2018 release and "
         "the 2020 Form D give San Francisco. This slug also carries the firm's 2015-2017 listing of Bloom "
         "(bloomcloser.com, a family smart-device startup, partner Rich Miner), a different company that explains "
         "first_seen 2015.",
    rounds=[rnd("2018", "Seed", None, None, False, W("Bloom Institute of Technology"), "press"),
            rnd("2018-10-08", "Series A", 14000000, "GV", True, BT, "company"),
            rnd("2019-01", "Series B", 30000000, None, True, W("Bloom Institute of Technology"), "press"),
            rnd("2020-08", "Series C", 74000000, None, None, W("Bloom Institute of Technology"), "press")]))

# ---------------------------------------------------------------- blue-water-autonomy
BWA = NEWS("blue-water-autonomy", "Series A Led by GV")
L.append(cls(
    "blue-water-autonomy", status="private", rng="below_1b", country="US", city="Boston", focus="Industrial & Robotics",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=BWA, entry_date="2025-08",
    note="Long-range autonomous naval ships (Boston). GV led the $50M Series A announced 2025-08-26 (PR Newswire; the "
         "firm's own post: 'I'm honored to lead this Series A'); the $14M seed of April 2025 came from Eclipse, Riot "
         "and Impatient Ventures (the same release), so GV entered at the A.",
    rounds=[rnd("2025-04", "Seed", 14000000, "Eclipse", False, BWA, "company"),
            rnd("2025-08-26", "Series A", 50000000, "GV", True, BWA, "company")]))

# ---------------------------------------------------------------- bonnet
UKBN = "https://www.uktech.news/mobility/bonnet-funding-20220302"
L.append(cls(
    "bonnet", status="acquired", rng="below_1b", country="GB", country_src="web_verified", country_cite=UKBN,
    city="London", focus="Climate & Energy",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2022-03",
    note="EV-charging app ('London-based', UKTN). GV joined the $5.5M (GBP 4M) round led by Lightspeed in March 2022 "
         "('venture capital firms Lightspeed, GV and 20VC also provided funding', UKTN, 2022-03-02), the year the firm "
         "first listed it. UKTN names no series and calls the $1.2M round of August 2021 the seed; Lightspeed, the "
         "lead, labels this entry Seed and the amount sits inside the 2022 seed band, so the round reads Seed at "
         "medium confidence, as in the 20VC and Lightspeed rows. OVO Energy agreed to buy Bonnet in November 2023 "
         "(Mercom), completed 2025-07-23 per the Lightspeed row." + GRAD_LATER,
    rounds=[rnd("2021-08", "Seed", 1200000, None, False, UKBN, "press"),
            rnd("2022-03-02", "round (unnamed; Lightspeed's card: Seed)", 5500000, "Lightspeed", True, UKBN, "press")]))

# ---------------------------------------------------------------- bounti
MTC = NEWS("bounti", "Bounti Secures $16 Million in Funding from Google Ventures")
L.append(cls(
    "bounti", status="private", rng="below_1b", country="US", focus="AI & Applied AI",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=MTC, entry_date="2023-07",
    flags=["city_unknown"],
    extra={"valuation_range_source": "web_verified", "valuation_citation": MTC, "valuation_asof": ASOF},
    note="AI teammate for sales, marketing and customer-success teams (bounti.ai, founded 2023). '$16 million in seed "
         "funding led by Google Ventures' with Floodgate, Bloomberg Beta, Haystack, Octave and MS&AD, announced "
         "2024-09-12 as it came out of stealth (MarTech Cube; PYMNTS). Entry date from the firm's own /ai record "
         "('Invested' 2023-07, 'Re-invested' 2024-06; decisions D7), the seed's tranches. No source read places the "
         "company in a city (the Berlin 'Bounti' of the 2026 EU-Startups story and Local Bounti are other "
         "companies). Momentum-slice check 2026-09-28 (Google News for Bounti with raises and seed): no later "
         "round, no $1B mark." + GRAD_LATER,
    rounds=[rnd("2024-09-12", "Seed", 16000000, "GV", True, MTC, "press")]))

# ---------------------------------------------------------------- bowery
AGA = NEWS("bowery", "Bowery Farming Raises $20m Series A")
AGB = NEWS("bowery", "Bowery Raises $90m Series B from GV, Temasek")
L.append(cls(
    "bowery", status="defunct", rng="below_1b", city="New York", focus="Industrial & Robotics",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=AGA, entry_date="2017-06",
    flags=["stage_disputes_band"],
    note="Bowery Farming, indoor vertical farms (New York; its Form D address). GV joined the $20M Series A of June "
         "2017 co-led by General Catalyst and GGV (AgFunderNews, 2017-06-14; the $7.5M seed earlier in 2017 was "
         "First Round's and others', without GV), then led the $90M Series B of December 2018 'as an existing "
         "investor' (AgFunderNews); disputes the prefilled Form D band (Growth, 2018-12-05), which is that Series B. "
         "$300M Series C in May 2021 (Reuters). Wound down in November 2024 (Axios: 'to shut down'), as the First "
         "Round row reads. This slug holds two companies: the firm's 2014-2015 listings are Bowery (bowery.io, "
         "development environments, partner MG Siegler), a different company that needs its own row; the 2017-2024 "
         "listings are Bowery Farming.",
    rounds=[rnd("2017-02", "Seed", 7500000, "First Round Capital", False, AGA, "press"),
            rnd("2017-06-14", "Series A", 20000000, "General Catalyst; GGV Capital", True, AGA, "press"),
            rnd("2018-12-12", "Series B", 90000000, "GV", True, AGB, "press"),
            rnd("2021-05-25", "Series C", 300000000, None, None,
                NEWS("bowery", "Indoor vertical farming startup Bowery Farming raises $300 mln"), "press")]))

# ---------------------------------------------------------------- brightline
BLB = NEWS("brightline", "$72M Series B Funding Led by GV")
L.append(cls(
    "brightline", status="private", rng="below_1b", city="Palo Alto", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BLB, entry_date="2021-06",
    note="Pediatric behavioral health, virtual and in clinics (headquartered in Palo Alto per its 2021 release). GV led "
         "the $72M Series B of 2021-06-16 as a new investor (PR Newswire: GV among the new investors, Oak HC/FT and "
         "Threshold returning), the year the firm first listed it. KKR led the $105M round of March 2022 at $705M "
         "(Bloomberg headline), below $1B; still operating (new clinics in New York in 2025-2026).",
    rounds=[rnd("2021-06-16", "Series B", 72000000, "GV", True, BLB, "company"),
            rnd("2022-03-29", "round (unnamed)", 105000000, "KKR", None,
                NEWS("brightline", "KKR Values Behavioral-Health Startup Brightline"), "press")]))

# ---------------------------------------------------------------- buena
TEU = ("https://tech.eu/2025/07/23/gv-and-20vc-back-buenas-vision-to-reinvent-property-management-through-ai-"
       "powered-rollups-with-58m-investment/")
L.append(cls(
    "buena", status="private", rng="below_1b", country="DE", country_src="web_verified", country_cite=TEU,
    city="Berlin", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TEU, entry_date="2025-07",
    extra={"valuation_range_source": "web_verified", "valuation_citation": TEU, "valuation_asof": ASOF},
    note="AI-run property management built by buying and digitising property managers (Berlin). GV led the $58M "
         "(EUR 49M) Series A with 20VC, Stride and Capnamic (Tech.eu, 2025-07-23; the firm's own post of that day "
         "announces 'our investment'), the firm's first 'Invested' month on /ai; the EUR 3M round of 2017 (as Home) "
         "was EQT Ventures' (the EQT Ventures row). No valuation disclosed; momentum check 2026-09-28 (Google News on "
         "Buena with valuation): nothing at or above $1B.",
    rounds=[rnd("2017-08", "round (unnamed; EUR 3M, as Home)", None, "EQT Ventures", False,
                "https://index.commoncrawl.org/CC-MAIN-2017-47-index?url=https%3A%2F%2Feqtventures.com%2Farticle%2F"
                "home-raises-3-million-round-led-by-eqt-ventures%2F&output=json", "press"),
            rnd("2025-07-23", "Series A", 58000000, "GV", True, TEU, "press")]))

# ---------------------------------------------------------------- bufferbox
WBB = W("BufferBox")
L.append(cls(
    "bufferbox", status="acquired", rng="below_1b", country="CA", country_src="web_verified", country_cite=WBB,
    city="Waterloo", focus="Consumer & Marketplaces", stage="undetermined",
    note="Parcel-pickup kiosks, a University of Waterloo startup (Wikipedia; confirms the prefilled CA). Y Combinator "
         "2012; Google bought it on 2012-11-30 and closed the service in 2014 (Wikipedia; the firm's exit line "
         "'Acquired by Google, 2012'). The firm listed it from 2013 (Blake Byers), but no source read names a GV "
         "round: Google News for BufferBox with Google Ventures, seed and funding returned only the acquisition "
         "coverage, so the stage is undetermined; aligned with the a16z and General Catalyst rows.",
    rounds=[]))

# ---------------------------------------------------------------- cacheflow
TCC = NEWS("cacheflow", "Cacheflow doubles valuation while raising $10M")
L.append(cls(
    "cacheflow", rng="below_1b", country="US", city="San Francisco", focus="SaaS",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TCC, entry_date="2022-12",
    note="Billing, CPQ and subscription management for B2B software sales (San Francisco per TechCrunch, 2024). GV "
         "(Crystal Huang) led the $10M 'Seed+' round of December 2022 after GGV's $6M seed of November 2021 "
         "(TechCrunch, 2022-12-06); a seed extension reads Seed. HubSpot acquired the company in October 2024 "
         "(TechCrunch, 2024-10-11), having raised $16M in all; the firm's exit line agrees." + GRAD_LATER,
    rounds=[rnd("2021-11", "Seed", 6000000, "GGV Capital", False, TCC, "press"),
            rnd("2022-12-06", "Seed+", 10000000, "GV", True, TCC, "press")]))

# ---------------------------------------------------------------- career-karma
TCK = NEWS("career-karma", "Career Karma lands $40M to evolve")
L.append(cls(
    "career-karma", status="private", rng="below_1b", country="US", city="Miami", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TCK, entry_date="2022-01",
    note="Platform guiding career switchers into tech jobs (Miami, per Refresh Miami 2024). GV joined the $40M Series B "
         "of January 2022 led by Top Tier Capital Partners as a new investor (TechCrunch, 2022-01-10), the year the "
         "firm first listed it. In October 2024 the founders launched OutRival on the Series B's leftover capital, "
         "and 'Career Karma will continue as a separate company, just now owned by OutRival' (TechCrunch, "
         "2024-10-15): a restructuring under the founders' new parent, not a sale to a third party, so private.",
    rounds=[rnd("2022-01-10", "Series B", 40000000, "Top Tier Capital Partners", True, TCK, "press")]))

# ---------------------------------------------------------------- carbon
VBC = NEWS("carbon", "raises $260 million at $2.4 billion valuation")
L.append(cls(
    "carbon", status="private", rng="1b_plus", usd=2400000000, val_src="web_verified", val_cite=VBC, asof="2019-06",
    city="Redwood City", focus="Industrial & Robotics", flags=["stale"], extra=WV,
    note="Digital light synthesis 3D printing (Redwood City). Last priced mark with a figure: the $260M growth round "
         "of June 2019 at a $2.4B valuation, co-led by Madrone and Baillie Gifford (VentureBeat, 2019-06-25), as the "
         "Sequoia row carries; the $60M round of November 2025 disclosed no valuation (Bicycle Retailer) and no "
         "collapse evidence was found, so the stale mark stands. The entry stage stays the prefilled Form D band "
         "(Growth, August 2015).",
    rounds=[rnd("2019-06-25", "growth round", 260000000, "Madrone Capital Partners; Baillie Gifford", None, VBC,
                "press"),
            rnd("2025-11-13", "round (unnamed)", 60000000, None, None, NEWS("carbon", "closes on $60M funding"),
                "press")]))

# ---------------------------------------------------------------- cardurion-pharmaceuticals
L.append(cls(
    "cardurion-pharmaceuticals", status="private", rng="below_1b", city="Burlington", focus="Healthcare & Bio",
    note="Cardiovascular drug developer (Burlington MA; its 2024 Form D address). Closed a $260M Series B in July 2024 "
         "(Fierce Biotech), the round the prefilled Form D band dates (Growth, 2024-07-10) and the year the firm first "
         "listed it; no valuation disclosed, below_1b.",
    rounds=[rnd("2024-07-16", "Series B", 260000000, None, None,
                NEWS("cardurion-pharmaceuticals", "closes hearty $260M series B"), "press")]))

# ---------------------------------------------------------------- celsius-therapeutics
FBC = NEWS("celsius-therapeutics", "Celsius bags $65M")
ABV = NEWS("celsius-therapeutics", "AbbVie Acquires Celsius Therapeutics - PR Newswire")
L.append(cls(
    "celsius-therapeutics", status="acquired", rng="below_1b", country="US", city="Cambridge",
    focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FBC, entry_date="2018-05",
    note="Single-cell genomics drug discovery for autoimmune disease and cancer (Cambridge MA). Launched with a $65M "
         "Series A led by Third Rock Ventures 'with participation from Alphabet's venture arm GV' (Fierce Biotech, "
         "2018-05-15), the year the firm first listed it; an $83M financing followed in March 2022 (Fierce Biotech). "
         "AbbVie acquired all outstanding equity for $250M in cash on 2024-06-27 (AbbVie's release), as the firm's "
         "exit line records.",
    rounds=[rnd("2018-05-15", "Series A", 65000000, "Third Rock Ventures", True, FBC, "press"),
            rnd("2022-03-24", "round (unnamed)", 83000000, None, None, NEWS("celsius-therapeutics", "$83M financing"),
                "press")]))

# ---------------------------------------------------------------- censys
VBS = NEWS("censys", "Censys raises $15.5 million to bring attack surface")
TCS = NEWS("censys", "Censys, a search engine for internet devices, raises $15.5M Series A")
L.append(cls(
    "censys", status="private", rng="below_1b", country="US", city="Ann Arbor", focus="Security",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=VBS, entry_date="2018-11",
    grad="graduated", grad_src="web_verified", grad_cite=TCS, grad_conf="high",
    note="Internet-wide scanning and attack-surface intelligence (Ann Arbor). 'Censys had raised $2.6 million in a seed "
         "round led by GV and Greylock back in 2018' (VentureBeat, 2020-08-05; the seed was announced in November "
         "2018), as the Greylock row reads; GV and Decibel then co-led the $15.5M Series A of 2020-08-05 "
         "(TechCrunch), which graduates the row. Later rounds of $75M (October 2023) and $70M (March 2026) disclosed "
         "no valuation; below_1b.",
    rounds=[rnd("2018-11-27", "Seed", 2600000, "GV; Greylock", True, VBS, "press"),
            rnd("2020-08-05", "Series A", 15500000, "GV; Decibel", True, TCS, "press"),
            rnd("2023-10-24", "round (unnamed)", 75000000, None, None,
                NEWS("censys", "Censys Secures $75M in New Funding - PR Newswire"), "company"),
            rnd("2026-03-31", "round (unnamed)", 70000000, None, None,
                NEWS("censys", "Censys Raises $70 Million for Internet Intelligence Platform"), "press")]))

# ---------------------------------------------------------------- cerevance
CVB = "https://www.cerevance.com/media/cerevance-closes-45-million-series-b-financing"
CVM = "https://cerevance.com/media"
L.append(cls(
    "cerevance", status="private", rng="below_1b", country="US", city="Boston", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CVB, entry_date="2020-04",
    note="Neuroscience drug developer (Boston, MA per its release; research at Cambridge Science Park, UK). The Series "
         "B of 2020-04-14 brought '$45 million from new investors including GV (formerly Google Ventures), Bill Gates "
         "and Foresite Capital' (the company's release), the year the firm first listed it; the $36M launch of "
         "December 2016 predates GV. Series B extensions to $65M (July 2020) and by $51M (February 2023), a $47M "
         "Series B-1 (April 2024) and a $20M Series C (May 2026), valuations undisclosed.",
    rounds=[rnd("2016-12-02", "launch financing", 36000000, None, False, CVM, "company"),
            rnd("2020-04-14", "Series B", 45000000, None, True, CVB, "company"),
            rnd("2024-04-25", "Series B-1", 47000000, None, None, CVM, "company"),
            rnd("2026-05-12", "Series C", 20000000, None, None, CVM, "company")]))

# ---------------------------------------------------------------- checkr
NBC = NEWS("checkr", "Background Check Startup Checkr Raises $9M")
L.append(cls(
    "checkr", city="San Francisco", focus="SaaS",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NBC, entry_date="2014-10",
    note="Background-check platform (San Francisco, as the Accel, Coatue, IVP and YC rows read; the 2014 story places it "
         "in Sunnyvale). Google Ventures joined the $9M Series A of October 2014 led by Accel (NBC 7 San Diego, "
         "2014-10-14), the year the firm first listed it (Chris Hutchins); the firm's /ai record shows a "
         "re-investment in May 2018. The prefilled private $4.6B mark (the September 2021 Series E) stands.",
    rounds=[rnd("2014-10-14", "Series A", 9000000, "Accel", True, NBC, "press")]))

# ---------------------------------------------------------------- bitterroot-bio
P2B = NEWS("bitterroot-bio", "Pulse 2.0")
L.append(cls(
    "bitterroot-bio", status="private", rng="below_1b", country="US", city="Palo Alto", focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=P2B, entry_date="2023-06",
    note="Cardio-immunology drug developer (its releases are datelined Palo Alto, Needham and Melbourne, Palo Alto "
         "first). Came out of stealth with a $145M Series A co-led by ARCH Venture Partners and Deerfield with GV, "
         "Koch Disruptive Technologies and Alexandria (Pulse 2.0, 2023-06-20; Endpoints, 2023-06-07), its first "
         "financing and the year the firm first listed it. No valuation disclosed; below_1b.",
    rounds=[rnd("2023-06-07", "Series A", 145000000, "ARCH Venture Partners; Deerfield Management", True, P2B,
                "press")]))

# ---------------------------------------------------------------- cala-health
CALA_C = "https://calahealth.com/wp-content/uploads/2019/05/Cala-Health-Series-C-FINAL-1.pdf"
L.append(cls(
    "cala-health", status="private", rng="below_1b", country="US", city="Burlingame", focus="Healthcare & Bio",
    stage="undetermined",
    note="Wearable neuromodulation for essential tremor (Burlingame, the 2019 release's dateline). GV is already an "
         "existing investor in the $50M Series C of May 2019 ('All existing investors participated in the round, "
         "including ... dRx Capital, and GV', the company's release), so it entered in an earlier round; no source "
         "read names which (Google News for the Series A and B, the company's newsroom and one web search), so the "
         "stage is undetermined. Later a $77M round (November 2021) and a $50M financing (December 2024). Private, "
         "below_1b, aligned with the Lux row.",
    rounds=[rnd("2019-05-21", "Series C", 50000000, None, True, CALA_C, "company"),
            rnd("2021-11-16", "round (unnamed)", 77000000, None, None, NEWS("cala-health", "scores $77M"), "press"),
            rnd("2024-12-09", "round (unnamed)", 50000000, None, None,
                NEWS("cala-health", "Cala Health raises $50M to expand wearable tremor therapy"), "press")]))

# ---------------------------------------------------------------- cameo
BIC = NEWS("cameo", "Billion Valuation From GV, Alexa Fund")
L.append(cls(
    "cameo", status="private", rng="below_1b", country="US", city="Chicago", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=BIC, entry_date="2021-03",
    flags=["model_disputes_source"],
    note="Personalised celebrity video messages (Chicago; Wikipedia). GV entered in the $100M round of March 2021 "
         "('Cameo Snags New Funding at a $1 Billion Valuation From GV, Alexa Fund', Business Insider, 2021-03-30; "
         "Variety: 'Cameo Raises $100 Million From Investors Including Amazon, Google, UTA'; both bodies paywalled "
         "to this pass), the year the firm first listed it; it followed the $50M Series B led by Kleiner Perkins in "
         "June 2019 (the Bain Capital Ventures row), so it reads Growth. The 2021 $1B is SoftBank's estimate, which "
         "SoftBank cut to $100M in 2022, with the company's own investors at $50M by 2023 (Wikipedia): below_1b, "
         "aligned with the Bain Capital Ventures, Headline, Lightspeed and Spark rows. The prefilled IT is a "
         "one-word Wikidata join; disputed.",
    rounds=[rnd("2019-06", "Series B", 50000000, "Kleiner Perkins", False,
                "https://www.prnewswire.com/news-releases/cameo-closes-50-million-series-b-round-led-by-kleiner-"
                "perkins-300874358.html", "company"),
            rnd("2021-03-30", "round (unnamed)", 100000000, None, True, BIC, "press")]))

# ---------------------------------------------------------------- carebridge
HHCN = NEWS("carebridge", "Raise a Combined $70M in Funding")
ELV = "https://www.sec.gov/Archives/edgar/data/1156039/000115603925000057/elv-20250331.htm"
L.append(cls(
    "carebridge", status="acquired", rng="below_1b", country="US", city="Nashville", focus="Healthcare & Bio",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2020-01",
    note="Value-based care for Medicaid members receiving home and community-based services (Nashville). Launched on "
         "2020-01-13 'by announcing an initial $40 million funding round' from Oak HC/FT and GV (Home Health Care "
         "News, 2020-01-14; The Tennessean: 'backed by Google'), the year the firm first listed it; the launch round "
         "is the company's first priced financing and is named in no source read, so it reads Series A at medium "
         "confidence. Oak HC/FT led the $140M financing of June 2022 at a valuation over $1B (the company's "
         "release). Elevance Health completed the acquisition on 2024-12-10 (its Q1 2025 10-Q: 'RSV QOZB LTSS, "
         "Inc. and certain affiliated entities (CareBridge)'); acquired rows carry no mark.",
    rounds=[rnd("2020-01-13", "initial round (unnamed)", 40000000, None, True, HHCN, "press"),
            rnd("2022-06-08", "round (unnamed)", 140000000, "Oak HC/FT", None,
                NEWS("carebridge", "CareBridge Closes $140M Financing"), "company")]))

# ---------------------------------------------------------------- checkmate
L.append(cls(
    "checkmate", status="private", rng="below_1b", city="Santa Monica", city_src="formd_address",
    focus="Consumer & Marketplaces",
    stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=POST("checkmate-a-breakthrough"),
    note="Shopping app and browser extension that finds savings at checkout (joincheckmate.com; Santa Monica on its "
         "2023 Form D). The firm's own post of 2023-05-25: 'we're thrilled to announce our support of Checkmate on "
         "this journey, with $15M in Series A funding led by GV' (TechCrunch the same day: GV led, after a $5M seed "
         "of September 2022); the prefilled entry date is that Form D. Not the a16z 'Checkmate' (speedrun SR004, "
         "labyrinth.io, AI voice and fintech, founded 2024, San Francisco), a different company of the same name. "
         "No later round found; below_1b.",
    rounds=[rnd("2022-09", "Seed", 5000000, None, False,
                NEWS("checkmate", "Celebrity investors pile into consumer savings startup"), "press"),
            rnd("2023-05-25", "Series A", 15000000, "GV", True, POST("checkmate-a-breakthrough"), "firm")]))

# ---------------------------------------------------------------- biomodal
TCE = "https://techcrunch.com/2016/03/17/googles-gv-leads-21m-series-b-in-bioscience-firm-cambridge-epigenetix/"
L.append(cls(
    "biomodal", status="private", rng="below_1b", city="Cambridge", focus="Healthcare & Bio",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TCE, entry_date="2016-03",
    flags=["stage_disputes_band"],
    note="Genetic and epigenetic sequencing tools, Cambridge Epigenetix until its 2023 rebrand (Cambridge, UK; the 2018 "
         "Form D gives Great Cambourne, Cambridge). GV led the $21M Series B of March 2016 with Sequoia and the "
         "returning New Science Ventures, Syncona and Cambridge University (TechCrunch, 2016-03-17), the year the firm "
         "first listed it; disputes the prefilled Form D band (Series A, 2018-04-18), a later filing. An $88M round "
         "followed in November 2021 (Fierce Biotech headline). Private, below_1b, aligned with the Sequoia row.",
    rounds=[rnd("2016-03-17", "Series B", 21000000, "GV", True, TCE, "press"),
            rnd("2021-11-02", "round (unnamed)", 88000000, None, None,
                NEWS("biomodal", "GV-backed Cambridge Epigenetix lines up $88M"), "press")]))

# ---------------------------------------------------------------- autolus
AUF1 = FTS("Autolus Therapeutics Ltd", "F-1")
L.append(cls(
    "autolus", status="public", rng="below_1b", usd=495060000, val_src="web_verified", val_cite=SA("autl"), asof=ASOF,
    country="GB", country_src="web_verified", country_cite=AUF1, city="London", focus="Healthcare & Bio",
    stage="undetermined", extra=WV,
    note="Programmed T-cell therapies for cancer (Forest House, 58 Wood Lane, White City, London, the F-1's address). "
         "The F-1 of May 2018 names 'Google Ventures' among its backers, so GV held before the June 2018 Nasdaq IPO; "
         "the F-1 files every private round as series A preferred shares (September 2014 Syncona; March 2016 GBP "
         "23.3M; April to September 2017 GBP 36.7M; September 2017 $80.0M) and lists purchasers only above 5%, and no "
         "source read ties GV to one of them (Google News for the 2017 financing found none), so the stage is "
         "undetermined. Market cap $495.06M on 2026-09-28 (stockanalysis).",
    rounds=[rnd("2014-09-25", "series A preferred (initial)", None, "Syncona", False, AUF1, "filing"),
            rnd("2016-03-02", "series A preferred (GBP 23.3M)", None, None, None, AUF1, "filing"),
            rnd("2017-04-03", "series A preferred (GBP 36.7M)", None, None, None, AUF1, "filing"),
            rnd("2017-09-25", "series A preferred (press: Series C)", 80000000, None, None, AUF1, "filing")]))

# ---------------------------------------------------------------- blackthorn-therapeutics
NMS1 = "https://www.sec.gov/Archives/edgar/data/1885522/000119312523221589/d241143ds1.htm"
FB76 = NEWS("blackthorn-therapeutics", "BlackThorn bags $76M")
L.append(cls(
    "blackthorn-therapeutics", status="acquired", rng="below_1b", country="US", city="San Francisco",
    focus="Healthcare & Bio", stage="undetermined",
    note="Targeted treatments for neurobehavioral disorders (San Francisco). The firm listed it from 2017; the $76M "
         "round of June 2019 names GV among the 'existing backers' with ARCH, Alexandria, J&J Innovation and Mercury "
         "(Fierce Biotech, 2019-06-13), so GV entered in an earlier round that no source read names (Google News for "
         "the Series A and the launch found none), so the stage is undetermined. Neumora (then RBNC Therapeutics) "
         "acquired BlackThorn in late 2020 as a wholly owned subsidiary, later dissolved (Neumora's S-1, 2023); the "
         "firm's exit line 'Acquired by Neumora Therapeutics, 2020' agrees.",
    rounds=[rnd("2019-06-13", "round (unnamed)", 76000000, None, True, FB76, "press")]))

# ---------------------------------------------------------------- cambly
TCM = NEWS("cambly", "Hear how Cambly found profits after failing")
L.append(cls(
    "cambly", status="private", rng="below_1b", country="US", city="San Francisco", focus="Consumer & Marketplaces",
    stage="undetermined",
    note="Online English tutoring with native speakers (Y Combinator W14; San Francisco, as the YC row reads). The firm "
         "listed it from 2016 (M.G. Siegler), before the company, 'after failing to raise a Series A', went on to "
         "raise a $15M Series A led by Benchmark and a $40M Series B (TechCrunch, 2023-01-24; Bessemer's own post of "
         "June 2022); no source read names the round GV joined (Google News for Cambly with Google Ventures, seed and "
         "funding; one web search returned only vendor profiles, which disagree between a 2017 Series A and a second "
         "seed and never cite), so the stage is undetermined. Profitable and private; the Series B was reported near $250M in "
         "the YC row: below_1b.",
    rounds=[rnd(None, "Series A", 15000000, "Benchmark", None, TCM, "press"),
            rnd("2022-06", "Series B", 40000000, "Bessemer Venture Partners", None,
                NEWS("cambly", "Our investment in Cambly"), "press")]))

# ---------------------------------------------------------------- carnival-mobile
NZH = NEWS("carnival-mobile", "US investors back Kiwi tech firm")
L.append(cls(
    "carnival-mobile", status="acquired", rng="below_1b", country="US", city="New York", focus="SaaS",
    stage="Seed", stage_src="model", stage_conf="medium", entry_date="2013-09",
    note="Mobile marketing and messaging platform for apps (Carnival Labs, carnival.io), founded in New Zealand in 2008; "
         "by 2013 it had offices in Wellington, Auckland and New York and its CEO was based in New York (NZ Herald, "
         "2013-09-02); placed in New York, where its investors and its acquirer sat. It raised about US$2.4M in "
         "September 2013 from Lerer Ventures, Gary Vaynerchuk, Flybridge, Bowery Capital, Google Ventures, BoxGroup "
         "and angels (NZ Herald), its first institutional round, before the firm's 2014 listing (Kevin Rose); the "
         "story names no series and the amount sits in the 2011-2014 seed band, so it reads Seed at medium "
         "confidence. Sailthru acquired Carnival in April 2016 (Retail TouchPoints headline; the firm's exit line "
         "'Acquired by Sailthru, 2016')." + GRAD_LATER,
    rounds=[rnd("2013-09-02", "round (unnamed)", 2400000, None, True, NZH, "press")]))

# ---------------------------------------------------------------- carrick-therapeutics
CAR_L = ("https://www.carricktherapeutics.com/news-media/press-releases/detail/15/launch-of-carrick-therapeutics-"
         "signals-new-approach-to")
CAR_HQ = ("https://www.carricktherapeutics.com/news-media/press-releases/detail/24/carrick-therapeutics-establishes-"
          "new-headquarters-in")
L.append(cls(
    "carrick-therapeutics", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=CAR_HQ, city="Boston", focus="Healthcare & Bio",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-10",
    note="Oncology drug developer (CDK7 and CDK12/13 inhibitors), headquartered in Boston since the relocation from "
         "Dublin announced 2024-06-05 (the company's release; teams remain in Ireland and the UK). Launched on "
         "2016-10-03 with $95M from ARCH and Woodford (leads), Cambridge Enterprise, Cambridge Innovation Capital, "
         "Evotec, GV (Google Ventures) and Lightstone (the company's release), its first financing and the year the "
         "firm first listed it; the release names no series, so the launch round reads Series A at medium "
         "confidence. No valuation disclosed; below_1b.",
    rounds=[rnd("2016-10-03", "launch financing (unnamed)", 95000000,
                "ARCH Venture Partners; Woodford Investment Management", True, CAR_L, "company")]))

# ---------------------------------------------------------------- carmera
RRC = NEWS("carmera", "builds HD maps for autonomous vehicles in Brooklyn")
L.append(cls(
    "carmera", status="acquired", rng="below_1b", country="US", city="New York", focus="Industrial & Robotics",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=RRC, entry_date="2018",
    note="Street-level and HD maps for autonomous vehicles (Brooklyn, with offices in Seattle and San Francisco; "
         "Toyota's release: 'headquartered in New York City and Seattle'). 'Last year, CARMERA raised Series B "
         "funding of $20 million from GV, formerly Google Ventures' (The Robot Report, 2019-08-19), the year the firm "
         "first listed it; the firm's own posts name nothing earlier and the 2017 raise reported by GeekWire could "
         "not be read (403), so the entry reads Growth at medium confidence. Woven Planet Holdings (Toyota) closed the "
         "acquisition on 2021-08-17 (Toyota's release), as the firm's exit line records.",
    rounds=[rnd("2018", "Series B", 20000000, "GV", True, RRC, "press")]))

# ---------------------------------------------------------------- blue-bottle-coffee
BB12 = "https://www.sec.gov/Archives/edgar/data/1560324/000156032412000001/primary_doc.xml"
BB14 = "https://www.sec.gov/Archives/edgar/data/1560324/000156032414000001/primary_doc.xml"
BB15 = "https://www.sec.gov/Archives/edgar/data/1560324/000156032415000001/primary_doc.xml"
L.append(cls(
    "blue-bottle-coffee", status="acquired", rng="below_1b", country="US", city="Oakland",
    focus="Consumer & Marketplaces", stage="undetermined",
    note="Specialty coffee roaster and cafes (Oakland; its Form D address 2012-2015). The firm listed it from 2013 "
         "(Kevin Rose, David Krane). The company's first filed round is a $19.7M equity raise with first sale on "
         "2012-10-01 (Form D; 37, then 41 investors; directors Tony Conrad and Mike Volpi), then $25.75M in January "
         "2014 and $75M in May 2015 (Form Ds); no source read names GV in a round or names the series (Google News "
         "for Blue Bottle with Google Ventures and the 2012 funding), so the stage is undetermined. Nestle bought a "
         "68% stake in September 2017 (Wikipedia; the firm's exit line 'Acquired by Nestlé, 2017'), and Centurium "
         "Capital bought the global retail business from Nestle in 2026 for about $400M (Wikipedia): acquired.",
    rounds=[rnd("2012-10-01", "equity (unnamed)", 19672975, None, None, BB12, "filing"),
            rnd("2014-01-24", "equity (unnamed)", 25750039, None, None, BB14, "filing"),
            rnd("2015-05-29", "equity (unnamed)", 74958801, None, None, BB15, "filing")]))

# ---------------------------------------------------------------- bugsnag
L.append(cls(
    "bugsnag", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="DevTools & APIs",
    stage="undetermined",
    note="Error monitoring for web, mobile and server apps (San Francisco). The firm listed it from 2018 (Dave "
         "Munichiello), but no source read documents a Bugsnag round (Google News for Bugsnag with raises, funding "
         "round, Series A, Series B and SmartBear returned product news only; EDGAR holds no Form D), so the stage "
         "is undetermined. SmartBear acquired Bugsnag in 2021 (the firm's exit line 'Acquired by SmartBear, 2021').",
    rounds=[]))

# ---------------------------------------------------------------- buoyant
BUO15 = "https://www.sec.gov/Archives/edgar/data/1640131/000164013115000002/primary_doc.xml"
L.append(cls(
    "buoyant", status="private", rng="below_1b", country="US", city="San Francisco", focus="Data Infrastructure",
    stage="undetermined",
    note="Linkerd service mesh for Kubernetes (San Francisco; its 2015 Form D). A $3.5M equity round in 2015 (Form D, "
         "16 investors) and the $10.5M Series A of July 2017 led by Benchmark, without GV (TechCrunch, 2017-07-11); "
         "the firm listed Buoyant from 2019 (Dave Munichiello), so GV came in later, in a round no source read "
         "documents (Google News for Buoyant with Series B, raises and GV; its newsroom; EDGAR holds only the 2015 "
         "Form D), so the stage is undetermined. Still operating (Buoyant Enterprise for Linkerd, 2026).",
    rounds=[rnd("2015-04", "equity (unnamed)", 3499990, None, None, BUO15, "filing"),
            rnd("2017-07-11", "Series A", 10500000, "Benchmark", False,
                NEWS("buoyant", "Buoyant raises $10.5M Series A"), "press")]))

# ---------------------------------------------------------------- caraway-health
CWA = NEWS("caraway-health", "Caraway Secures Series A Funding to Fundamentally Change")
CWS = NEWS("caraway-health", "Caraway, Launches to Tackle College")
L.append(cls(
    "caraway-health", status="acquired", rng="below_1b", country="US", city="New York", focus="Healthcare & Bio",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=CWA, entry_date="2023-06",
    note="Virtual mental, reproductive and physical care for college-age women (New York, the releases' dateline). "
         "Maveron and GV co-led the $16.75M Series A of 2023-06-20 (the company's release), the year the firm first "
         "listed it; the $10.5M seed of July 2022 was led by 7wireVentures and OMERS without GV (the company's "
         "release). Summer Health bought Caraway Health in February 2025 (Endpoints headline, 2025-02-11; the "
         "firm's exit line 'Acquired by Summer Health, 2025'). Not Caraway Therapeutics, the Parkinson's biotech "
         "Merck agreed to buy in 2023.",
    rounds=[rnd("2022-07-26", "Seed", 10500000, "7wireVentures; OMERS Ventures", False, CWS, "company"),
            rnd("2023-06-20", "Series A", 16750000, "Maveron; GV", True, CWA, "company")]))

# ---------------------------------------------------------------- blavity
WBL = W("Blavity")
L.append(cls(
    "blavity", status="private", rng="below_1b", city="Los Angeles", focus="Media, Gaming & Advertising",
    stage="Series A", stage_src="model", stage_conf="medium",
    note="Digital media for Black millennials and the AfroTech conference (Los Angeles; Wikipedia and the 2018 Form D "
         "address). Closed a $1M seed in September 2016, then in July 2018 'raised $6.5 million through GV, Comcast "
         "Ventures, Plexo Capital, and Baron Davis Enterprises' (Wikipedia; the June 2018 Form D with John Lyman as "
         "director gives the prefilled entry date), the year the firm first listed it. No source read names the "
         "2018 series (the Business Journals story could not be opened; Google News for Blavity with Series A "
         "returned the site's own articles); as the first priced round after the named seed and above the seed "
         "band, it reads Series A at medium confidence. Still operating (AfroTech, 2024).",
    rounds=[rnd("2016-09", "Seed", 1000000, None, False, WBL, "press"),
            rnd("2018-07", "round (unnamed)", 6500000, None, True, WBL, "press")]))

# ---------------------------------------------------------------- blue-vision-labs
CBN = NEWS("blue-vision-labs", "Lyft Acquires Blue Vision Labs")
L.append(cls(
    "blue-vision-labs", status="acquired", rng="below_1b", country="GB", country_src="web_verified", country_cite=CBN,
    city="London", focus="AI & Applied AI", stage="undetermined",
    note="Computer-vision localization for collaborative augmented reality ('Based in London', founded 2016; Crunchbase "
         "News). It raised $17M in total from investors including Google Ventures (GV), Accel and Horizons Ventures "
         "before Lyft bought it on 2018-10-23 for about $72M to anchor Lyft Level 5 in the UK (Crunchbase News; the "
         "firm's exit line 'Acquired by Lyft, 2018'). No source read names the round GV joined (Google News for Blue "
         "Vision Labs with GV, Accel and funding returned the acquisition only; its Medium post returned 403), so "
         "the stage is undetermined.",
    rounds=[]))

jl.write("j2", L)
