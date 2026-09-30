"""PRO-100 NEA, judge c8, queue batch 15 (opendoor .. plato): listed members, classification only."""
import judge_lib as jl
from judge_lib import cls, rnd, SITE, POST, W, FTS, NEWS

WV = {"valuation_range_source": "web_verified"}
CHECKED = "2026-09-30"


def cap(tk):
    return f"https://stockanalysis.com/stocks/{tk}/market-cap/"


def momentum(url):
    """A below_1b row whose momentum check ran: the check is recorded with its citation and date."""
    return {"valuation_range_source": "web_verified", "valuation_citation": url, "valuation_asof": CHECKED}


L = []

# ---- opendoor
L.append(cls("opendoor", status="public", rng="1b_plus", usd=2320000000, val_src="web_verified", val_cite=cap("open"),
             asof="2026-09-30", stage="Growth", stage_src="first_party", stage_cite=SITE("opendoor"), stage_conf="medium",
             entry_date="2016", city="Tempe", focus="Consumer & Marketplaces", extra=WV,
             note="Listed on Nasdaq (OPEN) through the December 2020 merger with Social Capital Hedosophia II; market cap "
                  "$2.32B on 2026-09-30 (stockanalysis), fresher than the GV row's $2.36B of 2026-09-28. The firm labels its "
                  "2016 entry Growth. Principal office Tempe, as in the GV, Thrive, Felicis and Khosla rows (a16z and Coatue "
                  "carry San Francisco)."))

# ---- opower (dispute: the known Growth reads the $50M 2010 Form D; the firm's own post says NEA led the first round)
OPW = POST("opower-ipo")
OPW_GV = "https://globalventuring.com/ge-backed-opower-raises-50m/"
L.append(cls("opower", rng="below_1b", city="Arlington", stage="Series A", stage_src="first_party", stage_cite=OPW,
             stage_conf="medium", entry_date="2008", focus="SaaS", flags=["stage_disputes_band"],
             rounds=[rnd("2008", "Series A", None, lead="MHS Capital (Global Venturing); NEA per the firm's post",
                         firm_in_round=True, source=OPW_GV, source_type="press"),
                     rnd("2010-11-24", "Unnamed (Form D)", 50000022, lead=None, firm_in_round=True,
                         source=jl.FORMD_CITE("opower"), source_type="filing")],
             note="Dispute: the known Growth read the $50M Form D of November 2010, a later round. The firm's own post "
                  "(2014-04-03) says NEA led Opower's first round of institutional venture capital; Global Venturing calls "
                  "that round the A round of early 2008 (crediting MHS Capital's Mark Sugarman with the lead), and the firm "
                  "dates its entry 2008. Arlington, Virginia (Wikipedia); acquired by Oracle in 2016 for $532M."))

# ---- opsclarity
L.append(cls("opsclarity", status="acquired", rng="below_1b", city="Sunnyvale", city_src="formd_address",
             focus="Data Infrastructure",
             note="IT operations analytics startup acquired by Lightbend in 2016; the firm's archived listing carries the "
                  "exit (by Lightbend). Sunnyvale from the company's own 2014 Form D."))

# ---- orbis-medicines
ORBIS = NEWS("orbis-medicines", "secures €90m")
L.append(cls("orbis-medicines", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
             stage_cite=ORBIS, stage_conf="high", entry_date="2025-01-06", country="DK", country_src="web_verified",
             country_cite=ORBIS, city="Copenhagen", focus="Healthcare & Bio",
             rounds=[rnd("2024-02-29", "Seed", None, lead="Novo Holdings", firm_in_round=False,
                         source=NEWS("orbis-medicines", "Launches with €26 Million Seed"), source_type="press"),
                     rnd("2025-01-06", "Series A", 93000000, lead="NEA", firm_in_round=True, source=ORBIS,
                         source_type="press")],
             note="Danish oral macrocycle biotech. NEA led the EUR 90M (about $93M) Series A of January 2025 (European "
                  "Biotechnology; BioPharma Dive), its entry, after a EUR 26M seed from Novo Holdings in 2024. The Novo "
                  "Nordisk licensing deal of 2026-09 (up to $1.4B) is milestones, not a valuation."))

