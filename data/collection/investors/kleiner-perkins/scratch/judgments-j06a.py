"""Judge j06, batch 11 (PRO-99 Kleiner Perkins). Run: NQ_TAG=j06 python3 judgments-j06a.py"""
import judge_lib as jl
from judge_lib import cls, verdict, rnd, SITE, ARCH, POST, W, FTS

L = []
TODAY = "2026-09-30"

# ---- membership traps (verdict line only)
L.append(verdict("alcatel", "not_member",
    "Sale consideration: the firm's investment was TiMetra Networks, which Alcatel bought in 2003; the archived page "
    "lists the acquirer (status Merged), not a company a Kleiner Perkins fund backed (Erik 2026-09-22 sale-consideration rule).",
    ec="site_listing", conf="high"))
for s, n in (("alibaba", "Alibaba"), ("baidu", "Baidu")):
    L.append(verdict(s, "not_member",
        f"partner-carried: Tina Ju's TDF Capital deal before KPCB China (Erik 2026-09-17 partner-carried rule; "
        f"decisions.md X1); no KPCB China fund round in {n} is documented.", ec="site_listing", conf="high"))

# ---- classification lines
L.append(cls("adknowledge", status="acquired", rng="below_1b", country="US", city="Palo Alto",
    stage="undetermined", entry_date="1997", rounds=[], focus="Media, Gaming & Advertising",
    note="AdKnowledge, online ad management (Palo Alto), backed by the firm in 1997 and bought by CMGI (the firm's own "
         "exit field). No source names the firm's round. The TCV row 'Adknowledge' is the later Kansas City company "
         "(v2 Ventures Group) TCV entered in 2010, a different company with the same name, so it is not aligned."))

L.append(cls("aesthera", status="acquired", rng="below_1b", country="US", city="Pleasanton",
    stage="undetermined", focus="Healthcare & Bio",
    note="AesThera, light-based aesthetic devices, Pleasanton CA; the firm's archived pages read Acquired from 2012 "
         "(merged into Solta Medical, the merger agreement ruling R2 cites). Entry round not researched beyond the "
         "firm's pages; stage undetermined."))

L.append(cls("affectiva", status="acquired", rng="below_1b", city="Boston",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2012/08/07/the-new-face-of-ad-tech-goes-consumer-emotion-tracker-affectiva-takes-12m-from-kpcb-horizon-ventures-others/",
    entry_date="2012-08-07", focus="AI & Applied AI",
    rounds=[rnd("2012-08-07", "Series C", 12000000, "Horizons Ventures; KPCB Digital Growth Fund", True,
                "https://techcrunch.com/2012/08/07/the-new-face-of-ad-tech-goes-consumer-emotion-tracker-affectiva-takes-12m-from-kpcb-horizon-ventures-others/", "press"),
            rnd("2021-05", "Acquisition by Smart Eye", 73500000, None, None, W("Affectiva"), "press")],
    note="Emotion-recognition AI spun out of the MIT Media Lab, Boston. The KPCB Digital Growth Fund co-led the $12M "
         "Series C with Horizons Ventures (TechCrunch 2012-08-07), a Digital Growth Fund position and so IN under D2. "
         "Acquired by Smart Eye for about $73.5M, mostly stock, in May 2021 (Wikipedia)."))

for s, dup in (("ag-mi-systems", "agami"), ("agami", "ag-mi-systems")):
    L.append(cls(s, status="defunct", rng="below_1b", country="US", city="Sunnyvale",
        stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=W("Agámi Systems"),
        entry_date="2003", focus="Data Infrastructure",
        rounds=[rnd("2003", "first venture round (Series A)", 5500000, None, True, W("Agámi Systems"), "press"),
                rnd("2004-09", "second round", 25000000, None, None, W("Agámi Systems"), "press"),
                rnd("2008-02", "third round (announced, existing investors)", 45000000, None, None, W("Agámi Systems"), "press")],
        note=f"Agámi Systems, network storage, Sunnyvale. Its first venture round of about $5.5M included Kleiner Perkins "
             f"with Vinod Khosla on the board (Wikipedia), a seat from his KP years (before Khosla Ventures, 2004); the "
             f"round preceded the $25M second round of September 2004, so the entry reads Series A and is dated 2003 "
             f"(founded April 2003). It shut down on 2008-07-28; the former CEO later bought the assets for a new company, "
             f"not a going-concern sale, so defunct. Same company as the row '{dup}' (one base company carried twice)."))

