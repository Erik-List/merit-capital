"""PRO-161 grind, batch 2 (judge b2): the 43 member rows of queue batch-002 (gorila to settle; robinhood was
already classified and mercado-libre is not_member). Evidence: the judge view (show.py --batch 2), Wikipedia
(wikifetch.py), the Google News sweep and nq.py (tag b2), sibling books, and company and press pages read with
WebFetch (the literal URLs below are pages fetched and read in this pass). Every pre-filled value was checked;
wrong joins are corrected with the flag model_disputes_source and named in the note."""
import importlib.util
import os
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV, FORMD_CITE = (jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W,
                                                           jl.NEWS, jl.SPV, jl.FORMD_CITE)
L = []
WV = {"valuation_range_source": "web_verified"}
SWEEP = "news sweep 2026-09-28"

# ---- pages fetched and read in this pass (company sites, releases, press)
GORILA_SITE = "https://gorila.com.br/"
GORILA_LAVCA = "https://www.lavca.org/ribbit-capital-leads-a-r35m-investment-in-gorila-invest-em-portugues/"
GUIA_EXAME = "https://exame.com/pme/app-que-te-ajuda-a-economizar-r-750-por-mes-recebe-aporte/"
HABITO_A = "https://financialit.net/news/investment/habito-uks-digital-mortgage-broker-raises-ps55m-series-funding"
PRAVALER_SITE = "https://www.pravaler.com.br/"
PRAVALER_NEOFEED = ("https://neofeed.com.br/negocios/"
                    "a-nova-licao-de-casa-da-pravaler-financiar-1-milhao-de-estudantes-ate-2025/")
PRAVALER_ITAU = "https://euqueroinvestir.com/educacao-financeira/itau-unibanco-aumenta-sua-participacao-no-pravaler"
I2G_PR = ("https://www.prnewswire.com/news-releases/"
          "invoice2go-raises-35-million-in-financing-led-by-accel-partners-276459911.html")
JETTY_PR = ("https://www.prnewswire.com/news-releases/"
            "jetty-announces-115-million-series-a-financing-led-by-valar-300500828.html")
KASA_TERMS = "https://kasa.com/terms"
MONEYVIEW_DB = "https://inc42.com/company/money-view/funding/"
MORPHO_TECHEU = "https://tech.eu/2022/07/15/morpho-sees-18-million-eclosion-in-a16z-and-variant-led-round/"
NAVE_SITE = "https://www.navebank.com/en"
ONZE_2021 = ("https://finsidersbrasil.com.br/2021/05/25/"
             "ribbit-capital-investe-us-10-milhoes-na-onze-de-previdencia-corporativa")
PARAFIN_A = "https://www.parafin.com/blog/parafin-series-a-financing"
PARAFIN_B = "https://www.parafin.com/blog/parafin-series-b-financing"
PING_SITE = "https://www.pingxx.com/"
PINHOME_A = "https://hybrid.co.id/post/ribbit-capital-reportedly-led-series-a-funding-for-pihhome/"
POINT_PR = ("https://www.prnewswire.com/news-releases/point-raises-154-million-in-total-funding-led-by-"
            "andreessen-horowitz-to-help-homeowners-unlock-home-equity-wealth-without-borrowing-300326695.html")
RAISIN_B = "https://nordic9.com/news/raisin-to-get-20m-in-series-b-round-led-by-ribbit-capital-and-index-ventures//"
RAISIN_E = "https://www.raisin.com/en/corporate/press/Raisin-Announces-60M-Funding/"
RELAY_FW = "https://www.freightwaves.com/news/digital-payment-startup-raises-43m"
RELAY_PR = ("https://www.relaypayments.com/newsroom/"
            "relay-payments-raises-43-million-in-new-funding-to-transform-transportation-payments")
ROOT_CAP = "https://stockanalysis.com/stocks/root/market-cap/"

# ---------------------------------------------------------------- Latin America
L.append(cls("gorila", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=GORILA_SITE, city="São Paulo", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined", entry_date="2019-09", flags=["model_disputes_source"],
    note="Gorila Invest, a portfolio aggregator for Brazilian investors (Rua Iaiá 77, Itaim Bibi, São Paulo, per its "
         "own live site, 2026 copyright). The pre-filled country ES is a wrong Wikidata join; the company is Brazilian. "
         "Ribbit led the R$35M (about $8.4M) round of September 2019 with Monashees, Canary and Iporanga (LAVCA "
         "2019-09-30; LatamList 2019-10-17), which both reports call the company's first (major) round without naming "
         "it seed or Series A, so the stage is undetermined with the entry dated. Momentum check: no round at or above "
         "$1B found, " + SWEEP + ".",
    rounds=[rnd("2019-09", "first major round (unnamed)", 8400000, "Ribbit Capital", True, GORILA_LAVCA, "press")]))

L.append(cls("guiabolso", status="acquired", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=NEWS("guiabolso", "PicPay plans to raise"), city="São Paulo", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=GUIA_EXAME, entry_date="2015",
    note="Personal finance and open-banking app (Brazil). Exame (2016-05-18) sets out the rounds: seed from e.bricks "
         "and Valor Capital (2013), Series A from Kaszek (2014), then 'em 2015, veio o terceiro investimento, de série "
         "B', from Ribbit Capital; Ribbit also joined the R$60M round of May 2016 with the IFC, Kaszek and QED. Meyer "
         "Malka is a director on the company's January 2016 Form D ($19.2M). PicPay announced its acquisition of "
         "Guiabolso ('a Brazilian fintech specialising in open banking services') in July 2021 (Retail Banker "
         "International, 2025, which reports it as done), so the row reads acquired with no figure.",
    rounds=[rnd("2015", "Series B", None, "Ribbit Capital", True, GUIA_EXAME, "press"),
            rnd("2016-01-07", "Form D sale", 19243811, None, None, FORMD_CITE("guiabolso", 0), "filing"),
            rnd("2016-05", "unnamed (R$60M)", None, None, True, GUIA_EXAME, "press")]))

L.append(cls("ideal-invest", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=PRAVALER_SITE, city="São Paulo", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined",
    note="Ideal Invest, the student-loan company now named Pravaler (Pravaler S.A., Av. Doutora Ruth Cardoso 7221, "
         "Pinheiros, São Paulo, per its own site, which the firm's Rebels entry links). Operating: NeoFeed "
         "(2021-03-05, " + PRAVALER_NEOFEED + ") names Ribbit Capital with EOS Investimentos among the shareholders, "
         "and a December 2019 report on Itaú Unibanco raising its stake lists Ribbit among the institutional "
         "shareholders who remain (" + PRAVALER_ITAU + "). No source read names or dates the transaction through which "
         "Ribbit entered a company founded in 2001 and earlier backed by Victoria Capital Partners and the IFC, so the "
         "stage is undetermined; the firm first lists it in January 2017.",
    rounds=[]))

