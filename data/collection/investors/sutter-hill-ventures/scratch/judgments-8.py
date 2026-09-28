#!/usr/bin/env python3
"""PRO-77 Sutter Hill Ventures, delta batch after the rebuild (queue/batch-001.json), judge b8.

Rows: 20 recall additions, 6 new Form D seats (Toolkit, Datawizz, Neos, BlueCava, Orgenesis, Leibniz; Matic is
also a recall addition), 7 IA-era software rows (the firm's 2000 and 2001 software pages), LifeSize
Communications' country. The four S2A rows of this queue (connection-engine, xios-therapeutics, boxer,
freestyle-software-inc) were closed by the graduation pass (grad-001) a minute after the queue was built and are
not repeated here.

Run: NQ_TAG=b8 python3 judgments-8.py
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
INV = HERE.parent
L = []
ASOF = "2026-09-28"

# ---- citations read from disk (never typed) --------------------------------------------------------
_LED = json.loads((INV / "companies/membership-ledger.json").read_text())["sutter-hill-ventures"]
_RC = {r["slug"]: r["citation"] for r in _LED["recall_additions"]}
_SIB = json.loads((HERE / "siblings.json").read_text())
_MOD = {r["name"]: r for r in json.loads((HERE / "recall/modern-candidates.json").read_text())}
_LOOSE = {r["name"]: r for r in json.loads((HERE / "recall/loose-candidates.json").read_text())}


def RC(slug):
    """The recall addition's verified citation (the URL inside the base note), from the ledger."""
    return _RC[slug]


def SIBV(slug, investor, key="val_cite"):
    m = [x for x in _SIB.get(slug, []) if x["investor"] == investor and x.get(key)]
    if len(m) != 1:
        raise SystemExit(f"SIBV({slug!r}, {investor!r}, {key!r}): {len(m)} matches")
    return m[0][key]


def MOD_URL(name, sub):
    m = [u for u in _MOD[name]["other_urls"] if sub in u]
    if len(m) != 1:
        raise SystemExit(f"MOD_URL({name!r}, {sub!r}): {len(m)} matches")
    return m[0]


def LOOSE_URL(name):
    return _LOOSE[name]["evidence_url"]


# press and filing URLs decoded by the helpers from headlines the tools printed
DR_REUTERS = NEWS("datarobot", "valued at $6.3 bln")
DR_CB20 = NEWS("datarobot", "Lands $270M At $2.7B")
RAMP_CNBC = SIBV("ramp", "coatue")
RAMP_32 = NEWS("ramp", "Ramp Valued at $32 Billion After $300 Million")
RAMP_PD = NEWS("ramp", "Ramp debuts accounting product")
RGTI_SA = SIBV("rigetti-computing", "lux-capital")
PHQ_NZH = NEWS("predicthq", "fund injection PredictHQ")
PHQ_18 = NEWS("predicthq", "Kiwi startup raises $15m")
ATTO_A = NEWS("attotude", "Raises $29M in Series A")
ATTO_B = NEWS("attotude", "$50M Series B Funding Led by Mayfield")
ATTO_C = NEWS("attotude", "$52 Million Series C")
GRID_LAUNCH = NEWS("gridcare", "GridCARE Launches with a Mission")
KOV_AH = NEWS("kovair", "Surge Ventures Acquires Kovair")
IO_SFS = NEWS("io-products", "OpenAI acquires Jony Ive")
IO_W = W("Io (company)")
VL_SF = NEWS("vlocity", "Salesforce Signs Definitive Agreement to Acquire Vlocity")
CURB_MD = NEWS("curbside", "Rakuten acquires mobile pickup platform")
CURB_TC14 = MOD_URL("Curbside", "2014/10/06")
TP_TC20 = MOD_URL("Transposit", "techcrunch.com/2020")
INFER_TC14 = NEWS("infer", "Infer Gets Another $25 Million")
RIDGE_26 = NEWS("ridge-biotechnologies", "Expands Investor Base as Demand Accelerates for AI-Designed Bioconjugate Therapeutics - businesswire")
ATM_AW = NEWS("atmosic-technologies", "Weekly Notable Startup Funding Report: 3/10/25")
MATIC_SR = NEWS("matic-robots", "Collisons back")
IB_FORMD = MOD_URL("Integrated Biosciences", "sec.gov")
LOGI_8K = LOOSE_URL("Lifesize, Inc. (2016 Logitech spin-off)")
QUME_W = W("Qume")
RGTI_W = W("Rigetti Computing")

# =====================================================================================================
# 1. Recall additions: membership (each citation was re-fetched and names Sutter Hill), then classification.
# =====================================================================================================

def member(slug, basis, conf="high", suffix=" Recall addition; the firm's archived lists end in 2016."):
    L.append(verdict(slug, "member", basis + suffix, ec="web", conf=conf, cite=RC(slug)))


# ---- Astronomer
member("astronomer", "A documented round names SHV: the $213M Series C (2022-03-23), led by Insight Partners, "
       "'with participation by ... Sutter Hill Ventures' (PR Newswire).")
