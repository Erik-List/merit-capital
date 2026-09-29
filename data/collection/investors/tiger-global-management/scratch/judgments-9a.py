#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 9, chunk a (rows midas .. mottu). Run: NQ_TAG=b9 python3 judgments-9a.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# midas: the recall headline is about a person, not a company named Midas.
FORBES = "https://www.forbes.com/sites/alexkonrad/2022/10/03/midas-list-investor-john-curtius-leaves-tiger-global/"
L.append(verdict("midas", "not_member",
                 "The recall headline is Forbes on John Curtius leaving Tiger Global ('Midas List' is Forbes' investor "
                 "ranking), not a company named Midas; a Bing News search for Midas with Tiger Global returns only that "
                 "article, and the Turkish broker Midas's 2024 Series A was led by Portage. No record ties the firm to a "
                 "round of any company named Midas",
                 ec="web", conf="high", cite=FORBES))

# miferia
TC_MIF = "https://techcrunch.com/2022/08/08/miferia-wants-to-expand-its-wholesale-inventory-marketplace-across-latin-america/"
PRN_MIF = "https://www.prnewswire.com/news-releases/miferia-raises-7-million-to-digitalize-inventory-procurement-in-mexico-301601172.html"
L.append(verdict("miferia", "member",
                 "TechCrunch (2022-08-08): the $7M seed round 'was co-led by Bain Capital Ventures and Tiger Global'",
                 ec="web", conf="high", cite=TC_MIF))
L.append(cls("miferia", status="private", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=TC_MIF, stage_conf="high", entry_date="2022-08-08",
             rounds=[rnd("2022-08-08", "Seed", 7_000_000, "Bain Capital Ventures; Tiger Global", True, TC_MIF)],
             country="MX", country_src="web_verified", country_cite=PRN_MIF, city="Mexico City",
             focus="Consumer & Marketplaces",
             note="Mexican B2B wholesale marketplace; Tiger co-led its $7M seed (PR Newswire release datelined Mexico "
                  "City). miferia.com now redirects to mercanto.mx (checked 2026-09-29), so the business trades on under "
                  "a new name; no exit or shutdown found. No priced round at $1B or more. Graduation left for the "
                  "graduation pass."))

# milkrun (seeded; Wikipedia and AFR name Tiger's Series A)
AFR_MR = "https://www.afr.com/technology/young-rich-lister-dany-milham-scores-75m-for-milkrun-from-tiger-20220119-p59pi2"
L.append(cls("milkrun", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=W("Milkrun"), stage_conf="high", entry_date="2022-01",
             rounds=[rnd("2022-01-19", "Series A", None, "Tiger Global", True, AFR_MR)],
             country="AU", country_src="web_verified", country_cite=W("Milkrun"), city="Sydney",
             focus="Consumer & Marketplaces",
             note="Sydney grocery quick-commerce startup; Wikipedia: 'It received $75million in a series A round by Tiger "
                  "Global in early 2022' (A$75M, AFR 2022-01-19). Shut down in April 2023 and all staff made redundant "
                  "(AFR 2023-04-11); Woolworths then took over the brand (SMH 2023-05-24), so acquired stands. The Milkrun "
                  "rows at Spark Capital and Y Combinator are a different company (Portland, US)."))

# minka
Y_MINKA = "https://finance.yahoo.com/news/bogota-based-minka-building-tech-161448380.html"
L.append(cls("minka", status="private", rng="below_1b",
             stage="Series A", stage_src="model", stage_cite=Y_MINKA, stage_conf="medium", entry_date="2022-04-27",
             rounds=[rnd("2021", "Seed", None, "FinTech Collective", False, Y_MINKA),
                     rnd("2022-04-27", "funding round ($24M)", 24_000_000, "Tiger Global; Kaszek", True, Y_MINKA)],
             country="CO", country_src="web_verified", country_cite=Y_MINKA, city="Bogotá",
             focus="Fintech & Payments",
             note="Bogota-based payments infrastructure startup (TechCrunch via Yahoo, 2022-04-27): $24M 'in a funding round "
                  "co-led by Tiger Global Management and Kaszek', the first round after the 2021 seed FinTech Collective "
                  "led; the press does not name the series, so Series A is the model's reading of a first post-seed "
                  "round. Momentum check (Bing News, 2026-09-29): no later priced round found."))

