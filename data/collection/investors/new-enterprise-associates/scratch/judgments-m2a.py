"""PRO-100 NEA, judge m2, part a: the first 38 slugs of queue/m2.json (Form D name-match rows), judged cluster-first.

Clusters resolved (the firm's own team pages give the years):
- Ross Jaffe: Versant Ventures co-founder; NEA lists him only as a 2019 venture advisor. His filings sit at Versant's
  address or c/o the company; no NEA source names any of his rows. All out.
- Harry Weller: NEA general partner to his death in 2016; every seat is in tenure. Four rows are legal-name twins of
  listed companies (440 Labs = Timescale, Clearspring = AddThis, Kimble = eeGeo, Luminal = Fugue, one CIK each);
  Quick Hit carries his seat c/o NEA. Experiment Fund is NEA's Harvard seed vehicle (D5) and FabricLock an NEA 14
  entity with no identified business: both out.
- Dayna Grayson: NEA 2012/13 to 2020, then Construct Capital. APX Labs (= Upskill), Cloudline (= Evenly) and WireWheel
  (NEA co-led the 2018 Series A) are in; Awareness and Viximo predate her NEA years, Buffalo Market and Verve follow them.
- Peter Barris: NEA general partner throughout. Cyren Call and Jobfox carry his seat at NEA's Chevy Chase office;
  Goji, ViewLift (= SnagFilms) and Watermelon Express (= BenchPrep) are twins of listed rows.
- Robert Garland: every seat is an operator role or another fund's (Breakthrough 307). All out.
- Rick Yang: daTangle is a homonym; Focal App's business could not be identified; Hykso (= FightCamp) and Play Versus
  (= PlayVS) are twins of listed rows.
- Crystal Huang: NEA Principal from 2018, now a GV general partner; her 2024 seats are GV's; ProSky is a homonym.
"""
import json

import judge_lib as jl
from judge_lib import cls, rnd, verdict

BASE = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def fd(slug, i=0):
    """The i-th Form D link on the row's own formd_links (copied from disk, never typed)."""
    return [x.strip() for x in BASE[slug]["formd_links"].split(";") if x.strip()][i]


L = []


def nm(slug, basis, conf="high", cite=None, ec="formd_adjudicated"):
    L.append(verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=cite or fd(slug)))


def twin(slug, canonical, basis, i=0):
    L.append(verdict(slug, "member", f"Legal-name twin of the firm's listed {canonical}: {basis} Folds into "
                                     f"{canonical} at the rebuild (identity-merges.json).",
                     ec="formd_adjudicated", conf="high", cite=fd(slug, i)))


# ---- Ross Jaffe (Versant Ventures)
nm("alterg-inc", "Ross Jaffe's seat is Versant Ventures' (he co-founded Versant; the 2011 filing gives his address "
   "c/o Versant Ventures, 3000 Sand Hill Road). NEA shows him only as a 2019 venture advisor and no NEA listing, "
   "filing or press names AlterG.")
nm("calypso-medical-technologies-inc", "Ross Jaffe, Versant Ventures' co-founder, signs from Versant's Sand Hill Road "
   "address (2009-2011), years before NEA's only listing of him (venture advisor, 2019); no NEA source names Calypso.")
nm("cerephex-corp", "Ross Jaffe's 2012 seat predates NEA's only listing of him (venture advisor, 2019) and falls in "
   "his Versant years; no NEA listing, filing or press names Cerephex.")
nm("docmatter-inc", "Ross Jaffe's 2018 and 2022 seat: NEA lists him only as a 2019 venture advisor, and D4 counts an "
   "advisor's seat only where an NEA fund held the position; no NEA listing, filing or press names DocMatter.",
   conf="medium")
nm("portaero-inc", "Ross Jaffe signs Portaero's 2009 filing from Versant Ventures' address (3000 Sand Hill Road, "
   "Bldg 4); Versant's position, not NEA's. Same issuer as respira-inc (CIK 1405656, Respira renamed Portaero in 2009).")
nm("respira-inc", "Same issuer as portaero-inc (CIK 1405656, Respira Inc renamed Portaero in 2009); Ross Jaffe signs "
   "from Versant Ventures' address, so the position is Versant's, not NEA's.")
nm("sympara-medical-inc", "Ross Jaffe's 2013-2014 seat falls in his Versant years, before NEA's only listing of him "
   "(venture advisor, 2019); no NEA listing, filing or press names Sympara.")