L.append(cls("astronomer", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=RC("astronomer"), stage_conf="high", entry_date="2022-03-23",
    city="Cincinnati", focus="Data Infrastructure",
    extra={"valuation_range_source": "web_verified", "valuation_citation": RC("astronomer"), "valuation_asof": ASOF},
    rounds=[rnd("2022-03-23", "Series C", 213_000_000, "Insight Partners", True, RC("astronomer"), "company")],
    note="Data orchestration on Apache Airflow. SHV first appears in the $213M Series C of March 2022 (a Series C "
         "entry, Growth); no source read shows SHV in the 2019 seed or the 2020 to 2021 rounds, and Scott Yara of "
         "SHV later sat on the board. Momentum check 2026-09-28 (Google News for the company's valuation and later "
         "rounds): no priced round at $1B or more is reported; the 2025 Series D (about $93M, led by Bain Capital "
         "Ventures per that sibling's row) disclosed no valuation, and vendor estimates do not band (Rule A). "
         "below_1b, Cincinnati and private aligned with the Bain Capital Ventures and Insight rows."))

# ---- Atmosic Technologies
member("atmosic-technologies", "A documented financing names SHV: the chip startup 'has raised $21 million from "
       "investors that include Sutter Hill Ventures, Clear Ventures, and Walden International' (Stacey on IoT, "
       "2018-10-30).")
L.append(cls("atmosic-technologies", status="private", rng="below_1b", stage="undetermined",
    country="US", city="Campbell", city_src="web_verified", focus="Industrial & Robotics",
    rounds=[rnd("2018-10-30", "launch funding (no series named)", 21_000_000, None, True, RC("atmosic-technologies"), "press"),
            rnd("2025-03", "funding round (no series named)", 40_000_000, None, True, ATM_AW, "press")],
    note="Fabless semiconductor company making ultra-low-power Bluetooth chips with RF energy harvesting, "
         "'Campbell-based' (AlleyWatch, 2025-03). SHV was among the backers of the $21M raised by its launch in "
         "October 2018 and of the $40M round of March 2025 (Clear Ventures, Quantum Innovation Fund, SHV). Neither "
         "report names a round or a lead, so SHV's entry stage is undetermined. No valuation disclosed; below_1b."))

# ---- AttoTude
member("attotude", "A documented round names SHV: the $29M Series A of September 2024 lists 'Sutter Hill Ventures, "
       "Canaan Partners, and Wing Venture Capital' (the company's news page).")
L.append(cls("attotude", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC("attotude"), stage_conf="medium", entry_date="2024-09",
    country="US", city="Menlo Park", city_src="web_verified", focus="Industrial & Robotics",
    extra={"valuation_range_source": "web_verified", "valuation_citation": ATTO_C, "valuation_asof": ASOF},
    rounds=[rnd("2024-03-13", "Series Seed", 11_339_998, None, None, RC("attotude"), "company"),
            rnd("2024-09-04", "Series A", 28_828_036, None, True, ATTO_A, "press"),
            rnd("2025-04-02", "Series B", 50_000_000, "Mayfield", True, ATTO_B, "press"),
            rnd("2026-05-22", "Series C", 52_000_000, "The Westly Group", True, ATTO_C, "press")],
    note="Terahertz interconnect chips for AI and hyperscale data centers, Menlo Park (the company's page; its Form "
         "Ds give 506 Santa Cruz Avenue, later 70 Willow Road). Its Form Ds: Series Seed $11.3M (first sale "
         "2024-03-13, 35 investors), Series A $28.8M of $30M (2024-09-04), Series B $50M (2025-04-02), Series C "
         "$49.7M of $70M (2026-05-22); no SHV person is on any of them. SHV is first named in the Series A and is "
         "an existing investor in the B (Mayfield led) and the C (The Westly Group led). No source names the "
         "seed's investors, so an SHV seed check cannot be ruled out: Series A at medium. Chips read Industrial & "
         "Robotics. Momentum check 2026-09-28: the $52M Series C (Pulse 2.0, 2026-06-16) disclosed no valuation "
         "and no $1B+ round was found; below_1b."))

# ---- Cipher Data Products (Wikipedia is the only source: medium)
member("cipher-data-products", "Wikipedia: 'The company was initially funded by Sutter Hill Ventures of Palo Alto, "
       "California' (a 1968 San Diego tape-drive maker that the firm's 1999 table omits).", conf="medium",
       suffix=" Recall addition.")
L.append(cls("cipher-data-products", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Diego", city_src="web_verified", focus="Data Infrastructure",
    rounds=[rnd("1968", "initial funding (no series named)", None, None, True, RC("cipher-data-products"), "press")],
    note="Tape drives, San Diego, 1968 to 1992 (Wikipedia). SHV funded it at the start and began selling its shares "
         "to Computer Machinery Corporation in May 1973; Archive Corporation bought Cipher for $120M in 1990 and "
         "folded it into its software division in 1992. The record gives no round name for SHV's funding: "
         "undetermined. Storage reads Data Infrastructure. Status, band and city aligned with the Greylock and IVP "
         "rows."))

