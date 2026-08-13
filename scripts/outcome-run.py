#!/usr/bin/env python3
"""Driver for the current-valuation + graduation classification run.

Subcommands:
  prepare   pin the base, run every deterministic layer, emit the work queue
  status    resolved / pending counts, derived from disk
  record    merge a batch's JSONL answers into the durable classification
  verify    assertion suite; exits non-zero with the rows that need fixing

Two properties matter more than anything else here.

**The base is pinned.** It is rebuilt by other work in this repo (on 2026-08-10 it
gained 131 Tier A rows mid-session). A run reading the live base would see rows
appear and vanish underneath it. `prepare` snapshots it and every other command
reads the snapshot.

**Progress lives on disk, not in context.** The agent answering batches holds one
batch at a time and writes it back before taking the next, so an interrupted run
resumes at the first pending batch instead of restarting.
"""
import argparse
import csv
import hashlib
import json
import shutil
import sys
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import outcome_sources as S                                    # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = ROOT / "data" / "aggregation" / "company-base"
OUT = ROOT / "data" / "aggregation" / "outcomes"
QUEUE = OUT / "queue"

BATCH_SIZE = 45
CENSOR_MONTHS = 24

# Entry-round bands, in offering dollars. Deliberately coarse: Form D reports one
# amount and nothing else, so anything finer would be false precision. Reviewable
# because entry_offering_usd travels with the label.
STAGE_BANDS = ((1_000_000, "Pre-Seed"), (7_500_000, "Seed"), (30_000_000, "Series A"))
GRADUATION_MULTIPLE = 2.0
GRADUATION_FLOOR = 5_000_000

# ---- run 2: value tags, countries, regions -------------------------------
VALUE_TAGS = ("below_1b", "1b_plus", "10b_plus", "100b_plus")
VALID_STAGES = {"Pre-Seed", "Seed", "Series A", "Growth"}

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
    "United States of America": "United States",
    "UNITED KINGDOM": "United Kingdom", "Kingdom of the Netherlands": "Netherlands",
    "People's Republic of China": "China", "CHINA": "China",
    "KOREA, REPUBLIC OF": "South Korea", "Republic of Korea": "South Korea",
    "RUSSIAN FEDERATION": "Russia", "TAIWAN, PROVINCE OF CHINA": "Taiwan",
    "Republic of Ireland": "Ireland", "CZECHIA": "Czech Republic",
    "Czechia": "Czech Republic", "VIET NAM": "Vietnam",
    "UNITED ARAB EMIRATES": "United Arab Emirates", "HONG KONG": "Hong Kong",
}
REGION_OF = {}
for _reg, _cs in (
    ("North America", ["United States", "Canada"]),
    ("Europe", ["United Kingdom", "Germany", "France", "Netherlands", "Sweden",
                "Switzerland", "Belgium", "Ireland", "Spain", "Italy", "Denmark",
                "Norway", "Finland", "Austria", "Poland", "Portugal", "Estonia",
                "Lithuania", "Latvia", "Czech Republic", "Romania", "Bulgaria",
                "Hungary", "Greece", "Croatia", "Ukraine", "Russia", "Luxembourg",
                "Iceland", "Cyprus", "Malta", "Slovakia", "Slovenia", "Serbia"]),
    ("Middle East", ["Israel", "United Arab Emirates", "Saudi Arabia", "Bahrain",
                     "Qatar", "Kuwait", "Jordan", "Lebanon", "Turkey"]),
    ("Asia", ["China", "India", "Japan", "South Korea", "Singapore", "Hong Kong",
              "Taiwan", "Indonesia", "Vietnam", "Thailand", "Malaysia",
              "Philippines", "Pakistan", "Bangladesh", "Sri Lanka", "Kazakhstan"]),
    ("Latin America", ["Brazil", "Mexico", "Argentina", "Colombia", "Chile",
                       "Peru", "Uruguay", "Ecuador", "Costa Rica", "Panama",
                       "Guatemala", "Venezuela", "Dominican Republic", "Bahamas"]),
    ("Africa", ["Nigeria", "South Africa", "Kenya", "Egypt", "Ghana", "Morocco",
                "Tunisia", "Ethiopia", "Senegal", "Rwanda", "Uganda"]),
    ("Oceania", ["Australia", "New Zealand"]),
):
    for _c in _cs:
        REGION_OF[_c] = _reg


