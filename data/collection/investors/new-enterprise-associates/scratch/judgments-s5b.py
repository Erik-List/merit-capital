"""PRO-100 NEA, stage pass s5, second half (51 rows): the round in which an NEA fund first invested, and the funding
history found (COLLECTION.md s6, PRO-143). Run: NQ_TAG=s5 python3 judgments-s5b.py"""
import json

import judge_lib as jl

cls, rnd, NEWS, FTS = jl.cls, jl.rnd, jl.NEWS, jl.FTS
C = json.load(open(jl.INV / "companies" / "classification.json"))
L = []


def R(slug, *new, drop=()):
    """The rounds already on disk for the row (minus `drop` (date, round) pairs), plus the new ones."""
    old = [r for r in (C.get(slug) or {}).get("funding_rounds") or [] if (r.get("date"), r.get("round")) not in drop]
    have = {(r.get("date"), r.get("round"), r.get("source")) for r in old}
    return old + [r for r in new if (r["date"], r["round"], r["source"]) not in have]


def U(slug, note, *new, entry_date=None):
    """Stage stays undetermined; the rounds found (or none) are recorded with what was searched."""
    L.append(cls(slug, stage="undetermined", entry_date=entry_date, rounds=R(slug, *new), note=note))


PRE = ("pre-web era; Wikipedia, Google News and EDGAR full text (2001 on) carry nothing on its private rounds, so the "
       "round NEA entered is not on record.")

U("amplica-inc", "Stage pass: " + PRE)

ARYX = FTS("ARYx", "8-K")
U("aryx-therapeutics-inc", "Stage pass: NEA's only recorded purchase is the November 2008 private placement by Growth "
  "Equity Opportunities Fund (an NEA 12 vehicle) into ARYx, listed since its 2007 IPO, and the IPO filings name no NEA "
  "holder; this is a public purchase (the X1 class), so the membership verdict should be reviewed.",
  rnd("2008-11-12", "Private placement (PIPE)", None, None, True, ARYX, "filing"))

U("carewise-inc", "Stage pass: " + PRE)
U("hospital-partners-of-america-inc", "Stage pass: Google News and TechCrunch's own search returned nothing on its rounds; "
  "NEA's round is not on record.")
U("novast-holdings-limited", "Stage pass: Google News (the name with NEA) returned nothing on its rounds; NEA's 2008 "
  "round is not named.")
U("protostar-ltd", "Stage pass: Google News and TechCrunch's own search returned no funding report naming NEA's round.")

VF = NEWS("valuefirst", "ValueFirst raises Rs 70cr")
U("valuefirst", "Stage pass: Moneycontrol (2011-02-04) reports Rs 70 crore from Headland Asian Ventures Fund 3 and NEA, "
  "and MediaNama (2008-10) a $5-8M round then pending with undisclosed investors; no source names the round of NEA's "
  "2008 entry.", rnd("2011-02-04", "unnamed", None, "Headland Asian Ventures; NEA", True, VF, "press"))

U("bandgap-engineering", "Stage pass: Google News returns only the physics term; NEA's 2007 round is not named.")

MX = NEWS("moximed", "Moximed closes $91M Series D")
U("moximed", "Stage pass: MassDevice (2024-08-13) reports a $91M Series D, and the firm's 2021 post says ExploraMed and "
  "NEA spun Moximed out, but no source names the round of NEA's 2007 entry.",
  rnd("2024-08-13", "Series D", 91000000, None, None, MX, "press"))

U("solar-junction", "Stage pass: Google News and TechCrunch's own search returned nothing on its rounds; NEA's 2007 "
  "round is not named.")

VY = NEWS("vytronus", "NEA startup VytronUS")
U("vytronus", "Stage pass: the firm's 2014 post reports a $31.6M round led by new investors including Abbott, and Fierce "
  "Biotech (2016) a $49M round; neither names the round of NEA's 2007 entry.",
  rnd("2016-07-29", "unnamed", 49000000, None, None, VY, "press"))

