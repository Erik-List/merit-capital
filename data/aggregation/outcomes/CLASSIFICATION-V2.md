# Classification v2 constitution

Adversarial second pass over three published columns: `valuation_usd (+asof)`,
`entry_stage`, `hq_country`. Extends ENTRY-STAGE.md and MEMBERSHIP.md; base-v2
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
adversarial pass cites country for the visible slice (`hq_country_citation`) and
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

## 3c. HQ city (added 2026-08-13, Erik)

`hq_country` alone cannot carry a geography distribution: 749 of 873 rows are
United States, so the column answers "where does Sequoia invest?" with a
single bar. `hq_city` is the column that makes the distribution readable, and
it publishes as the pair `hq_city` + `hq_country`.

**Definition.** The city of the company's headquarters — current for live
companies, last known for dead and acquired ones — and it must sit inside the
country already recorded on the row. The pair is published together, so a row
may not say Tel Aviv / United States.

**Rendering is constrained even though the vocabulary is not.** The set of
cities a portfolio touches is open, so this is free text, not a taxonomy. What
`record` enforces is the shape: the bare municipality in title case, no state
or country suffix ("Palo Alto", never "Palo Alto, CA"). Grouping is the
reader's job downstream and a suffix would fragment it.

- **Municipality, not neighbourhood or metro.** Boroughs and districts roll up
  to their city (Brooklyn and Manhattan → New York; Redwood Shores → Redwood
  City). Genuinely separate municipalities stay separate: Mountain View, Menlo
  Park, Palo Alto, South San Francisco and Santa Monica are not San Francisco
  or Los Angeles. Any metro rollup (an "SF Bay Area" bucket, matching the
  investor-side `geo` vocabulary) is derived later, from these, and cannot be
  recovered if the cities are pre-collapsed.
- **Common English exonym** where one is standard: Munich, Cologne, Vienna,
  Tel Aviv (not Tel Aviv-Yafo), Bengaluru, Mumbai.

**Evidence order.** `model_knowledge` (recognized company, known HQ) >
`formd_address` (the city on the company's own Form D) > `web_verified`.
Knowledge leads here, unlike `hq_country`, because the filing address is
entry-time and the column is current-HQ; only 151 rows carry a Form D address
at all. The address is used as the answer when the company is not recognizable
from name, sector and note — for those rows it is the best evidence that
exists — and as corroboration otherwise.

Three known defects in the Form D address, each a reason to override it:
it is entry-time (companies move: Palantir left Palo Alto, Coinbase left San
Francisco); it is sometimes counsel's, an investor's or a parent's address;
and foreign issuers routinely file a US office while operating from Tel Aviv
or Berlin. A filing city that contradicts the recorded country is therefore
the signal to override, never to record.

**No city priors.** A company that cannot be located carries `hq_city: null`
and flag `city_unknown`. Filling unidentifiable rows with "San Francisco"
because the row is US and the era is Sequoia's would manufacture exactly the
concentration the column exists to measure. Same discipline as the closed
focus taxonomy: null over force-fit.

**Confidence.** high = recognized company with a well-known HQ, or a Form D
address corroborated by knowledge. medium = recognized but the HQ may have
moved since the May-2026 cutoff, or a Form D address standing alone.
low = located only by a weak signal (a note, a sector convention).

Where city and country cannot both be true, the row is flagged
`city_country_conflict` with a note and the city is recorded truthfully, so
the country correction stays Erik's call rather than a side effect of this
pass. Six rows carry it, and all six are country defects rather than
relocations: Barracuda (Campbell, country BE), Aquarium (San Francisco,
country DE) and Avanex (Fremont, country CH) are wikidata identity errors;
Rappi (Bogotá) and Bubble Motion (Singapore) took country US from a US
subsidiary's filing address; LayerZero operates from Vancouver under a US
incorporation.

**Result of the run (2026-08-13).** One parametric pass over all 873 rows,
120 per batch, briefed with the Form D address trail and the recorded country.
**664 of 873 located (76%), 146 distinct cities.** Coverage is complete
exactly where the column publishes: **100% of the $1B+ rows** (15/15 $100B+,
38/38 $10B+, 95/95 $1B+) and 193 of 195 rows in the visible slice — the two
gaps, `pace` and `two`, are acquired era-D rows whose company identity is
itself unresolved. All 209 nulls sit in the sub-$1B tail and carry
`city_unknown`: the 2006-09 scrape strays and the era-D seed listings that
the note describes only as "early, small". Confidence splits 408 high /
181 medium / 75 low; source splits 545 model_knowledge / 119 formd_address.

What the column was built to show: **San Francisco 176, New York 54, San Jose
30, Mountain View 26, Palo Alto 25, Santa Clara 24, Sunnyvale 20, Tel Aviv 18,
Redwood City 16, Los Angeles 11.** Bay Area municipalities together account
for 384 of the 664 located rows (58%), which is the concentration `country`
was hiding behind its 749 United States rows.

Twenty-odd rows moved city since their filing address, and those moves are
where the entry-time trap would have bitten: Aurora Innovation files from Palo
Alto and Mountain View but runs from Pittsburgh; Snowflake from San Mateo but
runs from Bozeman; Block left San Francisco for Oakland, Green Dot for Austin,
Natera for Austin, Omnicell for Fort Worth, Bird for Miami, Picsart for Miami,
Appirio for Indianapolis, SpaceX for Starbase.

## 4. The two-pass structure

Applied to the **visible slice** ($1B+ or currently public): pass A defends
each recorded value (find the confirming source), pass B attacks it (search
for the newer round, the acquisition, the down round, the wrong stage, the
relocated HQ). Agreement with citation closes the row; disagreement is
arbitrated by a targeted search; what survives goes to the sampling sheet.
Elsewhere: one rigorous cited pass, sampling as the default review element.

## 5. Verify invariants (additions)

1. `is_public` and `valuation_range >= 1b_plus` implies `valuation_citation` present.
2. Non-US country on a visible row implies `hq_country_citation` or
   `formd_address`/`wikidata` provenance.
3. Standing invariants from runs 1-3 unchanged.
