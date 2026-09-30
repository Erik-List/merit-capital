"""PRO-100 NEA, stage pass s5, first half (51 rows): the round in which an NEA fund first invested, and the funding
history found (COLLECTION.md s6, PRO-143). Run: NQ_TAG=s5 python3 judgments-s5a.py"""
import json

import judge_lib as jl

cls, rnd, NEWS, SITE, FTS = jl.cls, jl.rnd, jl.NEWS, jl.SITE, jl.FTS
C = json.load(open(jl.INV / "companies" / "classification.json"))
L = []


def R(slug, *new, drop=()):
    """The rounds already on disk for the row (minus `drop` (date, round) pairs), plus the new ones."""
    old = [r for r in (C.get(slug) or {}).get("funding_rounds") or [] if (r.get("date"), r.get("round")) not in drop]
    have = {(r.get("date"), r.get("round"), r.get("source")) for r in old}
    return old + [r for r in new if (r["date"], r["round"], r["source"]) not in have]


def OLD(slug, round_):
    """The source URL of a round already on disk (read, never typed)."""
    m = [r for r in (C.get(slug) or {}).get("funding_rounds") or [] if r.get("round") == round_ and r.get("source")]
    if len(m) != 1:
        raise SystemExit(f"OLD({slug!r}, {round_!r}) matched {len(m)}")
    return m[0]["source"]


def U(slug, note, *new, entry_date=None, drop=()):
    """Stage stays undetermined; the rounds found (or none) are recorded with what was searched."""
    L.append(cls(slug, stage="undetermined", entry_date=entry_date, rounds=R(slug, *new, drop=drop), note=note))


# ---------------- $1B+ and public rows ----------------
MT = "https://www.medianama.com/2015/11/223-mindtickle-raises-12million/"
L.append(cls("mindtickle", stage="Series A", stage_src="web_verified", stage_cite=MT, stage_conf="high",
             entry_date="2015-11-20",
             rounds=R("mindtickle",
                      rnd("2014-10", "Seed", 1800000, None, False, MT, "press"),
                      rnd("2015-11-20", "Series A", 12500000, "NEA", True, MT, "press"),
                      rnd("2021-08-05", "Series E", 100000000, "SoftBank Vision Fund 2", None,
                          NEWS("mindtickle", "Mindtickle becomes a unicorn after SoftBank-led"), "press")),
             note="Stage pass: MediaNama (2015-11-20) reports a $12.5M Series A led by New Enterprise Associates with "
                  "Qualcomm Ventures and existing investor Accel, after a $1.8M seed from Accel and Moneta in October "
                  "2014 without NEA; the firm's 2015 year matches, so NEA entered at the Series A."))

BOX_F3 = jl._base()["box"]["edgar_links"].split(";")[0].strip()
BOX_S1 = "https://www.sec.gov/Archives/edgar/data/1372612/000119312514112417/d642425ds1.htm"
L.append(cls("box", stage="Growth", stage_src="web_verified", stage_cite=BOX_F3, stage_conf="high", entry_date="2011",
             rounds=R("box",
                      rnd("2011", "Series D-2", None, None, True, BOX_S1, "filing"),
                      rnd("2012", "Series E", None, "General Atlantic", True, BOX_S1, "filing")),
             note="Stage pass: NEA 13's Form 3 at the January 2015 IPO lists only Series D2 and Series E preferred and "
                  "common, and the S-1 dates the D-2 issue to 2011 (with a concurrent secondary of DFJ and USVP "
                  "shares); every NEA share is a Series D or later purchase, so Growth. The firm's 2008 year predates "
                  "NEA 13 and is not supported by the filings."))

U("healthsouth", "Stage pass: Wikipedia (Encompass Health) names only the founders' $50,000 and Citicorp Venture "
  "Capital's $1M at the 1984 founding, and EDGAR full text (2001 on) has no NEA purchase; the firm's 1995 year postdates "
  "the 1986 IPO, so the round, if any, is not on record.")

ARCA = FTS("ARCA biopharma", "8-K")
U("arca-biopharma-inc", "Stage pass: NEA's only recorded purchase is the June 2015 private placement led by Venrock into "
  "ARCA, listed on Nasdaq since the 2009 Nuvelo merger, and no filing shows an earlier NEA private round; this is a "
  "public purchase (the X1 class), so the membership verdict should be reviewed rather than a stage written.",
  rnd("2015-06-10", "Private placement (PIPE)", None, "Venrock", True, ARCA, "filing"))

