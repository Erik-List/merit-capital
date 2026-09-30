"""PRO-100 NEA, stage pass s3, second half of queue/s3.json (51 rows): the entry round NEA first invested in,
with the funding history found (COLLECTION.md s6, PRO-143). Most rows are 1990s to 2000s entries; the IPO
prospectuses on EDGAR are the main source. Run: NQ_TAG=s3 python3 judgments-s3b.py"""
import json

import judge_lib as jl

C = json.loads((jl.INV / "companies/classification.json").read_text())
Q = json.loads((jl.Q / "s3.json").read_text())["slugs"]
rnd = jl.rnd
L = []


def R(slug, *new, drop=()):
    """The rounds already on the row (minus any named in `drop`) plus the ones found here, date order."""
    out = [r for r in (C.get(slug, {}).get("funding_rounds") or []) if r.get("round") not in drop]
    for r in new:
        if not any(o.get("date") == r["date"] and o.get("round") == r["round"] for o in out):
            out.append(r)
    return sorted(out, key=lambda r: str(r.get("date") or ""))


def U(slug, note, *new, drop=(), entry_date=None):
    L.append(jl.cls(slug, stage="undetermined", rounds=R(slug, *new, drop=drop), entry_date=entry_date, note=note))


def S(slug, stage, src, cite, conf, entry_date, note, *new, drop=()):
    L.append(jl.cls(slug, stage=stage, stage_src=src, stage_cite=cite, stage_conf=conf, entry_date=entry_date,
                    rounds=R(slug, *new, drop=drop), note=note))


NQ = "Google News (nq.py)"
NOIPO = ("EDGAR holds no IPO prospectus for the company (its electronic record starts after the listing) and NEA's "
         "filings on it are post-listing ownership reports, so no source names NEA's round.")

# IPO prospectuses and merger proxies on EDGAR (URLs printed by the SEC submissions listing or FTS())
S4_TRANSCEPT = jl.FTS("NOVACEA", "S-4")
S4_OCCAM = jl.FTS("ACCELERATED NETWORKS", "S-4")
S1_ASC = "https://www.sec.gov/Archives/edgar/data/1095583/000095013300002777/s-1.txt"
S1_NETC = "https://www.sec.gov/Archives/edgar/data/1081404/000101287099002445/0001012870-99-002445.txt"
S1_CORVIS = "https://www.sec.gov/Archives/edgar/data/1060490/000092838500001395/0000928385-00-001395.txt"
S1_AICX = "https://www.sec.gov/Archives/edgar/data/816066/000101287096000077/0001012870-96-000077.txt"
S1_MOBIUS = "https://www.sec.gov/Archives/edgar/data/1025148/000095012398002102/0000950123-98-002102.txt"
S1_BE = "https://www.sec.gov/Archives/edgar/data/895921/000101287099001419/0001012870-99-001419.txt"
S1_GADZ = "https://www.sec.gov/Archives/edgar/data/1084722/000089161899002049/0000891618-99-002049.txt"
S1_PKTR = "https://www.sec.gov/Archives/edgar/data/1011344/000089161899002402/0000891618-99-002402.txt"
S1_DIAT = "https://www.sec.gov/Archives/edgar/data/1011888/000095013596002057/0000950135-96-002057.txt"
S1_ALIEN = "https://www.sec.gov/Archives/edgar/data/1350415/000119312506079679/ds1.htm"
S1_MOTR = "https://www.sec.gov/Archives/edgar/data/1336691/000119312510010871/ds1.htm"
S1_PFWD = "https://www.sec.gov/Archives/edgar/data/1050180/000095013504001281/b49029pfsv1.htm"

U("aprius-inc", f"Stage pass 2026-09-30: {NQ} finds only a Light Reading item on an $11M raise with no date or "
  "investors; NEA's round is not named.")
U("bariatric-partners-inc", f"Stage pass 2026-09-30: {NQ} for Bariatric Partners and Journey Lite finds nothing; no "
  "round on record.")
U("drobo", f"Stage pass 2026-09-30: {NQ} under Drobo and Data Robotics (founded 2005, Wikipedia) finds no funding "
  "report naming NEA's 2008 round.")
U("lifemetrix-inc", f"Stage pass 2026-09-30: {NQ} has nothing on LifeMetrix's financings.")
U("predictive-biosciences", f"Stage pass 2026-09-30: {NQ} has no funding report; the 2010 Form D filings are later "
  "than NEA's 2008 year and name no round.")
U("telsima-corporation", f"Stage pass 2026-09-30: {NQ} for Telsima with NEA finds nothing; no round on record.")