# ---- Curbside
member("curbside", "A documented round names SHV as lead: 'The round was led by Sutter Hill Ventures', with the "
       "earlier backer Index Ventures joining (TechCrunch, 2015-06-25, the $25M Series B).")
L.append(cls("curbside", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=RC("curbside"), stage_conf="high", entry_date="2015-06-25",
    country="US", city="Palo Alto", focus="Consumer & Marketplaces",
    rounds=[rnd("2014-10-06", "seed and Series A (launch)", 9_500_000, "Index Ventures", False, CURB_TC14, "press"),
            rnd("2015-06-25", "Series B", 25_000_000, "Sutter Hill Ventures", True, RC("curbside"), "press")],
    note="Same-day in-store pickup app, Palo Alto. SHV was new at the $25M Series B it led in June 2015 (a Series B "
         "entry, Growth); the earlier $9.5M from Index Ventures names no SHV. Rakuten bought Curbside in June 2018 "
         "(Marketing Dive) and later renamed it Rakuten Ready: acquired, below_1b."))

# ---- DataRobot
member("datarobot", "A documented round names SHV: the $300M Series G was 'joined by new investors ... Sutter Hill "
       "Ventures' (DataRobot's release, 2021-07-27).")
L.append(cls("datarobot", rng="1b_plus", usd=6_300_000_000, val_src="web_verified", val_cite=DR_REUTERS,
    asof="2021-07-27", val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=RC("datarobot"), stage_conf="high", entry_date="2021-07-27",
    city="Boston", focus="AI & Applied AI", flags=("stale",), clear=("unicorn_name_match",),
    rounds=[rnd("2020-11-17", "Series F", 270_000_000, None, False, DR_CB20, "press"),
            rnd("2021-07-27", "Series G", 300_000_000, "Altimeter Capital and Tiger Global", True, RC("datarobot"), "company")],
    note="Enterprise AI platform, Boston. SHV entered as a new investor in the $300M Series G of July 2021 (Growth), "
         "which valued DataRobot at $6.3B (Reuters, 2021-07-27): the last priced primary round, so the mark is "
         "cited and older than 24 months (stale). Momentum check 2026-09-28 (Google News): no later priced round; "
         "Benzinga (2026-09-22) reports secondary-market prices about 83% under the 2021 mark, which is a platform "
         "estimate and does not band or re-mark the row (Rule A). The unicorn-list prefill is replaced by the "
         "cited figure."))

# ---- GridCARE
member("gridcare", "A documented round names SHV as lead: 'Sutter Hill Ventures led the investment' in the $64M "
       "Series A (Latitude Media, 2026-05-14).")
L.append(cls("gridcare", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC("gridcare"), stage_conf="high", entry_date="2026-05-14",
    country="US", city="Redwood City", city_src="web_verified", focus="Climate & Energy",
    extra={"valuation_range_source": "web_verified", "valuation_citation": RC("gridcare"), "valuation_asof": ASOF},
    rounds=[rnd("2025-05-27", "Seed", 13_500_000, "Xora", False, GRID_LAUNCH, "press"),
            rnd("2026-05-14", "Series A", 64_000_000, "Sutter Hill Ventures", True, RC("gridcare"), "press")],
    note="Finds spare grid capacity to power AI data centers; its launch release is datelined and based in Redwood "
         "City (GlobeNewswire, 2025-05-27). The $13.5M seed was led by Xora with no SHV; SHV entered by leading "
         "the $64M Series A of May 2026. Momentum check 2026-09-28: no valuation disclosed for the Series A "
         "(Latitude Media, Pulse 2.0) and no later round; below_1b."))

# ---- Infer
member("infer", "A documented round names SHV: 'Infer has raised $10 million in Series A funding led by Redpoint "
       "Ventures, with other investors including ... Sutter Hill Ventures' (TechCrunch, 2013-04-23).")
L.append(cls("infer", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC("infer"), stage_conf="medium", entry_date="2013-04-23",
    country="US", country_src="formd_address", city="Palo Alto", city_src="formd_address", focus="SaaS",
    flags=("model_disputes_source",),
    rounds=[rnd("2013-03-13", "Series A", 10_000_000, "Redpoint Ventures", True, RC("infer"), "press"),
            rnd("2014-12-11", "Series B", 25_000_000, "Redpoint Ventures", None, INFER_TC14, "press")],
    note="Predictive lead scoring for sales teams; Infer, Inc. filed its Form Ds from Palo Alto (395 Page Mill Road "
         "in 2013, 260 Sheridan Avenue in 2014; incorporated 2010). SHV joined the Redpoint-led $10M Series A "
         "(Form D first sale 2013-03-13, announced 2013-04-23). The founder Vik Singh had been an entrepreneur in "
         "residence at SHV (TechCrunch), but no source names an earlier SHV round, so Series A at medium. Sold to "
         "ESW Capital's Ignite Technologies (2017 to 2018): acquired, as both US siblings read it. Country "
         "disputed: the Wikidata CZ is a wrong join on a one-word name; the filings give Palo Alto. The Y "
         "Combinator row named Infer (Bangalore) is a different company."))

