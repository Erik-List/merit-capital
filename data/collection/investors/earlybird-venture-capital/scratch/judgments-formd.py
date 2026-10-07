#!/usr/bin/env python3
"""The 15 Form D name-match rows, judged cluster-first (COLLECTION.md s3): one
ruling per person, then every row that person explains. None of the fifteen is
on any Earlybird list, live or archived, and no round names an Earlybird fund."""
import judge_lib as J

CARNOT = "https://health.earlybird.com/members/lionel-carnot"
GROS = "https://health.earlybird.com/members/florent-gros"
L = []
# Lionel Carnot: Bay City Capital until 2016
for slug, co, yrs in [("interleukin-genetics-inc", "Interleukin Genetics", "2013 to 2016"),
                      ("madrigal-pharmaceuticals-inc", "Madrigal Pharmaceuticals", "2016"),
                      ("merus-n-v", "Merus", "2017 to 2018"),
                      ("nabsys-inc", "NABsys", "2014"),
                      ("nexus-dx-inc", "Nexus Dx", "2009")]:
    L.append(J.verdict(slug, "not_member",
        f"Form D name-match only: Lionel Carnot is a related person on {co}'s filings of {yrs}. The firm's own page: "
        "'Lionel joined Earlybird Health as a Partner in 2016 ... Prior to Earlybird, he was Managing Director at Bay City Capital'. "
        f"{co} is a Bay City Capital company, the seat travelled with him (T4: a seat is dated against the person's firm), "
        "and no Earlybird list or round names it.", ec="formd_adjudicated", conf="high", cite=CARNOT))
# Florent Gros: Novartis Venture Fund until 2020
for slug, co, yrs in [("adicet-bio-inc", "Adicet Bio", "2016 to 2018"),
                      ("gensight-biologics-s-a", "GenSight Biologics", "2015"),
                      ("kanyos-bio-inc", "Kanyos Bio", "2015"),
                      ("vaxin-inc", "Vaxin (Altimmune)", "2015")]:
    L.append(J.verdict(slug, "not_member",
        f"Form D name-match only: Florent Gros is a related person on {co}'s filings of {yrs}. The firm's own page: "
        "'Florent joined Earlybird Health as a Partner in 2020 ... he spent 15 years at the Novartis Venture Fund'. "
        f"The seat is the Novartis Venture Fund's (T4), years before his Earlybird tenure, and no Earlybird list or round names {co}.",
        ec="formd_adjudicated", conf="high", cite=GROS))
# Konstantin Guericke: personal directorships of a LinkedIn co-founder
for slug, co, why in [
        ("doximity-inc", "Doximity", "he co-founded Doximity's predecessor network and sat on its board personally (2012 filing)"),
        ("rallypoint-networks-inc", "RallyPoint Networks", "a personal board seat (2015 filing)"),
        ("whitepages-inc", "Whitepages", "a personal board seat (2015 filing)")]:
    L.append(J.verdict(slug, "not_member",
        f"Form D name-match only: Konstantin Guericke, a LinkedIn co-founder and an Earlybird partner 2012 to 2015, is a related "
        f"person on {co}'s filing: {why}. No Earlybird list, post or round names {co}; a partner's personal directorship "
        "locates the person, never a firm position (T4, COLLECTION.md s1).", ec="formd_adjudicated", conf="high"))
# Jason Whitmire: BlueYard Capital, his next firm (founded 2016)
for slug, co, why in [
        ("seeqc-inc", "SeeQC", "BlueYard Capital led SeeQC's 2020 seed and he sits on its board for BlueYard (filings 2020 to 2026)"),
        ("spaceknow-inc", "SpaceKnow", "BlueYard Capital led SpaceKnow's 2017 Series A")]:
    L.append(J.verdict(slug, "not_member",
        f"Form D name-match only: Jason Whitmire is a related person on {co}'s filings. He co-founded BlueYard Capital in 2016 "
        f"after Earlybird; {why}. A next-firm deal (T4): no Earlybird list or round names {co}.",
        ec="formd_adjudicated", conf="high"))
L.append(J.verdict("twinstrand-biosciences-inc", "not_member",
    "Form D name-match only, and a homonym: the Michael Schmitt on TwinStrand Biosciences' 2016 filing is its co-founder, a "
    "University of Washington scientist in Seattle, not the Munich Earlybird-X venture partner of the same name (on the "
    "firm's team page from 2021). Three years before that tenure, and no Earlybird list or round names TwinStrand.",
    ec="formd_adjudicated", conf="high"))
J.write("formd-clusters", L)
