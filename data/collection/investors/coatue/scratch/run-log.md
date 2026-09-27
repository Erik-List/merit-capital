# Coatue run log (PRO-78). Resume point after a context reset.

Re-read data/collection/COLLECTION.md, then `python3 scripts/run.py status coatue`
(subcommands take the slug POSITIONALLY), then this file.

## Done (2026-09-26, UTC)
- Phase 0: documentation/decisions.md (D1-D12, X1-X4); Linear PRO-78 comment posted, issue In Progress.
- config.json written (desks, eras, traps, shape 0.60, edgar.thirteenf_ciks, edgar.registered_fund_ciks).
- Site: scratch/pull-site-coatue.py -> sources/site/portfolio-2026.json (372), posts.json (65), quick-takes.json (64).
- ADV: scratch/parse-adv.py -> sources/registers/adv-157910.json (RAUM $92.7B, 144 funds, GAV $126.9B).
- Own fund Form Ds: scratch/formd-own-issuers.py -> sources/edgar/formd-own-issuers.json (253 filings).
- NEW shared scripts: scripts/edgar-13f.py (13f-holdings.json, 1,384 issuers, 93 filings; per-filing dollar scale),
  scripts/edgar-registered-fund.py (registered-fund-holdings.json, 14 restricted issuers; N-CSR gives no acquisition dates).
- Roster curated: sources/wayback/partner-roster.json (35 people, basis per person).
- run.py collect coatue done: formd-sweep.json (2,237 accessions, 73 operating issuers), entities.json (163), edgar-companies.json (40 + 12 CTEK rows via scratch/merge-registered-fund-rows.py; RE-RUN that merge after any collect).
- Archive: IA in cooldown until ~02:05 UTC 2026-09-27; Common Crawl captures parsed (scratch/parse-cc-coatue.py) into sources/wayback/parsed/2024-2026.json. Every /portfolio capture carries only the grid's first 48 rows.
- Base v1 built (442 rows: A 110, B 263, C 69). prepare done: 442 rows queued in 10 batches (scratch/queue/).
- Wikipedia insource done (97 articles, 18 company candidates for the recall probe).
- scratch/siblings.json (238 rows with sibling facts; HOMONYMS exist, recognition-check each), scratch/cards.py (judge cards).

## Running / pending
- edgar-fts-sweep.py still running in background (log scratch/fts-sweep.log) -> sources/edgar/fts-hits.json.
- CC index pass (scratch/cc-index.log), then `pull-cc-coatue.py fetch` + parse again.
- Wayback pull after the cooldown: `python3 scripts/wayback-pull.py coatue`.
- Round research for every row: `scripts/graduation-surfaces.py coatue --slugs ...` (Google News firm+company, TechCrunch, Crunchbase News).
- The grind: 10 batches; judgments written compactly and expanded by scratch/emit.py; record per pair of batches.
- Then: recall probe (13F issuers listed after 2013 checked for a pre-IPO round; Wikipedia candidates; FTS registrants; parametric list),
  ONE rebuild, re-prepare, A/B pass on the $1B+ and public slice, momentum slice, caps (stockanalysis.com), duties 1-9,
  profile (build-firm-profile.py, firm-offices.py, icon dry run), verify, export, review, report.md, close, commit, Linear, message to Erik.

## Usage line
Kickoff: weekly 33%, Fable 5%. At 23:05 UTC: weekly 37%, Fable 11%. Web searches used so far: 8 of 200.

