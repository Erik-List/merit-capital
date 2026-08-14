#!/usr/bin/env python3
"""Build the firm-level profile for an investor, plus its per-field source sidecar.

Reads  data/aggregation/entities/<slug>.json          (SEC vehicles)
       data/aggregation/sources/edgar/formd-sweep.json (Form D, partner-matched)
       data/aggregation/sources/wayback/partner-roster.json
       data/aggregation/company-base/<slug>.json
Writes data/aggregation/investors/institutions.json                 (ingest input)
       data/aggregation/investors/institutions/<slug>.sources.json  (provenance)

Everything an evidence layer can answer is computed here. Everything only the
open web can answer is declared in RESEARCHED below, each value carrying the URL
it came from. Nothing is written without a source: a field with no evidence is
null with a recorded reason.

Usage: python3 scripts/build-firm-profile.py [investor-slug]
"""
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGG = ROOT / "data" / "aggregation"
SLUG = sys.argv[1] if len(sys.argv) > 1 else "sequoia-capital"

# Sequoia's own SEC vehicles carry these name stems. Used to separate the firm's
# own filings from the portfolio-company filings in the same sweep.
OWN_VEHICLE_RE = re.compile(r"sequoia|scge", re.I)

# Vehicles that left with the June 2023 separation: China went to HongShan,
# India and Southeast Asia to Peak XV. Their funds are no longer this firm's.
DEPARTED_DESK_RE = re.compile(r"china|india|sea\b|southeast", re.I)

# Sequoia's own site sector tags -> the closed focus taxonomy in
# data/taxonomy/focus.json. Tags with no target are reported as a gap rather
# than forced into an approximate bucket.
FOCUS_CROSSWALK = {
    "ai": "AI & Applied AI",
    "infrastructure": "Data Infrastructure",
    "data-analytics": "Data Infrastructure",
    "networking": "Data Infrastructure",
    "storage": "Data Infrastructure",
    "search": "Data Infrastructure",
    "apps-services": "SaaS",
    "operations": "SaaS",
    "productivity": "SaaS",
    "gtm": "SaaS",
    "marketing": "SaaS",
    "legal": "SaaS",
    "developer-tools": "DevTools & APIs",
    "dev-tools": "DevTools & APIs",
    "fintech": "Fintech & Payments",
    "financial": "Fintech & Payments",
    "crypto": "Fintech & Payments",
    "hardware": "Industrial & Robotics",
    "devices": "Industrial & Robotics",
    "climate": "Climate & Energy",
}

# A focus label needs this many crosswalked companies to be published. Below it
# the signal is a rounding error on a 1,293-row base.
FOCUS_MIN_COMPANIES = 25

# Recognition-first selection from the confirmed base, per PRO-7. Membership is
# evidence-bound (every name is asserted against auto_confirmed rows below);
# which of them are famous is judgement, and is recorded as such.
NOTABLE_PICKS = [
    "Airbnb", "Apple", "Google", "Nvidia", "PayPal", "Stripe", "WhatsApp", "YouTube",
]

# Web-sourced values. Each carries the URL it came from; none may be written
# from memory. Keyed field -> (value, source, basis).
RESEARCHED = {
    "name": ("Sequoia Capital", "https://www.sequoiacap.com/", "firm site"),
    "website": ("https://www.sequoiacap.com", "https://www.sequoiacap.com/", "firm site"),
    "icon_url": (
        "https://www.sequoiacap.com/favicon.ico",
        "https://www.sequoiacap.com/favicon.ico",
        "favicon fetch, verified HTTP 200 image/x-icon",
    ),
    "founding_year": (1972, "https://sequoiacap.com/our-history/", "firm site, stated"),
    "history": (
        "Founded by Don Valentine in 1972. Its first $3 million fund backed both "
        "Apple and Atari.",
        "https://sequoiacap.com/our-history/",
        "firm site, paraphrased from stated facts",
    ),
    "investment_concept": (
        "We help the daring build legendary companies.",
        "https://www.sequoiacap.com/",
        "firm site, verbatim tagline",
    ),
}

