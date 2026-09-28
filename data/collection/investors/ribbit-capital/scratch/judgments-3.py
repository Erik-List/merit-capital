"""PRO-161 grind, batch 3: the member rows of queue/batch-003.json (Solana to Deel, archive order).
Evidence: the judge view (show.py), Wikipedia (wikifetch.py), the Google News sweep and nq.py (NQ_TAG=b3),
pages fetched and read (company releases, press), and the firm's deal vehicles (SPV).
Skipped: bitcoin (not_member), caret (recorded by another judge). bank-jago takes a verdict line (T3)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV = jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W, jl.NEWS, jl.SPV
WV = {"valuation_range_source": "web_verified"}
L = []

# ---------------------------------------------------------------- Solana
SOL_CG = "https://www.coingecko.com/en/coins/solana"
SOL_SALE = ("https://solana.com/news/solana-labs-completes-a-314-15m-private-token-sale-led-by-andreessen-horowitz-"
            "and-polychain-capital")
L.append(cls("solana", status="private", rng="10b_plus", usd=69944038416, val_src="web_verified", val_cite=SOL_CG,
    asof="2026-09-28", stage="undetermined", country="US", country_src="web_verified",
    country_cite=W("Solana (blockchain platform)"), city="San Francisco", city_src="web_verified",
    focus="Crypto & Web3", flags=("model_disputes_source",),
    note="Solana Labs, the San Francisco company that launched the Solana network (Wikipedia). The prefilled public "
         "status and $6.2M float are a match on an unrelated SEC filer (cik_weak), disputed: Solana Labs is private. "
         "Band on the SOL token network cap, $69.94B on CoinGecko on 2026-09-28, the basis a16z's row uses (no Solana "
         "Labs equity mark exists). Entry round not established: Solana Labs financed itself through SOL token sales, "
         "and the largest, the $314.15M private sale of June 2021 led by a16z and Polychain, does not name Ribbit "
         "(Solana's own announcement); Ribbit's archived Our Bets page lists Solana from August 2022. Stage undetermined; "
         "the record does not show how Ribbit bought in, so no token_funded flag.",
    rounds=[rnd("2021-06-09", "Private token sale", 314159265, "Andreessen Horowitz; Polychain Capital", None,
                SOL_SALE, "company")], extra=WV))

# ---------------------------------------------------------------- Stark Bank
BL_STARK = NEWS("stark-bank", "Bezos Backs Brazil")
L.append(cls("stark-bank", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=BL_STARK, entry_date="2022-04", city="São Paulo", city_src="web_verified",
    focus="Fintech & Payments",
    note="Brazilian business bank headquartered in São Paulo (Bloomberg Línea). Ribbit led the $45M Series B of April "
         "2022 after following the company since March 2020; the $13M Series A of December 2021 was led by Lachy Groom "
         "(Bloomberg Línea, 2022-04-11). Y Combinator's row carries San Francisco, US from its directory fields; this "
         "row records the São Paulo headquarters the press gives. Momentum check: no round at or above $1B found, news "
         "sweep 2026-09-28.",
    rounds=[rnd("2021-12", "Series A", 13000000, "Lachy Groom", None, BL_STARK, "press"),
            rnd("2022-04", "Series B", 45000000, "Ribbit Capital", True, BL_STARK, "press")]))

# ---------------------------------------------------------------- Stitch
TC_STITCH_A = NEWS("stitch", "Stitch raises $21M for its API infrastructure")
TC_STITCH_X = NEWS("stitch", "Stitch raises $25M Series A extension led by Ribbit")
L.append(cls("stitch", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=TC_STITCH_X, entry_date="2023-10", country="ZA", country_src="web_verified",
    country_cite=W("Stitch Money"), city="Cape Town", city_src="web_verified", focus="Fintech & Payments",
    note="South African payments infrastructure company headquartered in Cape Town (Wikipedia). Ribbit led the $25M "
         "Series A extension of October 2023 (TechCrunch, 2023-10-02); the original $21M Series A of February 2022 was "
         "led by The Spruce House Partnership and TechCrunch's list of its investors does not name Ribbit. Ribbit took "
         "part in the $55M Series B of April 2025 as an existing funder (Wikipedia). Momentum check: no round at or "
         "above $1B found, news sweep 2026-09-28. The a16z, General Catalyst and Y Combinator rows named Stitch are "
         "other companies (Stitch Technologies, a US and London developer-tools startup): name collisions, not aligned.",
    rounds=[rnd("2021-02", "Seed", 4000000, None, None, W("Stitch Money"), "press"),
            rnd("2022-02", "Series A", 21000000, "The Spruce House Partnership", False, TC_STITCH_A, "press"),
            rnd("2023-10", "Series A extension", 25000000, "Ribbit Capital", True, TC_STITCH_X, "press"),
            rnd("2025-04", "Series B", 55000000, "QED Investors; Glynn Capital; Flourish Ventures; Norrsken22", True,
                W("Stitch Money"), "press")]))

# ---------------------------------------------------------------- Tako
TC_TAKO = NEWS("tako", "Exclusive: Brazilian fintech Tako")
LL_TAKO18 = NEWS("tako", "Tako raises $18M")
L.append(cls("tako", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=TC_TAKO, entry_date="2024-11", grad="censored", country="BR", country_src="web_verified",
    country_cite=TC_TAKO, city="São Paulo", city_src="web_verified", focus="SaaS",
    note="São Paulo employee life-cycle and payroll platform (TechCrunch). Ribbit co-led the $13.2M seed with a16z "
         "(TechCrunch, 2024-11-11). An $18M round followed in July 2025, again led by Ribbit and a16z (LatamList), but "
         "the source gives it no round name and it is below twice the $13.2M seed, so it does not graduate the row; "
         "the entry is inside the 24-month window, so censored. a16z's row reads graduated on the $16M bar for an "
         "undisclosed seed amount, but LatamList and TechCrunch give $13.2M: raised for alignment. a16z's US country "
         "is an inferred value; this row cites São Paulo. Momentum check: no round at or above $1B found, news sweep "
         "2026-09-28.",
    rounds=[rnd("2024-11", "Seed", 13200000, "Andreessen Horowitz; Ribbit Capital", True, TC_TAKO, "press"),
            rnd("2025-07", "Unnamed", 18000000, "Ribbit Capital; Andreessen Horowitz", True, LL_TAKO18, "press")]))

# ---------------------------------------------------------------- Tala
TALA_B = "https://tala.co/series-b-press-release/"
MN_TALA = NEWS("tala", "US-based fintech firm announces its expansion")
LABJ_TALA = NEWS("tala", "Microloan Company Tala Lands")
L.append(cls("tala", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=TALA_B, entry_date="2017-02", country="US", country_src="web_verified", country_cite=LABJ_TALA,
    city="Santa Monica", city_src="web_verified", focus="Fintech & Payments", flags=("model_disputes_source",),
    note="Mobile credit for emerging markets. 'Tala has raised more than $30 million in Series B financing, led by IVP "
         "and joined by Ribbit Capital', with Lowercase, Data Collective, Collaborative Fund and F3 named as the "
         "existing investors (the company's release, 2017-02-22), so Ribbit entered at the Series B. Ribbit was an "
         "existing investor in the $50M Series C of April 2018 (MediaNama), also held through its TL-C vehicle. The "
         "$145M Series E of October 2021 gave an enterprise valuation above $800M (Los Angeles Business Journal); no "
         "later round at or above $1B found, news sweep 2026-09-28. The prefilled Algeria (DZ) is a Wikidata namesake, "
         "disputed. City: Santa Monica (Los Angeles Business Journal, 2021); IVP's row carries Los Angeles, from the "
         "company's 2017 release.",
    rounds=[rnd("2017-02", "Series B", 30000000, "IVP", True, TALA_B, "company"),
            rnd("2018-04", "Series C", 50000000, "Revolution Growth", True, MN_TALA, "press"),
            rnd("2021-10", "Series E", 145000000, "Upstart", None, LABJ_TALA, "press")]))

# ---------------------------------------------------------------- Taxbit
PRN_TAXBIT = NEWS("taxbit", "TaxBit Raises $130M Series B at $1.33B")
PP_TAXBIT = NEWS("taxbit", "PayPal Ventures Invests In TaxBit")
L.append(cls("taxbit", status="private", rng="1b_plus", usd=1330000000, val_src="web_verified", val_cite=PRN_TAXBIT,
    asof="2021-08-12", stage="undetermined", country="US", city="Draper", focus="Fintech & Payments",
    flags=("stale",),
    note="Tax information reporting software for digital assets (Draper, Utah; aligned with the IVP and Insight rows). "
         "Ribbit's round is not on record: neither the $100M Series A of March 2021 (Paradigm and Tiger Global; "
         "PayPal's release lists the participants) nor the $130M Series B at $1.33B of August 2021 (IVP and Insight; "
         "the company's release) names Ribbit, and the firm's archive lists Taxbit from 2022. Stage undetermined. "
         "Mark: the Series B's $1.33B (company release, 2021-08-12), older than 24 months and aligned with the "
         "sibling rows; staff cuts and a CEO change in 2023 (Business Journals) carry no price.",
    rounds=[rnd("2021-03", "Series A", 100000000, "Paradigm; Tiger Global", None, PP_TAXBIT, "press"),
            rnd("2021-08", "Series B", 130000000, "IVP; Insight Partners", None, PRN_TAXBIT, "company")],
    extra=WV))

# ---------------------------------------------------------------- Teya
UKTN = "https://www.uktech.news/funding/tiger-global-uk-investments-20220518"
CITYAM = NEWS("teya", "London fintech Teya launches")
L.append(cls("teya", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=UKTN,
    asof="2021", stage="undetermined", country="GB", country_src="web_verified", country_cite=CITYAM,
    city="London", city_src="web_verified", focus="Fintech & Payments", flags=("stale",),
    note="Teya (SaltPay until 2023), payments and software for small merchants, London-based and incorporated in the "
         "Cayman Islands, backed by Tiger Global and Ribbit (City AM, 2026-02-03). No source read names Ribbit's "
         "round: SaltPay raised a $478M Series C in April 2021 with Tiger Global (UKTN), about $500M in 2021 by City "
         "AM's count, and Ribbit's archive lists SaltPay from 2022. Stage undetermined. Band aligned with Accel's row: "
         "UKTN (2022-05-18) gives SaltPay's valuation as $1bn after the 2021 Series C; the figure sits exactly on the "
         "$1B edge and is older than 24 months. Accel's cited Sifted page now returns 404.",
    rounds=[rnd("2021-04", "Series C", 478000000, None, None, UKTN, "press")], extra=WV))

# ---------------------------------------------------------------- Tomo
GW_TOMO20 = NEWS("tomo", "Former Zillow execs raise $40M seed round")
GW_TOMO22 = NEWS("tomo", "Tomo, a ‘PayPal for the mortgage")
GW_TOMO25 = NEWS("tomo", "Digital mortgage startup Tomo lands $20M")
L.append(cls("tomo", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=GW_TOMO20, entry_date="2020-10", grad="graduated", grad_src="web_verified", grad_cite=GW_TOMO22,
    grad_conf="high", country="US", city="New York", city_src="web_verified", focus="Fintech & Payments",
    flags=("model_disputes_source",),
    note="Tomo (Tomo Networks, now Tomo Mortgage), digital mortgage lender founded by former Zillow executives. Ribbit "
         "co-led the $40M seed with Zigg Capital and NFX (GeekWire, 2020-10-27). Graduated: the $40M Series A of "
         "March 2022, led by SVB Capital with Ribbit participating, at a $640M valuation (GeekWire, 2022-03-21). Ribbit "
         "is also an existing investor in the $20M Series B of March 2025, when the company made New York its "
         "headquarters (GeekWire, 2025-03-11). The prefilled acquired status and Italy (IT) are a Wikidata namesake "
         "join, disputed: Tomo operates and is private. Last priced mark $640M (2022); no later round at or above $1B "
         "found, news sweep 2026-09-28. Bain Capital Ventures' Tomo (a personal AI coach, 2026) is another company; "
         "General Catalyst's 'Tomo, Inc.' is unresolved on that row.",
    rounds=[rnd("2020-10", "Seed", 40000000, "Ribbit Capital; Zigg Capital; NFX", True, GW_TOMO20, "press"),
            rnd("2022-03", "Series A", 40000000, "SVB Capital", True, GW_TOMO22, "press"),
            rnd("2025-03", "Series B", 20000000, None, True, GW_TOMO25, "press")]))

# ---------------------------------------------------------------- Toss
TC_TOSS = NEWS("toss", "closes $405M Series G")
L.append(cls("toss", status="private", rng="1b_plus", usd=7002897246, val_src="web_verified", val_cite=TC_TOSS,
    asof="2022-12-19", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("Viva Republica"),
    entry_date="2018-12", country="KR", country_src="web_verified", country_cite=TC_TOSS, city="Seoul",
    city_src="web_verified", focus="Fintech & Payments", flags=("stale",),
    note="Viva Republica, operator of the Toss super-app, Seoul (TechCrunch). 'In 2018, the company became a unicorn "
         "after raising $80 million in a funding round led by Kleiner Perkins and Ribbit Capital' (Wikipedia); the "
         "earlier backers Wikipedia names (Altos, PayPal, Sequoia China, GIC) do not include Ribbit, and Ribbit's "
         "January 2018 archived page does not list Toss. A late round at a $1.2B valuation reads Growth. Mark: the "
         "Series G of December 2022 at KRW 9.1 trillion (TechCrunch, 2022-12-19); KRW 9100.00B @ ECB 2022-12-19 "
         "(KRW/EUR 1377.17, EUR/USD 1.0598) = $7.00B, older than 24 months. Still private: the planned US listing was "
         "put on hold in July 2026 (Seoul Economic Daily).",
    rounds=[rnd("2018-12", "Unnamed ($1.2B valuation)", 80000000, "Kleiner Perkins; Ribbit Capital", True,
                W("Viva Republica"), "press"),
            rnd("2022-12", "Series G", 405000000, "Tonic Private Equity", None, TC_TOSS, "press")], extra=WV))

# ---------------------------------------------------------------- Ualá
UALA_A = "https://www.ua.la/prensa/argentine-fintech-uala-raises-10m-in-series-a-founding"
LAVCA_UALA = "https://www.lavca.org/goldman-sachs-leads-us34m-round-in-argentine-mobile-banking-app-uala/"
TC_UALA_D = "https://techcrunch.com/2021/08/13/argentine-fintech-uala-lands-350m-at-a-2-45b-valuation/"
LL_UALA_E = NEWS("uala", "Ualá raises $300M Series E")
BAT_UALA = NEWS("uala", "Ualá reaches US$3.2-billion valuation")
L.append(cls("uala", status="private", rng="1b_plus", usd=3200000000, val_src="web_verified", val_cite=BAT_UALA,
    asof="2026-03-04", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LAVCA_UALA,
    entry_date="2018-10", country="AR", country_src="web_verified", country_cite=UALA_A, city="Buenos Aires",
    city_src="web_verified", focus="Fintech & Payments",
    note="Argentine digital bank based in Buenos Aires (the company's release). The $10M Series A announced 2018-02-06 "
         "was led by Soros Fund Management with Jefferies and Point72, and the company's release does not name Ribbit; "
         "Ribbit is named in the $34M Series B led by Goldman Sachs (LAVCA, 2018-10-03), its entry. Ribbit followed "
         "through its UA-D vehicle in the 2021 Series D. Mark: the $195M equity round led by Allianz X at $3.2B "
         "(Buenos Aires Times, 2026-03-04), up from $2.75B at the 2024 Series E.",
    rounds=[rnd("2018-02", "Series A", 10000000, "Soros Fund Management", False, UALA_A, "company"),
            rnd("2018-10", "Series B", 34000000, "Goldman Sachs Investment Partners", True, LAVCA_UALA, "press"),
            rnd("2021-08", "Series D", 350000000, "SoftBank; Tencent", True, TC_UALA_D, "press"),
            rnd("2024-11", "Series E", 300000000, "Allianz X", None, LL_UALA_E, "press"),
            rnd("2026-03", "Unnamed equity round", 195000000, "Allianz X", None, BAT_UALA, "press")], extra=WV))

# ---------------------------------------------------------------- Uniswap
UNI_A = "https://blog.uniswap.org/uniswap-raise"
TC_UNI = NEWS("uniswap", "Uniswap Labs valued at $1.66 billion in $165 million")
L.append(cls("uniswap", status="private", rng="1b_plus", usd=1660000000, val_src="web_verified", val_cite=TC_UNI,
    asof="2022-10-13", stage="undetermined", country="US", city="New York", focus="Crypto & Web3", flags=("stale",),
    note="Uniswap Labs, developer of the Uniswap protocol (New York; aligned with the a16z and USV rows). Ribbit's round "
         "is not on record: Uniswap's own Series A post (August 2020, $11M led by a16z) and the Series B coverage "
         "(TechCrunch and CoinDesk, October 2022, $165M led by Polychain) do not name Ribbit, and Ribbit's archive "
         "lists Uniswap from August 2022, before the Series B. Fortune's 2026 Crypto 100 entry for Ribbit names "
         "Uniswap as a holding without a round. Stage undetermined; the record does not show a token purchase "
         "either, so no token_funded flag. Mark: the Series B at $1.66B (TechCrunch, 2022-10-13), aligned with the "
         "sibling rows, older than 24 months; no equity round since.",
    rounds=[rnd("2020-08", "Series A", 11000000, "Andreessen Horowitz", None, UNI_A, "company"),
            rnd("2022-10", "Series B", 165000000, "Polychain Capital", None, TC_UNI, "press")], extra=WV))

# ---------------------------------------------------------------- Upgrade
USV_UPG = "https://www.usv.com/writing/2017/04/upgrade/"
FIN_UPG = NEWS("upgrade", "Upgrade Raises $165 Million, Sees Valuation Rise")
L.append(cls("upgrade", status="private", rng="1b_plus", usd=7300000000, val_src="web_verified", val_cite=FIN_UPG,
    asof="2025-10-16", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=USV_UPG,
    entry_date="2017-04", country="US", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    note="Consumer credit and neobank, San Francisco (Wikipedia). USV's own post on the April 2017 round: 'We are "
         "excited to be Series A investors in this new venture, along with our friends at VY Capital, Sands Capital, "
         "FirstMark Capital, Ribbit Capital, Silicon Valley Bank and others'; the $60M Series A was Upgrade's first "
         "institutional round (Wikipedia), so Ribbit entered at the Series A. Ribbit followed through its UP-F vehicle "
         "in the November 2021 Series F and took part in the Series G as an existing shareholder (Wikipedia). Mark: "
         "the $165M Series G at $7.3B (Finovate, 2025-10-16), aligned with Coatue's row; USV's row carries the older "
         "$6.28B, same band. Private: an IPO is targeted, not filed.",
    rounds=[rnd("2017-04", "Series A", 60000000, None, True, USV_UPG, "press"),
            rnd("2021-11", "Series F", 280000000, "Coatue; DST Global", True, SPV("UP-F"), "filing"),
            rnd("2025-10", "Series G", 165000000, "Neuberger Berman", True, W("Upgrade, Inc."), "press")],
    extra=WV))

# ---------------------------------------------------------------- Vise (stage prefilled: Growth, formd_band)
RIABIZ_VISE = NEWS("vise", "Vise falls way short")
II_VISE = NEWS("vise", "Vise Valued at More Than")
L.append(cls("vise", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=RIABIZ_VISE,
    asof="2021-05", city="New York", city_src="web_verified", focus="Fintech & Payments", flags=("stale",),
    note="AI-driven portfolio management for financial advisors, New York City (RIABiz). Ribbit led the $65M Series C "
         "of May 2021 (Institutional Investor; RIABiz has Sequoia and Ribbit), which matches the prefilled Growth "
         "entry from the 2021 Form D. Mark: the Series C 'based on a $1 billion valuation' (RIABiz, 2021-06-08), "
         "exactly on the $1B edge and older than 24 months; the 2023 reset (Business Insider) carries no priced round, "
         "so the mark stands. Aligned with Sequoia's row.",
    rounds=[rnd("2021-05", "Series C", 65000000, "Ribbit Capital", True, II_VISE, "press")], extra=WV))

# ---------------------------------------------------------------- Vouch (stage prefilled: Series A, formd_band)
L.append(cls("vouch", status="private", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
    note="Vouch Insurance, business insurance for startups founded by Sam Hodges, San Francisco. Operating and private: "
         "it raised $25M in a round led by Ribbit in March 2024 (FinTech Global), and in August 2025 agreed to sell "
         "its MGA (Corix) and its carrier subsidiary to Hiscox USA, subject to regulatory approval, while Vouch "
         "continues as an independent broker (Coverager). No valuation at or above $1B found. First Round's 'Vouch' "
         "(a 2015 social-lending startup) is another company; Y Combinator's 'Vouch' (Summer 2019, Chicago) carries a "
         "defunct status copied from First Round's row, a possible misalignment if it is this company."))

# ---------------------------------------------------------------- Warren
PT_WARREN = "https://pt.wikipedia.org/wiki/Warren_Investimentos"
LAVCA_WARREN = ("https://www.lavca.org/ribbit-capital-leads-r25m-investment-in-brazil-based-digital-brokerage-"
                "warren-em-portugues/")
NEOFEED_WARREN = ("https://neofeed.com.br/wealth-management/warren-e-vendida-para-plataforma-de-investimentos-"
                  "argentina-cocos-capital/en/")
L.append(cls("warren", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=PT_WARREN, entry_date="2019-03", country="BR", country_src="web_verified",
    country_cite=PT_WARREN, city="Porto Alegre", city_src="web_verified", focus="Fintech & Payments",
    note="Warren Investimentos, Brazilian digital investment platform, headquartered in Porto Alegre (Portuguese "
         "Wikipedia). Ribbit led Warren's first institutional round, R$25M in March 2019 with Kaszek and Chromo Invest "
         "(LAVCA, 2019-03-28), which Wikipedia names the Series A; BRL 25.0M @ ECB 2019-03-28 (BRL/EUR 4.4592, EUR/USD "
         "1.1218) = $6.3M. QED led the R$120M Series B (2020) and GIC the R$300M Series C (2021). Cocos Capital "
         "(Argentina) agreed in 2026 to buy Warren's brokerage (Warren Rena), asset management and capital markets "
         "operations, terms undisclosed, with closing subject to Brazilian regulatory approval (NeoFeed; Valor "
         "International, 2026-07-02); a signed, unclosed sale is not a status change, so the row stays private. No "
         "priced valuation at or above $1B found (the 'R$20 billion' figures are assets under custody).",
    rounds=[rnd("2019-03", "Series A", 6289245, "Ribbit Capital", True, LAVCA_WARREN, "press"),
            rnd("2020", "Series B", None, "QED Investors", None, PT_WARREN, "press"),
            rnd("2021", "Series C", None, "GIC", None, PT_WARREN, "press")]))

# ---------------------------------------------------------------- Wave
FTG_WAVE = NEWS("wave", "Wave closes largest Series A round for an African FinTech at")
TC_WAVE = NEWS("wave", "Wave, a Stripe-backed African fintech")
L.append(cls("wave", status="private", rng="1b_plus", usd=1700000000, val_src="web_verified", val_cite=FTG_WAVE,
    asof="2021-09-07", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FTG_WAVE,
    entry_date="2021-09", country="SN", country_src="web_verified", country_cite=TC_WAVE, city="Dakar",
    focus="Fintech & Payments", flags=("model_disputes_source", "stale"),
    note="Wave Mobile Money, mobile money across francophone West Africa, Senegal-based (TechCrunch, 2022). Its first "
         "priced round, the $200M Series A of September 2021 led by Sequoia Heritage and Founders Fund with Stripe and "
         "Ribbit, valued it at $1.7B (FinTech Global, 2021-09-07); Ribbit's archive lists Wave from 2022. The "
         "prefilled acquired status rides an SEC filer match on another Wave (cik_weak), disputed: the company "
         "operates (a EUR 117M debt facility in July 2025, TechAfrica News) and is private. The 2025 facility is debt, "
         "so the Series A mark stands, older than 24 months; aligned with Y Combinator's row. a16z's 'Wave' row is an "
         "unresolved different company.",
    rounds=[rnd("2021-09", "Series A", 200000000, "Sequoia Heritage; Founders Fund", True, FTG_WAVE, "press")],
    extra=WV))

# ---------------------------------------------------------------- Wealthfront (public)
TC_WF = NEWS("wealthfront", "Wealthfront Raises $35M From Index")
SA_WLTH = "https://stockanalysis.com/stocks/wlth/market-cap/"
L.append(cls("wealthfront", rng="1b_plus", usd=1560000000, val_src="web_verified", val_cite=SA_WLTH,
    asof="2026-09-28", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=TC_WF,
    entry_date="2014-04", city="Palo Alto", city_src="web_verified", focus="Fintech & Payments",
    note="Automated investing and cash management, Palo Alto (Wikipedia). Ribbit co-led the $35M round of April 2014 "
         "with Index Ventures (TechCrunch, 2014-04-02; Wikipedia adds Benchmark); TechCrunch names Social+Capital, "
         "Greylock and DAG as existing investors and Index as the 2013 round's lead, so this later round is Ribbit's "
         "entry and reads Growth (the source gives no series letter). Ribbit Capital II, L.P. appears among the "
         "investors in Wealthfront's 2025 registration statement (EDGAR full text). Public on Nasdaq since December "
         "2025: the prefilled $0 float predates the listing, so the row is pinned by market cap, $1.56B on 2026-09-28 "
         "(stockanalysis), same band as the Greylock and Spark rows.",
    rounds=[rnd("2014-04", "Unnamed", 35000000, "Index Ventures; Ribbit Capital", True, TC_WF, "press")],
    extra=WV))

# ---------------------------------------------------------------- Xapo (stage prefilled: Series A, formd_band)
L.append(cls("xapo", status="private", rng="below_1b", city="Gibraltar", city_src="web_verified",
    focus="Crypto & Web3", flags=("city_country_conflict",),
    note="Xapo Bank, a bitcoin-focused private bank headquartered in Gibraltar under a Gibraltar licence (Wikipedia); "
         "the headquarters moved from Palo Alto to Zug in 2015 and the institutional custody business went to "
         "Coinbase in 2019. Ribbit joined the $20M Series A of March 2014 led by Benchmark (Wikipedia), which matches "
         "the prefilled Series A from the Form D. Operating in 2026 (Crowdfund Insider, August 2026). No priced round "
         "at or above $1B found. Country: Gibraltar (GI) is missing from the pipeline's ISO table, so the row keeps "
         "the filing's US with city_country_conflict, as Greylock's row does; the correction is Erik's call.",
    rounds=[rnd("2014-03", "Series A", 20000000, "Benchmark", True, W("Xapo Bank"), "press")]))

# ---------------------------------------------------------------- Aave
AAVE_CG = "https://www.coingecko.com/en/coins/aave"
DL_AAVE = NEWS("aave", "Inside Aave founder")
L.append(cls("aave", status="private", rng="1b_plus", usd=2284530899, val_src="web_verified", val_cite=AAVE_CG,
    asof="2026-09-28", stage="undetermined", country="GB", country_src="web_verified", country_cite=DL_AAVE,
    city="London", city_src="web_verified", focus="Crypto & Web3",
    note="Aave Labs (Aave Companies, then Avara), developer of the Aave lending protocol founded in 2017 as ETHLend "
         "(Wikipedia); its parent company is based in London (DL News, 2024-07-05), matching the firm's own 'United "
         "Kingdom' label on the archived Our Bets page (2022-2025). A member under the issuing organisation "
         "(decisions.md D2). No Aave financing read names Ribbit (Google News for Aave with Ribbit returns only Morpho "
         "items), so the entry round is undetermined, and the record does not show a token purchase, so no "
         "token_funded flag. Band on the AAVE token network cap, $2.28B on CoinGecko on 2026-09-28, the basis the "
         "a16z and Bain Capital Ventures books use for protocol rows with no equity mark (Solana, NEAR, Avalanche, "
         "World); no Aave Labs equity valuation was found.",
    rounds=[], extra=WV))

# ---------------------------------------------------------------- AIUC
YH_AIUC = NEWS("aiuc", "AIUC raises $40M Series A from Ribbit")
IJ_AIUC = NEWS("aiuc", "AIUC Emerges From Stealth")
L.append(cls("aiuc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=YH_AIUC, entry_date="2026-09", country="US", city="San Francisco",
    city_src="web_verified", focus="Fintech & Payments",
    note="AIUC (the Artificial Intelligence Underwriting Company), insurance and a certification standard for AI "
         "agents, headquartered in San Francisco. Ribbit led the $40M Series A of September 2026 with First Harmonic "
         "(the company's release on Yahoo Finance, 2026-09-15); the $15M seed of July 2025 was led by Nat Friedman's "
         "NFDG and its investor list does not include Ribbit (Insurance Journal). Valuation undisclosed; momentum "
         "check: no round at or above $1B found, news sweep 2026-09-28.",
    rounds=[rnd("2025-07", "Seed", 15000000, "NFDG", False, IJ_AIUC, "press"),
            rnd("2026-09", "Series A", 40000000, "Ribbit Capital", True, YH_AIUC, "company")]))

# ---------------------------------------------------------------- Alpen Labs
TB_ALPEN = NEWS("alpen-labs", "Bitcoin scaling developer Alpen Labs comes out of stealth")
L.append(cls("alpen-labs", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_conf="high", stage_cite=TB_ALPEN, entry_date="2023", country="US", focus="Crypto & Web3",
    flags=("city_unknown",),
    note="Alpen Labs, Bitcoin scaling and Bitcoin-native finance developer. 'The venture firm Ribbit Capital led a seed "
         "funding round for Alpen in 2023' ($10.6M with Castle Island, Geometry, Stillmark, Robot Ventures and others; "
         "The Block, 2024-04-10). No later priced round found in the news sweep of 2026-09-28; Graduation left for the "
         "graduation pass. No source read places the company (The Block, its own site): city unknown, the country US "
         "from model knowledge. Momentum check: no round at or above $1B found.",
    rounds=[rnd("2023", "Seed", 10600000, "Ribbit Capital", True, TB_ALPEN, "press")]))

# ---------------------------------------------------------------- Antora Energy
PULSE_ANTORA = NEWS("antora-energy", "Antora Energy Raises $550 Million In Series C Funding Co-Led")
FS_ANTORA_B = NEWS("antora-energy", "Antora Energy Raises $150M in Series B")
L.append(cls("antora-energy", status="private", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=PULSE_ANTORA, entry_date="2026-07", country="US", city="San Jose", city_src="web_verified",
    focus="Climate & Energy", flags=("needs_web_value",),
    note="Thermal battery maker, San Jose (Pulse 2.0; Crunchbase News). Ribbit is named among the new investors in the "
         "$550M Series C of July 2026, co-led by G2 Venture Partners and Eclipse (Pulse 2.0, 2026-08-02), its entry. "
         "The company did not disclose the valuation (Crunchbase News, 2026-07-30); a $550M round points to $1B or more "
         "but no figure exists, so the row carries needs_web_value for the web pass instead of a band.",
    rounds=[rnd("2024-02", "Series B", 150000000, None, False, FS_ANTORA_B, "press"),
            rnd("2026-07", "Series C", 550000000, "G2 Venture Partners; Eclipse", True, PULSE_ANTORA, "press")]))

# ---------------------------------------------------------------- Aside (Aside, Inc. = the company behind Daffy)
FIN_DAFFY = NEWS("aside", "Charitable Giving App Daffy Secures")
L.append(cls("aside", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=FIN_DAFFY, entry_date="2022-02", country="US", city="San Francisco",
    city_src="web_verified", focus="Fintech & Payments",
    note="Aside, Inc. is the company behind the charitable giving app Daffy: 'Aside, the company behind charitable "
         "giving app Daffy, has secured $17.1 million in Series A funding', led by Ribbit (Finovate, 2022-02-09; San "
         "Francisco), and daffy.org's footer reads 'Powered by Aside'. This row and the daffy row are one company "
         "(two listings on the firm's archived Our Bets page). Momentum check: no round at or above $1B found, news "
         "sweep 2026-09-28. Y Combinator's 'Aside' (a Fall 2025 agentic browser) is another company.",
    rounds=[rnd("2022-02", "Series A", 17100000, "Ribbit Capital", True, FIN_DAFFY, "press")]))

# ---------------------------------------------------------------- Atlantic Money
TFN_ATL = NEWS("atlantic-money", "Launched by Rohinhood alumni")
FIN_ATL = NEWS("atlantic-money", "Deel Acquires Atlantic Money")
L.append(cls("atlantic-money", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_conf="high", stage_cite=TFN_ATL, entry_date="2022-03", country="GB", country_src="web_verified",
    country_cite=FIN_ATL, city="London", focus="Fintech & Payments",
    note="UK money-transfer app founded by Robinhood alumni. Amplo and Ribbit co-led the $4.5M seed (Tech Funding News, "
         "2022-03-09). Deel acquired it for an undisclosed sum (Finovate, 2024-12-02: 'Deel has acquired U.K.-based "
         "international funds transfer company Atlantic Money'). No later round found before the sale; Graduation left "
         "for the graduation pass.",
    rounds=[rnd("2022-03", "Seed", 4500000, "Amplo; Ribbit Capital", True, TFN_ATL, "press")]))

# ---------------------------------------------------------------- Avant (band prefilled)
GA_AVANT = NEWS("avant", "Avant Announces $325 Million Series E")
L.append(cls("avant", stage="undetermined", city="Chicago", city_src="web_verified", focus="Fintech & Payments",
    note="Online consumer lender, Chicago (the Series E release on General Atlantic's site). Ribbit's round is not on "
         "record: the $325M Series E of September 2015 names General Atlantic, Balyasny, J.P. Morgan, Tiger Global, "
         "August Capital, RRE and DFJ Growth, not Ribbit, and Ribbit's archive lists Avant from November 2015. Stage "
         "undetermined. The prefilled $1.98B comes from the unicorn snapshot (2015), not a cited priced round; left "
         "to the A/B pass.",
    rounds=[rnd("2015-09", "Series E", 325000000, "General Atlantic", None, GA_AVANT, "company")]))

# ---------------------------------------------------------------- axio and Capital Float (one company)
IR_CF = NEWS("capital-float", "Amazon In Talks With Capital Float")
KNN_CF = NEWS("capital-float", "Amazon to invest $22 million in MSME lender")
ET_CF = NEWS("capital-float", "Digital financial firm Capital Float rebrands")
ET_AXIO = NEWS("axio", "Amazon completes $200 million cash acquisition")
AXIO_ROUNDS = [rnd("2017", "Series C", 45000000, "Ribbit Capital", True, IR_CF, "press"),
               rnd("2018-04", "Series C (continued)", 22000000, "Amazon", None, KNN_CF, "press")]
AXIO_NOTE = ("the Indian lending and BNPL company Capital Float, renamed axio in July 2022 (The Economic Times). "
             "Ribbit's first round was Capital Float's $45M Series C, 'led by Silicon Valley-based Ribbit Capital, "
             "with participation from existing investors SAIF Partners, Sequoia India and Creation Investments' "
             "(Indian Retailer, December 2017); Amazon continued the Series C with $22M in 2018 (KNN India). Amazon "
             "completed its roughly $200M cash acquisition in September 2025 (The Economic Times, 2025-09-04). "
             "Bengaluru, written Bangalore (Indian Retailer).")
L.append(cls("axio", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=IR_CF, entry_date="2017", country="IN", country_src="web_verified", country_cite=IR_CF,
    city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    note="axio, " + AXIO_NOTE + " This row and capital-float are one company. Accel's 'Axio' (a US company in "
         "Cambridge) is another company: name collision, not aligned.", rounds=AXIO_ROUNDS))
L.append(cls("capital-float", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=IR_CF, entry_date="2017", country="IN", country_src="web_verified",
    country_cite=IR_CF, city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    note="Capital Float, " + AXIO_NOTE + " The acquisition closing is cited to " + ET_AXIO + ". This row and axio are "
         "one company (the firm linked capitalfloat.com 2017-2025 and lists axio.co.in today).",
    rounds=AXIO_ROUNDS))

# ---------------------------------------------------------------- Ballet
CD_BALLET = NEWS("ballet", "Bobby Lee Returns With Ballet")
L.append(cls("ballet", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=CD_BALLET, entry_date="2019-09", country="US", city="Las Vegas", city_src="web_verified",
    focus="Crypto & Web3",
    note="Ballet, crypto hardware wallets, founded by BTCC's Bobby Lee. It 'has raised an undisclosed amount of capital "
         "in a seed round backed by Ribbit Capital' and has 'a global headquarters in Las Vegas' (CoinDesk, "
         "2019-09-12). No later priced round found in the news sweep of 2026-09-28; Graduation left for the graduation "
         "pass. The product is still sold and reviewed in 2025-2026 (99Bitcoins), so the status reads private.",
    rounds=[rnd("2019-09", "Seed", None, None, True, CD_BALLET, "press")]))

# ---------------------------------------------------------------- Base Power
TC_BASE_B = "https://techcrunch.com/2025/04/09/a16z-backs-base-power-in-200m-round-for-home-backup-batteries/"
TC_BASE_C = NEWS("base-power", "Base Power raises $1B to deploy home batteries")
PULSE_BASE = NEWS("base-power", "Base Power Raises $1 Billion Series D At $13 Billion")
L.append(cls("base-power", status="private", rng="10b_plus", usd=13000000000, val_src="web_verified",
    val_cite=PULSE_BASE, asof="2026-08-03", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=TC_BASE_C, entry_date="2025-10", country="US", city="Austin", city_src="web_verified",
    focus="Climate & Energy",
    note="Home batteries and power retail, Austin (TechCrunch). Ribbit's first round is the $1B Series C of October "
         "2025, led by Addition with CapitalG, Elad Gil, Lightspeed, Ribbit, Thrive and Valor, at $3B pre-money "
         "(TechCrunch, 2025-10-08); the April 2025 $200M Series B names no Ribbit (TechCrunch). Ribbit then co-led the "
         "$1B Series D at $13B post-money with Addition, Valor and JPMorganChase (Pulse 2.0, 2026-08-03). Mark aligned "
         "with the a16z, Lightspeed and Spark rows.",
    rounds=[rnd("2025-04", "Series B", 200000000, "Addition; Andreessen Horowitz; Lightspeed; Valor", False,
                TC_BASE_B, "press"),
            rnd("2025-10", "Series C", 1000000000, "Addition", True, TC_BASE_C, "press"),
            rnd("2026-08", "Series D", 1000000000, "Ribbit Capital; Addition; Valor; JPMorganChase", True,
                PULSE_BASE, "press")], extra=WV))

# ---------------------------------------------------------------- Blockaid
CAL_BLOCK = NEWS("blockaid", "Web3 security startup Blockaid raises $27 million Series A")
FT_BLOCK = NEWS("blockaid", "Tel Aviv–based Blockaid raises $33 million")
BB_BLOCK = NEWS("blockaid", "Blockaid: Ribbit Leads $50 Million")
L.append(cls("blockaid", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=CAL_BLOCK, entry_date="2023-10", country="IL", country_src="web_verified",
    country_cite=FT_BLOCK, city="Tel Aviv", city_src="web_verified", focus="Security",
    note="Onchain transaction security, Tel Aviv (Fortune). Ribbit and Variant led the $27M Series A of October 2023 "
         "with Cyberstarts, Sequoia and Greylock (Calcalist, 2023-10-23); the earlier seed of about $6M is credited to "
         "Sequoia, Greylock and Cyberstarts on Greylock's row, not to Ribbit, so Ribbit entered at the Series A. Ribbit "
         "led the $50M Series B of February 2025 (Bloomberg). Momentum check: no round at or above $1B found, news "
         "sweep 2026-09-28. Aligned with the Greylock and Sequoia rows.",
    rounds=[rnd("2023-10", "Series A", 27000000, "Ribbit Capital; Variant", True, CAL_BLOCK, "press"),
            rnd("2025-02", "Series B", 50000000, "Ribbit Capital", True, BB_BLOCK, "press")]))

# ---------------------------------------------------------------- bonify
TEU_BONIFY = "https://tech.eu/2017/02/21/bonify-raises-funding/"
TEU_SCHUFA = NEWS("bonify", "Schufa absorbs German fintech Forteil")
L.append(cls("bonify", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=TEU_BONIFY, entry_date="2017-02", country="DE", country_src="web_verified",
    country_cite=TEU_BONIFY, city="Berlin", focus="Fintech & Payments",
    note="bonify (Forteil GmbH), consumer credit-score and personal finance app, Berlin. The EUR 5.5M Series A 'was led "
         "by London's Mosaic Ventures and Ribbit Capital, with participation from Index Ventures, DN Capital, HW "
         "Capital' (Tech.eu, 2017-02-21); EUR 5.5M @ ECB 2017-02-21 (EUR/USD 1.0537) = $5.8M. SCHUFA acquired Forteil "
         "in December 2022 for an undisclosed price (Tech.eu, 2022-12-21: 'Schufa absorbs German fintech Forteil'), "
         "and SCHUFA has run the bonify app since.",
    rounds=[rnd("2017-02", "Series A", 5795350, "Mosaic Ventures; Ribbit Capital", True, TEU_BONIFY, "press"),
            rnd("2019", "Series C", None, None, None, TEU_SCHUFA, "press")]))

# ---------------------------------------------------------------- Borro
DB_BORRO = NEWS("borro", "What Happened to Borro")
L.append(cls("borro", status="acquired", rng="below_1b", stage="undetermined", city="London",
    focus="Fintech & Payments",
    note="Borro, online lender against luxury assets, founded in London. Ribbit listed it on its 2012-2014 Bets pages, "
         "but no source read names Ribbit's round (deBanked names Victory Park, Canaan, Eden Ventures and Augmentum "
         "among its backers): stage undetermined. The business failed: Victory Park took it over through "
         "administration in November 2017 and it stopped new lending in 2019 (deBanked, 2019-10), then Luxury Asset "
         "Capital bought and relaunched Borro in February 2020 (Business Wire; Wikipedia). Insolvency followed by a "
         "sale reads acquired. City: London, the last headquarters of the company Ribbit backed; the relaunched US "
         "brand sits inside Luxury Asset Capital. Cited: " + DB_BORRO + " and " + W("Borro") + ".",
    rounds=[]))

# ---------------------------------------------------------------- Breezy
PULSE_BREEZY = NEWS("breezy", "Breezy: $10 Million Pre-Seed Funding")
L.append(cls("breezy", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified",
    stage_conf="high", stage_cite=PULSE_BREEZY, entry_date="2026-02", country="US", city="Los Angeles",
    city_src="web_verified", focus="AI & Applied AI",
    note="Breezy, an AI operating system for residential real estate agents; 'The Los Angeles-based startup was founded "
         "in early 2024' (Pulse 2.0). Ribbit led the $10M pre-seed with Fifth Wall, DST Global Partners, Liquid 2 and "
         "others (Pulse 2.0, 2026-02-02); the source names the round pre-seed, so the stage is Pre-Seed and the row "
         "takes no S2A. Momentum check: no round at or above $1B found, news sweep 2026-09-28. Felicis's 'Breezy' (a "
         "2017 seed, SaaS) is another company.",
    rounds=[rnd("2026-02", "Pre-Seed", 10000000, "Ribbit Capital", True, PULSE_BREEZY, "press")]))

# ---------------------------------------------------------------- BTCJam
FIN_BTCJAM = NEWS("btcjam", "BTCJam: P2P Lending via Bitcoin")
L.append(cls("btcjam", status="defunct", rng="below_1b", stage="undetermined", city="San Francisco",
    focus="Crypto & Web3",
    note="Bitcoin peer-to-peer lending platform (founders in Brazil and San Francisco, Finovate 2013). It 'received "
         "investments from Ribbit Capital, Foundation Capital, Pantera Capital' (Wikipedia) and Micky Malka named it "
         "among Ribbit's four bitcoin investments in March 2014 (CoinDesk). In November 2013 it was raising about $1M "
         "on AngelList (Finovate), but no source ties Ribbit to that or any named round: stage undetermined. It shut "
         "down entirely in 2017 (Wikipedia): defunct.",
    rounds=[rnd("2013-11", "Seed raise on AngelList (in progress)", None, None, None, FIN_BTCJAM, "press")]))

# ---------------------------------------------------------------- Campfire
PRN_CF_A = NEWS("campfire", "Campfire Raises $35 Million Series A Led by Accel")
PRN_CF_B = NEWS("campfire", "Campfire Raises $65 Million Series B")
L.append(cls("campfire", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=PRN_CF_B, entry_date="2025-10", country="US", city="San Francisco",
    city_src="web_verified", focus="Fintech & Payments", flags=("model_disputes_source",),
    note="Campfire, AI-native ERP and accounting software (John Glasgow), headquartered in San Francisco (its Series A "
         "release). Ribbit co-led the $65M Series B of October 2025 with Accel as a new partner (the company's release, "
         "2025-10-15); the $35M Series A of June 2025 was led by Accel and does not name Ribbit. Valuation undisclosed; "
         "momentum check: no round at or above $1B found, news sweep 2026-09-28. The prefilled Japan (JP) is a "
         "Wikidata namesake, disputed; aligned with the Accel and Y Combinator rows (San Francisco, US).",
    rounds=[rnd("2025-06", "Series A", 35000000, "Accel", False, PRN_CF_A, "company"),
            rnd("2025-10", "Series B", 65000000, "Accel; Ribbit Capital", True, PRN_CF_B, "company")]))

# ---------------------------------------------------------------- CAN Capital
MD_CAN = NEWS("can-capital", "CAN Capital Acquires Equipment Finance Platform")
L.append(cls("can-capital", status="private", rng="below_1b", stage="undetermined", country="US", city="Atlanta",
    city_src="web_verified", focus="Fintech & Payments",
    note="CAN Capital (Capital Access Networks), small-business financing since 1998. Ribbit listed it on its 2012-2018 "
         "pages, but no source read names Ribbit's round: stage undetermined. Operating and private in 2026: it bought "
         "an equipment-finance platform from Republic Bank, and its release says it is 'headquartered in Atlanta' "
         "(MonitorDaily, 2026-02-23, " + MD_CAN + "); Accel's row carries Kennesaw, the Atlanta-area office it moved "
         "its executive functions to in 2018 (deBanked, 2019). No valuation at or above $1B found.",
    rounds=[]))

# ---------------------------------------------------------------- Castle Technologies
CASTLE = "https://castle.tech/"
L.append(cls("castle-technologies", status="private", rng="below_1b", stage="undetermined", country="US",
    focus="Fintech & Payments", flags=("model_disputes_source", "city_unknown"),
    note="Castle Technologies (castle.tech) turns business risks into tradeable event contracts on regulated venues; "
         "its site names Ribbit Capital and Jump Trading as its backers and shows it operating in August 2026 "
         "(" + CASTLE + "). The prefilled acquired status comes from an SEC filer match on another Castle (cik_weak), "
         "disputed: private. No round naming Ribbit found in the news sweep (2026-09-28): stage undetermined; "
         "momentum check: no round at or above $1B found. No source read places the company (its site gives no "
         "address): city unknown, the country US from model knowledge. The First Round and Khosla rows named Castle "
         "(account-takeover security; property management) are other companies.",
    rounds=[]))

# ---------------------------------------------------------------- Chipper Cash
PC_CHIP_A = NEWS("chipper-cash", "Chipper Cash Closes a UGX51.6")
TN_CHIP_B = NEWS("chipper-cash", "Chipper Cash Raises $30m in Series B")
TCB_CHIP = NEWS("chipper-cash", "Chipper Cash valued at $2 billion after investment from FTX")
TC_CHIP_FTX = NEWS("chipper-cash", "FTX marked down Chipper")
WT_CHIP = NEWS("chipper-cash", "Chipper Cash Reportedly Cut Its Valuation")
L.append(cls("chipper-cash", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=TN_CHIP_B, entry_date="2020-11", country="US", city="San Francisco",
    focus="Fintech & Payments",
    note="Chipper Cash, cross-border payments across Africa, San Francisco headquarters. Ribbit led the $30M Series B "
         "of November 2020 with Bezos Expeditions (Technext24, 2020-11-19); the $13.8M Series A of June 2020 was led by "
         "Deciens Capital and the report names no Ribbit (PC Tech Magazine). The FTX-led Series C extension of "
         "November 2021 valued it at about $2B (TechCabal). Collapse evidence rules the row below $1B: FTX marked its "
         "stake down to $1.25B in December 2022 (TechCrunch), and in 2023 the internal valuation was cut by 70% from "
         "$2.2B while sale talks with Zepz valued it at $250M to $500M (WeeTracker, 2023-08-17, " + WT_CHIP + "); no "
         "priced round since. For review: the evidence is a reported internal cut and a failed sale, not a priced "
         "round.",
    rounds=[rnd("2020-06", "Series A", 13800000, "Deciens Capital", None, PC_CHIP_A, "press"),
            rnd("2020-11", "Series B", 30000000, "Ribbit Capital", True, TN_CHIP_B, "press"),
            rnd("2021-11", "Series C extension", 150000000, "FTX", None, TCB_CHIP, "press")]))

# ---------------------------------------------------------------- Cognition
COG_BLOG = NEWS("cognition", "More Devins in More Places")
TC_COG48 = ("https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-"
            "is-far-from-a-winner-take-all-market/")
L.append(cls("cognition", status="private", rng="10b_plus", usd=48000000000, val_src="web_verified",
    val_cite=TC_COG48, asof="2026-09-08", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=COG_BLOG, entry_date="2026-05", country="US", city="San Francisco", city_src="web_verified",
    focus="AI & Applied AI",
    note="Cognition AI, maker of the Devin coding agent, headquartered in San Francisco (Wikipedia). Ribbit's first "
         "round is the over-$1B Series D at $26B of May 2026, where the company's own post welcomes 'new investors "
         "including Ribbit Capital, Atreides, and Layer Global' (cognition.com, 2026-05-27). Mark: the $2B Series E "
         "at $48B (TechCrunch, 2026-09-08), matching Bain Capital Ventures' row; the 8VC, General Catalyst, Khosla "
         "and Lux rows still carry the $10.2B of September 2025 (same band).",
    rounds=[rnd("2026-05", "Series D", 1000000000, "Lux Capital; General Catalyst; 8VC", True, COG_BLOG, "company"),
            rnd("2026-09", "Series E", 2000000000, "Andreessen Horowitz; Accel; Founders Fund; General Catalyst; "
                "Avenir", None, TC_COG48, "press")], extra=WV))

# ---------------------------------------------------------------- CoPlane
PY_COPLANE = NEWS("coplane", "CoPlane Raises $14 Million to Build")
L.append(cls("coplane", status="private", rng="below_1b", stage="Seed", stage_src="web_verified",
    stage_conf="high", stage_cite=PY_COPLANE, entry_date="2025-11", grad="censored", country="US",
    focus="AI & Applied AI", flags=("city_unknown",),
    note="CoPlane (Chris Sperandio), AI-native software that automates enterprise back-office work on top of ERP "
         "systems. Ribbit led the $14M seed announced 2025-11-25 (PYMNTS, quoting Ribbit partner Jordan Angelos). "
         "Inside the 24-month window: censored. Momentum check: no round at or above $1B found, news sweep 2026-09-28. "
         "No source read places the company (PYMNTS, its own site): city unknown, the country US from model knowledge.",
    rounds=[rnd("2025-11", "Seed", 14000000, "Ribbit Capital", True, PY_COPLANE, "press")]))

# ---------------------------------------------------------------- Cowboy Space
TC_AETHER = NEWS("cowboy-space", "Space solar startup Aetherflux raises $50M")
TC_COWBOY = NEWS("cowboy-space", "There aren't enough rockets")
L.append(cls("cowboy-space", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
    val_cite=TC_COWBOY, asof="2026-05-11", stage="undetermined", country="US", city="San Carlos",
    city_src="web_verified", focus="Industrial & Robotics",
    note="Cowboy Space Corporation (Aetherflux until May 2026), orbital data centers and launch, founded by Robinhood "
         "co-founder Baiju Bhatt; San Carlos (TechCrunch, 2025). Ribbit's round is not on record: the $50M Series A of "
         "April 2025 (Index and Interlagos, with Breakthrough, a16z and NEA) and the $275M Series B of May 2026 (Index, "
         "with Breakthrough, Construct, IVP and SAIC) do not name Ribbit (TechCrunch), so the stage is undetermined. "
         "Mark: the Series B at a $2B post-money valuation (TechCrunch, 2026-05-11), aligned with IVP's row; a16z's row "
         "still reads below $1B from before that round.",
    rounds=[rnd("2025-04", "Series A", 50000000, "Index Ventures; Interlagos", None, TC_AETHER, "press"),
            rnd("2026-05", "Series B", 275000000, "Index Ventures", None, TC_COWBOY, "press")], extra=WV))

# ---------------------------------------------------------------- Deel
W_DEEL = W("Deel, Inc.")
L.append(cls("deel", rng="10b_plus", usd=17300000000, val_src="web_verified", val_cite=W_DEEL, asof="2025-10",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W_DEEL, entry_date="2025-10",
    country="US", city="San Francisco", focus="SaaS", flags=("model_disputes_source",),
    clear=("unicorn_name_match",),
    note="Deel, global payroll and HR, San Francisco. 'In October 2025, Deel raised a US $300 million Series E funding "
         "round co-led by Ribbit Capital and Andreessen Horowitz, bringing its valuation to approximately US $17.3 "
         "billion' (Wikipedia); Ribbit is not named in the Series A to D or the February 2025 secondary, and the firm's "
         "archived pages never listed Deel, so the Series E is its entry. The prefilled country 'Israel / United "
         "States' is a Wikidata string, not a country code, disputed: US. The $17.3B is re-sourced from the unicorn "
         "snapshot to the cited Series E. Deel also bought Atlantic Money, another Ribbit row, in 2024.",
    rounds=[rnd("2021-10", "Series D", 425000000, "Coatue; DST Global", None, W_DEEL, "press"),
            rnd("2025-02", "Secondary", 300000000, None, None, W_DEEL, "press"),
            rnd("2025-10", "Series E", 300000000, "Ribbit Capital; Andreessen Horowitz", True, W_DEEL, "press")],
    extra=WV))

# ---------------------------------------------------------------- Bank Jago: not a venture position (T3)
TEMPO_JAGO = NEWS("bank-jago", "Bank Jago Shares Gain 75%")
PYMNTS_JAGO = "https://www.pymnts.com/news/investment-tracker/2021/ribbit-capital-invests-in-indonesian-digital-bank-bank-jago/"
L.append(verdict("bank-jago", "not_member",
    "Listed on the Rebels list (Jerry Ng, jago.com), but PT Bank Jago Tbk already traded on the Indonesia Stock "
    "Exchange as ARTO before Ribbit's entry (Tempo, 2021-01-26: ARTO closed at Rp6,825 on 25 January 2021). Ribbit's "
    "position was announced in October 2021 as a minority stake of undisclosed size in the listed bank ('Ribbit "
    "Capital recently bought a minority stake in a Jakarta-based digital bank Bank Jago', PYMNTS, " + PYMNTS_JAGO +
    "; under 5% by other reports), with no venture round. A purchase into an already-listed company with no venture "
    "entry is out (T3; decisions.md D4), as for Futu, Sea and Tinkoff.",
    ec="web", conf="medium", cite=TEMPO_JAGO))

jl.write("batch-003", L)
