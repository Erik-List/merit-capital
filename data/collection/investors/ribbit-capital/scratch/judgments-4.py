"""PRO-161 grind, batch 4 (44 member rows; `sea` is not_member and skipped).
Evidence: the judge view (show.py), Wikipedia (wikifetch.py), the Google News sweep and nq.py (NQ_TAG=b4),
pages fetched and read with WebFetch (URLs below were printed by a tool run in this session and read),
and 15 WebSearch calls. Run: NQ_TAG=b4 python3 judgments-4.py"""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV = jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W, jl.NEWS, jl.SPV
L = []
TODAY = "2026-09-28"


def momentum(cite):
    """The momentum-slice web check recorded on a below_1b private row (COLLECTION.md s6)."""
    return {"valuation_range_source": "web_verified", "valuation_asof": TODAY, "valuation_citation": cite}


VAL = {"valuation_range_source": "web_verified"}
MOM = "Momentum check 2026-09-28 (Google News on the name with Ribbit and round words): "

# Pages fetched and read in this session (each URL was printed by WebSearch or a decode, then read).
MS_ETHENA = ("https://www.marketscreener.com/quote/cryptocurrency/BITCOIN-BTC-USD-45553945/news/"
             "What-is-Ethena-the-stablecoin-issuer-now-partnering-with-BlackRock-48034206/")
BLOCK_ETHENA = "https://www.theblock.co/post/342955/ethena-100-million-usd-private-ena-token-sale-new-chain-institutional-product"
IQ_ETHENA = "https://iq.wiki/wiki/guy-young"
TC_FUZE = ("https://techcrunch.com/2012/09/27/fuze-network-a-payments-company-focused-on-serving-the-unbanked-"
           "under-banked-raises-2-5-million/")
PRN_HIQ = ("https://www.prnewswire.com/news-releases/health-iq-secures-346-million-in-series-c-funding-led-by-"
           "andreessen-horowitz-300556289.html")
CFI_MESO = ("https://www.crowdfundinsider.com/2024/02/221751-former-paypal-and-venmo-professionals-introduce-meso-"
            "to-link-cryptocurrency-wallets-with-banking-accounts/")
MOONPAY_MESO = "https://www.moonpay.com/newsroom/meso-acquisition"
FTG_MONZO = "https://fintech.global/2024/02/20/monzo-eyes-4bn-valuation-in-landmark-funding-round/"
FTC_NYDIG = "https://fintech.io/articles/fintech-collective-leads-50m-equity-round-in-nydig"
TECHEU_PARASUT = "https://tech.eu/2016/11/24/parasut-series-b/"
RISK_QOG = "https://www.qognitiveai.com/papers/RiskNet12-2023.pdf"
MARTECH_RHI = ("https://martechseries.com/sales-marketing/crm/thanx-receives-strategic-investment-from-rhi-group-"
               "m33-growth-and-ribbit-capital/")
M33_RHI = "https://www.m33growth.com/rhi-group-316811"
PEHUB_RHI = "https://www.pehub.com/m33-growth-backs-rhi-group/"
PRN_SEALANCE = ("https://www.prnewswire.com/news-releases/sealance-emerges-from-stealth-with-seed-funding-from-"
                "galaxy-ribbit-capital-among-other-top-investors-301656490.html")
BLOCK_SLINGSHOT_A = ("https://www.theblock.co/post/127009/defi-trading-platform-slingshot-raises-15-million-in-"
                     "series-a-led-by-ribbit-capital")
COVERAGER_SOFIA = "https://coverager.com/health-and-technology-startup-sofia-announces-series-a-investment/"
FTG_SOFIA = "https://fintech.global/2020/11/23/sofia-said-to-close-19m-series-a-round-led-by-index-venutres/"
SC_SLING = "https://siliconcanals.com/sling-money-series-a-union-square-ventures/"

# ---------------------------------------------------------------- crypto and protocol rows (decisions.md D2)
L.append(cls("diem", status="defunct", rng="below_1b", country="US", city="Washington", city_src="web_verified",
    focus="Crypto & Web3", stage="undetermined", grad="undetermined", flags=["token_funded"],
    note="The Libra Association (renamed Diem in December 2020), the payments consortium Facebook launched in June "
         "2019; Wikipedia lists Ribbit Capital among the association's members, and each founding investor committed "
         "$10 million (Banking Dive). Ribbit's position is that founding-member Libra Investment Token stake: no priced "
         "equity round exists, so the stage and the graduation read undetermined with flag token_funded (decisions.md "
         "D2). The a16z, Thrive and USV rows label the same stake Growth; stage is not a column rule 10 binds. The "
         "association moved its operating headquarters from Geneva to Washington (Wikipedia), wound down in January "
         "2022 and sold its assets to Silvergate for about $182M (" + NEWS("diem", "Diem to end crypto project") + "): "
         "defunct, below $1B, aligned with the three sibling rows. Wikipedia: " + W("Diem (digital currency)") + ".",
    rounds=[rnd("2019-06", "Libra Association founding membership (Libra Investment Token)", 10000000, None, True,
                NEWS("diem", "Diem to end crypto project"), "press")]))

L.append(cls("ethena-labs", status="private", rng="below_1b", country="PT", country_src="web_verified",
    country_cite=MS_ETHENA, city="Lisbon", city_src="web_verified", focus="Crypto & Web3", stage="undetermined",
    extra=momentum(BLOCK_ETHENA),
    note="Ethena Labs, issuer of the USDe synthetic dollar (founded 2023 by Guy Young; 'a Lisbon-based decentralized "
         "stablecoin issuer', MarketScreener 2024). Under decisions.md D2 the row is the issuing organisation. The "
         "record names Ethena's $6M seed of July 2023 (Dragonfly, Arthur Hayes; IQ.wiki), the $14M strategic round of "
         "February 2024 at a $300M valuation co-led by Dragonfly and Maelstrom, and the $100M private ENA token sale of "
         "December 2024 (Franklin Templeton, Polychain, Pantera, Dragonfly, F-Prime; The Block). None of those sources "
         "names Ribbit, so neither the round nor the instrument of Ribbit's entry is on record: stage undetermined (no "
         "token_funded flag, since no source shows a Ribbit token purchase). " + MOM + "the last priced equity mark "
         "is $300M (February 2024); ENA token prices are not a priced round (Rule A), so below $1B. Felicis's "
         "'Ethena' row is a different company (a 2021 New York compliance-training SaaS).",
    rounds=[rnd("2023-07", "Seed", 6000000, "Dragonfly", None, IQ_ETHENA, "press"),
            rnd("2024-02", "strategic round at $300M", 14000000, "Dragonfly, Maelstrom", None, BLOCK_ETHENA, "press"),
            rnd("2024-12", "private ENA token sale", 100000000, None, False, BLOCK_ETHENA, "press")]))

