#!/usr/bin/env python3
"""PRO-167 Tiger Global, class sweep (COLLECTION.md 8, duty 9), chunk b: wiz-freight's status (The Loadstar,
September 2025), and seven undetermined rows where the sweep found rounds but no page names the round Tiger
entered. Their stage stays undetermined; the rounds found are kept on the row (COLLECTION.md 6, PRO-143) with a note.
Run: NQ_TAG=sw python3 swb.py"""
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


# URLs printed by the tools run in this sweep (WebSearch results), fetched and read.
INC42_CARTRADE = "https://inc42.com/buzz/cartrade-funding/"
TC_WIKIMART = "https://techcrunch.com/2010/08/09/tiger-global-acquires-50-of-russian-online-mall-wikimart-for-5m/"

L = []

# ---- Wiz Freight: collapse reported by The Loadstar (September 2025)
LOADSTAR = NEWS("wiz-freight", "Another Indian digital forwarder bites the dust")
L.append(cls("wiz-freight", status="defunct", rng="below_1b",
             note="Status, class sweep 2026-09-29: The Loadstar (2025-09-17, 'Another Indian digital forwarder "
                  "bites the dust', " + LOADSTAR + ") reports that Wiz Freight had steadily suspended export "
                  "bookings, that container lines withdrew its credit lines and airlines stopped issuing it air "
                  "waybill stock, that executives left, and that local bookings now route through TVS Supply Chain "
                  "Solutions, which took on some of its staff; it counts Wiz among the failed Indian logistics "
                  "start-ups. No sale of the business is reported (a TVS deal is only rumoured), so the row reads "
                  "defunct (COLLECTION.md 6: a business that ended; staff taken on by another firm do not make it "
                  "acquired). No later report of a revival or sale in the two searches run (Bing, Google News)."))

# ---- CarTrade: Tiger led the 2011 'third round'; not a stage word
L.append(cls("cartrade",
             rounds=[rnd("2011", "Third round (not labelled)", 13000000, "Tiger Global Management", True,
                         INC42_CARTRADE),
                     OLD("cartrade", "2014-10")],
             note="Class sweep 2026-09-29: inc42 (2014-10-13) says MXC Solutions, CarTrade's operator, raised $13M "
                  "in 2011 in 'its third round of funding led by venture capital firm Tiger Global Management, "
                  "with participation from existing investor Canaan Partners', so Tiger's entry is that 2011 round. "
                  "'Third round' is not a stage word and the two earlier Canaan rounds are not labelled in what was "
                  "read, so the stage stays undetermined."))

# ---- CommonFloor: Tiger in the Series B of October 2012
VCC13 = OLD("commonfloor", "2013-07-05")["source"]
L.append(cls("commonfloor",
             rounds=[rnd("2012-10", "Series B", None, "Accel Partners, Tiger Global", True, VCC13),
                     OLD("commonfloor", "2013-07-05"), OLD("commonfloor", "2014-01"), OLD("commonfloor", "2014-09")],
             note="Class sweep 2026-09-29: VCCircle's Series C report (2013-07-05) adds that in October 2012 "
                  "CommonFloor 'raised an undisclosed amount in Series B from Accel Partners and Tiger Global', so "
                  "Tiger was in by the Series B; whether it was also in the Series A is not on record, so the stage "
                  "stays undetermined (Growth if Tiger first came in at the B)."))

# ---- HeadSpin: Tiger in the Series C of February 2020
FP = NEWS("headspin", "HeadSpin Announces $60M Series C")
TC24 = NEWS("headspin", "PE firm PartnerOne paid $28M")
L.append(cls("headspin",
             rounds=[rnd("2020-02-24", "Series C", 60000000, "Dell Technologies Capital, ICONIQ Capital", True, FP,
                         "company"),
                     rnd("2024-07", "Sale to PartnerOne (about $28.2M)", None, "PartnerOne", None, TC24)],
             note="Class sweep 2026-09-29: HeadSpin's release of 2020-02-24 (Financial Post copy) announces the $60M "
                  "Series C at $1.16B led by Dell Technologies Capital and ICONIQ 'with participation from "
                  "institutional investors Tiger Global Management, Kearny Jackson, and Alpha Square Group'. It does "
                  "not say whether Tiger was new, and the Series A and B investors were not read, so the stage stays "
                  "undetermined (Growth unless Tiger was in the A)."))

