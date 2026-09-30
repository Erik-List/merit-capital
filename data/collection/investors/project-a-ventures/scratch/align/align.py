"""Stale sibling rows aligned from the Project A run (PRO-102) in its own ingest (COLLECTION.md s9; Erik 2026-09-29).
Adapted from Tiger Global's kit (PRO-167). One classification line per stale row, written to scratch/align/<book>.jsonl
and recorded ONCE into that book with `run.py record --investor <book>` (the record note-join bug). Each line cites the
underlying evidence, never Project A's own site.

The pairs are `same` rulings in companies/cross-rulings.json: rows the name key could not join, so rule 10 had never
compared them. Two sibling sides are stale:
- y-combinator:tabula read `defunct` carried from Benchmark's and Greylock's Tabula, the FPGA chip maker that shut in
  2015; YC's Tabula is Tabula GmbH (tabula.de, Berlin, S24), which YC's own page lists as Active.
- insight-partners:expresssteuer-fka-express-group read `unknown`; ExpressGroup GmbH (Hamburg) has been in liquidation
  since March 2024 after a December 2023 insolvency, with no sale.
One city is aligned too: balderton-capital:quantum-systems read Munich, the metro; every group entity is registered in
Gilching (the city rule publishes the municipality).
Superseded the same day: Erik ruled that Quantum Systems reads Munich (Gilching is near Munich). Balderton's row was
restored to its earlier state, and the Project A and HV Capital rows moved to Munich (report.md section 15). The
balderton-capital line below is kept as the record of what was written; do not re-record it.
Skipped at the gate and reported: y-combinator (tabula; verify not clean on an unrelated Vela pair, readback before
differs by one row) and sequoia-capital (stark reads Munich; SKD SE's registered office is Berlin; verify not clean on
an unrelated Versatile pair).

Usage: python3 align.py [--dry] [book ...]
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro102"
TAG = "Aligned 2026-09-30 from the Project A run (PRO-102, rule 10)"

LINES = {
    "y-combinator": [{
        "slug": "tabula", "who": WHO, "status": "private",
        "status_citation": "https://www.ycombinator.com/companies/tabula",
        "flags": ["model_disputes_source"],
        "note": f"{TAG}: this is Tabula GmbH (tabula.de), the Berlin accounting-automation company from Summer 2024, "
                "which YC's own page lists as Active (founded 2024, 13 people). The `defunct` status and the 2015 date "
                "came from Tabula Inc., the FPGA chip maker Benchmark and Greylock backed, which shut in 2015: a "
                "namesake join, ruled distinct in this book's cross-rulings.json.",
    }],
    "balderton-capital": [{
        "slug": "quantum-systems", "who": WHO, "hq_city": "Gilching", "hq_city_source": "web_verified",
        "note": f"{TAG}: Gilching is the registered seat of Quantum-Systems GmbH (Amtsgericht München HRB 217004) "
                "and of every group entity (North Data); Munich is the metro, which the city rule does not publish. "
                "The HV Capital and Project A rows read Gilching.",
    }],
    "insight-partners": [{
        "slug": "expresssteuer-fka-express-group", "who": WHO, "status": "defunct",
        "status_citation": "https://www.northdata.com/ExpressGroup%20GmbH,%20Hamburg/HRB%20135813",
        "note": f"{TAG}: ExpressGroup GmbH (Hamburg, HRB 135813) had a provisional insolvency administrator appointed on "
                "2023-12-12 and has been in liquidation since March 2024, with no sale (North Data): defunct.",
    }],
}

DISTINCT = {
    "y-combinator": [
        {"rows": ["y-combinator:tabula", f"{b}:{s}"],
         "note": "YC's Tabula is Tabula GmbH (tabula.de), the Berlin accounting-automation company from Summer 2024; "
                 f"{b}'s is Tabula Inc., the Santa Clara FPGA chip maker that shut in 2015. Different companies under "
                 "one name (ruled at the Project A ingest, PRO-102, 2026-09-30)."}
        for b, s in (("benchmark", "tabula"), ("greylock", "tabula"), ("balderton-capital", "tabula"),
                     ("new-enterprise-associates", "tabula-inc"))],
}


def rule_distinct(inv):
    p = ROOT / f"data/collection/investors/{inv}/companies/cross-rulings.json"
    d = json.loads(p.read_text())
    have = {frozenset(e["rows"]) for e in d.get("distinct", [])}
    add = [e for e in DISTINCT.get(inv, []) if frozenset(e["rows"]) not in have]
    if add:
        d.setdefault("distinct", []).extend(add)
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
    print(f"   {inv}: {len(add)} distinct pair(s) ruled")


if __name__ == "__main__":
    dry = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for inv, lines in sorted(LINES.items()):
        if only and inv not in only:
            continue
        p = HERE / f"{inv}.jsonl"
        p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines))
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if dry:
            continue
        rule_distinct(inv)
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)], cwd=ROOT,
                           capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-800:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
