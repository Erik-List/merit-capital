#!/usr/bin/env python3
"""The shape rule for the two reader-facing paragraphs of a firm profile.

`components/investor/overview.tsx` renders exactly `investment_concept` (the
thesis) and `history`, and a reader who has never heard of Merit Capital must
understand every word of both (Erik, 2026-09-24, PRO-147; COLLECTION.md §11):

  thesis   the firm's own crisp statement, in its own words, 1-2 sentences
           and at most 25 words, sourced from the firm's own site (Erik,
           2026-09-26). A firm that publishes none (Benchmark) carries a
           derived line, marked `derived: true` on the sidecar field.
  history  at most 3 sentences, 40-80 words, third person: founded (year,
           city, founders), the bets that made the firm, where it stands today.

Neither may carry this pipeline's vocabulary, filing vocabulary or a dash as
punctuation. `build-firm-profile.py` refuses to write a profile that breaks
the rule and `run.py verify` fails it.

Usage: python3 scripts/profile_copy.py [<investor-slug> ...]   (no slug = all)
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

THESIS_SENTENCES = (1, 2)
THESIS_WORDS = (2, 25)
HISTORY_SENTENCES = (1, 3)
HISTORY_WORDS = (40, 80)

# Words that only make sense to someone who has read the playbook. "member"
# and "base" have plain meanings too, but the two paragraphs never need them.
BANNED = re.compile(
    r"\b(base|bases|book|books|filings?|filed|form d|form adv|adv|crd|cik|"
    r"edgar|ledger|verdicts?|members?|registered|registration|"
    r"exempt reporting|relying adviser|sidecar|pipeline|"
    r"(?:recorded|counted|shown|excluded) here)\b", re.I)
FIRST_PERSON = re.compile(r"\b(We|we|Our|our|Us)\b")
DASH = re.compile(r"—| – | -- | - ")

# A period after one of these does not end a sentence.
ABBREVIATIONS = {"inc", "co", "corp", "ltd", "jr", "sr", "dr", "mr", "mrs", "ms",
                 "st", "vs", "no", "e.g", "i.e", "u.s", "l.p", "u.k"}


def sentences(text: str) -> list[str]:
    """Split on . ! ? followed by space and a capital or digit, unless the
    period closes an abbreviation or a single initial ("H. DuBose")."""
    out, start = [], 0
    for m in re.finditer(r"[.!?][\"')”]?\s+(?=[A-Z0-9\"(“])", text):
        word = re.search(r"([A-Za-z.]+)[.!?][\"')”]?\s+$", text[start:m.end()])
        token = (word.group(1) if word else "").lower().rstrip(".")
        if token in ABBREVIATIONS or re.fullmatch(r"[a-z]", token):
            continue
        out.append(text[start:m.end()].strip())
        start = m.end()
    tail = text[start:].strip()
    if tail:
        out.append(tail)
    return out


def words(text: str) -> int:
    return len(text.split())


def problems(row: dict, fields: dict | None = None) -> list[str]:
    """Every way the profile's thesis and history break the shape rule. With
    `fields` (investor/sources.json's), also a sidecar value that differs."""
    out = []
    for key, label, (smin, smax), (wmin, wmax) in (
            ("investment_concept", "thesis", THESIS_SENTENCES, THESIS_WORDS),
            ("history", "history", HISTORY_SENTENCES, HISTORY_WORDS)):
        text = (row.get(key) or "").strip()
        if not text:
            out.append(f"{label}: empty")
            continue
        n, w = len(sentences(text)), words(text)
        if not smin <= n <= smax:
            out.append(f"{label}: {n} sentences (allowed {smin}-{smax})")
        if not wmin <= w <= wmax:
            out.append(f"{label}: {w} words (allowed {wmin}-{wmax})")
        if terms := sorted({m.group(0).lower() for m in BANNED.finditer(text)}):
            out.append(f"{label}: internal words {terms}")
        if DASH.search(text):
            out.append(f"{label}: a dash used as punctuation; use a comma, "
                       f"colon or a new sentence")
        if key == "history" and FIRST_PERSON.search(text):
            out.append(f"{label}: written in the firm's own voice (we/our); "
                       f"write it in the third person")
        if fields is not None and (fields.get(key) or {}).get("value") != row.get(key):
            out.append(f"{label}: investor/sources.json value differs from investor.json")
    # The thesis is self-given: its source is a page on the firm's own site.
    field = (fields or {}).get("investment_concept") or {}
    if fields is not None and not field.get("derived"):
        site, src = host(row.get("website")), host(field.get("source"))
        if not site or src != site:
            out.append(f"thesis: source {field.get('source')!r} is not the firm's own "
                       f"site ({row.get('website')!r}); quote the firm, or mark the "
                       f"field derived when it publishes no statement")
    return out


def host(url: str | None) -> str:
    netloc = urlparse(url or "").netloc.lower()
    return netloc[4:] if netloc.startswith("www.") else netloc


def main() -> None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from paths import ROOT  # noqa: E402
    root = ROOT / "data" / "collection" / "investors"
    slugs = sys.argv[1:] or sorted(p.name for p in root.iterdir()
                                   if (p / "investor" / "investor.json").exists())
    bad = 0
    for slug in slugs:
        inv = root / slug / "investor"
        row = json.loads((inv / "investor.json").read_text())
        fields = json.loads((inv / "sources.json").read_text()).get("fields", {})
        found = problems(row, fields)
        t, h = row.get("investment_concept") or "", row.get("history") or ""
        print(f"{slug:24} thesis {len(sentences(t))}s/{words(t):3}w  "
              f"history {len(sentences(h))}s/{words(h):3}w  "
              f"{'ok' if not found else '; '.join(found)}")
        bad += bool(found)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
