#!/usr/bin/env python3
"""Cross-investor alignment batch, 2026-09-03 (COLLECTION.md §10 invariant 10).

The first four runs (Sequoia, a16z, Accel, Lightspeed) classified alone, so
the same company read differently across investors. This file is the one
reproducible record of how every disagreement `run.py verify` reported was
resolved: which side was stale, what the current evidence is, and the
citation. It emits one record batch per investor into
`investors/<slug>/scratch/queue/cross-align-2026-09-03.jsonl`, which is then
recorded with `run.py record` (the validating gate), exported and verified.

Resolution rule (the playbook, not a new one): status is current-state; an
acquired/defunct row carries no value; a private row carries its last primary
mark unless documented collapse evidence supersedes it; a public row carries
a cited market cap. Where two runs held different marks for one company the
fresher, cited one won; where both public rows were stale the cap was
re-read on 2026-09-03 for both. Homonyms and thin unresolved pairs are ruled
in data/collection/cross-investor.json, not here.

Rows raised into a $1B+ band whose entry stage has no class-1/2 evidence get
`cite_pending` (verify invariant 4), computed from the investor's own merged
record so the debt marker is never added where a citation already exists.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from run import merge_rows, range_of  # noqa: E402

INV = ROOT / "data" / "collection" / "investors"
WHO = "cross-investor-align-2026-09-03"
TAG = "cross-investor alignment 2026-09-03"

SA = "https://stockanalysis.com/stocks/{t}/market-cap/"


def retire(slug, status, note):
    """Acquired / defunct: no standalone value (§6)."""
    return {"slug": slug, "status": status, "valuation_usd": None,
            "valuation_asof": None, "valuation_source": None,
            "valuation_citation": None, "valuation_range": "below_1b",
            "is_public": False, "note": f"{note} [{TAG}]"}


def mark(slug, status, usd, asof, cite, note, stale=False, clear=()):
    rec = {"slug": slug, "status": status, "valuation_usd": usd,
           "valuation_asof": asof, "valuation_source": "web_verified",
           "valuation_citation": cite, "valuation_range": range_of(usd),
           "valuation_confidence": "high", "note": f"{note} [{TAG}]"}
    if status == "public":
        rec["is_public"] = True
    if stale:
        rec["flags"] = ["stale"]
    if clear:
        rec["clear_flags"] = list(clear)
    return rec


def nomark(slug, note, clear=()):
    """Private, no sourced figure: below_1b without a number (§6)."""
    rec = {"slug": slug, "status": "private", "valuation_usd": None,
           "valuation_asof": None, "valuation_source": None,
           "valuation_citation": None, "valuation_range": "below_1b",
           "note": f"{note} [{TAG}]"}
    if clear:
        rec["clear_flags"] = list(clear)
    return rec


def status_only(slug, status, note):
    return {"slug": slug, "status": status, "note": f"{note} [{TAG}]"}


XAI = ("Absorbed into SpaceX in the Feb-2026 all-stock merger (announced "
       "2026-02-02, xAI at $250B; Axios, Yahoo Finance); the Jan-2026 $230B "
       "standalone mark is retired under the current-value rule (§6), as the "
       "Sequoia and a16z runs already had it. The value survives only inside "
       "SpaceX, which Lightspeed does not hold")
NTSK = ("Market cap $5.91B (stockanalysis, 2026-09-03; Nasdaq: NTSK, IPO Sep "
        "2025). The deterministic layer's $0 float was measured at the "
        "pre-IPO quarter end and was never a value (§6); same-day cap shared "
        "with Accel")
REFL = ("Reflection AI: $2B at $8B post-money (Oct 2025, TechCrunch), then the "
        "2026 round closed at a $25B pre-money per the CEO on CNBC "
        "(2026-04-23); the ~$2.5B size and ~$27.5B post-money are press-derived "
        "(WSJ), so the CEO-confirmed $25B is the recorded floor. Same mark on "
        "the Sequoia row")
FIRE = ("$1.5B Series D at $17.5B post-money (company blog 2026-07-15, "
        "BusinessWire/CNBC 2026-07-16; Atreides/Index/TCV led, Lightspeed "
        "participating); supersedes the Oct-2025 Series C $4B mark")
NOMI = ("$80M Series B-2 at $1B post-money led by Founders Fund (2026-03-05, "
        "press release; Lightspeed participating). Sequoia led the Jun-2025 "
        "$75M Series B with Lightspeed a significant participant, so the "
        "card's 'Series B, backed since 2025' stands")
ULTI = ("No post-money was ever disclosed for the 2022 ~$600M raise (Axios "
        "2022-06-01) or any later round; Tracxn/Caplight show no priced round "
        "2023-2026, and the $1B was an aggregator inference, not a source "
        "figure. below_1b without a figure, as the a16z run had it")

RECORDS = {
    # ------------------------------------------------------------- lightspeed
    "lightspeed": [
        retire("xai", "acquired", XAI),
        mark("netskope", "public", 5_910_000_000, "2026-09-03", SA.format(t="ntsk"), NTSK),
        mark("reflection", "private", 25_000_000_000, "2026-04",
             "https://www.cnbc.com/video/2026/04/23/reflection-ceo-on-ai-race-the-best-open-models-are-coming-from-china.html",
             REFL),
        mark("fireworks-ai", "private", 17_500_000_000, "2026-07-16",
             "https://fireworks.ai/blog/series-d-announcement", FIRE),
        mark("nominal", "private", 1_000_000_000, "2026-03-05",
             "https://www.globenewswire.com/news-release/2026/03/05/3250350/0/en/nominal-valued-at-1b-as-founders-fund-leads-80m-acceleration-round.html",
             NOMI),
        nomark("ultima-genomics", ULTI, clear=("stale",)),
        retire("delphix", "acquired",
               "Acquired by Perforce Software, announced 2024-02-14, closed 2024-03-25 "
               "(perforce.com press release); the card's 'Private' was stale"),
        retire("autograph", "acquired",
               "Merged into Future (digital fitness coaching) on 2025-01-23; Future is the "
               "surviving name and management (PR Newswire, TechCrunch 2025-01-23); the a16z "
               "run had it acquired"),
        retire("parsable", "acquired",
               "Acquired by CAI Software (an STG portfolio company) in September 2024 "
               "(parsable.com/news); resolves the 'trace thins after 2022-23' read"),
        status_only("all-day-kitchens", "defunct",
                    "Wound down through 2024 (the a16z run's A/B evidence: SF Chronicle "
                    "closures, listings marked closed, company unresponsive); aligned"),
        status_only("rockyou", "defunct",
                    "Chapter 7 liquidation 2019 (the Sequoia row); the card's 'acquired' was "
                    "the bankruptcy asset sale, not a surviving company; aligned"),
        {**mark("arena", "private", 1_700_000_000, "2026-01",
                "https://techcrunch.com/2026/01/06/lmarena-lands-1-7b-valuation-four-months-after-launching-its-product/",
                "Identity resolved: this Arena is LMArena (arena.ai, the Jan-2026 rebrand; "
                "Angelopoulos/Chiang/Stoica), the same company as the a16z row. Lightspeed "
                "participated in the $100M seed (May 2025, a16z/UC Investments-led) and the "
                "$150M Series A at $1.7B (2026-01-06, Felicis/UC Investments-led). The Arena "
                "Group float was a wrong-entity join, already disputed"),
         "hq_city": "San Francisco", "hq_city_source": "model_knowledge",
         "clear_flags": ["city_unknown"]},
        retire("flow", "acquired",
               "Identity resolved: this Flow is Flow Specialty (formerly Capitola, insurance "
               "wholesale brokerage; Lightspeed led the 2021 seed and joined the Apr-2023 "
               "Series A), not Adam Neumann's Flow. ReSource Pro acquired its technology, IP "
               "and team on 2026-06-24 (terms undisclosed); the card's 'Private' was stale"),
    ],
    # -------------------------------------------------------- sequoia-capital
    "sequoia-capital": [
        mark("waymo", "private", 126_000_000_000, "2026-02-02",
             "https://waymo.com/blog/2026/02/waymo-raises-usd16-billion-investment-round/",
             "Never acquired: an Alphabet-controlled subsidiary (majority investor) that "
             "raises priced external rounds; the $16B round at $126B post-money (2026-02-02) "
             "was co-led by Sequoia with Dragoneer and DST. 'acquired' retired under §6 "
             "(no acquisition event); aligned with a16z. Ruling proposed by the agent, "
             "Erik to confirm at re-ingest"),
        mark("grafana", "private", 9_000_000_000, "2026-02",
             "https://siliconangle.com/2026/02/13/grafana-labs-reportedly-raising-funding-9b-valuation/",
             "Grafana Labs: GIC-led round at ~$9B reported Feb 2026 (The Information, "
             "SiliconANGLE; Tracxn logs the $250M Series E 2026-02-25); last "
             "company-confirmed post-money $6B (Aug 2024, Lightspeed-led, Sequoia in). "
             "The below_1b read was a dedup remnant (Raintank) that never received a value; "
             "aligned with Lightspeed"),
        mark("harvey", "private", 11_000_000_000, "2026-03-25",
             "https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises",
             "$200M at $11B post-money co-led by GIC and Sequoia (2026-03-25; TechCrunch, "
             "CNBC); a $15.5B round reported in talks Aug 2026 is not closed. The below_1b "
             "read was a dedup remnant (Counsel AI) that never received a value; aligned "
             "with a16z"),
        mark("ethos", "public", 2_420_000_000, "2026-09-03", SA.format(t="life"),
             "Ethos Technologies IPO'd 2026-01-28 at $19 (Nasdaq: LIFE; Cooley deal note); "
             "market cap $2.42B (stockanalysis, 2026-09-03). The $351.8M was the cover-page "
             "public float, never a value (§6); same-day cap shared with Accel"),
        mark("doordash", "public", 96_350_000_000, "2026-09-03", SA.format(t="dash"),
             "Same-day cap shared with a16z: the two runs had straddled the $100B edge on "
             "as-of date alone ($91.9B vs $102.6B, both August 2026)"),
        mark("ironclad", "private", 3_200_000_000, "2022-01",
             "https://siliconangle.com/2022/01/18/digital-contract-management-startup-ironclad-raises-150m-3-2b-valuation/",
             "$150M Series E at $3.2B (Jan 2022, Franklin Templeton-led, all-insider incl. "
             "Sequoia and Accel); no primary since, so the mark is stale. As-of corrected "
             "from 2025-06 (an ARR remark, not a round); citation added; aligned with Accel",
             stale=True),
        mark("reflection-ai", "private", 25_000_000_000, "2026-04",
             "https://www.cnbc.com/video/2026/04/23/reflection-ceo-on-ai-race-the-best-open-models-are-coming-from-china.html",
             REFL.replace("Same mark on the Sequoia row", "Same mark on the Lightspeed row")),
        {"slug": "physical-intelligence",
         "valuation_citation": "https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/",
         "note": f"Citation added for the Nov-2025 $600M Series B at $5.6B (CapitalG-led); the "
                 f"~$11B 2026 round remains in talks, not closed (Bloomberg 2026-03-27). "
                 f"Aligned with Accel [{TAG}]"},
        retire("census", "acquired",
               "Acquired by Fivetran: definitive agreement 2025-05-01 (fivetran.com press); "
               "completion evidenced by getcensus.com redirecting to Fivetran and the product "
               "rebranded Fivetran Activations (close date not announced); the a16z run had it"),
        retire("replicate", "acquired",
               "Acquired by Cloudflare, announced 2025-11-17, closed 2025-12-01 for $57.4M "
               "total consideration (Cloudflare FY2025 10-K); the a16z run had it"),
        retire("stainless", "acquired",
               "Acquired by Anthropic, announced 2026-05-18 (anthropic.com; TechCrunch reports "
               ">$300M per The Information, unconfirmed); no closing notice found, so "
               "successor-entity ambiguity → acquired + note (§6); the a16z run had it"),
        retire("varagesale", "acquired",
               "Acquired by VerticalScope 2017-11-07 (BetaKit); the service runs on under "
               "Maxsold since early 2026. 'dormant-small private' was stale; the Lightspeed "
               "card had it acquired"),
        retire("bird", "defunct",
               "Bird Global: Chapter 11 2023-12-20, assets sold in a 363 credit bid to Third "
               "Lane Mobility (closed 2024-03-08), liquidating plan effective 2024-09-17 with "
               "equity receiving nothing; the VC-backed entity is defunct, the brand survives "
               "under a private owner. Same reading as Accel's bird-scooters row"),
        retire("iron-fish", "acquired",
               "Team acquired by Coinbase for Base (2025-03-06, CoinDesk/Coinbase blog); the "
               "chain and token continue under the Iron Fish Foundation, unaffiliated. "
               "Acqui-hire → acquired; same reading on the a16z row"),
        status_only("orchid-labs", "private",
                    "Orchid protocol and VPN app operating (orchid.com); no wind-down "
                    "evidence; aligned with a16z"),
    ],
    # ------------------------------------------------------------------- a16z
    "a16z": [
        mark("doordash", "public", 96_350_000_000, "2026-09-03", SA.format(t="dash"),
             "Same-day cap shared with Sequoia (the Aug-28 $102.6B close had it above the "
             "$100B edge; the Sequoia row read $91.9B the same month)"),
        mark("harvey", "private", 11_000_000_000, "2026-03-25",
             "https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises",
             "Source upgraded from unicorn_list to the round itself: $200M at $11B "
             "post-money co-led by GIC and Sequoia, a16z participating (2026-03-25); "
             "aligned with Sequoia"),
        nomark("lookout",
               "Last priced primary is the Aug-2014 Series F at '$1B-plus' (Bloomberg); "
               "superseded by documented collapse evidence (§6): consumer business sold to "
               "F-Secure for $223M EV (2023), cloud security business sold to Fortra (2025), "
               "secondaries ~$296M (Caplight, Dec 2024). below_1b, as the Accel run had it"),
        mark("unconventional-ai", "private", 4_500_000_000, "2025-12-09",
             "https://techcrunch.com/2025/12/09/unconventional-ai-confirms-its-massive-475m-seed-round",
             "$475M seed at $4.5B post-money co-led by a16z and Lightspeed (TechCrunch "
             "2025-12-09; Bloomberg 2025-12-08); no later close through 2026-09. The "
             "'round details undocumented' read missed a16z's own co-lead; aligned with "
             "Lightspeed"),
        mark("groupon", "public", 768_980_000, "2026-09-03", SA.format(t="grpn"),
             "Market cap replaces the Jun-2025 SEC float (§6: cap is canonical for public "
             "rows); same-day cap shared with Accel"),
        status_only("airtime", "defunct",
                    "Wound down (this run's own note: app wound down ~2023; the Sequoia row: "
                    "repeatedly relaunched, effectively wound down); aligned"),
        status_only("otter", "private",
                    "Otter (withotter.com): Sequoia-led $23M Series A (2021) with a16z as "
                    "seed investor; operating, no wind-down found; aligned with Sequoia"),
        status_only("pyn", "private",
                    "Operating (pynhq.com live, founders active 2025); aligned with Accel"),
        retire("parsable", "acquired",
               "Acquired by CAI Software (an STG portfolio company) in September 2024 "
               "(parsable.com/news); the Lightspeed row read the same"),
        status_only("ciridae", "private",
                    "Ciridae: $20M seed led by Accel with a16z and General Catalyst (Fortune "
                    "2026-05-11); operating; aligned with Accel"),
        retire("iron-fish", "acquired",
               "Team acquired by Coinbase for Base (2025-03-06, CoinDesk/Coinbase blog); the "
               "chain and token continue under the Iron Fish Foundation. Acqui-hire → "
               "acquired; same reading on the Sequoia row"),
        status_only("eon", "private",
                    "Identity resolved (medium confidence): this EON is Endeavor Optical "
                    "Networks (space-laser data-center links; $10.75M seed co-led by General "
                    "Catalyst and a16z, out of stealth 2026-08-04, TechCrunch), which "
                    "appeared on the a16z list after Feb 2026; not Eon the cloud-backup "
                    "company (no a16z round) and not the wikidata MX match"),
    ],
    # ------------------------------------------------------------------ accel
    "accel": [
        mark("captivateiq", "private", 1_250_000_000, "2022-01",
             "https://techcrunch.com/2022/01/26/captivateiq-raises-100m-at-a-1-25b-valuation/",
             "$100M Series C at $1.25B post-money (Jan 2022, ICONIQ/Accel/Sequoia-led); no "
             "primary since, so stale; aligned with Sequoia", stale=True),
        mark("ironclad", "private", 3_200_000_000, "2022-01",
             "https://siliconangle.com/2022/01/18/digital-contract-management-startup-ironclad-raises-150m-3-2b-valuation/",
             "$150M Series E at $3.2B (Jan 2022, Franklin Templeton-led, all-insider incl. "
             "Accel); no primary since, so stale; aligned with Sequoia", stale=True),
        mark("decagon", "private", 4_500_000_000, "2026-01",
             "https://www.bloomberg.com/news/articles/2026-01-28/ai-customer-support-startup-decagon-valued-at-4-5-billion",
             "$250M Series D at $4.5B (Jan 2026, Coatue/Index-led), tripling the Jun-2025 "
             "$1.5B Series C; aligned with a16z"),
        mark("falconx", "private", 8_000_000_000, "2022-06",
             "https://siliconangle.com/2022/06/22/institutional-crypto-assets-platform-falconx-raises-150m-8b-valuation/",
             "$150M Series D at $8B post-money (Jun 2022, GIC/B Capital); no primary since, "
             "so stale; aligned with Lightspeed", stale=True),
        mark("mux", "private", 1_000_000_000, "2021-04",
             "https://techcrunch.com/2021/04/30/mux-series-d/",
             "$105M Series D at $1B+ (Apr 2021, Coatue-led; exact post-money undisclosed, "
             "recorded at the $1B floor as the a16z row has it); stale", stale=True),
        mark("periodic-labs", "private", 1_300_000_000, "2025-09",
             "https://techcrunch.com/2025/09/30/former-openai-and-deepmind-researchers-raise-whopping-300m-seed-to-automate-science/",
             "$300M seed at $1.3B post-money (Sep 2025, a16z-led, Accel participating); a "
             "~$7B round reported in talks 2026 is not closed; aligned with a16z and "
             "Lightspeed"),
        mark("physical-intelligence", "private", 5_600_000_000, "2025-11",
             "https://www.therobotreport.com/physical-intelligence-raises-600m-advance-robot-foundation-models/",
             "$600M Series B at $5.6B post-money (Nov 2025, CapitalG-led); the ~$11B 2026 "
             "round remains in talks, not closed (Bloomberg 2026-03-27). Membership rests on "
             "Accel's own listing: no press names Accel in a PI round. Aligned with Sequoia"),
        mark("skydio", "private", 4_400_000_000, "2026-04",
             "https://www.skydio.com/blog/skydio-series-f",
             "$110M Series F at $4.4B (Apr 2026, existing investors), doubling the 2023 "
             "$2.2B; aligned with a16z"),
        mark("snorkel-ai", "private", 1_300_000_000, "2025-05-29",
             "https://www.hpcwire.com/bigdatawire/this-just-in/snorkel-ai-announces-100m-series-d-and-expanded-platform-to-power-next-phase-of-ai-with-expert-data/",
             "$100M Series D at $1.3B post-money (2025-05-29, Addition-led, Lightspeed "
             "participating; the company release as carried by BigDATAwire); aligned with "
             "Lightspeed"),
        mark("ethos", "public", 2_420_000_000, "2026-09-03", SA.format(t="life"),
             "Ethos Technologies IPO'd 2026-01-28 at $19 (Nasdaq: LIFE); market cap $2.42B "
             "(stockanalysis, 2026-09-03) supersedes the May-2022 $2.7B SoftBank mark; "
             "same-day cap shared with Sequoia", clear=("stale",)),
        mark("netskope", "public", 5_910_000_000, "2026-09-03", SA.format(t="ntsk"),
             "Same-day cap shared with Lightspeed (refreshed from the Aug-31 $6.18B read)"),
        mark("groupon", "public", 768_980_000, "2026-09-03", SA.format(t="grpn"),
             "Same-day cap shared with a16z (refreshed from the Aug-2026 $1.5B read); below "
             "the $1B band"),
        mark("lightspeed", "public", 1_350_000_000, "2026-09-03", SA.format(t="lspd"),
             "Lightspeed Commerce (NYSE/TSX: LSPD, not the venture firm): market cap $1.35B "
             "(stockanalysis, 2026-09-03); the row had no value at all"),
        retire("blameless", "acquired",
               "Acquired by FireHydrant, announced and closed 2024-08-21 (FireHydrant press "
               "release, BusinessWire); the Lightspeed row had it"),
        retire("split", "acquired",
               "Split Software acquired by Harness, announced 2024-05-29, completed "
               "2024-06-11 (PR Newswire); the Lightspeed row had it"),
        retire("graphite", "acquired",
               "Acquired by Cursor (Anysphere): definitive agreement 2025-12-19 (cursor.com "
               "and graphite.com posts; TechCrunch: cash and equity, 'way over' the $290M "
               "mark); no closing notice found but graphite.com now routes sales to "
               "cursor.com and the a16z page marks it acquired → acquired + note (§6)"),
        retire("despegar", "acquired",
               "Acquired by Prosus at $19.50/share (~$1.7B), announced 2024-12-23, completed "
               "2025-05-15 and delisted from NYSE (Prosus release, SEC 6-K); 'NYSE: DESP' was "
               "stale; the Sequoia row had it"),
        retire("brightcove-inc", "acquired",
               "Acquired by Bending Spoons at $4.45/share (~$233M), announced 2024-11-25, "
               "closed 2025-02-04 and delisted from Nasdaq (Brightcove pressroom); 'still "
               "listed' was stale"),
        retire("rovio", "acquired",
               "Acquired by Sega via tender offer (~EUR 706M), completed 2023-08-17, delisted "
               "from Nasdaq Helsinki Dec 2023 (Sega Sammy release); 'HEL: ROVIO' was stale"),
        retire("remedy-corporation", "acquired",
               "Acquired by Peregrine Systems, completed 2001-08-26 (~$1.2B), the unit then "
               "sold to BMC in 2002; 'NASDAQ: RMDY' was two decades stale"),
        retire("uunet-technologies", "acquired",
               "Acquired by MFS Communications, effective 1996-08-12 (~$2B stock), MFS into "
               "WorldCom 1996-12-31; 'NASDAQ: UUNT' was three decades stale"),
        retire("bird-scooters", "defunct",
               "Bird Global: Chapter 11 2023-12-20, assets sold in a 363 credit bid to Third "
               "Lane Mobility (closed 2024-03-08), liquidating plan effective 2024-09-17 with "
               "equity receiving nothing; the OTC quote was the liquidating shell. Same "
               "reading as the Sequoia bird row"),
        retire("datagravity-inc", "acquired",
               "Assets acquired by HyTrust in 2017 (the a16z row); the 'dark row' read is "
               "resolved as an acquisition"),
    ],
}

# rows whose stale/float flags are cleared because the value they described is gone
CLEAR_ON_RETIRE = {"graphite": ["stale"], "brightcove-inc": ["stale"], "bird": ["stale"]}


def main() -> None:
    total = 0
    for inv, recs in RECORDS.items():
        base = json.loads((INV / inv / "base.json").read_text())
        resolved = json.loads((INV / inv / "resolved.json").read_text())
        cls = json.loads((INV / inv / "classification.json").read_text())
        merged = merge_rows(base, resolved, cls)
        slugs = {r["slug"] for r in base}
        out = []
        for rec in recs:
            assert rec["slug"] in slugs, f"{inv}: {rec['slug']} not in base"
            cur = merged.get(rec["slug"], {})
            rec["who"] = WHO
            # invariant 4: a $1B+ row needs class-1/2 stage evidence or the debt marker
            if rec.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus"):
                cited = bool((cur.get("entry_stage_citation") or "").strip()) \
                    or cur.get("entry_stage_source") in ("formd_structural", "formd_band")
                if not cited:
                    rec["flags"] = sorted(set(rec.get("flags") or []) | {"cite_pending"})
            if rec["slug"] in CLEAR_ON_RETIRE and rec.get("status") in ("acquired", "defunct"):
                rec["clear_flags"] = sorted(set(rec.get("clear_flags") or [])
                                            | set(CLEAR_ON_RETIRE[rec["slug"]]))
            out.append(rec)
        dest = INV / inv / "scratch" / "queue" / "cross-align-2026-09-03.jsonl"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n".join(json.dumps(r) for r in out) + "\n")
        print(f"{inv}: {len(out)} records -> {dest.relative_to(ROOT)}")
        total += len(out)
    print(f"total {total}")


if __name__ == "__main__":
    main()
