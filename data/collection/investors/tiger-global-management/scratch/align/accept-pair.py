"""Record an accepted rule-10 pair in a sibling book's OWN companies/cross-rulings.json (COLLECTION.md 9): the pair
the alignment surfaces when a book aligned from Tiger's cited evidence meets a book the gate skipped, whose row is
still stale on the same evidence. Usage: python3 accept-pair.py book:slug other:slug "note" """
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic
a, b, note = sys.argv[1], sys.argv[2], sys.argv[3]
p = ROOT / f"data/collection/investors/{a.split(':')[0]}/companies/cross-rulings.json"
C = json.loads(p.read_text())
C.setdefault("accepted", [])
if frozenset([a, b]) in {frozenset(x["rows"]) for x in C["accepted"]}:
    print("already there"); sys.exit()
C["accepted"].append({"rows": [a, b], "note": note})
write_atomic(p, json.dumps(C, indent=1, ensure_ascii=False) + "\n")
print(f"accepted {a} ~ {b} in {p.relative_to(ROOT)}")