# ---- FORT Robotics: Tiger led the Series B; the $13M round of March 2021 is not tied to Tiger
RR = NEWS("fort-robotics", "FORT Robotics brings in $25M in Series B funding")
L.append(cls("fort-robotics",
             rounds=[rnd("2021-03", "Round of $13M (investors not named)", 13000000, None, None, RR),
                     rnd("2022-07-13", "Series B", 25000000, "Tiger Global", True, RR),
                     OLD("fort-robotics", "2026-08-18")],
             note="Class sweep 2026-09-29: The Robot Report (2022-07-13) says Tiger Global led the $25M Series B and "
                  "that FORT's round before it, $13M, closed in March 2021, without naming that round's investors; "
                  "whether Tiger was in the 2021 round is not on record, so the stage stays undetermined."))

# ---- Wikimart: Tiger's first deal bought 50%; no round label
L.append(cls("wikimart",
             rounds=[rnd("2009-06", "Angel round", 700000, "Western business angels", False, TC_WIKIMART),
                     rnd("2010-05", "Purchase of a 50% stake for $5M (not labelled)", 5000000, "Tiger Global", True,
                         TC_WIKIMART),
                     OLD("wikimart", "2011"), OLD("wikimart", "2012-03"), OLD("wikimart", "2014-10")],
             note="Class sweep 2026-09-29: no page names Tiger's first round, so the stage stays undetermined. "
                  "TechCrunch (2010-08-09, citing Vedomosti) reports that Tiger bought a 50% stake for $5M in a "
                  "deal done in May 2010 (Russian Wikipedia puts Tiger's first money, about $5M, in late 2009), "
                  "after a $0.7M angel round in June 2009: Tiger's first cheque bought half the company, which bears "
                  "on the control-position question already listed for Erik."))

# ---- INDmoney: Tiger's August 2019 round sits between the October 2018 seed and the Series C
VCC19 = NEWS("indmoney", "Tiger Global invests in Ibibo founder")
INC42C = NEWS("indmoney", "INDwealth Is Raising $12 Mn Series C")
SERIES_C = dict(OLD("indmoney", "2020-01-27"), firm_in_round=True, source=INC42C, date="2020-01-23")
L.append(cls("indmoney",
             rounds=[rnd("2018-10", "Seed", 30000000, "Steadview Capital", False, VCC19),
                     OLD("indmoney", "2019-08-22"), SERIES_C, OLD("indmoney", "2022-01-17")],
             note="Class sweep 2026-09-29: VCCircle (2019-08-22) places Tiger's $15M after a $30M seed from Steadview "
                  "Capital in October 2018, and inc42 (2020-01-23) shows Tiger allotted Series C preference shares "
                  "in January 2020, calling the $30M and the $15M 'its last two rounds'. Tiger's August 2019 round "
                  "sits between the seed and the Series C and no page names it, so the stage stays undetermined."))

# ---- GetNinjas: the June 2015 R$40M round 'marks the entry' of Tiger; not labelled
BAG = NEWS("getninjas-holdings-ltd", "GetNinjas: aporte de R$ 40")
L.append(cls("getninjas-holdings-ltd",
             rounds=[rnd("2015-06-17", "Round of R$40M (not labelled)", None, None, True, BAG),
                     OLD("getninjas-holdings-ltd", "2015-06-15")],
             note="Class sweep 2026-09-29: Baguete (2015-06-17) says the R$40M round of June 2015 'marca a entrada da "
                  "Tiger Global Management' beside Monashees and Kaszek, so that round is Tiger's entry; neither "
                  "Baguete nor the Form D names it, so the stage stays undetermined."))

jl.write("sweep-b", L)
