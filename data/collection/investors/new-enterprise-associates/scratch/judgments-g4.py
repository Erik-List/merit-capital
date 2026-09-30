"""Delta pass g4 (PRO-100 NEA): queue batch 4, 18 items. Two graduation-pass rows (Popdust, Quick Hit), nine recall
additions (membership plus full classification) and seven 1990s filing rows needing status, country, city and band.
Every citation below was read in this pass (SEC documents through secget.py, web pages through a fetch) or is a
headline the helpers read from disk. Run with NQ_TAG=g4."""
import judge_lib as jl
from judge_lib import cls, rnd, verdict

WV = "web_verified"
VRS = {"valuation_range_source": WV}
ASOF = "2026-09-30"

# ---- citations (read in this pass)
TC_QUAD = "https://techcrunch.com/2013/02/18/with-11m-from-nea-comcast-others-quad-learning-wants-to-create-a-more-affordable-track-to-top-tier-degrees/"
IHE_QUAD = jl.NEWS("quad-learning-american-honors", "Quad Learning attempted and failed")
W_QUAD = jl.W("Quad Learning, Inc.")
HYPEBOT_ROYAL = jl.NEWS("royal-music-nft-marketplace", "Music NFT marketplace Royal raises")
COINDESK_ROYAL = jl.NEWS("royal-music-nft-marketplace", "3LAU Raises $16M to Tokenize")
W_ROYAL = jl.W("Royal.io")
W_SCALIX = jl.W("Scalix")
CB_SCALIX = "https://www.crunchbase.com/organization/scalix"  # vendor, listed in rounds only, never cited
SEKAI_PR = jl.GNEWS("sekai", "Sekai Raises $26M in Seed and Series A")
SPIRE_GB = jl.NEWS("spire-animation-studios", "Epic Games joins Spire Animation")
SPIRE_2020 = jl.GNEWS("spire-animation-studios", "CAA And VC Firm New Enterprise Associates Form Connect Ventures")
SPIRE_TEMASEK = jl.GNEWS("spire-animation-studios", "Spire Animation Studios raises round from Temasek")
SPORTSPRO_TMRW = "https://www.sportspro.com/news/tmrw-sports-series-a-investment-round-funding-tgl-golf-dynasty-equity-connect-ventures/"
THR_TMRW = jl.GNEWS("tmrw-sports", "Scores Investments From CAA")
UPTAKE_BI = "https://finance.yahoo.com/news/meet-uptake-technologies-startup-run-162634016.html"
UPTAKE_D = jl.GNEWS("uptake", "Uptake Raises $117m Series D")
W_UPTAKE = jl.W("Uptake (business)")
VELA_13D = "https://www.sec.gov/Archives/edgar/data/713275/000101297506000430/0001012975-06-000430.txt"
PHARMOS_PROXY = "https://www.sec.gov/Archives/edgar/data/713275/000116923206003958/d69507_def14a.htm"
VUZE_TC = "https://techcrunch.com/2007/12/18/vuze-raises-20m-more-in-series-c-brings-aboard-tivo-co-founder-ramsay/"

CONNECT = ("Connect Ventures is IN under decisions.md's Connect Ventures re-derivation (T1): NEA's own Form ADV lists "
           "Connect Ventures I, L.P. among the private funds its adviser advises.")

L = []

# ======================================================================================================
# 1. Graduation pass
# ======================================================================================================


def fix_popdust(lines):
    out = []
    for s in lines:
        if s.startswith("googlenews:"):
            s = ("googlenews: Google News, the company's name with round and exit words -> 26 headlines, every one an "
                 "article Popdust itself published (music and culture pieces, some about other companies' rounds, such "
                 "as Vydia's $7M Series A in 2018); none reports a round, sale or shutdown of Popdust")
        out.append(s)
    return out


