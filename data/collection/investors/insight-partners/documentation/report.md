# Insight Partners: Build & Reconciliation Report (PRO-165)

**Linear issue** PRO-165 · **slug** `insight-partners` · one run under the merged shape of
`data/collection/COLLECTION.md`, in two sessions (the first stopped on the usage limit at
02:20 UTC; the second resumed at 13:58 UTC) · report written 2026-09-27. **Ingested on 2026-09-27 with Erik's
approval** (last section).

---

## 1. The answer PRO-165 asked for

**The base is 800 companies, plain `verify` is clean (links checked), and every transaction in
which the firm took control is out: 115 rows are excluded as control positions.** The page's
track record covers Insight's minority venture and growth investments only, and the profile says
so in its history.

| Done-when item | State |
|---|---|
| Plain `verify` green with only flagged debt | Clean on 800 rows, link checks included (section 6 lists the flags) |
| `control_position` rows counted | 115 excluded rows, about 90 companies once their holding-company renderings are counted with them (section 3) |
| Profile states the minority-only boundary | History: "The track record on this page covers its minority stakes only; the companies it bought outright are left out." |
| Profile fields populated or null, sourced | `investor/investor.json` and `investor/sources.json`; `profile_copy.py` ok; built by `build-firm-profile.py` |
| `review.html` rendered | Served on the review surface and checked: rows flat, 800 shown, profile panel expands |
| `report.md` with delta outcomes, open rulings, prompt count | This file |
| Closing message with the ingest request | Sent with this report |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 800 | |
| Private | 460 | 58% |
| Acquired | 238 | 30% |
| Unknown | 56 | 7% |
| Public | 25 | 3% |
| Defunct | 21 | 3% |
| $1B and above | 119 | 14.9% |
| of which $10B and above | 13 | Anthropic, OpenAI, Alibaba.com, Databricks, Shopify, JD.com, Fanatics, Fireworks, ClickHouse, DocuSign, Delivery Hero, Checkout.com, JFrog |
| of which $100B and above | 5 | Anthropic $965B, OpenAI $852B, Alibaba.com $273B, Databricks $190B, Shopify $183B |

There is no ceiling on the $1B+ share (Erik, 2026-09-26). Read against the profile: a growth
investor entering at Series B and later, with a $12.5B to $20B flagship, sits naturally near 15%.

Entry stage: Growth 431, Series A 198, Seed 24, Pre-Seed 1, round not on record 146.
Headquarters: US 532, Israel 71, UK 37, Germany 35, Canada 22, Australia 13, France 12, India 10,
Netherlands 9, Brazil 6. Evidence tiers: A 717, B 73, C 10. Membership rests on the firm's own
listing for 788 rows, on press for 6, on a Form D ruled by the judge for 4 and on a fund filing
for 2. `defunct` is undercounted by construction (§6): the column is the last known state.

### S2A block

Of 24 seed entries, 5 were too recent to count (Flank, Golden Analytics, Hallo Theo, Modus,
Waterlily). Of the 19 that remain, **31.6%** raised a later round (6). Of the 13 that did not, 4
rest on a cited end (a sale or a closure), 8 on the dated absence test over the named surfaces and
1 on the Form D filings.

| Seed entries | Censored | Cohort | Graduated | Rate |
|---|---|---|---|---|
| 24 | 5 | 19 | 6 | 31.6% |

The cohort is small by design: Insight enters at growth rounds, and 79% of the staged rows are
Growth.

## 3. The control-position boundary

The firm makes minority growth investments and buyouts from the same fund family. Each row was
judged on its own entry (R5 in `decisions.md`): control where the firm alone or with co-investors
took at least half the voting equity in the transaction that made it an investor, or where the
company reported a change of control.

- **115 rows excluded as control positions** (`excluded.json`), of which about 25 are the
  holding-company vehicles of the same purchases (Boxer Parent for BMC, Diamond Parent for
  Diligent, Eagle Parent for E2open, Revere Parent for Bullhorn, Whistler Parent for Within3).
- **The largest excluded outcomes** (X1): Dotmatics (sold to Siemens for $5.1B, 2025), Inovalon
  ($7.3B take-private with a consortium, 2021), CoreLogic, now Cotality (about $6B with Stone
  Point, 2021), Kaseya, Diligent, E2open ($2.57B listing, 2021), Tricentis (the $1.33B GTCR
  investment, 2024), SolarWinds, Planview, commercetools ($1.9B in 2021), Optimizely (Episerver,
  bought for $1.16B in 2018), Turnitin ($752M, 2014) and Enverus.