VU = jl.NEWS("vuclip", "$6 Million Series B")
U("vuclip", "Stage pass 2026-09-30: Vuclip's $6M Series B of September 2009 was led by Jafco with NEA investing as an "
  "existing investor (MediaNama), so NEA came in before it, in 2008 per the firm; no source names that round.",
  rnd("2009-09-22", "Series B", 6000000, "Jafco Ventures", True, VU, "press"))

U("imergy-power-systems", f"Stage pass 2026-09-30: {NQ} under Imergy and its former name Deeya Energy finds no "
  "report of NEA's 2007 round.")
U("plusmo", f"Stage pass 2026-09-30: {NQ} has no funding report for Plusmo.")
U("techforward", f"Stage pass 2026-09-30: {NQ} finds only the 2012 Best Buy verdict; NEA's 2007 round, which "
  "predates the 2009 Form D filings, is not named.")

CV = jl.W("Conviva")
U("conviva", "Stage pass 2026-09-30: Wikipedia gives $15M from Time Warner Investments (February 2012), $44M from "
  "Foundation Capital, GGV and NEA (2013) and $40M with NEA (2017), all after NEA's 2006 entry; that round is not "
  "named anywhere read.",
  rnd("2012-02", "financing (round not named)", 15000000, "Time Warner Investments", None, CV, "press"),
  rnd("2013", "financing (round not named)", 44000000, None, True, CV, "press"),
  rnd("2017", "financing (round not named)", 40000000, None, True, CV, "press"))

S("paratek-formerly-transcept-pharmaceuticals", "Growth", "model", S4_TRANSCEPT, "medium", "2007-02",
  "The 2008 Novacea merger S-4 lists Transcept's rounds (Series A 2002, Series B 2003, a $23M Series C in 2005, a "
  "$40M Series D in February 2007) and its NEA holders as NEA 12 and NEA Ventures 2007, funds that postdate the "
  "Series C; with the firm's 2007 year, NEA's entry reads as the February 2007 Series D. No page states NEA's "
  "series in words, hence medium. The CIK's earlier NEA filings (2006) are Novacea's, a separate NEA holding.",
  rnd("2002-02", "Series A", None, None, None, S4_TRANSCEPT, "filing"),
  rnd("2003-07", "Series B", 7966748, None, None, S4_TRANSCEPT, "filing"),
  rnd("2005-10", "Series C", 23000000, None, None, S4_TRANSCEPT, "filing"),
  rnd("2007-02", "Series D", 40000000, None, True, S4_TRANSCEPT, "filing"))

U("rotation-medical", f"Stage pass 2026-09-30: {NQ} finds the 2016 $12M raise and Smith & Nephew's 2017 purchase but "
  "no report of the round NEA entered.",
  rnd("2016-08-17", "financing (round not named)", 12000000, None, None, None, "press"))
U("availink", f"Stage pass 2026-09-30: {NQ} has no funding report for Availink.")
U("sugarcrm", f"Stage pass 2026-09-30: {NQ} for SugarCRM with NEA and round words finds nothing naming NEA's 2005 "
  "round; Wikipedia lists NEA among investors without a round.")
U("motricity", "Stage pass 2026-09-30: the 2010 S-1 shows NEA 10 as a holder with a director since 2004 and describes "
  "the 2005 Series F and later rounds, but names no series NEA bought; stage stays undetermined.",
  rnd("2005-06", "Series F", 30000000, None, None, S1_MOTR, "filing"))
U("vantage-oncology", f"Stage pass 2026-09-30: {NQ} has no report naming NEA's 2004 round.")
U("hillcrest-laboratories", "Stage pass 2026-09-30: Wikipedia names NEA among early investors and in the 2011 "
  "financing without naming a round; NEA's 2003 round is not on record.")

S("occam-networks-inc", "Series A", "web_verified", S4_OCCAM, "high", "2000-02",
  "Occam's private rounds are listed in the 2001 Accelerated Networks merger S-4: New Enterprise Associates bought "
  "2,712,500 shares of the $1.00 Series A of February and March 2000, then Series B (2001) and Series C (2002); "
  "NEA's Tom McConnell joined the board in February 2000.",
  rnd("2000-02", "Series A", 6975000, None, True, S4_OCCAM, "filing"),
  rnd("2001-01", "Series B", 30840001, None, True, S4_OCCAM, "filing"),
  rnd("2002", "Series C (pre-merger)", None, None, True, S4_OCCAM, "filing"))

U("decru", f"Stage pass 2026-09-30: {NQ} has no funding report naming NEA's 2002 round.")

