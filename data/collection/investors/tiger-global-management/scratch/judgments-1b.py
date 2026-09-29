#!/usr/bin/env python3
"""Batch 1, chunk b (rows 16-30): palantir .. absolute. Run: NQ_TAG=b1 python3 judgments-1b.py
Citations come from judge_lib helpers, the row's evidence view (evidence-pack.json), a sibling book's
recorded valuation citation (siblings.json) or a URL printed by a search tool; none is typed from memory."""
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

# 16. Palantir
WP = W("Palantir")
L.append(verdict(
    "palantir", "member",
    "Wikipedia: 'As of December 2014, the company continued to have diverse private funders, ... Tiger Global "
    "Management, and Founders Fund', a holding in the private company before its 2020 listing; Our Story also "
    "names it (D4)",
    ec="web", conf="medium", cite=WP))
L.append(cls(
    "palantir", stage="Growth", stage_src="model", stage_conf="medium",
    country="US", city="Miami", focus="Data Infrastructure",
    note="Palantir Technologies (NYSE: PLTR). Tiger was among its private funders by December 2014 (Wikipedia), "
         "when Palantir was valued in the billions after several rounds, so the entry is Growth; the round is not "
         "named in our sources. Headquarters moved from Denver to Miami (announced Feb 2026, Wikipedia)."))

# 17. Scale AI
WS = W("Scale AI")
L.append(verdict(
    "scale-ai", "member",
    "Wikipedia: Tiger Global Management is among Scale's early investors, and 'By July 2021, Scale had reached a "
    "valuation of $7 billion, after a financing led by Greenoaks, Dragoneer Investment Group and Tiger Global "
    "Management'; Our Story also names it (D4)",
    ec="web", conf="high", cite=WS))
L.append(cls(
    "scale-ai", status="private", **V("scale-ai", "coatue"), clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-12",
    rounds=[rnd("2020-12", "Series D", 155_000_000, "Tiger Global", True,
                NEWS("scale-ai", "Scale, which helps companies improve"), "press"),
            rnd("2021-04", "Series E", 325_000_000, "Greenoaks, Dragoneer, Tiger Global", True, WS, "press")],
    country="US", city="San Francisco", focus="AI & Applied AI",
    note="Scale AI, San Francisco. Tiger's first round on record is the $155M Series D at $3.5B (Dec 2020), which "
         "it co-led, followed by the $325M Series E at $7.3B (2021) led by Greenoaks, Dragoneer and Tiger. Meta "
         "bought 49% at about $29B in June 2025 (not a control purchase), mark as in the Coatue book (rule 10)."))

# 18. Snowflake
SX = PK("snowflake", "sec", "tender offer holders")
L.append(verdict(
    "snowflake", "member",
    "IPO registration exhibit (investors' rights agreement, 2020): Tiger Global PIP 11 Holdings-2 LLC is on the "
    "schedule of tender offer holders, shares bought in a tender in the private company (T3: a tender entry)",
    ec="fund_filing", conf="high", cite=SX))
L.append(cls(
    "snowflake", **V("snowflake", "coatue"),
    stage="Growth", stage_src="web_verified", stage_cite=SX, stage_conf="high",
    country="US", city="Bozeman", focus="Data Infrastructure",
    note="Snowflake (NYSE: SNOW), principal office Bozeman. Tiger bought in a tender offer before the Sep 2020 "
         "IPO (the rights agreement lists Tiger Global PIP 11 Holdings-2 LLC among the tender offer holders); a "
         "tender entry is Growth. Market cap as in the Coatue book (rule 10), replacing the float figure."))

# 19. Stripe
BF = NEWS("stripe", "Deal of the Month January 2019")
L.append(verdict(
    "stripe", "member",
    "Business & Finance (2019-02-01): 'Deal of the Month January 2019: Stripe hits $22.5bn valuation through Tiger "
    "Global investment', a primary investment in the private company; Our Story also names it (D4)",
    ec="web", conf="high", cite=BF))
L.append(cls(
    "stripe", status="private", **V("stripe", "coatue"), clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2019-01",
    rounds=[rnd("2019-01", "growth round", 100_000_000, "Tiger Global", True, BF, "press")],
    country="US", city="South San Francisco", focus="Fintech & Payments",
    note="Stripe, South San Francisco. Tiger's first investment was the $100M round at $22.5B in January 2019 "
         "(Growth). Mark as in the Coatue book (rule 10)."))