# --- AUM: multi-source, anchored on the firm's own sworn filing. -----------
# Item 5.F of the Form ADV for Sequoia Capital Operations, LLC (CRD 157373,
# SEC 801-122957, filed 2026-07-17): regulatory AUM $82,165,771,068 across 60
# discretionary accounts. Press corroboration: ~$85B (2026). SCGE (Sequoia
# Capital Global Equities) is a SEPARATE registered adviser (801-73468, RAUM
# $10.4B) and is excluded here, as are its funds below.
AUM_VALUE = {"bottom": 82_165_771_068, "top": 85_000_000_000}
AUM_SOURCES = [
    ("https://adviserinfo.sec.gov/firm/summary/157373",
     "Form ADV Item 5.F, Sequoia Capital Operations LLC, filed 2026-07-17: "
     "RAUM $82,165,771,068 (60 accounts, all discretionary). Filing-grade."),
    ("https://www.bloomberg.com/news/articles/2025-02-06/sequoia-capital-s-evergreen-fund-grows-to-almost-20-billion",
     "Bloomberg 2025-02-06: evergreen Sequoia Capital Fund alone at $19.6B."),
    ("https://valueaddvc.com/blog/sequoia-capital-portfolio-2026-biggest-bets-biggest-wins-and-what-theyre-investing-in-now",
     "2026 press estimate: ~$85B AUM. Not filing-grade; used as the top."),
]

# --- Funds: curated last-10-years list. -------------------------------------
# The mechanical Form D derivation cannot produce this list alone: since the
# 2021 restructure, LP capital enters through the evergreen Sequoia Capital
# Fund and the strategy sub-funds' own Form Ds show only principals' side
# money. So sizes come from Form D where the vehicle raised directly, and from
# press where the size is an allocation under the evergreen. Every entry
# carries its sources; entries with an accession are asserted against
# data/aggregation/sources/edgar/fund-formds.json at build time.
TC_2026_EXPANSION = "https://techcrunch.com/2026/04/16/new-leaders-new-fund-sequoia-has-raised-7b-to-expand-its-ai-bets/"
TC_2025_EARLY = "https://techcrunch.com/2025/10/27/sequoia-unveils-950m-in-new-early-stage-funds-as-it-strives-to-be-only-as-good-as-our-next-investment/"
TC_2023_CUTS = "https://techcrunch.com/2023/07/28/sequoia-cuts-crypto-and-ecosystem-funds/"
INFO_2022_PAIR = "https://www.theinformation.com/articles/sequoia-capital-targets-2-25-billion-for-two-u-s-vc-funds"
FORMDS = "data/aggregation/sources/edgar/fund-formds.json"

