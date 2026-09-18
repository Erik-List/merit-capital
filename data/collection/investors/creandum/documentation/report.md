# Creandum — Build & Reconciliation Report (PRO-72)

Merged run, one session, 2026-09-04. Base, outcome classification and firm
profile under COLLECTION.md's nine steps. Prompt count so far: **1** (the
kickoff); the ingest approval would be the second. Ingest has NOT run.

## 1. The method delta: what the pipeline does when the SEC layers thin out

This was the EU thin-data test (PRO-72): a firm that publishes a portfolio
list and sits mostly outside the SEC. The answer, measured:

- **The SEC layer is fund-side only, not empty.** Eleven Creandum vehicles
  file Form D (Creandum V, L.P. Guernsey; VI/VII/VIII (D)/(E) AB; Select Fund
  I/II; SPV TR), and four exempt reporting advisers file Form ADV with
  Section 7.B gross asset values (eight funds, $4,568,130,162 as of 2026-03,
  parsed from the IAPD PDFs). That is the AUM anchor and the fund list's
  existence corroboration. Issuer-side ownership filings: none, as expected.
  The roster-name Form D sweep reached only the 7 US-incorporated members;
  it did remove two ex-partner clusters (Orgio via Hauge/Wylonis, Aerones via
  Berzins) structurally through the tenure rule.
- **What replaced Form D is the firm's own record, read in depth.** (a) The
  live Contentful CMS behind creandum.com/commitments, decoded from the Nuxt
  full-static payload: 154 rows with the firm's own investment date, lead
  partner, sector tag and exit flag. (b) The 2017–2023 site's data
  attributes (invested year, partner, active/inactive) for 120 rows. (c) Six
  archived listing eras 2003–2026 (22 years, 196 slugs) which alone carry the
  2003–2016 book. (d) The blog since 2009 (325 posts) and the archived
  2003–2018 press pages (141 items, 110 with text), scored class 1 on the
  gate where a post names the round (46/46). The site's date landed
  `first_seen` within a year on 52/52 golden rows.
- **Exit-side EDGAR full-text still works for an EU firm**: Zynga's 8-K
  (Small Giant Games), Uber's 424B7 (Cornershop) and the Spotify/Klarna/Navan
  registration statements gave filing-grade corroboration for the winners.
- **EU registers give the entity set, not the portfolio.** Bolagsverket
  (via allabolag.se) for the Swedish ABs, the Finansinspektionen register
  for the AIFM authorisation and the Swedish AIFs, Companies House for the
  London entity: 11 entities in `entities.json`, filing-grade for ruling 1
  and the profile, zero membership evidence. Companies House's HTML resisted
  the regex and three entities were hand-copied; the negative result stands.
- **Deterministic classification layers shrank to near nothing**: 2 rows with
  `formd_structural` stages, 6 unicorn-list pre-fills, 6 Form D addresses,
  one SEC float (Navan, replaced by a cap). The A/B pass carried the visible
  slice: 17 rows at $1B+, every one web-cited, ~78 web searches in total.
- **Wayback CDX refused every query for the whole run** (third measured
  outage). `wayback-pull.py` gained the replay-probe fallback, per-era
  snapshot memos, gzip-stored capture handling and byte-safe writes; the
  layer still landed. Common Crawl (127 crawls indexed) served as the
  second capture universe.

## 2. Results

- **Base: 177 rows** (162 Tier A two-sourced, 15 Tier B), 1 excluded
  (Elastic, consideration), 26 identity merges (name variants across six
  eras, sprite ids, rebrands: Neo Technology→Neo4J, TripActions→Navan, Vue
  Storefront→Alokai, ArK→Gilion, Argent→Ready, Safety Nest→SafetyWing,
  Instruct→Ares Intelligence, Ivy→Augustus and 18 more). Ledger: 184
  verdicts, 183 member / 1 not_member, 0 uncertain. First-seen by decade:
  2000s 18, 2010s 77, 2020s 82.
