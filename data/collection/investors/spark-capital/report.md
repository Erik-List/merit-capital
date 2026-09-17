# Spark Capital collection report

## PRO-85 — Base, outcome classification, firm profile (one merged run)

Single-session autonomous run, 2026-09-05, slot 2 of the two-session test
wave (PRO-86 Union Square Ventures ran in slot 1 on the same checkout under
§12): investor-specific decisions derived from the confirmed Phase 0, the
evidence layers, both calibration sets pre-registered and cleared, one grind
answering membership and every classification column per row (8 batches +
fixups), recall probe, the scheduled rebuild and its delta, the A/B pass on
the visible slice, the momentum slice, the standing duties, the firm profile
built once against the landed base, `verify` (plain, clean) / `export` /
`review` / this report and the playbook write-back proposal. Ingest is not
part of the run (§9).

**Ingested 2026-09-06 with Erik's approval** (icon uploaded from the site's vector
mark, investor row upserted, 325 companies upserted; `public.companies` holds 325
rows for spark-capital). Rule A (vendor marks never band a row, Erik's ruling
2026-09-06) was applied to Spark by the USV session before the ingest (Justworks
and MatX to below_1b, six rows re-cited, Capitolis re-dated).

**Prompt count: 3, final** — the kickoff ("please collect Spark capital; phase
0 is confirmed"; the "continue" after an interrupted Linear call is the same
prompt), the question on the Justworks disagreement (answered, which led to
Erik's Rule A), and the ingest approval. Checkpoint approvals requested: 0; milestone comments
posted-and-continued: 2 (kickoff facts, grind complete). The session survived
one context compaction after the grind on the disk state alone.

**Usage line:** Erik reads Settings > Usage at close — kickoff percentages
were not given for this session; the line is filled at ingest
(weekly %, Fable %, base rows 325).

### 1. The method delta — a winners' selection with a deep archive

Spark's live site lists **45 selected companies** (the issue expected ~120:
the 124 Webflow cards repeat across six tabs). The base therefore rests on
the archive: eleven Wayback eras (2006 static HTML → ExpressionEngine →
two WordPress generations → a B12 interim site → Webflow 2020–2026), each
with its own parser, plus the Webflow archive cards 2021–2026 whose exit
markers ("Acquired by …", "IPO") corroborate status. The 2015–2020 WordPress
cards carry sector / geo / stage classes: the gate scored the `seed` and
`growth` classes as corroboration (5/5, 8/8) and `venture` as no stage
claim (ruling 13).

EDGAR reaches the public winners through 38 own vehicles (Forms 3/4/13G on
Braze, CNET, Flywire, SmartRent, Sonder, Talkspace, Twitter, Wayfair, Mandalay
Digital) and the long tail through the roster-name Form D sweep (52 names,
440 accessions, 246 issuers), judged cluster-first around the homonym
clusters (Benjamin Simon, Dennis Miller, Andrew Parker, Rob Go, Haber,
Clayton). Start@Spark (2009) was verified on the archived news page and
ruled IN as fund money (D4). The firm's own news archive 2006–2016 named the
entry round on a quarter of the golden rows and served as class-1 citation.

Recall: EDGAR full-text (Teamshares 13G, Securitize S-1 selling stockholder),
Wikipedia insource (Dispo, Pray.com) and a press sweep (Underdog, Cardless,
Anrok, Antithesis, West Co, Kinnu, Roi) added 11 rows — 3% of the base —
which is what a firm whose archive listed everything for fifteen years
leaves for recall.

### 2. Result

**325 published rows** — Tier A 261 / B 47 / C 17 — 332 ledger
members and 4 `uncertain` (identity unresolved: Kepler Software, Lulo
Ventures, Postabon, STTG); **46 rows in `excluded.json`** (not_member 45 · build_filter 1).
Ledger 381 verdicts (member 332 · not_member 45 · uncertain 4); member evidence classes: site_listing 315 · web 9 · formd_adjudicated 6 · fund_filing 2.
Identity: 45 merge groups, 2 never-merge pairs (Medallion /
Medallion Resources, Cover / Cover Genius), 1 rejected merge.