L.append(cls("farcaster", status="acquired", rng="below_1b", country="US", city="Los Angeles", focus="Crypto & Web3",
    stage="undetermined",
    note="Farcaster, the decentralized social protocol of Merkle Manufactory (Los Angeles, as the sibling rows). The "
         "record names two rounds: the $30M seed of 2022 led by a16z and the $150M Series A of May 2024 led by "
         "Paradigm with a16z, Haun, USV, Variant and Standard Crypto (" + NEWS("farcaster", "Degen token surges") + "); "
         "neither names Ribbit, and no source read ties Ribbit to a round, so the stage stays undetermined. Merkle "
         "Manufactory sold Farcaster to Neynar in January 2026 and returned the $180M it had raised to investors ("
         + NEWS("farcaster", "Billion-Dollar Dreams Fade") + "): acquired, below $1B, aligned with the a16z and USV "
         "rows (First Round's row still reads private).",
    rounds=[rnd("2022-07", "Seed", 30000000, "a16z", None, NEWS("farcaster", "Billion-Dollar Dreams Fade"), "press"),
            rnd("2024-05-21", "Series A", 150000000, "Paradigm", False, NEWS("farcaster", "Degen token surges"), "press")]))

L.append(cls("ftx", status="defunct", rng="below_1b", country="BS", country_src="web_verified", country_cite=W("FTX"),
    city="Nassau", focus="Crypto & Web3", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("ftx", "FTX Trading Ltd. Closes"), entry_date="2021-07",
    note="FTX Trading, the crypto exchange (incorporated in Antigua and Barbuda, headquartered in the Bahamas since "
         "September 2021; Wikipedia). The company's release for the $900M Series B of 20 July 2021 at $18B names Ribbit "
         "Capital among its investors; Ribbit also joined the $420.69M round of October 2021 at $25B (The Block). FTX "
         "had no earlier round of that kind open to Ribbit on record, so the entry is the Series B: Growth. Chapter 11 "
         "from 11 November 2022: defunct under the bankruptcy ruling, aligned with the IVP, Lightspeed and Sequoia rows "
         "(Lux's FTX row is unresolved).",
    rounds=[rnd("2021-07-20", "Series B", 900000000, None, True, NEWS("ftx", "FTX Trading Ltd. Closes"), "company"),
            rnd("2021-10-21", "unnamed round at $25B", 420690000, None, True, NEWS("ftx", "FTX raises $420 million"),
                "press")]))

L.append(cls("futureswap", status="unknown", rng="below_1b", country="US", focus="Crypto & Web3", stage="undetermined",
    entry_date="2021-10", flags=["city_unknown"],
    note="Futureswap, a decentralized futures exchange, 'US-headquartered' (Global Venturing). Ribbit, Framework "
         "Ventures, True Ventures and Placeholder each put in $2M to co-lead its $12M round of October 2021; the "
         "company had raised $1.6M before, including $400,000 from Framework in March 2020 (" +
         NEWS("futureswap", "Daily Deal Round Up: October 13") + "). No source names that round's series or says "
         "whether it bought equity or FST tokens, so the stage stays undetermined. Status unknown: futureswap.com now "
         "serves an unrelated crypto-casino review site (read 2026-09-28) and no shutdown or sale report was found; the "
         "firm listed Futureswap on its Our Bets pages 2022-2025. No city on record.",
    rounds=[rnd("2020-03", "early funding ($1.6M in total)", 1600000, "Framework Ventures", False,
                NEWS("futureswap", "Daily Deal Round Up: October 13"), "press"),
            rnd("2021-10", "unnamed round", 12000000, "Ribbit Capital, Framework Ventures, True Ventures, Placeholder",
                True, NEWS("futureswap", "Daily Deal Round Up: October 13"), "press")]))

L.append(cls("helium", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified",
    val_cite=NEWS("helium", "Helium changes name to Nova Labs"), asof="2022-03-30", country="US", city="San Francisco",
    focus="Crypto & Web3", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("helium", "Helium changes name to Nova Labs"), entry_date="2022-03", flags=["stale"], extra=VAL,
    note="The Helium network; under decisions.md D2 the row is its developer, Nova Labs (formerly Helium Inc., San "
         "Francisco). Ribbit Capital is named in the $200M Series D of March 2022 at a $1.2B valuation led by Tiger "
         "Global and a16z (SiliconANGLE), a priced equity round, so the row is staged normally: Growth. Medium "
         "confidence: the investor list of the $111M investment of August 2021 (a16z) could not be read, and an earlier "
         "Ribbit round would still be past Series A. The $1.2B mark is older than 24 months (stale); Nova Labs sold its "
         "Helium Mobile consumer plan business to Nobile Mobile in June 2026 at an undisclosed price (Wikipedia: " +
         W("Helium Network") + "), which is not a priced event. YC's 'Helium' row is a different company "
         "(tryhelium.com).",
    rounds=[rnd("2021-08", "$111M investment joined by a16z", 111000000, "Andreessen Horowitz", None,
                NEWS("helium", "Andreessen Horowitz Joins $111M"), "press"),
            rnd("2022-03-30", "Series D", 200000000, "Tiger Global, Andreessen Horowitz", True,
                NEWS("helium", "Helium changes name to Nova Labs"), "press")]))

L.append(cls("lighter", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
    val_cite=NEWS("lighter", "protocol Lighter - Fortune"), asof="2025-11-11", country="US", focus="Crypto & Web3",
    stage="undetermined", entry_date="2025-11", flags=["city_unknown"], extra=VAL,
    note="Lighter, a perpetuals DEX and Ethereum layer 2 developed by 'Florida-based Elliot Technologies' (DL News); "
         "under decisions.md D2 the row is that company. Founders Fund and Ribbit co-led its $68M round of 11 November "
         "2025, equity plus token warrants, at about $1.5B (Fortune; Wilson Sonsini: $1.5B fully diluted); Ribbit is "
         "not named in the $21M round of 2024 led by Haun Ventures and Craft Ventures. The November round is a priced "
         "equity round, but no source gives its series and the company had one earlier round, so the label could be "
         "Series A or B: stage undetermined. The LIT token's fully diluted value of about $2.5B after the December 2025 "
         "airdrop (" + NEWS("lighter", "Lighter airdrop pushes") + ") is a token value, not a priced round. City left "
         "unknown: Coatue's row reads New York, DL News says Florida. a16z's row still reads below $1B.",
    rounds=[rnd("2024", "unnamed round", 21000000, "Haun Ventures, Craft Ventures", False,
                NEWS("lighter", "protocol Lighter - Fortune"), "press"),
            rnd("2025-11-11", "unnamed round (equity and token warrants)", 68000000, "Founders Fund, Ribbit Capital", True,
                NEWS("lighter", "protocol Lighter - Fortune"), "press")]))

L.append(cls("lightning-labs", status="private", rng="below_1b", country="US", city="San Francisco",
    city_src="web_verified", focus="Crypto & Web3", stage="Series A", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("lightning-labs", "Lightning Labs raises $10M Series A, launches"), entry_date="2020-02",
    extra=momentum(NEWS("lightning-labs", "Lightning Labs Raises $70M")),
    note="Lightning Labs, bitcoin Lightning Network infrastructure (San Francisco, The Block). Ribbit participated in "
         "the $10M Series A of February 2020 led by Craft Ventures, with RRE Ventures and Slow Ventures. Medium "
         "confidence: the 2018 seed's investor list (CNBC: Jack Dorsey among the backers) could not be read. The $70M "
         "Series B of April 2022 (Valor, Brevan Howard) followed. " + MOM + "no priced round at or above $1B found.",
    rounds=[rnd("2020-02-05", "Series A", 10000000, "Craft Ventures", True,
                NEWS("lightning-labs", "Lightning Labs raises $10M Series A, launches"), "press"),
            rnd("2022-04-05", "Series B", 70000000, None, None, NEWS("lightning-labs", "Lightning Labs Raises $70M"),
                "press")]))