# missfresh-ltd (ec=filing: verdict line required)
DRS_MF = "https://www.sec.gov/Archives/edgar/data/1851682/000095012321003839/filename1.htm"
L.append(verdict("missfresh-ltd", "member",
                 "The 2021 IPO DRS lists Series A1, B1, B2, C, E and F preferred shares held by Internet Fund IV Pte. Ltd. "
                 "(a Tiger vehicle controlled by Coleman and Shleifer) while the company was private, with Tiger MD "
                 "Pengfei Wang on the board since June 2017: a private-round position (the SC 13G filings are the later "
                 "listed-company holding)",
                 ec="fund_filing", conf="high", cite=DRS_MF))
L.append(cls("missfresh-ltd", status="defunct", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=DRS_MF, stage_conf="medium", entry_date="2017",
             rounds=[rnd("2017", "Series C", None, "Tiger Global", True, DRS_MF, "filing"),
                     rnd("2018", "Series E", 10_000_000, None, True, DRS_MF, "filing")],
             country="CN", country_src="web_verified", country_cite=DRS_MF, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Beijing online grocery delivery. Tiger's fund holds Series C, E and F preferred (and Series A1/B shares, "
                  "read as bought from earlier holders when Tiger came in; no report ties Tiger to the 2015-2016 rounds), "
                  "and its MD joined the board in June 2017 after the Series C Tiger led, so the entry is Growth, dated "
                  "2017. Listed on Nasdaq June 2021 (former unicorn, ~$2.5B at IPO); stopped paying salaries as it ran out "
                  "of cash in July 2022 (FT), got a Nasdaq delisting notice in November 2023, and its grocery business "
                  "ended: defunct."))

# moglix
VCC_MOG = "https://www.vccircle.com/tiger-global-leads-60-mn-funding-round-in-b2b-marketplace-moglix"
L.append(cls("moglix", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=VCC_MOG, stage_conf="high", entry_date="2019-07-11",
             rounds=[rnd("2019-07-11", "Series D", 60_000_000, "Tiger Global", True, VCC_MOG),
                     rnd("2021-05-17", "Series E", 120_000_000, "Falcon Edge", None, NEWS("moglix", "Moglix joins unicorn club")),
                     rnd("2022-01-28", "Series F", 250_000_000, "Alpha Wave Global; Tiger Global", True,
                         NEWS("moglix", "Moglix Valued At $2.6 Bn"))],
             country="SG", country_src="web_verified", country_cite=NEWS("moglix", "B2B unicorn Moglix cuts losses"),
             city="Singapore", focus="Consumer & Marketplaces",
             note="B2B industrial goods marketplace, Singapore-based per Tech in Asia (2024) with operations in India "
                  "(Noida); aligned with the Accel row. Tiger's entry: the $60M Series D it led in July 2019 (VCCircle); "
                  "earlier rounds were Accel, Jungle Ventures and Sequoia's. Tiger co-led the January 2022 round at $2.6B."))

# moka
Y_MOKA = "https://finance.yahoo.com/news/chinas-hr-tech-startup-moka-032138449.html"
L.append(cls("moka", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=Y_MOKA, stage_conf="high", entry_date="2021-11",
             rounds=[rnd("2021-11", "Series C", 100_000_000, "Tiger Global", True, Y_MOKA)],
             country="CN", country_src="web_verified", country_cite=Y_MOKA, city="Beijing",
             focus="SaaS",
             note="Chinese HR SaaS provider (PR Newswire release datelined Beijing); closed a $100M Series C led by Tiger "
                  "Global in November 2021 (TechCrunch via Yahoo), Tiger's first round on record."))