L.append(cls("agnion", status="acquired", rng="below_1b", country="DE", country_src="web_verified",
    country_cite="https://www.presseportal.de/pm/108587/2481582", city="Pfaffenhofen an der Ilm", city_src="web_verified",
    stage="undetermined", entry_date="2007", focus="Climate & Energy",
    rounds=[rnd("2007", "founding round", None, None, True,
                "https://evt.tf.fau.de/forschung/forschungsschwerpunkte/verbrennung_vergasung/heatpipe-reformer", "press"),
            rnd("2013-05", "sale of all shares to ENTRADE", None, None, None, "https://www.presseportal.de/pm/108587/2481582", "company")],
    note="agnion, biomass Heatpipe-Reformer, Pfaffenhofen an der Ilm (Bavaria). Founded in 2007 by Prof. Karl with "
         "Munich Venture Partners and Kleiner Perkins as investors (FAU chair page); the round has no series label, so "
         "the stage is undetermined. The operating company filed for insolvency in January 2013 and the ENTRADE group "
         "bought all shares of agnion Energy Inc. from the venture investors in May 2013 (press release), so acquired."))

L.append(cls("agrivida", status="private", rng="below_1b", country="US", city="Woburn",
    stage="undetermined", focus="Climate & Energy",
    note="Agrivida, engineered crops and feed enzymes (Woburn MA), Greentech team, John Denniston. Last known operating "
         "(low confidence); the firm's round was not researched beyond its archived pages, so undetermined."))

L.append(cls("airware", rng="below_1b", city="San Francisco",
    stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://agfundernews.com/drone-company-airware-raises-25-million-series-b",
    entry_date="2014-07-24", focus="Industrial & Robotics",
    rounds=[rnd("2013-05-15", "Series A", 10700000, "Andreessen Horowitz", False,
                "https://techcrunch.com/2013/05/15/airware-raises-10-7m-to-build-brains-for-unmanned-drones/", "press"),
            rnd("2014-07-24", "Series B", 25000000, "Kleiner Perkins Caufield & Byers", True,
                "https://agfundernews.com/drone-company-airware-raises-25-million-series-b", "press"),
            rnd("2016-03", "Series C", 30000000, "Next World Capital", True, W("Airware"), "press")],
    note="Commercial drone platform, San Francisco. Kleiner Perkins led the $25M Series B (AgFunderNews 2014-07-24, "
         "Mike Abbott), its first round; it followed on in the 2016 Series C. Shut in September 2018 with the assets "
         "sold to Delair, so the prefilled acquired stands (asset-sale rule), as the a16z, Felicis and GV rows read."))

L.append(cls("akimbo", status="defunct", rng="below_1b", country="US", city="San Mateo",
    stage="undetermined", focus="Media, Gaming & Advertising",
    note="Akimbo Systems, video-on-demand set-top service, San Mateo (Wikipedia, 'Akimbo'). It went out of business on "
         "2008-06-02. No source names the firm's round (William Hearst III's deal)."))

L.append(cls("aleees", status="public", rng="below_1b", country="TW", country_src="web_verified",
    country_cite=ARCH("aleees"), city="Taoyuan", stage="undetermined", focus="Climate & Energy",
    flags=["kpcb_china"],
    note="Advanced Lithium Electrochemistry (Aleees), LFP battery materials, Taiwan (the firm's China listing gives "
         "'Taiwan'). Listed on the Taipei Exchange (5227): market cap TWD 2.14B on 2026-09-30 "
         "(https://stockanalysis.com/quote/tpex/5227/market-cap/), about $67M, far below $1B. A KPCB China position "
         "(Tina Ju), provisional IN under X1. The fund's round is not documented."))

