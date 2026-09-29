#!/usr/bin/env python3
"""PRO-167 Tiger Global, adversarial A/B pass (COLLECTION.md 7), slice 1, chunk b: the private rows.

Pass A checks that each recorded mark rests on a cited priced event; pass B looks for anything newer (a priced round
or tender, a sale, an IPO, a down round, a shutdown). Surfaces: Bing News (bq.py storage, NQ_TAG=ab1: two to four
queries per row, 2026-09-29), WebFetch of the cited and newer articles, and web search for the rows Bing left thin
(ByteDance, Ankorstore, 1Password, Automattic, ActiveCampaign, Bitso, FalconX, Blockdaemon, Clubhouse, Cribl, Flock
Safety, AngelList, Chargebee, ClickUp, CoinSwitch, Apna). Rows with no newer event and a sound citation need no line;
a note-only line records what the check found where it bears on the mark. Secondary sales and fund marks go in the
note, never in the mark.
Run: NQ_TAG=ab1 python3 ab1b.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls

HERE = Path(__file__).resolve().parent
CLS_ON_DISK = json.loads((HERE.parent / "companies" / "classification.json").read_text())
WV = {"valuation_range_source": "web_verified"}


def B(slug, title_sub, url_sub=""):
    """The one publisher URL among the row's cached news items (news-extra*.json) whose title contains
    `title_sub` and whose URL contains `url_sub`."""
    items = []
    for f in sorted(HERE.glob("news-extra*.json")):
        items += json.loads(f.read_text()).get(slug, [])
    us = list(dict.fromkeys(i["url"] for i in items if i.get("url") and not i.get("gid")
                            and title_sub.lower() in i["title"].lower() and url_sub in i["url"]))
    if len(us) != 1:
        raise SystemExit(f"B({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(us)}")
    return us[0]


def ONDISK(slug, key):
    """A key of this book's classification record for the row, read from disk."""
    v = (CLS_ON_DISK.get(slug) or {}).get(key)
    if not v:
        raise SystemExit(f"ONDISK({slug!r}, {key!r}) missing")
    return v


L = []

# ---------------------------------------------------------------- BigID (newer priced round, same band)
L.append(cls("bigid", rng="1b_plus", usd=1_000_000_000, val_src="web_verified",
             val_cite=B("bigid", "60M Growth Round for Unicorn BigID", "prnewswire.com"), asof="2024-03-18",
             extra=WV, flags=("stale",),
             note="A/B 2026-09-29: a newer priced round than the 2020 Series D is on record: the $60M growth round "
                  "led by Riverwood Capital with Silver Lake Waterman and Advent, 'at over $1B in valuation' (the "
                  "company's release, 2024-03-18), figure written as $1.0B at the band edge (the April 2021 Series D "
                  "extension had stated $1.25B). Older than 24 months, so still stale; no later round or sale found "
                  "(Bing, 2026-09-29)."))

# ---------------------------------------------------------------- Cohere (newer priced round; merger and talks)
L.append(cls("cohere", rng="1b_plus", usd=7_000_000_000, val_src="web_verified",
             val_cite=B("cohere", "Cohere hits $7B valuation", "techcrunch.com"), asof="2025-09-24", extra=WV,
             note="A/B 2026-09-29: the $6.8B round of August 2025 was extended by $100M at $7B on 2025-09-24 "
                  "(TechCrunch), the latest priced round, so the mark moves to $7B. Cohere and Aleph Alpha announced "
                  "a merger on 2026-04-24 (Cohere holders about 90%, The Next Web) and signed the merger agreement on "
                  "2026-09-16 (SiliconANGLE); the combined company's $20B is a reported figure (Handelsblatt), and "
                  "the $2B-3B raise at about $20B was in advanced talks on 2026-09-11 (The Globe and Mail): reported "
                  "and in talks, not marks. The head office stays Toronto until the merger closes (Berlin and "
                  "Toronto after)."))

