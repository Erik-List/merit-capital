#!/usr/bin/env python3
"""Batch 2, chunk c (rows 31-45): avicena .. bit. Run: NQ_TAG=b2 python3 judgments-2c.py
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

# 31. Avicena
YAV = PK("avicena", "press", "Yahoo Finance | Avicena Announces Series B Funding Round Led by Tiger Global")
L.append(cls(
    "avicena", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=YAV, stage_conf="high", entry_date="2025-05",
    rounds=[rnd("2025-05-14", "Series B", 65_000_000, "Tiger Global", True, YAV, "press")],
    country="US", city="Sunnyvale", focus="Industrial & Robotics",
    note="Avicena (AvicenaTech Corp.), microLED-based chip interconnects, Sunnyvale. Tiger led the $65M Series B with "
         "SK hynix participating (May 2025), its first round; no priced round at $1B or more is on record."))

# 32. Axis (Egypt; the Wikidata Japan join is wrong)
YAX = PK("axis", "press", "Tiger Global-backed Axis launches digital payments platform")
L.append(cls(
    "axis", status="private", rng="below_1b",
    stage="Seed", stage_src="web_verified", stage_cite=YAX, stage_conf="medium", entry_date="2023",
    rounds=[rnd("2023", "Seed", 8_250_000, None, True, YAX, "press")],
    country="EG", country_src="web_verified", country_cite=YAX, city="Cairo", focus="Fintech & Payments",
    flags=["model_disputes_source"],
    note="Axis, digital payments and wallets for Egyptian SMEs, Cairo. 'Tiger Global-backed Axis' launched its "
         "platform in May 2023 'months after its $8.25M seed' (TechCrunch via Yahoo), Tiger's only round on record; "
         "the seed closed in the months before May 2023, so the entry is dated to the year. The pre-filled Japan "
         "is a wrong Wikidata join on a one-word name. Graduation left for the graduation pass."))

# 33. Baby.com.br
WBB = W("Baby.com.br")
L.append(cls(
    "baby-com-br", status="acquired", rng="below_1b",
    stage="Series A", stage_src="model", stage_conf="medium", entry_date="2011-02",
    rounds=[rnd("2011-02", "first round", 4_400_000, None, True, WBB, "press")],
    country="BR", country_src="web_verified", country_cite=WBB, city="São Paulo", focus="Consumer & Marketplaces",
    note="Baby.com.br, baby-goods e-commerce, São Paulo. Tiger joined its first round of $4.4M with Monashees, "
         "Felicis, Social+Capital and SV Angel (Feb 2011, Wikipedia); Felicis's own portfolio labels that round "
         "Series A. Later folded into the Netshoes group (status as in the Felicis book)."))

# 34. BabyOye
MN = PK("babyoye", "press", "MediaNama | Babyoye.com Raises $2.5M")
L.append(cls(
    "babyoye", status="acquired", rng="below_1b", stage="undetermined",
    rounds=[rnd("2011-04-13", None, 2_500_000, "Accel Partners", True, MN, "press")],
    country="IN", country_src="web_verified", country_cite=MN, city="Mumbai", focus="Consumer & Marketplaces",
    note="BabyOye, online baby products store. Tiger joined the $2.5M round led by Accel (Apr 2011, MediaNama), which "
         "the coverage does not name, so the stage is undetermined. Mahindra bought it in 2015 and sold it to "
         "FirstCry in 2016. City from model knowledge."))

# 35, 40. Hedge funds named beside Tiger, not portfolio companies
L.append(verdict(
    "balyasny-asset-management", "not_member",
    "Balyasny is a hedge fund manager; the Wikipedia sentence names Tiger Global only as a peer that invests in "
    "private startups, not as an investor in Balyasny (T5, no round)",
    ec="web", conf="high", cite=W("Balyasny Asset Management")))
L.append(verdict(
    "beach-point-capital-management", "not_member",
    "Beach Point is a hedge fund manager; the Wikipedia sentence ranks it against Tiger Global Management by size, "
    "no investment by the firm (T5, no round)",
    ec="web", conf="high", cite=W("Beach Point Capital Management")))

# 36. Bamboo
TCB = NEWS("bamboo", "lead $15m Series A round in Nigeria")
L.append(cls(
    "bamboo", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=TCB, stage_conf="high", entry_date="2022-01",
    rounds=[rnd("2022-01-31", "Series A", 15_000_000, "Tiger Global, Greycroft", True, TCB, "press")],
    country="NG", country_src="web_verified", country_cite=PK("bamboo", "press", "Nigerian investment app Bamboo"),
    city="Lagos", focus="Fintech & Payments",
    note="Bamboo, investment app, Lagos. Tiger Global and Greycroft led the $15M Series A (Jan 2022)."))

# 37. 'Bankruptcy of FTX': an article, and FTX has its own row
L.append(verdict(
    "bankruptcy-of-ftx", "not_member",
    "The row is Wikipedia's article on FTX's bankruptcy, not a company (T5); the company is the ftx row in this base, "
    "which carries Tiger's FTX rounds, so this row is a duplicate",
    ec="web", conf="high", cite=W("Bankruptcy of FTX")))

# 38. Battery Smart
EN = PK("battery-smart", "press", "Exclusive: Tiger Global leads $25 Mn Series A round in Battery Smart")
L.append(cls(
    "battery-smart", status="private", rng="below_1b",
    stage="Series A", stage_src="web_verified", stage_cite=EN, stage_conf="high", entry_date="2022-06",
    rounds=[rnd("2022-06-13", "Series A", 25_000_000, "Tiger Global", True, EN, "press")],
    country="IN", country_src="web_verified", country_cite=EN, city="Gurugram", focus="Climate & Energy",
    note="Battery Smart, EV battery swapping, Gurugram ('Gurugram-based', Entrackr). Tiger led the $25M Series A (Jun "
         "2022) and joined the $33M pre-Series B (Jul 2023)."))

# 39. Bazaar (Pakistan; the Wikidata Greece join is wrong)
TCZ = PK("bazaar", "press", "TechCrunch | Bazaar raises $70 million")
MB = NEWS("bazaar", "Bazaar raises $70 million Series B led by Dragoneer and Tiger")
L.append(cls(
    "bazaar", status="private", rng="below_1b",
    stage="Growth", stage_src="web_verified", stage_cite=MB, stage_conf="high", entry_date="2022-03",
    rounds=[rnd("2022-03-14", "Series B", 70_000_000, "Dragoneer, Tiger Global", True, MB, "press")],
    country="PK", country_src="web_verified", country_cite=TCZ, city="Karachi", focus="Consumer & Marketplaces",
    flags=["model_disputes_source"],
    note="Bazaar Technologies, B2B e-commerce for retailers, Karachi. Dragoneer and Tiger led the $70M Series B (Mar "
         "2022), Tiger's first round. The pre-filled Greece is a wrong Wikidata join on a one-word name."))

# 41. Beleza.com = Beleza na Web
L.append(verdict(
    "beleza-com-ltd", "member",
    "Director-of-record pattern: Lee Fixel (Tiger, in tenure) is a director on Beleza.Com Ltd.'s Jul 2013 Form D "
    "($5.7M) and Evan Feinberg (Tiger) on its May 2015 Form D ($26.5M); the other directors are Alexandre Serodio "
    "and Luana Bertoletti, the founders of the Brazilian beauty retailer Beleza na Web, and Kaszek's Hernan Kazah, so "
    "the issuer resolves to that operating company (São Paulo) and no contrary evidence exists",
    ec="formd_adjudicated", conf="medium", cite=SEC("beleza-com-ltd", "formd", 0)))
L.append(cls(
    "beleza-com-ltd", status="acquired", rng="below_1b", grad="graduated", grad_src="formd",
    city="São Paulo", city_src="formd_address", focus="Consumer & Marketplaces",
    note="Beleza.Com Ltd. is the Cayman holding company of Beleza na Web, beauty e-commerce, São Paulo (its founders "
         "sign the Form Ds). The Form D sequence ($5.7M in 2013, then $26.5M in 2015) graduates the seed-band "
         "entry. Bought by Grupo Boticário (status from model knowledge)."))

# 42. BharatPe
YB = PK("bharatpe", "press", "Yahoo Finance | India's BharatPe valued at $2.85 billion")
L.append(cls(
    "bharatpe", status="private", **V("bharatpe", "ribbit-capital"), flags=["stale"], clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=YB, stage_conf="high", entry_date="2021-08",
    rounds=[rnd("2021-08-03", "Series E", 370_000_000, "Tiger Global", True, YB, "press")],
    country="IN", country_src="web_verified", country_cite=YB, city="New Delhi", focus="Fintech & Payments",
    note="BharatPe, merchant payments, New Delhi. Tiger led the $370M Series E at $2.85B (Aug 2021), its first round "
         "(Ribbit and Coatue led the earlier C and D). No later primary; a 2025 secondary at the same $2.85B was "
         "reported (Entrackr). Mark as in the Ribbit book, stale."))

# 43. BigID (New York; the Wikidata Israel claim is the R&D base)
BWB = NEWS("bigid", "BigID Starts 2020 with $50 Million in New Funding from Tiger Global")
P2 = PK("bigid", "press", "BigID: $70 Million And Over A $1 Billion Valuation")
L.append(cls(
    "bigid", status="private", rng="1b_plus", usd=1_000_000_000, val_src="web_verified", val_cite=P2,
    asof="2020-12-16", extra={"valuation_range_source": "web_verified"}, flags=["stale"],
    clear=["needs_web_value"],
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2020-01",
    rounds=[rnd("2020-01-06", "Series C", 50_000_000, "Tiger Global", True, BWB, "press"),
            rnd("2020-12-16", "Series D", 70_000_000, None, None, P2, "press")],
    country="US", city="New York", focus="Security",
    note="BigID, data security and privacy, New York (founded in Israel, R&D in Tel Aviv). Tiger led the $50M round "
         "of January 2020, the company's Series C and Tiger's entry; the $70M round of Dec 2020 valued it at more "
         "than $1B (figure written as $1.0B, at the band edge), stale. The pre-filled Israel is the company's "
         "research base, not its head office."))

# 44. BillMe: the headline is about Razorpay
L.append(verdict(
    "billme", "not_member",
    "The recall headline names Tiger as the backer of Razorpay, BillMe's acquirer ('Tiger Global-backed Razorpay marks "
    "8th acquisition with BillMe', VCCircle 2023-09-12); no round of BillMe names the firm",
    ec="web", conf="high", cite=PK("billme", "press", "VCCircle | Tiger Global-backed Razorpay")))

# 45. BIT: the round was Matrixport's
L.append(verdict(
    "bit", "not_member",
    "Wikipedia's BIT (company) sentence names Tiger among participants in Matrixport's Series C (Aug 2021); BIT is "
    "Matrixport's exchange and raised no round naming the firm. The investment belongs to Matrixport, which has no "
    "row in this base",
    ec="web", conf="high", cite=W("BIT (company)")))

if __name__ == "__main__":
    jl.write("batch-002c", L)
