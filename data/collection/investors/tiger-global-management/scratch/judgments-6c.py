#!/usr/bin/env python3
"""PRO-167 grind, queue batch 6, chunk c (rows 31-45). Judge b6.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b6 (bq.py), sibling books' records, and pages fetched and read in this pass (the
literal URLs below). Every citation is read from disk by a helper or is a page fetched and read here."""
import json
import os
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PKD = json.loads((HERE / "evidence-pack.json").read_text())
BND = json.loads((HERE / "bing-news.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PK(slug, sub, kind="press"):
    """A URL from the row's evidence-pack lines (press '|| URL', sec line tail, wiki or recall parentheses)."""
    p = PKD.get(slug, {})
    if kind == "recall":
        m = re.findall(r"\((https?://[^)\s]+)\)", p.get("recall_basis") or "")
        if not m:
            raise SystemExit(f"PK recall {slug}")
        return m[-1]
    urls = []
    for x in p.get(kind) or []:
        if sub.lower() not in x.lower():
            continue
        if kind == "press":
            m = re.search(r"\|\| URL (\S+)", x)
        elif kind == "sec":
            m = re.search(r"\| (https?://\S+)\s*$", x)
        else:
            m = re.search(r"\((https?://[^)\s]+)\)", x)
        if m:
            urls.append(m.group(1))
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {sub!r}, {kind}) -> {urls}")
    return urls[0]


def BN(key, sub):
    """A publisher URL from the Bing candidate cache (bing-news.json[key]) whose title contains sub."""
    urls = list(dict.fromkeys(i["url"] for i in (BND.get(key) or {}).get("items", [])
                              if sub.lower() in i["title"].lower()))
    if len(urls) != 1:
        raise SystemExit(f"BN({key!r}, {sub!r}) -> {urls}")
    return urls[0]


def SIB(slug, inv):
    """(usd, asof, citation) of a sibling book's mark for the same company, from the evidence pack."""
    for x in PKD.get(slug, {}).get("sib", []):
        if x["investor"] == inv and x.get("val_cite"):
            return int(float(x["usd"])), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}) missing")


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []
CHECK = "2026-09-29"

# ---------------------------------------------------------------- gupshup (recall seed confirmed)
GU_W = W("Gupshup")
GU_FID = NEWS("gupshup", "Fidelity marks down conversational AI platform Gupshup")
L.append(cls("gupshup", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": GU_FID, "valuation_asof": "2026-01-31"},
             stage="Growth", stage_src="web_verified", stage_cite=GU_W, stage_conf="high", entry_date="2021-04-08",
             country="US", city="San Francisco", focus="DevTools & APIs",
             note="Conversational messaging and AI platform, San Francisco with its main operations in Mumbai. Tiger "
                  "led the $100M Series F of April 2021 at $1.4B (Wikipedia; Bloomberg), its first round: Growth; a "
                  "$240M round followed in July 2021. Collapse evidence: Fidelity's fund marked its Gupshup holding "
                  "down more than 80%, to about $278M, as of 2026-01-31 (reported April 2026), after a string of "
                  "markdowns from 2023; the 2021 mark no longer stands, so below $1B with no figure. Momentum check "
                  + CHECK + ": no later priced round at $1B or more.",
             rounds=[rnd("2021-04-08", "Series F", 100_000_000, "Tiger Global", True, GU_W, "press")]))

# ---------------------------------------------------------------- gushan (seeded filing row)
GH_X = PK("gushan-environmental-energy-ltd", "Tiger Holder", "sec")
L.append(verdict("gushan-environmental-energy-ltd", "member",
                 "Gushan's 2007 F-1 exhibits: the share and note purchase agreement for Carling Technology, the "
                 "pre-IPO holding company, lists Tiger Global Private Investment Partners III as holder of a "
                 "$19.9M convertible note issued 2006-02-23 and of shares beside Tiger Global, L.P., II and Ltd., and "
                 "PIP III signs the investors' rights agreement as the 'Tiger Holder': a private-equity desk fund held "
                 "the company before its December 2007 NYSE listing", ec="fund_filing", conf="high", cite=GH_X))