# ---- orby-ai
ORBY_SEED = NEWS("orby-ai", "Emerges from Stealth")
ORBY_A = NEWS("orby-ai", "take business process automation")
L.append(cls("orby-ai", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_cite=ORBY_SEED,
             stage_conf="high", entry_date="2022", grad="graduated", grad_src="web_verified", grad_cite=ORBY_A,
             grad_conf="high", grad_asof=CHECKED, country="US", city="Sunnyvale", city_src="web_verified",
             focus="AI & Applied AI",
             rounds=[rnd("2023-05-10", "Seed", 4500000, lead="Pear VC; NEA", firm_in_round=True, source=ORBY_SEED,
                         source_type="company"),
                     rnd("2024-06-27", "Series A", 30000000, lead="NEA; Wing VC; WndrCo", firm_in_round=True,
                         source=ORBY_A, source_type="press")],
             note="Pear VC and NEA led the $4.5M seed (announced 2023-05-10, Sunnyvale dateline; the firm dates its entry "
                  "2022 and labels it Seed); NEA, Wing VC and WndrCo led the $30M Series A of June 2024 (SiliconANGLE). "
                  "Acquired by Uniphore, announced 2025-08-28 (Business Wire)."))

# ---- orexigen-therapeutics (X1 candidate)
L.append(cls("orexigen-therapeutics", rng="below_1b", stage="Growth", stage_src="model", stage_conf="medium",
             entry_date="2010-12", city="San Diego", focus="Healthcare & Bio",
             note="Obesity drug developer based in La Jolla (San Diego); Chapter 11 in 2018 and sold to Nalpropion "
                  "(Wikipedia). NEA's first filing is a Schedule 13G of 2010-12-21, three years after the April 2007 IPO, "
                  "and the firm labels the position Public/PIPES: a listed purchase, so any entry reads Growth. X1 "
                  "candidate: no NEA private round before the listing is on record."))

# ---- oric (X1 candidate)
L.append(cls("oric", status="public", rng="1b_plus", usd=1430000000, val_src="web_verified", val_cite=cap("oric"),
             asof="2026-09-30", stage="Growth", stage_src="web_verified", stage_cite=FTS("Oric", "8-K"),
             stage_conf="high", entry_date="2024-01-22", country="US", city="South San Francisco",
             focus="Healthcare & Bio", extra=WV,
             rounds=[rnd("2024-01-22", "PIPE", 125000000, lead=None, firm_in_round=True, source=FTS("Oric", "8-K"),
                         source_type="filing")],
             note="ORIC Pharmaceuticals (Nasdaq: ORIC, listed April 2020); market cap $1.43B on 2026-09-30 "
                  "(stockanalysis). NEA's entry is the $125M private placement of January 2024, bought through Growth "
                  "Equity Opportunities 18 VGE (the 8-K names NEA). X1 candidate: a PIPE into a listed company with no "
                  "earlier NEA private round on record."))

# ---- origin-medsystems
L.append(cls("origin-medsystems", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991",
             country="US", city="Menlo Park", focus="Healthcare & Bio",
             note="Endosurgery device maker acquired by Eli Lilly (the firm's exit line), later part of Guidant. The "
                  "record does not name NEA's 1991 round."))

# ---- orphomed
L.append(cls("orphomed", status="defunct", rng="below_1b", city="Mill Valley", city_src="formd_address",
             focus="Healthcare & Bio",
             note="Dimer-conjugate biotech (GI and pain programs). A search for OrphoMed returns Endpoints' 2023-01-12 "
                  "report that a Takeda-backed GI and pain biotech quietly shut down; the firm still lists it as private, "
                  "which goes stale. Mill Valley from the company's 2017 Form D."))

# ---- ouro
OURO_A = NEWS("ouro", "Launches to Define the Future")
L.append(cls("ouro", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=OURO_A,
             stage_conf="high", entry_date="2025-01-10", country="US", city="San Francisco", city_src="web_verified",
             focus="Healthcare & Bio",
             rounds=[rnd("2025-01-10", "Series A", 120000000, lead="TPG Life Sciences Innovations; NEA; Norwest",
                         firm_in_round=True, source=OURO_A, source_type="company")],
             note="Ouro Medicines launched in January 2025 with a $120M Series A co-led by TPG, NEA and Norwest (San "
                  "Francisco dateline); the firm dates the investment 2024. Gilead and Lakefront completed the "
                  "acquisition on 2026-06-04 (about $1.7B to $2.2B reported)."))

