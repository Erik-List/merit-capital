#!/usr/bin/env python3
"""Score the membership trap set (COLLECTION.md §4).

Gate: ZERO false members at high confidence before any verdict writes.

A trap is scored against the verdict that will actually publish -- the ledger
seed where one exists, overridden by any verdict the grind has written into a
batch .out.jsonl. A trap whose issuer never reached the base at all is scored
`dropped_pre_base`: the build's own fund-vehicle and non-operating-company
filters removed it, which is the right outcome by a different mechanism, and
saying so is more honest than counting it as a judge success.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "scratch" / "queue"


SUFFIX = re.compile(
    r"\b(incorporated|inc|llc|l\.?l\.?c|corp|corporation|ltd|limited|"
    r"holdings|holding|lp|l\.?p|plc|co|company|de)\b", re.I)


def norm(s: str) -> str:
    """Loose name key. The trap issuers are REGISTERED names ('SHOPIFY INC.',
    'Dedrone Holdings, Inc.') while the base carries trading names, so the
    corporate suffix has to come off or a real member reads as absent."""
    s = (s or "").split("/")[0]
    s = SUFFIX.sub(" ", s)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def main() -> None:
    golden = json.loads((ROOT / "golden.json").read_text())
    traps = golden["membership_trap_set"]["traps"]

    base = json.loads((ROOT / "base.json").read_text())
    by_norm = {norm(r["name"]): r["slug"] for r in base}
    by_norm.update({norm(r["slug"]): r["slug"] for r in base})

    ledger = json.loads((ROOT / "base-verification.json").read_text())
    verdicts = {k: v for k, v in ledger["felicis"]["verdicts"].items()}

    # Anything the grind has already written wins over the seed.
    for f in sorted(QUEUE.glob("batch-*.out.jsonl")):
        for line in f.read_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if "verdict" in r:
                verdicts[r["slug"]] = r

    false_members, ok, dropped, misses = [], [], [], []
    for t in traps:
        slug = by_norm.get(norm(t["issuer"]))
        want = t["expect"]
        if not slug:
            dropped.append(t)
            continue
        got = verdicts.get(slug, {})
        v = got.get("verdict")
        conf = got.get("confidence")
        if v == want:
            ok.append((t["issuer"], want, got.get("who", "?")))
        elif want == "not_member" and v == "member":
            false_members.append((t["issuer"], slug, conf, got.get("who")))
        else:
            misses.append((t["issuer"], want, v, conf))

    print(f"trap set: {len(traps)} traps")
    print(f"  correct                       : {len(ok)}")
    print(f"  never reached the base         : {len(dropped)}"
          "   (build filters, not judge work)")
    print(f"  FALSE MEMBERS at high confidence: "
          f"{sum(1 for _, _, c, _ in false_members if c == 'high')}")
    if false_members:
        for iss, slug, conf, who in false_members:
            print(f"      !! {iss} -> {slug} member ({conf}, {who})")
    if misses:
        print(f"  other misses ({len(misses)}):")
        for iss, want, got, conf in misses:
            print(f"      {iss}: expected {want}, got {got} ({conf})")
    if dropped:
        print("  dropped before the base:")
        for t in dropped:
            print(f"      {t['issuer']}  [{t['class']}]")

    gate = sum(1 for _, _, c, _ in false_members if c == "high") == 0
    print(f"\nGATE: {'PASS' if gate else 'FAIL'} "
          f"(zero false members at high confidence)")
    sys.exit(0 if gate else 1)


if __name__ == "__main__":
    main()