L.append(cls("gushan-environmental-energy-ltd", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=GH_X, stage_conf="medium", entry_date="2006-02-23",
             country="HK", country_src="web_verified", country_cite=GH_X, city="Hong Kong",
             focus="Climate & Energy",
             note="Biodiesel producer with plants in mainland China, notice address in Hong Kong (the F-1 exhibit). "
                  "Tiger's PIP III held a $19.9M convertible note issued in February 2006 in the pre-IPO holding "
                  "company, a financing of an established producer: Growth. Listed on the NYSE in December 2007; "
                  "taken private in 2012 (Schedule 13E-3 from June 2012, registration terminated 2012-10-29 on "
                  "EDGAR): acquired. The public-desk funds named beside PIP III do not move the row (X1 needs a "
                  "public-desk vehicle alone).",
             rounds=[rnd("2006-02-23", "convertible note", 19_900_000, None, True, GH_X, "filing")]))

# ---------------------------------------------------------------- harbinger (membership open)
HB_PR = PK("harbinger", "irblog.prnewswire.com | HARBINGER MOTORS")
L.append(verdict("harbinger", "member",
                 "Harbinger's release on the $60M Series A (2023-09-20): 'Further investment includes return investors "
                 "Tiger Global, Kalyani Mobility, Maniv Mobility, Overture and Ironspring Ventures'; TechCrunch "
                 "(2025-01-14) calls Tiger an existing investor in the Series B, so the firm holds the company "
                 "through private rounds", ec="web", conf="high", cite=HB_PR))
L.append(cls("harbinger", status="private", rng="below_1b", stage="undetermined",
             country="US", city="Garden Grove", focus="Industrial & Robotics",
             note="Medium-duty electric truck chassis, Garden Grove (California). Tiger was already an investor at the "
                  "$60M Series A of September 2023 ('return investors', the company's release) and joined the $100M "
                  "Series B (January 2025) and the $160M Series C (November 2025); the earlier round it entered is not "
                  "named on record, so the stage is undetermined.",
             rounds=[rnd("2023-09-20", "Series A", 60_000_000, None, True, HB_PR, "company")]))

# ---------------------------------------------------------------- harry-s-inc and hf-global-inc (one company)
HR_E = NEWS("harry-s-inc", "Raises A $155 Million Series E At $1.7 Billion")
HARRYS = dict(status="private", rng="1b_plus", usd=1_700_000_000, val_src="web_verified", val_cite=HR_E,
              asof="2021-03-31", extra=WV, flags=["stale"],
              stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014-12",
              city="New York", focus="Consumer & Marketplaces",
              rounds=[rnd("2014-12", "Form D sale ($75M), filed as HF Global, Inc.", 75_000_000, None, True,
                          SEC("hf-global-inc", "formd", 0), "filing"),
                      rnd("2021-03-31", "Series E", 155_000_000, None, None, HR_E, "press")])
HARRYS_NOTE = ("Harry's, razors and personal care brands, New York. The company filed its Form Ds as HF Global, Inc. in "
               "2014-2015 and as Harry's, Inc. from 2017 (same CIK 1556308, so the rows harry-s-inc and hf-global-inc "
               "are one company). Lee Fixel, a Tiger partner until early 2019, is director on the $75M Form D of the "
               "fourth quarter of 2014 and on the 2015 and 2017 filings: the entry is the December 2014 $75M round "
               "(the New York Times and Vox reported it), a Growth round of a company that had raised $122.5M earlier "
               "that year (model, medium). His seats on the 2021-2022 filings are Addition's (D7). Mark: the $155M "
               "Series E at $1.7B (Forbes, 2021-03-31), older than 24 months, so stale.")