# momo (Hello Group)
DRS_MOMO = "https://www.sec.gov/Archives/edgar/data/1610601/000095012314006753/filename1.htm"
SA_MOMO = "https://stockanalysis.com/stocks/momo/market-cap/"
L.append(cls("momo", status="public", rng="below_1b", usd=695_910_000, val_src="web_verified", val_cite=SA_MOMO,
             asof="2026-09-28", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=DRS_MOMO, stage_conf="high", entry_date="2014-05-15",
             rounds=[rnd("2014-05-15", "Series D", 31_750_000, None, True, DRS_MOMO, "filing")],
             country="CN", country_src="web_verified", country_cite=DRS_MOMO, city="Beijing",
             focus="Consumer & Marketplaces",
             note="Momo Inc. (renamed Hello Group Inc. in 2021, Nasdaq MOMO), Beijing social and live-video apps. The IPO "
                  "DRS: 6,551,424 Series D preferred issued to Tiger Global Eight Holdings on 2014-05-15 for $31.75M. "
                  "Market cap $695.91M (stockanalysis.com, checked 2026-09-28)."))

# moneyview
L.append(cls("moneyview", status="private", rng="below_1b", usd=623_890_000, val_src="web_verified",
             val_cite=NEWS("moneyview", "Accel-backed Moneyview seeks $624 million valuation"), asof="2026-09-21", extra=WV,
             stage="Growth", stage_src="web_verified",
             stage_cite=NEWS("moneyview", "raises $75 mn in series D funding from Tiger Global"),
             stage_conf="medium", entry_date="2022-03-09",
             rounds=[rnd("2022-03-09", "Series D", 75_000_000, None, True,
                         NEWS("moneyview", "raises $75 mn in series D funding from Tiger Global")),
                     rnd("2022-12-26", "Series E", 75_000_000, "Apis Partners", None,
                         NEWS("moneyview", "Money View raises $75 Mn in Series E at $900 Mn valuation"))],
             country="IN", country_src="web_verified", country_cite=NEWS("moneyview", "FE Best Bank Awards 2026"),
             city="Bangalore", focus="Fintech & Payments",
             note="Bengaluru digital lender. Tiger's first round on record is the $75M Series D of March 2022 at $625M "
                  "(no earlier headline ties Tiger to Money View); Apis led the $75M Series E at $900M in December 2022. "
                  "The IPO (price band Rs 32-34, bidding 2026-09-24 to 09-28, 98x subscribed, allotment 2026-09-29) values "
                  "it at up to Rs 59.85B, $623.89M (Reuters): the IPO price is the newest priced event, and the row stays "
                  "private until the shares list."))

# monnai
BW_MON = ("https://www.businesswire.com/news/home/20230309005305/en/Monnai-Secures-6.5-Million-Series-A-Funding-Led-by-"
          "Tiger-Global-to-Support-Mission-of-Becoming-the-Single-Source-of-Truth-for-Fintech-Decision-making-Globally")
L.append(cls("monnai", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=BW_MON, stage_conf="high", entry_date="2023-03-09",
             rounds=[rnd("2023-03-09", "Series A", 6_500_000, "Tiger Global", True, BW_MON)],
             country="US", city="San Francisco", focus="Fintech & Payments",
             note="Consumer-insights data infrastructure for financial institutions; Business Wire release datelined San "
                  "Francisco: '$6.5 Million Series A Funding Led by Tiger Global' (earlier backers Better Tomorrow "
                  "Ventures, 500 Global, Emphasis Ventures). Momentum check (Bing News, 2026-09-29): no later priced round."))

# mono (Nigeria)
TC_MONO = "https://techcrunch.com/2021/10/11/tiger-global-backs-african-fintech-mono-in-15m-series-a-round/"
L.append(cls("mono", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=TC_MONO, stage_conf="high", entry_date="2021-10-11",
             rounds=[rnd("2021-10-11", "Series A", 15_000_000, "Tiger Global", True, TC_MONO)],
             country="NG", country_src="web_verified", country_cite=NEWS("mono", "Flutterwave buys Nigeria"),
             city="Lagos", focus="Fintech & Payments",
             note="Nigerian open-banking API company (YC W21); Tiger led its $15M Series A (TechCrunch 2021-10-11). "
                  "Flutterwave bought it in an all-stock deal reported at $25M-40M (January 2026). A different Mono, a "
                  "Colombian startup-banking company, raised a $6M seed led by Tiger Global in June 2022 (La Republica, "
                  "LatamList): not this row, and no row of its own in the base."))

