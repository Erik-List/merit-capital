#!/usr/bin/env python3
"""One driver for the per-investor pipeline: membership and classification.

Subcommands:
  collect   run the deterministic EDGAR collector chain in dependency order
            (formd-query, edgar-entities, edgar-companies, and the Form D
            rescan once a base exists); site, wayback and partner-roster
            collection stay separate scripts because they carry judgment steps
  prepare   seed membership verdicts, run every deterministic layer, emit the
            one work queue (membership judgments + classification gaps)
  record    validate a batch's JSONL and merge it into the durable overlays;
            a line carrying "verdict" is a membership verdict, anything else
            is a classification row — one file may mix both
  status    coverage counts, derived from disk
  verify    assertion suite over base, membership and classification; exits
            non-zero with the rows that need fixing
  export    write the one merged CSV (the published per-investor surface)
  review    write the read-only review.html

Base and classification share one surface: `export` writes
data/collection/investors/<slug>/base.csv with identity, membership
verdict, evidence links and every classification column. A base that runs
without classification just leaves those fields empty. Durable state stays in
the overlays (base-verification.json, classification.json, identity-merges
.json); the CSV is derived from them in one merge step and is what
scripts/ingest-companies.ts reads.

Every path derives from the investor slug via scripts/paths.py, and every
investor-specific constant lives in the investor's config.json — nothing in
here is specific to one investor.

Two properties matter more than anything else here.

**The base is read live** from the investor's base.json. No pinned
snapshot; the rule is that the base is not rebuilt for an investor while that
investor's run is in flight. Overlays join on slug, so `verify` catches a
violation as drift between resolved.json keys and base slugs.

**Progress lives on disk, not in context.** The agent answering batches holds
one batch at a time and writes it back before taking the next, so an
interrupted run resumes at the first pending batch instead of restarting.

The rules the batches are judged under live in data/collection/COLLECTION.md
(plus the investor's own decisions.md next to its base); a session running
this pipeline reads that playbook first and re-reads it after any context
compaction.
"""
import argparse
import csv
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outcome_sources as S                                    # noqa: E402
from paths import ROOT, Paths                                  # noqa: E402

# Set in main() from the parsed investor slug; every path derives from them.
P: Paths
CFG: dict = {}
SAMPLE_SLUGS: set[str] = set()
UA = "Merit Capital research erik@meritcapit.al"

BATCH_SIZE = 45
CENSOR_MONTHS = 24

# Entry-round bands, in offering dollars. Deliberately coarse: Form D reports one
# amount and nothing else, so anything finer would be false precision. Reviewable
# because entry_offering_usd travels with the label.
STAGE_BANDS = ((1_000_000, "Pre-Seed"), (7_500_000, "Seed"), (30_000_000, "Series A"))
GRADUATION_MULTIPLE = 2.0
GRADUATION_FLOOR = 5_000_000

VALUATION_RANGES = ("below_1b", "1b_plus", "10b_plus", "100b_plus")
VALID_STAGES = {"Pre-Seed", "Seed", "Series A", "Growth"}
VALID_STATUS = {"private", "public", "acquired", "defunct", "unknown"}
VALID_CONF = {"high", "medium", "low"}
# Sources allowed to carry a dollar figure. `model_knowledge` is deliberately
# absent: the model classifies and disputes, but never mints a number. A figure
# the model believes in must be pinned by the web pass (-> web_verified) before
# it may appear.
VALUE_SOURCES = {"sec_public_float", "wikidata", "unicorn_list", "web_verified"}

# Membership ledger vocabularies (COLLECTION.md §2)
VERDICTS = {"member", "not_member", "uncertain"}
EVIDENCE = {"site_listing", "fund_filing", "formd_adjudicated", "knowledge", "web"}

# Closed focus vocabulary, owned by data/taxonomy/focus.json (the same twelve
# values the frontend and DB use). Never extended here: a company that does not
# fit any of them carries focus=None, which the distribution reports as
# "outside taxonomy" rather than being force-fitted into a near-miss bucket.
_FOCUS_FILE = ROOT / "data" / "taxonomy" / "focus.json"
VALID_FOCUS = set(json.loads(_FOCUS_FILE.read_text())["values"]) \
    if _FOCUS_FILE.exists() else set()

# hq_city is free text, not a closed vocabulary: the set of cities a portfolio
# touches is open and the frontend derives its options from the data. What IS
# constrained is the rendering — the bare municipality, no state or country
# suffix ("Palo Alto", never "Palo Alto, CA"), so city and country stay separate
# columns that a reader can group on.
CITY_SOURCES = {"formd_address", "model_knowledge", "web_verified"}
CITY_SUFFIX_RE = re.compile(r"[,/]|\s+\b([A-Z]{2}|USA|UK)\b\s*$")

US_STATES = {
    "ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO",
    "CONNECTICUT", "DELAWARE", "DISTRICT OF COLUMBIA", "FLORIDA", "GEORGIA",
    "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY",
    "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA",
    "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE",
    "NEW JERSEY", "NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA",
    "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA", "PUERTO RICO", "RHODE ISLAND",
    "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT",
    "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING",
}
# Business addresses in filing havens say nothing about where a company
# operates; fall through to the next country source instead.
OFFSHORE = {"CAYMAN ISLANDS", "VIRGIN ISLANDS, BRITISH", "BERMUDA",
            "MARSHALL ISLANDS", "BAHAMAS", "JERSEY", "GUERNSEY"}
COUNTRY_CANON = {
    "UNITED STATES": "United States", "UNITED STATES OF AMERICA": "United States",
    "United States of America": "United States", "USA": "United States",
    "UNITED KINGDOM": "United Kingdom", "UK": "United Kingdom",
    "Kingdom of the Netherlands": "Netherlands",
    "People's Republic of China": "China", "CHINA": "China",
    "KOREA, REPUBLIC OF": "South Korea", "Republic of Korea": "South Korea",
    "RUSSIAN FEDERATION": "Russia", "TAIWAN, PROVINCE OF CHINA": "Taiwan",
    "Republic of Ireland": "Ireland", "CZECHIA": "Czech Republic",
    "Czechia": "Czech Republic", "VIET NAM": "Vietnam",
    "UNITED ARAB EMIRATES": "United Arab Emirates", "HONG KONG": "Hong Kong",
}
# ISO 3166-1 alpha-2. `hq_country` is stored, validated and exported as the
# two-letter code; rendering a display name is the frontend's job. Keys are
# the canonical display names COUNTRY_CANON and the EDGAR title-casing
# produce. A name missing here passes through canon_country verbatim, so
# verify flags it instead of silently dropping the signal.
ISO_OF = {
    "United States": "US", "Canada": "CA",
    "United Kingdom": "GB", "Germany": "DE", "France": "FR",
    "Netherlands": "NL", "Sweden": "SE", "Switzerland": "CH", "Belgium": "BE",
    "Ireland": "IE", "Spain": "ES", "Italy": "IT", "Denmark": "DK",
    "Norway": "NO", "Finland": "FI", "Austria": "AT", "Poland": "PL",
    "Portugal": "PT", "Estonia": "EE", "Lithuania": "LT", "Latvia": "LV",
    "Czech Republic": "CZ", "Romania": "RO", "Bulgaria": "BG", "Hungary": "HU",
    "Greece": "GR", "Croatia": "HR", "Ukraine": "UA", "Russia": "RU",
    "Luxembourg": "LU", "Iceland": "IS", "Cyprus": "CY", "Malta": "MT",
    "Slovakia": "SK", "Slovenia": "SI", "Serbia": "RS",
    "Israel": "IL", "United Arab Emirates": "AE", "Saudi Arabia": "SA",
    "Bahrain": "BH", "Qatar": "QA", "Kuwait": "KW", "Jordan": "JO",
    "Lebanon": "LB", "Turkey": "TR", "Armenia": "AM",
    "China": "CN", "India": "IN", "Japan": "JP", "South Korea": "KR",
    "Singapore": "SG", "Hong Kong": "HK", "Taiwan": "TW", "Indonesia": "ID",
    "Vietnam": "VN", "Thailand": "TH", "Malaysia": "MY", "Philippines": "PH",
    "Pakistan": "PK", "Bangladesh": "BD", "Sri Lanka": "LK", "Kazakhstan": "KZ",
    "Brazil": "BR", "Mexico": "MX", "Argentina": "AR", "Colombia": "CO",
    "Chile": "CL", "Peru": "PE", "Uruguay": "UY", "Ecuador": "EC",
    "Costa Rica": "CR", "Panama": "PA", "Guatemala": "GT", "Venezuela": "VE",
    "Dominican Republic": "DO", "Bahamas": "BS",
    "Nigeria": "NG", "South Africa": "ZA", "Kenya": "KE", "Egypt": "EG",
    "Ghana": "GH", "Morocco": "MA", "Tunisia": "TN", "Ethiopia": "ET",
    "Senegal": "SN", "Rwanda": "RW", "Uganda": "UG",
    "Australia": "AU", "New Zealand": "NZ",
}
ISO_CODES = frozenset(ISO_OF.values())


# ---------------------------------------------------------------------------
# shared plumbing
# ---------------------------------------------------------------------------

def load_base(investor: str) -> list[dict]:
    """Rows of the live Company Base (no pinned snapshot; see module docstring).

    The evidence detail lives in base.json, written by
    build-company-base.py; the sibling base.csv is the merged published
    surface this driver derives, so it is never read back.
    """
    if not P.base_json.exists():
        sys.exit(f"no company base at {P.base_json}")
    return json.loads(P.base_json.read_text())


def merge_rows(rows: list[dict], resolved: dict, cls: dict) -> dict[str, dict]:
    """slug -> deterministic record overlaid with the batch classification.

    Flags are additive across layers: a batch answer must not be able to clear
    a deterministic flag (duplicate, boundary, ...) by emitting its own list.
    Everything else is a per-key override.
    """
    merged = {}
    for row in rows:
        det, overlay = resolved.get(row["slug"], {}), cls.get(row["slug"], {})
        rec = {**det, **overlay,
               "flags": sorted(set(det.get("flags") or [])
                               | set(overlay.get("flags") or []))}
        merged[row["slug"]] = rec
    return merged


def load_ledger(investor: str) -> tuple[dict, dict]:
    """-> (full ledger, this investor's verdicts dict, live reference)."""
    led = json.loads(P.ledger.read_text()) if P.ledger.exists() else {}
    bucket = led.setdefault(investor, {"verdicts": {}, "recall_additions": []})
    return led, bucket["verdicts"]

