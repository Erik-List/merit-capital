# Company Base v0 — Sequoia Capital (US/EU) — Build & Reconciliation Report

Built: 2026-07-19 · Window: 2006–2026 (20 years) · Entity: Sequoia Capital US/EU (post-2024 split; HongShan and Peak XV excluded per attribution rule)

## 1. What this is

Company Base v0 is the first bottom-up reconstruction of Sequoia's investable universe (the denominator for all merit metrics), built exclusively from free public sources. Every row carries per-source evidence so it can be manually reconciled. This document explains how it was built, what each source contributed, and where the known weaknesses are.

**Files:**
- `sequoia-capital.csv` / `.json` — the base, one row per company candidate
- `other-desk-companies.csv` — HongShan / Peak XV companies, partitioned out of the US/EU denominator
- `../entities/sequoia-capital.json` — the investor's own vehicles (CIK → desk); one table serving role resolution, fund exclusion and lineage
- Raw evidence: `../sources/wayback/` (snapshots + parsed years), `../sources/edgar/` (`edgar-companies.json`, `formd-sweep.json`), `../../filings/edgar-headers/` (1,658 cached submission headers — the evidence of record)
- Scripts (reproducible for any investor): `scripts/wayback-pull.py`, `scripts/partner-roster.py`, `scripts/formd-query.py`, `scripts/edgar-entities.py`, `scripts/edgar-companies.py`, `scripts/build-company-base.py`

## 2. Headline numbers

| Metric | Value |
|---|---|
| Total candidate rows | **1,293** |
| Tier A (2+ independent sources) | **279** — `auto_confirmed` |
| Tier B (single-source listing) | 719 — `needs_review` |
| Tier C (Form D / EDGAR only) | 295 — `needs_review` |
| Fund vehicles dropped | 182 issuers / 253 filings (pooled) + 16 non-portfolio-industry |
| Other-desk companies partitioned out | 22 (21 china, 1 india) |
| Ex-partner deals removed | 105 |
| Duplicate name-variants merged | 94 (6 kept separate) |
| Rows flagged (kept, other evidence) | 9 ex-partner / 19 ambiguous industry |
| Entity registry | 301 vehicles (151 us-eu, 75 china, 39 india, 11 israel, 25 external) |

## 3. The four evidence layers

### Layer 1 — Wayback portfolio listings (primary denominator)
Sequoia's own portfolio pages, one snapshot per year, four site eras:

| Era | Path | Years | Yield |
|---|---|---|---|
| A | `/company/<slug>` | 2006–2009 | 284/66/87/24 slugs per year (enumerated from CDX index) |
| B | `/us/<slug>` via `/sitemap` + homepage | 2010–2014 | 275–377 paths per year (2013–14 thin: site redesign) |
| C | `/companies/` single page | 2015–2021 | 188 → 290 companies, **with sector + partner tags** |
| D | `/our-companies/` | 2021–2026 | 32 entries per year only (lazy-loaded page; see §5) |

Because these are Sequoia's own listings captured over time, they also recover companies later removed from the live site (survivorship correction).

### Layer 1b — The investor's own site API (current portfolio)

All three SEC/archive layers structurally miss recent private companies, and the gap was concrete: **Linear, Etched and Rillet were absent from the base entirely.** Three independent causes stack up:

- the modern portfolio page is JS-rendered and has **no per-company URLs**, so the CDX enumeration that rescued era A and the partner roster has nothing to enumerate — the archive holds only `?_categories=…` filter variants of one listing page;
- recent startups increasingly raise under **Section 4(a)(2)** rather than Reg D and file no Form D at all. Etched and Rillet file nothing; only third-party SPVs do (`Etched AI Mar 2024 a Series of CGF` via Sydecar, `Rillet I a Series of FOG Ventures`), and those name the syndicate, not Sequoia;
- neither has IPO'd, so EDGAR is silent.

sequoiacap.com runs WordPress with an **open REST API**. `/wp-json/wp/v2/types` exposes `company`, `team-member` and `founder` post types; paginating `company` returns **418 companies** with slug, canonical URL and sector categories (from `class_list`), plus 59 current team members. This is the investor's own authoritative, current list — the strongest single source in the build, and it counts as an independent source for tiering.

