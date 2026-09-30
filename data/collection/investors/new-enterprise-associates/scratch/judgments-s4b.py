"""PRO-100 NEA stage pass, tag s4, second half (51 rows). Entry-round research per STAGE-BRIEF.md.
Rounds already on file are kept and the new ones appended (funding_rounds replaces on record)."""
import json

import judge_lib as jl
from judge_lib import cls, rnd, NEWS

CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def R(slug, *new):
    """Rounds on file plus the new ones (deduplicated on date and round)."""
    out = list((CLS.get(slug) or {}).get("funding_rounds") or [])
    for n in new:
        if not any(o.get("date") == n["date"] and o.get("round") == n["round"] for o in out):
            out.append(n)
    return out


# SEC documents read this pass (URLs printed by scratchpad/s4/edg.py from each registrant's EDGAR index)
IASIA_424B4 = "https://www.sec.gov/Archives/edgar/data/1110992/0001012870-00-004145.txt"
VERSICOR_424B4 = "https://www.sec.gov/Archives/edgar/data/1052547/0000912057-00-034513.txt"
CARRIER_S1 = "https://www.sec.gov/Archives/edgar/data/1018074/0000927356-98-000919.txt"
COM21_S1 = "https://www.sec.gov/Archives/edgar/data/945379/0000891618-98-001138.txt"
CYBER_S1 = "https://www.sec.gov/Archives/edgar/data/1019156/0000891618-96-001923.txt"
FOX_424B4 = "https://www.sec.gov/Archives/edgar/data/1217688/000119312504179837/d424b4.htm"
GLIA_S1A = "https://www.sec.gov/Archives/edgar/data/885741/0000950152-96-002537.txt"
BROADVIEW_S1A = "https://www.sec.gov/Archives/edgar/data/1104358/0000950130-00-001958.txt"
PCORDER_424B4 = "https://www.sec.gov/Archives/edgar/data/1068726/0001012870-99-000660.txt"
NETSOLVE_S1 = "https://www.sec.gov/Archives/edgar/data/1071342/0000950109-98-004752.txt"
CELERIS_424B4 = "https://www.sec.gov/Archives/edgar/data/946994/0000950131-96-003156.txt"
ODI_S1 = "https://www.sec.gov/Archives/edgar/data/1014955/0000950135-96-002496.txt"

REGDEX = "EDGAR holds only paper Regulation D notices (REGDEX) for it, no prospectus"
NOREG = "EDGAR company search finds no registrant"
L = []

# ---- staged rows (IPO prospectuses)
L.append(cls("iasiaworks-inc", stage="Series A", stage_src="web_verified", stage_cite=IASIA_424B4, stage_conf="high",
             entry_date="1995-08",
             rounds=R("iasiaworks-inc",
                      rnd("1995-08", "Series A", 3375000, None, True, IASIA_424B4, "filing"),
                      rnd("1996-10", "Series B", 10173851, None, True, IASIA_424B4, "filing"),
                      rnd("1998-08", "Series C", 9807047, None, True, IASIA_424B4, "filing"),
                      rnd("1999-08", "Series D", 85000000, None, True, IASIA_424B4, "filing")),
             note="Stage pass (s4): the 2000 IPO prospectus (certain transactions) says the company issued Series A "
                  "preferred in August and November 1995 to investors including New Enterprise Associates VI, whose "
                  "general partner Peter Morris co-founded it and joined the board in August 1995; NEA also bought "
                  "the B, C and D. Entry is the 1995 Series A."))

L.append(cls("carrier-access-corporation", stage="Growth", stage_src="web_verified", stage_cite=CARRIER_S1,
             stage_conf="high", entry_date="1997-09",
             rounds=R("carrier-access-corporation",
                      rnd("1996-06", "Series A", 3463062, None, False, CARRIER_S1, "filing"),
                      rnd("1997-09", "Series B", 12564291, None, True, CARRIER_S1, "filing")),
             note="Stage pass (s4): the 1998 S-1 (certain transactions) shows NEA VII, NEA Presidents Fund and NEA "
                  "Ventures 1997 with no Series A (June 1996) and 1,013,026 shares of the Series B sold in September "
                  "1997 at $4.99, the firm's 1997 year; the entry is the Series B (Growth)."))