L.append(verdict("harry-s-inc", "member",
                 "Director-of-record: Lee Fixel, a Tiger partner in tenure, is director on Harry's 2017 Form Ds and, "
                 "under the company's earlier name HF Global, Inc. (same CIK), on its 2014 and 2015 Form Ds; the "
                 "issuer resolves to the razor company and no contrary evidence exists (seats from 2021 are "
                 "Addition's, D7)", ec="formd_adjudicated", conf="medium", cite=SEC("harry-s-inc")))
L.append(cls("harry-s-inc", note=HARRYS_NOTE, **HARRYS))
L.append(verdict("hf-global-inc", "member",
                 "Director-of-record: Lee Fixel, a Tiger partner in tenure, is director on the 2014 ($75M) and 2015 "
                 "Form Ds of HF Global, Inc., the earlier filing name of Harry's, Inc. (same CIK 1556308); the issuer "
                 "resolves to the razor company and no contrary evidence exists. Same company as harry-s-inc: the two "
                 "rows should merge", ec="formd_adjudicated", conf="medium", cite=SEC("hf-global-inc")))
L.append(cls("hf-global-inc", note=HARRYS_NOTE, **HARRYS))

# ---------------------------------------------------------------- headspin (membership open)
HS_TC = PK("headspin", "PE firm PartnerOne paid $28M")
L.append(verdict("headspin", "member",
                 "TechCrunch (2024-07-18): 'Prior to the allegations of fraud, the company had raised $117 million from "
                 "investors including Google Ventures, ICONIQ Capital, Dell Technologies Ventures, Battery Ventures, "
                 "Felicis and Tiger Global', and its 2024-07-12 report says the SEC and DOJ charged the founder with "
                 "lying to Tiger and others: the firm invested in the private company", ec="web", conf="medium",
                 cite=HS_TC))
L.append(cls("headspin", status="acquired", rng="below_1b", stage="undetermined",
             country="US", city="Palo Alto", focus="DevTools & APIs",
             note="Mobile app performance testing, Palo Alto. Tiger is named among the investors of the $117M the "
                  "company raised before its founder's fraud case (TechCrunch); the round it entered is not on "
                  "record, so the stage is undetermined. PartnerOne bought HeadSpin for about $28M in July 2024 "
                  "(TechCrunch): acquired, as the ICONIQ and GV rows read (the Battery, EQT and Felicis rows still read "
                  "private).",
             rounds=[]))

# ---------------------------------------------------------------- heavy-ai (recall seed confirmed)
HV_W = W("HEAVY.AI")
L.append(cls("heavy-ai", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=HV_W, stage_conf="high", entry_date="2018-10",
             country="US", city="San Francisco", focus="Data Infrastructure",
             note="GPU-accelerated analytics database (formerly MapD, then OmniSci), San Francisco. Tiger led the $55M "
                  "Series C of October 2018 with existing investors In-Q-Tel, NEA, Vanedge, Nvidia and Verizon "
                  "Ventures (Wikipedia): Growth. No later round or sale found.",
             rounds=[rnd("2018-10", "Series C", 55_000_000, "Tiger Global Management", True, HV_W, "press")]))

# ---------------------------------------------------------------- hello-english (recall seed confirmed)
HE_W = W("Hello English")
HE_BY = PK("hello-english", "", "recall")
L.append(cls("hello-english", status="unknown", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=HE_W, stage_conf="high", entry_date="2015-03",
             country="IN", country_src="web_verified", country_cite=HE_W, city="Gurugram",
             focus="Consumer & Marketplaces",
             note="English-learning app by CultureAlley, Gurugram. Tiger led the $6.5M Series A of March 2015 "
                  "(Wikipedia): the firm's entry. Entrackr reported in November 2021 that Byju's was set to acquire "
                  "the company; no closing or later news was found (Bing, " + CHECK + "), so the current state is "
                  "unknown.",
             rounds=[rnd("2015-03", "Series A", 6_500_000, "Tiger Global Management", True, HE_W, "press")]))