## Grind state (2026-09-27 00:40 UTC)
- identity-merges.json written (Lime, Grafana Labs, Uplight, BOSS Zhipin, Tome) and base REBUILT before any judgment: 438 rows.
- News surfaces ran for 407 rows (scratch/graduation-surfaces.json, 0 failures). scratch/siblings.json, cards.py, emit.py in place.
- Judgments: scratch/judgments/clusters-1.out.jsonl (55 not_member), batch-001..009.py (expanded by emit.py into scratch/queue/batch-00N.out.jsonl, all recorded).
- OPEN after the grind: (a) valuation pass for every row flagged needs_web_value (vr="later") plus canva; (b) cap pass for public rows (stockanalysis.com, IVP's caps.py pattern);
  (c) graduation pass for Seed rows (amo, butterflies-ai, fancraze, fero, httpie, lutra-ai, meticulous-ai, portalone, stability, sunday, wisdom-ai; skypilot censored, deepjudge graduated);
  (d) citations pending (flags cite_pending / stage_uncited); (e) country pass for non-US $1B+ rows (rule 6, hq_country_citation);
  (f) research list: dingdong-maicai, fiture, kujiale, rec-room, stytch, step, stash, gantry, youxinpai, legion-security round word, unresolved identities (ara, decidehq, dialect, graphy, radpod) via sources/web/company-sites.json;
  (g) identity merge to add: jetpack-io -> jetify; name pins at the rebuild (Alchemy, Snap, Mason, Meituan, CoreWeave, dbt Labs, ClassIn, Bitdeer, CloudWalk, XPeng, Endeavor, Chagee, Weidian, Valsoft, Reliable Robotics, Relativity Space, Persona, Komodo Health, Wisdom AI -> WisdomAI);
  (h) recall probe: Wikipedia candidates (Lunchclub, StarkWare is listed, Relativity is listed, Wolt, Manycore = Kujiale, Syrn, commercetools), fts-hits.json, 13F issuers listed after 2013, parametric list;
  (i) R1 class for Erik: site-listed positions entered at or after listing (Hut 8 ruled not_member; Endeavor kept, flagged boundary).

## State at 2026-09-27 01:10 UTC (context reset expected; resume HERE)
Command forms: `python3 scripts/run.py collect coatue` and `prepare coatue` are POSITIONAL; `record/status/verify/export/review/close` take `--investor coatue`.
Judging tools (all under scratch/): `cards.py <batch|all> [slugs]` prints evidence cards; judgments are compact dicts in `judgments/<name>.py`
(keys documented in emit.py); `python3 scratch/emit.py <name>` writes `queue/<name>.out.jsonl`; then `run.py record --investor coatue <file>`.
NEVER type a citation URL from memory: use esn/vn/gn (headline match against scratch/graduation-surfaces.json) or a URL copied whole from a source file.

DONE since the last entry
- All 438 queued rows judged once: 378 members classified, 60 not_member (clusters-1 + batch-001..009).
- Cap pass: 46 public rows pinned to stockanalysis.com caps as of 2026-09-25 (scratch/caps.py, scratch/caps/caps.json; HKD/INR rows converted with fx-convert.py).
- Valuation pass 1 (judgments/valuation-1.py): 31 private rows pinned to cited priced events; Rec Room now defunct; GoStudent and Rebel Foods below $1B on collapse evidence.
- Linear PRO-78: kickoff comment + milestone comment posted; issue In Progress.

RUNNING IN BACKGROUND (results arrive as task notifications)
- Research agent A: priced valuation events for ~22 rows still flagged needs_web_value (bytedance, ant-group, alchemy-insights, zuoyebang, rapyd, retool, sila, tamara,
  persona-identities, cloudwalk, form-energy, dayone, manner-coffee, vantage-data-centers, scala, abogenbio, classin, fiture, kuaikan-comics, mafengwo, pingpong, weidan),
  status questions (mech-mind and kujiale/Manycore HK listings, stytch, step, stash, gantry, dingdong, voltron-data, butterflies-ai) and the unidentified domains
  (ara, decidehq, graphy, radpod, crypthulhu-studios, meld, placement, product-science, revops, swarm-aero, sundeck, verse, httpie, lutra-ai).
- Research agent B: recall probe reading (20 SEC filings from sources/edgar/fts-hits.json + ~55 candidate deals to confirm a private Coatue round).
- `graduation-surfaces.py coatue --all-seed` (log scratch/surfaces-seed.log).

NEXT STEPS IN ORDER
1. Record agent A's findings (valuation-2.py; statuses; identities). Rows nobody can price: below_1b with the dated check in the note, or keep needs_web_value debt.
2. Graduation pass (judgments/graduation-1.py): sunday, portalone, fancraze graduated (gn headline match); wisdom-ai graduated (Series A Nov 2025, needs a URL);
   stability, fero, httpie, lutra-ai, meticulous-ai, butterflies-ai, amo decided by the absence test (graduation_source absence_check, graduation_asof today,
   graduation_surfaces lines "firm: ...", "formd: ...", "googlenews: ...", "techcrunch: ..."); every decided row needs entry_date.
3. identity-merges.json: add {"canonical": "jetify", "duplicates": ["jetpack-io"]}; pin names at the rebuild with "name" entries where needed
   (Alchemy, Snap, Mason, Meituan, CoreWeave, dbt Labs, ClassIn, Bitdeer, CloudWalk, XPeng, Endeavor, Chagee, Weidian, Valsoft, Reliable Robotics, Relativity Space, Persona, Komodo Health, WisdomAI).
4. Recall additions from agent B: ledger `recall_additions` entries (name, slug, citation, basis, first_seen, source) + member verdicts (evidence_class web or fund_filing).
5. Copy scratch/queue/queue.json (done once as scratch/queue-v1.json), ONE rebuild (`build-company-base.py coatue`), re-run scratch/merge-registered-fund-rows.py only if collect was re-run,
   `prepare coatue`, judge the delta. If the delta produces a membership verdict, one final rebuild.
6. Wayback pull (`python3 scripts/wayback-pull.py coatue`) once the IA cooldown has passed (after 02:05 UTC); eras are in config. Then it merges into sources/wayback/parsed/.
7. Country pass (rule 6): non-US rows at $1B+ need hq_country_citation (fetch the cited page, confirm it names the city).
8. A/B pass on the $1B+ and public slice; momentum slice (private rows first seen in the last five years in AI, Fintech, Data Infrastructure, DevTools get one web check recorded with valuation_range_source web_verified);
   duties 1-9 of COLLECTION.md 8 (blind 5% re-judgment uses scratch/queue-v1.json).
9. Profile: write investor/investor.json + investor/sources.json by hand-researched values, then `build-firm-profile.py coatue`, `firm-offices.py coatue`, icon `fetch-investor-icon.ts --discover https://www.coatue.com` and a --dry-run.
   AUM = sum of the private-markets vehicles' 7.B gross (master funds only) from sources/registers/adv-157910.json, labelled a floor; thesis = the site's own line
   ("Coatue is a lifecycle investment platform focused on turning big ideas into world-shaping technology companies." is the meta description; check the homepage headline); HQ New York.
10. `verify --investor coatue` (plain) green with flagged debt only; cross-rulings.json for homonym pairs (Abacus, Braintrust, Ghost, Clara, Cadence, Enter, Keep, Sunday, Nomic, Saturn, Rox, Sila, Upstream, Sweep, Open, Haystack, Handshake, PingPong, Flex, Titan, Origin, Verse)
    and accepted pairs where the sibling side is stale (Aurora Solar/Lux, Distyl/Khosla, Lyra/Greylock, Reify/Battery, Lighter/a16z, Norm Ai/Khosla, The Boring Company, Rapyd/Spark, Covariant).
11. export, review (serve with the review-surface launch entry and check it renders), report.md, playbook write-back proposal, `run.py close --investor coatue`, commit with pathspec
    (data/collection/investors/coatue plus the two new scripts scripts/edgar-13f.py and scripts/edgar-registered-fund.py), Linear comment, closing message to Erik with the ingest request. NO ingest without Erik's approval.

OPEN RULINGS FOR ERIK (collect for report.md)
X1 shape guard 0.60; X2 no crossover stage vocabulary, leaderboard needs a cohort floor; X3 registered-fund fair values never band a row; X4 no new valuation source from 13F/N-PORT;
R1 site-listed positions entered at or after listing (Hut 8 out, Endeavor kept); director-of-record members not on the firm's page (Nomos AI, Pill Club, Sungage, Fire Pit Collective);
Covariant status vs the acqui-hire ruling; Stability's $101M "seed" read as Seed; token-funded Braintrust.

USAGE LINE: kickoff weekly 33% / Fable 5%; at 01:10 UTC weekly 42% / Fable 20%. Web searches by this session: 10 (plus two research agents).

## 01:35 UTC additions
- graduation-1.out.jsonl recorded: sunday, portalone, fancraze graduated; stability, fero, httpie, meticulous-ai not graduated (absence test). Still open: amo, butterflies-ai, lutra-ai, wisdom-ai (graduated, needs the Series A URL).
- Brand names are fixed AT THE SOURCE: NAME_FIXES in scratch/pull-site-coatue.py (site_name keeps the page's rendering). Before the rebuild: re-run the pull script (offline cache) and
  `python3 scripts/site-portfolio.py coatue`. The rebuild will RENAME about 45 slugs; read rekey_overlays' output, and if it did not move an overlay, re-key
  classification.json and membership-ledger.json by hand from the old slug (old slug = slug of site_name) before prepare. identity-merges.json now also merges jetpack-io into jetify.
- Profile facts on file: venture-desk AUM floor $40,532,176,864 (111 private-markets master funds, ADV 2026-07-29; RAUM $92,705,722,582 stays in the basis);
  thesis candidates: homepage line "Investing in innovation through public and private markets with responsible risk management" and the meta description
  "Coatue is a lifecycle investment platform focused on turning big ideas into world-shaping technology companies."; site offices New York, Menlo Park, San Francisco, Hong Kong, London;
  notable five proposed: OpenAI, SpaceX, Uber, Spotify, Snap; icon: favicon.jpg 192px is marginal, the only vector is the CTEK logo, so the mark comes from the page markup.

## 00:10 UTC 2026-09-27 (CLOCK NOTE: the two entries above labelled 01:10 and 01:35 UTC were written at about 23:20 and 23:50 UTC on 2026-09-26; the IA cooldown ends about 02:05 UTC)
- Profile DRAFTS written: investor/investor.json and investor/sources.json (17 funds from the firm's own Form Ds, 12 with a sworn size and accession; AUM floor both ends;
  thesis = homepage line in quotation marks; history 69 words; notable five with slugs openai, spacex, uber, spotify, snap: the slug `snap` exists only after the rename rebuild).
  Team source: sources/site/team-curated.json (17 people, each with the record that gives the title), registered in config site_api.team_sources / team_buckets.
  Still to do at the profile step: run `python3 scripts/site-portfolio.py coatue` (writes team.json), `build-firm-profile.py coatue` (median, focus recompute, checks), `firm-offices.py coatue`, the icon.

## 00:35 UTC 2026-09-27
- Country pass recorded (country-1, country-2: 22 non-US $1B+ rows cited). STILL UNCITED: alan, choco, pleo, dapper-labs (need a page that names the city).
- Momentum slice recorded (momentum-1, momentum-2): 39 private hot-sector rows read below $1B each carry a dated web check (valuation_range_source web_verified).
- Site source regenerated with brand names (sources/site/companies.json) and team.json written (17 people). The BASE is not yet rebuilt on them.
- fixes-1 recorded (unresolved rows undetermined in all three columns; stage_uncited on fancraze, httpie, meticulous-ai; cite_pending on choco).
- KNOWN verify items to clear later: "edgar_links missing on 12 rows with forms" (the CTEK N-PORT rows carry no CIK by design; decide between giving them the fund's CIK for the link
  and teaching verify the exception; check what run.py does with a shared edgar_cik around line 1963 first); notable_investments pass only after `export`; `known positions missing`
  and `jetpack-io` clear at the rename rebuild; about 50 cross-investor lines need cross-rulings.json (homonyms distinct, stale siblings accepted) after the last valuation pass.
- OPEN Seed rows owing a graduation decision (5): amo (stage source model, entry 2023); butterflies-ai (stage source web_verified, entry 2024-06); lutra-ai (stage source model, entry 2024-04); wisdom-ai (stage source web_verified, entry 2025-05); fire-pit-collective-inc (stage source formd_band, entry 15-DEC-2022). Rows whose Seed comes from formd_band were never judged for stage: check each against the firm's page and the news file first.

## Agent A recorded (2026-09-27, about 00:50 UTC)
- scratch/record-agent-a.py -> agent-a-1.out.jsonl (20 valuations, ClassIn below $1B, Scala still needs_web_value, statuses: mech-mind and kujiale PUBLIC, stytch acquired, gantry and voltron-data defunct).
- scratch/record-agent-a2.py -> agent-a-2.out.jsonl (Seed entries with citations and absence tests whose Form D line is a search actually run; verse graduated; ara, graphy, radpod identities resolved by editing the overlay; decidehq and dialect stay unresolved).
- STILL OPEN: caps for mech-mind (stockanalysis quote/hkg/9615) and kujiale (quote/hkg/0068), both in HKD; graduation for amo, wisdom-ai (graduated, needs URL), fire-pit-collective-inc; scala valuation;
  "equity raised as a valuation floor" (dayone, vantage-data-centers) is an OPEN RULING for Erik. Agent B (recall probe) had not reported yet.

## 00:30 UTC 2026-09-27 (real clock)
- graduation-2.out.jsonl recorded (scratch/record-graduation-2.py). FINDING: the four standard surfaces MISSED three later rounds. Meticulous (Series A Jul 2026), Stability (Series B Aug 2026)
  and WisdomAI (Series A Nov 2025) are now graduated, each cited to the company's own post. RevOps acquired by Maxio (Mar 2025); Fire Pit Collective read acquired (KemperSports, Jul 2025), flagged.
  Every absence-test row was re-checked by one web search; the Form D line in each says what the name hits are. Write-back candidate: a name scan of the Form D data for single-deal vehicles
  named after the company (it was the "Meticulous Sept 2025" vehicle that exposed the miss), and a web search per no.
- Caps recorded for mech-mind ($1.33B) and kujiale/Manycore ($1.73B), converted from HKD.
- RECALL PROBE DONE: scratch/recall-additions.py wrote 4 ledger recall additions (lunchclub, wolt, syrn, firmus) and sources/web/recall-probe.json (113 rejections by reason).
  The full-text registrants that show a fund position were all base rows already. Lightfield = Tome renamed (Series A 2026-09-09 with Coatue taking part): note goes on the tome row.
  PIPE-at-SPAC positions (SoFi, Payoneer, Sunlight, CCC) rejected under T3: OPEN RULING for Erik (R1 class).
- Filing facts to record on existing rows: uplight entry = the March 2021 round at $1.5B (AES 8-K exhibit https://www.sec.gov/Archives/edgar/data/874761/000095010321003471/dp147276_ex9901.htm);
  dayone entry = Series B led by Coatue (GDS 6-K 2024-10-29 https://www.sec.gov/Archives/edgar/data/1526125/000110465924112068/tm2427015d1_ex99-1.htm);
  iambic: Coatue Ventures II LP holds 5.4% and is a Series A preferred holder (DRS https://www.sec.gov/Archives/edgar/data/1997038/000119312526315779/filename1.htm);
  nextdoor: management rights letter with Coatue Private Fund I dated 2014-08-29; singular-genomics and anaplan have NO status yet.
- Two research agents running: head office city citations (13 rows + Firmus + Scala value) and entry round citations (30 rows). Their reports arrive as hand-back messages.
- Wayback pull started in the background (it waits out the IA cooldown, ends 02:04 UTC); log scratch/wayback-pull.log.
- NEXT: rebuild now (renames about 45 slugs), prepare, judge the delta, record verdicts for the 4 additions; then enrichment records; cross-rulings; profile; a final rebuild after the Wayback pull lands.

## 01:25 UTC 2026-09-27
- REBUILD DONE (3 builder runs, all technical): base 381 rows. 23 slugs re-keyed by the builder, 5 by hand (jet-com, manycore-tech, weidian, uxin, mason); identity-merges.json now merges mason <- by-mason.
- Registered-fund rows REMOVED from sources/edgar/edgar-companies.json (the builder cannot link a filing under the fund's CIK; verify failed on it). Kalshi is now a ledger recall addition citing the N-PORT.
  scratch/merge-registered-fund-rows.py was rewritten to do exactly this; do NOT re-add the rows. decisions.md D4 amended.
- Recorded: delta-1 (4 recall additions + filing facts), fixes-2 (uipath cap restored, ghost band), country-3 and country-4 (rule 6 now clean for all 16 rows; Firmus mark raised to $10.5B, Aug 2026).
- companies/cross-rulings.json written: 24 distinct, 24 accepted. verify --in-flight then showed ZERO problems.
- Profile BUILT: investor/investor.json + sources.json (icon source = sources/site/logo-wordmark.svg saved from the page header, dry run preview investor/icon-preview.png; range $3M / $100M / $500M press-based;
  scope Generalist with 8 sectors; 17 funds; 17 people; sources/offices.json written). Socials stay null (the firm has no team page).
- config: one_b_share_max REMOVED (the playbook dropped the ceiling on 2026-09-26); decisions.md X1 withdrawn; run-time rulings R1 to R7 written.
- RUNNING AGENTS: entry round citations (30 rows), three valuation attack passes (51 old $1B+ marks + Rec Room, Gorillas, Hopin), blind re-judgment of 20 rows (scratch/blind-sample.json).
- Wayback pull still waiting out the IA cooldown (ends 02:04 UTC), log scratch/wayback-pull.log. After it lands: builder + prepare once more, judge any new rows.
- THEN: record agent results, plain verify, export, review (serve + check), report.md, write-back proposal, close, commit (pathspec), Linear comment, memory, closing message. NO ingest without Erik's approval.

## CLOCK CORRECTION (read at 00:42 UTC 2026-09-27 from `date -u`)
The two entries above labelled "00:30 UTC" and "01:25 UTC" were written at about 00:05 and 00:35 UTC. The IA cooldown still ends at 02:04 UTC.
- 00:42 UTC: stage-cites-1.out.jsonl recorded (30 rows: 25 confirmed, avail / choco / ramp / weights-biases corrected, geneva undetermined). Entry-round agent DONE.
- Still running: three valuation attack agents, the blind re-judgment agent. The Wayback pull is a background task that may be killed by its 10 minute limit; if scratch/wayback-pull.log stops growing, restart it after 02:04 UTC.

## 00:50 UTC 2026-09-27
- PLAIN verify: clean. export wrote companies/base.csv (381 rows); review.html built (566 KB) and checked on the review-surface server (port 8931, renders, no console errors).
- config names.published set for five Form D names; 43 leftover needs_web_value flags cleared (scala and vipkid keep theirs); scala banded below_1b under Rule A, flagged.
- scripts/edgar-13f.py FIXED: per-filing scale by implied price (the 2001 filings are in dollars, 2002 to 2022 in thousands); layer file rebuilt (1,399 issuers, 93 filings).
- documentation/report.md WRITTEN with two placeholders: AB_PASS_PLACEHOLDER (fill from the three attack agents + the blind agent) and USAGE_PLACEHOLDER.
  Usage read at 00:47 UTC: weekly 53%, Fable 41% (kickoff: weekly 33%, Fable 5%).
- WEB SEARCH BUDGET SPENT: the session's 200 searches are used up (subagents count against it). WebFetch still works.
- Nothing is committed yet: the whole investor directory is untracked. Closing commit = `git add` of the investor directory and the two new scripts by explicit path, then `git commit -- <those paths>`.
- WAITING FOR: attack agents 1 to 3, blind re-judgment agent, Wayback pull (after 02:04 UTC). After the pull: builder + prepare, judge new rows, verify, export, review, fill the report, close, commit, Linear, memory, closing message.

## 02:03 UTC 2026-09-27
- ATTACK PASS recorded (attack-1, attack-2): Panther acquired (Databricks), newer marks for Cadence, Checkr, Reify Health, Side; Attentive, Chainalysis, Cohesity, Postman, Relativity Space flagged needs_review; 41 marks stand.
  cross-rulings.json: +1 accepted (panther vs lightspeed), now 24 distinct / 25 accepted. Databricks mark corrected to $190B (fixes-6).
- scratch/verify-urls.py re-fetches agent-reported citation pages (stage, country, valuation files all passed).
- BLIND RE-JUDGMENT done (scratch/blind-sample.json, 20 rows, 100 cells): 7 cells on 5 rows disagreed. Adjudicated in blind-1.out.jsonl:
  * nomos-ai-inc IS Norm Ai (registered name Nomos Ai Inc.): identity-merges.json now merges norm-ai <- nomos-ai-inc; applies at the NEXT builder run. After it, drop the `nomos-ai-inc` key from classification.json if it is left behind.
  * norm-ai entry corrected to Seed (Coatue led the seed, the A and the B), graduated -> S2A cohort 21, graduated 9.
  * take-take-take Pre-Seed; kikoff Series A + $1.5B mark (needs_review); lighter and moonpay city flagged `unstable`; commonwealth-fusion-systems needs_review (no stated valuation).
- CLASS SWEEP (duty 9) RUNNING: three agents check the 55 rows with an undetermined entry stage (lists in the scratchpad, und-part1..3.txt). They search by page fetch because the WebSearch budget is spent.
- report.md: A/B section and usage filled; BLIND_PLACEHOLDER still open; counts must be refreshed after the sweep and the final build.
- Wayback pull starts when the cooldown ends (02:04 UTC).

## 02:10 UTC 2026-09-27 (written 13:58 UTC, after a pause on the usage limit)
- Wayback pull DONE after the cooldown: 2023 capture added (48 rows, IA); 2024-2026 stay Common Crawl (parse-cc-coatue.py re-run to merge). No archive name the base lacks.
- Builder run 4: base 380 rows (norm-ai absorbed nomos-ai-inc); classification key nomos-ai-inc removed by hand; prepare-5 (2 rows queued: decidehq, dialect, the two unnameable rows);
  config names.published entry for nomos-ai-inc removed; cross-rulings.json +2 accepted (kikoff vs lightspeed, norm-ai vs khosla nomos-ai-inc) -> 24 distinct / 27 accepted.
- verify clean, export 380 rows, profile rebuilt. S2A: 22 seed entries, 1 censored, cohort 21, graduated 9, rate 42.9%.
- report.md: BLIND section written; ENTRY_DATES_LINE placeholder left at the Debt section; counts to refresh at the end.
- The three sweep agents (55 undetermined stages) FAILED on the account's usage limit before reporting. Resumed 13:58 UTC: the sweep is done in this session by page fetch.

## 14:40 UTC 2026-09-27: CLOSE
- Stage sweep done in-session (stage-sweep.py, open-hit.py; stage-sweep-1/2.out.jsonl): Distyl Seed (graduated), OneText and Dirac Seed (censored), Sourceful Series A, Figma Growth (2024 secondary);
  Saturn acquired by Snap (June 2025); Lead Bank, Nate, Swarm Aero, Open stay undetermined with the page cited. Sri Viswanath removed from the team (left fall 2025).
- Momentum citations re-checked: 7 of 39 named another company (arch, fero, lindy, sundeck, titan, tome, karat); replaced (fixes-8). Saturn value source set (fixes-7).
- Teamflow merged into Lindy (identity-merges.json; the founder: same legal entity). Builder run 5: base 379; teamflow overlay key removed by hand; prepare-6.
- All 125 private $1B+ valuation citations re-fetched: hold (check-value-cites.py).
- FINAL: base 379, verify clean (plain), export 379, review 579 KB rendered, profile rebuilt (16 people). S2A 25 seed, 3 censored, cohort 22, graduated 10, 45.5%.
- report.md final. Usage at close: weekly 74%, Fable 80%. NOT INGESTED: waits for Erik.
