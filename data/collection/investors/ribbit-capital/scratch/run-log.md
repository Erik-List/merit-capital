# Ribbit Capital run log (PRO-161)

Kickoff 2026-09-28 19:20 UTC, prompt 1 ("please collect ribbit capital"). Linear PRO-161 In Progress, kickoff comment posted.
Usage line: weekly / Fable percentages not readable from this session; record at close if available.

## RESUME NOTES
- Re-read COLLECTION.md, then `python3 scripts/run.py status --investor ribbit-capital`, then this file.
- Boundary: decisions.md D1 (one RIA, CRD 165308, no relying advisers, 67 private funds incl. ~40 deal SPVs),
  D2 (Bitcoin/Ethereum out; protocols in under their labs org; Diem in), D3 (Ribbit LEAP out), D4 (T3 public
  positions: Mercado Libre, Sea, Futu, Tinkoff out), D6 (SPV codes = a round Ribbit was in, never the entry).
- Sources: sources/site (scratch/pull-site.py: rebels.json 155 rows, team-pages.json 33), sources/registers
  (adv-165308.pdf, adv-funds-draft.json, spv-decode.json), sources/wayback (scratch/wayback-ribbit.py fetch/parse
  over IA + scratch/cc-fetch.py over Common Crawl; identity-map.json maps link hosts to companies),
  sources/edgar (formd-sweep, entities, edgar-companies, fts-hits, 13f-holdings), sources/web/wikipedia-insource.json.
- Grind tooling: scratch/show.py --batch N; judge_lib.py; judgments-N.py; nq.py (Google News); wikifetch.py;
  news-sweep.json (per row); evidence-pack.py; siblings.py; JUDGE-BRIEF.md.

