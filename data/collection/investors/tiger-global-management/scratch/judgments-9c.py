#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 9, chunk c (moveworks and notco .. oico). Run: NQ_TAG=b9 python3 judgments-9c.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

L = []
WV = {"valuation_range_source": "web_verified"}

# moveworks
VB_MW = "https://venturebeat.com/business/moveworks-raises-200m-to-automate-enterprise-it-tasks/"
L.append(cls("moveworks", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=VB_MW, stage_conf="high", entry_date="2021-06-30",
             rounds=[rnd("2021-06-30", "Series C", 200_000_000, "Tiger Global; Alkeon Capital", True, VB_MW)],
             city="Mountain View", focus="AI & Applied AI",
             note="VentureBeat (2021-06-30): 'a $200 million series C funding round led by Tiger Global and Alkeon "
                  "Capital'; the Series A and B were Lightspeed's, Bain's and ICONIQ's rounds. ServiceNow agreed in March "
                  "2025 to buy Moveworks for $2.85B and the deal closed; aligned with the three sibling rows."))

# notco (membership open)
FBN_NOT = "https://www.foodbusinessnews.net/articles/19186-notco-raises-235-million"
FN_NOT = NEWS("notco", "NotCo raises $85m to expand plant-based empire")
L.append(verdict("notco", "member",
                 "Food Business News (2021-07-26): NotCo 'raised $235 million in a Series D funding round led by Tiger "
                 "Global' (City A.M.: valued at $1.5bn after the round Tiger led)",
                 ec="web", conf="high", cite=FBN_NOT))
L.append(cls("notco", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=FBN_NOT, stage_conf="high", entry_date="2021-07-26",
             rounds=[rnd("2020-09-09", "Series C", 85_000_000, "Future Positive; L Catterton", None, FN_NOT),
                     rnd("2021-07-26", "Series D", 235_000_000, "Tiger Global", True, FBN_NOT),
                     rnd("2022-12-11", "Series D1", 70_000_000, None, None, NEWS("notco", "Closes $70M in Funding"))],
             country="CL", country_src="web_verified", country_cite=FN_NOT, city="Santiago",
             focus="Consumer & Marketplaces",
             note="Santiago-based food-tech (FoodNavigator), with a US office in New York. The September 2020 $85M Series C "
                  "was co-led by Future Positive and L Catterton, not by Tiger (the inferred 'Tiger led the C' recall line "
                  "was wrong); Tiger's first round on record is the $235M Series D it led in July 2021 at $1.5B. Aligned "
                  "with the General Catalyst row."))

# nothing
YS_NOTH = "https://yourstory.com/2025/09/nothing-smartphones-series-c-funding-tiger-global-nikhil-kamath-unicorn"
L.append(cls("nothing", status="private", rng="1b_plus", usd=1_300_000_000, val_src="web_verified", val_cite=YS_NOTH,
             asof="2025-09-15", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=W("Nothing (company)"), stage_conf="high",
             entry_date="2025-09-15",
             rounds=[rnd("2022", "Series B", 70_000_000, None, False, W("Nothing (company)")),
                     rnd("2025-09-15", "Series C", 200_000_000, "Tiger Global", True, YS_NOTH)],
             country="GB", country_src="web_verified", country_cite=W("Nothing (company)"), city="London",
             focus="Consumer & Marketplaces",
             note="Carl Pei's consumer electronics company, 'headquartered in London' (Wikipedia); the FR country was a "
                  "one-word Wikidata join. Tiger led the $200M Series C at a $1.3B valuation in September 2025, its first "
                  "round (earlier backers GV, EQT Ventures, C Ventures, Highland Europe). Aligned with the EQT Ventures row."))

# nowports (membership open)
PRN_NOW = "https://www.prnewswire.com/news-releases/nowports-raises-60m-usd-to-revolutionize-latams-supply-chain-301445856.html"
Y_NOW = "https://finance.yahoo.com/news/mexicos-nowports-gains-unicorn-status-170849355.html"
L.append(verdict("nowports", "member",
                 "Nowports' release (PR Newswire, 2021-12-16): it 'closed its Series B investment round of $ 60M, led by "
                 "Tiger Global'; Tiger also joined the May 2022 Series C",
                 ec="web", conf="high", cite=PRN_NOW))
