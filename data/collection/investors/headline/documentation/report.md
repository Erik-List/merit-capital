# Headline: Build & Reconciliation Report (PRO-164)

Headline (e.ventures 2012 to 2021, BV Capital 2000 to 2012, Bertelsmann
Ventures from 1997), collected 2026-09-27 under `data/collection/COLLECTION.md`
in one session. Nothing is ingested: the icon upload, `ingest-investor.ts` and
`ingest-companies.ts` wait for Erik's approval (section 14).

## 1. The answer PRO-164 asked for

**268 companies, plain `verify` clean, profile built, review surface checked.
Ingest awaits approval.**

| Done-when item | State |
|---|---|
| Plain `verify` green | `verify: clean` (flagged debt only, section 6) |
| Entity set in `decisions.md` | D1: six exempt reporting advisers (CRDs 304362, 309084, 319198, 323219, 323221, 344374) plus BV Capital Management (160568, last filed 2017); 20 own-desk CIKs in `entities.json` |
| Every row judged, classified, cited | 309 verdicts (275 member, 34 not_member) over 268 published + 163 excluded rows (129 other_desk, 34 not_member); 268/268 classified |
| Coverage per evidence model (D11) | Section 4, never blended |
| Firm profile | `investor/investor.json` + `sources.json`, built by `build-firm-profile.py`, `profile_copy.py` ok |
| `review.html` rendered | Served on the review surface (port 8931) and checked: 268/268 rows flat, profile panel opens with every field's source and basis |
| Cross-investor (rule 10) | 129 shared rows: 120 agree, 9 accepted (sibling side stale, aligned at the wave pass), 0 disagree; 21 namesake pairs ruled distinct, all in Headline's own `companies/cross-rulings.json` |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share of 262 nameable |
|---|---|---|
| Companies | 268 (6 unnameable, excluded from every metric) | |
| Private | 142 | 54% |
| Acquired | 77 | 29% |
| Defunct | 19 | 7% |
| Unknown | 18 | 7% |
| Public | 6 | 2% |
| $1B and above | 20 | 7.6% |
| of which $10B and above | 1 | Mistral $24.4B (EUR 21B, September 2026) |

The 20: Mistral $24.4B, Gopuff $8.5B, AppFolio $7.2B (public), Recursive $4.7B,
AMI Labs $4.5B, Sorare $4.3B (2021, stale), Creditas $3.3B, Black Forest Labs
$3.25B, Flutterwave $3.2B, Icertis $2.8B (2021, stale), Fetch $2.5B (2022,
stale), Owner $2.3B, Sonos $2.15B (public), Acorns $1.9B (2022, stale),
Lightricks $1.8B (2021, stale), Exein $1.7B, Fundamental $1.2B, Staffbase $1.1B
(2022, stale), The RealReal $1.07B (public), Swile $1.0B (2021, stale, floor).
Every mark is web-verified with a citation; public rows carry the market cap of
2026-09-25. The $1B+ share (7.6%) reads right against the profile: an early
book with a growth sleeve since 2014, much of it pre-2012 internet and European
seed.

Entry stage over the 195 rows whose round is on record: Series A 85, Seed 57,
Growth 51, Pre-Seed 2; 67 nameable rows (26%) stay `undetermined` (no source
names the round the firm entered in). Stage source over the decided rows:
web_verified 131, model 31, first_party 21, formd_band 12.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 57 | 7 | 50 | 38 | 12 | **76.0%** |

Coverage 100%. The twelve nos rest on Form D absence (2), a cited end (3) and
the absence test (7). Eleven decided rows rest on an uncited (model) entry
stage; their own evidence decides them and they carry `stage_uncited` with
confidence low.

## 3. The boundary

- **D1 one firm across three renames**: every Bertelsmann Ventures, BV
  Capital, e.ventures and Headline vehicle is in: early funds, growth funds,
  co-invest sleeves and SPVs.
- **D2 Asia desk out** (Infinity Ventures, now Headline Asia: own fund family,
  own managers, no adviser link) and **D3 Brazil desk out** (Redpoint
  e.ventures, now Headline Brazil): 129 rows `other_desk` in `excluded.json`; a
  row stays where a home vehicle held it. Counter-fact raised as X1 (section 9).
- **D4 partner-carried deals out**, **D5 Porsche Ventures II out** (a
  corporate programme the Luxembourg manager advises), **D6/D7** instruments
  and sale consideration as the standing rules.