- **Members that were bought later stay members**, because their entry was a minority round:
  Armis, Recorded Future, Veeam, Alteryx, AMCS, LeanTaaS, Bynder, DistroKid, Illuminate Education,
  Achieve3000 (R5).
- **New this session from the counsel's notes** (R11): commercetools and Folhamatic, whose only
  transaction was the majority purchase. commercetools was a $1B+ member until then.
- **Low or medium confidence, listed for Erik**: Digital Room, Academic Partnerships, VisualLogix
  (ownership evidence only, R9), Vertafore (date coincidence), Key Data Systems (majority owner by
  2018 on a single transaction, medium).

## 4. Coverage per evidence regime

| Surface | What it gave |
|---|---|
| The firm's live site (856 panels, insight/v1 endpoint) | 788 of the 800 members; first-investment month and year; deal partners |
| The firm's posts (1,941) | Entry-round citations; the control announcements |
| The firm's counsel's deal notes (Willkie, 244 notes) | Control evidence (Enverus, commercetools, Folhamatic, SignUp), two recall additions (Inforcer, Flightkeys), fund sizes |
| Internet Archive | 2000 list (43), 2006 and 2008 PHP pages, 2009 to 2012 and 2019 to 2026 company pages |
| **Common Crawl** (new this run for Insight, while the Internet Archive refused this machine) | Full portfolio listings with names for 2010, 2012, 2013, 2017 and 2018 (134 to 306 companies each, with the firm's own active/prior status), 3,254 company-page captures, and the investment-team pages of 2010 to 2022 |
| EDGAR (Form D, full text, 13F, SC 13D/G) | 1,107 partner-matched accessions after the archived roster; entry rounds; the control vehicles (R1) |
| Form ADV (CRD 142994) | AUM, offices, 175 private funds |
| Google News and web search | S2A surfaces, control checks, stage citations; 89 of 200 web searches used |

The archive layer (section 10) added 19 companies the live site no longer lists under their own
names (and corroborated three recall additions: Intent Media, Path, Payfactors), and folded every
other archive slug onto its existing row through a curated map of 243 slug variants
(`scratch/wayback-name-map.json`). The archived team pages gave the roster 36 departed or former
investing people with seat titles, which dates departures the live site cannot.

## 5. Method deltas

- **Common Crawl as the archive layer during an IA block**, through the static index on the data
  host (`scratch/cc-cluster.py`, `cc-fetch.py`, `cc-parse.py`, `cc-roster.py`, adapted from
  Balderton). The old ARC collections (2009 to 2012) held Insight's 2010 and 2012 listings.
- **Panels under an acquirer's name** (R10): five live-site rows carry the backed company's text
  under the buyer's name; the archive names the backed company. Swept across all 856 panels.
- **Counsel's notes as a control surface** (R11).
- **Weak-join quarantine** found six floats from wrong registrants still sitting under judged
  statuses (NNG Inc at $71.5B, NMI Holdings at $2.7B, SLM Corp, Genesis Group Holdings, Turing
  Holding, INKY Inc) and two statuses taken from them (Unit read as acquired from Unit Corp, an
  oil company; Noble from Noble Corp, the driller). All corrected.
- **Rebuild repairs**: the one rebuild renamed 22 rows; 8 renamed variant rows escaped their
  identity merges, and the re-keying moved 15 control verdicts from site rows (Kaseya, CentralReach,
  E2open, Thycotic, Real) onto holding-company renderings. Merges were pointed at the new slugs and
  the verdicts restored under both keys (known class: rename disarms merge).

## 6. Flags and debt behind `verify`

On the 800 published rows: `stage_uncited` 229 (a model stage on a row under $1B; allowed),
`stale` 58, `model_disputes_source` 57, `unicorn_name_match` 52, `stage_disputes_band` 35,
`city_unknown` 34, `momentum_ruled_out` 23, `cik_weak` 17, `cite_pending` 4 (Alibaba.com,
DocuSign, Persona, Simply: $1B+ rows whose entry round no source names), `rule_a_below_1b` 2
(Mosyle, Filevine), `entry_anchor_weak` 2, `unstable` 1 (B2B-Center, section 7). Cross-investor:
311 rows shared, 284 agree, 27 accepted (the sibling is stale or wrong, for the wave alignment),
0 disagree; 16 namesake pairs ruled distinct in `companies/cross-rulings.json`.

## 7. Standing duties and the A/B pass

- **Duty 1 and the A/B pass**: 25 public caps fetched, 33 valuation pins, 68 entry-round citations
  for $1B+ rows (49 in the first session, 19 in the second after the research agent failed on the
  session limit: 17 cited, Persona and Simply `cite_pending`).
- **Duty 2**: every `not_graduated` has its absence test or a cited end; none is $1B+ or public.
- **Duty 3 and 8**: the weak-join audit above.
- **Duty 4 and 5**: public rows carry fresh caps; acquired rows from the float layer checked in the
  same audit.
- **Duty 6**: the unicorn list re-intersected with loose normalisation; no misses.
- **Duty 7**: 41 rows (5% of members), 164 values re-judged blind: **5 disagreements**. Adjudicated:
  B2B-Center's entry to Growth (counsel's note, "a significant minority stake"); the other four
  recorded values upheld. The sample also exposed a duplicate the archive had created (CrossBorder
  Solutions is Exactera), which led to the rename sweep in R10.