POP_SURF = fix_popdust(jl.GRADLINES(
    "popdust-inc", name="Popdust",
    firm_note="NEA's own posts, live list and archived listings -> none names Popdust; the row rests on the May 2012 "
              "Form D naming NEA's Hugh Panero and Tony Florence",
    extra=["sibling:project-a-ventures: its row for Popdust -> no later round; its note reads the same 2012 Form D "
           "($4.5M, eight investors) as the only round and the company still publishing under Popdust, Inc."]))
L.append(cls("popdust-inc", entry_date="2012-05-25", grad="not_graduated", grad_src="formd",
             grad_cite=jl.FORMD_CITE("popdust-inc", 0), grad_conf="high", grad_asof=ASOF, surfaces=POP_SURF,
             note="S2A: not graduated; the Form D layer finds one filing, the $4.5M May 2012 seed, and nothing after it, "
                  "and the absence test found no later round either (surfaces listed; the Project A row agrees)."))

QH_SURF = jl.GRADLINES(
    "quick-hit-inc", name="Quick Hit",
    firm_note="NEA's own posts, live list and archived listings -> none names Quick Hit; the row rests on the 2010-11 "
              "Form D filings naming NEA's Harry Weller",
    extra=["exit: Majesco's purchase of Quick Hit (Capsule Computers, 2011-06-12) -> the company was sold eight months "
           "after the seed, so no later round could follow"])
L.append(cls("quick-hit-inc", entry_date="2010-10-06", grad="not_graduated", grad_src="formd",
             grad_cite=jl.FORMD_CITE("quick-hit-inc", 0), grad_conf="high", grad_asof=ASOF, surfaces=QH_SURF,
             note="S2A: not graduated; the $2.47M October 2010 seed and a $750K extension in March 2011 (under twice the "
                  "entry) were the last rounds before Majesco bought Quick Hit in June 2011, as the Form D layer reads."))

# ======================================================================================================
# 2. Recall additions: membership plus full classification
# ======================================================================================================

# ---- Quad Learning (American Honors)
L.append(verdict("quad-learning-american-honors", "member",
    "TechCrunch (2013-02-18): Quad Learning 'has raised more than $11 million in seed and series A financing from New "
    "Atlantic Ventures, Swan and Legend Fund, NEA, Comcast Ventures and others'; the Washington Business Journal "
    "headline of the same week names New Enterprise Associates and Comcast Ventures as the launch investors. A round "
    "naming NEA, so fund money (D2).",
    ec="web", conf="high", cite=TC_QUAD))
L.append(cls("quad-learning-american-honors", status="acquired", rng="below_1b", stage="undetermined",
             entry_date="2013-02", country="US", city="Washington", city_src=WV, focus="Consumer & Marketplaces",
             rounds=[rnd("2013-02-18", "Seed and Series A (announced together)", 11000000, None, True, TC_QUAD, "press"),
                     rnd("2014-04", "Series B", 10000000, None, None, W_QUAD, "press")],
             note="Washington, D.C. community-college honors and transfer programmes (TechCrunch). NEA came in with the "
                  "$11M seed and Series A announced together in February 2013, and no source says which half NEA "
                  "bought, so the stage is undetermined (were it the seed, the April 2014 Series B would graduate it). "
                  "Status: Inside Higher Ed (2019-05-22) reports American Honors was sold to Wellspring International "
                  "Education in 2018 in a distress sale worth a small fraction of what Quad raised; Wikipedia dates the "
                  "sale November 2018."))

# ---- Royal (music NFT marketplace)
L.append(verdict("royal-music-nft-marketplace", "member",
    "Hypebot (2021-11-23): Royal's $55M Series A 'was led by Andreessen Horowitz's a16z Crypto fund with participation "
    "from ... CAA, NEA's Connect Ventures, ... Founders Fund and Paradigm'. " + CONNECT,
    ec="web", conf="high", cite=HYPEBOT_ROYAL))