# ---- Integrated Biosciences
member("integrated-biosciences", "A documented round names SHV as lead: 'closed a $17.2 million seed financing, "
       "led by Sutter Hill Ventures' (citybiz, 2024-10-03), with Keith Loebner of SHV joining the board.")
L.append(cls("integrated-biosciences", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=RC("integrated-biosciences"), stage_conf="high",
    entry_date="2024-10-03",
    grad="graduated", grad_src="web_verified", grad_cite=IB_FORMD, grad_conf="medium",
    country="US", city="Redwood City", city_src="web_verified", focus="Healthcare & Bio",
    rounds=[rnd("2024-10-03", "Seed", 17_200_000, "Sutter Hill Ventures", True, RC("integrated-biosciences"), "press"),
            rnd("2026-07-21", "unnamed (Form D)", 68_374_977, None, None, IB_FORMD, "filing")],
    note="Synthetic biology and machine learning for drugs against aging-related disease, Redwood City (the "
         "release's dateline; the 2026 Form D gives 900 Island Drive). SHV led the $17.2M seed. The company's "
         "Form D of 2026-08-05 reports a new equity offering, $68.4M sold of $100M from 39 investors (first sale "
         "2026-07-21), with Keith Loebner (SHV) a director: no press names the round, and an unnamed later round "
         "at about four times the seed passes the step-up test (2x entry and $5M), so graduated on the filing "
         "(medium). No valuation disclosed; below_1b."))

# ---- io Products
member("io-products", "The press names SHV as an investor: 'Bloomberg also confirmed Sutter Hill Ventures was an "
       "investor' (TechCrunch, 2025-05-22); Wikipedia lists SHV among the backers of io's $225M raise of 2024.")
L.append(cls("io-products", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    rounds=[rnd("2024", "funding (no series named)", 225_000_000, None, True, IO_W, "press")],
    note="AI hardware devices from Jony Ive, Scott Cannon, Evans Hankey and Tang Tan, San Francisco. io raised "
         "$225M in 2024 from SHV, Emerson Collective, SV Angel, Maverick and Thrive (Wikipedia), but no source names "
         "the round or when SHV came in: undetermined. OpenAI agreed in May 2025 to buy io in an all-stock deal "
         "valuing it at about $6.5B (San Francisco Standard) and completed it in 2025: acquired, below_1b. A "
         "consumer device reads Consumer & Marketplaces."))

# ---- K2 Optronics
member("k2-optronics", "A documented round names SHV: the $29M second round of March 2001 'featured proportional "
       "investments from first-round financing participants: Alloy Ventures, Sutter Hill Ventures, JAFCO' "
       "(Lightwave); the firm's 2000 to 2006 networking pages also listed it.", suffix=" Recall addition.")
L.append(cls("k2-optronics", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Sunnyvale", focus="Industrial & Robotics",
    rounds=[rnd("2000", "first round (no series named)", None, None, True, RC("k2-optronics"), "press"),
            rnd("2001-03", "second round", 29_000_000, "Bessemer Venture Partners", True, RC("k2-optronics"), "press")],
    note="Transmission lasers for fiber-optic networks, founded 2000 in Sunnyvale. SHV was in the 2000 first round "
         "and took its pro-rata share of the Bessemer-led $29M second round; the record calls the entry only a "
         "'first round', which names no stage, so undetermined. EMCORE, already a holder, bought the rest in "
         "January 2006 for about $4.1M in EMCORE stock (EMCORE 8-K; the firm's 2006 page: acquired by Emcore). "
         "SHV's EMCORE shares were the sale consideration, not a separate position. Lasers and optical components "
         "read Industrial & Robotics, as on the other chip and photonics rows."))

# ---- Lifesize (2016 Logitech spin-off): a control position, not a venture entry
v = verdict("lifesize", "not_member",
    "Control position (T3 control addendum; the run's Therma-Wave precedent). On 2015-12-28 Redpoint, Sutter Hill "
    "and Meritech bought the new Series B Preferred of Lifesize, Inc. ($17.5M from the company plus $2.5M from "
    "Logitech), holding 62.5% of the shares, while Logitech kept 37.5% as non-voting Series A with 'no voting "
    "rights or other influence' and reported the deal as the divestment of its video conferencing segment "
    "(Logitech 8-K, Items 1.01 and 2.01). The firm's co-investor group took control of a corporate carve-out, which "
    "is not a venture entry, although SHV's own third was a minority. LifeSize Communications (2003 to 2009) stays "
    "a member on its own row. The recall brief proposed member: flagged for review.",
    ec="web", conf="medium", cite=LOGI_8K)
v["exclusion"] = "control_position"
L.append(v)