nm("vital-therapies-inc", "Ross Jaffe's 2009-2011 seat is Versant Ventures' (Vital Therapies, now Immunic, was a "
   "Versant company); no NEA vehicle appears on its filings and the firm never lists it.")

# ---- Harry Weller
twin("440-labs-inc", "Timescale", "440 Labs, Inc. is Timescale's issuer (EDGAR CIK 1644511, whose later filings sit on "
     "the timescale row), and Harry Weller, NEA general partner, is a director on its 2015 seed filing.")
L.append(cls("440-labs-inc", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite="https://www.businesswire.com/news/home/20220222005363/en/Timescale-Valuation-Rockets-to-Over-%241B-with-%24110M-Round-Marking-the-Explosive-Rise-of-Time-Series-Data",
             asof="2022-02-22", stage="Seed", stage_src="formd_band", stage_conf="medium", entry_date="2015-06-01",
             grad="graduated", grad_src="web_verified",
             grad_cite="https://techcrunch.com/2018/01/24/timescale-raises-12-4m-to-build-a-new-breed-of-time-series-database-software/",
             grad_conf="high", grad_asof="2018-01-24", city="New York", focus="Data Infrastructure",
             flags=["stale", "identity_conflated"], extra={"valuation_range_source": "web_verified"},
             rounds=[rnd("2015-06-01", "Seed", 3656724, None, True, fd("440-labs-inc"), "filing"),
                     rnd("2018-01-24", "Series A", 12400000, "Benchmark", True,
                         "https://techcrunch.com/2018/01/24/timescale-raises-12-4m-to-build-a-new-breed-of-time-series-database-software/", "press"),
                     rnd("2022-02-22", "Series C", 110000000, "Tiger Global", None,
                         "https://www.businesswire.com/news/home/20220222005363/en/Timescale-Valuation-Rockets-to-Over-%241B-with-%24110M-Round-Marking-the-Explosive-Rise-of-Time-Series-Data", "press")],
             note="Timescale (renamed TigerData in 2025), New York. NEA's entry is the 2015 $3.7M seed this filing "
                  "records (Harry Weller on the board; the firm dates its first investment 2015), which the band reads "
                  "as Seed; TechCrunch (2018-01-24) reports the $12.4M Series A led by Benchmark with NEA "
                  "participating, so it graduated. Mark: the $110M Series C of 2022-02-22 at over $1B (Business Wire), "
                  "recorded at $1B, stale; aligned with the Tiger Global, Benchmark and Redpoint rows. Same company as "
                  "the timescale row; merge."))

twin("clearspring-technologies-inc", "AddThis", "Clearspring Technologies renamed itself AddThis in 2012, and Harry "
     "Weller, NEA general partner, is its director at NEA's Chevy Chase office (5425 Wisconsin Avenue) on the 2011 "
     "filings.")
L.append(cls("clearspring-technologies-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2008",
             city="McLean", focus="Media, Gaming & Advertising", flags=["identity_conflated", "stage_disputes_band"],
             note="Clearspring Technologies (AddThis from 2012), McLean, acquired by Oracle in 2016 (the firm's exit "
                  "line). The firm dates its first investment 2008, so the pre-filled 2011 Series A band reads a later "
                  "round; no source names NEA's 2008 round. Same company as the addthis row; merge."))

nm("experiment-fund-llc", "D5: a fund, not an operating company. The Experiment Fund is the seed vehicle NEA founded "
   "with Harvard's engineering school (the firm's archived Harvard Experiment Fund listing); its 2012 filing lists NEA's "
   "finance and legal chiefs as its officers and Weller and Chung as investment-board members. Same vehicle as the "
   "harvard-experiment-fund row.")
nm("fabriclock-inc", "An NEA 14 entity, not an identified operating company: its only filing (2014, $2M) lists Harry "
   "Weller and Ron Bernal as its executive officers c/o New Enterprise Associates 14, L.P. at NEA's Chevy Chase office, "
   "and no source names a FabricLock business (D5; unresolved identity).", conf="medium")

twin("kimble-inc", "eeGeo", "Kimble, Inc. renamed itself eeGeo Inc. in 2010 (EDGAR CIK 1504775, the CIK of the eegeo "
     "row's filing), and Harry Weller, Patrick Chung and Megan Alderete sit as its directors at NEA's Timonium address "
     "on the 2010 filing.")
