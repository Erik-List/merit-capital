#!/usr/bin/env python3
"""A/B pass (COLLECTION.md 7), slice 3, chunk b: private rows. PRO-167, 2026-09-29.

Pass B searched each private row for a newer priced round or tender, a sale (signed vs
closed), a listing, a down round or a shutdown: Bing News (bq.py, cache
news-extra-bing-ab3.json) for every row, a web search for the stale marks. Rows with no
newer event and a sound citation carry no line.
Run: NQ_TAG=ab3 python3 ab3b.py
"""
import copy
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls, rnd, NEWS

L = []
WV = {"valuation_range_source": "web_verified"}
_CLS = json.loads((Path(__file__).resolve().parents[1] / "companies" / "classification.json").read_text())


def BURL(slug, title_sub, url_sub):
    """A Bing News item from this pass's cache (news-extra-bing-ab3.json) whose title and
    publisher URL both match; refuses a missing or ambiguous match."""
    d = json.loads((Path(__file__).resolve().parent / "news-extra-bing-ab3.json").read_text())
    m = {i["url"] for i in d.get(slug, [])
         if title_sub.lower() in i["title"].lower() and url_sub in i["url"]}
    if len(m) != 1:
        raise SystemExit(f"BURL({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(m)}")
    return m.pop()


def ROUNDS(slug):
    """The row's funding_rounds as recorded, copied, so a line that adds a round keeps them."""
    return copy.deepcopy(_CLS[slug].get("funding_rounds") or [])


# ---------------------------------------------------------------- stripe
# Stripe's own release of 2026-02-24 (printed by the pass's web search and read with curl:
# 'a tender offer at a $159B (EUR 135B) valuation').
STRIPE_REL = "https://stripe.com/newsroom/news/stripe-2025-update"
L.append(cls("stripe", rng="100b_plus", usd=159_000_000_000, val_src="web_verified", val_cite=STRIPE_REL,
             asof="2026-02-24", extra=WV,
             note="A/B pass 2026-09-29: the Payments Dive address cited here returns 'Page not found'; "
                  "re-cited to Stripe's own release of 2026-02-24 (a tender offer at a $159B (EUR 135B) "
                  "valuation, most of the funds from Thrive, Coatue, a16z and others). No later tender or round "
                  "found (Bing News, web search, 2026-09-29). The Coatue, ICONIQ, Khosla and Thrive rows cite the "
                  "same dead address."))

# ---------------------------------------------------------------- trm-labs
TRM_REL = NEWS("trm-labs", "TRM Labs Announces Series C Expansion at $2 Billion Valuation")
trm_r = ROUNDS("trm-labs")
for r in trm_r:
    if r.get("date") == "2026-02-04":
        r.update({"round": "Series C", "lead": "Blockchain Capital"})
trm_r.append(rnd("2026-09-09", "Series C extension", None, "Blockchain Capital", None, TRM_REL, "company"))
L.append(cls("trm-labs", rng="1b_plus", usd=2_000_000_000, val_src="web_verified", val_cite=TRM_REL,
             asof="2026-09-09", extra=WV, rounds=trm_r,
             note="A/B pass 2026-09-29: TRM announced on 2026-09-09 a Series C expansion valuing it at $2B, led "
                  "by Blockchain Capital (which also led the February Series C) with existing investors, size "
                  "not disclosed (the company's GlobeNewswire release; Fortune reported the same). The mark moves "
                  "from the $1B of February 2026; YC's row still reads $1B (same band, figure stale)."))

# ---------------------------------------------------------------- vanta
L.append(cls("vanta", rng="1b_plus", usd=4_150_000_000, val_src="web_verified",
             val_cite=NEWS("vanta", "Compliance startup Vanta valued at $4.15B"), asof="2025-07-23", extra=WV,
             note="A/B pass 2026-09-29: the CNBC citation gives 'roughly $4 billion'; the $4.15B figure is "
                  "re-cited to SiliconANGLE (Reuters and Bloomberg report the same). No later priced round found "
                  "(Bing News, web search, 2026-09-29); the mark is under 24 months old."))

# ---------------------------------------------------------------- weee
L.append(cls("weee", rng="1b_plus", usd=4_100_000_000, val_src="web_verified",
             val_cite=BURL("weee", "Weee! delivers second big funding round", "finance.yahoo.com/news/"),
             asof="2022-02-28", extra=WV, flags=["stale"],
             note="A/B pass 2026-09-29: the Business Journals page is paywalled and could not be read; the $4.1B "
                  "figure is re-cited to TechCrunch's report of the $425M Series E ('boosts Weee!'s valuation to "
                  "$4.1 billion', via Yahoo Finance). No later priced round, tender or down round found (Bing "
                  "News, web search, 2026-09-29), so the mark stands, stale. Lightspeed's row cites a vendor page "
                  "(Sacra) for the same figure."))