L.append(cls("com21", stage="Series A", stage_src="web_verified", stage_cite=COM21_S1, stage_conf="high",
             entry_date="1994-06",
             rounds=R("com21",
                      rnd("1994-06", "Series A", 2852965, None, True, COM21_S1, "filing"),
                      rnd("1994-09", "Series B", 500000, None, False, COM21_S1, "filing"),
                      rnd("1995-05", "Series C", 500000, None, False, COM21_S1, "filing"),
                      rnd("1995-05", "Series D", 7250000, None, True, COM21_S1, "filing"),
                      rnd("1996-04", "Series F", 23245840, None, True, COM21_S1, "filing"),
                      rnd("1997-07", "Series G", 23099588, None, True, COM21_S1, "filing"),
                      rnd("1997-08", "Series E (warrant exercise)", 1630000, None, True, COM21_S1, "filing")),
             note="Stage pass (s4): the 1998 S-1 (certain transactions) shows NEA VI buying 632,912 shares of the "
                  "Series A sold in June 1994 at $1.58, with Kramlich a director from May 1994, and later the D to G "
                  "series; entry is the 1994 Series A."))

L.append(cls("cybermedia", stage="Growth", stage_src="web_verified", stage_cite=CYBER_S1, stage_conf="high",
             entry_date="1995",
             rounds=R("cybermedia",
                      rnd(None, "Series A", 1035880, None, False, CYBER_S1, "filing"),
                      rnd("1995", "Series B", 4460000, None, True, CYBER_S1, "filing"),
                      rnd(None, "Series C", 5000001, None, True, CYBER_S1, "filing")),
             note="Stage pass (s4): the 1996 S-1 (certain transactions) shows NEA VI and NEA Ventures 1995 with no "
                  "Series A or Series A warrants, 1,800,000 Series B shares at $0.70 and 140,254 Series C shares; "
                  "Peter Morris joined the board in September 1995 as the Series B holders' designee. Entry is the "
                  "Series B (Growth), dated by the firm's 1995 year."))

# ---- undetermined, with what this pass found
L.append(cls("american-pathology-partners", stage="undetermined", rounds=R("american-pathology-partners"),
             note="Stage pass (s4): nothing beyond the April 2008 $75M equity commitment, which names no round."))

for s in ("arch-rock-corporation",):
    L.append(cls(s, stage="undetermined", rounds=R(s),
                 note="Stage pass (s4): EDGAR has the registrant but no prospectus; nothing names a round."))

for s in ("bethesda-research-laboratories", "hospital-group-of-america-inc", "nazomi-communications-inc",
          "primax-recoveries-inc"):
    L.append(cls(s, stage="undetermined", rounds=R(s),
                 note=f"Stage pass (s4): {NOREG}; the firm's historical list carries no round word."))

L.append(cls("uni-power-group", stage="undetermined", rounds=R("uni-power-group"),
             note=f"Stage pass (s4): Google News ('Uni-Power' NEA) returned nothing and {NOREG}."))

L.append(cls("aciex", stage="undetermined",
             rounds=R("aciex", rnd("2011-08-02", "minority stake (Akorn)", None, "Akorn", None,
                                   NEWS("aciex", "Akorn Acquires Minority"), "press")),
             note="Stage pass (s4): Google News ('Aciex' Series A, 'Aciex Therapeutics') shows only Akorn's 2011 "
                  "minority stake; NEA's 2007 round stays unnamed."))

L.append(cls("ivantis", stage="undetermined",
             rounds=R("ivantis", rnd("2017-01-10", "unnamed", 25000000, None, None,
                                     NEWS("ivantis", "bags $25M"), "press")),
             note="Stage pass (s4): Google News ('Ivantis' Series A, NEA) shows only the 2017 $25M round; the 2007 "
                  "founding round and the 2008 paper Regulation D notices name no series."))

L.append(cls("smartdrive-systems", stage="undetermined",
             rounds=R("smartdrive-systems",
                      rnd("2007-01-23", "Series C", None, "Oak Investment Partners", False,
                          NEWS("smartdrive-systems", "Completes Series C"), "press"),
                      rnd("2015-03-30", "unnamed", 50000000, None, None,
                          NEWS("smartdrive-systems", "raises $50M in funding"), "press")),
             note="Stage pass (s4): Work Truck Online (2007-01-23) lists the Series C investors as Oak (new), "
                  "Revolution, Founders Fund and Western Technology, without NEA; NEA's 2007 entry therefore came "
                  "after that close, a later C close or a later round (either reads Growth), but no source names it."))

L.append(cls("teracent", stage="undetermined", rounds=R("teracent"),
             note="Stage pass (s4): Google News ('Teracent' Series A, funding) returned nothing; EDGAR shows only "
                  "paper Regulation D notices before the 2009 Form D."))