L.append(cls("justos", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=NEWS("justos", "Justos raises a $35M"), city="São Paulo", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("justos", "Justos raises a $35M"),
    entry_date="2021-10",
    note="Brazilian auto insurtech. Ribbit led the $35.8M Series A of October 2021, whose new investors included "
         "SoftBank's Latin America fund and GGV (contxto 2021-10-26); the $2.8M seed of May 2021 is reported with Kaszek "
         "and founder and executive angels, not Ribbit (medium, since contxto's wording on the seed's other investors "
         "is loose). Ribbit also led the $16.5M growth round of June 2025 with Kaszek, Scale Up and Endeavor Catalyst "
         "(LatamList 2025-06-23). Momentum check: no round at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2021-05", "Seed", 2800000, None, False, NEWS("justos", "Justos raises a $35M"), "press"),
            rnd("2021-10", "Series A", 35800000, "Ribbit Capital", True, NEWS("justos", "Justos raises a $35M"), "press"),
            rnd("2025-06", "growth round", 16500000, "Ribbit Capital", True, NEWS("justos", "Justos lands"), "press")]))

L.append(cls("kavak", rng="1b_plus", usd=2200000000, val_src="web_verified",
    val_cite=NEWS("kavak", "75% lower valuation"), asof="2025-03", city="Mexico City", city_src="web_verified",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-09",
    flags=["model_disputes_source"], extra=WV,
    note="Used-car marketplace and auto financing (Mexico City, Wikipedia). Ribbit's deal vehicle KV-E Bullfrog "
         "Opportunity I (Form D, 2021 Q3, $30.9M sold) decodes to the Series E, the $700M round of September 2021 at "
         "$8.7B (Wikipedia; General Catalyst led it, per that firm's book); Wikipedia lists Ribbit among Kavak's "
         "investors, no earlier round names Ribbit, and the firm first lists Kavak in 2022, so the Series E is read as "
         "the entry (model, medium). The pre-filled $8.7B mark is superseded by documented collapse evidence: Kavak "
         "raised $127M in March 2025 at a $2.2B valuation, led by SoftBank and General Atlantic (contxto 2025-04-15; "
         "Bloomberg put the cut at $6.5B), and the $300M Series F of February 2026 led by a16z disclosed no valuation "
         "(contxto 2026-02-17). The a16z and General Catalyst books still carry $8.7B, the stale side for rule 10.",
    rounds=[rnd("2021-09", "Series E", 700000000, None, True, SPV("KV-E"), "filing"),
            rnd("2025-03", "unnamed", 127000000, "SoftBank, General Atlantic", None,
                NEWS("kavak", "75% lower valuation"), "press"),
            rnd("2026-02", "Series F", 300000000, "Andreessen Horowitz", None,
                NEWS("kavak", "Kavak closes $300 million Series F"), "press")]))

L.append(cls("nubank", status="public", city="São Paulo", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("nubank", "Series D Funding"),
    entry_date="2016-12", flags=["model_disputes_source"],
    note="Digital bank, São Paulo (Wikipedia). Listed on the NYSE as NU since December 2021, so the pre-filled status "
         "acquired is a wrong join and the row reads public; the market cap is pinned in the A/B pass (aligned with the "
         "Sequoia, Thrive and Redpoint books). Ribbit took part in the $80M Series D of December 2016 led by DST Global, "
         "with Founders Fund, QED, Redpoint, Sequoia and Tiger (Finovate 2016-12-21); no earlier round names Ribbit and "
         "the firm's pages first list Nubank in January 2017, so the entry is dated to the Series D rather than to the "
         "February 2018 Form D the band anchored on (Growth either way).",
    rounds=[rnd("2016-12", "Series D", 80000000, "DST Global", True, NEWS("nubank", "Series D Funding"), "press"),
            rnd("2018-02-15", "Form D sale", 151065517, None, None, FORMD_CITE("nubank", 4), "filing")]))

L.append(cls("onze", status="private", rng="below_1b", country="BR", country_src="web_verified",
    country_cite=NEWS("onze", "Onze raises $20M"), city="São Paulo", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=ONZE_2021, entry_date="2021-05",
    note="Corporate pension platform, a Brazilian fintech started inside Red Ventures. Ribbit's entry is the US$10M "
         "round of May 2021, 'numa rodada Série A toda liderada pelo fundo Ribbit Capital' (Finsiders Brasil "
         "2021-05-25). Ribbit also led the US$20M round of December 2024 with Atlantico and Red Ventures (LatamList "
         "2024-12-04), which Brazil Journal (2024-12-02) calls the Série A while dating the 2021 money as an earlier "
         "US$10M 'também com a Ribbit'; the labels conflict, so medium, taking the one published at the entry. "
         "Momentum check: no round at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2021-05", "Series A", 10000000, "Ribbit Capital", True, ONZE_2021, "press"),
            rnd("2024-12", "Series A (Brazil Journal)", 20000000, "Ribbit Capital", True,
                NEWS("onze", "Onze raises $20M"), "press")]))

L.append(cls("quinto-andar", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified",
    val_cite=NEWS("quinto-andar", "Raises $300m"), asof="2021-05", country="BR", country_src="web_verified",
    country_cite=NEWS("quinto-andar", "Raises $300m"), city="São Paulo", city_src="web_verified",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("quinto-andar", "Raises $300m"), entry_date="2021-05", flags=["stale"], extra=WV,
    note="Rental and home-sales marketplace ('Sao Paulo-based'). The $300M Series E of May 2021 at a $4B valuation "
         "names Ribbit first among its investors, with LTS, Maverik and SoftBank's Latin America fund, and quotes a "
         "Ribbit partner (Online Marketplaces 2021-05-28); no earlier round names Ribbit and the firm first lists "
         "QuintoAndar in 2022, so the Series E is read as the entry (medium). The $4B mark is older than 24 months and "
         "flagged stale; a later 2021 extension may carry a higher figure for the A/B pass to pin.",
    rounds=[rnd("2021-05", "Series E", 300000000, None, True, NEWS("quinto-andar", "Raises $300m"), "press")]))

L.append(cls("nave-bank", status="private", rng="below_1b", country="PR", country_src="web_verified",
    country_cite=NAVE_SITE, city="San Juan", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined",
    note="Nave Bank, a digital-first business bank in San Juan, Puerto Rico (its own site, which names Ally, Bank of "
         "America, PNC and Ribbit Capital among its backers with more than 20 local investors); it received approval to "
         "operate in August 2023 and passed $400M in assets in January 2026 (News is My Business). No source read names "
         "the round or date of Ribbit's investment, so the stage is undetermined. Momentum check: no round at or above "
         "$1B found, " + SWEEP + ".",
    rounds=[]))

