"""PRO-100 NEA, stage pass s1, second half of queue/s1.json (50 rows): the round NEA first entered, with the
funding history found (COLLECTION.md s6, PRO-143). Run: NQ_TAG=s1 python3 judgments-s1b.py"""
import json

import judge_lib as jl

C, rnd = jl.cls, jl.rnd
CLS = json.loads((jl.INV / "companies/classification.json").read_text())
Q = json.loads((jl.Q / "s1.json").read_text())["slugs"][50:]
FTSR = json.loads((jl.INV / "sources/edgar/fts-hits.json").read_text())["registrants"]


def OLD(slug):
    """The funding rounds already on the row (kept: a new list replaces the key)."""
    return list((CLS.get(slug) or {}).get("funding_rounds") or [])


def FD(slug, firm=None):
    """The row's own Form D sequence as unnamed rounds, each cited to its filing index."""
    out = []
    for i, r in enumerate(jl.FORMD_ROUNDS(slug)):
        out.append(rnd((r.get("sale_date") or r.get("quarter") or "")[:10], "unnamed (Form D)",
                       r.get("offering_usd") or r.get("sold_usd"), None, firm, jl.FORMD_CITE(slug, i), "filing"))
    return out


def FTS_FILE(reg, sub):
    """The one full-text hit URL of registrant `reg` whose URL contains `sub`."""
    m = [f["url"] for r in FTSR if reg.lower() in r["registrant"].lower() for f in r.get("filings", [])
         if sub in f["url"]]
    m = list(dict.fromkeys(m))
    if len(m) != 1:
        raise SystemExit(f"FTS_FILE({reg!r}, {sub!r}) matched {len(m)}")
    return m[0]


def MERGE(*lists):
    seen, out = set(), []
    for lst in lists:
        for x in lst:
            k = (x.get("date"), x.get("round"), x.get("amount_usd"))
            if k not in seen:
                seen.add(k)
                out.append(x)
    return out


SRCH = "Stage pass 2026-09-30: Google News, TechCrunch's own search and EDGAR full text"
PRE = " The IPO prospectus predates EDGAR's electronic filings."
L = []

s = "addthis"
TC_CS = "https://techcrunch.com/2011/05/10/addthis-indeed-clearspring-raises-20-million-as-it-rides-social-sharing-boom/"
L.append(C(s, stage="undetermined",
           rounds=[rnd("2011-05-10", "Series D", 20000000, "Institutional Venture Partners", True, TC_CS, "press")],
           note="Stage pass 2026-09-30: TechCrunch names Clearspring's 2011 $20M round a Series D with NEA "
                "participating, but no source names the round NEA entered in 2008."))

s = "akashic-memories-corporation"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Akashic Memories."))

s = "anadys-pharmaceuticals-inc"
AN = jl.FTS("ANADYS", "S-1")
L.append(C(s, stage="undetermined",
           rounds=[rnd("2002-06-20", "Series C", None, "Care Capital", None, AN, "filing")],
           note="Stage pass 2026-09-30: the June 2002 registration rights agreement filed with the IPO lists New "
                "Enterprise Associates 5 among the older holders (the Scriptgen era) but ties it to no series; the "
                "prospectus names no NEA purchase."))

s = "autoimmune-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "china-health-citic"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round. Same company as the citic-pharmaceuticals row (same description and acquirer)."))

s = "ibah-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "novatorque"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of NovaTorque."))

s = "provation-medical-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of ProVation."))

s = "vertiflex"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Vertiflex."))

s = "fanhattan"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round of Fanhattan."))

s = "novatium"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Novatium."))

s = "spinmedia"
BZ1 = "https://techcrunch.com/2007/05/24/buzznet-lands-6million"
BZ2 = "https://www.mediapost.com/publications/article/102550/buzznet-morphs-into-buzz-media-lands-125-millio.html"
L.append(C(s, stage="undetermined",
           rounds=[rnd("2007-05", "venture round (unnamed)", 6000000, "Redpoint Ventures; Anthem Venture Partners", None,
                       BZ1, "press"),
                   rnd("2008", "venture round (unnamed)", 25000000, None, None, BZ2, "press"),
                   rnd("2009-03-20", "venture round (unnamed)", 12500000, None, None, BZ2, "press")],
           note="Stage pass 2026-09-30: BuzzNet's rounds as the Sutter Hill book records them carry no series names "
                "and do not tie NEA to its 2007 entry."))

s = "baihe"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Baihe."))

s = "luminary-micro"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Luminary Micro."))

s = "redbaby"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Redbaby."))

s = "vertica"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round; TechCrunch's 2011 report gives only $30.5M raised in total."))

s = "clearcommerce"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round of ClearCommerce."))

s = "xensource"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of XenSource."))

s = "psyadon-pharmaceuticals"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Psyadon."))

s = "elance-inc"
TC_EL = ("https://techcrunch.com/2012/01/24/"
         "online-job-marketplace-elance-raises-16m-from-kleiner-perkins-nea-and-the-stripes-group/")