def save_ledger(led: dict) -> None:
    P.ledger.write_text(json.dumps(led, indent=1, sort_keys=True) + "\n")


def today() -> str:
    return date.today().isoformat()


def load(p: Path, default):
    return json.loads(p.read_text()) if p.exists() else default


def accs_of(row: dict) -> set[str]:
    """Partner-attributed Form D accessions of a base row."""
    return {a.strip() for a in (row.get("formd_accessions") or "").split(";")
            if a.strip()}


def evidence_class(r: dict) -> str:
    listed = bool(r["site_url"]) or bool(r["wayback_years"])
    filing = bool(r["edgar_forms"])
    formd = bool(r["formd_accessions"]) or bool(r["partners_formd"])
    if listed:
        return "listed"
    if filing:
        return "filing"
    if formd:
        return "formd_only"
    return "none"


def write_queue(prefix: str, items: list, size: int, jsonl: bool = False) -> int:
    """Replace scratch/queue/<prefix>-NNN.json with `items` chunked by `size`."""
    for f in P.queue.glob(f"{prefix}-*.json"):
        f.unlink()
    for i in range(0, len(items), size):
        chunk = items[i:i + size]
        text = ("\n".join(json.dumps(q) for q in chunk) + "\n") if jsonl \
            else json.dumps(chunk, indent=1)
        (P.queue / f"{prefix}-{i // size + 1:03d}.json").write_text(text)
    return (len(items) + size - 1) // size


# ---------------------------------------------------------------------------
# graduation, layer 1: deterministic Form D
# ---------------------------------------------------------------------------

def band_stage(offering: int | None) -> str | None:
    if not offering:
        return None
    for ceiling, label in STAGE_BANDS:
        if offering < ceiling:
            return label
    return "Growth"


def round_date(rnd: dict) -> str | None:
    """Sale date is the economic event; filing date is the fallback."""
    return rnd.get("sale_date") or rnd.get("filing_date") or None


def months_since(iso: str | None) -> int | None:
    if not iso:
        return None
    try:
        then = datetime.fromisoformat(iso[:10]).date()
    except ValueError:
        return None
    now = date.today()
    return (now.year - then.year) * 12 + (now.month - then.month)


def graduation_from_formd(rounds: list[dict], partner_accs: frozenset | set = frozenset()) -> dict:
    """Entry stage and graduation from a company's own Form D sequence.

    **Entry is anchored at the earliest partner-attributed round**, per PRO-6's
    original spec. The CIK rescan deliberately collects rounds the investor never
    touched (that is what makes the graduation test honest), but it also means
    the first round in the sequence may predate the investor: 23andMe's first
    filing is a 2009 $27.8M round, Sequoia's filings start 2017. Banding the
    first round would misstate the investor's entry stage entirely.

    Graduation is a *step-up* test rather than a named-round test: a later
    offering at least 2x the entry round and at least $5M. That is what the
    profile card actually claims ("completed an additional investment round after
    the initial investment"), and it survives across eras in a way that fixed
    "a Series A is $5-30M" bands do not.
    """
    priced = [r for r in rounds if r.get("offering_usd")]
    if not priced:
        return {"entry_stage": None, "seed_to_a_graduation": None,
                "graduation_source": "formd", "graduation_confidence": "low",
                "flags": []}

    priced.sort(key=lambda r: (round_date(r) or "", r.get("quarter") or ""))

    flags: list[str] = []
    entry_idx = next(
        (i for i, r in enumerate(priced)
         if partner_accs & set(r.get("accessions") or [r.get("accession")])),
        None)
    if entry_idx is None:
        # No partner filing among the priced rounds (partner was on an unpriced
        # filing, or attribution came from another source). First round is the
        # fallback, marked so review can see the anchor is inferred.
        entry_idx = 0
        if partner_accs:
            flags.append("entry_anchor_weak")

    entry = priced[entry_idx]
    entry_usd = entry["offering_usd"]
    stage = band_stage(entry_usd)

    later = [r for r in priced[entry_idx + 1:]
             if r["offering_usd"] >= max(entry_usd * GRADUATION_MULTIPLE, GRADUATION_FLOOR)]
    graduated = later[0] if later else None

    rec = {
        "entry_stage": stage,
        "entry_offering_usd": entry_usd,
        "entry_quarter": entry.get("quarter"),
        "entry_date": round_date(entry),
        "prior_rounds": entry_idx,
        "round_count": len(priced),
        "next_offering_usd": graduated["offering_usd"] if graduated else None,
        "next_quarter": graduated.get("quarter") if graduated else None,
        "graduation_source": "formd",
        "graduation_confidence": "high",
        "flags": flags,
    }

    if stage != "Seed":
        rec["seed_to_a_graduation"] = None          # not applicable
        return rec

    if graduated:
        rec["seed_to_a_graduation"] = True
        return rec

    age = months_since(round_date(entry))
    if age is not None and age < CENSOR_MONTHS:
        # Too recent to have had the chance. Counting it False would bias the
        # published rate downward, so it leaves the denominator entirely.
        rec["seed_to_a_graduation"] = None
        rec["flags"].append("censored")
    elif age is None:
        rec["seed_to_a_graduation"] = None
        rec["graduation_confidence"] = "low"
    else:
        rec["seed_to_a_graduation"] = False
    return rec


def range_of(usd: float | int) -> str:
    if usd >= 1e11:
        return "100b_plus"
    if usd >= 1e10:
        return "10b_plus"
    if usd >= 1e9:
        return "1b_plus"
    return "below_1b"


def canon_country(raw: str | None) -> str | None:
    """Normalize an ISSUERS state description, Wikidata label, or free-form
    country to an ISO 3166-1 alpha-2 code; US states collapse to US; offshore
    filing havens return None (no signal). An unrecognized name comes back
    verbatim so verify can flag it rather than losing the signal."""
    if not raw:
        return None
    raw = raw.strip()
    if len(raw) == 2 and raw.upper() in ISO_CODES:
        return raw.upper()
    if raw.upper() in US_STATES:
        return "US"
    if "CANADA" in raw.upper():
        return "CA"
    if raw.upper() in OFFSHORE:
        return None
    name = COUNTRY_CANON.get(raw) or COUNTRY_CANON.get(raw.upper())
    if name is None:
        if raw.isupper():  # EDGAR renders foreign countries in caps
            name = " ".join(w if w in ("of", "and", "the") else w.capitalize()
                            for w in raw.lower().split())
        else:
            name = raw
    return ISO_OF.get(name, name)


def add_flag(rec: dict, flag: str) -> None:
    rec["flags"] = sorted(set(rec.get("flags") or []) | {flag})


def never_merge_pairs(investor: str) -> set:
    if not P.identity_merges.exists():
        return set()
    return {frozenset(p["slugs"]) for p in
            json.loads(P.identity_merges.read_text())
            .get(investor, {}).get("never_merge", [])}


def flag_base_defects(resolved: dict, layer_a: dict, base: dict, investor: str) -> None:
    """Mark rows whose *membership in the portfolio* is doubtful.

    The valuation work answers "what is this company worth". It cannot answer
    "did this investor actually back it", and two base defects show up precisely
    at the top of the value ranking, where they do the most damage:

    `duplicate`     -- two base rows resolving to one SEC registrant are the same
                       company under an old and a new name (Service-now.com and
                       ServiceNow; Square and Block). Counted twice they inflate
                       every bucket.
    `suspect_base`  -- a Tier C row (Form D / EDGAR evidence only, never listed on
                       the investor's own site) carrying a billion-dollar
                       valuation. The reconciliation report already flags Form D
                       common-name collisions as the Tier C failure mode, and a
                       $150B company the investor never listed is exactly that
                       shape.

    Both are flagged, never dropped. Membership is the base review's call, and
    the aggregate must not quietly include or exclude a company on this pass's
    say-so.
    """
    by_cik: dict[str, list[str]] = {}
    for slug, rec in layer_a.items():
        if rec.get("cik") and slug in resolved:
            by_cik.setdefault(rec["cik"], []).append(slug)

    never = never_merge_pairs(investor)
    for slugs in by_cik.values():
        if len(slugs) > 1 and frozenset(slugs) not in never:
            for slug in slugs:
                add_flag(resolved[slug], "duplicate")

    for slug, rec in resolved.items():
        row = base.get(slug, {})
        if (rec.get("valuation_usd") or 0) >= 1e9 and row.get("tier") == "C" \
                and not (row.get("wayback_years") or "").strip():
            add_flag(rec, "suspect_base")


# ---------------------------------------------------------------------------
# prepare
# ---------------------------------------------------------------------------

def seed_membership(rows: list[dict], investor: str) -> None:
    """Auto-verdict rows whose evidence class is sufficient on its own
    (site listing, fund filing); leave name-match rows for the judge."""
    led, v = load_ledger(investor)
    n = {"listed": 0, "filing": 0, "skipped": 0}
    for r in rows:
        if r["slug"] in v:
            continue
        ec = evidence_class(r)
        if ec == "listed":
            v[r["slug"]] = {
                "verdict": "member", "who": "seed-evidence",
                "evidence_class": "site_listing",
                "basis": "Listed on the investor's own portfolio site "
                         f"({r['wayback_years'] or 'current site'}).",
                "confidence": "high", "decided": today()}
            n["listed"] += 1
        elif ec == "filing":
            v[r["slug"]] = {
                "verdict": "member", "who": "seed-evidence",
                "evidence_class": "fund_filing",
                "basis": f"SEC ownership filing by a fund vehicle "
                         f"(forms {r['edgar_forms']}, CIK {r['edgar_cik']}).",
                "confidence": "high", "decided": today()}
            n["filing"] += 1
        else:
            n["skipped"] += 1
    save_ledger(led)
    print(f"membership seed: {n['listed']} site_listing, {n['filing']} fund_filing; "
          f"left for the judge: {n['skipped']}")