Reusable pattern for the next investor, in order of preference: **(1)** WordPress REST (`/wp-json/wp/v2/types` → find the post type → paginate); **(2)** Next.js `__NEXT_DATA__` or `/_next/data/<build>/*.json`; **(3)** any SPA — watch XHR in the browser pane, then call that endpoint directly; **(4)** last resort, render headless and parse the DOM. Collector: `scripts/site-portfolio.py`.

### Layer 2 — EDGAR public-market filings
Driven by CIK, not keyword. Every vehicle in the entity registry is crawled via the SEC **submissions API** (filings *filed by* that entity — zero text-mention false positives), then each unique filing's **submission header** is read for authoritative roles: `SUBJECT COMPANY:`/`FILED BY:` on 13D/G, `ISSUER:`/`REPORTING-OWNER:` on Forms 3/4/5. **1,658 unique filings → 141 companies** (115 us-eu, 23 china, 2 israel, 1 india), each with accessions, filer CIKs and desk.

This is evidence a company reached public markets — *not* an outcome classification. It misses private winners (a pre-IPO Stripe files no 13D/G) and includes failed IPOs.

### Layer 3 — SEC Form D bulk data (private board-seat layer)
All 74 quarterly structured datasets (2008Q1–2026Q2) scanned for **285 partner names** from the roster (see below): **1,679 filings → 890 distinct private issuers**, with board role, round size, and dates. Of these, 241 filings are fund vehicles rather than portfolio companies and are filtered out (see §3a).

## 3a. Excluding what is not a portfolio company

Three populations contaminate a naive collection, each with its own filter:

**1. Fund vehicles (funds, FoFs, GP entities).** A fund raise is a Reg D offering like any other, and a fund's "related persons" are its GPs — so `Sequoia Capital Fund, L.P.`, `Accel XV Entrepreneurs L.P.` and `S Capital III, L.P.` all surface in a partner-name sweep. Filtered by **issuer self-declaration**, using both flags Form D provides:

- `INDUSTRYGROUPTYPE == "Pooled Investment Fund"` — the industry category, and
- `ISPOOLEDINVESTMENTFUNDTYPE == true` — a *separate boolean*, set by funds that categorised themselves elsewhere. These diverge materially: in 2025Q1, 9,645 filings set the boolean but only 9,196 carry the label, the gap being REITs (88), Other Real Estate (91) and Investing (52). `Northern Tower Fund I/II` are exactly this case — real-estate funds labelled `REITS and Finance`.

**182 issuers / 253 filings dropped.**

A fund that ticks neither flag still self-classifies into a financial or property branch. Those rows are dropped **only when Form D is their sole evidence** (`Investing`, `Investment Banking`, `Commercial Banking`, `REITS and Finance`, `Residential`, `Commercial`, `Construction` — 16 rows, e.g. `Parkside Manor Fund, LLC`). Two branches are deliberately **excluded** from that rule and merely flagged for review: `Other Banking and Financial Services` and `Other Real Estate` are exactly where fintech and proptech startups classify themselves — Prosper, SoFi, LendingHome, Yapstone and Fundrise all sit there, and an earlier, broader version of this rule wrongly removed all of them.

**2. EDGAR co-filers.** One position is held through a stack of vehicles — a single DoorDash Form 4 names 11 parties: DoorDash plus 10 Sequoia entities. Full-text search returned them in a flat list with no roles, so a name-shape heuristic had to guess which was the company, and it misread GP/management vehicles as portfolio companies. Now resolved structurally: the **submission header** labels every party, so co-filers are never mistaken for the subject.

**3. Text-mention matches.** FTS matched the string `"Sequoia Capital"` anywhere in a document — **713 of its 1,447 filings (49%) had no Sequoia entity as a named party at all.** These were acquisition filings that merely mention Sequoia in a merger agreement: HotJobs was *Yahoo's* 13D, Latitude Communications was *Cisco's*, Genesis Microchip was *Pixelworks'*, Juniper was *NetScreen's*. Eliminated at source by driving collection from entity CIKs rather than keywords.

**Entity form.** A venture-backed operating company is a corporation or an LLC, essentially never a limited partnership. Rows whose legal name carries an `L.P.`/`LP` suffix and which have no listing evidence are funds, SPVs or professional partnerships — 3 dropped (`NAH SERIES-XMCP OPPORTUNITY FUND LP`, `MEDICAL CENTER SURGERY ASSOCIATES, L.P.`, `MARBELLA PLACE INVESTORS LP`). This reads the legal entity type, not name content, and is the only remaining rule keyed on the name string.

