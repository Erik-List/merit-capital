"""PRO-100 NEA, stage pass s2, first half (50 rows): the round NEA first entered, with the funding history found.
Run: NQ_TAG=s2 python3 judgments-s2a.py"""
import json

import judge_lib as jl

cls, rnd, NEWS = jl.cls, jl.rnd, jl.NEWS
L = []
_OLD = json.loads((jl.INV / "companies" / "classification.json").read_text())


def R(slug, *new, drop=()):
    """The row's rounds already on disk (minus dates in `drop`), then the new ones not already there."""
    old = [r for r in (_OLD.get(slug, {}).get("funding_rounds") or []) if r.get("date") not in drop]
    have = {(r.get("date"), r.get("round")) for r in old}
    return old + [r for r in new if (r["date"], r["round"]) not in have]


def und(slug, note, rounds):
    L.append(cls(slug, stage="undetermined", rounds=rounds, note=note))


GN = "Google News (the company with NEA and round words)"
TCS = "TechCrunch's own search"

# ---- tool-printed citations (EDGAR full-text hits, S-4 main documents, TechCrunch search results read in this pass)
CELC_8K = "https://www.sec.gov/Archives/edgar/data/1603454/000149315222013952/ex99-1.htm"
LQDA_S1 = "https://www.sec.gov/Archives/edgar/data/1330436/000104746918004801/a2235907zs-1.htm"
MILLENDO_S4 = "https://www.sec.gov/Archives/edgar/data/1544227/000119312521114415/d150774ds4.htm"
RAAC_S4 = "https://www.sec.gov/Archives/edgar/data/1824734/000121390021016725/fs42021_revolutionaccacq.htm"
TC_BG = "https://techcrunch.com/2020/01/21/as-retail-robotics-heats-up-berkshire-grey-raises-263m/"
TC_LETGO = "https://techcrunch.com/2018/08/08/letgo-the-2nd-hand-shopping-app-raises-another-500m-at-over-a-1-5b-valuation/"
TC_CODA = "https://techcrunch.com/2017/10/19/two-google-alums-just-raised-60m-to-rethink-documents/"
TC_PLACEMETER = ("https://techcrunch.com/2015/06/23/placemeter-uses-computer-vision-to-help-businesses-and-cities-"
                 "measure-vehicle-and-pedestrian-traffic/")
TC_VIRTRU14 = "https://techcrunch.com/2014/06/17/virtru-a-secure-email-app-built-by-an-ex-nsa-engineer-raises-6m/"
TC_FANTASY = ("https://techcrunch.com/2012/01/23/fantasy-shopper-confirms-its-hottness-with-3-3m-first-money-from-"
              "accel-and-nea/")
TC_WELLTOK = ("https://techcrunch.com/2013/04/10/welltok-lands-18-7m-from-nea-emergence-others-to-make-your-health-"
              "plan-more-engaging/")
TC_CURALATE = "https://techcrunch.com/2016/02/02/profiting-from-pretty-pictures/"
TC_NICIRA = ("https://techcrunch.com/2012/02/05/andreessen-horowitz-backed-nicira-pulls-the-curtains-back-on-disruptive-"
             "network-virtualization-platform/")
TC_TABBEDOUT = "https://techcrunch.com/2011/05/09/tabbedout-raises-4m-for-restaurant-mobile-payments-platform/"
CADENCE_8K = "https://www.sec.gov/Archives/edgar/data/1333248/000119312509033835/dex991.htm"
# read in this pass after a web search (the page itself states what is cited)
VB_ONECONCERN = "https://venturebeat.com/ai/one-concern-raises-20-million-for-ai-that-predicts-the-impact-of-natural-disasters/"
PRN_HEARSAY = "https://www.prnewswire.com/news-releases/hearsay-social-secures-18-million-from-nea-and-sequoia-capital-126317798.html"

# ---------------------------------------------------------------- $1B+ and public rows
und("celcuity", "Stage pass: the only NEA position on record is the May 2022 private placement into the listed company "
    "(8-K), so no venture round exists to stage; the row is an X1 and R2 case (a PIPE with no earlier NEA private round).",
    [rnd("2022-05-16", "PIPE (private placement into the listed company)", None,
         "Venrock Healthcare Capital Partners", True, CELC_8K, "filing")])
und("chinaway-technologies-limited", f"Stage pass: {GN} (English and Chinese names) found no report of the round NEA "
    "entered by 2013; the rounds on file are later.", R("chinaway-technologies-limited"))
und("liquidia-corporation", "Stage pass: the 2018 IPO prospectus lists Series A, A-1, B, C, C-1 and D preferred but "
    "dates none of the early series and ties no series to NEA 12; Google News found no 2007 round report.",
    [rnd(None, "Series A, A-1, B, C, C-1 and D preferred (undated in the prospectus)", None, None, None, LQDA_S1,
         "filing")])