IOMAI = C["iomai-corporation"]
L.append(cls("intercell-usa-inc", stage=IOMAI["entry_stage"], stage_src=IOMAI["entry_stage_source"],
             stage_cite=IOMAI["entry_stage_citation"], stage_conf=IOMAI["entry_stage_confidence"],
             entry_date=IOMAI["entry_date"], rounds=R("intercell-usa-inc"),
             note="Stage pass: Intercell USA, Inc. is Iomai Corporation renamed after Intercell bought it in 2008 (the "
                  "same EDGAR CIK 1125001 as the iomai-corporation citation), a duplicate of that row; classified as "
                  "it: NEA 10 held only Series C preferred, sold December 2002."))

U("portauthority", "Stage pass: Google News and TechCrunch's own search returned nothing on PortAuthority's rounds; NEA's "
  "2006 round is not named.")
U("solfocus-inc", "Stage pass: Google News and TechCrunch's own search returned nothing on SolFocus's rounds; NEA's 2006 "
  "round is not named.")
U("carticept-medical", "Stage pass: Google News (the name with financing) returned nothing; NEA's 2005 round is not "
  "named.")

WSS = FTS("WEBSIDESTORY", "8-K")
U("websidestory-inc", "Stage pass: NEA 10 signs WebSideStory's 2005 agreements as an 'Avivo investor': its WebSideStory "
  "shares were the consideration for WebSideStory's purchase of Avivo, so the holding is stock received on a sale (D8), "
  "as the visual-sciences row already rules, and this row's membership should be reviewed.",
  rnd("2005-02-10", "Stock received for Avivo (sale consideration)", None, None, True, WSS, "filing"))

U("prostor-systems-inc", "Stage pass: TechCrunch's own search returned only a namesake fund; the 2010 Form D is a later "
  "round and NEA's 2004 round is not named.")

XO_F3 = jl._base()["xoom-corporation"]["edgar_links"].split(";")[0].strip()
L.append(cls("xoom-corporation", stage="Growth", stage_src="web_verified", stage_cite=XO_F3, stage_conf="high",
             entry_date="2004",
             rounds=R("xoom-corporation",
                      rnd("2004", "Series C", None, None, True, XO_F3, "filing"),
                      rnd("2009-12", "Series F", 58250010, None, True,
                          "https://www.sec.gov/Archives/edgar/data/1315657/000119312513010596/d364901ds1.htm", "filing")),
             note="Stage pass: NEA 11's Form 3 at the February 2013 IPO lists Series C, C-1, D, E and F preferred, and "
                  "NEA 9 holds Series F only; with no NEA share below Series C, NEA entered at the Series C (Kramlich "
                  "joined the board in April 2005, the firm's year is 2004): Growth."))

U("luxtera", "Stage pass: Google News and TechCrunch's own search returned only the 2018 Cisco sale; the 2009 Form D is a "
  "later round and NEA's 2003 round is not named.")

ZH = C["zhone-technologies"]
L.append(cls("zti-merger-subsidiary-iii-inc", stage=ZH["entry_stage"], stage_src=ZH["entry_stage_source"],
             stage_cite=ZH["entry_stage_citation"], stage_conf=ZH["entry_stage_confidence"], entry_date=ZH["entry_date"],
             rounds=R("zti-merger-subsidiary-iii-inc"),
             note="Stage pass: ZTI Merger Subsidiary III is the private Zhone Technologies after its 2003 merger with "
                  "Tellium (the same EDGAR CIK 1097703 as the zhone-technologies citation), a duplicate of that row; "
                  "classified as it: Series A preferred, November 1999."))

U("mainstream-data", "Stage pass: " + PRE)
U("anulex-technologies-inc", "Stage pass: Google News (the name with financing) returned nothing; the 2009 Form D is a "
  "later round and NEA's 2001 round is not named.")

IT = NEWS("intrinsic-therapeutics", "raises $52m for Barricaid")
U("intrinsic-therapeutics", "Stage pass: MassDevice (2019-04-11) reports a $52M raise, and the Form Ds start in 2010; no "
  "source names the round of NEA's 2001 entry.", rnd("2019-04-11", "unnamed", 52000000, None, None, IT, "press"))