L.append(cls("eci-acquisition-holdings", stage="undetermined", rounds=R("eci-acquisition-holdings"),
             note="Stage pass (s4): Google News ('ECI Software' NEA) returned nothing on the 2006 transaction."))

L.append(cls("pharmos", stage="undetermined", rounds=R("pharmos"),
             note="Stage pass (s4): no round to name; the stake came as consideration for Vela Pharmaceuticals (D8)."))

L.append(cls("snaptell-inc", stage="undetermined", rounds=R("snaptell-inc"),
             note=f"Stage pass (s4): Google News ('SnapTell' Series A, funding) returned nothing and {REGDEX}."))

L.append(cls("broadview-network-holdings", stage="undetermined",
             rounds=R("broadview-network-holdings",
                      rnd("1999-04-23", "Series C", None, None, None, BROADVIEW_S1A, "filing"),
                      rnd("2000-02", "Series D", None, None, None, BROADVIEW_S1A, "filing")),
             note="Stage pass (s4): the withdrawn 2000 S-1 already lists NEA VII, NEA Presidents Fund and NEA Ventures "
                  "1998 as 12.8% holders with board designation rights, so NEA entered by 1999, well before the "
                  "firm's 2005 year; the prospectus does not say which of the Series A to D NEA bought."))

L.append(cls("surgrx", stage="undetermined", rounds=R("surgrx"),
             note=f"Stage pass (s4): Google News ('SurgRx' Series, funding) returned nothing and {REGDEX}."))

L.append(cls("picaboo", stage="undetermined", rounds=R("picaboo"),
             note=f"Stage pass (s4): Google News ('Picaboo' Series A, funding) returned only namesakes and {REGDEX}."))

L.append(cls("xfire", stage="undetermined", rounds=R("xfire"),
             note=f"Stage pass (s4): Google News ('Xfire' Series A, funding) and Wikipedia name no 2004 round, and "
                  f"{REGDEX}."))

L.append(cls("luxn", stage="undetermined", rounds=R("luxn"),
             note="Stage pass (s4): nothing to add; the acquirer's filing names no round."))

L.append(cls("teneros", stage="undetermined", rounds=R("teneros"),
             note="Stage pass (s4): Google News ('Teneros' Series A, funding) returned nothing on the 2003 round."))

L.append(cls("hydra-biosciences-inc", stage="undetermined", rounds=R("hydra-biosciences-inc"),
             note=f"Stage pass (s4): {REGDEX}; no round is named."))

L.append(cls("aeluros", stage="undetermined", rounds=R("aeluros"),
             note=f"Stage pass (s4): {REGDEX}; Wikipedia names no round."))

L.append(cls("versicor-inc-ca", stage="undetermined",
             rounds=R("versicor-inc-ca",
                      rnd("1995-07", "Series A (issued to Sepracor for a license)", None, "Sepracor", False,
                          VERSICOR_424B4, "filing"),
                      rnd("1997-12-09", "Series B (Sepracor notes converted)", 9530150, "Sepracor", False,
                          VERSICOR_424B4, "filing"),
                      rnd("1997-12-09", "Series C", 22000000, None, None, VERSICOR_424B4, "filing"),
                      rnd("1999-03-31", "Series D-1", 3750000, None, False, VERSICOR_424B4, "filing"),
                      rnd("1999-03-31", "Series E-1", 3000000, None, False, VERSICOR_424B4, "filing"),
                      rnd("1999-10-29", "Series F", 40183189, None, None, VERSICOR_424B4, "filing")),
             note="Stage pass (s4): the 2000 IPO prospectus lists the preferred history (A and B to parent Sepracor, "
                  "the $22M Series C to private investors in December 1997, D-1 and E-1 to strategic investors, the "
                  "$40.2M Series F in 1999) and NEA VII as a 9.7% holder with Thomas McConnell a director since 1997, "
                  "but it does not tie NEA to a series; the December 1997 Series C is the likely entry, unconfirmed."))

L.append(cls("aronex-pharmaceuticals-inc", stage="undetermined", rounds=R("aronex-pharmaceuticals-inc"),
             note="Stage pass (s4): only NEA's 2000 13G is on EDGAR; no round is named."))

for s in ("e2o-communications", "guardent", "polyserve"):
    L.append(cls(s, stage="undetermined", rounds=R(s), note=f"Stage pass (s4): {REGDEX}; no round is named."))