L.append(cls("kimble-inc", status="unknown", rng="below_1b", stage="Series A", stage_src="formd_band",
             stage_conf="medium", entry_date="2010-10-20", city="Dundee", focus="Media, Gaming & Advertising",
             flags=["identity_conflated"],
             note="eeGeo (later WRLD), 3D mapping, Dundee; no news after 2017 and its current state could not be "
                  "established (as the eegeo row reads). NEA's first filing is this 2010 round, $2.5M sold of $4.6M "
                  "with three NEA directors and no earlier filing, which the era's bands read as a Series A. Same "
                  "company as the eegeo row; merge."))

twin("luminal-inc", "Fugue", "Luminal, Inc. renamed itself Fugue, Inc. in 2015 (EDGAR CIK 1603449, the CIK of the fugue "
     "row's filings), with NEA's Michael O'Dell (2014) and Harry Weller (2015) as directors of record.")
L.append(cls("luminal-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014",
             city="Frederick", focus="Security", flags=["identity_conflated"],
             note="Luminal (Fugue from 2015), cloud security, Frederick, Maryland; Fugue was acquired by Snyk in 2022 "
                  "(the firm's exit line). The firm dates its first investment 2014, the year of both a $5.0M and a "
                  "$10M filing, and no source says which round NEA entered. The Felicis and YC Luminal rows are a "
                  "different company (an AI startup of 2025). Same company as the fugue row; merge."))

L.append(verdict("quick-hit-inc", "member", "Harry Weller, NEA general partner in tenure, is a director of record c/o "
                 "New Enterprise Associates, 1954 Greenspring Drive, on Quick Hit's 2010 and 2011 filings, beside "
                 "Valhalla Partners' directors; Quick Hit (formerly Head to Head and Play Hard Sports) is the "
                 "Foxborough maker of Quick Hit Football. Unannounced on the firm's pages; flagged for the A/B pass.",
                 ec="formd_adjudicated", conf="medium", cite=fd("quick-hit-inc")))
L.append(cls("quick-hit-inc", status="acquired", rng="below_1b", city="Foxborough", city_src="formd_address",
             focus="Media, Gaming & Advertising",
             note="Online football game maker in Foxborough, Massachusetts; Majesco acquired Quick Hit in June 2011 "
                  "(Capsule Computers, 2011-06-12). Stage kept from the Form D band. Graduation left for the "
                  "graduation pass."))

# ---- Dayna Grayson (NEA to 2020, then Construct Capital) and Peter Barris
twin("apx-labs-inc", "Upskill", "APX Labs, Inc. renamed itself Upskill, Inc. (EDGAR CIK 1607943, the CIK of the upskill "
     "row's filing), with NEA's Peter Barris and Dayna Grayson as its directors on the 2014 filing.")
L.append(cls("apx-labs-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014",
             city="Vienna", focus="SaaS", flags=["identity_conflated"],
             note="APX Labs (Upskill from 2016), enterprise wearables software, acquired by TeamViewer (the firm's exit "
                  "line). The firm dates its first investment 2014, the year of this $15.6M filing, but no page names "
                  "the round. Aligned with the upskill row; merge."))

nm("awareness-inc", "Dayna Grayson's 2011 seat predates her NEA years (the firm's team pages first show her in 2013 "
   "and the 2008-2010 pages do not), and the filing seats her beside North Bridge's Richard D'Amore; no NEA listing, "
   "filing or press names Awareness.", conf="medium")
nm("buffalo-market-inc", "Dayna Grayson's 2021 and 2023 seats follow her NEA years (last on the firm's pages in 2020; "
   "she then co-founded Construct Capital); no NEA source names Buffalo Market.")

twin("cloudline-technologies-inc", "Evenly", "Cloudline Technologies filed its 2019 round from NEA's own Chevy Chase "
     "office with Barry Beck, the Bluemercury co-founder whose orthodontics company is Evenly (WWD, 2023), as its "
     "executive and NEA's Dayna Grayson as director.")
L.append(cls("cloudline-technologies-inc", status="private", rng="below_1b", city="Washington",
             focus="Healthcare & Bio", flags=["identity_conflated"],
             note="Evenly, outsourced orthodontics for dental offices (Washington, as the evenly row reads). Stage kept "
                  "from the Form D band of this 2019 $10.3M round, the firm's first-investment year. Same company as "
                  "the evenly row; merge."))

nm("verve-inc", "Dayna Grayson's 2021-2026 seats follow her NEA years (last on the firm's pages in 2020; she then "
   "co-founded Construct Capital); no NEA source names Verve.")
nm("viximo-inc", "Dayna Grayson is an executive officer of Viximo on its 2009 filing, an operator role before her NEA "
   "years (first on the firm's pages in 2013); no NEA source names Viximo.")