# ---- Matic Robots (recall addition and a Victor Miller Form D seat)
member("matic-robots", "A documented round names SHV: 'The company just announced a new $50 million fundraise, its "
       "Series A, from Sutter Hill Ventures' (Newcomer, 2026-02); Victor Miller (SHV) is a director on the round's "
       "Form D (first sale 2025-07-29).")
L.append(cls("matic-robots", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC("matic-robots"), stage_conf="medium",
    city="Mountain View", city_src="formd_address", focus="Consumer & Marketplaces",
    flags=("stage_disputes_band",),
    extra={"valuation_range_source": "web_verified", "valuation_citation": RC("matic-robots"),
           "valuation_asof": "2026-02-05"},
    rounds=[rnd("2023-11", "angel round (no series named)", 30_000_000, None, False, MATIC_SR, "press"),
            rnd("2025-07-29", "Series A", 50_000_000, "Sutter Hill Ventures", True, RC("matic-robots"), "press")],
    note="Home robot vacuum that maps rooms on-device, Mountain View (the Form D address, 339 N Bernardo Avenue). "
         "Earlier backers were angels (the Collisons, Garry Tan, Adam D'Angelo; a $30M round, Silicon Republic "
         "2023). SHV led the $50M Series A at a $650M valuation with Valor and Atreides (Newcomer). Its Form D "
         "(first sale 2025-07-29, $77.3M sold of $86.9M, 66 investors) is inferred to be that round with the "
         "earlier money converting, so the entry date stays 2025-07-29; the band's Growth, read from the $77.3M, "
         "is disputed because the record names the round Series A (medium, as the amounts differ). A $650M priced "
         "round and no later one: below_1b. A consumer device reads Consumer & Marketplaces."))

# ---- PredictHQ
member("predicthq", "A documented round names SHV as lead: 'PredictHQ announced it has raised $22 million in Series "
       "B funding led by Sutter Hill Ventures' (Pulse 2.0, 2020-02).")
L.append(cls("predicthq", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=RC("predicthq"), stage_conf="high", entry_date="2020-02",
    country="NZ", country_src="web_verified", country_cite=PHQ_NZH, city="Auckland", city_src="web_verified",
    focus="Data Infrastructure",
    rounds=[rnd("2018-11", "Series A", 15_000_000, None, False, PHQ_18, "press"),
            rnd("2020-02", "Series B", 22_000_000, "Sutter Hill Ventures", True, RC("predicthq"), "press")],
    note="Demand intelligence from real-world events, Auckland (NZ Herald: 'Auckland's PredictHQ raises $34m', "
         "NZ$34M being the US$22M), with a San Francisco office. SHV was new at the Series B it led in February "
         "2020, its first major investment in New Zealand (NZ Herald); Lightspeed backed the earlier Series A. "
         "Growth entry. No later priced round at $1B or more found; below_1b. Status, band, country and city "
         "aligned with the Lightspeed row."))

# ---- Qume
member("qume", "Paul Wythes's obituary (Mercury News, 2012-11-05) names Qume among the companies Sutter Hill backed "
       "early; the firm's 1999 table omits it, as it omits other 1970s positions the obituary names.",
       suffix=" Recall addition.")
L.append(cls("qume", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="San Jose", city_src="web_verified", focus="Industrial & Robotics", rounds=[],
    note="Daisy-wheel printers (later terminals and disk drives), founded 1973 by David S. Lee and Robert "
         "Schroeder in Hayward, later San Jose; ITT bought it for $164M in 1978, and it was later part of Wyse "
         "(Wikipedia). Acquired, below_1b. The obituary names no round or date for SHV's investment: "
         "undetermined. Printer hardware reads Industrial & Robotics."))

# ---- Ramp
member("ramp", "A documented round names SHV: 'New investors for this round include: Sutter Hill Ventures, "
       "Lightspeed Ventures, T. Rowe Price Associates, Inc., GV' (PR Newswire, the $500M round at $22.5B, July 2025).")
L.append(cls("ramp", rng="10b_plus", usd=44_000_000_000, val_src="web_verified", val_cite=RAMP_CNBC,
    asof="2026-06-04", val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=RC("ramp"), stage_conf="high", entry_date="2025-07-30",
    city="New York", focus="Fintech & Payments", clear=("unicorn_name_match",),
    rounds=[rnd("2025-07-30", "Series E-2", 500_000_000, "ICONIQ", True, RC("ramp"), "company"),
            rnd("2025-11-17", "primary round and tender", 300_000_000, None, True, RAMP_32, "press"),
            rnd("2026-06", "funding round at $44B", 750_000_000, "ICONIQ Growth, GIC, Ontario Teachers'", None, RAMP_PD, "press")],
    note="Corporate cards and spend management, New York. SHV entered as a new investor in the $500M Series E-2 "
         "at $22.5B (July 2025), a Growth entry, and was an existing investor in the $300M round at $32B "
         "(November 2025). The last priced round is the $750M of June 2026 at $44B (CNBC; Payments Dive), the "
         "mark the Coatue, Lightspeed, Sequoia, Spark and Thrive rows carry; the $60B talks reported in September "
         "2026 are not a priced event. The unicorn-list $32B prefill is replaced. The Balderton row named Ramp "
         "(Warsaw, crypto) is a different company."))

