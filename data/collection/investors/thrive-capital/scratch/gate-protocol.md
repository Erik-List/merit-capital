# Calibration gate protocol (COLLECTION.md §4) — Thrive, 2026-09-03

Both sets pre-registered in golden.json before the first build (commit order: golden.json
written 16:4x, build-company-base.py first run 16:5x). Run after build + prepare + seed, before
ANY verdict or classification record.

1. `run.py status` — 0 recorded agent verdicts beyond the 108 evidence-class seeds (106 board
   listings + 2 fund_filing).
2. Membership set (30): structural falses (13F-only Amazon/Shopify, Thrive Holdings' Current and
   Shield, the Giants, five namesake filers, Trolley) must have NO base row; judged rows in the
   base (rakuten-medical-inc, 3play-media-inc, piedmont-stone-center-pllc, chrono-inc = falses;
   justin-tv-inc = true) get blind verdicts through decisions.md + COLLECTION.md §1-3, cluster-first
   (the person, the seat, the date, the issuer's address); seeded trues are checked for the
   evidence the seed claims. Press-only trues (instagram, warby-parker, github, slack) are not
   buildable from any layer and are the recall probe's test rows.
3. Stage set (35): every candidate layer scored against the key BEFORE the grind trusts it —
   the Form D band (graduation layer 1, partner-anchored), the job board's Getro `stage` field
   (a current-stage label, mapped Series B+ -> Growth), and the press/announcement layer; then the
   blind replay row by row through the production order. Same-session caveat as Accel/Lightspeed:
   the session that wrote the key runs the pass, so honesty = document-anchored key (every row a
   URL naming the round and Thrive's participation, or a fund vehicle / Form D seat) registered
   pre-build; the pass verifies that the production evidence order reproduces the documents.
4. Score, decompose by layer, fix the layer (never the instance), record PASS in run-log.md and
   the milestone comment on PRO-64. Gate: zero false members at high confidence; the evidence
   order the grind will use is written down before the first batch.
