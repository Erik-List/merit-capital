#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 10, chunk c (perimeter-solutions-sa .. porter). Run: NQ_TAG=b10 python3 judgments-10c.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# perimeter-solutions-sa (ec=filing: 13G on a listed company)
L.append(verdict("perimeter-solutions-sa", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Perimeter Solutions, "
                 "owned by SK Capital before, listed on the NYSE through EverArc's November 2021 merger, and the adviser's "
                 "SC 13G (from late 2021) and 13F lines are listed-company holdings",
                 ec="fund_filing", conf="high", cite=SEC("perimeter-solutions-sa", "edgar")))

# petlove (seeded; Form D seat of Lee Fixel in 2013 plus the SPAC director bio)
F4_PET = "https://www.sec.gov/Archives/edgar/data/1896049/000119312522028735/d197822df4.htm"
L.append(cls("petlove", status="private", rng="below_1b",
             country="BR", country_src="web_verified", country_cite=F4_PET, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="Brazilian pet e-commerce (a 2022 SEC filing calls it 'private Brazilian pet e-commerce Petlove', an "
                  "investee of Tiger's funds); Lee Fixel sat on PetLove Cayman's January 2013 Form D ($9.8M), the entry "
                  "the Form D band reads as Series A. Still operating in 2025 (it contested the Petz-Cobasi merger at "
                  "CADE). No priced round at $1B or more found."))

# pharmeasy: reports of talks only
L.append(verdict("pharmeasy", "not_member",
                 "The recall headline reports talks ('Tiger Global eyes PharmEasy stake', April 2021; 'in talks to pick up "
                 "stake', May 2021); Bing News for PharmEasy or its parent API Holdings with Tiger Global (2026-09-29) "
                 "finds no report or filing that Tiger invested, so no record ties the firm to a round",
                 ec="web", conf="medium",
                 cite="https://timesofindia.indiatimes.com/business/india-business/tiger-global-eyes-pharmeasy-stake-amid-e-pharmacy-consolidation/articleshow/81928880.cms"))

# phoenix-tree-holdings-ltd (ec=filing: verdict line required; duplicate of danke-phoenix-tree)
F1_DK = "https://www.sec.gov/Archives/edgar/data/1785154/000104746919005933/a2239834zf-1.htm"
L.append(verdict("phoenix-tree-holdings-ltd", "member",
                 "The 2019 IPO F-1: Series A-2, B-2 and C redeemable convertible preferred shares 'collectively held by "
                 "Internet Fund IV Pte. Ltd.', 'ultimately controlled by Tiger Global Management, LLC', while the company "
                 "was private (the 2021 SC 13G is the later listed holding)",
                 ec="fund_filing", conf="high", cite=F1_DK))
L.append(cls("phoenix-tree-holdings-ltd", status="defunct", rng="below_1b", stage="undetermined",
             rounds=[rnd(None, "Series A-2, B-2 and C preferred held (F-1)", None, None, True, F1_DK, "filing")],
             country="CN", country_src="web_verified", country_cite=F1_DK, city="Beijing", flags=["duplicate"],
             focus="Consumer & Marketplaces",
             note="Duplicate of danke-phoenix-tree: Phoenix Tree Holdings is the listed parent of Danke Apartment (NYSE, "
                  "January 2020); flagged here so the company counts once. Tiger's Internet Fund IV held Series A-2, B-2 "
                  "and C preferred, and the filing does not say which it bought first or when, so the stage is "
                  "undetermined. Danke collapsed in 2020 amid unpaid landlords and tenants and was delisted in 2021: "
                  "defunct."))

