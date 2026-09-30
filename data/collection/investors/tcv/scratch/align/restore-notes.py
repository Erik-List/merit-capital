"""Restore seven sibling notes that the alignment's repeated `record` calls blanked (run.py record: a note already
contained in the stored one is written over it, the join then skipped; found by the Northzone session, 2026-09-29).
Each note becomes the note before the TCV alignment commit + " | " + the alignment sentence, written under the book's
record lock; then export, review, verify clean, a diff of only the note cells, dry run with 0 removals, write,
readback 0, and the book's three company files committed. Usage: python3 restore-notes.py"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "scripts"))
from shared_throttle import exclusive
from paths import write_atomic
LOST = {"8vc": (["aviatrix"], "6e08cd6f"), "a16z": (["revolut"], "ad803e75"), "creandum": (["klarna"], "98d1a48d"),
        "benchmark": (["zillow-com"], "117e92ae"), "thrive-capital": (["nourish"], "32b5525f"),
        "menlo-ventures": (["grow-therapy", "nourish"], "e8133c37")}
def sh(*a):
    r = subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True, timeout=1800)
    return r.returncode, r.stdout + r.stderr
for b, (slugs, commit) in [(k, v) for k, v in LOST.items() if len(sys.argv) < 2 or k in sys.argv[1:]]:
    D = f"data/collection/investors/{b}/companies"; P = ROOT / D / "classification.json"
    before = json.loads(sh("git", "show", f"{commit}^:{D}/classification.json")[1])
    with exclusive(f"record-{b}"):
        cls = json.loads(P.read_text())
        for s in slugs:
            orig, now = before[s]["note"], cls[s]["note"]
            if now.startswith(orig + " | Aligned 2026-09-29 from the TCV run"):
                continue   # already restored by an earlier pass that stopped at the gate
            assert now.startswith("Aligned 2026-09-29 from the TCV run") and not now.startswith(orig), (b, s)
            cls[s]["note"] = f"{orig} | {now}"
        write_atomic(P, json.dumps(cls, indent=1, sort_keys=True))   # exactly as run.py record writes it
    sh("python3", "scripts/run.py", "export", "--investor", b); sh("python3", "scripts/run.py", "review", "--investor", b)
    rc, o = sh("python3", "scripts/run.py", "verify", "--investor", b)
    if "verify: clean" not in o: print(f"STOP {b}: verify\n{o[-900:]}"); continue
    rc, o = sh("python3", "data/collection/investors/tcv/scratch/align/csvdiff.py", b)
    cols = dict(re.findall(r"^\s+(\S+): (\[.*\])", o, re.M))
    if set(cols) != set(slugs) or any(c != "['note']" for c in cols.values()) or "added []" not in o or "removed []" not in o:
        print(f"STOP {b}: diff is more than the notes\n{o[:900]}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b, "--dry-run")
    plan = next((l for l in o.splitlines() if l.startswith("Plan:")), o[-300:])
    if not re.search(r"\b0 removed\b", plan): print(f"STOP {b}: dry run removes rows\n{o[-900:]}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b)
    if rc: print(f"STOP {b}: write failed\n{o[-600:]}"); continue
    rb = sh("npx", "tsx", "data/collection/investors/20vc/scratch/align/readback.ts", b)[1].strip().splitlines()[-1]
    if "missing 0, extra 0, differing cells 0" not in rb: print(f"STOP {b}: readback {rb}"); continue
    msg = (f"PRO-169: {b} notes restored ({', '.join(slugs)}): the alignment's repeated record blanked them, re-ingested\n\n"
           "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")
    sh("git", "commit", "-q", "-m", msg, "--", f"{D}/classification.json", f"{D}/base.csv", f"{D}/review.html")
    print(f"OK {b}: {plan} | {rb} | {sh('git', 'log', '--oneline', '-1')[1].strip()}")