L.append(cls("align-commerce", status="private", rng="below_1b", city="San Francisco",
    stage="undetermined", focus="Fintech & Payments",
    rounds=[rnd("2017-03-08", "growth round (unlabelled)", 24000000, "NAB Ventures", True,
                "https://techcrunch.com/2017/03/08/align-commerce-veem-24-million/", "press")],
    note="Align Commerce renamed itself Veem (San Francisco cross-border B2B payments; Wikipedia, 'Veem'). Kleiner "
         "Perkins was already an investor when NAB Ventures led the $24M round of March 2017 (TechCrunch); the round "
         "it entered is not named, so undetermined. Momentum check 2026-09-30 (TechCrunch's own search for Veem): no "
         "$1B+ priced round, so below_1b."))

L.append(cls("alphavax", status="unknown", rng="below_1b", country="US", city="Durham",
    stage="undetermined", focus="Healthcare & Bio",
    note="AlphaVax, alphavirus-replicon vaccines, Research Triangle Park NC (Durham). No Wikipedia article; the company's "
         "state after 2012 and the firm's round were not established."))

L.append(cls("alta-devices", status="acquired", rng="below_1b", country="US", city="Sunnyvale",
    stage="undetermined", focus="Climate & Energy",
    note="Alta Devices, thin-film GaAs solar, Sunnyvale (Bill Joy, Wen Hsieh). Bought by Hanergy in 2013 and shut in "
         "2019 (Wikipedia, 'Alta Devices'); acquired, as the NEA row reads. The firm's round is not named on record."))

L.append(cls("altarock-energy-inc", status="acquired", rng="below_1b", country="US", city="Seattle",
    stage="undetermined", focus="Climate & Energy",
    note="AltaRock Energy, enhanced geothermal, Seattle (Joe Lacob). Acquired by Ormat Technologies in 2025 (Wikipedia, "
         f"'AltaRock Energy', {W('AltaRock Energy')}); the Khosla row still reads unknown, and this cited sale is the "
         "fresher evidence. The firm's round is not cited here, so undetermined."))

L.append(cls("american-superconductor-corporation", status="public", rng="1b_plus", usd=1410000000,
    val_src="web_verified", val_cite="https://stockanalysis.com/stocks/amsc/market-cap/", asof=TODAY,
    extra={"valuation_range_source": "web_verified"}, country="US", city="Ayer",
    stage="undetermined", entry_date="1987", focus="Climate & Energy",
    note="AMSC, superconductor wire, power electronics and wind systems, Ayer MA (Wikipedia). The firm's 1987 entry "
         "matches the founding year; no source names the round. Market cap $1.41B on 2026-09-30 (stockanalysis)."))

L.append(cls("angellist", status="private", rng="1b_plus", usd=4100000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2022/03/12/angellist-tiger-global-money/", asof="2022-03-12",
    extra={"valuation_range_source": "web_verified"}, flags=["stale"], country="US", city="San Francisco",
    stage="Series A", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://techcrunch.com/2013/09/23/angellist/", entry_date="2013-09", focus="Fintech & Payments",
    rounds=[rnd("2013-09", "$24M round (Series A by the record's later naming)", 24000000, "Google Ventures; Atlas Venture", True,
                "https://techcrunch.com/2013/09/23/angellist/", "press"),
            rnd("2022-03", "Series B", 100000000, "Tiger Global; Accomplice", None,
                "https://techcrunch.com/2022/03/12/angellist-tiger-global-money/", "press")],
    note="AngelList, San Francisco. Kleiner Perkins is named among the investors in the $24M round of 2013 (TechCrunch "
         "2013-09-23); the record calls the 2022 round the Series B (Wikipedia), which makes 2013 the Series A (medium, "
         "as the GV row reads). Mark: $4.1B on the $100M round of March 2022 (TechCrunch), stale."))