- **Duty 9**: the "status unknown" class swept against the firm's own current investments: one
  fixed (Famous, private).

## 8. Firm profile

Thesis: “We scale ambition at every stage.” (the homepage title tag and section heading, read
2026-09-27). History: founded New York 1995 by Jeff Horing and Jerry Murdock; Twitter, Shopify,
Alibaba, Wiz, monday.com; about $92 billion managed after the $20 billion Fund XII of 2022; the
minority-only boundary. AUM $92,178,934,483 (Form ADV Item 5.F, 2026-09-09). HQ New York, NY.
Funds: 11 from the firm's releases and counsel's notes (XIII family $12.5B 2025 down to
Coinvestment Fund II $450M 2011); no accessions (the vehicles file "Indefinite" offerings).
Range $5M to $500M, the firm's own words (January 2025), median $24M over 144 partner-anchored
Form D entry rounds. Stage Seed, Series A, Growth. Geo core US, other Europe and Israel. Focus
recomputed from the site's 29 sector tags: SaaS, Fintech & Payments, Healthcare & Bio, Consumer &
Marketplaces, Data Infrastructure, Security, AI & Applied AI, DevTools & APIs. Notables: OpenAI,
Twitter, Anthropic, Shopify, Alibaba.com. Team: 140 current, 26 departed. Icon: the site's "IP"
mark, dry run only (5.3:1 contrast, 0.5 px ramp, no enlargement).

HQ note: `firm-offices.py` read the contact page's "36th Floor New York 10036" as the city
"Floor, NY". Fixed in the script on Erik's instruction (9e12be5), with a judged override
(`profile.hq_override`) for any future reading that is obviously wrong; `--all --check` changed
only Insight.

## 9. Open rulings for Erik

1. **Ecova and Cadence Network** (R10): ENGIE Insight Services (Ecova) is out as sale
   consideration and Cadence Network is in, on company databases plus the firm's Ecova page.
2. **MICEX and RBC**: the firm's page for "Micex" (2013 to 2021) became the RBC Information Systems
   page in 2023 with the same MICEX text. Read as one position in a listed company, out under T3.
3. **WeWork PIPE** (R8): not added; the firm's shares come from the PIPE at the de-SPAC.
4. **Low-confidence control rows**: Digital Room, Academic Partnerships, VisualLogix (low),
   Vertafore and Key Data Systems (medium).
