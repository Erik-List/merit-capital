#!/usr/bin/env python3
"""Second alignment pass (PRO-99): the books the first pass skipped because their verify failed AFTER the lines.
Records every remaining kit first (so books that share a stale company move together), adds `cite_pending` where a row
is lifted to $1B+ on an uncited stage (rule 4), rules the namesake pair the alignment surfaced, then verifies; a book
whose verify is still not clean is restored from its backup and the loop repeats until the set is stable. Only books
that end clean are re-ingested through the s9 gate (dry run with 0 removals, write, readback exact, commit)."""
import json, subprocess, shutil, sys
from pathlib import Path
ROOT = Path("/Users/erik/Developer/merit-capital"); HERE = Path(__file__).resolve().parent
INV = ROOT / "data/collection/investors"; RB = "data/collection/investors/20vc/scratch/align/readback.ts"
def sh(cmd): return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=isinstance(cmd, str))
res = (HERE / "results.txt").read_text().splitlines()
books = [l.split()[1] for l in res if l.startswith("SKIPPED") and "after the lines" in l]
out = []; FILES = ["classification.json", "base.csv", "review.html", "cross-rulings.json"]
def backup(b):
    for f in FILES:
        p = INV / b / "companies" / f
        if p.exists(): shutil.copy(p, f"/tmp/kp2-{b}-{f}")
def restore(b):
    for f in FILES:
        s = Path(f"/tmp/kp2-{b}-{f}"); p = INV / b / "companies" / f
        if s.exists(): shutil.copy(s, p)
        elif f == "cross-rulings.json" and p.exists() and not sh(f"git ls-files --error-unmatch {p.relative_to(ROOT)}").returncode == 0: p.unlink()
live = []
for b in books:
    B = INV / b
    if (B / "scratch/in-flight.json").exists() or sh(f"git status --short -- {B.relative_to(ROOT)}/companies").stdout.strip():
        out.append(f"SKIPPED {b}: in flight or uncommitted"); continue
    backup(b)
    C = json.loads((B / "companies/classification.json").read_text()); C = C.get(b, C)
    R = json.loads((B / "companies/resolved.json").read_text()); R = R.get(b, R)
    lines = []
    for l in (HERE / f"{b}.jsonl").read_text().splitlines():
        d = json.loads(l); m = {**R.get(d["slug"], {}), **C.get(d["slug"], {})}
        if d.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus") and m.get("entry_stage_source") not in ("web_verified", "first_party", "formd_structural", "program_terms"):
            d["flags"] = sorted(set(d.get("flags", [])) | {"cite_pending"})
        lines.append(json.dumps(d, ensure_ascii=False))
    kit2 = HERE / f"{b}.pass2.jsonl"; kit2.write_text("\n".join(lines) + "\n")
    r = sh(["python3", "scripts/run.py", "record", "--investor", b, str(kit2)])
    if "REJECTED" in r.stdout + r.stderr or r.returncode:
        restore(b); out.append(f"SKIPPED {b}: record rejected a line: {(r.stdout + r.stderr)[-200:]!r}"); continue
    if b == "iconiq-growth":
        p = B / "companies/cross-rulings.json"
        cr = json.loads(p.read_text()) if p.exists() else {"_doc": "iconiq-growth's rule-10 rulings.", "distinct": [], "accepted": [], "same": []}
        cr.setdefault("distinct", []).append({"rows": ["iconiq-growth:assured", "first-round-capital:assured"], "note": "ICONIQ's Assured is assured.com, the insurance claims company (its own grid links assured.com); First Round's Assured is withassured.com, a different company (ruled at the Kleiner Perkins alignment, PRO-99, 2026-09-30)."})
        p.write_text(json.dumps(cr, indent=1, ensure_ascii=False) + "\n")
    live.append(b)
for b in live:
    sh(["python3", "scripts/run.py", "export", "--investor", b]); sh(["python3", "scripts/run.py", "review", "--investor", b])
changed = True
while changed:
    changed = False
    for b in list(live):
        v = sh(["python3", "scripts/run.py", "verify", "--investor", b])
        if v.returncode:
            probs = [x.strip()[:150] for x in v.stdout.splitlines() if x.startswith("  - ")][:2]
            restore(b); live.remove(b); changed = True; out.append(f"SKIPPED {b}: verify not clean with all kits recorded: {probs}")
for b in live:
    B = (INV / b).relative_to(ROOT)
    d = sh(f"npx tsx scripts/ingest-companies.ts {b} --dry-run").stdout
    if ", 0 removed" not in d:
        restore(b); out.append(f"SKIPPED {b}: dry run would remove rows"); continue
    w = sh(f"npx tsx scripts/ingest-companies.ts {b}")
    rb = sh(f"npx tsx {RB} {b}").stdout.strip().splitlines()[-1]
    if "missing 0, extra 0, differing cells 0" not in rb:
        out.append(f"STOP {b}: readback after not exact: {rb}"); break
    n = sum(1 for _ in (HERE / f"{b}.pass2.jsonl").read_text().splitlines())
    paths = [f"{B}/companies/{f}" for f in FILES if (ROOT / B / "companies" / f).exists()]
    sh(["git", "add", "--"] + paths)
    sh(["git", "commit", "-q", "-m", f"PRO-99: {b} aligned to the Kleiner Perkins run's cited evidence ({n} row(s), rule 10), re-ingested\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>", "--"] + paths)
    out.append(f"ALIGNED {b} ({n} rows): re-ingested, readback exact, commit {sh('git log --oneline -1').stdout[:8]}")
(HERE / "results2.txt").write_text("\n".join(out) + "\ndone\n")
