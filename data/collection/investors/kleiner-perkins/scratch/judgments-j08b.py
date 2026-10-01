"""PRO-99 Kleiner Perkins, judge j08, batch 16 (lightera .. noteworth)."""
import judge_lib as jl
from judge_lib import cls, verdict, rnd

L = []
C = lambda *a, **k: L.append(cls(*a, **k))
ASOF = "2026-09-30"
SA = "https://stockanalysis.com/quote/"

# ---- KPCB China listing companies (X1, flag kpcb_china)
C("limei", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("limei"),
  focus="Media, Gaming & Advertising", flags=["kpcb_china", "city_unknown"],
  note="KPCB China company (Teams China / Digital, partner Wei Zhou; pages 2013-24): mobile advertising in China. "
       "limei.com serves nothing now; no round, sale or shutdown is on record, and the city is not established.")
C("madhouse", status="acquired", country="CN", country_src="web_verified", country_cite=jl.ARCH("madhouse"), city="Shanghai",
  rng="below_1b", stage="undetermined", rounds=[], focus="Media, Gaming & Advertising",
  flags=["kpcb_china", "model_disputes_source"],
  note="Madhouse (Yidong), the Shanghai mobile advertising network on the KPCB China listing from 2010. The CA "
       "country is a join to the Japanese anime studio of the same name: disputed to CN on the firm's own listing. "
       "Status stays acquired (BlueFocus took a majority stake, 2015, from knowledge; the brand still operates at "
       "madhouse.cn). Entry round not on record.")
C("manzuo", status="unknown", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("manzuo"), city="Beijing",
  focus="Consumer & Marketplaces", flags=["kpcb_china"],
  note="KPCB China company (partner Wei Zhou; pages 2012-24): Manzuo, a Beijing group-buying site. manzuo.com serves "
       "nothing now and no sale or shutdown is on record, so status is unknown.")
C("meican", status="private", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("meican"), city="Beijing",
  focus="Consumer & Marketplaces", flags=["kpcb_china"],
  note="Meican, corporate employee-meal platform (partner Wei Zhou, KPCB China; pages 2014-24); meican.com still "
       "operates. Beijing from knowledge. No priced round or mark on record.")
C("miaozhen-systems", status="acquired", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="web_verified", country_cite=jl.ARCH("miaozhen-systems"), city="Beijing",
  focus="Media, Gaming & Advertising", flags=["kpcb_china"],
  note="Miaozhen Systems, third-party ad measurement (partner Wei Zhou, KPCB China; pages 2013-24). It merged into "
       "Mininglamp (Beijing) and runs as its measurement brand (miaozhen.com), read as acquired with Mininglamp as "
       "successor (from knowledge, medium). Entry round not on record.")
C("miaopai", status="private", rng="below_1b", stage="undetermined", rounds=[],
  country="CN", country_src="model_knowledge", city="Beijing",
  focus="Media, Gaming & Advertising", flags=["kpcb_china"],
  note="Miaopai, the Chinese short-video app (Wikipedia: a Chinese video sharing and live streaming service) of Yixia Technology (Beijing), on the kleinerperkins.com logo grid "
       "2021-24 (the KPCB China class). No priced round or later mark is on record; read as private.")
C("med-zenith", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined", rounds=[],
  country="CN", country_src="model_knowledge", focus="Healthcare & Bio",
  flags=["kpcb_china", "identity_unresolved"],
  note="On the kleinerperkins.com logo grid 2021-24 with a site on a Chinese site-builder (med-zenith.jedoo.com, now "
       "404). Which Chinese medical company 'Med Zenith' is could not be established from any filing or publisher, so "
       "the row is unresolved; CN from the Chinese site, low.")

# ---- India
C("map-my-india", status="public", rng="below_1b", stage="undetermined", rounds=[],
  country="IN", country_src="web_verified", country_cite=jl.W("MapmyIndia"), city="New Delhi",
  focus="Data Infrastructure",
  note="MapmyIndia (C.E. Info Systems), digital maps, New Delhi (Wikipedia); Flipkart's 2015 purchase of a 34% stake "
       "gave the early investors their exit, and the company listed on the NSE in December 2021. Market cap INR 46.99B "
       "on 2026-09-30 (stockanalysis.com, " + SA + "nse/MAPMYINDIA/market-cap/): INR 46.99B @ ECB 2026-09-30 "
       "(INR/EUR 108.8205, EUR/USD 1.1355) = $490.3M, below $1B. The round Kleiner Perkins entered is not on record.")