# ---------------------------------------------------------------- India and Asia
L.append(cls("groww", status="public", country="IN", country_src="web_verified",
    country_cite=NEWS("groww", "Groww Raises $21.4Mn Series B Funding"), city="Bangalore", city_src="web_verified",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("groww", "Groww Raises $21.4Mn Series B Funding"), entry_date="2019-09",
    note="Investing platform (Bellandur, Bengaluru, per the company's own post). Ribbit came in as a new investor "
         "leading the $21.4M Series B of September 2019, with Sequoia India and Y Combinator participating (the "
         "company's post; Entrackr 2019-09-19); its deal vehicle GW-E then took part in the 2021 Series E. Listed on "
         "the NSE in November 2025 (as Billionbrains Garage Ventures), so public; Ribbit sold down in block deals in "
         "May and August 2026. The market cap is pinned in the A/B pass.",
    rounds=[rnd("2019-09", "Series B", 21400000, "Ribbit Capital", True,
                NEWS("groww", "Mn Series B round led by Ribbit"), "press"),
            rnd("2021", "Series E", None, None, True, SPV("GW-E"), "filing")]))

L.append(cls("moneyview", status="private", rng="below_1b", country="IN", country_src="web_verified",
    country_cite=NEWS("moneyview", "Moneyview DRHP: Accel Largest"), city="Bangalore", focus="Fintech & Payments",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2014",
    note="Digital lending (Whizdm Innovations, renamed Moneyview; Bengaluru). The firm's 2015 Bets page lists it. The "
         "company's first institutional round, late 2014 and about $1.65M, came from Accel India and Ribbit: inc42's "
         "funding database lists it as a September 2014 Series A with 'Accel, +1 more', Accel's own card labels its "
         "entry Series A, and search summaries of India's startup databases name Ribbit beside Accel; no press "
         "article read names Ribbit in it, so model at medium. The March 2026 DRHP shows Ribbit holding 10.2% "
         "(inc42). The IPO opened on 2026-09-24 and had not listed by 2026-09-28, so the row is still private; the "
         "last cited priced round is the $75M Series E at $900M (FinTech Futures), and the 2024 Series F that was to "
         "pass $1B was reported only as in talks (Entrackr 2024-07-19), so below_1b, aligned with Accel's book. The "
         "A/B pass should pin the listing.",
    rounds=[rnd("2014-09", "Series A", 1650000, "Accel", True, MONEYVIEW_DB, "vendor"),
            rnd("2022-12", "Series E", 75000000, None, None, NEWS("moneyview", "Series E funding at $900m"), "press")]))

L.append(cls("phonepe", status="private", rng="10b_plus", usd=12000000000, val_src="web_verified",
    val_cite=W("PhonePe"), asof="2023-02", city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("PhonePe"), entry_date="2023-02",
    flags=["model_disputes_source", "stale"], extra=WV,
    note="Digital payments and financial services, Bengaluru (Wikipedia). The pre-filled status acquired reads "
         "Flipkart's 2016 purchase; PhonePe has since raised priced primary rounds from outside investors as a "
         "stand-alone company majority-owned by Walmart, and its IPO was paused in March 2026, so the row reads "
         "private. Entry: 'It raised another $100 million in primary capital in February 2023 from Ribbit Capital, "
         "Tiger Global, and TVS Capital Funds', within the round at a pre-money valuation of $12B (Wikipedia), which is "
         "also the last primary mark, flagged stale; the co-founders' 2025 sale to General Atlantic is a secondary and "
         "stays out of the figure.",
    rounds=[rnd("2023-02", "primary round ($12B pre-money)", 100000000, None, True, W("PhonePe"), "press")]))

L.append(cls("policy-bazaar", status="public", country="IN", country_src="web_verified",
    country_cite=NEWS("policy-bazaar", "focus on PaisaBazaar"), city="Gurugram", city_src="web_verified",
    focus="Fintech & Payments", stage="Growth", stage_src="model", stage_conf="medium",
    note="Insurance marketplace (Policybazaar, parent PB Fintech; 'Gurgaon based', MediaNama), listed on the NSE and "
         "BSE in November 2021, so public; the market cap is pinned in the A/B pass. The firm's Bets page lists it from "
         "its first capture (December 2014), and MediaNama (2015-04-15) names 'new and existing investors including "
         "Tiger Global and Ribbit Capital' in the $40M Series D led by PremjiInvest. Wikipedia dates the Series A "
         "(Intel Capital, Inventus) before the April 2013 Series B and the May 2014 Series C, so whichever round or "
         "share purchase brought Ribbit in (April 2013 to December 2014) was a Series B or later: Growth (model, "
         "medium). No source dates Ribbit's first round, so no entry date is given. The company leaves the firm's "
         "pages after 2018.",
    rounds=[rnd("2014-05", "Series C", 20000000, None, None, W("Policybazaar"), "press"),
            rnd("2015-04", "Series D", 40000000, "PremjiInvest", True,
                NEWS("policy-bazaar", "focus on PaisaBazaar"), "press")]))

L.append(cls("razorpay", city="Bangalore", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("razorpay", "Razorpay bags"),
    entry_date="2019-06",
    note="Payments (Bengaluru, per Entrackr). Ribbit co-led the $75M Series C of June 2019 with Sequoia India; the "
         "backers named as earlier investors are Tiger Global, Y Combinator's Continuity Fund and Matrix, not Ribbit "
         "(Entrackr and FinTech Global, 2019-06-18), so the Series C is Ribbit's entry. Its deal vehicle RZ-E then took "
         "part in the 2021 Series E. The pre-filled $7.5B (December 2021) stays for the A/B pass.",
    rounds=[rnd("2019-06", "Series C", 75000000, "Ribbit Capital, Sequoia India", True,
                NEWS("razorpay", "Razorpay bags"), "press"),
            rnd("2021", "Series E", None, None, True, SPV("RZ-E"), "filing")]))

L.append(cls("pinhome", status="private", rng="below_1b", country="ID", country_src="web_verified",
    country_cite=PINHOME_A, city="Jakarta", focus="Consumer & Marketplaces",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=PINHOME_A, entry_date="2021-07",
    note="Indonesian property platform (home buying, renting and home services across Indonesian cities). Ribbit led "
         "the $25.5M Series A of July 2021 with Goodwater, Insignia and Global Founders Capital (Hybrid.co.id "
         "2021-07-22, reported before the company confirmed it, hence medium). Operating in 2025 (CNBC profile, "
         "2025-05-20). Momentum check: no round at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2021-07", "Series A", 25500000, "Ribbit Capital", True, PINHOME_A, "press")]))

