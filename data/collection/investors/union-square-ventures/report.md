# Union Square Ventures — collection run report (PRO-86)

Run: one autonomous session on `main`, 2026-09-05 16:41 → close, merged shape (base + outcome classification + firm profile, COLLECTION.md §1–§12), beside the Spark Capital session (PRO-85). Slug `union-square-ventures`.
Prompt count: **1** (kickoff "please collect USV; phase 0 confirmed" plus one "continue" after an interrupted tool call); the ingest approval will be prompt 2.
Usage line: weekly __% → __%, Fable __% → __% (Erik records the account percentages before kickoff and at close); 220 base rows. Web budget: ~70 searches and ~16 fetches of ~200.

## 1. Result

| | |
|---|---|
| base rows (members) | 220 |
| ledger verdicts | 266 (43 not_member → excluded.csv, 0 uncertain) |
| recall additions | 7 (Uniswap, Diem, Brilliant.org, Chamber, Glif, Tasklet, Alqem) |
| identity merges | 31 + 21 name-variant merges |
| $1B+ / $10B+ / $100B+ | 23 / 5 / 1 |
| C2A cohort | 43, graduated 30 (69.8%) |
| verify (plain, links checked 21:52; final --skip-links) | verify: clean |
| cross-investor | 77 rows shared with other investors, 72 agree, 5 accepted, 0 disagree |

Final `verify` block (scratch/verify-final.log):

```
membership      : 266 verdicts, 0 uncertain
cross-investor  : 77 rows shared with other investors, 72 agree, 5 accepted, 0 disagree
rows            : 220
classified      : 220
$1B+ / $10B+ / $100B+ : 23 / 5 / 1
focus           : {'Consumer & Marketplaces': 38, 'Crypto & Web3': 32, 'Climate & Energy': 31, 'Fintech & Payments': 30, 'Media, Gaming & Advertising': 27, 'Healthcare & Bio': 15, 'AI & Applied AI': 11, 'DevTools & APIs': 10, 'SaaS': 10, 'Industrial & Robotics': 9, 'Data Infrastructure': 5, 'Security': 2}
hq_city         : 49 distinct, 189/220 filled; top {'New York': 66, 'San Francisco': 44, 'London': 11, 'Berlin': 6, 'Los Angeles': 6, 'Boston': 4, 'Pittsburgh': 3, 'Toronto': 3}
valuation_range : {'below_1b': 197, '1b_plus': 18, '10b_plus': 4, '100b_plus': 1}
entry_stage     : {'Series A': 111, 'Seed': 73, 'Growth': 35, 'Pre-Seed': 1}
C2A cohort      : 43  graduated 30  rate 69.8%

verify: clean
```

## 2. Method deltas against the playbook

- **Internet Archive outage during the run.** The five listing eras (2005–2009 `portfolio.html`, 2010–2012 `/investments`, 2013–2015 `/portfolio` attribute rows, 2016–2019 cards, 2019–2026 `/companies/` list rows) were parsed by hand from raw captures pulled before the outage; era D's "More" links pointed at blog posts and minted junk rows until the cards were re-parsed with a domain→name map. Replay-path convergence keyed on slug + path.
- **Live list.** `usv.com/companies/` is a server-rendered WordPress table (`m__list-row`) with first-investment round and year, exit detail and a post link; no REST route exposes the `company` type. The writing archive (3,807 posts) came through REST and gave the announcement posts that cite most entry rounds.
- **Stage evidence classes.** The site label scored 51/52 (live) and 87/89 (archived) on the gate → class 1; the Form D band 8/25 → ceiling. Record beats label on four rows (Zemanta, Wesabe, CoverWallet, Reservoir).
- **Exempt reporting adviser.** No Item 5.F RAUM exists for an ERA; the ADV Schedule D 7.B.(1) gross asset values (26 funds, $3,235,446,464, filed 2026-03-27) are the sworn AUM substitute (write-back item 5).
- **Recall probe.** Seven companies never on any usv.com surface entered through the firm's own posts and press. One corrective rebuild: the name-variant prefix merge folded "Brilliant" into Brilliant Planet; renamed Brilliant.org (R12, write-back item 4).
- **Record rejections read as warnings.** Two alignment files were rejected ("REJECTED — n problem(s), nothing recorded") and the header was cut off by a truncated read; verify caught the holes (write-back item 1). The scratch fix script also replaced 16 judge notes instead of appending; restored from the judgment files (write-back item 2).
- **A/B pass.** ~46 checks: every $1B+ figure now cites a primary or a market-cap page (caps at the 2026-09-04 close; Funding Circle converted at the ECB reference rate); Farcaster and Stash moved to acquired (R8); Polygon banded on the company's own $2B statement (R9); Justworks, OneFootball and Hume AI hold the aggregator rule (R11).
- **Cross-investor.** Spark closed during this run; 77 shared rows compare, 72 agree, 5 accepted pairs in `cross-rulings.json` (a16z Human Dx, Pascal, Kiosk; Spark Bug Labs, Justworks).