U("virtela", "Stage pass: Google News returned only the 2013 NTT sale; NEA's 2001 round is not named.")
U("benu-inc", "Stage pass: " + PRE)
U("echopass-corporation", "Stage pass: Wikipedia (Genesys) mentions only the founders' family loans; Google News returned "
  "nothing on its rounds, so NEA's 2000 round is not named.")
U("laurel-networks", "Stage pass: Wikipedia (ECI Telecom) and Google News carry nothing on its rounds; NEA's 2000 round is "
  "not named.")
U("spine-wave", "Stage pass: Google News (the name with financing) returned nothing on its rounds; NEA's 2000 round is not "
  "named.")
U("censtor-corp-ca", "Stage pass: NEA's only filing is a 1999 Schedule 13G on a listed company; no source names a private "
  "round, so the stage (and whether this is a public purchase) is open.")
U("patientkeeper", "Stage pass: Google News returned nothing on its rounds; NEA's 1999 round is not named.")
U("spiration", "Stage pass: Google News (the name with financing) returned nothing; NEA's 1999 round is not named.")

WX = "https://www.sec.gov/Archives/edgar/data/1109935/000109581100002156/e424b4.txt"
L.append(cls("webex-communications", stage="Growth", stage_src="web_verified", stage_cite=WX, stage_conf="high",
             entry_date="1999-12",
             rounds=R("webex-communications",
                      rnd("1998-05", "Series A", 1287533, None, False, WX, "filing"),
                      rnd("1998-08", "Series B", 5816955, "Vanenburg Capital", False, WX, "filing"),
                      rnd("1999-12", "Series C", 24363975, None, True, WX, "filing"),
                      rnd("2000-03-30", "Series D", 25668063, None, True, WX, "filing")),
             note="Stage pass: WebEx's 2000 IPO prospectus shows entities affiliated with New Enterprise Associates "
                  "buying 2,326,667 Series C shares ($7.0M) and Series D, and no Series A or B; Scott Sandell joined "
                  "the board in December 1999, so NEA entered at the Series C: Growth."))

AU = "https://www.sec.gov/Archives/edgar/data/1010919/000093639297000843/0000936392-97-000843.txt"
L.append(cls("aurora-biosciences-corporation", stage="Series A", stage_src="web_verified", stage_cite=AU,
             stage_conf="high", entry_date="1996-03",
             rounds=R("aurora-biosciences-corporation", rnd("1996-03", "Series A", 13600000, None, True, AU, "filing")),
             note="Stage pass: Aurora's 1997 IPO prospectus lists New Enterprise Associates VI and NEA Ventures 1996 "
                  "among the Series A buyers (March 1996, the company's first round after founder notes), and no "
                  "later NEA purchase: NEA entered at the Series A."))

U("good-technology", "Stage pass: the 2013 DRS investor-rights agreement lists New Enterprise Associates VII, NEA "
  "Presidents Fund and NEA Ventures 1998 as holders of Visto (renamed Good), but no source read gives the series NEA "
  "bought in 1998.")
U("proxima-therapeutics", "Stage pass: " + PRE)
U("trading-dynamics", "Stage pass: " + PRE)
U("eroom", "Stage pass: " + PRE)
U("graphix-zone-inc-de", "Stage pass: NEA's only filings are 1997-1999 Schedule 13Gs on the listed company; no source "
  "names a private round (Graphix Zone had merged with StarPress in 1996), so the stage and the way NEA came to hold it "
  "are open.")
U("opta-food-ingredients-inc-de", "Stage pass: NEA's only filings are 1997-2000 Schedule 13Gs after the 1992 IPO; no "
  "source names the private round NEA entered.")
U("silicon-spice", "Stage pass: " + PRE)