# ---- Ridge Biotechnologies
member("ridge-biotechnologies", "A documented round names SHV as lead and incubator: 'The funding round was led by "
       "Sutter Hill Ventures (SHV), which incubated Ridge Bio' (SynBioBeta, the $25M seed of 2025-09-09).")
L.append(cls("ridge-biotechnologies", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=RC("ridge-biotechnologies"), stage_conf="high",
    entry_date="2025-09-09", grad="censored",
    country="US", city="Palo Alto", city_src="web_verified", focus="Healthcare & Bio",
    rounds=[rnd("2025-09-09", "Seed", 25_000_000, "Sutter Hill Ventures", True, RC("ridge-biotechnologies"), "press"),
            rnd("2026-09-09", "Seed extension", 13_000_000, "Dimension Capital", None, RIDGE_26, "press")],
    note="Machine-learning design of enzymes and bioconjugates (ADC linkers), 'Based in Palo Alto' (the launch "
         "release). An SHV incubation (D3) whose first round the record names a seed: SHV incubated it and led "
         "the $25M seed; the September 2026 extension to about $38M (anchored by Dimension Capital) is the same "
         "seed, not a later round. Entry 2025-09-09 is inside the 24-month window: censored. below_1b."))

# ---- Rigetti Computing (public)
member("rigetti-computing", "A documented round names SHV: 'Institutional investors in Series A include Sutter Hill "
       "Ventures, Susa Ventures, Streamlined Ventures, Lux Capital, and Bloomberg Beta' (PR Newswire, 2017-03-28).")
L.append(cls("rigetti-computing", rng="1b_plus", usd=5_320_000_000, val_src="web_verified", val_cite=RGTI_SA,
    asof=ASOF, val_conf="high", extra={"valuation_range_source": "web_verified"},
    stage="Series A", stage_src="web_verified", stage_cite=RC("rigetti-computing"), stage_conf="high",
    entry_date="2017-03",
    city="Berkeley", city_src="web_verified", focus="Industrial & Robotics",
    rounds=[rnd("2017-03-28", "Series A", 24_000_000, "Andreessen Horowitz", True, RC("rigetti-computing"), "company"),
            rnd("2017-03-28", "Series B", 40_000_000, "Vy Capital", None, RC("rigetti-computing"), "company")],
    note="Superconducting quantum computers, Berkeley (the release's dateline; Wikipedia). SHV's first named round "
         "is the $24M Series A led by Andreessen Horowitz, announced 2017-03-28 with the $40M Series B; the "
         "release does not date the A's close (Wikipedia places it earlier) and the $69.2M total implies about "
         "$5M raised before it with no investors named, so the entry date is the announcement. Public on Nasdaq "
         "(RGTI) since the Supernova II merger of March 2022. Market cap $5.32B at the 2026-09-28 close "
         "(stockanalysis.com), fresher than the siblings' $5.07B of 2026-09-04, same band; it replaces the SEC "
         "float prefill."))

# ---- Transposit
member("transposit", "A documented round names SHV as lead: 'Sutter Hill Ventures led the Series A round, with "
       "participation from SignalFire and Unusual Ventures' (SiliconANGLE, 2019-03-07).")
L.append(cls("transposit", status="defunct", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC("transposit"), stage_conf="medium", entry_date="2019-03-07",
    country="US", city="San Francisco", focus="DevTools & APIs",
    rounds=[rnd("2019-03-07", "Series A", 12_200_000, "Sutter Hill Ventures", True, RC("transposit"), "press"),
            rnd("2020-09-02", "Series B", 35_000_000, "Altimeter Capital", True, TP_TC20, "press")],
    note="API composition, later incident-management runbooks for engineering teams, San Francisco. SHV led the "
         "$12.2M Series A (2019) and was an existing investor in the $35M Series B led by Altimeter (TechCrunch, "
         "2020). A small earlier seed has no named investors, so Series A at medium. The company's own site says "
         "it 'made the difficult decision to shut our doors' and that Harness is licensing its product and "
         "technology: a licence, not a purchase of the company, so defunct."))

# ---- Vlocity
member("vlocity", "A documented round names SHV as co-lead: 'The round was led by Sutter Hill Ventures and Salesforce "
       "Ventures' (TechCrunch, 2019-03-26, the $60M Series C).")
L.append(cls("vlocity", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=RC("vlocity"), stage_conf="high", entry_date="2019-03-26",
    country="US", city="San Francisco", focus="SaaS",
    rounds=[rnd("2019-03-26", "Series C", 60_000_000, "Sutter Hill Ventures and Salesforce Ventures", True,
                RC("vlocity"), "press")],
    note="Industry cloud applications built on Salesforce, San Francisco. SHV co-led the $60M Series C at a $1B "
         "valuation (March 2019), its entry (Growth); no source shows SHV in the earlier rounds. Salesforce signed "
         "to buy Vlocity for $1.33B in cash on 2020-02-25 (Salesforce's release) and closed in 2020: acquired, "
         "below_1b."))