L.append(cls("m0", status="private", rng="below_1b", country="US", focus="Crypto & Web3", stage="Growth",
    stage_src="web_verified", stage_conf="high", stage_cite=NEWS("m0", "Exclusive: Crypto startup M0"),
    entry_date="2025-08", flags=["city_unknown"],
    extra={**momentum(NEWS("m0", "Exclusive: Crypto startup M0")), "hq_country_confidence": "low"},
    note="M0 (M^0), stablecoin issuance infrastructure (the site's legal entity is the M0 Foundation; under decisions.md "
         "D2 the row is that organisation). Polychain and Ribbit co-led the $40M Series B of August 2025, equity plus "
         "locked tokens, Ribbit as a new investor (Fortune); the $22.5M seed of 2023 was led by Pantera and the $35M "
         "Series A of June 2024 by Bain Capital Crypto, with no Ribbit in the Series A list (The Block). Entry: the "
         "Series B, Growth. No source read places the company: the country is the model's reading at low confidence "
         "and the city is unknown. " + MOM + "the Series B valuation was not disclosed and no round at or above $1B "
         "was found.",
    rounds=[rnd("2023", "Seed", 22500000, "Pantera Capital", None,
                NEWS("m0", "Bain Capital Crypto leads $35 million Series A for stablecoin minting"), "press"),
            rnd("2024-06-05", "Series A", 35000000, "Bain Capital Crypto", False,
                NEWS("m0", "Bain Capital Crypto leads $35 million Series A for stablecoin minting"), "press"),
            rnd("2025-08-28", "Series B", 40000000, "Polychain Capital, Ribbit Capital", True,
                NEWS("m0", "Exclusive: Crypto startup M0"), "press")]))

L.append(cls("meso", status="acquired", rng="below_1b", country="US", focus="Crypto & Web3", stage="Seed",
    stage_src="web_verified", stage_conf="high", stage_cite=CFI_MESO, entry_date="2024-02", flags=["city_unknown"],
    note="Meso, crypto on-ramp payment infrastructure founded by ex-PayPal, Braintree and Venmo engineers Ben Mills and "
         "Ali Aghareza. Solana Ventures and Ribbit co-led its $9.5M seed of February 2024 with Canonical Crypto and 6th "
         "Man Ventures (Crowdfund Insider). MoonPay announced its acquisition of Meso in September 2025, the founders "
         "joining MoonPay as CTO and product lead (" + MOONPAY_MESO + "): acquired, below $1B. No later round was "
         "found before the sale. Graduation left for the graduation pass. No city on record.",
    rounds=[rnd("2024-02-21", "Seed", 9500000, "Solana Ventures, Ribbit Capital", True, CFI_MESO, "press")]))

L.append(cls("nydig", status="private", rng="1b_plus", usd=7000000000, val_src="web_verified",
    val_cite=NEWS("nydig", "NYDIG Announces $1 Billion Funding Round"), asof="2021-12-14", country="US",
    city="New York", city_src="web_verified", focus="Crypto & Web3", stage="undetermined", entry_date="2020-10",
    flags=["stale"], extra=VAL,
    note="NYDIG, bitcoin custody and financial services ('New York-based', FinTech Collective). Ribbit joined the $50M "
         "equity round of October 2020 led by FinTech Collective, with Bessemer, Starr and Stone Ridge, which brought "
         "NYDIG's equity raised to $100M. That round carries no series name and no source says whether Ribbit held "
         "shares before it, so the stage stays undetermined. Ribbit is not named in the $1B round of December 2021 led "
         "by WestCap, which valued NYDIG at more than $7B (the company's release); that mark is older than 24 months "
         "(stale) and no later priced round was found.",
    rounds=[rnd("2020-10-13", "equity round", 50000000, "FinTech Collective", True, FTC_NYDIG, "press"),
            rnd("2021-12-14", "growth equity round at more than $7B", 1000000000, "WestCap", False,
                NEWS("nydig", "NYDIG Announces $1 Billion Funding Round"), "company")]))

L.append(cls("osmosis", status="private", rng="below_1b", country="SG", country_src="web_verified",
    country_cite=ARCH("osmosis"), city="Singapore", focus="Crypto & Web3", stage="undetermined",
    extra=momentum(NEWS("osmosis", "Osmosis Closes $21M Token Sale to Make")),
    note="Osmosis, the Cosmos DEX (the firm's Our Bets pages 2022-2025 link app.osmosis.zone with the country label "
         "Singapore). Under decisions.md D2 the row is the issuing organisation, the Osmosis Foundation, whose $21M OSMO "
         "token sale of October 2021 was led by Paradigm with Robot Ventures, Nascent, Ethereal, Figment and Do Kwon "
         "(the release is datelined Tortola). Ribbit is not named there and no source read names how or when Ribbit "
         "entered, so the stage stays undetermined (no token_funded flag without a recorded Ribbit purchase). "
         + MOM + "no priced round at or above $1B exists; the only financing on record is the token sale. The Felicis "
         "and YC 'Osmosis' rows are different companies.",
    rounds=[rnd("2021-10-27", "OSMO token sale", 21000000, "Paradigm", False,
                NEWS("osmosis", "Osmosis Closes $21M Token Sale to Make"), "company")]))

L.append(cls("provenance", status="private", rng="below_1b", country="US", city="San Francisco",
    city_src="web_verified", focus="Crypto & Web3", stage="undetermined",
    extra=momentum(NEWS("provenance", "Provenance Blockchain Foundation Names Morgan McKenney")),
    note="Provenance Blockchain, the financial-services Layer 1 that Figure Technologies built (the firm's Our Bets "
         "pages 2022-2025 link its wallet page). Under decisions.md D2 the row is the issuing organisation, the "
         "Provenance Blockchain Foundation, 'a San Francisco based public blockchain network' (blockchain.news, 2022). "
         "No source read names a Ribbit HASH purchase or a priced round of the foundation, so the stage stays "
         "undetermined; Figure itself is a separate row in this base. " + MOM + "no priced round at or above $1B "
         "found for the foundation; HASH trades as a token, which is not a priced round (Rule A).",
    rounds=[]))

L.append(cls("sealance", status="acquired", rng="below_1b", country="US", city="Miami", city_src="web_verified",
    focus="Crypto & Web3", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PRN_SEALANCE,
    entry_date="2022-10",
    note="Sealance, a zero-knowledge compliance engine for blockchains founded by Shlomit Azgad-Tromer, Matthew Green "
         "and Eran Tromer ('Miami-based', the company's release). It emerged from stealth in October 2022 with a seed "
         "round led by Galaxy and Ribbit Capital, with Coinbase Ventures, Gemini Frontier Fund, Luno Expeditions and "
         "Jump Capital. Forte acquired Sealance Corp in February 2025 (" + NEWS("sealance", "Forte Acquires Sealance")
         + "): acquired, below $1B. No later round was found before the sale. Graduation left for the graduation pass.",
    rounds=[rnd("2022-10-24", "Seed", None, "Galaxy, Ribbit Capital", True, PRN_SEALANCE, "company")]))

