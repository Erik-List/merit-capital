"""Judge j01, part b (PRO-80 Bessemer Venture Partners, batch 1): rows amperos .. avantos.

Evidence read on 2026-10-01 as in part a. Run as NQ_TAG=j01 python3 judgments-j01b.py.
"""
import judge_lib as jl
from judge_lib import ARCH, POST, SITE, W, cls, rnd

WV = "web_verified"
FP = "first_party"
BVP = "Bessemer Venture Partners"

CITYBIZ_AMPEROS = "https://www.citybiz.co/article/835644/amperos-health-raises-16-million-series-a-to-expand-ai-denial-management-platform/"
VCPOST_ANAQUA = "https://www.vcpost.com/articles/16630/20131017/bessemer-venture-partners-invests-usd-25-million-anaqua.htm"
ET_ANUNTA = "https://m.economictimes.com/industry/banking/finance/bessemer-funds-ex-firstsource-ceo-ananda-mukerjis-startup-anunta-tech/articleshow/18601661.cms"
RR_ANYBOTICS = "https://www.therobotreport.com/anybotics-raises-50m-to-expand-international-deployments-develop-new-capabilities/"
TC_ANYBOTICS = "https://techcrunch.com/2023/05/16/anybotics-raises-50-million-to-help-deploy-its-robot-dog/"
EUS_ANYBOTICS = "https://www.eu-startups.com/2023/05/zurich-based-anybotics-secures-e46m-series-b-round-to-conquer-the-industrial-world-with-its-four-legged-workforce/"
TFN_ANYTHING = "https://techfundingnews.com/anythings-viral-debut-pushes-create-to-8-5m-raise-led-by-bessemer/"
TC_ANYTHING = "https://techcrunch.com/2025/09/29/vibe-coding-startup-anything-nabs-a-100m-valuation-after-hitting-2m-arr-in-its-first-two-weeks/"
CT_APPWRITE_SEED = "https://www.calcalistech.com/ctech/articles/0,7340,L-3918413,00.html"
CT_APPWRITE_A = "https://www.calcalistech.com/ctechnews/article/bj60000nyq5"
UKTN_APRON = "https://www.uktech.news/fintech/apron-series-a-ex-revolut-20230928"
TC_APRON = "https://techcrunch.com/2023/09/28/apron-grabs-15-million-to-simplify-invoice-processing/"
CITYBIZ_ARCHY = "https://www.citybiz.co/article/617246/archy-raises-15m-series-a/"
BW_ARCION = "https://www.businesswire.com/news/home/20220217005345/en/Arcion-Formerly-Blitzz-Secures-%2413M-Series-A-To-Transform-Data-Infrastructure"
CNBC_ARCION = "https://www.cnbc.com/2023/10/23/databricks-the-43-billion-ai-firm-acquires-arcion-for-100-million.html"
HIT_ARTEMIS = "https://hitconsultant.net/2019/03/15/artemis-health-raises-25m-to-expand-benefits-data-analytics-platform/"
BO_ASPEN = "https://www.businessobserverfl.com/news/2021/jan/15/health-care-tech-firm-raises-dollar23-million/"
CT_ASTRIX_SEED = "https://www.calcalistech.com/ctechnews/article/hkdsnqqgq"
CT_ASTRIX_A = "https://www.calcalistech.com/ctechnews/article/b1dfntyun"
GLOBES_ASTRIX = "https://en.globes.co.il/en/article-cisco-to-acquire-israeli-co-astrix-security-1001541978"
AGF_ATOMO = "https://agfundernews.com/why-we-invested-in-atomo"
GNW_ATOMO = "https://www.globenewswire.com/news-release/2022/06/28/2470283/0/en/food-technology-company-atomo-closes-40-million-series-a-to-scale-beanless-coffee-product-line.html"
TC_AUTH0_F = "https://techcrunch.com/2020/07/14/identity-platform-auth0-raises-120m-series-f-round-at-1-92b-valuation/"
AVANT_ABOUT = "https://avantarte.com/about"
CITYBIZ_AVANTOS = "https://www.citybiz.co/article/807827/avantos-raises-25m-series-a-led-by-bessemer/"
P_AMPEROS = POST("amperos-tackling")
P_ANAQUA = POST("anaqua-acquisition-astorg")
P_ANTHROPIC_E = POST("3-5-billion-more-for-anthropic")
P_ANTHROPIC = POST("why-we-invested-in-anthropic")
P_AUTH0 = POST("memos/auth0")
P_AVANTOS = POST("doubling-down-on-avantos")

