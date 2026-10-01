"""PRO-99 Kleiner Perkins, judge j13, batch 25 (19 rows). Evidence: show.py --batch 25, the rows' own Form D
primary documents and KP-vehicle 13G headers read through secget.py, the Healtheon 1999 prospectus on EDGAR,
nq.py / Wikipedia / press pages read before citing. Rulings cited: decisions.md D2, D3, D5, T3/T5, X1; JUDGE-BRIEF
run notes (membership traps)."""
import judge_lib as jl

cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
L = []
W = "web_verified"
U = "undetermined"
_B = jl._base()


def FL(slug, acc):
    """The one Form D link on the row's own formd_links whose URL carries accession `acc`."""
    m = [u.strip() for u in (_B[slug].get("formd_links") or "").split(";") if acc in u]
    if len(m) != 1:
        raise SystemExit(f"FL({slug!r}, {acc!r}) matched {len(m)}")
    return m[0]

# ---------------------------------------------------------------- not_member: seats outside KP years (D5)
L.append(verdict(
    "textio-inc", "not_member",
    "Form D name match only: Aileen Lee is a director on Textio's filings from 2015-12 to 2022, after she left Kleiner "
    "Perkins in 2012 to found Cowboy Ventures (decisions.md D5, seats travel); no KP fund, listing or press names Kleiner "
    "Perkins in a Textio round.",
    ec="formd_adjudicated", conf="high", cite=jl.FORMD_CITE("textio-inc", 2)))

L.append(verdict(
    "weee-inc", "not_member",
    "Form D name match only: Chi-Hua Chien is a director on Weee!'s filings from 2016-05 to 2021, after he left Kleiner "
    "Perkins in 2014 to found Goodwater Capital (decisions.md D5); the firm never listed Weee! and no filing or press names a "
    "KP fund in its rounds.",
    ec="formd_adjudicated", conf="high"))

L.append(verdict(
    "zylo-inc", "not_member",
    "Form D name match only: Matthew Murphy signs Zylo's 2019-09 Series B filing from 2884 Sand Hill Road, Menlo Ventures' "
    "office (Menlo's own book carries Zylo at the Series B); Murphy's seat is Menlo's, not Kleiner Perkins' (decisions.md D5).",
    ec="formd_adjudicated", conf="high", cite=jl.FORMD_CITE("zylo-inc", 3)))

L.append(verdict(
    "veriflow-systems-inc", "not_member",
    "Form D name match only: Matthew Murphy is a director on Veriflow's 2016-06 filing, and that $8.2M Series A 'was led by "
    "Menlo Ventures and included the participation of New Enterprise Associates' (eWeek, 2016-07); Murphy's seat is Menlo's "
    "and no source names Kleiner Perkins (decisions.md D5).",
    ec="formd_adjudicated", conf="high",
    cite="https://www.eweek.com/security/veriflow-raises-8-2m-to-help-verify-network-security/"))

L.append(verdict(
    "uptake-technologies-inc", "not_member",
    "Form D name match only: Raymond Lane is a director from Uptake's 2015-10 filing on, the round Uptake announced as "
    "'$45 million in venture capital led by GreatPoint Ventures' (Wikipedia), Lane's own firm founded in 2015 after he became "
    "partner emeritus at Kleiner Perkins; no KP fund is named in any Uptake round (decisions.md D5).",
    ec="formd_adjudicated", conf="high", cite=jl.W("Uptake (business)")))

L.append(verdict(
    "yaupon-therapeutics-inc", "not_member",
    "Form D name match only: James Huang is a director on Yaupon's 2009-08 and 2010-11 filings (Radnor, PA), before he "
    "joined KPCB China as a managing partner in 2011 (the firm's own partner page); the seat predates his KP years "
    "(decisions.md D5) and nothing names a KP fund.",
    ec="formd_adjudicated", conf="high", cite=FL("yaupon-therapeutics-inc", "0001175706-09-000003")))

L.append(verdict(
    "vertice-pharma-uk-parent-ltd", "not_member",
    "Form D name match only: Noah Knauf signs Vertice Pharma's 2015-12 $300M filing from 450 Lexington Avenue, New York "
    "(Warburg Pincus, with Warburg's Ruoxi Chen beside him), before he became an investing partner at Kleiner Perkins in "
    "2016; the seat is Warburg's (decisions.md D5) and no KP vehicle is named.",
    ec="formd_adjudicated", conf="high", cite=jl.FORMD_CITE("vertice-pharma-uk-parent-ltd", 0)))

L.append(verdict(
    "xsell-technologies-inc", "not_member",
    "Form D name match only: Larry Leisure, a Kleiner Perkins operating partner on the firm's pages 2012-2017, is a "
    "director on XSELL's 2020-07 filing, after those years; an operating partner's own seat is not fund money (decisions.md "
    "D3, D5) and no source names a KP fund in an XSELL round.",
    ec="formd_adjudicated", conf="high", cite=jl.FORMD_CITE("xsell-technologies-inc", 0)))