def cmd_collect(args) -> None:
    """The deterministic EDGAR chain, in dependency order.

    formd-query feeds edgar-entities (its pooled-fund vehicles come from the
    sweep), which feeds edgar-companies; the Form D rescan needs a built base,
    so on a fresh investor it is deferred to `prepare`, which auto-runs it.
    Site, wayback and partner-roster collection are deliberately NOT here:
    they carry judgment steps (CMS escalation ladder, snapshot selection,
    tenure windows) that must not hide behind one opaque command.
    """
    roster = P.wayback / "partner-roster.json"
    if not roster.exists():
        sys.exit(f"no roster at {roster.relative_to(ROOT)} — run "
                 f"scripts/partner-roster.py {args.investor} first (judgment "
                 f"step: CDX patterns and tenure windows live in config.json)")
    for script in ("formd-query.py", "edgar-entities.py", "edgar-companies.py"):
        print(f"\n==== {script}")
        subprocess.run([sys.executable, str(ROOT / "scripts" / script),
                        args.investor], check=True)
    if P.base_json.exists():
        print("\n==== formd-issuer-rounds.py")
        subprocess.run([sys.executable,
                        str(ROOT / "scripts" / "formd-issuer-rounds.py"),
                        args.investor], check=True)
    else:
        print("\nno base.json yet — the Form D rescan (formd-issuer-rounds.py) "
              "runs via `prepare` after build-company-base.py")


def cmd_prepare(args) -> None:
    P.queue.mkdir(parents=True, exist_ok=True)

    rows = load_base(args.investor)
    print(f"rows: {len(rows)}")

    seed_membership(rows, args.investor)
    _, verdicts = load_ledger(args.investor)

    # ---- Form D round sequences + issuer evidence (offline rescan, one sweep)
    if not P.formd_rounds.exists() or args.refresh:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "formd-issuer-rounds.py"),
                        args.investor], check=True)
    formd = json.loads(P.formd_rounds.read_text())

    # ---- Layer A: SEC public float
    index = S.load_cik_lookup()
    layer_a: dict[str, dict] = load(P.layer_a, {})
    todo = [r for r in rows if r["slug"] not in layer_a]
    print(f"layer A (SEC public float): {len(todo)} rows to resolve")

    hits = {r["slug"]: S.resolve_cik(r, index) for r in todo}
    S.prefetch_public_float(
        [h["cik"] for h in hits.values() if h],
        progress=lambda d, t: print(f"    fetched {d}/{t}", flush=True))

    for i, row in enumerate(todo, 1):
        hit = hits[row["slug"]]
        rec: dict = {"cik": None}
        if hit:
            rec.update(hit)
            series = S.public_float(hit["cik"])
            if series:
                rec.update(S.from_public_float(series, today()))
                if hit.get("cik_weak"):
                    rec.setdefault("flags", []).append("cik_weak")
        layer_a[row["slug"]] = rec
        if i % 100 == 0:
            (P.layer_a).write_text(json.dumps(layer_a, indent=1))
            print(f"    {i}/{len(todo)}")
    (P.layer_a).write_text(json.dumps(layer_a, indent=1))
    public = sum(1 for v in layer_a.values() if v.get("is_public"))
    print(f"    resolved a CIK: {sum(1 for v in layer_a.values() if v.get('cik'))}"
          f"   with public float: {public}")

    # ---- Layer B: Wikidata
    layer_b: dict[str, dict] = load(P.layer_b, {})
    pending = [r for r in rows if r["slug"] not in layer_b]
    print(f"layer B (Wikidata): {len(pending)} rows in batches of 60")
    for i in range(0, len(pending), 60):
        chunk = pending[i:i + 60]
        hits = S.wikidata_batch([r["name"] for r in chunk])
        for r in chunk:
            layer_b[r["slug"]] = hits.get(S.norm(r["name"]), {})
        (P.layer_b).write_text(json.dumps(layer_b, indent=1))
        print(f"    {min(i + 60, len(pending))}/{len(pending)}")
    print(f"    matched: {sum(1 for v in layer_b.values() if v)}")

    # ---- Layer C: unicorn list
    uni = S.load_unicorn_list()
    print(f"layer C (unicorn list): {len(uni['current'])} current, "
          f"{len(uni['former'])} former")

    # ---- Graduation layer 1, entry anchored at partner-attributed filings
    partner_accs = {r["slug"]: accs_of(r) for r in rows}
    grad = {slug: graduation_from_formd(rec["rounds"], partner_accs.get(slug, set()))
            for slug, rec in formd.items()}
    P.graduation.write_text(json.dumps(grad, indent=1))
    determined = sum(1 for g in grad.values() if g.get("seed_to_a_graduation") is not None)
    seeds = sum(1 for g in grad.values() if g.get("entry_stage") == "Seed")
    anchored = sum(1 for g in grad.values() if g.get("prior_rounds", 0) > 0)
    print(f"graduation layer 1: {len(grad)} companies, {seeds} entered at Seed, "
          f"{determined} decided deterministically, "
          f"{anchored} entries moved past pre-investor rounds")

    issuer_ev = load(P.issuer_evidence, {}).get("accessions", {})

    def entry_country(slug: str) -> tuple[str | None, str | None]:
        """Country at the earliest partner-attributed Form D filing."""
        accs = sorted(partner_accs.get(slug, ()),
                      key=lambda a: (int(a.split("-")[1]), a))
        for acc in accs:
            e = issuer_ev.get(acc)
            if e and e.get("state_desc"):
                c = canon_country(e["state_desc"])
                if c:
                    return c, acc
        return None, None

    # ---- Consolidate and emit the queue
    resolved, queue = {}, []
    cls_prev = load(P.classification, {})
    for row in rows:
        slug = row["slug"]
        a, b, g = layer_a.get(slug, {}), layer_b.get(slug, {}), grad.get(slug, {})
        rec: dict = {"slug": slug, "name": row["name"]}
        rec.update({k: v for k, v in g.items() if v is not None or k == "seed_to_a_graduation"})
        if rec.get("entry_stage"):
            rec["entry_stage_source"] = "formd_band"
        # Country precedence: entry-time Form D business address beats a
        # current-HQ Wikidata claim; offshore havens carry no signal.
        fd_country, fd_acc = entry_country(slug)
        if fd_country:
            rec["hq_country"] = fd_country
            rec["hq_country_source"] = "formd_address"
        elif canon_country(b.get("country")):
            rec["hq_country"] = canon_country(b["country"])
            rec["hq_country_source"] = "wikidata"

        if a.get("valuation_usd") or a.get("status"):
            rec.update({k: v for k, v in a.items()
                        if k in ("status", "valuation_usd", "valuation_asof",
                                 "valuation_source", "valuation_confidence",
                                 "is_public", "public_since")})
            rec["flags"] = sorted(set(rec.get("flags", []) + a.get("flags", [])))
        elif b.get("dissolved"):
            # Wikidata occasionally returns a malformed dissolved value (a
            # truncated URI, not a date); only a date-shaped value may travel.
            dissolved = b["dissolved"] if re.fullmatch(
                r"\d{4}(-\d{2}){0,2}", str(b["dissolved"])) else None
            rec.update({"status": "defunct", "valuation_usd": None,
                        "valuation_source": "wikidata",
                        "valuation_asof": dissolved,
                        "valuation_confidence": "medium"})
        elif b.get("parent"):
            rec.update({"status": "acquired", "valuation_usd": None,
                        "valuation_source": "wikidata", "valuation_confidence": "medium"})
        elif (u := uni["current"].get(S.norm(row["name"]))) and u.get("valuation_usd"):
            # Still-private $1B+ by external list. Name-match only, so medium
            # confidence and a flag; every $1B+ claim is web-verified before it
            # ships regardless of source.
            rec.update({"status": "private", "valuation_usd": u["valuation_usd"],
                        "valuation_asof": u.get("asof"),
                        "valuation_source": "unicorn_list",
                        "valuation_confidence": "medium", "is_public": False})
            if not rec.get("hq_country") and canon_country(u.get("country")):
                rec["hq_country"] = canon_country(u["country"])
                rec["hq_country_source"] = "wikidata"
            rec["flags"] = sorted(set(rec.get("flags", []) + ["unicorn_name_match"]))

        if rec.get("valuation_usd"):
            rec["valuation_range"] = range_of(rec["valuation_usd"])
            rec["valuation_range_source"] = rec.get("valuation_source")
        # ---- gap queue: what the deterministic layers plus the existing
        # classification still leave open for this row.
        overlaid = dict(rec)
        overlaid.update({k: v for k, v in cls_prev.get(slug, {}).items()
                         if v is not None})
        flags_now = set(overlaid.get("flags") or []) | set(rec.get("flags") or [])
        need = [f for f in ("status", "hq_country", "entry_stage") if not overlaid.get(f)]
        # Rows awaiting web evidence keep valuation_range open for the web pass; the
        # batch judge may only ever rule DOWN to below_1b, never mint a figure.
        if not overlaid.get("valuation_range") and "needs_web_value" not in flags_now:
            need.append("valuation_range")
        item = {
            "slug": slug, "name": row["name"],
            "first_seen": row.get("first_seen"),
            "sector": row.get("sector"),
            "tier": row.get("tier"),
            "formd_span": row.get("formd_span"),
            "formd_max_round_usd": row.get("formd_max_round_usd"),
            "rounds": [
                {"q": r.get("quarter"), "usd": r.get("offering_usd")}
                for r in formd.get(slug, {}).get("rounds", [])
            ],
        }
        if slug not in verdicts:
            # Membership first: judging classification for a row that may not
            # even belong in the portfolio is wasted work, so the same queue
            # item asks for the verdict alongside whatever else is open.
            need.insert(0, "membership")
            item["partners_formd"] = row.get("partners_formd")
        if need:
            e = issuer_ev.get(fd_acc, {}) if fd_acc else {}
            item.update({
                "issuer_city": e.get("city"), "issuer_state": e.get("state_desc"),
                "year_inc": e.get("year_inc"),
                "former_unicorn": uni["former"].get(S.norm(row["name"])),
                "known": {k: overlaid.get(k) for k in
                          ("status", "valuation_usd", "entry_stage",
                           "seed_to_a_graduation", "hq_country", "valuation_range", "note")
                          if overlaid.get(k) is not None},
                "need": need,
            })
            queue.append(item)
        resolved[slug] = rec

    flag_base_defects(resolved, layer_a, {r["slug"]: r for r in rows}, args.investor)
    P.resolved.write_text(json.dumps(resolved, indent=1))

    batches = write_queue("batch", queue, BATCH_SIZE)
    print(f"\ndeterministically resolved: {len(rows) - len(queue)}/{len(rows)}")
    print(f"queued for judgment       : {len(queue)} rows in {batches} batches")


# ---------------------------------------------------------------------------
# record
# ---------------------------------------------------------------------------

