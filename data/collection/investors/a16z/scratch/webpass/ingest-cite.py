#!/usr/bin/env python3
"""Transform a citation-agent JSONL into classification record rows.
found entry rows -> web_verified stage + citation; found=false -> cite_pending.
found cap rows -> web_verified cap + citation + derived range.
Emits one row per (slug, kind); if a slug appears for both kinds the two
dicts are merged into one record row (record merges per slug last-wins)."""
import json, sys

agent_file, out_file = sys.argv[1], sys.argv[2]
per_slug = {}
for line in open(agent_file):
    line = line.strip()
    if not line: continue
    r = json.loads(line)
    slug = r["slug"]
    row = per_slug.setdefault(slug, {"slug": slug})
    if r["task"] == "entry_citation":
        if r.get("found"):
            row.update({"entry_stage": r["entry_stage"], "entry_stage_source": "web_verified",
                        "entry_stage_citation": r["citation"], "entry_stage_confidence": "high"})
        else:
            row.setdefault("flags", []).append("cite_pending")
    else:
        if r.get("found"):
            v = int(r["valuation_usd"])
            rng = "100b_plus" if v >= 100e9 else "10b_plus" if v >= 10e9 else "1b_plus" if v >= 1e9 else "below_1b"
            row.update({"valuation_usd": v, "valuation_source": "web_verified",
                        "valuation_asof": r.get("valuation_asof"), "valuation_citation": r["citation"],
                        "valuation_range": rng, "valuation_confidence": "high"})
        else:
            row.setdefault("flags", []).append("cite_pending")
    if r.get("note_add"):
        prev = row.get("note", "")
        row["note"] = (prev + " | " if prev else "") + r["note_add"][:230]

with open(out_file, "w") as f:
    for row in per_slug.values():
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"{out_file}: {len(per_slug)} record rows")
