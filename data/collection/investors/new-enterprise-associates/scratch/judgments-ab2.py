"""A/B pass ab2 (PRO-100 NEA, COLLECTION.md s6 momentum slice, s7, s8 duty 6), 2026-09-30.

Part 1: every private row first seen since 2021 in AI, fintech, data infrastructure or dev tools (queue/ab2.json)
gets one mechanical check for a $1B+ priced round (scratch/ab-news.json plus nq.py queries under NQ_TAG=ab2). The
outcome is recorded either way: the latest round found is cited as valuation_range_source web_verified with the check
date, or the row keeps below_1b with a dated note that nothing was found.

Part 2 (duty 6): the unicorn list (current and former) re-intersected with loose names against every member row
(scratchpad/ab2/duty6.py, duty6b.py). Hits already banded belong to ab1 (private $1B+) or ab3 (public); exits are
settled in their notes; the four namesake hits without a settling note get one here.
"""
import json

import judge_lib as jl
from judge_lib import NEWS, cls

INV = jl.INV
_C = json.loads((INV / "companies/classification.json").read_text())
_C = _C.get("new-enterprise-associates", _C)
_R = json.loads((INV / "companies/resolved.json").read_text())
_R = _R.get("new-enterprise-associates", _R)


def row(slug):
    return {**_R.get(slug, {}), **_C.get(slug, {})}


def rounds(slug):
    return list(row(slug).get("funding_rounds") or [])


def rsrc(slug, date_prefix):
    """The source URL of the row's own recorded round dated `date_prefix` (read from disk, never typed)."""
    m = [r for r in rounds(slug) if str(r.get("date") or "").startswith(date_prefix) and
         str(r.get("source") or "").startswith("http")]
    if len(m) != 1:
        raise SystemExit(f"rsrc({slug!r}, {date_prefix!r}) matched {len(m)}")
    return m[0]["source"]


CHK = "Checked 2026-09-30 for a priced round at $1B or more: none found (Google News)"
ASOF = "2026-09-30"


def wv(url, asof=True):
    d = {"valuation_range_source": "web_verified", "valuation_citation": url}
    if asof:
        d["valuation_asof"] = ASOF
    return d


L = []


def add(slug, tail, extra=None, **kw):
    L.append(cls(slug, note=f"{CHK}; {tail}", extra=extra, **kw))


# ---- rows that had no cited check: the latest round found is cited
add("ai-squared", "the latest priced round is the $13.8M Series A of April 2024.",
    wv(rsrc("ai-squared", "2024-04-17")))
add("august", "the $7M seed of August 2025 is the only round found; the other headlines under the name are about the month.",
    wv(rsrc("august", "2025-08-05")))
add("aurelian", "the $14M Series A of August 2025 is the latest round.", wv(rsrc("aurelian", "2025-08-27")))
add("backflip-ai", "the $30M Series A of December 2024 is the latest round; the 2026 items are product launches.",
    wv(rsrc("backflip-ai", "2024-12-19")))
add("centralize", "the $15M Series A of July 2026 is the latest round, no valuation disclosed.",
    wv(rsrc("centralize", "2026-07-29")))
add("ceramic", "the $12M seed of March 2025 is the only round found.", wv(rsrc("ceramic", "2025-03-05")))
add("flox", "the $25M Series B of September 2025 is the latest round; the 2026 Flox headlines are the Swedish wildlife company, a namesake.",
    wv(rsrc("flox", "2025-09")))
add("foresight", "the $5.5M seed of June 2025 is the only round found; the 2026 Foresight headlines are Foresight Autonomous and Foresight Group, namesakes.",
    wv(rsrc("foresight", "2025-06-26")))
add("functional-finance", "the $8M seed of August 2023 is the latest round.",
    wv(rsrc("functional-finance", "2023-08-03")))
add("genmo", "no round after the $30M Series A the firm's post announced in October 2024 was reported.",
    wv(rsrc("genmo", "2024-10-22")))
ga_ext = NEWS("golden-analytics", "lands $14M seed extension")
ga_rounds = rounds("golden-analytics")
for r in ga_rounds:
    if r.get("round") == "Seed extension" and not r.get("source"):
        r["source"] = ga_ext
        r["source_type"] = "press"
add("golden-analytics", "the $14M seed extension of June 2026 is the latest round.", wv(ga_ext), rounds=ga_rounds)
add("kira", "the $15M Series A of May 2023 is the latest round; the 2025 Kira seed headlines are a Latin American fintech and the 2026 ones a biotech, namesakes.",
    wv(NEWS("kira", "Kira Learning Raises $15M in Series A")))
add("latitude", "the $35M Series A of September 2026 is the latest round, and Fortune reports the CEO declined to give a valuation.",
    wv(NEWS("latitude", "Latitude, founded by Stripe and Uber alums")))
add("ledge", "the $9M seed of February 2023 is the latest round.",
    wv(NEWS("ledge", "Ledge aims to build automation tools")))
add("ledgy", "the EUR 22M Series B of September 2022 is the latest round.",
    wv(NEWS("ledgy", "Zurich-based Ledgy secures")))
add("lizzyai", "the $5M seed of December 2025 is the only round found.", wv(rsrc("lizzyai", "2025-12-02")))
add("martian", "the $9M seed of November 2023 is the latest priced round (Accenture's 2024 investment was unpriced).",
    wv(NEWS("martian", "tool automatically switches between LLMs")))