- Run-time rulings (all flagged for review in `decisions.md`): **R1**
  eVenture Capital Partners was the firm's European branch before 2012 (kaufDA,
  Vicampo, Friendsurance in); **R2** Raisin is sale consideration, Deposit
  Solutions the member (the book loses Raisin's $1.6B mark); **R3** hidden CMS
  docs judged on corroboration (Thrive Market, Flutterwave, Friendsurance in;
  Wawa out); **R4** the CMS "Growth" label sets a stage (scored 3/3), "Early"
  does not; **R5** the Moscow and Kiev deals came from the European fund (BV
  Capital's own February 2012 page), in; **R6** the e.ventures logo wall is the
  firm's own listing (identified home-desk companies in; acquirers, platforms
  and incubators not rows).

## 4. Coverage per evidence regime (D11)

A row is `sec_visible` when the base carries a Form D or EDGAR issuer record
for it, `non_sec` otherwise. The split is reported, never blended.

| | sec_visible | non_sec |
|---|---|---|
| Rows (nameable) | 31 (31) | 237 (231) |
| Membership evidence | site 21, web 8, formd_adjudicated 2 | site 223, web 14 |
| Status | private 16, acquired 7, unknown 4, public 3, defunct 1 | private 126, acquired 70, defunct 18, unknown 14, public 3 |
| Stage decided / undetermined | 27 / 4 (13%) | 168 / 63 (27%) |
| Stage source (decided) | formd_band 12, web_verified 12, model 2, first_party 1 | web_verified 119, model 29, first_party 20 |
| S2A cohort / rate | 8 / 75.0% | 42 / 76.2% (7 censored) |
| $1B+ | 4 (12.9%) | 16 (6.9%) |

The book is 88% `non_sec`: two thirds European or pre-2009, and the US recall
additions came from the logo wall and press, not filings. The SEC layer carried
membership for only two rows (ViaVia and Daily Secret, director-of-record seats);
the firm's site, its Sanity CMS (293 company docs incl. 44 hidden) and the
archived logo wall carried the rest.

## 5. Method deltas

- **Logo-wall layer (R6, invented under §5 when the archive failed):** one CDX
  enumeration of eventures.vc (1,758 URLs) before the Internet Archive
  firewalled the machine again; the WordPress upload filenames name the
  portfolio logos. 166 non-people logos: 46 already known, 119 researched by
  four agents, 89 recall additions (69 members, 20 desk rows).
- **Recall press sweep**: nine more confirmed (Soldsie, All Def Digital, Candid,
  Test.ai, Flowhub, Zeller, Ahara, The Young Turks, Exporo) plus Deposit
  Solutions (R2).
- **Common Crawl** read bvcapital.com's 2008 to 2010 portfolio and team pages;
  its index host refused connections for eventures.vc, eventures.com and
  headline.vc all run.
- **Stage pass** by five research agents on Google News and direct fetches (no
  WebSearch), the CMS "Growth" label scored 3/3 before use.
- **Two rebuilds**: rebuild 1 injected the recall additions and its name-variant
  pass merged Verse into Verse Medical; `never_merge` and rebuild 2 fixed it
  (268 rows, delta of 71 judged).

## 6. Flags and debt behind `verify`

| Flag | Rows | Meaning |
|---|---|---|
| model_disputes_source | 22 | a pre-fill (Wikidata, float, Form D band) overruled by the row's evidence, noted |
| stale | 12 | mark older than 24 months (Sorare, Icertis, Fetch, Acorns, Lightricks, Staffbase, Swile, and five below $1B) |
| stage_uncited | 11 | decided S2A rows on a model stage, confidence low |
| unstable | 6 | the blind 5% disagreements (section 7) |
| cik_weak | 9 | float-sweep registrant joins: six right company, three wrong and quarantined (section 7) |
| identity_unresolved / country_prior | 6 / 6 | title-only CMS docs (Indigo, Journey, Keeper, Nouri, Root, Tandem) |
| cite_pending | 5 | model stages still owed a citation (Fetch, Sonos, AMI Labs, Sorare, Staffbase) |
| stage_disputes_band | 4 | cited round disagrees with the Form D band |
| valuation_floor | 3 | mark is a floor figure |
| boundary | 2 | AppFolio and Sonos, a fact flag from the deterministic layer (unclearable); both have documented venture entries (AppFolio's 2007 Series A led by BV Capital, Sonos' 2005 Series A) |
| formd_adjudicated / unannounced_deal | 2 / 2 | ViaVia and Daily Secret (director of record, medium) |
| city_unknown | 1 | ClarityCare (looked, not placed) |

**Archive debt** (the IA block held the rest of the run, cooldown to about
02:20 on 2026-09-28): headline.com and headline.vc eras, bvcapital.com 2000 to
2007, per-year snapshot parses of eventures.vc, and 18 logo filenames not
identified (dworld, ilemon, kking, muse, savoteur, dparadise, relevant-media,
tx, bump, cake, dragonmeets, folie, lamg, baboo, daguu, huomu, moyogame,
xibao; medicina and firstline have their own portfolio pages to check).

## 7. Standing duties and the A/B pass

- **A/B pass** on the 23 visible rows: one Google News sweep per row for events
  after its mark. No band moved; every later event was talk (Icertis' $5B sale
  talks, Bumble exploring a sale, Gopuff IPO talk), a raise without a stated
  valuation (Icertis $50M, Sorare's eight-figure round of September 2026) or a
  sale of a subsidiary (Acorns sold GoHenry). Fixes: Creditas country BR (the
  NL pre-fill was the holding), Sonim's leftover stage source, Flutterwave's
  doubled note.
- **Momentum slice**: 25 recent hot-sector rows checked mechanically; no new
  $1B+ mark found.
- **Duty 1**: every $1B+ mark web-verified; the nine unicorn-list pre-fills now
  carry cited rounds (their flags cleared).
- **Duty 3 and 8, weak joins and float collisions**: nine registrant joins
  audited. Six are the company (Sonim, Sonos, YuMe, Bumble, Semrush, Bright
  Health). Three were other registrants (Pronto Networks' 2017 float, Flux,
  Pulse) and had also set `is_public`, which would have counted them as IPOs:
  quarantined and the listing cleared.
- **Duty 6**: the unicorn list re-matched with loose normalisation: no miss.
- **Duty 7, blind 5%**: 14 random rows re-judged blind by a subagent that saw only the evidence view (`scratch/blind-rejudge.json`). 7 disagreed on a field. One was the blind judge's error (Scopely: it banded an acquired row by its $4.9B sale; the rule nulls the figure). Three were ours and are corrected: Flowhub's entry is the Series A e.ventures co-led in 2019, not Growth; TVSmiles is now run by Verve Group (acquired, not unknown); All Def Digital entered at the 2014 Series A and its assets were bought by Culture Genesis (acquired, not defunct; a16z's row reads defunct, ruled `accepted`). Three stand with the blind reading in the note (nCircle's Series B rests on a VC-database snippet that would not load; Test.ai has no named buyer; Circadia's LA dateline states no HQ). All six carry `unstable`. **Duty 9 sweep** of the Flowhub class (recall rows staged 'by sequence' without checking earlier rounds): The Young Turks had the same error (its 2017 $20M was its first priced round, Series A, not Growth); Candid's Series A holds.
- **City pass**: the last five nameable rows placed (Openbucks San Jose from its
  Form D, Vulcun and Mira San Francisco, Playbook New York) or recorded unknown
  (ClarityCare).

## 8. Firm profile

HQ San Francisco, CA (ADV principal office, 101 Montgomery Street, the
Presidio; the site lists it with Berlin, Paris, London, Hamburg and Sao
Paulo). Founded 1997. Thesis, the title-tag tagline because the homepage has no
headline element: “Global venture capital helping founders win, bigger.”
History 3 sentences, 79 words. Stage Seed, Series A, Growth. Geo core US and
Europe (US 139, Europe 110 of 262). Focus recomputed from the site's tags: SaaS,
Consumer & Marketplaces, Fintech & Payments, Data Infrastructure (the grind's
own focus column ranks Media 32 and Healthcare 17 above Data Infrastructure 9:
a gap between the site's four tags and the portfolio, flagged, not
overwritten). Range $1.5M (the firm's stated early check) / $10M median (158
entry rounds on record, press-based: Form D covers only 29 members) / $110M
(Fonoa's Series C, led, 12.7% of the $865M growth fund). AUM $4.02B to $4.14B,
the Section 7.B composite of six exempt reporting advisers (no Item 5.F
exists); the top adds Porsche Ventures II, which the Luxembourg manager
advises (D5 keeps its positions out of the portfolio). Nine funds, Global
Growth IV ($865M, 2024) to eVentures Growth ($100M, 2014); four sizes are Form
D offering amounts filed at $0 sold (flagged). Notables: Sonos, Bumble, Mistral,
Farfetch, Goop. 83 people from the site CMS. Icon: the site's vector favicon,
dry run clean (contrast 19:1, ramp 0.92 px); upload waits for the ingest.

## 9. Open rulings for Erik

1. **X1, the regional desks.** The firm calls its 2021 result "a single firm,
   Headline, to invest together globally", while Asia (Headline Asia, own
   funds, own managers) and Brazil (Headline Brazil) have no adviser link. Out
   as derived (129 rows `other_desk`); a reversal is a config change plus a
   delta grind.
2. **R1, R2, R5, R6** (above), each flagged for review. R2 costs the book
   Raisin's $1.6B mark; R5 puts ten Moscow and one Kiev company in.
3. **Sorare vs Accel.** The rule reads 1b_plus (the 2021 $4.3B round is the
   last priced mark); Accel's row reads below_1b on layoffs. Sorare's
   September 2026 round stated no valuation.
4. **Sibling alignment at the wave pass** (all ruled `accepted` in
   Headline's `cross-rulings.json`, the sibling side stale): Accel BetterCloud
   (acquired), Sequoia Bird (acquired out of insolvency), a16z All Def Digital (acquired, asset sale), General Catalyst Coya
   (acquired, Luko 2022), Battery Fundamental (1b_plus, $1.2B), Khosla K2
   Network (a 2012 merger into its own subsidiary, not an exit), 8VC Plated
   (acquired by Albertsons 2017), Redpoint Sonos (market cap $2.15B, 1b_plus),
   Accel Sorare (item 3). Also for the wave pass, same band: Redpoint Owner's
   citation is dead, Y Combinator Flutterwave's citation is dead, Spark Clyde
   (press says Headline led the Series B; assets to Cover Genius March 2023),
   Redpoint Fanhattan (sale closed 2014, not 2016).

## 10. Rebuilds and deltas

Two rebuilds, both before the grind closed: rebuild 1 injected the 89 recall
additions (and wrongly merged Verse into Verse Medical); rebuild 2 fixed it with
`never_merge`. The post-rebuild delta (71 rows) was judged in full. No rebuild
after the last pass.

## 11. Playbook write-backs proposed (not applied mid-wave)

For the tooling session, as COLLECTION.md and script changes:

1. **§5, the upload-filename layer.** When the archive blocks, one CDX
   enumeration of a WordPress site's `/wp-content/uploads/` lists the logo
   wall by filename; identify each logo and judge it as a site listing
   (acquirers, platforms and incubators are not rows).
2. **§8 duty 8, a wrong registrant join sets `is_public` too.** Quarantining
   the float is not enough: clear `is_public` and `public_since`, or the row
   counts as an IPO (Pronto, Flux, Pulse). And the duty-3 list must read the
   exported view: `cik_weak` appears in `base.csv`, not in `base.json` or the
   overlay.
3. **`run.py record` note merge**: a new note inside the stored one replaces
   it (a fragment silently truncates the note); keep the old note instead.
4. **`edgar-entities.py`** drops entities whose seed query returns a single
   EDGAR company page (Headline lost US VII, Global Growth IV, the SPVs and
   the BV Capital funds until re-added by hand).
5. **ADV 7.B parse**: a fund whose value prints at the top of the next page
   takes the next fund's value (Headline US VI read as Growth III's).
6. **`build-company-base.py` name-variant merge** joined Verse and Verse
   Medical; namesake prefixes need a guard.
7. **`profile_copy.notable_problems`** matches the base name, not
   `names.published`, so a notable cannot read "Mistral AI" while the row is
   "Mistral".
8. **`focus_crosswalk` is case-sensitive**: lowercase keys never matched the
   site's capitalised tags, and the build fell back silently.
9. **Uncommitted shared-script hunk, for the tooling session to land**:
   `scripts/graduation-surfaces.py` FIRM_TERMS gained
   `"headline": '("e.ventures" OR "BV Capital" OR "Headline")'`, which the
   graduation pass used; the firm's three names need the OR query.
10. **Rule-10 rulings belong in the investor's own `cross-rulings.json`**: this
   run first wrote its 21 namesake pairs into the shared file and moved them
   before close (shared file back to HEAD); a guard in `verify` for a shared
   file edited mid-wave would catch it.

## 12. Usage line

Kickoff: 5-hour 5%, weekly all models 80%, weekly Fable 82%. Close: weekly all
models 96%, weekly Fable 85% (reset 2026-09-29 18:00 UTC). 268 published rows
(431 judged including exclusions). Five research subagents on the stage pass,
four on the logo wall, one blind re-judge. Two context compactions.

## 13. Prompt count

3 so far: the kickoff and two "continue" prompts after context compactions.
Final after the ingest decision.

## 14. Ingest request (not run)

Order for a first-time investor: icon upload
(`fetch-investor-icon.ts headline <favicon.svg>`), `ingest-investor.ts
headline`, then `ingest-companies.ts headline` (268 companies). Nothing has
been written to the database.
