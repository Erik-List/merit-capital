"""Judge j01, part c (PRO-80 Bessemer Venture Partners, batch 2): rows avnera .. boards.

Evidence read on 2026-10-01 as in part a. Run as NQ_TAG=j01 python3 judgments-j01c.py.
"""
import judge_lib as jl
from judge_lib import ARCH, POST, SITE, W, cls, rnd

WV = "web_verified"
FP = "first_party"
BVP = "Bessemer Venture Partners"

OL_AVNERA = "https://www.oregonlive.com/silicon-forest/2018/08/skyworks_buys_beaverton-based.html"
FORTUNE_AXIAMATIC = "https://fortune.com/2026/03/11/exclusive-ai-startup-axiamatic-raises-54-million-to-help-companies-push-their-digital-transformations-forward/"
PULSE_AXIAMATIC = "https://pulse2.com/axiamatic-54-million-funding/"
PRN_AXION = "https://www.prnewswire.com/news-releases/axion-ray-announces-17-5-million-in-series-a-funding-led-by-bessemer-venture-partners-302086459.html"
CM_BASIS = "https://clayandmilk.com/2022/04/26/basis-theory-raises-17-million-funding-round/"
FINOVATE_BASIS = "https://finovate.com/data-privacy-management-software-provider-basis-theory-secures-33-million/"
FINSMES_BASTILLE = "https://www.finsmes.com/2024/01/bastille-raises-44m-in-series-c-funding.html"
BBG_BETTERMENT = "https://www.bloomberg.com/news/articles/2021-09-29/betterment-valuation-rises-to-1-3-billion-on-new-funding-round"
CNBC_BETTERMENT_B = "https://www.cnbc.com/2012/10/03/betterment-raises-10-million-series-b-financing-from-menlo-ventures-bessemer-venture-partners-anthemis-group.html"
BK_TRIBE = "https://betakit.com/tribe-technologies-announces-november-seed-funding-as-company-looks-to-scale-online-community-platform/"
CBN_BEYOND = "https://news.crunchbase.com/venture/proptech-startup-beyond-pricing-raises-42-5m-series-a-from-bessemer-venture-partners/"
TEAM_FEINSTEIN = "https://www.bvp.com/team/brian-feinstein"
IBT_CONSIM = "https://www.ibtimes.com/after-yahoo-consim-dates-bvp-sustain-leadership-online-matrimony-864430"
AGF_BIGBASKET = "https://agfundernews.com/indian-e-grocer-bigbasket-com-becomes-unicorn-in-50m-series-c-funding"
TNM_BIGBASKET = "https://www.thenewsminute.com/money/tata-group-acquires-majority-stake-online-grocer-bigbasket-149726"
TC_BILLGUARD_B = "https://techcrunch.com/2011/10/18/khosla-schmidt-founders-fund-10-million-billguard/"
WIRED_BILLGUARD = "https://www.wired.com/story/billguard-acquired-prosper-marketplace/"
MARTECH_BIZO = "https://martech.org/linkedin-acquire-bizo-deal-valued-175-million/"
AGF_BLACKSHEEP = "https://agfundernews.com/black-sheep-foods-bags-5-3m-funding-from-agfunder-others-plant-based-lamb"
TC_BLACKSHEEP = "https://techcrunch.com/2022/12/08/black-sheep-foods-12-3m-plant-based-meat/"
SEC_BLADELOGIC_REDEMPTION = "https://www.sec.gov/Archives/edgar/data/1175685/000104746907005074/a2178464zex-10_27.htm"
SEC_BLADELOGIC_S1 = "https://www.sec.gov/Archives/edgar/data/1175685/000104746907002616/a2177017zs-1.htm"
SEC_BLUENILE_S1 = "https://www.sec.gov/Archives/edgar/data/1091171/000089102004000321/v97093orsv1.htm"
BI_BLUEAPRON = jl.NEWS("blue-apron", "is now valued at $2 billion")