L.append(cls("royal-music-nft-marketplace", status="private", rng="below_1b",
             stage="Series A", stage_src=WV, stage_conf="high", stage_cite=HYPEBOT_ROYAL, entry_date="2021-11",
             country="US", city="Austin", city_src=WV, focus="Crypto & Web3",
             rounds=[rnd("2021-08-26", "Seed", 16000000, "Paradigm and Founders Fund", False, COINDESK_ROYAL, "press"),
                     rnd("2021-11-23", "Series A", 55000000, "a16z crypto", True, HYPEBOT_ROYAL, "press")],
             note="Music-rights marketplace founded in 2021 by 3LAU and JD Ross, headquartered in Austin (Wikipedia). "
                  "Connect Ventures entered at the November 2021 Series A; CoinDesk's account of the August 2021 $16M "
                  "seed lists Paradigm, Founders Fund, Atomic and angels, not Connect. Status private, disagreeing with "
                  "the a16z row's defunct (its status came from a Wikidata join to a Swedish namesake): the song-drop "
                  "marketplace was sunset in 2024, but royal.io still presents a live product, 'Programmable Money for "
                  "Creators' (read 2026-09-30). Momentum check 2026-09-30 (Google News, the company's name with round "
                  "and exit words): no round after the Series A, which disclosed no valuation."))

# ---- Scalix
L.append(verdict("scalix", "member",
    "Scalix's own About page (captured 2003-06-21, quoted in the recall triage): 'Scalix is backed by leading Silicon "
    "Valley venture firms Mayfield and New Enterprise Associates'; Wikipedia: 'The company was funded by venture firms "
    "New Enterprise Associates (NEA), Mohr Davidow Ventures (MDV) and Mayfield Fund.' Named as a funding firm by the "
    "company itself (D2). Not on NEA's own list in any era.",
    ec="web", conf="high", cite=W_SCALIX))
L.append(cls("scalix", status="acquired", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium",
             entry_date="2003-06", country="US", city="San Mateo", focus="SaaS",
             rounds=[rnd("2003-06-04", "Series A", 13200000, None, True, CB_SCALIX, "vendor")],
             note="Linux email and groupware server built on HP's OpenMail code, founded in 2002 by Julie Hanna at "
                  "Mayfield, San Mateo. Stage from the model: Crunchbase's transcription (a vendor, listed not cited) "
                  "has a $13.2M Series A in June 2003 with Mayfield and NEA, which matches the company's own June 2003 "
                  "page naming exactly those two backers; Mohr Davidow came in later. Xandros bought Scalix in July 2007 "
                  "(Wikipedia), and resold it to Sebring Software in 2011."))

# ---- Sekai
L.append(verdict("sekai", "member",
    "The company's release (2026-06-03): 'The Series A of $20 million was co-led by Keith Rabois at Khosla Ventures "
    "and Nicole Quinn at Connect Ventures'; Pulse 2.0 (2026-06-02) also names New Enterprise Associates among the "
    "participants. " + CONNECT,
    ec="web", conf="high", cite=SEKAI_PR))
L.append(cls("sekai", status="private", rng="below_1b", stage="Series A", stage_src=WV, stage_conf="high",
             stage_cite=SEKAI_PR, entry_date="2026-06-03", country="US", city="Sunnyvale", city_src=WV,
             focus="AI & Applied AI",
             rounds=[rnd("2026-06-03", "Series A", 20000000, "Khosla Ventures and Connect Ventures", True, SEKAI_PR,
                         "company")],
             note="Social platform for AI-built mini apps. Connect Ventures co-led the $20M Series A of June 2026; the "
                  "release names the seed's lead (Mayfield) and its returning investors (a16z speedrun, A*, MVP) and not "
                  "Connect, so the Series A is the entry. City aligned with the a16z row (Sunnyvale, web verified); the "
                  "release carries a San Francisco dateline. Momentum check 2026-09-30 (Google News, valuation and "
                  "billion words): no $1B+ priced round; the Series A disclosed no valuation."))

# ---- Spire Animation Studios
L.append(verdict("spire-animation-studios", "member",
    "GamesBeat (2022-02-01): 'Epic is investing in Spire alongside existing investor Connect Ventures, an investment "
    "partnership formed by Creative Artists Agency (CAA) and New Enterprise Associates (NEA)'; Deadline's headline of "
    "2020-06-24 has CAA and NEA forming Connect Ventures and backing Spire, Connect's first investment. " + CONNECT,
    ec="web", conf="high", cite=SPIRE_GB))
