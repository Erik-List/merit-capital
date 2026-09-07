#!/usr/bin/env python3
"""Machinery for the classification half of the grind.

The judge supplies, per slug, only what it actually decided:

    J = {
      "plaid":  ("private", "US", "10b_plus", 6_100_000_000,
                 "https://stockanalysis.com/...", "note"),
      "aardvark": ("acquired", "US", None, None, None, "acq. by Google, 2010"),
    }

Everything mechanical is filled here rather than retyped 600 times:

* `entry_stage` comes from the row's own `site_entry_stage` -- the resolved
  first-party layer (decisions.md R3) -- mapped into the published taxonomy,
  cited to the surface that carried it: the firm's company page where the CMS
  supplied it, the archived listing where the circles did. §6 ranks "the
  firm's own memo/company page" as class 1 `web_verified`, which is what the
  gate measured it as.
* Only the columns the queue ASKED for are emitted (§8), plus the one licensed
  exception: a deliberate dispute of a value a deterministic layer pre-filled.
* `valuation_range` >= 1b_plus is refused without a sourced figure, and a
  figure is refused on a non-private/public status, so a slip becomes an error
  here rather than a `record` rejection later.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "scratch" / "queue"
SITE = "https://www.felicis.com/companies/"
PORTFOLIO = "https://www.felicis.com/portfolio"

# Which surface actually carries the firm's stage claim for a given row.
# /companies/<slug> 308-redirects to /portfolio for every company without a
# dedicated page (only 17 have one), so citing it for the other 200-odd rows
# would be citing a redirect. The portfolio page IS the CMS rendering that
# publishes the stage, so it is the honest citation for those; a circles-only
# row is not on the live site at all and is cited to the archived listing that
# carried its round ladder.
_layer = json.loads((ROOT / "sources" / "site" / "entry-stage-layer.json").read_text())
_cms = json.loads((ROOT / "sources" / "site" / "sanity-companies.json").read_text())


def _key(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


_BASIS = {_key(r["name"]): r["stage_basis"] for r in _layer["rows"]}
_HASPAGE = {_key(r["name"]): (r.get("slug"), bool(r.get("has_page")))
            for r in _cms["rows"]}


def stage_citation(item):
    """The URL that names the firm's own stage claim for this row."""
    k = _key(item.get("name"))
    basis = _BASIS.get(k)
    if basis == "circles_only":
        return item.get("wayback_first_link") or None
    slug, has_page = _HASPAGE.get(k, (None, False))
    if has_page and slug:
        return SITE + slug
    return PORTFOLIO

TAXO = {"pre-seed": "Pre-Seed", "seed": "Seed", "series a": "Series A"}


def taxonomy(word):
    if not word:
        return None
    w = str(word).strip().lower()
    if w in TAXO:
        return TAXO[w]
    if re.match(r"^series [b-z]$", w) or w in {"common", "growth"}:
        return "Growth"
    return None


# Slugs that fix-slug-variants.py renames in the parsed sources. They are
# still in THIS queue (it was built before the fix) but will not exist after
# the scheduled rebuild, so classifying them now would leave orphaned overlay
# keys and fail verify's drift invariant (§10.8). They are skipped here and
# picked up as canonical rows in the post-rebuild delta.
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("_fsv", Path(__file__).with_name("fix-slug-variants.py"))
_fsv = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_fsv)
VARIANTS = set(_fsv.MAP) | set(_fsv.REJECTS)


def load(batch: int):
    return json.loads((QUEUE / f"batch-{batch:03d}.json").read_text())


def build(batch: int, J: dict, *, country_disputes: dict | None = None,
          stage_overrides: dict | None = None, extra: dict | None = None):
    """Return the classification lines for one batch."""
    items = {x["slug"]: x for x in load(batch)}
    country_disputes = country_disputes or {}
    stage_overrides = stage_overrides or {}
    extra = extra or {}
    lines, missing = [], []

    for slug, item in items.items():
        need = set(item["need"])
        if "membership" in need and slug not in J:
            continue                      # handled by judge-membership.py
        if slug in VARIANTS:
            continue                      # renamed at the rebuild
        if slug not in J:
            missing.append(slug)
            continue
        status, country, vrange, vusd, cite, note = (list(J[slug]) + [None] * 6)[:6]
        row = {"slug": slug, "who": WHO}

        if "status" in need and status:
            row["status"] = status
        if "hq_country" in need and country:
            row["hq_country"] = country
            row["hq_country_source"] = "model_knowledge"
            row["hq_country_confidence"] = "high"
        if "valuation_range" in need and vrange:
            row["valuation_range"] = vrange
            row["valuation_confidence"] = "high"
            if vrange != "below_1b":
                if not vusd:
                    raise SystemExit(f"{slug}: {vrange} without a figure")
                if status not in ("private", "public"):
                    raise SystemExit(f"{slug}: figure on status {status}")
                row["valuation_usd"] = vusd
                row["valuation_source"] = "web_verified"
                row["valuation_range_source"] = "web_verified"
                if not cite:
                    raise SystemExit(f"{slug}: {vrange} without a citation")
                row["valuation_citation"] = cite

        if "entry_stage" in need:
            st = stage_overrides.get(slug)
            if st:
                stage, src, scite = st
                # Overrides go through the same taxonomy map as the layer, so
                # a judge writing the round word ("Series B") cannot leak a
                # value outside the published four.
                stage = taxonomy(stage) or stage
            else:
                stage = taxonomy(item.get("site_entry_stage"))
                src, scite = ("web_verified", stage_citation(item)) if stage else (None, None)
                if stage and not scite:
                    src, scite = "model", None
            if stage:
                row["entry_stage"] = stage
                row["entry_stage_confidence"] = "high"
                if src:
                    row["entry_stage_source"] = src
                if scite:
                    row["entry_stage_citation"] = scite

        # The licensed exception (§8): a deliberate dispute of a value a
        # deterministic layer pre-filled and the queue therefore never asked
        # about. Ruling R5 -- the Wikidata single-token joins.
        if slug in country_disputes:
            cc, why = country_disputes[slug]
            row["hq_country"] = cc
            row["hq_country_source"] = "model_knowledge"
            row["hq_country_confidence"] = "high"
            row.setdefault("flags", []).append("model_disputes_source")
            note = f"{note + ' ' if note else ''}{why}"

        if note:
            row["note"] = note
        for k, v in (extra.get(slug) or {}).items():
            if k in ("flags", "clear_flags"):
                row[k] = sorted(set(row.get(k, [])) | set(v))
            else:
                row[k] = v
        lines.append(row)

    if missing:
        raise SystemExit(f"batch {batch}: {len(missing)} rows unjudged: {missing}")
    return lines


def write(batch: int, lines: list[dict]):
    out = QUEUE / f"batch-{batch:03d}.out.jsonl"
    prev = [l for l in (out.read_text().splitlines() if out.exists() else []) if l.strip()]
    seen = {(json.loads(l)["slug"], "verdict" in json.loads(l)) for l in prev}
    new = [json.dumps(r, ensure_ascii=False) for r in lines
           if (r["slug"], False) not in seen]
    out.write_text("\n".join(prev + new) + "\n")
    print(f"batch-{batch:03d}.out.jsonl: {len(prev)} existing + {len(new)} classification")
    return out