U("linekong", "Stage pass: Google News (the name with NEA) and TechCrunch's own search returned nothing on Linekong's "
  "private rounds; the Hong Kong prospectus that would list NEA's preferred series is not on disk, so the 2008 round "
  "is not named.")

QL = "https://www.sec.gov/Archives/edgar/data/882508/000089843097002476/0000898430-97-002476.txt"
L.append(cls("quicklogic", stage="Growth", stage_src="web_verified", stage_cite=QL, stage_conf="high",
             entry_date="1995-06",
             rounds=R("quicklogic",
                      rnd("1995-06", "Series E", 3200000, None, True, QL, "filing"),
                      rnd("1997", "Series F", 919050, None, True, QL, "filing")),
             note="Stage pass: QuickLogic's 1997 S-1 lists New Enterprise Associates buying $3.2M of Series E "
                  "preferred (June 1995) and $0.9M of Series F, and NEA's 766,244 shares equal exactly those two "
                  "purchases, so NEA entered at the Series E, the firm's 1995 year: Growth."))

TR_SEED = NEWS("translucent", "Translucent AI: $7 Million Raised")
TR_A = OLD("translucent", "Series A")
L.append(cls("translucent", stage="Seed", stage_src="web_verified", stage_cite=TR_SEED, stage_conf="high",
             entry_date="2025-08-07", grad="graduated", grad_src="web_verified", grad_cite=TR_A, grad_conf="high",
             rounds=R("translucent", rnd("2025-08-07", "Seed", 7000000, None, True, TR_SEED, "press"),
                      drop=[("2025-08", "Seed")]),
             note="Stage pass: Pulse 2.0 (2025-08-08) reports the $7M seed funded by NEA, Virtue, FPV and Redesign "
                  "Health, the company's first round and the firm's 2025 year; the $27M Series A led by GV with NEA "
                  "(March 2026, AlleyWatch) graduates it."))

RR = NEWS("red-ridge-bio", "Pierre Fabre Laboratories and RedRidge")
U("red-ridge-bio", "Stage pass: the Pierre Fabre partnership release (PR Newswire, 2025-03-12) says Pierre Fabre joins a "
  "Series A 'to be announced separately', and Google News found no announcement since; NEA's 2023 entry round is not "
  "named.", rnd("2025-03-12", "Series A (announced as forthcoming)", None, None, None, RR, "press"))

U("revelio", "Stage pass: Google News (the name with round words and with NEA) returned only a 2025 hiring item; no "
  "round is on record for NEA's 2022 entry.")

U("trivalence", "Stage pass: Google News (the name with Series A and with funding) returned only the 2025 CEO "
  "appointment and an unrelated Trivalence Technologies merger; no round is on record for NEA's 2021 entry.")

AL_C = NEWS("allay-therapeutics", "Temasek invests in US biotech")
L.append(cls("allay-therapeutics", stage="Series A", stage_src="model", stage_conf="low", entry_date="2019-01-31",
             rounds=R("allay-therapeutics", rnd("2021-09-15", "Series C", 60000000, "Arboretum Ventures", True, AL_C,
                                                "press")),
             note="Stage pass: The Business Times (2021-09-16) names the $60M round of September 2021 a Series C with "
                  "NEA participating; the company's only earlier filed rounds are January 2019 ($28.8M, its first "
                  "Form D, the firm's 2019 year) and April 2020 ($15M), so NEA's 2019 entry reads as the Series A, "
                  "inferred from the sequence rather than named."))

MG19 = NEWS("magenta-medical", "NEA makes first Israeli")
MG17 = NEWS("magenta-medical", "Transcatheter co Magenta Medical raises")
U("magenta-medical", "Stage pass: Globes (2019-07-29) reports NEA leading an undisclosed round, its first Israeli "
  "investment, after a $15M round in 2017 and earlier backing by Pitango; no source names the 2019 round's series.",
  rnd("2017-09-28", "unnamed", 15000000, None, False, MG17, "press"),
  rnd("2019-07-29", "undisclosed", None, "NEA", True, MG19, "press"))