L.append(cls("spire-animation-studios", status="private", rng="below_1b", stage="undetermined", entry_date="2020-06",
             country="US", city="Los Angeles", city_src=WV, focus="Media, Gaming & Advertising",
             rounds=[rnd("2020-06-24", "unnamed (Connect Ventures' first investment)", None, None, True, SPIRE_2020, "press"),
                     rnd("2022-02-01", "unnamed", 20000000, "Epic Games", True, SPIRE_GB, "press"),
                     rnd("2022-08-18", "unnamed (Temasek)", None, "Temasek", None, SPIRE_TEMASEK, "press")],
             note="Los Angeles animation studio making features with real-time game-engine tools (GamesBeat). Connect "
                  "Ventures backed it at formation in June 2020; no source names that round, and GamesBeat does not "
                  "name the $20M 2022 round either, so the stage is undetermined. Still operating: Asia Asset "
                  "Management reported a Temasek investment in March 2026."))

# ---- TMRW Sports
L.append(verdict("tmrw-sports", "member",
    "SportsPro (2024-06): Connect Ventures, 'an investment partnership between Creative Artists Agency (CAA) and "
    "venture capital firm New Enterprise Associates (NEA)', co-led TMRW's Series A with Dynasty Equity and 'also "
    "co-led the initial fundraising round for TMRW' (The Hollywood Reporter, 2022-11-02: 'TMRW Sports Scores "
    "Investments From CAA's Connect Ventures'). " + CONNECT,
    ec="web", conf="high", cite=SPORTSPRO_TMRW))
L.append(cls("tmrw-sports", status="private", rng="below_1b", stage="undetermined", entry_date="2022-11",
             country="US", city="Winter Park", focus="Media, Gaming & Advertising",
             rounds=[rnd("2022-11-02", "initial round (unnamed)", None, "Connect Ventures (co-lead)", True, THR_TMRW, "press"),
                     rnd("2024-06-24", "Series A", None, "Dynasty Equity and Connect Ventures", True, SPORTSPRO_TMRW,
                         "press")],
             note="Sports company of Tiger Woods, Rory McIlroy and Mike McCarley that runs the TGL golf league (founded "
                  "2022). Connect co-led the initial round of November 2022, which no source names, so the stage is "
                  "undetermined. The June 2024 Series A valued TMRW at about $500M (SportsPro); September 2026 reports "
                  "(Front Office Sports via Dallas Sports Journal) have a new round near $1B still in talks, not a "
                  "priced event. City from company-profile listings (Winter Park, Florida), inferred, not cited."))

# ---- Uptake
L.append(verdict("uptake", "member",
    "Wikipedia: the $45M round of 2015-10-27 was 'led by GreatPoint Ventures and existing investors including New "
    "Enterprise Associates and Caterpillar' (citing the New York Times); Business Insider via Yahoo Finance "
    "(2017-02-01): 'Uptake Technologies' other investments include ... Lightbank, New Enterprise Associates'. A round "
    "naming NEA, so fund money (D2). Not on NEA's own list in any era.",
    ec="web", conf="high", cite=UPTAKE_BI))