## 3. Distributions against the expected shape

Expected (issue): 220–300 members, seed-and-A heavy with a small Opportunity tail, the largest C2A cohort relative to base size, a real crypto book, market caps canonical on the visible slice.

| entry_stage | rows |
|---|---|
| Series A | 111 |
| Seed | 73 |
| Growth | 35 |
| Pre-Seed | 1 |

Seed + Series A = 184 of 220 (84%); Growth 35 = the Opportunity Fund rounds plus two secondary entries (Stripe, Twitter-era purchases are not in the base). The vehicle was never read as the round.

| status | rows |
|---|---|
| private | 144 |
| acquired | 51 |
| defunct | 15 |
| public | 9 |
| unknown | 1 |

| valuation_range | rows |
|---|---|
| below_1b | 197 |
| 1b_plus | 18 |
| 10b_plus | 4 |
| 100b_plus | 1 |

| focus | rows |
|---|---|
| Consumer & Marketplaces | 38 |
| Crypto & Web3 | 32 |
| Climate & Energy | 31 |
| Fintech & Payments | 30 |
| Media, Gaming & Advertising | 27 |
| Healthcare & Bio | 15 |
| AI & Applied AI | 11 |
| DevTools & APIs | 10 |
| SaaS | 10 |
| Industrial & Robotics | 9 |
| Data Infrastructure | 5 |
| Security | 2 |

| hq_country | rows |
|---|---|
| US | 177 |
| GB | 11 |
| DE | 10 |
| CA | 6 |
| BR | 2 |
| IN | 2 |
| AU | 2 |
| CO | 1 |
| SE | 1 |
| NO | 1 |
| EE | 1 |
| FR | 1 |

$1B+ rows (23):

| company | band | figure | as of | status |
|---|---|---|---|---|
| Stripe | 100b_plus | $159.00B | 2026-02-24 | private |
| Cloudflare | 10b_plus | $99.31B | 2026-09-04 | public |
| Coinbase | 10b_plus | $48.71B | 2026-09-04 | public |
| Twilio | 10b_plus | $35.77B | 2026-09-04 | public |
| MongoDB | 10b_plus | $29.65B | 2026-09-04 | public |
| Dapper Labs | 1b_plus | $7.60B | 2021-09-22 | private |
| Carta | 1b_plus | $7.40B | 2021-08 | private |
| Duolingo | 1b_plus | $7.19B | 2026-09-04 | public |
| Etsy | 1b_plus | $7.02B | 2026-09-04 | public |
| Upgrade | 1b_plus | $6.28B | 2021-11-16 | private |
| Suno | 1b_plus | $5.40B | 2026-06 | private |
| Abridge | 1b_plus | $5.30B | 2026-04 | private |
| Outschool | 1b_plus | $3.00B | 2021-10-14 | private |
| Generalist | 1b_plus | $3.00B | 2026-08-25 | private |
| Lending Club | 1b_plus | $2.21B | 2026-09-04 | public |
| Polygon | 1b_plus | $2.00B | 2022-02-07 | private |
| Radiant | 1b_plus | $1.80B | 2025-12 | private |
| Uniswap | 1b_plus | $1.66B | 2022-10 | private |
| Nova Labs | 1b_plus | $1.20B | 2022-03 | private |
| Dune Analytics | 1b_plus | $1.00B | 2022-02-02 | private |
| Quizlet | 1b_plus | $1.00B | 2020-05-13 | private |
| Shippo | 1b_plus | $1.00B | 2021-06-02 | private |
| Sift Science | 1b_plus | $1.00B | 2021-04-22 | private |