U("cista", "Stage pass: Google News on 'Cista Design' returned nothing; no round is on record for NEA's 2018 entry.")
U("simplerose", "Stage pass: Google News found only a 2023 Business Journals item on a $23M raise (paywalled); no source "
  "names the round of NEA's 2018 entry.")

CAT = "https://techcrunch.com/2021/09/30/dna-based-data-storage-platform-catalog-raises-35m-series-b-to-scale-its-dna-computation/"
L.append(cls("catalog", stage="Seed", stage_src="web_verified", stage_cite=CAT, stage_conf="high", entry_date="2018",
             grad="graduated", grad_src="web_verified", grad_cite=CAT, grad_conf="high",
             rounds=R("catalog",
                      rnd("2018", "Seed", 9000000, "NEA; OS Fund", True, CAT, "press"),
                      rnd("2020", "Series A", 10000000, "Horizons Ventures", None, CAT, "press"),
                      rnd("2021-09-30", "Series B", 35000000, "Hanwha Impact", None, CAT, "press")),
             note="Stage pass: TechCrunch (2021-09-30) says Catalog's $9M seed in 2018 was co-led by New Enterprise "
                  "Associates and OS Fund, followed by a $10M Series A led by Horizons in 2020; NEA entered at the seed "
                  "(the firm lists 2017, a close year) and the Series A graduates it."))

U("pionyr-immunotherapeutics", "Stage pass: Google News (the name with financing, Series B and launch words) returned "
  "only the Gilead option items; no source names the round of NEA's 2017 entry.")

UN = "https://techcrunch.com/2017/08/01/former-battlefield-runnerup-unifiyid-announces-10m-series-a/"
L.append(cls("unifyid", stage="Series A", stage_src="web_verified", stage_cite=UN, stage_conf="high",
             entry_date="2017-08-01",
             rounds=R("unifyid",
                      rnd("2016", "Seed", None, None, False, UN, "press"),
                      rnd("2017-08-01", "Series A", 20000000, "NEA", True, UN, "press")),
             note="Stage pass: TechCrunch (2017-08-01) reports a $20M Series A led by NEA with Andreessen Horowitz, "
                  "StartX and Accomplice, each of which had been in the seed; NEA is not among the seed backers and "
                  "the firm's year is 2017, so NEA entered at the Series A (the a16z row's note calls a16z the lead)."))

GL_C = "https://techcrunch.com/2017/04/20/gladly-incubated-at-greylock-nabs-36-million-in-series-c-funding/"
GL_F = "https://www.finsmes.com/2016/06/customer-service-startup-gladly-raises-27m-in-funding.html"
GL_V = "https://www.crunchbase.com/funding_round/gladly-software-series-b--fb698dd6"
U("gladly", "Stage pass: FinSMEs (2016-06-24) reports $27M from Greylock and NEA without naming rounds, and TechCrunch "
  "calls NEA an earlier backer at the April 2017 Series C; only a vendor profile splits the $27M into a Greylock Series "
  "A and an NEA-led $15M Series B, which cannot cite (Rule A).",
  rnd("2016-06-24", "unnamed ($27M, Greylock and NEA)", 27000000, None, True, GL_F, "press"),
  rnd("2016-06-25", "Series B", 15000000, "NEA", True, GL_V, "vendor"),
  rnd("2017-04-20", "Series C", 36000000, "GGV Capital", True, GL_C, "press"))

BH_S1 = "https://www.sec.gov/Archives/edgar/data/1671284/000110465921069324/tm217793-7_s1.htm"
L.append(cls("neuehealth", stage="Series A", stage_src="web_verified", stage_cite=BH_S1, stage_conf="high",
             entry_date="2016",
             rounds=R("neuehealth",
                      rnd("2016", "Series A", None, None, True, BH_S1, "filing"),
                      rnd("2020-09-22", "Series E", 500000000, None, True,
                          NEWS("neuehealth", "Announces $500 Million Series E"), "company")),
             note="Stage pass: Bright Health's 2021 S-1 principal-stockholder table shows New Enterprise Associates 15 "
                  "holding Series A, B, C and D preferred, Series A being the company's first preferred series, and "
                  "the firm's year is 2016: NEA entered at the Series A."))

