"""A/B pass ab2, first half (PRO-99 Kleiner Perkins; COLLECTION.md s6 momentum slice, s7), 2026-09-30.

Every private row first seen since 2021 in AI, fintech, data infrastructure or dev tools (queue/ab2.json) gets one
mechanical check for a $1B+ priced round: one Google News query per row under NQ_TAG=ab2 (scratchpad/ab2/nq-out.txt
and news-extra-ab2.json), the publisher page read where a round was found. The outcome is recorded either way: the
latest round found is cited as valuation_range_source web_verified, or the row keeps below_1b with the dated note.

Rows a to n of the list: balerion .. nooks. Two rows change beyond the check: nearside (acquired by Plastiq in 2022)
and captions (renamed Mirage, an unpriced 2026 financing).
"""
import json
import os

import judge_lib as jl
from judge_lib import NEWS, cls, rnd

INV = jl.INV
_C = json.loads((INV / "companies/classification.json").read_text())
_C = _C.get("kleiner-perkins", _C)
_R = json.loads((INV / "companies/resolved.json").read_text())
_R = _R.get("kleiner-perkins", _R)
ASOF = "2026-09-30"


def row(slug):
    return {**_R.get(slug, {}), **_C.get(slug, {})}


def rounds(slug):
    return [dict(r) for r in (row(slug).get("funding_rounds") or [])]


def rsrc(slug, date_prefix):
    """The source URL of the row's own recorded round dated `date_prefix` (read from disk, never typed)."""
    m = {r["source"] for r in rounds(slug) if str(r.get("date") or "").startswith(date_prefix)
         and str(r.get("source") or "").startswith("http")}
    if len(m) != 1:
        raise SystemExit(f"rsrc({slug!r}, {date_prefix!r}) matched {len(m)}")
    return m.pop()


def wv(url=None, asof=None):
    d = {"valuation_range_source": "web_verified"}
    if url:
        d["valuation_citation"] = url
    if asof:
        d["valuation_asof"] = asof
    return d


def chk(surface="Google News"):
    return f"Checked {ASOF} for a priced round at $1B or more: none found ({surface})"


L = []


def add(slug, tail, extra=None, surface="Google News", **kw):
    L.append(cls(slug, note=f"{chk(surface)}; {tail}", extra=extra, **kw))


# ---- balerion: the seed is the only round; citybiz places the company
add("balerion", "the $6M seed of April 2026 led by Kleiner Perkins is the only round found (Axios, citybiz, Pulse 2.0). "
    "citybiz (2026-04-17) calls the company San Francisco-based.",
    wv(rsrc("balerion", "2026-04-17"), ASOF), city="San Francisco", city_src="web_verified")

# ---- browserbase: already cited by the grind; the check date added
add("browserbase", "the $40M Series B of June 2025 is the latest round (SiliconANGLE, the company's own post).",
    wv(asof=ASOF))

# ---- captions: renamed Mirage; the 2026 money is unpriced growth financing
cap_tc = NEWS("captions", "Mirage raises $75M to continue")
cap_c = NEWS("captions", "Captions Raises Series C to Invest")
add("captions", "the company renamed itself Mirage in September 2025, when TechCrunch put it at over $100M raised and a "
    "$500M valuation, and in March 2026 it took $75M of growth financing from General Catalyst's Customer Value Fund "
    "(TechCrunch, 2026-03-24), which carries no valuation; the $60M Series C of July 2024 stays the latest priced round.",
    wv(cap_tc, ASOF),
    rounds=rounds("captions") + [
        rnd("2024-07-09", "Series C", 60000000, lead=None, firm_in_round=None, source=cap_c, source_type="company"),
        rnd("2026-03-24", "Growth financing (unpriced, Customer Value Fund)", 75000000, lead="General Catalyst",
            firm_in_round=None, source=cap_tc, source_type="press")])