def validate_verdict(rec: dict, slugs: set[str]) -> list[str]:
    errs = []
    s = rec.get("slug")
    if not s or s not in slugs:
        return [f"slug {s!r} not in the base"]
    if rec.get("verdict") not in VERDICTS:
        errs.append(f"{s}: verdict {rec.get('verdict')!r}")
    if rec.get("evidence_class") not in EVIDENCE:
        errs.append(f"{s}: evidence_class {rec.get('evidence_class')!r}")
    if rec.get("confidence") not in VALID_CONF:
        errs.append(f"{s}: confidence {rec.get('confidence')!r}")
    if not (rec.get("basis") or "").strip():
        errs.append(f"{s}: empty basis")
    # a member verdict resting on a name-match must say what corroborates it
    if rec.get("verdict") == "member" and rec.get("evidence_class") == "formd_adjudicated" \
            and not rec.get("citation") and rec.get("confidence") == "low":
        errs.append(f"{s}: low-confidence member on a name-match needs a citation")
    return errs


def validate_record(rec: dict, slugs: set[str]) -> list[str]:
    errs = []
    slug = rec.get("slug")
    if not slug or slug not in slugs:
        return [f"slug {slug!r} not in the base"]
    if "status" in rec:
        if rec["status"] not in VALID_STATUS:
            errs.append(f"{slug}: status {rec['status']!r}")
        if rec.get("valuation_usd") is not None:
            if rec["status"] not in ("private", "public"):
                errs.append(f"{slug}: {rec['status']} carries a valuation")
            if rec.get("valuation_source") not in VALUE_SOURCES:
                errs.append(f"{slug}: figure with source "
                            f"{rec.get('valuation_source')!r} (model may not mint numbers)")
    if rec.get("seed_to_a_graduation") is not None and rec.get("entry_stage") != "Seed":
        errs.append(f"{slug}: graduation set but entry_stage={rec.get('entry_stage')!r}")
    for key in ("valuation_confidence", "graduation_confidence",
                "entry_stage_confidence", "hq_country_confidence",
                "hq_city_confidence"):
        if rec.get(key) is not None and rec[key] not in VALID_CONF:
            errs.append(f"{slug}: bad {key} {rec[key]!r}")
    if rec.get("valuation_range") is not None:
        if rec["valuation_range"] not in VALUATION_RANGES:
            errs.append(f"{slug}: valuation_range {rec['valuation_range']!r}")
        elif rec["valuation_range"] != "below_1b" and not rec.get("valuation_usd"):
            errs.append(f"{slug}: valuation_range {rec['valuation_range']} without a sourced figure")
    if rec.get("entry_stage") is not None and rec["entry_stage"] not in VALID_STAGES:
        errs.append(f"{slug}: entry_stage {rec['entry_stage']!r}")
    if rec.get("focus") is not None and rec["focus"] not in VALID_FOCUS:
        errs.append(f"{slug}: focus {rec['focus']!r} outside the closed taxonomy")
    if rec.get("focus_source") is not None and rec["focus_source"] not in (
            "model", "web_verified"):
        errs.append(f"{slug}: focus_source {rec['focus_source']!r}")
    if "hq_city" in rec and rec["hq_city"] is not None:
        city = rec["hq_city"]
        if not isinstance(city, str) or not city.strip():
            errs.append(f"{slug}: hq_city must be a non-empty string or null")
        elif CITY_SUFFIX_RE.search(city):
            errs.append(f"{slug}: hq_city {city!r} carries a state/country suffix; "
                        f"emit the bare city name")
        elif city != city.strip() or city != city[0].upper() + city[1:]:
            errs.append(f"{slug}: hq_city {city!r} is not clean title case")
        if not rec.get("hq_city_source"):
            errs.append(f"{slug}: hq_city without hq_city_source")
    if rec.get("hq_city_source") is not None and rec["hq_city_source"] not in CITY_SOURCES:
        errs.append(f"{slug}: hq_city_source {rec['hq_city_source']!r}")
    if rec.get("entry_stage_source") is not None and rec["entry_stage_source"] not in (
            "formd_band", "formd_structural", "model", "web_verified"):
        errs.append(f"{slug}: entry_stage_source {rec['entry_stage_source']!r}")
    # web_verified stage claims must carry their citation (COLLECTION.md §6)
    if rec.get("entry_stage_source") == "web_verified" \
            and not (rec.get("entry_stage_citation") or "").strip():
        errs.append(f"{slug}: web_verified stage without entry_stage_citation")
    for key in ("valuation_citation", "hq_country_citation", "entry_stage_citation"):
        v = rec.get(key)
        if v is not None and (not isinstance(v, str) or not v.startswith("http")):
            errs.append(f"{slug}: {key} must be a URL")
    if rec.get("hq_country") is not None and rec["hq_country"] not in ISO_CODES:
        errs.append(f"{slug}: hq_country {rec['hq_country']!r} is not a known "
                    f"ISO 3166-1 alpha-2 code")
    if rec.get("hq_country_source") is not None and rec["hq_country_source"] not in (
            "formd_address", "wikidata", "model_knowledge", "web_verified"):
        errs.append(f"{slug}: hq_country_source {rec['hq_country_source']!r}")
    for key in ("flags", "clear_flags"):
        if key in rec and not isinstance(rec[key], list):
            errs.append(f"{slug}: {key} must be a list")
    return errs


def cmd_record(args) -> None:
    """One validating record step for both judgment kinds.

    A line carrying "verdict" is a membership verdict bound for the ledger;
    anything else is a classification row bound for classification.json. All
    lines validate before anything is written, so a bad batch never lands
    half-recorded.
    """
    src = Path(args.jsonl)
    slugs = {r["slug"] for r in load_base(args.investor)}
    cls = load(P.classification, {})
    led, verdicts = load_ledger(args.investor)
    cls_in, verd_in, errors = {}, {}, []
    for n, line in enumerate(src.read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {n}: {e}")
            continue
        if "verdict" in rec:
            errors.extend(validate_verdict(rec, slugs))
            verd_in[rec["slug"]] = rec
            continue
        # Answers may name the country in prose form; collapse to the alpha-2
        # code before validation so only genuinely unknown names bounce.
        if isinstance(rec, dict) and rec.get("hq_country"):
            rec["hq_country"] = canon_country(rec["hq_country"]) or rec["hq_country"]
        errors.extend(validate_record(rec, slugs))
        cls_in[rec["slug"]] = rec
    if errors:
        print(f"REJECTED — {len(errors)} problem(s), nothing recorded:")
        for e in errors[:25]:
            print("  -", e)
        sys.exit(1)

    for s, rec in verd_in.items():
        prev = verdicts.get(s)
        if prev and prev.get("who") == "erik":
            print(f"  kept human verdict on {s}")
            continue
        rec.setdefault("who", "agent-precision-pass")
        rec["decided"] = today()
        verdicts[s] = rec
    if verd_in:
        save_ledger(led)

    # A record replaces only the keys it carries: an answer merges per key into
    # the existing record instead of replacing it, flags union, and only an
    # explicit clear_flags list may remove a flag (the web pass clearing
    # needs_web_value after pinning).
    for slug, rec in cls_in.items():
        prev = cls.get(slug)
        if prev is None:
            rec["flags"] = sorted(set(rec.get("flags") or [])
                                  - set(rec.pop("clear_flags", [])))
            cls[slug] = rec
            continue
        # Human classification keys mirror the ledger rule: an agent record
        # may ADD keys to a who:"erik" row but never overwrite or unflag the
        # keys the human set (BFL's corrected stage must survive the grind).
        if prev.get("who") == "erik" and rec.get("who") != "erik":
            kept = [k for k in list(rec)
                    if k in prev and k not in ("slug", "flags", "clear_flags", "note")]
            for k in kept:
                rec.pop(k)
            rec.pop("clear_flags", None)
            if kept:
                print(f"  kept human classification keys on {slug}: {sorted(kept)}")
        fl = set(prev.get("flags") or []) | set(rec.get("flags") or [])
        fl -= set(rec.get("clear_flags") or [])
        old_note = prev.get("note")
        prev.update({k: v for k, v in rec.items()
                     if k not in ("flags", "clear_flags")})
        prev["flags"] = sorted(fl)
        if old_note and rec.get("note") and rec["note"] not in old_note:
            prev["note"] = f"{old_note} | {rec['note']}"
    # normalize country renderings at the door
    for rec in cls_in.values():
        tgt = cls[rec["slug"]]
        if tgt.get("hq_country"):
            tgt["hq_country"] = canon_country(tgt["hq_country"]) or tgt["hq_country"]
    if cls_in:
        P.classification.write_text(json.dumps(cls, indent=1, sort_keys=True))
    print(f"recorded {len(verd_in)} verdicts + {len(cls_in)} classification rows; "
          f"ledger holds {len(verdicts)}, classification holds {len(cls)}")


def cmd_status(args) -> None:
    rows = load_base(args.investor)
    _, verdicts = load_ledger(args.investor)
    cls = load(P.classification, {})
    c = Counter(verdicts[r["slug"]]["verdict"] if r["slug"] in verdicts else "UNJUDGED"
                for r in rows)
    batches = sorted(P.queue.glob("batch-*.json"))
    done = [b for b in batches if all(
        r["slug"] in cls and r["slug"] in verdicts
        for r in json.loads(b.read_text()))]
    pending = [b.name for b in batches if b not in done]
    print(f"base rows        : {len(rows)}")
    print(f"membership       : {dict(c.most_common())}")
    print(f"batches          : {len(done)}/{len(batches)} recorded")
    print(f"classified rows  : {len(cls)}")
    print(f"next pending     : {pending[0] if pending else 'none'}")


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------

def http_ok(url: str) -> bool:
    try:
        code = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "-L",
             "--max-time", "30", "-H", f"User-Agent: {UA}", url],
            capture_output=True, check=True).stdout.decode().strip()
        return code.startswith("2")
    except subprocess.CalledProcessError:
        return False