L.append(cls("slingshot", status="acquired", rng="below_1b", country="US", focus="Crypto & Web3", stage="Series A",
    stage_src="web_verified", stage_conf="high", stage_cite=BLOCK_SLINGSHOT_A, entry_date="2021-12",
    flags=["model_disputes_source", "city_unknown"],
    note="Slingshot (slingshot.finance), a crypto trading app aggregating DEX liquidity (CEO Clinton Bembry). Ribbit led "
         "its $15M Series A of December 2021 as a new investor; Framework Ventures and Electric Capital joined as "
         "existing investors from the $3.1M seed (The Block). Magic Eden completed its acquisition in April 2025 after "
         "$33M raised in total (" + NEWS("slingshot", "Magic Eden acquires crypto trading app") + "): acquired, below "
         "$1B. The pre-filled New Zealand country is a wrong Wikidata join (Slingshot, the New Zealand internet "
         "provider); the country is the model's reading and no source places the city. The Felicis and YC 'Slingshot' "
         "rows are different companies.",
    rounds=[rnd("2020", "Seed", 3100000, None, False, BLOCK_SLINGSHOT_A, "press"),
            rnd("2021-12-09", "Series A", 15000000, "Ribbit Capital", True, BLOCK_SLINGSHOT_A, "press"),
            rnd("2025", "insider round", 2500000, None, None, NEWS("slingshot", "Magic Eden acquires crypto trading app"),
                "press")]))

# ---------------------------------------------------------------- fintech and payments
L.append(cls("digit", status="acquired", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("digit", "Ribbit Capital, General Catalyst back"), entry_date="2016-06",
    flags=["model_disputes_source"],
    note="Digit, the automated savings app ('San Francisco-based', Fortune). Its $11.3M round of May 2015 was led by "
         "General Catalyst with Baseline, Google Ventures and angels, no Ribbit (Fortune); Ribbit and General Catalyst "
         "backed the $22.5M Series B of June 2016 (AltAssets headline): entry Growth, medium confidence because the "
         "2014 seed's investor list was not read. Oportun completed its acquisition on 22 December 2021 for about "
         "$211.1M (" + NEWS("digit", "Oportun completes acquisition of Digit") + "): acquired, below $1B, aligned with "
         "General Catalyst's row. The pre-filled defunct status and Japan country are a wrong Wikidata join on the "
         "name.",
    rounds=[rnd("2015-05-05", "unnamed round", 11300000, "General Catalyst", False,
                NEWS("digit", "Digit, your personal piggy bank"), "press"),
            rnd("2016-06", "Series B", 22500000, None, True, NEWS("digit", "Ribbit Capital, General Catalyst back"),
                "press")]))

L.append(cls("fuze-networks", status="unknown", rng="below_1b", country="US", city="Salt Lake City",
    city_src="web_verified", focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=TC_FUZE, entry_date="2012-09",
    note="Fuze Network (the firm's 2012-2014 Bets page reads 'Fuze Networks': 'a one-of-a-kind payment platform "
         "changing the way retailers and developers send money'), cash-to-card payments, Salt Lake City (TechCrunch). "
         "Its $2.5M Series A of September 2012 was led by Matrix Partners and Meyer Malka of Ribbit, with Ribbit "
         "Capital named among the investors; the $1.2M seed of February 2012 came from Metamorphic Ventures and "
         "Kickstart Seed Fund. Status unknown: no source read gives the company's fate after 2012.",
    rounds=[rnd("2012-02", "Seed", 1200000, "Metamorphic Ventures, Kickstart Seed Fund", False, TC_FUZE, "press"),
            rnd("2012-09-27", "Series A", 2500000, "Matrix Partners, Ribbit Capital", True, TC_FUZE, "press")]))

L.append(cls("health-iq", status="defunct", rng="below_1b", country="US", city="Mountain View", city_src="web_verified",
    focus="Fintech & Payments", stage="undetermined",
    note="Health IQ, life insurance for health-conscious buyers (Mountain View, the company's release). Ribbit is an "
         "existing investor by the $34.6M Series C of November 2017 led by a16z (the release lists CRV, Ribbit, "
         "Foundation Capital, First Round, Felicis and WTI as existing investors) and is named in the $55M Series D of "
         "May 2019; the firm listed Health IQ from its 2015 page, and no source read names the round Ribbit entered, so "
         "the stage stays undetermined. Health IQ filed for Chapter 7 in September 2023 (" +
         NEWS("health-iq", "Health IQ files for Chapter 7") + "): defunct, aligned with the a16z and Felicis rows; First "
         "Round's row reads acquired.",
    rounds=[rnd("2017-11", "Series C", 34600000, "Andreessen Horowitz", True, PRN_HIQ, "company"),
            rnd("2019-05", "Series D", 55000000, "Greenspring Associates, Aquiline Technology Growth, Hanwha Asset Management",
                True, NEWS("health-iq", "Insurance startup Health IQ closes Series D"), "press")]))

L.append(cls("hiro", status="defunct", rng="below_1b", country="US", city="New York", focus="Fintech & Payments",
    stage="undetermined",
    note="Hiro (hirofinance.com), an AI personal finance planner founded in 2024 by Ethan Bloch (Digit's founder) and "
         "Rushabh Doshi, backed by Ribbit, General Catalyst and Restive; Hiro never disclosed what it raised, so no "
         "round can be named: stage undetermined. OpenAI hired the team in April 2026 and Hiro shut its operations on "
         "20 April and deleted user data on 13 May (" + NEWS("hiro", "OpenAI has bought") + "): an acqui-hire, so the "
         "row reads defunct (the acqui-hire rule). General Catalyst's row reads acquired; this is fresher cited "
         "evidence. City aligned with General Catalyst's row. The Lux (Hiro Systems) and YC (hirosecure.com) 'Hiro' "
         "rows are different companies.",
    rounds=[]))

L.append(cls("lead-bank", status="private", rng="1b_plus", usd=1470000000, val_src="web_verified",
    val_cite=NEWS("lead-bank", "A16z-backed Lead Bank hits"), asof="2025-09-04", country="US", city="Kansas City",
    city_src="web_verified", focus="Fintech & Payments", stage="undetermined", extra=VAL,
    note="Lead Bank, a chartered bank serving fintech and crypto companies (Kansas City), acquired in 2022 for $56M by a "
         "team of tech executives led by CEO Jackie Reses. Ribbit is named an existing backer in the $70M Series B of "
         "September 2025 at $1.47B (with a16z, Coatue, Khosla and Zeev; ICONIQ and Greycroft new), but no source names "
         "the round Ribbit entered, so the stage stays undetermined, as on Coatue's row. Mark aligned with the a16z, "
         "Coatue and Khosla rows.",
    rounds=[rnd("2022", "acquisition of Lead Bank by an investor group ($56M)", 56000000, None, None,
                NEWS("lead-bank", "A16z-backed Lead Bank hits"), "press"),
            rnd("2025-09-04", "Series B", 70000000, None, True, NEWS("lead-bank", "A16z-backed Lead Bank hits"), "press")]))