| column | distribution |
|---|---|
| status | private 172 · acquired 79 · unknown 34 · defunct 21 · public 17 |
| valuation_range | below_1b 259 · 1b_plus 51 · 10b_plus 14 · 100b_plus 1 — all 66 $1B+ rows web-cited (65) |
| entry_stage | Seed 62 · Series A 146 · Growth 110 |
| focus | Consumer & Marketplaces 74 · Fintech & Payments 52 · Media, Gaming & Advertising 44 · SaaS 30 · AI & Applied AI 25 · Healthcare & Bio 22 · Industrial & Robotics 22 · Data Infrastructure 16 · Security 9 · Crypto & Web3 9 · DevTools & APIs 9 · Climate & Energy 2 |
| hq_country | US 283 · GB 8 · DE 7 · CA 6 · IL 4 · ES 3 · FR 2 · BR 2 · NO 2 · CY 1 · NL 1 · TR 1 · AU 1 · IE 1 |

Largest marks: anthropic $965.0B, coinbase $48.7B, ramp $44.0B, crusoe $30.0B, affirm $24.4B, kalshi $22.0B, deel $17.3B, rapyd $15.0B, discord $15.0B, scale-ai $14.8B, wayfair $13.6B, grammarly $13.0B.
Public rows (17): market caps as of 2026-09-04 from companiesmarketcap /
stockanalysis (Coinbase $48.7B, Affirm $24.4B, Wayfair $13.6B, JFrog $10.8B,
Snap $9.3B …); 1stDibs, SmartRent and Talkspace stay on the SEC float
(below_1b).

### 3. Calibration gate and corrections taken

Registered 2026-09-05 16:25 before the build: 44 stage keys (web-verified,
incl. the issue's corrections — Plaid Seed 2013, Cruise Series A 2015,
Coinbase/Discord/Ramp/Marqeta/Kalshi/Glossier/Warby Parker late Growth) and
26 membership keys (11 true, 15 traps). Blind pass 44/44 with six pack-only
divergences where the first filed round would have been taken for the entry
(Carta, Flywire, Lightmatter, Abridge, eToro, AdMeld) — the §6 ceiling rule
applied throughout. Layer scores in `golden.json` `_layer_scores`.

Corrections after the grind: three deterministic homonym floats quarantined
(CoStar Group, Oculus CIK 1107280, Post Holdings); Nomad's entry moved to
2022 (ruling 20); Perch and The Bot Company re-keyed Series A under the
label rule (ruling 15); 14 momentum rows had their entry year corrected
where the listing year was not the round year.

### 4. Standing duties and the A/B pass

- **A/B pass** — 13 public caps and 53 private pins; every $1B+ row carries a
  figure and a citation. Band moves: 9fin up (Series C at $1.3B, Mar 2026),
  Parallel up ($2B, Apr 2026), Sift down (2026 secondary marks, ruling 16);
  Chronosphere (Palo Alto Networks), Niantic (Scopely), Perch (Razor Group),
  Clyde (Cover Genius), Cimulate (Salesforce), Producer (Google) → `acquired`;
  Teamshares below_1b on its $454M cap. 22 rows keep `stale` with the
  last priced mark named.
- **Momentum slice** — 40 rows (entries 2023+ in hot sectors) each got one
  web check recorded as a `web_verified` band with the announcement as
  citation.
- **Weak-CIK audit** — clean after the grind's three quarantines; 3 `cik_weak`
  rows flagged.
- **Stale-float sweep** — no public row on a float older than 2025-06.
- **Unicorn re-intersection** — 8 name matches on below_1b rows, all
  acquired/defunct/former (Kik, Niantic, Postmates, Slack, SmileDirectClub,
  Sonder, Twitter) or documented (Sift).
- **5% blind self-consistency** — 16 rows (seed 85), no correction needed.
- **City/country coherence** — 9 fixes (flags vs filled cities; Securitize
  Miami, Teamshares New York, Sonder San Francisco).

### 5. Findings Erik should know about

1. **At-scale first rounds** (ruling 15): Antithesis ($105M "Series A"), The
   Bot Company ($150M "Series A") and Perch are keyed Series A by label;
   Wayfair, Harmonix and IPWireless stay Growth as growth equity into mature
   companies. Say if the size should govern instead — three rows move.
