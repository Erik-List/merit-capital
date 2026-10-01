"""PRO-99 Kleiner Perkins, judge j08, batch 15 (hurray .. lifesquare)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd

L = []
V = lambda *a, **k: L.append(verdict(*a, **k))
C = lambda *a, **k: L.append(cls(*a, **k))
ASOF = "2026-09-30"
GRAD_LATER = "Graduation left for the graduation pass."

# ---- membership traps and boundary rulings
V("hurray", "not_member",
  "partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; decisions.md X1); "
  "the KPCB China listing carried it, and no KPCB China fund round in Hurray! is on record",
  ec="site_listing", conf="high")
V("hyperion-solutions-corporation", "not_member",
  "sale consideration (Erik 2026-09-22): Kleiner Perkins held Brio Technology (Brio Software), which Hyperion acquired "
  "in 2003; Hyperion's S-4 lists Kleiner Perkins Caufield & Byers among Brio's holders, and Arbor Software's 1998 "
  "merger proxy with Hyperion Software names no Kleiner Perkins fund. The acquired company is the base row "
  "brio-technology-inc.",
  ec="fund_filing", conf="medium", cite=jl.FTS("HYPERION", "S-4"))
V("kanghui", "not_member",
  "partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; decisions.md "
  "X1). The F-1 shows TDF Capital China II, LP bought Kanghui's Series A in July 2006 (and its Series B in January "
  "2008); no KPCB China fund appears as a holder, the F-1 calls KPCB China Fund only an affiliate of TDF Capital "
  "China II.",
  ec="fund_filing", conf="high", cite=jl.FTS("Kanghui", "F-1"))

# ---- KPCB China listing companies (X1, flag kpcb_china)
C("huxaxun", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("huxaxun"),
  focus="Industrial & Robotics", flags=["kpcb_china", "city_unknown"],
  note="On the KPCB China listing in 2010 only (GPS chips, Shanxi province; company site fast-china.com, now dead). "
       "No record of its rounds or fate was found, so status is unknown and the city is not placed beyond the province.")
C("id5", status="private", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("id5"),
  city="Beijing", focus="Fintech & Payments", flags=["kpcb_china"],
  note="KPCB China portfolio company (2012-17 page under Teams China, partner Wei Zhou; logo grid to 2023): "
       "identity and credit verification in China, site q.id5.cn (Guozhengtong, Beijing, inferred from the domain). "
       "No priced round or exit on record; the firm listed it as private through 2023.")
C("intohotel", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("intohotel"),
  focus="Consumer & Marketplaces", flags=["kpcb_china", "city_unknown"],
  note="KPCB China listing (2010) and 2013-14 company page: B2B hotel and travel services, Zhejiang province. "
       "The intohotel.com domain is now for sale; no shutdown or sale is on record, so status is unknown.")
C("kindstar-global", status="public", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("kindstar-global"),
  city="Wuhan", focus="Healthcare & Bio", flags=["kpcb_china"],
  note="KPCB China company (Teams China / Life Sciences, partner James Huang): specialty diagnostic testing labs, "
       "Wuhan; listed on HKEX (9960) in 2021. Market cap HKD 920.3M on 2026-09-30 (stockanalysis.com, "
       "https://stockanalysis.com/quote/hkg/9960/market-cap/): HKD 920.3M @ ECB 2026-09-30 (HKD/EUR 8.9095, "
       "EUR/USD 1.1355) = $117.3M, below $1B. The entry round is not on record.")
C("kingnet", status="public", rng="1b_plus", usd=5065227900, val_src="web_verified",
  val_cite="https://stockanalysis.com/quote/she/002517/market-cap/", asof=ASOF,
  extra={"valuation_range_source": "web_verified"},
  stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("kingnet"),
  city="Shanghai", focus="Media, Gaming & Advertising", flags=["kpcb_china"],
  note="KPCB China social-game company (partners Tina Ju, Xin Tang; founded 2008, after KPCB China opened); the "
       "listing's site kingnet.com is Kingnet Network (Kaiying), Shanghai, listed on the Shenzhen exchange (002517). "
       "Market cap CNY 33.96B on 2026-09-30: CNY 33.96B @ ECB 2026-09-30 (CNY/EUR 7.613, EUR/USD 1.1355) = $5.07B. "
       "The KPCB China round is not on record.")
C("kejingyuan", status="public", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite="http://www.kejingyuan.com/",
  city="Beijing", focus="Climate & Energy", flags=["kpcb_china"],
  note="On the kleinerperkins.com logo grid 2021-24 (the KPCB China class); the tile's site is Beijing Kejingyuan "
       "Technology (water environment treatment), listed on the Shenzhen ChiNext board (301372). Market cap CNY 2.35B "
       "on 2026-09-30 (stockanalysis.com): CNY 2.35B @ ECB 2026-09-30 (CNY/EUR 7.613, EUR/USD 1.1355) = $350.5M. "
       "Entry round not on record.")
C("jiangsu-yangtze-river-delta-fine-chemical", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("jiangsu-yangtze-river-delta-fine-chemical"),
  focus="Industrial & Robotics", flags=["kpcb_china", "city_unknown"],
  note="KPCB China company (Teams China / Greentech, partner Victor Leung; listed 2012-24): fine chemicals producer in "
       "Jiangsu. It listed on Nasdaq in 2016 as Delta Technology Holdings through the CIS Acquisition SPAC merger (the "
       "skipped duplicate delta-technology-holdings-ltd); its later fate was not established and its site js-csj.com "
       "no longer answers, so status is unknown.")
C("jhl-biotech", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
  country="TW", country_src="web_verified", country_cite="https://edenbiologics.com/", city="Hsinchu",
  city_src="web_verified", focus="Healthcare & Bio", flags=["kpcb_china"],
  note="Biologics developer and manufacturer founded 2012 in Taiwan; partners James Huang and Jimmy Wei were KPCB "
       "China's life-sciences partners, so the position is read as KPCB China's (flagged). Renamed Eden Biologics in "
       "February 2021 (based in Hsinchu, its site says); Bora Pharmaceuticals acquired its CDMO business, the operating "
       "core, effective 2022-07-01, read as acquired with Bora as successor. Entry round not on record.")

# ---- US and other listed companies
C("indigo", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
  focus="Industrial & Robotics", flags=["city_unknown"],
  note="The firm's page (invest year 1995, Early, Prior) describes digital color printing press technology (Indigo, "
       "bought by HP in 2001-02) but names J&J as acquirer (J&J bought Indigo Medical in 1996): the identity is split "
       "on the firm's own card. Acquired either way; the entry round is not on record, and the city is left unplaced.")
C("infinera", city="San Jose", rng="below_1b",
  stage="Series A", stage_src="web_verified", stage_conf="high", entry_date="2001",
  stage_cite="https://www.sec.gov/Archives/edgar/data/1138639/000119312507038979/dex1010.htm",
  rounds=[rnd("2001", "Series A", 36906000, None, True,
              "https://www.sec.gov/Archives/edgar/data/1138639/000119312507038979/dex1010.htm", "filing")],
  focus="Data Infrastructure",
  note="Exhibit A of the investors' rights agreement filed with the 2007 S-1 lists KPCB Holdings (nominee for KPCB X) "
       "first among the Series A holders; the S-1 shows KPCB X-A and X-B as 9.3% holders. Series A amount from the "
       "liquidation preferences (Sutter Hill's row). Nokia bought Infinera (closed 2025); San Jose since 2019, matching "
       "Accel and Sutter Hill.")
C("inmobi", country="IN", country_src="web_verified", country_cite=jl.W("InMobi"), city="Bangalore",
  stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=jl.W("InMobi"), entry_date="2008",
  rounds=[rnd("2008", "Series A", 7100000, "Kleiner Perkins Caufield & Byers", True, jl.W("InMobi"), "press"),
          rnd("2010", "Series B", 8000000, None, None, jl.W("InMobi"), "press")],
  focus="Media, Gaming & Advertising",
  note="Wikipedia: after the rebrand from mKhoj, the Series A of $7.1M came from Kleiner Perkins Caufield & Byers in "
       "2008 (iFund page, partner Mike Abbott). The India country is confirmed (Bangalore; the firm's 2010 listing "
       "said Mumbai/Bangalore). The base row mkhoj is the same company under its former name.")
C("inrix", status="private", rng="below_1b", city="Kirkland",
  stage="Growth", stage_src="model", stage_conf="medium", entry_date="2011",
  rounds=[], focus="Data Infrastructure",
  note="Traffic data and analytics, Kirkland WA (Wikipedia infobox). Kleiner Perkins came in through the Green Growth "
       "Fund (2012-18 page), in the round it led in 2011 after August Capital and Venrock's earlier rounds from 2005: "
       "a later round, Growth, not cited this pass. No $1B mark on record.")
C("insidesales", status="acquired", rng="below_1b", country="US", city="Provo",
  stage="Growth", stage_src="model", stage_conf="medium", rounds=[],
  focus="SaaS",
  note="InsideSales.com (renamed XANT in 2019), Provo UT; Aurea completed its acquisition on 2021-08-02 (Business "
       "Wire). Kleiner Perkins entered through the Digital Growth Fund (partners Alex Kurland, Matt Murphy), leading "
       "the $100M round of 2014: a later round, Growth; not cited this pass.")
C("insite-vision", country="US", city="Alameda", rng="below_1b", stage="undetermined", rounds=[],
  focus="Healthcare & Bio",
  note="InSite Vision, ophthalmic drug delivery, Alameda CA, publicly listed and bought by Akorn in 2015. The firm's "
       "2012 page carries a mismatched description ('multimedia authoring tools'); the entry round is not on record.")
C("instart-logic", status="acquired", rng="below_1b", country="US", city="Palo Alto",
  stage="undetermined", focus="Data Infrastructure",
  rounds=[rnd("2012-02", "Series A", 9000000, None, None, jl.W("Instart"), "press"),
          rnd("2013-04", "Series B", 17000000, None, None, jl.W("Instart"), "press"),
          rnd("2014-05", "Series C", 26000000, None, None, jl.W("Instart"), "press"),
          rnd("2015-05", "Series C2", 13000000, None, None, jl.W("Instart"), "press")],
  note="Web application delivery, Palo Alto. On the firm's list from 2014 (partners Alex Kurland, Matt Murphy); "
       "Wikipedia gives the rounds but no investor per round, so the round Kleiner Perkins entered is not tied down. "
       "Akamai took the customers and select IP (2020), as a16z and Sutter Hill record.")
C("instinct", rng="10b_plus", usd=10000000000, val_src="web_verified",
  val_cite="https://www.pymnts.com/news/artificial-intelligence/2026/personal-ai-agent-instinct-quadruples-valuation-to-10-billion-in-1-month/",
  asof="2026-09-28", extra={"valuation_range_source": "web_verified"},
  stage="Series A", stage_src="web_verified", stage_conf="high", entry_date="2026-08",
  stage_cite="https://techfundingnews.com/noah-shinns-instinct-goes-from-100m-to-2-5b-in-weeks-23-year-olds-ai-assistant-just-raised-250m-series-b/",
  rounds=[rnd("2026", "Seed", None, "Conviction and Greenoaks", False,
              "https://techfundingnews.com/noah-shinns-instinct-goes-from-100m-to-2-5b-in-weeks-23-year-olds-ai-assistant-just-raised-250m-series-b/", "press"),
          rnd("2026-08", "Series A", 75000000, "Kleiner Perkins", True,
              "https://techfundingnews.com/noah-shinns-instinct-goes-from-100m-to-2-5b-in-weeks-23-year-olds-ai-assistant-just-raised-250m-series-b/", "press"),
          rnd("2026-08-26", "Series B", 250000000, "Index Ventures and Benchmark", None,
              "https://techfundingnews.com/noah-shinns-instinct-goes-from-100m-to-2-5b-in-weeks-23-year-olds-ai-assistant-just-raised-250m-series-b/", "press"),
          rnd("2026-09-28", "Series C", 1000000000, "Sequoia, Benchmark and Coatue", None,
              "https://www.pymnts.com/news/artificial-intelligence/2026/personal-ai-agent-instinct-quadruples-valuation-to-10-billion-in-1-month/", "press")],
  focus="AI & Applied AI", flags=["city_unknown"],
  note="Personal AI agent (Noah Shinn). Mamoon Hamid of Kleiner Perkins led the $75M Series A in early August 2026 at "
       "about $500M, after a seed led by Conviction and Greenoaks without KP (Tech Funding News). The $1B Series C at "
       "$10B closed 2026-09-28 (PYMNTS), replacing the $2.5B Series B mark. Momentum check 2026-09-30 done. No city "
       "on the company's site or in the coverage. The y-combinator row 'Instinct' (London) is a different company.")
C("intercom", status="acquired", rng="below_1b", city="San Francisco",
  stage="Growth", stage_src="web_verified", stage_conf="high", entry_date="2018-03",
  stage_cite=jl.W("Intercom (company)"),
  rounds=[rnd("2013-03", "Series A", 6000000, "Social Capital", False, jl.W("Intercom (company)"), "press"),
          rnd("2014-01", "Series B", 23000000, "Bessemer Venture Partners", False, jl.W("Intercom (company)"), "press"),
          rnd(None, "Series C-1", 50000000, "Index Ventures", False, jl.W("Intercom (company)"), "press"),
          rnd("2018-03", "Series D", 125000000, "Kleiner Perkins", True, jl.W("Intercom (company)"), "press")],
  focus="SaaS",
  note="Kleiner Perkins led the $125M Series D in March 2018 at $1.275B (Wikipedia; CNBC and EU-Startups headlines), "
       "its first round in Intercom. Renamed Fin; Salesforce agreed to buy it for about $3.6B on 2026-06-15 and closed "
       "the deal (GV's row records the closing, 2026-09-14), so the stale private $1.2B mark is replaced by acquired.")
C("interpore-international", status="acquired", rng="below_1b", country="US", city="Irvine",
  stage="undetermined", rounds=[], focus="Healthcare & Bio",
  note="Coral-derived synthetic bone graft maker, Irvine CA; public from 1993 and acquired by Biomet in 2004. The "
       "entry round is not on record.")
C("intersperse", status="acquired", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Data Infrastructure", flags=["city_unknown"],
  note="Hosted integration services (partner Kevin Compton); the firm's 2012-14 page shows Acquired and its company "
       "link points to tidalsoftware.com, so Tidal Software was the buyer. City not established.")
C("intraware", status="acquired", rng="below_1b", country="US", city="Orinda", stage="undetermined",
  rounds=[rnd("2001-01", "Series A Preferred (post-IPO private placement)", 5200000, None, True,
              jl.FTS("INTRAWARE", "8-K"), "company")],
  focus="SaaS",
  note="Intraware's January 2001 release says Kleiner Perkins invested before the 1999 IPO and joined the $5.2M "
       "post-IPO preferred placement (KPCB VIII Associates signed), so the position is venture; the pre-IPO round is "
       "not named. Acquired by Acresso Software in 2009; Orinda matches TCV.")
C("invisioneer", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Media, Gaming & Advertising", flags=["city_unknown"],
  note="Video discovery app backed with partner Randy Komisar (2013-15 pages); its site no longer answers and no "
       "round, sale or shutdown is on record.")
C("iolon", status="acquired", rng="below_1b", city="San Jose", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="Tunable lasers and optical devices (partner Vinod Khosla, during his KP years); the firm's page shows Acquired "
       "with the company link pointing to coherent.com, Coherent being the buyer. City from knowledge, medium.")
C("ip-unity", status="private", rng="below_1b", country="US", city="Atlanta", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="IP Unity (Milpitas in the firm's 2008-10 listing), telecom service platforms, became Movius Interactive; the "
       "firm's Movius page (2013-14) carries the same partner (Vinod Khosla). The base row movius is the same company, "
       "classified alike (private, Atlanta as Battery records).")
C("ivillage", status="acquired", rng="below_1b", city="New York", stage="undetermined", rounds=[],
  focus="Media, Gaming & Advertising",
  note="Women's online network, New York; public from 1999 and bought by NBCUniversal in 2006 for $600M (Wikipedia). "
       "The pre-IPO round Kleiner Perkins entered is not on record.")
C("izon-formerly-ophthonix", status="unknown", rng="below_1b", country="US", city="San Diego",
  stage="undetermined", rounds=[], focus="Healthcare & Bio",
  note="Ophthonix (iZon high-resolution eyeglass lenses), San Diego, on the firm's 2008 list. The izonlens.com domain "
       "is for sale; no sale or shutdown is on record, so status is unknown.")
C("izumi", status="acquired", rng="below_1b", country="US", city="South San Francisco", stage="undetermined",
  rounds=[], focus="Healthcare & Bio",
  note="iZumi Bio (iPS cells, South San Francisco) merged with Pierian in 2009 to form iPierian, which Bristol-Myers "
       "Squibb acquired in 2014 (successor). The round Kleiner Perkins entered is not cited this pass.")
C("jawbone", city="San Francisco", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
  rounds=[], focus="Consumer & Marketplaces",
  note="AliphCom (Jawbone), San Francisco, liquidated in 2017. Kleiner Perkins came in through the sFund and Digital "
       "Growth Fund (partners Bing Gordon, Mary Meeker) after Sequoia's and Khosla's early rounds and a16z's 2011 "
       "round: a later round, Growth, not cited this pass.")
C("jd-com", status="public", rng="10b_plus", usd=35750000000, val_src="web_verified",
  val_cite="https://stockanalysis.com/stocks/jd/market-cap/", asof=ASOF,
  extra={"valuation_range_source": "web_verified"},
  city="Beijing", stage="Growth", stage_src="model", stage_conf="medium", rounds=[],
  focus="Consumer & Marketplaces",
  note="Held by the KPCB Digital Growth Fund and KPCB China (the F-1 names the KPCB funds and KPCB China Fund among "
       "pre-IPO holders), so it is IN under D2 without the kpcb_china flag. KP was not in Capital Today's 2007 Series A "
       "or the 2009 Series B, so its entry was a later round, Growth; the round is not named. Market cap $35.75B on "
       "2026-09-30, fresher than Insight's and Tiger's $35.63B. The skipped 360buy row is the same company.")
C("k2-space", status="private", rng="1b_plus", usd=6800000000, val_src="web_verified",
  val_cite="https://pulse2.com/k2-space-raises-500-million-series-d-at-6-8-billion-valuation/", asof="2026-07",
  extra={"valuation_range_source": "web_verified"},
  country="US", country_src="model_knowledge", city="Torrance",
  stage="Growth", stage_src="first_party", stage_conf="medium", entry_date="2026-07",
  stage_cite=jl.POST("k2-space-building-bigger-2"),
  rounds=[rnd("2026-07", "Series D", 500000000, "Kleiner Perkins", True, jl.POST("k2-space-building-bigger-2"), "firm")],
  focus="Industrial & Robotics", flags=["model_disputes_source"],
  note="The firm's post says it led K2's $500M Series D (July 2026, $6.8B post, Payload Space and Pulse 2.0), and its "
       "own page dates the relationship to 2026, so the D is the entry: Growth. Satellite maker in Torrance CA; the GB "
       "country is a bad join, disputed to US as ICONIQ and Redpoint have it.")
C("kaiima", status="private", rng="below_1b", country="BR", country_src="web_verified",
  country_cite="https://kaiima.com.br/", city="Campinas", stage="undetermined", rounds=[],
  focus="Climate & Energy",
  note="Seed and breeding technology backed by the Green Growth Fund (partners John Denniston, Ryan Popple), founded in "
       "Israel; kaiima.com now redirects to Kaiima Sementes, a hybrid castor-seed breeder at Campinas, Brazil, which is "
       "where it operates now. Entry round not cited this pass.")
C("kalpana", status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="First Ethernet switch maker, Sunnyvale CA (Wikipedia), acquired by Cisco in 1994; the firm's page gives 1992 "
       "and Early, an anchor only. Menlo's row has Santa Clara; Wikipedia places it in Sunnyvale.")
C("kapwing", status="private", rng="below_1b", country="US", city="San Francisco", stage="undetermined", rounds=[],
  focus="SaaS",
  note="Online video editor, San Francisco (its About page). On the firm's consumer logo grid 2018-19; the round "
       "Kleiner Perkins entered is not on record this pass. No $1B mark.")
C("kilowatt-financial", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Climate & Energy", flags=["city_unknown"],
  note="Residential solar and efficiency lending backed by the Green Growth Fund (partners Ben Kortlang, Daniel Oros), "
       "on the firm's pages 2014-15. Its domain no longer serves the company; no sale or shutdown is on record.")
C("knack", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="AI & Applied AI", flags=["city_unknown"],
  note="Game-based talent assessment (partner Bing Gordon), on the firm's pages 2013-26; its knack.it site no longer "
       "resolves and no later round, sale or shutdown is on record, so status is unknown.")
C("knownow-inc", status="unknown", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Event-driven integration software, Sunnyvale in the firm's 2008 listing (partner Kevin Compton); shown private "
       "to 2014, with no sale or shutdown on record.")
C("kodiak-networks", status="acquired", rng="below_1b", country="US", city="Plano", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Push-to-talk over cellular; acquired by Motorola Solutions in 2017 (Redpoint's row, Plano; the firm's 2008 "
       "listing had San Ramon). The round Kleiner Perkins entered is not on record; Redpoint's card gives Redpoint's "
       "own Series A in 2003.")
C("kotak-urja", status="unknown", rng="below_1b", country="IN", country_src="web_verified",
  country_cite=jl.ARCH("kotak-urja"), city="Bangalore", stage="undetermined", rounds=[],
  focus="Climate & Energy",
  note="Solar PV and thermal provider, Bangalore, on the firm's greentech list 2010-12. No round or later fate on record.")
C("kuark-finance", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined", rounds=[],
  country="CN", country_src="model_knowledge", focus="Fintech & Payments",
  flags=["kpcb_china", "identity_unresolved"],
  note="On the kleinerperkins.com logo grid 2021-24 with site kuark.com, which now serves only a Chinese-language "
       "frame to an unrelated page; no filing, publisher or register names the company behind 'Kuark Finance', so the "
       "row cannot be identified. Read as the KPCB China class on the grid (CN from the zh-CN page, low).")
C("leanplum", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined", rounds=[],
  focus="SaaS",
  note="Mobile engagement platform, San Francisco; leanplum.com now redirects to CleverTap, which bought it in 2022. "
       "The round Kleiner Perkins entered (on the firm's pages from 2017) is not on record this pass.")
C("leo", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Consumer & Marketplaces", flags=["city_unknown"],
  note="Ephemeral photo and video sharing app for family and friends (partner Megan Quinn, pages 2014-18); its "
       "getleoapp.com domain now serves an unrelated shop. No round or fate on record.")
C("level", country="US", country_src="model_knowledge", city="San Francisco", rng="below_1b",
  stage="undetermined", rounds=[], focus="Fintech & Payments", flags=["model_disputes_source"],
  note="Level Money (levelmoney.com), the San Francisco budgeting app (partners Chi-Hua Chien, Megan Quinn), bought by "
       "Capital One in 2015. The ES country is a bad one-word join: disputed to US. The first-round (New York dental "
       "benefits), lightspeed (New York, 2020) and y-combinator (S21) rows named Level are other companies.")
C("lifesquare", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Healthcare & Bio", flags=["city_unknown"],
  note="Emergency health-information service (partners Brook Byers, Dana Mead), on the firm's page in 2013 only; its "
       "site no longer serves content and no round or fate is on record.")

jl.write("j08a", L)