add("namespace", "the $23M of Seed and Series A announced in March 2026 is the latest round.",
    wv(rsrc("namespace", "2026-03-23")))
add("neo-cybernetica", "the $30M seed of February 2022 is the only round found.",
    wv(rsrc("neo-cybernetica", "2022-02-09")))
ng_url = NEWS("ng-cash", "NG CASH raises $15M")
add("ng-cash", "a $15M strategic round led by Blockchain Capital (Crypto Briefing, 2026-09-23) followed the 2025 Series B, with no valuation disclosed.",
    wv(ng_url), rounds=rounds("ng-cash") + [jl.rnd("2026-09-23", "Strategic (unnamed)", 15000000, lead="Blockchain Capital",
                                                   firm_in_round=None, source=ng_url, source_type="press")])
add("nitra", "the $187M of March 2026 is a $50M Series B plus the earlier $22M Series A, venture debt and a warehouse facility, and no report gives a valuation.",
    wv(rsrc("nitra", "2026-03-10")))
oh_url = NEWS("ohai", "Mental Load - PR Newswire")
add("ohai", "the August 2025 strategic investment led by Muse Capital is the latest round, amount and price undisclosed.",
    wv(oh_url), rounds=rounds("ohai") + [jl.rnd("2025-08-19", "Strategic (unnamed)", None, lead="Muse Capital",
                                                firm_in_round=None, source=oh_url, source_type="company")])
add("sundeck", "the $20M seed of 2023 is the only round found.", wv(rsrc("sundeck", "2023-05-31")))
add("tokenz", "the JPY 1B Series A of June 2026 (the company's release on PR Times) is the latest round.",
    wv(rsrc("tokenz", "2026-06-02")))
add("valarian", "the $50M Series A of July 2026 is the latest round; Fortune gives no valuation.",
    wv(NEWS("valarian", "help governments and enterprises escape")))
wv_ricoh = NEWS("weaviate", "Ricoh invests in AI-native vector database")
add("weaviate", "the $50M Series B of April 2023 is the latest priced round; Ricoh's June 2026 investment through its innovation fund was unpriced.",
    wv(rsrc("weaviate", "2023-04-21")),
    rounds=rounds("weaviate") + [jl.rnd("2026-06-16", "Strategic (unnamed)", None, lead="RICOH Innovation Fund",
                                        firm_in_round=None, source=wv_ricoh, source_type="company")])

# ---- rows already cited web_verified by the grind: the check is recorded; asof added where it was missing
add("clockwork", "the $20.5M round of September 2025 is the latest.")
add("corca", "the $7.8M seed of June 2026 is the latest round.")
add("corestory", "the $32M Series A of October 2025 is the latest round.", {"valuation_asof": ASOF})
add("crowdbotics", "the $40M Series B of January 2023 is the latest round.")
add("databento", "the $97M Series B of July 2026 is the latest round; the company's release and the press give no valuation.")
add("p-1", "the $50M Series A of July 2026 is the latest round; the release gives no valuation.")
add("payzen", "the $32M Series B of August 2024 is the latest priced round (the '$220 Million Growth Round' release dates from November 2022).")
add("quotewell", "the $12M of October 2025 is the latest round, valuation undisclosed.")
sam_url = NEWS("samaya-ai", "Secures New Investment from NVentures and Databricks Ventures")
add("samaya-ai", "the only later event is the February 2026 investment from NVentures and Databricks Ventures, unpriced.",
    {"valuation_asof": ASOF},
    rounds=rounds("samaya-ai") + [jl.rnd("2026-02-10", "Strategic (unnamed)", None, lead=None, firm_in_round=None,
                                         source=sam_url, source_type="company")])
add("second-front", "the $750M Series C mark of September 2024 stays the last priced round and keeps its stale flag; the 2026 items are deployment partnerships.")
add("snowplow", "the $40M Series B of June 2022 is the latest round; its 2025 purchase of Poplin Data raised nothing.",
    {"valuation_asof": ASOF})
add("spektr", "the $20M Series A of April 2026 is the latest round.", {"valuation_asof": ASOF})
add("twelvelabs", "the $100M Series B of July 2026 is the latest round; neither the release nor the press gives a valuation.")

# ---- no round of the company found at all: band kept below_1b, the dated note is the record
add("change-io", "no round of the company was reported at all.")
add("hos", "no round of the company was reported (the HoS headlines are Nigerian civil-service heads and Hornbeck Offshore, namesakes).")
add("prime-financial-technologies", "no round of the company was reported.")
add("sol", "no round of this Sol (meetsol.com) was reported; the September 2026 'Sol raises $4M' headlines are an email-assistant startup backed by General Catalyst, a namesake.")

# ---- duty 6: unicorn-list namesake hits with no settling note
D6 = "Unicorn list re-intersected 2026-09-30 (duty 6): "
L.append(cls("amber-therapeutics", note=D6 + "the listed Amber Group (Hong Kong, cryptocurrency) is a different company; no band."))
L.append(cls("shape-therapeutics", note=D6 + "the former-unicorn Shape Security (acquired by F5) is a different company; no band."))
L.append(cls("eucalyptus-systems", note=D6 + "the listed Eucalyptus Health (Australia) is a different company; this row exited to HP in 2014."))
L.append(cls("divvy", note=D6 + "the listed Divvy Homes is a different company; this row is the spend management company Bill.com bought in 2021."))

jl.write("ab2", L)