S("advanced-switching-communications-inc", "Growth", "web_verified", S1_ASC, "high", "1999-09-10",
  "The 2000 S-1 shows NEA VIII and affiliates buying only Class D preferred ($12.5M of a $40M class issued "
  "1999-09-10 and 1999-10-10), after Class A, B and C sold in 1998-99; Arthur Marks of NEA joined the board in "
  "September 1999.",
  rnd("1998", "Class A preferred", None, None, False, S1_ASC, "filing"),
  rnd("1998-06", "Class B preferred", None, None, False, S1_ASC, "filing"),
  rnd(None, "Class C preferred", None, None, False, S1_ASC, "filing"),
  rnd("1999-09-10", "Class D preferred", 40001979, None, True, S1_ASC, "filing"),
  rnd("2000-06-29", "Class E preferred", 500000, None, False, S1_ASC, "filing"))

U("home-account-network", "Stage pass 2026-09-30: InteliData's 2001 resale prospectus lists the NEA holders but no "
  "series; no other source names NEA's round.")
U("phase-forward", "Stage pass 2026-09-30: the 2004 S-1's related-party section does not name NEA (NEA VI appears only "
  "in an exhibit's signature pages), so no series is tied to NEA.")
U("appriva-medical", f"Stage pass 2026-09-30: {NQ} has no report naming NEA's 2000 round.")
U("e-offering", f"Stage pass 2026-09-30: {NQ} returns no funding report naming NEA's 2000 round.")
U("fineground-networks", f"Stage pass 2026-09-30: {NQ} finds only Cisco's purchase; NEA's 2000 round is not named.")

S("netcentives-inc", "Growth", "web_verified", S1_NETC, "high", "1997-09",
  "The 1999 S-1 lists every preferred sale since inception: New Enterprise Associates (with Stewart Alsop) bought "
  "Series C, D and E but no Series A or B, so its entry is the $10.1M Series C of September 1997; Alsop joined the "
  "board that month.",
  rnd("1996-09", "Series A", 944198, None, False, S1_NETC, "filing"),
  rnd("1996-11", "Series B", 485000, None, False, S1_NETC, "filing"),
  rnd("1997-09-16", "Series C", 10081301, None, True, S1_NETC, "filing"),
  rnd("1998-08-14", "Series D", 17250005, None, True, S1_NETC, "filing"),
  rnd("1999-03", "Series E", 36000936, None, True, S1_NETC, "filing"))

U("alien-technology-corporation", "Stage pass 2026-09-30: the 2006 S-1's preferred-sales table covers only purchases "
  "since October 2002, after NEA VIII's 1999 entry, and the early series carry no dates; stage stays undetermined.")
U("connetics-corp", f"Stage pass 2026-09-30: {NOIPO}")
U("procket", f"Stage pass 2026-09-30: {NQ} finds only Cisco's $89M purchase (EE Times, 2004); NEA's 1999 round is not "
  "named.")
U("testmart", f"Stage pass 2026-09-30: {NQ} has nothing on TestMart's financings.")
U("argon-networks", f"Stage pass 2026-09-30: {NQ} has nothing on Argon Networks' financings.")

S("corvis", "Series A", "web_verified", S1_CORVIS, "medium", "1998-05-06",
  "The 2000 S-1 records a Series A sale on 1998-05-06 to Frank Bonsal and persons or entities affiliated with him "
  "(NEA VII is the affiliated holder; Bonsal, an NEA founder, joined the board in March 1998), then the $13.5M "
  "Series B of 1998-05-15 in which the same group bought 465,116 shares. Medium, because the filing does not split "
  "the small Series A purchase between Bonsal and the fund.",
  rnd("1998-05-06", "Series A", None, None, True, S1_CORVIS, "filing"),
  rnd("1998-05-15", "Series B", 13532253, None, True, S1_CORVIS, "filing"),
  rnd("1999-02-26", "Series C", 28099932, None, None, S1_CORVIS, "filing"),
  rnd("1999-08-13", "Series F", 42000982, None, True, S1_CORVIS, "filing"))

U("netrix-corp", f"Stage pass 2026-09-30: {NOIPO}")
U("sci-solutions", f"Stage pass 2026-09-30: {NQ} has no report naming NEA's 1998 round.")

U("applied-imaging-corp", "Stage pass 2026-09-30: the 1996 S-1 shows NEA V buying Series I (August 1993) and Series J "
  "(September 1995), but NEA already held a large stake from earlier series the filing does not describe, so the "
  "entry round is not established.",
  rnd("1993-08", "Series I", 5336137, None, True, S1_AICX, "filing"),
  rnd("1995-09", "Series J", 4701422, None, True, S1_AICX, "filing"))