WW_PR = "https://www.prnewswire.com/news-releases/privacy-protection-platform-wirewheel-closes-10-million-in-financing-300737392.html"
L.append(verdict("wirewheel-inc", "member", "NEA and PSP Growth led WireWheel's $10M Series A, and NEA's Dayna Grayson "
                 "joined the board (PR Newswire, 2018-10-25); she is its director of record on the 2020 filing.",
                 ec="web", conf="high", cite=WW_PR))
L.append(cls("wirewheel-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=WW_PR, stage_conf="high", entry_date="2018-10-25", city="Arlington", focus="Security",
             rounds=[rnd("2018-10-25", "Series A", 10000000, "NEA; PSP Growth", True, WW_PR, "press"),
                     rnd("2021-02-10", "Series B", 20000000, None, None,
                         jl.NEWS("wirewheel-inc", "Raises $20 Million in Series B"), "press")],
             note="Privacy-management software, Arlington, Virginia. NEA co-led the 2018 Series A (the pre-filled 2020 "
                  "date is a later filing carrying its director of record). Osano acquired WireWheel in December 2023 "
                  "(IAPP; The Business Journals)."))

L.append(verdict("cyren-call-communications-corp", "member", "Peter Barris, NEA general partner, is a director of "
                 "record at NEA's Chevy Chase office (5425 Wisconsin Avenue) on Cyren Call's 2009 filing, beside "
                 "Battery's Scott Tobin and Columbia Capital's James Fleming; Cyren Call is Morgan O'Brien's McLean "
                 "public-safety broadband company. Unannounced on the firm's pages; flagged for the A/B pass.",
                 ec="formd_adjudicated", conf="medium", cite=fd("cyren-call-communications-corp")))
L.append(cls("cyren-call-communications-corp", status="defunct", rng="below_1b", stage="undetermined", country="US",
             city="McLean", focus="Data Infrastructure",
             note="Public-safety broadband spectrum venture founded by Nextel's Morgan O'Brien, superseded when FirstNet "
                  "was created in 2012 (aligned with the Battery row; the General Catalyst row reads unknown). NEA's "
                  "seat shows on the 2009 $165K filing after Regulation D notices from 2006; the entry round is not "
                  "named."))

twin("goji-food-solutions-ltd", "Goji Solutions", "NEA general partners Peter Barris and Ravi Viswanathan are directors "
     "on Goji Food Solutions' 2011 $25M filing, and the firm's card links gojifoodsolutions.com.")
L.append(cls("goji-food-solutions-ltd", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=jl.SITE("goji-solutions"), stage_conf="medium", entry_date="2011", country="IL",
             country_src="web_verified",
             country_cite="https://spectrum.ieee.org/israeli-startup-goji-is-planning-the-oven-of-the-future",
             focus="Industrial & Robotics", flags=["identity_conflated", "stage_disputes_band", "city_unknown"],
             note="Goji's RF-energy cooking technology, an Israeli company (IEEE Spectrum) registered in Bermuda. The "
                  "firm labels its 2011 entry Growth, which replaces the pre-filled Series A band read off this $25M "
                  "filing, the company's first US filing. Aligned with the goji-solutions row; merge."))

L.append(verdict("jobfox-inc", "member", "Peter Barris, NEA general partner, is a director of record at NEA's Chevy "
                 "Chase office on Jobfox's December 2009 filing, beside Menlo Ventures' Sonja Perkins; Jobfox is Rob "
                 "McGovern's McLean job-matching company. Unannounced on the firm's pages; flagged for the A/B pass.",
                 ec="formd_adjudicated", conf="medium", cite=fd("jobfox-inc", 1)))
L.append(cls("jobfox-inc", status="defunct", rng="below_1b", stage="undetermined", country="US", city="McLean",
             focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
             note="Career-matching site (formerly Market10) in McLean, wound down around 2011 (aligned with the Menlo "
                  "row). The pre-filled Seed reads a 2009 $3M filing, but Jobfox had filed Regulation D notices since "
                  "2007 and raised earlier rounds, so it is a late round; NEA's entry round is not named."))

twin("viewlift-inc", "SnagFilms", "SnagFilms, Inc. renamed itself ViewLift, Inc. in 2018 (EDGAR CIK 1508196, the CIK of "
     "the snagfilms row's filings), and Peter Barris is its director c/o SnagFilms on the 2019 filing.")