# Era-adjusted band ceilings (seed, series A) by entry year. Round sizes
# inflated roughly 5x between 2006 and 2022; one fixed cutoff put Block's
# $27.5M 2011 Series B under a 30M "Series A" ceiling.
ERA_BANDS = ((2010, 1_500_000, 12_000_000), (2014, 2_500_000, 15_000_000),
             (2018, 4_000_000, 20_000_000), (2021, 6_000_000, 30_000_000),
             (9999, 8_000_000, 40_000_000))


def era_band(usd: int | None, year: int | None) -> str | None:
    if not usd:
        return None
    year = year or 2016
    for cutoff, seed_max, a_max in ERA_BANDS:
        if year <= cutoff:
            if usd <= seed_max / 4:
                return "Pre-Seed"
            if usd <= seed_max:
                return "Seed"
            if usd <= a_max:
                return "Series A"
            return "Growth"
    return None


def structural_stage(rounds: list[dict], partner_accs: set,
                     year_inc: int | None) -> dict:
    """Label Sequoia's entry round from Form D STRUCTURE, not amount alone.

    The first partner-attributed filing is only a ceiling on entry recency
    (the run-3 golden set showed Airbnb's and Stripe's seeds never filed), so
    the result carries a confidence the knowledge layer may override:
      - >=2 filings before the entry filing        -> Growth
      - exactly 1 prior                             -> Series A or Growth by band
      - 0 priors AND founded >=2008 AND <=4y old    -> era band (sound first round)
      - 0 priors otherwise                          -> band at LOW confidence
        (coverage starts 2008; earlier rounds simply never filed)
    """
    seq = sorted((r for r in rounds if r.get("accessions")),
                 key=lambda r: (r.get("sale_date") or "9999",
                                min(r["accessions"])))
    entry_idx = next((i for i, r in enumerate(seq)
                      if partner_accs & set(r["accessions"])), None)
    if entry_idx is None:
        return {}
    e = seq[entry_idx]
    usd = e.get("offering_usd")
    year = int(e["sale_date"][:4]) if e.get("sale_date") else None
    prior = entry_idx
    band = era_band(usd, year)
    if prior >= 2:
        stage, conf = "Growth", "high"
    elif prior == 1:
        stage = "Growth" if band == "Growth" else "Series A"
        conf = "medium"
    else:
        # A zero-prior label is NEVER high confidence: seeds routinely skip
        # Form D under 4(a)(2) (Airbnb '09, Stripe '10), and year_inc resets on
        # holdco re-incorporation (Nubank's Cayman entity says 2016). Only
        # ordinality >= 2 earns "high"; the knowledge layer outranks this.
        stage = band
        covered = (year_inc or 0) >= 2008
        young = year is not None and year_inc and (year - year_inc) <= 4
        conf = "medium" if (covered and young) else "low"
    return {"stage": stage, "confidence": conf, "prior_filings": prior,
            "entry_usd": usd, "entry_year": year, "band": band,
            "age_at_entry": (year - year_inc) if (year and year_inc) else None}


def tag_of(usd: float | int) -> str:
    if usd >= 1e11:
        return "100b_plus"
    if usd >= 1e10:
        return "10b_plus"
    if usd >= 1e9:
        return "1b_plus"
    return "below_1b"


