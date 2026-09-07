#!/usr/bin/env python3
"""Send back to the judge the two columns a deterministic layer filled without earning it.

COLLECTION.md §8, the Black Forest Labs class: `prepare`'s queue asks only about
EMPTY fields, so a deterministic pre-fill silently keeps the judge away from its
row. Two layers on this run pre-filled columns they are not entitled to label:

1. **Wikidata `hq_country` (44 rows).** The First Round failure, worse here: 8VC's
   book is full of single-token names and the joins are wrong at a rate no layer
   survives — Color→CZ, Oscar→BE, Esper→DE, Honor→CN, Oculus→LV, Baton→RU,
   Alloy→AU, Luna→RS, Orchestra→FR, Rainbow→PL, Create→JP, Flux/Premise→CZ,
   Pango/Radius→SE, all of them US companies. Every Wikidata-sourced value is
   stripped and re-queued; the layer is demoted to corroboration for this
   investor.
2. **`formd_band` `entry_stage` on recent or large rows (§8, §6).** The first
   filed round is a ceiling on entry recency, not the entry: modern seeds often
   never file. Rows entered 2020 or later, or carrying a $1B+ signal, go back
   through the judge with the announcement check.

Rewrites scratch/queue/queue.json and the batch files in place, and strips the
demoted values from resolved.json so nothing publishes them. Idempotent.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic  # noqa: E402

P = Paths("8vc")
QD = P.root / "scratch" / "queue"

resolved = json.loads((P.root / "resolved.json").read_text())
base = json.loads(P.base_json.read_text())
rows = base["companies"] if isinstance(base, dict) and "companies" in base else base
by_slug = {r["slug"]: r for r in rows}

wikidata_country = {s for s, v in resolved.items() if v.get("hq_country_source") == "wikidata"}
band_stage = {s for s, v in resolved.items() if v.get("entry_stage_source") == "formd_band"}


def recent_or_big(slug: str) -> bool:
    v = resolved.get(slug, {})
    r = by_slug.get(slug, {})
    year = str(r.get("first_seen") or "")[:4]
    entry = str(v.get("entry_date") or "")[:4]
    if (year and year >= "2020") or (entry and entry >= "2020"):
        return True
    flags = v.get("flags") or []
    return bool({"unicorn_name_match", "former_unicorn"} & set(flags)) or \
        bool(v.get("valuation_usd")) or (v.get("entry_offering_usd") or 0) >= 40_000_000


band_requeue = {s for s in band_stage if recent_or_big(s)}
print(f"wikidata hq_country to re-judge : {len(wikidata_country)}")
print(f"formd_band entry_stage rows     : {len(band_stage)}")
print(f"  of which recent/large, re-judged: {len(band_requeue)}")

# 1. strip the demoted values so nothing publishes them
stripped = 0
for s in wikidata_country:
    v = resolved[s]
    v.pop("hq_country", None)
    v.pop("hq_country_source", None)
    v.setdefault("flags", [])
    if "wikidata_country_demoted" not in v["flags"]:
        v["flags"].append("wikidata_country_demoted")
    stripped += 1
write_atomic(P.root / "resolved.json", json.dumps(resolved, indent=1, ensure_ascii=False))
print(f"stripped {stripped} wikidata countries from resolved.json")


def fix(item: dict) -> dict:
    s = item["slug"]
    need = list(item.get("need") or [])
    known = dict(item.get("known") or {})
    if s in wikidata_country:
        known.pop("hq_country", None)
        if "hq_country" not in need:
            need.append("hq_country")
    if s in band_requeue:
        if "entry_stage" not in need:
            need.append("entry_stage")
        item["band_stage_to_check"] = known.get("entry_stage")
        known.pop("entry_stage", None)
    order = ["membership", "status", "hq_country", "hq_city", "entry_stage", "valuation_range"]
    item["need"] = sorted(set(need), key=lambda x: order.index(x) if x in order else 99)
    item["known"] = known
    return item


q = json.loads((QD / "queue.json").read_text())
q = [fix(it) for it in q]
write_atomic(QD / "queue.json", json.dumps(q, indent=1, ensure_ascii=False))
for f in sorted(QD.glob("batch-*.json")):
    items = [fix(it) for it in json.loads(f.read_text())]
    write_atomic(f, json.dumps(items, indent=1, ensure_ascii=False))
    print(f"  {f.name}: {len(items)} items")
from collections import Counter
print("\nneed distribution after requeue:",
      Counter(tuple(it["need"]) for it in q).most_common(10))
