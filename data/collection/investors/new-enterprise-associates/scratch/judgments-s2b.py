"""PRO-100 NEA, stage pass s2, second half: the round NEA first entered, with the funding history found.
Run: NQ_TAG=s2 python3 judgments-s2b.py"""
import json

import judge_lib as jl

cls, rnd, NEWS = jl.cls, jl.rnd, jl.NEWS
L = []
_OLD = json.loads((jl.INV / "companies" / "classification.json").read_text())


def R(slug, *new):
    """The row's rounds already on disk, then the new ones not already there."""
    old = list(_OLD.get(slug, {}).get("funding_rounds") or [])
    have = {(r.get("date"), r.get("round")) for r in old}
    return old + [r for r in new if (r["date"], r["round"]) not in have]


def und(slug, note, rounds):
    L.append(cls(slug, stage="undetermined", rounds=rounds, note=note))


GN = "Google News (the company with NEA and round words)"

# ---- tool-printed citations: EDGAR full-text hits and filing indexes listed in this pass, TechCrunch search results
SPRD_F1 = "https://www.sec.gov/Archives/edgar/data/1287950/000119312507130965/df1.htm"
NTDM_S1 = "https://www.sec.gov/Archives/edgar/data/1292653/000119312507009970/ds1.htm"
GLYC_S1 = "https://www.sec.gov/Archives/edgar/data/1253689/000119312513391443/d572031ds1.htm"
CONC_S1 = "https://www.sec.gov/Archives/edgar/data/1341740/000089161807000508/f31027orsv1.htm"
FNGN_S1 = "https://www.sec.gov/Archives/edgar/data/1430592/000095012309069405/f52084orsv1.htm"
CHG_S1 = "https://www.sec.gov/Archives/edgar/data/1356792/000119312506063319/ds1.htm"
XTERA_DRS = "https://www.sec.gov/Archives/edgar/data/1122051/000095012315009647/filename1.htm"
IMAN_424 = "https://www.sec.gov/Archives/edgar/data/1093242/0000891618-99-005296-index.html"
MCS_424 = "https://www.sec.gov/Archives/edgar/data/1087194/0000899243-99-002298-index.html"
DCCA_424 = "https://www.sec.gov/Archives/edgar/data/941775/0000950109-99-003913-index.html"
MCDE_424 = "https://www.sec.gov/Archives/edgar/data/1010915/0000891618-96-000535-index.html"
AMSY_424 = "https://www.sec.gov/Archives/edgar/data/1003202/0000928385-96-000671-index.html"
ASPM_424 = "https://www.sec.gov/Archives/edgar/data/886235/0000950135-00-000301-index.html"
TC_PENTAHO12 = ("https://techcrunch.com/2012/10/30/open-source-business-intelligence-company-pentaho-lands-23-million-"
                "series-c/")
TC_PENTAHO08 = "https://techcrunch.com/2008/02/21/pentaho-takes-12-million-series-c/"
TC_TIDALTV = "https://techcrunch.com/2011/03/31/tidaltv-raises-over-30m-for-online-video-ad-optimization-technology/"

# ---------------------------------------------------------------- staged from the IPO prospectus or press
L.append(cls("spreadtrum-communications", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=SPRD_F1, entry_date="2004-04",
             rounds=[rnd("2002-11", "Series B", 19848602, None, False, SPRD_F1, "filing"),
                     rnd("2004-04", "Series C", 35200526, None, True, SPRD_F1, "filing"),
                     rnd("2006-09", "Series D", 19458792, None, True, SPRD_F1, "filing")],
             note="The F-1's related-party section lists NEA among the buyers of the April 2004 Series C ($1.01 a share) "
                  "and the 2006 Series D, not the 2002-2003 Series B, so NEA entered at the Series C: Growth."))
L.append(cls("neutral-tandem", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=NTDM_S1,
             entry_date="2003",
             rounds=[rnd("2003", "Series A", 8600000, None, True, NTDM_S1, "filing"),
                     rnd("2004", "Series B-1", 8300000, None, True, NTDM_S1, "filing"),
                     rnd(None, "Series B-2 and Series C", None, None, True, NTDM_S1, "filing")],
             note="The 2007 S-1: the company issued 8,723,000 Series A shares in 2003 for $8.6M, and NEA 10 and NEA "
                  "Ventures 2003 hold 3,746,000 of them (with B-1, B-2 and C shares), the firm's own 2003 entry."))
L.append(cls("glycomimetics", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=GLYC_S1,
             entry_date="2003",
             rounds=[rnd("2003", "Series A", 9064795, None, None, GLYC_S1, "filing"),
                     rnd(None, "Series B", 15350818, None, None, GLYC_S1, "filing"),
                     rnd("2009", "Series A-1 (recapitalization)", 38805055, None, True, GLYC_S1, "filing")],
             note="The 2013 S-1 shows Series A as the only preferred sold from the May 2003 founding through 2004 ($9.1M), "
                  "and NEA 10's common came from the Series A and B converted in the 2009 A-1 recap; with the firm's "
                  "own 2003 year, the entry reads Series A at medium."))
