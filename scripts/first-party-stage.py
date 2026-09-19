#!/usr/bin/env python3
"""Re-source every weakly-staged row from the firm's own listing (PRO-135).

PRO-131 (a) made the firm's own listing class-1 `first_party` entry_stage
evidence where it gives a round word, and PRO-135 item 1 says that pass runs
before the sweep spends a single web fetch: the source is already on disk under
`sources/site/`, `build-company-base.py` now resolves it to `site_entry_round`,
and every row it reaches is a row that does not have to be written
`undetermined`.

A row is WEAK when its stage rests on something PRO-135 retires:

  * an empty `entry_stage_source`            (item 3, 214 rows, all Lux)
  * the retired `stage_prior` flag           (item 2, 950 rows)
  * `model`, on a row the listing can source (item 1)
  * `web_verified` on a citation shared by SHARED_CITATION_MIN rows or more
                                             (item 4, 526 rows)

and the pass splits what it can do to one into three:

  RESOURCE   the listing agrees with the stage already published. Nothing the
             reader sees changes; the provenance is repaired. Safe at any
             visibility, because no value moves.
  RESTAGE    the listing names a different round. Below $1B and pre-2021 this
             lands, because class-1 first-party evidence outranks what it
             replaces (a model guess, an inferred prior, an index page). On a
             $1B+ or post-2020 row it does NOT land: those are exactly the rows
             where "the firm led the A" folklore fails and where a documented
             round must override the site's own label (COLLECTION.md 6, the
             socure and Personio classes), so they are listed for the judge.
  RESIDUE    the listing has no round word for the row. Nothing here is
             written: the row goes to the judge, and `undetermined` is the
             answer where the record does not give the round.

Usage: python3 scripts/first-party-stage.py <investor> [--apply]
       (without --apply it only reports; --apply writes the batch and records it)
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("investor")
ap.add_argument("--apply", action="store_true",
                help="write scratch/first-party-stage.jsonl and record it")
args = ap.parse_args()
P = Paths(args.investor)
CFG = P.config()
CONF = (CFG.get("site_api") or {}).get("entry_stage_confidence") or "medium"

SHARED_MIN = 10
VISIBLE_RANGES = {"1b_plus", "10b_plus", "100b_plus"}

base = {r["slug"]: r for r in json.loads(P.base_json.read_text())}
# A row ruled out of the book is not staged, whatever its listing says: it
# leaves base.json at the next rebuild and nothing published reads it.
_led = json.loads(P.ledger.read_text()) if P.ledger.exists() else {}
not_members = {slug for book in _led.values()
               for slug, v in ((book or {}).get("verdicts") or {}).items()
               if (v or {}).get("verdict") == "not_member"}
cls = json.loads(P.classification.read_text()) if P.classification.exists() else {}

shared = {}
for rec in cls.values():
    c = (rec.get("entry_stage_citation") or "").strip()
    if c:
        shared[c] = shared.get(c, 0) + 1
shared = {c for c, n in shared.items() if n >= SHARED_MIN}


def weakness(rec: dict) -> str | None:
    """Why this row's stage does not survive PRO-135, or None if it does."""
    stage = rec.get("entry_stage")
    if stage in (None, "undetermined"):
        return "unstaged" if stage is None else None
    src = rec.get("entry_stage_source")
    if not src:
        return "no source"
    if "stage_prior" in (rec.get("flags") or []):
        return "stage_prior"
    if src == "model":
        return "model"
    if src == "web_verified" and (rec.get("entry_stage_citation") or "").strip() in shared:
        return "shared citation"
    return None


def visible(rec: dict) -> bool:
    """A row whose stage a reader can see against the record: the big marks and
    the recent ones, which is where the firm's own label goes wrong."""
    if rec.get("valuation_range") in VISIBLE_RANGES:
        return True
    year = str(rec.get("entry_date") or "")[:4]
    return year.isdigit() and int(year) >= 2021


# A weak row is not necessarily a defect. `model` is rungs 3 and 4 of the
# evidence order and stays legal where the pass can name the company's round in
# the note; the harvest simply outranks it where the listing has the round word.
# The three classes PRO-135 REFUSES must end up somewhere else or read
# `undetermined`, so they are counted apart.
REFUSED = {"no source", "stage_prior", "shared citation"}

lines, review, residue, counts = [], [], [], {}
for slug, rec in sorted(cls.items()):
    why = weakness(rec)
    if not why or slug in not_members:
        continue
    counts[why] = counts.get(why, 0) + 1
    row = base.get(slug) or {}
    lab = row.get("site_entry_round")
    cite = row.get("site_entry_stage_citation")
    if not lab or not cite:
        residue.append((slug, why, rec.get("entry_stage")))
        continue
    same = lab == rec.get("entry_stage")
    if not same and visible(rec):
        review.append((slug, why, rec.get("entry_stage"), lab, rec.get("valuation_range")))
        continue
    # `record` merges per key, so a fresh `note` would REPLACE the row's audit
    # trail rather than extend it. Append.
    said = (f"Entry round from the firm's own listing "
            f"({row.get('site_entry_stage') or lab}); replaces {why}"
            + ("" if same else f" and the {rec.get('entry_stage')} it carried"))
    prev = (rec.get("note") or "").strip()
    out = {
        "slug": slug,
        "entry_stage": lab,
        "entry_stage_source": "first_party",
        "entry_stage_citation": cite,
        "entry_stage_confidence": CONF,
        "note": f"{prev} | {said}" if prev else said,
    }
    if "stage_prior" in (rec.get("flags") or []):
        out["clear_flags"] = ["stage_prior"]
    lines.append(out)

resourced = sum(1 for x in lines if x["entry_stage"] == cls[x["slug"]].get("entry_stage"))
print(f"{args.investor}: {sum(counts.values())} weak rows {counts}")
print(f"  re-source (value unchanged): {resourced}")
print(f"  re-stage  (value changes):   {len(lines) - resourced}")
print(f"  for the judge ($1B+/recent): {len(review)}")
must = [r for r in residue if r[1] in REFUSED]
print(f"  no round word, keeps {'{'}model{'}'}:     {len(residue) - len(must)}")
print(f"  no round word, MUST resolve:  {len(must)}")
if must:
    byclass: dict[str, int] = {}
    for _, why, _ in must:
        byclass[why] = byclass.get(why, 0) + 1
    print(f"      {byclass}")
for slug, why, was, now, val in review[:15]:
    print(f"      {slug}: {was} -> {now} ({why}, {val})")

if args.apply and lines:
    out = P.scratch / "first-party-stage.jsonl"
    out.write_text("".join(json.dumps(x) + "\n" for x in lines))
    print(f"  wrote {out} ({len(lines)} lines)")
    subprocess.run([sys.executable, str(Path(__file__).with_name("run.py")),
                    "record", "--investor", args.investor, str(out)],
                   check=True)