# ---- outrider
L.append(cls("outrider", status="private", rng="below_1b", city="Brighton", city_src="formd_address",
             focus="Industrial & Robotics",
             note="Autonomous yard trucks. City from the company's own 2026 Form D (Brighton, Colorado), fresher than the "
                  "8VC row's Golden. No $1B+ priced round on record."))

# ---- oyster-point
L.append(cls("oyster-point", rng="below_1b", city="Princeton", focus="Healthcare & Bio",
             note="Oyster Point Pharma (Nasdaq: OYST) was acquired by Viatris in January 2023, so no figure is carried."))

# ---- p-1
P1_A = NEWS("p-1", "Announces Its Series A")
L.append(cls("p-1", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=P1_A,
             stage_conf="medium", entry_date="2026-07-29", country="US", city="San Mateo", city_src="web_verified",
             focus="AI & Applied AI", extra=momentum(P1_A),
             rounds=[rnd("2025-04", "Seed", 23000000, lead="Radical Ventures", firm_in_round=False,
                         source=NEWS("p-1", "$23 Million Raised"), source_type="press"),
                     rnd("2026-07-29", "Series A", 50000000, lead="NEA", firm_in_round=True, source=P1_A,
                         source_type="company")],
             note="P-1 AI (engineering AI for physical systems, San Mateo dateline). NEA led the $50M Series A announced "
                  "2026-07-29; the $23M seed of 2025 was led by Radical Ventures and names no NEA fund. The firm dates its "
                  "first investment 2025, so the Series A may have closed before the announcement (medium confidence). "
                  "Momentum check 2026-09-30: no $1B+ priced round."))

# ---- pacific-light-hologram
L.append(cls("pacific-light-hologram", status="private", rng="below_1b", city="South Pasadena",
             city_src="formd_address", focus="Industrial & Robotics",
             note="Stealth holographic display company; South Pasadena from its own 2019 Form D. No priced mark on record."))

# ---- packeteer
L.append(cls("packeteer", status="acquired", rng="below_1b", stage="undetermined", entry_date="1996", country="US",
             city="Cupertino", focus="Data Infrastructure",
             note="WAN bandwidth management company in Cupertino, listed on Nasdaq and acquired by Blue Coat Systems in "
                  "2008 (Wikipedia). The record does not name NEA's 1996 round."))

# ---- pager
L.append(cls("pager", status="private", rng="below_1b", stage="undetermined", entry_date="2015", city="New York",
             focus="Healthcare & Bio",
             note="Pager Health, care-navigation software for health plans, still operating (NCQA reaccreditation, "
                  "2026-09-15; the $70M raise of September 2021 carried no $1B mark). Status aligned with the Lux row "
                  "(the GV row's unknown is superseded). The firm dates its first investment 2015 without a round word, "
                  "and no source read ties NEA to a named round."))

# ---- pair
L.append(cls("pair", status="private", rng="below_1b", city="New York", city_src="formd_address",
             focus="Consumer & Marketplaces",
             note="Pair Eyewear, direct-to-consumer glasses; its Form D address is in Brooklyn (New York). No $1B+ mark."))

# ---- panacea-medical-technologies
L.append(cls("panacea-medical-technologies", status="private", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("panacea-medical-technologies"), stage_conf="medium", entry_date="2013", country="IN",
             country_src="web_verified", country_cite=W("Panacea Medical Technologies"), city="Bangalore",
             focus="Healthcare & Bio",
             note="Radiotherapy and radiology equipment maker headquartered in Bangalore (Wikipedia), from NEA's India "
                  "desk. The firm labels its 2013 entry Growth."))

# ---- paratek (formerly Transcept)
L.append(cls("paratek-formerly-transcept-pharmaceuticals", rng="below_1b", stage="undetermined", entry_date="2007",
             country="US", city="Boston", focus="Healthcare & Bio",
             note="Transcept merged into Novacea's listed shell in 2009 and into Paratek in 2014; Paratek (Boston) was "
                  "taken private by Novo Holdings and Gurnet Point in 2023. The record does not name NEA's 2007 round."))

# ---- parc-place
L.append(cls("parc-place", status="acquired", rng="below_1b", stage="undetermined", entry_date="1991", country="US",
             city="Sunnyvale", focus="DevTools & APIs",
             note="ParcPlace Systems (Smalltalk tools) merged with Digitalk and became ObjectShare, whose product lines "
                  "were sold by 1999; the firm lists it acquired. The record does not name NEA's 1991 round."))

