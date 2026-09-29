#!/usr/bin/env python3
"""Batch 1, chunk c (rows 31-45): accrue-savings .. alibaba. Run: NQ_TAG=b1 python3 judgments-1c.py
Citations come from judge_lib helpers, the evidence view (evidence-pack.json), a sibling book's recorded
valuation citation (siblings.json) or a URL printed by a search tool; none is typed from memory."""
import json
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
_PK = json.loads((HERE / "evidence-pack.json").read_text())
_SIB = json.loads((HERE / "siblings.json").read_text())
_VENDOR = re.compile(r"sacra\.com|pitchbook|cbinsights|tracxn|crunchbase\.com/organization|dealroom|getlatka|forgeglobal|caplight")


def PK(slug, kind, sub):
    """The URL on the row's evidence-view line of `kind` ('sec' or 'press') that contains `sub`."""
    urls = []
    for x in (_PK.get(slug, {}).get(kind) or []):
        if sub.lower() not in x.lower():
            continue
        if kind == "sec":
            u = x.rsplit(" | ", 1)[-1].strip()
        else:
            m = re.search(r"\|\| URL (\S+)", x)
            u = m.group(1) if m else ""
        if u.startswith("http"):
            urls.append(u)
    urls = list(dict.fromkeys(urls))
    if len(urls) != 1:
        raise SystemExit(f"PK({slug!r}, {kind!r}, {sub!r}) matched {len(urls)}")
    return urls[0]


def SIB(slug, inv):
    """A sibling book's recorded mark for the same company: (usd, asof, citation)."""
    for x in _SIB.get(slug, []):
        if x["investor"] == inv:
            if not x.get("val_cite") or _VENDOR.search(x["val_cite"]) or not x.get("usd"):
                raise SystemExit(f"SIB({slug!r}, {inv!r}): no usable citation")
            return float(x["usd"]), x["asof"], x["val_cite"]
    raise SystemExit(f"SIB({slug!r}, {inv!r}): no sibling row")


def band(usd):
    return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"


def V(slug, inv):
    """Keyword arguments for cls() pinning a sibling's cited mark (rule 10 alignment)."""
    usd, asof, cite = SIB(slug, inv)
    return dict(rng=band(usd), usd=usd, val_src="web_verified", val_cite=cite, asof=asof,
                extra={"valuation_range_source": "web_verified"})


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []

# 31. Accrue Savings
RC = PK("accrue-savings", "sec", "Accrue Savings raised a $25m Series A")
L.append(cls(
    "accrue-savings", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=RC, stage_conf="medium", entry_date="2022-01",
    rounds=[rnd("2022-01", "Series A", 25_000_000, "Tiger Global", True,
                NEWS("accrue-savings", "Recently Closed $25 Million In Series A"), "press")],
    country="US", flags=["city_unknown"], focus="Fintech & Payments",
    note="Accrue Savings, save-now-buy-later wallets for merchants. A third-party Reg CF filing (Flexpay, 2022) "
         "says Tiger Global led its $25M Series A of January 2022 (Pulse 2.0 reports the close, Feb 2022). City "
         "not found in the sources read (Bing News, the filing)."))

# 32. Actifio
WA = W("Actifio")
L.append(cls(
    "actifio", status="acquired", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=WA, stage_conf="high", entry_date="2014-03",
    rounds=[rnd("2014-03-23", "Series E", 100_000_000, "Tiger Global Management", True,
                PK("actifio", "press", "Actifio secures funds led by Tiger Global"), "press")],
    country="US", city="Waltham", focus="Data Infrastructure",
    note="Actifio, copy data management, Waltham. Tiger led the $100M Series E at $1.1B (Mar 2014), its first "
         "round in the company. Acquired by Google, Dec 2020."))

# 33. ActiveCampaign
WAC = W("ActiveCampaign")
BIC = PK("activecampaign", "press", "ActiveCampaign Hits $3B+ Valuation")
L.append(cls(
    "activecampaign", status="private", rng="1b_plus", usd=3_000_000_000, val_src="web_verified", val_cite=BIC,
    asof="2021-04-21", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    stage="Growth", stage_src="web_verified", stage_cite=WAC, stage_conf="high", entry_date="2021-04",
    rounds=[rnd("2021-04-21", "Series C", 240_000_000, "Tiger Global", True, BIC, "press")],
    country="US", city="Chicago", focus="SaaS",
    note="ActiveCampaign, marketing automation, Chicago. Tiger led the $240M Series C (Apr 2021) that valued the "
         "company at more than $3B (figure written as $3.0B); no later priced round is on record, so the mark is "
         "stale."))

# 34. Adalo
AP = PK("adalo", "sec", "Adalo")
L.append(cls(
    "adalo", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=AP, stage_conf="medium", entry_date="2021-05",
    rounds=[rnd("2021-05-17", "Series A", 8_000_000, "Tiger Global", True,
                NEWS("adalo", "No-code app development platform Adalo nabs $8M"), "press")],
    country="US", flags=["city_unknown"], focus="DevTools & APIs",
    note="Adalo (formerly Foundry), no-code app builder. A third-party Reg CF filing (Apphive, 2023) says Tiger "
         "Global led Adalo's $8M Series A, dating it May 2022; VentureBeat reported the $8M raise on 2021-05-17, "
         "so the entry date follows the press. City not found in the sources read."))