BJ = "https://techcrunch.com/2015/05/07/banjo-seriesc/"
L.append(cls("banjo", stage="Growth", stage_src="model", stage_cite=BJ, stage_conf="medium", entry_date="2015",
             rounds=R("banjo",
                      rnd("2010-08", "Series A", 5000000, None, None, BJ, "press"),
                      rnd("2014-03", "Series B", 16000000, None, None, BJ, "press"),
                      rnd("2015-05-07", "Series C", 100000000, "SoftBank", None, BJ, "press")),
             note="Stage pass: TechCrunch (2015-05-07) gives Banjo's $5M Series A (2010), $16M Series B (March 2014) "
                  "and $100M SoftBank-led Series C (May 2015); the firm dates NEA's first investment to 2015, after "
                  "the Series B, so NEA entered at the Series C or later: Growth, inferred from the dated history."))

GP_A = "https://www.builtinla.com/articles/gwyneth-paltrows-goop-secures-10-million-plans-move-la"
L.append(cls("goop", stage="Series A", stage_src="web_verified", stage_cite=GP_A, stage_conf="high", entry_date="2015-08",
             rounds=R("goop",
                      rnd("2015-08", "Series A", 10000000, "NEA", True, GP_A, "press"),
                      rnd("2016-08-16", "Series B", 10000000, None, True, NEWS("goop", "Gwyneth goes west"), "press")),
             note="Stage pass: Built In LA (2016-08-17) says Goop 'received a nearly identical Series A funding led by "
                  "New Enterprise Associates in August 2015', and NEA's Tony Florence spoke of 'accelerating our "
                  "investment' at the Series B; the firm's year is 2015, so NEA entered at the Series A."))

U("mode", "Stage pass: TechCrunch's own search found nothing further; the company's 2018 release says NEA led an $8M Series "
  "A closed in 2017, while the firm dates its first investment to 2015, so an earlier NEA round may exist and the entry "
  "is not established.")

SW = NEWS("swift-navigation", "34 Million Series B")
L.append(cls("swift-navigation", stage="Growth", stage_src="model", stage_cite=SW, stage_conf="medium",
             entry_date="2017-07-13",
             rounds=R("swift-navigation",
                      rnd("2017-07-13", "Series B", 34000000, "NEA", True, SW, "press"),
                      drop=[("2017-07-13", "Series B")]),
             note="Stage pass: Inside Unmanned Systems (2017-07-13) reports the $34M Series B led by NEA's Forest "
                  "Baskett and Greg Papadopoulos 'with participation from existing investors Eclipse and First Round', "
                  "so NEA reads as new at the Series B: Growth. The firm's own 2015 year conflicts with this and is "
                  "left for review."))

U("xtuit", "Stage pass: Google News on 'XTuit Pharmaceuticals' and with Polaris and NEA returned nothing on its rounds; "
  "the Form D history ($1.5M in 2014, $22M in November 2014) does not name NEA's round.")
U("cape", "Stage pass: TechCrunch's own search and Google News returned no funding report for Cape Productions (the drone "
  "video service); NEA's 2014 round is not named.")

NX = "https://www.sec.gov/Archives/edgar/data/1538210/000119312521045015/d344961d424b4.htm"
U("neximmune", "Stage pass: the 2021 IPO prospectus dates the Series A to December 2017 through August 2018 ($25.0M), "
  "then Series A-2 and A-3 in 2019, so NEA's 2014 round ($3.0M, James Barrett director of record) came before the "
  "Series A and is not named.",
  rnd("2014-07-10", "unnamed (pre-Series A)", 3000000, None, True,
      jl._base()["neximmune"]["formd_links"].split(";")[0].strip(), "filing"),
  rnd("2017-12", "Series A", 25000000, None, None, NX, "filing"),
  rnd("2019-01", "Series A-2", 7800000, None, None, NX, "filing"),
  rnd("2019-11", "Series A-3", 11000000, None, None, NX, "filing"), entry_date="2014")

U("ulink", "Stage pass: no source searched (its own Chinese site, Google News) names a round; NEA's 2014 entry round is "
  "not on record.")
U("ziarco", "Stage pass: Google News (the name with NEA and with financing) returned only the 2016 Novartis sale and "
  "later items; the round NEA joined in 2014 is not named.")

