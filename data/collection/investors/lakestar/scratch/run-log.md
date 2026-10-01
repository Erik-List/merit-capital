# Lakestar run log (PRO-108)

Kickoff 2026-10-01 10:31 local (machine clock EDT) on Erik's "please collect Lakestar". One session, one run, slug `lakestar`.

## Usage line at kickoff (get_usage)
- 5-hour limit 3% (resets 19:20 UTC)
- Weekly, all models: 73% (resets 2026-10-06 18:00 UTC)
- Weekly, Fable: 8%
- Extra usage: disabled

## Siblings on this checkout at kickoff
- Live sessions: Index Ventures collection, Collect Bessemer, more Robust IA (tooling), Less Open Decisions.
- In-flight markers present: atomico, bain-capital-ventures, founders-fund, general-catalyst (not this session's to touch).
- IA: the pull of 15 listing captures ended in a firewall refusal at 10:36 (machine-wide cooldown 60 min, set by ia_fetch). Common Crawl carried the archive meanwhile.

## Prompt count
1. kickoff ("please collect Lakestar")

## Layer notes
- Live site (July 2026 relaunch): Next.js on headless WordPress, wp-json open. Three logo blocks (home 11, /funds 15, /resilience 21) and the Resilience I press release (20 names): 38 companies, no names in the blocks (mapped from logo file stems in scratch/site_2026.py), no dates, rounds or team list.
- Archive: lakestar.com CDX 3,278 URL keys (scratch/cdx/). Site generations: WordPress 2011-2013 (/portfolio/<slug>), parked 2014-2017, single page 2018-2021 (logo strip, /about highlights, /team with per-partner company lists), Next.js on Craft CMS 2022 to June 2026 (/portfolio with 98-109 companies, stage + thesis; /company/<slug> with deal partners; /team; /news).
- Common Crawl (static cluster.idx route; scratch/cc-cluster.py, cc-fetch.py from Project A): 545 captures 2013-2026, all fetched. scratch/archive_listings.py parses both archives: 140 companies, 95 people.
- Firm posts: 105 archived news posts indexed per company (scratch/press_index.py, sources/site/press-archive.json).
- EDGAR: 7 Lakestar filers (3 GP 13F filers: Spotify; Opendoor + Oscar; Oscar. 4 fund Form D filers). No ADV. Full-text sweep 9 phrases, 63 registrants: Oscar Health S-1 (IRA lists Lakestar I, II and Growth I), C.H. Robinson 8-K (sennder), the rest person bios, LP-side registered funds and namesakes. Form D roster sweep: 132 accessions, 74 issuers.
- Zefix (Swiss register): open JSON, no key. Lakestar Advisors GmbH (CHE-114.605.813, ex Brightsquare Consulting GmbH, owned by Hommels Holding GmbH until 2023), Lakestar Holding AG (2022).

## State at 11:20 local (resume notes; read with COLLECTION.md and `run.py status --investor lakestar`)
- Base built once (197 rows: 158 listed, 39 Form D name-matches). `prepare` ran; queue 197 items. Surfaces ran for the 158 listed rows (scratch/graduation-surfaces.json).
- Verdicts recorded: 38 Form D rows (scratch/judgments-formd.py; ShareIQ re-ruled not_member, seat only), 8 D2 rows not_member (scratch/judgments-d2.py: facebook, skype, airbnb, klarna, king, coinbase, sumup, helsing). feed-media-inc still unjudged (2013 site row pending).
- Research: 7 sonnet agents wrote scratch/research-g0..g6.json per scratch/row-research-brief.md (groups in research-groups.json); D2 research in research-d2.json (opus). scratch/judge_research.py turns research into record lines (`--dry` prints the table; overrides in scratch/judge-overrides.json). scratch/check_research.py lists rows whose entry is uncited or dated after the first archive listing -> scratch/second-pass.json. NOTHING from the g-files is recorded yet.
- Known fixes to apply: tesseract is Fuse Energy (identity merge at the rebuild); netspeak-games entry is the 2020 seed, not the 2022 Series A; the 2013-site rows (IA pull scratch/ia_pull.py --max-year 2013, cooldown ended ~11:36) are the founder's angel book and get not_member under D2 once parsed (scratch/archive_listings.py needs a 2013 parser).
- Recall probe agent running -> scratch/recall-candidates.json. Roster gained Henrik Persson (build_roster.py edited, not re-run; re-run `collect` before the scheduled rebuild).
- Profile groundwork: icon composed (sources/site/lakestar-mark-composed.svg, dry run ok), team-cards.json (2026-06-09 team page), fund facts: Lakestar I EUR 135M 2013 (TechCrunch 2015-08-23), II EUR 350M 2015, III $245M + Growth I $490M Feb 2020 (unquote), Early IV + Growth II ~$600M April 2024 (firm post), CF I $265M Sept 2025 (firm), Resilience I $300M July 2026 (firm). Thesis line: homepage headline "Patient. Principled. Founder-centric." No ADV: AUM firm-stated (EUR 2bn funds, April 2024; "$6 billion" platform incl. personal investments, 2026). HQ Zurich (legal page).
- WebSearch tally: main 6, D2 23, g3 12, g6 14 (others to add). Cap 200.
- Usage at 11:20: 5-hour 24%, weekly all models 79%, Fable 17%.

## State at 12:05 local
- Scheduled rebuild done (165 rows; 47 excluded; merges fuse-energy<-tesseract, reneo<-condo, onlife<-aglet; 7 recall additions: chamo-games, cosine, juo, generalmind, antidote, pit, argo). `prepare` re-run. Delta verdicts recorded: 10 rows of the 2013 site + idx-llc not_member (need the FINAL rebuild before export), recall additions member + classified.
- Recorded so far: research-ok (76 rows), research-second (53), research-recall (7), duty-7 fixes (qmware St. Gallen, trace Austin/Media, kinta-ai unstable). Each row recorded once; patches without `note` or with the full note (record note-join bug).
- Second research pass: scratch/research2-s0..s2.json (21 entries cited of 71). Overrides in scratch/judge-overrides.json. R1 to R7 in decisions.md.
- Still to record: the 39 visible rows (group `visible` in research-groups.json) once scratch/visible-research.json is complete (opus agent, A/B pass): `python3 scratch/judge_research.py visible --dry`, review, then record.
- Blind 5% (duty 7): documentation/duty7-blind.json, 8 rows; adjudicated (see report).
- Profile inputs: scratch/build_profile_inputs.py writes investor/investor.json + sources.json (re-run after the grind, then scripts/build-firm-profile.py lakestar). offices.json written (Zurich, site statement). Thesis: title-tag tagline. Socials: 0/30, gap recorded in config profile.socials_gap.
- WebSearch tally: main 7, D2 23, g0-g6 88, recall 10, s0-s2 30, blind 8, visible up to 22 = about 188 of 200.
- IA: second firewall block at 11:37 (cooldown 120 min) after 19 of 23 captures of the 2013 site; 132 further IA captures (company, team and news pages Common Crawl lacks) not pulled: debt.
- Disk: 2.0 GB free at 11:23 (99% used).

## State at 12:40 local: GRIND COMPLETE, plain verify CLEAN (resume here after a compaction)
- Final rebuild done: base 154 rows, all members, all classified; excluded.json 58. `run.py verify --investor lakestar` prints `verify: clean`. `export` and `review` written (base.csv 154 rows; review.html checked on the review surface: 154/154 rows, profile panel opens, no console errors).
- Profile built (`scratch/build_profile_inputs.py` then `scripts/build-firm-profile.py lakestar`): HQ Zurich (site statement), AUM $2.1458B to $6B firm-stated, 7 funds, range $4.5M / $15.7M / $80M over 91 entry rounds, notables Spotify, Revolut, SoFi, Opendoor, Glovo, 30 individuals, socials 0/30 (gap in config profile.socials_gap). Icon source: sources/site/lakestar-mark-composed.svg (dry run ok).
- Results: private 108, acquired 30, defunct 8, public 6, unknown 2; $1B+ 27 (17.5%), $10B+ 2 (SoFi, Poolside), $100B+ 2 (Revolut, Spotify); stages Seed 46, Growth 36, Series A 22, Pre-Seed 2, undetermined 48; S2A: 46 seed entries, 11 censored, cohort 35, graduated 17, not graduated 18 (15 absence test, 3 cited end), rate 48.6%. Countries DE 42, GB 39, US 30, CH 9, SE 7, FR 7.
- Cross-investor: companies/cross-rulings.json holds 8 distinct pairs, 2 accepted a16z pairs (pit, onodrim: unidentified a16z rows) and 12 accepted STALE-SIBLING pairs to align at ingest and then remove: cherry (aware, rows), accel (cambridge-aerospace, public, rows), greylock (entrepreneur-first), lux-capital (kela-technologies, varda), sequoia-capital (kela), lightspeed (lemon-markets), seedcamp (priori-data), khosla-ventures (varda). Kit to adapt: data/collection/investors/project-a-ventures/scratch/align/{align.py,reingest.py,precheck.sh}; readback tool data/collection/investors/20vc/scratch/align/readback.ts. Skip books with scratch/in-flight.json (atomico, bain-capital-ventures, founders-fund, general-catalyst, speedinvest, index-ventures, bessemer) or uncommitted company files.
- STILL TO DO, in order: (1) documentation/report.md; (2) `python3 scripts/run.py close --investor lakestar`; (3) closing commit with explicit pathspec `git commit -- data/collection/investors/lakestar` (git add that directory only; never add -A); (4) ingest gate COLLECTION.md s9: `npx tsx scripts/fetch-investor-icon.ts lakestar data/collection/investors/lakestar/sources/site/lakestar-mark-composed.svg`, `npx tsx scripts/ingest-investor.ts lakestar`, `npx tsx scripts/ingest-companies.ts lakestar --dry-run` (expect 154 new, 0 removed), write, readback `npx tsx data/collection/investors/20vc/scratch/align/readback.ts lakestar --investor-row`; commit the icon provenance; (5) sibling alignment; (6) Linear PRO-108 closing comment + state Done, PRO-87 comment with archetype-B corrections; (7) memory file lakestar-run-pro108.md + MEMORY.md line; (8) closing message to Erik with results, open rulings, what was ingested. If the permission classifier refuses a DB write: do not work around it; list the remaining commands in report.md section 15 and tell Erik.
- Open rulings for the report (section 10): Helsing and the founder-investment class (D2, R5); 2013-site rows (R4); Terra Quantum SPAC mark (R7); 1047 Games band, one ruling for three books (R9); majority takeovers read acquired (R8); unnamed rounds between named rounds (R6: Marley Spoon, Omio, Harry's as Series A); ShareIQ seat-only (R3); 2026 own-capital deals in, scout/Halo out (R2, R4); Spotify Growth on structure (R10); AUM range ($2.15B funds vs $6B platform); ShapeShift defunct with a live GmbH, Kinta AI unknown; Lightium and Picterra published as Zurich and Lausanne (register seats Schlieren, Chavannes-pres-Renens); a16z's unidentified Pit and Onodrim rows; 48 undetermined stages; OneFootball below $1B.
- WebSearch total: 178 of 200 (main 7, D2 23, g0-g6 88, recall 10, s0-s2 30, blind 8, visible 12).
- Usage at 12:40: 5-hour 79%, weekly all models 93%, Fable 42% (kickoff: 3%, 73%, 8%).
- Process notes for the report: a research subagent ran `pkill -f news.py` (may have killed other sessions' helpers); `timeout` does not exist on macOS, so the Google News helper hung for agents; IA blocked twice (15 and 19 fetches); disk 2.0 GB free.