L.append(cls("uptake", rng="1b_plus", usd=2300000000, val_src=WV, val_cite=UPTAKE_D, asof="2017-12-01",
             stage="undetermined", city="Chicago", city_src=WV, focus="AI & Applied AI",
             flags=["stale"], clear=["unicorn_name_match"], extra=VRS,
             rounds=[rnd("2015-10-27", "unnamed ($45M)", 45000000, "GreatPoint Ventures", True, W_UPTAKE, "press"),
                     rnd("2017-02-01", "Series C", 40000000, "Revolution Growth", None, UPTAKE_BI, "press"),
                     rnd("2017-12-01", "Series D", 117000000, "Baillie Gifford", None, UPTAKE_D, "press")],
             note="Chicago industrial AI and predictive-maintenance company (founded 2014). Mark re-pinned to the $117M "
                  "Series D led by Baillie Gifford at $2.3B (AgFunderNews, 2017-12-01), stale; no newer priced round. "
                  "Bosch agreed to buy Uptake on 2026-03-19 (Bosch release, terms not disclosed, 'upon closing' "
                  "language) and no closing was found by 2026-09-30, so the row stays private. Stage undetermined: "
                  "Wikipedia calls NEA an existing investor at the October 2015 round, which puts NEA's entry at an "
                  "earlier 2015 round no source names, while a vendor dates NEA's first check to that October round "
                  "itself; the two readings differ (Series A or Growth)."))

# ---- Vela Pharmaceuticals
L.append(verdict("vela-pharmaceuticals", "member",
    "NEA's own Schedule 13D on Pharmos (2006): 'NEA 10 acquired 1,880,824 shares of Common Stock ... on October 25, "
    "2006 in exchange for 7,500,075 shares of Series D Convertible Preferred Stock ... of Vela Pharmaceuticals, Inc.' "
    "and notes convertible into Series D. An NEA fund held Vela privately before Pharmos bought it; Pharmos' 2006 "
    "proxy names New Enterprise Associates among Vela's three principal shareholders. The Pharmos stock is the sale "
    "consideration (D8), so the base row pharmos is the acquirer and Vela the member.",
    ec="fund_filing", conf="high", cite=VELA_13D))
L.append(cls("vela-pharmaceuticals", status="acquired", rng="below_1b",
             stage="Growth", stage_src=WV, stage_conf="high", stage_cite=VELA_13D, entry_date="2002",
             country="US", city="Ewing", city_src=WV, focus="Healthcare & Bio",
             rounds=[rnd("2002", "Series D", 24781407, None, True, PHARMOS_PROXY, "filing")],
             note="Brain-gut drug developer in Ewing, New Jersey (Pharmos proxy, 2006). Vela sold Series A and B in "
                  "1999-2000, Series C, and in 2002 a Series D ($24.8M of proceeds); at the end of 2005 7,500,075 Series "
                  "D shares were outstanding, exactly the number NEA 10 exchanged in the merger, and NEA's 13D names no "
                  "other series, so NEA entered at the Series D (Growth). Pharmos completed the purchase on 2006-10-25."))

# ---- Vuze
L.append(verdict("vuze", "member",
    "TechCrunch (2007-12-18): Vuze, 'previously known as Azureus, has raised $20M in a Series C round of funding led "
    "by New Enterprise Associates (NEA)', with Redpoint, Greycroft, BV Capital and Jarl Mohn as existing investors. A "
    "round NEA led, so fund money (D2).",
    ec="web", conf="high", cite=VUZE_TC))
L.append(cls("vuze", status="defunct", rng="below_1b", stage="Growth", stage_src=WV, stage_conf="high",
             stage_cite=VUZE_TC, entry_date="2007-12-18", country="US", city="Palo Alto",
             focus="Media, Gaming & Advertising",
             rounds=[rnd("2006", "Series A", 2000000, "BV Capital", False, VUZE_TC, "press"),
                     rnd("2006-12", "Series B", 12000000, "Redpoint Ventures", False, VUZE_TC, "press"),
                     rnd("2007-12-18", "Series C", 20000000, "New Enterprise Associates", True, VUZE_TC, "press")],
             note="Vuze, Inc. (formerly Azureus), the BitTorrent client and video platform. NEA was new at the $20M "
                  "Series C it led in December 2007 (TechCrunch lists the earlier A and B without NEA), so the entry is "
                  "Growth. Status and city aligned with the Headline and Redpoint rows (defunct, Palo Alto); Wikipedia's "
                  "Vuze article says Spigot acquired Vuze in December 2010 without a source, and its Vuze, Inc. article "
                  "places the company in San Mateo."))

# ======================================================================================================
# 3. Leftovers: the 1990s filing rows (status, country, city, band)
# ======================================================================================================