RESEARCHED_FUNDS = [
    {"name": "Sequoia Capital Fund, L.P.", "size": 22_722_245_832, "vintage": 2022,
     "accession": "0002062357-26-000016",
     "sources": [(FORMDS, "Form D/A 2026: $22,722,245,832 sold. Evergreen umbrella; "
                  "includes rolled-up public positions."),
                 ("https://www.bloomberg.com/news/articles/2025-02-06/sequoia-capital-s-evergreen-fund-grows-to-almost-20-billion",
                  "Bloomberg 2025-02-06: $19.6B and growing, same trajectory.")]},
    {"name": "Sequoia Capital Global Growth Fund III - Endurance Partners, L.P.",
     "size": 8_004_500_000, "vintage": 2018, "accession": "0001740907-21-000002",
     "sources": [(FORMDS, "Form D/A: $8,004,500,000 sold."),
                 ("https://techcrunch.com/2018/06/26/confirmed-sequoia-has-already-secured-three-quarters-of-what-will-be-an-8-billion-global-fund/",
                  "TechCrunch 2018: the $8B global growth vehicle.")]},
    {"name": "Sequoia Capital Expansion Fund (2026)", "size": 7_000_000_000, "vintage": 2026,
     "sources": [(TC_2026_EXPANSION, "TechCrunch 2026-04-16 (citing Bloomberg): ~$7B "
                  "for the late-stage expansion strategy, US and Europe."),
                 ("https://www.privateequitywire.co.uk/sequoia-raises-about-7bn-for-new-expansion-fund-under-fresh-leadership/",
                  "Private Equity Wire: same figure independently. No Form D on "
                  "EDGAR yet; legal vehicle name unconfirmed.")]},
    {"name": "Sequoia Capital Expansion Fund I", "size": 3_400_000_000, "vintage": 2022,
     "sources": [(TC_2026_EXPANSION, "TechCrunch 2026: names the 2022 predecessor at $3.4B."),
                 (FORMDS, "US/E Expansion I Principals Fund on EDGAR (first filed "
                  "2022-10) confirms the vehicle family and vintage.")]},
    {"name": "Sequoia Capital Global Growth Fund II, L.P.", "size": 1_999_500_000,
     "vintage": 2015, "accession": "0001656515-17-000001",
     "sources": [(FORMDS, "Form D/A 2017: $1,999,500,000 sold. First filed Dec 2015, "
                  "final close 2017; sits at the edge of the 10-year window.")]},
    {"name": "Sequoia Capital U.S. Growth Fund IX, L.P.", "size": 1_505_500_000,
     "vintage": 2020, "accession": "0001814893-21-000002",
     "sources": [(FORMDS, "Form D/A 2021: $1,505,500,000 sold."),
                 ("https://aum13f.com/fund/sequoia-capital-us-growth-fund-ix-lp",
                  "Independent filing mirror, same figure.")]},
    {"name": "Sequoia Capital Growth Fund X", "size": 1_500_000_000, "vintage": 2022,
     "sources": [(INFO_2022_PAIR, "The Information 2022: $1.5B target for the US "
                  "growth fund; closed July 2022 per follow-on coverage."),
                 (FORMDS, "US/E Growth X Principals Fund on EDGAR (2022-10) confirms "
                  "the vehicle. Size is the press target, not a Form D amount.")]},
    {"name": "Sequoia Capital U.S. Growth Fund VIII, L.P.", "size": 998_500_000,
     "vintage": 2018, "accession": "0001743290-19-000001",
     "sources": [(FORMDS, "Form D/A 2019: $998,500,000 sold."),
                 ("https://news.crunchbase.com/venture/sequoia-capital-filings-disclose-nearly-3-35b-for-new-funds-focused-on-the-u-s-and-china/",
                  "Crunchbase News 2019-12-03: $998.5M, 120 LPs. Exact match.")]},
    {"name": "Sequoia Capital Ecosystem Fund", "size": 900_000_000, "vintage": 2022,
     "sources": [(TC_2023_CUTS, "TechCrunch 2023-07-28: launched Feb 2022 at ~$900M, "
                  "halved to ~$450M in July 2023. Size shown is as raised.")]},
    {"name": "Sequoia Capital Venture Fund XVIII", "size": 750_000_000, "vintage": 2022,
     "sources": [(INFO_2022_PAIR, "The Information 2022: $750M target for the "
                  "earlier-stage fund of the July 2022 pair."),
                 (FORMDS, "US/E Venture XVIII Principals Fund on EDGAR (2022-10) "
                  "confirms the vehicle. Size is the press target.")]},
    {"name": "Sequoia Capital Venture Fund XIX", "size": 750_000_000, "vintage": 2025,
     "sources": [(TC_2025_EARLY, "TechCrunch 2025-10-27: $750M early-stage fund "
                  "targeting Series A."),
                 (FORMDS, "Venture XIX Principals Fund on EDGAR (2026-04) confirms "
                  "the vehicle and vintage.")]},
    {"name": "Sequoia Capital U.S. Venture Fund XVII, L.P.", "size": 649_500_000,
     "vintage": 2020, "accession": "0001814910-21-000002",
     "sources": [(FORMDS, "Form D/A 2021: $649,500,000 sold."),
                 ("https://www.formds.com/issuers/sequoia-capital-u-s-venture-fund-xvii-l-p",
                  "Independent Form D mirror, same figure.")]},
    {"name": "Sequoia Capital Crypto Fund", "size": 585_000_000, "vintage": 2022,
     "sources": [(TC_2023_CUTS, "TechCrunch 2023-07-28: launched Feb 2022 at $585M, "
                  "cut to ~$200M in July 2023. Size shown is as raised.")]},
    {"name": "Sequoia Capital Seed Fund VI", "size": 200_000_000, "vintage": 2025,
     "sources": [(TC_2025_EARLY, "TechCrunch 2025-10-27: $200M seed fund."),
                 (FORMDS, "Seed VI Principals Fund on EDGAR (2026-04) confirms the "
                  "vehicle and vintage.")]},
]