The result is that **no name-content pattern filter remains anywhere in the pipeline.** Everything is either a structured data field (`INDUSTRYGROUPTYPE`) or an authoritative role label from the filing itself.

### Desk attribution and the other-desk partition

`entities/sequoia-capital.json` maps every one of the investor's 301 vehicles to a desk (151 us-eu, 75 china, 39 india, 11 israel, 25 external). Because filings carry filer CIKs, a company's desk follows deterministically from *who filed on it* rather than from a name regex. Companies whose only investor evidence is a China/India-desk entity leave the US/EU denominator into `other-desk-companies.csv` (**22 rows: 21 china, 1 india**) under the decision-desk attribution rule. Wayback presence outranks a single foreign-desk filing, since a listing on Sequoia's own US site is direct evidence of US/EU ownership.

Two by-products worth noting:
- **`external` (25 entities).** Co-filer discovery necessarily picks up unrelated institutions that merely appear on the same filing — Ameriprise, GIC, SINA, Hermes. Crawling their submissions would have imported their entire portfolios as Sequoia's. They are identified by *not* matching the partner roster and excluded from crawling.
- **`israel` (11 entities, 2 companies).** Sequoia Israel is neither US/EU nor an excluded desk. Currently retained in the base; needs an explicit in-scope decision.

### Partner roster and tenure windows

The roster is the input to the Form D sweep, so its completeness bounds that layer's recall and its tenure data bounds precision. Both were previously broken.

The modern `/people/` listing pages are JS-rendered — the 2020 snapshot's HTML contains 16 partners, and Pat Grady, a sitting partner, is absent entirely. Parsing those pages produced 90 names with wrong tenure: Grady showed `2011–2012`.

**Fix: enumerate individual profile pages from the Wayback CDX index rather than parsing listing pages.** The archive records every `/people/<slug>` URL it ever captured, independent of how the listing rendered — the same technique that took era-A companies from 42 to 284. Result: **286 people, 2006–2026**, with tenure from each person's snapshot span. Spot-checked against known facts: Grady `2016–2026`, Botha `2006–2026`, Sonya Huang `2019–2026`, David Cahn `2023–2026`, Moritz `2006–2023` (he stepped back in 2023), Sameer Gandhi `2006–2008` (left for Accel in 2008).

**Tenure check.** Form D related-persons are the *issuer's* officers and directors, not its investors — so an ex-partner on a filing means they took a job or a board seat at their next firm, not that Sequoia invested. Rows are flagged where the filing postdates the partner's last archived appearance by more than 3 years, requiring ≥3 snapshots of signal and skipping anyone still current (last seen ≥ 2025). **115 rows flagged**, and the flags are substantively right: Sameer Gandhi → Accel (Freshworks, Public, Rylo), Mark Kvamme and Chris Olsen → Drive Capital (MarkLogic, Root), Gaurav Garg → Wing (Cohesity), Mickey Arabelovic → Fundraise Up (16 years after leaving; confirmed backed by Summit Partners, not Sequoia).

**Removal rule.** A row is removed only when an ex-partner is its *sole* claim to being a Sequoia deal: no listing on Sequoia's own site, no Sequoia entity on any SEC filing, and no still-serving partner among its Form D related persons. That removes **106 rows** — deals belonging to Accel, Drive Capital, Wing and other firms the partner joined afterwards.

The remaining **9 flagged rows stay**, because a flag can be correct while the row still belongs. Cohesity is a genuine Sequoia company via Bill Coughran (Wayback-listed); Garg's Form D presence there reflects Wing's separate involvement. Guardant Health carries both Wayback and EDGAR evidence. Removing on the flag alone would have deleted all of them.

Two residual cautions: the archived-snapshot span under-reports tenure for rarely-crawled people, and a partner absent from the roster is treated as attributable rather than removed, so the rule errs toward keeping.

## 4. Row anatomy and reconciliation workflow

Each row, in review order: `name, status, first_seen, wayback_first_link, formd_links, edgar_links, partners_site, partners_formd, partner_match, sector`, then secondary/audit fields `tier, lineage, slug, wayback_years, edgar_forms, edgar_span, edgar_cik, formd_roles, formd_max_round_usd, formd_span, formd_accessions, notes`.

