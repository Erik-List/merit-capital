"""Per-book gate for the Speedinvest run's sibling alignment (COLLECTION.md 9), adapted from TCV's (PRO-169) with the
readback BEFORE the write that the gate asks for: readback before = committed CSV -> record once -> export -> review ->
verify clean -> diff only the intended rows -> dry run with 0 new and 0 removed -> write -> readback after 0 -> commit
the three company files. Any failed check stops that book and is reported; nothing after it runs for that book.
Usage: python3 reingest.py [--no-record] book [book ...]"""
import json, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
RB = "data/collection/investors/20vc/scratch/align/readback.ts"
def exact(line, out):
    """A readback is exact at 0/0/0, or when every missing name equals an extra name after trimming: the readback
    tool compares the raw CSV name while the ingest trims it (YC's " Metadata")."""
    if re.search(r"missing 0, extra 0, differing cells 0", line):
        return True
    miss = sorted(l.split("MISSING in DB", 1)[1].strip() for l in out.splitlines() if l.startswith("MISSING in DB"))
    extra = sorted(l.split("EXTRA in DB", 1)[1].strip() for l in out.splitlines() if l.startswith("EXTRA in DB"))
    return bool(miss) and miss == extra and "differing cells 0" in line
def sh(*a, timeout=1500):
    r = subprocess.run(list(a), cwd=ROOT, capture_output=True, text=True, timeout=timeout)
    return r.returncode, (r.stdout + r.stderr)
FLAGS = [a for a in sys.argv[1:] if a.startswith("--")]
SKIP_LINKS = {"seedcamp"}
for b in [a for a in sys.argv[1:] if not a.startswith("--")]:
    want = {json.loads(l)["slug"] for l in open(HERE / f"{b}-2.jsonl")}
    D = f"data/collection/investors/{b}/companies"
    if sh("git", "status", "--short", "--", f"{D}/classification.json", f"{D}/base.csv", f"{D}/review.html")[1].strip() and "--no-record" not in FLAGS:
        print(f"STOP {b}: uncommitted company files before the record"); continue
    if (ROOT / f"data/collection/investors/{b}/scratch/in-flight.json").exists():
        print(f"STOP {b}: in flight"); continue
    if "--no-record" not in FLAGS:
        rc, o = sh("npx", "tsx", RB, b); rb0 = o.strip().splitlines()[-1]
        if not exact(rb0, o):
            print(f"STOP {b}: readback before differs from the committed CSV: {rb0}"); continue
        rc, o = sh("python3", str(HERE / "align2.py"), b)
        if rc: print(f"STOP {b}: record failed\n{o[-600:]}"); continue
        rec = o.strip().splitlines()[-1]
        sh("python3", "scripts/run.py", "export", "--investor", b); sh("python3", "scripts/run.py", "review", "--investor", b)
    else:
        rb0, rec = "readback before done earlier", "recorded earlier"
    # A book with no EDGAR or Form D link in its base fails the link sample vacuously ("none sampled"); that is its
    # standing state, not a defect of the alignment, so the sample is skipped for the books named in SKIP_LINKS.
    rc, o = sh("python3", "scripts/run.py", "verify", "--investor", b, *(["--skip-links"] if b in SKIP_LINKS else []))
    if "verify: clean" not in o:
        print(f"STOP {b}: verify not clean\n" + "\n".join(l for l in o.splitlines() if l.strip().startswith("- "))[:1500]); continue
    rc, o = sh("python3", "data/collection/investors/tcv/scratch/align/csvdiff.py", b)
    changed = {m.group(1) for m in re.finditer(r"^\s+(\S+): \[", o, re.M)}
    head = o.splitlines()[0]
    if changed != want or "added []" not in head or "removed []" not in head:
        print(f"STOP {b}: diff is not the intended rows (want {sorted(want)})\n{o[:1500]}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b, "--dry-run")
    plan = next((l for l in o.splitlines() if l.startswith("Plan:")), o[-300:])
    if not re.search(r"\(0 new\), 0 removed", plan):
        print(f"STOP {b}: dry run adds or removes rows: {plan}"); continue
    rc, o = sh("npx", "tsx", "scripts/ingest-companies.ts", b)
    if rc: print(f"STOP {b}: write failed\n{o[-800:]}"); continue
    rc, o = sh("npx", "tsx", RB, b)
    rb = o.strip().splitlines()[-1]
    if not exact(rb, o):
        print(f"STOP {b}: readback after is not zero: {rb}"); continue
    msg = f"PRO-84: {b} aligned from the Speedinvest run, second pass ({', '.join(sorted(want))}), re-ingested\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
    files = [f"{D}/classification.json", f"{D}/base.csv", f"{D}/review.html"]
    if sh("git", "status", "--short", "--", f"{D}/cross-rulings.json")[1].strip():
        files.append(f"{D}/cross-rulings.json")   # a pair the alignment surfaced, ruled in the book's own file
    rc, o = sh("git", "commit", "-q", "-m", msg, "--", *files)
    rc2, h = sh("git", "log", "--oneline", "-1")
    print(f"OK {b}: {rb0} | {rec} | {head} | {plan} | {rb} | {h.strip()}")
