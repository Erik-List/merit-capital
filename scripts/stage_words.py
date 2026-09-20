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

import re

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
# A numbered tranche of one round is that round ("Series A-1", "Seed-2" on
# Lightspeed's cards): the company negotiated one A and closed it in pieces.
for _n in "123456":
    _ROUND[f"seed-{_n}"] = "Seed"
    _ROUND[f"seed {_n}"] = "Seed"
    _ROUND[f"a-{_n}"] = "Series A"      # a card that drops the word "Series"
    _ROUND[f"a{_n}"] = "Series A"
    for _sep in ("-", " "):
        _ROUND[f"series a{_sep}{_n}"] = "Series A"
        _ROUND[f"series-a{_sep}{_n}"] = "Series A"
    for _letter in "bcdefgh":
        _ROUND[f"series {_letter}-{_n}"] = "Growth"
        _ROUND[f"series-{_letter}-{_n}"] = "Growth"
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
    "common", "common stock", "ordinary", "ordinary shares", "preferred",
    "token", "tokens", "grant", "warrant", "convertible note", "note",
    "series unknown", "series_unknown", "unknown", "other", "n/a", "none",
    "ipo", "m&a", "spac", "acquisition", "acquired", "exit", "debt",
})

# Seed before Series A before Growth: where a field carries every round the firm
# joined, the ENTRY is the earliest of them.
_ORDER = {"Pre-Seed": 0, "Seed": 1, "Series A": 2, "Growth": 3}


# A qualifier that says the value is NOT read off the record. The firm's own CMS
# carries these beside real round words ("Seed (prior)", "Partnered (round
# unstated)"), and they mean the opposite of a label.
_DISCLAIMED = re.compile(r"\b(prior|unstated|unknown|tbd|n/?a|undisclosed)\b", re.I)
# ...and a role word that trails the round in a CMS milestone line ("Series C
# Partner", from Menlo's "2018 - Partnered, Series C").
_ROLE_TAIL = re.compile(r"\s*\b(partner|partnered|investor|round|financing|stage)\b\s*$", re.I)


def round_word(value) -> str | None:
    """The single taxonomy stage a firm's own label collapses onto, or None.

    None means the value is not a round word — an anchor, an event, or a coarse
    band that straddles two stages. It never means "not recognised": an
    unrecognised value returns None too, and `unknown_round_words` is how a run
    finds out that a site changed its vocabulary.
    """
    if value is None:
        return None
    raw = " ".join(str(value).strip().split())
    if _DISCLAIMED.search(raw):
        return None
    s = raw.lower()
    if s in _NOT_A_ROUND:
        return None
    if s in _ROUND:
        return _ROUND[s]
    # Only then peel a trailing role word ("Series C Partner", "Seed Round").
    # Never before: "Late Stage" is a value in its own right, and stripping
    # "Stage" from it first turned 71 Accel rows into unrecognised "Late".
    for _ in range(2):
        peeled = _ROLE_TAIL.sub("", raw).strip()
        if peeled == raw:
            break
        raw = peeled
        if raw.lower() in _NOT_A_ROUND:
            return None
        if raw.lower() in _ROUND:
            return _ROUND[raw.lower()]
    return None


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
        raw = " ".join(str(v).strip().split())
        if raw.isdigit():
            continue          # a year travelling with the round word ("Series A, 2022")
        if round_word(raw):
            continue          # the vocabulary resolves it
        if _DISCLAIMED.search(raw):
            continue          # a deliberate refusal, not an unknown word
        if raw.lower() not in _NOT_A_ROUND:
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
        if isinstance(it, str) and any(sep in it for sep in "|,+/"):
            # "Seed + Series A", "Series A / Series B", "Series A, 2022": one
            # field holding several rounds, or a round travelling with its year.
            for sep in "|+/":
                it = it.replace(sep, ",")
            out.extend(p for p in (x.strip() for x in it.split(",")) if p)
        else:
            out.append(it)
    return out