Observability columns:
- `wayback_first_link` — archive.org link to the earliest evidence: the company's own archived Sequoia profile page for 2006–2014 rows, the archived portfolio listing for 2015+ rows (Ctrl-F the name). 787 rows have one.
- `formd_accessions` / `formd_links` — the SEC accession numbers and clickable `sec.gov/Archives` filing-index URLs behind every Form D match. 354 rows have at least one; every Tier C row is verifiable in one click.
- `edgar_links` / `edgar_cik` — clickable SEC filing-index URLs for the 13D/G and Form 3/4/5 evidence, plus the subject CIK the row joined on. 118 rows.
- `sector` — Sequoia's own category tags (taxonomy extracted from the 2015–2021 filter UI, e.g. marketplace, healthcare-consumer). 317 rows.
- `partners_site` vs `partners_formd` — partner attribution from Sequoia's historical site tags vs from SEC director filings, kept separate deliberately: agreement is the strongest attribution signal available.
- `partner_match` — derived sort key: `both` (51 rows, gold-grade attribution), `site_only` (188), `formd_only` (297), `site+formd_disagree` (6, review these), `none` (552).

**Person-name matching.** The two partner columns come from different sources that spell the same person differently (site slug `pat-grady` vs SEC filing `PATRICK GRADY`). Comparison therefore uses `same_person()` rather than string equality: it requires equal surnames, then accepts an exact given-name match, an irregular nickname via a small map (bill/william, jim/james, mike/michael, tom/thomas…), a prefix shortening (pat/patrick, greg/gregory, doug/douglas), or a single initial (`R. Botha` = `Roelof Botha`). Requiring the surname to match keeps the loose given-name rule safe. The same function collapses variants *within* a single row, so `Doug Leone; Douglas Leone` no longer renders as two people.

Workflow for the manual pass:
1. Sort by `tier`. Tier A rows are cross-confirmed; spot-check only.
2. Tier B (Wayback-only): mostly legitimate older portfolio companies; the main defects are name-normalization duplicates (same company under two spellings) and residual non-company pages from era B. Merge or delete, then set `status=human_confirmed`.
3. Tier C (Form D / EDGAR-only): two populations mixed — genuine unannounced/newer deals (high value: these are the "dark matter") and false positives from common partner names (e.g. Fan Zhang, Gary Li matching unrelated filers). Check `formd_partners` + issuer name plausibility; confirm or delete.
4. `lineage` is now derived from the filing entity's desk (see §3a); China/India rows have already been partitioned out, so remaining values are `us-eu` or `israel`.

## 4a. Audit findings and corrections

A systematic audit before outcome classification found five defects, all now fixed and re-verified:

1. **Person filed as a company.** `William Coughran` was a row: the era-B person filter matched roster *slugs*, and the roster records him as `bill-coughran`. Now matched with `same_person()` instead of string equality. 0 people remain in the base.
2. **Name-collision on a feminine variant.** The prefix rule in `same_person()` treated **`Josephine Chen` as `Joseph Chen`**, attributing Renren's fintech deals (SoFi, LendingHome, Fundrise) to Sequoia. Added an explicit `DISTINCT_DESPITE_PREFIX` set (joseph/josephine, daniel/danielle, patrick/patricia, …) — the surname-equality guard cannot catch this, since the surname genuinely matches.
3. **Property LLCs under a common name.** 12 rows (`100 CROSSING APARTMENTS LLC`, `1480 PARK 33 PROPERTY LLC` …) traced to a *different* Ravi Gupta — the Sequoia partner of that name is current, so the tenure rule could not help. Resolved by extending the non-portfolio industry rule: **audit showed all 19 rows previously spared as "ambiguous industry" were noise.** The earlier reasoning — that Prosper/SoFi/LendingHome are real fintechs — confused *being a real company* with *being a Sequoia deal*; none were the latter, and all were uncorroborated Form D-only rows.
4. **Spacing duplicates.** `Mark Logic`/`MarkLogic`, `Kayak Com`/`Kayakcom`, `Link Exchange`/`LinkExchange` and 10 more were separate rows. The join key now strips spacing and punctuation entirely.
5. **A regression introduced by (4).** Making the key space-insensitive silently broke the word-prefix duplicate check, which looks for a space — so `Aruba` and `ARUBA NETWORKS, INC.` stopped being flagged. A separate space-preserving key (`norm_words`) now backs that check.