L.append(C(s, stage="undetermined",
           rounds=[rnd("2012-01-24", "unnamed", 16000000, "Stripes Group", True, TC_EL, "press")],
           note="Stage pass 2026-09-30: TechCrunch names NEA an existing investor in the 2012 round; the 2003 round "
                "NEA entered is not named."))

s = "motion-computing"
WM = jl.W("Motion Computing")
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd("2002", "first funding (unnamed)", 6500000, None, None, WM, "press"),
    rnd("2003", "second funding round (unnamed)", 11200000, None, None, WM, "press"),
    rnd("2004", "Series C", 25000000, None, None, WM, "press"),
    rnd("2008", "Series D", 6000000, None, None, WM, "press"),
    rnd("2009", "unnamed", 5600000, None, None, WM, "press")], FD(s)),
    note="Stage pass 2026-09-30: Wikipedia puts the second funding round ($11.2M) in 2003, the firm's own year, "
         "before a 2004 Series C, but no source ties NEA to a round."))

s = "bridgepoint-medical"
L.append(C(s, stage="undetermined", rounds=FD(s),
           note=SRCH + " name no round of the firm's 2002 entry; the Form D rounds are later."))

s = "neoteris"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Neoteris."))

s = "boingo-wireless"
BO = "https://www.sec.gov/Archives/edgar/data/1169988/000104746911004582/a2203889z424b4.htm"
L.append(C(s, stage="undetermined",
           rounds=[rnd(None, x + " convertible preferred", None, None, None, BO, "filing")
                   for x in ("Series A", "Series A-2", "Series B", "Series C")],
           note="Stage pass 2026-09-30: the 2011 prospectus lists Series A, A-2, B and C preferred but neither dates "
                "them nor ties NEA 10 to a series."))

s = "nanoopto"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round of NanoOpto."))

s = "vitae-pharmaceuticals"
VT = FTS_FILE("Vitae", "filename20")
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=VT, stage_conf="medium", entry_date="2001",
           rounds=MERGE([rnd("2001", "Series A-2 preferred", None, None, True, VT, "filing"),
                         rnd(None, "Series B preferred", None, None, True, VT, "filing"),
                         rnd(None, "Series C preferred", None, None, True, VT, "filing"),
                         rnd(None, "Series D preferred", None, None, False, VT, "filing")], FD(s)),
           note="The capitalization table filed with the 2014 draft registration shows NEA 10 holding Series A-2, B "
                "and C preferred and none of the common or Series A-1, and NEA Ventures 2001 only Series A-2, so NEA "
                "entered at the Series A in 2001, the firm's own year; the table gives no dates, hence medium."))

s = "caremark-rx-inc"
# The f1 fix pass recorded NEA VI's MedPartners Series A (1993) after this pass took its snapshot, and the first run
# of this file wrote undetermined over it; this line restores the f1 stage from the record it left on disk.
F1 = next(json.loads(x) for x in (jl.Q / "f1.out.jsonl").read_text().splitlines()
          if x.strip() and json.loads(x).get("slug") == s and "verdict" not in json.loads(x))
L.append(C(s, stage=F1["entry_stage"], stage_src=F1["entry_stage_source"], stage_cite=F1["entry_stage_citation"],
           stage_conf=F1["entry_stage_confidence"], entry_date=F1["entry_date"], rounds=F1["funding_rounds"],
           note="Correction: the f1 pass's Series A entry (NEA VI in MedPartners' 1993 Series A, S-4 of 1996) stands; "
                "the stage pass line before this one was written from an older snapshot."))

s = "entevo"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round of Entevo."))

s = "medicalogic-medscape-inc"
ML = "https://www.sec.gov/Archives/edgar/data/923899/0000912057-99-009044.txt"
L.append(C(s, stage="undetermined",
           rounds=[rnd("1996-05", "Series C preferred (additional closing)", 5638433, None, True, ML, "filing")],
           note="MedicaLogic's 1999 prospectus shows NEA IV buying Series C in May 1996, but NEA was already a 5% holder "
                "(Ronald Kase a director since July 1994), so the entry round is earlier and not named."))

s = "ultradns"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of UltraDNS."))

s = "centerbeam"
L.append(C(s, stage="undetermined", rounds=FD(s),
           note=SRCH + " name no round of the firm's 1999 entry; the Form D round is from 2013."))

s = "platinum-software-corp"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " show only NEA's 1999 13G on a company already listed; no private round is on record."))

s = "supplybase"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of SupplyBase."))

s = "xros"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Xros."))

s = "cardima-inc"
CA = "https://www.sec.gov/Archives/edgar/data/1022570/0001012870-97-001126.txt"
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=CA, stage_conf="high", entry_date="1993-05",
           rounds=[rnd("1993-05", "Series A preferred", 2999969, None, True, CA, "filing"),
                   rnd("1993-06", "Series B preferred (Target Therapeutics exchange)", None, None, False, CA, "filing"),
                   rnd("1994-06", "Series C preferred", None, None, True, CA, "filing"),
                   rnd("1996-01", "Series D preferred", None, None, True, CA, "filing"),
                   rnd("1997-03", "Series E preferred", None, None, True, CA, "filing")],
           note="Cardima's 1997 IPO prospectus lists New Enterprise Associates V (with Catalyst Ventures) among the "
                "Series A buyers; the Series A was sold for cash in May 1993."))