def verify_base(rows: list[dict], investor: str, problems: list[str],
                skip_links: bool) -> None:
    """Structural assertions over the built Company Base."""
    names = {r["name"].lower() for r in rows}
    slugs = {r["slug"] for r in rows}

    vcfg = CFG.get("verify", {})
    if vcfg:
        # text-mention and co-filer leaks that motivated the evidence rules,
        # plus known positions — investor-specific data, from config.json
        ec_p = P.edgar / "edgar-companies.json"
        ec_names = {c["name"].lower() for c in json.loads(ec_p.read_text())} \
            if ec_p.exists() else set()
        for leak in vcfg.get("text_mention_leaks", []):
            if any(leak in n for n in names) or any(leak in n for n in ec_names):
                problems.append(f"text-mention leak: {leak.upper()} present")
        leaks = [n for n in vcfg.get("cofiler_leaks", []) if n in names]
        if leaks:
            problems.append(f"co-filer leak (GP/management vehicles in base): {leaks}")
        missing = [w for w in vcfg.get("known_positions", [])
                   if not any(w in n for n in names)]
        if missing:
            problems.append(f"known positions missing: {missing}")

    if P.entities.exists():
        ent_ciks = {e["cik"] for e in json.loads(P.entities.read_text())}
        own = [r["name"] for r in rows if r.get("edgar_cik") and r["edgar_cik"] in ent_ciks]
        if own:
            problems.append(f"own-vehicle appears as a company: {own[:5]}")

    if P.excluded.exists():
        onames = {r["name"].lower() for r in csv.DictReader(open(P.excluded))
                  if r.get("reason") == "other_desk"}
        overlap = names & onames
        if overlap:
            problems.append(f"row in both base and other-desk: {sorted(overlap)[:5]}")
    else:
        problems.append("excluded.csv missing")

    gap = [r["name"] for r in rows if r["edgar_forms"] and not r.get("edgar_links")]
    if gap:
        problems.append(f"edgar_links missing on {len(gap)} rows with forms: {gap[:5]}")

    # regex sweep: no name-based filters may creep back into the collectors
    src = ""
    for f in ("edgar-companies.py", "build-company-base.py"):
        src += (ROOT / "scripts" / f).read_text()
    banned = [t for t in ("FILER_PAT", "is_issuer", "FUNDISH", "hongshan|peak xv") if t in src]
    if banned:
        problems.append(f"name-based filter regexes present: {banned}")

    # identity overlay applied: no absorbed/rejected slug published, every
    # canonical present, no unexplained shared CIK
    idm_p = P.identity_merges
    if idm_p.exists():
        ov = json.loads(idm_p.read_text()).get(investor, {})
        gone_expected = {d for m in ov.get("merges", []) for d in m["duplicates"]}
        gone_expected |= {rj["slug"] for rj in ov.get("rejects", [])}
        if still := sorted(gone_expected & slugs):
            problems.append(f"absorbed/rejected slug in published base: {still[:5]}")
        _, verdicts = load_ledger(investor)
        bv_gone = {s for s, r in verdicts.items() if r.get("verdict") == "not_member"}
        canon_missing = sorted({m["canonical"] for m in ov.get("merges", [])} - slugs
                               - {dk["slug"] for dk in ov.get("desk", [])} - bv_gone)
        if canon_missing:
            problems.append(f"merge canonical absent from base: {canon_missing[:5]}")
        allowed = {frozenset(p["slugs"]) for p in ov.get("never_merge", [])}
        by_cik: dict[str, list] = {}
        for r in rows:
            if r.get("edgar_cik"):
                by_cik.setdefault(r["edgar_cik"], []).append(r["slug"])
        shared = [ss for ss in by_cik.values()
                  if len(ss) > 1 and frozenset(ss) not in allowed]
        if shared:
            problems.append(f"unexplained shared CIK among published rows: {shared[:3]}")

    if not skip_links:
        el = [r["edgar_links"].split("; ")[0] for r in rows if r.get("edgar_links")][:3]
        fl = [r["formd_links"].split("; ")[0] for r in rows if r.get("formd_links")][:2]
        bad = [u for u in el + fl if not http_ok(u)]
        if bad or not (el or fl):
            problems.append(f"sampled evidence links failing: {bad or 'none sampled'}")


def verify_membership(rows: list[dict], investor: str, problems: list[str]) -> None:
    """Every published row verdicted; no not_member published."""
    _, verdicts = load_ledger(investor)
    unjudged, leaked = [], []
    for r in rows:
        rec = verdicts.get(r["slug"])
        if not rec:
            unjudged.append(r["slug"])
        elif rec["verdict"] == "not_member":
            leaked.append(r["slug"])
    unc = sum(1 for r in rows
              if verdicts.get(r["slug"], {}).get("verdict") == "uncertain")
    print(f"membership      : {len(verdicts)} verdicts, {unc} uncertain")
    if unjudged:
        problems.append(f"{len(unjudged)} published rows without a membership "
                        f"verdict: {unjudged[:5]}")
    if leaked:
        problems.append(f"published despite not_member: {leaked[:5]}")


def cmd_verify(args) -> None:
    rows = load_base(args.investor)
    resolved = load(P.resolved, {})
    cls = load(P.classification, {})
    problems: list[str] = []

    verify_base(rows, args.investor, problems, skip_links=args.skip_links)
    verify_membership(rows, args.investor, problems)

    # Drift tripwire: a base rebuild after prepare shows up as a key mismatch
    # against resolved.json. Stale classification keys are expected (absorbed
    # earlier-run answers) and unused by the merge.
    base_slugs = {r["slug"] for r in rows}
    if resolved or not args.base_only:
        gone, new = set(resolved) - base_slugs, base_slugs - set(resolved)
        if gone or new:
            problems.append(f"base rebuilt since prepare: {len(gone)} resolved slugs "
                            f"no longer in the base, {len(new)} base rows unresolved; "
                            f"re-run prepare")
    if stale := len(set(cls) - base_slugs):
        print(f"stale classification keys: {stale} (earlier base versions)")

    # A base-only run (the "company base" half of a collection, before the
    # classification session) has nothing to assert about the columns it
    # never wrote: full fills, source gates and citation invariants are the
    # classification run's contract. Everything above — base structure,
    # membership coverage, drift, published-surface currency (below) —
    # still holds.
    if args.base_only:
        csv_p = P.base_csv
        if not csv_p.exists():
            problems.append(f"{csv_p.name} missing; run export")
        else:
            csv_slugs = {r["slug"] for r in csv.DictReader(open(csv_p))}
            if csv_slugs != base_slugs:
                problems.append(f"{csv_p.name} stale relative to the base "
                                f"({len(csv_slugs ^ base_slugs)} slugs differ); re-run export")
        if not P.review_html.exists():
            problems.append("review.html missing; run review")
        elif rows and rows[0]["name"] not in P.review_html.read_text(
                encoding="utf-8", errors="replace"):
            problems.append("review.html stale relative to the base; re-run review")
        if problems:
            print(f"\n{len(problems)} problem(s):")
            for p in problems[:40]:
                print("  -", p)
            sys.exit(1)
        print("\nverify (base-only): clean")
        return

    merged = merge_rows(rows, resolved, cls)
    for slug, rec in merged.items():
        if not rec.get("status"):
            problems.append(f"{slug}: no status")
            continue
        if rec["status"] not in VALID_STATUS:
            problems.append(f"{slug}: status {rec['status']!r} not in vocabulary")
        if rec.get("valuation_confidence") and rec["valuation_confidence"] not in VALID_CONF:
            problems.append(f"{slug}: bad confidence {rec['valuation_confidence']!r}")
        if rec.get("valuation_usd") and rec["status"] not in ("private", "public"):
            problems.append(f"{slug}: {rec['status']} carries a current valuation")
        if rec.get("valuation_usd") and rec.get("valuation_source") not in VALUE_SOURCES:
            problems.append(f"{slug}: figure from {rec.get('valuation_source')!r} "
                            f"is not a value-bearing source")
        if rec.get("seed_to_a_graduation") is not None and rec.get("entry_stage") != "Seed":
            problems.append(f"{slug}: graduation set but entry_stage={rec.get('entry_stage')!r}")

        # ---- full fills, tag/figure consistency
        tag, usd = rec.get("valuation_range"), rec.get("valuation_usd")
        if not tag:
            problems.append(f"{slug}: no valuation_range")
        elif tag not in VALUATION_RANGES:
            problems.append(f"{slug}: valuation_range {tag!r} not in vocabulary")
        elif usd and tag != range_of(usd):
            problems.append(f"{slug}: valuation_range {tag} disagrees with figure {usd:,.0f}")
        elif tag != "below_1b" and not usd:
            problems.append(f"{slug}: valuation_range {tag} without a sourced figure")
        if not rec.get("hq_country"):
            problems.append(f"{slug}: no hq_country")
        elif rec["hq_country"] not in ISO_CODES:
            problems.append(f"{slug}: hq_country {rec['hq_country']!r} is not a known "
                            f"ISO 3166-1 alpha-2 code")
        if not rec.get("entry_stage"):
            problems.append(f"{slug}: no entry_stage")
        elif rec["entry_stage"] not in VALID_STAGES:
            problems.append(f"{slug}: entry_stage {rec['entry_stage']!r} not in vocabulary")
        # COLLECTION.md invariant 4: a bucket-visible row needs class 1/2
        # stage evidence (a citation, or the deterministic filing structure).
        stage_cited = bool((rec.get("entry_stage_citation") or "").strip()) \
            or rec.get("entry_stage_source") in ("formd_structural", "formd_band")
        flags_now = set(rec.get("flags") or [])
        if (rec.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")
                and not stage_cited and "cite_pending" not in flags_now):
            problems.append(f"{slug}: $1B+ row without cited/structural entry stage "
                            f"and no cite_pending marker")
        # COLLECTION.md invariant 3: public $1B+ value is a cited market cap
        if rec.get("is_public") and rec.get("valuation_range") in (
                "1b_plus", "10b_plus", "100b_plus") \
                and not (rec.get("valuation_citation") or "").strip() \
                and "cite_pending" not in flags_now:
            problems.append(f"{slug}: public $1B+ row without a cited market cap")
        # invariant 3: cohort rows are verified on both legs or carry the flag
        if rec.get("seed_to_a_graduation") is not None:
            legs_verified = stage_cited and rec.get("graduation_source") in (
                "formd", "web_verified")
            if not legs_verified and "cohort_unverified" not in (rec.get("flags") or []):
                problems.append(f"{slug}: cohort row neither verified nor flagged "
                                f"cohort_unverified")

    # cumulative invariant
    def names(floor):
        return {s for s, r in merged.items() if (r.get("valuation_usd") or 0) >= floor}
    one_b, ten_b, hundred_b = names(1e9), names(1e10), names(1e11)
    if not hundred_b <= ten_b <= one_b:
        problems.append("cumulative invariant violated: hundred_b ⊄ ten_b ⊄ one_b")

    # Two base rows resolving to one SEC registrant are the same company under
    # two names (Network Appliance -> NetApp). Left alone they double-count in
    # every bucket, so they are reported rather than silently summed.
    layer_a = load(P.layer_a, {})
    proven_distinct = never_merge_pairs(args.investor)
    by_cik: dict[str, list[str]] = {}
    for slug, rec in layer_a.items():
        if rec.get("cik") and slug in base_slugs:
            by_cik.setdefault(rec["cik"], []).append(slug)
    dupes = {c: s for c, s in by_cik.items()
             if len(s) > 1 and frozenset(s) not in proven_distinct}
    if dupes:
        print(f"duplicate companies (same SEC registrant): {len(dupes)} groups")
        # Duplicates are a base defect awaiting human adjudication. The run's
        # obligation: within each registrant group at most ONE row may be
        # unflagged (the canonical row that derivation counts); a group with two
        # unflagged rows would double-count and fails verify. A fully flagged
        # group is fine -- canonical selection then happens at derivation.
        for cik, slugs in sorted(dupes.items()):
            unflagged = [s for s in slugs
                         if "duplicate" not in (merged.get(s, {}).get("flags") or [])]
            if len(unflagged) > 1:
                problems.append(f"CIK {cik}: {len(unflagged)} unflagged duplicates "
                                f"({', '.join(unflagged)})")

    total = len(rows)
    print(f"rows            : {total}")
    print(f"classified      : {sum(1 for r in merged.values() if r.get('status'))}")
    print(f"$1B+ / $10B+ / $100B+ : {len(one_b)} / {len(ten_b)} / {len(hundred_b)}")
    bad_focus = [s for s, r in merged.items()
                 if r.get("focus") is not None and r["focus"] not in VALID_FOCUS]
    if bad_focus:
        problems.append(f"focus outside taxonomy on {len(bad_focus)} rows: "
                        f"{bad_focus[:3]}")
    foc = Counter(r.get("focus") or "(outside taxonomy)" for r in merged.values())
    print(f"focus           : {dict(foc.most_common())}")
    bad_city = [s for s, r in merged.items()
                if r.get("hq_city") and CITY_SUFFIX_RE.search(r["hq_city"])]
    if bad_city:
        problems.append(f"hq_city carries a state/country suffix on "
                        f"{len(bad_city)} rows: {bad_city[:3]}")
    cities = Counter(r["hq_city"] for r in merged.values() if r.get("hq_city"))
    print(f"hq_city         : {len(cities)} distinct, "
          f"{sum(cities.values())}/{total} filled; top "
          f"{dict(cities.most_common(8))}")
    tags = Counter(r.get("valuation_range") for r in merged.values())
    print(f"valuation_range : {dict(tags.most_common())}")
    stages = Counter(r.get("entry_stage") for r in merged.values())
    print(f"entry_stage     : {dict(stages.most_common())}")
    cohort = [r for r in merged.values() if r.get("seed_to_a_graduation") is not None]
    grad = sum(1 for r in cohort if r["seed_to_a_graduation"])
    print(f"C2A cohort      : {len(cohort)}  graduated {grad}"
          f"  rate {grad / len(cohort) * 100:.1f}%" if cohort else "C2A cohort      : 0")

    # Sanity guard, not an invariant. Raised from 15% once the initial-only
    # person-match defect was fixed: dropping ~50 misattributed near-worthless
    # rows shrinks the denominator without touching the numerator, so a cleaner
    # base legitimately shows a HIGHER winner share.
    if one_b and len(one_b) / total > 0.20:
        problems.append(f"$1B+ is {len(one_b)/total:.1%} of the base; expected <20%")
    if cohort and grad / len(cohort) > 0.80:
        problems.append(f"C2A is {grad/len(cohort):.1%}; expected <80%")

    # published surfaces current: the merged CSV and review.html must reflect
    # the live base (same slugs, same first row)
    csv_p = P.base_csv
    if not csv_p.exists():
        problems.append(f"{csv_p.name} missing; run export")
    else:
        csv_slugs = {r["slug"] for r in csv.DictReader(open(csv_p))}
        if csv_slugs != base_slugs:
            problems.append(f"{csv_p.name} stale relative to the base "
                            f"({len(csv_slugs ^ base_slugs)} slugs differ); re-run export")
    if not P.review_html.exists():
        problems.append("review.html missing; run review")
    elif rows and rows[0]["name"] not in P.review_html.read_text(
            encoding="utf-8", errors="replace"):
        problems.append("review.html stale relative to the base; re-run review")

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems[:40]:
            print("  -", p)
        sys.exit(1)
    print("\nverify: clean")


