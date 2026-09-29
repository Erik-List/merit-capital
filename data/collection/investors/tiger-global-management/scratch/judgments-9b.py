#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 9, chunk b (rows mr-yum .. nomad). Run: NQ_TAG=b9 python3 judgments-9b.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# mr-yum
Y_MRY = "https://finance.yahoo.com/news/melbourne-based-mobile-ordering-platform-140038794.html"
L.append(cls("mr-yum", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=Y_MRY, stage_conf="high", entry_date="2021-11-29",
             rounds=[rnd("2021-04", "Post-seed", 8_000_000, None, False, Y_MRY),
                     rnd("2021-11-29", "Series A", 65_000_000, "Tiger Global", True, Y_MRY)],
             country="AU", country_src="web_verified", country_cite=Y_MRY, city="Melbourne", focus="SaaS",
             note="Melbourne mobile ordering and payments platform for restaurants (TechCrunch via Yahoo): 'a $65 million "
                  "USD Series A round, led by Tiger Global', seven months after an $8M post-seed Tiger was not in. Merged "
                  "with the UK's Ready in 2023 and trades as me&u; no sale of the company found."))

# multiplier
VCC_MUL = "https://www.vccircle.com/multiplier-valuation-touches-400-mn-after-series-b-co-led-round-by-tiger-global-sequoia"
NAS_MUL = "https://www.nasdaq.com/press-release/global-employment-platform-multiplier-raises-$60m-led-by-tiger-global-sequoia-capital"
L.append(cls("multiplier", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=VCC_MUL, stage_conf="medium", entry_date="2022-03-15",
             rounds=[rnd("2022-03-15", "Series B", 60_000_000, "Tiger Global; Sequoia Capital India", True, VCC_MUL)],
             country="SG", country_src="web_verified", country_cite=NAS_MUL, city="Singapore", focus="SaaS",
             note="Global employment (employer-of-record) platform, 'Founded in Singapore in 2020' (the company's release). "
                  "Tiger co-led the $60M Series B at a $400M valuation (VCCircle), its first round on record. The Y "
                  "Combinator row named Multiplier (New York, AI) looks like a different company."))

# mutiny (membership open)
TC_MUT = "https://techcrunch.com/2022/04/20/mutiny-which-personalizes-website-copy-and-headlines-using-ai-raises-50m/"
L.append(verdict("mutiny", "member",
                 "TechCrunch (2022-04-20): Mutiny 'raised $50 million in a Series B round co-led by Tiger Global and "
                 "Insight Partners at a $600 million valuation'",
                 ec="web", conf="high", cite=TC_MUT))
L.append(cls("mutiny", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=TC_MUT, stage_conf="high", entry_date="2022-04-20",
             rounds=[rnd("2022-04-20", "Series B", 50_000_000, "Tiger Global; Insight Partners", True, TC_MUT)],
             country="US", city="San Francisco", focus="SaaS",
             note="San Francisco website-personalization software (YC S18). Tiger co-led the $50M Series B at $600M; no "
                  "earlier round names Tiger. Aligned with the Sequoia row; the Y Combinator row placed in New York may be "
                  "a different company of the same name."))

# mygate
L.append(cls("mygate", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=W("MyGate"), stage_conf="high", entry_date="2019-10",
             rounds=[rnd("2018-01", "Seed", 2_500_000, "Prime Venture Partners", False, W("MyGate")),
                     rnd("2018-10", "Series A", None, "Prime Venture Partners", False, W("MyGate")),
                     rnd("2019-10", "Series B", 56_000_000, "Tiger Global; Tencent", True, W("MyGate")),
                     rnd("2022-11", "unnamed (Rs 100 crore)", None, "Urban Company; Acko", None, W("MyGate"))],
             country="IN", country_src="web_verified", country_cite=W("MyGate"), city="Bangalore", focus="SaaS",
             note="Gated-community security and management app, headquartered in Bangalore (Wikipedia). Tiger came in at "
                  "the October 2019 $56M Series B with Tencent, JS Capital and existing investor PVP."))

# myntra
VCC_MYN = "https://www.vccircle.com/myntra-secures-20m-tiger-global-others"
L.append(cls("myntra", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=W("Myntra"), stage_conf="high",
             rounds=[rnd("2008-11", "Series A", 5_000_000, None, False, W("Myntra")),
                     rnd(None, "Series B", 14_000_000, "Tiger Global", True, W("Myntra")),
                     rnd("2012-02-08", "Series C", 20_000_000, "Tiger Global", True, VCC_MYN)],
             country="IN", country_src="web_verified", country_cite=W("Myntra"), city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Bengaluru fashion e-commerce. Wikipedia: the $14M Series B 'was led by Tiger Global', after the November "
                  "2008 round Tiger was not in; VCCircle (2012-02-08): the $20M Series C, 'led by Tiger Global'. The "
                  "Series B date is not on the cited page (it falls between November 2008 and late 2011), so no entry "
                  "date is written. Flipkart bought Myntra in May 2014; Tiger and Accel were common shareholders."))

