#!/usr/bin/env python3
"""Seat dating at quarter granularity, merged into every queue item.

The gate (golden.json, scratch/gate.md) found the queue's `formd_span` is
YEAR-granular while three of Benchmark's trap rows turn on a boundary INSIDE a
year: Jack Altman's Copilot Labs seat (2026q1) sits one quarter before his
first Benchmark fund filing (2026-06-30), and reads as in-tenure at year
granularity. Benchmark hired four partners out of other firms between 2021 and
2026, so the boundary cases are a class here, not a curiosity.

This writes, per queued row, one line per (partner, quarter) from the Form D
sweep next to that partner's roster window, plus a computed flag:

  in_tenure | pre_tenure | post_tenure | boundary   (boundary = same year as an
  edge of the window, which is exactly where the judge must not trust the year)

It also carries the partner's roster basis, so a cluster is ruled once.
"""
import json, sys
from collections import defaultdict
sys.path.insert(0, "scripts")
from paths import Paths, write_atomic                                  # noqa: E402

P = Paths("benchmark")
sweep = json.loads((P.edgar / "formd-sweep.json").read_text())
roster = {r["name"].upper(): r for r in json.loads((P.wayback / "partner-roster.json").read_text())}

# the sweep keys people by an upper-case display form; map both name variants
alias = {}
for r in roster.values():
    alias[r["name"].upper()] = r
    parts = r["name"].upper().split()
    alias[f"{parts[0]} {parts[-1]}"] = r
EXTRA = {"ANDREW RACHLEFF": "Andy Rachleff", "ROBERT KAGLE": "Bob Kagle",
         "WILLIAM GURLEY": "Bill Gurley", "J. WILLIAM GURLEY": "Bill Gurley",
         "MITCHELL LASKY": "Mitch Lasky", "MATTHEW COHLER": "Matt Cohler",
         "STEVEN SPURLOCK": "Steve Spurlock", "STEVEN M. SPURLOCK": "Steve Spurlock"}
for k, v in EXTRA.items():
    alias[k] = roster[v.upper()]

seats = defaultdict(list)
for acc, v in sweep.items():
    for p in v["persons"]:
        seats[v["issuer"]].append((p["person"], p["quarter"], acc, v.get("total_offering")))

def slugify(n):
    import re
    return re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-")

base = {r["name"]: r["slug"] for r in json.loads(P.base_json.read_text())}
queue = json.loads((P.queue / "queue.json").read_text())
by_slug = {r["slug"]: r for r in queue}

enriched = 0
for issuer, rows in seats.items():
    slug = base.get(issuer) or slugify(issuer)
    item = by_slug.get(slug)
    if item is None:
        continue
    lines = []
    for person, quarter, acc, off in sorted(rows, key=lambda x: x[1]):
        r = alias.get(person.upper())
        y = int(quarter[:4])
        if not r or r["first_seen"] is None:
            verdict, window = "roster_window_unknown", "?"
        else:
            f, l = r["first_seen"], r["last_seen"]
            window = f"{f}-{l}"
            if y in (f, l):
                verdict = "boundary"
            elif y < f:
                verdict = "pre_tenure"
            elif y > l:
                verdict = "post_tenure"
            else:
                verdict = "in_tenure"
        lines.append({"partner": person, "quarter": quarter, "accession": acc,
                      "offering_usd": off, "roster_window": window, "seat": verdict})
    item["seat_dates"] = lines
    item["seat_flags"] = sorted({l["seat"] for l in lines})
    enriched += 1

write_atomic(P.queue / "queue.json", json.dumps(queue, indent=1) + "\n")
# rewrite the batch files from the enriched queue, same chunking
BATCH = 45
batches = [queue[i:i + BATCH] for i in range(0, len(queue), BATCH)]
for i, b in enumerate(batches, 1):
    write_atomic(P.queue / f"batch-{i:03d}.json", json.dumps(b, indent=1) + "\n")
from collections import Counter
print(f"enriched {enriched} of {len(queue)} queued rows with quarter-level seat dating")
print(Counter(f for r in queue for f in r.get("seat_flags", [])))
print(f"rewrote {len(batches)} batch files")