C("naukri", status="public", rng="1b_plus", usd=8242510924, val_src="web_verified",
  val_cite=SA + "nse/NAUKRI/market-cap/", asof=ASOF, extra={"valuation_range_source": "web_verified"},
  country="IN", country_src="web_verified", country_cite=jl.W("Info Edge"), city="Noida",
  stage="undetermined", rounds=[], focus="Consumer & Marketplaces",
  note="Naukri.com is Info Edge (India), Noida, listed on the NSE since 2006. Market cap INR 789.92B on 2026-09-30: "
       "INR 789.92B @ ECB 2026-09-30 (INR/EUR 108.8205, EUR/USD 1.1355) = $8.24B. Open for review: no pre-IPO "
       "Kleiner Perkins round in Info Edge was found, and the firm's 2012 page calls it Acquired, so the listing may "
       "record a post-IPO or joint-vehicle position (T3, R3).")
C("mkhoj", status="private", country="IN", country_src="web_verified", country_cite=jl.W("InMobi"), city="Bangalore",
  stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=jl.W("InMobi"), entry_date="2008",
  rounds=[rnd("2008", "Series A", 7100000, "Kleiner Perkins Caufield & Byers", True, jl.W("InMobi"), "press")],
  rng="1b_plus", usd=1000000000, val_src="unicorn_list", asof="2017", flags=["stale"],
  focus="Media, Gaming & Advertising",
  note="mKhoj is InMobi's former name (Wikipedia: the Series A of $7.1M from Kleiner Perkins Caufield & Byers in 2008 "
       "came after the rebrand); the base row inmobi is the same company and this row mirrors it for the merge.")

# ---- the rest
C("lightera", status="acquired", rng="below_1b", country="US", city="Cupertino", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Optical networking equipment maker; the firm's page gives 1998, Early (an anchor only) and Ciena as acquirer "
       "(1999). Cupertino from knowledge. Ciena is its own base row.")
C("lotus-health-ai", status="private", rng="below_1b", country="US", city="San Francisco",
  stage="Series A", stage_src="first_party", stage_conf="medium", stage_cite=jl.SITE("lotus-health-ai"),
  entry_date="2024",
  rounds=[rnd("2026-02-03", "Series A (announced)", 35000000, "CRV and Kleiner Perkins", True,
              jl.SITE("lotus-health-ai"), "firm")],
  focus="Healthcare & Bio",
  note="AI primary-care practice. The firm's own page says KP co-led Lotus's Series A and dates the relationship to "
       "2024 (a close year); TechCrunch reported the $35M Series A on 2026-02-03 ($41M raised in all), and the firm "
       "posted about Lotus in February 2025. No $1B mark.")
C("m2z-networks", status="defunct", rng="below_1b", country="US", city="Menlo Park", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Ad-supported wireless broadband plan built on an FCC spectrum bid that was never granted; wound down, as "
       "Redpoint records, and its domain now serves an unrelated site.")
PULSE_MAI = "https://pulse2.com/mai-25-million-raised-to-launch-ai-agents-that-automate-performance-marketing-for-small-businesses/"
C("mai", status="private", rng="below_1b", flags=["city_unknown"],
  extra={"valuation_range_source": "web_verified", "valuation_citation": PULSE_MAI, "valuation_asof": "2025-10-07"},
  stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=jl.POST("mai-seed"), entry_date="2025-09",
  grad="censored", country="US",
  rounds=[rnd("2025-09-30", "Seed", 25000000, "Kleiner Perkins", True, PULSE_MAI, "press")],
  focus="AI & Applied AI",
  note="AI agents for performance marketing (founders Yuchen Wu, Jian Wang). The firm's post of 2025-09-30 says it "
       "led MAI's seed; Pulse 2.0 gives the $25M seed led by Kleiner Perkins with Gaorong and UpHonest. Entry inside "
       "24 months: censored. Momentum check 2026-09-30: no later priced round found, below $1B. City not stated.")
C("mango-health", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
  rounds=[], focus="Healthcare & Bio",
  note="Medication adherence app (partner Beth Seidenberg), San Francisco, acquired by TrialCard in 2018 (First "
       "Round's row). The firm's pages start in 2014, the year of the $5.25M Series A, but no source ties Kleiner "
       "Perkins to that round. The y-combinator Mango Health (W24, OCD therapy) is a different company.")