## 4. Flags and debt

| flag | rows | meaning here |
|---|---|---|
| cohort_unverified | 48 | Seed rows whose graduation leg is knowledge, not a filing or citation (13 vetted individually, all stand; Bug Labs flipped to graduated on its 2010 Form D) |
| stage_disputes_band | 38 | the site label (class 1) or a cited round overrides the Form D band |
| city_unknown | 30 | hq_city not established (189/220 filled) |
| model_disputes_source | 21 | a deterministic layer disputed: Wikidata glitches (Stripe, Polygon, Kiosk, Karat, Firebase, Funding Circle), float collisions (Ghost, Tapestry, Koko, fomo), unicorn collisions (Bolt, Odyssey), site `inactive` labels (Props, Brilliant Planet, Oddcast), unicorn-list OneFootball |
| stale | 17 | last primary mark older than 24 months, all cited |
| unicorn_name_match | 9 | layer flag: the unicorn list matched by name; all nine verified (six confirmed with primaries, Bolt and Odyssey collisions, Stash acquired) |
| censored | 8 | C2A cohort right-censored (too young to graduate) |
| cik_weak | 7 | layer flag: loose public-float join; audited — Cloudflare, Teamshares, Shapeways fit; fomo, Ghost, Tapestry, Koko are the disputed collisions |
| stage_uncited | 7 | entry stage from a prior (unnamed rounds: Chamber, Tasklet, Tracked, Anon-class rows) |
| country_prior | 2 | |

Debt carried: 31 rows without hq_city; 7 stages from priors; the icon (below).

## 5. Wave alignment (after both sessions closed)

- a16z rows to refresh: Human Dx (unknown → private), Pascal (unknown → private), Kiosk (Wikidata defunct-2001 glitch → private).
- Spark rows: Bug Labs (unknown → defunct), Justworks ($2.53B PitchBook mark → note, below_1b per R11). Spark's Abridge, Coinbase and Generalist already agree.
- Thrive: Justworks agrees (below_1b); Diem agrees (defunct).
- Same company, different slug across investors (R13): matter-labs-zksync / a16z matter-labs; sift-science / spark sift; dapper-labs / accel dapper; foursquare / a16z four-square; mediachain / a16z media-chain; quantopian-inc / a16z quantopian; flip / a16z flip-labs; blackbird-labs / a16z blackbird; granola-inc, zerion-inc, sidecar, stacks, koko / lightspeed variants; dia / sequoia dia-co. Verify compares by name key, the companies table would hold two rows — one slug per company should be picked at alignment.
- Shared caches touched by this run and outside the pathspec: new `data/collection/shared/sec/public-float/*.json` entries (untracked), to be committed at alignment.

## 6. Firm profile (§11)