L.append(cls("ping", status="private", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=PING_SITE, city="Shanghai", city_src="web_verified", focus="Fintech & Payments",
    stage="undetermined",
    note="Ping++, an aggregated-payments API for Chinese apps (Shanghai Jianmi Network Technology Co., Ltd., per its "
         "own live site with a Shanghai ICP licence). No citable source read names Ribbit's round: the only records "
         "tying Ribbit to Ping++ are vendor profiles (Tracxn, Crunchbase), which never cite, so the stage is "
         "undetermined. The sibling rows named Ping in the First Round, General Catalyst and Y Combinator books are "
         "other companies (Time by Ping, Ping Identity, a Y Combinator Summer 2022 company).",
    rounds=[]))

L.append(cls("onekey", status="private", rng="below_1b", country="HK", country_src="web_verified",
    country_cite=NEWS("onekey", "OneKey raises $20 million"), city="Hong Kong", city_src="web_verified",
    focus="Crypto & Web3", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("onekey", "OneKey raises $20 million"), entry_date="2022-09",
    note="Crypto hardware and software wallets (Hong Kong, per The Block). Ribbit co-led the $20M Series A of "
         "September 2022 with Dragonfly, joined by Coinbase Ventures, Framework, Sky9 and others (The Block "
         "2022-09-28), and took part in the 2025 Series B led by YZi Labs (a Binance Square post). Momentum check: no "
         "round at or above $1B found (the Series B's valuation was not disclosed), " + SWEEP + ". The Y Combinator "
         "row OneKey (Summer 2020 batch, Paris) is a different company with the same name.",
    rounds=[rnd("2022-09", "Series A", 20000000, "Dragonfly, Ribbit Capital", True,
                NEWS("onekey", "OneKey raises $20 million"), "press"),
            rnd("2025", "Series B", None, "YZi Labs", True, NEWS("onekey", "OneKey Completes"), "press")]))

L.append(cls("multiplier", status="private", rng="below_1b", country="SG", country_src="web_verified",
    country_cite=NEWS("multiplier", "Singapore tech firm Multiplier"), city="Singapore", city_src="web_verified",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("multiplier", "nabs $27.5M"), entry_date="2025",
    grad="graduated", grad_src="web_verified", grad_cite=NEWS("multiplier", "nabs $27.5M"), grad_conf="high",
    note="Multiplier Holdings, founded by ex-Stripe executive Noah Pepper, buys accounting and tax firms and runs them "
         "on its own AI tooling ('Singapore-based Multiplier', Startup Daily 2026-04-01). Ribbit led the seed, with SV "
         "Angel, and Lightspeed led the Series A that followed, $27.5M in all, announced together (TechCrunch "
         "2025-06-18): graduated on the named Series A, and a $35M Series B followed in August 2026 (Business Wire). "
         "Lightspeed's book places the company in San Francisco; the Singapore report is fresher. The Y Combinator row "
         "Multiplier (Spring 2026 batch, New York) is a different company with the same name. Momentum check: no round "
         "at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2025", "Seed", None, "Ribbit Capital", True, NEWS("multiplier", "nabs $27.5M"), "press"),
            rnd("2025", "Series A", None, "Lightspeed Venture Partners", None, NEWS("multiplier", "nabs $27.5M"),
                "press"),
            rnd("2026-08", "Series B", 35000000, None, None,
                NEWS("multiplier", "Multiplier Raises $35 Million Series B to Build"), "company")]))

# ---------------------------------------------------------------- Europe
L.append(cls("habito", status="acquired", rng="below_1b", country="GB", country_src="web_verified",
    country_cite=HABITO_A, city="London", city_src="web_verified", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=HABITO_A, entry_date="2017-01",
    note="Digital mortgage broker, based in East London (Financial IT). Ribbit led the GBP 5.5M Series A of January "
         "2017 as a new investor, with existing investor Mosaic Ventures, after seed and angel money from Mosaic, "
         "Taavet Hinrikus, Samir Desai and Yuri Milner (Financial IT, 2017-01-23); Atomico led the Series B later in "
         "2017 (Atomico's book). Monzo agreed to buy Habito on 2025-12-16 and 'has today completed the acquisition' on "
         "2026-04-30 (" + NEWS("habito", "Monzo completes acquisition of Habito") + "), aligned with Atomico's "
         "acquired row.",
    rounds=[rnd("2017-01", "Series A", None, "Ribbit Capital", True, HABITO_A, "press")]))

L.append(cls("raisin", status="private", rng="below_1b", country="DE", country_src="web_verified",
    country_cite=NEWS("raisin", "closes €30m round"), city="Berlin", city_src="web_verified",
    focus="Fintech & Payments", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=RAISIN_B,
    entry_date="2015-08",
    note="Savings and deposit marketplace (WeltSparen in German-speaking markets; 'Berlin-based', Silicon Republic). "
         "Ribbit co-led the EUR 20M Series B of August 2015 with Index Ventures, with Avala, b2venture, DN Capital, Tom "
         "Stafford and Yuri Milner (Nordic 9, 2015-08-08; medium, a deal-news service); it was an existing investor in "
         "the EUR 30M Series C led by Thrive in January 2017 (Silicon Republic) and in the 2019 round (Tech.eu), and "
         "is named among Raisin's backers at the EUR 60M Series E of March 2023 (the company's release, " + RAISIN_E +
         "). No source read gives Raisin a valuation, so below_1b with the check recorded.",
    rounds=[rnd("2015-08", "Series B", None, "Ribbit Capital, Index Ventures", True, RAISIN_B, "press"),
            rnd("2017-01", "Series C", None, "Thrive Capital", True, NEWS("raisin", "closes €30m round"), "press"),
            rnd("2023-03", "Series E", None, None, True, RAISIN_E, "company")]))

L.append(cls("revolut", rng="100b_plus", usd=115000000000, val_src="web_verified", val_cite=W("Revolut"),
    asof="2026-07-22", country="GB", country_src="web_verified", country_cite=W("Revolut"), city="London",
    city_src="web_verified", focus="Fintech & Payments", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=NEWS("revolut", "Revolut Lands $8.7 Million"), entry_date="2016-07",
    flags=["model_disputes_source"], extra=WV,
    note="Digital bank headquartered in London (Wikipedia); the pre-filled country LT is its Lithuanian banking entity, "
         "a wrong join. Ribbit came in on the Series A of July 2016 ($8.7M, GBP 6.8M): 'Investors include Ribbit "
         "Capital along with existing contributors Balderton Capital, Index Ventures, Point Nine Capital, Venrex and "
         "Seedcamp' (Finovate 2016-07-11); it was an existing backer in the $66M Series B of July 2017 led by Index "
         "(UKTN), and its deal vehicles RV-D and RV-E followed in 2018 and 2020. The pre-filled $75B (the 2025 share "
         "sale) is superseded by the secondary share sale of July 2026 at $2,017 per share, a $115B valuation "
         "(Wikipedia, citing Reuters), so 100b_plus, aligned with the Balderton, Coatue and Point Nine books; the a16z "
         "and Greylock books still read $75B.",
    rounds=[rnd("2016-07", "Series A", 8700000, None, True, NEWS("revolut", "Revolut Lands $8.7 Million"), "press"),
            rnd("2017-07", "Series B", 66000000, "Index Ventures", True, NEWS("revolut", "UKTN"), "press"),
            rnd("2018", "Series C (the firm's letter D)", None, None, True, SPV("RV-D"), "filing"),
            rnd("2020", "Series D (the firm's letter E)", None, None, True, SPV("RV-E"), "filing")]))