L.append(verdict(
    "vaxinnate-corp", "not_member",
    "Form D name match only: Thomas Monath appears only on VaxInnate's 2015-09 filing (c/o the company), after his KPCB "
    "years on the firm's pages (2008-2012); the 2009 and 2010 rounds' directors come from New Leaf, HealthCare Ventures, "
    "Canaan, CHL Medical, Wellcome Trust and MedImmune, with no KP fund, and the firm never listed VaxInnate (decisions.md D5).",
    ec="formd_adjudicated", conf="high", cite=jl.FORMD_CITE("vaxinnate-corp", 3)))

L.append(verdict(
    "unsupervised-com-inc", "not_member",
    "Form D name match only: Arielle Zuckerberg is a director on Unsupervised's 2019-08 filing, but no source names "
    "Kleiner Perkins in its $12.8M Series A (2019) or $35M Series B (2021, led by Cathay Innovation and SignalFire with "
    "Eniac and Coatue, VentureBeat), and the firm never listed the company; missing corroboration reads not_member.",
    ec="formd_adjudicated", conf="medium",
    cite="https://venturebeat.com/technology/analytics-startup-unsupervised-raises-35m-to-spot-patterns-in-enterprise-data"))

L.append(verdict(
    "zume-inc", "not_member",
    "Form D name match only: Bing Gordon is a director on Zume's 2018-10 $375M SoftBank filing, but Crunchbase News on that "
    "round names him only as a former EA executive who 'joined Kleiner Perkins as a partner in 2008' and does not say a KP fund "
    "invested; the firm's own site never listed Zume, no filing names a KP vehicle and The Robot Report's Series B story "
    "names no investor. A vendor profile puts Kleiner Perkins in the $48M Series B (2017-10), which no press or filing read "
    "confirms, so the seat is not corroborated as fund money (decisions.md D3).",
    ec="formd_adjudicated", conf="medium",
    cite="https://news.crunchbase.com/venture/zume-pizzas-parent-company-raises-350m-from-softbank-beer-exec-joins-board/"))

# ---------------------------------------------------------------- not_member: homonyms, angel checks, SPAC
L.append(verdict(
    "workforce-software-holdings-llc", "not_member",
    "Homonym: the James Huang on WorkForce Software's 2017-2018 filings is an executive officer at the company's Livonia, "
    "Michigan office, not the KPCB China life-sciences partner; no KP fund is named.",
    ec="formd_adjudicated", conf="high", cite=FL("workforce-software-holdings-llc", "0001677149-18-000001")))

L.append(verdict(
    "xollent-biotech-inc", "not_member",
    "Homonym: Weili Zhou, a director of a Raleigh, North Carolina biotech that sold $50,000 in 2018, is not Kleiner "
    "Perkins' Wei Zhou and signs at the company's address; no KP fund is named.",
    ec="formd_adjudicated", conf="high", cite=FL("xollent-biotech-inc", "0001740943-18-000001")))

L.append(verdict(
    "yardbarker-inc", "not_member",
    "Partner's personal angel check (decisions.md D3): Yardbarker's 2008 round lists 'Russ Siegelman (who invested "
    "personally, not as part of his firm, Kleiner Perkins)' (VentureBeat, 2008-04-03); his 2009 Form D seat is at a "
    "personal Palo Alto address and no KP fund is named.",
    ec="web", conf="high", cite="https://venturebeat.com/social/sports-sites-yardbarker-college-fanz-raise-funding/"))

L.append(verdict(
    "thayer-ventures-acquisition-corp", "not_member",
    "SPAC shell (T5; JUDGE-BRIEF membership trap): Thayer Ventures Acquisition Corp is the listed shell that merged with "
    "Inspirato in February 2022; the KP filings on it report Inspirato stock the firm held from its private rounds, and "
    "Inspirato is its own member row.",
    ec="fund_filing", conf="high"))

# ---------------------------------------------------------------- members
# Airware (incorporated as Unmanned Innovation, Inc.): the same company as the base row `airware`.
L.append(verdict(
    "unmanned-innovation-inc", "member",
    "Unmanned Innovation, Inc. is Airware ('incorporated as Unmanned Innovation, Inc.', Wikipedia), which the firm listed "
    "on kpcb.com 2014-2018 (Digital team, Mike Abbott); Mike Abbott signs the 2014-07-15 Form D from 2750 Sand Hill Road, "
    "and AgFunderNews names KPCB as lead of that $25M Series B. Duplicate of the base row airware.",
    ec="site_listing", conf="high", cite=jl.ARCH("airware")))
