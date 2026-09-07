#!/usr/bin/env python3
"""Strip keys the queue did not ask for, then hand the batch to `run.py record`.

COLLECTION.md §8: "Emit only the keys for the needs asked (plus flags, note) —
extra keys clobber filing-grade facts at merge time". Measured on batch 1 of this
run: a `valuation_range: below_1b` emitted for a row whose need list was
[hq_country, entry_stage] would have downgraded Asana's pre-filled 1b_plus, and
two rows were rejected outright for a band with no figure behind it.

The one licensed exception is a DELIBERATE DISPUTE (§8): a key the queue did not
ask for because a deterministic layer already filled it, which the judge is
overruling. Kept when the row flags `stage_disputes_band`, `model_disputes_source`
or `country_conflict`.

Usage: python3 emit.py <batch-NNN.out.jsonl> [--dry-run]
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths  # noqa: E402

DISPUTE = {"stage_disputes_band", "model_disputes_source", "country_conflict",
           "city_country_conflict"}
COLS = ("membership", "status", "hq_country", "entry_stage", "valuation_range")

P = Paths("8vc")
out_path = Path(sys.argv[1])
batch = P.root / "scratch" / "queue" / out_path.name.replace(".out.jsonl", ".json")
needs = {it["slug"]: set(it["need"]) for it in json.loads(batch.read_text())}

lines, stripped = [], []
for raw in out_path.read_text().splitlines():
    raw = raw.strip()
    if not raw:
        continue
    rec = json.loads(raw)
    if "verdict" in rec:                       # membership verdicts pass through
        lines.append(json.dumps(rec, ensure_ascii=False))
        continue
    need = needs.get(rec["slug"], set())
    disputing = DISPUTE & set(rec.get("flags") or [])
    for col in COLS:
        if col in rec and col not in need and not disputing:
            rec.pop(col)
            for extra in (f"{col}_source", f"{col}_confidence", f"{col}_citation"):
                rec.pop(extra, None)
            stripped.append(f"{rec['slug']}:{col}")
    lines.append(json.dumps(rec, ensure_ascii=False))

out_path.write_text("\n".join(lines) + "\n")
print(f"{out_path.name}: {len(lines)} lines"
      + (f"; stripped unasked keys: {', '.join(stripped)}" if stripped else "; nothing stripped"))
if "--dry-run" not in sys.argv:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "run.py"), "record",
                    "--investor", "8vc", str(out_path)], check=False)