L.append(cls("morpho", status="private", rng="below_1b", country="FR", country_src="web_verified",
    country_cite=MORPHO_TECHEU, city="Paris", city_src="web_verified", focus="Crypto & Web3",
    stage="undetermined", entry_date="2024-08", grad="undetermined", flags=["token_funded"],
    note="Morpho, the DeFi lending protocol, recorded under its issuing organisation Morpho Labs ('Paris-based', "
         "Tech.eu 2022-07-15; decisions.md D2). Ribbit's first money was the $50M round of August 2024 that it led, "
         "which CoinDesk (2024-08-01) describes as 'a private token sale' with a16z crypto, Coinbase Ventures, Variant, "
         "Pantera and others; no source names Ribbit in the $18M 2022 round of Morpho Labs (a16z crypto and Variant), "
         "so the stage and the graduation read undetermined with the flag token_funded. Morpho Labs became a subsidiary "
         "of the non-profit Morpho Association in June 2025 (The Defiant), and Ribbit co-led the $175M raise of June "
         "2026 with Paradigm and a16z crypto (The Block); token pricing is not a company equity mark, so below_1b, "
         "aligned with the a16z and Cherry books.",
    rounds=[rnd("2022-07", "unnamed", 18000000, "a16z crypto, Variant", None, MORPHO_TECHEU, "press"),
            rnd("2024-08", "private token sale", 50000000, "Ribbit Capital", True,
                NEWS("morpho", "Morpho Bags $50M"), "press"),
            rnd("2026-06", "token round", 175000000, "Paradigm, a16z crypto, Ribbit Capital", True,
                NEWS("morpho", "co-led by Paradigm, a16z crypto and Ribbit"), "press")]))

# ---------------------------------------------------------------- United States
L.append(cls("gusto", rng="1b_plus", usd=9300000000, val_src="web_verified", val_cite=W("Gusto, Inc."),
    asof="2025-06", country="US", city="San Francisco", city_src="web_verified", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("gusto", "ZenPayroll Receives $60M"),
    entry_date="2015-04", flags=["model_disputes_source"], extra=WV,
    note="Payroll, benefits and HR software (San Francisco; ZenPayroll until 2015). Ribbit came in as a new investor "
         "in ZenPayroll's $60M round of April 2015 led by Google Capital, beside new investor Emergence and existing "
         "investors General Catalyst, Kleiner Perkins and Google Ventures (CPA Practice Advisor 2015-04-06); that round "
         "followed the seed and the $20M Series A of 2014 (General Catalyst's book), so the entry is Growth (medium, "
         "the article gives no series letter). Two pre-filled values are wrong joins: the country NL (Wikidata matched a "
         "Dutch entity) and the 10b_plus band at $10B (an aggregator figure). The freshest priced event is the June "
         "2025 employee tender offer at $9.3B (Wikipedia), so 1b_plus; the last primary was the Series E at $9.5B in "
         "August 2021. The a16z and Felicis books still carry 10b_plus at $10B, the stale side for rule 10.",
    rounds=[rnd("2015-04", "unnamed ($60M, the Series B)", 60000000, "Google Capital", True,
                NEWS("gusto", "ZenPayroll Receives $60M"), "press")]))

L.append(cls("hippo", country="US", country_src="web_verified", country_cite=W("Hippo (company)"),
    city="San Jose", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("hippo", "Hippo Closes $150 Million Series E"), entry_date="2020-07",
    flags=["model_disputes_source"],
    note="Home insurance (Hippo Holdings, now at One Almaden Blvd, San Jose: Wikipedia and the company's EDGAR business "
         "address). The pre-filled country BY is a wrong Wikidata join. Ribbit came in as a new investor in the $150M "
         "Series E of July 2020 at $1.5B, beside FinTLV, Dragoneer and Innovius, with existing backers including "
         "Felicis, Comcast Ventures and Fifth Wall (Insurance Innovation Reporter 2020-07-21); Ribbit Capital VI also "
         "took 300,000 shares in the PIPE of the August 2021 merger with Reinvent Technology Partners Z (Hippo's S-1 of "
         "2021-08-24), which does not decide membership since the venture entry came first. Public since August 2021; "
         "the value stays with the A/B pass.",
    rounds=[rnd("2020-07", "Series E", 150000000, None, True, NEWS("hippo", "Hippo Closes $150 Million Series E"),
                "press")]))

L.append(cls("id-me", rng="1b_plus", usd=2000000000, val_src="web_verified",
    val_cite=NEWS("id-me", "ID.me Raises $340 Million to Combat"), asof="2025-09-03", city="McLean",
    city_src="web_verified", focus="Security", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("id-me", "ID.me sets $1.8b valuation"), entry_date="2024-10", extra=WV,
    note="Digital identity verification (McLean, Virginia: Wikipedia and the release's dateline). Ribbit's first "
         "position came through the tender offer of October 2024 at a $1.8B valuation, in which Viking Global and "
         "CapitalG, 'along with new investor Ribbit Capital', bought $67M of shares from employees and early investors "
         "(Biometric Update 2024-10-10); a tender entry reads Growth. Ribbit then led the $65M Series E of September "
         "2025, part of $340M with a credit facility, at a valuation above $2B (the company's release, 2025-09-03), "
         "which replaces the pre-filled $1.5B mark; the band is unchanged.",
    rounds=[rnd("2024-10", "tender offer", 67000000, "Viking Global, CapitalG", True,
                NEWS("id-me", "ID.me sets $1.8b valuation"), "press"),
            rnd("2025-09", "Series E", 65000000, "Ribbit Capital", True,
                NEWS("id-me", "ID.me Raises $340 Million to Combat"), "company")]))

