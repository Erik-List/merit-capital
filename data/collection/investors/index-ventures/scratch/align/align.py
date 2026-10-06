#!/usr/bin/env python3
"""Stale sibling rows aligned from the Index Ventures run (PRO-82) in its own ingest (COLLECTION.md s9; Erik 2026-09-29
and 2026-10-01: decide on the evidence and write every book). Adapted from the Kleiner Perkins and Lakestar kits.

Step 1 (`python3 align.py kits`): one classification line per stale sibling row, built from the Index row's own cited
evidence (never the firm's site), written to scratch/align/<book>.jsonl. A row lifted to $1B+ on an uncited stage
takes `cite_pending` (rule 4). The line carries a `note` sentence, which record joins to the book's own note.
Step 2 (`python3 align.py local`, then `python3 align.py ingest` after the Index book is ingested): for every book that is not in flight and has no uncommitted company files: verify
clean before, readback exact before, record the kit ONCE, export, review; then verify every touched book with all kits
recorded (books that share a stale company move together), restore any book that is still not clean, and re-ingest the
clean ones through the gate (dry run with 0 removals, write, readback exact, commit of that book's three files).
Every outcome is one line in results.txt."""
import json, shutil, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]; INV = ROOT / "data/collection/investors"
RB = "data/collection/investors/20vc/scratch/align/readback.ts"
BK = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e489e954-0402-4086-a124-b7bdf9329af1/scratchpad/align-backup")
WHO = "agent-align-pro82"; TODAY = "2026-10-06"
sys.path.insert(0, str(HERE.parent))
FILES = ["classification.json", "base.csv", "review.html"]
def sh(cmd): return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, shell=isinstance(cmd, str))
PAIRS = json.loads((HERE / "pairs.json").read_text()) if (HERE / "pairs.json").exists() else {}
EXTRA = json.loads((HERE / "extra.json").read_text()) if (HERE / "extra.json").exists() else {}      # book -> raw lines appended to its kit
REPAIRS = json.loads((HERE / "repairs.json").read_text()) if (HERE / "repairs.json").exists() else {}  # book -> substrings of pre-existing problems the kit repairs