L = []

# ---- amperos
L.append(cls("amperos", status="private", rng="below_1b", stage="Series A", stage_src=FP, stage_cite=P_AMPEROS,
             stage_conf="high", entry_date="2025", country="US", city="New York", focus="Healthcare & Bio",
             rounds=[rnd("2025", "Seed", None, None, False, CITYBIZ_AMPEROS, "press"),
                     rnd("2026-04-22", "Series A", 16000000, BVP, True, P_AMPEROS, "firm")],
             note="Amperos Health, AI agents for medical claim denials, New York (citybiz). The firm's own post (2026-04-22): 'Bessemer Venture Partners leads Amperos Health's $16M Series A'; the seed of 2025 (Uncork, Neo) names no Bessemer, and the post does not speak of an earlier Bessemer round. The entry date is the firm's partnered year, 2025, the close ahead of the April 2026 announcement. A $16M Series A carries no $1B mark."))

# ---- anaqua
L.append(cls("anaqua", status="acquired", rng="below_1b", city="Boston", stage="Growth", stage_src=FP,
             stage_cite=P_ANAQUA, stage_conf="high", entry_date="2013-09-23", focus="SaaS",
             flags=["stage_disputes_band"],
             rounds=[rnd("2013-07", "growth equity investment with a buyout of the earlier investors", None, "Insight Venture Partners", False, None, "press"),
                     rnd("2013-10-17", "growth investment", 25000000, BVP, True, VCPOST_ANAQUA, "press")],
             note="Anaqua, intellectual property management software, Boston; acq. by Astorg, 2019 (the firm's own post). The firm's own post (2019-04-24): 'Bessemer Venture Partners invested in Anaqua at the growth stage back in 2013'; VCPost (2013-10-17) reports its $25M investment, made three months after Insight Venture Partners took its controlling position, so Bessemer's is a minority growth investment and not the control transaction. The Form D band read Pre-Seed off a $250K filing of 2015, which is not the entry; re-staged to Growth on the firm's own date."))

# ---- ansible-health
L.append(cls("ansible-health", status="private", rng="below_1b", stage="undetermined", entry_date="2021", country="US",
             city="Mountain View", focus="Healthcare & Bio", rounds=[],
             note="Ansible Health, virtual care for chronic lung disease, Mountain View (as the First Round book reads). The firm's list dates the partnership to 2021, the founding year, and its posts only name the company among its health AI investments; no funding report names a round (Google News, 2026-10-01), so undetermined. No sale or shutdown found."))

# ---- anthropic
L.append(cls("anthropic", city="San Francisco", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2024", focus="AI & Applied AI",
             rounds=[rnd("2023-05", "Series C", 450000000, "Spark Capital", False, None, "press"),
                     rnd("2024", "the firm's first investment (round not named by the firm)", None, None, True, P_ANTHROPIC, "firm"),
                     rnd("2025-03-03", "Series E", 3500000000, "Lightspeed", True, P_ANTHROPIC_E, "firm")],
             note="Anthropic, San Francisco. The firm's own post of 2024-10-22 speaks of an investment it had already made, without naming the round, its list dates the partnership to 2024, and its post of 2025-03-03 says it is 'doubling down' in the Series E. Every Anthropic financing of 2024 came after the Series C of May 2023 (Series D tranches and secondary sales), so the entry is Growth by the company's own round history; the exact 2024 round is not established, hence medium."))