# 20. Toast
L.append(verdict(
    "toast", "member",
    "IPO registration exhibit (fifth amended investors' rights agreement, 2021): Tiger Global PIP 10 LLC and Tiger "
    "Global Private Investment Partners X sign as holders of the private company's preferred stock; the IPO "
    "prospectus lists PIP 10 LLC as a 5% holder whose shares come from Series B to F preferred",
    ec="fund_filing", conf="high", cite=PK("toast", "sec", "Tiger Global PIP 10 LLC")))
L.append(cls(
    "toast", status="public", rng="10b_plus", usd=17_180_000_000, val_src="web_verified",
    val_cite="https://companiesmarketcap.com/toast/marketcap/", asof="2026-09",
    extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="model", stage_conf="medium",
    country="US", city="Boston", focus="SaaS",
    note="Toast (NYSE: TOST), restaurant software and payments, Boston. Tiger Global PIP 10 LLC held shares from "
         "Series B to F preferred and bought $143M of Series D, E and F (IPO prospectus); it co-led the $250M "
         "Series E at $2.7B with TCV (Apr 2019). The first purchase is not dated in our sources; every round it "
         "held is Series B or later, so Growth. Market cap $17.18B (September 2026)."))

# 21. Uber
MI = PK("uber", "press", "picks up stake in Uber")
L.append(verdict(
    "uber", "member",
    "Mint (2015-12-04): 'Tiger Global, top Ola investor, picks up stake in Uber', a purchase in the private company "
    "during its late-2015 round at $62.5B; Our Story also names it (D4)",
    ec="web", conf="high", cite=MI))
L.append(cls(
    "uber", status="public", **V("uber", "coatue"),
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2015-12",
    rounds=[rnd("2015-12", "growth round", None, None, True, MI, "press")],
    country="US", city="San Francisco", focus="Consumer & Marketplaces",
    note="Uber (NYSE: UBER), San Francisco. Tiger bought into Uber in December 2015 while leading rounds in rival "
         "Ola (Mint, Forbes), a late private round, so Growth. Market cap as in the Coatue book (rule 10)."))

# 22. Waymo
TC = NEWS("waymo", "self-driving arm, raises $2.5B")
L.append(verdict(
    "waymo", "member",
    "TechCrunch (2021-06-16): Waymo's $2.5B second external investment round, whose investors include Tiger Global; "
    "Hedge Fund Alpha (2026-01) reports Tiger's gains on Waymo; Our Story also names it (D4)",
    ec="web", conf="medium", cite=TC))
L.append(cls(
    "waymo", status="private", **V("waymo", "sequoia-capital"),
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-06",
    rounds=[rnd("2021-06-16", "external round", 2_500_000_000, None, True, TC, "press")],
    country="US", city="Mountain View", focus="Industrial & Robotics",
    note="Waymo, Alphabet's autonomous driving unit, Mountain View. Tiger's first round on record is the $2.5B "
         "external round of June 2021; Waymo sells priced rounds to outside investors, so it reads private with "
         "that mark (COLLECTION.md 6). Mark as in the Sequoia book (rule 10)."))

# 23. 17 Education & Technology
ST = NEWS("17-education-and-technology", "Files Its Annual Report on Form 20-F")
L.append(cls(
    "17-education-and-technology", status="public", rng="below_1b", stage="undetermined",
    country="CN", country_src="web_verified", country_cite=ST, city="Beijing", focus="SaaS",
    note="17 Education & Technology Group (Nasdaq: YQ, 17zuoye), K-12 learning software, Beijing. Tiger Global Seven "
         "Parent Holdings signs its pre-IPO shareholders agreement (F-1 exhibit, 2020); which preferred series it "
         "bought first is not in our sources, so the stage is undetermined. Listed Dec 2020; the stock trades far "
         "below $1B of market value (thin trading, 2026)."))

# 24. 1Life Healthcare (One Medical)
L.append(verdict(
    "1life-healthcare-inc", "not_member",
    T3 + ": the adviser's Schedule 13G filings (2021-2023) and 13F holdings from 2020-12-31 come after One Medical's "
    "January 2020 IPO, and no pre-IPO round names Tiger",
    ec="fund_filing", conf="high", cite=SEC("1life-healthcare-inc", "edgar")))