def kits():
    from merged import view
    V = view()
    for b, pairs in sorted(PAIRS.items()):
        B = INV / b
        C = json.loads((B / "companies/classification.json").read_text()); C = C.get(b, C)
        R = json.loads((B / "companies/resolved.json").read_text()) if (B / "companies/resolved.json").exists() else {}; R = R.get(b, R)
        lines = []
        for sib, mine, kind, why in pairs:
            c = V[mine]; m = {**(R.get(sib) or {}), **(C.get(sib) or {})}
            assert sib in C or sib in R, (b, sib)
            d = {"slug": sib, "who": WHO}
            if kind == "status":
                d.update(status=c["status"], valuation_range=c.get("valuation_range") or "below_1b")
                cite = c.get("status_citation") or why.get("cite")
                if cite: d["status_citation"] = cite
                if m.get("valuation_usd") and d["valuation_range"] == "below_1b" and c["status"] != "public":
                    d["valuation_usd"] = None
                d["note"] = f"Aligned {TODAY} from the Index Ventures run (PRO-82, rule 10): status {c['status']}; {why['says']}" + (f" ({cite})" if cite else "")
            else:
                d.update(status=c["status"], valuation_range=c["valuation_range"], valuation_usd=c["valuation_usd"], valuation_source="web_verified",
                         valuation_range_source="web_verified", valuation_citation=c["valuation_citation"], valuation_asof=c["valuation_asof"])
                d["note"] = f"Aligned {TODAY} from the Index Ventures run (PRO-82, rule 10): ${c['valuation_usd']/1e9:.2f}B as of {c['valuation_asof']}; {why['says']} ({c['valuation_citation']})"
                if d["valuation_range"] in ("1b_plus", "10b_plus", "100b_plus") and m.get("entry_stage_source") not in ("web_verified", "first_party", "formd_structural", "program_terms"):
                    d["flags"] = ["cite_pending"]
            for k, v in (why.get("extra") or {}).items(): d[k] = v
            lines.append(d)
        lines += EXTRA.get(b, [])
        (HERE / f"{b}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
        print(b, len(lines), "line(s)")

def readback(b):
    """-> (exact, last line). A CSV name with stray whitespace reads as one MISSING and one EXTRA row although the
    ingest trims names (YC's ' Metadata', 2026-10-06): exact when the two sets are equal after trimming."""
    lines = sh(f"npx tsx {RB} {b}").stdout.strip().splitlines() or [""]
    last = lines[-1]
    if "missing 0, extra 0, differing cells 0" in last: return True, last
    miss = sorted(l.split("MISSING in DB", 1)[1].strip() for l in lines if l.startswith("MISSING in DB"))
    extra = sorted(l.split("EXTRA in DB", 1)[1].strip() for l in lines if l.startswith("EXTRA in DB"))
    if miss and miss == extra and "differing cells 0" in last: return True, last + " (names equal after trimming)"
    return False, last
def backup(b):
    (BK / b).mkdir(parents=True, exist_ok=True)
    for f in FILES: shutil.copy(INV / b / "companies" / f, BK / b / f)
def restore(b):
    for f in FILES: shutil.copy(BK / b / f, INV / b / "companies" / f)

def run(only=None):
    out = []; live = []; old_live = []
    if only and (HERE / "live.json").exists():
        old_live = [b for b in json.loads((HERE / "live.json").read_text()) if b not in only]
        out = [l for l in (HERE / "results.txt").read_text().splitlines() if l and not l.startswith("local phase done") and not any(l.startswith(f"SKIPPED {b}") for b in only)]
    def log(s): out.append(s); print(s, flush=True); (HERE / "results.txt").write_text("\n".join(out) + "\n")
    for b in sorted(PAIRS):
        if only and b not in only: continue
        B = INV / b; rel = B.relative_to(ROOT); n = len(PAIRS[b])
        if (B / "scratch/in-flight.json").exists(): log(f"SKIPPED {b} ({n} rows): in flight"); continue
        if sh(f"git status --short -- {rel}/companies").stdout.strip(): log(f"SKIPPED {b} ({n} rows): uncommitted company files"); continue
        v = sh(["python3", "scripts/run.py", "verify", "--skip-links", "--investor", b])
        pre = [x.strip() for x in v.stdout.splitlines() if x.startswith("  - ")]
        mine_only = [x for x in pre if "index-ventures:" in x or any(s in x for s in REPAIRS.get(b, []))]
        if v.returncode and len(mine_only) != len(pre):
            log(f"SKIPPED {b} ({n} rows): its own verify is not clean before the lines: {[x[:140] for x in pre if x not in mine_only][:2]}"); continue
        ok, rb = readback(b)
        if not ok: log(f"SKIPPED {b} ({n} rows): readback before is not exact: {rb}"); continue
        backup(b)
        r = sh(["python3", "scripts/run.py", "record", "--investor", b, str(HERE / f"{b}.jsonl")])
        (HERE / f"{b}.log").write_text(r.stdout + r.stderr)
        if r.returncode or "REJECTED" in r.stdout + r.stderr:
            restore(b); log(f"SKIPPED {b} ({n} rows): record rejected a line: {(r.stdout + r.stderr)[-240:]!r}"); continue
        live.append(b)
    for b in live:
        e = sh(["python3", "scripts/run.py", "export", "--investor", b]); sh(["python3", "scripts/run.py", "review", "--investor", b])
        if e.returncode: restore(b); live.remove(b); log(f"SKIPPED {b}: export refused: {(e.stdout + e.stderr)[-200:]!r}")
    live = old_live + live
    changed = True
    while changed:
        changed = False
        for b in list(live):
            v = sh(["python3", "scripts/run.py", "verify", "--skip-links", "--investor", b])
            if v.returncode:
                probs = [x.strip()[:170] for x in v.stdout.splitlines() if x.startswith("  - ")][:3]
                restore(b); live.remove(b); changed = True; log(f"SKIPPED {b}: verify not clean with all kits recorded: {probs}")
    (HERE / "live.json").write_text(json.dumps(live))
    log("local phase done; live: " + ", ".join(live))

def ingest():
    """Phase 2, after the Index book itself is ingested: database writes for the books the local phase left clean."""
    live = json.loads((HERE / "live.json").read_text()); out = (HERE / "results.txt").read_text().splitlines()
    def log(s): out.append(s); print(s, flush=True); (HERE / "results.txt").write_text("\n".join(out) + "\n")
    for b in live:
        rel = (INV / b).relative_to(ROOT); n = len(PAIRS[b])
        v = sh(["python3", "scripts/run.py", "verify", "--skip-links", "--investor", b])
        if v.returncode:
            probs = [x.strip()[:170] for x in v.stdout.splitlines() if x.startswith("  - ")][:3]
            restore(b); log(f"SKIPPED {b} ({n} rows): verify not clean at ingest time, files restored: {probs}"); continue
        d = sh(f"npx tsx scripts/ingest-companies.ts {b} --dry-run"); (HERE / f"{b}.dry").write_text(d.stdout + d.stderr)
        if ", 0 removed" not in d.stdout: restore(b); log(f"SKIPPED {b} ({n} rows): dry run would remove rows or failed: {(d.stdout + d.stderr)[-200:]!r}"); continue
        w = sh(f"npx tsx scripts/ingest-companies.ts {b}")
        with open(HERE / f"{b}.log", "a") as f: f.write(w.stdout + w.stderr)
        if w.returncode: log(f"STOP {b}: INGEST FAILED after local changes (files left changed): {(w.stdout + w.stderr)[-300:]!r}"); break
        ok, rb = readback(b)
        if not ok: log(f"STOP {b}: readback after is not exact: {rb}"); break
        paths = [f"{rel}/companies/{f}" for f in FILES]
        sh(["git", "add", "--"] + paths)
        c = sh(["git", "commit", "-q", "-m", f"PRO-82: {b} aligned to the Index Ventures run's cited evidence ({n} row(s), rule 10), re-ingested\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>", "--"] + paths)
        log(f"ALIGNED {b} ({n} rows): re-ingested, readback exact, commit {sh('git log --oneline -1').stdout[:8]}" + ("" if not c.returncode else f" (COMMIT FAILED: {c.stderr[-120:]!r})"))
    log("done")

if __name__ == "__main__":
    if sys.argv[1] == "kits": kits()
    elif sys.argv[1] == "local": run(set(sys.argv[2:]) or None)
    elif sys.argv[1] == "ingest": ingest()