# =====================================================================================================
# 2. New Form D rows from the three people added to the roster (Blond, Miller, Peets) and Leibniz.
# =====================================================================================================
FD = "formd_adjudicated"

L.append(verdict("toolkit-inc", "not_member",
    "Seat dating (D5): Brian Blond is a director on Toolkit's only Form D (first sale 2024-12-13, $3.35M), filing c/o "
    "the company in San Francisco, not from SHV's suite. He had left SHV for Human Capital by May 2023 (Human "
    "Capital's team page; TechCrunch, 2026-02-11: 'a partner at Human Capital and was formerly at Sutter Hill'), so "
    "the money behind the seat was not SHV's. No SHV listing, SHV filing or documented round names Toolkit.",
    ec=FD, conf="high", cite=SEC("toolkit-inc")))

L.append(verdict("datawizz-inc", "not_member",
    "Seat dating (D5): Brian Blond is a director on Datawizz's August 2025 Form D (first sale 2025-08-29, $12.9M), "
    "filing from 340 Pine Street, San Francisco, beside founder Iddo Gino. Human Capital led the $12.5M seed and "
    "the release has Blond join the board as 'Investment Partner at Human Capital'; it does not name SHV (PR "
    "Newswire, 2025-09-30). He had left SHV by May 2023. No SHV listing, filing or documented round names Datawizz.",
    ec=FD, conf="high", cite=SEC("datawizz-inc")))

L.append(verdict("neos-therapeutics-inc", "not_member",
    "Victor Miller is an executive officer on Neos Therapeutics' 2011 to 2014 Form Ds at the company's own address "
    "in Grand Prairie, Texas, among its managers (the same officer list titles him VP Finance in a December 2013 "
    "filing): an officer of the issuer, not an SHV seat, and years before the roster's first SHV date for a "
    "Victor Miller (2025), so a namesake or a pre-SHV role (seat dating, D5). No SHV listing, SHV filing or "
    "documented round names Neos.",
    ec=FD, conf="high", cite=SEC("neos-therapeutics-inc")))

L.append(verdict("bluecava-inc", "not_member",
    "BlueCava, Inc. (Irvine, device identification for advertising) filed a December 2013 Form D whose officer list "
    "is Neos Therapeutics' management at Neos's Grand Prairie, Texas address, including Victor Miller as 'VP "
    "Finance': a filer's error or shared filer, not an SHV person. Read at face value it is still an issuer "
    "finance officer before the roster's first SHV date for a Victor Miller (2025; seat dating, D5). No SHV "
    "listing, SHV filing or documented round names BlueCava.",
    ec=FD, conf="high", cite=SEC("bluecava-inc")))

L.append(verdict("orgenesis-inc", "not_member",
    "Victor Miller is an executive officer on Orgenesis's March 2024 Form D ($2.34M) at the company's own address in "
    "Germantown, Maryland: the issuer's officer, not an SHV seat, and before the roster's first SHV date for a "
    "Victor Miller (2025), so a namesake or a pre-SHV role (seat dating, D5). Orgenesis, an SEC-reporting "
    "cell-therapy company since 2011, names no SHV person on its other Form Ds, and no SHV listing, filing or "
    "documented round names it.",
    ec=FD, conf="high", cite=SEC("orgenesis-inc")))

L.append(verdict("leibniz-data-systems-inc", "member",
    "Incubation and director-of-record pattern (D3; COLLECTION.md s1): on the company's only Form D (first sale "
    "2021-09-15, $15.0M equity from 34 investors) both founders, Divanny Lamas (an SHV managing director) and "
    "Efstratios Ydraios, are directors and executive officers filing from SHV's own suite (Bldg A 200, 755 Page "
    "Mill Road), and Brian Blond (at SHV in 2021) is a director. The issuer resolves to a company SHV formed; no "
    "announcement names the round, hence medium.",
    ec=FD, conf="medium", cite=SEC("leibniz-data-systems-inc")))
L.append(cls("leibniz-data-systems-inc", status="unknown", rng="below_1b",
    city="Palo Alto", city_src="formd_address", focus="Data Infrastructure",
    rounds=[rnd("2021-09-15", "unnamed (Form D)", 14_999_998, None, None, SEC("leibniz-data-systems-inc"), "filing")],
    note="An SHV incubation housed at the firm's suite in Palo Alto (the Form D address). Beyond the one Form D no "
         "website, press item, later filing or rename was found through 2026, so its fate is not on record: "
         "status unknown, below_1b. Data Infrastructure is inferred from the name ('Data Systems'). The band's "
         "Series A stands: no documented round names the entry otherwise (a vendor profile also says Series A, "
         "which cannot cite)."))

