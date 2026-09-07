#!/usr/bin/env python3
"""Cross-investor alignment and the standing verification duties (§8, §10).

Invariant 10 compared this base against every published sibling and found 56
disagreements on 228 shared companies. Three kinds came out of it:

1. **This run was stale or wrong** -- almost always because a deterministic
   layer had pre-filled the row and the queue therefore never asked. The
   float sweep put Arena at $0.08B and the unicorn snapshot put Voi at $1B;
   both are fixed here against the freshest cited figure.
2. **This run is the fresher side** -- Runway at $5.3B against two siblings
   still at below_1b, Poolside at $12B against Redpoint's $3B. Those are left
   alone and reported for the wave-level alignment, since a session aligns
   its own investor and not its siblings.
3. **The pair is not the same company.** Two of these are genuine name
   collisions and are ruled `distinct` in cross-rulings.json rather than
   aligned -- the a16z "arena" row cites an LMArena round, and a16z's
   "luma-ai" is the video model, not the mesh-WiFi company Felicis backed.

Public caps are all re-read at one as-of date (2026-09-04) rather than
inherited from siblings, because §10 warns that runs months apart straddle a
band edge on date alone.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "scratch" / "queue" / "align.out.jsonl"
SA = "https://stockanalysis.com/stocks/{}/market-cap/"

ROWS = []


def row(slug, **kw):
    r = {"slug": slug, "who": WHO}
    r.update(kw)
    ROWS.append(r)


# ---- public rows: one fresh cap each, as of 2026-09-04
for slug, tick, usd, band, note in [
    ("guardant-health", "gh", 21_660_000_000, "10b_plus",
     "Nasdaq: GH, market cap $21.66B as of 2026-09-04. Corrects a $6.20B "
     "stale-float pre-fill that the queue never asked about; the siblings "
     "holding this row had it at $21.88B and $22.54B, so the disagreement was "
     "this run's."),
    ("warby-parker", "wrby", 3_010_000_000, "1b_plus",
     "NYSE: WRBY, market cap $3.01B as of 2026-09-04. Four siblings hold this "
     "row between $2.90B and $3.01B on different as-of dates; re-read here at "
     "one date rather than inherited."),
    ("liveramp", "ramp", 2_300_000_000, "1b_plus",
     "NYSE: RAMP, market cap $2.30B as of 2026-09-04."),
]:
    row(slug, status="public", status_confidence="high",
        valuation_range=band, valuation_usd=usd,
        valuation_source="web_verified", valuation_range_source="web_verified",
        valuation_confidence="high", valuation_citation=SA.format(tick),
        note=note, clear_flags=["cite_pending", "needs_web_value", "stale"])

# ---- private rows aligned to the freshest cited figure
row("plaid", status="private", status_confidence="high",
    valuation_range="1b_plus", valuation_usd=8_000_000_000,
    valuation_source="web_verified", valuation_range_source="web_verified",
    valuation_confidence="high",
    valuation_citation="https://en.wikipedia.org/wiki/Plaid_Inc.",
    note="Aligned to the freshest sibling figure ($8.0B, Feb 2026). This run "
         "carried $13.4B from the 2021-04 unicorn snapshot, which is the "
         "pre-fill class ruling R5 demotes -- three siblings all had it lower "
         "and more recent. Felicis entered at the $12.5M Series A in 2014.",
    clear_flags=["stale", "cite_pending"])

row("unconventional-ai", status="private", status_confidence="high",
    valuation_range="1b_plus", valuation_usd=4_500_000_000,
    valuation_source="web_verified", valuation_range_source="web_verified",
    valuation_confidence="high",
    valuation_citation="https://techcrunch.com/2025/12/09/unconventional-ai-confirms-its-massive-4",
    note="Corrected from below_1b: three independent sibling runs (a16z, "
         "Lightspeed, Lux) all hold this at $4.5B on the Dec-2025 seed. A "
         "2026-vintage row this run had ruled out by the small-and-recent "
         "heuristic, and exactly the miss the momentum slice exists to catch.",
    clear_flags=["needs_web_value"])

row("lm-arena", status="private", status_confidence="high",
    valuation_range="1b_plus", valuation_usd=1_700_000_000,
    valuation_source="web_verified", valuation_range_source="web_verified",
    valuation_confidence="high",
    valuation_citation="https://techcrunch.com/2026/01/06/lmarena-lands-1-7b-valuation-four-months",
    note="LMArena reached $1.7B in Jan 2026. Found by chasing invariant 10: "
         "the a16z row named 'arena' cites this round, which is how the "
         "collision with Felicis's arena.ai was spotted.",
    clear_flags=["needs_web_value"])

row("voi", status="private", status_confidence="high",
    valuation_range="below_1b", valuation_range_source="web_verified",
    valuation_confidence="high",
    valuation_citation="https://micromobility.substack.com/p/what-a-week-dott-raised-85m-voi-hits",
    note="Corrected from a 1b_plus unicorn-snapshot pre-fill to below_1b, "
         "aligning with Creandum's fresher reading (2025-09). Voi's 2021 $1B "
         "mark did not hold; its lead investor VNV Global has published fair "
         "values a third below it, which is §6's documented-collapse test.",
    clear_flags=["stale", "needs_web_value"])

# ---- status corrections where a sibling's evidence is better
for slug, status, note in [
    ("solum", "acquired",
     "acq. by Monsanto, 2014. This run's own note said so while the status "
     "column still read private -- corrected."),
    ("stainless", "acquired",
     "Aligned: a16z and Sequoia independently hold this row as acquired."),
    ("resourcely", "acquired", "Aligned with a16z."),
    ("sleuth", "acquired", "Aligned with Menlo Ventures."),
    ("snowball", "defunct", "Aligned with First Round Capital."),
    ("circulate", "defunct", "Aligned with First Round Capital."),
    ("civitas-learning", "acquired", "Aligned with First Round Capital."),
    ("chloe-isabel", "acquired",
     "Aligned with First Round Capital: the business was sold rather than "
     "simply wound up, which §6 reads as acquired."),
]:
    row(slug, status=status, status_confidence="medium", note=note)

# ---- §10 invariant 4: a $1B+ row needs class 1/2 stage evidence or the
# cite_pending marker that says the debt is known and queued.
for slug in ("opendoor", "radiant-nuclear", "modern-health", "planet-labs",
             "recursion-pharmaceuticals"):
    row(slug, flags=["cite_pending"],
        note="Entry stage carries no class-1 citation: the row is $1B+, so the "
             "citation debt is marked rather than left implicit (§10.4).")


def main() -> None:
    OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in ROWS) + "\n")
    print(f"wrote {OUT.name}: {len(ROWS)} rows")


if __name__ == "__main__":
    main()