# ---------------------------------------------------------------------------
# export: the one merged CSV
# ---------------------------------------------------------------------------

# Identity, membership, evidence, classification — DB-aligned names throughout
# (the classification headers are the public.companies column names, which is
# what lets ingest-companies.ts read this file without a mapping layer).
EXPORT_COLUMNS = [
    "slug", "name", "membership_verdict", "membership_evidence",
    "first_seen", "sector", "partners_site", "partners_formd",
    "site_url", "wayback_first_link", "formd_links", "edgar_links",
    "status", "valuation_range", "valuation_usd", "valuation_asof",
    "valuation_source", "valuation_citation",
    "entry_stage", "entry_stage_source", "entry_stage_citation",
    "hq_city", "hq_country", "focus", "seed_to_a_graduation", "flags", "note",
]

EVIDENCE_COLUMNS = ("first_seen", "sector", "partners_site", "partners_formd",
                    "site_url", "wayback_first_link", "formd_links", "edgar_links")


def cmd_export(args) -> None:
    """Write the merged per-investor CSV in one merge step: base evidence +
    membership verdict + classification overlays. A base without a
    classification run just leaves those fields empty."""
    rows = load_base(args.investor)
    _, verdicts = load_ledger(args.investor)
    merged = merge_rows(rows, load(P.resolved, {}),
                        load(P.classification, {}))

    out_rows = []
    for row in rows:
        slug = row["slug"]
        rec = merged.get(slug, {})
        v = verdicts.get(slug, {})
        out = {"slug": slug, "name": row["name"],
               "membership_verdict": v.get("verdict", ""),
               "membership_evidence": v.get("evidence_class", "")}
        out.update({k: row.get(k, "") for k in EVIDENCE_COLUMNS})
        out.update({k: rec.get(k) for k in EXPORT_COLUMNS if k not in out})
        out["flags"] = ";".join(rec.get("flags") or [])
        out_rows.append({k: "" if out.get(k) is None else out[k]
                         for k in EXPORT_COLUMNS})

    dest = P.base_csv
    with open(dest, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_COLUMNS)
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {dest.relative_to(ROOT)} ({len(out_rows)} rows)")


# ---------------------------------------------------------------------------
# review: the one read-only surface
# ---------------------------------------------------------------------------

def in_sample(r: dict) -> bool:
    """Rows a human should spot-check, since sampling replaced full review.

    Every row that publishes a headline claim ($10B+ bucket or a graduation
    boolean), plus low-confidence rows attached to a published claim, plus the
    verification loop's own recoveries and seeding checks.
    """
    if r["slug"] in SAMPLE_SLUGS:
        return True
    if (r.get("valuation_usd") or 0) >= 1e10:
        return True
    if r.get("seed_to_a_graduation") is not None:
        return True
    publishes = bool(r.get("valuation_usd")) or bool(r.get("is_public"))
    return publishes and (r.get("valuation_confidence") == "low"
                          or r.get("entry_stage_confidence") == "low")


def priority(r: dict) -> tuple:
    """Lower sorts first. Ranked by the cost of getting the row wrong.

    Low confidence only elevates a row when it is attached to a claim that
    publishes (a bucket membership or a graduation boolean). A low-confidence
    "obscure and worth nothing" row publishes nothing, so it must not outrank
    the rows that do.
    """
    val = r.get("valuation_usd") or 0
    flags = set(r.get("flags") or [])
    publishes = bool(val) or bool(r.get("is_public")) \
        or r.get("seed_to_a_graduation") is not None
    low_conf = (r.get("valuation_confidence") == "low"
                or r.get("graduation_confidence") == "low")
    if val >= 1e9:
        return (0, -val)                              # every published claim
    if flags & {"graduation_disagree", "duplicate", "suspect_base",
                "model_disputes_source"}:
        return (1, -val)
    if low_conf and publishes:
        return (2, 0)
    if flags & {"boundary", "cik_weak", "stale", "unicorn_name_match",
                "entry_anchor_weak"}:
        return (3, 0)
    if r.get("seed_to_a_graduation") is not None:
        return (4, 0)                                 # feeds the published rate
    return (5, 0)


REVIEW_FIELDS = [
    "slug", "name", "membership_verdict", "membership_evidence", "membership_basis",
    "status", "valuation_range", "valuation_usd", "valuation_asof",
    "valuation_source", "valuation_confidence", "is_public",
    "entry_stage", "entry_stage_source", "entry_stage_confidence",
    "entry_stage_citation", "valuation_citation", "entry_offering_usd",
    "round_count", "seed_to_a_graduation", "graduation_confidence",
    "hq_city", "hq_country", "focus", "flags", "tier", "first_seen", "sector",
    "site_url", "formd_links", "edgar_links", "wayback_first_link", "note",
]

# Order a reviewer should read the profile fields in: cheap and factual first,
# judgement-heavy last.
PROFILE_ORDER = [
    "name", "website", "icon_url", "hq_location", "founding_year",
    "history", "investment_concept",
    "investment_stage", "investment_geo", "investment_scope",
    "investment_range", "notable_investments",
    "aum", "funds", "individuals",
]

REVIEW_TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store">
<title>Review — __INVESTOR__</title>
<style>
:root { --bg:#fbfaf8; --panel:#fff; --ink:#1c1a17; --muted:#6d6558; --line:#e3ded4;
  --accent:#7a5c2e; --ok:#2e6b40; --no:#8c3232; --chip:#f0ece4; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#171614; --panel:#1f1e1b; --ink:#ece8e1; --muted:#9a9284; --line:#332f2a;
          --accent:#c9a227; --ok:#6bbd85; --no:#e08585; --chip:#2a2724; } }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--ink);
  font:13px/1.45 ui-sans-serif,-apple-system,"SF Pro Text",Segoe UI,sans-serif; }
header { position:sticky; top:0; z-index:10; background:var(--panel);
  border-bottom:1px solid var(--line); padding:10px 14px; }
