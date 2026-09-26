# Atomico: Build & Reconciliation Report (PRO-79)

Run date 2026-09-26, one session, one merged run (derivation protocol,
`decisions.md` D1-D11 with 0 deltas, run-time rulings 12-17). Prompt count 1
(kickoff); the target is 2 with the ingest approval. Ingest not run, gated on
Erik's approval. Committed by pathspec (`data/collection/investors/atomico`).

## 1. The questions PRO-79 asked

**Is a Companies House register layer filing-grade?** Yes (ruling 17). A
company's annual return or confirmation statement that lists an Atomico vehicle
as a shareholder is a statutory filing, the UK counterpart of a fund vehicle on
a Form D, so it admits a member alone (`fund_filing`). It found the book's only
register-only member, **VisualDNA** (Imagini Holdings Ltd, whose 2008 and 2009
returns list Atomico Investment Holdings Ltd), dated entries nothing else dates
(Rekki between Nov 2016 and Nov 2017 with A Preferred shares; Kheiron between
May 2019 and May 2020; Zattikka by Sep 2009), and gave statuses, renames and
dissolutions (Streetbees in administration, Qatalog dissolved, Kheiron renamed
DeepHealth UK). Of 45 companies backtraced, 34 name an Atomico vehicle. A
director seat alone is not evidence (Rabbit Hole Labs is a lead, not a row).

**Config shape.** `config.registers.uk`: `firm_entities` (the firm's own
Companies House numbers: OC342228, 06570634, 07266688, 12488333, 15015365),
`firm_addresses` (regexes for the firm's service addresses: 7 Savoy Court,
Hanover House, 50 New Bond Street, 29-35 Rathbone Street) and `holder_pattern`
(`(?i)\batomico\b`). Code: `scratch/companies_house.py` (website reader, no API
key), `ch_officer_graph.py` (people anchored by firm entity or address, then
name and birth month), `ch_backtrace.py` (profile, whole filing history,
AR01/363/CS01 statements read by pypdf or macOS Vision OCR) and
`pdf-ocr.swift`. All proposed for `scripts/` in section 8.

**Cost per row.** First run: 40 companies at a mean of 9.7 requests, 4.0
documents, 30 OCR pages and 26 seconds each (17 minutes in all); a re-run from
cache costs 2.6 seconds a company. The officer graph over 109 archived people
returned 139 seats (76 at companies outside the base, every one read and ruled).

**Recall without Form D, measured.** Unchanged: 165 of 165 members. The Form D
layer produced 28 candidates and no member: nine are Teddie Wardi's Insight
Partners seats after he left in 2017, the rest ex-staff, namesakes or founders'
own filings, and the one real match is Pelago's legal entity (Digital
Therapeutics, Inc.), already a site row. For a European firm the Form D layer
is pure precision cost. Recall comes from the firm's own record: the 2021-2026
CMS (128 companies), five archived listing eras back to the 2008 Flash site,
the Getro job board (14 board-only rows, five of them 2026 deals the CMS
captures missed), the register (1) and the press (2).

## 2. Results

| Surface | Count |
|---|---|
| Base rows | 165 |
| Excluded | 30 `not_member` (27 Form D candidates; Skype, Free Now, Joost) |
| Identity merges | 22 duplicate rows, 6 found this run: IMA←Fashiolista, Pelago←Quit Genius + Digital Therapeutics Inc, Aplo←SheeldMarket, Fab←Hem, Vay←Ree Technology |
| Membership ledger | 201 verdicts, 0 uncertain |
| Classification | 165/165 |
| Status | private 86, acquired 48, defunct 16, unknown 8, public 7 |
| Valuation range | below_1b 131, 1b_plus 30, 10b_plus 1 (Telegram), 100b_plus 1 (Stripe) |
| Entry stage | Series A 56, Growth 48, Seed 18, undetermined 43 (2 unnameable) |
| Stage sources | web_verified 110, the firm's own label 6, Form D band 4, model 2 |
| Cross-investor | 95 shared rows: 87 agree, 8 accepted for wave alignment, 3 distinct |

**S2A.** 18 Seed entries, 5 censored, cohort 13, 6 graduated, 7 not
graduated: **46.2%**, coverage 100%. The nos rest on a cited end for five
(Equal Media dissolved, Heysan and Vaayu acquired, Siine dissolved, Silk's
acqui-hire) and on the full absence test for two (Deeploi, Opna); none rests on
Form D absence. Graduated: EVRYTHNG, Farmdrop, Hailo, Light, Quipper, Betable.

**$1B+ rows (32):** Stripe $159B (Feb 2026 tender), Telegram $30B (unpriced,
low), Hinge Health $7.71B and Compass $7.11B (market caps), StarkWare $8B
(stale), Neko Health $7B, PsiQuantum $7B, Attentive $5B (stale), Klarna $4.85B
(cap), Sorare $4.3B (stale), Bird $3.8B (stale), Aiven $3B (stale), MasterClass
$2.75B (stale), TravelPerk $2.7B, Factorial $2.5B, PhysicsX $2.4B, Wellhub
$2.4B (stale), Mews $2.37B, Viagogo $2.08B (StubHub Holdings cap), DeepL,
Framer, SmartNews, The Exploration Company $2B, Lime $1.9B (cap), Zocdoc, Nourish,
Pomelo Care, CodeRabbit, Jobandtalent, CADDi, Scandit and Upside Foods.

## 3. Method delta

- **The site is bot-walled.** atomico.com sits behind a Vercel checkpoint, so
  every page (CMS, posts, team, homepage) was read from Common Crawl or
  Internet Archive captures, never bypassed. The Archive refused this machine
  twice (the machine-wide cooldown now runs to about 02:00 UTC on 27 Sep) and
  the Common Crawl index server was down for part of the day.