# ---------------------------------------------------------------- hibob (recall seed replaced)
L.append(verdict("hibob", "not_member",
                 "The recall headline (Business Insider, 2024-02-13) calls Pento, the payroll startup HiBob bought, "
                 "Tiger Global-backed; HiBob is the acquirer and no record ties Tiger Global to a HiBob round (HiBob "
                 "shares received for Pento would be sale consideration, not an entry)", ec="web", conf="high",
                 cite=PK("hibob", "", "recall")))

# ---------------------------------------------------------------- highspot (membership open)
HI_Y = PK("highspot", "Yahoo Finance | Seattle Mints a New Unicorn")
HI_M = PK("highspot", "Seismic completes Highspot merger")
L.append(verdict("highspot", "member",
                 "Bloomberg via Yahoo Finance (2021-02-22): 'The funding round was led by Tiger Global and included an "
                 "investment from Bain & Co.', the $200M Series E at $2.3B of the private company",
                 ec="web", conf="high", cite=HI_Y))
L.append(cls("highspot", status="acquired", rng="below_1b", clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=HI_Y, stage_conf="high", entry_date="2021-02-22",
             city="Seattle", focus="SaaS",
             note="Sales enablement software, Seattle. Tiger led the $200M Series E at $2.3B (February 2021), its "
                  "first round: Growth. Highspot merged into Seismic, which completed the deal in August 2026 (GeekWire "
                  "via MSN, 2026-08-18): acquired, as the ICONIQ row reads.",
             rounds=[rnd("2021-02-22", "Series E", 200_000_000, "Tiger Global", True, HI_Y, "press"),
                     rnd("2026-08-18", "merger into Seismic completed", None, None, None, HI_M, "press")]))

# ---------------------------------------------------------------- hike (recall seed confirmed)
HK_C = PK("hike", "inc42.com | Hike Raises $65 Mn In Series C")
HK_END = NEWS("hike", "Hike, once a unicorn, shuts down")
L.append(cls("hike", status="defunct", rng="below_1b", flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=HK_C, stage_conf="high", entry_date="2014-08-26",
             country="IN", country_src="web_verified", country_cite=W("Hike Messenger"), city="New Delhi",
             focus="Consumer & Marketplaces",
             note="Hike, the Indian messaging app that later became a real-money gaming company (Rush), New Delhi. The "
                  "pre-filled Japan and 'acquired' came from a wrong name match. Tiger led the $65M Series C of August "
                  "2014 with Bharti SoftBank (inc42; Reuters), its first round: Growth. After India's real-money gaming "
                  "ban, founder Kavin Bharti Mittal shut the company down in September 2025 (Yahoo Finance, "
                  "2025-09-13): defunct.",
             rounds=[rnd("2014-08-26", "Series C", 65_000_000, "Tiger Global", True, HK_C, "press"),
                     rnd("2025-09-13", "shutdown", None, None, None, HK_END, "press")]))

# ---------------------------------------------------------------- hinge-health (recall seed confirmed)
HH_D = NEWS("hinge-health", "Hinge Health Valued at $3 Billion by Tiger Global, Coatue")
HH_DRS = PK("hinge-health", "PIP 15-35", "sec")
hh_usd, hh_asof, hh_cite = SIB("hinge-health", "coatue")
L.append(cls("hinge-health", rng="1b_plus", usd=hh_usd, val_src="web_verified", val_cite=hh_cite, asof=hh_asof,
             extra=WV, flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=HH_D, stage_conf="high", entry_date="2021-01-05",
             country="US", city="San Francisco", focus="Healthcare & Bio",
             note="Digital musculoskeletal care, San Francisco (NYSE: HNGE since May 2025). Tiger and Coatue led the "
                  "$300M Series D at $3B of January 2021 (The Information), and Tiger Global PIP 15-35 LLC bought "
                  "about $200M of the Series E of October 2021 (the IPO filing): Growth. Market cap replaces the SEC "
                  "float: $7.71B (2026-09-25), as the Atomico, Coatue and Insight rows read.",
             rounds=[rnd("2021-01-05", "Series D", 300_000_000, "Tiger Global, Coatue", True, HH_D, "press"),
                     rnd("2021-10", "Series E", 400_000_000, "Coatue, Tiger Global", True, HH_DRS, "filing")]))

