# Classification v2 constitution

Adversarial second pass over three published columns: `valuation_usd (+asof)`,
`entry_stage`, `country`. Extends ENTRY-STAGE.md and MEMBERSHIP.md; base-v2
rigor applied column-wise. Erik's rulings, 2026-08-13:

## 1. Valuation

- **Public companies: market capitalization is canonical**, web-cited with an
  as-of date (`valuation_source: web_verified`, `valuation_citation` URL).
  SEC public float remains corroborating evidence only; a public $1B+ row
  without a cited cap FAILS verify.
- **Private companies**: last credible primary-round mark stays canonical
  (run-2 policy), `stale` flag beyond 24 months. Secondary-market estimates
  are recorded in the note, never as `valuation_usd`. The attack pass searches
  stale marks for newer rounds, down rounds, and exits.
- **below_1b rule-outs**: web-checked only on a signal (past unicorn mark,
  mega-raise, hot sector, recent momentum); otherwise validated by a blind
  stratified re-judge sample. Absence claims are not citeable at scale.

## 2. Entry stage

ENTRY-STAGE.md governs. Citation attempted for every row in priority order
($1B+ incl. IPO, then recents, then the tail); `stage_uncited` marks attempted
failures. C2A cohort keeps model-medium rows flagged `cohort_unverified`.

## 3. Country

Entry-time-first hierarchy stands (formd_address > wikidata > model). The
adversarial pass cites country for the visible slice (`country_citation`) and
for every non-US claim (the map's interesting rows); the US mass is validated
by the same blind sample.

## 3b. Focus (added 2026-08-13, Erik)

`focus` is a **single primary value from the closed seven** in
`data/taxonomy/focus.json` (the vocabulary the frontend and DB already use),
so the distribution sums cleanly. One parametric classification run over all
873 rows, web search only where the company was unidentifiable from name,
sector tags and the accumulated note; no adversarial second pass, because a
sector label is not a claim that publishes a number.

Rules used, recorded here so the next run is consistent rather than
re-derived:

- The taxonomy is **closed**. A company that fits none of the seven carries
  `focus: null`, reported as "outside taxonomy". Force-fitting into a
  near-miss bucket would corrupt the distribution it exists to produce.
- Judgment over the alias table where they disagree. `hardware` aliases to
  Industrial & Robotics, but **consumer** devices (Apple, Atari, Jawbone) are
  outside the taxonomy while semis, robotics, defense and manufacturing are
  Industrial & Robotics.
- Enterprise **infrastructure and networking** (Cisco, Aruba, Confluent,
  MongoDB, Cohesity) is Data Infrastructure, following the taxonomy's own
  `infrastructure` alias. Chips are Industrial & Robotics.
- **Security** has no value of its own: enterprise security *software* is
  SaaS (Wiz, Palo Alto, Armis, Cyera), security *tooling for developers* is
  DevTools & APIs (Chainguard, Oso), security *hardware* is Industrial.
- **AI & Applied AI** means AI is the product (labs, model providers, AI-native
  applications), not that the company uses ML internally.
- Adtech/media networks, marketplaces, consumer social, gaming, healthcare and
  biotech are **outside the taxonomy**, by design of the seven.

**Taxonomy expanded 2026-08-13 (Erik), seven values to twelve.** The original
seven were enterprise/infra-centric and left a third of a real portfolio
unclassifiable. Added: `Consumer & Marketplaces`, `Healthcare & Bio`,
`Media, Gaming & Advertising`, `Crypto & Web3`, `Security`. The first four
close coverage gaps; Security does not (those rows were already classified)
but corrects a distortion, since security software had been spread across
SaaS, DevTools and Industrial and inflated SaaS.

Every row was re-judged against the twelve, not mechanically remapped.
Result: **821 of 873 classified (94.0%), 52 outside (6.0%)**, of which 47 are
the permanently unidentifiable floor (2006-09 scrape strays with no trace).
Real residual ambiguity is therefore 5 rows.

Rules added with the new values:

- **Consumer & Marketplaces** covers consumer internet, marketplaces, commerce,
  social, travel and consumer devices (Apple, Jawbone), which previously fell
  outside because `hardware` aliased to Industrial.
- **Healthcare & Bio** is the whole vertical: care delivery, diagnostics,
  devices, therapeutics, health IT. Healthcare vertical SaaS goes here, not SaaS.
- **Media, Gaming & Advertising** includes ad networks and audience
  monetization (AdMob, AdBrite, Amobee, Chartboost). Martech sold to businesses
  as software stays SaaS (Attentive, Hearsay); ad *networks* are media.
- **Crypto & Web3** takes precedence over Fintech for on-chain businesses
  (Fireblocks, Phantom, FTX, LayerZero, StarkWare); Robinhood stays Fintech
  because crypto is a product line, not the business.
- **Security** takes precedence over SaaS/DevTools/Industrial whenever security
  is what the company sells (Wiz, Palo Alto, Okta, Symantec, Verkada,
  Chainguard). Security *for developers* still resolves here, not DevTools.

Distribution in `track-record-proposal.json` under `by_focus`, with a $1B+
breakdown so the reader can see which areas produced winners.

**Downstream, not yet done:** `investors.investment_scope.focus` in the DB and
the leaderboard filter still hold the original seven. The five new values need
a migration plus a frontend filter update before investor-side focus is
re-derived; tracked separately.

## 4. The two-pass structure

Applied to the **visible slice** ($1B+ or currently public): pass A defends
each recorded value (find the confirming source), pass B attacks it (search
for the newer round, the acquisition, the down round, the wrong stage, the
relocated HQ). Agreement with citation closes the row; disagreement is
arbitrated by a targeted search; what survives goes to the sampling sheet.
Elsewhere: one rigorous cited pass, sampling as the default review element.

## 5. Verify invariants (additions)

1. `is_public` and `value_tag >= 1b_plus` implies `valuation_citation` present.
2. Non-US country on a visible row implies `country_citation` or
   `formd_address`/`wikidata` provenance.
3. Standing invariants from runs 1-3 unchanged.