def canon_country(raw: str | None) -> str | None:
    """Normalize an ISSUERS state description, Wikidata label, or free-form
    country to one display name; US states collapse to United States; offshore
    filing havens return None (no signal)."""
    if not raw:
        return None
    raw = raw.strip()
    if raw.upper() in US_STATES:
        return "United States"
    if "CANADA" in raw.upper():
        return "Canada"
    if raw.upper() in OFFSHORE:
        return None
    if raw in COUNTRY_CANON:
        return COUNTRY_CANON[raw]
    if raw.upper() in COUNTRY_CANON:
        return COUNTRY_CANON[raw.upper()]
    if raw.isupper():  # EDGAR renders foreign countries in caps
        return " ".join(w if w in ("of", "and", "the") else w.capitalize()
                        for w in raw.lower().split())
    return raw


def today() -> str:
    return date.today().isoformat()


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def load_snapshot() -> list[dict]:
    snap = OUT / "base-snapshot.csv"
    if not snap.exists():
        sys.exit("no base snapshot; run `prepare` first")
    return list(csv.DictReader(open(snap)))


def load(name: str, default):
    p = OUT / name
    return json.loads(p.read_text()) if p.exists() else default


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


def never_merge_pairs() -> set:
    idm = BASE_DIR / "identity-merges.json"
    if not idm.exists():
        return set()
    return {frozenset(p["slugs"]) for p in
            json.loads(idm.read_text()).get("sequoia-capital", {}).get("never_merge", [])}


def flag_base_defects(resolved: dict, layer_a: dict, base: dict) -> None:
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

    never = never_merge_pairs()
    for slugs in by_cik.values():
        if len(slugs) > 1 and frozenset(slugs) not in never:
            for slug in slugs:
                flags = set(resolved[slug].get("flags") or [])
                flags.add("duplicate")
                resolved[slug]["flags"] = sorted(flags)

    for slug, rec in resolved.items():
        row = base.get(slug, {})
        if (rec.get("valuation_usd") or 0) >= 1e9 and row.get("tier") == "C" \
                and not (row.get("wayback_years") or "").strip():
            flags = set(rec.get("flags") or [])
            flags.add("suspect_base")
            rec["flags"] = sorted(flags)


# ---------------------------------------------------------------------------
# prepare
# ---------------------------------------------------------------------------