2. **Two down-rulings on stale marks** (ruling 16): Sift to below_1b on
   secondary marks; MatX carries a $1.0B floor against a stated "several
   billion".
3. **Justworks** is an accepted cross-investor disagreement (Spark 1b_plus on
   aggregator marks, Thrive below_1b without a figure) — your band call.
4. **West Co = Workshop for Emotional & Spiritual Technology Corp** (ruling
   19); the merge waits for the next rebuild, the corp row is flagged
   `duplicate`.
5. **Spark IX ($1.0B) and Growth Fund VI ($2.33B) closed in 2026** — the
   profile's AUM ($15.57B, ADV 7.B) predates them; the history names them.
6. **Two site-listed non-members** (ruling 14): CNET (2008 activist public
   stake) and Mandalay Media (Twistbox consideration), plus KIT digital and
   Mandalay Digital on the same rule.

### 6. The C2A sentence

Of 65 seed entries, 39 are in the graduation cohort (the rest are
censored or undetermined); **21 graduated to a priced A (53.8%)** — Spark's
seeds are mostly first checks into companies that then raised from the
firm's own A-stage funds (Plaid, Mark43, Pray.com, Midas, Vinyl Equity), and
the misses are 2010–2013 consumer seeds that never priced an A.

### 7. Debt, all flagged in rows

stage_uncited 91 · stage_disputes_band 39 · model_disputes_source 28 · cohort_unverified 28 · cite_pending 24 · stale 22 · city_unknown 20 · country_prior 12 · censored 9 · duplicate 7 · identity_uncertain 5 · cik_weak 3 · graduation_disagree 1.
`stage_uncited` is concentrated in 2006–2014 archive rows whose only
stage evidence is the site class or the Form D band; `cite_pending` marks
$1B+ rows whose entry round is not yet named (Snap, Securitize, Generalist,
Capitolis-era alignments). Rebuild debt in `scratch/rebuild-queue.md`: the
West Co merge.

### 8. Firm profile