5. **Flagged members**: Marigold (Campaign Monitor), PayIt, Flightkeys (a "strategic growth
   investment" whose size of stake is not stated).
6. **Niche**: a company page on the firm's 2006 site that could not be read while the Internet
   Archive refused this machine; published as a member with nothing else established.
7. **Four $1B+ rows with no named entry round**: Alibaba.com, DocuSign, Persona, Simply.
8. **Tricentis moved to control** (its 2017 entry is the majority purchase), and **commercetools
   and Folhamatic** moved to control this session (R11).
9. **Rule A rows**: Mosyle and Filevine read below $1B (vendor marks only).
10. **Departed partners' seats** (R12): 26 Form D rows ruled out; the builder's three-year
    snapshot minimum kept them in.

## 10. Rebuilds and deltas

- **Rebuild 1** (after the recall probe and the archive layer): 975 to 862 rows; 22 renames.
- **Delta 1**: 70 rows. 28 members classified (25 archive-listed rows, including the recall
  additions Intent Media, Path and Payfactors, and the recall additions Cadence Network, Inforcer
  and Flightkeys), 4 control positions (Ministry Brands, Spanning, SignUp Software, Key Data Systems), 26
  departed-partner Form D rows and TeamBuy (merger consideration for Dealfind) ruled out.
- **Rebuild 2** (final, needed because the delta ruled membership): 800 rows, no renames. The
  export then caught one more duplicate (Nexus Cognitive is the site's Nexus One), folded before
  the final build. Four archive rows judged in delta 1 turned out to be site rows under other names
  and vanished at the final build (CrossBorder Solutions, Employer Direct Healthcare, MICEX, Nexus
  Cognitive); their answers were removed as stale keys. Excite Japan, the McKinley Group's page
  under its buyer's name, was ruled out at the same time (R10).

## 11. Playbook write-backs proposed (not applied mid-wave)

1. **Common Crawl as the IA-block archive** (PRO-158): promote the cluster.idx route and the
   listing and team-page parsers to `scripts/`; its old ARC collections hold 2009 to 2012.
2. **Acquirer-labelled panels** (R10) and **"formerly"/"fka" panels**: add a sweep comparing each
   panel's description subject with its name, before the rebuild.
3. **Counsel's notes as a control surface** (R11) for buyout-capable firms.
4. **Rebuild re-keying**: copy rather than move a ledger verdict when the source row is an
   excluded site row, and carry identity merges across renames (8 escaped here).
5. **Tenure filter**: a roster person absent from the live team whose last archived year is 3+
   years before a filing should count as departed even with fewer than three capture years.
6. **`firm-offices.py` city parse**: done (9e12be5), with the judged override, on Erik's
   instruction at the ingest approval.
7. **`verify` trap matching** strips descriptor words ("Systems"), so a trap for Resolve Systems
   fired on Resolve; match on the slug first even after the slug leaves the base.
8. **Notables**: `build-firm-profile.py` checks names against base names, `verify` against
   published names; they disagree when `names.published` renames a notable row.
9. **A judged status that disputes a float should null the float** at export (NNG, NMI).
10. **`verify` prints only the first 80 problems**; `graduation-surfaces.py` needs
    `investor/investor.json` to exist.
11. **The Internet Archive blocked again after 20 requests at 1/s**, ten minutes after the previous
    cooldown ended; Google News answered 429 in the second session. Both want a longer settle.
12. **Run-time rulings R1 to R12** as candidates for the standing rules on control positions.

## 12. Usage line

Kickoff (2026-09-26 23:15 UTC): weekly all models 40%, Fable 16%, 5-hour 69%, extra usage EUR
9.29 of 50. The first session hit the usage limit at 02:20 UTC. Close (2026-09-27, second session,
on Opus 5.5): weekly all models 76%, Fable 81%, 5-hour 11%, extra usage EUR 12.14 of 50. Web
searches: 89 of 200 across both sessions.

## 13. Prompt count

**3, final**: the kickoff ("please collect insight partners"), "continue" after the usage limit,
and the ingest approval ("ingest, fix the script and like now allow model override if obvious
flaw"). Corrections from Erik: none; one tooling request (the office parse and its override).

## 14. Ingest request (not run)

First-time investor, so in this order, each only on Erik's approval:

1. `npx tsx scripts/fetch-investor-icon.ts insight-partners https://www.insightpartners.com/wp-content/themes/insight/images/cropped-IP-icon-orange-grey-rgb-270x270.png`
2. `npx tsx scripts/ingest-investor.ts insight-partners`
3. `npx tsx scripts/ingest-companies.ts insight-partners --dry-run`, read the list (a first
   ingest removes nothing), then the same without `--dry-run`: 800 companies.

## Ingest 2026-09-27 (Erik's approval, third prompt)

Erik approved with "ingest, fix the script and like now allow model override if obvious flaw".
The office script was fixed first (9e12be5), so the profile's New York, NY comes from the rule
itself. Then, in the order for a first-time investor:

| Step | Result |
|---|---|
| Icon upload | `investors/insight-partners-0c2f26f337.png` in the Icon Images bucket (the firm's "IP" disc, contrast 5.3:1, ramp 0.50 px, no enlargement) |
| `ingest-investor.ts insight-partners` | 1 investor row upserted |
| `ingest-companies.ts insight-partners --dry-run` | Plan: 800 upserted (800 new), 0 removed, from 0 live |
| `ingest-companies.ts insight-partners` | 800 of 800 upserted |
| Readback (`scratch/readback.ts`) | csv 800, live 800, missing 0, differing cells 0 |

The database derived from the rows: 800 companies, 25 public, 119 at $1B and above, 13 at $10B
and above, 5 at $100B and above, and S2A 31.6% on a cohort of 19 (24 seed entries, 5 censored).
The open rulings of section 9 stand as applied; a ruling that changes a row needs a re-export and
a fresh approval before the next ingest.