L.append(cls("monzo", rng="1b_plus", usd=5900000000, val_src="web_verified", val_cite=W("Monzo"), asof="2024-10",
    city="London", city_src="web_verified", focus="Fintech & Payments", stage="Growth", stage_src="web_verified",
    stage_conf="medium", stage_cite=FTG_MONZO, entry_date="2024", flags=["model_disputes_source"], extra=VAL,
    note="Monzo, the UK online bank (London, Wikipedia). Ribbit joined the 2024 round of up to GBP 350M led by "
         "Alphabet's CapitalG with Tencent (FinTech Global, February 2024); no earlier Ribbit round was found, and any "
         "Ribbit round after Monzo's early crowdfunding and seed years would be Growth too. Medium confidence on the "
         "round. The pre-filled $2.5B is the stale June 2019 mark; the last priced event is the October 2024 secondary "
         "share sale at $5.9B (Wikipedia), aligned with the Accel, Coatue, General Catalyst and Thrive rows. Reported "
         "Nubank interest (September 2026) is talk, not a mark.",
    rounds=[rnd("2024", "late-stage round (up to GBP 350M)", None, "CapitalG", True, FTG_MONZO, "press"),
            rnd("2024-10", "secondary share sale at $5.9B", None, None, None, W("Monzo"), "press")]))

L.append(cls("nevis", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("nevis", "Nevis: Bringing AI to Wealth"), entry_date="2025", flags=["model_disputes_source"],
    extra=momentum(NEWS("nevis", "Nevis: Bringing AI to Wealth")),
    note="Nevis, AI tools for wealth managers, founded by ex-Revolut Mark Swan, Philipp Burda and Ivan Chalov (New "
         "York, Sequoia's post). Sequoia put in a $5M seed in 2024; Ribbit came in with Sequoia and ICONIQ in the "
         "Series A of nearly $35M in 2025, announced in December 2025 (Sequoia's post; FinTech Global). The pre-filled "
         "Russia country is a wrong Wikidata join on the name. " + MOM + "$40M raised in total, no round at or above "
         "$1B found. Sequoia's 'Nevis' row, left unresolved, is this company.",
    rounds=[rnd("2024", "Seed", 5000000, "Sequoia Capital", False, NEWS("nevis", "Nevis: Bringing AI to Wealth"), "press"),
            rnd("2025", "Series A", 35000000, "Sequoia Capital", True, NEWS("nevis", "Nevis: Bringing AI to Wealth"),
                "press")]))

L.append(cls("outpost", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=NEWS("outpost", "UK startup Outpost raises"), city="London", city_src="web_verified",
    focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("outpost", "Outpost secures £13 million"), entry_date="2026-03", flags=["model_disputes_source"],
    extra=momentum(NEWS("outpost", "Outpost secures £13 million")),
    note="Outpost, payments and tax-compliance infrastructure for cross-border commerce (merchant of record), founded "
         "by ex-Revolut Will Mahon-Heap, 'London-headquartered' (BusinessCloud). Ribbit led the GBP 13M ($17.5M) Series "
         "A of March 2026; the $3M seed about a year earlier was led by Better Tomorrow Ventures without Ribbit (UK "
         "Tech News). The pre-filled Indonesia country is a wrong join. " + MOM + "no round at or above $1B found.",
    rounds=[rnd("2025", "Seed", 3000000, "Better Tomorrow Ventures", False, NEWS("outpost", "Outpost secures £13 million"),
                "press"),
            rnd("2026-03-10", "Series A", 17500000, "Ribbit Capital", True, NEWS("outpost", "Outpost secures £13 million"),
                "press")]))

L.append(cls("parasut", status="acquired", rng="below_1b", country="TR", country_src="web_verified",
    country_cite=TECHEU_PARASUT, city="Istanbul", city_src="web_verified", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TECHEU_PARASUT,
    note="Paraşüt, cloud accounting and invoicing for Turkish SMEs ('Istanbul-based', Tech.eu; the firm's 2014-2018 "
         "Bets pages list it as eDefter). Its 'Series A of $1.9 million from Ribbit Capital' preceded the $2M Series B "
         "of November 2016 with Diffusion Capital Partners, 500 Startups and the existing investors Revo Capital and "
         "Ribbit (Tech.eu): entry Series A. No entry date is given: no source read dates the Series A, and the firm "
         "already listed the company in August 2014 (a capture, which may not date an entry). Mikro and Zirve (DST "
         "Technology Group, backed by TURKVEN and Earlybird) completed the purchase on 31 May 2019 (" +
         NEWS("parasut", "sale is now finalized") + "): acquired, below $1B.",
    rounds=[rnd(None, "Series A", 1900000, "Ribbit Capital", True, TECHEU_PARASUT, "press"),
            rnd("2016-11", "Series B", 2000000, None, True, TECHEU_PARASUT, "press")]))

L.append(cls("payflows", status="private", rng="below_1b", country="FR", country_src="web_verified",
    country_cite=NEWS("payflows", "Paris-based Payflows raises"), city="Paris", city_src="web_verified",
    focus="Fintech & Payments", stage="Seed", stage_src="model", stage_conf="medium",
    stage_cite=NEWS("payflows", "Treasury management startup Payflows"), entry_date="2022-10",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("payflows", "SaaS Payflows raises"), grad_conf="high",
    extra=momentum(NEWS("payflows", "SaaS Payflows raises")),
    note="Payflows, finance-operations software founded in 2022 by Pauline Glikman and Joseph Assouline (Paris). "
         "Ribbit co-led its $5.5M round of October 2022 (Business Insider headline; Headline co-led per its own row), "
         "the company's only round before the Series A, and is named an existing investor in the EUR 25M Series A of "
         "April 2024 led by Balderton (Tech.eu); a pre-Series A round of that size in 2022 reads Seed (model, medium). "
         "Graduated: the Series A is a named later round (EUR 25M @ ECB 2024-04-22, EUR/USD 1.0632 = $26.6M). "
         + MOM + "no round at or above $1B found.",
    rounds=[rnd("2022-10-18", "first round (unnamed)", 5500000, "Ribbit Capital, Headline", True,
                NEWS("payflows", "Treasury management startup Payflows"), "press"),
            rnd("2024-04-22", "Series A", 26580000, "Balderton Capital", True, NEWS("payflows", "SaaS Payflows raises"),
                "press")]))

L.append(cls("slash", city="San Francisco", city_src="web_verified", focus="Fintech & Payments", stage="Growth",
    stage_src="web_verified", stage_conf="high", stage_cite=W("Slash (company)"), entry_date="2026-04",
    note="Slash Financial, vertical business banking (San Francisco, Wikipedia). Its seed and Series A of 2022-2023 "
         "($19M combined) were led by NEA and the $41M Series B of May 2025 by Goodwater, neither naming Ribbit; Ribbit "
         "led the $100M Series C of April 2026 at $1.4B, co-led by Khosla and Goodwater (Wikipedia): entry Growth. Mark "
         "as pre-filled, aligned with the Khosla, Menlo and YC rows.",
    rounds=[rnd("2022", "Seed and Series A (combined)", 19000000, "New Enterprise Associates", False,
                W("Slash (company)"), "press"),
            rnd("2025-05", "Series B", 41000000, "Goodwater Capital", False, W("Slash (company)"), "press"),
            rnd("2026-04", "Series C", 100000000, "Ribbit Capital", True, W("Slash (company)"), "press")]))