U("genemedicine-inc", f"Stage pass 2026-09-30: {NOIPO}")

S("mobius-management-systems", "Series A", "web_verified", S1_MOBIUS, "high", "1997-05-12",
  "The 1998 S-1 records the company's first preferred sale: $12.0M of Series A Convertible Preferred on 1997-05-12 to "
  "Oak Investment Partners, New Enterprise Associates VII, NEA President's Fund and NEA Ventures 1997 and others, "
  "with NEA's Peter Barris joining the board; the record calls it Series A although the company dated from 1981.",
  rnd("1997-05-12", "Series A", 12000130, None, True, S1_MOBIUS, "filing"))

U("quadramed-corporation", f"Stage pass 2026-09-30: {NOIPO}")

S("be", "Growth", "web_verified", S1_BE, "high", "1996-04-12",
  "The 1999 S-1 shows New Enterprise Associates VI buying Series 1 Convertible Preferred in the $14.1M financing of "
  "1996-04-12, done with a recapitalisation that converted the earlier Series A, A1 and B into common; the firm's "
  "1996 year matches, so NEA entered at the recap round, after three earlier series.",
  rnd(None, "Series A, A1 and B (converted to common in 1996)", None, None, None, S1_BE, "filing"),
  rnd("1996-04-12", "Series 1 (recapitalisation)", 14116000, None, True, S1_BE, "filing"),
  rnd("1998-02-04", "Series 2", 26899373, None, True, S1_BE, "filing"))

S("gadzoox-networks", "Growth", "web_verified", S1_GADZ, "high", "1996-09-05",
  "The 1999 S-1 shows New Enterprise Associates VI, NEA Presidents Fund and NEA Ventures 1996 buying Series E "
  "preferred at $1.80 on 1996-09-05, the firm's 1996 year; no earlier NEA purchase is described.",
  rnd("1996-09-05", "Series E", 7999999, None, True, S1_GADZ, "filing"))

S("packeteer", "Series A", "web_verified", S1_PKTR, "high", "1996-02",
  "The 1999 S-1's table of purchases since inception shows New Enterprise Associates buying Series A (February and "
  "April 1996, $0.25 a share), then Series B and C.",
  rnd("1996-02", "Series A", 700000, None, True, S1_PKTR, "filing"),
  rnd("1996-09", "Series B", 4821860, None, True, S1_PKTR, "filing"),
  rnd("1997-06", "Series C", 4432640, None, True, S1_PKTR, "filing"),
  rnd("1998-04", "Series D", 10058115, None, False, S1_PKTR, "filing"))

U("cardiothoracic-systems", f"Stage pass 2026-09-30: {NOIPO}")
U("bravo-health", f"Stage pass 2026-09-30: {NQ} under Bravo Health and Elder Health finds no report naming NEA's 1994 "
  "round.")

S("diatide", "Growth", "web_verified", S1_DIAT, "high", "1993-11-12",
  "The 1996 S-1 lists related-party financings since January 1993: New Enterprise Associates V bought Series C "
  "Convertible Preferred at $2.50 (closings 1993-11-12 and 1994-01-14) and Series D units in 1995, and was not in "
  "the 1993 notes; its affiliate Donald Murfin joined the board in November 1993, the firm's 1993 year.",
  rnd("1993-02-19", "Convertible notes", 946000, None, False, S1_DIAT, "filing"),
  rnd("1993-11-12", "Series C", 11474138, None, True, S1_DIAT, "filing"),
  rnd("1995-05-17", "Series D units", 3440216, None, True, S1_DIAT, "filing"),
  rnd("1995-08", "Series E", 10000000, "Nycomed", False, S1_DIAT, "filing"))

U("clarify", f"Stage pass 2026-09-30: {NOIPO}")
U("onstream", "Stage pass 2026-09-30: a 1991 private round; no filing, press item or Wikipedia sentence names it.")
U("ascend-communications", "Stage pass 2026-09-30: Wikipedia names NEA among Ascend's initial investors with KPCB and "
  "Greylock but names no round, and the 1994 listing predates EDGAR's record.")
U("macromedia", "Stage pass 2026-09-30: the firm's post says Dick Kramlich led the investment but no source names the "
  "round, and the 1993 listing predates EDGAR's record.")
U("devices-for-vascular-intervention", "Stage pass 2026-09-30: a 1986 private round; no source names it.")
U("bethesda-research-labs", "Stage pass 2026-09-30: a 1980 private round; no source names it.")

want = set(Q[52:])
got = {x["slug"] for x in L}
assert got == want, (sorted(want - got), sorted(got - want))
jl.write("s3b", L)
