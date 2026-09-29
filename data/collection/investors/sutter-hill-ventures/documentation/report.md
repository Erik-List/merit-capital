# Sutter Hill Ventures: Build & Reconciliation Report (PRO-77)

**Linear issue** PRO-77 · **slug** `sutter-hill-ventures` · one run, one session, under the merged shape of
`data/collection/COLLECTION.md` · report written 2026-09-28. **Ingested 2026-09-28 with Erik's approval (see the last section).**

---

## 1. The answer PRO-77 asked for

**The base is 274 companies and plain `verify` is clean.** Sutter Hill is one evergreen partnership advised by
SUTTER HILL VENTURES, L.L.C. (CRD 162959, exempt reporting adviser), plus a 2024 opportunity fund. Its live site
is a wordmark, but the archive holds its own list from 1999 to 2016, starting with a table of every investment
since 1970.

**Does the related-persons sweep need a role dimension?** Not as the issue framed it. It needs the related
person's **address**, and the role is a small bonus:

- An address sweep (every related person filing from the firm's own office, all three role slots,
  `scratch/formd-address-sweep.py`, 13 seconds over the local bulk zips) found 43 issuers with a Sutter Hill person
  on them. 42 of the 43 were already in the roster-name sweep, so the address adds almost no recall.
- What the address adds is **identity**. It settles a common name in one step: 5 of 32 "James White" issuers and
  none of 70 "David Anderson" issuers were filed from the firm's office. It also dates a departure: Greg Sands's
  seats move from 755 Page Mill Road to Costanoa's 160 Forest Avenue in 2013.
- The **role** marks incubations. On 4 issuers a firm managing director is an executive officer: Os76 (Pure
  Storage), Laserlike, Augment and a 2015 stealth company. It never shows money, so it cannot decide membership
  alone (decisions D3).
- Cost to add to `formd-query.py`: three fields per matched person (RELATIONSHIP_2/3, STREET1/2). The roster sweep
  keeps only RELATIONSHIP_1 today, and 5 firm-person lines lost their second role.
- One trap: Morrison & Foerster's Palo Alto office is also at 755 Page Mill Road, with no suite. The firm's
  address is the suite (A-200), not the building (R1).
- Bain Capital Ventures' run built its own address reader the day before, so this is the second run to need it.
  For run 7 (Founders Fund) the address is what separates a partner's firm seat from a personal or SPV one.

**Does a from-inception position have a valid entry stage?** Yes, so no §9 trigger 3 fired. The fund's first
preferred round is the entry, labelled as the record names it (D3). Snowflake's is its August 2012 Series Seed:
Sutter Hill bought about 48% of it (its own Form 3), and the row graduated at the named Series A. Pure Storage's
first round is a Series A. Mike Speiser's own founder shares as acting CEO are a person's position, not the entry.

| Done-when item | State |
|---|---|
| Plain `verify` green | Clean (`verify: clean`), with 9 stale classification keys noted (rows merged away, not failures) |
| Every row judged and classified | 337 verdicts; 274 published rows, all classified; 0 uncertain |
| Distributions sanity-checked | Section 2 |
| Firm profile | `investor/investor.json` + `sources.json`, built by `build-firm-profile.py`, copy rules pass |
| `review.html` rendered | Served on the review surface (8931); the profile panel expands, 274 rows render flat |
| Cross-investor (rule 10) | 110 shared rows: 105 agree, 5 accepted, 0 disagree; 20 namesake pairs ruled distinct |
| Report, write-back, ingest request | This file (sections 11 and 14) |

## 2. Results

| | Count | Share |
|---|---|---|
| Companies | 274 | |
| Acquired | 184 | 67% |
| Unknown | 30 | 11% |
| Private | 29 | 11% |
| Public | 16 | 6% |
| Defunct | 15 | 5% |
| $1B and above | 18 | 6.6% |
| of which $10B and above | 7 | Nvidia $5.53T, Snowflake $116B, Astera Labs $61B, Ramp $44B, Pure Storage $43B, NetApp $40B, Corcept $12.5B |