for slug, other in (("sling-money", "morse-money"), ("morse-money", "sling-money")):
    L.append(cls(slug, status="private", rng="below_1b", country="GB", country_src="web_verified",
        country_cite=ARCH("sling-money"), city="London", focus="Fintech & Payments", stage="Seed",
        stage_src="web_verified", stage_conf="high", stage_cite=NEWS("sling-money", "Sling Money, a stablecoin-based"),
        flags=["country_conflict"], extra=momentum(NEWS("sling-money", "Sling Money, a stablecoin-based")),
        note="Sling Money, the stablecoin-based global payments app of Avian Labs (Mike Hudack and Simon Amor, ex-Monzo), "
             "now Morse Money: sling.money redirects to morsemoney.com, which Avian Labs runs (read 2026-09-28), so the "
             "rows " + slug + " and " + other + " are one company. Ribbit led the $5M seed (Slow Ventures joined) and "
             "co-led the $15M Series A of August 2024 with USV and Slow (The Block). The seed is undated in every source "
             "read, so no entry date is given; the Series A is a named later round, and the graduation is left for the "
             "graduation pass once the seed is dated. Country: the firm's 2025 Our Bets page labels it London; Silicon "
             "Canals calls it 'based in the US and Netherlands' (Delaware parent, Amsterdam branch): country_conflict. "
             + MOM + "no round at or above $1B found.",
        rounds=[rnd(None, "Seed", 5000000, "Ribbit Capital", True, NEWS("sling-money", "Sling Money, a stablecoin-based"),
                    "press"),
                rnd("2024-08-14", "Series A", 15000000, "Union Square Ventures, Ribbit Capital, Slow Ventures", True,
                    NEWS("sling-money", "Sling Money, a stablecoin-based"), "press")]))

L.append(cls("sofia", status="private", rng="below_1b", country="MX", country_src="web_verified",
    country_cite=COVERAGER_SOFIA, city="Mexico City", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=COVERAGER_SOFIA, entry_date="2020-03",
    grad="graduated", grad_src="web_verified", grad_cite=FTG_SOFIA, grad_conf="high", flags=["model_disputes_source"],
    extra=momentum(NEWS("sofia", "Sofía raises $13.5M")),
    note="Sofía, a Mexican health insurer with telemedicine (Mexico City, Coverager). Ribbit was in the $6.3M seed of "
         "March 2020 with Kaszek and Cavalry Ventures (Coverager) and joined the $19M Series A of November 2020 led by "
         "Index Ventures (FinTech Global): graduated. A $13.5M round of December 2024 was led by Kfund (LatamList). The "
         "pre-filled country (Bulgaria) is a wrong Wikidata join on the name. " + MOM + "no round at or above $1B "
         "found.",
    rounds=[rnd("2020-03", "Seed", 6300000, None, True, COVERAGER_SOFIA, "press"),
            rnd("2020-11", "Series A", 19000000, "Index Ventures", True, FTG_SOFIA, "press"),
            rnd("2024-12", "unnamed round", 13500000, "Kfund", False, NEWS("sofia", "Sofía raises $13.5M"), "press")]))

# ---------------------------------------------------------------- AI, hardware, security, energy, other
L.append(cls("enigma", status="private", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("enigma", "Israeli AI robotics startup Enigma"), focus="AI & Applied AI", stage="Seed",
    stage_src="web_verified", stage_conf="high", stage_cite=NEWS("enigma", "Israeli AI robotics startup Enigma"),
    entry_date="2026-07", grad="censored", flags=["city_unknown"],
    extra=momentum(NEWS("enigma", "Enigma raises $71M to make controlling")),
    note="Enigma, foundation AI models for robots, founded by Jonathan Jacobi and Gal Niv (Israeli, Calcalist; hangars "
         "in Israel and California, TechCrunch). Index Ventures and Ribbit co-led its $71M seed of July 2026 with "
         "Conviction: entry Seed, censored (inside 24 months). " + MOM + "no valuation disclosed and no round at or "
         "above $1B found. No city on record. Insight Partners' 'Enigma' row is a different company (aftermarket "
         "software, Burlington).",
    rounds=[rnd("2026-07-27", "Seed", 71000000, "Index Ventures, Ribbit Capital", True,
                NEWS("enigma", "Israeli AI robotics startup Enigma"), "press")]))

L.append(cls("enter", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified",
    val_cite=NEWS("enter", "Greenberg Traurig"), asof="2026-05-08", country="BR", country_src="web_verified",
    country_cite=NEWS("enter", "Greenberg Traurig"), city="São Paulo", focus="AI & Applied AI", stage="Growth",
    stage_src="web_verified", stage_conf="high", stage_cite=NEWS("enter", "Greenberg Traurig"), entry_date="2026-05",
    flags=["model_disputes_source"], extra=VAL,
    note="Enter (getenter.ai, formerly Talisman), legal AI, 'Brazil-based' (release datelined Sao Paulo). Its $37.5M "
         "round of September 2025 at $375M post-money was led by Founders Fund with Sequoia, ONEVC and Atlantico, no "
         "Ribbit (LatamList); Ribbit joined the $100M Series B of May 2026 led by Founders Fund at about $1.2B: entry "
         "Growth. The pre-filled defunct status and Russia country are a wrong Wikidata join on a common word. "
         "Coatue's 'Enter' row is a different company (enter.de, Berlin); Sequoia's row is this company but reads "
         "country US.",
    rounds=[rnd("2025-03", "undisclosed round (Sequoia)", None, None, None,
                NEWS("enter", "Enter raises $37.5M led by Founders Fund"), "press"),
            rnd("2025-09-25", "unnamed round at $375M post-money", 37500000, "Founders Fund", False,
                NEWS("enter", "Enter raises $37.5M led by Founders Fund"), "press"),
            rnd("2026-05-08", "Series B", 100000000, "Founders Fund", True, NEWS("enter", "Greenberg Traurig"), "press")]))

L.append(cls("etched", city="Cupertino", focus="Industrial & Robotics", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=NEWS("etched", "Etched raises $500M at $5B valuation"), entry_date="2026-01",
    note="Etched, transformer inference chips (Cupertino, as the sibling rows). The $120M Series A of June 2024 was led "
         "by Primary Venture Partners and Positive Sum with Two Sigma, Peter Thiel and Kyle Vogt, no Ribbit (TechCrunch's "
         "2024 list); Ribbit joined the round of about $500M at about $5B led by Stripes in January 2026 (Tech Funding "
         "News), past the Series A: Growth. Mark as pre-filled, aligned with the Bain Capital Ventures row.",
    rounds=[rnd("2024-06-25", "Series A", 120000000, "Primary Venture Partners, Positive Sum", False,
                NEWS("etched", "full list of 49 US AI startups"), "press"),
            rnd("2026-01", "unnamed round at about $5B", 500000000, "Stripes", True, NEWS("etched", "Etched raises $500M at $5B valuation"),
                "press")]))

