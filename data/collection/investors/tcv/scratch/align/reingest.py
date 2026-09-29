"""Per-book gate for the TCV run's sibling alignment (COLLECTION.md 9): record -> export -> review -> verify clean ->
diff only the intended rows -> dry run with 0 removals -> write -> readback 0 -> commit the three company files.
Any failed check stops that book (nothing written) and is reported. Usage: python3 reingest.py book [book ...]"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
def sh(*a, timeout=1200):
    r = subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    return r.returncode, (r.stdout + r.stderr)
FLAGS = [a for a in sys.argv[1:] if a.startswith("--")]
for b in [a for a in sys.argv[1:] if not a.startswith("--")]:
    want = {json.loads(l)["slug"] for l in open(HERE / f"{b}.jsonl")}
    D = f"data/collection/investors/{b}/companies"
    steps = []
    if "--no-record" not in FLAGS:
        rc, o = sh("python3", str(HERE / "align.py"), b); steps.append(o.strip().splitlines()[-1])
        if rc: print(f"STOP {b}: record failed\n{o[-600:]}"); continue
        sh("python3", "scripts/run.py", "export", "--investor", b); sh("python3", "scripts/run.py", "review", "--investor", b)
    else:
        steps.append("recorded earlier")
    rc, o = sh("python3", "scripts/run.py", "verify", "--investor", b)
    if "verify: clean" not in o:
        print(f"STOP {b}: verify not clean\n" + o[o.find("problem(s)")-4:][:1500]); continue
    rc, o = sh("python3", str(HERE / "csvdiff.py"), b)
    changed = {m.group(1) for m in re.finditer(r"^\s+(\S+): \[", o, re.M)}
    head = o.splitlines()[0]
    if changed != want or "added []" not in head or "removed []" not in head:
        print(f"STOP {b}: diff is not the intended rows (want {sorted(want)})\n{o[:1200]}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b, "--dry-run")
    plan = next((l for l in o.splitlines() if l.startswith("Plan:")), o[-300:])
    if not re.search(r"\b0 removed\b", plan):
        print(f"STOP {b}: dry run removes rows\n{o[-1500:]}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b)
    if rc: print(f"STOP {b}: write failed\n{o[-800:]}"); continue
    rc, o = sh("npx", "tsx", "data/collection/investors/20vc/scratch/align/readback.ts", b)
    rb = o.strip().splitlines()[-1]
    if not re.search(r"missing 0, extra 0, differing cells 0", rb):
        print(f"STOP {b}: readback after is not zero: {rb}"); continue
    msg = f"PRO-169: {b} aligned from the TCV run ({', '.join(sorted(want))}), re-ingested\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
    files = [f"{D}/classification.json", f"{D}/base.csv", f"{D}/review.html"]
    if sh("git", "status", "--short", "--", f"{D}/cross-rulings.json")[1].strip():
        files.append(f"{D}/cross-rulings.json")   # a namesake pair the alignment surfaced, ruled in the book's own file
    rc, o = sh("git", "commit", "-q", "-m", msg, "--", *files)
    rc2, h = sh("git", "log", "--oneline", "-1")
    print(f"OK {b}: {steps[0]} | {head} | {plan} | {rb} | {h.strip()}")