### Duplicate resolution — decided automatically

Name variants (`Aruba` / `ARUBA NETWORKS, INC.`) had to be merged without creating the opposite error, since `Carbon` / `Carbon Black` and `Linear` / `Linear Technology` are genuinely different companies with the same name shape.

**The arbiter is the investor's own publications.** If any *single snapshot* of a listing — the current site, or one archived portfolio page — names both, they are two entries in one published list and therefore two companies. If no listing ever names both together, they are one company under two renderings, and are merged.

Snapshot scoping matters: an earlier version keyed on *year* and wrongly split `Barracuda` / `Barracuda Networks`, because the 2021 file mixes a January era-C snapshot with a December era-D one. Keying on `snapshot_ts` fixed it.

A differing EDGAR subject CIK also proves distinctness, but only when **both** rows are independently listed — a company files through several legal entities (`Aurora Innovation` / `Aurora Operations`), so an EDGAR-only row with its own CIK is normally a filing vehicle of the listed company.

Result: **93 merged, 6 kept separate** (`Carbon`/`Carbon Black`, `Linear`/`Linear Technology`, `Magic`/`Magic Eden`, `Parallel`/`Parallel Web Systems`, `Elevate`/`Elevate Credit`, `Nimble Storage`/`Nimble Rx`). Merging unions all evidence, prefers the investor's own current rendering of the name, and the tier is recomputed afterwards — a merged row corroborated by two sources is promoted to Tier A, which is most of the Tier A rise from 251 to 280.

**HTML entities.** Archived markup and the WordPress API both render names escaped, so `Alpha &amp; Omega Semiconductor` normalised to `alphaampomegasemiconductor` and never joined `ALPHA & OMEGA SEMICONDUCTOR Ltd`. Names are now decoded at every point one is read — era-B alt attributes, era-C/D listing markup, and the site API's `title.rendered` — and the join keys decode defensively as well.

A multi-strategy duplicate sweep over the finished base (identical-after-normalisation, same word-set in any order, word-prefix, and ≥0.92 string similarity) returns **zero unresolved duplicates**. The only near-misses are genuinely distinct companies: `Square` (payments, Tier A) vs `SquareX Holdings` (browser security, Tier C), and `Thread` (2010) vs `Threads` (2020, productivity).

### Era-B category pages

The 2010–2014 sitemap links companies and sector pages identically, so `Communications`, `Gaming`, `Media` and 65 others were rows. Sequoia's old CMS failed to interpolate the region name for category links, leaving a Ruby object in the alt text (`alt="#<Region:0x..> Gaming"`) while company links carry the clean name (`alt="Mixpanel"`). Filtering on that removes all 68 category pages per snapshot and supplies proper display names for era B — a structural signal from the markup, not a curated word list.

Post-fix integrity checks, all clean: 0 rows with no evidence, 0 Tier A rows with fewer than 2 sources, 0 Tier B rows without exactly 1, 0 people, 0 property entities, 0 spacing duplicates.

## 5. Known limitations