L.append(cls("imprint", status="private", rng="1b_plus", usd=1200000000, val_src="web_verified",
    val_cite=NEWS("imprint", "Series D At $1.2 Billion"), asof="2025-12", country="US", city="New York",
    city_src="web_verified", focus="Fintech & Payments", stage="Growth", stage_src="web_verified",
    stage_conf="medium", stage_cite=NEWS("imprint", "Led by Ribbit"), entry_date="2023-11", extra=WV,
    note="Co-branded credit cards (New York; the release's dateline). Ribbit led the $75M Series B of November 2023, "
         "with significant participation from Thrive Capital, Kleiner Perkins and Moore Specialty Credit (the "
         "company's release, 2023-11-13); no earlier round names Ribbit and the firm first lists Imprint in 2024, so "
         "the Series B is read as the entry (medium). Ribbit joined the $150M Series D at a $1.2B post-money valuation "
         "in December 2025 (Pulse 2.0, 2025-12-23), the mark, aligned with the Khosla and Thrive books; that round is "
         "also the momentum check's $1B+ event.",
    rounds=[rnd("2023-11", "Series B", 75000000, "Ribbit Capital", True, NEWS("imprint", "Led by Ribbit"), "company"),
            rnd("2025-12", "Series D", 150000000, "Khosla Ventures", True,
                NEWS("imprint", "Series D At $1.2 Billion"), "press")]))

L.append(cls("invoice2go", status="acquired", rng="below_1b", country="US", country_src="web_verified",
    country_cite=W("Invoice2go"), city="Redwood City", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=I2G_PR, entry_date="2014-09",
    flags=["model_disputes_source"],
    note="Mobile invoicing and payments for small businesses, founded in Australia in 2002 and headquartered in both "
         "Silicon Valley and Sydney (Wikipedia). The pre-filled country AU is the founding country; the company ran "
         "from California after the 2014 financing, so country and city follow Accel's book (Redwood City, US). Ribbit "
         "came in with Accel in the $35M financing of September 2014, 'the first round of funding for the startup' "
         "(the company's release, Palo Alto, 2014-09-23); SmartCompany (2015-11-03) calls that money 'series A and B "
         "rounds' and Accel's card calls its entry the Series A, so the entry reads Series A at medium. Ribbit led the "
         "$15M Series C of November 2015 as an existing investor (SmartCompany). Bill.com acquired the company in 2021 "
         "(Wikipedia), aligned with Accel's acquired row.",
    rounds=[rnd("2014-09", "first round (Series A and B)", 35000000, "Accel Partners", True, I2G_PR, "company"),
            rnd("2015-11", "Series C", 15000000, "Ribbit Capital", True,
                NEWS("invoice2go", "SME mobile payments"), "press")]))

L.append(cls("jetty", status="private", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=JETTY_PR,
    entry_date="2016", grad="graduated", grad_src="web_verified", grad_cite=JETTY_PR, grad_conf="high",
    note="Renters insurance and deposit alternatives (New York; the release's dateline). Ribbit is one of the "
         "'original Jetty seed investors, including Ribbit Capital, SV Angel, BoxGroup, and Red Swan' that renewed in "
         "the $11.5M Series A led by Valar Ventures (the company's release, 2017-08-08); the seed is dated 2016 because "
         "the firm's January 2017 page already lists Jetty and no source dates the seed itself. Graduated: the Series A "
         "of August 2017 is a later round named Series A; Ribbit was again an existing investor in the $25M Series B "
         "led by Khosla Ventures in February 2019 (HousingWire). Still operating (Farmers Insurance equity investment "
         "2021; Jetty Rent launched September 2021).",
    rounds=[rnd("2016", "Seed", None, None, True, JETTY_PR, "company"),
            rnd("2017-08", "Series A", 11500000, "Valar Ventures", True, JETTY_PR, "company"),
            rnd("2019-02", "Series B", 25000000, "Khosla Ventures", True,
                NEWS("jetty", "Renter-focused insurance startup Jetty"), "press")]))

L.append(cls("juniper-square", status="private", rng="1b_plus", usd=1100000000, val_src="web_verified",
    val_cite=NEWS("juniper-square", "Series D Financing Round at $1.1 Billion"), asof="2025-06",
    city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=NEWS("juniper-square", "HousingWire"),
    entry_date="2018-12", extra=WV,
    note="Investment management and fund administration software for private markets (San Francisco; the release's "
         "dateline). Ribbit led the $25M Series B of December 2018 with Felicis and Zigg Capital (HousingWire "
         "2018-12-14); no earlier round names Ribbit, so the pre-filled Growth stands with the entry dated to that round "
         "rather than to the 2019 first-sale date on the 2025 Form D, where Nick Shalek is a director. Ribbit also led "
         "the $130M Series D of June 2025 at a $1.1B valuation, with Fifth Wall, Redpoint and others (the company's "
         "release, 2025-06-16), the mark, aligned with the Felicis and Redpoint books.",
    rounds=[rnd("2018-12", "Series B", 25000000, "Ribbit Capital", True, NEWS("juniper-square", "HousingWire"), "press"),
            rnd("2025-06", "Series D", 130000000, "Ribbit Capital", True,
                NEWS("juniper-square", "Series D Financing Round at $1.1 Billion"), "company")]))

L.append(cls("kasa", status="private", rng="below_1b", country="US", city="Miami", city_src="web_verified",
    focus="Consumer & Marketplaces", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite=NEWS("kasa", "Serviced Apartment"), entry_date="2020-10",
    note="Tech-enabled apartment-hotel and short-term rental brand (Kasa, Inc., a Delaware corporation; its terms of use "
         "give 390 NE 191st St, Miami, as the company address, " + KASA_TERMS + "). Ribbit led the $30M Series B of "
         "October 2020 with RET Ventures, Zigg Capital, Allegion Ventures and BoxGroup (Serviced Apartment News "
         "2020-10-14); no earlier round names Ribbit and the firm first lists Kasa in 2021 (medium). Ribbit joined the "
         "$70M Series C of October 2023 led by Citi Ventures and FirstMark (AlleyWatch). Operating (live site, 2026 "
         "copyright); no valuation reported, so below_1b.",
    rounds=[rnd("2020-10", "Series B", 30000000, "Ribbit Capital", True, NEWS("kasa", "Serviced Apartment"), "press"),
            rnd("2023-10", "Series C", 70000000, "Citi Ventures, FirstMark Capital", True,
                NEWS("kasa", "Kasa Living Raises Another"), "press")]))

L.append(cls("kiavi", status="acquired", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
    note="Kiavi (LendingHome until 2021), lending to real-estate investors, San Francisco. Figure Technology Solutions "
         "agreed to acquire Kiavi on 2026-06-10 and completed the acquisition on 2026-09-01 ("
         + NEWS("kiavi", "Acquisition of Kiavi - GlobeNewswire") + "; reported at $717M), so the row reads acquired "
         "with no figure. The pre-filled Series A (Form D band, August 2014, Meyer Malka a director) stands; no press "
         "found names the 2014 round. First Round's book still reads private, the stale side for rule 10."))