# ---------------------------------------------------------------- hive (recall seed confirmed)
HV_BI = PK("hive", "", "recall")
L.append(cls("hive", status="private", rng="below_1b", flags=["model_disputes_source"],
             stage="Series A", stage_src="web_verified", stage_cite=HV_BI, stage_conf="high", entry_date="2021-11-11",
             country="DE", country_src="web_verified", country_cite=HV_BI, city="Berlin",
             focus="Consumer & Marketplaces",
             note="Hive Technologies, e-commerce fulfilment for direct-to-consumer brands, Berlin. The pre-filled "
                  "Russia and 'acquired' came from a wrong name match. Tiger led the $34M (EUR 29M) Series A of "
                  "November 2021 (Business Insider): the firm's entry. The company raised EUR 28.2M more in June 2024 "
                  "(EU-Startups) and operates. The 8VC, General Catalyst (Hive AI) and Y Combinator rows named Hive are "
                  "other companies.",
             rounds=[rnd("2021-11-11", "Series A", 34_000_000, "Tiger Global", True, HV_BI, "press")]))

# ---------------------------------------------------------------- hologram (recall seed confirmed)
HO_B = PK("hologram", "", "recall")
L.append(cls("hologram", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": HO_B, "valuation_asof": CHECK},
             stage="Growth", stage_src="web_verified", stage_cite=HO_B, stage_conf="high", entry_date="2021-08-10",
             country="US", city="Chicago", focus="Data Infrastructure",
             note="Cellular connectivity platform for IoT devices, Chicago. Tiger led the $65M Series B of August 2021 "
                  "(IoT For All; Built In Chicago), its first round: Growth. Momentum check " + CHECK + ": the Bing "
                  "search found no later round.",
             rounds=[rnd("2021-08-10", "Series B", 65_000_000, "Tiger Global", True, HO_B, "company")]))

# ---------------------------------------------------------------- homeaway-inc (seeded filing row)
HA_X = PK("homeaway-inc", "PIP V", "sec")
L.append(verdict("homeaway-inc", "member",
                 "HomeAway's 2011 S-1 exhibits: Tiger Global Private Investment Partners V signs the amended voting "
                 "agreement as an investor, and the stock repurchase agreement of 2010-07-30 buys back Series A and "
                 "Series B preferred from PIP V and from Tiger Global, L.P., II and Master Fund: preferred held in the "
                 "private company before its June 2011 IPO, with a private-equity desk fund named",
                 ec="fund_filing", conf="high", cite=HA_X))
L.append(cls("homeaway-inc", rng="below_1b",
             stage="Growth", stage_src="model", stage_conf="medium",
             country="US", city="Austin", focus="Consumer & Marketplaces",
             note="Vacation rental marketplace, Austin; listed in June 2011, bought by Expedia in 2015 (acquired). "
                  "Tiger's funds held Series A and B preferred by July 2010 (the S-1 exhibit). PIP V is a 2008 vehicle, "
                  "so its shares came in 2008 or later, after the company's first rounds, through a later private "
                  "round or secondary purchases, Growth either way (model, medium); the date is not on record.",
             rounds=[rnd("2010-07-30", "stock repurchase from Tiger funds (Series A and B preferred)", None, None, True,
                         HA_X, "filing")]))

if __name__ == "__main__":
    jl.write("batch-006c", L, record=os.environ.get("DRY") != "1")