1. **Era D shallow (2022–2026 Wayback):** the modern site lazy-loads its company list; only ~32 server-rendered entries per snapshot were captured, and 2023–2026 snapshot fetches were refused. Mitigation: Form D covers 2022–2026 well (e.g. Harvey AI $200M, 2026). Fix candidates: archived XHR/JSON captures, or the live site's API.
2. **2013–2014 gap:** site redesign left almost no parseable portfolio listing; covered indirectly by the 2012 sitemap and 2015 listing overlap.
3. **Name normalization.** Normalization strips only legal-entity suffixes (`Inc`, `Ltd`, `LLC`, `Holdings`…). It previously also stripped descriptor words — `Technology`, `Systems`, `Networks`, `Labs` — which silently merged **Linear** (developer tools, 2021) with **Linear Technology** (semiconductors, 1980s) into one row carrying both companies' sectors. Correcting it split 33 such pairs. The opposite error is now possible instead — `Aruba` and `Aruba Networks` as two rows for one company — so word-prefix pairs are **flagged for review (101 pairs) and never merged automatically**, since Linear proves the same shape can be two different companies. Merging is a human call.
4. **Form D common-name false positives** in Tier C: a roster surname colliding with an unrelated filer. Check `partners_formd` plausibility during review.
5. **Form D structural blind spots:** electronic coverage starts 2009; stealth seed rounds under Section 4(a)(2) never file; non-US portfolio companies don't file at all. Lifetime coverage for US companies reaching Series A estimated 90%+.
6. **Partner roster ends 2021** for archived team pages; current-era partners appended manually. Full 2022–2026 roster reconstruction pending.
7. **Era A partial:** 2006–2009 listings enumerated via CDX index rather than parsed page-by-page, so year-of-first-listing in that era is approximate. Pre-2006 history is out of window by design, which also means Sequoia's foundational era (Apple, Cisco, Oracle) is absent from this base.
8. **EDGAR pre-2001 and pre-registry entities.** Collection is bounded by the entity registry; a vehicle that filed in the 1990s and never appears in a modern filing or company-name search would be missed. The recall audit against the old FTS output found no such case among genuine US/EU companies, but the registry is the limiting factor and should grow as new investors are added.
9. **249 rows have `first_seen = '?'`** — site-listed companies with no archive or filing date. The site API's `published` field is a page-creation date, not an investment date (Etched shows 2026 for a 2024 round), so it is deliberately not used as a proxy.
10. **94 unresolved duplicate pairs** inflate the denominator by up to ~6% until reviewed; hit-rate figures should be computed after that pass, not before.
11. **`israel` desk undecided** — 11 entities, 2 companies currently retained in the US/EU base (see §3a).

## 5a. What changed in the v0.2 rebuild, and why

The EDGAR layer previously guessed which party in a filing was the portfolio company, because full-text search returns all parties in one flat list with no roles. Two failure modes were measured and are now eliminated at source:

| | Before | After |
|---|---|---|
| Collection driver | keyword `"Sequoia Capital"` in document text | entity CIKs → SEC submissions API |
| Role assignment | name-shape heuristic (`is_issuer()`) | `SUBJECT COMPANY`/`ISSUER` from the submission header |
| Lineage | filer-name regex → 29 rows tagged | filer CIK → registry desk → 22 rows partitioned out |
| Fund/GP exclusion | name pattern (`FUNDISH`), 17 rows | structural: co-filers can no longer be read as subjects |
| Filings collected | 1,447 (49% text-mention leaks) | 1,658, all genuinely filed by a registry entity |
| Companies | 212 (incl. partners, GP vehicles, others' 13Ds) | 141 |
| Base rows | 1,173 | **1,094** |
| Tier A | 138 | **144** |

Tier A *rising* while the base shrank is the signal that matters: joining on CIK is more reliable than joining on names, so more rows are now cross-confirmed by two independent sources even though contaminated rows were removed.

The 71 companies that left the EDGAR layer were audited individually. They fall into three groups, all correct removals: Sequoia partners misfiled as companies (`LEONE DOUGLAS M`, `MORITZ MICHAEL J`, `VALENTINE DONALD T`), GP/management vehicles (`SCGF III MANAGEMENT`, `Francisco Partners II`), and other firms' acquisition 13Ds that merely mention Sequoia (HotJobs → Yahoo, Latitude → Cisco, Genesis Microchip → Pixelworks, Juniper → NetScreen). Where such a company was genuinely in the portfolio — E*Loan, NetScreen — it is retained through the Wayback layer instead, so nothing real was lost.

All 10 assertions in `scripts/verify-company-base.py` pass.

## 6. What v0 already supports

- A defensible **denominator floor**: 138 Tier A + reviewed Tier B, with the Tier A/B/C sensitivity band reported alongside any hit-rate figure.
- **Decision-desk attribution** per company from two independent channels (Wayback partner tags 2015–2021, Form D directorships 2009–2026).
- Reproducibility: every number regenerates from the scripts; every claim links to a cacheable source (archive.org URL or SEC accession number).

## 7. Next steps

1. Manual reconciliation pass (Tier B merge/dedupe, Tier C confirm/delete).
2. Era D fix via archived JSON/XHR or live-site pull; extend partner roster 2022–2026.
3. Outcome classification per confirmed company (unicorn/decacorn/IPO/M&A/dead) → numerators.
4. Compute hit rates over the three denominators (A, A+B, A+B+C) with confidence bands.