# naspers: a co-investor in the recall headline, not a portfolio company
TC_AVE = ("https://techcrunch.com/2015/11/20/argentinian-e-commerce-leader-avenida-gets-30m-series-c-round-from-naspers-"
          "and-tiger-global/")
L.append(verdict("naspers", "not_member",
                 "The recall headline is Avenida's $30M Series C, in which Naspers invested beside Tiger Global: Naspers is "
                 "the co-investor, a JSE-listed South African internet group, and no record ties the firm to a round of "
                 "Naspers (Avenida is its own row, avenida-inc)",
                 ec="web", conf="high", cite=TC_AVE))

# near-protocol (token round)
BLOCK_NEAR = ("https://www.theblock.co/news/ecosystems/2022-04-06-near-protocol-raises-350-million-in-new-funding-round-"
              "led-by-tiger-global-140751")
L.append(cls("near-protocol", status="private", rng="below_1b",
             stage="undetermined", grad="undetermined",
             rounds=[rnd("2022-04-06", "token round", 350_000_000, "Tiger Global", True, BLOCK_NEAR)],
             country="CH", country_src="web_verified", country_cite=NEWS("near-protocol", "Swiss-Based NEAR Foundation"),
             city="Zug", flags=["token_funded"], focus="Crypto & Web3",
             note="Tiger led the $350M raise of April 2022 (The Block, Bloomberg), money that went in as purchases of NEAR "
                  "tokens: no priced equity round to stage, so stage and graduation read undetermined (token rule). The "
                  "issuing organisation is the Swiss-based NEAR Foundation (Zug). No priced round states a valuation; the "
                  "token's market price is not a company mark, so the band stays below_1b."))

# nestaway
ET_NEST = ("https://retail.economictimes.indiatimes.com/news/e-commerce/e-tailing/flipkart-tiger-global-team-up-to-invest-"
           "rs-76-crore-in-online-home-rental-startup-nestaway/48167922")
BL_NEST = NEWS("nestaway", "NestAway raises $30 m in series C funding")
L.append(cls("nestaway", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=ET_NEST, stage_conf="medium", entry_date="2015-07",
             rounds=[rnd("2015-07-22", "Series B", 12_000_000, "Tiger Global", True, ET_NEST),
                     rnd("2016-04-17", "Series C", 30_000_000, "Tiger Global; Yuri Milner; IDG Ventures", True, BL_NEST)],
             country="IN", country_src="web_verified", country_cite=BL_NEST, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Bangalore managed home rentals. Tiger first invested in the July 2015 Rs 76 crore ($12M) round with "
                  "Flipkart (ET Retail); the April 2016 $30M round was the Series C Tiger co-led (Business Line), so the "
                  "2015 round was the B. Aurum PropTech bought 100% of NestAway for up to Rs 90 crore (~$11M) in June "
                  "2023 (VCCircle)."))

# new-oriental (ec=filing: verdict line required)
F1_EDU = "https://www.sec.gov/Archives/edgar/data/1372920/000119312506177813/df1.htm"
SA_EDU = "https://stockanalysis.com/stocks/edu/market-cap/"
L.append(verdict("new-oriental-education-technology-group-inc", "member",
                 "The 2006 IPO F-1: 'In December 2004, we issued an aggregate of 11,111,111 preferred shares to the "
                 "entities affiliated with Tiger Global in a private placement'; the principal-shareholder table names "
                 "Tiger Global Private Investment Partners II, L.P. (a PIP vehicle). The SC 13G filings are the later "
                 "listed-company holding",
                 ec="fund_filing", conf="high", cite=F1_EDU))
L.append(cls("new-oriental-education-technology-group-inc", status="public", rng="1b_plus", usd=8_420_000_000,
             val_src="web_verified", val_cite=SA_EDU, asof="2026-09-29", extra=WV,
             stage="Series A", stage_src="web_verified", stage_cite=F1_EDU, stage_conf="high", entry_date="2004-12",
             rounds=[rnd("2004-12", "Series A preferred (private placement)", None, "Tiger Global", True, F1_EDU, "filing")],
             country="CN", country_src="web_verified", country_cite=F1_EDU, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Beijing private education group (NYSE EDU since September 2006). The F-1 says its financing consisted of "
                  "Series A convertible preferred shares, all of it the December 2004 placement to Tiger's funds: the "
                  "record names the round Series A, though the company was then eleven years old and profitable. Market "
                  "cap $8.42B (stockanalysis.com, 2026-09-29)."))

