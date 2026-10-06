#!/usr/bin/env python3
"""Align the stale sibling rows found by the Bessemer run (PRO-80) and re-ingest each book through the
COLLECTION.md s9 gate (the Kleiner Perkins second-pass design: record every kit first, so books that share a stale
company move together, then verify, then gate book by book).

A book is SKIPPED, with nothing written to the database and its files restored, when: it is in flight; its company
files carry uncommitted changes; its own verify is not clean before the lines; the readback before is not exact;
record rejects a line; its verify is not clean with every kit recorded; the dry run would remove a row. A row lifted
to $1B or more on an uncited entry stage gains `cite_pending` (verify rule 4). Every outcome is one line in
results.txt. Usage: python3 run-align.py"""
import json, shutil, subprocess
from pathlib import Path

ROOT = Path("/Users/erik/Developer/merit-capital")
HERE = Path(__file__).resolve().parent
INV = ROOT / "data/collection/investors"
RB = "data/collection/investors/20vc/scratch/align/readback.ts"
BK = HERE / "backup"
BK.mkdir(exist_ok=True)
FILES = ["classification.json", "base.csv", "review.html", "cross-rulings.json"]
EXACT = "missing 0, extra 0, differing cells 0"
out = []


def sh(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=isinstance(cmd, str))


def say(line):
    out.append(line)
    print(line, flush=True)
    (HERE / "results.txt").write_text("\n".join(out) + "\n")


def backup(b):
    for f in FILES:
        p = INV / b / "companies" / f
        if p.exists():
            shutil.copy(p, BK / f"{b}-{f}")


def restore(b):
    for f in FILES:
        s, p = BK / f"{b}-{f}", INV / b / "companies" / f
        if s.exists():
            shutil.copy(s, p)


books = sorted(k.stem for k in HERE.glob("*.jsonl") if not k.stem.endswith(".pass"))
live = []
for b in books:
    B = INV / b
    n = sum(1 for l in (HERE / f"{b}.jsonl").read_text().splitlines() if l.strip())
    if (B / "scratch/in-flight.json").exists():
        say(f"SKIPPED {b} ({n} rows): in flight"); continue
    if sh(f"git status --short -- {B.relative_to(ROOT)}/companies/classification.json {B.relative_to(ROOT)}/companies/base.csv {B.relative_to(ROOT)}/companies/review.html").stdout.strip():
        say(f"SKIPPED {b} ({n} rows): uncommitted company files"); continue
    v = sh(["python3", "scripts/run.py", "verify", "--investor", b])
    if v.returncode:
        probs = [x.strip()[:170] for x in v.stdout.splitlines() if x.startswith("  - ")][:3]
        say(f"SKIPPED {b} ({n} rows): its own verify is not clean before the lines: {probs}"); continue
    r = sh(f"npx tsx {RB} {b}")
    last = (r.stdout.strip().splitlines() or [""])[-1]
    if EXACT not in last:
        say(f"SKIPPED {b} ({n} rows): readback before is not exact: {last[:200]}"); continue
    backup(b)
    C = json.loads((B / "companies/classification.json").read_text()); C = C.get(b, C) if isinstance(C.get(b), dict) and "slug" not in C.get(b, {}) else C
    R = json.loads((B / "companies/resolved.json").read_text()); R = R.get(b, R) if isinstance(R.get(b), dict) and "slug" not in R.get(b, {}) else R
    lines = []
    for l in (HERE / f"{b}.jsonl").read_text().splitlines():
        if not l.strip():
            continue
        d = json.loads(l)
        m = {**(R.get(d["slug"]) or {}), **(C.get(d["slug"]) or {})}
        if d.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") and m.get("valuation_range") not in ("1b_plus", "10b_plus", "100b_plus") \
                and m.get("entry_stage_source") not in ("web_verified", "first_party", "formd_structural", "program_terms"):
            d["flags"] = sorted(set(d.get("flags", [])) | {"cite_pending"})
        lines.append(json.dumps(d, ensure_ascii=False))
    kit = HERE / f"{b}.pass.jsonl"
    kit.write_text("\n".join(lines) + "\n")
    r = sh(["python3", "scripts/run.py", "record", "--investor", b, str(kit)])
    (HERE / f"{b}.log").write_text(r.stdout + r.stderr)
    if "REJECTED" in r.stdout + r.stderr or r.returncode:
        restore(b)
        say(f"SKIPPED {b} ({n} rows): record rejected a line: {(r.stdout + r.stderr)[-300:]!r}"); continue
    live.append((b, n))

for b, _ in live:
    sh(["python3", "scripts/run.py", "export", "--investor", b])
    sh(["python3", "scripts/run.py", "review", "--investor", b])

changed = True
while changed:
    changed = False
    for b, n in list(live):
        v = sh(["python3", "scripts/run.py", "verify", "--investor", b])
        if v.returncode:
            probs = [x.strip()[:200] for x in v.stdout.splitlines() if x.startswith("  - ")][:3]
            restore(b); live.remove((b, n)); changed = True
            say(f"SKIPPED {b} ({n} rows): verify not clean with all kits recorded: {probs}")

for b, n in live:
    B = (INV / b).relative_to(ROOT)
    d = sh(f"npx tsx scripts/ingest-companies.ts {b} --dry-run")
    (HERE / f"{b}.dry").write_text(d.stdout + d.stderr)
    if ", 0 removed" not in d.stdout:
        restore(b)
        plan = [x for x in d.stdout.splitlines() if x.startswith("Plan")]
        say(f"SKIPPED {b} ({n} rows): dry run would remove rows: {plan}"); continue
    w = sh(f"npx tsx scripts/ingest-companies.ts {b}")
    if w.returncode:
        say(f"STOP {b}: INGEST FAILED after local changes (files left changed): {(w.stdout + w.stderr)[-300:]!r}"); break
    r = sh(f"npx tsx {RB} {b}")
    last = (r.stdout.strip().splitlines() or [""])[-1]
    if EXACT not in last:
        say(f"STOP {b}: readback after is not exact: {last[:200]}"); break
    files = [f"{B}/companies/classification.json", f"{B}/companies/base.csv", f"{B}/companies/review.html"]
    c = sh(["git", "commit", "-q", "-m",
            f"PRO-80: {b} aligned to the Bessemer run's cited evidence ({n} row(s), rule 10), re-ingested\n\n"
            "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>", "--"] + files)
    h = sh("git log --oneline -1").stdout[:8]
    say(f"ALIGNED {b} ({n} rows): re-ingested, readback exact, commit {h}" + ("" if not c.returncode else f" (commit said: {(c.stdout + c.stderr)[-120:]!r})"))
say("done")
