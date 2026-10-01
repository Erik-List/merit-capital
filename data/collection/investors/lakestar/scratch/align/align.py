"""Stale sibling rows aligned from the Lakestar run (PRO-108) in its own ingest (COLLECTION.md s9; Erik 2026-09-29).
Adapted from Project A's kit (PRO-102). One classification line per stale row, built from the Lakestar row's own
cited evidence (never Lakestar's site), written to scratch/align/<book>.jsonl and recorded ONCE into that book with
`run.py record --investor <book>` (the record note-join bug: the line carries no `note` key that would replace the
book's own note; the alignment sentence goes into `alignment_note`).
Usage: python3 align.py [--dry] [book ...]"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro108"
C = json.loads((HERE.parents[1] / "companies" / "classification.json").read_text())
# book -> [(sibling slug, lakestar slug, kind)]
PAIRS = {
    "cherry": [("aware", "aware", "status"), ("rows", "rows", "status")],
    "accel": [("cambridge-aerospace", "cambridge-aerospace", "value"), ("public", "public", "value"), ("rows", "rows", "status")],
    "greylock": [("entrepreneur-first", "entrepreneur-first", "value")],
    "lux-capital": [("kela-technologies", "kela", "value"), ("varda", "varda", "value")],
    "sequoia-capital": [("kela", "kela", "value")],
    "lightspeed": [("lemon-markets", "lemon-markets", "status")],
    "seedcamp": [("priori-data", "priori-data", "status")],
    "khosla-ventures": [("varda", "varda", "value")],
}
def line(sib, mine, kind):
    c = C[mine]
    d = {"slug": sib, "who": WHO}
    if kind == "status":
        d.update(status=c["status"], valuation_range="below_1b")
        if c.get("status_citation"):
            d["status_citation"] = c["status_citation"]
        d["note"] = f"Aligned 2026-10-01 from the Lakestar run (PRO-108, rule 10): status {c['status']} ({c.get('status_citation', 'see the Lakestar row')})."
    else:
        d.update(valuation_range=c["valuation_range"], valuation_usd=c["valuation_usd"], valuation_source="web_verified",
                 valuation_range_source="web_verified", valuation_citation=c["valuation_citation"], valuation_asof=c["valuation_asof"])
        d["note"] = f"Aligned 2026-10-01 from the Lakestar run (PRO-108, rule 10): ${c['valuation_usd']/1e9:.2f}B as of {c['valuation_asof']} ({c['valuation_citation']})."
    return d
def main():
    dry = "--dry" in sys.argv
    books = [a for a in sys.argv[1:] if not a.startswith("--")] or list(PAIRS)
    for b in books:
        lines = [line(*p) for p in PAIRS[b]]
        f = HERE / f"{b}.jsonl"
        f.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
        if dry:
            print(b, len(lines), "line(s) written, not recorded"); continue
        r = subprocess.run(["python3", "scripts/run.py", "record", "--investor", b, str(f)], cwd=ROOT, capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip().splitlines()
        print(b, "|", out[-1] if out else "")
        if r.returncode or "recorded" not in (out[-1] if out else ""):
            print("\n".join(out[-12:])); sys.exit(1)
if __name__ == "__main__":
    main()
