"""Stale sibling rows aligned from the NEA run (PRO-100), in the run's own ingest (COLLECTION.md 9).
One classification line per stale row, built from the cross-book judges' plan (scratch/sibling-align.json: each
sibling value with a citation that is not nea.com), written to scratch/align/<book>.jsonl and recorded into that
book ONCE with `run.py record --investor <book>` (the note-join defect). A $1B+ row whose stage that book does not
cite also gets cite_pending (verify's rule), as the TCV kit does.
Usage: python3 align.py --build            (write the jsonl files only)
       python3 align.py --record <book>    (record one book's file)
"""
import csv, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro100"
TAG = "Aligned 2026-09-30 from the NEA run (PRO-100, rule 10)"


def owes_cite(inv, slug, band):
    row = next((r for r in csv.DictReader(open(ROOT / f"data/collection/investors/{inv}/companies/base.csv"))
                if r["slug"] == slug), {})
    cited = bool((row.get("entry_stage_citation") or "").strip()) or \
        row.get("entry_stage_source") in ("formd_structural", "formd_band")
    return band in ("1b_plus", "10b_plus", "100b_plus") and not cited and \
        row.get("entry_stage") not in ("undetermined", "", None) and \
        "cite_pending" not in (row.get("flags") or "").split(";")


def build():
    per = {}
    for p in json.load(open(HERE.parent / "sibling-align.json")):
        s = dict(p["sibling"])
        inv, slug = s.pop("book"), s.pop("slug")
        note = s.pop("note", "").strip()
        s.pop("status_citation", None)          # not a classification key; the note names the source
        line = {"slug": slug, "who": WHO, **s, "note": f"{TAG}: {note}"}
        if "valuation_range" in s and owes_cite(inv, slug, s["valuation_range"]):
            line["flags"] = ["cite_pending"]
        per.setdefault(inv, []).append(line)
    return per


if __name__ == "__main__":
    if "--build" in sys.argv:
        for inv, lines in sorted(build().items()):
            (HERE / f"{inv}.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines))
            print(f"{inv}: {len(lines)} line(s)")
    elif "--record" in sys.argv:
        inv = sys.argv[sys.argv.index("--record") + 1]
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(HERE / f"{inv}.jsonl")],
                           cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-1500:])
        sys.exit(r.returncode)