L.append(cls("nowports", status="private", rng="1b_plus", usd=1_100_000_000, val_src="web_verified", val_cite=Y_NOW,
             asof="2022-05-24", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=PRN_NOW, stage_conf="high", entry_date="2021-12-16",
             rounds=[rnd("2021-07-01", "Series A", 16_000_000, None, None, NEWS("nowports", "LatAm’s shipping industry")),
                     rnd("2021-12-16", "Series B", 60_000_000, "Tiger Global", True, PRN_NOW),
                     rnd("2022-05-24", "Series C", 150_000_000, "SoftBank Latin America Fund", True, Y_NOW)],
             country="MX", country_src="web_verified", country_cite=PRN_NOW, city="Monterrey", focus="SaaS",
             note="Monterrey digital freight forwarder (YC). The July 2021 $16M Series A names Mouro Capital and others, not "
                  "Tiger; Tiger led the December 2021 Series B and joined the SoftBank-led $150M Series C that valued "
                  "Nowports at $1.1B (May 2022). No later priced round or collapse evidence found, so the mark stands, "
                  "stale. Aligned with the Y Combinator row."))

# nse (National Stock Exchange of India)
VCC_NSE = "https://www.vccircle.com/national-stock-exchange-files-ipo?logintype=premium%2F"
L.append(cls("nse", status="public", rng="10b_plus", usd=46_373_587_587, val_src="web_verified",
             val_cite=NEWS("nse", "NSE debut puts BSE under pressure"), asof="2026-09-24", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=VCC_NSE, stage_conf="medium",
             rounds=[rnd(None, "secondary purchase (about 3% via Tiger Global Five Holdings)", None, None, True, VCC_NSE)],
             country="IN", city="Mumbai", focus="Fintech & Payments",
             note="National Stock Exchange of India, unlisted until its IPO (an offer for sale by existing holders) listed "
                  "on the BSE on 2026-09-24. VCCircle (December 2016, the first IPO filing): 'Tiger Global Five Holdings "
                  "will sell its entire 3% stake', so Tiger bought unlisted shares from earlier holders before then (a "
                  "secondary in a private company, Growth by policy); the purchase date is not on the cited page, so no "
                  "entry date is written. Market cap INR 4.45 lakh crore at debut (Fortune India) = INR 4450.00B @ ECB "
                  "2026-09-24 (INR/EUR 109.0775, EUR/USD 1.1367) = $46.37B."))

# ntopology
PRN_NT = "https://www.prnewswire.com/news-releases/ntopology-secures-65m-in-series-d-funding-led-by-tiger-global-301427395.html"
L.append(cls("ntopology", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=PRN_NT, stage_conf="high", entry_date="2021-11-18",
             rounds=[rnd("2021-11-18", "Series D", 65_000_000, "Tiger Global", True, PRN_NT)],
             country="US", city="New York", focus="SaaS",
             note="New York engineering design software for advanced manufacturing; Tiger led the $65M Series D "
                  "(PR Newswire, 2021-11-18), its first round on record. No priced round at $1B or more found."))

# nuro
TC_NURO = "https://techcrunch.com/2021/11/02/nuro-lands-investment-from-google-tiger-global-in-new-600-million-round/"
L.append(cls("nuro", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=TC_NURO, stage_conf="high", entry_date="2021-11-02",
             rounds=[rnd("2021-11-02", "Series D", 600_000_000, "Tiger Global", True, TC_NURO),
                     rnd("2025-04-09", "Series E", 106_000_000, None, None,
                         "https://pulse2.com/nuro-106-million-series-e-raised-at-6-billion-valuation-for-autonomous-driving-platform/")],
             city="Mountain View", focus="Industrial & Robotics",
             note="Autonomous delivery and driving; Tiger led the $600M Series D of November 2021 (TechCrunch; Pandaily: "
                  "'led by Tiger Global Management'), its first round. Series E at $6B in 2025."))

