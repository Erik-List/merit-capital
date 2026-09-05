# Calibration gate protocol (COLLECTION.md §4) — Union Square Ventures, 2026-09-05

Both sets pre-registered in `golden.json` before the first build (key registered 20:1x, `build-company-base.py`
first run 20:3x, `prepare` 20:41). Run after build + prepare + seed, before ANY verdict or classification
record.

1. `run.py status`: 0 recorded agent verdicts beyond the 223 evidence-class seeds (site_listing; no
   fund_filing seed because every ownership-filing subject is also site-listed).
2. Membership set (30). Structural falses must have NO base row: the namesake filers (Union Square
   Advisors, Park Partners, Partners/Capital Z, Hospitality) — none built (registry desk `external`);
   Anchor and Vanta — none built (no roster-name filing survived the build's filters). Judged rows in
   the base get blind verdicts through decisions.md + COLLECTION.md §1–3, cluster-first: the eight
   site-listed falses seeded `member` by evidence class (six crypto funds, Tucows, Marley Spoon) and the
   person-level traps that the sweep pulled in under their legal names (GroupMe = Mindless Dribble Inc.,
   Hecht 2011; Mignano's Lightspeed-era seats: Granola, Magical Tome, Novoscribe 2023–2024). Seeded trues
   (14) are checked for the evidence the seed claims (a listing year on the firm's own surface).
3. Stage set (53), every candidate layer scored against the key BEFORE the grind trusts it:
   - the live site's "FIRST INVESTMENT" label (2026): **51 agree / 1 disagree / 1 no label** of 53
     → class 1 where present (the Zemanta row is the firm contradicting its own 2008 post; the 13
     bare-year rows are the layer's silence, not its error);
   - the archived per-card labels 2013–2015 (`usv:investment_series`) and 2016–2019 (card meta):
     **87 agree / 2 disagree** (Zemanta in both eras) → class 1, and stable across 13 years;
   - the Form D band (graduation layer 1, partner-anchored): **8 agree / 17 disagree / 28 no band**
     → a ceiling, never a label (Twitter's $5M Series A reads Growth; Twilio's, Stack Overflow's and
     MongoDB's Series A read Seed; Return Path's Series E reads Seed);
   - the firm's own announcement post naming the round (class 1 by construction: the key is built from
     it) and press on the visible rows: the blind replay below checks that the production evidence
     order reproduces the documents.
   Evidence order for the grind: (1) the firm's post naming the round / press = `web_verified` with
   citation; (2) the site label (live, or archived where the row left the list) = `web_verified` cited
   to the list page, medium confidence, unless a document contradicts it (`stage_disputes_band` + note);
   (3) `formd_structural` only where ≥2 prior filings make the position unambiguous; (4) `model` low.
4. Score, decompose by layer, fix the layer (never the instance), record PASS in run-log.md and the
   milestone comment on PRO-86. Gate: zero false members at high confidence; the evidence order the
   grind will use is written down before the first batch.

Same-session caveat as every run: the session that wrote the key runs the pass, so honesty = a
document-anchored key (every stage row a URL naming the round and the firm's participation) registered
pre-build, and a membership set whose falses are structural classes rather than rows the judge picked.
