#!/usr/bin/env python3
"""Carry an investor's overlays across a base rebuild that renames a slug.

A base row's slug is derived from its display name, and the builder picks the
name from the most recent rendering it can see (c8f28f7). So a rebuild can
rename a row it has not otherwise touched — `MapR Technology` became `MapR`,
`Sidecar Technologies, Inc.` became `Sidecar` — and every overlay joins on the
slug. Left alone the row loses its verdict and its classification, reappears
unjudged, and `verify` reports the old key as stale rather than as work thrown
away: nine Lightspeed rows, two Accel, two Spark, on a single rebuild.

The rename is provable rather than guessed. Each base row carries evidence that
identifies it independently of its name — the site id or URL the listing gave
it, its CIK, its Form D accessions, the wayback capture it was first seen in —
and a rename leaves every one of those untouched. So an old slug that has
vanished and a new slug that has appeared are the SAME ROW when they share one
of those keys and nothing else claims it. Where no key matches, nothing moves
and the pair is reported: a row that genuinely left the base and a row that
genuinely arrived look exactly like a rename from the slug alone, and only the
evidence tells them apart.
"""
from __future__ import annotations

import json
from pathlib import Path

# Strongest first. Each is unique to one company by construction; a value shared
# by two rows on either side is dropped rather than trusted.
_IDENTITY_KEYS = ("_site_id", "site_url", "edgar_cik", "formd_accessions",
                  "wayback_first_link")


def _fingerprints(row: dict) -> list[tuple[str, str]]:
    out = []
    for k in _IDENTITY_KEYS:
        v = row.get(k)
        if v in (None, "", [], {}):
            continue
        # A multi-valued field identifies by its first member, which is the
        # earliest filing or capture and does not move when later ones land.
        if isinstance(v, str) and ";" in v:
            v = v.split(";")[0]
        out.append((k, str(v).strip()))
    return out


def _unique_index(rows: list[dict]) -> dict[tuple[str, str], str]:
    """fingerprint -> slug, keeping only fingerprints held by exactly one row."""
    seen: dict[tuple[str, str], list[str]] = {}
    for r in rows:
        for fp in _fingerprints(r):
            seen.setdefault(fp, []).append(r["slug"])
    return {fp: slugs[0] for fp, slugs in seen.items() if len(slugs) == 1}


def _name_key(row: dict) -> str:
    return "".join(ch for ch in str(row.get("name") or "").lower() if ch.isalnum())


def rename_map(old_rows: list[dict], new_rows: list[dict]) -> dict[str, str]:
    """Old slug -> new slug, for rows the rebuild renamed."""
    old_slugs = {r["slug"] for r in old_rows}
    new_slugs = {r["slug"] for r in new_rows}
    gone = old_slugs - new_slugs
    arrived = new_slugs - old_slugs
    if not gone or not arrived:
        return {}
    left = [r for r in old_rows if r["slug"] in gone]
    right = [r for r in new_rows if r["slug"] in arrived]
    index = _unique_index(right)
    out: dict[str, str] = {}
    claimed: set[str] = set()
    for r in left:
        for fp in _fingerprints(r):
            hit = index.get(fp)
            if hit and hit not in claimed:
                out[r["slug"]] = hit
                claimed.add(hit)
                break
    # A row whose only evidence is a listing INDEX capture has no unique
    # fingerprint — several rows were first seen on the same page — so the
    # match above refuses it. Fall back to the name, which the rebuild only
    # ever shortens or re-renders: `Icebreaker / Crush or Flush` became
    # `Icebreaker`. Accepted only when the containment is unambiguous in both
    # directions, so a genuine departure and a genuine arrival never pair up.
    for r in left:
        if r["slug"] in out:
            continue
        a = _name_key(r)
        if len(a) < 4:
            continue
        cands = [n for n in right
                 if n["slug"] not in claimed and _name_key(n)
                 and len(_name_key(n)) >= 4
                 and (a.startswith(_name_key(n)) or _name_key(n).startswith(a))]
        if len(cands) == 1 and sum(
                1 for o in left if o["slug"] not in out
                and (_name_key(o).startswith(_name_key(cands[0]))
                     or _name_key(cands[0]).startswith(_name_key(o)))) == 1:
            out[r["slug"]] = cands[0]["slug"]
            claimed.add(cands[0]["slug"])
    return out


def apply_rename(paths, renames: dict[str, str]) -> list[str]:
    """Move each overlay's entry from the old slug to the new one.

    Only ever fills a key the new slug does not already hold: where both exist
    the rebuild did something other than rename, and the newer answer stands.
    Returns one line per file touched, for the build's own output.
    """
    if not renames:
        return []
    report = []
    for path in (paths.classification, paths.resolved, paths.cross_rulings):
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        moved = 0
        for old, new in renames.items():
            if old in data and new not in data:
                rec = data.pop(old)
                if isinstance(rec, dict) and rec.get("slug") == old:
                    rec["slug"] = new
                data[new] = rec
                moved += 1
        if moved:
            Path(path).write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
            report.append(f"{path.name}: {moved} re-keyed")
    # The ledger nests its slug-keyed verdicts one level down, under the
    # investor slug, beside the recall lists.
    if paths.ledger.exists():
        led = json.loads(paths.ledger.read_text())
        moved = 0
        for book in led.values():
            verdicts = (book or {}).get("verdicts")
            if not isinstance(verdicts, dict):
                continue
            for old, new in renames.items():
                if old in verdicts and new not in verdicts:
                    rec = verdicts.pop(old)
                    if isinstance(rec, dict) and rec.get("slug") == old:
                        rec["slug"] = new
                    verdicts[new] = rec
                    moved += 1
        if moved:
            Path(paths.ledger).write_text(json.dumps(led, indent=1, ensure_ascii=False) + "\n")
            report.append(f"{paths.ledger.name}: {moved} re-keyed")
    return report