L.append(cls("anthropic", city="San Francisco", stage="undetermined", entry_date="2025", focus="AI & Applied AI",
    rounds=[rnd("2025-03-03", "Series E", 3500000000, "Lightspeed Venture Partners", False,
                "https://www.anthropic.com/news/anthropic-raises-series-e-at-usd61-5b-post-money-valuation", "company"),
            rnd("2025-09-02", "Series F", 13000000000, "ICONIQ; Fidelity; Lightspeed", False,
                "https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation", "company"),
            rnd("2026-05-28", "Series H", 65000000000, "Altimeter; Dragoneer; Greenoaks; Sequoia", False,
                "https://www.anthropic.com/news/series-h", "company")],
    note="The firm's page dates its Anthropic investment to 2025 (Growth). Anthropic's own announcements of the Series "
         "E, F and H name no Kleiner Perkins, so the round the firm entered (a 2025 primary it is not named in, or a "
         "secondary) is not established: undetermined. The $965B mark is carried by the deterministic layer."))

L.append(cls("anza-therapeutics", status="acquired", rng="below_1b", country="US", city="Concord",
    stage="undetermined", focus="Healthcare & Bio",
    note="Anza Therapeutics, Listeria-based immunotherapies spun out of Cerus in 2007, Concord CA. It closed in 2009 and "
         "its platform went to Aduro BioTech (medium confidence), so acquired with a successor note. The firm's round "
         "is not documented."))

L.append(cls("aoptix", status="unknown", rng="below_1b", country="US", city="Campbell",
    stage="undetermined", focus="Data Infrastructure",
    note="AOptix Technologies, adaptive-optics laser communications and iris biometrics, Campbell CA (the firm's 2008 "
         "listing). No Wikipedia article; its state after the mid-2010s was not established (Kevin Compton's deal)."))

L.append(cls("apcera", status="acquired", rng="below_1b", country=None, city="San Francisco",
    stage="undetermined", focus="Data Infrastructure",
    rounds=[rnd("2014-09", "majority stake by Ericsson", None, "Ericsson", None, W("Apcera"), "press")],
    note="Apcera, container management platform, founded 2012 in San Francisco (Wikipedia). Ericsson took a majority "
         "stake in September 2014 and later wound it down, so acquired, as the a16z row reads. TechCrunch's own search "
         "shows no round naming Kleiner Perkins (Mike Abbott's deal), so undetermined."))

L.append(cls("apnicure", status="unknown", rng="below_1b", country="US", city="Redwood City",
    stage="undetermined", focus="Healthcare & Bio",
    note="ApniCure (Winx sleep-apnea therapy), Redwood City CA (Dana Mead, Lawrence Leisure). Its state after the "
         "firm's 2018 pages was not established."))

L.append(cls("app-orbit", status="unknown", rng="below_1b", country="US", flags=["city_unknown"],
    stage="undetermined", focus="Data Infrastructure",
    note="App Orbit (appOrbit), enterprise application modernisation across clouds, on the firm's 2017-19 enterprise "
         "list. TechCrunch's own search returned nothing on it; city, state and round not established."))

L.append(cls("apperian", status="acquired", rng="below_1b", city="Boston",
    stage="undetermined", focus="SaaS",
    rounds=[rnd("2011-03-29", "$9.5M round (unlabelled)", 9500000, None, True,
                "https://techcrunch.com/2011/03/29/apperian-raises-9-5m-for-enterprise-mobile-app-deployment-platform/", "press"),
            rnd("2012-03", "$12.4M round from existing investors", 12400000, None, True, W("Apperian"), "press"),
            rnd("2015-09-09", "$12M round", 12000000, None, None,
                "https://techcrunch.com/2015/09/09/apperian-snares-12m-as-mobile-applications-management-catches-on/", "press")],
    note="Apperian, mobile application management, Boston (Wikipedia). The KPCB iFund joined the $9.5M round of March "
         "2011 (TechCrunch), which carries no series label and may follow an earlier round, so undetermined. Acquired "
         "by Arxan Technologies in January 2017."))

