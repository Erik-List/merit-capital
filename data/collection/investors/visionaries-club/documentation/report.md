# Visionaries Club: Build & Reconciliation Report (PRO-103)

Run of 2026-09-30, one session, slug `visionaries-club`. Archetype B (European early stage), sub-issue of PRO-87.

## 1. The answer PRO-103 asked for

Visionaries Club is collected: **76 companies**, plain `verify` clean with only flagged debt, the firm profile
through the taxonomy gate, `review.html` rendered and checked in a browser. **S2A 53.8%** (7 of a 13-row
cohort whose seed entries run from February 2021 to February 2025). **7 companies at $1B or more.** The ingest
ran through the §9 gate at the end of the run; section 15 records what was written.

The four deltas of the issue, in one line each:

- **Youngest firm, short archive, small base**: confirmed. The firm's own site exists from mid-2020 (the domain
  was a Japanese Toastmasters club's before, D7); the base is 76 rows, 65 of them private, 7 acquired, 3 defunct,
  1 unknown. The thin exit record is the vintage, not missing evidence.
- **The S2A cohort may be too young**: measured. 18 seed entries, 5 still inside the 24-month window (2024-12 to
  2026-05), cohort 13 with entries from 2021-02 to 2025-02. Published with that range; the rate is a small-sample
  figure (7 of 13) and says so.
- **The LP base is a T2 trap**: held. 22 LP and prior-firm companies (Adyen, UiPath, Supercell, Hugging Face,
  Stihl, Siemens, Deel, Groq, Parloa and others) are membership traps in `config.verify.not_members`; none is a row.
- **Multiple sleeves under T1**: verified by registration. One exempt reporting adviser (CRD 317147) reports all
  eleven vehicles: Seed I and II, Growth I and II (with feeders), Late Growth I to IV and Tomorrow Fund I (D1 to D3).

## 2. Results

| | |
| -- | -- |
| Rows | 76 (68 on the firm's live pages, 4 from the 2023-25 WordPress archive only, 6 recall additions) |
| Verdicts | 78: 77 member (76 rows plus Uify, merged into turian) and 1 not_member (Personio, R1) |
| Evidence | site_listing 71, fund_filing 3 (German shareholder lists), web 3 (press) |
| Status | private 65, acquired 7 (Arculus, Localyze, Pledge, Quantive, Yokoy, Accountable, Rows), defunct 3 (Acapela, Fina, Trana), unknown 1 (Tactic) |
| $1B+ | 7: Lovable ($13.3B), n8n ($5.2B), Black Forest Labs ($3.25B), Proxima Fusion ($2.74B), Miro ($1.79B, Bending Spoons deal signed, unclosed), Choco ($1.2B, 2022, stale), Pigment ($1.0B, 2024, stale) |
| Entry stage | Seed 18, Pre-Seed 12, Growth 11, Series A 10; 25 nameable rows undetermined; 0 unnameable |
| Focus | AI & Applied AI 22, SaaS 18, Fintech & Payments 12, Industrial & Robotics 10, Climate & Energy 7, Healthcare & Bio 3, DevTools & APIs 2, Consumer & Marketplaces 1, Security 1 |
| Country | DE 30, GB 19, US 9, FR 4, CH 3, ES 3, NL 2, SE 2, BE 2, NO 1, HU 1 |
| City | 76 of 76 filled, 26 distinct; London 17, Berlin 15, Munich 8 |
| Rule 10 | 74 rows shared with other books; 71 agree, 3 accepted as stale on the other side (section 15), 0 disagree; namesakes ruled distinct: Lux's Tactic, 20VC's Cycle |

### S2A block

18 seed entries, 5 censored (Autarc, Arago, Level Nine, Pave Space, CodeWords), cohort 13, **7 graduated, 6 not
graduated, rate 53.8%**, entries 2021-02 to 2025-02. The six nos rest on the absence test (the firm's surfaces, a
Form D search for the two US-linked companies, and at least two publisher surfaces, as of 2026-09-30), none on a
cited end or on the filings. Graduated: Two, Pledge, Cycle, Apron, Adfin, SirenOpt (on the unnamed-round test:
its 2026-09 Form D sold $19.43M, 2.0x its seed filing), Lovable. Not graduated: CourtCorrect, Qonversion, Tactic,
Secjur, Cosmic Aerospace, H Company. Twelve pre-seed entries (a third of the staged rows, most of them the
Tomorrow fund's and the 2025-26 seed fund's) sit outside the cohort by rule.

`defunct` is undercounted by construction (§6): quiet shutdowns present as `private` or `unknown`, and the German
register status pass was blocked (section 6), so no mortality rate may be read off the status column.

## 3. Calibration against Cherry and Creandum

A smaller, younger, winner-weighted base: 76 rows against Cherry's 148 and Creandum's 177, from a firm six years
old. The $1B+ share is 9.2% (7 of 76), between Cherry (5.4%) and Creandum (11.9%): the growth fund's late entries
(Miro, n8n, Black Forest Labs) carry it, not the seed book. 25 rows (33%) read `undetermined` for the entry round,
the highest share of the archetype-B books: the firm publishes no round, year or fund per company on any surface it
ever ran, so every stage rests on outside press, and the growth-fund's quieter entries (Miro, Pigment, incident.io,
Causaly, Langdock) were never announced.