# ---- pathos
PATHOS = NEWS("pathos", "HLTH")
L.append(cls("pathos", status="private", rng="1b_plus", usd=1600000000, val_src="web_verified", val_cite=PATHOS,
             asof="2025-05", city="Chicago", city_src="formd_address", focus="Healthcare & Bio", extra=WV,
             note="AI-driven oncology drug developer. The $365M Series D of May 2025 set a post-money of about $1.6B "
                  "(HLTH, 2025-05-16). Endpoints reported on 2026-08-03 a planned Series E at $3B, not closed, so the "
                  "Series D stands."))

# ---- patientkeeper
L.append(cls("patientkeeper", status="acquired", rng="below_1b", stage="undetermined", entry_date="1999",
             city="Waltham", focus="Healthcare & Bio",
             note="Physician mobile software acquired by HCA Healthcare in 2020 and folded into Commure (the firm's "
                  "company link now points to commure.com). The 2009 Form D is a later round; the record does not name "
                  "NEA's 1999 entry."))

# ---- patreon
PAT = POST("patreon-putting-the-creator-first")
L.append(cls("patreon", stage="Growth", stage_src="first_party", stage_cite=PAT, stage_conf="high",
             entry_date="2020-09-02", city="San Francisco", focus="Media, Gaming & Advertising",
             rounds=[rnd("2020-09-02", "Series E", 90000000, lead="NEA (co-lead)", firm_in_round=True, source=PAT,
                         source_type="firm")],
             note="The firm's own post of 2020-09-02: NEA co-led Patreon's $90M Series E, its first investment (the firm "
                  "dates it 2020 and labels it Growth)."))

# ---- payzen
PZ = NEWS("payzen", "PayZen secures $32M Series B")
L.append(cls("payzen", status="private", rng="below_1b", city="San Francisco", city_src="formd_address",
             focus="Fintech & Payments", extra=momentum(PZ),
             note="Care-now-pay-later financing for hospital patients. NEA led the $32M Series B of August 2024 at a "
                  "valuation reported above $200M (TechCrunch). Momentum check 2026-09-30: no $1B+ priced round."))

# ---- pcorder
L.append(cls("pcorder", status="acquired", rng="below_1b", stage="undetermined", entry_date="1998", country="US",
             city="Austin", focus="Consumer & Marketplaces",
             note="pcOrder.com, Trilogy's online computer-products marketplace, listed in 1999 and taken back in by "
                  "Trilogy in 2000 (the firm's exit line). The record does not name NEA's round."))

# ---- pentaho
L.append(cls("pentaho", status="acquired", rng="below_1b", stage="undetermined", entry_date="2005", city="Orlando",
             focus="Data Infrastructure",
             note="Open-source BI vendor acquired by Hitachi Data Systems in 2015 (Wikipedia). The 2010 Form D is a later "
                  "round (the band was withheld against the firm's 2005 year); the record does not name NEA's 2005 round."))

# ---- peplin (X1 candidate)
PEP = FTS("PEPLIN", "10-12G")
L.append(cls("peplin", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_cite=PEP,
             stage_conf="medium", entry_date="2008-08-18", country="US", city="Emeryville", focus="Healthcare & Bio",
             rounds=[rnd("2008-08-18", "Private placement (ASX-listed)", 24067299, lead=None, firm_in_round=True,
                         source=PEP, source_type="filing")],
             note="Dermatology drug developer, then listed on the ASX, headquartered in Emeryville; acquired by LEO Pharma "
                  "in 2009. NEA 12 bought 264,608 units for $4.8M in the August 2008 unit placement (Form 10 exhibit). X1 "
                  "candidate: a placement into a listed company, and the firm labels it Public/PIPES."))

# ---- perplexity
L.append(cls("perplexity", status="private", rng="10b_plus", usd=20000000000, val_src="web_verified",
             val_cite="https://finance.yahoo.com/news/perplexity-finalizes-20-billion-valuation-232758524.html",
             asof="2025-09", city="San Francisco", focus="AI & Applied AI", extra=WV,
             note="Aligned with the Accel, IVP and 20VC rows: the September 2025 round at $20B is the last priced mark. "
                  "San Francisco also on its 2023 Form D."))

