#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 10, chunk b (outsystems .. pento). Run: NQ_TAG=b10 python3 judgments-10b.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# outsystems
L.append(cls("outsystems", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=W("OutSystems"), stage_conf="high", entry_date="2021-02-17",
             rounds=[rnd("2021-02-17", "unnamed ($150M at $9.5B)", 150_000_000, "Abdiel Capital; Tiger Global", True,
                         W("OutSystems"))],
             city="Boston", focus="DevTools & APIs",
             note="Low-code development platform founded in Portugal, headquartered in Boston. Wikipedia: 'In 2021, "
                  "OutSystems raised $150 million at a reported $9.5 billion valuation in a round led by Abdiel Capital and "
                  "Tiger Global' (February 2021), Tiger's first round, after KKR and Goldman's 2018 investment."))

# overstock-com-inc (ec=filing: 13G on a listed company)
L.append(verdict("overstock-com-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the adviser's SC 13G "
                 "filings of 2003-2006 cover Overstock.com, listed on Nasdaq since its May 2002 IPO, before Tiger's "
                 "private-equity funds began investing",
                 ec="fund_filing", conf="high", cite=SEC("overstock-com-inc", "edgar")))

# own (Own Company, formerly OwnBackup): the recall headline was a false match, the company is a real position
FP_OWN = ("https://financialpost.com/pmn/press-releases-pmn/business-wire-news-releases-pmn/ownbackup-approaches-3-35-billion-"
          "valuation-with-series-e-investment-expands-its-leading-cloud-to-cloud-data-protection-to-microsoft")
L.append(verdict("own", "member",
                 "The recall headline (The Information on John Curtius leaving 'to Launch His Own Fund') is a false name "
                 "match, but the row is Own Company, formerly OwnBackup (Salesforce's $1.9B purchase of 'Own', 2024): "
                 "OwnBackup's $240M Series E of August 2021 'includes investments from Alkeon Capital, B Capital Group, "
                 "BlackRock Private Equity Partners, Tiger Global' (company release)",
                 ec="web", conf="high", cite=FP_OWN))
L.append(cls("own", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=FP_OWN, stage_conf="medium", entry_date="2021",
             rounds=[rnd("2021-01", "Series D", 167_500_000, None, None,
                         "https://pulse2.com/ownbackup-167-5-million-funding-and-nearly-1-4-billion-valuation/"),
                     rnd("2021-08-10", "Series E", 240_000_000, "Alkeon Capital; B Capital Group", True, FP_OWN)],
             country="US", city="Englewood Cliffs", focus="Security",
             note="SaaS data backup and protection company (OwnBackup, renamed Own Company in 2023), US-Israeli, based in "
                  "Englewood Cliffs, New Jersey. Tiger is named in the $240M Series E at $3.35B (August 2021); whether it "
                  "was already in the January 2021 Series D is not on record, so the entry is dated 2021, Growth either "
                  "way. Salesforce bought Own for $1.9B in cash (announced September 2024). Aligned with the Insight row."))

# oxyzo
BL_OXY = ("https://www.thehindubusinessline.com/companies/oxyzo-financial-services-raises-200-mn-series-a-at-1-bn-valuation/"
          "article65251878.ece")
INC_OXY = ("https://inc42.com/buzz/ofbusiness-financial-arm-oxyzo-becomes-indias-98th-unicorn-after-raising-countrys-"
           "biggest-series-a/")
L.append(cls("oxyzo", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=BL_OXY,
             asof="2022-03-22", extra=WV, flags=["stale"],
             stage="Series A", stage_src="web_verified",
             stage_cite=NEWS("oxyzo", "turns unicorn with record $200M Series A from Tiger Global"), stage_conf="high",
             entry_date="2022-03-22",
             rounds=[rnd("2022-03-22", "Series A", 200_000_000, "Alpha Wave Global", True, BL_OXY)],
             country="IN", country_src="web_verified", country_cite=INC_OXY, city="Gurugram",
             focus="Fintech & Payments",
             note="Gurugram non-bank lender, the lending arm of OfBusiness with its own outside equity. Tiger and Alpha Wave "
                  "were in its record $200M Series A at a $1B valuation (March 2022). Momentum check (Bing News, "
                  "2026-09-29): a Series B was planned in May 2025 (VCCircle) and debt raised since, but no later priced "
                  "equity round, so the mark stands, stale."))

# pagaya-technologies-ltd (ec=filing: verdict line required)
DRS_PGY = "https://www.sec.gov/Archives/edgar/data/1883085/000095012321015882/filename2.htm"
L.append(verdict("pagaya-technologies-ltd", "member",
                 "Pagaya's DRS: a Series E preferred share purchase agreement with Tiger Global Private Investment Partners "
                 "XIV dated March 17, 2021, and Tiger holding 52.7m shares before the listing: a private-round position "
                 "(the SC 13G filings are the later listed holding)",
                 ec="fund_filing", conf="high", cite=DRS_PGY))