## 4. Coverage per evidence regime

| Layer | What it gave | Notes |
| -- | -- | -- |
| Live visionaries.vc (Kirby single page) | 59 companies with the firm's claim, description and thesis; no year, stage or fund | `scratch/site-live.py` |
| Live tomorrow.vc (Visionaries Tomorrow) | 10 companies | `scratch/site-tomorrow.py`; older captures render only the carousel's first slide |
| WordPress /portfolio/ 2023-2025 | 32, 38 and 44 companies per year; 4 names since dropped (Tactic, Uify, Sustained, Loxo) | Common Crawl only; the Internet Archive blocked this machine twice |
| Gatsby site 2020-2022 | no portfolio list at all | the page-component bundle (fetched from the Internet Archive at 14:42) carries the manifesto and a "See portfolio" button linking to the firm's Crunchbase page |
| EDGAR | 3 own Form Ds (2021); one portfolio Form D (Zigguratum, 2026, Marton Sarkadi Nagy a director) once compound surnames were matched; full-text search: 3 own hits, no exit-side filing | the shared sweep keys on the last surname token and missed "Sarkadi Nagy" (write-back 4) |
| Form ADV (CRD 317147) | 11 private funds, $193.1M gross assets; owners Lacher and Pollok | AUM floor, fund ladder, T1 |
| German register (North Data) | fund KGs named on 16 portfolio GmbHs' shareholder lists; yearly holding counts per fund | `fund_filing` class (R3); added Tytan, ContextFab, Acapela; dated Tacto and GetMomo to 2020 |
| Deutsche Startups (WordPress search API) | 189 posts, 268 sentences naming the firm, 2019-2026 | recall: Fina, Trana; identities Simplo = GetMomo, aiConomix = automaited, DashDash = Rows |
| Google News sweeps | half-year windows 2019-2026 for "Visionaries Club", "Visionaries Tomorrow" | recall: Conveo, Tytan; rejected Causal Labs, Roboat |
| Wikipedia insource | 6 articles, 3 in the base, no new company | |
| Vendor lists (Tracxn, Startupintros) | leads only, never cited | Conveo came from here and was confirmed in press |


## 5. Method deltas

1. **The domain's previous owner.** visionaries.vc was a Japanese Toastmasters club's site until 2019; every capture
   before 2020 is that club's and was not read (D7).
2. **Archive route.** The Internet Archive refused this machine three times (11:43 for 60 minutes, 12:43 for 120,
   14:43 for 480). Common Crawl carried the 2023-2025 WordPress era (72 crawls from 2019; the CC-MAIN-2023-06 index
   was unreadable) and tomorrow.vc. The IA pass was reordered to fetch the one thing only it held, the Gatsby page
   bundle, first; it arrived before the third block and showed the 2020-22 site had no portfolio list.
3. **Register as a membership layer.** North Data's free fund pages list the portfolio GmbHs whose shareholder lists
   name each fund KG (up to three a year, the rest counted): forward enumeration the §5 table calls aggregator-only,
   filing-grade (R3). It added Tytan, ContextFab and Acapela and dated Tacto's and GetMomo's entries to 2020.
4. **Deutsche Startups' WordPress search API** returned every post naming the firm with full text (189 posts, two
   requests): the German deal monitor found Fina and Trana and resolved three renames (Simplo = GetMomo,
   aiConomix = automaited, DashDash = Rows). FinanceFWD's API, tried the same way, added only a date (Apron).
5. **Stage by construction** (R2): a firm founded after a company's Series A can only have entered at Growth.
6. **Compound surnames in the Form D sweep.** The shared `formd-query.py` keys on the last surname token, so a partner
   filed as "SARKADI NAGY" never matched; `scratch/formd-query-compound.py` also keys on the last two tokens and found
   Zigguratum's 2026 Form D with Marton Sarkadi Nagy as director (write-back 4).

## 6. Flags and debt behind `verify`

`model_disputes_source` 7 (pre-fills overridden: Arculus and Two weak joins, Omnia and Acapela and Fina one-word
Wikidata joins, Miro's unicorn-list mark and country, TrueLayer's unicorn-list mark), `stale` 4 (Choco and Pigment on
their $1B+ marks; Arculus and Two carry it from the overridden pre-fills), `cik_weak` 2 (Arculus, Two), `cite_pending` 1 (Miro's Growth stage, R2), `unstable` 1 (Pallery,
duty 7), `country_conflict` 1 (Conveo: New York per its release, Antwerp per Balderton, London per YC),
`unicorn_name_match` 1 (TrueLayer, whose unicorn-list $1B is overridden). City debt 0, country debt 0. The German register status pass hit North Data's login wall
after two lookups (21 recorded `lookup_failed`, never as active), so status rests on the research's press and
company-site checks.