L.append(cls("lightspark", status="private", rng="below_1b", country="US", city="Los Angeles",
    focus="Crypto & Web3", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("lightspark", "ledgerinsights"), entry_date="2022-05",
    note="Bitcoin and Lightning payments infrastructure (David Marcus). Ribbit took part in the Series A of May 2022 "
         "led by a16z and Paradigm, with Thrive, Coatue, Felix Capital, Matrix and Zeev (Ledger Insights 2022-05-13; "
         "CoinDesk 2022-05-12 names the same investors). Private and operating (Visa and SoFi partnerships "
         "reported 2025 to 2026). Momentum check: no round at or above $1B found, " + SWEEP + "; aligned with the a16z, "
         "Coatue and Thrive books.",
    rounds=[rnd("2022-05", "Series A", None, "a16z crypto, Paradigm", True, NEWS("lightspark", "ledgerinsights"),
                "press")]))

L.append(cls("next-insurance", status="acquired", rng="below_1b", city="Palo Alto", city_src="web_verified",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("next-insurance", "Raises $13M"), entry_date="2016-03",
    grad="graduated", grad_src="web_verified",
    grad_cite=NEWS("next-insurance", "Israeli Insurtech Firm Next Insurance Raises $83M"), grad_conf="high",
    flags=["stage_disputes_band"],
    note="Small-business insurance (Palo Alto). The pre-filled Growth from the Form D band (March 2017, $35M) is not "
         "the entry: Ribbit co-led the $13M seed round of March 2016 with Zeev Ventures and TLV Partners (NoCamels "
         "2016-03-15). Graduated: the $83M Series B of July 2018 led by Redpoint, with Ribbit taking part, brought total "
         "funding to $131M (NoCamels 2018-07-11), after the 2017 round on the Form D. Munich Re signed to buy Next for "
         "$2.6B in March 2025 (TechCrunch, which names Ribbit among the backers) and ERGO completed the acquisition ("
         + NEWS("next-insurance", "Ergo completed") + "); the company now trades as ERGO NEXT, so the row reads acquired "
         "with no figure, aligned with the Battery and Redpoint books.",
    rounds=[rnd("2016-03", "Seed", 13000000, "Zeev Ventures, TLV Partners, Ribbit Capital", True,
                NEWS("next-insurance", "Raises $13M"), "press"),
            rnd("2017-03-24", "Form D sale", 34999798, None, None, FORMD_CITE("next-insurance", 3), "filing"),
            rnd("2018-07", "Series B", 83000000, "Redpoint Ventures", True,
                NEWS("next-insurance", "Israeli Insurtech Firm Next Insurance Raises $83M"), "press")]))

L.append(cls("onepay", status="private", rng="1b_plus", usd=4000000000, val_src="web_verified",
    val_cite=NEWS("onepay", "after share buyback"), asof="2026-01", city="New York", focus="Fintech & Payments",
    stage="undetermined", entry_date="2021", extra=WV,
    note="OnePay (One Finance, Inc., formerly ONE), the consumer finance app 'founded by Walmart and Ribbit Capital' "
         "(CFO Brew 2026-01-30): the Walmart and Ribbit venture was set up in 2021 and, as Hazel, agreed in January "
         "2022 to merge with ONE and Even (PR Newswire) and took the ONE name. Ribbit's first stake came at the "
         "venture's formation, not in a named round, so the stage is undetermined; Walmart and Ribbit then led a $300M "
         "round in 2024 at $2.5B (Investing.com). The mark is the share buyback from employees reported by Bloomberg in "
         "January 2026 at more than $4B (Investing.com 2026-01-09; PYMNTS), a company-run transaction with a stated "
         "figure, read like a tender; it is also the momentum check's $1B+ event.",
    rounds=[rnd("2024", "unnamed", 300000000, "Walmart, Ribbit Capital", True, NEWS("onepay", "after share buyback"),
                "press")]))

L.append(cls("parafin", status="private", rng="below_1b", country="US", city="San Francisco",
    focus="Fintech & Payments", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=PARAFIN_B,
    entry_date="2021", grad="graduated", grad_src="web_verified", grad_cite=PARAFIN_B, grad_conf="high",
    note="Embedded small-business financing, founded by former Robinhood engineers (San Francisco). Parafin's own "
         "Series B post names 'Series A and seed lead investors, Thrive Capital and Ribbit Capital', so Ribbit led the "
         "seed and Thrive the Series A, announced together in September 2021 as a $34M Series Seed and A financing "
         "(" + PARAFIN_A + "). Graduated: the Series A, then the $60M Series B led by GIC in August 2022 (the company's "
         "post). Ribbit joined the $100M Series C of December 2024 led by Notable Capital (FinTech Global), reported at "
         "a $750M valuation (Bloomberg), so below_1b; Redpoint's book carries $1.5B from a Parafin page that no longer "
         "loads, which disagrees with that report. Momentum check: no round at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2021", "Seed", None, "Ribbit Capital", True, PARAFIN_B, "company"),
            rnd("2021-09", "Series A", None, "Thrive Capital", True, PARAFIN_A, "company"),
            rnd("2022-08", "Series B", 60000000, "GIC", True, PARAFIN_B, "company"),
            rnd("2024-12", "Series C", 100000000, "Notable Capital", True, NEWS("parafin", "Parafin bags $100m"),
                "press")]))

L.append(cls("persona", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
    val_cite=NEWS("persona", "SiliconANGLE"), asof="2025-04-30", country="US", country_src="web_verified",
    country_cite=NEWS("persona", "SiliconANGLE"), city="San Francisco", city_src="web_verified", focus="Security",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("persona", "SiliconANGLE"),
    entry_date="2025-04", flags=["model_disputes_source"], extra=WV,
    note="Identity verification (San Francisco). Two pre-filled values are wrong joins to other companies of the name: "
         "the status acquired and the country RU. 'Founders Fund and Ribbit Capital led the deal with participation "
         "from returning backers BOND, Coatue, First Round Capital and Index Ventures': the $200M Series D of April "
         "2025 at a $2B valuation (SiliconANGLE 2025-04-30), where only those four are returning and the firm first "
         "lists Persona in 2025, so the Series D is Ribbit's entry and its figure the mark, aligned with the Coatue and "
         "Insight books.",
    rounds=[rnd("2025-04", "Series D", 200000000, "Founders Fund, Ribbit Capital", True,
                NEWS("persona", "SiliconANGLE"), "press")]))

L.append(cls("plaid", rng="1b_plus", usd=8000000000, val_src="web_verified", val_cite=W("Plaid Inc."),
    asof="2026-02", city="San Francisco", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="model", stage_conf="medium", stage_cite=NEWS("plaid", "Plaid Raises $425 Million"),
    entry_date="2021-04", flags=["model_disputes_source"], extra=WV,
    note="Financial data network (San Francisco, Wikipedia). The firm first lists Plaid in 2022, Business Insider's "
         "report of the $425M Series D of April 2021 led by Altimeter names Silver Lake and Ribbit (its headline and "
         "URL; the page itself could not be read), and Wikipedia calls Ribbit a 'former backer' at the 2025 round; "
         "every round after the 2014 Series A is Growth, so the entry is Growth dated to the Series D (model, medium). "
         "The pre-filled 10b_plus at $13.4B is the stale 2021 mark: the April 2025 round priced Plaid at $6.1B and the "
         "employee share sale of February 2026 at $8B (Wikipedia), so 1b_plus at $8B, aligned with the Coatue, Felicis "
         "and Spark books.",
    rounds=[rnd("2021-04", "Series D", 425000000, "Altimeter Capital", True,
                NEWS("plaid", "Plaid Raises $425 Million"), "press"),
            rnd("2025-04", "unnamed", 575000000, "Franklin Templeton", True, W("Plaid Inc."), "press")]))

