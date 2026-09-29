#!/usr/bin/env python3
"""Batch 2, chunk b (rows 16-30): aporia .. avenida-inc. Run: NQ_TAG=b2 python3 judgments-2b.py
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

# 16. Aporia
TCP = PK("aporia", "press", "Aporia raises $25M Series A")
L.append(cls(
    "aporia", status="acquired", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=TCP, stage_conf="high", entry_date="2022-02",
    rounds=[rnd("2022-02-23", "Series A", 25_000_000, "Tiger Global", True, TCP, "press")],
    country="IL", country_src="web_verified", country_cite=TCP, city="Tel Aviv", focus="AI & Applied AI",
    note="Aporia, ML observability and AI guardrails, Tel Aviv. Tiger led the $25M Series A (Feb 2022). Acquired by "
         "Coralogix, Dec 2024 (SiliconANGLE)."))

# 17. Apple: a listed-stock stake
L.append(verdict(
    "apple", "not_member",
    T3 + ": 13F-driven press on a listed-stock stake (Benzinga, 2023-05); 13F holding 2008-2023",
    ec="web", conf="high", cite=PK("apple", "press", "New Apple Stake")))

# 18. Arianee
FWA = PK("arianee", "press", "[Série A] Blockchain")
L.append(cls(
    "arianee", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=FWA, stage_conf="high", entry_date="2022-05",
    rounds=[rnd("2022-05-10", "Series A", 21_000_000, "Tiger Global", True, FWA, "press")],
    country="FR", country_src="web_verified", country_cite=FWA, city="Paris", focus="Crypto & Web3",
    note="Arianee, digital product passports on blockchain for luxury brands, Paris. Tiger led the EUR 20M Series A "
         "(May 2022)."))

# 19. Ariga
SA = PK("ariga", "press", "Database schema-as-code startup Ariga raises $18M")
CT = NEWS("ariga", "Ariga raises $18 million for database schema changes platform")
L.append(verdict(
    "ariga", "member",
    "SiliconANGLE (2023-06-01): Ariga Technologies 'has closed on an $18 million early-stage funding round led by "
    "Tiger Global, TLV Partners', a private round",
    ec="web", conf="high", cite=SA))
L.append(cls(
    "ariga", status="private", rng="below_1b", stage="undetermined",
    rounds=[rnd("2023-06-01", "early-stage round", 18_000_000, "Tiger Global, TLV Partners", True, SA, "press")],
    country="IL", country_src="web_verified", country_cite=CT, city="Tel Aviv", focus="DevTools & APIs",
    note="Ariga (Atlas, Ent), database schema as code, Tel Aviv. Tiger and TLV Partners led an $18M round reported "
         "only as 'early-stage' (Jun 2023), with no seed or Series A label, so the stage is undetermined."))

# 20. Asana
AS = PK("asana", "sec", "tender offer")
L.append(cls(
    "asana", **V("asana", "a16z"),
    stage="Growth", stage_src="web_verified", stage_cite=AS, stage_conf="high", entry_date="2019-10",
    rounds=[rnd("2019-10", "tender offer", None, "Tiger Global", True, AS, "filing")],
    country="US", city="San Francisco", focus="SaaS",
    note="Asana (NYSE: ASAN), San Francisco. Tiger Global Private Investment Partners XI and an affiliate ran an "
         "October 2019 tender offer for Asana shares under a September 2019 participation agreement (IPO DRS), a "
         "tender entry (Growth). Market cap as in the a16z book (rule 10), replacing the float figure."))

# 21. Assignar
PRA = PK("assignar", "press", "Assignar Closes $16.5 Million In Secondary Sale")
L.append(cls(
    "assignar", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=PRA, stage_conf="high", entry_date="2021-11",
    rounds=[rnd("2021-11-08", "secondary sale", 16_500_000, "Tiger Global, SecondQuarter Ventures", True, PRA,
                "press")],
    country="AU", country_src="web_verified", country_cite=PRA, city="Sydney", focus="SaaS",
    note="Assignar, construction operations software, Sydney. Tiger bought shares in a $16.5M secondary sale with "
         "SecondQuarter Ventures (Nov 2021), a secondary entry (Growth by the policy constant)."))

# 22. Ather Energy
WAE = W("Ather Energy")
L.append(cls(
    "ather-energy", status="public", rng="1b_plus", usd=5_813_614_977, val_src="web_verified",
    val_cite="https://stockanalysis.com/quote/nse/ATHERENERG/market-cap/", asof="2026-09-29",
    extra={"valuation_range_source": "web_verified"},
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2015-05",
    rounds=[rnd("2015-05", "Series A", 12_000_000, "Tiger Global", True, WAE, "press")],
    city="Bangalore", focus="Climate & Energy",
    note="Ather Energy (NSE: ATHERENERG), electric scooters, Bangalore. Tiger's $12M of May 2015 (Wikipedia) was "
         "the company's first institutional round after the founders' seed money, reported as its Series A. Listed "
         "in May 2025; Tiger sold its whole stake in Nov 2025. Market cap INR 558.02B @ ECB 2026-09-29 (INR/EUR "
         "108.991, EUR/USD 1.1355) = $5.81B."))

# 23. August Schools
BWS = PK("august-schools", "press", "August Schools Raises $5M Seed Funding Led by Tiger Global")
L.append(cls(
    "august-schools", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=BWS, stage_conf="high", entry_date="2022-04",
    rounds=[rnd("2022-04-05", "Seed", 5_000_000, "Tiger Global", True, BWS, "press")],
    country="US", flags=["city_unknown"], focus="Healthcare & Bio",
    note="August Schools, school health records software. Tiger led the $5M seed (Apr 2022). City not found in the "
         "sources read (the release, FinSMEs). Graduation left for the graduation pass."))

# 24. Augustus
PRG = PK("augustus", "press", "Augustus Announces $180M Series B at $1B Valuation")
L.append(cls(
    "augustus", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=PRG,
    asof="2026-07-21", extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_cite=PRG, stage_conf="high", entry_date="2026-07",
    rounds=[rnd("2026-07-21", "Series B", 180_000_000, "Tiger Global", True,
                PK("augustus", "press", "Tiger Global leads round for bank startup Augustus"), "press")],
    country="US", city="New York", focus="Fintech & Payments",
    note="Augustus (formerly Ivy), dollar clearing bank for fintechs, New York. Tiger led the $180M Series B at a $1B "
         "valuation (Jul 2026), its first round; the figure sits on the band edge. Mark as in the Creandum book."))

# 25. Autohome: listed-company holding
L.append(verdict(
    "autohome-inc", "not_member",
    T3 + ": Autohome listed in December 2013; Tiger's 13F holding starts 2013-12-31 and its 13G filings run "
    "2014-2017, and no private round names the firm",
    ec="fund_filing", conf="high", cite=SEC("autohome-inc", "edgar")))

# 26. Automattic
PH = PK("automattic", "press", "PE Hub | Tiger Global invests $50 million")
L.append(cls(
    "automattic", status="private", **V("automattic", "iconiq-growth"), flags=["stale"],
    clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=PH, stage_conf="high", entry_date="2013-05",
    rounds=[rnd("2013-05-24", "share purchase", 50_000_000, "Tiger Global", True, PH, "press")],
    city="San Francisco", focus="SaaS",
    note="Automattic (WordPress.com), San Francisco. Tiger paid $50M for a stake in May 2013, shares sold to it by the "
         "company's holders ('feeds $50 million in stock to hungry Tiger', Business Journals), a late entry in a "
         "company past its Series B (Growth). Mark as in the ICONIQ book ($7.5B, 2021), stale; staff cuts in 2025 "
         "but no priced down round on record."))

# 27. Avant
WAV = W("Avant (company)")
L.append(cls(
    "avant", status="private", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
    rounds=[rnd("2014", "equity rounds", 225_000_000, None, True, WAV, "press")],
    city="Chicago", focus="Fintech & Payments",
    note="Avant, online consumer lending, Chicago. Tiger's first round on record is the 2014 equity raising of $225M "
         "with Peter Thiel and KKR (Wikipedia), after August Capital's earlier round, so Growth. The Sutter Hill "
         "row named Avant (Fremont, industrial) is a different company."))

# 28. Avataar
BWV = PK("avataar", "press", "Business Wire | Avataar Raises $45 Million")
L.append(cls(
    "avataar", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=BWV, stage_conf="high", entry_date="2022-01",
    rounds=[rnd("2022-01-07", "Series B", 45_000_000, "Tiger Global", True,
                PK("avataar", "press", "Avataar secures $45 million Series B funding led by Tiger Global"), "press")],
    country="IN", country_src="web_verified", country_cite=PK("avataar", "press", "Sequoia-backed AI firm Avataar"),
    city="Bangalore", focus="AI & Applied AI",
    note="Avataar, 3D and generative AI for product visualisation, Bangalore. Tiger led the $45M Series B with "
         "Sequoia India (Jan 2022), its first round."))

# 29. Avendus: the adviser, not a portfolio company
L.append(verdict(
    "avendus", "not_member",
    "Avendus is the Indian investment bank (KKR bought a majority in 2015); the recall headline is Avendus's own page "
    "about advising Zenoti on a Series C led by Tiger, a different company, and no round of Avendus names the firm",
    ec="web", conf="high", cite=PK("avendus", "press", "Avendus advises Zenoti")))

# 30. Avenida.com
CX13 = PK("avenida-inc", "sec", "Cnova going-private")
L.append(verdict(
    "avenida-inc", "member",
    "Evan Feinberg (Tiger partner, in tenure) is director on Avenida Inc.'s 2015 Form D ($30M sold, Vicente López, "
    "Buenos Aires), and Cnova's going-private 13E-3 fairness exhibit lists the Sep 2014 and Nov 2015 stakes in the "
    "private Argentine e-commerce company Avenida.com bought by Naspers and Tiger Global: a documented round plus "
    "the seat",
    ec="formd_adjudicated", conf="high", cite=CX13))
L.append(cls(
    "avenida-inc", status="unknown", rng="below_1b",
    stage="undetermined", entry_date="2014-09", flags=["stage_disputes_band"],
    rounds=[rnd("2014-09", None, 17_500_000, "Naspers, Tiger Global", True,
                NEWS("avenida-inc", "Avenida.com recibe 17,5 millones"), "press"),
            rnd("2015-07", None, 30_000_000, "Naspers, Tiger Global", True, CX13, "filing")],
    city="Vicente López", city_src="formd_address", focus="Consumer & Marketplaces",
    note="Avenida.com, online retailer, Greater Buenos Aires (the Form D address is Vicente López). Tiger and Naspers "
         "first bought in September 2014 ($17.5M, DossierNet; Cnova's exhibit), before the 2015 Form D the band "
         "read as the entry, and neither round is named, so the stage is undetermined. No news of the company after "
         "2016 was found, so its status is not established."))

if __name__ == "__main__":
    jl.write("batch-002b", L)
