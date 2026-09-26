# Point Nine: collection run report

**Linear issue** PRO-101 (sub-issue of the PRO-87 wave umbrella) · **slug**
`point-nine` · run closed **2026-09-26** · one session, one run, under the
merged shape of `data/collection/COLLECTION.md`. Ingest is **not** done: it
waits for Erik's explicit approval (order for a first-time investor: icon
upload, then `ingest-investor.ts`, then `ingest-companies.ts`).

---

## The answer PRO-101 asked for

**Archetype B carried over from Cherry to Point Nine: the method transferred
whole, but three of PRO-87's layer weightings did not hold for this firm.**

Carried over unchanged:

- The firm's own lists as the membership anchor (all 199 members rest on a
  first-party list), archived lists for the old book, the blog as a
  first-party press surface (D12), the job board under Thrive ruling 8 (D11),
  `fx-convert` on ECB rates, the market-cap rule for listings outside the SEC
  (Delivery Hero, Westwing and Mister Spex, all Frankfurt), the insolvency
  convention (Kreditech as Monedo), the A/B pass, the momentum-slice web check
  and the S2A absence test.
- North Data for the German entity tree: 27 entities (the two exempt reporting
  advisers, Funds I to VII, Annex and Annex II, the co-invest and team KGs),
  filing-grade for D1 and for the profile.
- A smaller, winner-weighted base: 199 rows, 7.0% at $1B+, between Cherry
  (5.4%) and Creandum (10.7%).

Did not hold:

1. **The German register gave membership corroboration, not status.** Point
   Nine's fund KGs publish their holdings (annual accounts, shareholder lists)
   and North Data's free block shows them: 29 holdings on 28 companies. Every
   member among them was already on a list (zerolens is Mokker.ai), and three
   register positions were rejected as sale consideration (acardo group,
   Personio for Back, Lindentor 226 for Lemoncat). Cherry's holdings sat
   behind the paywall. No status came from a register: the one insolvency (Kreditech, as Monedo) came from the press, and
   the firm's own card (RIP, Acquired) did the status work, stale in both
   directions (R3). PRO-87 says registers pay off on status, not membership;
   here it was the reverse, and small.
2. **Form D is partial by row, not absent.** 42 members are US-based (21%,
   against Cherry's 8% and Creandum's 12%). Form D links 5 of them and carries
   no membership, but it did three jobs: the partner-name sweep (45
   accessions) removed 7 partner seats from other firms (D10: Wittenborn's
   Insight and Adjacent seats, Ockenfels's at Speedinvest), it decided one
   graduation, and every US "no" carries its Form D line.
3. **The firm's list mixes three books** (D2, D7). The site presents the
   founders' personal angel checks of 2008 to 2011 as its own ("Since 2008,
   we've invested..."), beside the funds' book and a few non-seed positions
   since 2025 (an LP stake in Project Europe, a Series G in Anthropic). The
   firm's own words separated them: its old list's "previous" flag and its
   old CMS's "Pre Point Nine" gave 17 build rejects, and 7 live cards that the
   firm itself calls Christoph Janz's angel investments (Zendesk, FreeAgent,
   Geckoboard, Momox, Propertybase, samedi, Server Density) became
   `not_member` verdicts, with Project Europe as a fund. Neither Cherry nor
   Creandum had this class.

PRO-101's other three predictions held: the blog is a real surface (410 posts
read; it names rounds the list omits, but found no company missing from the
lists), the S2A cohort is the largest of any European book so far (145), and the
mixed portfolio needs its coverage reported per regime (below).

## Results