# ---------------------------------------------------------------- AngelList (post-money mark, rule 10)
L.append(cls("angellist", rng="1b_plus", usd=4_100_000_000, val_src="web_verified",
             val_cite=ONDISK("angellist", "valuation_citation"), asof="2022-03-08", extra=WV, flags=("stale",),
             note="A/B 2026-09-29: the mark is now the post-money $4.1B (the $100M on the $4B pre-money the cited "
                  "report states), the figure the GV row carries (rule 10). No later priced round found (Bing and "
                  "web search, 2026-09-29); AngelList bought Ark in July 2026."))

# ---------------------------------------------------------------- ByteDance (secondaries only since the buyback)
L.append(cls("bytedance",
             note="A/B 2026-09-29: the mark is the company's employee buyback of October 2025 at $200.41 a share, "
                  "about $330B (SCMP, via Yahoo Finance). The higher prices since are secondary sales between "
                  "investors: Bank of China Group Investment's stake sold to Capital Today at about $480B in November "
                  "2025 (SCMP) and General Atlantic marketing a stake at about $550B in February 2026 (PYMNTS); "
                  "secondary figures stay in the note. No newer company buyback or primary round found."))

# ---------------------------------------------------------------- Automattic (fund marks, no band change)
L.append(cls("automattic",
             note="A/B 2026-09-29: no priced round since the 2021 round at $7.5B. BlackRock's published fund marks "
                  "cut its Automattic stake by 10% in late 2024 (TechCrunch) and further since (a cumulative "
                  "markdown of about 63% on its 2021 price of $85 a share is reported), which would still leave the "
                  "company above $1B: a fund's fair-value mark, not a priced event, and no band change. The General "
                  "Catalyst and Insight rows still carry the 2019 round at $3B."))

# ---------------------------------------------------------------- 1Password (secondary at the same price)
L.append(cls("1password",
             note="A/B 2026-09-29: in October 2025 the founders sold $100M of shares in a secondary to the Halo Fund "
                  "and Flume Ventures that held the $6.8B of the 2022 round (BetaKit): no newer primary round and no "
                  "collapse, so the 2022 mark stands, stale."))

# ---------------------------------------------------------------- DispatchHealth (merger, still private)
L.append(cls("dispatchhealth",
             note="A/B 2026-09-29: Medically Home became part of DispatchHealth in a merger that closed on "
                  "2025-06-04 (the companies' release); the combined company keeps the DispatchHealth name and is "
                  "private. No priced round since the 2021 Series D, so that mark stands, stale."))

# ---------------------------------------------------------------- Blockdaemon (IPO pipeline, not listed)
L.append(cls("blockdaemon",
             note="A/B 2026-09-29: Blockdaemon is in Hong Kong's 2026 IPO pipeline (LSEG data of 2026-05-04, "
                  "Reuters) but is not listed; no priced round since the 2022 Series C, so that mark stands, stale."))

# ---------------------------------------------------------------- FalconX (confidential IPO filing, still private)
L.append(cls("falconx",
             note="A/B 2026-09-29: FalconX filed confidentially for a US IPO on 2026-05-28 (CoinDesk) and cut about "
                  "10% of its staff in August 2026 (The Straits Times); no priced round since June 2022, so the $8B "
                  "mark stands, stale."))

# ---------------------------------------------------------------- BharatPe (momentum check: debt only)
L.append(cls("bharatpe",
             note="A/B 2026-09-29, momentum check: no new equity round; BharatPe raised Rs 135 crore of debt in "
                  "September 2026 ahead of a planned IPO (MediaNama), so the 2021 mark stands, stale."))

# ---------------------------------------------------------------- Flock Safety (talks and stress, no priced event)
L.append(cls("flock-safety",
             note="A/B 2026-09-29: Axios reported in April 2026 that Flock was talking to investors about a new "
                  "round, and in August and September 2026 some 93 cities cancelled contracts and the company offered "
                  "staff buyouts (Yahoo Finance); no priced round or sale since March 2025, so the $7.5B mark "
                  "stands."))

if __name__ == "__main__":
    jl.write("ab-1b", L)
