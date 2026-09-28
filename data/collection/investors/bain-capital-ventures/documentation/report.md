# Bain Capital Ventures: Build & Reconciliation Report (PRO-162)

**Linear issue** PRO-162 · **slug** `bain-capital-ventures` · one run under the merged shape of
`data/collection/COLLECTION.md`, in two sessions (the second on Erik's "continue with cc", with Common
Crawl carrying the archive layer while the Internet Archive blocked this machine) · report written
2026-09-27. **Not ingested: the ingest waits on Erik's approval (section 14).**

---

## 1. The answer PRO-162 asked for

**The base is 414 companies (416 before Erik's ruling of 2026-09-28, section 9). Plain `verify` (links checked) has one open item, Celestia's country,
which needs a one-line tooling fix (section 9).** BCV has its own adviser (Bain Capital Ventures, LP,
CRD 145652), and Bain Capital Crypto sits under it, so both are in with no desk partition (D1).
Bain Capital's generalist-fund book that the firm's 2003-2010 pages carried is out (78 rows, R1), and
every transaction in which BCV with its co-investors took control is out (33 rows, D4).

| Done-when item | State |
|---|---|
| Plain `verify` green | One problem: `celestia: no hq_country` (Liechtenstein is missing from run.py's ISO table; section 9) |
| Every row judged, classified, cited | 664 verdicts on 414 published + 228 excluded rows; 414/414 classified |
| Firm profile | `investor/investor.json` + `sources.json`, built by `build-firm-profile.py`, `profile_copy.py` ok |
| `review.html` rendered | Served on the review surface and checked (416/416 before the ruling; re-rendered at 414) |
| Cross-investor (rule 10) | 243 shared rows: 212 agree, 31 accepted, 0 disagree; 24 namesake pairs ruled distinct |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 414 | |
| Private | 200 | 48% |
| Acquired | 181 | 44% |
| Unknown | 17 | 4% |
| Public | 10 | 2% |
| Defunct | 6 | 1% |
| $1B and above | 49 | 11.8% |
| of which $10B and above | 7 | Cognition $48B, Crusoe $30.9B, Rubrik $22.7B, Etched $21B, DocuSign $12.6B, Poolside $12B, DCG $10B |

Entry stage: Seed 108, Growth 102, Series A 87, Pre-Seed 2, round not on record 117 (mostly pre-2010
rows whose round no source names). Headquarters: US 376, Canada 8, UK 6, Israel 5, France 3,
Germany 3, India 3. Membership rests on the firm's own listing for 408 rows, a Form D ruled by the
judge for 4, a fund filing for 1 and the firm's own post for 1 (Cogsy).

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 108 | 13 | 95 | 70 | 25 | **73.7%** |

Coverage 100%. The 25 nos rest on the Form D absence (2), a cited end (9: an acquisition or shutdown
before any later round) and the dated absence test over the named surfaces (14). DCG's yes rests on
its 2021 priced secondary sale at $10B (open ruling, section 9).

## 3. The boundary: heritage and control

- **R1, the generalist-fund heritage book (78 rows out).** The firm's 2006 page files Bain Capital's
  deals since 1984 under its own portfolio. A row is out when its only Bain holder was a generalist
  fund: entries before the first venture vehicle (Bain Capital Venture Fund, L.P., which held
  Recruitsoft from November 1999), and archive-only rows that Bain Capital Private Equity's own
  portfolio list carries while no record names a venture vehicle (`sources/web/bain-pe-portfolio.json`;
  that list leaves out the venture funds' own positions of the same years, Taleo, Vonage, Tengion,
  aPriori). 21 of these rest on that list at medium confidence, several of them 1999-2002 deals
  (iWon, NetLibrary, ProfitLogic, Shopping.com, eTranslate, Imagitas) where the 1999 venture fund could
  in principle have co-invested; flagged for Erik under COLLECTION.md s9 trigger 2.
- **D4, control positions (33 rows, about 19 companies).** SolarWinds (S-1: investors led by BCV and
  Insight bought 67.8% in the December 2005 recapitalisation; Insight's run excluded the same deal),
  SurveyMonkey (Spectrum and Bain bought a majority in 2009), Zelis (the 2019 Parthenon/Bain merger),
  Air Medical Group (AMGH), iPay ("our new majority shareholders"), M/C Communications, OneSource,
  Publishing Group of America, USinternetworking, Blue Coat, BMC, the 1990s buyouts (Gartner,
  Experian, Waters, Dade Behring, Physio-Control, Wesley Jessen, Stage Stores, DDi, STATS ChipPAC,
  SMTC, ICS, Nutraceutical). The Syncapay lineage (Swift Prepaid, daVinci Payments, Onbe) is out as not verified to be a venture investment (Erik, 2026-09-28).
- **T3 placements into listed companies**: US LEC, EDGAR Online, The Princeton Review, CTC
  Communications, Open Text, Instinet.
- **Sale consideration**: Signify Health (stock for Remedy Partners), and the Radionomy and Datica
  renderings folded into the positions BCV actually bought (TargetSpot, Sansoro Health).

The profile's history says it: "The track record on this page covers its minority venture stakes;
companies bought outright and Bain Capital's earlier deals are left out."

## 4. Coverage per evidence regime

- **Live site**: the public Sanity CMS (280 portfolio docs) plus Bain Capital Crypto's list (18); a
  compliance list (R3: 2007-vintage funds, 10%+ stakes), so absence from it is not evidence.
- **Archive**: Internet Archive for 2003 and 2006 (cached before the block); Common Crawl for 2010 to
  2024 (old ARC collections held 2010 and 2012; WordPress-era listings and company pages 2016-2022).
  **Debt: 45 Internet Archive captures of 2007-2009 are unread** (the block, section 5); rows listed
  only in those years and gone by 2010 may be missing.
- **Form D**: roster-name sweep over 66 people with tenure windows; the related persons' filed
  addresses (`scratch/formd-addr.py`) decided the 41 in-tenure name matches.
- **Exit side**: EDGAR full-text on seven fund phrases (complete, no failed windows); all 96
  third-party and ownership registrants triaged (`scratch/recall/fts-triage.json`): 81 in the base,
  zero missing companies.
- **Wikipedia insource** (63 articles) and **Google News** per row (the firm-news sweep, 639 rows).
- **Recall probe**: one addition (Cogsy, the firm's own seed post), rejections in
  `scratch/recall/rejections.json`.

## 5. Method deltas

- **Common Crawl as the archive during an IA block** (Erik's "continue with cc"), through the static
  cluster index. **The IA block outlasted a four-hour cooldown**: the first request after the 240-minute
  cooldown ended (22:20 UTC) was refused and the machine-wide cooldown doubled to 480 minutes.
- **Form D related-person addresses** as membership evidence: a seat filed at the firm's own office
  (111 Huntington Avenue, 200 Clarendon Street) corroborates a common name; a home or company address
  with nothing else does not. Also identified AMGH as Air Medical (Bain PE partners on the filing).
- **Bain Capital Private Equity's portfolio list as the heritage discriminator** (section 3).
- **Rebuild repairs**: the one rebuild moved 17 verdicts from excluded rows onto name-variant renderings
  (two onto other companies: Ameritrade's onto the 2006 Shopping.com row, Stream International's onto
  the Stream Global Services Form D row), and merge groups whose canonical was excluded resurfaced
  their duplicates. Restored by hand under the record lock; the third build was clean.
- **Parallel judges**: seven classification judges and two graduation judges from written briefs
  (`scratch/JUDGE-BRIEF.md`, `GRAD-BRIEF.md`), per-judge news caches (`NQ_TAG`), recording under the
  per-investor lock; `judge_lib.GRADLINES` writes the absence test's surface lines.

## 6. Flags and debt behind `verify`

On the 416 published rows: `model_disputes_source` 33, `stage_disputes_band` 26, `stale` 25,
`city_unknown` 14, `unicorn_name_match` 12, `cik_weak` 3, `stage_uncited` 3 (
TrueMotion, Stamped and one more rest on their own evidence at low confidence),
`identity_conflated` 1, `identity_unresolved` 1 (Nerati, unnameable). Archive debt: 2007-2009.
Base-build note: 5 multi-issuer Form D filings name two base companies (co-issuers), not examined.

## 7. Standing duties and the A/B pass

Visible slice checked: public caps pinned (Lime $1.9B, ACV $1.78B, Rapid7 $783M, DocuSign $12.62B,
Flywire $2.12B, Rubrik $22.71B, as of 2026-09-25); DCG, Etched, Ankorstore, Mirakl, Pleo and Simile
moved from the unicorn list to their rounds' own citations; Attentive's mark aligned with Atomico's
$5B (2021); momentum-slice checks by the judges on 2021+ hot-sector rows (Cognition $48B, Crusoe
$30.9B, Poolside $12B, Wonder $9B, Lumilens, Mind Robotics, Norm Ai, Rillet, ShopMy, Whop fresher than
their siblings). No $1B+ mark rests on a vendor.

## 8. Firm profile

Thesis "Capital's duty to the future." (the homepage headline; competing line the meta description).
History 74 words. HQ Boston, MA (Form ADV principal office). AUM $9,837,931,000 (ADV 2026-03-31, Item
5.F). Funds: 15 entries, Fund 2001 $250M to Fund XI $1.6B (2026); Bain Capital Crypto's funds carry
no citable size and are not listed. Stages Seed, Series A, Growth; geography US, then Europe and
Canada; range $3M to $76M around a $15M median entry round (Form D, derived). Notables LinkedIn,
DocuSign, Rubrik, Redis, Rent the Runway. Individuals 35 (Investing Team and the platform team;
the Operating Team group is unmapped so operations staff stay out). Icon: the site's 512px manifest
icon, dry run clean (0.45x, contrast 4.3:1); upload at ingest.

## 9. Open rulings for Erik

1. **Tooling: add Liechtenstein (LI) to `ISO_OF` in `scripts/run.py`.** Celestia Labs is in Vaduz
   (its registered address); until then `verify` fails that row. No tooling session was running.
2. **Tooling: the rebuild's rename step should count excluded rows as present** (section 5).
3. **R1 scope**: the 21 archive-only rows ruled heritage on the private-equity list (section 3).
4. **Control questions kept as members**: SquareTrade (2012 "$238M growth equity" beside Bain Capital
   Fund X; the merger agreement's "Contingent Consideration attributable to the Bain Capital
   Transaction" reads like acquisition accounting), TravelClick (on both the PE list and BCV's live
   2007-vintage list; the 2007 entry may be a co-investment in Genstar's buyout), Bluestem/Fingerhut
   (the 2004 recapitalisation), Work 'N Gear.
5. **Syncapay lineage** (Swift Prepaid, daVinci, Onbe) ruled control at medium: the release does not
   state the investor group's share of the holding company.
6. **DCG graduation**: its only later priced event is the 2021 secondary sale at $10B; recorded
   graduated at medium (rule 7 refuses a $1B+ row that did not).
7. ~~Director-of-record members at medium: Mynd and Boon~~. **Ruled by Erik, 2026-09-28**: "rm Mynd,
   Boon, Swift, daVinci, Onbe if not verified to be a venture investment". None of the five is
   verified: Mynd and Boon rested only on a venture or operating partner's board seat, and the
   Syncapay lineage on a holding company of unknown ownership. All five are `not_member` with
   `who: erik` (the three Syncapay rows lose the `control_position` code: out as unverified, not as
   proven control). The base is 414 companies after the fifth build (no renames).

## 10. Rebuilds and deltas

One scheduled rebuild after the recall probe, run three times because of the re-keying defect
(section 5), then one final rebuild after the delta for the sneakpeeq/Symphony Commerce merge (one
SEC issuer). Delta: 44 items (39 graduations, Cogsy, Adaptive Innovations split from Adaptive
Security, Bluestem). 55 identity merges, one never-merge pair (the two companies the CMS titles
"Adaptive").

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **Heritage discriminator**: for a firm spun out of a buyout parent, the parent's own portfolio list
   separates the parent's positions from the venture arm's (decisions R1 here).
2. **Form D related-person addresses** as the corroboration test for common-name seats (section 5).
3. **Rebuild re-keying**: copy, not move, a verdict when the source row is excluded (Insight's item 4
   again; it recurred here with two wrong-company moves).
4. **Merge groups with an excluded canonical**: have the build carry the canonical's verdict to the
   group, so the duplicates do not resurface.
5. **CMS title collisions**: two docs with one title fold into one row; bracket the domain at shaping.
6. **IA cooldown**: do not queue a job to fire when a long cooldown ends; plan on Common Crawl.
7. **ISO table**: Liechtenstein (and any other small jurisdiction) for crypto foundations.

## 12. Usage line

Close (2026-09-27, ~23:15 UTC, Opus 5.5, Pro plan): weekly all models 95%, Fable 85%, 5-hour 62%,
extra usage EUR 12.14 of 50 (disabled). Web searches: about 84 of 200 across both sessions and all
judges. Subagents: 7 classification judges, 2 graduation judges, 1 EDGAR triage.

## 13. Prompt count

**2 so far**: the kickoff ("please collect bain capital ventures") and "continue with cc". The ingest
approval would be the third. Corrections from Erik: none.

## 14. Ingest request (not run)

First-time investor, so in this order, each only on Erik's approval (and after the LI fix, or with
Celestia's country accepted as open):

1. `npx tsx scripts/fetch-investor-icon.ts bain-capital-ventures https://baincapitalventures.com/android-chrome-512x512.png`
2. `npx tsx scripts/ingest-investor.ts bain-capital-ventures`
3. `npx tsx scripts/ingest-companies.ts bain-capital-ventures --dry-run`, read the list (a first
   ingest removes nothing), then the same without `--dry-run`: 416 companies.

## Ingest 2026-09-28 (Erik's approval, third prompt)

Erik's third prompt: "rm Mynd, Boon, Swift, daVinci, Onbe if not verified to be a venture investment; afterwards ingest".
The five rows were ruled out (section 9, item 7), the base rebuilt clean at 414, plain `verify` rerun (the one known
item: Celestia's country), then, in order:

| Step | Result |
|---|---|
| `fetch-investor-icon.ts bain-capital-ventures <512px manifest icon>` | Uploaded `investors/bain-capital-ventures-e820755ddb.png` (9,720 bytes); `icon_url` now the bucket URL |
| `ingest-investor.ts bain-capital-ventures` | 1 investor row upserted ("Canada" added to the open geography vocabulary) |
| `ingest-companies.ts bain-capital-ventures --dry-run` | 414 new, 0 removed, from 0 live |
| `ingest-companies.ts bain-capital-ventures` | Upserted 414/414; `public.companies` holds 414 rows for the investor |

Celestia's country is published empty until Liechtenstein is added to `scripts/run.py`'s ISO table and the row is
re-recorded (a one-row re-ingest). Prompt count: **3, final**.