# new-york-life-insurance-co (Form D name-match)
L.append(verdict("new-york-life-insurance-co", "not_member",
                 "ALEXANDER COOK on these 2023-2024 Form Ds is a director of New York Life Insurance & Annuity Corp (New "
                 "York, NY), the New York Life officer the brief names as a homonym of Tiger's Alex Cook; the filings are "
                 "an insurer's annuity offerings, not a venture round, and no Tiger record names the company",
                 ec="formd_adjudicated", conf="high", cite=SEC("new-york-life-insurance-co")))

# nextdoor
LAT_ND = NEWS("nextdoor", "Nextdoor raises $60 million from Kleiner Perkins, Tiger Global")
L.append(cls("nextdoor", city="San Francisco",
             stage="Growth", stage_src="web_verified", stage_cite=LAT_ND, stage_conf="high", entry_date="2013-10-29",
             rounds=[rnd("2013-10-29", "Series D", 60_000_000, "Kleiner Perkins; Tiger Global", True, LAT_ND)],
             focus="Consumer & Marketplaces",
             note="Tiger (Lee Fixel) and Kleiner Perkins were the new investors leading Nextdoor's $60M round of October "
                  "2013 (Los Angeles Times, USA Today), its fourth venture round; Tiger's PIP VII vehicles still held "
                  "legacy shares at the 2021 de-SPAC. Public (NYSE KIND, now NXDR) below $1B."))

# ninjacart
YS_NIN = NEWS("ninjacart", "into Ninjacart's Series C round")
BL_NIN = "https://www.thehindubusinessline.com/economy/agri-business/tiger-global-invests-625-cr-in-agri-tech-firm-ninjacart/article26934370.ece"
L.append(cls("ninjacart", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=YS_NIN, stage_conf="high", entry_date="2019-04-23",
             rounds=[rnd("2019-04-23", "Series C", 89_000_000, "Tiger Global", True, YS_NIN)],
             country="IN", country_src="web_verified", country_cite=BL_NIN, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Bangalore B2B agri supply-chain marketplace. Tiger wrote the roughly $89M-100M Series C cheque in April "
                  "2019 (YourStory, Business Line), its first round; earlier rounds were Accel's and others'. No priced "
                  "round at $1B or more found."))

# nobroker
ENT_NB = NEWS("nobroker", "Tiger Global leads $50 Mn Series D round in NoBroker")
L.append(cls("nobroker", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=ENT_NB, stage_conf="high", entry_date="2019-10-02",
             rounds=[rnd("2019-10-02", "Series D", 50_000_000, "Tiger Global", True, ENT_NB),
                     rnd("2021-11-23", "Series E", 210_000_000, "General Atlantic; Tiger Global; Moore", True,
                         "https://www.businesstoday.in/entrepreneurship/story/nobroker-becomes-indias-first-proptech-unicorn-plans-heavy-investment-on-apartment-management-services-313130-2021-11-23")],
             country="IN", country_src="web_verified", country_cite=W("NoBroker"), city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Bangalore brokerage-free property marketplace. Tiger led the $50M Series D of October 2019 (Entrackr), "
                  "its first round, and joined the November 2021 $210M round that made NoBroker a unicorn."))

# noho-dental-inc (Form D name-match, Addition era)
L.append(verdict("noho-dental-inc", "not_member",
                 "Lee Fixel's director seat on NoHo Dental's 2021 Form D falls in his Addition years: from 2019 on his "
                 "investments are Addition's (D7 names NoHo Dental), and no Tiger round in the company is on record",
                 ec="formd_adjudicated", conf="high", cite=SEC("noho-dental-inc")))

# nomad
REU_NOM = "https://www.reuters.com/article/technology/brazil-fintech-nomad-raises-61-million-in-tiger-led-round-idUSL1N3A21UG/"
L.append(cls("nomad", status="private", rng="below_1b", usd=361_490_000, val_src="web_verified", val_cite=REU_NOM,
             asof="2023-08-22", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=NEWS("nomad", "Série B liderada pela Tiger Global"),
             stage_conf="medium", entry_date="2023-08-22",
             rounds=[rnd("2023-08-22", "Series B", 61_000_000, "Tiger Global", True, REU_NOM)],
             country="BR", country_src="web_verified", country_cite=REU_NOM, city="São Paulo",
             focus="Fintech & Payments",
             note="São Paulo fintech for Brazilians' international accounts and investing; the JP country was a one-word "
                  "Wikidata join. Tiger led the $61M Series B (PEGN) valuing Nomad at 1.8 billion reais, $361.49M "
                  "(Reuters, 2023-08-22), its first round on record. Momentum check (Bing News, 2026-09-29): no later "
                  "priced round, only 2025 product launches. Aligned with the Spark row."))

if __name__ == "__main__":
    jl.write("batch-009b", L)
