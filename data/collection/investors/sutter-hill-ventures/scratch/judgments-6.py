#!/usr/bin/env python3
"""Batch 6 of the Sutter Hill Ventures grind (PRO-77): 45 rows.

25 Form D rows judged for membership cluster-first (James White, Stefan
Dyckerhoff, Mike Speiser, Greg Sands, Ron Bernal, Andrew Sheehan, Keith
Loebner, Jeffrey Bird), two seeded rows disputed (venture-tdf-china-llc under
D6, aruba-networks-inc under D4), and every open column of the members.
Run: NQ_TAG=b6 python3 judgments-6.py
"""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, ARCH, W, NEWS, SEC, FORMD_CITE

N = 6
L = []

# ---- citations: helpers, or URLs printed by a tool run in this session
PRN_CREDIT_GENIE = NEWS("creditly-corp", "Credit Genie Secures $4 Million Series A")
FINOVATE_FINICITY = NEWS("finicity-corp", "FinTech Automation Inks Consumer Data")
GQ_AIR_PROTEIN = NEWS("air-protein-inc", "Air Protein Bags US$32M In Series A")
PULSE_ARIA = NEWS("aria-networks-inc", "Aria Networks: $125 Million Raised")
PRN_FATHOM = NEWS("atommap-corp", "Fathom Therapeutics, Formerly Atommap")
AUGMENT_BLOG = NEWS("augment-computing-inc", "Augment Code raises $227 Million")
PULSE_CELERO = NEWS("celero-communications-inc", "Celero Communications: $140 Million Raised")
SA_CELERO = NEWS("celero-communications-inc", "Celero Communications raises $140M")
AWS_CLUMIO = NEWS("clumio-inc", "Clumio CEO on Steering the Startup")
GNW_CLUMIO = NEWS("clumio-inc", "Clumio Announces $75M Series D")
NEXTPLATFORM_ENF = NEWS("enfabrica-corp", "Enfabrica Converges Extended Memory")
SA_ENF_B = NEWS("enfabrica-corp", "Enfabrica raises $125M to scale up GPUs")
CBN_ENF_C = NEWS("enfabrica-corp", "Nvidia-Backed Enfabrica Locks Up $115M")
ELDIARIO_EVERSIGHT = NEWS("eversight-inc", "Eversight Raises $14.5M Round Led by Sutter Hill")
GAMEDEV_FORTERRA = NEWS("forterra-systems-inc", "Forterra Spins Off There MMO To Makena")
TC_GHOST = NEWS("ghost-autonomy-inc", "OpenAI-backed Ghost Autonomy shuts down")
# printed by WebSearch / WebFetch / the EDGAR full-text tool in this session
CMSWIRE_WAVEFRONT = "https://www.cmswire.com/information-management/wavefront-closes-52m-series-b-round-eyes-global-expansion/"
TANZU_WAVEFRONT_B = ("https://blogs.vmware.com/tanzu/wavefront-raises-52m-in-series-b-funding-to-accelerate-"
                     "leadership-in-cloud-application-monitoring-for-enterprises-and-saas-companies/")
SILICONREPUBLIC_VALISTA = "https://www.siliconrepublic.com/business/belfasts-aepona-acquires-dublins-valista"
USANA_S3 = "https://www.sec.gov/Archives/edgar/data/896264/000110465910052346/a10-19366_1s3.htm"

# =====================================================================
# A. Form D rows: membership, cluster by cluster
# =====================================================================