L.append(cls("pagaya-technologies-ltd", country="US", city="New York",
             stage="Growth", stage_src="web_verified", stage_cite=DRS_PGY, stage_conf="high", entry_date="2021-03-17",
             rounds=[rnd("2021-03-17", "Series E", None, None, True, DRS_PGY, "filing")],
             focus="Fintech & Payments",
             note="AI credit network founded in Tel Aviv, now run from New York with R&D in Israel. Tiger's PIP XIV entered "
                  "at the Series E of March 2021 (DRS). Listed on Nasdaq through the EJF Acquisition merger in June 2022."))

# pandora-media-inc (ec=filing: 13G/13F on a listed company)
L.append(verdict("pandora-media-inc", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): Pandora listed on the "
                 "NYSE in June 2011, the 13F layer lists it only at 2012-12-31 and the adviser's SC 13G filings date from "
                 "2013-2014",
                 ec="fund_filing", conf="high", cite=SEC("pandora-media-inc", "edgar")))

# papa
BW_PAPA = "https://www.businesswire.com/news/home/20210413005053/en/Papa-Announces-60-Million-in-Series-C-Funding-Led-by-Tiger-Global"
HIT_PAPA = "https://hitconsultant.net/2021/11/04/papa-senior-companion-platform-funding/"
L.append(cls("papa", status="private", rng="1b_plus", usd=1_400_000_000, val_src="web_verified", val_cite=HIT_PAPA,
             asof="2021-11-04", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=BW_PAPA, stage_conf="high", entry_date="2021-04-13",
             rounds=[rnd("2021-04-13", "Series C", 60_000_000, "Tiger Global", True, BW_PAPA),
                     rnd("2021-11-04", "Series D", 150_000_000, "SoftBank Vision Fund 2", None, HIT_PAPA)],
             country="US", city="Miami", focus="Healthcare & Bio",
             note="Miami companionship and in-home help for older adults (YC). Tiger led the $60M Series C of April 2021, its "
                  "first round; the SoftBank-led $150M Series D valued Papa at $1.4B (November 2021). No later priced "
                  "round or collapse evidence found, so the mark stands, stale; aligned with the Y Combinator row."))

# papaya-global
L.append(cls("papaya-global", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=W("Papaya Global"), stage_conf="high", entry_date="2021-09",
             rounds=[rnd("2019-11", "Series A", 45_000_000, "Insight Partners; Bessemer Venture Partners", False, W("Papaya Global")),
                     rnd("2020-09", "Series B", 40_000_000, "Scale Venture Partners; Workday Ventures", False, W("Papaya Global")),
                     rnd("2021-03", "Series C", 100_000_000, "GreenOaks Capital Partners", False, W("Papaya Global")),
                     rnd("2021-09", "Series D", 250_000_000, "Insight Partners; Tiger Global", True, W("Papaya Global"))],
             country="US", city="New York", focus="SaaS",
             note="Global payroll and workforce payments platform founded in Israel; Wikipedia: 'headquartered in New York "
                  "City' with offices in Herzliya and elsewhere (the Insight row's Tel Aviv reads the R&D base; the IVP "
                  "row agrees on New York). Tiger's entry is the $250M Series D it co-led at $3.7B in September 2021; the "
                  "A to C rounds name other leads. Sale talks at $3.5B-4.5B were reported in January 2026, nothing signed."))

# parallel-learning
BI_PAR = "https://www.businessinsider.com/pitch-deck-startup-parallel-health-kids-tiger-dyslexia-global-2022-5"
L.append(cls("parallel-learning", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=BI_PAR, stage_conf="high", entry_date="2022-05-24",
             rounds=[rnd("2022-05-24", "Series A", 20_000_000, "Tiger Global", True, BI_PAR)],
             country="US", city="New York", focus="Healthcare & Bio",
             note="New York virtual psychoeducational evaluation and therapy for children with learning differences; raised "
                  "$20M from Tiger Global (Business Insider), reported as its Series A (Behavioral Health Business)."))

# patreon
SEC_PAT = "https://www.sec.gov/Archives/edgar/data/1883788/000095012321015995/filename1.htm"
L.append(cls("patreon", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=SEC_PAT, stage_conf="high", entry_date="2021-04-07",
             rounds=[rnd("2014-06", "Series A", 15_000_000, "Index Ventures", False, W("Patreon")),
                     rnd("2016-01", "Series B", 30_000_000, "Thrive Capital", False, W("Patreon")),
                     rnd("2021-04-07", "Series F", 155_000_000, "Tiger Global", True, SEC_PAT, "filing")],
             country="US", city="San Francisco", focus="Media, Gaming & Advertising",
             note="San Francisco creator-membership platform. A 2021 SEC filing describes Patreon's Series F, whose 'lead "
                  "investors include Tiger Global Management' ($155M at $4B, April 2021); no earlier round names Tiger "
                  "(Google News, 2026-09-29). Aligned with the Coatue and Thrive rows."))