## STATE
- 19:36Z IA firewall block (60 min machine-wide, set by this run's first fetch burst). Common Crawl carried the
  archive meanwhile (cc-cluster.py via cluster.idx; CC has ribbitcap.com 2013-2018 and 2021-2026, none 2018-30..2020).
- IA fetch (wayback-ribbit.py fetch, background) resumes after ~20:36Z: 2019-2020 our-bets + team captures, the
  archived rebels page chunks (2025-10..2026-08). Their companies land at the ONE rebuild (after the recall probe).
- Base 207 rows at prepare (19:55Z): 155 live + archive-only + Form D rows. prepare: 5 batches, in-flight marker set.
- Membership pass 1 recorded (judgments-members-1.py): 22 not_member (Bitcoin, Ethereum, Mercado Libre, Sea, Futu,
  Tinkoff; 16 Form D personal/founder/namesake seats), ibod-company-inc member (= Root, merged at rebuild).
  forusall-inc UNJUDGED: wait for the 2019-2020 archive (forusall.png upload suggests a listing; Shalek director 2018).
- Exemplar judgments-0.py recorded (robinhood, brex). 20:03Z four judges launched on batches 1-4 (15 WebSearch
  each); batch 5 (8 rows) is mine.
- WebSearch used by this session: 0 (judges up to 60).

## OPEN / TO DO
- Batch 5; recall probe (FTS third-party registrants: QIWI, Altice/Cheddar, Intuit/Credit Karma, Silvergate/Diem,
  Marqeta, Trinity Capital, Synchrony, Green Dot, Forward Industries, StableCoinX...; Wikipedia candidates; parametric
  enumeration; SPV codes not yet decoded).
- IA eras → parse → the one rebuild → prepare delta → grind delta.
- graduation-surfaces.py for Seed rows, graduation pass; A/B on the visible slice (public caps, $1B+ marks);
  momentum slice; profile (build-firm-profile.py, firm-offices.py, icon dry run); verify/export/review/report; close.

## STATE 2026-09-28 20:40Z
- 20:36Z IA re-blocked on the first requests after the cooldown (120 min, to 22:36:50Z). Bulk fetcher stopped. IA gave 27 Bets
  captures (2012-2015); Common Crawl gave Our Bets 2015-2018 and 2021-2025, the Rebels page 2025-12..2026-09, team pages.
  Only 2019-2020 is uncovered: scratch/ia-gap-fetch.py (4 replay requests, no CDX) runs in the background after the cooldown.
- Archive: 193 distinct names across 2012-2026; the only archive companies not in the base are renames (merged).
- Recall probe done: scratch/recall/rejections.json; Delphia added (ledger recall_additions, member via web).
- Batch 1 judge done (43 rows incl. caret, which sits in batch 3; b3 told to skip). fix-1: Conta Azul Series A (TNW 2013-01-07),
  entry 2012-09, graduation cleared.
- Team titles (profile): scratch/team-titles.json. Caps for public rows: scratch/caps.json (2026-09-28, stockanalysis; INR/GBP
  converted at ECB). Icon dry run clean (sources/site/icon-256.png from the site's icon.ico). Thesis: homepage hero "the future
  belongs to the rebels" (also on the firm's coin). Fund I $100M: LAVCA "Ribbit Capital Debuts With $100M Early-Stage Fund".
- Site disclaimer (sources/site/disclaimers.html): the Rebels list shows companies in ACTIVE strategies only and omits some for
  confidentiality or size -> coverage caveat for the report.
- Letters on /perspective are DocSend links (not machine-readable): surface tried, recorded.

## STATE 2026-09-28 21:55Z
- Grind complete: 183 members, 23 not_member, forusall-inc UNJUDGED (2019-2020 archive). A/B passes ab-1..3, graduation pass,
  cross pass (judgments-cross.py: Parafin $750M Bloomberg, Gusto $9.3B Fortune, Revolut $115B Bloomberg; notes via set-notes.py).
- Rule 10: companies/cross-rulings.json, 16 distinct + 19 accepted; in-flight verify then showed 0 disagreements. Siblings to
  align at the wave pass: a16z (Cowboy Space, Gusto, Lighter, Point, Revolut, Robinhood), Felicis (Gusto), Greylock (Revolut),
  Sequoia (Enter, Robinhood), Thrive (Robinhood), Creandum (Fuse), First Round (Farcaster, Gauntlet, Health IQ, Kiavi, Persona),
  Redpoint (Parafin), YC (Vouch: YC's Vouch IS Vouch Insurance, S19; its defunct came from First Round's namesake).
- Profile: scratch/write-profile.py (re-runnable; reads the landed base), firm-offices.py (Palo Alto, CA; ADV also lists New
  York), build-firm-profile.py (14 funds, 6 accessions asserted, 33 people), scratch/patch-profile.py (titles note).
  Titles overlay sources/web/team-titles.json + config site_api.team_sources[1]; 25 untitled people publish as 'other'.
  names.published in config (Cred, Root, Next Insurance, Nydig, Can Capital, Top Group, Bonify, DV01, Paraşüt).
- Duties: weak CIK audit clean (5 wrong-entity statuses/floats already overridden); unicorn re-intersect clean (Avant kill,
  Figure AI collision); caps fresh 2026-09-28; blind 5% sample (9 rows) with a subagent -> scratch/blind-results.json.
- decisions.md: kickoff text corrected (SPVs do file Form Ds; 40% non-US); R1 token-cap banding (OPEN), R2 Caret (OPEN), R3, R4.
- WebSearch used this session: ~64 (plus the blind judge's up to 12).

## CLOSE 2026-09-28 ~22:15Z
- Blind 5% (9 rows): 52/54 cells agree; Privy -> Growth, Teya keeps $1B on Sifted; both `unstable`. Duty 9: Lighter -> Growth.
- IA gap fetch STOPPED before it fired (BCV: the first request after a cooldown doubles the machine-wide block; Sutter Hill
  and 20VC active). ForUsAll decided on its own release (Ribbit led the $21M second round, Jan 2018): member, Growth.
- Rebuild 1: 195 rows (23 not_member out, 4 duplicates merged, Delphia + 14 Form D rows in); delta judged (14 out, Delphia in);
  rebuild 2: 181 rows. Both diffed: nothing re-keyed. prepare re-run; plain verify clean; export + review (checked on :8931).
- names.published extended (Checkout.com, CoinSwitch, GoodLeap, Policybazaar, QuintoAndar, Redefine, TaxBit, Ualá);
  cross-rulings 22 distinct (+Avant!, Lightning AI x2, Ping x3) + 19 accepted.
- report.md written; decisions.md R4 extended; run.py close done. Commit with the pathspec only; ingest awaits Erik.
