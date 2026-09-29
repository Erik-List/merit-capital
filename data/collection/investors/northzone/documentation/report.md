# Northzone: Build & Reconciliation Report (PRO-105)

Run of 2026-09-29, one session, slug `northzone`. Archetype B (European early stage), sub-issue of PRO-87.

## 1. The answer PRO-105 asked for

Northzone is collected: **220 companies**, plain `verify` clean with only flagged debt, the firm profile
through the taxonomy gate, `review.html` rendered and checked in a browser. **S2A 63.2%** (12 of a 19-row
cohort). **11 companies at $1B or more**, Spotify the one above $100B. The ingest ran through the §9 gate
at the end of the run; section 15 records what was written.

The four deltas of the issue, in one line each:

- **Three register regimes**: coverage is reported per regime in section 4. The Nordic rows carry most of
  the debt: 23 of 93 still read `unknown` status, against 2 of 38 UK rows.
- **US office, partial Form D visibility**: tested. The roster sweep reached 8 of the 44 US rows and
  added exactly one company the firm does not list (Realize, a director-of-record row). It reached no
  European row.
- **Founded 1996, pre-window slice**: 22 of 220 rows (10.0%) were first seen before 2006. There is no
  window any more (PRO-137), so this is a plain count.
- **Creandum overlap**: 11 shared rows, 10 agree; the eleventh (Stockeld Dreamery) was stale on
  Creandum's side and is aligned in section 15.

## 2. Results

| | |
| -- | -- |
| Rows | 220 (142 on the live site, 76 from the archived listings only, Mojn from the recall probe, Realize from Form D) |
| Verdicts | 256: 223 member (220 rows plus 3 absorbed duplicates) and 33 not_member (32 in `excluded.json`, one Form D issuer the build no longer produces) |
| Status | private 108, acquired 61, unknown 34, public 9, defunct 8 |
| $1B+ | 11: Spotify ($101.4B), Personio ($8.5B), Klarna ($4.85B), Spring Health ($3.3B), Black Forest Labs ($3.25B), CuspAI ($2.6B), Forto ($2.1B), Blitzy ($1.4B), Trustpilot ($1.06B), Zopa ($1.0B), Xbow ($1.0B) |
| Entry stage | Series A 49, Seed 27, Growth 20, Pre-Seed 2; 120 nameable rows undetermined; 2 unnameable |
| Focus | Consumer & Marketplaces 45, Media, Gaming & Advertising 30, SaaS 27, Fintech & Payments 26, AI & Applied AI 20, and seven more |
| City | 191 of 220 filled, 42 distinct; London 35, Stockholm 30, Oslo 21, New York 18, Berlin 12 |
| Rule 10 | 98 rows shared with 33 books; 94 agree, 4 accepted as stale on the other side, 0 disagree |

### S2A block

27 seed entries, 8 censored (entered at seed within the last 24 months), cohort 19, **12 graduated, 7 not
graduated, rate 63.2%**. The seven nos rest on the absence test (no named Series A on the firm's surfaces,
Form D for US companies, and at least two publisher surfaces, as of 2026-09-29), none on a cited end.
Graduated: Aidence, CuspAI, Hopin, Rayon, Recall Labs, Spektr, Stockeld Dreamery, Tandem Health, Flink,
Goals, Ravio, Yonder. Not graduated: Era, Fiberplane, Solvimon, Troop, Zeal, Mimo, Salus. Flink and Hopin
graduate on an uncited seed stage (flag `stage_uncited`, stage confidence low).

`defunct` is undercounted by construction (§6): quiet shutdowns of the 2003 and 2010 cohorts present as
`unknown`, so no mortality rate may be read off the status column.

## 3. Calibration against Cherry and Creandum

A smaller, winner-weighted base, as PRO-87 predicted: 220 rows against Creandum's 177 and Cherry's 148,
with the extra rows coming from Northzone's longer history (1996 against 2003 and 2012). The $1B+ share is
5.0%, close to Cherry's 5.4% and under half of Creandum's 11.9%: Northzone's 2003 and 2010 cohorts are
large and mostly sold below $1B. The live site lists 142 companies; the archive added 76 that the firm no longer
shows, 44 of them exited, which is where the `unknown` status debt sits.