# ---- anunta
L.append(cls("anunta", status="private", rng="below_1b", stage="undetermined", entry_date="2013-01-24", country="IN",
             country_src=WV, country_cite=ARCH("anunta"), city="Mumbai", focus="Data Infrastructure",
             rounds=[rnd("2013-02-21", "unnamed round", None, BVP, True, ET_ANUNTA, "press")],
             note="Anunta (Anunta Technology Management Services), managed virtual desktops, on the firm's India list (Mumbai from model knowledge). The Economic Times (2013-02-21) reports that Bessemer funded the startup of the former Firstsource chief executive Ananda Mukerji; the headline names no round and the page could not be opened, so the stage is undetermined on the firm's own date. Still operating; no sale or listing found."))

# ---- anybotics
L.append(cls("anybotics", status="private", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=RR_ANYBOTICS,
             stage_conf="high", entry_date="2023-05", country="CH", country_src=WV, country_cite=EUS_ANYBOTICS,
             city="Zurich", focus="Industrial & Robotics",
             rounds=[rnd("2023-05-16", "Series B", 50000000, "Walden Catalyst; NGP Capital", True, RR_ANYBOTICS, "press"),
                     rnd("2024-12-12", "unnamed round", 60000000, None, None, None, "press")],
             note="ANYbotics, legged inspection robots, Zurich (EU-Startups: 'Zurich-based ANYbotics'; the firm's desk tag reads US). The Robot Report (2023-05-16) on the $50M Series B quotes Alex Ferrara of Bessemer Venture Partners as an investor in the round, which Walden Catalyst and NGP Capital led (TechCrunch); the firm's partnered year is 2023, so the entry is the Series B, Growth. Later raises (December 2024, September 2025) published no valuation."))

# ---- anything
L.append(cls("anything", status="private", rng="below_1b", stage="undetermined", entry_date="2024", country="US",
             city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2023", "pre-seed and seed (Uncork and Bessemer, not split by round)", None, None, True, TC_ANYTHING, "press"),
                     rnd("2025-08-14", "unnamed round", 5500000, BVP, True, TFN_ANYTHING, "press"),
                     rnd("2025-09-29", "unnamed round at a $100M valuation", 11000000, "Footwork", True, TC_ANYTHING, "press")],
             note="Anything (fka Create), a text-to-app builder, San Francisco (Tech Funding News). TechCrunch (2025-09-29): the founders 'raised some pre-seed and seed funding from Uncork and Bessemer Venture Partners', and Tech Funding News reports a $5.5M round led by Bessemer inside $8.5M of total funding; neither says whether Bessemer came in at the pre-seed or the seed, which are two stages, so undetermined on the firm's partnered year. Momentum check 2026-10-01: the newest round is $11M at a $100M valuation (September 2025)."))

# ---- apperian
L.append(cls("apperian", status="acquired", rng="below_1b", city="Boston", focus="SaaS",
             note="Apperian, enterprise mobile application management, Boston (as the Kleiner Perkins book reads); acq. by Arxan Technologies, 2017. The Form D entry of March 2011 is the $9.5M round Wikipedia names with North Bridge and Bessemer."))