L = []

# ---- avnera
L.append(cls("avnera", status="acquired", rng="below_1b", stage="undetermined", entry_date="2004-04-01",
             city="Beaverton", city_src=WV, focus="Industrial & Robotics", rounds=[],
             note="Avnera, analog system-on-chip audio semiconductors, Beaverton, Oregon; acq. by Skyworks, 2018 ($405M; The Oregonian, 2018-08-06: 'Beaverton-based Avnera'). The firm's own investment date is 2004-04-01, the company's founding year; no source read names that round (Google News found no funding report), so undetermined. The 2009 Form D seat the layer dated the entry from is a follow-on five years later."))

# ---- axiamatic
L.append(cls("axiamatic", status="private", rng="below_1b", stage="undetermined", entry_date="2025", country="US",
             city="San Francisco", focus="AI & Applied AI",
             rounds=[rnd("2026-03-11", "total funding announced at launch, rounds not broken out", 54000000,
                         "Greylock; Bessemer Venture Partners", True, FORTUNE_AXIAMATIC, "press")],
             note="Axiamatic, an AI platform for ERP and enterprise transformation programmes, San Francisco (Pulse 2.0, as the Greylock book reads). The company left stealth on 2026-03-11 with $54 million from Greylock and Bessemer (Fortune), a total that the reports do not break into rounds; Greylock's own page records a Series A entry and the firm's list dates Bessemer's partnership to 2025, but no source names the round Bessemer joined, so undetermined. Momentum check 2026-10-01: no valuation published."))

# ---- axion
L.append(cls("axion", status="private", rng="below_1b", stage="Series A", stage_src=WV, stage_cite=PRN_AXION,
             stage_conf="high", entry_date="2024-03", country="US", city="New York", focus="AI & Applied AI",
             flags=["model_disputes_source"],
             rounds=[rnd("2023-02-16", "Seed", 7500000, None, False, None, "press"),
                     rnd("2024-03-12", "Series A", 17500000, BVP, True, PRN_AXION, "press"),
                     rnd("2025-12-15", "Series B", 37000000, None, None, None, "press")],
             note="Axion (fka Axion Ray), AI that detects emerging product quality issues for manufacturers, New York. The company's release (2024-03-12): 'Axion Ray Announces $17.5 Million in Series A Funding Led by Bessemer Venture Partners'; the $7.5M seed of 2023 names no Bessemer. The pre-filled country AR is a Wikidata join to an Argentine namesake and is replaced by US; the Kleiner Perkins row named Axion is another company. Momentum check 2026-10-01: the newest round is the $37M Series B of December 2025, no $1B mark."))

# ---- axis-network-technology
L.append(cls("axis-network-technology", status="acquired", rng="below_1b", stage="undetermined", entry_date="2007-11-09",
             country="GB", country_src=WV, country_cite=ARCH("axis-network-technology"), focus="Data Infrastructure",
             flags=["city_unknown"], rounds=[],
             note="Axis Network Technology, digital radio heads for mobile broadband networks; acq. by Ace Technology, 2010 (the firm's own listing). The firm's archived list places it in Europe; the United Kingdom is from model knowledge (the business continued as AceAxis there) and no source read gives the town. The firm's own date is 2007-11-09; no source names the round, so undetermined."))

# ---- axonius
L.append(cls("axonius", city="New York", focus="Security",
             note="Axonius, cybersecurity asset management, New York (as the Accel, ICONIQ and Lightspeed books read). The firm's own post confirms the entry: 'When we invested in Axonius at the Series A in early 2019'."))