C("mascoma-corporation", status="acquired", rng="below_1b", country="US", city="Lebanon",
  stage="Growth", stage_src="web_verified", stage_conf="high", entry_date="2006-11",
  stage_cite=jl.FTS("Mascoma", "S-1"),
  rounds=[rnd(None, "Series A", 5000000, None, False, jl.FTS("Mascoma", "S-1"), "filing"),
          rnd("2006-11", "Series B", 30000000, None, True, jl.FTS("Mascoma", "S-1"), "filing")],
  focus="Climate & Energy",
  note="Cellulosic ethanol, Lebanon NH. The S-1 shows KPCB Holdings (nominee) buying $8.0M of the $30.0M Series B of "
       "November 2006 and becoming a 5% holder upon it, while Khosla and Flagship already held the Series A: entry at "
       "the B, Growth. The business went to Lallemand in 2014 (acquired, as General Catalyst and Khosla record).")
C("masergy", status="acquired", rng="below_1b", country="US", city="Plano", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Managed network services, Plano TX; KPCB Holdings appears as a 1.6% selling holder in the 2011 S-1/A (partner "
       "Kevin Compton). Comcast bought Masergy in 2021. The round Kleiner Perkins entered is not on record.")
C("mcube", status="private", rng="below_1b", country="US", city="San Jose", stage="undetermined", entry_date="2009",
  rounds=[rnd("2014", "Series C", 37000000, None, True, jl.W("MCube"), "press")],
  focus="Industrial & Robotics",
  note="MEMS motion sensors; Wikipedia says mCube was founded by Charles Yang and Kleiner Perkins in 2009, so KP was "
       "in from the founding round, which is not named. mCube bought Xsens and became Movella (mcube-inc.com now "
       "redirects to Xsens): the base row movella is the same company.")
C("metamatrix", status="acquired", rng="below_1b", country="US", city="New York", stage="undetermined", rounds=[],
  focus="Data Infrastructure", flags=["model_disputes_source"],
  note="Federated data access software (New York in the firm's 2008 listing). Red Hat acquired MetaMatrix in June "
       "2007 (Wikipedia; the firm's 2012 page shows Acquired), so the Wikidata 'defunct' is disputed.")
C("metaram", status="defunct", rng="below_1b", country="US", city="San Jose", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="Fabless memory-controller chips (MetaSDRAM), San Jose; the company closed in 2009 (from knowledge, medium).")
C("meter-parts", status="private", rng="below_1b", country="US", city="Boston", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="A 2021 logo-grid tile whose site meter.parts now redirects to Lumafield (industrial CT scanning, Boston); read "
       "as Lumafield's earlier name. The base row lumafield (on the live site since 2019) is the same company, and "
       "this row mirrors it.")
C("metricstream", status="private", rng="below_1b", country="US", city="San Jose", stage="undetermined", rounds=[],
  focus="SaaS",
  note="Governance, risk and compliance software; began in 1999 as Zaplet (partner Vinod Khosla, during his KP years) "
       "and became MetricStream in 2004 (Redwood Shores in the 2008 listing, San Jose now, from knowledge). The round "
       "Kleiner Perkins entered is not named on record.")
C("mevio", status="defunct", rng="below_1b", country="US", city="San Francisco",
  stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005-08",
  rounds=[rnd("2005-08", "first venture round (unnamed)", 8850000, None, True, jl.W("Mevio"), "press"),
          rnd("2008-07", "Series C", 15000000, "Crosslink Capital", True, jl.W("Mevio"), "press")],
  focus="Media, Gaming & Advertising",
  note="PodShow, later Mevio, San Francisco. Wikipedia: Kleiner Perkins, Sequoia and Sherpalo put about $8.85M into "
       "PodShow in August 2005, its first venture round, and the July 2008 round is named Series C, so the 2005 round "
       "reads Series A (model, medium). Defunct, as Sequoia records.")
C("miasole", status="acquired", rng="below_1b", country="US", city="Santa Clara",
  stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=jl.W("Miasolé"), entry_date="2005-06",
  rounds=[rnd("2005-06", "Series B", 16000000, "Kleiner Perkins Caufield & Byers", True, jl.W("Miasolé"), "press"),
          rnd("2006-10", "later round", 35000000, None, None, jl.W("Miasolé"), "press")],
  focus="Climate & Energy",
  note="Thin-film CIGS solar (partners John Doerr, Mark Allen). Wikipedia: Kleiner Perkins led the $16M B round of "
       "June 2005; no source puts KP in the earlier round, so the B is read as its entry (Growth, medium). Hanergy "
       "acquired MiaSole in 2013; San Jose in the 2008 listing, Santa Clara later.")
C("microchip-technology", status="public", rng="10b_plus", usd=42230000000, val_src="web_verified",
  val_cite="https://stockanalysis.com/stocks/mchp/market-cap/", asof=ASOF,
  extra={"valuation_range_source": "web_verified"},
  city="Chandler", stage="undetermined", rounds=[], focus="Industrial & Robotics",
  note="Microcontrollers, Chandler AZ (Wikipedia); it became independent of General Instrument in 1989 through a "
       "venture group led by Sequoia, and the round Kleiner Perkins took part in is not named. Market cap $42.23B on "
       "2026-09-30, fresher than Sequoia's $49.76B of 2026-08 (same band).")
C("mind-robotics", status="private", rng="1b_plus", usd=3400000000, val_src="web_verified",
  val_cite="https://www.channelnewsasia.com/business/rivian-spinout-mind-robotics-valued-34-billion-in-new-funding-round-6119256",
  asof="2026-05-13", extra={"valuation_range_source": "web_verified"},
  country="US", city="Palo Alto",
  stage="Growth", stage_src="first_party", stage_conf="medium", entry_date="2026-05",
  stage_cite=jl.POST("mind-robotics-building-the-ai-native-robotics-platform-for-manufacturing-2"),
  rounds=[rnd("2025-11", "Seed", 115000000, "Eclipse", False, "https://www.ocbj.com/automobiles/rivian-backed-mind-robotics-startup-raises-500-million/", "press"),
          rnd("2026-03", "Series A", 500000000, "Accel and Andreessen Horowitz", False, "https://www.ocbj.com/automobiles/rivian-backed-mind-robotics-startup-raises-500-million/", "press"),
          rnd("2026-05", "unnamed round after the Series A", 400000000, "Kleiner Perkins", True,
              jl.POST("mind-robotics-building-the-ai-native-robotics-platform-for-manufacturing-2"), "firm")],
  focus="Industrial & Robotics",
  note="Rivian spin-out, industrial AI robotics, Palo Alto. The firm's post (2026-05-13) says KP led Mind's latest "
       "round, the $400M round at $3.4B (Reuters via CNA), which followed Eclipse's $115M seed and the $500M Series A "
       "that Accel and a16z led in March 2026 without KP (the a16z and BCV rows): a post-A entry, Growth. The $3.4B "
       "mark is fresher than the below_1b that a16z, Accel and Redpoint recorded before it.")

C("mobilygen", status="acquired", rng="below_1b", country="US", city="Santa Clara", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="Low-power H.264 codec chips, Santa Clara (partner Russell Siegelman); Maxim Integrated acquired it in 2008 "
       "(Wikipedia). The round Kleiner Perkins entered is not on record.")
C("move-com", status="acquired", rng="below_1b", country="US", city="Austin", stage="undetermined", rounds=[],
  focus="Consumer & Marketplaces",
  note="Move, Inc. (Homestore until 2006; the skipped homestore-com-inc row is the same company), operator of "
       "realtor.com; News Corp bought it in 2014, and it moved its headquarters from Santa Clara to Austin in February "
       "2025 (Wikipedia). KPCB VIII filed a 13G amendment on Homestore in February 2001 (a fund holding); the entry round is not named.")
C("movius", status="private", rng="below_1b", country="US", city="Atlanta", stage="undetermined", rounds=[],
  focus="Data Infrastructure",
  note="Movius Interactive, mobile communications software, is the former IP Unity (the firm's 2013-14 page keeps "
       "partner Vinod Khosla from the IP Unity years); the base row ip-unity is the same company. Private, Atlanta, "
       "as Battery records. The round Kleiner Perkins entered in IP Unity is not on record.")
C("n3twork", status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined", rounds=[],
  focus="Media, Gaming & Advertising",
  note="Mobile games and media (sFund; partners Bing Gordon, Megan Quinn), San Francisco; Scopely bought its "
       "business in 2021, read as acquired as GV records. The round Kleiner Perkins entered is not cited this pass.")
C("navigenics", status="acquired", rng="below_1b", city="Foster City", stage="undetermined", rounds=[],
  focus="Healthcare & Bio", flags=["model_disputes_source"],
  note="Consumer genomics (partner Dana Mead). Life Technologies acquired Navigenics in July 2012 (Wikipedia; the "
       "firm's 2013-14 page shows Acquired), so the Wikidata 'defunct' is disputed; Sequoia's row also reads defunct "
       "and should be aligned. Foster City as Sequoia records (Redwood Shores in the 2008 listing).")
C("nchip", status="acquired", rng="below_1b", country="US", city="San Jose", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="Multichip module packaging; the firm's page gives 1989, Early (an anchor only) and Flextronics as acquirer. "
       "San Jose from knowledge, medium.")
C("neomagic", status="public", rng="below_1b", country="US", city="Santa Clara", stage="undetermined", rounds=[],
  focus="Industrial & Robotics",
  note="Fabless mobile multimedia chips; KPCB general partner James Lally sat on the board from July 1993, before the "
       "1997 IPO (the 2001 proxy), which ties the position to the firm's venture years. Still reporting acquisitions in "
       "2023 (Wikipedia); a micro-cap, below $1B, public and Santa Clara as Sequoia records. Entry round not named.")
C("neos-geosolutions", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Climate & Energy", flags=["city_unknown"],
  note="Subsurface interpretation for oil, gas and mineral exploration (Greentech team, partner Russell Siegelman; "
       "pages 2012-18). Its site no longer answers and no sale or shutdown is on record.")
C("netskope", rng="1b_plus", usd=7130000000, val_src="web_verified",
  val_cite="https://stockanalysis.com/stocks/ntsk/market-cap/", asof=ASOF,
  extra={"valuation_range_source": "web_verified"},
  country="US", city="Santa Clara", stage="undetermined", rounds=[], focus="Security",
  note="Cloud security, Santa Clara; the firm's page gives 2012, Early (an anchor only), Prior, IPO (NTSK, 2025). The "
       "pre-listing $0 float is replaced by the market cap, $7.13B on 2026-09-30 (the siblings' $5.91B and $7.29B "
       "marks share the band). The round Kleiner Perkins entered is not tied down this pass.")
C("new-vine-logistics", status="unknown", rng="below_1b", country="US", city="Napa", stage="undetermined", rounds=[],
  focus="Consumer & Marketplaces",
  note="Compliant direct-to-consumer wine fulfillment, Napa, on the firm's list 2008-12; its site no longer answers "
       "and no sale or shutdown is on record.")
C("next-autoworks", status="defunct", rng="below_1b", country="US", city="San Diego", stage="undetermined",
  rounds=[], focus="Industrial & Robotics",
  note="Planned low-cost fuel-efficient US car maker (Greentech team, partner Ray Lane) that never launched and wound "
       "down around 2012, as GV records (San Diego).")

SANG_M = "https://siliconangle.com/2026/06/25/mirendil-raises-200m-speed-scientific-research-ai/"
C("mirendil", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=SANG_M,
  asof="2026-06-25", extra={"valuation_range_source": "web_verified"},
  country="US", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=SANG_M, entry_date="2026-06",
  grad="censored",
  rounds=[rnd("2026-06-25", "Seed", 200000000, "Andreessen Horowitz", True, SANG_M, "press")],
  focus="AI & Applied AI", flags=["city_unknown"],
  note="Frontier AI lab for automated AI R&D (ex-Anthropic and Google founders). SiliconANGLE: $200M seed at a $1B "
       "valuation, led by a16z with Kleiner Perkins participating; the firm's post says it backed the team from day "
       "one, so the seed is the entry, inside 24 months (censored). Momentum check 2026-09-30: talks at $5B were "
       "reported on 2026-09-22 (Bloomberg), not a priced round, so the $1B seed stands. City not stated anywhere read.")
PULSE_MF = "https://pulse2.com/manifest-os-60-million-raised-at-750-million-valuation-to-scale-ai-native-law-firm-model/"
C("manifest-os", status="private", rng="below_1b",
  extra={"valuation_range_source": "web_verified", "valuation_citation": PULSE_MF, "valuation_asof": "2026-04-28"},
  country="US", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=PULSE_MF, entry_date="2026-04",
  rounds=[rnd("2026-04-28", "Series A", 60000000, "Menlo Ventures", True, PULSE_MF, "press")],
  focus="AI & Applied AI", flags=["city_unknown"],
  note="Platform for AI-native law firms (Manifest Law, business immigration). Pulse 2.0: $60M Series A at a $750M "
       "valuation, led by Menlo Ventures alongside Kleiner Perkins, First Round and Quiet (2026-04-28); the firm's page "
       "dates the relationship to 2026 and no earlier round names KP, so the A is the entry. Momentum check "
       "2026-09-30: no later priced round found, below $1B. City not stated in the sources read.")
SANG_N = "https://siliconangle.com/2025/03/25/nexthop-ai-launches-110m-build-next-gen-cloud-ai-infrastructure/"
NH_B = "https://nexthop.ai/news-and-event/nexthop-ai-accelerates-into-hypergrowth-with-oversubscribed-500m-series-b-funding-catapulting-the-companys-valuation-to-4-2-billion/"
C("nexthop-ai", status="private", rng="1b_plus", usd=4200000000, val_src="web_verified", val_cite=NH_B,
  asof="2026-03-10", extra={"valuation_range_source": "web_verified"},
  country="US", city="Santa Clara",
  stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=SANG_N, entry_date="2025-03",
  rounds=[rnd("2025-03-25", "Series A", 110000000, "Lightspeed Venture Partners", True, SANG_N, "press"),
          rnd("2026-03-10", "Series B", 500000000, "Lightspeed Venture Partners", True, NH_B, "company")],
  focus="Data Infrastructure",
  note="AI data-center networking, Santa Clara. SiliconANGLE names Kleiner Perkins among the participants in the "
       "$110M launch round led by Lightspeed (2025-03-25), the round the Series B release and Lightspeed's card treat as "
       "the Series A; the firm's page dates KP to 2025. Momentum check 2026-09-30: the $500M Series B at $4.2B "
       "(company release, 2026-03-10), with all existing investors, is the latest priced round.")
GNW = "https://globenewswire.com/news-release/2021/12/06/2346797/0/en/nearside-formerly-hatch-raises-58-million-series-b-for-free-checking-account-with-universal-1-cashback-rewards-for-business.html"
C("nearside", status="private", rng="below_1b",
  extra={"valuation_range_source": "web_verified", "valuation_citation": GNW, "valuation_asof": "2021-12-06"},
  country="US", city="San Francisco",
  stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=jl.POST("hatch-series-a"),
  rounds=[rnd(None, "Seed", None, None, True, jl.POST("hatch-series-a"), "firm"),
          rnd("2021-04", "Series A", 20000000, None, True, jl.POST("hatch-series-a"), "firm"),
          rnd("2021-12-06", "Series B", 58000000, "Valar Ventures", True, GNW, "company")],
  focus="Fintech & Payments",
  note="Nearside is the renamed Hatch (founder Thomson Nguyen; 'Nearside (formerly Hatch)' in its Series B release); "
       "the base row hatch is the same company. The firm's April 2021 post says Hatch was formed in its offices and "
       "that it supported the company from Seed to Series A (the $20M A of April 2021), and KP joined Valar's $58M "
       "Series B (2021-12-06, San Francisco dateline). The seed date is not on record, so the named Series A cannot "
       "yet be recorded as a graduation. Graduation left for the graduation pass. Momentum check 2026-09-30: no later "
       "priced round or $1B mark found.")

C("mindbloom", status="private", rng="below_1b", country="US", city="New York", stage="undetermined", rounds=[],
  focus="Healthcare & Bio",
  note="At-home ketamine therapy (founder Dylan Beynon, 2018; Wikipedia), New York, where it opened its clinic; the "
       "firm's page dates KP to 2021 (Early, an anchor only) and no source names the round. 8VC's Seattle looks like "
       "the older Seattle health-app company of the same name (GeekWire, acquired 2014), a name collision.")
C("mashgin", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified",
  val_cite="https://www.prnewswire.com/news-releases/mashgin-raises-62-5m-series-b-funding-at-a-1-5-billion-valuation-led-by-nea-301542339.html",
  asof="2022-05-09", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
  country="US", city="Palo Alto", stage="undetermined", rounds=[], focus="AI & Applied AI",
  note="Computer-vision self-checkout, Palo Alto. On the firm's company pages 2017-18; the round Kleiner Perkins "
       "entered is not on record. Last priced mark: the $62.5M Series B at $1.5B led by NEA (2022-05-09), older than "
       "24 months, as NEA and YC record.")
C("mason-finance", status="unknown", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Fintech & Payments", flags=["city_unknown"],
  note="On the firm's consumer logo grid 2018-19 (masonfinance.com, which no longer serves content). No round, city or "
       "fate was established.")
C("noteworth", status="private", rng="below_1b", country="US", stage="undetermined", rounds=[],
  focus="Healthcare & Bio", flags=["city_unknown"],
  note="Remote patient monitoring (legal name Data Minded Solutions, the firm's 2017-18 page). PR Newswire reported a "
       "$5M round in July 2020 and a hospital partnership followed in 2021, so it is read private at last report; the "
       "round Kleiner Perkins entered and the city are not established.")

jl.write("j08b", L)
