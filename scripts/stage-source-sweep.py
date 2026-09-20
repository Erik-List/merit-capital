"""Source every weakly-staged row from what its own note says, or write
`undetermined`.

PRO-135 items 2 and 3: a stage with an empty `entry_stage_source` has no
provenance at all, and a stage carrying `stage_prior` has provenance that Erik
has deleted — the firm's classic round is a fact about the firm, and 833 rows
published it as a fact about a company, 817 of them at `low` confidence with a
note that says so outright ("unidentifiable stray: the firm's classic entry
stage as prior").

The value came from somewhere, and the row's note is where the pass that wrote
it said so, so the note decides between the two honest endings:

  * the note NAMES the company's round — a round word pinned to one transaction
    by an amount or a date ("the $193M Series A of 2023", "Ahana's $2.25M seed
    of 2020-06-02") — and the row takes `model`, which is rung 3 of the
    evidence order and exactly what this is.
  * the note names no round, or says outright that none could be found ("entry
    round not documented on any Lux surface", "no round announcement naming Lux
    could be retrieved", "pre-window entry so entry_stage is null by policy") —
    and the row reads `undetermined`. There is nothing left to source, and
    PRO-137 has since removed the date policy the third phrasing rested on.

An absence phrase OUTRANKS a round word in the same note: a note that says no
round could be retrieved and mentions "Series A" in passing is saying the round
is unknown.

A `stage_prior` row that turns out to carry REAL evidence — its own Form D
sequence, or a `web_verified` citation — keeps everything and only loses the
flag, which was stale.

Usage: python3 scripts/stage-source-sweep.py <investor> [--apply]
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import Paths
from stage_words import round_word

ap = argparse.ArgumentParser()
ap.add_argument("investor"); ap.add_argument("--apply", action="store_true")
a = ap.parse_args()
P = Paths(a.investor)
cls = json.loads(P.classification.read_text())
base = {r["slug"] for r in json.loads(P.base_json.read_text())}
led = json.loads(P.ledger.read_text()) if P.ledger.exists() else {}
nm = {s for b in led.values() for s, v in ((b or {}).get("verdicts") or {}).items()
      if (v or {}).get("verdict") == "not_member"}

ROUND = re.compile(r"\b(series\s+[a-h]\b|pre-?seed\b|seed\b)", re.I)
PINNED = re.compile(r"(\$[\d.]+\s*[MBmb]\b|€[\d.]+\s*[MBmb]\b|\b(?:19|20)\d\d\b)")
# `Growth` is the one stage a note can establish WITHOUT a round word, because
# it is the whole of the ladder from Series B up: a note that places the entry
# after the company's earlier rounds has said Growth, whatever the round was
# called ("Lux entered in 2020 at a later round, not at formation"; "a decade
# after founding and at one of the late private rounds"). The same sentence
# would not establish Seed or Series A, which is why this is gated on the value.
LATE = re.compile(
    r"(later\s+round|late[\s-]stage|late\s+private\s+round|growth\s+round"
    r"|after\s+the\s+\w+\s+rounds?|long\s+after\s+the\s+early|well\s+after\s+the"
    r"|decade\s+after\s+founding|postdates\s+the\s+early|at\s+scale"
    r"|very\s+large\s+first\s+round|not\s+at\s+formation|secondary|tender)", re.I)
ABSENT = re.compile(
    r"(no\s+(?:\w+\s+){0,3}round\b|round\s+not\s+documented|not\s+documented"
    r"|could\s+not\s+be\s+(?:retrieved|found|established)|no\s+announcement"
    r"|null\s+by\s+policy|undocumented|unknown\s+round|no\s+priced\s+round)", re.I)

# A row with NO stage at all is not a re-sourcing question: the value has to be
# read out of the evidence, and a note that mentions two rounds does not say
# which was the entry. Those go to the judge, listed with their notes.
# A row whose own Form D sequence gives the same stage is rung 2, not rung 3:
# the accessions are the citation and the band is not the model's opinion.
band = {}
_res = json.loads(P.resolved.read_text()) if P.resolved.exists() else {}
_g = json.loads(P.graduation.read_text()) if P.graduation.exists() else {}
for _s in cls:
    _b = (_res.get(_s) or {}).get("entry_stage")
    if not _b and isinstance(_g.get(_s), dict):
        _b = _g[_s].get("entry_stage")
    if _b:
        band[_s] = _b

named, vague, unstaged, structural, stale_flag, disputed = [], [], [], [], [], []
for s, r in sorted(cls.items()):
    if s not in base or s in nm:
        continue
    # The row as it PUBLISHES: a deterministic fill in resolved.json is a real
    # answer, and `prepare` fills the Form D band there rather than in
    # classification.json.
    view = {**((_res.get(s)) or {}), **{k: v for k, v in r.items() if v is not None}}
    st = view.get("entry_stage")
    prior = "stage_prior" in (view.get("flags") or [])
    if st == "undetermined":
        if prior:
            stale_flag.append(s)   # the value is already gone; retire the flag
        continue
    if st is not None and view.get("entry_stage_source") and not prior:
        continue
    # A `stage_prior` row whose stage actually rests on its own filings or on a
    # cited page was never an inferred fill: the flag is stale and nothing else
    # about the row moves.
    if prior and (view.get("entry_stage_source") in ("formd_structural", "formd_band",
                                                     "program_terms", "first_party")
                  or (view.get("entry_stage_source") == "web_verified"
                      and (view.get("entry_stage_citation") or "").strip())):
        stale_flag.append(s)
        continue
    note = r.get("note") or ""
    if st is None:
        unstaged.append(s)
        continue
    if band.get(s) == st:
        structural.append(s)
        continue
    ok = False
    note_rounds = set()
    if st == "Growth" and LATE.search(note):
        ok = True
    elif not ABSENT.search(note):
        for m in ROUND.finditer(note):
            if PINNED.search(note[max(0, m.start() - 60):m.end() + 60]):
                note_rounds.add(round_word(m.group(0)))
    if note_rounds:
        # **A note that names a round the row does not carry is a CORRECTION, not
        # a source.** Lightspeed's `substrate` reads Growth off a name collision
        # with an unrelated chip startup, and its own note ends "raised only an
        # $8M seed (Lightspeed-led, June 2024)". Auto-writing `model` there would
        # have re-published the wrong stage with a source attached to it, which
        # is worse than the unsourced version. Agreement lands; disagreement goes
        # to the judge with both readings.
        if st in note_rounds:
            ok = True
        else:
            disputed.append((s, st, sorted(note_rounds)))
            continue
    (named if ok else vague).append(s)

print(f"{a.investor}: {len(structural)} -> formd_band (its own filings agree); "
      f"{len(named)} rows whose note names the round -> model; "
      f"{len(vague)} -> undetermined; {len(stale_flag)} stale stage_prior flags; "
      f"{len(unstaged) + len(disputed)} rows for the judge "
      f"({len(disputed)} where the note contradicts the stage)")
lines = []
for s in stale_flag:
    lines.append({"slug": s, "clear_flags": ["stage_prior"]})
for s in structural:
    r = cls[s]
    out = {"slug": s, "entry_stage": r["entry_stage"], "entry_stage_source": "formd_band",
           "entry_stage_confidence": r.get("entry_stage_confidence") or "medium",
           "note": f"{(r.get('note') or '').strip()} | Sourced `formd_band` (PRO-135): the "
                   f"company's own Form D sequence gives this stage, so the accessions are the "
                   f"citation and the stage never rested on the firm's habits"}
    if "stage_prior" in (r.get("flags") or []):
        out["clear_flags"] = ["stage_prior"]
    lines.append(out)
for s in named:
    r = cls[s]
    out = {"slug": s, "entry_stage": r["entry_stage"], "entry_stage_source": "model",
           "entry_stage_confidence": r.get("entry_stage_confidence") or "low",
           "note": f"{(r.get('note') or '').strip()} | Sourced `model`: the note names the "
                   f"company's own round, which is rung 3 of the evidence order (PRO-135); "
                   f"the stage does not rest on the firm's habits"}
    if "stage_prior" in (r.get("flags") or []):
        out["clear_flags"] = ["stage_prior"]
    lines.append(out)
for s in vague:
    r = cls[s]
    out = {"slug": s, "entry_stage": "undetermined", "entry_stage_confidence": "low",
           "note": f"{(r.get('note') or '').strip()} | Stage undetermined (PRO-135): the record "
                   f"does not give the round this row entered at, and nothing in the evidence "
                   f"names one, so the column says so rather than carrying "
                   f"{r.get('entry_stage')!r} on the firm's habits or on no source at all"}
    # An undetermined stage is not a Seed entry, so the graduation column does
    # not apply; where a judge looked and found no round, it says undetermined too.
    if r.get("seed_to_a_graduation") is not None:
        out["seed_to_a_graduation"] = "undetermined"
    drop = [f for f in ("stage_uncited", "cite_pending", "pre_window_entry", "stage_prior",
                        "stage_disputes_band", "model_disputes_source")
            if f in (r.get("flags") or [])]
    if drop:
        out["clear_flags"] = drop
    lines.append(out)

if a.apply and lines:
    p = P.scratch / "source-or-undetermined.jsonl"
    p.write_text("".join(json.dumps(x) + "\n" for x in lines))
    print(f"  wrote {p} ({len(lines)} lines)")
    subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", a.investor, str(p)],
                   check=True)
if disputed:
    print("  the note names a round the row does not carry -- judge these:")
    for s, st, rs in disputed:
        print(f"    {s}: carries {st!r}, note names {rs} | {(cls[s].get('note') or '')[:120]}")
if unstaged:
    print("  unstaged, judge these:")
    for s in unstaged:
        r = cls[s]
        print(f"    {s} [{r.get('valuation_range')}] {(r.get('note') or '')[:150]}")
if not a.apply:
    for s in named[:4]:
        print(f"    MODEL {s}: {(cls[s].get('note') or '')[:110]}")
    for s in vague[:4]:
        print(f"    UNDET {s}: {(cls[s].get('note') or '')[:110]}")
