"""List the queue slugs of a batch whose ledger verdict is already not_member (skip them in the grind)."""
import json, sys
from pathlib import Path
R = Path(__file__).resolve().parents[1]
led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]["verdicts"]
cl = json.loads((R / "companies/classification.json").read_text())
cl = cl.get("index-ventures", cl)
n = int(sys.argv[1])
q = json.loads((R / f"scratch/queue/batch-{n:03d}.json").read_text())
items = q if isinstance(q, list) else q.get("items") or q.get("rows")
out, done = [], []
for i in items:
    s = i["slug"]
    if (led.get(s) or {}).get("verdict") == "not_member": out.append(s)
    elif s in cl: done.append(s)
print("not_member:", " ".join(out)); print("already classified:", " ".join(done))