# ---- appwrite
L.append(cls("appwrite", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=CT_APPWRITE_SEED,
             stage_conf="high", entry_date="2021-09", grad="graduated", grad_src=WV, grad_cite=CT_APPWRITE_A,
             grad_conf="high", country="IL", country_src=WV, country_cite=CT_APPWRITE_A, city="Tel Aviv",
             focus="DevTools & APIs",
             rounds=[rnd("2021-09-28", "Seed (second of two seed rounds)", 10000000, "Bessemer Venture Partners; Flybridge", True, CT_APPWRITE_SEED, "press"),
                     rnd("2022-04-05", "Series A", 27000000, "Tiger Global", True, CT_APPWRITE_A, "press")],
             note="Appwrite, open-source backend as a service, Tel Aviv (as the Seedcamp and Tiger Global books read). CTech (2021-09-28): $10 million in two successive seed rounds, the second led by Bessemer Venture Partners and Flybridge. Graduated on the $27M Series A of April 2022, 'led by Tiger Global Management and followed by Seed round participants Bessemer Venture Partners ...' (CTech). Momentum check 2026-10-01: no later priced round found."))

# ---- apron
L.append(cls("apron", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=UKTN_APRON,
             stage_conf="high", entry_date="2021", grad="graduated", grad_src=WV, grad_cite=TC_APRON, grad_conf="high",
             country="GB", country_src=WV, country_cite=TC_APRON, city="London", focus="Fintech & Payments",
             rounds=[rnd("2023-06", "Seed", 5500000, BVP, True, UKTN_APRON, "press"),
                     rnd("2023-09-28", "Series A", 15000000, "Index Ventures", True, TC_APRON, "press"),
                     rnd("2024-09-25", "Series B", 30000000, "Zinal Growth", None, None, "press")],
             note="Apron, supplier payments for small businesses, London (TechCrunch: 'London-based startup Apron'). UKTN (2023-09-28): 'Apron raised $5.5m in a Bessemer Venture Partners-led seed round', announced in mid 2023; the firm's own list dates the partnership to 2021 and the Visionaries Club book reads the register at December 2022, so the entry date is the firm's year. Graduated on the $15M Series A led by Index Ventures (TechCrunch, 2023-09-28). Momentum check 2026-10-01: the newest round is the $30M Series B of September 2024, no $1B mark."))

# ---- archy
L.append(cls("archy", status="private", rng="below_1b", stage="undetermined", entry_date="2022", country="US",
             city="San Jose", focus="Healthcare & Bio",
             rounds=[rnd("2024-10-23", "Series A", 15000000, "Entree Capital", True, CITYBIZ_ARCHY, "press"),
                     rnd("2025-10-30", "Series B", 20000000, "TCV", None, None, "press"),
                     rnd("2026-09-11", "Series C", 50000000, None, None, None, "press")],
             note="Archy, practice software for dental offices, San Jose (citybiz, as the TCV book reads). The firm partnered in 2022, two years before the $15M Series A of October 2024 in which it took part (citybiz), so its entry was an earlier round that no source read names (Google News, 2026-10-01): undetermined. Later rounds: Series B $20M (October 2025), Series C $50M (September 2026), no valuation published."))

# ---- arcion-labs
L.append(cls("arcion-labs", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2021", country="US", city="San Mateo", focus="Data Infrastructure",
             rounds=[rnd("2022-02-17", "Series A", 13000000, BVP, True, BW_ARCION, "press")],
             note="Arcion Labs (fka Blitzz), real-time data replication, San Mateo; acq. by Databricks, 2023 (about $100M, CNBC). The $13M Series A announced on 2022-02-17 (Business Wire headline) was led by Bessemer, which is named from knowledge because the release could not be opened; the firm's partnered year is 2021, the close ahead of the announcement."))

# ---- artemis-health
L.append(cls("artemis-health", status="acquired", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=HIT_ARTEMIS,
             stage_conf="high", entry_date="2019-03", city="Salt Lake City", focus="Healthcare & Bio",
             rounds=[rnd("2017-08-04", "Series B", 22700000, None, False, jl.FORMD_CITE("artemis-health", 1), "filing"),
                     rnd("2019-03-15", "Series C", 25000000, BVP, True, HIT_ARTEMIS, "press")],
             note="Artemis Health, benefits data analytics, Salt Lake City; acq. by Nomi Health, 2022 (the firm's own listing; Axios). HIT Consultant (2019-03-15): '$25 million in Series C funding led by Bessemer Venture Partners', which matches the firm's partnered year 2019. The 2017 Form D seat is Ambar Bhattacharyya's, who had left Bessemer by then (decisions.md D6), so the 2017 date is not the firm's entry."))