# --- Investment range: three legs, per the PRO-7 continuation run. ----------
# (1) Form D round distribution: 368 portfolio companies, 1,125 partner-
#     attributed rounds in formd-issuer-rounds.json. Entry-round median
#     $7.79M (p10 $287K, p90 $89.4M). Rounds, not checks; but Sequoia's
#     high-ownership model makes the entry round a fair check proxy where it
#     leads.
# (2) Fund bands: Arc/seed checks $500K-$1M out of the seed fund (Forbes);
#     the fund ladder ($200M seed -> $750M venture -> $1.5B growth -> $7B
#     expansion) spans seed checks to late-stage positions.
# (3) Ceiling: largest verified single round led is Citadel Securities'
#     $1.15B (shared with Paradigm, split undisclosed); the $7B expansion
#     fund at a 10-15% concentration limit supports $700M-$1B per company.
#     The Aug 2026 "$10B AI commitment" is a strategy allocation, not a
#     check, and is deliberately not the ceiling.
RANGE_VALUE = {"lower_limit": 500_000, "median": 8_000_000, "upper_limit": 1_000_000_000}
RANGE_SOURCES = [
    ("data/aggregation/sources/edgar/formd-issuer-rounds.json",
     "Entry-round median $7,791,486 across 368 companies; median published as "
     "$8M. p10 $287K, p90 $89.4M, p99 (all rounds) $723M."),
    ("https://www.forbes.com/sites/kenrickcai/2023/01/18/sequoia-new-seed-fund-and-arc-expansion/",
     "Arc program: $500K-$1M checks out of the seed fund. The lower limit."),
    ("https://www.citadelsecurities.com/news-and-insights/citadel-securities-announces-1-15-billion-investment-from-sequoia-and-paradigm/",
     "Largest verified Sequoia-led round: $1.15B into Citadel Securities with "
     "Paradigm, Jan 2022; Sequoia's split undisclosed. Upper limit set at $1B."),
    ("https://techcrunch.com/2026/04/16/new-leaders-new-fund-sequoia-has-raised-7b-to-expand-its-ai-bets/",
     "Dry-powder check: the $7B expansion fund at typical concentration "
     "supports single positions of $700M-$1B, consistent with the ceiling."),
]

# Stage labels the firm's own companies listing uses, mapped to the canonical
# 14-value taxonomy. "Early" is the firm's own bucket; reading it as Series A
# and B is this run's interpretation and is flagged for review.
STAGE_VALUE = ["Pre-Seed", "Seed", "Series A", "Series B", "Growth", "Late Stage"]
STAGE_SOURCE = "https://www.sequoiacap.com/our-companies/"
STAGE_BASIS = (
    "firm's own listing filters (Pre-Seed/Seed, Early, Growth); Early read as "
    "Series A + Series B; Late Stage from the SCGE crossover vehicles in Form D"
)

# The June 2023 separation is what fixes geography: Sequoia Capital is the
# US/Europe partnership, HongShan is China, Peak XV is India and Southeast Asia.
GEO_VALUE = {"core": ["US", "Europe"], "other": ["Israel"]}
GEO_SOURCE = "https://www.cnbc.com/2023/06/06/sequoia-capital-to-split-apart-us-china-india-businesses.html"
GEO_BASIS = (
    "core from the June 2023 three-way separation; other from the 11 Israel-desk "
    "vehicles in the entities layer, which did not move to HongShan or Peak XV"
)


def load(*parts):
    return json.loads((AGG.joinpath(*parts)).read_text())


def own_formd_filings(sweep):
    """The firm's own fund filings, split from the portfolio companies."""
    out = defaultdict(list)
    for accession, rec in sweep.items():
        if OWN_VEHICLE_RE.search(rec["issuer"]):
            out[rec["issuer"]].append((accession, rec))
    return out