CIR = "https://techcrunch.com/2010/09/20/cirtas-raises-10-million-from-amazon-and-others-launches-cloud-storage-system/"
L.append(cls("cirtas-systems-inc", stage="Series A", stage_src="web_verified", stage_cite=CIR, stage_conf="high",
             entry_date="2010-09-20",
             rounds=R("cirtas-systems-inc", rnd("2010-09-20", "Series A", 10000000, None, True, CIR, "press")),
             note="Stage pass: TechCrunch (2010-09-20) reports Cirtas raising $10M in Series A funding from NEA, "
                  "Lightspeed Venture Partners and Amazon, its first reported round: NEA entered at the Series A."))

EKO = NEWS("eko", "MGM Leads")
U("eko", "Stage pass: TheWrap (2015-12-08) calls MGM's $18.2M investment Interlude's third round (over $36M in total, "
  "Sequoia and Intel Capital returning); neither earlier round, nor the one NEA joined in 2013, is named in any source "
  "found.", rnd("2015-12-08", "third round", 18200000, "MGM", None, EKO, "press"))

U("forhealth-technologies", "Stage pass: Google News and TechCrunch's own search returned nothing on ForHealth's "
  "rounds; NEA's round is not on record.")

TL13 = "https://techcrunch.com/2013/08/14/thirdlove-5-6m-bra-iphone/"
TL16 = "https://techcrunch.com/2016/02/02/thirdlove-bras/"
L.append(cls("mecommerce", stage="Seed", stage_src="web_verified", stage_cite=TL13, stage_conf="high",
             entry_date="2013-08-14", grad="graduated", grad_src="web_verified", grad_cite=TL16, grad_conf="high",
             rounds=R("mecommerce",
                      rnd("2013-08-14", "Seed", 5600000, "NEA", True, TL13, "press"),
                      rnd("2016-02-02", "Series A", 8000000, "NEA", True, TL16, "press")),
             note="Stage pass: MeCommerce is ThirdLove's parent. TechCrunch (2013-08-14) reports its $5.6M seed led by "
                  "NEA with Andreessen Horowitz and Felicis, and (2016-02-02) an $8M Series A led by NEA, which "
                  "graduates the seed. ThirdLove still trades, so the defunct status is doubtful."))

NI = "https://techcrunch.com/2014/03/11/stealthy-enterprise-security-company-niara-raises-9m-from-index-and-nea/"
U("niara", "Stage pass: TechCrunch (2014-03-11) reports Niara's $9M from Index and NEA without naming the round; no "
  "later source names it, so the stage stays undetermined.",
  rnd("2014-03-11", "unnamed", 9000000, None, True, NI, "press"))

U("pmc-sierra-inc", "Stage pass: pre-web era; TechCrunch and Google News carry nothing on its private rounds, and EDGAR "
  "full text starts after its listing; NEA's round is not on record.")
U("shenghui-lighting", "Stage pass: Google News and TechCrunch's own search returned nothing on the company's rounds; "
  "NEA's round is not on record.")
U("targetrx-inc", "Stage pass: Google News and TechCrunch's own search returned nothing on TargetRx's rounds; NEA's "
  "round is not on record.")

VC = "https://techcrunch.com/2014/06/17/virtualizing-wide-area-networks-velocloud-rings-up-21-million/"
L.append(cls("velocloud", stage="Series A", stage_src="model", stage_cite=VC, stage_conf="medium", entry_date="2013",
             rounds=R("velocloud",
                      rnd("2012-11", "Seed", None, None, None, VC, "press"),
                      rnd("2013", "unnamed ($5M commitment)", 5000000, "NEA", True, VC, "press"),
                      rnd("2014", "Series B", 15000000, "Venrock", None, VC, "press")),
             note="Stage pass: TechCrunch (2014-06-17) says VeloCloud raised a seed in November 2012, 'followed by a "
                  "$5 million commitment from NEA', then Venrock led the $15M Series B; NEA's round sits between the "
                  "seed and the Series B, so it is the Series A (firm year 2013), inferred from the sequence."))

BP12 = "https://techcrunch.com/2012/07/03/benchprep-raises-6m/"
BP19 = "https://www.builtinchicago.org/articles/benchprep-20-million-funding-round"
L.append(cls("benchprep", stage="Growth", stage_src="model", stage_cite=BP12, stage_conf="medium",
             entry_date="2012-07-03",
             rounds=R("benchprep",
                      rnd("2011", "unnamed", 2200000, "Lightbank", False, BP12, "press"),
                      rnd("2012-07-03", "unnamed", 6000000, "NEA", True, BP12, "press"),
                      drop=[("2012-07", None)]),
             note="Stage pass: TechCrunch (2012-07-03) calls NEA's $6M the company's second round after $2.2M from "
                  "Lightbank, and Built In Chicago (2019) says the $20M Series C was the first new capital since, "
                  "bringing the total to $28.2M; with only two earlier rounds, NEA's is the Series B: Growth, inferred."))