und("cirrus-logic", "Stage pass: no round can be named; the firm's own 1990 year falls after Cirrus Logic's 1989 Nasdaq "
    f"listing, so the position may be a listed purchase (X1 and T3 review). {GN} found nothing on NEA.", [])
L.append(cls("tempest-therapeutics", stage="Growth", stage_src="web_verified", stage_conf="medium",
             stage_cite=_OLD["millendo"]["entry_stage_citation"], entry_date=_OLD["millendo"]["entry_date"],
             rounds=[rnd("2011-10", "Series A", 10000000, None, False, MILLENDO_S4, "filing"),
                     rnd("2018-02", "Series B", 25200000, None, False, MILLENDO_S4, "filing"),
                     rnd("2019-02", "Series B-1", 58000000, None, False, MILLENDO_S4, "filing")]
             + _OLD["millendo"]["funding_rounds"],
             note="The NEA position behind this row is Millendo, not legacy Tempest: the 2021 merger proxy (S-4) lists "
                  "legacy Tempest's Series A (one venture investor, 2011 to 2016), B and B-1 buyers (Versant, F-Prime, "
                  "Quan, LYFE and others, no NEA fund), while NEA led the $62M Series B of Millendo, the listed company "
                  "that merged with Tempest in 2021. Stage aligned with the millendo row (the same position)."))
und("neuropace", f"Stage pass: {GN} and TechCrunch's own search found no report of the round NEA entered in 2000; the "
    "IPO prospectus of 2021 could not be read in full.", [])
L.append(cls("august", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=NEWS("august", "Announces $7M in Seed"), entry_date="2025-08-05", grad="censored",
             rounds=R("august", rnd("2025-08-05", "Seed", 7000000, "NEA and Pear VC", True,
                                    NEWS("august", "Announces $7M in Seed"), "press"), drop=("2025-08",)),
             note="Law.com (2025-08-05) names the $7M round led by New Enterprise Associates and Pear VC a seed round; "
                  "the entry is inside the censoring window."))
und("sbc", f"Stage pass: {GN} found no round for Stablecoin.xyz or the SBC stablecoin.", [])
L.append(cls("escient-pharmaceuticals", stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite=NEWS("escient-pharmaceuticals", "10 Biggest Rounds Of November"), entry_date="2022-11",
             rounds=[rnd("2018-05-09", "unnamed", 40000000, None, None,
                         NEWS("escient-pharmaceuticals", "Escient Pharma grabs"), "press"),
                     rnd("2022-11", "Series C", 120000000, "NEA, Abingworth and Forge Life Science Partners", True,
                         NEWS("escient-pharmaceuticals", "10 Biggest Rounds Of November"), "press"),
                     rnd("2024-06-03", "Acquisition by Incyte", 750000000, None, None,
                         NEWS("escient-pharmaceuticals", "Incyte closes $750M"), "press")],
             note="Crunchbase News names the $120M Series C of November 2022 co-led by NEA, Abingworth and Forge; the "
                  "firm's own first year is 2022 and nothing earlier ties NEA, so NEA entered at the Series C."))
und("prime-financial-technologies", f"Stage pass: {GN} found no round for Prime Financial Technologies.", [])
und("stx-entertainment", f"Stage pass: {GN} found no report naming the round NEA 16 bought; Carmen Chang's board seat "
    "dates the position to 2015.", [])
und("curzion-pharmaceuticals", f"Stage pass: {GN} found only the 2020 Horizon acquisition ($45M, Wilson Sonsini); no "
    "round is named.", [rnd("2020-04-02", "Acquisition by Horizon Therapeutics", 45000000, None, None,
                            NEWS("curzion-pharmaceuticals", "Horizon snaps up Curzion"), "press")])
und("shape-therapeutics", "Stage pass: the company's Series B release (July 2021) names NEA's continued participation, so "
    "NEA entered earlier, in the 2019 round no source names.",
    [rnd("2021-07-15", "Series B", 112000000, "Decheng Capital and Breton Capital", True,
         NEWS("shape-therapeutics", "Shape Therapeutics Secures $112"), "company")])
und("foundry-therapeutics-1", "Stage pass: no round is named; the row is The Foundry's incubator vehicle, which R3 reads as "
    "fund-shaped (not_member until an operating company is shown).", [])
und("the-yes", "Stage pass: Vogue (2019-10-22) reports $30M across the seed and Series A with NEA among the investors but "
    "does not say which round NEA joined.",
    R("the-yes", rnd("2019-10-22", "Seed and Series A (combined)", 30000000, None, True,
                     NEWS("the-yes", "Ex-Stitch Fix COO"), "press")))