L.append(cls("data-critical-corporation", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=DCCA_424, entry_date="1998-03",
             rounds=[rnd("1998-03", "Series D", 9186936, None, True, DCCA_424, "filing")],
             note="The 1999 IPO prospectus: New Enterprise Associates VII, NEA Presidents Fund and NEA Ventures 1998 "
                  "bought 1,095,000 Series D shares at $4.00 (March to June 1998), exactly their holding, and Ronald "
                  "Kase joined the board in March 1998, so NEA entered at the Series D: Growth."))
L.append(cls("microcide-pharmaceuticals-inc", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=MCDE_424, entry_date="1994",
             rounds=[rnd("1993", "Series A", 2021751, None, False, MCDE_424, "filing"),
                     rnd(None, "Series B", 3977500, None, False, MCDE_424, "filing"),
                     rnd("1994", "Series C", None, None, True, MCDE_424, "filing"),
                     rnd(None, "Series D", 5017500, None, False, MCDE_424, "filing"),
                     rnd(None, "Series E", 5000000, None, False, MCDE_424, "filing")],
             note="The 1996 IPO prospectus's purchaser table shows New Enterprise Associates VI buying 533,333 Series C "
                  "shares ($3.75) and no Series A or B; NEA's Hugh Rienhoff joined the board in July 1994, which dates "
                  "the entry: Growth."))
L.append(cls("concentric-medical", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=CONC_S1,
             entry_date="1999",
             rounds=[rnd("1999", "Series A", None, None, True, CONC_S1, "filing"),
                     rnd(None, "Series B, C and D", None, None, None, CONC_S1, "filing")],
             note="The 2007 S-1: incorporated in August 1999, NEA's Ryan Drant on the board from November 1999, and "
                  "Series A the first of its four preferred series, so NEA's 1999 entry reads Series A at medium."))
L.append(cls("imanage", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=IMAN_424,
             entry_date="1998",
             rounds=[rnd("1996-12-27", "Series A", 2026133, None, False, IMAN_424, "filing"),
                     rnd("1997-12-15", "Series B", 5024000, None, True, IMAN_424, "filing"),
                     rnd("1998-09-28", "Series C", 4156759, None, True, IMAN_424, "filing")],
             note="The 1999 IPO prospectus: entities associated with NEA bought 1,034,401 Series B shares (closings "
                  "December 1997 to July 1998) and 1,705,599 Series C, none of the Series A; with the firm's own 1998 "
                  "year, NEA entered at the Series B: Growth."))
L.append(cls("mission-critical-software", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=MCS_424, entry_date="1996-09",
             rounds=[rnd("1996-09", "Series A (issued for the OnePoint software and $25,000)", None, None, False,
                         MCS_424, "filing"),
                     rnd("1996-09", "Series B", 2650000, None, True, MCS_424, "filing"),
                     rnd("1997-07", "Series C", None, None, True, MCS_424, "filing")],
             note="The 1999 IPO prospectus: NEA VII, NEA President's Fund and NEA Ventures 1996 bought 1,250,000 Series "
                  "B shares (September 1996, when Scott Sandell joined the board) and 683,333 Series C, no Series A "
                  "(issued for software assets); the record names the entry Series B: Growth."))
L.append(cls("amisys-managed-care", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=AMSY_424, entry_date="1994-05-26",
             rounds=[rnd("1994-05-26", "Acquisition from AIG (Class A common and notes)", 10000000,
                         "Greylock, NEA VI and ABS Capital Partners", True, AMSY_424, "filing")],
             note="The 1996 IPO prospectus: Greylock, NEA VI and ABS Capital bought the company from AIG on 1994-05-26 "
                  "for $10.0M cash, NEA VI taking 2,000,000 Class A shares and $4.0M of notes; a consortium buyout, read "
                  "Growth (buyout scale), and a control position to review under R1."))
L.append(cls("pentaho", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_PENTAHO12,
             entry_date="2005",
             rounds=[rnd("2005", "Series A", 5000000, "NEA", True, TC_PENTAHO12, "press"),
                     rnd("2006", "Series B", 8000000, None, True, TC_PENTAHO12, "press"),
                     rnd("2008-02-21", "Series C", 12000000, "Benchmark Capital", True, TC_PENTAHO08, "press"),
                     rnd("2010", "unnamed", 7000000, None, None, TC_PENTAHO12, "press"),
                     rnd("2012-10-30", "Series C (fifth round)", 23000000, None, None, TC_PENTAHO12, "press")],
             note="TechCrunch (2012-10-30): founded in 2004, Pentaho raised a $5M Series A from New Enterprise "
                  "Associates with Index Ventures participating, the firm's own 2005 entry."))