L.append(cls("applied-compute", status="private", rng="1b_plus", usd=1300000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2026/07/05/almost-40-new-unicorns-have-been-minted-so-far-this-year-here-they-are/",
    asof="2026-04", extra={"valuation_range_source": "web_verified"}, country="US", city="San Francisco",
    stage="Growth", stage_src="first_party", stage_conf="high", stage_cite=POST("applied-compute"),
    entry_date="2026-04", focus="AI & Applied AI",
    rounds=[rnd("2026-04", "Series B", 80000000, "Kleiner Perkins", True, POST("applied-compute"), "firm")],
    note="Applied Compute, custom enterprise models and agents, San Francisco. The firm's post (2026-05-14) partners "
         "with the team 'for their Series B', and its page dates the investment to 2026, so the entry is the Series B. "
         "Momentum check 2026-09-30: TechCrunch's 2026 unicorn list gives $1.3B in April 2026 on the $80M round led by "
         "Kleiner Perkins."))

L.append(cls("applied-materials", status="public", rng="100b_plus", usd=405830000000, val_src="web_verified",
    val_cite="https://stockanalysis.com/stocks/amat/market-cap/", asof=TODAY,
    extra={"valuation_range_source": "web_verified"}, city="Santa Clara",
    stage="undetermined", focus="Industrial & Robotics",
    note="Applied Materials, semiconductor equipment, Santa Clara; market cap $405.83B on 2026-09-30 (stockanalysis). "
         "It appears only on the 2021-24 logo grid; the company listed in 1972 and no private Kleiner Perkins round is "
         "on record, so the entry is undetermined and the listing itself is worth a second look (T3)."))

L.append(cls("applied-minds", status="private", rng="below_1b", city="Burbank", stage="undetermined",
    focus="Industrial & Robotics",
    note="Applied Minds, the Hillis and Ferren technology studio, headquartered in Burbank CA (Wikipedia, 'Applied "
         f"Minds', {W('Applied Minds')}); the firm's 2008 listing placed it in Glendale. No round is on record."))

L.append(cls("aptwater", status="unknown", rng="below_1b", country="US", city="Pleasant Hill",
    stage="undetermined", focus="Climate & Energy",
    note="APTwater, advanced water treatment, Pleasant Hill CA (low confidence), Greentech team. State after 2013 and the "
         "firm's round were not established."))

L.append(cls("ariba-inc", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined", focus="SaaS",
    note="Ariba, procurement software, Sunnyvale; bought by SAP in 2012. No round naming the firm is on record, as in "
         "the Benchmark and TCV rows."))

L.append(cls("armadin", status="private", rng="below_1b", city="San Francisco",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.prnewswire.com/news-releases/armadin-secures-record-breaking-189-9m-in-seed-and-series-a-funding-to-combat-the-era-of-ai-driven-hyperattacks-302709318.html",
    entry_date="2026-03-10", focus="Security",
    rounds=[rnd("2026-03-10", "Seed and Series A (combined)", 189900000, "Accel", True,
                "https://www.prnewswire.com/news-releases/armadin-secures-record-breaking-189-9m-in-seed-and-series-a-funding-to-combat-the-era-of-ai-driven-hyperattacks-302709318.html", "company")],
    note="Armadin, autonomous AI offensive security (Kevin Mandia), dateline San Francisco. The $189.9M 'Seed and Series "
         "A' was led by Accel with Kleiner Perkins participating and 'follow-on investment from 8VC and Ballistic', so "
         "the new investors entered at the Series A (company release 2026-03-10). No valuation disclosed: below_1b, as "
         "the siblings read; Accel's Menlo Park city differs from the dateline and the GV and Menlo rows."))

L.append(cls("arrail-dental", status="public", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("arrail-dental"), city="Beijing", stage="undetermined", focus="Healthcare & Bio",
    flags=["kpcb_china"],
    note="Arrail Group, dental clinics, Beijing (the firm's China listing). Listed in Hong Kong (6639) in 2022; market cap "
         "HKD 1.03B on 2026-09-30 (https://stockanalysis.com/quote/hkg/6639/market-cap/), about $131M "
         "(ECB 2026-09-30). A KPCB China position (Wei Zhou), provisional IN under X1; the fund's round is not named."))

L.append(cls("asia-forestry", status="unknown", rng="below_1b", country="CN", country_src="web_verified",
    country_cite=ARCH("asia-forestry"), flags=["kpcb_china", "city_unknown"], stage="undetermined",
    focus="Climate & Energy",
    note="Pine forestry and turpentine producer in China, a KPCB China position (Tina Ju), provisional IN under X1. The "
         "same description ran on the 2010 China listing as 'China Forestry (stealth company)', which places it only "
         "in Hainan province, so the two rows are one company and no city is established."))