# moonfrog-labs
INC_MF = NEWS("moonfrog-labs", "Bangalore Based Game Developer Startup Moonfrog Labs Raises")
L.append(cls("moonfrog-labs", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=INC_MF, stage_conf="high", entry_date="2015-03-12",
             rounds=[rnd("2013", "Seed", 1_000_000, "Sequoia Capital India", False, INC_MF),
                     rnd("2015-03-12", "Series A", 15_000_000, None, True, INC_MF)],
             country="IN", country_src="web_verified", country_cite=INC_MF, city="Bangalore",
             focus="Media, Gaming & Advertising",
             note="Teen Patti Gold maker; inc42 (2015-03-12): $15M 'in Series A from Tiger Global and existing investor "
                  "Sequoia Capital', after a ~$1M seed. Sweden's Stillfront Group bought Moonfrog Labs in February 2021 "
                  "(inc42)."))

# moonpay
L.append(cls("moonpay", status="private",
             stage="Series A", stage_src="web_verified", stage_cite=W("MoonPay"), stage_conf="high", entry_date="2021-11-22",
             rounds=[rnd("2021-11-22", "Series A", 555_000_000, "Tiger Global; Coatue", True, W("MoonPay"))],
             city="Miami", focus="Crypto & Web3",
             note="Wikipedia: 'In its first financing round, MoonPay raised US$555 million in November 2021 in an investment "
                  "led by Tiger Global Management and Coatue Management' (reported as an all-equity Series A at $3.4B). "
                  "Tiger's own internal mark of $2.8B at end-2022 is not a priced round. Aligned with the Coatue and "
                  "Thrive rows."))

# moov (semiconductor equipment marketplace)
BW_MOOV = ("https://www.businesswire.com/news/home/20211111005131/en/Moov-Closes-41M-Series-A-Round-Led-by-Tiger-Global-"
           "to-Help-Solve-the-Global-Chip-Shortage")
L.append(cls("moov", status="acquired", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=BW_MOOV, stage_conf="high", entry_date="2021-11-10",
             rounds=[rnd("2021-11-10", "Series A", 41_000_000, "Tiger Global", True, BW_MOOV)],
             country="US", city="Tempe", focus="Industrial & Robotics",
             note="Marketplace for used semiconductor manufacturing equipment (releases datelined Tempe, Ariz. and Austin, "
                  "Texas); Tiger led its $41M Series A. Axion Semiconductor acquired Moov Technologies (PR Newswire, "
                  "2026-05-21). The a16z row named Moov is a different company (Moov Financial, Cedar Falls)."))

# mottu (membership open)
TC_MOT = "https://techcrunch.com/2022/06/30/mottu-secures-40m-in-debt-equity-to-rent-motorcycles-to-couriers-in-latin-america/"
L.append(verdict("mottu", "member",
                 "TechCrunch (2022-06-30): 'Tiger Global Management participated in both Mottu's Series A and Series B rounds'",
                 ec="web", conf="high", cite=TC_MOT))
L.append(cls("mottu", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=TC_MOT, stage_conf="high", entry_date="2021",
             rounds=[rnd("2021", "Series A", 20_000_000, None, True, TC_MOT),
                     rnd("2022-06-30", "Series B", 30_000_000, "Base Partners; Crankstart", True, TC_MOT),
                     rnd("2023-09-15", "Series C", 50_000_000, None, None, NEWS("mottu", "closes $50M Series C"))],
             country="BR", country_src="web_verified", country_cite=TC_MOT, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="São Paulo motorcycle rental for delivery couriers. TechCrunch: a '$20 million Series A financing in early "
                  "2021', and Tiger participated in both the Series A and the $30M Series B. A $50M Series C followed in "
                  "September 2023 at a premium; no priced round at $1B or more found."))

if __name__ == "__main__":
    jl.write("batch-009a", L)