h1 { margin:0 0 8px; font-size:15px; font-weight:600; letter-spacing:-.01em; }
h1 small { font-weight:400; color:var(--muted); margin-left:8px; }
.bar { display:flex; flex-wrap:wrap; gap:6px; align-items:center; }
.chip { border:1px solid var(--line); background:var(--chip); color:var(--ink);
  border-radius:999px; padding:3px 10px; font-size:12px; cursor:pointer; }
.chip.on { background:var(--accent); border-color:var(--accent); color:#fff; }
@media (prefers-color-scheme: dark) { .chip.on { color:#171614; } }
input[type=search] { flex:1; min-width:180px; padding:5px 10px; border-radius:6px;
  border:1px solid var(--line); background:var(--bg); color:var(--ink); font-size:13px; }
.count { color:var(--muted); font-size:12px; margin-left:auto; white-space:nowrap; }
details.profile { border-bottom:1px solid var(--line); background:var(--panel); }
details.profile summary { cursor:pointer; padding:8px 14px; font-size:12px;
  color:var(--muted); }
.ptable { width:100%; border-collapse:collapse; font-size:12px; }
.ptable td { padding:6px 14px; border-top:1px solid var(--line); vertical-align:top; }
.ptable td.fname { width:170px; font-weight:600; }
.psrc { color:var(--muted); font-size:11px; margin-top:2px; }
.psrc a { color:var(--accent); }
.wrap { overflow-x:auto; }
table.rows { border-collapse:collapse; width:100%; font-size:12px; }
table.rows th { position:sticky; top:0; background:var(--panel); text-align:left;
  font-weight:600; padding:6px 8px; border-bottom:1px solid var(--line); cursor:pointer;
  white-space:nowrap; color:var(--muted); font-size:11px; text-transform:uppercase;
  letter-spacing:.04em; }
table.rows td { padding:5px 8px; border-bottom:1px solid var(--line); vertical-align:top;
  white-space:nowrap; }
.note-cell { max-width:240px; overflow:hidden; text-overflow:ellipsis; }
tr.row { cursor:pointer; }
tr.row:hover { background:var(--chip); }
#drawer { position:fixed; left:0; right:0; bottom:0; z-index:20; display:none;
  background:var(--panel); border-top:2px solid var(--accent);
  box-shadow:0 -6px 24px rgba(0,0,0,.25); max-height:45vh; overflow-y:auto;
  padding:12px 16px; font-size:13px; }
#drawer.open { display:block; }
#drawer h2 { margin:0 0 2px; font-size:14px; }
#drawer .dmeta { color:var(--muted); font-size:11px; margin-bottom:8px; }
#drawer .dfield { margin:6px 0; }
#drawer .dfield b { display:inline-block; min-width:110px; color:var(--muted);
  font-weight:600; font-size:11px; text-transform:uppercase; letter-spacing:.04em; }
#drawer .dtext { white-space:normal; line-height:1.5; }
#dclose { position:absolute; top:8px; right:12px; border:1px solid var(--line);
  background:var(--chip); color:var(--ink); border-radius:6px; padding:2px 10px;
  cursor:pointer; font-size:12px; }