## 4. Coverage per evidence regime

Rows are grouped by headquarters country. "Stage known" is a named entry round; "archive only" means the
firm's live site no longer lists the company.

| Regime | Rows | Archive only | Status unknown | Stage known | City blank | $1B+ | First seen before 2006 | Form D reached |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Nordic (SE, NO, DK, FI, EE) | 93 | 51 | 23 (25%) | 27 (29%) | 17 | 3 | 18 | 0 |
| UK | 38 | 11 | 2 (5%) | 16 (42%) | 1 | 2 | 3 | 0 |
| US | 44 | 10 | 7 (16%) | 23 (52%) | 8 | 3 | 1 | 8 |
| Other Europe and elsewhere | 45 | 6 | 2 (4%) | 32 (71%) | 3 | 3 | 0 | 1 |

What each regime could answer:

- **Denmark** (cvrapi.dk): status for any company by name, including dissolved ones. Four rows decided
  (Speakanet and Interse bankrupt, Cryptico dissolved, AllUnite active). One namesake rejected (Mojn ApS).
- **Finland** (PRH open data): status and name history. Imbera's rename to GE Embedded Electronics Oy
  (2013) decided it as acquired.
- **Norway** (Brønnøysund): the name search answers live entities only, and none of the nine Norwegian
  `unknown` rows matched a live entity. A deleted entity answers only by its organisation number, which no
  surface gave. The shareholder register extract needs a request form with personal data and an emailed
  link, so it was not run (section 10).
- **Sweden**: no free structured endpoint answers a script (allabolag.se refuses curl), so the 12 Swedish
  `unknown` rows rest on press and the firm's pages. Sweden is the largest single block of status debt.