# ---- bankjoy
L.append(cls("bankjoy", status="private", rng="below_1b", stage="undetermined", entry_date="2020", country="US",
             city="Troy", focus="Fintech & Payments",
             rounds=[rnd("2023-03-06", "unnamed round", None, "Curql", None, None, "press")],
             note="Bankjoy, digital banking software for credit unions and community banks, Troy, Michigan (as the Y Combinator book reads). The firm lists it from 2020 and names it once among its fintech investments; no funding report names Bessemer or the round (Google News, 2026-10-01), so undetermined. Momentum check: the only later raise found is the Curql investment of March 2023, no valuation."))

# ---- basis-theory
L.append(cls("basis-theory", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2021", country="US", focus="Fintech & Payments", flags=["city_unknown"],
             rounds=[rnd("2022-04-21", "unnamed round, the one before the Series B", 17000000, BVP, True, CM_BASIS, "press"),
                     rnd("2025-10-14", "Series B", 33000000, "Costanoa Ventures", True, FINOVATE_BASIS, "press")],
             note="Basis Theory, a tokenization API for payment data. Clay & Milk (2022-04-26): '$17 million in funding from Bessemer, Kindred, Conversion Capital, BoxGroup, Offline Ventures', with Bessemer named first and the firm's year reading 2021 (the close); Finovate (2025-10-15) calls the next round a Series B with Bessemer as an existing investor. So the $17M round Bessemer led is the Series A, named from knowledge since neither page uses the words. The company is distributed and no source read states a head office. Momentum check 2026-10-01: the $33M Series B, no $1B mark."))

# ---- bastille-networks
L.append(cls("bastille-networks", status="private", rng="below_1b", city="Santa Cruz", city_src=WV, focus="Security",
             note="Bastille Networks, radio-frequency threat detection, Santa Cruz, California (FinSMEs, 2024-01-25). The newest round is the $44M Series C led by Goldman Sachs Asset Management with Bessemer as an existing investor; no valuation published, so below $1B."))

# ---- berkeley-design-automation
L.append(cls("berkeley-design-automation", status="acquired", rng="below_1b", stage="undetermined", entry_date="2003-03-07",
             country="US", city="Santa Clara", focus="Industrial & Robotics", rounds=[],
             note="Berkeley Design Automation, analog and RF circuit verification software for chip design, Santa Clara; acq. by Mentor Graphics, 2014 (the firm's own listing). The firm's own date is 2003-03-07; no source read names the round, so undetermined, and the 2009 Form D seat is a later filing, not the entry."))

# ---- betterment
L.append(cls("betterment", status="private", rng="1b_plus", usd=1300000000, val_src=WV, val_cite=BBG_BETTERMENT,
             asof="2021-09", extra={"valuation_range_source": WV}, city="New York", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2010-11-23", focus="Fintech & Payments",
             flags=["stale", "stage_disputes_band"],
             rounds=[rnd("2010-11-23", "Series A", 3000000, BVP, True, jl.FORMD_CITE("betterment", 1), "filing"),
                     rnd("2012-10-03", "Series B", 10000000, "Menlo Ventures", True, CNBC_BETTERMENT_B, "press"),
                     rnd("2021-09-29", "Series F", 60000000, "Treasury", None, BBG_BETTERMENT, "press")],
             note="Betterment, automated investing, New York. Bessemer led the $3M round of November 2010 (the firm's own date and the Form D agree), which the company called its Series A: the next round was announced as 'Betterment Raises $10 Million Series B Financing from Menlo Ventures, Bessemer Venture Partners, & Anthemis Group' (CNBC, 2012-10-03). The Form D band read Seed from the amount, so the label is re-staged to Series A, named from knowledge because the 2010 release could not be opened. Mark: 'Betterment Valuation Rises to $1.3 Billion on Funding Round' (Bloomberg, 2021-09-29, the $60M Series F); no later priced round found on 2026-10-01, so stale. The Menlo row still reads below $1B."))