CB = "https://www.sec.gov/Archives/edgar/data/1065748/000095013399002213/0000950133-99-002213.txt"
U("careerbuilder", "Stage pass: the 1999 IPO prospectus shows NEA VI and NEA President's Fund buying Class B convertible "
  "preferred in July 1996 ($0.76), the company's first venture round (the Class A preferred being the founders' "
  "converted stock), then Class C to F; the record names the round Class B, which does not map onto the ladder, so it is "
  "left for a ruling.",
  rnd("1996-07", "Class B convertible preferred", None, None, True, CB, "filing"),
  rnd("1997-01", "Class C convertible preferred", None, None, True, CB, "filing"),
  rnd("1997-09", "Class D convertible preferred", None, None, True, CB, "filing"),
  rnd("1998-07", "Class E convertible preferred", None, None, True, CB, "filing"),
  rnd("1999-01", "Class F convertible preferred", None, None, True, CB, "filing"), entry_date="1996-07")

JN = "https://www.sec.gov/Archives/edgar/data/1043604/000089161899002862/0000891618-99-002862.txt"
L.append(cls("juniper-networks", stage="Growth", stage_src="web_verified", stage_cite=JN, stage_conf="high",
             entry_date="1996-08-05",
             rounds=R("juniper-networks",
                      rnd("1996-06-11", "Series A", 1743751, None, False, JN, "filing"),
                      rnd("1996-08-05", "Series B", None, None, True, JN, "filing")),
             note="Stage pass: Juniper's 1999 IPO prospectus lists only Kleiner Perkins funds among the June 1996 "
                  "Series A buyers and New Enterprise Associates VI, NEA Presidents Fund and NEA Ventures 1996 among "
                  "the Series B buyers (from August 1996; Kramlich joined the board in July 1996): Growth."))

U("tripod", "Stage pass: Wikipedia (Tripod.com) says Tripod's initial $4M of venture capital was led by New Enterprise "
  "Associates, before a $10M round in May 1997; the source does not name the round, so it is left for a ruling.",
  rnd("1996", "initial venture round", 4000000, "NEA", True, jl.W("Tripod.com"), "press"),
  rnd("1997-05", "unnamed", 10000000, None, None, jl.W("Tripod.com"), "press"), entry_date="1996")

U("insoft", "Stage pass: Wikipedia (InSoft Inc.) names NEA only among the backers of Adams Capital's financing, without a "
  "round; not on record.")

GT = "https://www.sec.gov/Archives/edgar/data/1023905/000095013596005079/0000950135-96-005079.txt"
L.append(cls("geotel-corporation", stage="Growth", stage_src="web_verified", stage_cite=GT, stage_conf="high",
             entry_date="1994-07-29",
             rounds=R("geotel-corporation",
                      rnd("1993-09-30", "Series A", 3300000, None, False, GT, "filing"),
                      rnd("1994-07-29", "Series B", 4557500, None, True, GT, "filing"),
                      rnd("1995-08-09", "Series C", 4000000, None, True, GT, "filing")),
             note="Stage pass: GeoTel's 1996 IPO prospectus lists Matrix, Sigma and Atlas as the September 1993 Series "
                  "A buyers and New Enterprise Associates VI buying 971,429 Series B shares on 1994-07-29 (the firm's "
                  "1994 year), then Series C: NEA entered at the Series B, Growth."))

ES = "https://www.sec.gov/Archives/edgar/data/940659/000091205797009491/0000912057-97-009491.txt"
L.append(cls("endocardial-solutions", stage="Series A", stage_src="web_verified", stage_cite=ES, stage_conf="high",
             entry_date="1993-03",
             rounds=R("endocardial-solutions",
                      rnd("1993-03", "Series A", 775000, None, True, ES, "filing"),
                      rnd("1993-12", "Series B", None, None, True, ES, "filing"),
                      rnd("1996-04", "Series C", 10002944, None, False, ES, "filing")),
             note="Stage pass: Endocardial's 1997 IPO prospectus shows New Enterprise Associates V and affiliates "
                  "buying Series A preferred (issued March 1993, the firm's 1993 year) and Series B: NEA entered at "
                  "the Series A."))

U("datalogix", "Stage pass: " + PRE)
U("parc-place", "Stage pass: " + PRE)
U("nellcor", "Stage pass: the firm labels its 1990 investment Public/PIPES, a purchase in a listed company, and no "
  "source names a private round.")
U("pyxis", "Stage pass: " + PRE)
U("sepracor", "Stage pass: " + PRE)

jl.write("s5b", L)
