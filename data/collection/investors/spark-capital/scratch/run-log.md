# PRO-85 run log (scratch, regenerable narrative)

2026-09-05, single session, merged shape (PRO-71), slot 2 of the two-session test wave (USV in slot 1,
its directory appeared ~15:45 during setup). Prompt count so far: 1 (kickoff "please collect Spark
capital; phase 0 is confirmed"). Usage line: Erik reads Settings > Usage; kickoff percentages not yet given.

## Kickoff facts pinned (15:30-16:30)
- Live site (Webflow): /companies renders 124 cards in six tabs = 45 distinct companies (10 exit markers,
  45 website links); /team = 23 people in four tabs (Early 7, Growth 8, Operations 5, Emeritus 3). No CMS API
  (ladder step 5): parsed from the server-rendered HTML into sources/site/webflow-companies.json, team-webflow.json.
- Archived site eras (Wayback CDX, 1,715 text/html urlkeys 2000-2026): 2006-07 static html/php (per-company
  /portfolio/<x>.html|php, image-only listing), 2007-08 PHP homepage listing, 2008-12 to 2012-03 ExpressionEngine
  (/company/<slug>, listing = logo slider noscript block with names), 2012-04 to 2015-10 WordPress (/portfolio/<slug>/,
  ?st= sector filters), 2015-11 to 2017-09 WordPress redesign (/companies/<slug>/, paginated, cards carry
  sector + geo + seed/venture/growth classes), 2017-10 to 2019 WordPress "menu-new-menu" theme (/companies/
  grouped by sector, website links, no per-company pages; /about/<slug>/ story pages), 2019-09 to 2020-08 B12
  interim site (data-title cards, tag-sector/tag-stage classes incl. "alumni"), 2020-09+ Webflow (h3 cards,
  acquisition-spec exit markers; 123 cards 2021, 151 in 2022, 163-164 in 2023-24, 159 in 2025, 132 in 2026-01,
  45 distinct live in 2026-09). Domain captures 2000-2004 belong to a prior owner.
- IA replay was flaky all afternoon (HTTP 000 / rc 7 on ~half the ad-hoc fetches, rc 61 on one id_ capture):
  wayback-pull run three times (cached raws survive), 2009 listing swapped by hand to the 2009-06-04 capture
  (the January capture has no listing), 2006 and 2007 rows curated from the CDX index (parsed/2006.json, 2007.json).
- EDGAR/IAPD: ERA CRD 161231 (Spark Capital / Spark Capital Partners, LLC, CIK 2098748), HQ 200 Clarendon St
  Boston, offices NY (165 Mercer) and SF (600 Montgomery). ADV 2026-03-27 Section 7.B: 27 funds, GAV $15.57B
  (scratch/adv-7b-funds.json; pypdf text repeats blocks per page - dedupe by pfid). entities.json: 38 own vehicles
  (32 funds, 5 GP LLCs, the adviser), all desk us. edgar-companies: 9 public-market subjects (Braze, CNET, Flywire,
  Mandalay Digital, SmartRent, Sonder, Talkspace, Twitter, Wayfair). Form D sweep on 52 roster names: 440 accessions,
  246 issuers, 76 pooled; homonym clusters visible (Benjamin Simon property LLCs, Dennis Miller, Andrew Parker/Papa,
  Rob Go's NextView seats, Haber's a16z seat, Clayton's Meritech seats).
- Roster: partner-roster.py (CDX 2012+ dash slugs, 46-48 people) + scratch/roster-curate.py (2006-2011 early-era
  slugs, 13 people, 4 added: Dennis Miller 2006-2011, Robert Go 2008-2010, Scott Borenstein 2006-2008, Charles
  Huang 2010-2011). Operations staff not pruned (archived team pages unreachable through the flaky replay);
  the judge handles their homonym clusters cluster-first.
- Start@Spark (2009 seed program, $250K checks from the fund) verified on the firm's archived news page -> D4 IN.
- Common Crawl: 127 indexes, 124 company slugs, 44 people slugs (done 16:40).

## Gate (golden.json registered 16:25, before the build)
- Stage key: 44 rows web-verified (primary press / company posts / Wikipedia), incl. corrections to the issue's
  candidates: Plaid = Seed 2013 (Spark led the $2.8M seed; NEA led the 2014 A), Cruise = Series A 2015 (not 2014),
  Coinbase/Discord/Ramp/Scale/Marqeta/Kalshi/Glossier/Warby Parker = late Growth entries. Held back: Discord
  (round of first participation unclear), Scale AI (Series C 2019 per aggregators only).
- Membership traps: 31 keys (11 known-true incl. Bond Street as a founder-seat member and Talkspace under its legal
  name; 20 not_member: founder-era paper, next-firm seats, homonyms, Mandalay consideration, CNET pre-vintage showcase).

## Post-grind (2026-09-05 evening)
- Recall probe: Wikipedia insource (Dispo, Pray.com), EDGAR FTS (Teamshares 13G, Securitize S-1 selling
  stockholder), press sweep (Underdog, Cardless, Anrok, Antithesis, West Co, Kinnu, Roi) -> 11 recall additions
  registered; Nomad entry corrected (2022). Identity queue (11 merges + cover/cover-genius never_merge) folded in.
- Scheduled rebuild: 366 -> 328 rows (42 not_member retired, 11 additions + cover landed, 48 overlay merges);
  delta prepare -> 19 rows (batch-001) judged; three registrant twins (cnet-networks-inc, imperfect-foods-spc,
  papa-inc) resurfaced (2tor case) and were judged not_member.
- A/B pass: 13 public caps (companiesmarketcap / stockanalysis, 2026-09-04) + 53 private pins (Wikipedia, press,
  company posts; aggregators where nothing else exists) -> every $1B+ row carries a figure and citation; 22 stale.
  Band moves: 9fin up (Series C $1.3B, Mar 2026), Parallel up ($2B, Apr 2026), Sift down (secondary marks),
  Chronosphere/Niantic/Perch/Clyde/Cimulate/Producer -> acquired, Teamshares below_1b (cap $454M).
- Momentum slice: 40 rows (entries 2023+ in hot sectors) web-checked and recorded as web_verified bands with the
  announcement as citation; entry years corrected on 14 rows (first_seen != round year).
- Duties: weak-CIK audit clean (3 quarantined in the grind); stale-float sweep (1stDibs/SmartRent/Talkspace stay on
  the SEC float, below_1b); unicorn re-intersection: 8 name matches, all acquired/defunct/former or documented
  (Sift); 5% blind sample (16 rows, seed 85) consistent; city/country coherence: 9 fixes.
- Cross-investor: 98 agree, 3 accepted (InVision, Justworks, Catalyst), 0 disagree; 9 distinct rulings.
- Profile: investor.json + investor.sources.json (ADV 7.B GAV $15.57B, 15 funds incl. IX $1.0B and Growth VI
  $2.33B closed 2026, 23 team members from the Webflow pages, icon = the site's vector mark, dry-run only).
- Second, retire-only rebuild (328 -> 325) to move the three twins to excluded.csv; verify plain: clean; export;
  review rendered on the shared server (http://localhost:8931/spark-capital/review.html).
