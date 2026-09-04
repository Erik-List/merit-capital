# Calibration gate protocol (COLLECTION.md §4) — Creandum, 2026-09-04

Both sets pre-registered in golden.json before the first base build (golden.json `_key_registered`
timestamp precedes build-company-base.py's first run by ~10 minutes; the key was assembled from the
firm's own stories/announcements archive, the Form D sweep, the EDGAR full-text hits and twelve
targeted web checks, never from the built rows). Run after build + prepare, before ANY verdict or
classification record.

1. `run.py status` — 0 recorded agent verdicts beyond the evidence-class seeds (site_listing on every
   listed row; no fund_filing seeds exist here — the vehicles file no issuer-side forms).
2. Membership set (25): the 14 falses must have NO base row (orgio-inc, aerones-inc, creades-ab, tink,
   tio-tech-a, amorelie, delivery-hero, goviral, eniram, sap-se, uber-technologies, zynga,
   grab-holdings, bokus — checked against base.json and excluded.csv); the 11 trues must carry a
   member verdict after seeding, and their seeded basis must name the evidence the key claims
   (archive-only listings for nanoxis and soundtrack-your-brand, the 2016 Klarna purchase, the
   Football Addicts secondary, the Form D seats for vivino / safety-wing / cast-ai, the exit-side
   filings for small-giant-games / cornershop / vay).
3. Stage set (55): every candidate layer scored against the key BEFORE the grind trusts it —
   (a) the firm's own stories/announcements (a post naming the round → the label; expected class 1),
   (b) the live CMS `date` and the 2017-2023 site's data-invested year as entry-YEAR evidence (no
   stage field exists), (c) the Form D band (partner-anchored first filing; expected to fail on
   vivino, abacum, cast-ai where the first partner filing is a later round), (d) model knowledge.
   Then the blind replay row by row through the production order: the judge sees the queue item
   (evidence fields, Form D rounds, site date, partner) and the stories/announcements text for the
   row, key out of context, and records stage + source + citation; scored after.
4. Score, decompose by layer, fix the layer (never the instance), record PASS in run-log.md and post
   the milestone comment on PRO-72. Gate: zero false members at high confidence; the evidence order
   the grind will use is written down before the first batch.

Same-session caveat as every run so far: the session that wrote the key runs the pass, so honesty =
a document-anchored key (every stage row a URL naming the round and Creandum's participation) and
the blind replay reading the production evidence, not the key.