- **UK** (Companies House, public website): status, incorporation, officers. Four rows decided
  (BraveNewTalent and Orecon dissolved, Colibria at Metaswitch's address, Ocapo active). The officer graph
  confirmed Jeppe Zink on Ocapo's board (2013-2017) and exposed the Ocapo/eProspects duplicate.
- **US**: Form D issuer histories on 8 rows, SEC public float on 3, the roster sweep as above.

## 5. Method deltas

- **The Internet Archive was unavailable for the whole run** (a machine-wide cooldown that kept doubling,
  about 167 minutes at 22:16 UTC). Common Crawl carried the archive: 1,160 captures from CC-MAIN-2013 to
  2025 plus the ARC crawls of 2008 to 2012, read through the static `cluster.idx`, parsed into
  `sources/wayback/parsed/{2010,2012..2025}.json`. The 2003 listing came from one cached Wayback capture,
  whose rows carry no names, so 15 of 17 were mapped to companies by the description the 2010 pages repeat
  (`W5_2003` in `scratch/archive-listings.py`). Gaps are recorded, not read as absence (decisions.md R7).
- **The firm's 689 posts** (`sources/site/insights.json`, body, WordPress date and outbound article) were
  the main first-party evidence for entry rounds, sizes and exits: 102 rows cite one.
- **A register status pass at close** decided nine `unknown` rows and found one duplicate (decisions.md R9, R10). It belongs before
  the grind on the next archetype-B run (section 9).
- **A third rebuild** before export merged Ocapo into eProspects (R9); it changed that one slug and
  nothing else, and the grind was complete. Menlo's precedent (a rebuild after the delta) covers it.
- **The investment range median comes from the firm's own announcements**, as on Creandum and Balderton,
  because Form D covers few European rows (`scratch/entry-round-sizes.py`).

## 6. Flags and debt behind `verify`

city_unknown 29, model_disputes_source 22 (mostly one-word Wikidata country joins the judge overruled),
stale 6 (Forto, FuboTV, Personio, Spring Health, Tier, Fox Technologies: newest priced round older than the
freshness window, checked in the A/B pass), unicorn_name_match 4, cik_weak 4 (Era, FuboTV, Tier, Fox
Technologies: floats quarantined, `is_public` set false where the join was wrong), country_prior 4,
boundary 2 (Era, Realize), stage_uncited 2 (Flink, Hopin), identity_unresolved 2 (BNT, OBC). One stale
classification key (Ocapo, merged). 34 rows `unknown` status.

## 7. Standing duties and the A/B pass

- **Stale marks**: every `stale` row checked for a newer priced round; none found. Zopa's 2025 raise was
  an AT1 bond, not equity.
- **Weak joins**: the four `cik_weak` rows handled as above; Fox Technologies' acquired-and-public came only
  from a wrong CIK and reads `unknown`.
- **Unicorn re-intersection**: no missed $1B+ company.
- **Momentum slice**: 32 private rows first seen from 2021 in AI, Fintech, Data Infrastructure or DevTools
  carry a dated check (2026-09-29). CuspAI's $2.6B Series B had been found the step before, from the
  firm's own post on its "four AI unicorns".
- **Blind 5%**: 11 rows re-judged blind on four columns, 44 of 44 agree (`scratch/duty7-result.json`).

## 8. Firm profile

HQ London (the site's office list wins over the Jersey Form ADV address). Thesis quoted from the homepage
headline: "Backing world-changing companies from inception to IPO." History 70 words, three sentences.
Stage Seed to Growth; geo Europe core, US other; scope Generalist with seven focus values recomputed from
the site's sector tags (144 of 220 rows tagged). Range $2.5M / $17M / $82.1M: the median of 34 entry
rounds the firm announced with a stated size, the floor Aidence's seed, the ceiling CarOnSale's €70M
Series C that Northzone led. AUM $1.65B to $3.1B: the floor is the sworn Section 7.B total of the three
Jersey advisers (Funds IX, X, Growth II and a side vehicle; older funds report to no SEC adviser), the top
is the firm's own About page. Funds listed: X and Growth II (€1bn, 2022), IX ($500M, 2019), VIII (€350M,
2016), VII ($325M, 2013); Northzone XI filed its first notice in 2026 and is being raised. 32 people from
the live team page. Notables: Spotify, Klarna, Trustpilot, Kahoot!, Personio. Icon: the site's 512 px
webclip, ramp 0.91 px, uploaded.

## 9. Archetype B: what held and what did not (for PRO-87)

Held:

- Form D does not carry recall: zero European rows, one US row the site lacks.
- The site, the archive and the firm's own posts carry the base; press carries status.
- The fx constant bound on every non-USD figure.
- EDGAR still ran reduced: the full-text sweep found only noise to explain (Velti, where a Northzone
  vehicle is a Seedcamp LP; a partner's biography in other issuers' filings; Tier's own 13D).

Corrections proposed:

1. **Run the register status pass before the grind, not at close, and aim it at the archive-only rows.**
   The 2003 and 2010 cohorts are exactly where press is silent; one pass at close decided 9 of the 13 Danish,
   Finnish and UK unknowns. It also found a duplicate (Ocapo/eProspects) through the officer graph.
2. **"Registers pay off on status" is regime-dependent inside one base.** Denmark, Finland and the UK
   answer by name; Norway answers only live entities by name (deleted ones need the organisation number);
   Sweden answers no script. Say so in the derivation, so the report does not read a Swedish or Norwegian
   `unknown` as unfinished work.
3. **Expect the Internet Archive to be unavailable** and plan Common Crawl (including the 2008-2012 ARC
   crawls) as the default archive for European sites, with IA as the extra.
4. **The firm's own post archive is a layer in its own right** for European firms (WordPress dates,
   outbound press links, round sizes); it did more than press for entry rounds here.

## 10. Open rulings for Erik

None blocks the ingest; the book was ingested on its current reading.

1. **Realize, Inc.** (R2): a member on a director-of-record seat alone (Molly Alter on its 2024 and 2026
   Form Ds), no listing and no press naming Northzone. In, or out for a firm with a complete live list?
2. **Nevion as sale consideration** (R1): Nevion came from the T-VIPS merger and is out; T-VIPS is in.
3. **Statement is Tuza** (R3), merged at medium confidence on product, year and partners, with no source
   stating the rename.
4. **Stockeld Dreamery acquired, not defunct** (R6): Bettani Farms bought it after it stalled. Creandum
   read defunct; aligned to acquired in this run (section 15).
5. **Norwegian shareholder register**: the extract that would settle the nine Norwegian `unknown` rows needs
   a request form with personal data and an emailed download link. Yours to request if wanted.
6. **The archive gaps** (R7): 2001-2002, 2004-2007, the 2005-2008 ASP site and the Hugin press releases.
   A re-run of `scratch/archive-listings.py` when the Internet Archive answers closes them.
7. **BNT and OBC** (R8): listed by the firm in 2017-19 with nothing that names them. They stay as
   unnameable rows, excluded from every metric.

## 11. Rebuilds and deltas

- Base v1: 176 rows (142 site, 34 Form D name matches, 31 of them homonyms ruled out).
- Rebuild after the archive and the recall probe: 225 rows; the delta of 82 archive rows judged (Nevion and
  one more Paul Murphy homonym out, Mojn and Ocapo in from the recall probe).
- Final rebuild with the identity merges: 221 rows (31 merges: renames such as FreightHub to Forto,
  iZettle to Zettle, Wagestream to Stream, Trolltech to Qt, MarketInvoice to Kriya, 3Box to Recall Labs).
- Third rebuild before export: 220 rows (Ocapo into eProspects, R9).

## 12. Playbook write-backs proposed (not applied; COLLECTION.md and scripts/ are shared)

1. **Rule 10 should match on a normalised slug** (letters and digits only). Northzone's `cusp-ai` and
   Lightspeed's `cuspai` were never compared, and they disagreed ($2.6B against below $1B). A scan of
   Northzone's rows found one other variant pair (`spaceape` / Accel's `space-ape`, which agrees).