U("gainspeed", "Stage pass: Google News and TechCrunch's own search returned no funding report for Gainspeed; the Form D "
  "history (from September 2012, the firm's year) does not name the round.")
U("solace-therapeutics", "Stage pass: Google News (the name with financing) returned nothing; NEA's 2012 round is not "
  "named.")
U("air-works", "Stage pass: Google News (the name with NEA) returned only the Adani deals; NEA's 2011 round is not "
  "named.")

GK = "https://techcrunch.com/2011/07/20/cloud-based-game-streaming-service-gaikai-raises-30m-from-qualcomm-nea-and-others/"
L.append(cls("gaikai", stage="Growth", stage_src="model", stage_cite=GK, stage_conf="medium", entry_date="2011-07-20",
             rounds=R("gaikai", rnd("2011-07-20", "unnamed", 30000000, "NEA", True, GK, "press")),
             note="Stage pass: TechCrunch (2011-07-20) reports a $30M round led by NEA with Qualcomm, Benchmark, Rustic "
                  "Canyon and Intel Capital, bringing funding over $40M; it followed the 2010 round PR Newswire "
                  "announced as the Series B (the Benchmark row), so NEA's 2011 entry is Growth, inferred."))

U("leyden-energy", "Stage pass: Google News and TechCrunch's own search returned only the 2013 technology profile and the "
  "2014 A123 asset purchase; NEA's 2011 round is not named.")
U("vibrynt-inc", "Stage pass: Google News on the name returned nothing on its rounds; the firm's 2021 post says NEA and "
  "ExploraMed spun the company out, but no source names the round, and the 2011 Form D is a later filing.")

EU10 = "https://techcrunch.com/2010/07/01/eucalyptus-systems-raises-20-million-for-open-source-private-cloud-software/"
EU12 = "https://techcrunch.com/2012/04/18/open-source-private-cloud-software-startup-eucalyptus-raises-30m-from-ivp-benchmark-to-take-on-vmware/"
L.append(cls("eucalyptus-systems", stage="Growth", stage_src="model", stage_cite=EU10, stage_conf="medium",
             entry_date="2010-07-01",
             rounds=R("eucalyptus-systems",
                      rnd("2010-07-01", "unnamed", 20000000, "NEA", True, EU10, "press"),
                      rnd("2012-04-18", "Series C", 30000000, "IVP", True, EU12, "press"),
                      drop=[("2010", None), ("2012-04", None)]),
             note="Stage pass: TechCrunch (2010-07-01) reports $20M led by NEA with current investors Benchmark and BV "
                  "Capital, total $25.5M, so the round after Benchmark's $5.5M Series A; the 2012 round was the Series "
                  "C. NEA's 2010 entry is therefore the Series B: Growth, inferred from the sequence."))

SN = "https://techcrunch.com/2013/01/18/snagfilms-another-6m/"
U("snagfilms", "Stage pass: TechCrunch (2013-01-18) lists NEA among existing investors in a $6M round, SnagFilms having "
  "raised $17M since 2008; no source names the round NEA entered in 2010.",
  rnd("2013-01-18", "unnamed", 6000000, None, True, SN, "press"))

U("astrowatt", "Stage pass: TechCrunch's own search and Google News returned nothing on AstroWatt's rounds; the 2009 "
  "Form D does not name NEA's round.")
U("jobfox-inc", "Stage pass: TechCrunch's own search returned no funding report for Jobfox; NEA's round is not named.")
U("svaya-nanotechnologies", "Stage pass: Google News on the name returned nothing on its rounds; NEA's 2009 round is not "
  "named.")
U("adaptec-inc", "Stage pass: pre-web era, listed in 1986; no source on disk or searched names the round NEA entered.")
U("agitar-software-inc", "Stage pass: Google News and TechCrunch's own search returned nothing on Agitar's rounds; NEA's "
  "round is not named.")

jl.write("s5a", L)