# ---- cartesia: a $100M round the grind did not have, price undisclosed
car = NEWS("cartesia", "Who is Karan Goel")
add("cartesia", "the founder announced $100M raised from Kleiner Perkins, Index Ventures, Lightspeed and NVIDIA in "
    "October 2025 (Hindustan Times, 2025-10-30), with no valuation given by the company or the press; vendor profiles "
    "call it the Series B and their estimates are not marks (Rule A).",
    wv(car, ASOF), surface="Google News and one web search",
    rounds=rounds("cartesia") + [
        rnd("2025-10", "Series B (so named by vendor profiles)", 100000000, lead=None, firm_in_round=True,
            source=car, source_type="press")])

# ---- discovery-loop: no closed priced round; needs_web_value stays
dl = NEWS("discovery-loop", "Livemint")
L.append(cls("discovery-loop", extra=wv(dl, ASOF), note=(
    f"Checked {ASOF} for a priced round at $1B or more: none closed (Google News and one web search). The first round "
    "announced on 2026-08-05, led by Radical Ventures and Khosla Ventures with Kleiner Perkins, disclosed no valuation; "
    "the roughly $1B at about $10B reported on 2026-08-13 was talks the company did not confirm, and the $50B of "
    "2026-09-11 is the target of a new round (Livemint and Reuters on Business Insider). Tech Funding News reads the "
    "$10B as the first round's price, which no other report confirms, so below_1b stays with needs_web_value until a "
    "round closes at a stated figure.")))

# ---- rows the grind already cited: the check is recorded, the date added where it was missing
add("engram", "the $98M of seed and Series A announced in June 2026 at a $600M valuation (Calcalist) is the latest; "
    "the Engram Lab listing headlines are a namesake.")
add("enterpret", "the $20.8M Series A of December 2024 led by Canaan is the latest round.", wv(asof=ASOF))

# ---- inworld: the 2023 round at $500M is the latest priced round
add("inworld", "the August 2023 round led by Lightspeed at a $500M valuation (Crunchbase News, Business Wire) is the "
    "latest priced round; the 2026 headlines are product news.",
    wv(NEWS("inworld", "Character-Creating Startup Inworld AI"), ASOF))

add("juna-ai", "the $7.5M seed of November 2024 is the only round found.")
add("mai", "the $25M seed of September 2025 is the only round found. The company's release of 2025-09-30 carries a "
    "San Francisco dateline (PR Newswire via Yahoo Finance).", city="San Francisco", city_src="web_verified")
add("manifest-os", "the $60M Series A of April 2026 at a $750M valuation (Bloomberg, Business Wire) is the latest "
    "round. Legal IT Insider (2026-04-28) calls the company New York-based, as the First Round row reads; the Menlo "
    "row's London does not match.", city="New York", city_src="web_verified")
add("maxima", "the $41M of seed and Series A announced in November 2025 (Business Wire, Reuters) is the latest, with "
    "no valuation disclosed.")
add("mine", "the $14.4M seed announced in June 2024, as Fizz, is the latest round.")
add("multiply", "the $23.5M Series A of March 2025 is the latest round, its price not disclosed.")

# ---- nearside: not private any more
S4 = "https://www.sec.gov/Archives/edgar/data/1837739/000119312522283900/d383265ds4.htm"
L.append(cls("nearside", status="acquired", rng="below_1b",
             extra={"valuation_range_source": "web_verified", "valuation_citation": S4,
                    "valuation_asof": "2022-09-08"},
             note=("A/B pass 2026-09-30: Plastiq acquired Nearside Business Corp. on 2022-09-08 (the Form S-4 of "
                   "Plastiq's SPAC partner: 'On September 8, 2022, Plastiq completed the Nearside acquisition'), so "
                   "the row is acquired, not private; Plastiq shut the Nearside service down later in 2022 and itself "
                   "went through Chapter 11 into Priority Technology in 2023. The $58M Series B of December 2021 was "
                   "the last round and no $1B mark exists.")))

add("nooks", "the $43M Series B of October 2024 is the latest round; the August 2026 headline is Nooks buying "
    "FullyRamped.")

jl.write("ab2a", L, record=not os.environ.get("DRY"))