| | |
|---|---|
| **Base** | **199 companies** (tier A 6 · B 193) |
| Excluded, preserved in `excluded.json` | 33: 17 build rejects (the firm's own "previous" and "Pre Point Nine" flags, D2) and 16 `not_member` verdicts (7 angel checks, Project Europe, Mobilike, 7 partner seats at other firms) |
| Membership ledger | 215 verdicts · 0 uncertain (199 member, 16 not_member) |
| `status` | private 121 · acquired 53 · defunct 20 · public 3 · unknown 2 |
| `entry_stage` | Seed 153 · Pre-Seed 20 · Series A 18 · Growth 2 · **undetermined 6** (R2) |
| stage sources | first_party 130 (the scored card label, D13) · web_verified 60 · model 3 |
| `hq_country` | DE 56 · US 42 (21%) · FR 21 · GB 16 · NL 9 · ES 7 · CA 7 · PL 7 · 26 others with 34 rows |
| `hq_city` | 199/199 filled, 63 distinct (Berlin 36, San Francisco 23, Paris 20, London 14) |
| `focus` | 100% fill: SaaS 63 · Consumer & Marketplaces 48 · AI & Applied AI 18 · Healthcare & Bio 13 · DevTools & APIs 9 · Climate & Energy 9 · Fintech & Payments 9 · Industrial & Robotics 9 · Crypto & Web3 6 · Media, Gaming & Advertising 6 · Data Infrastructure 5 · Security 4 |
| Visible slice | **14 rows at $1B+** (7.0%), 4 at $10B+, 2 at $100B+ (Anthropic $965B, Revolut $115B) |
| S2A | 153 seed entries, 8 censored · cohort **145** · graduated 80 · not 65 · **55.2%** · coverage 100% |
| Era span | first seen 2009 to 2026 (2009-2012: 31 · 2013-2017: 62 · 2018-2022: 63 · 2023-2026: 29) · 14 rows undated |
| Firm profile | HQ Berlin · AUM $2,092,009,841 (sworn, both ends) · 9 funds · 14 people · thesis "Point Nine is a thesis-driven early-stage venture capital firm." |

`verify` is **clean in plain mode**. Cross-investor: 72 shared rows, 65 agree,
7 accepted (Point Nine's side fresher, for the wave alignment, listed under
open rulings), 11 homonym pairs ruled distinct, 0 disagree. Atomico was in
flight and not compared.

## Coverage per evidence regime

| regime | rows | Form D linked | stage cited on the web | seed cohort | graduated | rate | nos on the absence test | $1B+ |
|---|---|---|---|---|---|---|---|---|
| US | 42 | 5 | 13 | 28 | 19 | **67.9%** | 6 (each with its Form D line) | 7 |
| Germany | 56 | 0 | 10 | 43 | 21 | **48.8%** | 20 | 1 |
| rest of Europe and elsewhere | 101 | 1 | 37 | 74 | 40 | **54.1%** | 20 | 6 |

The US rows graduate more often, and part of the gap is coverage, not
outcome: a US round shows in Form D and in dense English press, a European
round only in press, often in the home language. 40 of the 46 absence tests
are European, and every one now carries a home-language search: 30 through
`googlenews_local`, 8 by hand where the script has no edition (Polish,
Russian, Greek, Peruvian Spanish) or the row missed it (Athenian), and the two
English-market rows (Airstoc, Sloika) through the main search. The hand pass
found merXu's Nov 2021 round named a Series A (EMEA Startups), so merXu
graduated; Accel's row has the same miss. The risk runs both ways: this run
first read Heygo's seed as a missing round and Upciti's Series A as a seed,
both corrected (R4). Membership does not depend on the regime here: every
member, US or not, rests on the firm's own lists.

## Calibration against Cherry and Creandum

| | Point Nine | Cherry | Creandum |
|---|---|---|---|
| Base rows | 199 | 148 | 177 |
| $1B+ | 14 (7.0%) | 8 (5.4%) | 19 (10.7%) |
| private / acquired / defunct / public / unknown | 121 / 53 / 20 / 3 / 2 | 106 / 24 / 10 / 1 / 7 | 107 / 50 / 10 / 5 / 5 |
| Seed share of staged rows | 79% | 71% | 45% |
| S2A cohort, rate | 145, 55.2% | 83, 62.7% | 71, 52.1% |
| US share | 21% | 8% | 12% |
| Entry check median | $2.8M | $5M | $7M |
| AUM | $2.09B | $0.91B to $1.0B | $4.57B |

Point Nine has the largest base of the three and sits between the two on
winner share and S2A rate. It is the most seed-weighted and has the smallest
checks, which fits a seed specialist. Its defunct share (10%) is above
Cherry's (7%) and Creandum's (6%): an older book (from 2009), and a firm that
keeps its failures on its own list marked RIP.

## Method deltas

- **The Internet Archive refused this machine twice** (the shared cooldown
  doubled to 120 minutes). Common Crawl WARC records from data.commoncrawl.org
  replaced it for the pointninecap.com list 2012 to 2015 (4 captures, 82
  companies) and the p9-family list 2021 to 2023 (3 captures, 158), each row
  citing its capture.
- **The 2018 to 2020 CMS was read live.** The archived site shipped a
  read-only Contentful token to every visitor; the public delivery API still
  answers and gave 113 companies with the firm's own fund, round, status and
  a "Pre Point Nine" marker: the T2 evidence for D2.
- **The live card's round label** ("P9 INVESTMENT") scored 36/40 = 90% blind
  and labels at `medium` (D13); its misses are one class, 2011 to 2013 rounds
  of $1M to $2M the press named Series A. Before a named round overrides the
  card, the card's own round is searched for (R4).
- **Sale consideration** (R1): a holding received in exchange for a portfolio
  company's shares (Mobilike for madvertise) is not a member; the kickoff's
  three register rejections are the same class.

Evidence layers: live list 193 cards · job board 107 · CMS 2018 to 2020 113 ·
p9-family 2021 to 2023 158 · pointninecap.com 2012 to 2015 82 · blog 410 posts
(122 companies named) · TechCrunch 90 articles (71 companies) · registers 27
entities, 29 holdings · Form D partner sweep 45 accessions · EDGAR full text 13
registrants · issuer-round histories 8.

## The A/B pass and the standing duties

- **Every $1B+ private row is pinned to a priced event with a citation.** The
  A/B pass attacked 7 rows and each held: Anthropic (confidential IPO filing
  2026-06-01, not listed; last primary $965B, 2026-05-28), Delivery Hero
  (Uber's offer runs to 2026-11-05 with closing expected H2 2027, so public at
  market cap, $12.82B), Chainalysis ($8.6B of 2022 stands, stale; a vendor
  secondary near $1.55B stays in the note under Rule A), and Mambu, Algolia,
  Front and NexHealth (no newer event; stale).
- **Fresh marks**: Revolut $115B (company-run secondary, 2026-07-22), Poolside
  $12B (Nvidia, 2026-08-24), Clio $5B (2025-11), Factorial $2.44B (2026-06),
  Odyssey $1.45B (2026-06), Preply $1.2B (2026-01).
- **Public rows**: all 3 on Frankfurt with a market cap at the ECB rate.
- **Momentum slice**: 13 recent rows web-checked, all below $1B, each check on
  its row.
- **Blind self-consistency**: 10 rows re-judged, 0 disagreements.
- **Status over the card** (R3): Calldesk and Typeform were sold while the card
  says Active; Kreditech (Monedo) was liquidated and Zenaton closed while the
  card says Acquired; June is defunct under the acqui-hire rule.

## S2A block

| seed entries | censored | cohort | graduated | not graduated | rate | coverage |
|---|---|---|---|---|---|---|
| 153 | 8 | 145 | 80 | 65 | 55.2% | 100% |

Of 153 seed entries, 8 were too recent to count (Aardaia, Aletiq, Draxon,
Duplo, EraDrive, Modern Relay, rerun, Sensmore). Of the 145 that remain, 55.2%
raised a later round. Of the 65 that did not, 19 rest on a cited end and 46 on
a dated search of the firm's archive and at least two publisher surfaces, plus
Form D for US rows and a home-language search for European ones. The entry
leg: 98 rows on the scored card label, 44 cited on the web, 3 on the model
alone (BabyBoom, Hipway, Kekemeke, `stage_uncited`, low).

## Firm profile

Built by `build-firm-profile.py`, checked by `profile_copy.py` and `verify`:

- **AUM $2,092,009,841**, both ends: the Section 7.B(1) gross asset values of
  the two exempt reporting advisers (annual amendments 2026-03-26): CRD 306640
  (Funds I to V and Annex, $1.50B) and CRD 319531 (Funds VI, VII and Annex II,
  $0.59B). An ERA files no RAUM, so the 7.B composite is the sworn figure
  (Creandum precedent); the firm publishes none.
- **Funds**: I ($6.7M, 2011) to VII (2025), with Annex (2016) and Annex II
  (2022); sizes from the firm's own posts, press and two fund Form Ds, euro
  figures at the ECB rate of their date; VII and Annex II have no published
  size.
- **HQ** Berlin (newest ADV principal office, Torstr. 19; the site names none).
- **Team** 14. **Range** $0.5M / $2.8M / $17M (83 documented entry rounds).
- **Focus** (Specialist): SaaS, Consumer & Marketplaces, AI & Applied AI,
  Industrial & Robotics, DevTools & APIs, Fintech & Payments.
- **Notables**: Revolut, Anthropic, Delivery Hero, Loom, Typeform.
- **History** 62 words, no filing vocabulary. **Thesis**: the homepage
  headline, verbatim, in quotation marks.
- **Icon**: the firm's own vector mark, dry run passed; `icon_url` points at
  the source until the upload runs with the ingest (Benchmark precedent).

## Open rulings for Erik

1. **R2, six members with no round that ties Point Nine**: five listed only on
   the job board (Audigo Labs, Blockit, Ditto, Elea, Recast Systems) and
   EatFirst; for four of them the round press names other investors. Kept as
   members with an undetermined stage; remove them?
2. **D2**: the founders' personal angel checks of 2008 to 2011 are out
   (Zendesk, FreeAgent and five more; Clio stays on the fund's own 2011
   entry). A derivation, vetoable.
3. **R5, Tier** reads below $1B on collapse evidence (the Dott merger), the
   Creandum Pipe precedent.
4. **merXu** is defunct on the firm's RIP alone; Accel's row reads private.
   Its Nov 2021 round is a named Series A, so it graduated here, and Accel's
   row reads not graduated on the same round (S2A is not a rule-10 column).
5. **Mason** ruled distinct from Accel's Mason (getmason.io), which the same
   founders started after this one shut in 2019.
6. **Seven accepted rule-10 pairs** for the wave alignment, Point Nine's side
   fresher: June against a16z and YC (acqui-hire rule), Revolut against a16z
   and Greylock ($115B), Poolside against Redpoint ($12B), Zenaton and merXu
   against Accel.
7. **REKKI's S2A against Cherry**: the firm's own 2020 post names Rekki's
   Series A; Cherry's row reads not graduated (not a rule-10 column).
8. **Published names (PRO-146)**: AMMP, LIFT and REKKI publish in capitals,
   MisterSpex should read Mister Spex, and HeyGo is spelled Heygo by the
   press. A rename costs nothing before the first ingest, but the per-row
   override PRO-146 needs does not exist yet.
9. **Upciti**: two sources call different rounds its Series A (FrenchWeb the
   2023 round, the company's own release the 2025 one); the card's 2023 label
   stands at medium.

## Playbook write-backs proposed (for the tooling session and PRO-87)

1. **Common Crawl is the archive fallback when the IA cooldown hits**, not only
   when a domain is excluded (IVP's case): WARC records per capture, each row
   citing it.
2. **An archived page can ship a CMS read token**; the CMS then gives an era's
   list with the firm's own fields (Contentful here, Cherry's Sanity before).
3. **The firm's own "previous" and "Pre Point Nine" flags are T2 evidence** for
   founders' angel books presented as the firm's own.
4. **Sale consideration includes share swaps at a sale** (R1).
5. **Search for the firm's own round label before the record overrides it**
   (R4): Heygo's Series A press omitted the seed Point Nine led.
6. **Reject slugs must match the builder's slugging of non-ASCII names**:
   KäuferPortal slugs as `k-uferportal`, and a reject written `kauferportal`
   failed silently until the second build.
7. **`record` keeps only the last line per slug in one file** (IVP reported the
   same); a second Upciti line was lost.
8. **`clear_flags` cannot clear a flag the resolved layer carries**:
   `needs_web_value` stays on 8 pinned rows here (67 on YC) because the merge
   unions the resolved flags back.
9. **Rows known only from Common Crawl captures, the CMS or the job board have
   no `first_seen`** (14 here, 8 of them with an `entry_date`): the CC captures
   could feed the build's archive layer as IVP's did (458fcc7).
10. **A sibling's row is a surface for the absence test** of a shared company:
    Accel's run had merXu's Nov 2021 round, which this run's English search
    missed.
11. **`graduation-surfaces.py` needs more home editions**: Polish, Russian,
    Greek and a Spanish edition for Latin America (Peru) are missing, so those
    rows were searched in English only until the hand pass; the merXu Series A
    was found that way.

**Two shared-script edits made during this run are uncommitted** and left for
the tooling session: `scripts/stage_words.py` maps "later stage" and
"later-stage" to Growth (the card's "Later-stage" label), and
`scripts/graduation-surfaces.py` gains the `point-nine` entry in FIRM_TERMS.

## Usage line

Weekly (all models) **21% at kickoff, 30% at close**; Fable 4% at both; extra
usage EUR 9.29 of 50, unchanged. The 5-hour window reset mid-run (18% at
kickoff, 30% at close in the new window). Atomico and IVP ran in the same
window, so the nine weekly points are an upper bound for this run. 137 web
searches of the 200 budget, and 28 page fetches.

## Prompt count

**1** at close: the kickoff ("Now please collect Point Nine"). The ingest
approval will make it 2.