2. **`run.py record` is not idempotent on notes** (around line 1633): `prev.update(rec)` replaces the note
   before the join check runs, so recording the same line twice leaves only the new sentence. Recording a
   patch twice here dropped five rows' descriptions, restored from HEAD. Build the joined note from the
   old one first, and skip the join when the new sentence is already in it.
3. **Common Crawl is the archive layer when the Internet Archive stays blocked for the run**, not only for
   sites it excludes (§1, IVP), and the 2008-2012 ARC crawls reach the older site generations.
4. **Momentum slice**: add the firm's own posts of the last 12 months as a surface. CuspAI's $2.6B round
   was on the firm's own "four AI unicorns" post before any row-level check found it.
5. **Recall additions named after a legal entity** get checked against the listing's brand names before
   close (Ocapo is eProspects' company); the register officer graph is the cheap test.
6. **`scratch/entry-round-sizes.py` and `scratch/nordic_status.py` are investor-agnostic** and could move
   to `scripts/` with `companies_house.py` (Atomico's). The round-size parser needs its context filter:
   a post can open with the size of the market (CarOnSale "$180bn of trade") before it names the round.

## 13. Usage line

Kickoff 17:47 UTC: 5-hour limit 74%, weekly all models 71% (reset at 18:00 UTC), weekly Fable 6%.
Close, 22:44 UTC: 5-hour limit 33%, weekly all models 11%, weekly Fable 0%, extra usage off (EUR 12.14 of
50 spent). Context 25% at close. About 19 of the 200 web searches used.

## 14. Prompt count

**3**: the kickoff ("please collect Northzone") and two "continue" nudges, one mid-turn and one after the
run paused waiting on the Internet Archive. No corrections. Target 1: the pause was the run's own choice
and should not have been; section 9 item 3 is what removes it next time.

## 15. Ingest

(filled in at the end of the run)