# phonepe (disputes the acquired status: a separated subsidiary selling priced primary rounds)
ENT_PP = NEWS("phonepe", "PhonePe closes $700 Mn round with participation of Tencent and Tiger")
TC_PP = "https://techcrunch.com/2023/02/14/walmart-phonepe-india/"
L.append(cls("phonepe", status="private", rng="10b_plus", usd=12_000_000_000, val_src="web_verified", val_cite=W("PhonePe"),
             asof="2023-02", extra=WV, flags=["stale", "model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=ENT_PP, stage_conf="high", entry_date="2021-08",
             rounds=[rnd("2021-08", "unnamed ($700M, existing Flipkart investors)", 700_000_000, "Walmart", True, ENT_PP),
                     rnd("2023-02-14", "unnamed ($100M tranche of the 2023 round at $12B)", 100_000_000,
                         "Ribbit Capital; Tiger Global; TVS Capital", True, TC_PP)],
             country="IN", country_src="web_verified", country_cite=W("PhonePe"), city="Bangalore",
             focus="Fintech & Payments",
             note="Status disputed from acquired to private: Flipkart bought PhonePe in 2016, but it separated from Flipkart "
                  "(2020-2022) and sells priced primary rounds to outside investors, so it reads private with its own mark "
                  "(the Waymo reading). Tiger entered in the $700M round of Flipkart's existing investors that closed in "
                  "August 2021 (Entrackr: 'with participation of Tencent and Tiger'), and put in $100M more in February "
                  "2023 at a $12B valuation (TechCrunch, Wikipedia). The IPO filed in 2025-2026 was paused in March 2026 "
                  "and has not listed (CNBCTV18, September 2026), so the 2023 mark stands, stale. Aligned with the Ribbit "
                  "row."))

# physna
BJ_PHY = "https://www.bizjournals.com/cincinnati/inno/stories/news/2021/07/07/physna-raises-56m-tiger-global-gv-sequoia.html"
L.append(cls("physna", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=BJ_PHY, stage_conf="high", entry_date="2021-07-01",
             rounds=[rnd("2021-07-01", "Series B", 56_000_000, "Tiger Global", True, BJ_PHY)],
             country="US", city="Cincinnati", focus="Data Infrastructure",
             note="Cincinnati geometric (3D) search engine; raised $56M 'led by Tiger Global with participation from GV and "
                  "Sequoia Capital' (July 2021), five months after the Sequoia-led Series A, so the Series B. Momentum "
                  "check (Bing News, 2026-09-29): no later priced round. Aligned with the Sequoia row."))

# pine-labs: the recall headline is about Shopflo
L.append(verdict("pine-labs", "not_member",
                 "The recall headline is Pine Labs' April 2026 purchase of 'Tiger Global-backed Shopflo' (Shopflo is its "
                 "own row); Bing News for Pine Labs with Tiger Global (2026-09-29) returns only that deal, and no record "
                 "ties the firm to a round of Pine Labs",
                 ec="web", conf="high",
                 cite="https://www.msn.com/en-in/money/technology/pine-labs-acquires-tiger-global-backed-shopflo-for-88-cr/ar-AA21Hjzy"))

# plum (Indian insurtech)
VCC_PLUM = "https://www.vccircle.com/tiger-global-leads-series-a-funding-in-group-health-insurance-startup-plum"
BL_PLUM = ("https://www.thehindubusinessline.com/companies/group-health-insurance-start-up-plum-raises-156-million-in-series-a-"
           "led-by-tiger-global/article34686496.ece")
L.append(cls("plum", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=VCC_PLUM, stage_conf="high", entry_date="2021-05-31",
             rounds=[rnd("2021-05-31", "Series A", 15_600_000, "Tiger Global", True, VCC_PLUM),
                     rnd("2026-03-25", "Series B", None, "Peak XV Partners", None,
                         "https://www.ciol.com/news/plum-funding-peak-xv-series-b-health-benefits-platform-11265173")],
             country="IN", country_src="web_verified", country_cite=BL_PLUM, city="Bangalore", focus="Fintech & Payments",
             note="Bangalore group health insurance and employee benefits (the JP country was a one-word Wikidata join). "
                  "Tiger led the $15.6M Series A of May 2021 (existing investor Sequoia joined). Momentum check (Bing News, "
                  "2026-09-29): a Rs 193 crore Series B led by Peak XV in March 2026, well below $1B. The Khosla row named "
                  "Plum (US) is a different company."))

# policybazaar
SA_PB = "https://stockanalysis.com/quote/nse/POLICYBZR/market-cap/"
L.append(cls("policybazaar", status="public", rng="1b_plus", usd=5_549_938_971, val_src="web_verified", val_cite=SA_PB,
             asof="2026-09-28", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=W("Policybazaar"), stage_conf="medium",
             rounds=[rnd(None, "Series A", 9_000_000, "Intel Capital; Inventus Capital Partners", False, W("Policybazaar")),
                     rnd("2013-04", "Series B", 5_000_000, "Inventus Capital Partners", False, W("Policybazaar")),
                     rnd("2014-05", "Series C", 20_000_000, None, True, W("Policybazaar")),
                     rnd("2015-04", "Series D", None, "Premji Invest", True,
                         NEWS("policybazaar", "Policybazaar looks to raise Rs 400 crore from its existing investors"))],
             country="IN", country_src="web_verified", country_cite=W("Policybazaar"), city="Gurugram",
             focus="Fintech & Payments",
             note="Gurugram insurance marketplace (PB Fintech, listed November 2021). Wikipedia: the May 2014 $20M Series C "
                  "came 'from existing investors including Tiger Global Management', and the April 2013 Series B names "
                  "only Inventus, Info Edge and Intel, so Tiger came in after the B and by May 2014: Growth, with no entry "
                  "date written. Tiger held about 21% by 2019 (Tiger Global Eight Holdings, Internet Fund III). Market cap "
                  "from the Ribbit row's stockanalysis.com citation (2026-09-28)."))

# polygon (token sale; disputes the acquired status)
CNBC_POL = "https://www.cnbc.com/2022/02/07/sequoia-leads-450-million-investment-in-polygon-blockchain.html"
YS_POL = "https://yourstory.com/the-decrypting-story/funding-alert-polygon-sequoia-tiger-softbank-ethereum"
L.append(cls("polygon", status="private", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=CNBC_POL,
             asof="2022-02-07", extra=WV, flags=["stale", "token_funded", "model_disputes_source", "city_unknown"],
             stage="undetermined", grad="undetermined",
             rounds=[rnd("2022-02-07", "token sale", 450_000_000, "Sequoia Capital India", True, YS_POL)],
             country="IN", country_src="web_verified", country_cite=W("Polygon (blockchain)"),
             focus="Crypto & Web3",
             note="Status disputed from acquired (a one-word join) to private: Polygon Labs is independent. Tiger bought in "
                  "the $450M private sale of MATIC tokens led by Sequoia Capital India (February 2022, Wikipedia, "
                  "YourStory): a token purchase with no priced equity round to stage, so stage and graduation read "
                  "undetermined. Founded in India as Matic Network; its co-founder says it has no headquarters "
                  "(YourStory), so the city is unknown. Band and mark aligned with the General Catalyst and USV rows "
                  "(CNBC, 2022-02-07), stale."))

# pomelo (Argentine card-issuing infrastructure)
CNY_POM = "https://news.cnyes.com/news/id/4751307"
TC_POM = ("https://techcrunch.com/2021/10/21/tiger-global-bets-on-latam-fintech-pomelo-which-just-raised-35m-from-a-slew-"
          "of-high-profile-investors/")
CRO_POM = ("https://www.cronista.com/infotechnology/it-business/pomelo-la-fintech-argentina-que-recibio-us-9-m-busca-70-"
           "nuevos-empleados-en-argentina/")
L.append(cls("pomelo", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=CNY_POM, stage_conf="high", entry_date="2021-10-21",
             rounds=[rnd("2021-05", "Seed", 9_000_000, None, None, CRO_POM),
                     rnd("2021-10-21", "Series A", 35_000_000, "Tiger Global", True, TC_POM),
                     rnd(None, "unnamed ($55M)", 55_000_000, None, None,
                         "https://gestion.pe/economia/empresas/pomelo-recauda-us-55-millones-para-acelerar-expansion-regional-y-desarrollar-pagos-en-stablecoins-noticia/")],
             country="AR", country_src="web_verified", country_cite=CRO_POM, city="Buenos Aires",
             focus="Fintech & Payments",
             note="Buenos Aires card-issuing and payments infrastructure ('la fintech argentina', Cronista). Tiger led the "
                  "$35M Series A of October 2021 (cnyes: A round, Tiger Global led; TechCrunch), after a $9M seed in May "
                  "2021 that names no Tiger. Momentum check (Bing News, 2026-09-29): a later $55M raise and the 2024 Series "
                  "B with Kaszek and Insight, none at $1B or more. The US remittance startup Pomelo ($20M seed 2022) is a "
                  "different company. Aligned with the Insight and 20VC rows."))

# popmenu
BW_POP = ("https://www.businesswire.com/news/home/20210611005326/en/CORRECTING-and-REPLACING-Popmenu-Raises-%2465M-Funding-"
          "Round-Led-by-Tiger-Global-to-Accelerate-A.I.-Powered-Digital-Solution-for-Restaurants")
L.append(cls("popmenu", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=BW_POP, stage_conf="high", entry_date="2021-06-11",
             rounds=[rnd("2020-10-14", "Series B", 17_000_000, "Bedrock Capital", False, None),
                     rnd("2021-06-11", "Series C", 65_000_000, "Tiger Global", True, BW_POP)],
             country="US", city="Atlanta", focus="SaaS",
             note="Atlanta restaurant marketing and ordering software. Tiger led the $65M round of June 2021 at about $525M "
                  "(Business Wire; The Information), which followed the Bedrock-led $17M Series B of October 2020 (Business "
                  "Wire), so it was the Series C. Aligned with the Felicis row."))

# popup-bagels
BBG_PUB = "https://www.bloomberg.com/news/articles/2026-04-10/tiger-global-backs-popup-bagels-at-300-million-valuation"
L.append(cls("popup-bagels", status="private", rng="below_1b", usd=300_000_000, val_src="web_verified", val_cite=BBG_PUB,
             asof="2026-04-10", extra=WV, stage="undetermined",
             rounds=[rnd("2026-03", "undisclosed investment at $300M", None, "Tiger Global", True, BBG_PUB)],
             country="US", city="Westport", focus="Consumer & Marketplaces",
             note="Bagel franchise started in Westport, Connecticut in 2020 (Wikipedia). Tiger agreed in late March 2026 to "
                  "invest an undisclosed amount at a $300M valuation (Bloomberg, 2026-04-10), about five times the "
                  "company's valuation five months earlier; no source names the round, so the stage is undetermined."))

# portalone
BW_P1 = ("https://www.businesswire.com/news/home/20220127005113/en/PortalOne-Raises-60m-Series-A-to-Accelerate-Content-"
         "Production-for-the-World%E2%80%99s-First-Hybrid-Games-Platform")
L.append(cls("portalone", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=BW_P1, stage_conf="medium", entry_date="2022-01-26",
             rounds=[rnd("2021-04-29", "unnamed ($15M)", 15_000_000, None, None,
                         "https://www.pocketgamer.biz/portalone-15-million-mobile-game-tv-mash-ups/"),
                     rnd("2022-01-26", "Series A", 60_000_000, "Tiger Global", True, BW_P1)],
             country="US", city="Los Angeles", focus="Media, Gaming & Advertising",
             note="Hybrid games platform founded by the Kasin brothers; raised a $60M Series A with Tiger Global (Business "
                  "Wire; Business Insider: 'used to raise $60 million from Tiger Global'), after an April 2021 $15M round "
                  "that names no Tiger. Still shipping in 2023 (Forbes). Aligned with the Coatue row."))

# porter (Indian intra-city logistics)
OUT_POR = ("https://www.outlookindia.com/business/business-news-porter-raises-rs-750-crore-in-series-e-funding-from-tiger-"
           "global-vitruvian-partners-news-398695")
MSN_POR = ("https://www.msn.com/en-in/money/markets/porter-joins-unicorn-club-with-200-million-funding-round-valuation-hits-"
           "1-2-billion/ar-AA1EpaYT")
L.append(cls("porter", status="private", rng="1b_plus", usd=1_200_000_000, val_src="web_verified", val_cite=MSN_POR,
             asof="2025-05-08", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=OUT_POR, stage_conf="high", entry_date="2021-10-25",
             rounds=[rnd("2021-10-25", "Series E", None, "Tiger Global; Vitruvian Partners", True, OUT_POR),
                     rnd("2024-05", "internal round at $1B", None, None, None,
                         NEWS("porter", "Porter quietly turns unicorn")),
                     rnd("2025-05-08", "Series F", 200_000_000, "Kedaara Capital; Wellington Management", None, MSN_POR)],
             country="IN", country_src="web_verified", country_cite=OUT_POR, city="Bangalore",
             focus="Consumer & Marketplaces",
             note="Bangalore intra-city goods transport marketplace. Tiger co-led the Rs 750 crore Series E of October 2021 "
                  "at Rs 3,750 crore (Mint, Outlook India), its first round. The May 2025 $200M Series F led by Kedaara and "
                  "Wellington valued Porter at $1.2B (MSN). The Y Combinator row named Porter (New York) is a different "
                  "company."))

if __name__ == "__main__":
    jl.write("batch-010c", L)