def fund_rows(own):
    """One row per fund: the largest amount sold, and the earliest filing year.

    total_offering reads "Indefinite" on every one of these, so the amount
    actually sold on the most recent amendment is the only number available.
    """
    rows = []
    for issuer, items in own.items():
        if DEPARTED_DESK_RE.search(issuer):
            continue
        best = max(items, key=lambda x: int(x[1]["total_sold"] or 0))
        year = min(2000 + int(a.split("-")[1]) for a, _ in items)
        rows.append({
            "name": issuer,
            "size": int(best[1]["total_sold"] or 0),
            "vintage": year,
            "_accession": best[0],
            "_city": f'{best[1]["city"].title()}, {best[1]["state"]}',
        })
    return sorted(rows, key=lambda r: -r["size"])


def hq_from_filings(own):
    """Issuer address on the firm's own filings. Filing-grade, and unanimous."""
    places = Counter(
        f'{r["city"].title()}, {r["state"]}' for items in own.values() for _, r in items
    )
    return places.most_common(1)[0], places


def current_people(roster, team):
    """The live team CMS is the source of record for membership, roles and
    socials; the Wayback roster is the historical cross-check. Position is the
    CMS title where the CMS has one; members the CMS files under its investing
    tabs (seed-early / growth) but leaves untitled are shown as "Partner",
    which is how the firm's own team page presents them. Operators without a
    title stay null.
    """
    latest = max(p["last_seen"] for p in roster)
    roster_names = {p["name"].lower() for p in roster if p["last_seen"] == latest}

    def position(m):
        if m.get("cms_title"):
            return m["cms_title"]
        if set(m.get("role_bucket", [])) & {"seed-early", "growth"}:
            return "Partner"
        return None

    def sort_key(m):
        investing = bool(set(m.get("role_bucket", [])) & {"seed-early", "growth"})
        return (0 if investing else 1, m["name"])

    people = [
        {"name": m["name"], "position": position(m),
         "socials": {"linkedin_url": m.get("linkedin_url"), "x_url": m.get("x_url")}}
        for m in sorted(team, key=sort_key)
    ]
    departed = sorted(n for n in roster_names
                      if n not in {m["name"].lower() for m in team})
    return latest, people, departed


def focus_from_site_tags(base):
    tags = Counter()
    for row in base:
        for tag in filter(None, (row.get("sector") or "").split(",")):
            tags[tag.strip()] += 1
    mapped, unmapped = Counter(), Counter()
    for tag, count in tags.items():
        target = FOCUS_CROSSWALK.get(tag)
        (mapped if target else unmapped)[target or tag] += count
    published = [f for f, c in mapped.most_common() if c >= FOCUS_MIN_COMPANIES]
    return published, mapped, unmapped


def verify_funds_against_filings(funds, fund_formds):
    """Every curated entry naming an accession must match the filed amount."""
    by_accession = {}
    for name, v in fund_formds.items():
        for f in v.get("filings", []):
            by_accession[f["accession"]] = (name, f.get("sold"))
    for fund in funds:
        acc = fund.get("accession")
        if not acc:
            continue
        if acc not in by_accession:
            raise SystemExit(f"Refusing to write: accession {acc} not in {FORMDS}")
        _, sold = by_accession[acc]
        if int(sold or 0) != fund["size"]:
            raise SystemExit(
                f"Refusing to write: {fund['name']} size {fund['size']:,} does not "
                f"match filed amount {int(sold or 0):,} on {acc}")