L.append(cls("assured", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_conf="medium",
    val_cite="https://www.bloomberg.com/news/articles/2025-03-04/iconiq-kleiner-perkins-back-insurance-startup-assured-at-1-billion-valuation",
    asof="2025-03-04", extra={"valuation_range_source": "web_verified"}, country="US", flags=["city_unknown"],
    stage="undetermined", entry_date="2024", focus="Fintech & Payments",
    rounds=[rnd("2025-03-04", "equity round at about $1B (series not named)", None, "ICONIQ; Kleiner Perkins", True,
                "https://www.bloomberg.com/news/articles/2025-03-04/iconiq-kleiner-perkins-back-insurance-startup-assured-at-1-billion-valuation", "press")],
    note="Assured (assured.com), AI claims processing for insurers, founded 2019 by Justin Lewis-Weber and Theo Patt. "
         "Bloomberg's headline (2025-03-04, paywalled): 'Iconiq, Kleiner Perkins Back Insurance Startup Assured at $1 "
         "Billion Valuation'; the figure sits on the band edge. The round's series is not named, so the stage is "
         "undetermined. The First Round and ICONIQ rows describe a New York healthcare company (withassured.com, 2025 "
         "seed), a different company with the same name. Momentum check 2026-09-30 by web search."))

L.append(cls("athena-neurosciences", status="acquired", rng="below_1b", country="US", city="South San Francisco",
    stage="undetermined", focus="Healthcare & Bio",
    note="Athena Neurosciences, central nervous system drugs, South San Francisco; bought by Elan in 1996. The firm's "
         "round is not on record."))

L.append(cls("autograph", rng="below_1b", country="US", city="Los Angeles",
    flags=["model_disputes_source"], stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2022/01/19/tom-bradys-buzzy-celebrity-nft-startup-autograph-banks-170m-from-silicon-valleys-top-crypto-investors/",
    entry_date="2022-01-19", focus="Crypto & Web3",
    rounds=[rnd("2022-01-19", "Series B", 170000000, "Andreessen Horowitz; Kleiner Perkins (co-lead)", True,
                "https://techcrunch.com/2022/01/19/tom-bradys-buzzy-celebrity-nft-startup-autograph-banks-170m-from-silicon-valleys-top-crypto-investors/", "press")],
    note="Autograph, Tom Brady's NFT platform, Los Angeles. The Wikidata AU is a wrong join on a one-word name: the "
         "company is US-based (the a16z row reads LA, US). Kleiner Perkins co-led the $170M Series B (TechCrunch "
         "2022-01-19), the year it first appears on the firm's grid. Merged into Future in January 2025, so acquired."))

L.append(cls("autonavi", rng="below_1b", country="CN", country_src="web_verified", country_cite=FTS("AutoNavi", "F-1"),
    city="Beijing", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FTS("AutoNavi", "F-1"),
    entry_date="2006-10-12", focus="Consumer & Marketplaces",
    rounds=[rnd("2006-10-12", "Series A", 40000000, None, True, FTS("AutoNavi", "F-1"), "filing")],
    note="AutoNavi, digital maps and navigation, Beijing. Its F-1 (2010) lists 6,527,520 Series A preferred shares held "
         "by Kleiner Perkins Caufield & Byers XII and KPCB XII Founders Fund, from the $40M Series A issued on "
         "2006-10-12 (the firm's main fund, not KPCB China, so no X1 flag). IPO 2010; bought by Alibaba in 2014."))

L.append(cls("avo", status="unknown", rng="below_1b", country="US", city="New York", stage="undetermined",
    focus="Consumer & Marketplaces",
    rounds=[rnd("2021-09-29", "Series B", 45000000, "Insight Partners", True,
                "https://www.prnewswire.com/news-releases/avo-announces-over-80m-in-funding-to-accelerate-ambitious-growth-plans-in-the-delivery--amenity-business-301387512.html", "company")],
    note="AVO, residential and office delivery and amenity platform, founded in Tel Aviv, based in New York and Israel. "
         "Kleiner Perkins was an existing investor in the $45M Series B led by Insight (company release 2021-09-29), so "
         "it entered earlier in a round not named on record. State unknown, as the Insight row reads."))

