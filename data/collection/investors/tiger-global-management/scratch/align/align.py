"""Stale sibling rows aligned from the Tiger Global run (PRO-167) in its own ingest (COLLECTION.md 9; Erik's
"ingest", 2026-09-30). One classification line per stale row, written to scratch/align/<book>.jsonl and recorded
ONCE into that book with `run.py record --investor <book>` (recording a line twice drops the row's note: the
record note-join bug). Each line copies Tiger's cited value; no line cites Tiger's own site.

The pairs (scratch/align/compare.py): the accepted rule-10 pairs in companies/cross-rulings.json whose other side
is stale, and same-band rows more than 20% off a newer Tiger mark. Only books that passed the precheck are written
(clean tree, no in-flight marker, verify clean, readback before = committed CSV): benchmark, 8vc, insight-partners,
menlo-ventures, redpoint-ventures, ribbit-capital, thrive-capital. Skipped and reported: a16z, accel,
battery-ventures, greylock, lightspeed, sequoia-capital, spark-capital (verify not clean on pairs of other books),
y-combinator (verify not clean; readback before differs), general-catalyst (in flight).

Usage: python3 align.py [--dry] [book ...]
"""
import csv, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro167"
TAG = "Aligned 2026-09-30 from the Tiger Global run (PRO-167, rule 10)"
INV = ROOT / "data/collection/investors"
MINE = {r["slug"]: r for r in csv.DictReader(open(INV / "tiger-global-management/companies/base.csv"))}
WHY = {
    "quora": "the $75M raise from Andreessen Horowitz of January 2024 at a $500M valuation (Yahoo Finance, 2024-01-09), which supersedes the 2017 $1.8B",
    "blend-labs": "market cap $248.3M on 2026-09-29 (StockAnalysis, NYSE: BLND)",
    "cred": "Meta's $900M for a 20% stake in June 2026, which prices CRED at $4.5B (Ascendants), the mark the Coatue and General Catalyst books carry",
    "avant": "the $325M Series E of September 2015, which 'would value the company at $1.975 billion' (BuzzFeed News, 2015-09-29)",
    "rogo": "the $160M Series D of April 2026 led by Kleiner Perkins at a $2B valuation (TipRanks, 2026-04-29)",
    "sidecar-health": "the $125M Series C of January 2021 at $1B (FinTech Global, 2021-02-01); the $165M Series D of June 2024 stated no valuation",
    "chime": "market cap $10.14B on 2026-09-25 (StockAnalysis, Nasdaq: CHYM)",
    "scribe": "the November 2025 round at a $1.3B valuation (TechCrunch, 2025-11-10)",
    "cockroach-labs": "the $278M Series F of December 2021 at $5B (Cockroach Labs' release, PR Newswire)",
    "nextdoor": "market cap $930.4M on 2026-09-29 (StockAnalysis, NYSE: NXDR)",
}
TARGETS = {   # tiger slug -> ["book:slug", ...]
    "quora": ["benchmark:quora"],
    "blend-labs": ["8vc:blend", "thrive-capital:blend-labs"],
    "cred": ["insight-partners:cred", "ribbit-capital:cred"],
    "avant": ["ribbit-capital:avant"],
    "rogo": ["thrive-capital:rogo"],
    "sidecar-health": ["menlo-ventures:sidecar-health"],
    "chime": ["menlo-ventures:chime"],
    "scribe": ["redpoint-ventures:scribe"],
    "cockroach-labs": ["redpoint-ventures:cockroach-labs"],
    "nextdoor": ["redpoint-ventures:nextdoor"],
}


def mine(slug):
    if slug in MINE:
        return MINE[slug]
    hits = [r for r in MINE.values() if r["name"].lower() == slug.replace("-", " ")]
    assert len(hits) == 1, slug
    return hits[0]


def owes_cite(inv, slug, band):
    """verify's rule: a $1B+ row whose stage is neither cited nor structural carries cite_pending."""
    row = next((r for r in csv.DictReader(open(INV / inv / "companies/base.csv")) if r["slug"] == slug), None)
    assert row, f"{inv}:{slug} not in the book"
    cited = bool((row.get("entry_stage_citation") or "").strip()) or row.get("entry_stage_source") in ("formd_structural", "formd_band")
    return band in ("1b_plus", "10b_plus", "100b_plus") and not cited and row.get("entry_stage") not in ("undetermined", "", None) \
        and "cite_pending" not in (row.get("flags") or "").split(";")


def line(inv, slug, m, why):
    r = {"slug": slug, "who": WHO, "status": m["status"], "note": f"{TAG}: {why}.", "clear_flags": ["needs_web_value"],
         "valuation_range": m["valuation_range"], "valuation_usd": float(m["valuation_usd"]),
         "valuation_source": "web_verified", "valuation_range_source": "web_verified",
         "valuation_asof": m["valuation_asof"], "valuation_citation": m["valuation_citation"], "valuation_confidence": "high"}
    if owes_cite(inv, slug, m["valuation_range"]):
        r["flags"] = ["cite_pending"]   # the book's entry round for this row is not cited
    return r


def build():
    per = {}
    for my, targets in TARGETS.items():
        m = mine(my)
        for t in targets:
            inv, slug = t.split(":")
            per.setdefault(inv, []).append(line(inv, slug, m, WHY[my]))
    return per


if __name__ == "__main__":
    dry = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    for inv, lines in sorted(build().items()):
        if only and inv not in only:
            continue
        p = HERE / f"{inv}.jsonl"
        p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines))
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if dry:
            continue
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)], cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-800:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