# ---- personal-genome-diagnostics
L.append(cls("personal-genome-diagnostics", status="acquired", rng="below_1b", city="Baltimore",
             city_src="formd_address", focus="Healthcare & Bio",
             note="PGDx was acquired by Labcorp in 2022 (the firm's exit line). NEA led its first institutional round in "
                  "2015 (the firm's own post)."))

# ---- pharmion
L.append(cls("pharmion", status="acquired", rng="below_1b", stage="Growth", stage_src="first_party",
             stage_cite=SITE("pharmion"), stage_conf="medium", entry_date="2001", country="US", city="Boulder",
             focus="Healthcare & Bio",
             note="Oncology and hematology company in Boulder, listed in 2003 and acquired by Celgene in 2008. The firm "
                  "labels its 2001 entry Growth; the 2003 S-1 names NEA 10 among the Series B holders, consistent with it."))

# ---- pharmos (D8 candidate)
L.append(cls("pharmos", stage="undetermined", entry_date="2006", country="US", city="Iselin",
             focus="Healthcare & Bio",
             note="NEA's Pharmos stock came in 2006 when Pharmos (Nasdaq: PARS, Iselin NJ) bought the NEA-backed Vela "
                  "Pharmaceuticals for cash and stock (8-K of 2006-03-15): sale consideration, a D8 candidate with Vela "
                  "the member. No round of Pharmos names NEA's entry."))

# ---- phase-forward
L.append(cls("phase-forward", status="acquired", rng="below_1b", stage="undetermined", entry_date="2001",
             country="US", city="Waltham", focus="Healthcare & Bio",
             note="Clinical-trial software company in Waltham, listed in 2004 and acquired by Oracle in 2010. The S-1 names "
                  "New Enterprise Associates VI among its holders, but the record does not name NEA's entry round."))

# ---- phasebio
L.append(cls("phasebio-pharmaceuticals", rng="below_1b", city="Malvern", focus="Healthcare & Bio",
             note="PhaseBio (Nasdaq: PHAS) filed for Chapter 11 in 2022 and sold its assets; no figure is carried."))

# ---- phathom (X1 candidate)
L.append(cls("phathom-pharmaceuticals", stage="Growth", stage_src="model", stage_conf="low", entry_date="2023",
             country="US", city="Florham Park", focus="Healthcare & Bio",
             note="Phathom (Nasdaq: PHAT) listed in October 2019; the firm dates its entry 2023 and labels it "
                  "Public/PIPES, a purchase into a listed company, so any entry reads Growth. X1 candidate."))

# ---- philo
L.append(cls("philo", status="private", rng="below_1b", city="San Francisco", grad="graduated", grad_src="web_verified",
             grad_cite=W("Philo (company)"), grad_conf="medium", grad_asof=CHECKED, focus="Media, Gaming & Advertising",
             rounds=[rnd("2013-07", "Series A", 6300000, lead="NEA (Patrick Chung)", firm_in_round=True,
                         source=W("Philo (company)"), source_type="press"),
                     rnd("2015-06", "Series B", 10000000, lead="NEA", firm_in_round=True, source=W("Philo (company)"),
                         source_type="press")],
             note="Streaming TV service, formerly Tivli, in San Francisco since 2015. The firm dates its first investment "
                  "2011 (archived label seed); Wikipedia names the July 2013 $6.3M Series A led by NEA's Patrick Chung and "
                  "the June 2015 $10M Series B, so the seed graduated."))

# ---- physical-intelligence
L.append(cls("physical-intelligence", status="private", rng="1b_plus", usd=5600000000, val_src="web_verified",
             val_cite="https://www.therobotreport.com/physical-intelligence-raises-600m-advancing-robot-foundation-models/",
             asof="2025-11-20", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2026", country="US",
             city="San Francisco", focus="AI & Applied AI", extra=WV,
             note="Aligned with eight sibling books at the $600M round of 2025-11-20 at $5.6B. Momentum check 2026-09-30: "
                  "a round of about $1B at $11B was reported in talks from 2026-03-27 to July 2026 (Bloomberg, The "
                  "Information), not confirmed closed. The firm dates its first investment 2026, after the $400M 2024 and "
                  "$600M 2025 rounds, so it reads Growth."))