The rest of the $1B+ list: Ionis, DataRobot, Grail, AAC Technologies, Rigetti, SiFive, Sigma Computing, Artisan
Partners, Sila, C3.ai and Omnicell. Entry stage: Series A 51, Growth 34, Seed 9, round not on record 177 (mostly the
1970 to 2000 book, where no source names the round) and 3 companies no source can name. HQ: US 266, UK 3, China 3,
Ireland 1, New Zealand 1. Membership rests on the firm's own listing for 232 rows, press for 27 (the recall
additions), a Form D ruled by the judge for 14 and the firm's own filing for 1. The base is winner-heavy and old:
two thirds are acquired companies from the firm's own 1970 to 2016 lists.

### S2A block

| Seed entries | Censored | Cohort | Graduated | Not graduated | Rate |
|---|---|---|---|---|---|
| 9 | 1 | 8 | 4 | 4 | **50.0%** |

Coverage is 100%. Of the 4 that did not graduate, 3 rest on the Form D absence and 1 (Boxer, bought by VMware in
2015) on the dated absence test over the named surfaces. The graduations are Snowflake, Laserlike, Celero and
Integrated Biosciences. The cohort is small because Sutter Hill mostly enters at a named Series A.

## 3. The boundary

- **D1:** one adviser, one office, two funds: the partnership ($2.94B gross assets) and 1962 Opportunity Fund I
  ($750M, 2024). External: Costanoa, Bluebird Ventures, a property partnership and the Sutter namesakes.