# ---- bettermode
L.append(cls("bettermode", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=BK_TRIBE,
             stage_conf="high", entry_date="2020-11", country="CA", country_src=WV, country_cite=BK_TRIBE, city="Toronto",
             focus="SaaS",
             rounds=[rnd("2020-11", "Seed", 7500000, "Bessemer Venture Partners; CRV", True, BK_TRIBE, "press")],
             note="Bettermode (fka Tribe), a customer community platform, Toronto. BetaKit (2021-06-29): 'Toronto-based Tribe Technologies has announced a $7.5 million USD seed financing round, closed in November', led by Bessemer Venture Partners and CRV. No later round found in Google News on 2026-10-01. Graduation left for the graduation pass."))

# ---- bevi
L.append(cls("bevi", status="private", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2019-01", country="US", city="Boston", focus="Consumer & Marketplaces",
             rounds=[rnd("2019-01", "Series C", 35000000, BVP, True, None, "press"),
                     rnd("2022-08-09", "Series D", 70000000, None, None, None, "press")],
             note="Bevi, smart water dispensers for workplaces, Boston. Bessemer led the $35M Series C of January 2019 (named from knowledge; the firm's partnered year is 2019 and the pages found could not be opened), so Growth. The newest round is the $70M of August 2022 (Boston Business Journal headline), no valuation published."))

# ---- beyond
L.append(cls("beyond", status="private", rng="below_1b", country="US", city="San Francisco", stage="Growth",
             stage_src=FP, stage_cite=TEAM_FEINSTEIN, stage_conf="medium", entry_date="2019-09", focus="SaaS",
             flags=["model_disputes_source"],
             rounds=[rnd("2015", "seed and post-seed", 3500000, None, False, CBN_BEYOND, "press"),
                     rnd("2019-09-26", "Series A (the press's word); 'growth buyout' (the firm's)", 42500000, BVP, True, CBN_BEYOND, "press")],
             note="Beyond (fka Beyond Pricing), revenue management for short-term rentals, San Francisco. The pre-filled public status, $400M figure and GB country are a name match to another Beyond and are replaced: the company is private, in the US, and carries no priced mark. Entry: the $42.5M of September 2019, which Crunchbase News calls a Series A and the firm's own partner page lists among Brian Feinstein's 'growth buyout investments'; the firm's label is read, so Growth. Whether the deal gave Bessemer control is not established by the sources read and is raised in the report. The Greylock row named Beyond is another company."))

# ---- bharat-matrimony
L.append(cls("bharat-matrimony", status="public", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=IBT_CONSIM,
             stage_conf="high", entry_date="2011-10", country="IN", country_src=WV, country_cite=SITE("bharat-matrimony"),
             city="Chennai", focus="Consumer & Marketplaces",
             rounds=[rnd("2011-10", "secondary purchase of Yahoo's 12% stake", None, BVP, True, IBT_CONSIM, "press")],
             note="Bharat Matrimony (Matrimony.com, fka Consim Info), online matchmaking, Chennai; listed on the NSE since September 2017 (the firm's own listing) and valued well under $1B. International Business Times (2012-11-08): 'Yahoo sold its 12 percent stake to Bessemer Venture Partners' in October 2011, with the existing investors Mayfield and Canaan; a purchase of existing shares in a private company six years before the listing, so a member and Growth."))

# ---- bigbasket
L.append(cls("bigbasket", status="acquired", rng="below_1b", stage="Growth", stage_src=WV, stage_cite=AGF_BIGBASKET,
             stage_conf="high", entry_date="2015-02-24", country="IN", country_src=WV, country_cite=AGF_BIGBASKET,
             city="Bangalore", focus="Consumer & Marketplaces",
             rounds=[rnd("2015-08-12", "Series C", 50000000, BVP, True, AGF_BIGBASKET, "press"),
                     rnd("2016-03-23", "Series D", 150000000, "Abraaj", None, None, "press")],
             note="bigbasket, online grocery, Bangalore; acq. by Tata Digital, 2021 (majority stake; The News Minute, 2021-05-29), so acquired and no figure. AgFunderNews (2015-08-13): the $50M Series C 'was led by Bessemer Venture Partners ... which has been working on it since late last year'; the firm's own investment date is 2015-02-24."))

