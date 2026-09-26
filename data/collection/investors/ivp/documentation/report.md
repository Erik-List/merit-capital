# IVP (Institutional Venture Partners): collection run report

**Linear issue** PRO-92 (sub-issue of the PRO-87 wave umbrella) · **slug** `ivp` ·
run closed **2026-09-26** · one session, one run, under the merged shape of
`data/collection/COLLECTION.md`. Ingest is **not** done: it waits for Erik's
explicit approval (order for a first-time investor: icon upload, then
`ingest-investor.ts`, then `ingest-companies.ts`).

---

## Results

| | |
|---|---|
| **Base** | **298 companies** (tiers A 174 · B 98 · C 26) |
| Excluded, preserved in `excluded.json` | 13 (all `not_member` verdicts, one scrape artifact among them) |
| Membership verdicts on the ledger | 324 · 0 uncertain (311 member, 13 of them on slugs later merged into another row) |
| Member evidence | site listing 282 · fund filing 22 · Form D adjudicated 5 · web 2 (recall additions) |
| `status` | acquired 156 · private 94 · public 36 · defunct 9 · unknown 3 |
| `entry_stage` | Growth 156 · Series A 12 · **undetermined 130** (older rows whose round nothing names) |
| `hq_country` | US 272 (91%) · UK 5 · Finland 3 · Germany 3 · Netherlands 2 · Sweden 2 · France 2 · Israel 2 · 7 others with one each |
| `hq_city` | 298/298 filled, 94 distinct |
| `focus` | 100% fill: SaaS 50 · Data Infrastructure 45 · Consumer & Marketplaces 44 · Media, Gaming & Advertising 34 · Healthcare & Bio 32 · Fintech & Payments 22 · Security 21 · Industrial & Robotics 21 · AI & Applied AI 16 · DevTools & APIs 10 · Crypto & Web3 3 |
| Visible slice | **70 rows at $1B+** (23.5%), 22 at $10B+, 6 at $100B+ (Anthropic, Netflix, CrowdStrike, Seagate, Uber, Robinhood) |
| S2A cohort | **0**: no row entered at Seed, so there is nothing to measure (see below) |
| Era span | first seen 1980 to 2026: 2 rows in the 1980s, 24 in the 1990s, 41 in the 2000s, 167 in the 2010s, 64 since 2020 |
| Firm profile | HQ Menlo Park, CA · AUM $9,945,403,983 (sworn, both ends) · 12 funds · 31 people · thesis "Supercharging growth." |

`verify` is **green in plain mode** with only flagged debt. Cross-investor:
279 shared rows, 268 agree, 11 accepted (sibling side stale, for the wave
alignment), 18 homonym pairs ruled distinct, 0 disagree. Atomico and Point
Nine were in flight and not compared.

## The delta this run was written for (X1)

PRO-92's delta was the base shape. **X1** restated `one_b_share_max` to 0.45
before the grind (`decisions.md`, flagged for Erik). The measured share is
**23.5%**, which is above the 20% default and far below 0.45: without the
restatement plain `verify` would fail on a correct base. The Coatue question
did not arise; IVP's growth entries fit the existing Growth label.

## Method deltas

- **The Internet Archive excludes ivp.com** (verified 16:03 EDT: every replay
  403s with "This URL has been excluded from the Wayback Machine"). Common
  Crawl became the archive layer: `scratch/pull-cc-ivp.py` and
  `parse-cc-ivp.py` read the firm's 2013 to 2025 pages (three site
  generations) into `sources/wayback/parsed/<year>.json`, each row citing its
  own `index.commoncrawl.org` capture (R1; tooling commit 458fcc7 made the
  build take `capture_url`). 299 companies appear across the captures.
- **ERA-only boundary** (D1): one exempt reporting adviser per fund GP, plus a
  London sub-adviser LLP. IAPD and EDGAR namesakes were ruled out by address,
  most importantly Insight Venture Partners' own "IVP (Venice)" and "IVP CIF"
  vehicles, whose Section 16 filings would otherwise read as IVP positions.
- **Curated roster** (D9): with no archive of people pages, 34 people were
  dated from the live team, IVP's fund Form Ds (2010 to 2024), CC team
  captures and press. Tooling fix 511b302 made the Form D sweep match "J.
  Sanford Miller".
- **Redpoint's founders' book** (D4): the IVP-era positions Redpoint ruled out
  of its own base (Excite, Juniper, TiVo, Wellfleet and others) are IVP's where
  an IVP fund held them; Redpoint's list served as a recall seed only.

## Evidence layers