# payglocal
VCC_PGL = "https://www.vccircle.com/sequoia-cred-s-kunal-shah-others-invest-12-mn-in-fintech-firm-payglocal"
L.append(cls("payglocal", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=VCC_PGL, stage_conf="high", entry_date="2022-06-18",
             rounds=[rnd("2021-12-02", "Series A", 4_900_000, "Sequoia Capital India", False,
                         "https://inc42.com/buzz/payglocal-raises-4-9-mn-to-enable-cross-border-payments/"),
                     rnd("2022-06-18", "Series B", 12_000_000, "Tiger Global; Sequoia Capital India", True, VCC_PGL)],
             country="IN", country_src="web_verified", country_cite=VCC_PGL, city="Bangalore", focus="Fintech & Payments",
             note="Bengaluru cross-border payments company. VCCircle: 'Series B funding of $12 million ... co-led by Tiger "
                  "Global and Sequoia Capital India' (June 2022), after the Sequoia-led $4.9M Series A. Got an in-principle "
                  "RBI payment aggregator licence in 2023. Momentum check (Bing News, 2026-09-29): no later priced round."))

# paytm: the recall headline is about Cube26
L.append(verdict("paytm", "not_member",
                 "The recall headline is Paytm's 2018 purchase of 'Tiger Global-backed technology firm Cube26' (Cube26 is "
                 "its own row); no record ties the firm to a round of Paytm (One97 Communications), whose backers were "
                 "Alibaba, Ant, SoftBank, SAIF and Berkshire",
                 ec="web", conf="high",
                 cite="https://www.moneycontrol.com/news/business/startup/paytm-acquires-tiger-global-backed-technology-firm-cube26-2606261.html"))

# pdax
Y_PDAX = "https://finance.yahoo.com/news/philippines-crypto-exchange-pdax-raises-121926173.html"
L.append(cls("pdax", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=Y_PDAX, stage_conf="high", entry_date="2022-02-10",
             rounds=[rnd("2022-02-10", "Series B", 50_000_000, "Tiger Global", True, Y_PDAX)],
             country="PH", country_src="web_verified", country_cite=Y_PDAX, flags=["city_unknown"],
             focus="Crypto & Web3",
             note="Philippine Digital Asset Exchange, a Philippine crypto exchange; Tiger led its $50M Series B (February "
                  "2022, CoinDesk via Yahoo). Its offices are in Metro Manila, but no source read names the municipality, "
                  "so the city is left unknown. Momentum check (Bing News, 2026-09-29): no later priced round, only 2024 "
                  "partnership news."))

# peloton (disputes the Form D seed band with the documented round)
BJ_PEL = NEWS("peloton", "Peloton gets $10.5M to help people not sweat")
SA_PEL = "https://stockanalysis.com/stocks/pton/market-cap/"
L.append(cls("peloton", status="public", rng="1b_plus", usd=2_100_000_000, val_src="web_verified", val_cite=SA_PEL,
             asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=BJ_PEL, stage_conf="medium", entry_date="2014-04-24",
             rounds=[rnd("2014-04-24", "Series B", 10_500_000, "Tiger Global", True, BJ_PEL)],
             city="New York", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             note="The Form D band read the June 2014 filing ($6.0M sold, Lee Fixel as director) as a seed; the filing is a "
                  "close of the $10.5M round Tiger joined in April 2014 (Business Journals, found beside Tiger Global in a "
                  "Google News search), Peloton's second venture round after a $3.5M Series A, so the entry is the Series "
                  "B, Growth. The IPO DRS defines 'Tiger' as PIP VII. Nasdaq PTON; market cap $2.1B (stockanalysis.com, "
                  "2026-09-29); aligned with the Coatue row."))

# pento
BI_PEN = "https://markets.businessinsider.com/news/stocks/pento-payroll-startup-raises-35m-series-b-tiger-global-2021-12"
ES_PEN = ("https://www.standard.co.uk/business/pento-london-payroll-startup-led-by-28-year-old-raises-35-million-in-round-"
          "led-by-new-york-based-vc-tiger-global-avid-ventures-b970410.html")
L.append(cls("pento", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=BI_PEN, stage_conf="high", entry_date="2021-12-07",
             rounds=[rnd("2021-12-07", "Series B", 35_000_000, "Tiger Global; Avid Ventures", True, BI_PEN)],
             country="GB", country_src="web_verified", country_cite=ES_PEN, city="London", focus="SaaS",
             note="London payroll automation (Danish founders); Tiger and Avid Ventures led its $35M Series B, the company's "
                  "second round of 2021 (Business Insider), after the seed Point Nine was in. HiBob acquired Pento in "
                  "February 2024 (Business Insider). Aligned with the General Catalyst and Point Nine rows."))

if __name__ == "__main__":
    jl.write("batch-010b", L)