L.append(cls("viewlift-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2010",
             city="Washington", focus="Media, Gaming & Advertising", flags=["identity_conflated"],
             note="SnagFilms closed its film service in 2020, but the issuer, renamed ViewLift, runs an OTT streaming "
                  "platform and was acquired by DAZN in May 2026 (TVBEurope, 2026-05-05), so it reads acquired; the "
                  "snagfilms row's defunct predates the sale. The firm dates its first investment 2010; the round is "
                  "not named. Merge into snagfilms."))

twin("watermelon-express-inc", "Benchprep", "Watermelon Express is BenchPrep's original name (founders Ashish Rangnekar "
     "and Ujjwal Gupta; Wikipedia records the July 2012 $6M round from NEA and Revolution), and Peter Barris sits as its "
     "director at NEA's Timonium address on this 2012 filing.")
L.append(cls("watermelon-express-inc", status="private", rng="below_1b", city="Chicago", focus="SaaS",
             flags=["identity_conflated"],
             note="BenchPrep, Chicago online-learning platform, still operating (aligned with the benchprep row). Stage "
                  "kept from the Form D band of the 2012 $6M round NEA joined (Wikipedia names NEA and Revolution, not "
                  "the round). Graduation left for the graduation pass. Merge into benchprep."))

# ---- Robert Garland
nm("boss-controls-llc", "Robert Garland's 2014-2018 seat (Pittsburgh and Ligonier addresses) falls after his NEA "
   "partner years (to 2013) and no NEA listing, filing or press names Boss Controls.", conf="medium")
nm("disa-llc", "The filing states that Mr. Garland serves on Disa's management board on behalf of Breakthrough 307 "
   "Fund, a Wyoming fund, not NEA.")
nm("enwyo-llc", "Robert Garland is ENWYO's member and manager (2020-2022, Laramie and Greenwood Village), an operator "
   "role; no NEA source names ENWYO.")
nm("intellispex-inc", "Robert Garland is IntelliSpeX's executive officer and promoter (2019-2021, Edgewater, "
   "Maryland), an operator role; no NEA source names the company.")

# ---- Rick Yang
nm("datangle-group-ltd", "Homonym: a $900 filing by a shell whose executive officer 'Rick Yang' gives a Grand Cayman "
   "address; not NEA's Rick Yang and not an operating venture.")
nm("focal-app-inc", "Rick Yang (NEA) is a director of record on Focal App's 2022 filing, but the issuer's business "
   "could not be identified (a Boulder company led by Giles Goodwin; no press, product or NEA listing names it, and "
   "General Catalyst's list carries only the legal name), so the seat stays uncorroborated (COLLECTION.md s1).",
   conf="medium")

twin("hykso-inc", "FightCamp", "Hykso Inc. is FightCamp's issuer (its chief executive Khalil Zahar founded Hykso), and "
     "NEA's Rick Yang, FightCamp's board member on the firm's card, is its director of record.")
L.append(cls("hykso-inc", status="private", rng="below_1b", city="Costa Mesa", city_src="formd_address",
             focus="Consumer & Marketplaces", flags=["identity_conflated"],
             note="FightCamp, connected home boxing. Stage kept from the pre-filled Growth band of the $89.6M offering "
                  "(the firm labels its 2021 entry Growth). City from the company's own 2021 filing (936 W. 17th "
                  "Street, Costa Mesa); the IVP row reads Newport Beach. Merge into fightcamp."))

twin("play-versus-inc", "PlayVS", "Play Versus Inc. files PlayVS's rounds, with NEA's Rick Yang, PlayVS's board member "
     "on the firm's card, as director.")
L.append(cls("play-versus-inc", status="private", rng="below_1b", city="Santa Monica",
             focus="Media, Gaming & Advertising", flags=["identity_conflated"],
             note="High school esports platform (Santa Monica, as the playvs, Battery and Coatue rows read). The "
                  "pre-filled Series A band matches the firm's own 2018 post announcing its Series A investment. "
                  "Merge into playvs."))

# ---- Crystal Huang (NEA Principal from 2018, now a GV general partner)
nm("mechanical-orchard-inc", "Crystal Huang left NEA (a Principal on its 2018 pages) for GV, where she is a general "
   "partner; her 2024-2026 seat is GV's (the GV book holds Mechanical Orchard), and no NEA source names the company.")
nm("prosky-inc", "Homonym: this 'Crystal Huang' is ProSky's own executive officer and director in Lehi, Utah (2019), "
   "not NEA's investor of that name.")
nm("roboflow-inc", "Crystal Huang's 2024 seat is GV's (she is a GV general partner and the GV book holds Roboflow); no "
   "NEA source names Roboflow.")

jl.write("m2a", L)