- **D2, partners' personal vehicles:** the partners' trusts co-invest beside the partnership (Amerigroup's S-1
  footnote; Clarus's 2002 proxy splits one managing director's own shares from the funds'). Membership needs a
  fund position; the personal holdings change nothing.
- **D6, the firm's "Investment Partnerships" category is out (8 rows):** Acacia, Biovest Partners, Chengwei, Golden
  Gate Capital, Helion, Makena, Venture TDF China, Costanoa. Indus International is out too: it is filed in the same
  category and has no venture entry on record.
- **Control positions (2):** Therma-Wave (Bain's 1997 recap with SHV and management at 88% of the vote) and the 2016
  Lifesize spin-off (Redpoint, Sutter Hill and Meritech took 62.5% and all votes; Logitech's 8-K).
- **Sale consideration (4):** IDEXX (paid for Blue Ridge Pharmaceuticals), Avid (for Digidesign), Curis (for
  Ontogeny), Emcore/USANA/TeleCommunication Systems (config traps). The acquired company is the member in each case.
- **Post-IPO purchases (T3):** Aruba Networks (first 13G 13 months after its IPO) and Corixa (a 2002 placement)
  are out. AAC and Pacific Biosciences stay: both had pre-IPO rounds with Sutter Hill.
- **Seat dating (D5):** 77 Form D name matches were removed by the tenure rule: David Anderson homonyms, Greg
  Sands's Costanoa seats and Ron Bernal's Sequel and NEA seats. Another 20 were judged out: James White homonyms,
  Victor Miller's pre-SHV seats, Brian Blond's seats after he joined Human Capital, and Andy Sheehan's
  Tippet-era Creditly.

## 4. Coverage per evidence regime

- **The firm's archive, 1999 to 2017:** the 1999 investments table (110 companies, each with the firm's own
  outcome line), 2000 to 2001 software pages, the 2004 to 2012 sector directories and the 2013 to 2016 full list
  (144 to 160 companies a year, each with its managing director).
- **Common Crawl:** the Internet Archive blocked this machine three times (60, then 120, then 240 minutes).
  Common Crawl carried 2008 to 2017 through its static `cluster.idx`, since the index server did not answer (705
  captures). The 2000 to 2001 software pages were already cached.
- **Archive debt:** the 2000 to 2003 medical, networking and IT pages and the 2004 to 2007 directory years
  were never read. Slugs seen only in the capture index: `/mt/cardia`, `/mt/metrika`, `/mt/vascular`,
  `/nt/bluzona`, `/nt/kmv`, `/software/vocalocity`, `/software/podbridge`, `/networking/trusteddata`,
  `/consumer/eos`, `/healthcare/vivios`. K2 Optronics and Insmed were resolved through press. One run of
  `scratch/ia-eras.py` after the Archive recovers reads the rest, into the parsed years. The new rows would then need
  one rebuild and one small delta.
- **EDGAR:** the partnership's own ownership filings (44 companies), the roster Form D sweep (604 filings),
  the address sweep, and the full-text exit side (sale-consideration cases, S-1 holder tables).
- **Recall:** 20 companies the lists never carried were added with citations: Rigetti, DataRobot, Ramp, io,
  Ridge Bio, GridCARE, AttoTude, Matic, Atmosic, Integrated Biosciences, Curbside, Infer, Transposit,
  Vlocity, PredictHQ, Astronomer, Cipher Data Products, Qume, K2 Optronics and the Lifesize spin-off (now a control
  row). 17 more were rejected with reasons (`scratch/recall/rejections.json`). The post-2016 book rests on
  press and Form D, so it undercounts quiet incubations.

## 5. Method deltas

- The address-and-role Form D sweep (section 1).
- A curated slug-to-name map in the parsed source for directory pages whose markup names the acquirer before the
  company. One example: "Virage was acquired by `<span>`Autonomy`</span>`". A naive extractor published "Autonomy" as the
  company.
- The icon composed from the site's own animation (section 8).

## 6. Flags and debt behind `verify`

- Stage unknown on 177 nameable rows. 3 companies can't be named (IEI, Trade, Bonafide): their country is
  inferred as US and flagged `country_prior`.
- 20 rows carry `city_unknown`; 30 rows are status `unknown` (old companies with no fate on record).
- 9 stale classification keys from merged rows remain: they are noted by `verify`, not failures.
- The DataRobot and Sila marks are flagged `stale` (older than 24 months).

## 7. Standing duties and the A/B pass

- All 19 public or $1B+ rows were defended and attacked, with every market cap re-read on 2026-09-28. The
  pass fixed:
  - Nvidia's 1993 Series A, now cited from its 1999 prospectus.
  - Astera Labs: a Growth entry at the November 2019 Series B, per Sutter Hill's own Form 3.
  - Corcept: moved to $10B-plus.
  - Snowflake: a Seed entry that graduated.
  - IDEXX and Avid: ruled out as sale consideration.
  - Grail: HQ corrected to Sunnyvale.
- The later rows carry the delta judge's cited caps and marks: Rigetti $5.32B, Ramp $44B, DataRobot $6.3B (stale).
- Wrong Wikidata joins were disputed on one-word names (Boxer, Bonafide, Aspect, IDEXX, Grand Junction, Lucy,
  Virage, Aida).

## 8. Firm profile

HQ Palo Alto (the ADV and the site agree). AUM $3.69B: the two funds' Section 7.B gross assets, an exempt reporting
adviser's sworn figure. Founding year 1962 is the firm's own statement; Wikipedia gives 1964 (recorded in the
sidecar). The thesis is **derived and flagged**, because the site states nothing. Team: eight managing directors,
each with a cited title and no social links, because the site has none.

The icon is the firm's own "SHV" monogram. It is the final frame of the shv.com wordmark animation, whose layers
are labelled "monogram S/H/V", composed from the page's own animation data. The dry run passes every rule (contrast
12.1:1). Stage: Seed, Series A, Growth. Range: $0.9M, $12M median (129 entry rounds), $375M (Sila's Series G, which
Sutter Hill led). Notables: Nvidia, Snowflake, Activision, Palm, Glassdoor.

## 9. Open rulings for Erik

1. **IDEXX and Avid as sale consideration** (medium): the 1999 table lists both as holdings beside Blue Ridge and
   Digidesign. IDEXX's 1998 8-K shows the Blue Ridge payment; no pre-IPO round with Sutter Hill was found for either.
2. **AAC Technologies:** it stays in because its pre-IPO rounds had Sutter Hill beside Chengwei. If Sutter Hill held
   it only through its Chengwei fund interest, D6 removes it.
3. **The two control positions** (Therma-Wave, the Lifesize spin-off): confirm the class for Sutter Hill.
4. **D6 as a class:** the firm's own "Investment Partnerships" category is out (8 rows plus Indus International).
5. **Pure Storage is Everpure since January 2026.** Four books publish it as Pure Storage; one rename would cover them all.
6. **Serviz:** a member by the director-of-record pattern (medium). The press names "Andy Sheehan of Sutter Hill".
7. **Accepted sibling disagreements, where this book holds newer cited evidence:** Room 77 (Lola bought it, not
   defunct), SilverRail (bought back from Expedia in 2020, private today), Sila ($2B mark), Ameritox, Banyan and
   Benu. They align at the wave pass.
8. **Tooling requests (scripts are the tooling session's):**
   - `prepare` reads only numeric years of incorporation, so a Form D answering "over five years" slips past
     the older-company band rule (PRO-157). The judges withheld those bands by hand.
   - The rebuild re-keyed three excluded verdicts onto name variants, the second run in two days to hit this.
     The verdicts were restored by hand.
   - `formd-query.py` should keep the address and all three role slots.

## 10. Rebuilds and deltas

- One scheduled rebuild after the recall probe. It landed 20 recall additions, the 2000 to 2001 software rows, 7 new
  Form D issuers and 12 identity merges.
- The delta judged 38 rows and ruled 6 out, so a second, final rebuild ran before export (§8).

## 11. Playbook write-backs proposed (not applied mid-wave)

1. §5.3 EDGAR: store each related person's address and all three role slots, and add an office-address sweep. The
   address resolves common names and dates departures; the role marks incubations. Require the suite, because
   office buildings are shared.
2. §1 T2/T3: incubations are members, and their entry is the first round the fund bought, as the record names it
   (D3, generalised).
3. §5 archive: when the Internet Archive blocks at kickoff, go straight to Common Crawl's static `cluster.idx`.
   This is the second run to need it. Parse the sector-directory eras with a curated slug map.
4. §11 icons: an animated wordmark can end on the firm's own monogram. Compose its final frame from the page's own
   animation data (this extends the Lux inline-SVG rule).

## 12. Usage line

- At 20:05 UTC, an hour after kickoff: 5-hour 17%, weekly 8%, Fable 3%.
- At close (23:45 UTC): 5-hour 74%, weekly 23%, Fable 6%.
- These readings are account-wide, and other sessions ran alongside this one.
- Base rows: 274, plus 56 excluded.

## 13. Prompt count

2, final: the kickoff and the ingest approval (which also ruled the Everpure rename).

## 14. Ingest request (not run)

This is a first-time investor, so the order is icon, investor row, companies:

1. `npx tsx scripts/fetch-investor-icon.ts sutter-hill-ventures data/collection/investors/sutter-hill-ventures/sources/site/shv-monogram.svg`
2. `npx tsx scripts/ingest-investor.ts sutter-hill-ventures`
3. `npx tsx scripts/ingest-companies.ts sutter-hill-ventures --dry-run`, read the list (a first ingest removes
   nothing), then the same without `--dry-run`: 274 companies.

## Ingest 2026-09-28 (Erik's approval, second prompt)

Erik: "rename pure Storage" and "ingest now". The rename is recorded as R4 in decisions.md: Pure Storage publishes as
**Everpure** (`config.names.published`, slug unchanged); `export` and plain `verify` were re-run clean before any
write.

1. Icon uploaded: `investors/sutter-hill-ventures-8b21517b8c.png` (the "SHV" monogram, 256x256, contrast 12.1:1,
   ramp 0.99px); `icon_url` and its provenance are in the profile files.
2. `ingest-investor.ts sutter-hill-ventures`: 1 investor record upserted.
3. `ingest-companies.ts sutter-hill-ventures --dry-run`: 274 new, 0 removed, from 0 live; then the real run upserted
   274/274, and `public.companies` holds 274 rows for the investor.

Greylock, IVP and Redpoint still publish the company as Pure Storage; renaming it there means re-exporting and
re-ingesting those three books, which waits on Erik's word.