def cmd_prepare(args) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    QUEUE.mkdir(parents=True, exist_ok=True)

    live = BASE_DIR / f"{args.investor}.csv"
    snap = OUT / "base-snapshot.csv"
    if snap.exists() and not args.repin:
        print(f"using existing snapshot ({md5(snap)[:12]}); --repin to refresh")
    else:
        shutil.copy2(live, snap)
        print(f"pinned base -> {snap.relative_to(ROOT)}  md5={md5(snap)[:12]}")

    rows = load_snapshot()
    (OUT / "manifest.json").write_text(json.dumps({
        "investor": args.investor,
        "pinned_at": datetime.now().isoformat(timespec="seconds"),
        "base_md5": md5(snap), "base_rows": len(rows),
        "live_base_md5": md5(live),
    }, indent=1) + "\n")
    print(f"rows: {len(rows)}")

    # ---- Form D round sequences (offline rescan)
    rounds_path = OUT / "formd-rounds.json"
    if not rounds_path.exists() or args.refresh:
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "scripts" / "formd-issuer-rounds.py"),
                        args.investor, "--base", str(snap), "--out", str(rounds_path)],
                       check=True)
    formd = json.loads(rounds_path.read_text())

    # ---- Layer A: SEC public float
    index = S.load_cik_lookup()
    layer_a: dict[str, dict] = load("layer-a.json", {})
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
            (OUT / "layer-a.json").write_text(json.dumps(layer_a, indent=1))
            print(f"    {i}/{len(todo)}")
    (OUT / "layer-a.json").write_text(json.dumps(layer_a, indent=1))
    public = sum(1 for v in layer_a.values() if v.get("is_public"))
    print(f"    resolved a CIK: {sum(1 for v in layer_a.values() if v.get('cik'))}"
          f"   with public float: {public}")

    # ---- Layer B: Wikidata
    layer_b: dict[str, dict] = load("layer-b.json", {})
    pending = [r for r in rows if r["slug"] not in layer_b]
    print(f"layer B (Wikidata): {len(pending)} rows in batches of 60")
    for i in range(0, len(pending), 60):
        chunk = pending[i:i + 60]
        hits = S.wikidata_batch([r["name"] for r in chunk])
        for r in chunk:
            layer_b[r["slug"]] = hits.get(S.norm(r["name"]), {})
        (OUT / "layer-b.json").write_text(json.dumps(layer_b, indent=1))
        print(f"    {min(i + 60, len(pending))}/{len(pending)}")
    print(f"    matched: {sum(1 for v in layer_b.values() if v)}")

    # ---- Layer C: unicorn list
    uni = S.load_unicorn_list()
    print(f"layer C (unicorn list): {len(uni['current'])} current, "
          f"{len(uni['former'])} former")

    # ---- Graduation layer 1, entry anchored at partner-attributed filings
    partner_accs = {
        r["slug"]: {a.strip() for a in (r.get("formd_accessions") or "").split(";")
                    if a.strip()}
        for r in rows}
    grad = {slug: graduation_from_formd(rec["rounds"], partner_accs.get(slug, set()))
            for slug, rec in formd.items()}
    (OUT / "graduation-formd.json").write_text(json.dumps(grad, indent=1))
    determined = sum(1 for g in grad.values() if g.get("seed_to_a_graduation") is not None)
    seeds = sum(1 for g in grad.values() if g.get("entry_stage") == "Seed")
    anchored = sum(1 for g in grad.values() if g.get("prior_rounds", 0) > 0)
    print(f"graduation layer 1: {len(grad)} companies, {seeds} entered at Seed, "
          f"{determined} decided deterministically, "
          f"{anchored} entries moved past pre-investor rounds")

    # ---- Issuer evidence: entry-time addresses + name histories (offline)
    ev_path = OUT / "issuer-evidence.json"
    if not ev_path.exists() or args.refresh:
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "scripts" / "formd-issuer-evidence.py"),
                        str(OUT / "base-snapshot.csv")], check=True)
    issuer_ev = json.loads(ev_path.read_text()).get("accessions", {})

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
    cls_prev = load("classification.json", {})
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
            rec["country"] = fd_country
            rec["country_source"] = "formd_address"
        elif canon_country(b.get("country")):
            rec["country"] = canon_country(b["country"])
            rec["country_source"] = "wikidata"

        if a.get("valuation_usd") or a.get("status"):
            rec.update({k: v for k, v in a.items()
                        if k in ("status", "valuation_usd", "valuation_asof",
                                 "valuation_source", "valuation_confidence",
                                 "is_public", "public_since")})
            rec["flags"] = sorted(set(rec.get("flags", []) + a.get("flags", [])))
        elif b.get("dissolved"):
            rec.update({"status": "defunct", "valuation_usd": None,
                        "valuation_source": "wikidata",
                        "valuation_asof": b["dissolved"],
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
            if not rec.get("country") and canon_country(u.get("country")):
                rec["country"] = canon_country(u["country"])
                rec["country_source"] = "wikidata"
            rec["flags"] = sorted(set(rec.get("flags", []) + ["unicorn_name_match"]))

        if rec.get("valuation_usd"):
            rec["value_tag"] = tag_of(rec["valuation_usd"])
            rec["value_tag_source"] = rec.get("valuation_source")
        if rec.get("country"):
            rec["region"] = REGION_OF.get(rec["country"])

        # ---- run-2 gap queue: what the deterministic layers plus the existing
        # classification still leave open for this row.
        overlaid = dict(rec)
        overlaid.update({k: v for k, v in cls_prev.get(slug, {}).items()
                         if v is not None})
        flags_now = set(overlaid.get("flags") or []) | set(rec.get("flags") or [])
        need = [f for f in ("status", "country", "entry_stage") if not overlaid.get(f)]
        # Rows awaiting web evidence keep value_tag open for the web pass; the
        # batch judge may only ever rule DOWN to below_1b, never mint a figure.
        if not overlaid.get("value_tag") and "needs_web_value" not in flags_now:
            need.append("value_tag")
        if need:
            e = issuer_ev.get(fd_acc, {}) if fd_acc else {}
            queue.append({
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
                "issuer_city": e.get("city"), "issuer_state": e.get("state_desc"),
                "year_inc": e.get("year_inc"),
                "former_unicorn": uni["former"].get(S.norm(row["name"])),
                "known": {k: overlaid.get(k) for k in
                          ("status", "valuation_usd", "entry_stage",
                           "seed_to_a_graduation", "country", "value_tag", "note")
                          if overlaid.get(k) is not None},
                "need": need,
            })
        resolved[slug] = rec

    flag_base_defects(resolved, layer_a, {r["slug"]: r for r in rows})
    (OUT / "resolved.json").write_text(json.dumps(resolved, indent=1))

    for f in QUEUE.glob("batch-*.json"):
        f.unlink()
    for i in range(0, len(queue), BATCH_SIZE):
        n = i // BATCH_SIZE + 1
        (QUEUE / f"batch-{n:03d}.json").write_text(
            json.dumps(queue[i:i + BATCH_SIZE], indent=1))

    batches = (len(queue) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"\ndeterministically resolved: {len(rows) - len(queue)}/{len(rows)}")
    print(f"queued for classification : {len(queue)} rows in {batches} batches")


# ---------------------------------------------------------------------------
# status / record / verify
# ---------------------------------------------------------------------------

def cmd_status(_args) -> None:
    rows = load_snapshot()
    cls = load("classification.json", {})
    batches = sorted(QUEUE.glob("batch-*.json"))
    done = [b for b in batches if all(
        r["slug"] in cls for r in json.loads(b.read_text()))]
    print(f"base rows        : {len(rows)}")
    print(f"batches          : {len(done)}/{len(batches)} recorded")
    print(f"classified rows  : {len(cls)}")
    pending = [b.name for b in batches if b not in done]
    print(f"next pending     : {pending[0] if pending else 'none'}")


VALID_STATUS = {"private", "public", "acquired", "defunct", "unknown"}
VALID_CONF = {"high", "medium", "low"}
# Sources allowed to carry a dollar figure. `model_knowledge` is deliberately
# absent: the model classifies and disputes, but never mints a number. A figure
# the model believes in must be pinned by the web pass (-> web_verified) before
# it may appear.
VALUE_SOURCES = {"sec_public_float", "wikidata", "unicorn_list", "web_verified"}


def validate_record(rec: dict, slugs: set[str]) -> list[str]:
    errs = []
    slug = rec.get("slug")
    if not slug or slug not in slugs:
        return [f"slug {slug!r} not in the pinned base"]
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
                "entry_stage_confidence", "country_confidence"):
        if rec.get(key) is not None and rec[key] not in VALID_CONF:
            errs.append(f"{slug}: bad {key} {rec[key]!r}")
    if rec.get("value_tag") is not None:
        if rec["value_tag"] not in VALUE_TAGS:
            errs.append(f"{slug}: value_tag {rec['value_tag']!r}")
        elif rec["value_tag"] != "below_1b" and not rec.get("valuation_usd"):
            errs.append(f"{slug}: value_tag {rec['value_tag']} without a sourced figure")
    if rec.get("entry_stage") is not None and rec["entry_stage"] not in VALID_STAGES:
        errs.append(f"{slug}: entry_stage {rec['entry_stage']!r}")
    if rec.get("entry_stage_source") is not None and rec["entry_stage_source"] not in (
            "formd_band", "formd_structural", "model", "web_verified"):
        errs.append(f"{slug}: entry_stage_source {rec['entry_stage_source']!r}")
    # web_verified stage claims must carry their citation (ENTRY-STAGE.md 1)
    if rec.get("entry_stage_source") == "web_verified" \
            and not (rec.get("entry_stage_citation") or "").strip():
        errs.append(f"{slug}: web_verified stage without entry_stage_citation")
    for key in ("valuation_citation", "country_citation", "entry_stage_citation"):
        v = rec.get(key)
        if v is not None and (not isinstance(v, str) or not v.startswith("http")):
            errs.append(f"{slug}: {key} must be a URL")
    if rec.get("country_source") is not None and rec["country_source"] not in (
            "formd_address", "wikidata", "model_knowledge", "web_verified"):
        errs.append(f"{slug}: country_source {rec['country_source']!r}")
    for key in ("flags", "clear_flags"):
        if key in rec and not isinstance(rec[key], list):
            errs.append(f"{slug}: {key} must be a list")
    return errs


def cmd_record(args) -> None:
    src = Path(args.jsonl)
    slugs = {r["slug"] for r in load_snapshot()}
    cls = load("classification.json", {})
    incoming, errors = {}, []
    for n, line in enumerate(src.read_text().splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"line {n}: {e}")
            continue
        errors.extend(validate_record(rec, slugs))
        incoming[rec["slug"]] = rec
    if errors:
        print(f"REJECTED — {len(errors)} problem(s), nothing recorded:")
        for e in errors[:25]:
            print("  -", e)
        sys.exit(1)
    # A record replaces only the keys it carries. Since run 2, that holds
    # within classification.json too: a second-pass answer (country, entry
    # stage, value tag) merges per key into the existing record instead of
    # replacing it, flags union, and only an explicit clear_flags list may
    # remove a flag (the web pass clearing needs_web_value after pinning).
    for slug, rec in incoming.items():
        prev = cls.get(slug)
        if prev is None:
            rec["flags"] = sorted(set(rec.get("flags") or [])
                                  - set(rec.pop("clear_flags", [])))
            cls[slug] = rec
            continue
        fl = set(prev.get("flags") or []) | set(rec.get("flags") or [])
        fl -= set(rec.get("clear_flags") or [])
        old_note = prev.get("note")
        prev.update({k: v for k, v in rec.items()
                     if k not in ("flags", "clear_flags")})
        prev["flags"] = sorted(fl)
        if old_note and rec.get("note") and rec["note"] not in old_note:
            prev["note"] = f"{old_note} | {rec['note']}"
    # normalize country renderings at the door
    for rec in incoming.values():
        tgt = cls[rec["slug"]]
        if tgt.get("country"):
            tgt["country"] = canon_country(tgt["country"]) or tgt["country"]
            tgt["region"] = REGION_OF.get(tgt["country"])
    (OUT / "classification.json").write_text(json.dumps(cls, indent=1, sort_keys=True))
    print(f"recorded {len(incoming)} rows; classification now holds {len(cls)}")


def cmd_verify(_args) -> None:
    rows = load_snapshot()
    resolved = load("resolved.json", {})
    cls = load("classification.json", {})
    problems: list[str] = []

    live = BASE_DIR / f"{json.loads((OUT / 'manifest.json').read_text())['investor']}.csv"
    manifest = json.loads((OUT / "manifest.json").read_text())
    if md5(live) != manifest["live_base_md5"]:
        problems.append("live base has changed since prepare; re-run prepare to re-pin")

    merged = {}
    for row in rows:
        slug = row["slug"]
        rec = dict(resolved.get(slug, {}))
        overlay = cls.get(slug, {})
        # Flags are additive across layers: a batch answer must not be able to
        # clear a deterministic flag (duplicate, boundary, ...) by emitting its
        # own list. Everything else is a per-key override.
        base_flags = set(rec.get("flags") or [])
        rec.update(overlay)
        rec["flags"] = sorted(base_flags | set(overlay.get("flags") or []))
        rec["region"] = REGION_OF.get(rec.get("country"))
        merged[slug] = rec

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

        # ---- run-2 invariants: full fills, tag/figure consistency
        tag, usd = rec.get("value_tag"), rec.get("valuation_usd")
        if not tag:
            problems.append(f"{slug}: no value_tag")
        elif tag not in VALUE_TAGS:
            problems.append(f"{slug}: value_tag {tag!r} not in vocabulary")
        elif usd and tag != tag_of(usd):
            problems.append(f"{slug}: value_tag {tag} disagrees with figure {usd:,.0f}")
        elif tag != "below_1b" and not usd:
            problems.append(f"{slug}: value_tag {tag} without a sourced figure")
        if not rec.get("country"):
            problems.append(f"{slug}: no country")
        elif rec["country"] not in REGION_OF:
            problems.append(f"{slug}: country {rec['country']!r} has no region mapping")
        if not rec.get("entry_stage"):
            problems.append(f"{slug}: no entry_stage")
        elif rec["entry_stage"] not in VALID_STAGES:
            problems.append(f"{slug}: entry_stage {rec['entry_stage']!r} not in vocabulary")
        # ENTRY-STAGE.md invariant 2: a bucket-visible row needs class 1/2
        # stage evidence (a citation, or the deterministic filing structure).
        stage_cited = bool((rec.get("entry_stage_citation") or "").strip()) \
            or rec.get("entry_stage_source") in ("formd_structural", "formd_band")
        flags_now = set(rec.get("flags") or [])
        if (rec.get("value_tag") in ("1b_plus", "10b_plus", "100b_plus")
                and not stage_cited and "cite_pending" not in flags_now):
            problems.append(f"{slug}: $1B+ row without cited/structural entry stage "
                            f"and no cite_pending marker")
        # CLASSIFICATION-V2.md invariant 1: public $1B+ value is a cited market cap
        if rec.get("is_public") and rec.get("value_tag") in (
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
    layer_a = load("layer-a.json", {})
    snapshot_slugs = {r["slug"] for r in rows}
    idm = BASE_DIR / "identity-merges.json"
    proven_distinct = set()
    if idm.exists():
        proven_distinct = {
            frozenset(p["slugs"]) for p in
            json.loads(idm.read_text()).get("sequoia-capital", {}).get("never_merge", [])}
    by_cik: dict[str, list[str]] = {}
    for slug, rec in layer_a.items():
        if rec.get("cik") and slug in snapshot_slugs:
            by_cik.setdefault(rec["cik"], []).append(slug)
    dupes = {c: s for c, s in by_cik.items()
             if len(s) > 1 and frozenset(s) not in proven_distinct}
    if dupes:
        print(f"\nduplicate companies (same SEC registrant): {len(dupes)} groups")
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
    from collections import Counter
    tags = Counter(r.get("value_tag") for r in merged.values())
    print(f"value_tag       : {dict(tags.most_common())}")
    regions = Counter(r.get("region") for r in merged.values())
    print(f"region          : {dict(regions.most_common())}")
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

    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems[:40]:
            print("  -", p)
        sys.exit(1)
    print("\nverify: clean")


EXPORT_COLUMNS = [
    "slug", "name", "status", "value_tag", "value_tag_source",
    "valuation_usd", "valuation_asof",
    "valuation_source", "valuation_confidence", "is_public", "public_since",
    "entry_stage", "entry_stage_source", "entry_stage_confidence",
    "entry_stage_citation", "valuation_citation", "country_citation",
    "entry_offering_usd", "entry_quarter", "prior_rounds",
    "round_count", "next_offering_usd", "next_quarter", "seed_to_a_graduation",
    "graduation_source", "graduation_confidence",
    "country", "country_source", "region", "flags",
    "tier", "first_seen", "sector", "cik", "note",
]


def cmd_stage_queue(_args) -> None:
    """Emit the run-3 entry-stage re-judgment queue: EVERY row, briefed with the
    structural Form D evidence, judged fresh (no run-2 answer in the brief)."""
    rows = load_snapshot()
    formd = load("formd-rounds.json", {})
    issuer_ev = load("issuer-evidence.json", {}).get("accessions", {})
    structural, queue = {}, []
    for row in rows:
        slug = row["slug"]
        partner_accs = {a.strip() for a in (row.get("formd_accessions") or "").split(";")
                        if a.strip()}
        year_inc = None
        for acc in sorted(partner_accs):
            yi = (issuer_ev.get(acc) or {}).get("year_inc")
            if yi and str(yi).isdigit():
                year_inc = int(yi)
                break
        s = structural_stage(formd.get(slug, {}).get("rounds", []),
                             partner_accs, year_inc)
        if s:
            structural[slug] = s
        queue.append({
            "slug": slug, "name": row["name"], "sector": row.get("sector"),
            "first_seen": row.get("first_seen"), "tier": row.get("tier"),
            "year_inc": year_inc,
            "rounds": [{"q": r.get("quarter"), "usd": r.get("offering_usd"),
                        "sale": r.get("sale_date"),
                        "partner": bool(partner_accs & set(r.get("accessions") or []))}
                       for r in formd.get(slug, {}).get("rounds", [])],
            "structural": s or None,
        })
    (OUT / "stage-structural.json").write_text(json.dumps(structural, indent=1))
    for f in QUEUE.glob("stage-*.json"):
        f.unlink()
    for i in range(0, len(queue), 50):
        (QUEUE / f"stage-{i // 50 + 1:03d}.json").write_text(
            json.dumps(queue[i:i + 50], indent=1))
    print(f"structural labels: {len(structural)}; "
          f"queued {len(queue)} rows in {(len(queue) + 49) // 50} stage batches")


def cmd_export(_args) -> None:
    """Write the review-table CSV: snapshot + deterministic + classification."""
    rows = load_snapshot()
    resolved = load("resolved.json", {})
    cls = load("classification.json", {})
    layer_a = load("layer-a.json", {})
    investor = json.loads((OUT / "manifest.json").read_text())["investor"]

    out_rows = []
    for row in rows:
        slug = row["slug"]
        rec = dict(resolved.get(slug, {}))
        overlay = cls.get(slug, {})
        base_flags = set(rec.get("flags") or [])
        rec.update(overlay)
        rec["flags"] = sorted(base_flags | set(overlay.get("flags") or []))
        rec["region"] = REGION_OF.get(rec.get("country"))
        rec.update({"slug": slug, "name": row["name"], "tier": row.get("tier"),
                    "first_seen": row.get("first_seen"), "sector": row.get("sector"),
                    "cik": layer_a.get(slug, {}).get("cik")})
        rec["flags"] = ";".join(rec.get("flags") or [])
        out_rows.append({k: rec.get(k, "") for k in EXPORT_COLUMNS})

    dest = OUT / f"{investor}-companies.csv"
    with open(dest, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_COLUMNS)
        w.writeheader()
        w.writerows(out_rows)
    print(f"wrote {dest.relative_to(ROOT)} ({len(out_rows)} rows)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("prepare"); p.set_defaults(fn=cmd_prepare)
    p.add_argument("investor", nargs="?", default="sequoia-capital")
    p.add_argument("--repin", action="store_true", help="refresh the pinned snapshot")
    p.add_argument("--refresh", action="store_true", help="re-run the Form D rescan")

    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    p = sub.add_parser("record"); p.set_defaults(fn=cmd_record)
    p.add_argument("jsonl")
    p = sub.add_parser("verify"); p.set_defaults(fn=cmd_verify)
    p = sub.add_parser("stage-queue"); p.set_defaults(fn=cmd_stage_queue)
    p = sub.add_parser("export"); p.set_defaults(fn=cmd_export)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
