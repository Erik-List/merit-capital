#!/usr/bin/env python3
"""Batch 2, chunk a (rows 1-15): alkira .. apollo-global-management-inc. Run: NQ_TAG=b2 python3 judgments-2a.py
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

# 1. Alkira
TCA = PK("alkira", "press", "Alkira connects with $100M")
L.append(verdict(
    "alkira", "member",
    "TechCrunch (2024-05-15): 'Tiger Global Management, a new investor in the startup, is leading this Series C' "
    "($100M); the company's release and CRN, SiliconANGLE and Light Reading say the same",
    ec="web", conf="high", cite=TCA))
L.append(cls(
    "alkira", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=TCA, stage_conf="high", entry_date="2024-05",
    rounds=[rnd("2024-05-15", "Series C", 100_000_000, "Tiger Global Management", True, TCA, "press")],
    country="US", city="San Jose", focus="Data Infrastructure",
    note="Alkira, network infrastructure as a service, San Jose. Tiger led the $100M Series C as a new investor "
         "(May 2024). Momentum check 2026-09-29 (Bing News, the company's name with valuation and funding): no "
         "later round and no priced valuation at $1B or more, so below_1b as in the Sequoia book."))

# 2. Allbirds
AB = PK("allbirds", "sec", "Series C preferred")
L.append(cls(
    "allbirds", stage="Growth", stage_src="web_verified", stage_cite=AB, stage_conf="high", entry_date="2018-10",
    rounds=[rnd("2018-10", "Series C", 50_000_000, None, True, AB, "filing")],
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    note="Allbirds (Nasdaq: BIRD), footwear, San Francisco. Tiger Global Private Investment Partners X bought Series C "
         "preferred in October 2018 (the $50M round at $1.4B) and became a 5% holder before the 2021 IPO (DRS)."))

# 3. AlloCine: owned by Tiger 2007-2013
L.append(verdict(
    "allocin", "not_member",
    "Control position (T3 addendum): Wikipedia: AlloCiné 'was sold to Tiger Global, an American investment fund that "
    "acquired a majority stake', and was under its ownership from June 2007 to 2013, a whole-company purchase, "
    "not a minority round",
    ec="web", conf="high", cite=W("AlloCiné"), exclusion="control_position"))

# 4. Almanac
BWM = PK("almanac", "press", "Almanac Raises $34 Million in Series A")
L.append(cls(
    "almanac", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=BWM, stage_conf="high", entry_date="2021-09",
    rounds=[rnd("2021-09-21", "Series A", 34_000_000, "Tiger Global", True, BWM, "press")],
    country="US", city="San Francisco", focus="SaaS",
    note="Almanac (almanac.io), collaborative documents for remote teams, San Francisco. Tiger led the $34M Series A "
         "(Sep 2021); still operating (Forbes, May 2023). Sibling rows named Almanac in the General Catalyst "
         "(one healthcare) and YC books may be different companies."))

# 5, 7, 9. Listed-company stakes
L.append(verdict(
    "alphabet", "not_member",
    T3 + ": the only record is 13F-driven press on a listed-stock stake (CNBC, 2022-11: 'Tiger Global increases "
    "stake in Alphabet'); 13F holding 2016-2026",
    ec="web", conf="high", cite=PK("alphabet", "press", "Tiger Global increases stake in Alphabet")))
L.append(verdict(
    "amazon", "not_member",
    T3 + ": 13F-driven press on a listed-stock position (Seeking Alpha, 2025-08); 13F holding since 2010",
    ec="web", conf="high", cite=PK("amazon", "press", "increases position in Amazon")))
L.append(verdict(
    "amd", "not_member",
    T3 + ": 13F-driven press on a new listed-stock position in Q2 2026 (Business Line, 2026-08-14)",
    ec="web", conf="high", cite=PK("amd", "press", "Business Line | Tiger Global reduces big tech bets")))

# 6. AltC Acquisition Corp.
L.append(verdict(
    "altc-acquisition-corp", "not_member",
    T3 + ": Schedule 13G filings (2021-2024) on the listed shares of AltC Acquisition Corp., a blank-check company "
    "(T5, no operating business) that merged with Oklo in May 2024; no private round of Oklo names Tiger",
    ec="fund_filing", conf="high", cite=SEC("altc-acquisition-corp", "edgar")))

# 8. Ambi Robotics
BWR = PK("ambi-robotics", "press", "Ambi Robotics Announces $26 Million Series A")
L.append(cls(
    "ambi-robotics", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=BWR, stage_conf="high", entry_date="2021-09",
    rounds=[rnd("2021-09-14", "Series A", 26_000_000, "Tiger Global", True, BWR, "press")],
    country="US", city="Berkeley", focus="Industrial & Robotics",
    note="Ambi Robotics, AI-powered parcel sorting robots, Berkeley. Tiger led the $26M Series A (Sep 2021); the "
         "company added $32M in Oct 2022. No priced round at $1B or more is on record."))

# 10. Amperity
SI = PK("amperity", "press", "streetinsider | Amperity Closes $28 million Series B")
L.append(cls(
    "amperity", status="private", **V("amperity", "general-catalyst"), flags=["stale"],
    stage="Growth", stage_src="web_verified", stage_cite=SI, stage_conf="high", entry_date="2017-10",
    rounds=[rnd("2017-10-26", "Series B", 28_000_000, "Tiger Global", True, SI, "press")],
    country="US", city="Seattle", focus="SaaS",
    note="Amperity, customer data platform, Seattle. Tiger led the $28M Series B (Oct 2017), its first round; the "
         "$100M Series D of July 2021 valued the company at more than $1B (figure written as $1.0B, at the band "
         "edge; as in the General Catalyst book). No later priced round is on record, so stale."))

# 11. AngelList
CI = PK("angellist", "press", "AngelList Venture Secures $100M")
L.append(cls(
    "angellist", status="private", rng="1b_plus", usd=4_000_000_000, val_src="web_verified", val_cite=CI,
    asof="2022-03-08", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    stage="Growth", stage_src="web_verified", stage_cite=W("AngelList"), stage_conf="high", entry_date="2022-03",
    rounds=[rnd("2022-03-08", "Series B", 100_000_000, "Tiger Global", True, CI, "press")],
    country="US", city="San Francisco", focus="Fintech & Payments",
    note="AngelList, venture investing platform, San Francisco. Tiger led the $100M Series B with Accomplice at a "
         "$4B pre-money valuation (Mar 2022; figure written as the $4B pre-money, post-money about $4.1B). No "
         "later priced round is on record, so stale."))

# 12. Ankorstore
FW = PK("ankorstore", "press", "Ankorstore lève 84 millions")
L.append(cls(
    "ankorstore", status="private", **V("ankorstore", "bain-capital-ventures"), flags=["stale"],
    clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=FW, stage_conf="high", entry_date="2021-05",
    rounds=[rnd("2021-05-17", "Series B", 102_000_000, "Tiger Global, Bain Capital Ventures", True, FW, "press"),
            rnd("2022-01-09", "Series C", 305_000_000, "Tiger Global", True,
                PK("ankorstore", "press", "Ankorstore becomes France’s latest unicorn"), "press")],
    country="FR", country_src="web_verified", country_cite=FW, city="Paris", focus="Consumer & Marketplaces",
    note="Ankorstore, wholesale marketplace, Paris. Tiger and Bain Capital Ventures led the EUR 84M Series B (May "
         "2021), Tiger's entry, and Tiger returned in the EUR 250M Series C at EUR 1.75B (Jan 2022). Mark as in the "
         "Bain Capital Ventures book ($1.98B, Jan 2022), stale; job cuts were reported in 2023, but no down round "
         "or tender is on record."))

# 13. Apna
MA = PK("apna", "press", "Apna raises $70 million led by Insight Partners, Tiger Global")
U = NEWS("apna", "valuation at $1.1 bn")
L.append(cls(
    "apna", status="private", rng="1b_plus", usd=1_100_000_000, val_src="web_verified", val_cite=U,
    asof="2021-09-15", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=MA, stage_conf="high", entry_date="2021-06",
    rounds=[rnd("2021-06-15", "Series B", 70_000_000, "Insight Partners, Tiger Global", True, MA, "press"),
            rnd("2021-09-15", "Series C", 100_000_000, "Tiger Global", True, U, "press")],
    country="IN", country_src="web_verified", country_cite=MA, city="Bangalore", focus="Consumer & Marketplaces",
    note="Apna, jobs platform for blue-collar workers, Bangalore. Insight and Tiger led the $70M Series B at $570M "
         "(Jun 2021), Tiger's entry; Tiger then led the $100M round at $1.1B (Sep 2021). No later priced round is "
         "on record, so stale; mark as in the Insight book."))

# 14. ApnaKlub
BL = PK("apnaklub", "press", "ApnaKlub raises $10 million in Series A from Tiger Global")
L.append(cls(
    "apnaklub", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=BL, stage_conf="high", entry_date="2022-05",
    rounds=[rnd("2022-05-11", "Series A", 10_000_000, "Tiger Global", True, BL, "press")],
    country="IN", country_src="web_verified", country_cite=BL, city="Bangalore", focus="Consumer & Marketplaces",
    note="ApnaKlub, B2B FMCG wholesale platform, Bangalore (Times of India files it under Bengaluru). Tiger led the "
         "$10M Series A (May 2022)."))

# 15. Apollo Global Management
L.append(verdict(
    "apollo-global-management-inc", "not_member",
    T3 + ": the filings on Apollo Global Management (Forms 3/4 and Schedule 13D/G) concern a listed alternative "
    "asset manager, not a venture round in an operating startup",
    ec="fund_filing", conf="high", cite=SEC("apollo-global-management-inc", "edgar")))

if __name__ == "__main__":
    jl.write("batch-002a", L)
