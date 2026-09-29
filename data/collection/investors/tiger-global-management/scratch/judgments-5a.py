#!/usr/bin/env python3
"""PRO-167 grind, queue batch 5, chunk a (rows 1-15). Judge b5.

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

# pages fetched and read in this pass
DDL_CAP = "https://stockanalysis.com/stocks/ddl/market-cap/"      # $471.91M as of 2026-09-29
DLO_CAP = "https://stockanalysis.com/stocks/dlo/market-cap/"      # $3.98B as of 2026-09-29

# ---------------------------------------------------------------- dingdong-cayman-ltd (seeded filing row)
DD_DRS = PK("dingdong-cayman-ltd", "Internet Fund V", "sec")
L.append(verdict("dingdong-cayman-ltd", "member",
                 "Dingdong's 2021 IPO draft registration statement records Series C1 and Series D preferred held by "
                 "Internet Fund V Pte. Ltd., the Singapore vehicle advised by Tiger Global Singapore (a private-equity "
                 "desk vehicle, D2), bought while the company was private; the later 13G filings are the listed holding",
                 ec="fund_filing", conf="high", cite=DD_DRS))
L.append(cls("dingdong-cayman-ltd", status="public", rng="below_1b", usd=471_910_000, val_src="web_verified",
             val_cite=DDL_CAP, asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=DD_DRS, stage_conf="high",
             country="CN", country_src="web_verified", country_cite=DD_DRS, city="Shanghai",
             focus="Consumer & Marketplaces",
             note="Dingdong Maicai, online grocery delivery, Shanghai (NYSE: DDL since June 2021). Tiger's Singapore "
                  "vehicle Internet Fund V held Series C1 and Series D preferred before the IPO (the draft registration "
                  "statement), so the entry is the Series C1, a Growth round; the filing extract read does not date "
                  "the C1 purchase. Market cap $471.91M on 2026-09-29 (StockAnalysis), below $1B.",
             rounds=[rnd(None, "Series C1", None, None, True, DD_DRS, "filing"),
                     rnd("2021-04", "Series D", None, None, True, DD_DRS, "filing")]))

# ---------------------------------------------------------------- dispatchhealth (membership open)
DH_Y = PK("dispatchhealth", "valued at over $1.7 bln")
DH_R = PK("dispatchhealth", "valued at over $1.7 billion")
L.append(verdict("dispatchhealth", "member",
                 "Reuters via Yahoo Finance (2021-03-03): 'The Series D funding round, led by Tiger Global Management, "
                 "brings the company's total funding to over $417 million', a private round led by the firm",
                 ec="web", conf="high", cite=DH_Y))
L.append(cls("dispatchhealth", status="private", rng="1b_plus", usd=1_700_000_000, val_src="web_verified",
             val_cite=DH_R, asof="2021-03-03", extra=WV, flags=["stale"],
             stage="Growth", stage_src="web_verified", stage_cite=DH_Y, stage_conf="high", entry_date="2021-03-03",
             country="US", city="Denver", focus="Healthcare & Bio",
             note="In-home acute care provider, Denver. Tiger led the $200M Series D at a valuation above $1.7B "
                  "(Reuters, 2021-03-03), the firm's entry (Growth). No later priced round found; the 2021 mark is "
                  "older than 24 months, so it stands flagged stale.",
             rounds=[rnd("2021-03-03", "Series D", 200_000_000, "Tiger Global Management", True, DH_Y, "press")]))

# ---------------------------------------------------------------- divvy-homes (recall seed confirmed)
DV_C = PK("divvy-homes", "secures $110M Series C")
DV_SALE = NEWS("divvy-homes", "Portfolio & Platform For About")
L.append(cls("divvy-homes", status="acquired", rng="below_1b", clear=["needs_web_value"],
             stage="Growth", stage_src="web_verified", stage_cite=DV_C, stage_conf="medium", entry_date="2021-02-02",
             country="US", city="San Francisco", focus="Fintech & Payments",
             note="Rent-to-own home financing, San Francisco. Tiger's entry is the $110M Series C of February 2021 "
                  "(TechCrunch via Yahoo, returned by the Bing search for the company with Tiger Global; a16z led the "
                  "earlier rounds), a Growth round; the $200M Series D at about $2B followed in August 2021. A "
                  "Brookfield private real estate fund agreed in January 2025 to buy Divvy's property portfolio and "
                  "platform for about $1B (Pulse 2.0, 2025-01-21), reported as a fire sale: acquired, aligned with "
                  "the a16z row.",
             rounds=[rnd("2021-02-02", "Series C", 110_000_000, None, True, DV_C, "press"),
                     rnd("2025-01-21", "sale of portfolio and platform to Brookfield", None, None, None, DV_SALE,
                         "press")]))

# ---------------------------------------------------------------- dlocal (recall seed: PIP 14-11 LLC)
DL_BB = NEWS("dlocal", "Valued at $5 Billion After Alkeon")
DL_F1 = PK("dlocal", "PIP 14-11", "sec")
L.append(cls("dlocal", status="public", rng="1b_plus", usd=3_980_000_000, val_src="web_verified",
             val_cite=DLO_CAP, asof="2026-09-29", extra=WV,
             stage="Growth", stage_src="web_verified", stage_cite=DL_BB, stage_conf="high", entry_date="2021-04-02",
             country="UY", country_src="web_verified", country_cite=DL_BB, city="Montevideo",
             focus="Fintech & Payments",
             note="Cross-border payments for emerging markets, Montevideo (Nasdaq: DLO since June 2021). Tiger "
                  "invested with Alkeon in the April 2021 pre-IPO round that valued the company at $5B (Bloomberg, "
                  "2021-04-02), a Growth entry; Tiger Global PIP 14-11 LLC signs the IPO registration rights "
                  "agreement as a pre-IPO holder. Market cap $3.98B on 2026-09-29 (StockAnalysis).",
             rounds=[rnd("2021-04-02", "pre-IPO round at $5B", None, None, True, DL_BB, "press"),
                     rnd("2021-05-20", "pre-IPO holder (registration rights agreement)", None, None, True, DL_F1,
                         "filing")]))

# ---------------------------------------------------------------- listed-stock rows (T3)
L.append(verdict("dolby-laboratories-inc", "not_member",
                 T3 + ": Dolby listed on the NYSE in February 2005 and Tiger's 13G filings date from 2005-2006",
                 ec="fund_filing", conf="high", cite=SEC("dolby-laboratories-inc", "edgar")))
L.append(verdict("dominos-pizza-inc", "not_member",
                 T3 + ": Domino's has been listed since 2004; Tiger's 13F lists it 2010-2019 and its 13G dates from "
                      "2017", ec="fund_filing", conf="high", cite=SEC("dominos-pizza-inc", "edgar")))

# ---------------------------------------------------------------- doubleverify (seeded filing row)
DVF = PK("doubleverify-holdings-inc", "Series A preferred purchase", "sec")
dv_usd, dv_asof, dv_cite = SIB("doubleverify-holdings-inc", "ivp")
L.append(verdict("doubleverify-holdings-inc", "member",
                 "DoubleVerify's IPO draft registration statement records the October 2020 purchase of about $350M "
                 "of preferred stock by an investor group led by Tiger Global Management, closed 18 November 2020 "
                 "while the company was private (a Providence Equity portfolio company); the filing names no "
                 "public-desk vehicle, so the home desk (D2)", ec="fund_filing", conf="high", cite=DVF))
L.append(cls("doubleverify-holdings-inc", rng="1b_plus", usd=dv_usd, val_src="web_verified", val_cite=dv_cite,
             asof=dv_asof, extra=WV, flags=["model_disputes_source"],
             stage="Growth", stage_src="web_verified", stage_cite=DVF, stage_conf="high", entry_date="2020-11-18",
             country="US", city="New York", focus="Media, Gaming & Advertising",
             note="Ad verification and measurement, New York (NYSE: DV since April 2021). Tiger led the $350M "
                  "pre-IPO investment of October 2020 (closed 2020-11-18) in the Providence-owned company; the "
                  "security was a newly created 'Series A' preferred, but the transaction is a pre-IPO growth "
                  "investment, so Growth (D12). The pre-filled figure was the SEC float; replaced by the market cap "
                  "the IVP row carries ($2.08B, 2026-09-25, StockAnalysis), same band.",
             rounds=[rnd("2020-10-27", "pre-IPO preferred (styled Series A)", 350_000_000,
                         "Tiger Global Management", True, DVF, "filing")]))

# ---------------------------------------------------------------- dream11 (recall seed confirmed)
DR_FE = NEWS("dream11", "Dream11 raises fresh $225 million")
DR_BT = NEWS("dream11", "Dream11 raises $400 million in funding round")
DR_BAN = NEWS("dream11", "Dream11 to shut real-money gaming arm")
L.append(cls("dream11", status="private", rng="below_1b", clear=["needs_web_value"],
             extra={"valuation_range_source": "web_verified", "valuation_citation": DR_BAN},
             stage="Growth", stage_src="web_verified", stage_cite=DR_FE, stage_conf="high", entry_date="2020-09-14",
             country="IN", country_src="web_verified", country_cite=W("Dream11"), city="Mumbai",
             focus="Media, Gaming & Advertising",
             note="Fantasy sports platform (Dream Sports), Mumbai. Tiger and TPG led the $225M round of September "
                  "2020 at about $2.5B (Financial Express, 2020-09-14), the firm's first round after reported talks "
                  "in January 2020: a Growth entry. Later rounds: $400M at nearly $5B (March 2021) and $840M at $8B "
                  "(November 2021, Entrackr and VCCircle headlines). Collapse evidence: India's Online Gaming Act "
                  "of August 2025 banned real-money games and Dream11 shut its real-money business, its core revenue "
                  "(Business Today, 2025-08-21), then pivoted to a sports engagement platform; the stale 2021 mark "
                  "no longer stands, so below $1B with no figure (agent reading, listed for review).",
             rounds=[rnd("2020-09-14", "unnamed ($225M)", 225_000_000, "Tiger Global, TPG", True, DR_FE, "press"),
                     rnd("2021-03-25", "unnamed ($400M, nearly $5B)", 400_000_000, None, None, DR_BT, "press")]))

# ---------------------------------------------------------------- dukaan (recall seed replaced)
L.append(verdict("dukaan", "not_member",
                 "The only record is Moneycontrol's report (2021-04-20) that Tiger was in talks to back Dukaan; the "
                 "round that closed, the $11M pre-Series A of September 2021, was led by 640 Oxford Ventures with "
                 "existing investors (Mint, Moneycontrol, VCCircle), and no record shows Tiger invested: talks are "
                 "not a round", ec="web", conf="medium", cite=PK("dukaan", "", "recall")))

# ---------------------------------------------------------------- dutchie (recall seed confirmed)
DU_Y = PK("dutchie", "Tiger Global-Led Group")
L.append(cls("dutchie", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=DU_Y, stage_conf="high", entry_date="2021-03-16",
             country="US", city="Bend", focus="SaaS",
             note="Cannabis dispensary e-commerce and point-of-sale software, Bend (Oregon). Tiger led the $200M "
                  "Series C at $1.7B (Yahoo Finance, 2021-03-16), after Thrive led the Series B: a Growth entry. D1 "
                  "led the $350M round at $3.75B in October 2021. Below $1B, aligned with the Thrive row, which "
                  "records that peak collapsing in a January 2024 round (rule 10).",
             rounds=[rnd("2021-03-16", "Series C", 200_000_000, "Tiger Global", True, DU_Y, "press")]))

# ---------------------------------------------------------------- more listed-stock rows (T3)
L.append(verdict("e-commerce-china-dangdang-inc", "not_member",
                 T3 + ": Dangdang listed on the NYSE in December 2010 and Tiger's 13G filings date from 2011-2012; "
                      "no prospectus names a Tiger vehicle", ec="fund_filing", conf="high",
                 cite=SEC("e-commerce-china-dangdang-inc", "edgar")))

# ---------------------------------------------------------------- easol (recall seed confirmed)
EA_BW = PK("easol", "Business Wire | Easol raises")
L.append(cls("easol", status="private", rng="below_1b",
             stage="Series A", stage_src="web_verified", stage_cite=EA_BW, stage_conf="high", entry_date="2021-12-08",
             country="GB", country_src="web_verified", country_cite=EA_BW, city="London", focus="SaaS",
             note="Experience-commerce platform for travel and event businesses, London. The $25M Series A of "
                  "December 2021 (the company's release) was backed by Tiger Global and Y Combinator (Business "
                  "Insider, 2021-12-08): Tiger's entry. No later round found.",
             rounds=[rnd("2021-12-08", "Series A", 25_000_000, "Tiger Global", True, EA_BW, "company")]))

# ---------------------------------------------------------------- eatclub-brands (recall seed confirmed)
EC_TIA = BN("eatclub", "Tiger Global leads $40m round")
EC_VCC = BN("eatclub", "Box8 parent raises $40 mn from Tiger Global")
EC_SEC = PK("eatclub-brands", "", "recall")
EC_25 = BN("eatclub", "EatClub to raise $22m")
L.append(cls("eatclub-brands", status="private", rng="below_1b",
             stage="Growth", stage_src="web_verified", stage_cite=EC_TIA, stage_conf="medium", entry_date="2021-11-30",
             country="IN", country_src="web_verified", country_cite=EC_VCC, city="Mumbai",
             focus="Consumer & Marketplaces",
             note="Cloud kitchen operator (BOX8, Mojo Pizza), Mumbai (Poncho Hospitality). Tiger led the $40M round "
                  "of November 2021 (Tech in Asia; KrASIA called it the firm's first cloud kitchen bet), the "
                  "company's first Tiger round after earlier institutional rounds from 2015 on, so Growth though "
                  "the round is not named. Tiger joined the $30M secondary of March 2022 and led a Rs 185 crore "
                  "round in July 2025.",
             rounds=[rnd("2021-11-30", "unnamed ($40M)", 40_000_000, "Tiger Global", True, EC_TIA, "press"),
                     rnd("2022-03-09", "secondary ($30M)", 30_000_000, None, True, EC_SEC, "press"),
                     rnd("2025-07-28", "unnamed (Rs 185 crore)", 22_000_000, "Tiger Global", True, EC_25, "press")]))

L.append(verdict("ecollege-com", "not_member",
                 T3 + ": eCollege listed on Nasdaq in December 1999; Tiger's 13G filings date from 2004-2006",
                 ec="fund_filing", conf="high", cite=SEC("ecollege-com", "edgar")))
L.append(verdict("ehi-car-services-ltd", "not_member",
                 T3 + ": eHi listed on the NYSE in November 2014 and Tiger's 13G filings date from 2015-2018; no "
                      "prospectus names a Tiger vehicle", ec="fund_filing", conf="high",
                 cite=SEC("ehi-car-services-ltd", "edgar")))

if __name__ == "__main__":
    jl.write("batch-005a", L, record=os.environ.get("DRY") != "1")