# ---------------------------------------------------------------- xendit
L.append(cls("xendit", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=NEWS("xendit", "Fintech startup Xendit achieves unicorn status"), asof="2021-09", extra=WV,
             flags=["stale"],
             note="A/B pass 2026-09-29: re-cited to GMA News (2021-09-16: the $150M Series C led by Tiger "
                  "'elevating its valuation to about $1 billion'); the former Forbes citation reports the May "
                  "2022 Series D, whose valuation was not disclosed (TechCrunch). At the band edge. No later "
                  "priced round found (Bing News, web search, 2026-09-29), so the mark stands, stale; the Accel, "
                  "Coatue and YC rows cite the same Forbes page."))

# ---------------------------------------------------------------- sidecar-health
SC_D = NEWS("sidecar-health", "Sidecar Health Secures $165M")
sc_r = ROUNDS("sidecar-health")
sc_r.append(rnd("2024-06-26", "Series D", 165_000_000, "Koch Disruptive Technologies", None, SC_D))
L.append(cls("sidecar-health", rounds=sc_r,
             note="A/B pass 2026-09-29: the $165M Series D of June 2024, led by Koch Disruptive Technologies, was "
                  "announced without a valuation (HIT Consultant; Tiger is not among the investors named), so the "
                  "January 2021 $1B mark stands, stale, at the band edge. Menlo's row reads below_1b with no "
                  "figure although Menlo joined that $1B round: the Menlo row is the side to align."))

# ---------------------------------------------------------------- snapdocs
L.append(cls("snapdocs",
             note="A/B pass 2026-09-29 (momentum slice): no priced round since the May 2021 Series D (Bing News, "
                  "web search); a 15% staff cut in July 2024. A data vendor's secondary-market estimate put the "
                  "company near $0.3B in August 2026, about 80% under the round; a vendor estimate is not a "
                  "priced event (Rule A), so the mark stands, stale, and the collapse signal is left for review. "
                  "The Sequoia and YC rows cite a vendor page (GetLatka) for the same $1.5B."))

# ---------------------------------------------------------------- sendbird
L.append(cls("sendbird",
             note="A/B pass 2026-09-29: no priced round since the April 2021 Series C (Bing News, web search). A "
                  "data vendor's secondary-market estimate put the company near $0.1B in August 2026, about 90% "
                  "under the round; not a priced event (Rule A), so the mark stands, stale, and the collapse "
                  "signal is left for review."))

# ---------------------------------------------------------------- scalapay
L.append(cls("scalapay",
             note="A/B pass 2026-09-29 (momentum slice): no priced equity round since the February 2022 Series B "
                  "(Bing News, web search); the EUR 70M EIB financing of December 2025 is a loan. Mark stands, "
                  "stale."))

# ---------------------------------------------------------------- tradingview
L.append(cls("tradingview",
             note="A/B pass 2026-09-29 (momentum slice): no priced round since the October 2021 round (Bing News, "
                  "web search); the secondary-market price estimates found are vendor figures, not marks (Rule A). "
                  "Mark stands, stale."))

# ---------------------------------------------------------------- scribe
L.append(cls("scribe",
             note="A/B pass 2026-09-29: no priced round after the November 2025 Series C (Bing News). Redpoint's "
                  "row for this company (its 2024 Series B entry) reads below_1b without that round: the Redpoint "
                  "row is the stale side. The Bangalore Scribe on YC's row and Dan Siroker's Scribe on First "
                  "Round's row are other companies."))

# ---------------------------------------------------------------- zip (focus left empty by the grind)
L.append(cls("zip", focus="SaaS",
             note="Focus filled in the A/B pass (the grind left it empty): procurement software, SaaS, as YC's "
                  "row reads. No priced round after the October 2024 Series D (Bing News, 2026-09-29); the mark "
                  "turns 24 months old on 2026-10-21."))

# ---------------------------------------------------------------- zipline (focus left empty by the grind)
L.append(cls("zipline", focus="Industrial & Robotics",
             note="Focus filled in the A/B pass (the grind left it empty): drone delivery, as the a16z, Felicis, "
                  "GV and Sequoia rows read. A/B pass 2026-09-29: the September 2026 reports of a raise of about "
                  "$1B at about $20B describe talks (Bloomberg, 2026-09-16); no closed round, so the January 2026 "
                  "mark stands."))

# ---------------------------------------------------------------- zuoyebang (focus left empty by the grind)
L.append(cls("zuoyebang", focus="Consumer & Marketplaces",
             note="Focus filled in the A/B pass (the grind left it empty): online tutoring sold to students and "
                  "families, as Coatue's row reads. A/B pass 2026-09-29: no priced round since the December 2020 "
                  "E+ (Bing News, web search); the April 2024 report of a confidential US IPO filing (Bloomberg) "
                  "is not a price. Mark stands, stale."))

if __name__ == "__main__":
    jl.write("ab-3b", L)