# nuvemshop
REU_NUV = "https://www.reuters.com/article/business/media-telecom/e-commerce-platform-nuvemshop-becomes-brazils-latest-unicorn-idUSL1N2PO153/"
PY_NUV = NEWS("nuvemshop", "Raises $500M In Series E Funding")
L.append(cls("nuvemshop", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=PY_NUV, stage_conf="high", entry_date="2021-08-16",
             rounds=[rnd("2021-08-16", "Series E", 500_000_000, "Insight Partners; Tiger Global", True, PY_NUV)],
             country="BR", country_src="web_verified", country_cite=REU_NUV, city="São Paulo", focus="SaaS",
             note="E-commerce platform (Tiendanube), founded in Buenos Aires and run from São Paulo; Reuters calls it a "
                  "Brazilian platform. The AR country claim is replaced by BR on that evidence (the Accel row pairs São "
                  "Paulo with AR). Tiger co-led the $500M Series E at $3.1B in August 2021 (pymnts), its first round."))

# nvidia: a 13F position in a listed company
L.append(verdict("nvidia", "not_member",
                 "13G/13F position in a listed company, no private round naming the firm (T3, D3): the recall headline is "
                 "a Motley Fool piece on Tiger's quarterly 13F moves, the 13F layer lists NVIDIA from 2023 to 2026, and "
                 "Nvidia listed in 1999, before the firm existed",
                 ec="web", conf="high",
                 cite="https://www.fool.com/investing/2025/05/20/billionaire-chase-coleman-add-to-nvidia-ai-stocks/"))

# nylas-inc (Form D director of record, in tenure)
BI_NYL = NEWS("nylas-inc", "Read the pitch deck Nylas used to raise")
L.append(verdict("nylas-inc", "member",
                 "John Curtius (Tiger partner until June 2022) is director on Nylas's Q2 2021 Form D ($115.5M sold), the "
                 "$120M Series C of June 2021; the issuer resolves to the San Francisco API company and nothing contrary "
                 "is on record (director-of-record pattern)",
                 ec="formd_adjudicated", conf="medium", cite=SEC("nylas-inc")))
L.append(cls("nylas-inc", status="private", rng="below_1b", city="San Francisco", focus="DevTools & APIs",
             rounds=[rnd("2021-06-16", "Series C", 120_000_000, None, True, BI_NYL)],
             note="San Francisco communications API platform; the Series C of June 2021 ($120M, Business Insider) matches "
                  "the Form D Tiger's partner sits on, which is Tiger's entry (Growth, Form D band). No priced round at $1B "
                  "or more found; aligned with the 8VC and Spark rows."))

# octoai and octoml: one company (OctoML renamed OctoAI in January 2024)
BI_OCTO = "https://www.businessinsider.com/nvidia-acquires-octoai-2024-9"
GW_OCTO = "https://www.geekwire.com/2024/chip-giant-nvidia-acquires-octoai-a-seattle-startup-that-helps-companies-run-ai-models/"
L.append(verdict("octoai", "member",
                 "Business Insider (2024-09-26): the Seattle startup's most recent round was 'an $85 million Series C round "
                 "led by Tiger Global Management'; Yahoo Finance (2024-09-18) also names Tiger among OctoAI's investors",
                 ec="web", conf="high", cite=BI_OCTO))
OCTO_ROUNDS = [rnd("2021-11-01", "Series C", 85_000_000, "Tiger Global", True, BI_OCTO)]
L.append(cls("octoai", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=BI_OCTO, stage_conf="high", entry_date="2021-11-01",
             rounds=OCTO_ROUNDS, country="US", city="Seattle", focus="AI & Applied AI",
             note="OctoML renamed itself OctoAI in January 2024 (GeekWire); row octoml is the same company. Tiger led the "
                  "$85M Series C of November 2021, its first round (the March 2021 Series B was Addition's). Nvidia "
                  "acquired OctoAI in September 2024 (GeekWire)."))
