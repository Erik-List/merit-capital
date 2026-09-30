"""PRO-100 NEA, judge c11, queue batch 22 (Vitae .. Zenas): classification of listed members."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, POST, W, FTS, NEWS

WV = {"valuation_range_source": "web_verified"}
TODAY = "2026-09-30"

# URLs printed by tools run in this session (ftsview/secget, stockanalysis curl, WebFetch/WebSearch reads)
SA = "https://stockanalysis.com/{}/market-cap/"
XENE_CO = "https://stockanalysis.com/stocks/xene/company/"
ARSANIS_S1A = "https://www.sec.gov/Archives/edgar/data/1501697/000119312517343803/d427310ds1a.htm"
XCEL_S1 = "https://www.sec.gov/Archives/edgar/data/1139665/000095010902000119/ds1.htm"
VC_A1 = "https://prweb.com/releases/2017/08/prweb14589605.htm"
WONDER_D = "https://www.restaurantdive.com/news/wonder-valuation-9-billion-latest-650m-funding/825417/"
YUGA_TC = "https://techcrunch.com/2022/03/22/bored-apes-nft-startup-yuga-labs-raises-at-monster-4-billion-valuation/"

L = []

# ---- Vitae Pharmaceuticals
L.append(cls("vitae-pharmaceuticals", country="US", city="Fort Washington", stage="undetermined", entry_date="2001",
             rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Computational drug-design company in Fort Washington, PA; IPO 2014, acquired by Allergan in 2016. The firm "
                  "dates its entry to 2001 (the pre-filled 2009 date is a later Form D), and no source names that round."))

# ---- Vitesse Semiconductor
VT_W = W("Vitesse Semiconductor")
L.append(cls("vitesse-semiconductor", city="Camarillo", stage="undetermined", entry_date="1987", rng="below_1b",
             focus="Industrial & Robotics",
             rounds=[rnd("1987", "venture", None, None, True, FTS("VITESSE", "DEF 14A"), "filing")],
             note="Camarillo chip company (Wikipedia), acquired by Microsemi in 2015. The firm labels it Public/PIPES from 1992, "
                  "but Wikipedia says it raised venture capital from Sequoia and NEA and its proxies show Spectra/NEA's James "
                  "Cole on the board since 1987, before the 1991 IPO, so NEA's first money was a private round (Spectra is "
                  "an NEA sleeve under D1); that round is not named."))

# ---- VividCortex
VC_R = NEWS("vividcortex", "builds on success with $4.5 million")
L.append(cls("vividcortex", status="acquired", city="Charlottesville", city_src="formd_address", stage="Series A",
             stage_src="model", stage_conf="medium", rng="below_1b", focus="Data Infrastructure",
             rounds=[rnd("2016", "Series A", 4500000, "NEA", True, VC_R, "press"),
                     rnd("2017-08-15", "Series A-1", 8500000, "Osage Venture Partners", True, VC_A1, "company")],
             note="NEA led the $4.5M round of 2016 (Charlottesville Tomorrow), and the company's release for the $8.5M round of "
                  "August 2017 names that one Series A-1 with NEA returning, so the 2016 round was the Series A. Acquired by "
                  "SolarWinds, per the firm's exit line."))

# ---- ViXS Systems
L.append(cls("vixs-systems", status="acquired", city="Toronto", stage="undetermined", entry_date="2006",
             rng="below_1b", focus="Industrial & Robotics", rounds=[],
             note="Toronto video-processing chip company (TSX-listed), acquired by Pixelworks in August 2017 (Pixelworks' "
                  "release). No source names the 2006 round NEA entered."))

# ---- Vonage
L.append(cls("vonage", city="Holmdel", stage="Growth", stage_src="first_party", stage_cite=SITE("vonage"),
             stage_conf="medium", entry_date="2003", rng="below_1b", focus="Consumer & Marketplaces",
             note="The firm labels its 2003 entry Growth. Acquired by Ericsson in 2022; city aligned with the BCV and IVP books."))

# ---- Vori Health (disputes the Form D band)
L.append(cls("vori-health", status="private", city="New York", city_src="formd_address", stage="Series A",
             stage_src="first_party", stage_cite=POST("our-investment-in-vori-health"), stage_conf="high",
             entry_date="2021-05-07", rng="below_1b", focus="Healthcare & Bio", flags=["stage_disputes_band"],
             rounds=[rnd("2021-05-07", "Series A", None, None, True, POST("our-investment-in-vori-health"), "firm")],
             note="The firm's own post (2021-05-07) announces its Series A investment in Vori Health; the Growth band read a "
                  "Form D sequence, not a named round."))

# ---- Vtesse
L.append(cls("vtesse", status="acquired", country="US", city="Gaithersburg", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2015-01-07", rng="below_1b", focus="Healthcare & Bio",
             rounds=[rnd("2015-01-07", "Series A", 25000000, None, True, POST("vtesse-first-spin-out"), "firm"),
                     rnd("2016-07-25", "Series A (additional)", 17000000, None, None, NEWS("vtesse", "nabs $17 million"),
                         "press")],
             note="Spun out of the NEA-backed Cydan with $25M in January 2015 (the firm's own post names NEA's investment); the "
                  "July 2016 $17M was reported as additional Series A, so the launch money was the Series A. Sucampo bought "
                  "Vtesse in April 2017 (Fierce Biotech)."))

# ---- Vuclip
L.append(cls("vuclip", status="acquired", city="Milpitas", stage="undetermined", entry_date="2008",
             rng="below_1b", focus="Media, Gaming & Advertising", rounds=[
                 rnd("2012-11-15", "Series D", 13000000, "Singtel Innov8", True,
                     NEWS("vuclip", "Raises $13M in Series D Funding"), "press")],
             note="Milpitas mobile video company (Wikipedia); PCCW took a majority stake in March 2015. NEA backed it from its "
                  "2008 founding and was in the 2012 Series D, but no source names the round NEA entered."))

# ---- VytronUS
L.append(cls("vytronus", status="acquired", city="Sunnyvale", city_src="formd_address", stage="undetermined",
             entry_date="2007", rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Cardiac ablation device company; the firm's listing says Acquired without naming a buyer, and no other source "
                  "found. The firm dates its entry to 2007; the pre-filled 2009 date is a later Form D."))

# ---- Wallapop
WP = NEWS("wallapop", "Naver buys it for")
L.append(cls("wallapop", status="acquired", country="ES", country_src="web_verified", country_cite=WP, city="Barcelona",
             stage="undetermined", entry_date="2015", rng="below_1b", focus="Consumer & Marketplaces", rounds=[],
             note="Barcelona second-hand marketplace; Naver agreed in August 2025 to buy it at a EUR 600M value "
                  "(Startupbusiness), and status is aligned with the Insight and Northzone books, which record the sale as "
                  "done. No source names the 2015 round NEA entered."))

# ---- Waltz Networks
L.append(cls("waltz-networks", status="unknown", city="San Francisco", city_src="formd_address", rng="below_1b",
             focus="Data Infrastructure",
             note="Adaptive networking startup; the firm listed it only in 2017-18 and nothing later was found. Graduation left "
                  "for the graduation pass."))

# ---- Waymark (disputes the Form D band)
WMK = POST("waymark-transforming")
L.append(cls("waymark", status="private", city="San Francisco", city_src="formd_address", stage="Series A",
             stage_src="first_party", stage_cite=WMK, stage_conf="high", rng="below_1b", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2022-01-04", "Series A", 45000000, None, True, WMK, "firm")],
             note="The firm's own post (2022-01-04) announces its investment with Waymark's $45M Series A; the Growth band read "
                  "the Form D sequence. City aligned with the a16z and Lux books."))

# ---- Wayport
L.append(cls("wayport", status="acquired", country="US", city="Austin", stage="undetermined", entry_date="1999",
             rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Austin Wi-Fi hotspot network acquired by AT&T in 2008, per the firm's exit line; the 1999 round is not named."))

# ---- Weaviate
WV_B = NEWS("weaviate", "Weaviate Raises $50 Million Series B")
WV_A = NEWS("weaviate", "ING invests in home-grown")
L.append(cls("weaviate", status="private", country="NL", country_src="web_verified", country_cite=WV_B,
             city="Amsterdam", stage="Series A", stage_src="web_verified", stage_cite=WV_A, stage_conf="high",
             entry_date="2022-02", rng="below_1b", focus="Data Infrastructure",
             rounds=[rnd("2022-02", "Series A", 16000000, "NEA, Cortical Ventures", True, WV_A, "press"),
                     rnd("2023-04-21", "Series B", 50000000, "Index Ventures", True, WV_B, "company")],
             note="ING's release names the $16M Series A (then SeMI Technologies) co-led by NEA and Cortical Ventures; the "
                  "firm's 2021 year is the close. The 2023 Series B release gives Amsterdam as headquarters (the Battery book "
                  "says San Francisco). Momentum check 2026-09-30: no round after the 2023 Series B found, no $1B mark."))

# ---- WebEx
L.append(cls("webex-communications", status="acquired", country="US", city="Santa Clara", stage="undetermined",
             entry_date="1999", rng="below_1b", focus="SaaS", rounds=[],
             note="Acquired by Cisco in 2007. NEA's Scott Sandell joined the board in December 1999 (the 2001 proxy); the round "
                  "is not named."))

# ---- WebMD (Healtheon)
L.append(cls("webmd-healtheon", status="acquired", country="US", city="New York", stage="undetermined",
             entry_date="1996", rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="NEA backed Healtheon in 1996; Healtheon/WebMD became WebMD Health, taken private by KKR's Internet Brands in "
                  "2017. The 1996 round is not named."))

# ---- Welltok
L.append(cls("welltok", status="acquired", city="Denver", city_src="formd_address", stage="undetermined",
             rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Consumer health platform acquired by Virgin Pulse in 2021, per the firm's exit line. The firm's own 2013 post "
                  "calls Welltok its first investment in the space but names no round."))

# ---- Wheelhouse
L.append(cls("wheelhouse", status="private", country="US", city="San Francisco", stage="undetermined",
             rng="below_1b", focus="SaaS", rounds=[],
             note="Revenue management software for short-term rentals; still private per the firm. Google News returned only "
                  "namesakes, so no round is on record."))

# ---- Wheels Up
WU = NEWS("wheels-up", "Wheels Up Lands Up To $115 Million")
L.append(cls("wheels-up", status="public", city="New York", stage="Growth", stage_src="web_verified", stage_cite=WU,
             stage_conf="medium", entry_date="2015-09-28", rng="below_1b", usd=122980000, val_src="web_verified",
             val_cite=SA.format("stocks/up"), asof=TODAY, extra=WV, focus="Consumer & Marketplaces",
             rounds=[rnd("2015-09-28", "unnamed", 115000000, "T. Rowe Price", True, WU, "company")],
             note="The company's release (2015-09-28) names NEA with T. Rowe Price and Fidelity in the up-to-$115M raise that "
                  "valued Wheels Up above $500M, a crossover round, matching the firm's 2015 year. Public via SPAC in 2021; "
                  "market cap $122.98M on 2026-09-30 (stockanalysis.com)."))

# ---- WiiTH
L.append(cls("wiith", status="private", country="US", stage="Seed", stage_src="first_party", stage_cite=SITE("wiith"),
             stage_conf="medium", entry_date="2022", rng="below_1b", focus="Consumer & Marketplaces",
             flags=["city_unknown"], rounds=[],
             note="Social messaging app the firm labels a 2022 Seed, now a past holding. No press or location found. "
                  "Graduation left for the graduation pass."))

# ---- Willow
L.append(cls("willow", status="private", country="US", city="Mountain View", city_src="web_verified",
             stage="undetermined", entry_date="2014", rng="below_1b", focus="Healthcare & Bio",
             flags=["model_disputes_source"], rounds=[],
             note="Willow Innovations, the Mountain View wearable breast pump maker (Business Journals, 2022), which bought "
                  "Elvie's assets in 2025; the pre-filled GB country was a one-word-name join, and the YC book's Willow is a "
                  "different company. No source names NEA's 2014 round."))

# ---- Wispr AI
WS_B = NEWS("wispr-ai", "Wispr Flow Raises $280 Million Series B")
L.append(cls("wispr-ai", status="private", country="US", city="San Francisco", stage="Seed", stage_src="first_party",
             stage_cite=SITE("wispr-ai"), stage_conf="medium", entry_date="2021", grad="graduated",
             grad_src="web_verified", grad_cite=WS_B, grad_conf="high", rng="1b_plus", usd=2000000000,
             val_src="web_verified", val_cite=WS_B, asof="2026-08-17", extra=WV, focus="AI & Applied AI",
             rounds=[rnd("2021", "Seed", None, None, True, SITE("wispr-ai"), "firm"),
                     rnd("2026-08-17", "Series B", 280000000, "Menlo Ventures", True, WS_B, "press")],
             note="The firm labels its 2021 entry Seed (its post of 2021-12-17 announces it). The $280M Series B of August 2026 "
                  "led by Menlo at a $2B valuation, with NEA returning (San Francisco), graduates and bands the row; momentum "
                  "check 2026-09-30."))

# ---- Wizard (disputes the Form D band)
WZ = NEWS("wizard", "Wizard emerges from stealth")
L.append(cls("wizard", status="private", city="New York", city_src="formd_address", stage="Series A",
             stage_src="web_verified", stage_cite=WZ, stage_conf="high", entry_date="2021-10-07", rng="below_1b",
             focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             rounds=[rnd("2021-10-07", "Series A", 50000000, "NEA", True, WZ, "press")],
             note="Fortune (2026-02-11) says Wizard raised a $50M Series A in 2021 led by NEA, with Accel and Marc Lore; the "
                  "Growth band read the filing. The New York company relaunched as a consumer shopping agent in 2026; no "
                  "later priced round or valuation found (checked 2026-09-30)."))

# ---- WNP Communications
L.append(cls("wnp-communications", status="acquired", country="US", stage="undetermined", entry_date="1998",
             rng="below_1b", focus="Data Infrastructure", flags=["city_unknown"], rounds=[],
             note="LMDS licence holder acquired by NEXTLINK, per the firm's exit line; Google News and Wikipedia have nothing "
                  "on its location or rounds."))

# ---- Woebot
L.append(cls("woebot", status="private", country="US", city="San Francisco", stage="Series A", stage_src="model",
             stage_conf="medium", entry_date="2017", rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Mental health chatbot company; NEA led its $8M Series A, announced in March 2018 (the firm's year 2017 is "
                  "the close). Google News on 2026-09-30 found no page to cite, so the stage rests on the named deal."))

# ---- Wonder
L.append(cls("wonder", status="private", city="New York", city_src="formd_address", rng="1b_plus", usd=9000000000,
             val_src="web_verified", val_cite=WONDER_D, asof="2026-07-16", extra=WV,
             focus="Consumer & Marketplaces",
             note="Restaurant Dive (2026-07-16): a $650M Series D at a $9B pre-money valuation; mark aligned with the Accel, "
                  "BCV, General Catalyst and GV books."))

# ---- Workday
L.append(cls("workday", city="Pleasanton", city_src="formd_address", focus="SaaS"))

# ---- Workera
WK_A = NEWS("workera", "Raises $16M in Funding Led by NEA")
L.append(cls("workera", status="private", country="US", city="Palo Alto", city_src="web_verified", stage="Series A",
             stage_src="web_verified", stage_cite=WK_A, stage_conf="high", entry_date="2021-08-26", rng="below_1b",
             focus="SaaS", flags=["model_disputes_source"],
             rounds=[rnd("2020-10", "Seed", 5000000, None, False, WK_A, "company"),
                     rnd("2021-08-26", "Series A", 16000000, "NEA", True, WK_A, "company"),
                     rnd("2023-03-23", "Series B", 23500000, None, None,
                         NEWS("workera", "closes $23.5m Series B"), "company")],
             note="The company's release (2021-08-26, Palo Alto) says NEA led the $16M Series A after a $5M seed; the pre-filled "
                  "CZ country was a one-word-name join. Pearson agreed to buy Workera on 2026-09-29, closing expected in the "
                  "second half of 2026 at an undisclosed price, so the row stays private."))

# ---- World Labs
WL_N = NEWS("world-labs", "NEA led a $100M round")
WL_AMD = NEWS("world-labs", "AMD Announces $8.2 Billion Acquisition")
L.append(cls("world-labs", status="private", city="San Francisco", stage="undetermined", entry_date="2024-08",
             rng="1b_plus", usd=8200000000, val_src="web_verified", val_cite=WL_AMD, asof="2026-09-29", extra=WV,
             focus="AI & Applied AI",
             rounds=[rnd("2024-04", "first round", None, "Andreessen Horowitz", False, WL_N, "press"),
                     rnd("2024-08-14", "unnamed", 100000000, "NEA", True, WL_N, "press")],
             note="TechCrunch (2024-08-14): NEA led a $100M round valuing World Labs above $1B, after a first round from a16z "
                  "and Radical at $200M; neither round is named, so the stage is undetermined. AMD agreed on 2026-09-29 to buy "
                  "World Labs in an all-stock deal valued at $8.2B (not yet closed), which is the mark."))

# ---- X4 Pharmaceuticals (X1 case)
L.append(cls("x4-pharmaceuticals", country="US", city="Boston", stage="Growth", stage_src="web_verified",
             stage_cite=ARSANIS_S1A, stage_conf="medium", entry_date="2017-11", focus="Healthcare & Bio",
             rounds=[rnd("2017-11", "concurrent private placement at IPO", 20000000, None, True, ARSANIS_S1A, "filing")],
             note="X1 case: the listed company is the former Arsanis, whose 2017 IPO came with a concurrent $20M private "
                  "placement to New Enterprise Associates 16 (S-1/A), a crossover-style entry at the listing; X4 merged into "
                  "it in 2019 and the firm now labels the row Public/PIPES from 2022. Membership under X1 is left to that "
                  "pass."))

# ---- Xaira Therapeutics
L.append(cls("xaira-therapeutics", status="private", country="US", city="South San Francisco", stage="Seed",
             stage_src="first_party", stage_cite=SITE("xaira-therapeutics"), stage_conf="medium", entry_date="2024",
             grad="censored", rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="AI drug-discovery company launched in April 2024 with over $1B; the firm labels its entry Seed. No valuation "
                  "has been disclosed (press calls it a unicorn without a figure), so below_1b. A bare 2024 entry is inside the "
                  "window, so censored. City aligned with the Menlo book."))

# ---- Xcel Pharmaceuticals (a documented round overrides the Growth label)
XC = FTS("XCEL PHARMACEUTICALS", "S-1")
L.append(cls("xcel", status="acquired", country="US", city="San Diego", stage="Series A", stage_src="web_verified",
             stage_cite=XC, stage_conf="medium", entry_date="2001-03-30", rng="below_1b", focus="Healthcare & Bio",
             flags=["stage_disputes_band"],
             rounds=[rnd("2001-03-30", "Series A", None, None, True, XC, "filing")],
             note="The S-1 exhibits name New Enterprise Associates among the Series A investors under the voting agreement of "
                  "2001-03-30, and NEA's Sigrid Van Bladel joined the board in March 2001, so the firm's Growth label gives way "
                  "to the named Series A. Acquired by Valeant in 2005."))

# ---- Xenon Pharmaceuticals (X1 case)
L.append(cls("xenon-pharma", status="public", country="CA", country_src="web_verified", country_cite=XENE_CO,
             city="Burnaby", stage="Growth", stage_src="model", stage_conf="low", entry_date="2019",
             rng="1b_plus", usd=3580000000, val_src="web_verified", val_cite=SA.format("stocks/xene"), asof=TODAY,
             extra=WV, focus="Healthcare & Bio", rounds=[],
             note="X1 case: Xenon has been listed on Nasdaq since 2014 and the firm labels its 2019 entry Public/PIPES; "
                  "membership under X1 is left to that pass, and the stage is the Growth X1 assigns if a PIPE is ruled an "
                  "entry. Market cap $3.58B on 2026-09-30 (stockanalysis.com)."))

# ---- XenSource
L.append(cls("xensource", status="acquired", country="US", city="Palo Alto", stage="undetermined", entry_date="2005",
             rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Xen virtualization company acquired by Citrix in 2007, per the firm's exit line; no source names the 2005 "
                  "round NEA entered."))

# ---- Xfire
L.append(cls("xfire", status="acquired", country="US", city="Menlo Park", stage="undetermined", entry_date="2004",
             rng="below_1b", focus="Media, Gaming & Advertising", rounds=[],
             note="Gamer messaging platform from Menlo Park, acquired by Viacom for $102M in April 2006 (Wikipedia); the 2004 "
                  "round is not named."))

# ---- Xoc Pharmaceuticals
L.append(cls("xoc-pharmaceuticals", status="private", city="Los Gatos", city_src="formd_address", rng="below_1b",
             focus="Healthcare & Bio",
             note="CNS drug developer still listed Private by the firm; no later event found."))

# ---- Xoom
L.append(cls("xoom-corporation", city="San Francisco", city_src="formd_address", stage="undetermined",
             entry_date="2004", rng="below_1b", focus="Fintech & Payments", rounds=[],
             note="Money-transfer company acquired by PayPal in 2015. NEA's Dick Kramlich joined the board in April 2005 and "
                  "the firm dates its entry to 2004; the pre-filled 2011 date is a later Form D, and the round is not named."))

# ---- Xros
L.append(cls("xros", status="acquired", country="US", city="Sunnyvale", stage="undetermined", entry_date="1999",
             rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Optical switching company acquired by Nortel in 2000; city aligned with the Greylock and Menlo books."))

# ---- XSKY
XS = NEWS("xsky", "Files for Hong Kong IPO")
L.append(cls("xsky", status="private", country="CN", country_src="web_verified", country_cite=XS, city="Beijing",
             stage="Growth", stage_src="first_party", stage_cite=SITE("xsky"), stage_conf="medium", entry_date="2018",
             rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Beijing software-defined storage company (Pandaily), funded through Series F+, which filed for a Hong Kong "
                  "IPO in February 2026; no listing or disclosed valuation found. The firm labels its 2018 entry Growth."))

# ---- Xtera Communications
L.append(cls("xtera-communications-inc", status="acquired", country="US", city="Allen", stage="undetermined",
             entry_date="2000", rng="below_1b", focus="Data Infrastructure", rounds=[],
             note="Optical transport company, IPO 2015; it filed Chapter 11 in 2016 and HC2 Holdings bought its assets in 2017, "
                  "an asset sale out of insolvency. The 2000 round is not named."))

# ---- XTuit
L.append(cls("xtuit", status="defunct", city="Waltham", city_src="formd_address", stage="undetermined",
             rng="below_1b", focus="Healthcare & Bio", rounds=[],
             note="Endpoints (2018-07-06) reports the XTuit implosion that sent its CEO to Lundbeck; no sale found, so defunct. "
                  "Its Form Ds show a 2014 round of $22M after a small 2013 one, and no source names the round NEA entered."))

# ---- Yubico
YW = W("Yubico")
L.append(cls("yubico", status="public", country="SE", country_src="web_verified", country_cite=YW, city="Stockholm",
             stage="undetermined", entry_date="2017", rng="below_1b", usd=889900000, val_src="web_verified",
             val_cite=SA.format("quote/sto/YUBICO"), asof=TODAY, extra=WV, focus="Security", rounds=[],
             note="Stockholm YubiKey maker listed on Nasdaq Stockholm. Market cap SEK 8.88B on 2026-09-30 (stockanalysis.com); "
                  "SEK 8.88B @ ECB 2026-09-30 (SEK/EUR 11.331, EUR/USD 1.1355) = $889.9M. No source names NEA's 2017 round."))

# ---- Yuga Labs
L.append(cls("yuga-labs", status="private", country="US", city="Miami", stage="Growth", stage_src="first_party",
             stage_cite=SITE("yuga-labs"), stage_conf="medium", entry_date="2022", rng="1b_plus", usd=4000000000,
             val_src="web_verified", val_cite=YUGA_TC, asof="2022-03-22", extra=WV, focus="Crypto & Web3",
             flags=["stale"],
             rounds=[rnd("2022-03-22", "Seed", 450000000, "Andreessen Horowitz", None, YUGA_TC, "press")],
             note="The firm labels its 2022 entry Growth; TechCrunch's list for the $450M a16z-led round at $4B does not name "
                  "NEA, so the label stands. Mark aligned with the a16z, GV and Lightspeed books, stale with no later priced "
                  "round."))

# ---- Zania
ZN = NEWS("zania", "Zania Raises $18M Series A Led by NEA")
L.append(cls("zania", status="private", country="US", city="San Francisco", stage="Series A", stage_src="web_verified",
             stage_cite=ZN, stage_conf="high", entry_date="2025-09-30", rng="below_1b", focus="Security",
             rounds=[rnd("2025-09-30", "Series A", 18000000, "NEA", True, ZN, "company")],
             note="The company's release (2025-09-30) names the $18M Series A led by NEA, the day of the firm's own post. "
                  "Momentum check 2026-09-30: no later round or valuation found. City aligned with the Menlo book."))

# ---- Zenas BioPharma
L.append(cls("zenas-biopharma", city="Waltham", city_src="formd_address", focus="Healthcare & Bio"))

jl.write("c11b", L)