L.append(cls("grey-rhino", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=VB_ONECONCERN,
             entry_date="2017-12-19",
             rounds=[rnd("2017-12-19", "Series A", 20000000, "NEA", True, VB_ONECONCERN, "press")],
             note="One Concern (this row's company): VentureBeat (2017-12-19) reports the $20M round led by New "
                  "Enterprise Associates, the firm's own 2017 year; FinSMEs' headline names it the Series A, so model at "
                  "medium. The one-concern row is the same company."))
und("runtime", f"Stage pass: {GN} found no round for Runtime (Apache Mynewt).", [])
L.append(cls("berkshire-grey", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=RAAC_S4,
             entry_date="2016",
             rounds=[rnd(None, "Series A", None, None, None, RAAC_S4, "filing"),
                     rnd("2020-01-21", "Series B", 263000000, "SoftBank", True, TC_BG, "press")],
             note="The merger proxy (S-4) shows only Series A and Series B (B-2, B-3) preferred, with Khosla's seed "
                  "funds and NEA 15 and NEA Ventures 2016 as holders; NEA joined the $263M Series B of 2020 as an existing "
                  "investor (TechCrunch), so its 2016 entry was the Series A, read at medium."))
und("letgo", "Stage pass: TechCrunch (2018) lists NEA among letgo's backers without dating its entry; the 2016 year is the "
    "Wallapop merger, so whether NEA's stake is merger consideration or a round stays open.",
    [rnd("2018-08-08", "unnamed", 500000000, None, None, TC_LETGO, "press")])
und("simple-psychology", f"Stage pass: {GN} (English and Chinese names) found no round naming NEA.", [])
und("coda", "Stage pass: TechCrunch's report of the $60M raise (2017) names Greylock, Khosla and General Catalyst, not NEA, "
    "and no source ties NEA's 2015 entry to a round.",
    [rnd("2017-10-19", "unnamed", 60000000, None, None, TC_CODA, "press")])
und("idfy", f"Stage pass: {GN} found only later rounds (up to the 2026 Series F); NEA's 2015 round is not named.",
    R("idfy"))
L.append(cls("nuvolo", stage="Seed", stage_src="model", stage_conf="medium", stage_cite=NEWS("nuvolo", "GE Ventures backs"),
             entry_date="2015", grad="graduated", grad_src="web_verified", grad_conf="high",
             grad_cite=NEWS("nuvolo", "GE Ventures backs"), grad_asof="2017-06-22",
             rounds=[rnd("2015", "pre-Series A funding (about $2M)", None, None, True, None, "press"),
                     rnd("2017-06-22", "Series A", 10000000, "GE Ventures", True, NEWS("nuvolo", "GE Ventures backs"),
                         "press"),
                     rnd("2019-07-18", "Series B", 12000000, None, None, NEWS("nuvolo", "Nuvolo Raises $12M"), "press")],
             note="SiliconANGLE (2017-06-22) names NEA an existing investor in the $10M Series A that brought total "
                  "funding just over $12M, so NEA's 2015 entry was the roughly $2M pre-A funding: Seed at medium, "
                  "graduated by that named Series A."))
und("therachon", f"Stage pass: {GN} and TechCrunch's own search found only the 2018 mezzanine round and the Pfizer sale; "
    "NEA's 2015 round is not named.", R("therachon"))
und("aera", f"Stage pass: {GN} found only the 2017 $50M raise under the Aera name; NEA's 2014 FusionOps round is not named.",
    R("aera"))
und("cyence", f"Stage pass: {GN} and TechCrunch's own search found no report naming NEA's 2014 round.", [])
L.append(cls("placemeter", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_PLACEMETER,
             entry_date="2014",
             rounds=[rnd("2013", "Techstars NY and seed", None, None, False, None, "press"),
                     rnd("2014", "Series A", 6000000, "NEA", True, TC_PLACEMETER, "press")],
             note="TechCrunch (2015-06-23): NEA led Placemeter's $6M Series A, of $7.8M raised after Techstars; the "
                  "firm's own year 2014 dates it."))
und("virtru", "Stage pass: TechCrunch's report of the June 2014 $6M round names Bessemer and angels, not NEA, and the "
    "Series A of 2016 lists NEA as a participant; the firm's 2014 year leaves the entry round open.",
    R("virtru", rnd("2014-06-17", "unnamed", 6000000, "Bessemer Venture Partners", None, TC_VIRTRU14, "press")))