L.append(cls("octoml", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=BI_OCTO, stage_conf="high", entry_date="2021-11-01",
             rounds=OCTO_ROUNDS, country="US", city="Seattle", focus="AI & Applied AI", flags=["duplicate"],
             note="Duplicate of octoai: OctoML renamed itself OctoAI in January 2024, so the two rows are one company; "
                  "flagged here so the company counts once (octoai carries the last name). Same facts: Tiger led the $85M "
                  "Series C of November 2021 (Business Insider), Nvidia acquired the company in September 2024."))

# ofbusiness
BT_OFB = ("https://www.businesstoday.in/latest/corporate/story/b2b-commerce-platform-ofbusiness-valuation-doubles-to-3-bn-"
          "after-tiger-global-led-round-308116-2021-09-30")
L.append(cls("ofbusiness", status="private",
             stage="Growth", stage_src="web_verified", stage_cite=BT_OFB, stage_conf="high", entry_date="2021-09-29",
             rounds=[rnd("2021-09-29", "unnamed ($200M, Tiger-led)", 200_000_000, "Tiger Global", True, BT_OFB),
                     rnd("2021-12-20", "unnamed ($325M)", 325_000_000, None, None,
                         "https://finance.yahoo.com/news/indias-ofbusiness-valued-5-billion-074925391.html")],
             country="IN", country_src="web_verified", country_cite=BT_OFB, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="Gurugram B2B raw-materials commerce and SME credit platform. Moneycontrol reported in August 2021 that "
                  "Tiger 'may back' OfBusiness, and Tiger then led the $200M round at $3B (Business Today, September "
                  "2021), after SoftBank's earlier round: Tiger's entry, Growth. The December 2021 $325M round valued it "
                  "at $5B."))

# offerup
L.append(cls("offerup", status="private", rng="below_1b", stage="undetermined", city="Bellevue",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2015-11-04", "$90M disclosed across its rounds", 90_000_000, None, None,
                         NEWS("offerup", "Fast-growing OfferUp breaks silence"))],
             note="Bellevue local-marketplace app; Wikipedia lists Tiger Global Management among its investors. The earliest "
                  "press pairing the two is the November 2015 disclosure of $90M raised (GeekWire), whose page refuses "
                  "scripted reads, and no headline names the round Tiger joined, so the stage is undetermined. The $850M "
                  "figure on the a16z and Coatue rows is a vendor estimate (UpMarket), which Rule A keeps out of the band; "
                  "below_1b aligns with them."))

# oico (membership open)
GLO_OICO = "https://blogs.oglobo.globo.com/capital/post/marketplace-de-material-de-construcao-oico-atrai-csn-e-fundos-valor-e-tiger-global.html"
BAG_OICO = "https://www.baguete.com.br/noticias/oico-recebe-rodada-seed-de-r-30-milhoes"
L.append(verdict("oico", "member",
                 "O Globo (2022-01-27): the construction-materials marketplace Oico 'atrai CSN e fundos Valor e Tiger "
                 "Global' in its R$30M round; Baguete: the seed round was led by Valor Capital Group and 'Também estão no "
                 "barco a Tiger Global'",
                 ec="web", conf="high", cite=GLO_OICO))
L.append(cls("oico", status="unknown", rng="below_1b",
             stage="Seed", stage_src="web_verified", stage_cite=BAG_OICO, stage_conf="high", entry_date="2022-01-26",
             rounds=[rnd("2022-01-26", "Seed", None, "Valor Capital Group", True, BAG_OICO)],
             country="BR", country_src="web_verified", country_cite=GLO_OICO, city="São Paulo",
             focus="Consumer & Marketplaces",
             note="São Paulo B2B construction-materials marketplace (YC). Tiger joined the R$30M seed Valor led (January "
                  "2022). In May 2023 Oico paused operations, laid off staff and was looking for a new business model "
                  "(Terra); nothing later found, so the state reads unknown, aligned with the Y Combinator row. "
                  "Graduation left for the graduation pass."))

if __name__ == "__main__":
    jl.write("batch-009c", L)
