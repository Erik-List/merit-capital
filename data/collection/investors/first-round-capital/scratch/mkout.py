#!/usr/bin/env python3
"""Turn a compact per-row judgment table into the queue's .out.jsonl.

One judged row per line, pipe-separated, so a 45-row batch is 45 short lines
instead of 45 JSON blobs:

  slug | status | range | stage | country | city | focus | conf | flags | note

Empty field = do not emit that key (§8: emit only the keys the needs asked,
plus flags and note, plus deliberate disputes). `-` in city = explicit null
(emits hq_city: null with its source). conf is one of high/medium/low and
applies to stage, country and valuation. flags are comma-separated.
Usage: python3 mkout.py <batch-number> < table.txt
"""
import json, sys
from pathlib import Path

INV = Path(__file__).resolve().parents[1]
n = int(sys.argv[1])
batch = json.loads((INV / f"scratch/queue/batch-{n:03d}.json").read_text())
need = {i["slug"]: set(i["need"]) for i in batch}
out = INV / f"scratch/queue/batch-{n:03d}.out.jsonl"

FOCUS = {"ai": "AI & Applied AI", "saas": "SaaS",
         "fin": "Fintech & Payments", "health": "Healthcare & Bio",
         "consumer": "Consumer & Marketplaces", "data": "Data Infrastructure",
         "dev": "DevTools & APIs", "sec": "Security", "crypto": "Crypto & Web3",
         "media": "Media, Gaming & Advertising", "industrial": "Industrial & Robotics",
         "climate": "Climate & Energy", "": None}

lines = []
for raw in sys.stdin.read().splitlines():
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    parts = [p.strip() for p in raw.split("|")]
    parts += [""] * (10 - len(parts))
    slug, status, vrange, stage, country, city, focus, conf, flags, note = parts[:10]
    if slug not in need:
        sys.exit(f"{slug} is not in batch {n}")
    rec = {"slug": slug}
    conf = conf or "medium"
    if status:
        rec["status"] = status
    if vrange:
        rec["valuation_range"] = vrange
        rec["valuation_confidence"] = conf
    if stage:
        rec["entry_stage"] = stage
        rec["entry_stage_source"] = "model"
        rec["entry_stage_confidence"] = conf
    if country:
        rec["hq_country"] = country
        rec["hq_country_source"] = "model_knowledge"
        rec["hq_country_confidence"] = conf
    if city:
        rec["hq_city"] = None if city == "-" else city
        rec["hq_city_source"] = "model_knowledge"
    if focus:
        rec["focus"] = FOCUS[focus]
        rec["focus_source"] = "model"
    if flags:
        rec["flags"] = [f for f in flags.split(",") if f]
    if note:
        rec["note"] = note
    lines.append(json.dumps(rec))

out.write_text("\n".join(lines) + "\n")
print(f"wrote {out.name} — {len(lines)} rows (batch has {len(batch)})")
missing = set(need) - {json.loads(l)['slug'] for l in lines}
if missing:
    print("MISSING:", sorted(missing))