# ---- bigid
L.append(cls("bigid", city="New York", focus="Security",
             note="BigID, data security and privacy, New York (as the Tiger Global book reads; research in Tel Aviv). The firm's own post confirms the entry: it led the $50M Series C of 2019."))

# ---- billguard
L.append(cls("billguard", status="acquired", rng="below_1b", city="New York", stage="Seed", stage_src=WV,
             stage_cite=W("BillGuard"), stage_conf="medium", entry_date="2010-05-28", grad="graduated", grad_src=WV,
             grad_cite=TC_BILLGUARD_B, grad_conf="high", focus="Fintech & Payments", flags=["model_disputes_source"],
             rounds=[rnd("2010-05", "Seed (Wikipedia); 'series A' in TechCrunch's later recap", 3000000, None, True, W("BillGuard"), "press"),
                     rnd("2011-10-18", "Series B", 10000000, "Khosla Ventures", True, TC_BILLGUARD_B, "press")],
             note="BillGuard, card-statement monitoring, New York with engineering in Tel Aviv; acq. by Prosper Marketplace, 2015 (about $30M; Wired, 2015-09-24), so the pre-filled defunct is replaced by acquired, as the Khosla book reads. Wikipedia: founded in 2010 'with $3 million in seed funding from Bessemer Venture Partners, Founder Collective, SV Angel, IA Ventures ...'; the firm's own date is 2010-05-28. TechCrunch's 2011 recap calls the same $3M a series A, hence medium. Graduated on the $10M Series B led by Khosla Ventures with Bessemer taking part (TechCrunch, 2011-10-18)."))

# ---- bizo
L.append(cls("bizo", status="acquired", rng="below_1b", city="San Francisco", stage="Growth", stage_src="model",
             stage_conf="medium", entry_date="2009-11-17", focus="Media, Gaming & Advertising",
             flags=["stage_disputes_band"],
             rounds=[rnd("2008", "Series A", None, "Crosslink Capital; Venrock", False, None, "press"),
                     rnd("2009-11-17", "Series B", 6000000, BVP, True, jl.FORMD_CITE("bizo", 0), "filing")],
             note="Bizo, business-audience ad targeting, San Francisco; acq. by LinkedIn, 2014 ($175M; MarTech, 2014-07-23). The company was set up in 2008 with a Series A from Crosslink and Venrock, and Bessemer led the $6M Series B of November 2009 (named from knowledge; the Form D of 2009-11-17 and the firm's own date agree on the round). The Form D band read Seed from the amount, so the entry is re-staged to Growth and the row leaves the seed cohort."))

# ---- black-sheep-foods
L.append(cls("black-sheep-foods", status="private", rng="below_1b", stage="Seed", stage_src=WV, stage_cite=AGF_BLACKSHEEP,
             stage_conf="medium", entry_date="2020", grad="graduated", grad_src=WV, grad_cite=TC_BLACKSHEEP, grad_conf="high",
             country="US", city="San Francisco", focus="Consumer & Marketplaces",
             rounds=[rnd("2022-01-27", "Seed", 5250000, None, True, AGF_BLACKSHEEP, "press"),
                     rnd("2022-12-08", "Series A", 12300000, "Unovis", True, TC_BLACKSHEEP, "press")],
             note="Black Sheep Foods, plant-based lamb, San Francisco. AgFunderNews (2022-01-27): '$5.25 million in seed funding' with Bessemer Venture Partners among the investors; the firm's list dates the partnership to 2020, so its money went in before the seed was announced, and the total of $18.05M leaves about $0.5M of earlier funding that is not described, hence medium. Graduated on the $12.3M Series A led by Unovis with Bessemer taking part (TechCrunch, 2022-12-08). Still operating in 2026."))