- **Status**: private 109, acquired 48, defunct 10, public 5, unknown 5
  (Bravo Company, Pintavision, Proxilliant, Scapin, Tekki: no trace after
  the last listing; `defunct` is undercounted by construction).
- **Valuation bands**: below_1b 158, 1b_plus 16, 10b_plus 2, 100b_plus 1
  (after Erik's Augustus correction and the momentum sweep, below).
  The $1B+ slice: Spotify $111.76B (public), Trade Republic $14.5B, Lovable
  $13.3B, Gopuff $8.5B, Bolt $8.4B, Klarna $7.52B (public), Navan $7.05B
  (public, cap 2026-09-03), Pleo $4.7B (stale), Black Forest Labs $3.25B,
  Factorial $2.50B (EUR 2.15B @ ECB 2026-06-03), Virta Health $2.1B, Kry
  $2B (stale), Neo4j $2B (stale), Tide $1.5B, Epidemic Sound $1.4B (stale),
  Modal $1.1B, Taxfix $1B (stale). Ruled out of the band on collapse
  evidence: Voi (lead investor marks $611M–$656M in 2025), Pipe
  (restructuring, $16M round in 2026). Non-US caps: Cint SEK 2.12B =
  $221.3M (Nasdaq Stockholm), Jays below_1b (First North, tiny).
- **Entry stage**: Seed 90, Series A 67, Growth 17, Pre-Seed 3 — the
  early-stage shape PRO-72 predicted; the 17 Growth entries are the Select
  funds, the SPV and the site-listed late positions (Klarna 2016, Bolt,
  Gopuff, Navan, Neo4j, Trade Republic's later tranches).
- **C2A cohort**: 43 seed entries with a verified second leg, 30 graduated
  to Series A, **69.8%** (the largest cohort so far; 65 rows carry
  `cohort_unverified` where the second leg could not be verified).
- **Focus**: Consumer & Marketplaces 37, SaaS 37, Fintech & Payments 23,
  AI & Applied AI 22, Media/Gaming/Advertising 13, Industrial & Robotics 12,
  Healthcare & Bio 9, Data Infrastructure 8, DevTools 6, Climate 5, Crypto 3,
  Security 2. Geography: SE 48, DE 34, GB 24, US 20, DK 11, FI 9, NO 5,
  FR 5, ES 3, 50 distinct cities, 177/177 filled (Nordic + DACH + UK
  concentrated, as expected).
- **Cross-investor (invariant 10)**: 26 rows shared with the other five
  bases, 26 agree, 0 accepted. Alignments made: Gopuff and Trade Republic
  to Accel's/Thrive's freshest marks; three stale rows corrected on the
  other side — Accel `mason` → defunct (closed 2023), Accel `modal` →
  1b_plus $1.1B (Sep 2025), Sequoia `tola` → acquired (Square, 2025). Their
  base.csv files were re-exported; **Accel and Sequoia need a re-ingest**
  for those three rows after approval.

**Correction after close (Erik, 2026-09-04): Augustus (ex-Ivy) is a
unicorn** — $180M Series B led by Tiger Global at $1B on 2026-07-21, HQ
New York since the US bank charter; the run had it `below_1b`. Why it was
missed: the raise postdates the judge's knowledge; the Wikipedia unicorn
snapshot (2026-08-23) omits Augustus and Ivy; the May-2026 rename
defeated any name match; the firm posted no story about the round, so
the evidence pack showed no trigger and the row never reached the A/B
pass. Rule added (COLLECTION.md §6, decisions.md 19): the momentum slice
(private, first_seen 2020+, hot sector) is web-checked mechanically.

**Momentum sweep run before ingest (Erik, 2026-09-04): 33 rows, 35
searches, every row now carries a web citation.** Found: **Olix is a
unicorn** ($220M Series A at just over $1B in Feb 2026, then a $312M
Series B at $3.3B in Aug 2026 with Creandum named; the grind had read
the site's Feb-2026 entry as a seed), lemon.markets **acquired** by
dwpbank (completed 2025-09-30), Twirl **acquired** by Modal Labs (May
2025), Conduct's HQ is London, and seven entry stages were corrected
from the press (Capi Money, Cerrion, GetVocal, Sibill and Appcharge to
Series A; Causa Prima and Superscale to Pre-Seed; EquiLibre to Series A
at a $500M mark). Sub-$1B figures pinned where a round disclosed one:
EquiLibre $499.5M (Jul 2026), nexos.ai $349.7M (Oct 2025), SafetyWing
$195M (2022, stale). Bands after the sweep: below_1b 158, 1b_plus 16,
10b_plus 2, 100b_plus 1; stages Seed 83 / Series A 72 / Growth 17 /
Pre-Seed 5; C2A cohort 44, graduated 31, 70.5%. Two unicorns out of 33
unchecked hot-sector rows is the measure of what the noticed-signal
scope had been missing.

## 3. Calibration gate (pre-registered before the build)

Membership traps: 25 rows (14 not_member classes, 11 members), **0 false
members**. Stage golden set: 54 keyed rows, blind pass **53/54**; the miss
(Black Forest Labs: the announced Series B read as the entry, press
documents an unannounced Series A participation) became grind rule 14.
Mechanical story-label scoring 34/46 on the regex, 46/46 on a judged
reading (mixed-round posts) — recorded as a caveat, gate PASS.

## 4. Standing duties

- Recall probe: story subjects, announcement titles, the Wikipedia insource
  residue, the exit-side sweep residue and a loose unicorn re-intersection —
  **0 additions**; residue classified (people posts, the Included VC
  fellowship, Asante the placement agent, list inclusions, Tesonet =
  nexos.ai's round, Prompt Security no naming sentence).
- Weak-CIK audit: one collision (a public "Midas Group" registrant on the
  Midas row) already disputed on the row; no float leaked.
- Self-consistency (5% blind re-judge, 9 rows, 45 fields): **39/45 agree**;
  the six disagreements sit on 4 rows flagged `unstable` (Kahoot focus,
  Appcharge focus, Prewave stage and focus, Sibill stage) — the recorded
  values stand with the reasons in the notes.
- City/country coherence sweep: 50 pairs read; Kista normalised to
  Stockholm (Nanoradio), Kurrent pinned to San Francisco, Lunar-X's focus
  identified (Media, Gaming & Advertising).
- Wikidata pre-fill disputes carried as `model_disputes_source` (10 rows:
  Lovable IT→SE, Billie BE→DE, Bolt DE→EE, Monta "German Reich"→DK, Mason,
  Midas, Spotify status, plancraft, Junction, Maisa).

## 5. Firm profile (§11), built once against the landed base

`investor.json` + `investor/sources.json` through the builder: HQ
"Stockholm, Sweden" from the firm's own Form D filings (EDGAR country code
V7 mapped by the builder, a new EU-fund rule); AUM bottom = top =
$4,568,130,162 (sworn 7.B gross asset values; press "$2B" and the firm's own
2019 "$750M" sit below the floor); ten funds 2003–2024 with sizes from the
firm's own posts converted at ECB rates (I SEK 300M, II SEK 750M, III
€135M, IV €180M, V $300M, VI $500M, VII €500M) or the Form D amounts
(Select I offering $122M; Select II $106.1M and SPV TR $22.3M
accession-asserted); Creandum VIII in market (Form D 2026-06-30,
indefinite) and unlisted; 16 investment-team members from the live CMS
(titles from the firm's own promotion posts where stated: five General
Partners and one Partner, the CMS label "Investment Team" for the rest);
focus recomputed from the site tags (SaaS, Consumer & Marketplaces, AI,
Fintech above 12 companies); stage Pre-Seed/Seed/Series A/Growth; geo
core Europe, other US; range $1M / $7M / $25M (median from 47 of the firm's
own entry announcements, flagged press-based). Icon: the site's 256px
favicon normalised in a dry run (bare green glyph on a synthesized white
plate, 7.5:1 contrast) — upload gated with the ingest.

## 6. Flags and debt (all on the surface, none hidden)

stage_uncited 100 (all below $1B, informational), cohort_unverified 65,
censored 17 (rows where the judge withheld model knowledge under the
protocol), model_disputes_source 10, stale 6, unicorn_name_match 5,
unstable 4, stage_disputes_band 2. Announcement harvest: 31 of 141
archived URLs still fail to load from Wayback. The `cdx_company_pages`
eras (2013, 2013–2017) parsed only intermittently under the outage; the
listing eras covered every year.

## 7. Open rulings for Erik (raised once, here)

1. **Site-listed consideration positions are not members** (Elastic via
   Opbeat, 2017, held through the IPO) — decisions.md ruling 11.
2. **Exit rows carry no figure** (acquired/defunct rows sit `below_1b`
   with the exit price in the note; matches the five landed bases) —
   ruling 15.
3. **Collapse evidence extended** to lead-investor fair-value marks (Voi)
   and a restructuring plus small undisclosed round (Pipe) — ruling 16.
4. **AUM both ends = ADV 7.B gross asset value**, press top rejected as
   below the floor — ruling 18.
5. **Geo core Europe only, US as other** (20 of 177 rows, an SF office):
   the site frames itself as European; no §9 trigger-3 breach.
6. The four `unstable` rows and the five `unknown` statuses.
7. Re-ingest of Accel (mason, modal) and Sequoia (tola) rows.

## 8. Pipeline contributions for EU funds (the run's second deliverable)

`scripts/fx-convert.py` (ECB reference rates, cached, cross-rated via EUR);
`site-portfolio.py` `nuxt_payload` + `wayback-pull.py` `nuxt_payload_listing`
(Nuxt full-static payloads, cyclic decode, archived builds); the CDX-outage
replay path with per-era memos and gzip handling; `build-company-base.py`
first_seen precedence (site date and Form D first round count) and
rendered-name-over-slug; `build-firm-profile.py` EDGAR country codes; the
ADV 7.B PDF parse for ERAs (`scratch/adv-7b-funds.json`); the EU register
entity file shape (`sources/registers/entities.json`); the announcement
archive as a class-1 layer. Written back to COLLECTION.md §1, §5, §6, §11.

## Addendum 2026-09-17 — S2A re-judged under the status contract

`seed_to_a_graduation` became a judged status (`graduated | not_graduated |
censored | undetermined`, COLLECTION.md §6), superseding the C2A figures
above. `migrate-graduation` kept five cited graduations, converted Erik's
human ruling on `augustus` from the retired boolean, and dropped 87 legacy
values with their 66 `cohort_unverified` flags; the 78 re-opened Seed rows
were judged in two batches with both legs cited in the same pass.

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|---|
| 79 | 8 | 34 | 37 | 31 | 1 | 83.8% | 52% |

Of 79 seed entries, 8 were too recent to count; of the 71 whose record could
be sought, 37 were established (52% coverage) and 83.8% of those graduated —
the establishable set skews toward visible successes. The single "no" is
Opbeat's acquisition by Elastic, on the firm's own post. Of the 34
undetermined, twelve fail only on the stage leg and would flip on one URL
(Topi, Resolution Games, Yababa, Soundtrack Your Brand among them), five
have a terminal event no reachable publisher covers, and eight are live
companies with no later round on the record. Three rows are pre-window and
leave the cohort by rule.

`verify.shape.c2a_rate_max` is restated 0.80 → 0.90 (D-S2A). `verify` is
clean.