# ---------------------------------------------------------------- undetermined, with what the search found
und("aspect-medical", "Stage pass: the 2000 IPO prospectus shows NEA IV already an investor at the October 1995 bridge "
    "and buying Series B-1 and Series C, but its related-party history starts in 1995 and does not name the 1989 round.",
    [rnd("1995-11", "Series B-1", 7600000, None, True, ASPM_424, "filing"),
     rnd(None, "Series C", 12900000, None, True, ASPM_424, "filing")])
und("financial-engines", "Stage pass: the 2009 S-1 dates the early series (Series A September 1996 to February 1997, "
    "Series B March 1997) but ties none to NEA VII; Richard Kramlich joined the board in January 1997, between them.",
    [rnd("1996-09-20", "Series A", 515003, None, None, FNGN_S1, "filing"),
     rnd("1997-03-28", "Series B", 4299981, None, None, FNGN_S1, "filing"),
     rnd("1998-06-05", "Series C", 11834696, None, None, FNGN_S1, "filing"),
     rnd("1999-04-30", "Series D", None, None, None, FNGN_S1, "filing")])
und("chg-healthcare", "Stage pass: the 2006 S-1 lists the NEA VIII, 8A and 10 holdings and Charles Linehan's board seat "
    "from December 1998 but no series or round for NEA's 1998 investment.", [])
und("xtera-communications-inc", "Stage pass: the 2015 registration statement gives no preferred history before its "
    "recent financings, and Google News found nothing on NEA's 2000 round.", [])
und("lumisys-inc-de", "Stage pass: NEA's only record is a 1997 13G after the 1995 listing; the IPO prospectus is not on "
    f"EDGAR and {GN} found nothing.", [])
und("premier-laser-systems-inc", "Stage pass: NEA's record is a 1997 13G/A on a company already listed; whether NEA "
    "bought a private round before the listing or a later placement is open (an X1 check), and no round is named.", [])
und("3com-corporation", "Stage pass: the firm's 1996 year falls twelve years after 3Com's 1984 listing, so no venture "
    f"round can be named (a D8 or X1 case); {GN} found nothing.", [])
und("rf-monolithics", "Stage pass: NEA's Cornelius Bond sat on the board from 1992, before the 1994 listing, but no "
    f"source names the round; {GN} found nothing.", [])
und("realtime-worlds-inc", "Stage pass: GamesBeat (2010) confirms $30M from NEA in 2006 but, like Wikipedia, names no "
    "series.", R("realtime-worlds-inc", rnd("2010-01", "unnamed", 21000000, None, None,
                                              NEWS("realtime-worlds-inc", "After raising $100M"), "press")))
und("videology", "Stage pass: TechCrunch (2011) reports TidalTV's $30M raise (total $61M) without naming investors per "
    "round; NEA's 2008 round is not named.", [rnd("2011-03-31", "unnamed", 30000000, None, None, TC_TIDALTV, "press")])
for s in ["konarka-technologies-inc", "suniva-inc", "chelsio-communications", "fulcrum-microsystems",
          "apnex-medical-inc"]:
    und(s, f"Stage pass: {GN} and TechCrunch's own search found no report naming NEA's entry round.", R(s))
for s, what in [("advanced-cardiovascular", "Advanced Cardiovascular Systems"), ("alkermes-inc", "Alkermes"),
                ("axys-pharmaceuticals-inc", "AXYS or Arris"), ("convex-computer-systems", "Convex Computer"),
                ("occupational-health-rehab", "Occupational Health + Rehabilitation"), ("hdmessaging", "HDMessaging"),
                ("pinnacle-engines", "Pinnacle Engines"), ("china-gtel-limited", "China Gtel"),
                ("movius-interactive-corporation", "Movius or IP Unity"), ("ringcube", "RingCube"),
                ("vixs-systems", "ViXS"), ("lsf-network", "LSF Network"), ("neuralieve", "NeuraLieve or eNeura"),
                ("newscale", "newScale"), ("yipes-communications", "Yipes"), ("exent-technologies", "Exent"),
                ("pponext", "ppoNEXT"), ("switchon-networks", "SwitchOn Networks"), ("3ware", "3ware"),
                ("salix", "Salix Technologies"), ("amplitude", "Amplitude (the 1990s calendaring company)"),
                ("endotex", "Endotex"), ("aneurx", "AneuRx"), ("grand-junction", "Grand Junction Networks"),
                ("genetic-therapy-inc", "Genetic Therapy"), ("surgical-health", "Surgical Health"),
                ("enzytech", "Enzytech"), ("life-technologies", "Life Technologies (GIBCO BRL)")]:
    und(s, f"Stage pass: {GN} found no round for {what}, and no filing on disk names one.", [])

jl.write("s2b", L)