# 35. Addition: Lee Fixel's own firm, not a portfolio company
L.append(verdict(
    "addition", "not_member",
    "Addition is Lee Fixel's own investment firm, founded after he left Tiger in 2019 (Wikipedia); a fund manager "
    "is not an operating company (T5), no Tiger fund invested in it, and the recall sentence names only Fixel's "
    "departure",
    ec="web", conf="high", cite=W("Addition (investment firm)")))

# 36. ADKM, Inc. = Harry's (same CIK as the harry-s-inc row)
L.append(verdict(
    "adkm-inc", "member",
    "Director-of-record pattern: Lee Fixel, head of Tiger's private-equity business (in tenure until 2019), is a "
    "director on ADKM, Inc.'s Jan 2014 Form D ($65M sold) beside the founders Andy Katz-Mayfield and Jeff Raider; "
    "ADKM, Inc. is Harry's, the razor company (CIK 1556308 files as Harry's, Inc. from 2017), so the identity "
    "resolves and no contrary evidence exists",
    ec="formd_adjudicated", conf="medium", cite=SEC("adkm-inc", "formd", 0)))
L.append(cls(
    "adkm-inc", status="private", city="New York", focus="Consumer & Marketplaces", flags=["needs_web_value"],
    note="ADKM, Inc. is the name under which Harry's (men's grooming, New York) filed its 2012-2014 Form Ds; the "
         "same CIK 1556308 files as Harry's, Inc. from 2017, so this row and harry-s-inc are one company. Tiger's "
         "entry is the Jan 2014 round (Fixel on the board). Harry's was reported at about $1.7B in later rounds, "
         "but no priced figure is cited here, so the band waits for the web pass."))

# 37. AfterShip
YA = PK("aftership", "press", "Yahoo Finance | E-commerce tracking platform AfterShip")
L.append(cls(
    "aftership", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=YA, stage_conf="high", entry_date="2021-04",
    rounds=[rnd("2021-04-22", "Series B", 66_000_000, "Tiger Global", True, YA, "press")],
    country="HK", country_src="web_verified", country_cite=YA, city="Hong Kong", focus="SaaS",
    note="AfterShip, e-commerce shipment tracking and post-purchase software, Hong Kong. 'The Hong Kong-headquartered "
         "startup ... raised a $66 million Series B led by Tiger Global' (TechCrunch via Yahoo, Apr 2021). No "
         "priced round at $1B or more is on record."))

# 38. AI Rudder
PRN = NEWS("ai-rudder", "AI Rudder Raises US$50 Million in Series B")
BT = PK("ai-rudder", "press", "Voice AI startup AI Rudder raises")
L.append(cls(
    "ai-rudder", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=PRN, stage_conf="high", entry_date="2022-03",
    rounds=[rnd("2022-03-08", "Series B", 50_000_000, "Tiger Global, Coatue", True, BT, "press")],
    country="SG", country_src="web_verified", country_cite=BT, city="Singapore", focus="AI & Applied AI",
    note="AI Rudder, voice AI for call centres, Singapore. Tiger Global and Coatue led the $50M Series B "
         "(Mar 2022); Coatue's book reads the same."))

# 39. ATRenew (AiHuiShou)
DRS = PK("aihuishou-international-co-ltd", "sec", "Series D-2")
L.append(verdict(
    "aihuishou-international-co-ltd", "member",
    "IPO DRS (2021): Internet Fund IV Pte. Ltd., advised by Tiger Global Singapore (a relying adviser, D1; a "
    "private-equity desk vehicle), bought 7,952,405 Series D-2 preferred shares on July 5, 2018 ($101M) and Series E "
    "in June 2019, and Tiger's Pengfei Wang joined the board in July 2018",
    ec="fund_filing", conf="high", cite=DRS))
L.append(cls(
    "aihuishou-international-co-ltd", status="public", rng="below_1b", usd=840_000_000, val_src="web_verified",
    val_cite="https://companiesmarketcap.com/atrenew/marketcap/", asof="2026-09-28",
    extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=DRS, stage_conf="high", entry_date="2018-07",
    rounds=[rnd("2018-07-05", "Series D-2", 101_000_000, "Tiger Global", True, DRS, "filing")],
    country="CN", country_src="web_verified", country_cite=W("ATRenew"), city="Shanghai",
    focus="Consumer & Marketplaces",
    note="ATRenew (NYSE: RERE, formerly AiHuiShou), pre-owned electronics, Shanghai. Tiger led the $150M 2018 round "
         "with JD.com through Internet Fund IV (Series D-2, July 2018). Market cap $0.84B on 2026-09-28 "
         "(companiesmarketcap), below $1B."))