L.append(cls("point", status="private", rng="below_1b", country="US", country_src="web_verified",
    country_cite=POINT_PR, city="Palo Alto", city_src="web_verified", focus="Fintech & Payments",
    stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=POINT_PR, entry_date="2015",
    grad="graduated", grad_src="web_verified", grad_cite=POINT_PR, grad_conf="high",
    flags=["model_disputes_source"],
    note="Home equity investments (point.com; founders Eddie Lim, Eoin Matthews and Alex Rampell). Two pre-filled "
         "values are wrong joins: the status defunct (another company named Point; this one operates, with a $2.5B "
         "Blue Owl home equity commitment in December 2025, "
         + NEWS("point", "Blue Owl commits $2.5B") + ") and the country CH. Point's own release (Palo Alto, "
         "2016-09-13) says Andreessen Horowitz 'also led the company's seed round in 2015' and, leading the $8.4M "
         "Series A, 'was joined by the company's earlier backers Ribbit Capital and Bloomberg Beta', so Ribbit's entry "
         "is the 2015 seed (medium: the release calls Ribbit an earlier backer without naming its round) and the row "
         "graduated on that named Series A. a16z's book reads this company as a defunct rewards-card Point with a West "
         "Point address; that row needs re-checking against this one.",
    rounds=[rnd("2015", "Seed", None, "Andreessen Horowitz", True, POINT_PR, "company"),
            rnd("2016-09", "Series A", 8400000, "Andreessen Horowitz", True, POINT_PR, "company")]))

L.append(cls("privy", status="acquired", rng="below_1b", country="US", city="New York", city_src="web_verified",
    focus="Crypto & Web3", stage="undetermined", entry_date="2025-03",
    note="Wallet infrastructure for crypto apps ('New York-based', The Block). Ribbit led the $15M round of March 2025 "
         "as a new investor, with existing investors Sequoia, Paradigm, BlueYard and Coinbase, after the 2022 seed "
         "(Sequoia and BlueYard) and the $18M Series A of 2023 led by Paradigm (The Block 2025-03-19); neither The Block "
         "nor Fortune names the round, so the stage is undetermined with the entry dated. Stripe announced the "
         "acquisition on 2025-06-11 (SiliconANGLE) and Privy has since operated as a Stripe company ('Stripe-Owned "
         "Privy', BeInCrypto 2026), so the row reads acquired, aligned with Sequoia's book.",
    rounds=[rnd("2025-03", "unnamed", 15000000, "Ribbit Capital", True,
                NEWS("privy", "Privy raises $15 million round led by Ribbit"), "press")]))

L.append(cls("relay-payments", status="private", rng="below_1b", country="US", city="Atlanta", city_src="web_verified",
    focus="Fintech & Payments", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=RELAY_FW,
    entry_date="2020-07",
    note="Payments for trucking and logistics (headquartered in Atlanta, per the company's release). The company raised "
         "$43M over the six months to January 2021, $7.7M in July 2020 and $35.3M on 2020-12-03, and 'Addition... led "
         "the Series A and Series B funding rounds, with participation from investment firms Ribbit Capital and Spark "
         "Capital' (FreightWaves; the company's release of 2021-01-12, " + RELAY_PR + ", says the same without round "
         "names). Read as Ribbit entering at the July 2020 Series A (medium: the sentence does not split the two "
         "rounds). Momentum check: no round at or above $1B found, " + SWEEP + ".",
    rounds=[rnd("2020-07", "Series A", 7700000, "Addition", True, RELAY_FW, "press"),
            rnd("2020-12", "Series B", 35300000, "Addition", True, RELAY_FW, "press")]))

L.append(cls("root", rng="below_1b", usd=722610000, val_src="web_verified", val_cite=ROOT_CAP, asof="2026-09-28",
    city="Columbus", city_src="web_verified", focus="Fintech & Payments",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("root", "Dan Manges"),
    entry_date="2017", flags=["model_disputes_source"], extra=WV,
    note="Car insurance (Root, Inc., Columbus, Ohio: Wikipedia). The pre-filled 1b_plus at $1.60B is an old SEC float; "
         "the market cap was $722.61M on 2026-09-28 (stockanalysis.com), so below_1b, aligned with the Coatue and "
         "Sequoia books. Entry: 'Our second round we raised from Ribbit Capital... we ended up completing a $21.5 "
         "million Series B' (co-founder Dan Manges, Smart Business 2019), which matches Nick Shalek joining the board "
         "in June 2017 (Root's 2020 registration statement); Growth as pre-filled, now dated 2017 rather than to the "
         "2018 Form D. Ribbit's vehicle RT-E then joined the 2019 Series E. The rows named Root in the Headline and "
         "Insight books are other companies (an unnamed Headline listing; Slim.AI, renamed Root).",
    rounds=[rnd("2017", "Series B", 21500000, "Ribbit Capital", True, NEWS("root", "Dan Manges"), "press"),
            rnd("2019-09", "Series E", 350000000, None, True, SPV("RT-E"), "filing")]))

L.append(cls("safetykit", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
    focus="AI & Applied AI",
    note="AI agents for trust and safety, fraud and compliance review (San Francisco, the address on its 2025 Form D "
         "filings; a Y Combinator Summer 2023 company per the YC book). The pre-filled Series A (Form D band, March "
         "2025, $27.3M, Jordan Angelos a director) stands; a second Form D followed in October 2025. Momentum check: no "
         "round at or above $1B found, " + SWEEP + " (an OpenAI customer story of September 2025 is the latest "
         "coverage)."))

L.append(cls("settle", status="private", rng="below_1b", city="San Francisco", city_src="web_verified",
    focus="Fintech & Payments",
    note="Accounts payable and cash-flow software for consumer brands ('based in San Francisco', Bloomberg via Yahoo "
         "Finance 2021-07-29). The pre-filled Growth (Form D band, August 2021, $75M, Nick Shalek a director) stands; "
         "that report had Settle raising at about $600M. Operating (a $145M credit facility in 2023; a new platform and "
         "an acquisition announced in October 2024). Momentum check: no round at or above $1B found, " + SWEEP + "."))

jl.write("batch-2", L, record=not os.environ.get("DRY"))