s = "growth-networks"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Growth Networks."))

s = "quantum-bridge-communications"
QB = "https://www.sec.gov/Archives/edgar/data/1114246/000095013500005482/b37459qbs-1.txt"
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=QB, stage_conf="high", entry_date="1998-11",
           rounds=[rnd("1998-11", "Series A convertible preferred (closes to March 1999)", 6250000, None, True, QB,
                       "filing"),
                   rnd("1999-08", "Series B convertible preferred", 15999994, None, True, QB, "filing"),
                   rnd(None, "Series C convertible preferred", None, None, True, QB, "filing")],
           note="Quantum Bridge's 2000 S-1: funds affiliated with NEA bought 3,740,000 of the 6,250,000 Series A shares "
                "sold between November 1998 and March 1999, then Series B and C."))

s = "wnp-communications"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of WNP Communications."))

s = "fibex"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Fibex."))

s = "innovasive-devices-inc"
IV = "https://www.sec.gov/Archives/edgar/data/1003608/0000927016-96-000370.txt"
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=IV, stage_conf="high", entry_date="1994-02",
           rounds=[rnd("1994-02", "Series A preferred", None, None, True, IV, "filing"),
                   rnd("1995-10", "Series B preferred", None, None, True, IV, "filing")],
           note="Innovasive's 1996 IPO prospectus: New Enterprise Associates VI bought 538,720 Series A shares in "
                "February 1994 for $2.0M and Series B in October 1995."))

s = "penederm-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "sonic-innovations"
SO = "https://www.sec.gov/Archives/edgar/data/1105982/0001012870-00-002495.txt"
L.append(C(s, stage="Growth", stage_src="web_verified", stage_cite=SO, stage_conf="high", entry_date="1997-10",
           rounds=[rnd("1997-05", "Series B preferred", None, None, False, SO, "filing"),
                   rnd("1997-10", "Series C preferred", None, None, True, SO, "filing"),
                   rnd("1998-10", "Series D preferred", None, None, True, SO, "filing"),
                   rnd(None, "convertible notes", None, None, True, SO, "filing")],
           note="Sonic Innovations' 2000 prospectus: NEA entities bought Series C (issued October 1997) and Series D, "
                "and none of the May 1997 Series B, so NEA entered at the Series C in its own year 1997."))

s = "ebenx"
EB = "https://www.sec.gov/Archives/edgar/data/1095825/0001045969-99-000933.txt"
L.append(C(s, stage="Growth", stage_src="web_verified", stage_cite=EB, stage_conf="high", entry_date="1996-03-19",
           rounds=[rnd("1996-03-19", "Series B preferred", 4500016, None, True, EB, "filing"),
                   rnd("1999-05-03", "Series C preferred", 5500004, None, True, EB, "filing"),
                   rnd("1999-06-09", "Series C preferred (second close)", 5000000, None, None, EB, "filing")],
           note="eBenX's 1999 prospectus: on 1996-03-19 New Enterprise Associates VI bought 424,630 of the 636,945 "
                "Series B shares sold, in the year John Nehra joined the board, so NEA entered at the Series B."))

s = "long-term-care-group"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Long Term Care Group."))

s = "webmd-healtheon"
HE = "https://www.sec.gov/Archives/edgar/data/1009575/0001047469-99-005587.txt"
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=HE, stage_conf="high", entry_date="1996-01-26",
           rounds=[rnd("1996-01-26", "Series A preferred", 5142500, None, True, HE, "filing"),
                   rnd("1996-10-01", "Series B preferred", 6000000, None, True, HE, "filing"),
                   rnd("1997-07-01", "Series C preferred (bridge notes converted)", None, None, True, HE, "filing")],
           note="Healtheon's 1999 IPO prospectus: New Enterprise Associates VI bought 2,000,000 of the 10,285,000 "
                "Series A shares sold on 1996-01-26, then Series B and the 1997 bridge."))

s = "virata"
VI = "https://www.sec.gov/Archives/edgar/data/1094371/0001012870-99-004291.txt"
L.append(C(s, stage="undetermined",
           rounds=[rnd("1997-12", "bridge notes convertible into Series D", 2642980, None, True, VI, "filing"),
                   rnd("1998-06", "Series D preference shares", 27259027, None, True, VI, "filing")],
           note="Virata's 1999 prospectus shows NEA in the 1997-98 bridge and the June 1998 Series D, and NEA among the "
                "holders whose Series B and C shares converted then; Peter Morris joined the board in May 1995, but "
                "the series NEA first bought is not stated."))

s = "gynecare"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "geltex-pharmaceuticals"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "vitesse-semiconductor"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round." + PRE))

s = "spectrian"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "silicon-graphics"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "cardiovascular-imaging-systems"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

s = "applix"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round." + PRE))

got = [x["slug"] for x in L]
assert got == Q, [a for a in Q if a not in got] + [b for b in got if b not in Q]
jl.write("s1b", L)
