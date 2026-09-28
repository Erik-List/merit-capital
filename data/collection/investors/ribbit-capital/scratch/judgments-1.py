"""PRO-161 grind, batch 1 (affirm .. good-leap), plus caret on the coordinator's instruction.
Evidence: the judge view (show.py --batch 1), Wikipedia (wikifetch.py), the Google News sweep and nq.py
(NQ_TAG=b1), pages fetched and read (WebFetch), the firm's deal vehicles (SPV) and the EDGAR full-text hits."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV = jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W, jl.NEWS, jl.SPV
FORMD_CITE = jl.FORMD_CITE
VRS = {"valuation_range_source": "web_verified"}
L = []


def FTS(registrant, form, date):
    """The document URL of one filing in the EDGAR full-text hits (sources/edgar/fts-hits.json)."""
    d = json.loads((jl._INV / "sources/edgar/fts-hits.json").read_text())
    m = [f["url"] for r in d["registrants"] if r["registrant"].strip() == registrant
         for f in r["filings"] if f["form"] == form and f["date"] == date]
    if len(m) != 1:
        raise SystemExit(f"FTS({registrant!r}, {form!r}, {date!r}) matched {len(m)}")
    return m[0]


# ---------------------------------------------------------------- pages fetched and read (WebFetch),
# URLs printed by WebSearch or by the sibling rows on disk, each opened before it is cited here
GV_COINBASE = "https://globalventuring.com/blog/2013/05/16/bitcoin-business-gets-5m-backing/"
COALITION_SEED = "https://www.coalitioninc.com/announcements/cyber-insurer-coalition-raises-10-million-to-solve-cyber-risk-for-smbs-2018-feb-28"
COALITION_C = "https://www.coalitioninc.com/announcements/coalition-raises-90m-in-funding-to-build-the-future-of-cyber-insurance"
TC_ACTIVEHOURS_SEED = "https://techcrunch.com/2014/05/21/activehours-raises-seed-financing-to-end-payday-lending/"
TC_ACTIVEHOURS_A = "https://techcrunch.com/2017/01/09/activehours-which-makes-every-day-a-payday-just-raised-22-million-in-series-a-funding/"
CHECKOUT_B = "https://www.checkout.com/newsroom/checkout-triples-valuation-in-series-b"
CHECKOUT_C = "https://www.pymnts.com/news/investment-tracker/2021/checkout-com-closes-450-million-series-c-for-15-billion-valuation/"
CHECKOUT_12B = "https://techcrunch.com/2025/09/26/checkout-coms-new-12b-valuation-is-a-glass-half-full-situation/"
ROI_CROSSRIVER = "https://www.roi-nj.com/2022/03/30/finance/cross-river-raises-620m-3b-in-valuation-to-fund-its-technology-focused-growth-strategy/"
CRYPTONEWS_OFFCHAIN = "https://cryptonews.net/news/ethereum/1648753/"
PARTECH_ALAN = "https://partechpartners.com/news/healthcare-super-app-alan-raises-185m-at-14bn-valuation-to-provide-personalised-healthcare-to-everyone-in-europe"
FORTUNE_BRIDGE = "https://fortune.com/crypto/2024/08/29/bridge-stablecoins-sequoia-ribbit-index-haun-58-million"
KR36_BAICAI = "https://pitchhub.36kr.com/project/2179876379053444"
ALTASSETS_FC = "https://www.altassets.net/private-equity-news/by-news-type/deal-news/accel-leads-37m-series-c-round-for-non-banking-loan-business-funding-circle.html"
PRN_COMPARA = "https://www.prnewswire.com/news-releases/comparaonline-raises-11-million-in-series-b-funding-222347441.html"
LAVCA_COMPARA = "https://www.lavca.org/bamboo-capital-ifc-invest-in-chiles-comparaonline/"
DECAGON_C = "https://decagon.ai/blog/series-c-announcement"
CRUSOE_D = "https://www.crusoe.ai/resources/newsroom/crusoe-closes-series-d-funding"
COINSPH_C = "https://coins.ph/blog/coinsph-series-c-ribbit-capital/"
EIGHTROADS_FBT_C = "https://eightroads.com/en/news/eight-roads-backed-fenbeitong-raises-series-c"
EIGHTROADS_FBT_CPLUS = "https://eightroads.com/en/news/fenbeitong-raises-140m-series-c"
BW_FBT_UNICORN = "https://www.businesswire.com/news/home/20220216006319/en/Fenbeitong-Hits-Unicorn-Status-Raising-%24140M-Series-C-Led-by-DST"
FIGURE_S1A = "https://www.sec.gov/Archives/edgar/data/2064124/000162828025041731/figuretechnologysolutionsi.htm"
AFFIRM_IRA = "https://www.sec.gov/Archives/edgar/data/1820953/000110465920126927/tm2026663d5_ex4-2.htm"
CORA_SITE = "https://www.cora.com.br/"


# ---------------------------------------------------------------- public rows (the cap is the A/B pass's)
L.append(cls("affirm", city="San Francisco", focus="Fintech & Payments",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2019-04",
    note="Buy now, pay later lender (San Francisco). Ribbit's first documented round is Affirm's April 2019 Series F: its AF-F "
         "Ribbit Opportunity III vehicle (Form D, 2019Q2) and Ribbit Capital III both signed the amended investors' rights "
         "agreement filed with the S-1 (exhibit 4.2, " + AFFIRM_IRA + "). Ribbit Capital III is a 2015 fund, so any earlier "
         "fund cheque falls in 2015 or later, when Affirm was past its Series A; the entry is Growth either way. Public since January 2021 "
         "(NASDAQ: AFRM); the market cap is pinned in the A/B pass.",
    rounds=[rnd("2019-04", "Series F", None, None, True, SPV("AF-F"), "filing")]))

L.append(cls("coinbase", status="public", city="San Francisco", city_src="web_verified", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=GV_COINBASE, entry_date="2013-05",
    note="Crypto exchange. Ribbit joined the $5M round of May 2013 led by Union Square Ventures (Global Venturing: USV 'led the "
         "round, and was joined by Ribbit Capital'), which Wikipedia names the Series A; it then joined the $25M round of December "
         "2013 with Andreessen Horowitz and USV (Wikipedia) and, through its CB and CB-D vehicles, the 2015 Series C and the 2017 "
         "Series D. Ribbit held more than 5% before the listing (the 2020 DRS). Public since the April 2021 direct listing (NASDAQ: "
         "COIN); the market cap is pinned in the A/B pass. Remote-first since 2020, with a San Francisco office as its physical "
         "headquarters from 2025 (Wikipedia).",
    rounds=[rnd("2013-05", "Series A", 5000000, "Union Square Ventures", True, GV_COINBASE, "press"),
            rnd("2013-12", "Series B", 25000000, "Andreessen Horowitz", True, W("Coinbase"), "press"),
            rnd("2015-01", "Series C", None, None, True, SPV("CB"), "filing"),
            rnd("2017-08", "Series D", None, None, True, SPV("CB-D"), "filing")]))

L.append(cls("figure", status="public", city="Reno", city_src="web_verified", focus="Fintech & Payments",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018-05", flags=["stage_disputes_band"],
    note="Blockchain-based lender (HELOCs on the Provenance chain). Principal office 100 West Liberty Street, Reno, Nevada (the "
         "2025 S-1/A, " + FIGURE_S1A + "). Ribbit co-led, with DST, the company's first institutional round of May 2018, about $50M "
         "(FinTech Global; the Form D of 2018-05-24 sold $51.1M). The next round was the named $65M Series B of February 2019 "
         "(the company's release, Ribbit participating), and Wikipedia names a 2018 Series A, so the 2018 round is the Series A: "
         "the band's Growth reads the round size, not the round, and is disputed. Ribbit Capital IV held 10.9% before the IPO. "
         "Public on NASDAQ (FIGR) since September 2025; the market cap is pinned in the A/B pass.",
    rounds=[rnd("2018-05", "Series A", 50000000, "DST Global, Ribbit Capital", True, NEWS("figure", "said to raise $50m"), "press"),
            rnd("2019-02", "Series B", 65000000, "RPM Ventures", True, NEWS("figure", "Raises $65 Million in Series B"), "company"),
            rnd("2021-05", "Series D", 200000000, "10T Holdings, Morgan Creek Digital", True, W("Figure Technology Solutions"), "press")]))

L.append(cls("funding-circle", status="public", country="GB", country_src="web_verified", country_cite=W("Funding Circle"),
    city="London", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Funding Circle"), entry_date="2013-10",
    flags=["model_disputes_source"],
    note="Small-business lending marketplace (London). The known country US is a wrong join (the American subsidiary); Funding "
         "Circle is British, as the Accel and USV sibling rows also record. Ribbit joined the $37M round of October 2013 led by "
         "Accel with USV and Index (Wikipedia), which AltAssets names the Series C (" + ALTASSETS_FC + "); USV and Index had "
         "funded the A and B, so Ribbit's entry is Growth. Its FC and FC-GEM vehicles followed. Listed on the London Stock "
         "Exchange since September 2018 (FCH); the market cap is pinned in the A/B pass.",
    rounds=[rnd("2013-10-24", "Series C", 37000000, "Accel Partners", True, ALTASSETS_FC, "press")]))

# ---------------------------------------------------------------- private $1B+ rows
L.append(cls("ajaib", city="Jakarta", city_src="web_verified", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("ajaib", "bags funds from Robinhood investor"), entry_date="2021-03",
    note="Indonesian retail brokerage and investment app, Jakarta (FX News Group). Ribbit led the $65M extension of Ajaib's "
         "Series A in March 2021, which followed a $25M first close in February (KrASIA: 'extended Series A round led by Ribbit "
         "Capital'); the October 2021 $153M Series B made Ajaib a unicorn (Jakarta Globe), the known $1B mark. SBI bought about "
         "20% in August 2026 (FX News Group; $270M per the Forbes headline) with no valuation stated, so no new figure is minted "
         "here; the A/B pass should re-read the mark.",
    rounds=[rnd("2021-02", "Series A", 25000000, None, None, NEWS("ajaib", "bags funds from Robinhood investor"), "press"),
            rnd("2021-03", "Series A extension", 65000000, "Ribbit Capital", True, NEWS("ajaib", "bags funds from Robinhood investor"), "press"),
            rnd("2021-10", "Series B", 153000000, None, None, NEWS("ajaib", "Series B Funding"), "press"),
            rnd("2026-08", "strategic stake (about 20%)", 270000000, "SBI Holdings", None, NEWS("ajaib", "acquires 20% stake"), "press")]))

L.append(cls("alan", status="private", rng="1b_plus", usd=6238100000, val_src="web_verified",
    val_cite=NEWS("alan", "Valuation Climbs"), asof="2026-06-25", val_conf="high",
    country="FR", country_src="web_verified", country_cite=NEWS("alan", "Valuation Climbs"), city="Paris",
    focus="Fintech & Payments", stage="undetermined", flags=["model_disputes_source"], extra=VRS,
    note="French health insurer (Paris). The known 'defunct' is a wrong join: Alan raised EUR 480M led by Prosus at a EUR 5.5B "
         "valuation in June 2026 (trendingtopics), the mark the Coatue sibling row also carries. EUR 5.50B @ ECB 2026-06-25 "
         "(EUR/USD 1.1342) = $6.24B. Ribbit was already an existing investor in the EUR 185M Series D of April 2021 led by Coatue "
         "(Orrick: 'historical investors Index Ventures and Ribbit Capital'; Partech's release, " + PARTECH_ALAN + "), and its AL-D "
         "vehicle bought into that round, but no source names the earlier round Ribbit entered: the Series C coverage of April "
         "2020 (Temasek lead) does not list it, so the stage is undetermined.",
    rounds=[rnd("2020-04", "Series C", None, "Temasek", None, NEWS("alan", "closes €50m Series C"), "press"),
            rnd("2021-04", "Series D", None, "Coatue", True, NEWS("alan", "Orrick Advises"), "press"),
            rnd("2022-05", "Series E", None, None, None, NEWS("alan", "Series E; Valued"), "press"),
            rnd("2026-06", "growth round (EUR 480M)", None, "Prosus", None, NEWS("alan", "Valuation Climbs"), "press")]))

L.append(cls("arbitrum", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified", val_cite=CRYPTONEWS_OFFCHAIN,
    asof="2021-08-31", val_conf="high", country="US", city="New York", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CRYPTONEWS_OFFCHAIN, entry_date="2021-08-31",
    flags=["stale"], extra=VRS,
    note="The row is Offchain Labs, the company that builds Arbitrum (decisions.md D2); Ribbit bought equity in a priced round, so "
         "the stage is read normally and the row takes no token flag. Ribbit is named among the investors in Offchain's $120M "
         "Series B of 31 August 2021 at a $1.2B valuation, after the $20M Series A of April 2021 led by Lightspeed "
         "(cryptonews.net). No later equity round found (news sweep 2026-09-28), so the 2021 mark stands, stale, as on the "
         "Lightspeed sibling row. HQ New York, as that row.",
    rounds=[rnd("2021-04", "Series A", 20000000, "Lightspeed Venture Partners", None, CRYPTONEWS_OFFCHAIN, "press"),
            rnd("2021-08-31", "Series B", 120000000, None, True, CRYPTONEWS_OFFCHAIN, "press")]))

L.append(cls("bharatpe", city="New Delhi", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("bharatpe", "Led By Ribbit Capital"),
    entry_date="2019-08",
    note="Merchant payments and credit, New Delhi (Wikipedia; the Coatue sibling says New Delhi, the Insight sibling Gurugram). "
         "Ribbit co-led, with Steadview, the $50M round of August 2019 as a new investor; the $15.5M Series A of April 2019 had "
         "come from Insight, Sequoia and Beenext (Inc42), so Ribbit's first round is the Series B, a Growth entry. Its BP-E vehicle "
         "joined the $370M Series E led by Tiger Global at $2.85B in August 2021 (Moneycontrol).",
    rounds=[rnd("2019-04", "Series A", 15500000, None, False, NEWS("bharatpe", "Led By Ribbit Capital"), "press"),
            rnd("2019-08", "Series B", 50000000, "Ribbit Capital, Steadview Capital", True, NEWS("bharatpe", "Led By Ribbit Capital"), "press"),
            rnd("2021-08", "Series E", 370000000, "Tiger Global", True, SPV("BP-E"), "filing")]))

L.append(cls("chainalysis", city="New York", city_src="web_verified", focus="Security",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("chainalysis", "added $13m"),
    entry_date="2020-07",
    note="Blockchain analytics and investigations, New York City (Wikipedia). Ribbit came in as a new investor, with Sound "
         "Ventures, in the $13M extension of the Series B in July 2020, joining previous investors Accel, Benchmark, MUFG "
         "and Sozo (FinTech Global); a Growth entry. Focus follows the sibling rows (Security). The known $4.2B mark is the 2021 round; "
         "the siblings carry the $8.6B Series F of May 2022, same band.",
    rounds=[rnd("2020-07", "Series B extension", 13000000, None, True, NEWS("chainalysis", "added $13m"), "press"),
            rnd("2020-11", "Series C", 100000000, None, None, NEWS("chainalysis", "unicorn status"), "press")]))

L.append(cls("checkout", status="private", rng="10b_plus", usd=12000000000, val_src="web_verified", val_cite=CHECKOUT_12B,
    asof="2025-09-26", val_conf="medium", country="GB", country_src="web_verified", country_cite=W("Checkout.com"),
    city="London", focus="Fintech & Payments",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021", extra=VRS,
    note="Payments processor, London (Wikipedia). Ribbit is named an existing investor in the $1B Series D of January 2022 at "
         "$40B (TechCrunch), but not among the investors of the June 2020 Series B (Coatue lead; Insight, DST, Blossom, GIC; the "
         "company's release) or the January 2021 Series C (Tiger lead; PYMNTS), and the $230M Series A of 2019 was the Insight "
         "and DST round: Ribbit's entry falls in 2021, after the Series C, a Growth position. Mark: the company's employee share "
         "buyback at $12B in September 2025 (TechCrunch, priced off a 409A), the figure the Coatue sibling row carries; the $40B "
         "of 2022 is the last primary round, same band.",
    rounds=[rnd("2020-06", "Series B", 150000000, "Coatue", False, CHECKOUT_B, "company"),
            rnd("2021-01", "Series C", 450000000, "Tiger Global", False, CHECKOUT_C, "press"),
            rnd("2022-01", "Series D", 1000000000, None, True, NEWS("checkout", "raises $1B round at $40B"), "press")]))

L.append(cls("clip", city="Mexico City", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020",
    note="Card acceptance and payments, Mexico City (the company's 2024 release). Ribbit's earliest vehicle in Clip is CL-C "
         "(Ribbit Opportunity IV, Form D 2020Q1, coded to the Series C); CL-D joined the $250M Series D of June 2021. No earlier "
         "Ribbit round was found: the May 2019 $100M round coverage names SoftBank and General Atlantic (LatamList), and the firm "
         "first listed Clip in 2022, when the company was past its Series D. The entry reads Growth.",
    rounds=[rnd("2020", "Series C", None, None, True, SPV("CL-C"), "filing"),
            rnd("2021-06", "Series D", 250000000, None, True, SPV("CL-D"), "filing")]))

L.append(cls("coinswitch", status="private", rng="1b_plus", usd=1900000000, val_src="web_verified",
    val_cite=NEWS("coinswitch", "valued at $1.9 bln"), asof="2021-10-06", val_conf="high",
    country="IN", country_src="web_verified", country_cite=NEWS("coinswitch", "raises $15 Mn in Series A round"),
    city="Bangalore", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("coinswitch", "raises $15 Mn in Series A round"),
    entry_date="2021-01", flags=["stale"], extra=VRS,
    note="Indian crypto investment platform, Bengaluru (Entrackr). Ribbit co-led, with Paradigm, the $15M Series A of January "
         "2021, its first Indian crypto deal; Sequoia and Kunal Shah were existing investors (Entrackr). Mark: the $260M Series "
         "C led by Andreessen Horowitz and Coinbase at $1.9B (Reuters, 2021-10-06), aligned with the a16z sibling row; no later "
         "round at or above $1B found, news sweep 2026-09-28, so the mark is stale.",
    rounds=[rnd("2021-01", "Series A", 15000000, "Ribbit Capital, Paradigm", True, NEWS("coinswitch", "raises $15 Mn in Series A round"), "press"),
            rnd("2021-10", "Series C", 260000000, "Andreessen Horowitz, Coinbase Ventures", None, NEWS("coinswitch", "valued at $1.9 bln"), "press")]))

L.append(cls("cred", city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=W("Cred (company)"), entry_date="2018",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("cred", "Series B funding led by Ribbit Capital"), grad_conf="high",
    note="Credit-card rewards and payments, Bengaluru (Wikipedia). Ribbit came in at founding: 'The company closed one of India's "
         "largest seed rounds at 30 million dollars from investors like Sequoia and Ribbit Capital' (Wikipedia), in 2018. The "
         "next round, $120M in August 2019 led by Ribbit, Gemini and Sequoia, is named (YourStory calls it the Series B, "
         "Moneycontrol the Series A), so the seed graduated. Meta's 20% stake for $900M in June 2026 (Wikipedia) prices the "
         "company at $4.5B, the figure the Coatue and General Catalyst siblings carry; the known $6.4B is the 2022 round, same band.",
    rounds=[rnd("2018", "Seed", 30000000, None, True, W("Cred (company)"), "press"),
            rnd("2019-08", "Series B", 120000000, "Ribbit Capital, Gemini Investments, Sequoia Capital", True,
                NEWS("cred", "Series B funding led by Ribbit Capital"), "press")]))

L.append(cls("cross-river-bank", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified", val_cite=ROI_CROSSRIVER,
    asof="2022-03-30", val_conf="medium", country="US", country_src="web_verified", country_cite=W("Cross River Bank"),
    city="Fort Lee", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Cross River Bank"), entry_date="2016-11",
    flags=["model_disputes_source", "stale"], extra=VRS,
    note="Banking-as-a-service lender, Fort Lee, New Jersey (Wikipedia). The known country IL is a wrong join; the a16z and "
         "Battery siblings dispute it the same way. Ribbit joined the $28M growth-equity investment led by Battery with "
         "Andreessen Horowitz, announced 1 November 2016 (Wikipedia), a Growth entry. Mark: CRB Group raised $620M 'at a "
         "valuation of more than $3 billion' in March 2022, co-led by Eldridge and a16z (ROI-NJ), as the siblings carry; the a16z "
         "sibling notes a small 2026 raise without a published figure, so the 2022 mark stands, stale.",
    rounds=[rnd("2016-11", "growth equity", 28000000, "Battery Ventures", True, W("Cross River Bank"), "press"),
            rnd("2022-03", "growth round", 620000000, "Eldridge, Andreessen Horowitz", None, ROI_CROSSRIVER, "press")]))

L.append(cls("crusoe", status="private", rng="10b_plus", usd=30900000000, val_src="web_verified",
    val_cite=NEWS("crusoe", "Series F at a $30.9B"), asof="2026-09-17", val_conf="high",
    country="US", city="Denver", city_src="web_verified", focus="Data Infrastructure",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=CRUSOE_D, entry_date="2024-12", extra=VRS,
    note="AI cloud and data-center builder, datelined Denver in its September 2026 release (the Felicis sibling says Denver, Spark "
         "San Francisco, where the 2024 release was datelined). Ribbit is named in the $600M Series D led by Founders Fund at "
         "$2.8B, closed 12 December 2024 ('new and existing investors, including ... Ribbit Capital'; the company's release), "
         "and is not among the named investors of the 2022 Series C (CoinDesk); the firm first listed Crusoe in 2025, so the "
         "Series D is its entry. Mark: the $3.9B Series F at a $30.9B post-money valuation, 17 September 2026 (the company's "
         "release), with Ribbit participating.",
    rounds=[rnd("2022-04", "Series C", 350000000, "G2 Venture Partners", None,
                NEWS("crusoe", "Flared-Gas Bitcoin Miner Crusoe Energy Raises $350M"), "press"),
            rnd("2024-12-12", "Series D", 600000000, "Founders Fund", True, CRUSOE_D, "company"),
            rnd("2026-09-17", "Series F", 3900000000, "Atreides Management, Mubadala Capital, Valor Equity Partners", True,
                NEWS("crusoe", "Series F at a $30.9B"), "company")]))

L.append(cls("dcg", status="private", rng="10b_plus", usd=10000000000, val_src="web_verified",
    val_cite=NEWS("dcg", "tops $10 billion"), asof="2021-11-01", val_conf="medium",
    country="US", city="Stamford", focus="Crypto & Web3",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021", flags=["stale"], extra=VRS,
    note="Digital Currency Group, Grayscale's parent (Stamford, Connecticut, as the Bain Capital Ventures sibling). Ribbit was "
         "not in the 2015 formation round; it bought in through the 2021 secondary sale led by SoftBank Vision Fund 2 that valued "
         "DCG at $10B (CNBC, 2021-11-01), via its DG-S Bullfrog Opportunity II vehicle ($140.8M sold, Form D 2021Q3): a secondary "
         "entry, Growth. The $10B stands as the last priced event, stale, aligned with the BCV row. DCG's lending unit Genesis "
         "filed for bankruptcy in January 2023 (Axios); DCG itself did not, so the row reads private.",
    rounds=[rnd("2021", "secondary", None, "SoftBank Vision Fund 2", True, SPV("DG-S"), "filing")]))

L.append(cls("decagon", status="private", rng="1b_plus", usd=4500000000, val_src="web_verified",
    val_cite=NEWS("decagon", "Valuation Triples to $4.5 Billion as it Ushers"), asof="2026-01-28", val_conf="high",
    country="US", city="San Francisco", focus="AI & Applied AI",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=DECAGON_C, entry_date="2025-06", extra=VRS,
    note="AI customer-service agents (San Francisco, as the siblings). Ribbit came in as a new investor in the $131M Series C at "
         "$1.5B of June 2025, co-led by Accel and Andreessen Horowitz (the company's post names 'new investors Avra, Forerunner, "
         "and Ribbit Capital'); a Growth entry. Mark: the $250M Series D at $4.5B of January 2026 (the company's release), which "
         "a March 2026 tender repeated.",
    rounds=[rnd("2025-06", "Series C", 131000000, "Accel, Andreessen Horowitz", True, DECAGON_C, "company"),
            rnd("2026-01", "Series D", 250000000, None, None, NEWS("decagon", "Valuation Triples to $4.5 Billion as it Ushers"), "company")]))

L.append(cls("fenbeitong", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=BW_FBT_UNICORN,
    asof="2022-02-16", val_conf="medium", country="CN", country_src="web_verified", country_cite=EIGHTROADS_FBT_C,
    city="Beijing", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=EIGHTROADS_FBT_C, entry_date="2020-03",
    flags=["stale"], extra=VRS,
    note="Corporate expense and spend management, Beijing (Eight Roads). Ribbit co-led, with Eight Roads and Glade Brook, the "
         "$36M Series B+ of March 2020, was an existing investor in the $92.5M Series C of March 2021 led by Tencent and GL "
         "Ventures (Eight Roads), and returned in the $140M Series C+ led by DST in February 2022 through its FBT-C vehicle. That "
         "round made the company a unicorn (the company's release: 'Fenbeitong Hits Unicorn Status'); no figure was published, "
         "so the row carries the $1B floor, stale. The entry is Growth.",
    rounds=[rnd("2020-03", "Series B+", 36000000, "Eight Roads, Ribbit Capital, Glade Brook Capital", True, EIGHTROADS_FBT_C, "press"),
            rnd("2021-03-17", "Series C", 92500000, "Tencent, GL Ventures", True, EIGHTROADS_FBT_C, "press"),
            rnd("2022-02", "Series C+", 140000000, "DST Global", True, EIGHTROADS_FBT_CPLUS, "press")]))

L.append(cls("fireblocks", status="private", rng="1b_plus", usd=8000000000, val_src="web_verified",
    val_cite=NEWS("fireblocks", "Zero to Crypto"), asof="2022-01-27", val_conf="high",
    country="US", country_src="web_verified", country_cite=NEWS("fireblocks", "Raises $133 Million in Series C"),
    city="New York", city_src="web_verified", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("fireblocks", "Raises $133 Million in Series C"),
    entry_date="2021-03", flags=["model_disputes_source", "stale"], extra=VRS,
    note="Digital-asset custody and settlement infrastructure, New York (the release dateline), with R&D in Tel Aviv. The known "
         "country IL reads the founding country; the Coatue and Spark siblings dispute it the same way. Ribbit co-led, with Coatue "
         "and Stripes, the $133M Series C of March 2021; the release lists Paradigm, Galaxy, Swisscom, Tenaya and Cyberstarts as "
         "the previous investors, so Ribbit was new. Mark: the $550M Series E at $8B of 27 January 2022 (the company's post); no "
         "later priced round found (news sweep 2026-09-28), stale.",
    rounds=[rnd("2021-03-18", "Series C", 133000000, "Coatue, Ribbit Capital, Stripes", True,
                NEWS("fireblocks", "Raises $133 Million in Series C"), "company"),
            rnd("2022-01-27", "Series E", 550000000, "D1 Capital Partners, Spark Capital", None, NEWS("fireblocks", "Zero to Crypto"), "company")]))

L.append(cls("gauntlet", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
    val_cite=NEWS("gauntlet", "raises $23.8 million"), asof="2022-03-14", val_conf="high",
    country="US", city="New York", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("gauntlet", "DeFi veteran Gauntlet raises"),
    entry_date="2022-03", flags=["stale"], extra=VRS,
    note="DeFi risk management and vault curation (New York, as the First Round sibling). Ribbit led the $23.8M round at a $1B "
         "valuation of March 2022 (The Block), which Fortune names the Series B; the 2020 $4.3M Series A was Paradigm's and a 2018 "
         "seed preceded it. The $125M Series C from SBI Holdings (June-July 2026) carried no disclosed valuation (Fortune), so the "
         "2022 $1B stands, stale, at the band edge. The First Round sibling reads below_1b; this row holds the cited $1B priced round.",
    rounds=[rnd("2020", "Series A", 4300000, "Paradigm", None, NEWS("gauntlet", "raises $23.8 million"), "press"),
            rnd("2022-03", "Series B", 23800000, "Ribbit Capital", True, NEWS("gauntlet", "DeFi veteran Gauntlet raises"), "press"),
            rnd("2026-07", "Series C", 125000000, "SBI Holdings", None, NEWS("gauntlet", "Gauntlet lands $125m"), "press")]))

L.append(cls("good-leap", status="private", rng="10b_plus", usd=12000000000, val_src="web_verified",
    val_cite=NEWS("good-leap", "GoodLeap closes $800 million"), asof="2021-10-13", val_conf="high",
    country="US", city="Roseville", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined", flags=["stale"], extra=VRS,
    note="GoodLeap (formerly Loanpal), financing for residential solar and home improvements, Roseville, California (Wikipedia). "
         "Mark: the $800M round led by MSD Partners with BDT and Davidson Kempner at a $12B valuation, October 2021 (the company's "
         "release), stale; no later priced round found (news sweep 2026-09-28). Ribbit is not named in that release, and no "
         "source found ties it to a GoodLeap round (Google News queries 2026-09-28), so the stage is undetermined.",
    rounds=[rnd("2021-10-13", "growth round", 800000000, "MSD Partners", None, NEWS("good-leap", "GoodLeap closes $800 million"), "company")]))

# ---------------------------------------------------------------- private below $1B, acquired, other
L.append(cls("alude", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=NEWS("alude", "free real estate platform"), city="São Paulo", focus="Fintech & Payments",
    note="Software for Brazilian real-estate brokers and agencies with embedded rental products (background checks, fire "
         "insurance, capitalization bonds); the site operates (2026). Ribbit backed the $3.3M seed with YC, Global Founders "
         "Capital and MAYA (Contxto, September 2020), the Form D round of 2020-08-07. City as the YC sibling. No round at or above "
         "$1B known. Graduation left for the graduation pass.",
    rounds=[rnd("2020-08", "Seed", 3300000, None, True, NEWS("alude", "free real estate platform"), "press")]))

L.append(cls("arta", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("arta", "Introducing Arta"), city="Mountain View", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined", flags=["model_disputes_source"],
    note="Arta Finance, a digital family office (wealth management), Mountain View, California (the launch release's dateline). "
         "The known country CZ is a wrong join. Ribbit is named with Sequoia India and Coatue among the backers of the more than "
         "$90M raised in stealth and announced in November 2022 (the release; Crunchbase News), but no source names the round, so "
         "the stage is undetermined, as on the Coatue sibling row. Momentum check: no round at or above $1B found, news sweep "
         "2026-09-28.",
    rounds=[rnd("2022-11", "undisclosed rounds in stealth (more than $90M)", 90000000, None, True, NEWS("arta", "Introducing Arta"), "company")]))

L.append(cls("baicai", status="private", rng="below_1b", country="CN", country_src="web_verified", country_cite=KR36_BAICAI,
    city="Tianjin", city_src="web_verified", focus="Consumer & Marketplaces", stage="undetermined",
    note="Baicai is the used-car trading platform Baicai Ershouche (baicai.58.com, now baicaiche.com), run by Tianjin 58 Yunche, "
         "a 58.com affiliate: 36Kr's company page names manager Cong Lin (the Rebels list's 'Lin Cong') and a registered office "
         "in Tianjin, and baicaiche.com carries the Tianjin company name. No funding round naming Ribbit was found (Google News in "
         "English and Chinese, one web search, 2026-09-28), so the stage is undetermined; the platform operates, and no round at "
         "or above $1B is known.",
    rounds=[]))

L.append(cls("balance", status="private", rng="below_1b", country="US", city="New York", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("balance", "nets $25 million"),
    entry_date="2021-08", flags=["model_disputes_source"],
    note="Balance (getbalance.com), B2B payments and net terms for merchants, with offices in New York and Tel Aviv (Calcalist); "
         "New York as the Lightspeed sibling. The known 'public, $4M' is a wrong join to an unrelated listed Balance (Lightspeed "
         "found the same); the company is private. Ribbit led the $25M Series A of August 2021; the earlier $5.5M seed came "
         "through YC, Lightspeed, Stripe and Max Levchin (Calcalist), so the entry is the Series A. Ribbit returned in the $56M "
         "Series B of July 2022 led by Forerunner. Momentum check: no round at or above $1B found, news sweep 2026-09-28. The YC "
         "sibling 'Balance' is a different company.",
    rounds=[rnd("2021", "Seed", 5500000, None, None, NEWS("balance", "nets $25 million"), "press"),
            rnd("2021-08", "Series A", 25000000, "Ribbit Capital", True, NEWS("balance", "nets $25 million"), "press"),
            rnd("2022-07", "Series B", 56000000, "Forerunner", True, NEWS("balance", "PayPal alums"), "press")]))

L.append(cls("bridge", status="acquired", rng="below_1b", country="US", city="San Francisco", focus="Crypto & Web3",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FORTUNE_BRIDGE, entry_date="2024-08",
    flags=["model_disputes_source"],
    note="Stablecoin payments infrastructure (San Francisco). The known country GB is a wrong join, as the Sequoia sibling found. "
         "Ribbit co-led, with Sequoia, the $40M Series A announced in August 2024; Index had backed the seed (Fortune, "
         "" + FORTUNE_BRIDGE + "). Stripe announced the acquisition for about $1.1B in October 2024 (Fortune) and Bridge now "
         "operates as Stripe's crypto unit (Reuters, February 2026), so the row reads acquired.",
    rounds=[rnd("2024-08", "Series A", 40000000, "Sequoia Capital, Ribbit Capital", True, FORTUNE_BRIDGE, "press")]))

L.append(cls("cheddar", status="acquired", rng="below_1b", country="US", city="New York", focus="Media, Gaming & Advertising",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("cheddar", "Tubefilter"), entry_date="2016-09",
    note="Streaming business-news network (New York). Ribbit joined the $10M round of September 2016 led by Lightspeed with "
         "Comcast Ventures (Wikipedia), Cheddar's second financing after about $3.1M in January 2016; Tubefilter names the May "
         "2017 $19M round the Series C, with Lightspeed, Comcast and Ribbit all returning, so Ribbit's round is the Series B, a "
         "Growth entry (the Lightspeed sibling's card reads Series A for its 2016 entry, a label conflict left for review). Altice USA bought Cheddar for $200M in cash, "
         "announced April 2019 and completed in June 2019 (AlleyWatch; Wikipedia), and sold it to Archetype in December 2023.",
    rounds=[rnd("2016-01", "first round (about $3.1M)", 3100000, None, False, W("Cheddar (TV channel)"), "press"),
            rnd("2016-09", "Series B", 10000000, "Lightspeed Venture Partners", True, W("Cheddar (TV channel)"), "press"),
            rnd("2017-05", "Series C", 19000000, "Raine Ventures", True, NEWS("cheddar", "Tubefilter"), "press")]))

L.append(cls("coalition", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=COALITION_SEED, entry_date="2018-02-28",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("coalition", "Series C At $890M"), grad_conf="high",
    flags=["stage_disputes_band"],
    note="Cyber insurance, headquartered in San Francisco (the company's release). Ribbit was in Coalition's first round: 'raised "
         "$10 million in Seed funding from leading technology investors including Vy Capital, Ribbit Capital, Valor Equity "
         "Partners' (the company, 28 February 2018; some press called it a Series A). The band's Growth reads the 2022 Series F "
         "filing, a later round, and is disputed. The named $25M Series B of May 2019 (Crunchbase News) graduates the seed. "
         "Ribbit partner Nick Shalek sits on the board.",
    rounds=[rnd("2018-02-28", "Seed", 10000000, None, True, COALITION_SEED, "company"),
            rnd("2019-05", "Series B", 25000000, None, None, NEWS("coalition", "Series C At $890M"), "press"),
            rnd("2020-05-20", "Series C", 90000000, "Valor Equity Partners", True, COALITION_C, "company")]))

L.append(cls("coins-ph", status="private", rng="below_1b", city="Taguig", city_src="web_verified", focus="Crypto & Web3",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=COINSPH_C, entry_date="2022-05",
    note="Philippine crypto exchange and e-wallet; CoinDesk calls it Manila-based, and it opened its office in Bonifacio Global "
         "City, Taguig, in 2023 (Newsbytes). Former Binance CFO Wei Zhou bought it from Gojek in April 2022 (CoinDesk); Ribbit "
         "then led the $30M Series C of May 2022 (the company's post), its first round here (the firm first listed Coins.ph in "
         "2022): a Growth entry. Momentum check: no round at or above $1B found, news sweep 2026-09-28.",
    rounds=[rnd("2022-05", "Series C", 30000000, "Ribbit Capital", True, COINSPH_C, "company")]))

L.append(cls("comparaonline", status="private", rng="below_1b", country="CL", country_src="web_verified", country_cite=PRN_COMPARA,
    city="Santiago", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=PRN_COMPARA, entry_date="2013-09-04",
    note="Insurance and financial-product comparison for Chile, Colombia and Brazil, Santiago (the release dateline; the firm's "
         "archived label says Brazil, one of its markets). Ribbit led the $11M Series B of 4 September 2013 after Kaszek's Series "
         "A (the company's release), a Growth entry, and returned in the $14M round of September 2017 led by Bamboo Capital and "
         "IFC (LAVCA). The site still serves Chile, Brazil and Colombia.",
    rounds=[rnd("2013-09-04", "Series B", 11000000, "Ribbit Capital", True, PRN_COMPARA, "company"),
            rnd("2017-09", "growth round", 14000000, "Bamboo Capital Partners, IFC", True, LAVCA_COMPARA, "press")]))

L.append(cls("conta-azul", rng="below_1b", city="Joinville", focus="Fintech & Payments",
    grad="graduated", grad_src="formd", grad_cite=FORMD_CITE("conta-azul", 2), grad_conf="high",
    note="Cloud accounting and ERP for Brazilian small businesses (Joinville). Visma agreed to buy Conta Azul in August 2025 "
         "(LatamList, pending CADE) and now presents it as part of Visma (Visma's founder story, January 2026), so the known "
         "'acquired' stands. The seed graduates on the company's Form D sequence: the $9.3M round of December 2014 is more than "
         "twice the $3.45M entry. Ribbit's Bets page already listed ContaAzul on 19 December 2012 (archive capture), before the "
         "2013 filing the band anchors on, so the entry may be the September 2012 round ($2.76M Form D); a review of the entry "
         "date is suggested.",
    rounds=[rnd("2012-09-10", "Form D round", 2764972, None, None, FORMD_CITE("conta-azul", 0), "filing"),
            rnd("2013-09-23", "Form D round", 3449531, None, True, FORMD_CITE("conta-azul", 1), "filing"),
            rnd("2014-12-05", "Form D round", 9304569, None, None, FORMD_CITE("conta-azul", 2), "filing")]))

L.append(cls("cora", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=NEWS("cora", "Brazil’s Cora raises $10M"), city="São Paulo", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("cora", "Brazil’s Cora raises $10M"),
    entry_date="2019-12", grad="graduated", grad_src="web_verified", grad_cite=NEWS("cora", "raises $26.7M"), grad_conf="high",
    flags=["model_disputes_source", "stage_disputes_band"],
    note="Digital bank for Brazilian small businesses, São Paulo (the company's site, " + CORA_SITE + "). The known country CA "
         "is a wrong join. Ribbit co-led, with Kaszek, Cora's first round, $10M, announced December 2019 (LatamList; the Form D "
         "sold $10.3M from 2019-09-13); the next round, the $26.7M of April 2021 that Ribbit led, is named the Series A "
         "(LatamList), so the first round is the seed and it graduated. The band's Growth reads the August 2021 Series B filing, "
         "a later round, and is disputed. Momentum check: no round at or above $1B found, news sweep 2026-09-28. The YC sibling "
         "'Cora' is a different company.",
    rounds=[rnd("2019-12", "Seed", 10000000, "Kaszek, Ribbit Capital", True, NEWS("cora", "Brazil’s Cora raises $10M"), "press"),
            rnd("2021-04", "Series A", 26700000, "Ribbit Capital", True, NEWS("cora", "raises $26.7M"), "press")]))

L.append(cls("credit-karma", status="acquired", rng="below_1b", city="Oakland", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Credit Karma"), entry_date="2013",
    note="Consumer credit scores and financial-product marketplace. Ribbit co-led, with Susquehanna Growth Equity, the $30M "
         "Series B of 2013 (Wikipedia), after QED's $2.5M Series A of 2009, a Growth entry; its CK-CS vehicle bought common "
         "stock in a 2019 secondary. Intuit acquired Credit Karma for about $7.1B in December 2020, and the company moved its "
         "headquarters from San Francisco to Oakland that month (Wikipedia; the Felicis sibling says San Francisco).",
    rounds=[rnd("2009-11", "Series A", 2500000, "QED Investors", False, W("Credit Karma"), "press"),
            rnd("2013", "Series B", 30000000, "Ribbit Capital, Susquehanna Growth Equity", True, W("Credit Karma"), "press"),
            rnd("2019", "secondary (common)", None, None, True, SPV("CK-CS"), "filing")]))

L.append(cls("crossmint", status="private", rng="below_1b", city="Orlando", city_src="formd_address", focus="Crypto & Web3",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2025-03",
    note="Blockchain and stablecoin developer platform (the founders are Spanish; the Form D gives an Orlando, Florida address). "
         "Ribbit led the $23.6M announced 18 March 2025 (The Block), which Fortune describes as the seed, Series A and strategic "
         "rounds together; Ribbit's lead is the Series A, as the band on the July 2025 Form D also reads. A $18.1M Form D of "
         "October 2022 is the earlier round. Momentum check: no round at or above $1B found, news sweep 2026-09-28.",
    rounds=[rnd("2022-10", "Form D round", 18147905, None, None, FORMD_CITE("crossmint", 1), "filing"),
            rnd("2025-03", "Series A (announced with the seed and strategic rounds)", 23600000, "Ribbit Capital", True,
                NEWS("crossmint", "Ribbit Capital leads"), "press")]))

L.append(cls("daffy", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("daffy", "Finovate"), entry_date="2022-02",
    note="Donor-advised fund app, San Francisco (Finovate). Ribbit led the $17.1M Series A announced in February 2022, with XYZ "
         "Capital and Coinbase Ventures (Finovate); no earlier round naming Ribbit was found, so the entry reads the Series A "
         "(confidence medium, the company launched in September 2021). Still operating (2026 releases). Momentum check: "
         "no round at or above $1B found, news sweep 2026-09-28.",
    rounds=[rnd("2022-02", "Series A", 17100000, "Ribbit Capital", True, NEWS("daffy", "Finovate"), "press")]))

L.append(cls("dv01", status="acquired", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("dv01", "Closes $5.5M Series A"),
    entry_date="2017-09-13",
    note="Data and analytics for lending and structured-finance markets, New York (the release dateline). Ribbit joined the $5.5M "
         "Series A of 13 September 2017 led by OCA Ventures; the release names Leucadia and Pivot as the existing investors, so "
         "Ribbit was new. Fitch Group agreed in September 2022 to take a majority stake, expected to close that quarter "
         "(HousingWire), and dv01 now runs inside Fitch (its founder moved to a Fitch role in August 2026), so the row reads acquired.",
    rounds=[rnd("2017-09-13", "Series A", 5500000, "OCA Ventures", True, NEWS("dv01", "Closes $5.5M Series A"), "company")]))

L.append(cls("earnin", status="private", rng="below_1b", city="Palo Alto", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_ACTIVEHOURS_SEED, entry_date="2014-05",
    grad="graduated", grad_src="web_verified", grad_cite=TC_ACTIVEHOURS_A, grad_conf="high",
    note="Earned-wage access, formerly Activehours, Palo Alto (TechCrunch 2014 and 2017; the Coatue and Felicis siblings say "
         "Mountain View). 'Financing ... was led by Ribbit Capital ... and the early stage venture firm Felicis Ventures' "
         "(TechCrunch, 21 May 2014), the seed. The $22M Series A of January 2017 led by Matrix, with Ribbit, graduates it "
         "(TechCrunch). Later rounds: $39M led by Andreessen Horowitz (2017) and the $125M Series C led by DST (December 2018).",
    rounds=[rnd("2014-05", "Seed", None, "Ribbit Capital, Felicis Ventures", True, TC_ACTIVEHOURS_SEED, "press"),
            rnd("2017-01", "Series A", 22000000, "Matrix Partners", True, TC_ACTIVEHOURS_A, "press")]))

L.append(cls("fi", status="private", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=NEWS("fi", "Former Google Pay execs raise"), city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("fi", "Former Google Pay execs raise"),
    entry_date="2020-01", grad="graduated", grad_src="web_verified", grad_cite=NEWS("fi", "valuation jumps 3X"), grad_conf="high",
    note="Fi (epiFi), a neobank app, Bengaluru (Entrackr). 'Sequoia Capital, Ribbit Capital, and Hillhouse Capital led the round': "
         "the $13.2M seed of January 2020 (Entrackr). The June 2021 Series A at $160M graduates it (Entrackr); B Capital led the "
         "$50M Series B in October 2021 at about $325M. In 2026 Fi wound down its consumer banking services and pivoted to AI "
         "software for enterprises, still operating (TechCrunch, March 2026), so private. Momentum check: no round at "
         "or above $1B found, news sweep 2026-09-28.",
    rounds=[rnd("2020-01", "Seed", 13200000, "Sequoia Capital, Ribbit Capital, Hillhouse Capital", True,
                NEWS("fi", "Former Google Pay execs raise"), "press"),
            rnd("2021-06", "Series A", 12000000, None, None, NEWS("fi", "valuation jumps 3X"), "press"),
            rnd("2021-10", "Series B", 50000000, "B Capital", None, NEWS("fi", "B Capital leads"), "press")]))

L.append(cls("forma", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("forma", "Twic rebrands"), entry_date="2022-03",
    note="Flexible employee benefits platform (formerly Twic), San Francisco (the release dateline). Ribbit led the $40M Series B "
         "of 8 March 2022, joining existing investors Emergence, Designer Fund, Upside and AngelPad (SiliconANGLE); a new investor "
         "at the B, a Growth entry. No round at or above $1B known.",
    rounds=[rnd("2022-03-08", "Series B", 40000000, "Ribbit Capital", True, NEWS("forma", "Twic rebrands"), "press")]))

L.append(cls("genesis-digital-assets", status="acquired", rng="below_1b", country="US", country_src="web_verified",
    country_cite=NEWS("genesis-digital-assets", "techtimes"), focus="Crypto & Web3",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-09", flags=["city_unknown"],
    note="Bitcoin miner founded in 2013 as Genesis Mining, with sites in the Carolinas, Texas and Sweden. Ribbit is named in the "
         "$431M round led by Paradigm of September 2021 (CoinDesk), which followed a $125M equity raise in July 2021; an "
         "eight-year-old miner raising at that scale, the round carries no letter and reads Growth. AiOnX closed the purchase of a 77% stake and all 15 facilities "
         "for $500M in June 2026 (Tech Times, 'a US-based Bitcoin mining operator'), so the row reads acquired. No source places "
         "a headquarters city.",
    rounds=[rnd("2021-07", "equity round", 125000000, None, None, NEWS("genesis-digital-assets", "Genesis Digital Assets Raises $431M"), "press"),
            rnd("2021-09", "equity round", 431000000, "Paradigm", True, NEWS("genesis-digital-assets", "Genesis Digital Assets Raises $431M"), "press")]))

L.append(cls("gigs", status="private", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
    note="Mobile-network-as-a-service APIs for companies ('MVNO in a box', TechCrunch), San Francisco (the Form D). Ribbit led the "
         "$73M Series B of December 2024 (Wikipedia), the band's Growth entry. Momentum check: no round at or above $1B found, "
         "news sweep 2026-09-28 (2026 items are partnerships).",
    rounds=[rnd("2024-12", "Series B", 73000000, "Ribbit Capital", True, W("Gigs"), "press")]))

L.append(cls("good-driver", status="private", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="Fintech & Payments", stage="undetermined",
    note="Good Driver Club (formerly Good Driver Mutuality), a membership cost-sharing alternative to collision and comprehensive "
         "cover founded by William Tu, datelined San Francisco (newswire, April 2026). The firm's archived listing (2022-2025) "
         "linked Baixing Chelian, a Chinese car-insurance telematics company, for the same row, so Ribbit's money may have gone "
         "into that predecessor. No round naming Ribbit was found (Google News in English and Chinese, one web search, "
         "2026-09-28), so the stage is undetermined. Momentum check: no round at or above $1B found, same searches.",
    rounds=[]))

# ---------------------------------------------------------------- Caret (batch 3's row, recorded here on the coordinator's
# instruction with the EDGAR full-text evidence; flagged for Erik: units in a listed REIT's subsidiary)
SAFE_8K = FTS("Safehold Inc.", "8-K", "2022-02-15")
L.append(cls("caret", status="private", rng="1b_plus", usd=1750000000, val_src="web_verified", val_cite=SAFE_8K,
    asof="2022-02", val_conf="high", country="US", city="New York", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=SAFE_8K, entry_date="2022-02",
    flags=["stale"], extra=VRS,
    note="Caret Ventures LLC, the Safehold subsidiary that holds the capital-appreciation interest in Safehold's ground leases "
         "(New York). Safehold's 8-K of 2022-02-15 reports a sale of Caret Units 'implying a total Caret Unit valuation of $1.75 "
         "billion', bought by investors 'including Ribbit Capital, Fifth Wall, Zigg Capital'; a priced placement into a private "
         "subsidiary, so the entry is Growth and the row reads private at $1.75B (the Waymo reading of a subsidiary that sells "
         "priced units to outside investors), stale. Membership is flagged for Erik: these are units in a listed REIT's "
         "subsidiary, which the firm listed 2022-2024.",
    rounds=[rnd("2022-02", "Caret Units placement", None, None, True, SAFE_8K, "filing")]))

jl.write("batch-001", L)