# ---- bladelogic
L.append(cls("bladelogic", status="acquired", rng="below_1b", stage="Series A", stage_src=WV,
             stage_cite=SEC_BLADELOGIC_REDEMPTION, stage_conf="high", entry_date="2001-09-06", country="US",
             city="Lexington", focus="Data Infrastructure",
             rounds=[rnd("2001-09-06", "Series A", 6000000, BVP, True, SEC_BLADELOGIC_REDEMPTION, "filing"),
                     rnd("2002", "Series B", 10000000, None, True, SEC_BLADELOGIC_S1, "filing")],
             note="BladeLogic, data centre automation software, Lexington, Massachusetts (as the Battery book reads); IPO July 2007, acq. by BMC, 2008. The S-1: 'In September 2001, the Company issued 12,000,000 shares of Series A Preferred Stock and 12,000,000 shares of common stock, for an aggregate cash payment of $6,000,000', and the Series A Preferred Stock Redemption Agreement of 2007 is signed by Bessemer Venture Partners V and Bessec Ventures V as investors under the purchase agreement of 2001-09-06. The firm says Bob Goodman backed the company 'from its founding in 2001'."))

# ---- blue-apron
L.append(cls("blue-apron", rng="below_1b", city="New York", stage="Seed", stage_src=FP, stage_cite=ARCH("blue-apron"),
             stage_conf="high", entry_date="2012", grad="graduated", grad_src=WV, grad_cite=BI_BLUEAPRON, grad_conf="high",
             focus="Consumer & Marketplaces",
             rounds=[rnd("2012", "Seed", None, BVP, True, ARCH("blue-apron"), "firm"),
                     rnd("2013-02", "Series A", 3000000, "First Round Capital", True, None, "press"),
                     rnd("2015-06-09", "Series D at a $2B valuation", 135000000, "Fidelity", None, BI_BLUEAPRON, "press")],
             note="Blue Apron, meal kits, New York; IPO June 2017, acq. by Wonder Group, 2023, so no figure. The firm's archived listing: 'BVP was eager to support our ... former Bessemer colleague, Matt Salzberg, with seed capital to build Blue Apron. We backed the company at every stage'; its year is 2012. Graduated: the company raised a Series A in February 2013 (the First Round book) and by June 2015 a round at a $2 billion valuation (Business Insider)."))

# ---- blue-nile
L.append(cls("blue-nile", rng="below_1b", country="US", city="Seattle", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="1999-05", focus="Consumer & Marketplaces",
             rounds=[rnd("1999-05", "Series A", None, None, True, SEC_BLUENILE_S1, "filing"),
                     rnd("1999-08", "Series B (a warrant on it is dated August 1999)", None, None, None, SEC_BLUENILE_S1, "filing")],
             note="Blue Nile, online diamonds and jewellery, Seattle; IPO 2004, taken private in 2017 and sold to Signet in 2022, so acquired and no figure. The firm: 'BVP invested in Blue Nile ... in 1999'. The S-1 shows Bessemer Venture Partners IV and Bessec Ventures IV with 18.7%, level with Trinity, and Joanna Strober of Bessemer on the board from May 1999, the month the company was bought and first financed; a Series B existed by August 1999. The S-1 pages read do not list the series each fund bought, so the first round is named Series A from knowledge at medium confidence."))

# ---- boards
L.append(cls("boards", status="private", rng="below_1b", stage="undetermined", entry_date="2021", country="IL",
             country_src=WV, country_cite=SITE("boards"), focus="SaaS", flags=["city_unknown"], rounds=[],
             note="Boards (boards.com), a messaging and content workspace for direct sales teams. The firm lists it from 2021 on its Israel and Europe desks with its Israel partners; no funding report was found (Google News, 2026-10-01), so the round is undetermined, and the company's site gives no address, so Israel rests on the firm's desk tag and the city is left open. The site is live; no sale or shutdown found."))

jl.write("j01c", L)