L.append(cls("opta-food-ingredients-inc-de", status="acquired", rng="below_1b", country="US", city="Bedford",
             city_src=WV, focus="Consumer & Marketplaces",
             note="Food-ingredient maker in Bedford, Massachusetts (its 8-K address). Stake Technology Ltd. (later "
                  "SunOpta) bought Opta through a $2.50-a-share tender offer: its subsidiary accepted about 10.1M "
                  "tendered shares on 2002-12-04 (Opta 8-K of 2002-12-09), and Opta deregistered that month."))

L.append(cls("penederm-inc", status="acquired", rng="below_1b", country="US", city="Foster City", city_src=WV,
             focus="Healthcare & Bio",
             note="Dermatology drug company in Foster City, California. Mylan Laboratories acquired Penederm by merger, "
                  "0.68 Mylan share per Penederm share, approved at the special meeting of 1998-10-02 (definitive proxy "
                  "of 1998-09-01); Penederm filed its Form 15 the same day."))

L.append(cls("platinum-software-corp", status="acquired", rng="below_1b", country="US", city="Irvine", city_src=WV,
             focus="SaaS",
             note="Platinum Software of Irvine, renamed Epicor Software in 1999 after buying DataWorks. Apax Partners "
                  "bought Epicor through a tender offer in April and May 2011 (Epicor deregistered on 2011-05-26). "
                  "Aligned with the IVP row (acquired, Irvine)."))

L.append(cls("premier-laser-systems-inc", status="defunct", rng="below_1b", country="US", city="Irvine",
             city_src=WV, focus="Healthcare & Bio",
             note="Dental and ophthalmic laser maker in Irvine, California. It suspended operations in March 2000, filed "
                  "Chapter 11, retained an adviser to liquidate all assets and sold the pieces separately (Topomax IP "
                  "to LaserSight, its Ophthalmic Imaging Systems stake to MediVision, the ophthalmic laser division to "
                  "SurgiLight); its Joint Plan of Liquidation took effect on 2001-10-09 (8-K). No buyer took the "
                  "business as a whole, so defunct. The later filings come from the estate representative's office in "
                  "Aliso Viejo."))

L.append(cls("sequana-therapeutics-inc", status="acquired", rng="below_1b", country="US", city="San Diego",
             city_src=WV, focus="Healthcare & Bio",
             note="Genomics drug-discovery company at North Torrey Pines Road, La Jolla (San Diego). It agreed on "
                  "1997-11-02 to merge with a subsidiary of Arris Pharmaceutical (8-K of 1997-11-12); its Form 15 of "
                  "1998-01-09 reports a single holder of record, and the combined company took the name Axys "
                  "Pharmaceuticals."))

L.append(cls("summit-medical-systems-inc-mn", status="acquired", rng="below_1b", country="US", city="Nashville",
             city_src=WV, focus="Healthcare & Bio",
             note="Summit Medical Systems of Minneapolis, renamed Celeris Corporation in 1999 and later based in "
                  "Nashville as a clinical research organisation. Shareholders were asked on 2002-06-26 to approve the "
                  "sale of substantially all of Celeris' assets to Statprobe, Inc. and a plan of liquidation (definitive "
                  "proxy of 2002-05-31); the record date for the dissolution payments followed in November 2002 and the "
                  "company deregistered in December. The business continued under Statprobe, so acquired; city is the "
                  "last known."))

L.append(cls("versicor-inc-ca", status="acquired", rng="below_1b", country="US", city="King of Prussia", city_src=WV,
             focus="Healthcare & Bio",
             note="Versicor, an anti-infective drug developer in Fremont, California, combined with Biosearch Italia in "
                  "2003 and took the name Vicuron Pharmaceuticals, based in King of Prussia, Pennsylvania (last known). "
                  "Pfizer bought Vicuron for $29.10 a share in cash (merger proxy of 2005-07-19); Vicuron deregistered "
                  "on 2005-09-14."))

jl.write("g4", L)