# 25. 1Password
BK = NEWS("1password", "largest in Canadian history")
CN = NEWS("1password", "Canadian password manager 1Password valued at $6.8 billion in new funding round")
L.append(verdict(
    "1password", "member",
    "BetaKit (2022-01-19): 'ICONIQ Growth led the round, with Tiger Global, Lightspeed Venture Partners, Backbone "
    "Angels, and Salesforce Ventures participating', the $620M Series C",
    ec="web", conf="high", cite=BK))
L.append(cls(
    "1password", status="private", rng="1b_plus", usd=6_800_000_000, val_src="web_verified", val_cite=CN,
    asof="2022-01-19", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=CN, stage_conf="high", entry_date="2022-01",
    rounds=[rnd("2022-01-19", "Series C", 620_000_000, "ICONIQ Growth", True, CN, "press")],
    country="CA", country_src="web_verified", country_cite=CN, city="Toronto", focus="Security",
    note="1Password, password manager, Toronto. Tiger joined the $620M Series C at $6.8B led by ICONIQ Growth "
         "(Jan 2022), its first round in the company. No later priced round is on record, so the 2022 mark "
         "stands, stale."))

# 26. 1X
W1 = W("1X Technologies")
L.append(cls(
    "1x", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=W1, stage_conf="high", entry_date="2023-03",
    rounds=[rnd("2023-03", "Series A2", 23_500_000, "OpenAI Startup Fund", True, W1, "press")],
    country="US", city="Palo Alto", focus="Industrial & Robotics",
    note="1X Technologies (formerly Halodi Robotics), humanoid robots, headquartered in Palo Alto with "
         "manufacturing in Hayward and Moss, Norway (Wikipedia). Tiger joined the $23.5M Series A2 led by the "
         "OpenAI Startup Fund (Mar 2023), a Series A. SoftBank was reported in talks (Aug 2026) to buy a majority "
         "stake at about $6B; talks are not a priced event, and no priced round at $1B or more is on record "
         "(checked 2026-09-29), so below_1b."))

# 27-28. 58.com and 8x8: listed-company holdings
L.append(verdict(
    "58-com-inc", "not_member",
    T3 + ": 58.com listed in October 2013; Tiger's 13F holding starts 2013-12-31 and its 13G filings run 2014-2016",
    ec="fund_filing", conf="high", cite=SEC("58-com-inc", "edgar")))
L.append(verdict(
    "8x8-inc-de", "not_member",
    T3 + ": 8x8 has been listed since the 1990s; the adviser's 13G filings date from 2020",
    ec="fund_filing", conf="high", cite=SEC("8x8-inc-de", "edgar")))

# 29. Abacus.AI
PR = PK("abacus-ai", "press", "backed by world-class investors")
ZD = NEWS("abacus-ai", "snags $50 million Series C")
L.append(verdict(
    "abacus-ai", "member",
    "Abacus.AI's own release (PR Newswire, 2026-09-10): 'Abacus.AI is backed by world-class investors, including "
    "Coatue, Tiger Global, and Index Ventures'; ZDNET (2021-10-27) reports the $50M Series C from the Tiger query",
    ec="web", conf="medium", cite=PR))
L.append(cls(
    "abacus-ai", status="private", rng="below_1b",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-10",
    rounds=[rnd("2021-10-27", "Series C", 50_000_000, None, True, ZD, "press")],
    country="US", city="San Francisco", focus="AI & Applied AI",
    note="Abacus.AI, AI platform, San Francisco. Tiger's round is the $50M Series C (Oct 2021); Coatue led the "
         "Series B. Momentum check 2026-09-29 (Bing News, the company's name with valuation and funding): no "
         "priced round at $1B or more, so below_1b as in the Coatue and General Catalyst books."))

# 30. Absolute
ET = PK("absolute", "press", "Absolute raises $100 million in funding led by")
L.append(cls(
    "absolute", status="private", rng="below_1b", stage="undetermined",
    rounds=[rnd("2022-05-05", "first institutional round", 100_000_000,
                "Sequoia Capital India, Alpha Wave Global, Tiger Global", True, ET, "press")],
    country="IN", country_src="web_verified", country_cite=ET, city="Bangalore", focus="Healthcare & Bio",
    note="Absolute (Absolute Foods), plant bioscience and bio-inputs for farming. Its $100M from Sequoia India, "
         "Alpha Wave and Tiger (May 2022) was its first institutional funding, raised 'across recent funding "
         "rounds' (VCCircle) with no round name, so the stage is undetermined. City from model knowledge."))

if __name__ == "__main__":
    jl.write("batch-001b", L)