- **Research fan-out.** 83 companies were researched by four parallel
  subagents; every URL and quote they returned was re-fetched by
  `scratch/verify-urls.py` before use. The session's 200-call WebSearch budget
  (shared with subagents) ran out mid-run; Google News through
  `graduation-surfaces.py` and WebFetch carried the rest.
- **The firm's own stage label.** The CMS "Stage" field is the sleeve that made
  the partnership. "Growth" scored 25/26 on the book's cited entry rounds
  (medium, under the 30-row bar) and now labels six rows (Klarna, Stripe,
  Compass, DeepL, Viagogo, Zocdoc); "Venture" straddles Seed to Series C
  (52/61) and mints nothing.
- **Register share classes** scored 16/17 as round words; refused as a label
  (under 30 rows, and the miss shows the failure: the first return naming the
  firm can postdate the entry).
- **Corrections taken during the run:** Andercore's entry predates its Series
  B (Tech.eu: "existing investors Atomico and Project A"), Lilium's predates its
  Series A (the firm's own 2016 post), The Climate Corporation's round is
  unnamed (the "Series B" was only a URL slug), Attentive's $2.2B was superseded
  by the 2021 Series E ($5B), and MasterClass's value rested on the unicorn-list
  pre-fill until CNBC's $2.75B replaced it.

## 4. Standing duties and the A/B pass

All 32 visible rows were defended and attacked (`scratch/ab-sweep.py`, press
after each value's date). Market caps re-read on 2026-09-25: Compass, Klarna,
Hinge Health, Lime (the cap the row owed) and LendInvest. Layoffs and
restructurings at StarkWare, DeepL, Upside Foods and Sorare are not collapse
evidence under §6, so their stale marks stand. The momentum slice (22 rows
entered since 2023 and below $1B) was checked the same way and moved one row:
The Exploration Company, reported in talks at $2B by the FT for the round that
closed at $450M. 30 of 32 visible rows carry a fresh or cited figure; Telegram
is flagged debt.

## 5. Firm profile

HQ London (the ADV principal office, 29-35 Rathbone Street, and the site's own
footer agree), founded 2006. Thesis, quoted from the homepage's lead heading:
"Capital is a commodity. Experience is not." History 52 words. AUM $4.17B, the
sworn Form ADV 7.B composite of both exempt reporting advisers (CRD 301113 and
165691). Six funds with sizes from the firm's own posts (Ventures II $165M 2010
to Growth VI $754M and Venture VI $485M, 2024). 56 people. Range $1M / $17M /
$100M. Notables: Klarna, Stripe, Supercell, Lime, DeepL. Icon: the homepage's
compact vector mark, dry run passed (keyline 63%/80%, contrast 11.4:1), not
uploaded.

## 6. Flagged debt

`verify: clean`. Flags: stale 12, model_disputes_source 9, stage_disputes_band
7, cite_pending 1 (Telegram, no priced figure), token_funded 1,
identity_unresolved 2 (IQube and Wunderloop, whose own 2008 pages could not be
read before the Archive refused).

## 7. Open rulings for Erik

1. **Skype** (ruling 12): `not_member` under T3 control and T4; the firm's
   founding story is absent from its track record.
2. **Telegram** (ruling 14): a refunded 2018 token presale kept as a member.
3. **Free Now and Pharmacy2U** (ruling 13): sale consideration, out.
4. **Wolt** (ruling 15): member on the firm's listing, possibly Zennström's own
   cheque.
5. **Ashby** (ruling 16): board-only and uncorroborated, kept a member.
6. **Joost** (D2): out, no Atomico vehicle ever shown.
7. **Sorare vs Accel** (accepted pair): IVP and this book keep the 2021 $4.3B
   as stale; Accel reads below $1B on layoffs.
8. **The Exploration Company at $2B** (low): a pre-close FT figure for a round
   whose price was never disclosed.
Also for the wave: Accel led Hailo's 2012 Series A and USV its Series B, yet
neither book carries the London Hailo.

## 8. Playbook write-back proposal (not applied mid-wave)

- §5, country table, UK row: the register layer as built here (config shape
  and code above, ruling 17's evidence reading, the cost). Register facts:
  SH01 never names the allottee; AR01 carried a full holder list only every
  third year; the website's filing-history category filter is not applied
  server-side (read the whole history).
- §5: when the Archive refuses and the site is bot-walled, Common Crawl
  captures carry the firm's own pages (cited as the index query); its index
  server fails too, so a failed lookup is retried, never read as absence.
- §3 recall probe: run a dense press sweep over the months since the newest
  site capture. Two of this run's three additions were Aug-Sep 2026 deals.
- §7: build the visible slice from the merged view (resolved plus
  classification), not from the grind's own lines; that is how MasterClass's
  pre-fill slipped past the first pass.
- §5 job boards: a Getro board titles itself "the Atomico network", so a
  board-only row nothing corroborates is flagged, not waved through.
- §5 Wayback: the 2008 Flash-era sites kept each company in
  `/OurPortfolio/<Name>.xml`; the CDX lists them.
- §12: the WebSearch budget is 200 calls per session, subagents included;
  plan research fan-outs around it.

## 9. Ingest request (not run)

On approval, in order: the icon upload (`npx tsx
scripts/fetch-investor-icon.ts atomico
data/collection/investors/atomico/sources/site/logo-small.svg`), then
`ingest-investor.ts`, then `ingest-companies.ts`.

**Usage line.** Kickoff: weekly 21%, Fable 4% (5-hour 18%). Close: weekly 34%,
Fable 6% (5-hour 47%, after one reset). 165 base rows: about 0.08 weekly points
per company.
