#!/usr/bin/env python3
"""Transform a webpass agent JSONL into classification record rows.

Rules:
- valuation_range derived from valuation_usd (1e9/1e10/1e11 breaks).
- web_verified source + citation + asof on every pinned figure.
- acquired/defunct corrections follow the current-value convention:
  valuation_range below_1b, no standalone figure, exit noted.
- every pinned row clears needs_web_value; the same pin is mirrored onto
  flagged merge-twins so their flags clear too.
- found=false rows keep their flag (stay as documented debt).
"""
import json, sys, os

A16Z = "data/collection/investors/a16z"
agent_file = sys.argv[1]
out_file = sys.argv[2]

c = json.load(open(f"{A16Z}/classification.json"))
merges = json.load(open(f"{A16Z}/identity-merges.json"))["a16z"]["merges"]
group = {}
for m in merges:
    members = [m["canonical"]] + m["duplicates"]
    for s in members:
        group[s] = members

def rng(v):
    if v is None: return None
    if v >= 100e9: return "100b_plus"
    if v >= 10e9: return "10b_plus"
    if v >= 1e9: return "1b_plus"
    return "below_1b"

rows, skipped = [], []
for line in open(agent_file):
    line = line.strip()
    if not line: continue
    r = json.loads(line)
    slug = r["slug"]
    if not r.get("found"):
        skipped.append((slug, r.get("note_add", "")))
        continue
    base = {"slug": slug, "clear_flags": ["needs_web_value"]}
    corr = r.get("status_correction")
    v = r.get("valuation_usd")
    if corr in ("acquired", "defunct"):
        base["status"] = corr
        base["status_source"] = "web_verified"
        base["valuation_range"] = "below_1b"
        base["valuation_confidence"] = "high"
    else:
        if corr in ("public", "private"):
            base["status"] = corr
            base["status_source"] = "web_verified"
        if v is not None:
            base["valuation_usd"] = int(v)
            base["valuation_source"] = "web_verified"
            base["valuation_asof"] = r.get("valuation_asof")
            base["valuation_citation"] = r.get("valuation_citation")
            base["valuation_range"] = rng(v)
            base["valuation_confidence"] = "high"
        else:
            base["valuation_range"] = "below_1b"
            base["valuation_confidence"] = "medium"
    if r.get("entry_citation"):
        base["entry_stage_source"] = "web_verified"
        base["entry_stage_citation"] = r["entry_citation"]
        prev_stage = (c.get(slug) or {}).get("entry_stage")
        if prev_stage:
            base["entry_stage"] = prev_stage
    if r.get("note_add"):
        base["note"] = r["note_add"][:300]
    rows.append(base)
    # mirror onto flagged merge twins
    for twin in group.get(slug, []):
        if twin == slug: continue
        trow = c.get(twin) or {}
        if "needs_web_value" in (trow.get("flags") or []):
            mirror = dict(base)
            mirror["slug"] = twin
            mirror["note"] = f"web pass pinned via the {slug} twin"
            rows.append(mirror)

with open(out_file, "w") as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
print(f"{agent_file}: {len(rows)} record rows ({len(skipped)} not-found kept flagged)")
for s, why in skipped:
    print("  not found:", s, "-", why[:90])
