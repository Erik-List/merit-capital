# BCV run log (PRO-162)

Kickoff 2026-09-27 19:05 UTC, prompt 1 ("please collect bain capital ventures").
Usage line: weekly / Fable percentages not readable from this session (no usage tool call made at kickoff); record at close if available.

## RESUME NOTES
- Re-read COLLECTION.md, then `python3 scripts/run.py status --investor bain-capital-ventures`.
- Boundary: decisions.md D1 (own RIA CRD 145652, crypto inside, no partition), D2/R1 (pre-2001 Bain Capital heritage out, flagged).
- Sources so far: sources/site (Sanity pull via scratch/pull-sanity.py + shape-site.py; crypto WP via pull-crypto.py),
  sources/registers/adv-145652.pdf, sources/wayback (2011-2015 era via wayback-pull; old eras via scratch/wayback-old-eras.py,
  enumerated from sources/wayback/cdx-domain.txt while CDX answered 503), sources/edgar (entities, edgar-companies, fts-hits, formd-sweep),
  sources/web/wikipedia-insource.json, scratch/insights-pack.json (firm's own posts by company).

## STATE
- 19:19 UTC IA firewall cooldown set machine-wide (another session tripped it), clears ~20:19 UTC.
- 19:30 UTC DISK FULL on the machine (~150 MB free). edgar-companies failed once on ENOSPC, re-ran clean. Erik notified.
- Provisional roster (33 people, no archived windows) -> formd-sweep (459 issuers) -> preliminary base 513 rows -> wikipedia sweep (63 articles, 17 candidates).

## TODO before prepare
1. After IA cooldown: finish scratch/wayback-old-eras.py (67 listing captures); re-run wayback-pull.py for the /portfolio/ 2016+ era (came back empty in a 503 spell).
2. partner-roster.py (people pages with capture years) -> scratch/roster-cdx.json; fetch titles of archived-only people to keep investors only; rebuild roster; re-run formd-query.
3. Rebuild base; not_members traps + known_positions in config; score site_stage (Seed/Early/Growth) for entry_stage_fields.
4. graduation-surfaces is run after prepare identifies Seed rows.

## STATE 2026-09-27 20:40 UTC (session 2, Erik: "continue with cc")
- Disk freed by Erik (6.9 GB). IA blocked again 20:19 UTC (120 min cooldown, to ~22:20).
- Common Crawl carries the archive layer (Erik 2026-09-26 ruling): scratch/cc-cluster.py (3,704 captures, 2009-2026),
  cc-fetch.py (830 bodies, 0 failed), cc-parse.py (listings 2010/2012/2013/2016-2022, company pages 2012-15 with
  "How we worked with" + exit lines, WP pages with Status/Exit/Stage/BCV Lead), cc-roster.py (212 people, titles, bio start years).
- Old IA eras: 2003 (44) and 2006 (101) parsed from cache (wayback-old-eras.py --cached-only); 45 captures (2007-09) wait for IA.
- Roster 66 people (build-roster.py, investing titles only); formd sweep 622 issuers.
- Identity merges: 30 (companies/identity-merges.json). Base 638 rows (639 incl. dup marker). prepare done: 15 batches, 638 open.
- graduation-surfaces running (investor/investor.json is a name-only stub until the profile build).

## GRIND TOOLING
- scratch/show.py --batch N  (queue item + evidence pack); scratch/judge_lib.py (verdict/cls/rnd/write, POST/SITE/W/ARC citations);
  scratch/judgments-N.py per batch; news.py for Google News; verify-urls.py for agent URLs.

## GRIND STATE (session 2)
- 20:45 heritage pass (37 verdicts), members-1 pass (87 verdicts: prior-firm/after-tenure seats, namesakes, 7 legal-entity dups).
- Batches 1-4 classified (172 rows). Seed graduations without a clear later round are left open for a graduation pass
  (re-run graduation-surfaces.py after the grind, then judge the nos with the absence test).
- Identity merges added for the rebuild: Halo x3, Factor Systems/Billtrust, Thorley/4moms, SM Holdco/SurveyMonkey, Cellular Longevity/Loyal,
  Material Technologies/Material Bank, Shop My Shelf/ShopMy, M|C Acquisition, Apparent Networks/AppNeta, Fingerhut/Bluestem,
  EData/EDR, ShiftLeft/Qwiet.
- Still open: 41 in-tenure name-match rows (wait for news-sweep to finish), batches 5-15, A/B pass (ACV cap, Lime cap, Attentive mark),
  graduation pass, recall probe (FTS + Wikipedia candidates), rebuild, delta.
- WebSearch used: 2 of 200.

## 2026-09-27 21:50Z (session 2, "continue with cc")
- Batch 5 recorded (judgments-5.py): SolarWinds OUT as control (S-1: investors led by BCV and Insight bought 67.8% in the Dec 2005
  recap; Insight excluded the same deal), SurveyMonkey + sm-holdco-llc OUT as control (Spectrum + Bain majority 2009), Zelis OUT
  (control), US LEC OUT (T3 placement in a listed company). SquareTrade kept as member (2012 "$238M growth equity"); control question
  OPEN for Erik (merger agreement's "Contingent Consideration attributable to the Bain Capital Transaction").
- Membership pass 2 (judgments-members-2.py, formd-addr.py reads related-person addresses): all 41 in-tenure name-match rows decided.
  Members: camino-real-inc (Ajay c/o Bain Capital 111 Huntington), idelic-inc (Kevin Zhang at 200 Clarendon), superstate-inc
  (Bain Capital Crypto led the $82.5M Series B, Jan 2026), mmjk-inc (PurePlay; Salil, director-of-record), mynd-management-inc
  (Clelia Peters, VP 2020-21, medium, flagged), boon-business-solutions-inc (Noah Breslow, Operating Partner, medium, flagged).
  Dups: scryer-inc -> reonomy-altus-group, groupay-inc -> gocardless (identity-merges.json). AMGH = Air Medical Group Holdings,
  Bain Capital PE buyout 2010 -> OUT control. Rest OUT (namesakes, pre-tenure, uncorroborated common names).
- bain-capital-ventures-investments = navigation link -> not_member; added to config wayback.non_company_slugs + rejects.
- adentro + zenreach are one company -> merge (canonical adentro, the live list's rendering).
- Ledger: 639/639 judged. Classification 219 rows before the parallel grind.
- Parallel grind: 7 judges on batches 6, 7, 8, 9, 10, 11, 12-14 (brief scratch/JUDGE-BRIEF.md; NQ_TAG per judge; record under the
  per-investor lock). One more agent triages the EDGAR full-text registrants -> scratch/recall/fts-triage.json.
- Recall probe (mine): scratch/recall/rejections.json (Wikipedia noise, other Bain desks, parametric candidates without a source);
  recall_additions: Cogsy (the firm's own seed post, 2021-12-22).
- Profile notes: thesis = homepage H1 "Capital's duty to the future." (competing: meta description "Bain Capital Ventures helps
  founders build iconic businesses that transform the way we live and work."). Socials: x.com/BainCapVC,
  linkedin.com/company/bain-capital-ventures. Homepage also announces "$1.6B for BCV Fund XI", "Autodesk ... MaintainX for $3.6B",
  "Moveworks + ServiceNow".
- IA cooldown ends ~22:20Z: then wayback-old-eras.py (45 captures) + wayback-pull.py for the 2016+ era.
- WebSearch used: 2 of 200 (judges capped at 12 each).
- Fund ladder for the profile (scratch/fund-formds.json has every vehicle's Form D): Fund XI $1.6B (businesswire 2026-09-16, in
  news-sweep; homepage "We've raised $1.6B for BCV Fund XI"), Fund X + Select IV $1.9B (post bcv-launches-new-fund-x-select-iv-funds,
  2023-02-28), Fund 2021 "our ninth core fund ... $1.3 billion" (post announcing-bcv-fund-2021, 2021-05-20), $1B in Nov 2018 (Fund
  2019 $650M + Coinvestment II $250M, Form Ds; post 1-billion-to-fuel..., which also says "$4.9 billion under management" and
  "2001"), Fund 2016 $600M, Fund 2014 $650M + Coinvestment $200M, Fund 2012 $600.6M (Form D totals sold). Crypto I/II sizes: find.
- Fund table (Wikipedia "Bain Capital Ventures", insource sweep): I 2001 $250M; II 2005 $250M; III 2007 $500M; IV 2009 $525M;
  V 2012 $660M (Form D total sold $600.6M); VI 2014 $650M + $200M coinvest; VII 2016 $600M; VIII 2019 $650M + $250M;
  IX 2021 $950M + $350M; X 2023 $1,440M + $480M (Select IV); XI 2026 $1.6B. Infobox: founded 2001, AUM $10B. Crypto I/II: cite needed.
- A/B part 1 recorded: Lime $1.9B (2026-09-25), ACV $1.78B, Rapid7 $783M (below_1b), Attentive $5B (2021-06, stale; Sequoia's
  $2.7B is an uncited secondary estimate), DCG $10B -> 10b_plus web_verified (CNBC 2021-11-01).
- More merges: seed-cx -> zero-hash, btrs-holdings-inc -> billtrust (found by the batch-12 judge). 46 merges.
- Old-era IA pull queued in the background (sleeps out the cooldown).
- Batch 12-14 judge done (judgments-12.py): 9 rows, 10 merge duplicates skipped. Cross-rulings to write: wonder accepted vs accel
  (BCV fresher, $9B July 2026, Restaurant Dive); wonder distinct vs eqt-ventures (wonder.me) and first-round-capital (research service).
  Work 'N Gear: "Expansion/Growth Buyout" bucket but no control evidence (CEO bought it out of bankruptcy 2002, ~$40M VC).
- EDGAR triage done (scratch/recall/fts-triage.json, 96 registrants): 81 in_base, 10 noise, 4 other Bain desk, 1 control (Domino's,
  not in base); zero candidate additions. Follow-up: signify-health -> not_member (sale consideration for Remedy Partners).
- Batch 7 judge done (judgments-7.py): 37 rows + 2 verdicts (eschelon-telecom heritage, ctc-communications T3). Merges added:
  datica -> sansoro-health, swift-prepaid-solutions + onbe -> davinci-payments, digital-compliance -> venminder-digital-comply,
  concurrent -> driven (50 merges). Onera fixed: ToolsGroup bought it June 2022 (the firm's "Lyniate" label is Datica's).
  OPEN for Erik: Syncapay's 2019 purchase of Swift Prepaid (BCV with Silversmith, MissionOG, Nyca) may be a control position;
  epoch / ecredit-com / dexterus / el-dorado-marketing had Bain PE directors (Nunnelly, Pagliuca, Ward) on their boards around
  2000: possible generalist-fund positions (R1), kept as members for lack of a fund-level source.
  Cross-rulings to write: distinct corridor (felicis), daylight (a16z, usv), curio (cherry), dream (a16z, y-combinator);
  accepted (BCV fresher or corrected) cognition vs 8vc/khosla/lux ($48B Series E, TechCrunch 2026-09-08), crosby vs sequoia,
  dna-games vs battery (city).
- Batch 8 judge done (judgments-8.py): 37 rows + 2 verdicts (instinet heritage/T3; ipay control: "our new majority shareholders",
  Spectrum + BCV, Dec 2006). Merge 1-800-dentist -> futuredontics (51 merges); fingerhut was already merged into bluestem-brands.
  OPEN for Erik: Fingerhut's Feb 2004 round (did the investor group take 50%+? Wikipedia lists "Bain Capital Ventures (2004)" among
  its owners). Check ameritrade (batch 6): likely the Datek stake (BCI Datek Investors, Fund VII) = other desk + sale consideration.
  Cross-rulings: distinct grain/hera/laika/index (y-combinator), index (greylock); accepted forus vs accel/gc/redpoint/thrive ($3B
  Series C Sept 2026), feather vs spark (acquired by Vesta Nov 2023), legacy vs y-combinator (Boston).
  fuel's Toronto rests on Tracxn only (weak).
- Batch 6 judge done (35 rows + 3 heritage verdicts: ameritrade, amr-interactive, cameraworld-com, all on Bain Capital Private
  Equity's own portfolio list). Batch 11 judge done (35 rows + 3 verdicts: usinternetworking control (Bain PE bought all of listed
  USi out of Chapter 11, 2002), swift-prepaid-solutions control (Syncapay holdco), the-lifelike-company heritage (Romney 1996)).
- fix-2: Bain PE's list (baincapitalprivateequity.com/portfolio/current-and-former-portfolio-companies, read 2026-09-27) carries
  Stream, TravelCLICK, Ameritrade, EPOCH Holdings, eCredit.com (SR Research), DexterUs; NOT Vonage, Taleo, El Dorado, Ameritox,
  Archer, Work 'N Gear. -> stream, epoch, ecredit-com, dexterus OUT (heritage, medium). davinci-payments + onbe OUT (control,
  medium, the Syncapay lineage). TravelClick KEPT (on BCV's live list = 2007+ venture fund, 10%+) but OPEN for Erik: both desks
  held it; the 2007 entry may be a co-investment in Genstar's buyout.
- Adaptive: two CMS docs titled "Adaptive" folded into one row; shape-site.py now brackets the domain on the second
  ("Adaptive (adaptive.co)", home health, /portfolio/adaptive-health/, Seed 2025) -> its own row at the rebuild; 'adaptive' is
  Adaptive Security. Merge basecoin -> basis (52 merges).
- TOOLING REQUEST (for Erik; no tooling session running): scripts/run.py ISO_OF lacks Liechtenstein (LI); Celestia (Vaduz) is left
  without a country until it is added.
- Cross-rulings: distinct arc (menlo), atoms (a16z), basis (accel, khosla), archer (y-combinator), swish + trade (y-combinator);
  accepted arc vs a16z (Axos closed July 2026), ameritox vs sequoia (asset sale 2018), trucksmarter vs a16z/thrive (acquired
  2026-09-02), veza vs accel (ServiceNow, March 2026).
- Batch 9 judge done (37 rows + 4 verdicts: maxm-systems heritage; onesource-information-services heritage + control (1993
  Lotus buyout, Information Partners); m-c-communications + m-c-acquisition-corp control (Bain Capital bought M/C in 2004)).
  Merge magazineradar -> media-radar (53 merges). Cross-rulings: distinct lumina + momento (y-combinator); accepted oratomic vs
  khosla (Pasadena); fresher marks lumilens $5.51B, mind-robotics $3.4B, modal $4.65B (check siblings at rule 10).
  Hunches: medivision, market-metrics maybe 1990s generalist positions (not on the PE list check yet); ndata vendor-only.
- Batch 10 judge done (38 rows + 3 verdicts: publishing-group-of-america + pgoa-media control (BCV + Shamrock bought it from
  Quadrangle; medium); risk-management-solutions heritage (DMGT bought RMS Jan 1998; medium)). Merge radionomy-azerion -> targetspot
  (54 merges; the live "Radionomy (Azerion), 2008" is the TargetSpot position). Cross-rulings: distinct orb-labs (greylock, menlo),
  osmo (accel, lux), palette (y-combinator; YC's palettehq is the match), primitive, pronto, skip (y-combinator), puzzle (felicis),
  scroll (usv); accepted rillet ($1B), shopmy vs menlo ($1.5B), poolside vs redpoint ($12B, 10b_plus), periodic-labs +
  prophet-security (Menlo Park).
- Heritage pass 2 (judgments-heritage2.py): 17 archive-only rows on Bain PE's list with no venture-vehicle record -> OUT (medium,
  R1): closings-ltd, cmc, convey-software, etranslate, environmental-data-resources-inc, imagitas, iwon-com, jtech, market-metrics,
  medivision, netlibrary, oasis-asset-management, professional-advantage-financial, profitlogic, shopping-com, strategic-mapping,
  t-r-a-d-e-inc. PE list saved as sources/web/bain-pe-portfolio.json.
- ALL SEVEN JUDGES DONE. Classification 447 rows.
- 22:20:30Z IA re-trip: the first request of wayback-old-eras.py after the 240-min cooldown ended was refused again (firewall
  signature on /portfolio/index.asp); ia_fetch set a 480-min machine-wide cooldown (to ~06:20Z). Pull stopped. The 45 captures of
  2007-2009 stay pending: ARCHIVE DEBT for the report (rows listed only in 2007-2009 and gone by the 2010 CC capture may be missing).
  The 2016+ era is covered by Common Crawl (parsed/2016-2022); wayback-pull.py is NOT run (it would rewrite those year files).
- 22:42Z: IA cooldown now 480 min (re-trip at 22:20:30 on the first request); old-era pull stopped; 2007-2009 = archive debt.
- REBUILD done (three passes, because of a tooling defect): build 1 moved 17 excluded rows' verdicts onto name-variant rows (the rename
  step treats excluded rows as departed; two landed on other companies: ameritrade -> 2006 Shopping.com row, stream -> Stream Global
  Services Form D row). Restored by hand under the record lock; resurfaced renderings of excluded canonicals given their own verdicts
  (judgments-rebuild1.py, rebuild2.py). Build 3 clean: base 417, excluded 226, no renames. TOOLING REQUEST for Erik: rekey_overlays
  should count excluded rows as present.
- Adaptive split: site-portfolio.py re-run + never_merge pair; adaptive-adaptive-co = Adaptive Innovations (home health; Seed 2025,
  graduated by the Felicis-led $50M Series A, June 2026). Cogsy recorded (member via the firm's post; acquired by Mayple 2023; GB via
  Companies House 12973044; not graduated, the acquisition ended the window). Bluestem stage undetermined (Fingerhut 2004 control Q open).
- Merge sneakpeeq -> symphony-commerce (one issuer CIK 1517646): Seed 2011 (TechCrunch) graduated by FirstMark's $7.5M Series A 2012.
- fix-3: focus on 32 rows, caps DocuSign $12.62B / Flywire $2.12B / Rubrik $22.71B (stockanalysis 2026-09-25), ACV stage cite
  (S-1 exhibit), Cube seed cite (TechCrunch), TrueMotion stage_uncited. known_positions: surveymonkey removed.
- Graduation pass: graduation-surfaces.py clean (39 rows, 0 failed); judge_lib GRADLINES/FORMD_CITE helpers; two judges on lists A/B.
- PROFILE built: thesis homepage H1, history 74 words, 15 funds, AUM $9.84B (ADV), HQ Boston (ADV principal), individuals 35
  (Operating Team unmapped), icon source android-chrome-512x512.png (dry run clean, 0.45x, contrast 4.3:1; upload at ingest).
- Cross-rulings written (companies/cross-rulings.json): 23 distinct, 29 accepted; rule 10 now 0 disagree.
- Graduation list A done (judgments-grad-A.py): 5 graduated, 12 not_graduated (2 Form D absence, 5 cited end, 6 dated search incl. one
  firm-post end), graniteshares entry 2016. Follow-ups (judgments-grad-fix.py): evertrue -> Series A (TechCrunch 2013-03-21);
  digital-currency-group -> graduated on the 2021 $700M secondary at $10B, medium, OPEN for Erik (secondary sale as graduation; rule 7).
