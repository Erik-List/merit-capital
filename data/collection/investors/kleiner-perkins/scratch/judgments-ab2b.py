"""A/B pass ab2, second half (PRO-99 Kleiner Perkins; COLLECTION.md s6 momentum slice, s7, s8 duty 6), 2026-09-30.

Part 1: the momentum check for rows omnifold .. wisdom-ai of queue/ab2.json (see judgments-ab2a.py for the method).

Part 2 (duty 6): the unicorn list (current and former) re-intersected with loose names against every member row
(scratchpad/ab2/duty6.py: 57 exact hits after stripping .io/.ai/.com, Labs, HQ, Technologies and the like, 25 looser
prefix hits, and a sweep of the notes for renames). The banded private hits belong to ab1, the public ones to ab3,
the exits and the one namesake (pivotal) are settled in their notes already. One hit was not settled: the listed
Intercom is the row `fin` as well as the row `intercom`, and `fin` still read private at the signed price after the
sale closed.
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


def patched(slug, date_prefix, **kw):
    """The row's rounds with the one dated `date_prefix` updated by `kw`."""
    rs = rounds(slug)
    hit = [r for r in rs if str(r.get("date") or "").startswith(date_prefix)]
    if len(hit) != 1:
        raise SystemExit(f"patched({slug!r}, {date_prefix!r}) matched {len(hit)}")
    hit[0].update(kw)
    return rs


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


add("omnifold", "the company's own post of 2026-06-26 puts the $30M Series B at a $300M valuation, the latest round.",
    surface="Google News, no result under the name; the company's blog")
add("phia", "the $35M Series A of January 2026 at $185M is the latest priced round; Fortune still called it a "
    "$185 million startup in August 2026.")
add("planetscale", "the $50M Series C of November 2021 led by Kleiner Perkins is the latest round found, and no report "
    "prices it at $1B.", wv(rsrc("planetscale", "2021-11-16"), ASOF), surface="Google News, two queries")

# ---- poetic: the company's own release now read and cited; it places the company
add("poetic", "the company's release of 2026-06-10 puts the $50M Series A led by Kleiner Perkins at a $500M valuation, "
    "the latest round; it carries a San Francisco dateline and says Poetic was formerly known as Forge.",
    wv(NEWS("poetic", "Poetic Raises $50M Series A to Automate"), ASOF),
    city="San Francisco", city_src="web_verified")

add("reevo", "the $80M of seed and Series A at a $500M valuation (November 2025) is the latest round.")

# ---- roadrunner: the check the grind could not finish
add("roadrunner", "Fortune (2026-05-12) reports $27M raised in total across the seed Kleiner Perkins led and the "
    "Series A Founders Fund led, with no valuation; the company's release of the same day carries a San Francisco "
    "dateline.", wv(NEWS("roadrunner", "Exclusive: Roadrunner raises $27 million"), ASOF),
    city="San Francisco", city_src="web_verified")

# ---- rudderstack: the Series B gets its source
rs_tc = NEWS("rudderstack", "RudderStack raises $56M")
add("rudderstack", "the $56M Series B of February 2022 led by Insight Partners, with Kleiner Perkins participating "
    "(TechCrunch), is the latest round. The Insight row's New York does not match this row's San Francisco.",
    wv(rs_tc, ASOF),
    rounds=patched("rudderstack", "2022-02-02", source=rs_tc, source_type="press", firm_in_round=True))

add("sail-research", "the $80M of seed and Series A at a $450M valuation (June 2026) is the latest round.")

# ---- settle: the check the grind could not finish; the company's own site now gives a New York address
st = NEWS("settle", "US fintech start-up Settle closes")
add("settle", "the $60M Series B of November 2021 (FinTech Futures headline) is the latest round, and the company has "
    "announced only a credit facility and its purchase of Turbine since. Its own site (settle.com, read 2026-09-30) "
    "gives Settle Inc., 36 W 20th St, New York, which replaces the San Francisco of 2021 that the Ribbit row still "
    "carries.", wv(st, ASOF), city="New York", city_src="web_verified",
    rounds=rounds("settle") + [rnd("2021-11-24", "Series B", 60000000, lead=None, firm_in_round=None, source=st,
                                   source_type="press")])

add("summation", "the $35M announced in October 2025 is the latest funding.")

# ---- superblocks: the 2025 round gets its source; AlleyWatch places the company
sb = NEWS("superblocks", "Exclusive: Superblocks raises $23M")
add("superblocks", "the $23M Series A extension of May 2025, with Kleiner Perkins among the investors (SiliconANGLE), "
    "is the latest round, $60M raised in total and no valuation given; the August 2026 headlines are an AWS "
    "partnership. AlleyWatch (2025-06-02) covers the company as a New York startup, which settles the city.",
    wv(sb, ASOF), city="New York", city_src="web_verified",
    rounds=patched("superblocks", "2025-05-27", round="Series A extension", source=sb, source_type="press",
                   firm_in_round=True))

add("traversal", "the $48M of seed and Series A of June 2025 is the latest priced round; Amex Ventures' strategic "
    "investment of March 2026 was unpriced.")
add("trovy", "the $15M Series A of June 2026, $25M raised in all, is the latest round.")
add("ulucu", "no funding report at all.", surface="Google News, no result under the Latin or the Chinese name")
add("upyun", "no funding report at all.", surface="Google News, no result under the Latin or the Chinese name")
add("wisdom-ai", "the $50M Series A of November 2025 led by Kleiner Perkins and Nvidia is the latest round.")

# ---- duty 6: the one unicorn-list hit not yet settled
if row("fin").get("status") == "private":
    _G = json.loads((INV.parent / "gv" / "companies" / "classification.json").read_text())
    _G = _G.get("gv", _G)
    pulse = _G["intercom"]["valuation_citation"]
    assert pulse.startswith("https://pulse2.com/salesforce-completes-acquisition-of-fin"), pulse
    L.append(cls("fin", status="acquired", rng="below_1b",
                 extra={"valuation_range_source": "web_verified", "valuation_citation": pulse,
                        "valuation_asof": "2026-09-14"},
                 note=("Unicorn list re-intersected 2026-09-30 (duty 6): the listed Intercom is this company, which "
                       "the base also carries as the row intercom (one company, two rows). Salesforce completed its "
                       "purchase of Fin on 2026-09-14 (Pulse 2.0: 'Salesforce has completed its acquisition of Fin, "
                       "formerly Intercom'), so the row is acquired and the $3.6B signed price no longer bands it, "
                       "as the intercom row and the GV book already read.")))

jl.write("ab2b", L, record=not os.environ.get("DRY"))