L.append(cls("evervault", status="private", rng="below_1b", country="IE", country_src="web_verified",
    country_cite=NEWS("evervault", "Irish data security start-up Evervault raises"), city="Dublin",
    city_src="web_verified", focus="Security", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("evervault", "Evervault raises $25M to scale"), entry_date="2026-03",
    extra=momentum(NEWS("evervault", "Evervault raises $25M to scale")),
    note="Evervault, encryption infrastructure for sensitive data, founded by Shane Curran ('New York and Dublin-based', "
         "Silicon Republic; Dublin kept, aligned with Sequoia's row). Ribbit led the $25M Series B of March 2026 with "
         "Sequoia, Index, Kleiner Perkins, Next Play and Operator Partners (SiliconANGLE; The Currency); the $3.2M seed "
         "of 2019 and the $16M Series A of 2020 are reported as Sequoia- and Index-backed, not naming Ribbit. Entry "
         "Growth, medium confidence since the seed's full list was not read. " + MOM + "no round at or above $1B "
         "found.",
    rounds=[rnd("2019-10", "Seed", 3200000, None, None, NEWS("evervault", "Irish data security start-up Evervault raises"),
                "press"),
            rnd("2020-05", "Series A", 16000000, None, None,
                NEWS("evervault", "Irish data security start-up Evervault raises"), "press"),
            rnd("2026-03-05", "Series B", 25000000, "Ribbit Capital", True,
                NEWS("evervault", "Evervault raises $25M to scale"), "press")]))

L.append(cls("fuse-energy", status="private", rng="1b_plus", usd=5000000000, val_src="web_verified",
    val_cite=NEWS("fuse-energy", "Fuse Energy Secures $70 Million"), asof="2025-12", city="London",
    city_src="web_verified", focus="Climate & Energy", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("fuse-energy", "Energy Startup Tesseract Raises"), entry_date="2022-09",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("fuse-energy", "Fuse Energy Secures $70 Million"),
    grad_conf="high", extra=VAL,
    note="Fuse Energy (Tesseract until 2023), energy supplier and developer founded by ex-Revolut Alan Chang and Charles "
         "Orr, headquartered in London (Wikipedia: " + W("Fuse Energy") + "). Ribbit is named in the $78M round of "
         "September 2022 led by Balderton and Lakestar (Mercom), which Wikipedia calls the company's seed. Graduated: "
         "the $70M Series B of December 2025 led by Balderton and Lowercarbon at a $5B valuation (Mercom), which names "
         "Ribbit an existing investor. Mark aligned with Balderton's row; Creandum's row still reads below $1B.",
    rounds=[rnd("2022-09-12", "Seed", 78000000, "Balderton Capital, Lakestar", True,
                NEWS("fuse-energy", "Energy Startup Tesseract Raises"), "press"),
            rnd("2025-12-22", "Series B", 70000000, "Balderton Capital, Lowercarbon Capital", True,
                NEWS("fuse-energy", "Fuse Energy Secures $70 Million"), "press")]))

L.append(cls("goodlord", status="private", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=NEWS("goodlord", "Goodlord secures further £7m"), city="London", city_src="web_verified",
    focus="SaaS", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("goodlord", "Rental Startup Goodlord"), entry_date="2017-03",
    note="Goodlord, lettings software for UK letting agents (Whitechapel Road, London, per its own site). Goodlord "
         "raised GBP 7.2M from Ribbit in March 2017 (Business Insider headline; GBP 7.2M @ ECB 2017-03-14 = $8.7M), the "
         "round its own post calls the 2017 Series A; the 2018 GBP 7M round was led by Finch Capital with Rocket "
         "Internet and Global Founders Capital, the earlier backers (" + NEWS("goodlord", "Goodlord secures further £7m")
         + "). Still operating in 2026 (its own posts): private, below $1B.",
    rounds=[rnd("2017-03-14", "Series A", 8741500, None, True, NEWS("goodlord", "Rental Startup Goodlord"), "press"),
            rnd("2018-10", "further round (GBP 7M)", None, "Finch Capital", None,
                NEWS("goodlord", "Goodlord secures further £7m"), "company")]))

L.append(cls("harmonic", status="private", rng="1b_plus", usd=1450000000, val_src="web_verified",
    val_cite=NEWS("harmonic", "Harmonic AI raises $120M"), asof="2025-11-25", country="US", city="Palo Alto",
    city_src="web_verified", focus="AI & Applied AI", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("harmonic", "Harmonic AI raises $120M"), entry_date="2025-11", flags=["model_disputes_source"],
    extra=VAL,
    note="Harmonic (harmonic.fun), the mathematical-reasoning AI company co-founded by Tudor Achim and Vlad Tenev (Palo "
         "Alto, Wikipedia: " + W("Harmonic (company)") + "). The $75M Series A of September 2024 was led by Sequoia "
         "(Index, Era, GreatPoint, DTS; no Ribbit) and the $100M Series B of July 2025 by Kleiner Perkins (Sequoia, "
         "Index, Paradigm); Ribbit led the $120M Series C of November 2025 at $1.45B (SiliconANGLE): entry Growth. The "
         "pre-filled public status and $0.65B are a wrong join to Harmonic Inc., the listed video company (Lightspeed's "
         "'Harmonic' row); aligned with Sequoia's row at $1.45B.",
    rounds=[rnd("2024-09-23", "Series A", 75000000, "Sequoia Capital", False,
                NEWS("harmonic", "Harmonic raises $75M to create AI"), "press"),
            rnd("2025-07", "Series B", 100000000, "Kleiner Perkins", False, W("Harmonic (company)"), "press"),
            rnd("2025-11-25", "Series C", 120000000, "Ribbit Capital", True, NEWS("harmonic", "Harmonic AI raises $120M"),
                "press")]))

L.append(cls("listen-labs", status="private", rng="below_1b", country="US", city="San Francisco",
    city_src="web_verified", focus="AI & Applied AI", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("listen-labs", "Listen Labs raises $69 million Series B"), entry_date="2026-01",
    extra=momentum(NEWS("listen-labs", "scrubbed a $1.5B")),
    note="Listen Labs, AI customer research (San Francisco, the release). Ribbit led the $69M Series B of January 2026, "
         "the release naming Evantic, Sequoia, Conviction and Pear VC as existing investors: entry Growth. " + MOM +
         "the Series B valued the company at $500M; a $125M Series C at $1.5B led by Menlo was signed and then "
         "abandoned, and Salesforce's talks at about $2B are not a deal (TechCrunch, 2026-09-09): below $1B on the "
         "last closed round.",
    rounds=[rnd("2026-01-14", "Series B", 69000000, "Ribbit Capital", True,
                NEWS("listen-labs", "Listen Labs raises $69 million Series B"), "press")]))