Live site 156 companies (Nuxt payloads) · CC archive 299 companies, 2013 to
2025 · EDGAR entities 61 (40 own-desk) · partner Form D sweep 304 accessions ·
full-text sweep 303 registrants (tooling fix 57d3472 split the deep pages) ·
issuer-round histories for 55 companies · SEC float 73 · Wikidata 122 ·
unicorn list 629 current / 209 former.

## Recall probe

Five additions, each cited on the ledger: Santera Systems (Tekelec 8-K),
mTone Wireless (S-1), Applied Medical (S-1), HearMe (10-K405) and Wellfleet
Communications (Redpoint partner bio). Every name IVP's own posts repeat as
boilerplate was already a row. Rejected with reasons in
`sources/web/recall-probe.json`: 216 full-text registrants, almost all
director bios of IVP people on other companies' boards (Pandora is the
clearest case: IVP appears only in Peter Gotcher's bio).

**The gap is reported, not hidden:** IVP says "400 companies, 135+ IPOs"; the
base holds 298. The missing ~100 are structurally the pre-1996 book: EDGAR
full text starts in 2001, electronic 13Gs in 1996, and no archive of the
firm's own pages exists before 2013.

## The A/B pass and the standing duties

- **Every $1B+ private row is pinned to a priced event with a citation** (31
  rows written, 20 of them replacing unicorn-list figures, which Rule A does
  not accept as marks). 71 rows carry `stale` (marks older than 24 months, and
  the float layer's old floats). Checked and kept private: Motive (IPO
  withdrawn 2026-09-10), Discord (confidential filing, not listed), Dream
  Games (CVC bought out the venture holders in 2025 at about $5B; the founders
  kept control, so the company stays private on its 2022 primary mark).
- **Public rows**: all 36 carry a market cap as of 2026-09-25.
- **Momentum slice**: all 23 recent hot-sector private rows carry a web check;
  the six below $1B (Appcharge, Cortex, GenLogs, Laurel at $510M, Numeric,
  Volt at $350M+) stay below with the check recorded.
- **Stage citations**: 18 of the 23 `cite_pending` rows are now cited; 12 name
  IVP in the round, 6 rest on IVP's own dated announcement after the company's
  Series B (open ruling 7). Uber, Vercel, Datadog, Pure Storage and Hims & Hers
  stay `cite_pending`.
- **Weak CIK joins** (31): every registrant is the right company, and every
  float date fits its history.
- **Unicorn re-intersection**: three loose matches, all explained (Eucalyptus
  is a homonym, Niantic sold its games business, "Superhuman $13B" is Grammarly
  after its 2025 rename).
- **Geography**: Wikidata's country was wrong on 13 rows during the grind
  (single-token joins) and unparseable on 3 more, and wrong on two at the sweep: Seagate (city now Fremont, its
  operating HQ; Dublin is only the legal domicile) and Shazam (GB, not the
  acquirer's US). Papaya Global moves to New York and Wonderful to Amsterdam,
  their current headquarters, both cited.
- **Blind 5% self-consistency**: 15 rows, 3 disagreements, each adjudicated
  and flagged `unstable`. Datalogix read `defunct` (Wikidata dissolution)
  although Oracle bought it; the class sweep found Sequent (IBM) the same way.
  Qubole's Growth stands, now cited. Surf Air's Form D band stage became
  undetermined.
- **Form D band sweep** (the class behind Surf Air): of 10 non-Growth band
  labels, 7 were wrong because the band reads the first electronic Form D, not
  the entry. Buddy Media, General Assembly and Wikia are now cited Growth
  rounds IVP led; Oportun (read as Pre-Seed) is Growth; Yodlee, Motion
  Computing and Exclusive Resorts are undetermined; The Honest Company's Series
  A is confirmed and cited.

## Debt, all flagged and counted

`stale` 71 · `stage_uncited` 34 · `cik_weak` 31 (audited) · `unicorn_name_match`
25 · `model_disputes_source` 25 · `stage_disputes_band` 7 · `identity_homonym` 6
· `cite_pending` 5 · `boundary` 4 · `unstable` 3 · `needs_review` 3.

## S2A block

| seed entries | censored | undetermined | cohort | graduated | not graduated | rate |
| -- | -- | -- | -- | -- | -- | -- |
| 0 | 0 | 0 | 0 | 0 | 0 | none |

IVP enters at growth rounds, so no row entered at Seed and no S2A rate is
published. `c2a_rate_max` never fires.

## Firm profile

Built by `build-firm-profile.py`, checked by `profile_copy.py` and `verify`:

- **AUM $9,945,403,983**, both ends: Section 7.B.(1) gross asset values of 17
  funds across the five active advisers (ADVs filed 2026-03-28), parsed to
  `sources/registers/adv-7b-funds.json` and deduped by fund ID. Press and vendor
  figures ($7B to $8B) sit below the sworn number and live in the flag.
- **Funds**: IVP XII ($600M, 2007) to XVIII ($1.6B), with the executive and P
  vehicles; the XVII-A to G and XVIII-A co-investment vehicles and Bow Tie
  Angels are counted in the basis.
- **HQ** Menlo Park, CA (newest ADV principal office; the site names none).
- **Team** 31: 26 investors plus the five partner-level operators (CMO, CFO,
  head of capital formation, head of HR and platform, portfolio GM).
- **Focus** (site tags): SaaS, Consumer & Marketplaces, Data Infrastructure, AI
  & Applied AI, Fintech & Payments, Healthcare & Bio. **Signal:** IVP's own
  vocabulary has no Security or Media value although the portfolio carries 21
  and 34 such rows (the Lightspeed pattern); left for the recompute, not added
  by hand.
- **Icon**: the firm's 512px mark, dry-run only (contrast 3.4:1, ramp 0.95px,
  no enlargement); `icon_url` is the content-hash path the upload will write.

