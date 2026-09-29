"""Stale sibling rows aligned from the TCV run (PRO-169), in the run's own ingest (COLLECTION.md 9, 2026-09-29).
One classification line per stale row, written to scratch/align/<investor>.jsonl and recorded into that book with
`run.py record --investor <investor>`. Each line copies TCV's cited value, never a citation of TCV's own site
(Aviatrix carries the company's PR Newswire release instead). The pairs: every accepted rule-10 pair in
cross-rulings.json, Greylock's Upwind (a slug difference rule 10 missed), and same-band rows more than 20% off a
newer TCV mark. Skipped: Y Combinator (its readback before the write differs in one name the run did not make).

Usage: python3 align.py [--dry] [book ...]
"""
import csv, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro169"
TAG = "Aligned 2026-09-29 from the TCV run (PRO-169, rule 10)"
MINE = {r["slug"]: r for r in csv.DictReader(open(ROOT / "data/collection/investors/tcv/companies/base.csv"))}
CITE = {"aviatrix": "https://www.prnewswire.com/news-releases/aviatrix-raises-200-million-in-funding-led-by-tcv-elevating-the-cloud-networking-leaders-valuation-to-2-billion-301371330.html"}
WHY = {
    "aviatrix": "the $200M Series E of September 2021 at $2B (Aviatrix's release, PR Newswire, 2021-09-08)",
    "grow-therapy": "the $150M Series D of March 2026 at $3B (Modern Healthcare)",
    "nourish": "the $100M Series C of May 2026 at $1.75B (Reuters)",
    "revolut": "the secondary share sale of July 2026 at $115B (Bloomberg, 2026-07-22)",
    "zillow": "listed on Nasdaq since July 2011 and operating: market cap $6.2B on 2026-09-29 (StockAnalysis)",
    "upwind-security": "the $300M Series C of September 2026 at $3.8B (SiliconANGLE, 2026-09-03)",
    "attentive": "the June 2021 round at $5B",
    "pennylane": "the January 2026 round at $4.25B (Bloomberg, 2026-01-20)",
    "klarna": "market cap $4.85B on 2026-09-25 (StockAnalysis)",
    "facebook": "market cap $1.83T on 2026-09-29 (StockAnalysis)",
    "groupon": "market cap $812.9M on 2026-09-29 (StockAnalysis)",
}
TARGETS = {
    "aviatrix": ["8vc:aviatrix"],
    "grow-therapy": ["menlo-ventures:grow-therapy", "sequoia-capital:grow-therapy"],
    "nourish": ["menlo-ventures:nourish", "thrive-capital:nourish"],
    "revolut": ["a16z:revolut", "greylock:revolut"],
    "zillow": ["benchmark:zillow-com"],
    "upwind-security": ["greylock:upwind"],
    "attentive": ["coatue:attentive", "felicis:attentive", "ivp:attentive"],
    "pennylane": ["sequoia-capital:pennylane"],
    "klarna": ["creandum:klarna", "sequoia-capital:klarna"],
    "facebook": ["accel:facebook"],
    "groupon": ["battery-ventures:groupon"],
}


def owes_cite(inv, slug, band):
    """verify's rule: a $1B+ row with a stage that is neither cited nor structural carries cite_pending."""
    row = next((r for r in csv.DictReader(open(ROOT / f"data/collection/investors/{inv}/companies/base.csv")) if r["slug"] == slug), {})
    cited = bool((row.get("entry_stage_citation") or "").strip()) or row.get("entry_stage_source") in ("formd_structural", "formd_band")
    return band in ("1b_plus", "10b_plus", "100b_plus") and not cited and row.get("entry_stage") not in ("undetermined", "", None) \
        and "cite_pending" not in (row.get("flags") or "").split(";")


def line(target_slug, mine, why, my_slug, inv):
    r = {"slug": target_slug, "who": WHO, "status": mine["status"], "note": f"{TAG}: {why}.", "clear_flags": ["needs_web_value"]}
    if owes_cite(inv, target_slug, mine["valuation_range"]):
        r["flags"] = ["cite_pending"]   # the book's entry round for this row is not cited
    r.update({"valuation_range": mine["valuation_range"], "valuation_usd": float(mine["valuation_usd"]),
              "valuation_source": "web_verified", "valuation_range_source": "web_verified",
              "valuation_asof": mine["valuation_asof"], "valuation_citation": CITE.get(my_slug, mine["valuation_citation"]),
              "valuation_confidence": "high"})
    return r


def build():
    per = {}
    for my, targets in TARGETS.items():
        for t in targets:
            inv, slug = t.split(":")
            per.setdefault(inv, []).append(line(slug, MINE[my], WHY[my], my, inv))
    # 8VC's Quince, aligned to $10.1B by the ICONIQ run, owes the same marker (8VC's verify fails on it)
    per.setdefault("8vc", []).append({"slug": "quince", "who": WHO, "flags": ["cite_pending"],
        "note": "Flagged cite_pending 2026-09-29 (PRO-169 alignment pass): a $1B+ row whose entry round is not cited."})
    # Rillet, aligned to $1B by the ICONIQ run, owes the same marker in a16z and Creandum (their verify fails on it)
    for inv in ("a16z", "creandum"):
        per.setdefault(inv, []).append({"slug": "rillet", "who": WHO, "flags": ["cite_pending"],
            "note": "Flagged cite_pending 2026-09-29 (PRO-169 alignment pass): a $1B+ row whose entry round is not cited."})
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
