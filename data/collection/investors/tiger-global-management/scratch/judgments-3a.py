#!/usr/bin/env python3
"""PRO-167 Tiger Global, queue batch 3, chunk a (Bitauto to Carvana, 18 rows).
Evidence: show.py --batch 3, the SEC filings the evidence pack cites (read), the press pages the
caches hold (read), Wikipedia (insource sweep and wikifetch.py). Run: NQ_TAG=b3 python3 judgments-3a.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import verdict, cls, rnd, W, NEWS, SEC

HERE = Path(__file__).resolve().parent
PK = json.loads((HERE / "evidence-pack.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def PACK(slug, kind="sec", i=0):
    """The URL at the end of the row's i-th evidence-pack line of that kind (never typed)."""
    line = (PK.get(slug) or {}).get(kind, [])[i]
    u = line.rsplit("| ", 1)[-1].strip()
    if not u.startswith("https://"):
        raise SystemExit(f"PACK({slug!r}, {kind!r}, {i}): no URL on the line")
    return u


def URLOF(slug, title_sub, url_sub):
    """One cached press item's publisher URL, chosen by title AND url substrings."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and title_sub.lower() in i["title"].lower()
                            and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"URLOF({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


T3 = "13G/13F position in a listed company, no private round naming the firm (T3, D3)"
L = []

# ---------------------------------------------------------------- Bitauto (13G only)
L.append(verdict("bitauto-holdings-ltd", "not_member",
    T3 + ": Tiger's first Schedule 13G on Bitauto reports an event of 2011-06-20, seven months after the "
    "November 2010 NYSE listing, and no prospectus or round names a Tiger vehicle as a pre-IPO holder",
    ec="fund_filing", conf="high", cite=SEC("bitauto-holdings-ltd", "edgar", 0)))

# ---------------------------------------------------------------- Bitso
BITSO_CB = NEWS("bitso", "Tiger Global, Coatue Lead Bitso")
BITSO_RT = NEWS("bitso", "valuación alcanza 2,200")
L.append(cls("bitso", status="private", rng="1b_plus", usd=2_200_000_000, val_src="web_verified",
    val_cite=BITSO_RT, asof="2021-05-05", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BITSO_CB, entry_date="2021-05", country="MX", country_src="web_verified", country_cite=BITSO_RT,
    city="Mexico City", focus="Crypto & Web3", flags=("stale",), clear=("needs_web_value",),
    note="Mexican crypto exchange (Reuters: 'Mexicana Bitso'), headquartered in Mexico City. Tiger Global and Coatue "
         "co-led the $250M Series C of May 2021 at a $2.2B valuation (Crunchbase News; Reuters); no earlier round in "
         "the evidence view names the firm. Mark $2.2B as of 2021-05, stale; the Coatue book carries the same mark. "
         "The Wikidata MX claim is confirmed.",
    rounds=[rnd("2021-05-05", "Series C", 250_000_000, "Tiger Global; Coatue", True, BITSO_CB, "press")], extra=WV))

# ---------------------------------------------------------------- Bizongo
BIZ_BL = NEWS("bizongo", "Bizongo raises $110 million in series D round")
L.append(cls("bizongo", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=BIZ_BL, entry_date="2021-12", country="IN", country_src="web_verified",
    country_cite=BIZ_BL, city="Mumbai", focus="Consumer & Marketplaces",
    note="Mumbai B2B e-commerce platform for packaging and supplies. Tiger Global led the $110M Series D of "
         "December 2021 at a $600M valuation (Business Line; VCCircle, Mint); it is the first round in the "
         "evidence view that names the firm. Below $1B on that mark; no later priced round found.",
    rounds=[rnd("2021-12", "Series D", 110_000_000, "Tiger Global", True, BIZ_BL, "press")]))

# ---------------------------------------------------------------- Blend Labs (X1: public-desk vehicles only)
BLEND_IRA = PACK("blend-labs-inc")
BLEND_PR = NEWS("blend-labs-inc", "Blend Closes $300M")
L.append(verdict("blend-labs-inc", "member",
    "Blend's IPO registration files its investors' rights agreement dated 2021-01-11, signed by Tiger Global "
    "Investments, L.P. and Tiger Global Long Opportunities Master Fund, L.P. as investors while Blend was private "
    "(the $300M Series G of January 2021). Both named vehicles are public-desk funds and no PIP vehicle is named: "
    "delta X1 would move the row to the other desk (flag boundary)",
    ec="fund_filing", conf="high", cite=BLEND_IRA))
L.append(cls("blend-labs-inc", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=BLEND_PR,
    entry_date="2021-01", country="US", city="San Francisco", focus="Fintech & Payments", flags=("boundary",),
    note="San Francisco mortgage and banking software company, listed on the NYSE since July 2021. Tiger's funds "
         "entered in the $300M Series G of January 2021 at $3.3B (PR Newswire), the round whose investors' rights "
         "agreement (2021-01-11) its two public-desk funds signed: X1 row. Listed below $1B (float prefill).",
    rounds=[rnd("2021-01-13", "Series G", 300_000_000, None, True, BLEND_PR, "press")]))

# ---------------------------------------------------------------- BlockFi
BFI_D = NEWS("blockfi", "Series D Funding And $3 Billion")
L.append(cls("blockfi", status="defunct", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=BFI_D, entry_date="2021-03", country="US", city="Jersey City",
    focus="Crypto & Web3",
    note="Jersey City crypto lender. Tiger Global was among the new investors in the $350M Series D of March 2021 "
         "at a $3B valuation, led by Bain Capital Ventures, DST partners, Pomp and Tiger (Pulse 2.0), after three "
         "earlier rounds that did not include the firm. BlockFi filed for Chapter 11 on 2022-11-28 and wound down "
         "(TechCrunch): defunct, as the BCV book reads.",
    rounds=[rnd("2021-03", "Series D", 350_000_000, "Bain Capital Ventures; DST Global partners; Pomp Investments; "
                "Tiger Global", True, BFI_D, "press")]))

# ---------------------------------------------------------------- Blumberg Capital (a venture firm)
L.append(verdict("blumberg-capital", "not_member",
    "Blumberg Capital is a venture capital firm, not an operating company (T5). The Wikipedia sentence names Tiger "
    "Global only as a fellow winner in DoubleVerify's IPO; no Tiger fund invested in Blumberg Capital",
    ec="web", conf="high", cite=W("Blumberg Capital")))

# ---------------------------------------------------------------- Bold (Colombia)
BOLD_TC = NEWS("bold", "LatAm - TechCrunch")
L.append(cls("bold", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BOLD_TC, entry_date="2022-02", country="CO", country_src="web_verified", country_cite=BOLD_TC,
    city="Bogotá", focus="Fintech & Payments", flags=("model_disputes_source",),
    note="Bold (bold.co), the Bogotá digital payments company. Tiger Global led its $55M Series B of February 2022 "
         "(TechCrunch; General Atlantic's release names the Series B). The Wikidata prefill (acquired, Chile) is a "
         "join on another company named Bold, disputed: Bold raised a further $50M led by General Atlantic and IFC in "
         "February 2024 (Forbes Colombia) and operates. Momentum check: that 2024 round discloses no valuation; no "
         "$1B+ priced round found. The a16z row 'bold' (Chile, acquired) and the Khosla row 'bold' (a US health app) "
         "are other companies: name collisions, not aligned.",
    rounds=[rnd("2022-02-03", "Series B", 55_000_000, "Tiger Global", True, BOLD_TC, "press"),
            rnd("2024-02", "Unnamed", 50_000_000, "General Atlantic; IFC", None, NEWS("bold", "Bold recauda US$50 millones"), "press")]))

# ---------------------------------------------------------------- Bravado
BRAV = NEWS("bravado", "Bravado Raises $26M Led By Tiger Global")
L.append(cls("bravado", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=BRAV, entry_date="2022-05", country="US", city="San Francisco",
    city_src="web_verified", focus="Consumer & Marketplaces",
    note="San Francisco professional network for B2B salespeople (the release's dateline). Tiger Global led the $26M "
         "Series B of 2022-05-19 (PR Newswire); the Redpoint book holds the earlier Series A, which does not name "
         "Tiger.",
    rounds=[rnd("2022-05-19", "Series B", 26_000_000, "Tiger Global", True, BRAV, "company")]))

# ---------------------------------------------------------------- Brex
BREX_W = W("Brex")
L.append(cls("brex", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BREX_W, entry_date="2021-04", city="San Francisco", focus="Fintech & Payments",
    note="San Francisco corporate card and spend company. Tiger Global led the $425M Series D of April 2021 at $7.4B "
         "(Wikipedia); the 2019 Series C-2 (Kleiner Perkins) and the 2020 extension do not name the firm. Capital One "
         "bought Brex: its 424B7 of 2026-04-23 registers the resale of COF shares Tiger Global PIP 14 LLC received as "
         "a former Brex holder, so the deal had closed. Acquired, as the IVP, Ribbit and Y Combinator books read.",
    rounds=[rnd("2019-06", "Series C-2", 100_000_000, "Kleiner Perkins", None, BREX_W, "press"),
            rnd("2020-05", "Series C extension", 150_000_000, None, None, BREX_W, "press"),
            rnd("2021-04", "Series D", 425_000_000, "Tiger Global", True, BREX_W, "press"),
            rnd("2021-10", "Unnamed", 300_000_000, None, None, BREX_W, "press")]))

# ---------------------------------------------------------------- Bright Scholar (13G only)
L.append(verdict("bright-scholar-education-holdings-ltd", "not_member",
    T3 + ": Tiger's 13G filings on Bright Scholar date from 2018, after its May 2017 NYSE listing, and no "
    "prospectus names a Tiger vehicle",
    ec="fund_filing", conf="high", cite=SEC("bright-scholar-education-holdings-ltd", "edgar", 0)))

# ---------------------------------------------------------------- Broadcom (13F position)
L.append(verdict("broadcom", "not_member",
    T3 + ": the recall headline reports Tiger's quarterly 13F moves in Broadcom stock, a company listed since "
    "2009; Tiger's 13F lists it from 2023. The Benchmark row 'broadcom' is the older Broadcom Corporation",
    ec="web", conf="high", cite=NEWS("broadcom", "cuts stakes in Alphabet, Broadcom")))

# ---------------------------------------------------------------- BRYTER
BRY_GS = NEWS("bryter", "Schnelle Riesenrunde")
BRY_PR = URLOF("bryter", "raises $66 million Series B", "080000285")
L.append(cls("bryter", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=BRY_GS, entry_date="2021-04", country="DE", country_src="web_verified", country_cite=BRY_PR,
    city="Berlin", focus="SaaS",
    note="German no-code service automation company, remote-first with offices in Berlin, Frankfurt, London and New "
         "York (its release). Tiger Global approached the company and led the $66M (EUR 55.7M) Series B of April "
         "2021 alongside existing investors Accel, Dawn, Notion and Cavalry, taking about 12% at a valuation near "
         "EUR 350M (Gruenderszene); the 2020 Series A was Accel's. City aligned with the Accel book (Berlin).",
    rounds=[rnd("2021-04-07", "Series B", 66_000_000, "Tiger Global", True, BRY_GS, "press")]))

# ---------------------------------------------------------------- bttn
BTTN = NEWS("bttn", "Tiger Global backs bttn")
L.append(cls("bttn", status="private", rng="below_1b", stage="Series A", stage_src="web_verified",
    stage_conf="high", stage_cite=BTTN, entry_date="2022-06", country="US", city="Seattle", city_src="web_verified",
    focus="Healthcare & Bio",
    note="Seattle B2B marketplace for medical supplies, founded March 2021 (TechCrunch). Tiger Global led its $20M "
         "Series A of 2022-06-13 at a $110M post-money valuation (TechCrunch).",
    rounds=[rnd("2022-06-13", "Series A", 20_000_000, "Tiger Global", True, BTTN, "press")]))

# ---------------------------------------------------------------- Calibrate
CAL_B = NEWS("calibrate", "Notches A $100 Million Series B From Founders Fund And Tiger Global - Forbes")
CAL_A = URLOF("calibrate", "Series A funding", "mobihealthnews")
L.append(cls("calibrate", status="private", rng="below_1b", stage="Growth", stage_src="web_verified",
    stage_conf="high", stage_cite=CAL_B, entry_date="2021-08", country="US", city="New York", focus="Healthcare & Bio",
    note="New York metabolic health and weight-loss company (its 2026 release is datelined New York). Founders Fund "
         "and Tiger Global led the $100M Series B of August 2021 (Forbes); the $22.5M Series A of January 2021 was led "
         "by Threshold Ventures and does not name Tiger (MobiHealthNews).",
    rounds=[rnd("2021-01", "Series A", 22_500_000, "Threshold Ventures", False, CAL_A, "press"),
            rnd("2021-08-25", "Series B", 100_000_000, "Founders Fund; Tiger Global", True, CAL_B, "press")]))

# ---------------------------------------------------------------- Captaris, Carter's, Carvana (13G only)
L.append(verdict("captaris-inc", "not_member",
    T3 + ": Captaris (formerly AVT Corporation) was Nasdaq-listed through the 1990s, before the firm existed; "
    "Tiger's 2004 13G is a listed-stock position",
    ec="fund_filing", conf="high", cite=SEC("captaris-inc", "edgar", 0)))
L.append(verdict("carters-inc", "not_member",
    T3 + ": Carter's has been NYSE-listed since 2003; Tiger's 13G filings date from 2013",
    ec="fund_filing", conf="high", cite=SEC("carters-inc", "edgar", 0)))
L.append(verdict("carvana-co", "not_member",
    T3 + ": Carvana listed on the NYSE in April 2017; Tiger's 13G filings and 13F lines start in 2019",
    ec="fund_filing", conf="high", cite=SEC("carvana-co", "edgar", 0)))

if __name__ == "__main__":
    jl.write("batch-003a", L)