L.append(cls("avoca", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2026/07/05/almost-40-new-unicorns-have-been-minted-so-far-this-year-here-they-are/",
    asof="2026-04", extra={"valuation_range_source": "web_verified"}, country="US", city="New York",
    stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=POST("avoca"),
    entry_date="2026", focus="AI & Applied AI",
    rounds=[rnd("2026", "Series A", None, "Kleiner Perkins", True, POST("avoca"), "firm"),
            rnd("2026-04", "Series B", 125000000, "General Catalyst; Meritech Capital",  None,
                "https://techcrunch.com/2026/07/05/almost-40-new-unicorns-have-been-minted-so-far-this-year-here-they-are/", "press")],
    note="Avoca, AI agents for home-service businesses. The firm's post (2026-04-27): 'We led Avoca's Series A'; the "
         "company emerged from stealth with its Seed, A and B, and the firm's page dates the investment to 2026. "
         "Momentum check 2026-09-30: TechCrunch's unicorn list gives $1B (April 2026) on the $125M Series B led by "
         "General Catalyst and Meritech; the figure sits on the band edge."))

L.append(cls("ayasdi", status="acquired", rng="below_1b", city="Menlo Park",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015-03", focus="AI & Applied AI",
    rounds=[rnd("2013-01-16", "Series A", 10000000, "Khosla Ventures; Floodgate", False,
                "https://techcrunch.com/2013/01/16/darpa-backed-ayasdi-launches-with-10m-from-khosla-floodgate-to-uncover-the-hidden-value-in-big-data/", "press"),
            rnd("2013-07-16", "Series B", 30600000, "Institutional Venture Partners", False,
                "https://techcrunch.com/2013/07/16/ayasdi-lands-30-6m-to-help-g-e-citi-the-u-s-government-and-more-find-needles-in-big-datas-haystack/", "press"),
            rnd("2015-03", "Series C", 55000000, "Kleiner Perkins Caufield & Byers", True, None, "press")],
    note="Ayasdi, topological data analysis, Menlo Park. TechCrunch's Series A and B reports (2013) name no Kleiner "
         "Perkins; the firm led the $55M Series C of March 2015 (model, medium: not cited here), so Growth. Acquired "
         "by SymphonyAI in 2019."))

L.append(cls("balerion", status="private", rng="below_1b", country="US", flags=["city_unknown"],
    stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://pulse2.com/balerion-ai-6-million-seed-raised-to-transform-mortgage-origination-with-agentic-ai/",
    entry_date="2026-04-17", grad="censored", focus="Fintech & Payments",
    rounds=[rnd("2026-04-17", "Seed", 6000000, "Kleiner Perkins", True,
                "https://pulse2.com/balerion-ai-6-million-seed-raised-to-transform-mortgage-origination-with-agentic-ai/", "press")],
    note="Balerion AI, agentic AI for mortgage loan origination, founded by a UC Berkeley team. Kleiner Perkins led the "
         "$6M seed with Formation and BoxGroup (Pulse 2.0, 2026-04-17). Censored: the entry is inside the 24-month "
         "window. Momentum check 2026-09-30 by web search: only the seed is reported. The company's own pages give "
         "no city."))

L.append(cls("bekon", status="acquired", rng="below_1b", country="DE", country_src="web_verified",
    country_cite="https://www.eggersmann-recyclingtechnology.com/recyclinganlagen/trockenfermentation/",
    city="Harsewinkel", city_src="web_verified", stage="undetermined", focus="Climate & Energy",
    note="BEKON, dry-fermentation biogas plants, a KPCB Green Growth Fund position (IN under D1). Now BEKON GmbH within "
         "the Eggersmann Group at Harsewinkel, Germany (bekon.eu redirects to Eggersmann's page), so acquired. The "
         "fund's round is not on record."))

jl.write("j06a", L)
