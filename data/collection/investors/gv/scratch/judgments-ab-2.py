#!/usr/bin/env python3
"""A/B pass (COLLECTION.md s7), private $1B+ rows (PRO-75, 2026-09-29). Pass B (ab-news.py: Google News after each
mark) found one exit: Salesforce completed its purchase of Fin, formerly Intercom, on 2026-09-14 (signed 2026-06-15
at about $3.6B), so the row is acquired. Pass A: five rows still carried the unicorn list's name-matched mark with
no citation (Rule A); each is pinned to its priced round's own announcement, read 2026-09-29."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

CHECK = "2026-09-29"
VR = {"valuation_range_source": "web_verified"}
cls = json.loads((jl.INV / "companies/classification.json").read_text())


def plus(slug, extra):
    return (cls.get(slug, {}).get("note") or "").rstrip() + " " + extra


FIN = "https://pulse2.com/salesforce-completes-acquisition-of-fin-to-expand-agentforce-customer-service-ai/"
L = [jl.cls("intercom", status="acquired", rng="below_1b",
            extra={"valuation_source": "web_verified", "valuation_citation": FIN, "valuation_asof": "2026-09-14"},
            note=plus("intercom", "A/B pass " + CHECK + ": the company renamed itself Fin in 2026; Salesforce signed a "
                      "definitive agreement to buy it for about $3.6B on 2026-06-15 (Salesforce's release) and "
                      "completed the purchase on 2026-09-14 (Pulse 2.0: 'Salesforce has completed its acquisition "
                      "of Fin, formerly Intercom'), so the row is acquired. ICONIQ's row still reads private at the "
                      "signed price."))]
PIN = [("checkr", 4600000000, "2021-09-01", "https://checkr.com/blog/checkr-raises-250-million-at-4-6-billion-valuation",
        "the $250M Series E at $4.6B (Checkr's own post, September 2021)"),
       ("homelight", 1600000000, "2021-09-02",
        "https://techcrunch.com/2021/09/02/homelight-closes-on-100m-series-d-at-a-1-6b-valuation-as-revenue-surges/",
        "the $100M Series D at $1.6B (TechCrunch, 2021-09-02); the later $115M (2022), $20M (2024) and $40M (2026) "
        "raises disclosed no valuation"),
       ("scandit", 1000000000, "2022-02-09",
        "https://www.scandit.com/blog/scandit-smart-data-capture-leader-150m-series-d-investment/",
        "the $150M Series D 'at a company valuation in excess of $1 billion' (Scandit's own release, 2022-02-09)"),
       ("headway", 2300000000, "2024-07-23", "https://www.mobihealthnews.com/news/headway-scores-100m-more-doubling-its-valuation-23b",
        "the $100M Series D at $2.3B (MobiHealthNews, 2024-07-23)"),
       ("vercel", 9300000000, "2025-09-30", "https://vercel.com/blog/series-f",
        "the Series F 'valuing our company at $9.3 billion' (Vercel's own post, 2025-09-30)")]
for s, usd, asof, cite, what in PIN:
    stale = asof < "2024-09-29"
    L.append(jl.cls(s, rng="10b_plus" if usd >= 1e10 else "1b_plus", usd=usd, val_src="web_verified", val_cite=cite,
                    asof=asof, flags=["stale"] if stale else (), clear=["unicorn_name_match"],
                    note=plus(s, "A/B pass " + CHECK + ": the mark is pinned from the unicorn list's name match to "
                              + what + "; a Google News search for a later round, sale or listing found none"
                              + (", so the mark is older than 24 months (stale)." if stale else ".")), extra=VR))
jl.write("ab-2", L)