# 40. Airbnb
L.append(cls(
    "airbnb", **V("airbnb", "general-catalyst"),
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015-06",
    rounds=[rnd("2015-06", "Series E", 1_500_000_000, "General Atlantic", True, W("Airbnb"), "press")],
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    note="Airbnb (Nasdaq: ABNB), San Francisco. Tiger's private position is on its investors' rights agreement "
         "(PIP IX, with the public-desk funds as further preferred holders); its round is the $1.5B Series E of "
         "June 2015 led by General Atlantic with Hillhouse and Tiger (Wikipedia names 'Tiger Management', a "
         "slip for Tiger Global). Market cap as in the General Catalyst book (rule 10), replacing the float "
         "figure."))

# 41. Alaiko
BIA = PK("alaiko", "press", "Versand-Plattform Alaiko bekommt 26 Millionen Euro")
DS = PK("alaiko", "press", "Tiger Global investiert in Alaiko")
L.append(cls(
    "alaiko", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=BIA, stage_conf="high", entry_date="2022-01",
    rounds=[rnd("2022-01-18", "Series A", 30_000_000, "Tiger Global", True, DS, "press")],
    country="DE", country_src="web_verified", country_cite=DS, city="Munich", focus="Consumer & Marketplaces",
    note="Alaiko, D2C fulfilment and e-commerce operations, Munich ('Das Münchner Startup', Deutsche Startups). "
         "Tiger Global, Next47 and angels put EUR 26M ($30M) into its Series A (Jan 2022). Merged with "
         "Zenfulfillment in Nov 2024 and continues under that name (Business Insider: 'Alaiko wird zu "
         "Zenfulfillment'), so acquired with a successor note."))

# 42. Aleo
BWA = PK("aleo", "press", "Aleo Raises $200M in Series B")
L.append(cls(
    "aleo", status="private", **V("aleo", "a16z"), flags=["stale"],
    stage="Growth", stage_src="web_verified", stage_cite=BWA, stage_conf="high", entry_date="2022-02",
    rounds=[rnd("2022-02-07", "Series B", 200_000_000, "Kora Management, SoftBank Vision Fund 2", True,
                PK("aleo", "press", "Privacy-focused blockchain project Aleo raises"), "press")],
    country="US", city="San Francisco", focus="Crypto & Web3",
    note="Aleo Systems, privacy blockchain (the operating company, equity round). Tiger joined the $200M Series B "
         "at $1.45B led by Kora and SoftBank Vision Fund 2 (Feb 2022); no later priced equity round is on record, "
         "so the mark (as in the a16z book) is stale."))

# 43. AlexandAlexa.com: a controlling stake
L.append(verdict(
    "alexandalexa-com", "not_member",
    "Control position (T3 addendum): Retail Week (2011-06-27) reports the luxury kidswear e-tailer 'has sold a "
    "majority stake in the business to investment management firm Tiger Global', a control purchase, not a "
    "minority round",
    ec="web", conf="high", cite=PK("alexandalexa-com", "press", "AlexandAlexa.com sells controlling stake"),
    exclusion="control_position"))

# 44. Algorithmiq
TE = NEWS("algorithmiq", "Tiger Global participates in quantum advantage software maker")
QI = NEWS("algorithmiq", "Quantum Scaleup Algorithmiq Raises $15M Series A")
L.append(cls(
    "algorithmiq", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=TE, stage_conf="high", entry_date="2022-02",
    grad="graduated", grad_src="web_verified", grad_cite=QI, grad_conf="high", grad_asof="2023-06-27",
    rounds=[rnd("2022-02-02", "Seed", 4_000_000, None, True, TE, "press"),
            rnd("2023-06-27", "Series A", 15_000_000, None, None, QI, "press")],
    country="FI", country_src="web_verified",
    country_cite=PK("algorithmiq", "press", "Tiger Global-backed Algorithmiq to collaborate"),
    city="Helsinki", focus="Healthcare & Bio",
    note="Algorithmiq, quantum software for drug discovery, Helsinki. Tiger joined its $4M seed (Feb 2022, "
         "Tech.eu); the company raised a $15M Series A in June 2023 (The Quantum Insider), so graduated."))

# 45. Alibaba
GI = PK("alibaba", "sec", "Giant Interactive")
L.append(cls(
    "alibaba", status="public", **V("alibaba", "iconiq-growth"),
    stage="Growth", stage_src="web_verified", stage_cite=GI, stage_conf="high", entry_date="2014-02",
    rounds=[rnd("2014-02-11", "secondary (LP interests in Yunfeng E-Commerce Funds holding Alibaba shares)",
                199_100_000, None, True, GI, "filing")],
    country="CN", country_src="web_verified", country_cite=W("Alibaba Group"), city="Hangzhou",
    focus="Consumer & Marketplaces",
    note="Alibaba Group (NYSE: BABA, HKEX: 9988), Hangzhou. Tiger Global Mauritius Fund bought Giant Interactive's LP "
         "interests in the Yunfeng funds that held pre-IPO Alibaba shares for about $199.1M (Giant's 6-K, Feb "
         "2014), a secondary in the private company seven months before the Sep 2014 IPO (Growth). Market cap "
         "as in the ICONIQ book (rule 10)."))

if __name__ == "__main__":
    jl.write("batch-001c", L)