# ---- picaboo
L.append(cls("picaboo", status="private", rng="below_1b", stage="undetermined", entry_date="2004", city="Palo Alto",
             focus="Consumer & Marketplaces",
             note="Photo book and yearbook service, still trading in 2026 (Tom's Guide and PetaPixel reviews); the firm "
                  "lists it private. The record does not name NEA's 2004 round."))

# ---- pilot-ai
L.append(cls("pilot-ai", status="acquired", rng="below_1b", stage="undetermined", entry_date="2016", country="US",
             focus="AI & Applied AI", flags=["city_unknown"],
             note="Pilot AI Labs, embedded deep-learning computer vision, acquired by Syntiant (the firm's exit line). A "
                  "news search for the deal found no dateline or office, so the city is left unknown. The record does not "
                  "name NEA's 2016 round."))

# ---- pinnacle-engines
L.append(cls("pinnacle-engines", status="private", rng="below_1b", stage="undetermined", entry_date="2007",
             country="US", city="San Carlos", focus="Climate & Energy",
             note="Opposed-piston engine developer; press through 2019 shows it still operating (Phys.org, 2019-02-12) and "
                  "the firm lists it private. The record does not name NEA's 2007 round."))

# ---- pionyr-immunotherapeutics
L.append(cls("pionyr-immunotherapeutics", status="acquired", rng="below_1b", stage="undetermined", entry_date="2017",
             country="US", city="San Francisco", focus="Healthcare & Bio",
             note="Myeloid-tuning cancer immunotherapy company acquired by Ikena Oncology in an all-stock deal in August "
                  "2023 (BioPharma Dive), after Gilead passed on its option. The record does not name NEA's 2017 round."))

# ---- pixiebrix
PIX = POST("our-series-a-investment-in-pixiebrix")
L.append(cls("pixiebrix", status="private", rng="below_1b", city="New York", city_src="formd_address",
             stage="Seed", stage_src="first_party", stage_cite=SITE("pixiebrix"), stage_conf="medium", entry_date="2021",
             grad="graduated", grad_src="first_party", grad_cite=PIX, grad_conf="medium", grad_asof=CHECKED,
             focus="SaaS", flags=["stage_disputes_band"], extra=momentum(PIX),
             rounds=[rnd("2021-06-29", "Seed", 3500000, lead=None, firm_in_round=True,
                         source=jl.FORMD_CITE("pixiebrix", 1), source_type="filing"),
                     rnd("2022-09-02", "Series A", None, lead="NEA", firm_in_round=True, source=PIX,
                         source_type="firm")],
             note="Low-code web customization. The firm labels its 2021 entry Seed (the $3.5M 2021 Form D); its own post of "
                  "2022-09-02 announces NEA's Series A investment, a later named round, so the seed graduated. The known "
                  "entry date 2022-05-19 read the Series A filing as the entry. Momentum check 2026-09-30: no $1B+ priced "
                  "round (2023 Form D $6.9M). New York address on its Form D."))

# ---- placemeter
L.append(cls("placemeter", status="acquired", rng="below_1b", stage="undetermined", entry_date="2014", country="US",
             city="New York", focus="AI & Applied AI",
             note="Computer-vision foot and vehicle traffic measurement from New York (TechCrunch 2015; Fast Company 2014), "
                  "acquired by Netgear in 2016 (the firm's exit line). The record does not name NEA's 2014 round."))

# ---- placester
L.append(cls("placester", status="private", rng="below_1b", city="Boston", city_src="formd_address", focus="SaaS",
             note="Real estate marketing software in Boston; still operating in 2021 (Business Wire) after 2018 layoffs. "
                  "Its last priced round, the $50M of 2017, carries no $1B mark."))

# ---- plaid
L.append(cls("plaid", city="San Francisco", focus="Fintech & Payments",
             note="San Francisco, as in every sibling book."))

# ---- plato (name collision with the Berlin Plato in the Atomico, Cherry and YC books)
PLATO = NEWS("plato", "bolster its Spatial Intelligence")
L.append(cls("plato", status="private", rng="below_1b", stage="undetermined", entry_date="2018", country="US",
             city="San Francisco", city_src="web_verified", focus="Industrial & Robotics",
             note="Plato Systems (plato.systems), a Stanford spin-off selling spatial intelligence for factories, San "
                  "Francisco dateline on its 2024-09-24 release; not the Berlin Plato in the Atomico, Cherry and YC books. "
                  "The record does not name NEA's 2018 round."))


jl.write("c8a", L)