def main():
    entities = load("entities", f"{SLUG}.json")
    sweep = load("sources", "edgar", "formd-sweep.json")
    fund_formds = load("sources", "edgar", "fund-formds.json")
    roster = load("sources", "wayback", "partner-roster.json")
    team = load("sources", "site", "team-members.json")
    base = load("company-base", f"{SLUG}.json")

    own = own_formd_filings(sweep)
    funds = RESEARCHED_FUNDS
    verify_funds_against_filings(funds, fund_formds)
    (hq, hq_count), hq_places = hq_from_filings(own)
    latest_year, people, departed = current_people(roster, team)
    focus, mapped, unmapped = focus_from_site_tags(base)

    # Case-insensitive: the base carries the site's own casing ("Paypal",
    # "Youtube"), which is not how the names should be published.
    confirmed = {r["name"].lower() for r in base if r["status"] == "auto_confirmed"}
    missing = [n for n in NOTABLE_PICKS if n.lower() not in confirmed]
    if missing:
        raise SystemExit(f"Refusing to write: not confirmed in the base: {missing}")

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    row = {
        "slug": SLUG,
        "name": RESEARCHED["name"][0],
        "investor_type": "Institutional",
        "website": RESEARCHED["website"][0],
        "icon_url": RESEARCHED["icon_url"][0],
        "hq_location": hq,
        "founding_year": RESEARCHED["founding_year"][0],
        "history": RESEARCHED["history"][0],
        "investment_concept": RESEARCHED["investment_concept"][0],
        "investment_stage": STAGE_VALUE,
        "investment_geo": GEO_VALUE,
        "investment_scope": {"type": "Generalist", "focus": focus},
        "investment_range": RANGE_VALUE,
        "notable_investments": sorted(NOTABLE_PICKS),
        "aum": AUM_VALUE,
        "funds": {"funds": [
            {"name": f["name"], "size": f["size"], "vintage": f["vintage"]} for f in funds
        ]},
        "individuals": people,
        "updated_at": now,
    }

    def field(value, source, basis):
        return {"value": value, "source": source, "basis": basis}

    sources = {
        "slug": SLUG,
        "generated_at": now,
        "run": "PRO-7 autonomous in-session run",
        "fields": {
            "name": field(*RESEARCHED["name"]),
            "website": field(*RESEARCHED["website"]),
            "icon_url": field(*RESEARCHED["icon_url"]),
            "founding_year": field(*RESEARCHED["founding_year"]),
            "history": field(*RESEARCHED["history"]),
            "investment_concept": field(*RESEARCHED["investment_concept"]),
            "hq_location": field(
                hq,
                "data/aggregation/sources/edgar/formd-sweep.json",
                f"issuer address on {hq_count} of {sum(hq_places.values())} of the firm's "
                f"own Form D filings; unanimous. Filing-grade.",
            ),
            "investment_stage": field(STAGE_VALUE, STAGE_SOURCE, STAGE_BASIS),
            "investment_geo": field(GEO_VALUE, GEO_SOURCE, GEO_BASIS),
            "investment_scope": field(
                {"type": "Generalist", "focus": focus},
                "data/aggregation/company-base/%s.json" % SLUG,
                "focus from the firm's own site sector tags on %d base rows, crosswalked "
                "to data/taxonomy/focus.json, published above %d companies. Generalist "
                "because the firm's thesis names no single sector and the portfolio "
                "spans every published label." % (sum(mapped.values()), FOCUS_MIN_COMPANIES),
            ),
            "investment_range": field(
                RANGE_VALUE,
                RANGE_SOURCES[0][0],
                " | ".join(note for _, note in RANGE_SOURCES),
            ),
            "notable_investments": field(
                sorted(NOTABLE_PICKS),
                "data/aggregation/company-base/%s.json" % SLUG,
                "Membership asserted against auto_confirmed base rows. Selection among "
                "them is recognition judgement, per PRO-7. This is the one field not "
                "fully evidence-bound.",
            ),
            "aum": field(
                AUM_VALUE,
                AUM_SOURCES[0][0],
                " | ".join(note for _, note in AUM_SOURCES) +
                " | SCGE (Sequoia Capital Global Equities) is a separate registered "
                "adviser (801-73468, RAUM $10.4B) and is excluded, as are its funds.",
            ),
            "funds": field(
                [{"name": f["name"], "size": f["size"], "vintage": f["vintage"],
                  "sources": [{"source": s, "note": n} for s, n in f["sources"]]}
                 for f in funds],
                FORMDS,
                f"{len(funds)} funds, vintage 2015-2026. Direct raises carry Form D "
                "amounts asserted against the filings at build time; post-2021 "
                "strategy sub-funds carry press-stated sizes because LP capital "
                "enters through the evergreen Sequoia Capital Fund and their own "
                "Form Ds show only principals' side money.",
            ),
            "individuals": field(
                people,
                "https://sequoiacap.com/wp-json/wp/v2/team-member",
                f"Live team CMS: {len(people)} members. Positions are CMS titles "
                f"({sum(1 for p in people if p['position'] and p['position'] != 'Partner')} "
                f"explicit); untitled members under the investing tabs render as "
                f"'Partner', the site's own presentation. Socials scraped from "
                f"profile pages: {sum(1 for p in people if p['socials']['linkedin_url'])} "
                f"LinkedIn, {sum(1 for p in people if p['socials']['x_url'])} X.",
            ),
        },
        "flags": [
            {
                "field": "investment_scope.focus",
                "severity": "high",
                "note": "The closed focus taxonomy cannot express three of the firm's "
                        "largest tag clusters: " + ", ".join(
                            f"{t} ({c})" for t, c in unmapped.most_common(6)
                        ) + ". These companies are simply absent from the focus label. "
                        "PRO-22 shipped focus at 7 values; its own text proposed 12 "
                        "including Security, Healthcare and Consumer.",
            },
            {
                "field": "funds",
                "severity": "medium",
                "note": "Two caveats a reader should know: the Crypto Fund was cut from "
                        "$585M to ~$200M and the Ecosystem Fund halved to ~$450M in July "
                        "2023 (sizes shown are as raised), and Growth X / Venture XVIII "
                        "sizes are the targets The Information reported, closed July 2022 "
                        "but never confirmed at a different number. Global Growth II is "
                        "vintage 2015, at the edge of the 10-year window.",
            },
            {
                "field": "aum",
                "severity": "low",
                "note": "RAUM is gross regulatory assets, which can overstate net AUM; "
                        "the Jan 2025 press figure of $56B is superseded by the firm's "
                        "own 2026-07-17 ADV at $82.17B. SCGE's $10.4B sits outside both "
                        "the range and the fund list, deliberately.",
            },
            {
                "field": "investment_range",
                "severity": "medium",
                "note": "Median is the Form D entry-round median, a round-not-check "
                        "proxy justified by the firm's high-ownership entry model. The "
                        "$1B ceiling reads the $1.15B Citadel round (split with Paradigm "
                        "undisclosed) against the $7B expansion fund's concentration "
                        "capacity. The Aug 2026 '$10B AI commitment' is a strategy "
                        "allocation, not a check, and was deliberately not used.",
            },
            {
                "field": "investment_geo",
                "severity": "medium",
                "note": "Israel is inferred from 11 Israel-desk vehicles in the entities "
                        "layer, not from a current firm statement. Verify or drop.",
            },
            {
                "field": "investment_stage",
                "severity": "medium",
                "note": "The firm publishes 'Early', not Series A/B. Splitting it into two "
                        "canonical stages is this run's interpretation.",
            },
            {
                "field": "individuals",
                "severity": "medium",
                "note": f"'Partner' for untitled investing-tab members is the site's own "
                        f"presentation, not a stated title. {len(departed)} names from the "
                        f"{latest_year} Wayback roster are no longer on the live team page "
                        f"and were dropped: {', '.join(departed[:8])}"
                        + ("..." if len(departed) > 8 else "") + ". Roelof Botha's absence "
                        "is verified, not a scrape error: he stepped down as steward in Nov "
                        "2025 (Lin and Grady are co-stewards, per techcrunch.com/2025/11/04/"
                        "sequoia-names-alfred-lin-and-pat-grady-as-new-co-stewards-as-roelof-"
                        "botha-steps-down/) and the firm no longer lists him. Socials come "
                        "from profile-page links; members whose pages redirect to the "
                        "homepage have none.",
            },
        ],
    }

    inst = AGG / "investors" / "institutions.json"
    existing = json.loads(inst.read_text()) if inst.exists() else []
    existing = [r for r in existing if r.get("slug") != SLUG] + [row]
    existing.sort(key=lambda r: r.get("slug") or "")
    inst.parent.mkdir(parents=True, exist_ok=True)
    inst.write_text(json.dumps(existing, indent=2) + "\n")

    side = AGG / "investors" / "institutions" / f"{SLUG}.sources.json"
    side.parent.mkdir(parents=True, exist_ok=True)
    side.write_text(json.dumps(sources, indent=2) + "\n")

    print(f"hq            {hq}  ({hq_count}/{sum(hq_places.values())} filings)")
    print(f"funds         {len(funds)}  aum {AUM_VALUE}")
    print(f"individuals   {len(people)}  (current cohort {latest_year})")
    print(f"focus         {focus}")
    print(f"unmapped tags {[t for t, _ in unmapped.most_common(6)]}")
    print(f"\nwrote {inst.relative_to(ROOT)}")
    print(f"wrote {side.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