L.append(cls(
    "unmanned-innovation-inc", status="acquired", rng="below_1b", city="San Francisco", city_src="formd_address",
    stage="Growth", stage_src=W, stage_conf="high", entry_date="2014-07",
    stage_cite=jl.NEWS("unmanned-innovation-inc", "Raises $25 Million Series B"),
    focus="Industrial & Robotics", flags=["stage_disputes_band"],
    note="Airware, the commercial drone operating system (San Francisco from 2014). Kleiner Perkins entered at the $25M "
         "Series B: 'The round was lead by Kleiner Perkins Caufield and Byers, with Andreessen Horowitz and First Round "
         "Ventures also contributing' (AgFunderNews, 2014-07-24); the Series A was a16z's and GV's, so the band's Series A "
         "is disputed. Ceased operations 2018-09-14 (TechCrunch) and Delair bought its assets (Wikipedia; The Drone Girl, "
         "2019-03-11): acquired with a successor note, as the airware row and the a16z, Felicis and GV books read it. Same "
         "company as the base row airware.",
    rounds=[rnd("2013-05", "Series A", 12200000, "Andreessen Horowitz and GV", False,
                jl.NEWS("unmanned-innovation-inc", "Raises $25 Million Series B"), "press"),
            rnd("2014-07", "Series B", 25000000, "Kleiner Perkins Caufield & Byers", True,
                jl.NEWS("unmanned-innovation-inc", "Raises $25 Million Series B"), "press"),
            rnd("2016-03", "Series C", 30000000, "Next World Capital", True, jl.W("Airware"), "press"),
            rnd("2019-03", "asset sale to Delair", None, "Delair", None,
                jl.NEWS("unmanned-innovation-inc", "Whatever happened to Airware"), "press")]))

# V-Vehicle (renamed Next Autoworks in 2010): the same company as the base row `next-autoworks`.
L.append(verdict(
    "v-vehicle-co", "member",
    "V Vehicle Co is Next Autoworks under its earlier name, which the firm listed on its 2012 company pages (Greentech "
    "team, Ray Lane); both 2009 Forms D name Ray Lane and John Doerr as directors 'c/o KPCB Holdings Inc, 2750 Sand Hill "
    "Road'. Duplicate of the base row next-autoworks.",
    ec="site_listing", conf="high", cite=jl.ARCH("next-autoworks")))
L.append(cls(
    "v-vehicle-co", status="defunct", rng="below_1b", country="US", city="San Diego", city_src="formd_address",
    stage=U, focus="Industrial & Robotics",
    note="San Diego car startup (V-Vehicle, renamed Next Autoworks), backed by Kleiner Perkins with T. Boone Pickens and "
         "Google Ventures. Ray Lane and John Doerr were already directors on the June 2009 bridge filing, so Kleiner "
         "Perkins entered at that round or earlier (the company filed a paper Form D in 2007); no source names the round, "
         "so the stage is undetermined. The DOE refused its loan in November 2011 and it closed its headquarters in "
         "December 2011 with no later activity: defunct, as GV's next-autoworks row reads. Same company as the base row "
         "next-autoworks.",
    rounds=[rnd("2009-06-10", "bridge ($3.4M sold of $4.4M)", 3400000, None, True,
                jl.FORMD_CITE("v-vehicle-co", 0), "filing"),
            rnd("2009-07-20", "equity ($62.3M sold)", 62256674, None, True,
                jl.FORMD_CITE("v-vehicle-co", 1), "filing")]))

# ---------------------------------------------------------------- classification only (membership already decided)
HEALTHEON_424B4 = "https://www.sec.gov/Archives/edgar/data/1009575/000104746999005587/0001047469-99-005587.txt"
L.append(cls(
    "webmd-corp-new", status="acquired", rng="below_1b", country="US", city="Elmwood Park", city_src="web_verified",
    stage="Series A", stage_src=W, stage_conf="high", entry_date="1996-01-26", stage_cite=HEALTHEON_424B4,
    focus="Healthcare & Bio",
    note="WebMD Corp /NEW/ is Healtheon (CIK 1009575: Healtheon Corp to 2000, WebMD Corp /NEW/ to 2005, then Emdeon Corp "
         "and HLTH Corp). Healtheon's 1999 prospectus: 'On January 26, 1996, Healtheon sold 10,285,000 shares of its "
         "Series A preferred stock for $.50 per share', purchasers including Kleiner Perkins Caufield & Byers VII and KPCB "
         "VII Founders Fund; KPCB VII also bought the October 1996 Series B. HQ Elmwood Park, NJ (the 2004 13G/A's issuer "
         "address). HLTH merged into WebMD Health Corp in 2009, which Internet Brands (KKR) bought in 2017: acquired. Same "
         "company as the base row healtheon.",
    rounds=[rnd("1996-01-26", "Series A", 5142500, None, True, HEALTHEON_424B4, "filing"),
            rnd("1996-10-01", "Series B", 6000000, None, True, HEALTHEON_424B4, "filing")]))

L.append(cls(
    "visioneer-inc", rng="below_1b", country="US", city="Fremont", city_src="web_verified", stage=U,
    focus="Industrial & Robotics",
    note="Visioneer, the PaperPort desktop scanner maker founded March 1992 (Wikipedia). Kleiner Perkins Caufield & Byers "
         "VI and KPCB VI Founders Fund reported ceasing to hold over 5% of its common stock on the 1998-02 13G/A (issuer "
         "business address Fremont, CA). The IPO prospectus is not on EDGAR (the company's filings start 1996-05) and no "
         "source read names the round the fund entered: undetermined. Visioneer bought ScanSoft from Xerox and took "
         "its name in 1999, became Nuance in 2005, and Microsoft acquired Nuance in 2022: acquired stands.",
    rounds=[]))

jl.write("j13", L)