L.append(cls("mach-industries", status="private", rng="1b_plus", usd=3700000000, val_src="web_verified",
    val_cite=NEWS("mach-industries", "Mach Industries Raises Additional $600 Million to Scale"), asof="2026-09-10",
    country="US", city="Huntington Beach", city_src="web_verified", focus="Industrial & Robotics", stage="Growth",
    stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("mach-industries", "Mach Industries Raises $300 Million in Series C Funding"), entry_date="2026-06",
    extra=VAL,
    note="Mach Industries, autonomous defense systems (Huntington Beach, the company's releases). Ribbit co-led the $300M "
         "Series C of June 2026 at $1.8B with Infinite Capital, both new investors beside Bedrock, Sequoia and Khosla: "
         "entry Growth. The $600M continuation of the Series C of 10 September 2026 at $3.7B names Ribbit again; that "
         "is the mark. The Khosla and Sequoia rows carry the June $1.8B; this is fresher cited evidence.",
    rounds=[rnd("2026-06-02", "Series C", 300000000, "Infinite Capital, Ribbit Capital", True,
                NEWS("mach-industries", "Mach Industries Raises $300 Million in Series C Funding"), "company"),
            rnd("2026-09-10", "Series C extension", 600000000, None, True,
                NEWS("mach-industries", "Mach Industries Raises Additional $600 Million to Scale"), "company")]))

L.append(cls("psiquantum", city="Palo Alto", city_src="web_verified", focus="Industrial & Robotics", stage="Growth",
    stage_src="web_verified", stage_conf="high", stage_cite=NEWS("psiquantum", "Temasek backs PsiQuantum"),
    entry_date="2025-09",
    note="PsiQuantum, photonic quantum computers (Palo Alto, Wikipedia: " + W("PsiQuantum") + "). Ribbit is one of the "
         "new investors in the $1B Series E of September 2025 at $7B led by BlackRock with Temasek and Baillie Gifford "
         "(TNGlobal): entry Growth. Mark as pre-filled, aligned with the Atomico and Redpoint rows.",
    rounds=[rnd("2025-09-10", "Series E", 1000000000, "BlackRock, Temasek, Baillie Gifford", True,
                NEWS("psiquantum", "Temasek backs PsiQuantum"), "press")]))

L.append(cls("qognitive", status="private", rng="below_1b", country="US", focus="AI & Applied AI", stage="undetermined",
    entry_date="2023", flags=["city_unknown"], extra=momentum(RISK_QOG),
    note="Qognitive, Inc., quantum cognition machine learning, founded by Dario Villani and Kharen Musaelian (the "
         "quants behind Duality Group). Risk.net (December 2023) names Ribbit Capital as the start-up's lead investor, "
         "with Raptor Capital Management; the round is not named, so the stage stays undetermined. Publishing research "
         "in 2025 (Nature, Phys.org): private. No source read places the company; the country is the model's reading. "
         + MOM + "no round at or above $1B found.",
    rounds=[rnd("2023", "founding financing (unnamed)", None, "Ribbit Capital", True, RISK_QOG, "press")]))

L.append(cls("redefine", status="unknown", rng="below_1b", country="IL", country_src="web_verified",
    country_cite=NEWS("redefine", "Blockchain security startup Redefine"), focus="Security", stage="Seed",
    stage_src="web_verified", stage_conf="high", stage_cite=NEWS("redefine", "Blockchain security startup Redefine"),
    entry_date="2022-01", flags=["city_unknown"],
    note="Redefine, DeFi risk and security tooling for institutions (Israeli, Calcalist; founders Shira Brezis and Alon "
         "Ram). Ribbit led its $11M seed of January 2022 with Jump Capital and ParaFi; More VC and Accomplice "
         "Blockchain came from the pre-seed. Status unknown: the firm listed it on its Our Bets pages 2022-2025 but not "
         "on the live list, redefine.net serves an empty page (checked 2026-09-28), and no later round, sale or "
         "shutdown was found. Graduation left for the graduation pass. No city on record.",
    rounds=[rnd(None, "Pre-seed", None, None, False, NEWS("redefine", "Blockchain security startup Redefine"), "press"),
            rnd("2022-01-17", "Seed", 11000000, "Ribbit Capital", True,
                NEWS("redefine", "Blockchain security startup Redefine"), "press")]))

L.append(cls("rhi-group", status="unknown", rng="below_1b", country="US", city="San Francisco", city_src="web_verified",
    focus="SaaS", stage="undetermined",
    note="RHI Group Inc., retail marketing technology (a loyalty and customer-data platform for offline retailers; its "
         "principals founded Air Miles, Nectar and Datalogix), 'financed by M33 Growth and Ribbit Capital' (Thanx "
         "release, October 2020, when RHI made a strategic investment in Thanx). M33 lists it at Toronto and San "
         "Francisco (" + M33_RHI + "); the firm's pages label it USA. M33 backed it in August 2019 (PE Hub) and no "
         "source names Ribbit's round, so the stage stays undetermined. Status unknown: rhigroup.com is a parked domain "
         "for sale (checked 2026-09-28) and no sale or shutdown report was found.",
    rounds=[rnd("2019-08", "financing (M33 Growth)", None, "M33 Growth", None, PEHUB_RHI, "press"),
            rnd("2020-10", "financing named in the Thanx release", None, None, True, MARTECH_RHI, "press")]))

L.append(cls("somos-internet", status="private", rng="below_1b", country="CO", country_src="web_verified",
    country_cite=NEWS("somos-internet", "Medellín Startup Somos Internet Secures Seed"), city="Medellín",
    city_src="web_verified", focus="Consumer & Marketplaces", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=NEWS("somos-internet", "Somos Internet raises $18M Series A"), entry_date="2025-08",
    note="Somos Internet, a Colombian fiber internet provider with its own router and network software ('Medellín-"
         "based', Finance Colombia). The $13.4M seed of July 2023 came from Nazca, K50 and Kaszek, no Ribbit; USV and "
         "Ribbit co-led the $18M Series A reported in late August 2025 (LatamList), and Bracket Capital and Ribbit "
         "co-led the $40M Series B of March 2026: entry Series A. YC's 'Somos' row is this company (Medellín, private).",
    rounds=[rnd("2023-07", "Seed", 13400000, None, False,
                NEWS("somos-internet", "Medellín Startup Somos Internet Secures Seed"), "press"),
            rnd("2025-08", "Series A", 18000000, "Union Square Ventures, Ribbit Capital", True,
                NEWS("somos-internet", "Somos Internet raises $18M Series A"), "press"),
            rnd("2026-03-31", "Series B", 40000000, "Bracket Capital, Ribbit Capital", True,
                NEWS("somos-internet", "Somos Internet raises $40M Series B"), "press")]))

L.append(cls("stedi", status="private", rng="below_1b", country="US", focus="Healthcare & Bio", stage="undetermined",
    flags=["city_unknown"],
    note="Stedi, an API-first healthcare clearinghouse founded by Zack Kanter (formerly Boulder-based, Daily Camera "
         "2020; no current city on record). Ribbit is named among the participants of the $70M Series B announced in "
         "August 2025 (a $50M earlier unannounced round plus $20M new, co-led by Stripe and Addition) and of the $50M "
         "Series C of March 2026 led by Addition; no source says whether Ribbit held shares before, so the stage stays "
         "undetermined, as on First Round's row.",
    rounds=[rnd("2025-08-14", "Series B ($50M earlier round plus $20M new)", 70000000, "Stripe, Addition", True,
                NEWS("stedi", "Announcing Stedi"), "company"),
            rnd("2026-03-30", "Series C", 50000000, "Addition", True,
                NEWS("stedi", "Stedi Raises $50M Series C to Modernize"), "press")]))

jl.write("batch-004", L)
