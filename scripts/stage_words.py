#!/usr/bin/env python3
"""The round-word vocabulary: what a firm's own stage label is allowed to mean.

PRO-131 (a) made the firm's own listing class-1 `first_party` entry_stage
evidence **where it gives a round word**, and kept the guard that a bare year is
an anchor and not a label. This module is that guard, written once and shared by
`build-company-base.py` (which harvests the label onto the base row) and
`run.py` (which gates what `record` will accept).

Two rules decide whether a site field may label a row, and they are different
questions:

1. **Eligibility is semantic.** The field must be the firm's own claim about the
   round IT entered — "initialInvestmentType", the card's "Invested" field,
   USV's "FIRST INVESTMENT" column. A field that reports the company's CURRENT
   stage is refused however accurate it looks: it describes the company, not the
   deal (Lux R2 and Thrive ruling 8 both refused a Getro job board's `stage`;
   scored here they return 5/14 and 16/29). So is a tag list naming every round
   the firm joined rather than the first (a16z's `stages`, 38/57, thirteen of
   its misses reading Growth on a Series A entry). Eligibility lives in the
   investor's `config.site_api.entry_stage_fields`, in listing order.

2. **A value must collapse onto exactly one taxonomy stage.** This is the bare-
   year guard generalised: `Late Stage`, `Growth` and `Buyout` all collapse onto
   `Growth`, so they label; `Early`, `Early Stage` and `venture` straddle Seed
   and Series A, so they are anchors that may bound entry recency and may not
   mint a stage. `Common`, `Token`, `IPO`, `M&A` and `series_unknown` name no
   round at all.

What the score decides is CONFIDENCE, not admission: an eligible field's label
is class 1 for the round it names (§6), and a documented round still overrides
it with `stage_disputes_band`. Scores measured 2026-09-19 against each book's
own cited rows are in COLLECTION.md §5.
"""
from __future__ import annotations

# Every round word that collapses onto exactly one taxonomy value. Series B and
# later is `Growth` by the §6 taxonomy, and so is a buyout-scale or late-stage
# entry.
_ROUND: dict[str, str] = {
    "pre-seed": "Pre-Seed", "pre seed": "Pre-Seed", "pre_seed": "Pre-Seed",
    "preseed": "Pre-Seed",
    "seed": "Seed", "seed round": "Seed", "seed stage": "Seed",
    "seed extension": "Seed", "safe": "Seed",
    "series-a": "Series A", "series a": "Series A", "series_a": "Series A",
    "a": "Series A", "series a round": "Series A",
}
for _letter in "bcdefghij":
    for _sep in ("-", " ", "_"):
        _ROUND[f"series{_sep}{_letter}"] = "Growth"
_ROUND.update({
    "series b+": "Growth", "series c+": "Growth", "series d+": "Growth",
    "series c or later": "Growth", "series b or later": "Growth",
    "growth": "Growth", "growth stage": "Growth", "late stage": "Growth",
    "late-stage": "Growth", "buyout": "Growth", "pre-ipo": "Growth",
    "pre ipo": "Growth", "crossover": "Growth", "secondary": "Growth",
})

# Values that name something real but not one round: a coarse early band
# straddles Seed and Series A, an event is not an entry, and `common` /
# `series_unknown` decline to say. Listed explicitly so an unrecognised value is
# a parser question rather than a silent refusal.
_NOT_A_ROUND = frozenset({
    "", "early", "early stage", "early-stage", "earlystage", "venture",
    "venture stage", "alumni", "seed/early", "multi-stage", "multistage",
    "common", "common stock", "preferred", "token", "tokens", "grant",
    "series unknown", "series_unknown", "unknown", "other", "n/a", "none",
    "ipo", "m&a", "spac", "acquisition", "acquired", "exit", "debt",
})

# Seed before Series A before Growth: where a field carries every round the firm
# joined, the ENTRY is the earliest of them.
_ORDER = {"Pre-Seed": 0, "Seed": 1, "Series A": 2, "Growth": 3}


def round_word(value) -> str | None:
    """The single taxonomy stage a firm's own label collapses onto, or None.

    None means the value is not a round word — an anchor, an event, or a coarse
    band that straddles two stages. It never means "not recognised": an
    unrecognised value returns None too, and `unknown_round_words` is how a run
    finds out that a site changed its vocabulary.
    """
    if value is None:
        return None
    s = " ".join(str(value).strip().lower().split())
    if s in _NOT_A_ROUND:
        return None
    return _ROUND.get(s)


def earliest_round(values) -> str | None:
    """The earliest round word in a multi-valued field (Felicis `stage_ladder`,
    Spark's era terms). A field that lists Seed and Series A describes a firm
    that entered at the Seed."""
    got = [round_word(v) for v in _flatten(values)]
    got = [g for g in got if g]
    return min(got, key=lambda g: _ORDER[g]) if got else None


def unknown_round_words(values) -> list[str]:
    """Values that are neither a round word nor a known non-round. A site that
    starts publishing "Series A-1" shows up here, not as a silent None."""
    out = []
    for v in _flatten(values):
        s = " ".join(str(v).strip().lower().split())
        if s.isdigit():
            continue  # a year travelling with the round word (USV: "Series A, 2022")
        if s not in _NOT_A_ROUND and s not in _ROUND:
            out.append(str(v))
    return out


def _flatten(values):
    """A site field is a string, a list, or a string with the scraper's own
    multi-value separator in it."""
    if values is None:
        return []
    if isinstance(values, (list, tuple, set)):
        items = list(values)
    else:
        items = [values]
    out = []
    for it in items:
        if isinstance(it, str) and ("|" in it or "," in it):
            out.extend(p for p in (x.strip() for x in it.replace("|", ",").split(",")) if p)
        else:
            out.append(it)
    return out
