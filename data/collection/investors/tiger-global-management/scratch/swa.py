#!/usr/bin/env python3
"""PRO-167 Tiger Global, class sweep (COLLECTION.md 8, duty 9) on the undetermined entry stages, chunk a:
the 12 rows where a page names the round Tiger entered and ties Tiger to it.
Evidence: one Bing News search per row (bq.py, NQ_TAG=sw), the rows' evidence view (show.py), pages the tools
printed (TechCrunch, Techcircle, LAVCA, PR Newswire, 36Kr, 163.com), the IPO prospectuses on EDGAR (MakeMyTrip,
TAL, Danke) and Scribe's own terms page.
Run: NQ_TAG=sw python3 swa.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls, rnd, NEWS

jl.WHO = "agent-review-pro167"
HERE = Path(__file__).resolve().parent
CLS = json.loads((HERE.parent / "companies" / "classification.json").read_text())


def OLD(slug, date=None, sub=None):
    """One funding_rounds entry already on the row, found by its date or a round-text substring."""
    m = [r for r in (CLS.get(slug, {}).get("funding_rounds") or [])
         if (date is None or r.get("date") == date) and (sub is None or sub.lower() in str(r.get("round")).lower())]
    if len(m) != 1:
        raise SystemExit(f"OLD({slug!r}, {date!r}, {sub!r}) matched {len(m)}")
    return m[0]


def SRC(slug, date):
    return OLD(slug, date)["source"]


# URLs printed by the tools run in this sweep (WebSearch results, EDGAR index listings), fetched and read.
TC_SCRIBE_A = "https://techcrunch.com/2021/10/18/scribe-launches-knowledge-capturing-software-that-gets-employees-on-the-same-page/"
TC_99_A = "https://techcrunch.com/2015/02/02/99taxis-raises-significant-new-cash-from-tiger-global/"
F1_MMYT = "https://www.sec.gov/Archives/edgar/data/1495153/000095012310068108/h04091fv1.htm"
F1_TAL = "https://www.sec.gov/Archives/edgar/data/1499620/000095012310090077/h04316fv1.htm"
LAVCA_KAVAK_E = "https://www.lavca.org/mexican-car-resale-marketplace-kavak-raises-usd700m-series-e/"
TC_KAVAK_D = "https://techcrunch.com/2021/04/07/mexican-unicorn-kavak-raises-a-485m-series-d-at-a-4b-valuation/"
PRN_GRUB_E = "https://www.prnewswire.com/news-releases/grubmarket-raises-200-million-series-e-to-accelerate-profitable-growth-and-ipo-readiness-301424632.html"
KR_MEICAI_E = "https://36kr.com/p/5112580.html"
N163_MEICAI = "https://m.163.com/dy/article/DTRF5RVK0518N443.html?spss=adap_pc"

L = []

# ---- Scribe: Tiger led the Series A of October 2021
TC_SCRIBE_C = SRC("scribe", "2025-11")
SCRIBE_ROUNDS = [
    rnd("2021", "Seed", 8000000, "Amplify Partners", False, TC_SCRIBE_A),
    rnd("2021-10-18", "Series A", 22000000, "Tiger Global Management", True, TC_SCRIBE_A),
    rnd("2025-11", "Series C", 75000000, "StepStone", True, TC_SCRIBE_C),
]
L.append(cls("scribe", stage="Series A", stage_src="web_verified", stage_cite=TC_SCRIBE_A, stage_conf="high",
             entry_date="2021-10-18", rounds=SCRIBE_ROUNDS,
             note="Class sweep 2026-09-29 (entry stage): Tiger Global led the $22M Series A of October 2021 "
                  "(TechCrunch, 2021-10-18: 'a new $22 million round of Series A funding that was led by Tiger "
                  "Global Management'). Amplify Partners (which led the $8M seed at the start of 2021), Haystack, "
                  "XYZ, AME Cloud, Morado and SEV joined it as existing investors; Tiger is not among them, so the "
                  "entry is the Series A. Redpoint's own row enters at the 2024 Series B, between this round and "
                  "the 2025 Series C. Colony Labs, Inc. is Scribe's legal name (scribehow.com/terms: 'Colony Labs, "
                  "Inc. dba Scribe'), so the row colony-labs is this company; it is flagged duplicate there."))

# ---- Colony Labs = Scribe (legal name); flag + note, stage as on scribe
L.append(cls("colony-labs", stage="Series A", stage_src="web_verified", stage_cite=TC_SCRIBE_A, stage_conf="high",
             entry_date="2021-10-18", city="San Francisco", city_src="web_verified", flags=["duplicate"],
             rounds=SCRIBE_ROUNDS[:2] + [OLD("colony-labs", "2025-11-10")],
             note="Class sweep 2026-09-29: Colony Labs, Inc. is the legal name of Scribe (scribehow.com/terms and "
                  "scribehow.com/privacy, read 2026-09-29: 'Copyright 2026 Colony Labs, Inc. dba Scribe'), and the "
                  "$75M of November 2025 from StepStone, Amplify, Redpoint, Tiger, Morado and New York Life is "
                  "Scribe's Series C. This row and scribe are one company: flagged duplicate for a merge into "
                  "scribe (the brand, carrying the $1.3B mark). Entry stage as on scribe: Tiger led the $22M "
                  "Series A of October 2021 (TechCrunch, which also calls the company San Francisco-based)."))

# ---- 99: TechCrunch names Tiger's early-2015 round the Series A
L.append(cls("99", stage="Series A", stage_src="web_verified", stage_cite=TC_99_A, stage_conf="high",
             entry_date="2015-02-02",
             rounds=[rnd("2015-02-02", "Series A", None, "Tiger Global Management", True, TC_99_A),
                     OLD("99", "2015-04"), OLD("99", "2017-01"), OLD("99", "2018-01")],
             note="Class sweep 2026-09-29: TechCrunch (2015-02-02) calls Tiger's early-2015 money 'The Series A "
                  "investment from Tiger Global', with the earlier backers Monashees and Qualcomm Ventures also "
                  "taking part, so the entry is the Series A of February 2015 (the round Baguete reported "
                  "without a name)."))

# ---- Inshorts: Series A of February 2015 from Tiger and Rebright
TCIRCLE = NEWS("inshorts", "secures $20M more from Tiger Global")
MN14 = NEWS("inshorts", "News In Shorts raises funding from Times Internet")
L.append(cls("inshorts", stage="Series A", stage_src="web_verified", stage_cite=TCIRCLE, stage_conf="high",
             entry_date="2015-02",
             rounds=[rnd("2013-09", "Seed (TLabs incubation, Rs 10 lakh)", None, "TLabs", False, MN14),
                     rnd("2014-07", "Seed", None, "Times Internet, Flipkart founders, angels", False, MN14),
                     rnd("2015-02", "Series A", 4000000, "Tiger Global, Rebright Partners", True, TCIRCLE),
                     rnd("2015-07-09", "Series B", 20000000, "Tiger Global", True, TCIRCLE),
                     OLD("inshorts", "2017-12-07"), OLD("inshorts", "2021-07-16")],
             note="Class sweep 2026-09-29: Techcircle (2015-07-09) says News in Shorts raised $4M (Rs 25 crore) "
                  "in Series A funding from Tiger Global and Rebright Partners in February 2015, the existing "
                  "angels joining, before Tiger's $20M Series B of July 2015; the 2013 and 2014 seed money came "
                  "from TLabs, Times Internet, the Flipkart founders and angels (MediaNama), not Tiger. Entry: the "
                  "Series A of February 2015."))

# ---- Fazz (Payfazz): Tiger led the $21M Series A of September 2018
YUK = NEWS("fazz", "Payfazz gets $53 million")
L.append(cls("fazz", stage="Series A", stage_src="web_verified", stage_cite=YUK, stage_conf="medium",
             entry_date="2018-09",
             rounds=[rnd("2018-09", "Series A", 21000000, "Tiger Global", True, YUK),
                     OLD("fazz", "2020-07-06"), OLD("fazz", "2022-09-13")],
             note="Class sweep 2026-09-29: TechCrunch's July 2020 report (Yahoo copy) says Payfazz's round before "
                  "the Series B was 'a $21 million Series A announced in September 2018, led by Tiger Global'. "
                  "Tiger led that round; the 2017 seed's investor list was not read, so the Series A entry is "
                  "held at medium confidence."))

# ---- Mayfair: Tiger led the $8M seed (April 2022); Amity and BoxGroup co-led the pre-seed
TC_MAYFAIR = NEWS("mayfair", "Mayfair emerges from stealth")
L.append(cls("mayfair", stage="Seed", stage_src="web_verified", stage_cite=TC_MAYFAIR, stage_conf="high",
             entry_date="2022-04",
             rounds=[rnd(None, "Pre-seed", 2000000, "Amity, BoxGroup", False, TC_MAYFAIR),
                     rnd("2022-04", "Seed", 8000000, "Tiger Global", True, TC_MAYFAIR)],
             note="Class sweep 2026-09-29: TechCrunch (2023-01-13): Amity and BoxGroup co-led the $2M pre-seed, "
                  "and 'Tiger Global, led by John Curtius (who has since departed the firm), led the company's "
                  "seed raise', the $8M seed that closed in April 2022, before Curtius's move to Cedar. Entry: "
                  "the Seed of April 2022. No later round found (Bing, 2026-09-29). Graduation left for the "
                  "graduation pass."))

# ---- MakeMyTrip: PIP IV's Series B preferred of August 2007 (F-1)
L.append(cls("makemytrip-ltd", stage="Growth", stage_src="web_verified", stage_cite=F1_MMYT, stage_conf="high",
             entry_date="2007-08-09",
             rounds=[rnd(None, "Series A", None, "SAIF, Helion Venture, Sierra Ventures", False, F1_MMYT, "filing"),
                     rnd("2007-08-09", "Series B", 15000579, None, True, F1_MMYT, "filing"),
                     rnd("2008-05-23", "Series C", 15000175, None, True, F1_MMYT, "filing")],
             note="Class sweep 2026-09-29: the F-1 (July 2010) lists Tiger Global Private Investment Partners IV "
                  "buying 75,146 Series B preferred shares on 9 August 2007 in the Series B (148,315 shares at "
                  "$101.14 to SAIF, Helion, the Sierra entities, PIP IV and three Tiger partners), and PIP V "
                  "buying Series C preferred on 23 May 2008; the Series A preferred sits with SAIF, Helion and "
                  "Sierra only. Entry: the Series B of August 2007, Growth."))

# ---- TAL: Tiger bought founders' common shares in August 2009 (a secondary), after KTB's Series A
L.append(cls("tal-education-group", stage="Growth", stage_src="web_verified", stage_cite=F1_TAL, stage_conf="high",
             entry_date="2009-08-12",
             rounds=[rnd("2009-02-12", "Series A", 5000000, "KTB/UCI China Ventures II", False, F1_TAL, "filing"),
                     rnd("2009-08-12", "Secondary: founders' common shares", 35000000,
                         "Tiger Global Five China Holdings", True, F1_TAL, "filing")],
             note="Class sweep 2026-09-29: the F-1 (2010) says the only pre-IPO preferred issue was the $5M Series A "
                  "of February 2009 to KTB/UCI China Ventures II, and that in August 2009 the four founders sold "
                  "21,875,000 common shares to Tiger Global Five China Holdings (held under PIP V) for $35M "
                  "(share purchase agreement of 12 August 2009). Tiger's entry is that secondary purchase from the "
                  "founders, which reads Growth (secondaries are Growth, COLLECTION.md 6); the F-1 does not bear "
                  "out the earlier reading that Tiger held shares before the agreement."))

# ---- Danke (Phoenix Tree): Series B-2 of May 2018 and a Series A-2 secondary, both Growth (F-1)
F1_DANKE = OLD("phoenix-tree-holdings-ltd")["source"]
L.append(cls("phoenix-tree-holdings-ltd", stage="Growth", stage_src="web_verified", stage_cite=F1_DANKE,
             stage_conf="high", entry_date="2018",
             rounds=[rnd("2015-11", "Series A-2", 3000000, "KIT Cube Limited", False, F1_DANKE, "filing"),
                     rnd("2018-02-12", "Series B (later B-1)", 60000000, None, False, F1_DANKE, "filing"),
                     rnd("2018-05-25", "Series B-2", 50000000, "Internet Fund IV, Joy Capital II", True, F1_DANKE,
                         "filing"),
                     rnd("2018-09-30", "Series C", 250000000, "Internet Fund IV", True, F1_DANKE, "filing"),
                     rnd(None, "Secondary: 32,247,379 Series A-2 shares from KIT Cube", None, None, True, F1_DANKE,
                         "filing")],
             note="Class sweep 2026-09-29: the F-1 shows Tiger's Internet Fund IV buying Series B-2 preferred on 25 "
                  "May 2018 (with Joy Capital II; $50M in all) and the whole $250M Series C on 30 September 2018. "
                  "Its 32,247,379 Series A-2 shares were issued to KIT Cube Limited in November 2015 and reached "
                  "Internet Fund IV by an undated transfer (KIT Cube holds the rest of the series). Either way the "
                  "entry is Growth (a Series B-2 purchase or a secondary), dated 2018, the year Tiger's Pengfei "
                  "Wang joined the board. The duplicate flag on this row predates the merge that made it the "
                  "canonical Danke row (danke-phoenix-tree is no longer in the base)."))

# ---- Kavak: Tiger first named in the Series E of September 2021
L.append(cls("kavak", stage="Growth", stage_src="web_verified", stage_cite=LAVCA_KAVAK_E, stage_conf="medium",
             entry_date="2021-09",
             rounds=[rnd("2020", "2020 round at about $1.2B", None, "SoftBank, DST Global, Greenoaks", None,
                         LAVCA_KAVAK_E),
                     rnd("2021-04-07", "Series D", 485000000, "D1 Capital Partners, Founders Fund, Ribbit, BOND",
                         None, TC_KAVAK_D),
                     rnd("2021-09-22", "Series E", 700000000, "General Catalyst", True, LAVCA_KAVAK_E),
                     OLD("kavak", "2025-03"), OLD("kavak", "2026-02-17")],
             note="Class sweep 2026-09-29: LAVCA (2021-09-22): the $700M Series E was 'led by General Catalyst, "
                  "with participation from Tiger Global' and others; the same page recaps the April 2021 $485M "
                  "Series D and the 2020 round from SoftBank, DST Global and Greenoaks without Tiger, and "
                  "TechCrunch's Series D report names D1, Founders Fund, Ribbit and BOND as its leads. Tiger is "
                  "first named in the Series E, so the entry reads Growth (September 2021) at medium confidence; "
                  "the 2016 to 2019 seed and early rounds were not read."))

# ---- GrubMarket: Tiger joins at the Series E of November 2021
L.append(cls("grubmarket", stage="Growth", stage_src="web_verified", stage_cite=PRN_GRUB_E, stage_conf="high",
             entry_date="2021-11-16",
             rounds=[rnd("2021-11-16", "Series E", 200000000, "Tiger Global Management", True, PRN_GRUB_E,
                         "company"),
                     OLD("grubmarket", "2022-09-28"), OLD("grubmarket", "2026-02-02")],
             note="Class sweep 2026-09-29: GrubMarket's release (PR Newswire, 2021-11-16) announces the $200M "
                  "Series E 'from Tiger Global Management, funds and accounts managed by BlackRock' and others at "
                  "over $1.2B, and quotes Tiger partner Griffin Schroeder: 'We look forward to being a part of "
                  "GrubMarket's journey', which reads as a new investor. Entry: the Series E, Growth."))

# ---- Meicai: Tiger co-led the January 2018 round, the Series E in the compiled history
KR_MEICAI_F = NEWS("meicai", "美菜网据称通过新一轮融资")
L.append(cls("meicai", stage="Growth", stage_src="web_verified", stage_cite=KR_MEICAI_E, stage_conf="medium",
             entry_date="2018-01",
             rounds=[rnd("2014-06", "Angel (RMB 10M)", None, "ZhenFund", False, N163_MEICAI),
                     rnd("2014-11", "Series A", None, "Blue Lake Capital", False, N163_MEICAI),
                     rnd("2015-02", "Series B", None, "Shunwei, Blue Lake Capital", False, N163_MEICAI),
                     rnd("2015-08", "Series C", None, None, None, N163_MEICAI),
                     rnd("2016-04", "Series D", None, None, None, N163_MEICAI),
                     rnd("2018-01-11", "Series E", 450000000, "Tiger Global Management, CMC", True, KR_MEICAI_E),
                     rnd("2018-10-10", "Round of at least $600M (about $800M at $7B)", 600000000,
                         "Hillhouse Capital, Tiger Global Management", True, KR_MEICAI_F)],
             note="Class sweep 2026-09-29: 36Kr (2018-01-11, from Bloomberg) reports a $450M round at about $2.8B "
                  "led by Tiger Global Management and CMC; the funding history compiled on 163.com (2018-10-12) "
                  "labels that January 2018 round the Series E, lists the angel (ZhenFund, 2014), Series A (Blue "
                  "Lake, 2014) and Series B (Shunwei and Blue Lake, 2015) without Tiger, and ties Tiger with "
                  "Hillhouse to the October 2018 round of at least $600M (36Kr flash, 2018-10-10). Tiger's entry "
                  "is Growth; January 2018 is the earliest Tiger round on record (a 2015 Series C or 2016 Series "
                  "D entry, whose investors are not listed, would read Growth too)."))

jl.write("sweep-a", L)