`investor.json` + `investor.sources.json`, built by build-firm-profile.py against the landed base: HQ New York, NY (25/25 own Form Ds), founded 2003, AUM $3,235,446,464 (ADV 7.B, ERA), 26 vehicles (2004 fund from the site; sized filings verified against accessions; $0-sold 2022/2024 filings published at offering with the caveat), 13 people from the live team page, stage ['Seed', 'Series A', 'Growth'], geo {'core': ['US'], 'other': ['Europe', 'Canada', 'Latin America']}, focus recomputed from the site's own sector tags (10 values), range {'lower_limit': 750000, 'median': 5000000, 'upper_limit': 50000000}, notable ['Twitter', 'Etsy', 'Tumblr', 'Coinbase', 'Twilio', 'Duolingo', 'Cloudflare', 'Kickstarter', 'Zynga', 'MongoDB'].
Icon: `--discover` found only sub-100px favicons and a 190px header logo; the WordPress media library holds the site-icon original `cropped-usv_logo.jpg` (512x512, white USV on green). The dry-run refused it at 2.70:1 contrast (3:1 floor) and `--plate` cannot re-plate an opaque brand plate. `icon_url` holds the source URL as a marked placeholder until the icon decision (§7) and the gated upload.

## 7. Open rulings for Erik (§9 triggers, raised once here)

1. **Tucows and Marley Spoon** — site-listed, judged not_member under the post-RIA public-purchase standing rule (public shares bought without a venture entry). Confirm or overrule.
2. **Stripe** — member and Growth on the site's own "Common, 2014" row (a documented secondary entry; D5), although Phase 0 said not to seed it on the gate (it was not seeded). $159B tender mark aligned with four sibling runs.
3. **Polygon** — token position banded 1b_plus on the company's own $2B statement to CNBC (R9); a16z-style token-cap proxies would say below_1b. Confirm the rule.
4. **Farcaster** — acquired (Neynar) with the full $180M returned to investors: acquired/below_1b as a16z; the $1B 2024 mark sits in the note.
5. **Site `inactive` label vs record** — Props, Brilliant Planet, Oddcast kept private with the label disputed (R10).
6. **Aggregator rule (R11)** — Justworks and OneFootball read below_1b against Spark's PitchBook mark and the unicorn list; Hume AI's figure moved to the note. One rule for the wave.
7. **Icon** — allow the brand green at 2.70:1, or recolour/re-plate the mark (script change), or pick another source. Nothing uploaded.
8. **Five accepted cross-investor pairs** (§5) to confirm; the shared `cross-investor.json` is untouched.
9. **Tasklet** — member on the firm's empty-bodied announcement post plus the company's and Grossman's own announcements of the USV/Lightspeed-led $20M round; Lightspeed's base does not carry it yet.
10. **Diem** — member under the token rule as a16z and Thrive carry it (Libra Investment Token founding-member position), defunct.
11. **Address** — the site and ADV say 817 Broadway, 14th Floor; every Form D still says 915 Broadway. hq_location reads New York, NY either way.

## 8. Ingest request (runs only on Erik's approval)

```bash
npm run ingest:companies -- union-square-ventures
```

then, after the icon decision, `tsx scripts/fetch-investor-icon.ts union-square-ventures <source> [--plate …]` and `npm run ingest:investor -- --investors name=union-square-ventures` (with `--columns icon_url` once the icon exists). Wave alignment with Spark (§5) before or with the ingest.

## 9. Files

Top level: `config.json`, `decisions.md` (D1–D9, R1–R13), `golden.json`, `identity-merges.json`, `cross-rulings.json` (11 distinct, 5 accepted, 1 same), `entities.json`, `base.json` / `base.csv` (220 rows), `excluded.csv` (43), `classification.json`, `resolved.json`, `base-verification.json`, `review.html`, `investor.json`, `investor.sources.json`, this report. `sources/`: site (live list, 3,807 posts, team), wayback (five parsed eras, curated roster), edgar (Form D sweep 417 accessions, 42 own entities, fund filings, FTS hits, issuer rounds), web (Wikipedia insource). `scratch/`: queue and out files, judgments-1..5, fix and align files, gate protocol and blind pass, run-log.md, verify logs, `collection-writeback.md` (ten proposed COLLECTION.md edits, for the tooling session, nothing committed from here).