## 7. Standing duties and the A/B pass

- $1B+ web verification and pass B (newest round, sale, down round) on all 7: no mark moved; Choco (2022) and
  Pigment (2024) carry `stale`, Miro sits at Bending Spoons' agreed $1.79B until closing (R10).
- No `not_graduated` row is $1B+ or public; no censored clock has expired.
- Weak joins: Arculus (a US float) and Two (an "acquired" status) overridden with citations.
- Momentum slice: 30 private rows first seen from 2021 in AI, fintech, data or devtools; every one carries a dated
  check (`valuation_range_source: web_verified`, 2026-09-30); none reached $1B on a priced event (Taktile's $110M
  Series C and Langdock's growth carry no stated valuation).
- Duty 7, blind re-check by a fresh agent of a seeded 5% sample (Tendrils, Solve Intelligence, Leapsome, Pallery):
  3 agree on every field; Pallery's stage disagreed (a job ad calling it "seed-stage", undated) and was adjudicated
  `undetermined`, flagged `unstable`.
- Recall probe: press sweeps by half-year 2019-2026, Deutsche Startups, FinanceFWD, the register, Wikipedia,
  vendor lead lists. Six additions landed; Causal Labs, Roboat and Lightfern rejected (R5).

## 8. Firm profile

HQ Berlin (ADV principal office, which the site lists beside London). Founded 2019. AUM $193.1M (ADV 7.B gross
assets, an exempt reporting adviser's sworn floor) to $515.2M (committed capital across the three generations,
converted at each announcement's ECB rate). Four funds listed (Growth II $197.7M, Seed II $148.3M, Tomorrow I
$49.4M, the first generation $119.8M); the Late Growth SPVs are described, not listed. Range $1.7M / $10.0M /
$30M (press-based median of 43 documented entry rounds). Notables: Miro, Lovable, n8n, Black Forest Labs, Pigment.
Thesis quoted from the homepage h1. Team: 15 from the live site. Icon: the SVG favicon (vector, contrast 11.4:1,
ramp 0.74 px).

## 9. Archetype B: what held and what did not (for PRO-87)

- Held: Form D carries no recall (one portfolio filing in 76 rows); the site, archives and press carry the base.
- Did not hold: "registers pay off on status, not membership". In Germany the free register pages name the fund on
  portfolio shareholder lists, which is a membership layer (R3); the status lookups, not the membership ones, hit the
  login wall.
- New: a young firm's growth-fund entries into famous companies are often unannounced (Miro, Pigment, incident.io),
  and a partner's previous-firm deal can sit on the list (Personio, R1): read partner bios before seeding a famous row.

## 10. Open rulings for Erik

1. **R1 Personio `not_member`** (partner-carried La Famiglia deal, Menlo rule). Moves an $8.5B row; reversal restores it.
2. R2 stage by construction (Miro, Rows = Growth).
3. R3 German shareholder lists as `fund_filing`.
4. R6 Sustained kept on its 2023 listing although its cap tables show founders only.
5. Pallery's stage (duty 7): `undetermined` vs a job ad's "seed-stage".

## 11. Rebuilds and deltas

Two rebuilds. The scheduled one after the recall probe landed the six additions, removed Personio and merged Uify
into turian (76 rows, delta of 6 judged in one batch). A second, for evidence only: the compound-surname Form D sweep
added Zigguratum's filing to Ziggiz; the rebuild changed that row's Form D columns and nothing else (diffed).

## 12. Playbook write-backs proposed (not applied; COLLECTION.md and scripts/ are shared)

1. §5 register table: Germany forward enumeration is partly free (North Data fund pages name holdings); add the
   shareholder list as `fund_filing` (R3) and the yearly counts as a recall check.
2. §5: check the earliest captures' titles before parsing a domain's eras (a previous owner, D7).
3. §5: Gatsby sites can hard-code content in the page-component bundle; only the IA holds JS; fetch it first.
4. `scripts/formd-query.py`: also key a three-token roster name on its last two tokens (compound surnames); the
   scratch variant is `scratch/formd-query-compound.py`.
5. `scripts/run.py verify`: the evidence-link sample fails "none sampled" on a book with no SEC links; it should pass
   vacuously or sample other citation links.
6. §5 recall: a WordPress news site's `wp-json/wp/v2/posts?search=` is a cheap full-text recall layer (Deutsche
   Startups, FinanceFWD).
7. §6 entry_stage: stage by construction from the fund's inception date (R2).
8. `scratch/judge_lib.py`: `fx-convert.to_usd` returns a dict as its detail; a caller printing it wrote a raw dict
   into one note (fixed on the row).

## 13. Usage line

Kickoff (12:08): weekly all models 15%, weekly Fable 1%. Close (after the usage-limit reset): weekly all models 40%,
weekly Fable 5%; the weekly figures include every session on the account. The session hit the 5-hour limit once and
resumed. 76 base rows.

## 14. Prompt count

2: the kickoff and a "continue" after the usage limit.

## 15. Ingest

See below.