# ---- aspen-rxhealth
L.append(cls("aspen-rxhealth", status="private", rng="below_1b", stage="undetermined", entry_date="2020", country="US",
             city="Tampa", focus="Healthcare & Bio",
             rounds=[rnd("2018-12-13", "unnamed round", 9000000, None, False, None, "press"),
                     rnd("2021-01-15", "unnamed round", 23000000, BVP, True, BO_ASPEN, "press")],
             note="Aspen RxHealth, a marketplace matching pharmacists with patients, Tampa (Business Observer). The Business Observer (2021-01-15) reports a $23 million raise led by Bessemer Venture Partners, the firm's entry by its own year (2020), after a $9M raise in 2018; neither report names the series, so undetermined. A later pass could settle it from the company's release. No sale or shutdown found."))

# ---- astrix
L.append(cls("astrix", status="acquired", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=CT_ASTRIX_SEED,
             stage_conf="high", entry_date="2021", grad="graduated", grad_src=WV, grad_cite=CT_ASTRIX_A, grad_conf="high",
             country="IL", country_src=WV, country_cite=CT_ASTRIX_SEED, city="Tel Aviv", focus="Security",
             rounds=[rnd("2022-02-23", "Seed", 15000000, "Bessemer Venture Partners; F2 Capital", True, CT_ASTRIX_SEED, "press"),
                     rnd("2023-06-28", "Series A", 25000000, "CRV", True, CT_ASTRIX_A, "press"),
                     rnd("2024-12-10", "Series B", 45000000, "Menlo Ventures", None, None, "press")],
             note="Astrix Security, non-human identity security, Tel Aviv ('the Israeli startup', CTech). CTech (2022-02-23): the $15M seed was 'led by Bessemer Venture Partners and F2 Capital'; the firm's partnered year is 2021, the close ahead of the announcement. Graduated on the $25M Series A led by CRV (CTech, 2023-06-28). Acq. by Cisco, 2026: the firm's own listing says 'Astrix was acquired by Cisco in May 2026' (Globes, 2026-05-04, about $400M), so acquired and no figure; the Menlo row still reads private."))

# ---- atomo-coffee
L.append(cls("atomo-coffee", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=AGF_ATOMO,
             stage_conf="high", entry_date="2020-08", grad="graduated", grad_src=WV, grad_cite=GNW_ATOMO, grad_conf="high",
             country="US", city="Seattle", focus="Consumer & Marketplaces",
             rounds=[rnd("2020-08-11", "Seed", 9000000, None, True, AGF_ATOMO, "press"),
                     rnd("2022-06-28", "Series A", 40000000, "S2G Ventures; AgFunder; Horizons Ventures", None, GNW_ATOMO, "press")],
             note="Atomo Coffee, beanless coffee, Seattle. AgFunderNews (2020-09-17): 'Atomo! announced its $9 million Seed round with Horizons Ventures, S2G Ventures, AgFunder, and Bessemer investing'. Graduated on the $40M Series A of June 2022 (the company's release). Still operating; no valuation published."))

# ---- august
L.append(cls("august", status="acquired", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2014-08-26", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2015-03-18", "Series B", 38000000, BVP, True, jl.FORMD_CITE("august", 0), "filing")],
             note="August (August Home), smart locks, San Francisco; acq. by ASSA ABLOY, 2017. Bessemer led the $38M Series B (named from knowledge; the Form D of 2015-03-18 is that round, and the firm's own date is 2014-08-26), a round after the 2013 Series A, so Growth; the 2017 Form D seat is a follow-on. The a16z and New Enterprise Associates rows named August are other companies."))