`investor.json` / `investor.sources.json` built by `build-firm-profile.py`
against the landed base: HQ Boston, MA (30/30 own filings); founded 2005;
15 funds (sizes from the closing Form Ds where filed — III, IV, Growth I–III,
VI, IX, Growth VI — press for the $0-sold first filings); AUM
$15,574,226,934 (ADV 7.B gross asset value, FY2025, bottom = top for an
exempt reporting adviser); 23 team members with titles from the Webflow
person pages (3 departed roster names); focus recomputed from the site tags
(SaaS, Consumer & Marketplaces, Industrial & Robotics, Fintech & Payments, Media, Gaming & Advertising, AI & Applied AI); investment range $1M / $10M
median / $1.1B (Form D rounds on members, upper = Baseten's Series F);
notable investments Twitter, Slack, Oculus, Discord, Coinbase, Anthropic,
Affirm, Wayfair (all ledger members). **Icon**: the site's own vector mark
(Spark dog, `Spark_Dog_Logo_R3.5.svg`) found with `--discover`, dry-run
rendered to `scratch/icon-dry.png` (master 256px, plate synthesized,
contrast 16.6:1, ramp 0.87px); the upload runs with the ingest approval and
replaces `icon_url`.

### 9. Cross-investor alignment

101 shared rows: 98 agree, 3 accepted (InVision vs Accel, Justworks vs
Thrive, Catalyst vs Accel), 0 disagree; 9 distinct rulings in
`cross-rulings.json`. Aligned this run: Careship → acquired (Creandum),
Sesame → 1b_plus $1.0B (a16z, Sequoia), Plaid/Mercury/Capitolis figures
matched to the siblings. USV (slot 1) was in flight and not compared.

### 10. Driver and playbook changes (write-back proposal, not committed)

1. **Judge the twins before the scheduled rebuild.** The exclusion-before-
   overlay order (§8) means a `not_member` canonical resurrects its merge
   twins after the rebuild; this run paid a second, retire-only rebuild
   (328 → 325, no other change). Proposed text for §8: "before the scheduled
   rebuild, list every merge group whose canonical is `not_member` and record
   a verdict for each duplicate slug; the rebuild then retires them all."
2. **Momentum slice is now a named step** (§8 duties): entries 2023+ in hot
   sectors get one web check recorded as `valuation_range_source:
   web_verified` with the announcement as citation; 40 rows here.
3. **Aggregator figures.** When no primary figure exists for a 1b_plus band,
   record the aggregator mark with `valuation_confidence: low` and name it a
   floor in the note (MatX); never leave `needs_web_value` into verify.
4. **Team pages behind SSL-pinned hosts**: python `urllib` failed on the
   Webflow host (local certificate chain), `curl` did not — note for the
   `site_api` team sources.
5. **`verify` exits 0 with problems.** A shell chain gated on `&&` ran export,
   review, close and the first commit past a two-problem verify (Bond Street's
   cohort row); the fix landed in a second commit. Either return non-zero on
   problems or document that chains must grep `verify: clean`.
6. **Wayback era parsers**: eleven eras with disjoint year ranges is the
   most any run has needed; the `listing_regex` era with `_id` (`wp2018`)
   pattern is reusable for WordPress "menu" themes.

### 11. Open rulings (§9 triggers, raised once)

- Ruling 15 (label vs scale), ruling 16 (Sift down, MatX floor), the Justworks
  and Catalyst accepted pairs, the Sesame $1.0B alignment on a weak figure.
- The 4 `uncertain` rows (Kepler Software 2026 $36M round with Natalie Vais
  as director; Lulo Ventures 2011; Postabon 2010; STTG 2010) and `whele-llc`
  stay out of the member count until identity resolves.

### 12. Environment

IA replay flaky all afternoon (HTTP 000 / rc 7 / rc 61); wayback-pull run
three times on cached raws; CDX with retry/backoff (5 attempts, shared
throttle). Common Crawl one puller. No `timeout` on macOS; sleep-chains
blocked (background tasks used). Shell cwd drift once (fixed with absolute
paths). `record` merges per key — the A/B pass emitted only the keys asked.
Second rebuild logged in `scratch/run-log.md`.

### 13. Artifacts

`base.json` / `base.csv` (325 rows), `excluded.json` (46), `review.html`
(shared server http://localhost:8931/spark-capital/review.html),
`classification.json`, `membership-ledger.json` (ledger + 11 recall
additions), `golden.json`, `identity-merges.json`, `cross-rulings.json`,
`investor.json`, `investor.sources.json`, `decisions.md` (D1–D12, rulings
13–20), `config.json`; `sources/` (site, wayback, edgar incl.
`fund-formds.json`, web); `scratch/` (queue, judgments-*.py, A/B and
momentum records, run-log, rebuild-queue, team pages, icon dry run).

Generated 2026-09-05T21:53+00:00.

## Addendum 2026-09-06 — Rule A applied (Erik's ruling, uniform for USV, Spark and every further investor)

Vendor valuations (PitchBook, CB Insights, Sacra, GetLatka, Caplight, PremierAlts and the like) never band a row; a `1b_plus` band needs a priced round, tender or float with a citable figure, and vendor figures go to the note. Applied post-close from the USV session (`scratch/queue/rule-a.out.jsonl`, recorded through `run.py record`; export, review and verify re-run, clean):

- **Re-cited, band and figure unchanged** (the mark is a priced round; the vendor page was only the citation): Ada $1.2B (Series C, May 2021, company announcement), Benchling $6.1B (Series F, 2021-11-18, company release), Noom $3.7B (Series F, 2021-05-25, TechCrunch), Outreach $4.4B (Series G, June 2021, company release), Stoke Space ~$2B (press-reported Series D mark, as-of moved to the October-2025 close; the reported $9B Series E stays in the note until confirmed).
- **Re-dated**: Capitolis $1.6B is the priced Series D of 2022-03-22 (TechCrunch); the 2025 SAFEs disclosed no valuation, so the row is `stale` again.
- **Re-banded below_1b, figure to the note**: Justworks (vendor estimates only; now aligned with USV and Thrive, the accepted pair withdrawn), MatX (the company says "several billion" without a figure; Caplight's $1.0B was an estimate).
- **Figure to the note, band unchanged**: Enfabrica (PitchBook's $445–560M estimate).

Open ruling 3 ("Aggregator figures") and the Justworks item in §7 are resolved by this rule.