und("alta-devices-inc", f"Stage pass: {GN} and TechCrunch's own search found no round naming NEA.", [])
und("cleave-biosciences", f"Stage pass: {GN} and TechCrunch's own search found no report of NEA's 2013 round.", [])
L.append(cls("fantasy-shopper", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_FANTASY,
             entry_date="2012-01-23",
             rounds=[rnd("2012-01-23", "Seed (convertible note, first round)", 3300000, "Accel Partners and NEA", True,
                         TC_FANTASY, "press")],
             note="TechCrunch (2012-01-23): the company's first round after the HackFWD accelerator, $3.3M on a "
                  "convertible note co-led by Accel and NEA, a seed. Graduation left for the graduation pass."))
for s, what in [("kor-electronics", "KOR Electronics"), ("microwave-technology-inc", "Microwave Technology (MwT)"),
                ("pacificdental-benefits-inc", "PacifiCare Dental Benefits"),
                ("quantum-medical-systems", "Quantum Medical Systems"), ("skyline-solar-inc", "Skyline Solar"),
                ("think3-inc", "think3")]:
    und(s, f"Stage pass: {GN} found no round for {what}, and no filing on disk names one.", [])
und("welltok", "Stage pass: TechCrunch (2013-04-10) names NEA an existing investor in the $18.7M Series B led by Emergence "
    "and InterWest, so NEA entered in the earlier funding (about $7.3M), which no source names.",
    [rnd("2013-04-10", "Series B", 18700000, "Emergence Capital Partners and InterWest Partners", True, TC_WELLTOK,
         "press")])
und("cuponation", f"Stage pass: {GN} and TechCrunch's own search found no round naming NEA.", [])
und("likelihood", f"Stage pass: {GN} returns only the common word; no round found.", [])
und("springpath", f"Stage pass: {GN} and TechCrunch's own search found no report naming NEA's 2012 round.", R("springpath"))
L.append(cls("curalate", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_CURALATE,
             entry_date="2011", grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_CURALATE,
             grad_asof="2016-02-02",
             rounds=[rnd("2011", "Seed", None, "NEA", True, TC_CURALATE, "press"),
                     rnd("2014-06-09", "Series B", 8600000, None, True, NEWS("curalate", "Curalate Secures"), "press"),
                     rnd("2016-02-02", "Series C", 27500000, "NEA", True, TC_CURALATE, "press")],
             note="TechCrunch (2016-02-02): NEA has led all of Curalate's rounds from the seed to the $27.5M Series C, "
                  "so the entry is the seed (the firm's own 2011 year), graduated by the named later rounds."))
L.append(cls("hearsay-social", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=PRN_HEARSAY,
             entry_date="2011-07-28",
             rounds=R("hearsay-social", rnd("2011-07-28", "Series B", 18000000, "NEA", True, PRN_HEARSAY, "company"),
                      drop=("2011-07-28",)),
             note="The company's release (2011-07-28): NEA led the $18M round, Jon Sakoda joined the board and existing "
                  "investor Sequoia participated, the round after Sequoia's first; press numbers it the Series B, so "
                  "Growth at medium."))
und("nicira", "Stage pass: TechCrunch (2012-02-05) gives $50M raised to date from Andreessen Horowitz, Lightspeed and NEA "
    "but no round per investor; vendor pages put NEA in a 2011 Series C, which cannot cite.",
    [rnd("2012-02-05", "funding to date", 50000000, None, True, TC_NICIRA, "press")])
und("cardionomic", f"Stage pass: {GN} found only the 2020 $16M raise; the Form D rounds are unnamed and NEA's 2010 round is "
    "not named.", [rnd("2020-02-24", "unnamed", 16000000, None, None, NEWS("cardionomic", "Heart failure startup"),
                       "press")])
und("motus-therapeutics", f"Stage pass: {GN} found only the 2016 Allergan acquisition; the Rhythm-era 2010 round is not "
    "named.", [])
L.append(cls("union", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_TABBEDOUT,
             entry_date="2010",
             rounds=[rnd("2011-05-09", "Series A", 5750000, None, True, TC_TABBEDOUT, "press")],
             note="TechCrunch (2011-05-09): TabbedOut raised $3.7M from New Enterprise Associates to complete its $5.75M "
                  "Series A; the firm's own first-invested year 2010 dates the entry. The tabbedout row is the same company."))
und("cadence-pharmaceuticals", "Stage pass: the only NEA position on record is the February 2009 private placement into "
    "the company listed since 2006 (8-K), so no venture round exists to stage (X1).",
    [rnd("2009-02-20", "PIPE (private placement into the listed company)", None, "Venrock", True, CADENCE_8K, "filing")])
und("myfit", f"Stage pass: {GN} and TechCrunch's own search found nothing for MyFit.", [])
und("acorn-cardiovascular-inc", f"Stage pass: {GN} found no round naming NEA.", [])

jl.write("s2a", L)