# --- James White cluster. SHV's Jim White is James N. White, on the firm's
# roster 2001 to 2017, filing from 755 Page Mill Road (Glassdoor, WebVisible).
L.append(verdict("access-industrial-maintenance-inc", "not_member",
    "Name-match only: James T. White on the 2011 Form D is a shareholder and former executive officer "
    "filing from Hermitage, Missouri, for a Denver maintenance company; SHV's Jim White (James N. White) "
    "files from 755 Page Mill Road. No SHV listing, filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("access-industrial-maintenance-inc")))
L.append(verdict("air-protein-inc", "not_member",
    "Name-match only: the James White on Air Protein's 2020 Form D is a director and executive officer at "
    "the company's Pleasanton address, not SHV's James N. White (755 Page Mill Road; last on the firm's "
    "roster in 2017). Air Protein's $32M Series A came from ADM Ventures, Barclays and GV (Green Queen, "
    "2021-01-09); no SHV listing, filing or round names the company.",
    ec="formd_adjudicated", conf="high", cite=GQ_AIR_PROTEIN))
L.append(verdict("anova-financial-corp", "not_member",
    "Name-match only: James D. White is one of eight directors of a bank holding company in Edenton, North "
    "Carolina, all filing from 112 West Eden Street; not SHV's James N. White. No SHV listing, filing or "
    "documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("anova-financial-corp")))
L.append(verdict("antipesto-inc", "not_member",
    "Name-match only: James F. White is director, executive officer and promoter at the company's own "
    "Portland, Maine address on its 2015 Form D; not SHV's James N. White (755 Page Mill Road). No SHV "
    "listing, filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("antipesto-inc")))
L.append(verdict("colucid-pharmaceuticals-inc", "not_member",
    "Name-match only: James F. White files as director and executive officer from CoLucid's Durham, North "
    "Carolina office on its 2010 and 2011 Form Ds, beside directors from Pappas Ventures and two Princeton "
    "firms; not SHV's James N. White. No SHV listing, filing or documented round names CoLucid: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("colucid-pharmaceuticals-inc")))
L.append(verdict("common-sensing-inc", "not_member",
    "Name-match only: James White is a director and executive officer (a founder) filing c/o Common Sensing "
    "in Cambridge, Massachusetts on all nine of its Form Ds from 2013 to 2020; not SHV's James N. White "
    "(755 Page Mill Road). No SHV listing, filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("common-sensing-inc")))
L.append(verdict("forerunner-industries-inc", "not_member",
    "Name-match only: James White is director and executive officer at a Brooklyn apartment address on the "
    "2019 Form D, two years after SHV's Jim White last appears on the firm's roster (2017). No SHV listing, "
    "filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("forerunner-industries-inc")))
L.append(verdict("grande-west-transportation-group-inc", "not_member",
    "Name-match only: James David Alexander White is a director of a bus maker in Aldergrove, British "
    "Columbia, filing from the company's own address (3168 262nd Street) on its 2020 Form D. No SHV listing, "
    "filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("grande-west-transportation-group-inc")))

# Eversight: the one James White seat at the firm's own address, and a documented round.
L.append(verdict("eversight-inc", "member",
    "James White (SHV managing director, on the firm's roster 2001 to 2017) is a director on Eversight's "
    "2016 Form Ds, filing from 755 Page Mill Road, Suite A-200, and Eversight's $14.5M round of April 2016 "
    "was led by Sutter Hill Ventures (the company's release, carried by El Diario NY, 2016-04-28).",
    ec="formd_adjudicated", conf="high", cite=ELDIARIO_EVERSIGHT))
L.append(cls("eversight-inc",
    status="acquired", rng="below_1b",
    stage="Series A", stage_src="formd_structural", stage_cite=SEC("eversight-inc"), stage_conf="medium",
    entry_date="2016-03-31",
    city="Palo Alto", city_src="web_verified", focus="SaaS",
    rounds=[rnd("2013-12-18", "unnamed (Form D, filed as Precipio, Inc.)", 9_686_236, None, None,
                FORMD_CITE("eversight-inc", 0), "filing"),
            rnd("2016-04", "unnamed", 14_500_000, "Sutter Hill Ventures", True, ELDIARIO_EVERSIGHT, "press")],
    note="AI pricing and promotions software for retailers and consumer brands, Palo Alto (the 2016 release). "
         "SHV entered by leading the unnamed $14.5M round of April 2016 (Form D first sale 2016-03-31). The only "
         "earlier filing is a $9.7M round of December 2013 under the name Precipio, Inc., with Emergence "
         "Capital's Brian Jacobs as director. One earlier filing and a round inside the 2015 to 2018 Series A "
         "ceiling read Series A under the structural rule; if the 2013 round was itself the Series A, SHV's "
         "entry would be Growth. Instacart acquired Eversight in September 2022 (Deli Market News, "
         "2022-09-02): acquired."))

# Forterra Systems: There, Inc. under its later name.
L.append(verdict("forterra-systems-inc", "member",
    "Forterra Systems is There, Inc. after its 2004 to 2005 split: the parent, renamed Forterra Systems, "
    "kept government simulation and spun the There MMO off to Makena Technologies (gamedeveloper.com, "
    "2005-04-20; Wikipedia, There (virtual world)). The firm lists There 2008 to 2012 (row there), and James "
    "White, SHV managing director in tenure, is a director on Forterra's 2009 Form D. Medium because that "
    "filing gives the company's San Mateo address rather than SHV's, so the seat is tied to SHV through the "
    "There link.",
    ec="formd_adjudicated", conf="medium", cite=GAMEDEV_FORTERRA))
L.append(cls("forterra-systems-inc",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Mateo", city_src="formd_address", focus="Media, Gaming & Advertising",
    flags=["stage_disputes_band"],
    rounds=[rnd("2009-05-14", "unnamed (Form D)", 1_179_999, None, None, SEC("forterra-systems-inc"), "filing")],
    extra={"entry_stage_source": None, "entry_date": None},
    note="There, Inc. under its later name (same company as the row there): virtual-world simulation and "
         "training software (OLIVE), San Mateo. SHV's position dates from There, Inc. (founded 1998), so the "
         "2009 Form D ($1.18M sold of $2.65M offered) is not SHV's entry and the band's Seed is disputed; SHV's "
         "round in There is not on record, so the stage is undetermined. SAIC bought the OLIVE product line with "
         "all its names, trademarks and licenses in February 2010 (vizworld, 2010): an asset sale of the "
         "business, acquired."))

# --- Stefan Dyckerhoff cluster (SHV managing director since 2012; roster 2012 to 2026).
L.append(verdict("aria-networks-inc", "member",
    "Stefan Dyckerhoff (SHV managing director since 2012) is a director on Aria's 2026 Form D, and every "
    "related person, the officers included, files from SHV's own office at 755 Page Mill Road (the D3 "
    "incubation pattern); the company's $125M first funding round names Sutter Hill Ventures among its "
    "backers, with Dyckerhoff joining the board (Pulse 2.0, 2026-04-11).",
    ec="formd_adjudicated", conf="high", cite=PULSE_ARIA))
L.append(cls("aria-networks-inc",
    status="private", rng="below_1b", stage="undetermined",
    city="Palo Alto", city_src="web_verified", focus="Data Infrastructure",
    flags=["stage_disputes_band"],
    rounds=[rnd("2026-04-06", "first funding round (no series named)", 125_000_000, None, True, PULSE_ARIA, "press")],
    extra={"entry_stage_source": None, "valuation_range_source": "web_verified",
           "valuation_citation": PULSE_ARIA, "valuation_asof": "2026-09-28"},
    note="AI-native networking for data centers; 'a Palo Alto, CA-based networking company' (FinSMEs headline). "
         "An SHV incubation under D3: the company and its officers file from SHV's office. Its $125M raise "
         "(Form D: $73.0M sold of $100.0M offered, first sale 2026-04-06) is reported only as the company's "
         "first funding round, backed by Sutter Hill Ventures, Atreides, Valor and Eclipse, with no series "
         "named (Pulse 2.0; The AI Insider). Under D3 an incubation's unnamed first round reads undetermined, "
         "and the band's Growth (Series B and later) is disputed because a first round cannot be one. Momentum "
         "check 2026-09-28: no valuation disclosed and no later priced round found; below_1b."))

L.append(verdict("celero-communications-inc", "member",
    "Stefan Dyckerhoff (SHV managing director since 2012) is a director on all three of Celero's Form Ds "
    "(2024 to 2025), and the press names Sutter Hill Ventures as lead of Celero's seed and Series A "
    "(SiliconANGLE, 2025-11-17; Pulse 2.0, 2025-11-18).",
    ec="formd_adjudicated", conf="high", cite=SA_CELERO))
L.append(cls("celero-communications-inc",
    status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=PULSE_CELERO, stage_conf="high",
    entry_date="2024-03-18",
    grad="graduated", grad_src="web_verified", grad_cite=PULSE_CELERO, grad_conf="high",
    city="Irvine", city_src="web_verified", focus="Industrial & Robotics",
    flags=["stage_disputes_band"],
    rounds=[rnd("2024-03-18", "Seed", None, "Sutter Hill Ventures", True, PULSE_CELERO, "press"),
            rnd("2024-12-11", "Series A", None, "Sutter Hill Ventures", True, PULSE_CELERO, "press"),
            rnd("2025-11-17", "Series B", 100_000_000, "CapitalG", None, SA_CELERO, "press")],
    extra={"valuation_range_source": "web_verified", "valuation_citation": SA_CELERO,
           "valuation_asof": "2026-09-28"},
    note="Coherent DSP chips for optical links in AI data centers, Irvine (Pulse 2.0). Sutter Hill Ventures led "
         "the company's 'earlier seed and Series A investments totaling $40 million' (Pulse 2.0) and Dyckerhoff "
         "is on the first Form D ($8.4M, first sale 2024-03-18), so SHV's entry is the seed; the band's Series A "
         "is disputed. The Series A (Form D: $30.0M, first sale 2024-12-11) graduates the seed, and CapitalG "
         "then led a $100M Series B (Form D 2025-10-24; SiliconANGLE). Momentum check 2026-09-28: no valuation "
         "disclosed; below_1b."))

L.append(verdict("cspeed-inc", "member",
    "Director-of-record pattern (D3; COLLECTION.md s1): Stefan Dyckerhoff (SHV managing director since 2012) "
    "is a director on Cspeed's 2023 and 2024 Form Ds, and the company itself gives SHV's office, 755 Page "
    "Mill Road, Suite A-200, as its business address, with its CEO Sanjai Kohli filing from there. The "
    "issuer resolves to a real company: a Palo Alto datacenter-connectivity (silicon photonics) startup "
    "founded in 2022 that sold $15.0M in 2023 and $28.3M in 2024 (Form Ds; its own site, cspeed.io). No "
    "announcement names SHV's round, hence medium.",
    ec="formd_adjudicated", conf="medium", cite=SEC("cspeed-inc", "formd", 1)))
L.append(cls("cspeed-inc",
    status="private", rng="below_1b",
    city="Palo Alto", city_src="formd_address", focus="Industrial & Robotics",
    rounds=[rnd("2023-04-12", "unnamed (Form D)", 15_000_000, None, None, FORMD_CITE("cspeed-inc", 1), "filing"),
            rnd("2024-11-18", "unnamed (Form D)", 28_349_982, None, None, FORMD_CITE("cspeed-inc", 0), "filing")],
    note="Silicon photonics and laser arrays for AI datacenter connectivity, Palo Alto, founded 2022, CEO "
         "Sanjai Kohli (SiRF co-founder); housed at SHV's office. Raised $15.0M (first sale 2023-04-12, 24 "
         "investors) and $28.3M (2024-11-18, 32 investors, when Atreides's Gavin Baker joined the board) on Form "
         "Ds. No announcement names either round, so the band's Series A stands. Momentum check 2026-09-28: no "
         "priced valuation found (only vendor profiles, which report about $43M raised); below_1b."))

L.append(verdict("enfabrica-corp", "member",
    "Stefan Dyckerhoff (SHV) is a director on Enfabrica's 2023 Form D and has sat on its board since May "
    "2020 (Astera Labs S-1, 2024); Enfabrica 'has raised $50 million in early stage venture funding from "
    "Sutter Hill Ventures' (The Next Platform, 2023-03-28), and SHV returned as an existing investor in the "
    "2023 Series B (SiliconANGLE).",
    ec="formd_adjudicated", conf="high", cite=NEXTPLATFORM_ENF))
L.append(cls("enfabrica-corp",
    status="private", rng="below_1b",
    stage="Series A", stage_src="model", stage_cite=NEXTPLATFORM_ENF, stage_conf="medium",
    entry_date="2020-05",
    city="Mountain View", city_src="web_verified", focus="Industrial & Robotics",
    flags=["stage_disputes_band"],
    rounds=[rnd("2020-05", "Series A", None, "Sutter Hill Ventures", True, NEXTPLATFORM_ENF, "press"),
            rnd("2023-09-12", "Series B", 125_000_000, "Atreides Management", True, SA_ENF_B, "press"),
            rnd("2024-11-19", "Series C", 115_000_000, "Spark Capital", True, CBN_ENF_C, "press")],
    extra={"valuation_range_source": "web_verified", "valuation_citation": CBN_ENF_C,
           "valuation_asof": "2026-09-28"},
    note="AI networking silicon (SuperNIC, elastic memory fabric), Mountain View (Crunchbase News). SHV entered "
         "well before the 2023 Series B that the band reads as its entry (disputed): Dyckerhoff has been a "
         "director since May 2020 (Astera Labs S-1), the early funding, $50M, came from Sutter Hill Ventures "
         "(The Next Platform), and TechCrunch calls the round before the B its Series A. SHV then joined the "
         "$125M Series B led by Atreides (2023) and the $115M Series C led by Spark (2024). In September 2025 "
         "Nvidia paid about $900M in cash and stock to hire the CEO and key staff and license the technology "
         "(StorageNewsletter), without buying the company, whose site still offers its products: private under "
         "the acqui-hire rule, as the Spark sibling reads it. No priced round at $1B or more is on record; "
         "below_1b."))

# --- Mike Speiser cluster (SHV managing director; roster 2008 to 2026).
L.append(verdict("augment-computing-inc", "member",
    "Mike Speiser (director and executive officer) and Palmer Rampell (director), both SHV managing "
    "directors, are on Augment's 2023 and 2024 Form Ds, filing from 755 Page Mill Road, and decisions.md D3 "
    "names Augment Computing (2022) as an SHV incubation; the company's own announcement says its $25M "
    "Series A was led by Sutter Hill Ventures (Augment Code blog, April 2024).",
    ec="formd_adjudicated", conf="high", cite=AUGMENT_BLOG))
L.append(cls("augment-computing-inc",
    status="private", rng="below_1b", usd=977_000_000, val_src="web_verified", val_cite=AUGMENT_BLOG,
    asof="2024-04",
    city="Palo Alto", city_src="web_verified", focus="DevTools & APIs",
    flags=["stale"],
    rounds=[rnd("2023-09-28", "Series A", 25_000_000, "Sutter Hill Ventures", True, AUGMENT_BLOG, "company"),
            rnd("2024-04", "Series B", 227_000_000, None, True, AUGMENT_BLOG, "company")],
    note="AI coding assistant for software teams (Augment Code), Palo Alto, founded 2022; an SHV incubation "
         "(D3). Its $25M Series A was led by Sutter Hill Ventures and its $227M Series B (April 2024, with SHV, "
         "Index, Innovation Endeavors, Lightspeed and Meritech) priced it at $977M post-money (company blog), "
         "which agrees with the band's Series A entry (first sale 2023-09-28). The $977M mark sits within 5% of "
         "the $1B edge and is older than 24 months (stale). Momentum check 2026-09-28: no later priced round "
         "found in Google News; below_1b."))

L.append(verdict("clumio-inc", "member",
    "Mike Speiser (SHV managing director) is a director on Clumio's 2017 Form D, filing from 755 Page Mill "
    "Road, and Clumio's October 2017 $11M Series A was 'led by founding investor Mike Speiser, Managing "
    "Director at Sutter Hill Ventures' (AWS Startups blog, 2021); SHV also led its 2024 Series D.",
    ec="formd_adjudicated", conf="high", cite=AWS_CLUMIO))
L.append(cls("clumio-inc",
    status="acquired", rng="below_1b",
    city="Santa Clara", city_src="web_verified", focus="Data Infrastructure",
    rounds=[rnd("2017-10", "Series A", 11_000_000, "Sutter Hill Ventures", True, AWS_CLUMIO, "press"),
            rnd("2024-02-21", "Series D", 75_000_000, "Sutter Hill Ventures", True, GNW_CLUMIO, "company")],
    note="Backup and recovery as a service for cloud data, Santa Clara (the 2024 release). SHV was the founding "
         "investor and led the October 2017 $11M Series A (AWS Startups blog), which agrees with the band's "
         "Series A (first sale 2017-11-17); SHV also led the $75M Series D of February 2024 ($261M raised in "
         "total). Commvault bought Clumio in October 2024 in a reported $47M deal (SC Media, 2024-10-01): "
         "acquired."))

L.append(verdict("freestyle-software-inc", "member",
    "Director-of-record pattern (D3 incubation): Mike Speiser (SHV managing director) is the executive "
    "officer on Freestyle Software's only Form D (2015), and the company's business address and telephone are "
    "SHV's own (755 Page Mill Road, A-200; 650-493-5600), with all three directors filing there. The issuer "
    "resolves to a real Palo Alto software startup incorporated in 2015 that sold $4.975M to 31 investors "
    "(Form D); its designer Andrei Herasimchuk lists Freestyle Software, Inc. as his company on GitHub. No "
    "announcement or later filing names it, hence medium.",
    ec="formd_adjudicated", conf="medium", cite=SEC("freestyle-software-inc")))
L.append(cls("freestyle-software-inc",
    status="unknown", rng="below_1b",
    city="Palo Alto", city_src="formd_address", focus="SaaS",
    rounds=[rnd("2015-04-28", "unnamed (Form D)", 4_975_000, None, None, SEC("freestyle-software-inc"), "filing")],
    note="A 2015 SHV incubation housed at the firm's office with Mike Speiser as executive officer; its product "
         "is not on record (a vendor profile files it under social and platform software, hence SaaS). One "
         "Form D ($4.975M from 31 investors, first sale 2015-04-28) and nothing after; its domain "
         "freestyle.software no longer resolves, and no source found gives its fate: status unknown. No round is "
         "named, so the band's Seed stands. Graduation left for the graduation pass."))

L.append(verdict("ghost-autonomy-inc", "member",
    "Mike Speiser (SHV managing director) is a director on Ghost's 2018 Form D, filing from SHV's office, and "
    "TechCrunch lists Sutter Hill Ventures (Mike Speiser) among Ghost Autonomy's major investors "
    "(2024-04-03).",
    ec="formd_adjudicated", conf="high", cite=TC_GHOST))
L.append(cls("ghost-autonomy-inc",
    status="defunct", rng="below_1b",
    city="Mountain View", city_src="web_verified", focus="Industrial & Robotics",
    rounds=[rnd("2018-07-31", "unnamed (Form D)", 14_999_998, None, None,
                FORMD_CITE("ghost-autonomy-inc", 3), "filing"),
            rnd("2019", "first funding (as announced)", 63_700_000, None, None, TC_GHOST, "press"),
            rnd("2021", "Series D", 100_000_000, None, None, TC_GHOST, "press"),
            rnd("2023", "down round", 55_000_000, None, None, TC_GHOST, "press")],
    note="Autonomous-driving software for consumer cars (Ghost Locomotion, later Ghost Autonomy), Mountain View, "
         "co-founded by Pure Storage's John Hayes. It 'ended worldwide operations and wound down the company' "
         "on 2024-04-03 after raising nearly $220M (TechCrunch): defunct. TechCrunch gives $63.7M first "
         "announced in 2019, a $100M Series D in 2021 and a $55M down round in 2023; SHV's 2018 entry (Form D, "
         "$15.0M sold, first sale 2018-07-31) keeps the band's Series A."))

# --- Greg Sands (SHV to 2012, then Costanoa at 160 Forest Avenue).
L.append(verdict("cogine-inc", "member",
    "Cogine, Inc. is Connection Engine, Inc. under its first name: EDGAR CIK 1495532 filed the 2010 Form D as "
    "Cogine and the 2011 Form D as Connection Engine with Cogine as its previous name, both with Greg Sands "
    "(SHV, in tenure) as director. The firm lists Connection Engine 2010 to 2016 (row connection-engine), so "
    "this row is a duplicate of a listed member, not a separate company.",
    ec="site_listing", conf="high", cite=ARCH("connection-engine")))
L.append(cls("cogine-inc",
    status="unknown", rng="below_1b",
    stage="Seed", stage_src="formd_structural", stage_cite=SEC("cogine-inc"), stage_conf="medium",
    entry_date="2010-06-25",
    city="Boulder", city_src="formd_address", focus="SaaS",
    rounds=[rnd("2010-06-25", "unnamed (Form D, as Cogine, Inc.)", 1_049_999, None, None, SEC("cogine-inc"), "filing"),
            rnd("2011-06-24", "unnamed (Form D, as Connection Engine, Inc.)", 1_049_997, None, None,
                SEC("connection-engine"), "filing")],
    note="Connection Engine (first filed as Cogine, Inc.), Boulder, Colorado: cloud software that analyses "
         "consumer data for digital marketing (the firm's 2010 page). Its first Form D (first sale 2010-06-25, "
         "$1.05M from 23 investors, incorporated 2010) carries Greg Sands of SHV as director: the "
         "partner-anchored first round, a Seed under the 2010 ceiling of $1.5M; the 2011 Form D ($1.05M) is its "
         "second. No source found gives its fate after 2011 (Google News and EDGAR searched), though the firm "
         "listed it through 2016: status unknown. Same company as the row connection-engine. Graduation left "
         "for the graduation pass."))
L.append(verdict("directly-inc", "not_member",
    "Greg Sands's 2015 seat is Costanoa's, not SHV's (D5 seat dating): he left SHV to run Costanoa Venture "
    "Capital from 2012 (his 2013 to 2015 filings give Costanoa's 160 Forest Avenue), and both of Directly's "
    "2015 Form Ds list him at the company's San Francisco address. No SHV listing, filing or documented round "
    "names Directly.",
    ec="formd_adjudicated", conf="high", cite=SEC("directly-inc")))

# --- Ron Bernal (SHV pages to 2009; NEA from 2010).
L.append(verdict("boulder-wind-power-inc", "not_member",
    "Ron Bernal's seat is NEA's, not SHV's (D5 seat dating): the three Form Ds were filed in September 2011, "
    "after his move to NEA in 2010, and they list NEA partners Harry Weller and Ravi Viswanathan beside him "
    "(the first offering, as Core Wind Power, began 2009-11-30 with three investors). No SHV listing, filing "
    "or documented round names the company (EDGAR full text and Google News searched).",
    ec="formd_adjudicated", conf="high", cite=SEC("boulder-wind-power-inc")))

# --- Andrew Sheehan (SHV partner 2007 to 2021; managing member of Tippet Venture Partners from 2014).
L.append(verdict("creditly-corp", "not_member",
    "Andy Sheehan's seat is his own firm's, not SHV's (D5 seat dating): he has run Tippet Venture Partners "
    "since 2014 beside his SHV partnership (Yext proxy, 2020), and Creditly, now Credit Genie, quotes 'Andy "
    "Sheehan of Tippet Ventures' on its 2023 Series A, led by Tippet Ventures and Khosla Ventures (PR "
    "Newswire, 2023-05-31). No SHV listing, filing or documented round names the company.",
    ec="formd_adjudicated", conf="high", cite=PRN_CREDIT_GENIE))
L.append(verdict("finicity-corp", "not_member",
    "Name-match only: the Andrew Sheehan on Finicity's 2018 Form D files from the company's Salt Lake City "
    "address, and an Andy Sheehan later served as Finicity's President and COO (Finovate, 2022). SHV's Andrew "
    "T. Sheehan also ran Tippet Venture Partners from 2014. No SHV listing, filing or documented round names "
    "Finicity (EDGAR full text and Google News searched).",
    ec="formd_adjudicated", conf="high", cite=FINOVATE_FINICITY))

# --- Keith Loebner (SHV, on the adviser's Schedule A 2022 to 2026).
L.append(verdict("atommap-corp", "member",
    "Keith Loebner (SHV managing director; on the adviser's Schedule A since 2022) is a director on Atommap's "
    "2026 Form D, and Sutter Hill Ventures, 'led by Keith Loebner (Managing Director)', led the company's $47M "
    "Series A as Fathom Therapeutics, formerly Atommap (PR Newswire, 2026-04-27).",
    ec="formd_adjudicated", conf="high", cite=PRN_FATHOM))
L.append(cls("atommap-corp",
    status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=PRN_FATHOM, stage_conf="high",
    entry_date="2026-03-06",
    city="New York", city_src="web_verified", focus="Healthcare & Bio",
    flags=["stage_disputes_band"],
    rounds=[rnd("2023-11-13", "unnamed (Form D)", 7_084_989, None, None, FORMD_CITE("atommap-corp", 0), "filing"),
            rnd("2026-03-06", "Series A", 47_000_000, "Sutter Hill Ventures", True, PRN_FATHOM, "company")],
    extra={"valuation_range_source": "web_verified", "valuation_citation": PRN_FATHOM,
           "valuation_asof": "2026-09-28"},
    note="Physics- and AI-based small-molecule drug design, New York with a Boston office; renamed Fathom "
         "Therapeutics in April 2026. SHV's entry is the Series A it led: the 2026 Form D itself describes the "
         "offering as Series A and Series A-1 preferred ($31.1M sold of $59.6M, first sale 2026-03-06), and the "
         "company announced a $47M Series A led by Sutter Hill Ventures (PR Newswire); the band's Growth is "
         "disputed. The 2023 round ($7.1M, 31 investors) lists only the founder, so no earlier SHV entry is on "
         "record. Momentum check 2026-09-28: no valuation disclosed; below_1b."))

# --- Jeffrey Bird (SHV's is Jeffrey W. Bird).
L.append(verdict("frank-s-international-n-v", "not_member",
    "Name-match only: Jeffrey J. Bird on the 2016 Form D is an executive officer of Frank's International, the "
    "Houston oilfield-services company, filing from its Houston office; SHV's managing director is Jeffrey W. "
    "Bird of 755 Page Mill Road. No SHV listing, filing or documented round names the company: a homonym.",
    ec="formd_adjudicated", conf="high", cite=SEC("frank-s-international-n-v")))

# =====================================================================
# B. Seeded rows disputed on membership
# =====================================================================
L.append(verdict("venture-tdf-china-llc", "not_member",
    "decisions.md D6 (T5, the LP-stake class): the firm's 2008 and 2012 to 2016 pages file Venture TDF China "
    "LLC under its own 'Investment Partnerships' category, and the 2008 page describes a manager formed in "
    "2000 'to manage China specific funds for Venture TDF' that raised its first fund, Venture TDF China LP, "
    "the same year. SHV's position is an interest in a fund, not equity in an operating company.",
    ec="site_listing", conf="high", cite=ARCH("venture-tdf-china-llc")))
L.append(verdict("aruba-networks-inc", "not_member",
    "decisions.md D4 (T3, a post-IPO public purchase): SHV's first ownership filing on Aruba is a Schedule 13G "
    "under Rule 13d-1(c) with an event date of 2008-04-08 (3,648,754 shares, 4.5%), thirteen months after the "
    "March 2007 IPO; the IPO prospectus (424B4, 2007-03-27) never names Sutter Hill, and the stake grew to "
    "4,898,258 shares by the February 2009 13G/A (Aruba's 2009 proxy), the pattern of market purchases. No "
    "pre-IPO round naming SHV is documented, so the fund filing records a crossover holding, not a venture "
    "entry.",
    ec="fund_filing", conf="high", cite=SEC("aruba-networks-inc", "edgar")))

# =====================================================================
# C. Listed members: classification only
# =====================================================================
L.append(cls("telesensory-systems",
    status="defunct", rng="below_1b", stage="undetermined",
    city="Mountain View", focus="Healthcare & Bio", rounds=[],
    note="Reading machines for the blind (the Optacon), founded 1970 in Palo Alto (Wikipedia, Telesensory "
         "Systems). TeleSensory, the former TSI, declared Chapter 7 bankruptcy in March 2005 and closed (same "
         "article): defunct. The firm's 1999 table: 'Private company'. City is its long-time Mountain View base "
         "(model knowledge); the 2005 address is unconfirmed. SHV's entry round predates EDGAR and no source "
         "names it: stage undetermined."))
L.append(cls("tellabs",
    rng="below_1b", stage="undetermined",
    city="Naperville", focus="Data Infrastructure", rounds=[],
    note="Telecom transport and access equipment. Public from 1980 (the firm's 1999 table: 'Public company'); "
         "acquired by Marlin Equity Partners in 2013 (Wikipedia, Tellabs). City is Naperville, its headquarters "
         "when acquired, matching the Greylock sibling; Wikipedia now places the successor in Carrollton, "
         "Texas. SHV's entry round predates EDGAR and no source names it: stage undetermined."))
L.append(cls("tesseract",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", focus="SaaS", rounds=[],
    note="Health benefits and human resources software. The firm's 1999 table: 'Acquired by Prudential Ins.' "
         "(its own outcome line, D8): acquired. City from model knowledge. The Accel row (an unidentified 2023 "
         "listing) and the Y Combinator row (Livermore hardware, S2017) named Tesseract are different companies "
         "with the same name and are not aligned. SHV's round is not on record: stage undetermined."))
L.append(cls("there",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Mateo", city_src="formd_address", focus="Media, Gaming & Advertising", rounds=[],
    note="There, Inc. (founded 1998) built the There.com virtual world. After 2004 layoffs it split: the parent, "
         "renamed Forterra Systems, kept government simulation and in April 2005 spun the There MMO off to "
         "Makena Technologies (gamedeveloper.com, 2005; Wikipedia, There (virtual world)). SAIC bought "
         "Forterra's OLIVE product line with its names, trademarks and licenses in February 2010 (vizworld), an "
         "asset sale of the business: acquired. City is Forterra's San Mateo address on its 2009 Form D. The row "
         "forterra-systems-inc is the same company under its later name. SHV's round is not on record: stage "
         "undetermined."))
L.append(cls("tollbridge-technologies",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Santa Clara", city_src="web_verified", focus="Data Infrastructure", rounds=[],
    note="Voice over DSL and broadband gateways, Santa Clara (Multichannel News, 2002-06-24). It locked its doors "
         "on 2002-06-14 after a failed funding round (same article), and Crunchbase records NewCross "
         "Technologies acquiring its assets and customers later in 2002: an asset sale out of the wind-down, "
         "acquired (the buyer rests on a vendor record, so a later pass may re-read it as defunct). The firm's "
         "1999 table: 'Private company'. SHV's round is not on record: stage undetermined."))
L.append(cls("tomfoolery",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", focus="SaaS", rounds=[],
    note="Workplace social apps (Anchor) from ex-Yahoo and AOL founders; the firm lists it 2013 to 2016 with Sam "
         "Pullara as managing director. Yahoo closed its acquisition in January 2014, as both siblings (a16z, "
         "Battery) read it from TechCrunch: acquired, San Francisco, aligned. The siblings entered at the $1.7M "
         "seed of January 2013 led by Andreessen Horowitz; no source found names SHV in that or any round, so "
         "SHV's stage is undetermined."))
L.append(cls("trade",
    status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    flags=["identity_unresolved"],
    note="The firm's 1999 table lists only 'Trade | Import data | Private company'. No filing, press item, "
         "Wikipedia article or web search ties an import-data company named Trade to SHV, so the company cannot "
         "be named: identity_unresolved, and stage, band and S2A read undetermined. The prefilled GB country is "
         "a Wikidata join on the one-word name and is unverified. The Y Combinator row named Trade (Broken "
         "Arrow, W2017) is a different company."))
L.append(cls("transglobal-systems",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", flags=["city_unknown"], focus="Fintech & Payments", rounds=[],
    note="Transaction processing. The firm's 1999 table: 'Acquired by First USA Merch.' (First USA Merchant "
         "Services): acquired. No filing or press item found places the company or names SHV's round (EDGAR "
         "full text starts in 2001, Google News has nothing): city unknown, stage undetermined."))
L.append(cls("valista",
    status="acquired", rng="below_1b", stage="undetermined",
    country="IE", country_src="web_verified", country_cite=SILICONREPUBLIC_VALISTA,
    city="Dublin", city_src="web_verified", focus="Fintech & Payments", rounds=[],
    note="Payments and settlement software for telecom operators, formed when Network365 and the US company "
         "iPIN combined (Irish Times, 2009-07-07). Belfast's Aepona acquired it in an all-share deal in "
         "July 2009 (Irish Times; Silicon Republic: 'Belfast's Aepona acquires Dublin's Valista'): acquired, "
         "Dublin. SHV's round is not on record: stage undetermined."))
L.append(cls("vical",
    country="US", city="San Diego", rng="below_1b", stage="undetermined",
    focus="Healthcare & Bio", rounds=[],
    note="Gene-based drugs and vaccines, 10390 Pacific Center Court, San Diego (its merger release, EDGAR). Public "
         "from 1993 (the firm's 1999 table: 'Public company'); in 2019 it merged with Brickell Biotech in an "
         "all-stock deal that gave Brickell's holders 60% and the Brickell name (Vical DEFA14A, 2019-06-03), "
         "consistent with the prefilled acquired. SHV's round predates EDGAR and is not on record: stage "
         "undetermined."))
L.append(cls("visionary-design-systems",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Santa Clara", focus="SaaS", rounds=[],
    note="e-engineering (CAD) software, the maker of IronCAD. Status aligned with the Benchmark sibling "
         "(acquired by Rand Technologies in 2000). The line continued as Alventive: Alventive's founder and CEO "
         "was also CEO of Visionary Design Systems and IronCAD (Celestica 20-F, 2006), and the firm's 2004 page "
         "lists Alventive, which batch 3 judged defunct with Benchmark's own Alventive row. The two rows "
         "(visionary-design-systems, alventive) look like one company with conflicting fates; flagged for the "
         "lead. SHV's round is not on record: stage undetermined."))
L.append(cls("vivace-networks",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Jose", focus="Data Infrastructure", rounds=[],
    note="Broadband multiservice (MPLS) switching. Tellabs acquired it in 2003 (the Redpoint sibling, about "
         "$135M): acquired, San Jose, aligned with Redpoint. The firm's 1999 table: 'Private company'; its "
         "2010 to 2016 pages kept listing it. SHV's round is not on record: stage undetermined."))
L.append(cls("volo-media",
    status="unknown", rng="below_1b", stage="undetermined",
    country="US", flags=["city_unknown"], focus="Media, Gaming & Advertising", rounds=[],
    note="Podcast audience measurement and ad network (the firm's 2008 page), formerly Podbridge, renamed Volo "
         "Media in November 2007 (Business Wire headline); The Register reported a US podcast patent granted to "
         "it in July 2009. No source found gives its later fate or its headquarters (Google News, EDGAR full "
         "text and web search): status unknown, city unknown. Country US from model knowledge. SHV's round is "
         "not on record: stage undetermined."))
L.append(cls("wavefront",
    status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=CMSWIRE_WAVEFRONT, stage_conf="high",
    entry_date="2014",
    country="US", city="Palo Alto", city_src="web_verified", focus="Data Infrastructure",
    rounds=[rnd("2014", "Series A", 13_500_000, "Sutter Hill Ventures and Sequoia Capital", True,
                CMSWIRE_WAVEFRONT, "press"),
            rnd("2016-10-25", "Series B", 52_000_000, None, True, TANZU_WAVEFRONT_B, "company")],
    note="Metrics monitoring for cloud applications, Palo Alto (the 2016 release's dateline). Wavefront closed a "
         "$13.5M Series A in 2014 while in stealth, led by Sutter Hill Ventures and Sequoia Capital (CMSWire, "
         "2016): SHV's entry. Both returned in the $52M Series B of October 2016 with new investor Tenaya "
         "Capital (company release). VMware announced its acquisition on 2017-04-12 (SiliconANGLE): acquired, "
         "aligned with the Sequoia sibling."))
L.append(cls("wildcard-systems",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Sunrise", city_src="web_verified", focus="Fintech & Payments", rounds=[],
    note="Prepaid and stored-value card processing, founded 1997 and headquartered in Sunrise, Florida. eFunds "
         "agreed on 2005-06-09 to buy it for $228.8M upfront plus up to $58.8M earn-out, closing expected in "
         "July 2005 (eFunds 8-K, exhibit 99.1; an 8-K/A followed in September 2005); the release names Sutter Hill Ventures as WildCard's financial advisor. "
         "Acquired. SHV's round is not on record: stage undetermined."))
L.append(cls("xcellenet",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Atlanta", focus="SaaS", rounds=[],
    note="Wide-area application and remote systems management software, Atlanta. The firm's 1999 table: "
         "'Acquired by Sterling Commerce' (1998): acquired, aligned with the Greylock sibling (IPO 1994, "
         "Sterling Commerce 1998). SHV's round is not on record: stage undetermined."))
L.append(cls("yaolan-babycare",
    status="acquired", rng="below_1b", stage="undetermined",
    country="CN", country_src="web_verified", country_cite=USANA_S3,
    city="Beijing", city_src="web_verified", focus="Consumer & Marketplaces", rounds=[],
    note="Nutritional products for mothers and infants, sold by direct selling; BabyCare was founded in 1999 and "
         "is headquartered in Beijing (USANA S-3, 2010-10-14). USANA bought BabyCare Holdings from Yaolan, Ltd. "
         "on 2010-08-16 for USANA shares, which Yaolan distributed to its holders, the SHV partnership among "
         "them (same S-3): acquired; those USANA shares are sale consideration, not a new position. SHV's round "
         "is not on record: stage undetermined."))
L.append(cls("zilo",
    status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="New York", city_src="web_verified", focus="Media, Gaming & Advertising", rounds=[],
    note="Entertainment and marketing network for college students (the campus cable channel Zilo TV), New York, "
         "founded 1999. Its founder sold Zilo to Sirk Productions in 2008 and Zilo TV passed to SirkTV in spring "
         "2009 (Wikipedia, Zilo and David Isaacs): acquired. SHV's round is not on record: stage undetermined."))


# ---- house style guard: no em-dashes, no retired words, in any basis or note
def _check(lines):
    bad = []
    for x in lines:
        for k in ("basis", "note"):
            t = x.get(k) or ""
            if "—" in t or re.search(r"(?i)\bprior\b|\binvariant\b|\bC2A\b", t):
                bad.append((x["slug"], k))
    if bad:
        raise SystemExit(f"style check failed: {bad}")


if __name__ == "__main__":
    _check(L)
    jl.write(f"batch-{N:03d}", L)
