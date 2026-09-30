"""PRO-100 NEA, judge m2, part b: slugs 39-76 of queue/m2.json (Form D name-match rows), judged cluster-first.

Clusters resolved (the firm's own team pages give the years):
- Crystal Huang: now a GV general partner; Sift's 2024 seat is GV's.
- Aaron Jacobson: NEA 2013 to date. Araz (= DeltaStream), Azevtec (= Outrider) and FloxDev (= Flox) are legal-name
  twins of listed rows.
- ChenLi Wang: NEA associate 2009-2010, now at WndrCo (with Sujay Jaswa); his 2019-2025 seats are out.
- Jeff Immelt: NEA venture partner since 2018 (D4). NBCUniversal is his GE role, Twilio an independent directorship
  of a listed company, Sila and MGT carry no NEA source. All out.
- James Barrett: NEA general partner to about 2019. ZP Holdings is Zosano (one CIK); AgeneBio carries his seat.
- Chetan Puttagunta: NEA to 2018, then Benchmark (Airbyte out); Logik Systems is Logikcull.
- James Treybig: ATX Innovation is TabbedOut (with Scott Sandell at NEA's address); Moray Farms is personal.
- Richard Yang (Biolinq, Sonablate), Jeongseuk / Jeong Gu Kang: homonyms. Jeong Kang (BlocPower) predates NEA's
  associate Jeon Kang.
- Josh Makower: DOTS Devices is DOTS Technology; ExploraMed NC6 is Nuelle; Wine Mosquito is Coravin, his own co-founded
  company. George Stamas: personal ventures after 2013. Jon Sakoda: Hearsay Labs and Players Tribune are twins.
- Lila Tretikov (NEA from 2024): Onfido and Toloka are independent directorships. Michele Park (Clarus), Matt Sacks
  (Lightbank), Yida Gao (Shima), Vladimir Jacimovic, Michael O'Dell (Dignitas homonym): out.
- Edward Mathers: OnKure is Reneo renamed (one CIK). Patrick Kerins: TidalTV is Videology.
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


nm("sift-stack-inc", "Crystal Huang's 2024 seat is GV's (she left NEA, a Principal on its 2018 pages, and is a GV "
   "general partner); no NEA source names Sift.")

# ---- Aaron Jacobson
DS_A = jl.NEWS("araz-inc", "DeltaStream Raises $15M in Series A")
twin("araz-inc", "DeltaStream", "Araz Inc. is founder Hojjat Jafarpour's company, filed with NEA's Aaron Jacobson, "
     "DeltaStream's board member on the firm's card, as director at NEA's Sand Hill Road address (2020).")
L.append(cls("araz-inc", status="private", rng="below_1b", stage="Seed", stage_src="first_party",
             stage_cite=jl.SITE("deltastream"), stage_conf="medium", entry_date="2020-12-23", grad="graduated",
             grad_src="web_verified", grad_cite=DS_A, grad_conf="high", grad_asof="2024-09-17",
             city="Menlo Park", focus="Data Infrastructure", flags=["identity_conflated", "stage_disputes_band"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": DS_A},
             rounds=[rnd("2020-12-23", "Seed", 9500000, None, True, jl.SITE("deltastream"), "firm"),
                     rnd("2024-09-17", "Series A", 15000000, None, None, DS_A, "press")],
             note="Serverless stream processing, Menlo Park (as the deltastream row reads). The firm labels its 2020 "
                  "entry Seed, which replaces the pre-filled Series A band of this $10.2M filing; Business Wire "
                  "(2024-09-17) reports DeltaStream's $15M Series A, so it graduated. Momentum check 2026-09-30 "
                  "(Google News): that Series A is the latest priced round, nothing near $1B. Merge into deltastream."))

twin("azevtec-inc", "Outrider", "Azevtec, Inc. renamed itself Outrider Technologies, Inc. in 2018 (EDGAR CIK 1724273, "
     "the CIK of the outrider row's filings), with NEA's Aaron Jacobson as director on the 2018 filing.")
L.append(cls("azevtec-inc", status="private", rng="below_1b", stage="Series A", stage_src="formd_band",
             stage_conf="medium", entry_date="2018-06-22", city="Brighton", focus="Industrial & Robotics",
             flags=["identity_conflated"],
             note="Autonomous yard trucks, Colorado (Brighton, as the outrider row reads from the 2026 filing; the 8VC "
                  "row reads Golden). The firm dates its first investment 2018, the year of this $8.1M round after a "
                  "$2.5M 2017 filing, which the band reads as a Series A. No $1B+ round on record. Merge into "
                  "outrider."))

FLOX_A = jl.NEWS("floxdev-inc", "Flox raises $27M")
FLOX_B = jl.NEWS("floxdev-inc", "$25 Million Series B")
twin("floxdev-inc", "Flox", "FloxDev, Inc. is Flox's issuer (the firm's card links floxdev.com and seats Aaron "
     "Jacobson, its director of record here, on the board), and TechCrunch (2023-02-07) reports NEA led its $16.5M "
     "Series A.")
L.append(cls("floxdev-inc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=FLOX_A, stage_conf="high", city="New York", city_src="formd_address",
             focus="DevTools & APIs", flags=["identity_conflated"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": FLOX_B},
             rounds=[rnd("2023-02-07", "Series A", 16500000, "NEA", True, FLOX_A, "press"),
                     rnd("2025-09-29", "Series B", 25000000, None, None, FLOX_B, "press")],
             note="Nix-based developer environments, New York (the company's filing address). NEA led the $16.5M "
                  "Series A (TechCrunch, 2023-02-07), the firm's 2023 first-investment year. Momentum check "
                  "2026-09-30 (Google News): the latest round is a $25M Series B (Pulse 2.0, 2025-09-29), nothing near "
                  "$1B. Merge into flox."))

# ---- ChenLi Wang (NEA associate 2009-2010, now WndrCo)
nm("daydream-labs-inc", "ChenLi Wang was an NEA associate in 2009-2010 (the firm's team pages); his 2025 seat falls "
   "long after, in his WndrCo years, and no NEA source names daydream.")
nm("netomi-inc", "ChenLi Wang's 2021 seat is WndrCo's, a decade after his NEA associate years (2009-2010); no NEA "
   "source names Netomi.")
nm("wc-sacd-holdings-inc", "WC SACD Holdings (now Point Wild Holdings, iSubscribed's parent) seats ChenLi Wang and "
   "Sujay Jaswa, both of WndrCo, c/o iSubscribed in 2019-2020; both left NEA after 2010, and no NEA source names it.")

# ---- Jeff Immelt (NEA venture partner since 2018)
nm("mgt-partners-inc", "Jeff Immelt is an NEA venture partner, and D4 counts his seat only where an NEA fund held the "
   "position; MGT, an AI small-business insurer, names Mubadala, Clocktower and Tacora in its Series B coverage and no "
   "NEA source names it.", conf="medium",
   cite="https://programbusiness.com/news/mgt-raises-21-6-million-to-expand-ai-native-small-business-insurance/")
nm("nbcuniversal-media-llc", "Jeffrey Immelt signs as a director of NBCUniversal c/o General Electric (2011), his GE "
   "operating role years before he joined NEA in 2018.")
nm("sila-nanotechnologies-inc", "Jeff Immelt (NEA venture partner since 2018) sits on Sila's board beside Bessemer, "
   "Sutter Hill, Matrix and Daimler directors; D4 counts a venture partner's seat only where an NEA fund held the "
   "position, and no NEA listing, filing or press names Sila.", conf="medium")

# ---- James Barrett
L.append(verdict("agenebio-inc", "member", "M. James Barrett, an NEA general partner in 2013, is a director of record "
                 "on AgeneBio's 2013 filings; AgeneBio is a real operating company (the Johns Hopkins spinout "
                 "developing AGB101 for Alzheimer's-related memory impairment). Unannounced on the firm's pages; "
                 "flagged for the A/B pass.", ec="formd_adjudicated", conf="medium", cite=fd("agenebio-inc")))
L.append(cls("agenebio-inc", status="private", rng="below_1b", stage="undetermined", entry_date="2013",
             city="Baltimore", focus="Healthcare & Bio",
             note="Baltimore biotech, still active in 2026 (Pulse 2.0). Barrett's seat dates from the 2013 filings, "
                  "after several earlier small raises from 2009; no source names the round NEA may have joined, so "
                  "the stage is undetermined."))

twin("zp-holdings-inc", "Zosano", "ZP Holdings Inc renamed itself Zosano Pharma Corp in 2014 (EDGAR CIK 1587221, the "
     "zosano row's EDGAR CIK); its S-1 records a 2013 convertible note to New Enterprise Associates 12, and James "
     "Barrett, NEA general partner, joined its board at the October 2013 closing.")
L.append(cls("zp-holdings-inc", rng="below_1b", stage="Growth", stage_src="first_party", stage_cite=jl.SITE("zosano"),
             stage_conf="medium", entry_date="2007", city="Fremont", focus="Healthcare & Bio",
             flags=["identity_conflated", "stage_disputes_band"],
             note="Zosano Pharma, Fremont transdermal drug delivery; Chapter 11 in 2022 with its assets sold, so "
                  "acquired below $1B. The pre-filled Seed band reads the 2013 recapitalisation filing; the firm's own "
                  "card dates its first investment 2007 and labels it Growth. Merge into zosano."))

# ---- Chetan Puttagunta (NEA to 2018, then Benchmark)
nm("airbyte-inc", "Chetan Puttagunta left NEA (last on its pages in 2018) for Benchmark; his 2021 seat is Benchmark's, "
   "which led Airbyte's Series A, and no NEA source names Airbyte.")
twin("logik-systems-inc", "Logikcull", "Logik Systems, Inc. files Logikcull's January 2018 $25M round (San Francisco; "
     "founders Andrew Wilson and Sheng Yang) with Chetan Puttagunta, then an NEA general partner, as director at NEA's "
     "Timonium address.")
L.append(cls("logik-systems-inc", status="acquired", rng="below_1b", stage="Growth", stage_src="model",
             stage_conf="medium", city="San Francisco", focus="SaaS",
             flags=["identity_conflated", "stage_disputes_band"],
             rounds=[rnd("2018-01-25", "Series B", 25000000, "NEA", True, fd("logik-systems-inc"), "filing")],
             note="eDiscovery software, San Francisco; acquired by Reveal in 2023 (LawSites, 2023-08-29). The $25M "
                  "January 2018 round NEA led was Logikcull's Series B (OpenView's Blake Bartlett, an earlier "
                  "investor, sits on the same filing), so Growth at medium confidence replaces the pre-filled Series A "
                  "band; the firm dates its first investment 2018. Merge into logikcull."))

# ---- James Treybig
twin("atx-innovation-inc", "TabbedOut", "ATX Innovation, Inc. is TabbedOut's Austin issuer (executive Rick Orr, named "
     "in TabbedOut's 2012 coverage), filed with NEA's Scott Sandell as director at NEA's Timonium address and James "
     "Treybig on its 2010 filing, the year the firm dates its first investment.")
L.append(cls("atx-innovation-inc", status="private", rng="below_1b", city="Austin", focus="Fintech & Payments",
             flags=["identity_conflated"],
             note="Mobile bar-tab payments, Austin, since renamed Union (the union and tabbedout rows), still private. "
                  "Stage kept from the Form D band of this 2010 round. Graduation left for the graduation pass. Merge "
                  "into tabbedout."))
nm("moray-farms-holdings-llc", "James Treybig is the manager of a farm holding company (2011, $50K sold), a personal "
   "venture; no NEA source names it.")

# ---- Richard Yang (homonym)
nm("biolinq-inc", "Homonym: Richard (Rich) Yang is Biolinq's own chief executive, an executive officer on every filing, "
   "not NEA's Rick Yang; no NEA source names Biolinq.")
nm("sonablate-corp", "Homonym: the Richard Yang on Sonablate's 2023 filing is its executive officer in Charlotte, not "
   "NEA's Rick Yang; no NEA source names Sonablate.")

# ---- Josh Makower, George Stamas
twin("dots-devices-inc", "DOTS Technology Corp", "DOTS Devices, Inc. renamed itself DOTS Technology Corp. in 2016 "
     "(EDGAR CIK 1652512, the CIK of the dots-technology-corp row's filings), with Josh Makower of NEA as its director.")
L.append(cls("dots-devices-inc", status="private", rng="below_1b", stage="Series A", stage_src="formd_band",
             stage_conf="medium", entry_date="2015-08-25", city="Natick", focus="Healthcare & Bio",
             flags=["identity_conflated"],
             note="Point-of-care allergen detection, Natick (aligned with the dots-technology-corp row). This 2015 $10M "
                  "round, the company's first filing and the firm's first-investment year, bands as a Series A. The "
                  "Felicis, Northzone and YC Dots rows are other companies. Merge into dots-technology-corp."))
nm("wine-mosquito-llc", "Josh Makower co-founded Coravin (the firm's own 2015 release calls him a Coravin "
   "co-founder), and Wine Mosquito LLC is Coravin's original name (EDGAR CIK 1517698), so the seat is a founder's; no "
   "NEA listing or filing names Coravin. Same issuer as the coravin-llc row.",
   cite=jl.POST("nea-names-josh-makower"))
nm("enduring-hydro-llc", "George Stamas is a manager of Enduring Hydro (Kristina Johnson's hydropower company) in "
   "2014, after his last NEA title (venture advisor, 2013); no NEA source names it.")
nm("fleet-street-energy-llc", "George Stamas is Fleet Street Energy's co-manager (an executive role, 2011); no NEA "
   "source names the company.")

# ---- Jon Sakoda
twin("hearsay-labs-inc", "Hearsay Social", "Hearsay Labs, Inc. filed its July 2011 $18M round with Jon Sakoda, NEA "
     "partner, as director c/o New Enterprise Associates.")
L.append(cls("hearsay-labs-inc", status="acquired", rng="below_1b", city="San Francisco", focus="SaaS",
             flags=["identity_conflated"],
             note="Hearsay Systems, social and compliance software for financial advisers, San Francisco; Yext "
                  "acquired it in 2024 (as the hearsay-social and Sequoia rows read). The pre-filled Series A band is "
                  "the July 2011 $18M round, the firm's first-investment year. Merge into hearsay-social."))
twin("players-tribune-inc", "The Players' Tribune", "its 2015 filing ($9.5M sold, Jon Sakoda of NEA as director) is "
     "the investment Wikipedia reports NEA made in June 2015.")
L.append(cls("players-tribune-inc", status="acquired", rng="below_1b", city="New York",
             focus="Media, Gaming & Advertising", flags=["identity_conflated"],
             note="Athlete-written sports media, New York; acquired by Minute Media in 2019 (the firm's exit line; "
                  "aligned with the GV and IVP rows). The pre-filled Series A band is NEA's June 2015 $9.5M "
                  "investment, after a 2014 $3M filing. Merge into the-players-tribune."))

# ---- Lila Tretikov (NEA from 2024)
nm("onfido-ltd", "Lila Tretikov joined NEA in 2024; her 2020 seat is an independent directorship (the firm's own 2024 "
   "release lists Onfido among her independent boards), and no NEA source names Onfido's rounds.",
   cite=jl.POST("nea-appoints-lila-tretikov"))
nm("toloka-group-inc", "Lila Tretikov's 2025 seat on Toloka (a Nebius-controlled company) matches her independent "
   "directorships; its May 2025 $72M round was led by Bezos Expeditions with Mikhail Parakhin (SiliconANGLE, "
   "2025-05-07), and no NEA source names Toloka.", conf="medium",
   cite="https://siliconangle.com/2025/05/07/ai-data-provider-toloka-raises-72m-funding/")

# ---- the Kang names
nm("amaryllis-therapeutics-inc", "Homonym: Jeongseuk Kang is the issuer's own executive officer (Cambridge, 2024), not "
   "an NEA investor.")
nm("blocpower-public-benefit-corp", "The 2020 director 'Jeong Kang' predates NEA's associate Jeon Kang (on the firm's "
   "pages 2021-2023), and an associate is not a director of record; no NEA source names BlocPower.")
nm("dignitas-esports-llc", "The Michael O'Dell on Dignitas' 2017 filing is its manager at 3 Banner Way, Camden, the "
   "Philadelphia 76ers' base under Harris Blitzer Sports & Entertainment, Dignitas' owner; not NEA's venture partner, "
   "and no NEA source names Dignitas.", conf="medium")

twin("exploramed-nc6-inc", "Nuelle", "ExploraMed NC6, Inc. renamed itself Nuelle, Inc. in 2014 (EDGAR CIK 1595965, the "
     "CIK of the nuelle row's filings), one of the ExploraMed companies Josh Makower builds with NEA, with NEA's John "
     "Nehra and Ryan Drant as directors.")
L.append(cls("exploramed-nc6-inc", status="acquired", rng="below_1b", stage="Series A", stage_src="formd_band",
             stage_conf="medium", entry_date="2014-01-13", city="Mountain View", city_src="formd_address",
             focus="Healthcare & Bio", flags=["identity_conflated"],
             note="Women's sexual wellness device company; the firm's card reads Acquired, with Aytu BioScience as the "
                  "exit. This January 2014 $14M round, its first filing, bands as a Series A (the nuelle row's "
                  "pre-filled stage). City from the filing's ExploraMed address. Merge into nuelle."))
nm("jk-biopharma-solutions-inc", "Homonym: Jeong Gu Kang is the issuer's own executive officer (Potomac, Maryland; a "
   "$50K filing), not NEA.")
nm("midnight-evergreen-technologies-inc", "Yida Gao was an NEA associate in 2017 (the firm's pages); his 2022 seat, "
   "filed from a Tortola address, falls after he left to co-found Shima Capital, and no NEA source names the company.")

# ---- Edward Mathers
RENEO_S1 = "https://www.sec.gov/Archives/edgar/data/1637715/000119312521087741/d63585ds1.htm"
twin("onkure-therapeutics-inc", "Reneo Pharmaceuticals", "Reneo renamed itself OnKure Therapeutics after its 2024 "
     "merger (EDGAR CIK 1637715, the reneo row's CIK; the firm's card reads NASDAQ: OKUR), and Edward Mathers, NEA "
     "partner and Reneo director since 2017, signs this 2024 filing.")
L.append(cls("onkure-therapeutics-inc", stage="Series A", stage_src="web_verified", stage_cite=RENEO_S1,
             stage_conf="high", entry_date="2015", city="Boulder",
             flags=["identity_conflated", "stage_disputes_band"],
             note="Reneo's 2021 S-1 lists Series A convertible preferred bought by New Enterprise Associates 15 at the "
                  "first closing, and the firm dates its first investment 2015; the pre-filled Growth band reads the "
                  "$65M private placement at the 2024 merger. OnKure is based in Boulder. Merge into "
                  "reneo-pharmaceuticals."))

nm("sientra-inc", "Michele Park signs Sientra's 2012 filing c/o Clarus Ventures, her firm before NEA (on its pages from "
   "2021).")
nm("springbig-holdings-inc", "Matt Sacks joined SpringBig's board in 2024 as co-managing partner of Lightbank, after "
   "leaving NEA (last on its pages in 2018), per SpringBig's own 8-K; and SpringBig was already listed (X1).")

# ---- Patrick Kerins
twin("tidaltv-inc", "Videology", "TidalTV, Inc. renamed itself Videology, Inc. in 2011 (EDGAR CIK 1473620, the CIK of "
     "the videology row's filings), with NEA's Patrick Kerins as director.")
L.append(cls("tidaltv-inc", status="acquired", rng="below_1b", stage="undetermined", entry_date="2008",
             city="New York", focus="Media, Gaming & Advertising", flags=["identity_conflated"],
             note="Video advertising platform founded in Baltimore as TidalTV, later in New York; Chapter 11 in 2018 "
                  "with its assets bought by Amobee (aligned with the videology row). The firm dates its first "
                  "investment 2008; no page names the round. Merge into videology."))

nm("twilio-inc", "Jeff Immelt joined Twilio's board in 2019 as an independent director of a listed company (Twilio's "
   "release calls him an NEA venture partner); the 2020-21 filings are post-IPO issuances, and NEA held no private "
   "round in Twilio (X1, T3).", cite=jl.FTS("TWILIO", "8-K"))
nm("videahealth-inc", "Vladimir Jacimovic appears on the firm's pages only as a 2008 venture partner; his 2019-2022 "
   "seat is a decade later, and no NEA source names VideaHealth.")

jl.write("m2b", L)
