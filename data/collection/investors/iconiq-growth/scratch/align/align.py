"""Rule-10 alignment from the ICONIQ Growth run (PRO-168), approved by Erik 2026-09-29 ("ingest", on
the closing message that offered aligning the stale sibling rows with the ingest). One classification line
per stale row, written to scratch/align/<investor>.jsonl and recorded into that investor's book with
`run.py record --investor <investor>` (per-key merge; a key Erik set by hand is kept). Each line copies the
ICONIQ row's cited value (its citation was read in this run or by the sibling runs that carry the same
figure). The pairs were found by scratch/align/compare.py: every accepted rule-10 pair in live books, plus
same-band pairs whose figure differs by more than 20% where the ICONIQ mark is the newer priced event.
Left out: books in flight or not yet ingested (Founders Fund, GV, Tiger Global), a16z's Backstory row (a16z
also carries People.ai, the same company: a double count for a16z's own rebuild), and figure-less
below-$1B rows (Pinecone, Braintrust).

Usage: python3 align.py [--dry]   (--dry writes the jsonl files, records nothing)
"""
import csv
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro168"
TAG = "Aligned 2026-09-29 from the ICONIQ Growth run (PRO-168, rule 10)"
MINE = {r["slug"]: r for r in csv.DictReader(open(ROOT / "data/collection/investors/iconiq-growth/companies/base.csv"))}

WHY = {
    "airbnb": "market cap $92.84B on 2026-09-25 (StockAnalysis), below the $100B edge",
    "aurora-solar": "the $250M Series D of February 2022 at $4B (Bloomberg)",
    "drata": "the $200M Series C of December 2022 at $2B",
    "headspin": "PartnerOne bought HeadSpin for $28.2M in July 2024 (TechCrunch, 2024-07-18): acquired",
    "houzz": "the $400M Series E of June 2017 at $4B (TechCrunch, 2017-06-24)",
    "k2-space": "the August 2026 round at $6.8B",
    "miro": "Bending Spoons' definitive agreement of 2026-09-10 at an equity value of about $1.79B (the buyer's release); signed, not closed, so private at the agreed price",
    "monte-carlo": "the $135M Series D of May 2022 at $1.6B (the company's post)",
    "omni": "the April 2026 round at $1.5B",
    "panther": "Databricks completed its acquisition of Panther in August 2026 (Databricks' post): acquired",
    "quince": "the $500M Series E of March 2026 at $10.1B (TechCrunch, 2026-03-11)",
    "rain": "the January 2026 Series C at $1.95B (Crunchbase News)",
    "reify-health": "the $220M Series C of August 2021 at $4.8B",
    "rillet": "the August 2026 round at $1B (the company's release)",
    "robinhood": "market cap $104.71B on 2026-09-28 (StockAnalysis), above the $100B edge",
    "ajaib": "SBI Holdings' $270M for about 20% in August 2026, valuing Ajaib at more than $1.3B (The Block, 2026-08-28)",
    "anthropic": "the round of May 2026 at $965B (the company's announcement)",
    "automattic": "the $288M round of 2021 at $7.5B (Matt Mullenweg's post of 2021-08-16); the $3B unicorn-list figure is superseded",
    "ezcater": "the $100M Series D-2 of December 2021 at $1.6B post-money (the company's release)",
    "floqast": "the $100M Series E of April 2024 at $1.6B",
    "hightouch": "the April 2026 round at $2.75B",
    "legora": "the March 2026 round at $5.55B",
    "ramp": "the June 2026 round at $44B (CNBC)",
    "wealthsimple": "the equity round of up to C$750M at a C$10B post-money valuation (the company's release of 2025-10-27), $7.15B at the ECB rate",
    "anduril": "the May 2026 round at about $61B",
    "openai": "the March 2026 round at $852B (CNBC)",
    "stripe": "the February 2026 tender at $159B",
    "whatnot": "the August 2026 round at $20B (Fortune)",
    "komodo-health": "the $220M Series E of March 2021 at $3.3B (MobiHealthNews); the aggregator's $3.71B is not a priced event (Rule A)",
}

TARGETS = {
    "airbnb": ["a16z:airbnb", "greylock:airbnb", "sequoia-capital:airbnb", "y-combinator:airbnb"],
    "aurora-solar": ["lux-capital:aurora-solar"],
    "drata": ["menlo-ventures:drata-inc"],
    "headspin": ["battery-ventures:headspin", "eqt-ventures:headspin", "felicis:headspin"],
    "houzz": ["sequoia-capital:houzz"],
    "k2-space": ["first-round-capital:k2-space", "lightspeed:k2-space", "redpoint-ventures:k2-space"],
    "miro": ["accel:miro"],
    "monte-carlo": ["accel:monte-carlo"],
    "omni": ["first-round-capital:omni", "redpoint-ventures:omni"],
    "panther": ["lightspeed:panther"],
    "quince": ["8vc:quince", "insight-partners:quince"],
    "rain": ["lightspeed:rain"],
    "reify-health": ["battery-ventures:reify-health"],
    "rillet": ["a16z:rillet", "creandum:rillet", "first-round-capital:rillet", "sequoia-capital:rillet"],
    "robinhood": ["a16z:robinhood", "sequoia-capital:robinhood", "thrive-capital:robinhood"],
    "ajaib": ["ivp:ajaib", "ribbit-capital:ajaib", "y-combinator:ajaib"],
    "anthropic": ["greylock:anthropic", "lightspeed:anthropic", "menlo-ventures:anthropic"],
    "automattic": ["general-catalyst:automattic", "insight-partners:automattic"],
    "ezcater": ["insight-partners:ezcater"],
    "floqast": ["insight-partners:floqast", "redpoint-ventures:floqast"],
    "hightouch": ["y-combinator:hightouch"],
    "legora": ["redpoint-ventures:legora"],
    "ramp": ["general-catalyst:ramp", "greylock:ramp", "khosla-ventures:ramp", "lux-capital:ramp", "redpoint-ventures:ramp"],
    "wealthsimple": ["greylock:wealthsimple", "redpoint-ventures:wealthsimple"],
    "anduril": ["lux-capital:anduril"],
    "openai": ["greylock:openai"],
    "stripe": ["redpoint-ventures:stripe"],
    "whatnot": ["a16z:whatnot", "redpoint-ventures:whatnot"],
    "komodo-health": ["a16z:komodo-health"],
}


def line(target_slug: str, mine: dict, why: str) -> dict:
    r = {"slug": target_slug, "who": WHO, "status": mine["status"], "note": f"{TAG}: {why}.",
         "clear_flags": ["needs_web_value"]}
    if mine["status"] in ("acquired", "defunct"):
        r.update({"valuation_range": "below_1b", "valuation_usd": None})
        return r
    r.update({"valuation_range": mine["valuation_range"],
              "valuation_usd": float(mine["valuation_usd"]) if mine["valuation_usd"] else None,
              "valuation_source": "web_verified", "valuation_range_source": "web_verified",
              "valuation_asof": mine["valuation_asof"], "valuation_citation": mine["valuation_citation"],
              "valuation_confidence": "high"})
    return r


def build() -> dict:
    per: dict = {}
    for my_slug, targets in TARGETS.items():
        mine = MINE[my_slug]
        for t in targets:
            inv, slug = t.split(":")
            per.setdefault(inv, []).append(line(slug, mine, WHY[my_slug]))
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
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-1500:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