## Open rulings for Erik

1. **X1**: keep `one_b_share_max` at 0.45 (the measured 23.5% would fail the
   20% default).
2. **Omniture**: IVP's archived page says "Year Invested 2009", after the 2006
   IPO, and no filing names an IVP fund. Kept as a member on the listing and
   Todd Chaffee's bio ("led investments in ... Omniture"); the site's year is
   unreliable for legacy entries (it dates Netflix 2006, where the 2002
   prospectus shows IVP VIII a holder since 1998). OUT only if it was a
   post-IPO purchase (T3).
3. **Exclusive Resorts and Surf Air** rest on the director-of-record pattern
   alone (Todd Chaffee on the 2009 Form D; Dennis Phelps on the 2018 Form Ds);
   no filing names an IVP fund.
4. **Sorare against Accel**: this run keeps the $4.3B primary (stale) because
   layoffs are not priced collapse evidence; Accel reads below $1B.
5. **Dream Games**: private on the 2022 primary after CVC's 2025 buyout of the
   venture holders, or acquired?
6. **Eleven accepted rule-10 pairs** for the wave alignment, sibling side
   stale: a16z (Cowboy Space, Robinhood), Sequoia and Thrive (Robinhood),
   Khosla (Indiegogo, KeepTruckin), Greylock (Lyra, Vessel), Accel (Monte
   Carlo, Sorare), Benchmark (LiveOps).
7. **Stage from a dated first-party announcement**: six Growth stages (Figma,
   Gamma, Robinhood, Suno, UiPath, Klarna) cite IVP's own dated post, not a
   round name; the round is certain only as "Series B or later".
8. **Thesis**: the rule took the homepage headline ("Supercharging growth.");
   the title tag reads "Venture capital for the Exceptional".
9. **The ~100-company gap** to IVP's stated 400.

## Playbook write-back proposed (sent to the tooling session)

1. **An archive exclusion is a kickoff check.** A 403 whose body reads
   "excluded from the Wayback Machine" means Common Crawl is the archive layer
   for that domain, with each row citing its CC capture (R1 here).
2. **`record` keeps only the last line per slug in a file.** Two
   classification lines for Suno in one file silently dropped the first;
   `record` should merge per key or refuse duplicates.
3. **The Form D band misreads old companies.** When a company was founded
   three or more years before its first electronic Form D, the band should not
   pre-fill Pre-Seed, Seed or Series A; queue the row instead (7 of 10 wrong
   here).
4. **Wikidata `defunct` misreads acquisitions** (Datalogix, Sequent): a
   dissolution date with an acquirer is `acquired`.
5. **Wikidata countries on single-token names**: 15 wrong codes and 3
   unparseable values here, including a legal domicile (Seagate) and an
   acquirer's country (Shazam).
6. **Full-text recall noise**: nearly all firm-name hits are director bios;
   the probe could pre-filter bio sentences.
7. **Invariant 6 is not enforced by `verify`**: four visible non-US rows passed
   on model knowledge alone before this run cited them.

## Usage line

Weekly (all models) **21% at kickoff, 28% at close**; Fable 4% at both; base
298 rows. The seven points include the sibling Atomico and Point Nine
sessions running in the same window, so they are an upper bound for this run.
About 110 web searches of the 200 budget.

## Prompt count

**1** at close: the kickoff ("please collect IVP"). The ingest approval will
make it 2.
