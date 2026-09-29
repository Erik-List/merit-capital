#!/usr/bin/env python3
"""PRO-167 grind, queue batch 5, chunk b (rows 16-30). Judge b5.

Evidence: the judge view (show.py --batch 5), the evidence pack, the Bing and Google candidate caches, Bing
lookups run with NQ_TAG=b5 (bq.py), sibling books' records, and pages fetched and read in this pass (the
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

# ---------------------------------------------------------------- eliyan (recall seed confirmed)
EL_B = PK("eliyan", "Yahoo Finance | Chiplet Interconnect Pioneer")
EL_C = NEWS("eliyan", "valued at $1bn following $145m Series C")
L.append(cls("eliyan", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=EL_C,
             asof="2026-07-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=EL_B, stage_conf="high", entry_date="2024-03-25",
             country="US", city="Santa Clara", focus="Industrial & Robotics",
             note="Chiplet and optical interconnect semiconductors, Santa Clara. Samsung Catalyst Fund and Tiger "
                  "Global co-led the $60M Series B of March 2024 (the company's release), the firm's entry after a "
                  "Series A it was not in: Growth. The $145M Series C of July 2026, led by Seligman Ventures, valued "
                  "the company at $1B (Datacenter Dynamics, 2026-07-30), exactly at the band edge.",
             rounds=[rnd("2024-03-25", "Series B", 60_000_000, "Samsung Catalyst Fund, Tiger Global", True, EL_B,
                         "press"),
                     rnd("2026-07-29", "Series C", 145_000_000, "Seligman Ventures", None, EL_C, "press")]))

# ---------------------------------------------------------------- embark-technology-inc (seeded filing row)
EM_8K = PK("embark-technology-inc", "Embark Holder", "sec")
EM_C = NEWS("embark-technology-inc", "Self-Driving Startup Embark Raises $70 Million")
EM_SALE = NEWS("embark-technology-inc", "EMBK Stock Alert")
L.append(verdict("embark-technology-inc", "member",
                 "Tiger Global Private Investment Partners XI signs the de-SPAC registration rights agreement as an "
                 "'Embark Holder', a former stockholder of the private Embark Trucks (closing 8-K, November 2021): a "
                 "private-equity desk fund held the company before its listing", ec="fund_filing", conf="high",
                 cite=EM_8K))
L.append(cls("embark-technology-inc", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EM_C, stage_conf="medium", entry_date="2019-09-25",
             country="US", city="San Francisco", focus="Industrial & Robotics",
             note="Autonomous trucking software, San Francisco. Tiger's entry is the $70M Series C of September 2019 "
                  "(Forbes, 2019-09-25), after Sequoia's Series B: Growth. Listed through the Northern Genesis SPAC in "
                  "November 2021, then sold to Applied Intuition for $2.88 a share in 2023 (Business Wire, 2023-05-24), "
                  "so acquired with no figure.",
             rounds=[rnd("2019-09-25", "Series C", 70_000_000, "Tiger Global", True, EM_C, "press"),
                     rnd("2021-11", "de-SPAC holder", None, None, True, EM_8K, "filing")]))

# ---------------------------------------------------------------- emerge (recall seed confirmed)
EG_PR = PK("emerge", "Yahoo Finance | Emerge Raises $130 Million")
L.append(cls("emerge", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EG_PR, stage_conf="high", entry_date="2021-09-23",
             city="Scottsdale", focus="Consumer & Marketplaces",
             note="Digital freight procurement marketplace, Scottsdale (Arizona). 9Yards Capital, Tiger Global and "
                  "Spruce House provided the $130M Series B of September 2021 (the company's release; Yahoo Finance "
                  "calls it the Series B), after a $20M Series A led by NewRoad Capital Partners in February 2020 "
                  "without Tiger: Growth. Still operating; no later priced round found.",
             rounds=[rnd("2020-02-03", "Series A", 20_000_000, "NewRoad Capital Partners", False,
                         NEWS("emerge", "Raises $20 Million in Series A Funding"), "press"),
                     rnd("2021-09-23", "Series B", 130_000_000, "9Yards Capital, Tiger Global, Spruce House", True,
                         EG_PR, "press")]))

# ---------------------------------------------------------------- emesent (membership open)
ES_SU = PK("emesent", "sUAS News")
L.append(verdict("emesent", "member",
                 "sUAS News (2022-02-20): 'The raise was led by Australian investment firm Perennial Partners, with "
                 "significant funding from international investors Tiger Global and TELUS Ventures', the $32M "
                 "Series A of the CSIRO spin-out, with Tiger partner Griffin Schroeder quoted",
                 ec="web", conf="high", cite=ES_SU))
L.append(cls("emesent", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=ES_SU, stage_conf="high", entry_date="2022-02-17",
             country="AU", country_src="web_verified", country_cite=ES_SU, city="Brisbane",
             focus="Industrial & Robotics",
             note="Autonomous drone and lidar mapping, Brisbane (a CSIRO spin-out). Tiger joined the A$32M Series A "
                  "led by Perennial Partners in February 2022 (AFR, sUAS News): the firm's entry.",
             rounds=[rnd("2022-02-17", "Series A", None, "Perennial Partners", True, ES_SU, "press")]))

# ---------------------------------------------------------------- encharge (recall seed confirmed)
EN_BI = PK("encharge", "Business Insider | AI chip startup EnCharge")
L.append(cls("encharge", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EN_BI, stage_conf="high", entry_date="2025-02-13",
             country="US", city="Santa Clara", focus="Industrial & Robotics",
             note="Analog in-memory AI inference chips, Santa Clara. Tiger led the $100M Series B of February 2025 "
                  "(Business Insider, TechCrunch), the firm's first round: Growth. A Bing News check on " + CHECK +
                  " for a later valuation found no priced round at $1B or more.",
             rounds=[rnd("2025-02-13", "Series B", 100_000_000, "Tiger Global", True, EN_BI, "press")]))

# ---------------------------------------------------------------- engflow (recall seed confirmed)
EF_BW = PK("engflow", "Business Wire | EngFlow Announces $18 Million Series A")
EF_TC = PK("engflow", "TechCrunch | With $18M in new funding")
EF_25 = PK("engflow", "Yahoo Finance | EngFlow Acquires")
L.append(cls("engflow", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": EF_25, "valuation_asof": CHECK},
             stage="Series A", stage_src="web_verified", stage_cite=EF_BW, stage_conf="high", entry_date="2022-11-15",
             country="US", focus="DevTools & APIs", flags=["city_unknown"],
             note="Remote build execution for Bazel and CMake. The $18M Series A of November 2022 (the company's "
                  "release) was led by a16z with Tiger Global and firstminute (TechCrunch, which also names the "
                  "earlier $3.7M seed, a16z-led and without Tiger): Tiger's entry is the Series A. Momentum check "
                  + CHECK + ": no later round (its 2025 release on buying tipi.build still names only those three "
                  "investors). City not placed: releases carry Aurora (Colorado) and Zurich datelines and no source "
                  "states a head office.",
             rounds=[rnd("2022-11-15", "Series A", 18_000_000, "Andreessen Horowitz", True, EF_TC, "press")]))

# ---------------------------------------------------------------- equipmentshare (recall seed: PIP 14 LLC)
EQ_IRA = PK("equipmentshare", "Tiger Global PIP 14 LLC", "sec")
EQ_230 = NEWS("equipmentshare", "EquipmentShare Completes $230M Funding Round")
eq_usd, eq_asof, eq_cite = SIB("equipmentshare", "insight-partners")
L.append(cls("equipmentshare", status="public", rng="1b_plus", usd=eq_usd, val_src="web_verified", val_cite=eq_cite,
             asof=eq_asof, extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=EQ_230, stage_conf="medium", entry_date="2021-07-15",
             country="US", city="Columbia", focus="Industrial & Robotics",
             note="Construction equipment rental and telematics, Columbia (Missouri); Nasdaq: EQPT since January "
                  "2026. The investors' rights agreement in the IPO filing defines 'Tiger' as Tiger Global PIP 14 LLC, "
                  "a 2021 vehicle, which places the entry at the $230M round of July 2021 (the company's release, "
                  "returned by the Bing search for the company with Tiger Global): Growth. Market cap $4.40B on "
                  "2026-09-25 (StockAnalysis), aligned with the Insight row.",
             rounds=[rnd("2021-07-15", "unnamed ($230M)", 230_000_000, None, True, EQ_230, "company"),
                     rnd(None, "investors' rights agreement ('Tiger')", None, None, True, EQ_IRA, "filing")]))

# ---------------------------------------------------------------- etsy-inc (seeded filing row)
ET_DRS = PK("etsy-inc", "PIP VII", "sec")
et_usd, et_asof, et_cite = SIB("etsy-inc", "union-square-ventures")
L.append(verdict("etsy-inc", "member",
                 "Etsy's IPO draft registration statement: on 1 April 2014 Etsy sold 6.6 million common shares to "
                 "Tiger Global Private Investment Partners VII for about $35M, a year before its April 2015 listing, "
                 "and PIP VII and VIII held more than 5% pre-IPO", ec="fund_filing", conf="high", cite=ET_DRS))
L.append(cls("etsy-inc", rng="1b_plus", usd=et_usd, val_src="web_verified", val_cite=et_cite, asof=et_asof,
             extra=WV, flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=ET_DRS, stage_conf="high", entry_date="2014-04-01",
             country="US", city="New York", focus="Consumer & Marketplaces",
             note="Handmade and vintage marketplace, Brooklyn (New York; the municipality, as the USV row has it, "
                  "while the Accel row reads Brooklyn). Tiger's PIP VII bought newly issued common shares in April "
                  "2014 (the draft registration statement), a late private round: Growth. The pre-filled figure was "
                  "the SEC float; replaced by the market cap the USV row carries ($7.02B, 2026-09-04).",
             rounds=[rnd("2014-04-01", "common stock purchase", 35_000_000, None, True, ET_DRS, "filing")]))

# ---------------------------------------------------------------- eventbrite (recall seed confirmed)
EB_W = W("Eventbrite")
EB_SALE = NEWS("eventbrite", "Bending Spoons Paid $3.3 Billion")
EB_DEF = NEWS("eventbrite", "Eventbrite Enters into Definitive Agreement")
L.append(cls("eventbrite", status="acquired", rng="below_1b", flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=EB_W, stage_conf="high", entry_date="2011-03-18",
             city="San Francisco", focus="Consumer & Marketplaces",
             note="Ticketing platform, San Francisco. Tiger led the $50M Series E of March 2011 (Wikipedia) and the "
                  "$60M growth round of April 2013; PIP VI and VII sign the IPO investors' rights agreement: Growth. "
                  "The pre-filled status was public: Eventbrite agreed on 2025-12-01 to be bought by Bending Spoons "
                  "for $4.50 a share (about $500M), shareholders approved in February 2026, and Forbes (2026-07-06) "
                  "reports Bending Spoons paid for AOL, Vimeo and Eventbrite, so acquired with no figure (the Sequoia "
                  "row still reads public).",
             rounds=[rnd("2011-03-18", "Series E", 50_000_000, "Tiger Global", True, EB_W, "press"),
                     rnd("2025-12-01", "definitive agreement to be acquired (Bending Spoons)", None, None, None,
                         EB_DEF, "press")]))

# ---------------------------------------------------------------- ever-body (recall seed confirmed)
EV_B = PK("ever-body", "", "recall")
L.append(cls("ever-body", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EV_B, stage_conf="high", entry_date="2021-05-25",
             country="US", city="New York", focus="Healthcare & Bio",
             note="Cosmetic dermatology clinics, New York. Tiger led the $38M Series B of May 2021 (citybiz), after a "
                  "$17M Series A in 2019 without Tiger: Growth. A $55.5M Series C followed in June 2022; a new CEO "
                  "was named in 2024 and the company still operates.",
             rounds=[rnd("2021-05-25", "Series B", 38_000_000, "Tiger Global Management", True, EV_B, "press"),
                     rnd("2022-06-09", "Series C", 55_500_000, None, None,
                         NEWS("ever-body", "ANNOUNCES $55.5M IN SERIES C"), "company")]))

# ---------------------------------------------------------------- exclusively-in-inc (membership open)
EX_MN = NEWS("exclusively-in-inc", "Snapdeal acquires online fashion portal")
L.append(verdict("exclusively-in-inc", "member",
                 "MediaNama (2015-02-18): Exclusively 'raised $16 million in a Series-B funding round led by Tiger "
                 "Global Management, with additional capital from existing investors Accel Partners India and "
                 "Helion Venture Partners in 2011'; the May 2011 Form D ($16.5M) names Lee Fixel, in his Tiger "
                 "tenure, as director beside Accel's and Helion's partners", ec="web", conf="high", cite=EX_MN))
L.append(cls("exclusively-in-inc", status="acquired", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EX_MN, stage_conf="high",
             flags=["stage_disputes_band", "model_disputes_source"],
             country="IN", country_src="web_verified", country_cite=EX_MN, city="New Delhi",
             focus="Consumer & Marketplaces",
             note="Online luxury fashion retailer Exclusively.in, founded by Sunjay Guleria, offices in New Delhi and "
                  "New York (MediaNama). Tiger led its 2011 Series B of about $16M (the Form D's $16.5M sold from "
                  "2011-05-12): Growth, which disputes the Form D band's Series A. The Delaware parent files from New "
                  "York, but the business is Indian, so IN (the Accel row reads US). Myntra bought a stake and sold "
                  "it back in 2013; Snapdeal acquired the company in February 2015: acquired.",
             rounds=[rnd("2011-05-12", "Series B", 16_504_349, "Tiger Global Management", True, EX_MN, "press")]))

# ---------------------------------------------------------------- fable (recall seed confirmed)
FB_PR = PK("fable", "", "recall")
L.append(cls("fable", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=FB_PR, stage_conf="high", entry_date="2021-12-16",
             country="US", city="Palo Alto", city_src="web_verified", focus="Consumer & Marketplaces",
             note="Fable, the social reading and book club app founded by Padmasree Warrior, Palo Alto (the release's "
                  "dateline). Tiger led the $20M Series A of December 2021, after a $7.25M seed led by Redpoint "
                  "(the company's release): Tiger's entry is the Series A. Same company as the Redpoint row; the "
                  "Greylock and Y Combinator rows named Fable are other companies.",
             rounds=[rnd("2021-12-16", "Series A", 20_000_000, "Tiger Global", True, FB_PR, "company")]))

# ---------------------------------------------------------------- facilio (recall seed confirmed)
FC_PR = PK("facilio", "irblog.prnewswire.com | Facilio Raises USD 6.4 Million")
FC_B = NEWS("facilio", "Facilio raises $35mn Series B financing led by Dragoneer")
L.append(cls("facilio", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=FC_PR, stage_conf="high", entry_date="2018-12-05",
             country="US", city="New York", focus="SaaS",
             note="Property operations and maintenance software (Facilio Inc.), New York with engineering in "
                  "Chennai; its 2025-2026 releases carry New York datelines, as the Accel row has it. Tiger and "
                  "existing investor Accel led the $6.4M Series A of December 2018 (the company's release): Tiger's "
                  "entry. Dragoneer led the $35M Series B in February 2022.",
             rounds=[rnd("2018-12-05", "Series A", 6_400_000, "Tiger Global, Accel", True, FC_PR, "company"),
                     rnd("2022-02-22", "Series B", 35_000_000, "Dragoneer", None, FC_B, "press")]))

# ---------------------------------------------------------------- factorial (membership open)
FA_FW = PK("factorial", "FrenchWeb")
FA_EP = NEWS("factorial", "Factorial busca ser la")
fa_usd, fa_asof, fa_cite = SIB("factorial", "atomico")
L.append(verdict("factorial", "member",
                 "FrenchWeb (2021-09-06): 'Factorial lève 80 millions de dollars auprès de Tiger Global', the $80M "
                 "Series B of September 2021 (Business Wire names the Series B; Point Nine's post names it as led "
                 "by Tiger Global)", ec="web", conf="high", cite=FA_FW))
L.append(cls("factorial", status="private", rng="1b_plus", usd=fa_usd, val_src="web_verified", val_cite=fa_cite,
             asof=fa_asof, extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=FA_FW, stage_conf="high", entry_date="2021-09-06",
             country="ES", country_src="web_verified", country_cite=FA_EP, city="Barcelona", focus="SaaS",
             note="HR and business management software for small companies, Barcelona. Tiger led the $80M Series B "
                  "of September 2021, after the CRV-led Series A and the Creandum and Point Nine seed: Growth. "
                  "Atomico and Tiger led the $120M Series C at $1B (October 2022); General Catalyst led the $150M "
                  "Series D at $2.5B in June 2026 (Tech.eu), the mark the sibling rows carry.",
             rounds=[rnd("2021-09-06", "Series B", 80_000_000, "Tiger Global", True, FA_FW, "press"),
                     rnd("2026-06-03", "Series D", 150_000_000, "General Catalyst", None, fa_cite, "press")]))

# ---------------------------------------------------------------- fairmoney (recall seed confirmed)
FM_TC = PK("fairmoney", "TechCrunch | Tiger Global leads $42M Series B")
FM_24 = NEWS("fairmoney", "in talks to buy Umba")
L.append(cls("fairmoney", status="private", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": FM_24, "valuation_asof": CHECK},
             stage="Growth", stage_src="web_verified", stage_cite=FM_TC, stage_conf="high", entry_date="2021-07-01",
             country="FR", country_src="web_verified", country_cite=FM_24, city="Paris", focus="Fintech & Payments",
             note="Credit-led digital bank for Nigeria (and India), 'based in Lagos and headquartered in Paris' "
                  "(TechCrunch, 2024-02-20). Tiger led the $42M Series B of July 2021 (TechCrunch), after a EUR 10M "
                  "round in 2019 without Tiger: Growth. Momentum check " + CHECK + ": the Bing search for its "
                  "valuation found no priced round at $1B or more.",
             rounds=[rnd("2021-07-01", "Series B", 42_000_000, "Tiger Global", True, FM_TC, "press")]))

if __name__ == "__main__":
    jl.write("batch-005b", L, record=os.environ.get("DRY") != "1")