L.append(cls("aquila-biopharmaceuticals-inc", stage="undetermined", rounds=R("aquila-biopharmaceuticals-inc"),
             note="Stage pass (s4): EDGAR holds only NEA's 1999 and 2000 13G filings for this listed company; no round "
                  "is named."))

for s in ("cyras-systems", "sierra-atlantic", "astral-point", "berkeley-networks", "infogear-technology",
          "origin-medsystems", "bay-networks-wellfleet"):
    L.append(cls(s, stage="undetermined", rounds=R(s), note=f"Stage pass (s4): {NOREG}; no round is named."))

L.append(cls("wayport", stage="undetermined", rounds=R("wayport"),
             note=f"Stage pass (s4): {REGDEX} (it never filed an S-1); no round is named."))

L.append(cls("fox-hollow-technologies", stage="undetermined",
             rounds=R("fox-hollow-technologies",
                      rnd("2001", "Series C", None, None, True, FOX_424B4, "filing"),
                      rnd("2003", "Series D", None, None, True, FOX_424B4, "filing"),
                      rnd("2004", "Series E", None, None, True, FOX_424B4, "filing")),
             note="Stage pass (s4): the 2004 IPO prospectus shows NEA VII buying the 2001 Series C, the 2003 Series D "
                  "and the 2004 Series E, but its related-party section starts in 2001; Ryan Drant joined the board "
                  "in February 1998, so NEA entered in an earlier series the prospectus does not name."))

L.append(cls("pcorder", stage="undetermined", rounds=R("pcorder"),
             note="Stage pass (s4): the 1999 IPO prospectus has NEA's Peter Barris a director since June 17, 1998, but "
                  "lists no NEA holding or NEA purchase; the firm's stake may sit in parent Trilogy, not established."))

L.append(cls("summit-medical-systems-inc-mn", stage="undetermined", rounds=R("summit-medical-systems-inc-mn"),
             note="Stage pass (s4): the 1996 follow-on prospectus lists NEA VI with Catalyst Ventures as a 10.2% holder "
                  "and John Nehra a director, but no preferred history."))

L.append(cls("gliatech-inc", stage="undetermined",
             rounds=R("gliatech-inc",
                      rnd("1994-07-29", "Series D", 3426428, None, True, GLIA_S1A, "filing"),
                      rnd("1994-10-14", "Series E", 1489500, "Johnson & Johnson Development", False, GLIA_S1A,
                          "filing"),
                      rnd("1995-06-30", "Series F", 4653089, None, None, GLIA_S1A, "filing")),
             note="Stage pass (s4): the 1996 follow-on prospectus shows NEA V buying 400,000 Series D shares in July "
                  "1994 but covers only the last few years; the company dates from 1988 and NEA's earlier series, if "
                  "any, are not named."))

L.append(cls("object-design-inc", stage="undetermined", rounds=R("object-design-inc"),
             note="Stage pass (s4): the 1996 S-1 lists Series A to J preferred by holder count only, with NEA V a 7.8% "
                  "holder and Mark Marks a director since 1990; no series is tied to NEA."))

L.append(cls("sequana-therapeutics-inc", stage="undetermined", rounds=R("sequana-therapeutics-inc"),
             note="Stage pass (s4): its 1995 IPO prospectus is not on EDGAR (the index starts with the 1997 10-K)."))

L.append(cls("transvascular", stage="undetermined", rounds=R("transvascular"),
             note=f"Stage pass (s4): {REGDEX}; no round is named."))

L.append(cls("dura-pharmaceuticals", stage="undetermined", rounds=R("dura-pharmaceuticals"),
             note="Stage pass (s4): Dura appears on EDGAR from 1995 as a listed company (13G filings), so the 1993 "
                  "purchase may have been into a listed company; no round is named."))

L.append(cls("conceptus", stage="undetermined", rounds=R("conceptus"),
             note="Stage pass (s4): its 1996 IPO prospectus is not on EDGAR (the index starts with the 1997 10-K)."))

L.append(cls("netsolve", stage="undetermined", rounds=R("netsolve"),
             note="Stage pass (s4): the 1998 S-1 names NEA IV as a 24.4% holder and Kramlich a director since April "
                  "1991, but gives no preferred history."))

L.append(cls("nationwide-remittance-centers", stage="undetermined", rounds=R("nationwide-remittance-centers"),
             note=f"Stage pass (s4): {NOREG}; no round is named. Same company as the nrc row."))

jl.write("s4b", L)
