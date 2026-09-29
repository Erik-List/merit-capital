#!/usr/bin/env python3
"""Repair notes doubled by record's append (PRO-75): `record` stores "old | new" unless the new note is already inside
the old, so a line that passed "old + sentence" stored "old | old sentence". Drop every " | " segment that a later
segment starts with (or equals); keep the order otherwise. Dry run by default; --write applies it under the record
lock."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
from shared_throttle import exclusive  # noqa: E402

P = Path(__file__).resolve().parent.parent / "companies" / "classification.json"


# Rows whose last line was written as a full replacement of the note (fixes-2): keep only that last segment.
REPLACED = {"apteligent", "mylaurel", "beamable", "nchroma-bio"}


def _lcp(a, b):
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def dedup(note):
    segs = [x.strip() for x in note.split(" | ")]
    keep = []
    for i, s in enumerate(segs):
        later = segs[i + 1:]
        if any(t.startswith(s) for t in later):
            continue
        # a later segment that repeats this one with its last sentence edited (d4 dropped "Graduation left for the
        # graduation pass." before appending its S2A text): a shared prefix of 80% or more
        if len(s) > 80 and any(_lcp(s, t) >= 0.8 * len(s) for t in later):
            continue
        if s in keep:
            continue
        keep.append(s)
    return " | ".join(keep)


# Sentences a later judge found unsupported by the cited page (d5 on DataFox): removed from the note.
UNSUPPORTED = {"datafox": " DataFox was last valued at $33M in January 2017 and had raised just under $19M when Oracle "
                          "bought it in October 2018 (TechCrunch)."}

write = "--write" in sys.argv
with exclusive("record-gv"):
    d = json.loads(P.read_text())
    changed = []
    for slug, rec in d.items():
        n = rec.get("note")
        if not n:
            continue
        m = n.split(" | ")[-1].strip() if slug in REPLACED else (dedup(n) if " | " in n else n)
        if slug in UNSUPPORTED:
            m = m.replace(UNSUPPORTED[slug], "")
        if m != n:
            changed.append((slug, len(n), len(m)))
            if write:
                rec["note"] = m
    if write and changed:
        write_atomic(P, json.dumps(d, indent=1, sort_keys=True))
print(("repaired" if write else "would repair"), len(changed), "notes")
for c in changed:
    print("  ", c)