# ---- auterion
L.append(cls("auterion", status="private", rng="below_1b", city="Arlington", focus="Industrial & Robotics",
             note="Auterion, software for autonomous drones, Arlington, Virginia. The firm led the $130M Series B of September 2025, which valued the company at 'north of $600 million' (Wikipedia), so below $1B; no later priced round found on 2026-10-01."))

# ---- auth0
L.append(cls("auth0", city="Bellevue", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=P_AUTH0, stage_conf="high",
             entry_date="2014-07-03", grad="graduated", grad_src=WV, grad_cite=TC_AUTH0_F, grad_conf="high",
             focus="Security", flags=["stage_disputes_band"],
             rounds=[rnd("2014-07", "Seed (convertible, $8M cap)", 1000000, None, True, P_AUTH0, "firm"),
                     rnd("2015", "Series A (the 2015 Form D)", 9300000, None, True, jl.FORMD_CITE("auth0", 2), "filing"),
                     rnd("2020-07-14", "Series F", 120000000, "Salesforce Ventures", None, TC_AUTH0_F, "press")],
             note="Auth0, identity platform for developers, Bellevue; acq. by Okta, 2021 ($6.5B), so no figure. The firm's own investment memo of 2014-06-28 ('Auth0 Seed IR'): 'We believe this $1M seed investment represents an attractive opportunity to get in early and maintain ball control for the eventual Series A', and its investment date is 2014-07-03. The Form D band read Series A off the 2015 seat, which is the follow-on, so the entry is re-staged to Seed. Graduated: the company went on to a Series A in 2015 and a named Series F at $1.92B (TechCrunch, 2020-07-14)."))

# ---- avalanche-technology
L.append(cls("avalanche-technology", status="private", rng="below_1b", stage="undetermined", entry_date="2009-09-03",
             city="Fremont", focus="Industrial & Robotics", rounds=[],
             note="Avalanche Technology, spin-transfer magnetic memory chips, Fremont (as the Sequoia book reads). The firm's own date is 2009-09-03, three years after the company was founded and among several 2009 and 2010 Form D filings; no source read names the round the firm joined, so undetermined. Still private and filing rounds through 2020. The a16z and Y Combinator rows named Avalanche are other companies."))

# ---- avant-arte
L.append(cls("avant-arte", status="private", rng="below_1b", stage="undetermined", entry_date="2022", country="GB",
             country_src=WV, country_cite=AVANT_ABOUT, city="London", focus="Consumer & Marketplaces", rounds=[],
             note="Avant Arte, art editions marketplace. The firm lists it from 2022 and names it among its creator-economy investments (its post of 2023-03-13) without a round, and no funding report was found (Google News, 2026-10-01), so undetermined. The company was founded in the Netherlands and runs its print house and main operations in London (its own about page), which is read as the head office at medium confidence; the firm's desk tag reads US."))

# ---- avantos
L.append(cls("avantos", status="private", rng="below_1b", stage="Seed", stage_src=FP, stage_cite=P_AVANTOS,
             stage_conf="high", entry_date="2024-09", grad="graduated", grad_src=FP, grad_cite=P_AVANTOS, grad_conf="high",
             country="US", city="New York", focus="Fintech & Payments",
             rounds=[rnd("2024-09", "Seed", 10000000, "E14 Fund", True, CITYBIZ_AVANTOS, "press"),
                     rnd("2026-02-18", "Series A", 25000000, BVP, True, P_AVANTOS, "firm")],
             note="Avantos, client onboarding and servicing software for financial services, New York (model knowledge). The firm's own post (2026-02-18): 'When we first invested in their seed round ...' and 'Bessemer Venture Partners leads Avantos' $25M Series A'; citybiz dates the $10M seed's close to September 2024. Graduated on that Series A. Momentum check 2026-10-01: no valuation published, no later round."))

jl.write("j01b", L)