# =====================================================================================================
# 3. IA-era rows: the firm's 2000 and 2001 software pages (listed members; logos only, the per-company pages
#    are in the Internet Archive, which blocks this machine). Classification only.
# =====================================================================================================

L.append(cls("collabrys", status="acquired", rng="below_1b", stage="undetermined",
    country="US", focus="SaaS", flags=("city_unknown",), rounds=[],
    note="Collabrys, Inc., interactive marketing technology and services (e-mail marketing: list management, "
         "delivery, tracking); the firm listed it under Software in 2001 and under Business & Financial Services "
         "in 2004. E-centives bought substantially all of its assets on 2004-06-29 for $15,000 in cash plus "
         "royalties (E-centives' 10-KSB for 2004): an asset sale out of a wind-down reads acquired, below_1b. No "
         "source read names the round SHV joined. City not found: vendor profiles give Bethesda, which is the "
         "acquirer's home, so city_unknown."))

L.append(cls("conscium", status="unknown", rng="below_1b", stage="undetermined",
    country="US", city="San Francisco", city_src="web_verified", focus="SaaS", rounds=[],
    note="Conscium, Inc., San Francisco: secure web collaboration on legal and financial documents through its "
         "Financialprinter.com unit (Computerworld, 2000-02-07; IntraLinks' 2005 S-1 calls it 'a web-based "
         "financial document company'); Adobe Ventures III also held it (Adobe's 10-K for 2000). On the firm's "
         "2000 software page only. Its fate is not on record: a vendor profile says acquired but names no buyer "
         "and no usable date, so status unknown. No round naming SHV found."))

L.append(cls("crossweave", status="defunct", rng="below_1b", stage="undetermined",
    country="US", city="Oakland", focus="SaaS", rounds=[],
    note="CrossWeave, Inc., web-services integration software; on the firm's software pages in 2000 and 2001 and "
         "gone by 2004. GXS's S-4/A of July 2003 still lists a Norwest partner on its board; no later record. "
         "Status, band and city aligned with the Redpoint row (defunct, Oakland: in Redpoint's own table 2000 to "
         "2003 and gone after); no fresher evidence. No round naming SHV found."))

L.append(cls("iei", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
    flags=("identity_unresolved",), rounds=[],
    note="Company not identified. The firm's January and March 2001 software pages show only an 'IEI' logo linking "
         "to /soft/iei.html, a page the Internet Archive holds (captured 2001-03-04) but this machine cannot read "
         "while the archive's block lasts. Tried: EDGAR full-text search ('IEI, Inc.', 2001 to 2004; Sutter Hill "
         "with IEI), Google News and web search: nothing ties an IEI to SHV. identity_unresolved, so stage, band "
         "and S2A read undetermined and status unknown; the archived page should settle it when the archive "
         "recovers."))

L.append(cls("kovair", status="acquired", rng="below_1b", stage="undetermined",
    country="US", city="Menlo Park", city_src="web_verified", focus="DevTools & APIs", rounds=[],
    note="Kovair Software, application lifecycle management and tool-integration software (the Omnibus platform), "
         "Menlo Park with development in Kolkata (its own site). The firm listed Kovair on its 2000 and 2001 "
         "software pages, and vendor profiles list SHV among Kovair's investors and date its founding to 1999 or "
         "2000 (one 2025 article says 2006). Surge Ventures took a majority stake in April 2024 (AdvisorHub; "
         "Wealth Management): acquired, below_1b. No source names the round SHV joined."))

L.append(cls("saltare", status="unknown", rng="below_1b", stage="undetermined",
    country="US", city="San Mateo", city_src="web_verified", focus="SaaS", rounds=[],
    note="Saltare (Saltare.com), web-based collaborative supply-chain event management software, founded 1998, "
         "2755 Campus Drive, San Mateo (vendor profile, used for identity and address only); backed by Draper "
         "Fisher Jurvetson, SHV and Weston Presidio. On the firm's software pages in 2000 and 2001 and gone by "
         "2004. Its fate is not established: vendor profiles disagree (acquired with no buyer named; closed) and "
         "no filing names it after 2001, so status unknown. No round naming SHV found."))

L.append(cls("websentric", status="unknown", rng="below_1b", stage="undetermined",
    country="US", focus="SaaS", flags=("city_unknown",), rounds=[],
    note="WebSentric, a web conferencing company: an E-Stamp director (Gumucio) chaired its board (E-Stamp's 2001 "
         "proxy), and Ezenia's 2005 reseller agreement lists it among web conferencing competitors. On the "
         "firm's 2000 software page only. No filing, press item or profile gives its city or its fate: status "
         "unknown, city_unknown; US is inferred from the firm's portfolio and its chairman. No round naming SHV "
         "found."))

# ---- LifeSize Communications: the one open column
L.append(cls("lifesize-communications", country="US",
    note="Country US: LifeSize Communications was an Austin, Texas company (the firm's own page) until Logitech "
         "bought it in 2009."))

if __name__ == "__main__":
    jl.write("delta-001", L)