.nm { font-weight:600; }
.mut { color:var(--muted); }
.val { font-variant-numeric:tabular-nums; text-align:right; white-space:nowrap; font-weight:600; }
.tag { font-size:11px; padding:1px 6px; border-radius:4px; background:var(--chip); white-space:nowrap; }
.t-100b { background:var(--accent); color:#fff; }
.t-10b { background:color-mix(in srgb,var(--accent) 55%,transparent); }
.t-1b { background:color-mix(in srgb,var(--accent) 25%,transparent); }
.s-public { background:color-mix(in srgb,var(--ok) 35%,transparent); }
.s-acquired, .s-defunct { background:color-mix(in srgb,var(--no) 25%,transparent); }
.s-unknown { background:var(--no); color:#fff; }
.v-member { background:color-mix(in srgb,var(--ok) 35%,transparent); }
.v-uncertain { background:var(--no); color:#fff; }
.g-true { background:var(--ok); color:#fff; }
.g-false { background:var(--chip); }
.f { font-size:10px; padding:1px 5px; border-radius:3px; background:var(--no);
  color:#fff; margin-right:3px; white-space:nowrap; }
.f-censored, .f-cik_weak, .f-cite_pending, .f-cohort_unverified { background:var(--muted); }
.c-low { color:var(--no); font-weight:600; }
a { color:var(--accent); text-decoration:none; }
a:hover { text-decoration:underline; }
.lnk { font-size:11px; white-space:nowrap; }
.help { color:var(--muted); font-size:11px; padding:6px 14px; border-top:1px solid var(--line);
  background:var(--panel); position:sticky; bottom:0; }
</style>
</head>
<body>
<header>
  <h1>Review <small>__INVESTOR__ · read-only · membership + classification</small></h1>
  <div class="bar">
    <span class="mut">value</span>
    <button class="chip" data-f="sample" data-v="1" title="stratified rows for manual spot-check">Sample</button>
    <button class="chip" data-f="th" data-v="100b">$100B+</button>
    <button class="chip" data-f="th" data-v="10b">$10B+</button>
    <button class="chip" data-f="th" data-v="1b">$1B+</button>
    <span class="mut" style="margin-left:8px">status</span>
    <button class="chip" data-f="status" data-v="public">public</button>
    <button class="chip" data-f="status" data-v="private">private</button>
    <button class="chip" data-f="status" data-v="acquired">acquired</button>
    <button class="chip" data-f="status" data-v="defunct">defunct</button>
    <button class="chip" data-f="status" data-v="unknown">unknown</button>
    <span class="mut" style="margin-left:8px">membership</span>
    <button class="chip" data-f="verdict" data-v="uncertain">uncertain</button>
    <button class="chip" data-f="verdict" data-v="formd_adjudicated">judged</button>
    <span class="mut" style="margin-left:8px">flag</span>
    <button class="chip" data-f="flag" data-v="duplicate">duplicate</button>
    <button class="chip" data-f="flag" data-v="cite_pending">cite pending</button>
    <button class="chip" data-f="flag" data-v="censored">censored</button>
    <button class="chip" data-f="flag" data-v="cik_weak">weak cik</button>
    <span class="mut" style="margin-left:8px">conf</span>
    <button class="chip" data-f="conf" data-v="low">low</button>
    <span class="mut" style="margin-left:8px">C2A</span>
    <button class="chip" data-f="grad" data-v="true">graduated</button>
    <button class="chip" data-f="grad" data-v="false">not</button>
  </div>
  <div class="bar" style="margin-top:6px">
    <input type="search" id="q" placeholder="search name, slug, city, country, sector…">
    <span class="count" id="count"></span>
  </div>
</header>
<details class="profile"><summary>Investor profile — every field with its source and basis</summary>
<table class="ptable" id="ptable"></table>
</details>
<div class="wrap"><table class="rows">
<thead><tr>
  <th></th><th data-s="name">Company</th><th data-s="membership_verdict">Member</th>
  <th data-s="valuation_usd">Value</th>
  <th data-s="status">Status</th><th data-s="valuation_asof">As of</th>
  <th data-s="valuation_source">Source</th><th data-s="entry_stage">Entry</th>
  <th data-s="round_count">Rds</th><th data-s="seed_to_a_graduation">C2A</th>
  <th>Flags</th><th data-s="hq_city">City</th><th data-s="hq_country">Country</th>
  <th data-s="focus">Focus</th><th data-s="tier">T</th>
  <th>Note</th>
</tr></thead>
<tbody id="tb"></tbody>
</table></div>
<div class="help">
  Read-only. Rows stay one line; <b>click any row</b> for the full note, membership
  basis and citations. Sorted by cost of error: $1B+ claims, then layer disagreements,
  then low confidence. Corrections land as overlay edits
  (<code>base-verification.json</code> / <code>classification.json</code>), recorded via
  <code>python3 scripts/run.py record</code>.
</div>
<div id="drawer">
  <button id="dclose">close</button>
  <h2 id="dname"></h2>
  <div class="dmeta" id="dmeta"></div>
  <div id="dbody"></div>
</div>
<script id="data" type="application/json">__DATA__</script>
<script id="profile" type="application/json">__PROFILE__</script>
<script>
const ROWS = JSON.parse(document.getElementById('data').textContent);
const PROFILE = JSON.parse(document.getElementById('profile').textContent);
let filters = {th:new Set(), status:new Set(), flag:new Set(), conf:new Set(),
               grad:new Set(), sample:new Set(), verdict:new Set()};
let q = '', sortKey = null, sortDir = 1;
const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

const usd = v => { const n = +v; if (!n) return '';
  return n >= 1e12 ? '$'+(n/1e12).toFixed(2)+'T' : n >= 1e9 ? '$'+(n/1e9).toFixed(2)+'B'
       : n >= 1e6 ? '$'+Math.round(n/1e6)+'M' : '$'+Math.round(n/1e3)+'k'; };
const thOf = r => { const v = +r.valuation_usd || 0;
  return v >= 1e11 ? '100b' : v >= 1e10 ? '10b' : v >= 1e9 ? '1b' : ''; };

function renderProfile() {
  document.getElementById('ptable').innerHTML = PROFILE.map(f => {
    const shown = f.value === null || f.value === undefined ? null
      : (typeof f.value === 'object' ? JSON.stringify(f.value, null, 1) : String(f.value));
    const src = f.source ? (/^https?:/.test(f.source)
      ? `<div class="psrc">source: <a href="${esc(f.source)}" target="_blank" rel="noopener">${esc(f.source)}</a></div>`
      : `<div class="psrc">source: <code>${esc(f.source)}</code></div>`) : '';
    const basis = f.basis ? `<div class="psrc">${esc(f.basis)}</div>` : '';
    return `<tr><td class="fname">${esc(f.name)}</td>
      <td>${shown === null ? '<span class="mut">null</span>' : esc(shown)}${src}${basis}</td></tr>`;
  }).join('');
}

function visible() {
  let rows = ROWS.filter(r => {
    if (filters.th.size && !filters.th.has(thOf(r))) return false;
    if (filters.status.size && !filters.status.has(r.status)) return false;
    if (filters.verdict.size && !filters.verdict.has(r.membership_verdict)
        && !filters.verdict.has(r.membership_evidence)) return false;
    if (filters.conf.size && !filters.conf.has(r.valuation_confidence)
        && !filters.conf.has(r.graduation_confidence)) return false;
    if (filters.flag.size && !(r.flags||[]).some(f => filters.flag.has(f))) return false;
    if (filters.grad.size && !filters.grad.has(String(r.seed_to_a_graduation))) return false;
    if (filters.sample.size && !r.sample) return false;
    if (q) { const h = (r.name+' '+r.slug+' '+(r.hq_city||'')+' '+(r.hq_country||'')+' '+(r.sector||'')).toLowerCase();
      if (!h.includes(q)) return false; }
    return true;
  });
  if (sortKey) rows = rows.slice().sort((a,b) => {
    const A = a[sortKey], B = b[sortKey];
    if (typeof A === 'number' || typeof B === 'number') return ((+B||0)-(+A||0))*sortDir;
    return String(A??'').localeCompare(String(B??''))*sortDir;
  });
  return rows;
}

function render() {
  const rows = visible(), tb = document.getElementById('tb');
  tb.innerHTML = rows.map((r,i) => {
    const th = thOf(r);
    const lnk = (h,t) => `<a class="lnk" href="${h}" target="_blank" rel="noopener">${t}</a>`;
    const srcLabel = (r.valuation_source||'').replace('sec_public_float','sec')
      .replace('model_knowledge','model').replace('web_verified','web');
    const edgar = (r.edgar_links||'').split('; ')[0], formd = (r.formd_links||'').split('; ')[0];
    const src = [
      srcLabel === 'sec' && edgar ? lnk(edgar,'sec') : srcLabel,
      r.site_url ? lnk(r.site_url,'site') : '',
      r.wayback_first_link ? lnk(r.wayback_first_link,'arch') : '',
      formd ? lnk(formd,'D') : '',
      srcLabel !== 'sec' && edgar ? lnk(edgar,'SEC') : '',
    ].filter(Boolean).join(' ');
    const g = r.seed_to_a_graduation;
    const gCell = g === true ? '<span class="tag g-true">yes</span>'
                : g === false ? '<span class="tag g-false">no</span>' : '';
    const conf = (r.valuation_confidence === 'low' || r.graduation_confidence === 'low')
                ? ' <span class="c-low">low</span>' : '';
    const v = r.membership_verdict || '';
    const vCell = v ? `<span class="tag v-${v}" title="${esc(r.membership_basis||'')}">${
      v === 'member' ? (r.membership_evidence||'member').replace('site_listing','site')
        .replace('fund_filing','filing').replace('formd_adjudicated','judged') : v}</span>` : '';
    return `<tr class="row" data-slug="${r.slug}">
      <td class="mut">${r.sample?'◦':''}</td>
      <td class="nm">${esc(r.name)}</td>
      <td>${vCell}</td>
      <td class="val ${th?'':'mut'}">${th?`<span class="tag t-${th}">`:''}${usd(r.valuation_usd)}${th?'</span>':''}${r.valuation_citation?` <a class="lnk" href="${r.valuation_citation}" target="_blank" rel="noopener">c</a>`:''}</td>
      <td><span class="tag s-${r.status||'unknown'}">${r.status||'—'}</span>${conf}</td>
      <td class="mut">${r.valuation_asof||''}</td>
      <td class="mut">${src}</td>
      <td class="mut">${r.entry_stage||''}${r.entry_stage_citation?` <a class="lnk" href="${r.entry_stage_citation}" target="_blank" rel="noopener">cite</a>`:''}${r.entry_offering_usd?` <span class="mut">${usd(r.entry_offering_usd)}</span>`:''}</td>
      <td class="mut">${r.round_count||''}</td>
      <td>${gCell}</td>
      <td>${(r.flags||[]).map(f=>`<span class="f f-${f}">${f}</span>`).join('')}</td>
      <td class="mut">${esc(r.hq_city||'')}</td>
      <td class="mut">${r.hq_country||''}</td>
      <td class="mut">${esc(r.focus||'')}</td>
      <td class="mut">${r.tier||''}</td>
      <td class="mut note-cell" title="click the row for the full note">${esc(r.note||'')}</td>
    </tr>`;
  }).join('');
  document.getElementById('count').textContent = `${rows.length} / ${ROWS.length} shown`;
}

const drawer = document.getElementById('drawer');
function openDrawer(slug) {
  const r = ROWS.find(x => x.slug === slug);
  if (!r) return;
  document.getElementById('dname').textContent = r.name;
  document.getElementById('dmeta').textContent =
    `${r.slug} · tier ${r.tier||'—'} · ${r.status||'unclassified'}` +
    (r.valuation_usd ? ` · ${usd(r.valuation_usd)}` : '') +
    (r.entry_stage ? ` · entry ${r.entry_stage}` : '');
  const link = u => u ? `<a href="${esc(u)}" target="_blank" rel="noopener">${esc(u)}</a>` : '';
  const fields = [
    ['Membership', r.membership_verdict ? `${r.membership_verdict} (${r.membership_evidence||'—'})` : ''],
    ['Basis', r.membership_basis],
    ['Note', r.note],
    ['Flags', (r.flags||[]).join(', ')],
    ['Stage citation', link(r.entry_stage_citation)],
    ['Value citation', link(r.valuation_citation)],
    ['Sources', [r.site_url && link(r.site_url), r.wayback_first_link && link(r.wayback_first_link),
                  (r.formd_links||'').split('; ')[0] && link((r.formd_links||'').split('; ')[0]),
                  (r.edgar_links||'').split('; ')[0] && link((r.edgar_links||'').split('; ')[0])]
                 .filter(Boolean).join('<br>')],
  ];
  document.getElementById('dbody').innerHTML = fields
    .filter(([,v]) => v)
    .map(([k, v]) => `<div class="dfield"><b>${k}</b> <span class="dtext">${
      k === 'Basis' || k === 'Note' ? esc(v) : v}</span></div>`).join('');
  drawer.classList.add('open');
}
document.getElementById('tb').addEventListener('click', e => {
  if (e.target.closest('a')) return;           // evidence links keep working
  const tr = e.target.closest('tr.row');
  if (tr) openDrawer(tr.dataset.slug);
});
document.getElementById('dclose').addEventListener('click', () => drawer.classList.remove('open'));
document.addEventListener('keydown', e => { if (e.key === 'Escape') drawer.classList.remove('open'); });

document.querySelectorAll('.chip').forEach(c => c.addEventListener('click', () => {
  const s = filters[c.dataset.f]; s.has(c.dataset.v) ? s.delete(c.dataset.v) : s.add(c.dataset.v);
  c.classList.toggle('on'); render();
}));
document.querySelectorAll('th[data-s]').forEach(th => th.addEventListener('click', () => {
  sortDir = (sortKey === th.dataset.s) ? -sortDir : 1; sortKey = th.dataset.s; render();
}));
document.getElementById('q').addEventListener('input', e => { q = e.target.value.toLowerCase(); render(); });
renderProfile();
render();
</script>
</body>
</html>
"""


def profile_fields(investor: str) -> list[dict]:
    """The firm profile as [{name, value, source, basis}], review order."""
    if not P.investor.exists() or not P.investor_sources.exists():
        return []
    row = json.loads(P.investor.read_text())
    fields = json.loads(P.investor_sources.read_text()).get("fields", {})
    ordered = [k for k in PROFILE_ORDER if k in fields]
    ordered += [k for k in fields if k not in ordered]
    return [{"name": k,
             "value": fields[k].get("value", row.get(k)),
             "source": fields[k].get("source"),
             "basis": fields[k].get("basis")} for k in ordered]


def cmd_review(args) -> None:
    # The firm-profile session (COLLECTION.md §11) runs in parallel with the
    # base collection and ends at this surface, so a missing base renders the
    # investor panel over an empty company table rather than refusing.
    if not P.base_json.exists():
        print("no company base yet — rendering the investor panel only")
        rows = []
    else:
        rows = load_base(args.investor)
    _, verdicts = load_ledger(args.investor)
    merged = merge_rows(rows, load(P.resolved, {}),
                        load(P.classification, {}))

    out = []
    for b in rows:
        r = {k: b.get(k) for k in ("slug", "name", "tier", "first_seen", "sector",
                                   "site_url", "formd_links", "edgar_links",
                                   "wayback_first_link")}
        r.update(merged[b["slug"]])
        v = verdicts.get(b["slug"], {})
        r.update({"membership_verdict": v.get("verdict"),
                  "membership_evidence": v.get("evidence_class"),
                  "membership_basis": v.get("basis")})
        row = {k: r.get(k) for k in REVIEW_FIELDS}
        row["sample"] = in_sample(row)
        out.append(row)

    out.sort(key=priority)
    data = json.dumps(out, separators=(",", ":")).replace("</script>", "<\\/script>")
    prof = json.dumps(profile_fields(args.investor),
                      separators=(",", ":")).replace("</script>", "<\\/script>")
    html = (REVIEW_TEMPLATE.replace("__DATA__", data)
            .replace("__PROFILE__", prof).replace("__INVESTOR__", args.investor))
    P.review_html.write_text(html, encoding="utf-8")
    print(f"wrote {P.review_html.relative_to(ROOT)} "
          f"({len(html)//1024} KB, {len(out)} rows)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("collect"); p.set_defaults(fn=cmd_collect)
    p.add_argument("investor")

    p = sub.add_parser("prepare"); p.set_defaults(fn=cmd_prepare)
    p.add_argument("investor")
    p.add_argument("--refresh", action="store_true", help="re-run the Form D rescan")

    p = sub.add_parser("record"); p.set_defaults(fn=cmd_record)
    p.add_argument("jsonl")
    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    p = sub.add_parser("verify"); p.set_defaults(fn=cmd_verify)
    p.add_argument("--skip-links", action="store_true",
                   help="skip the sampled evidence-link HTTP checks")
    p.add_argument("--base-only", action="store_true",
                   help="assert base structure + membership only (a company-base "
                        "run before its classification session)")
    p = sub.add_parser("export"); p.set_defaults(fn=cmd_export)
    p = sub.add_parser("review"); p.set_defaults(fn=cmd_review)

    for name, sp in sub.choices.items():
        if name not in ("collect", "prepare"):
            sp.add_argument("--investor", required=True)

    args = ap.parse_args()

    global P, CFG, SAMPLE_SLUGS
    P = Paths(args.investor)
    CFG = P.config()
    SAMPLE_SLUGS = set(CFG.get("sample_slugs", []))

    args.fn(args)


if __name__ == "__main__":
    main()
