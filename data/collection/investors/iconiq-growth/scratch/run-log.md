# ICONIQ Growth run log (PRO-168). Resume point after a context reset.

Re-read data/collection/COLLECTION.md, then `python3 scripts/run.py status --investor iconiq-growth`,
then this file. Command forms: `run.py collect iconiq-growth` and `prepare iconiq-growth` are POSITIONAL;
`record/status/verify/export/review/close` take `--investor iconiq-growth`.

Kickoff 2026-09-29 00:32 UTC on Erik's "please collect ICONIQ" (prompt 1). Usage at kickoff:
weekly all models 23%, Fable 6%, 5-hour 2%.

## Siblings in flight at kickoff
- Tiger Global (PRO-167, slug tiger-global-management): EDGAR chain, 13F, FTS, Wikipedia, Google News; also on Common Crawl.
  It killed my parse-adv.py once by a broad pkill (00:47 UTC), apologised; re-run fine.
- Founders Fund in flight (marker 2026-09-27). Atomico, BCV, GC markers are stale leftovers (their runs are ingested). Do not touch.

## Done (2026-09-29, UTC)
- Phase 0: documentation/decisions.md (D1-D12, X1-X6); Linear PRO-168 kickoff comment posted, issue In Progress.
- config.json v1 (desks growth / platform / umbrella / external; thirteenf_ciks 1569709; fts phrases; wikipedia phrases).
- ADV: data/filings/adv/159198.pdf (1,732 pages); text cache in the scratchpad (adv-159198-pages.jsonl);
  scratch/parse-adv.py -> sources/registers/adv-159198.json (351 funds, GP + adviser per fund; growth desk 81 funds $32.17B).
- IAPD: sources/registers/iapd-search.json (CRD 159198 + IPI Partners 284694).
- Own fund Form Ds: scratch/formd-own-issuers.py -> sources/edgar/formd-own-issuers.json (442 filings).
- Site: scratch/pull-site-iconiq.py -> sources/site/portfolio-2026.json (172), posts.json (143: 135 insights, 8 news);
  scripts/site-portfolio.py iconiq-growth -> sources/site/companies.json (172).
- 13F: scripts/edgar-13f.py iconiq-growth -> sources/edgar/13f-holdings.json (54 filings, 574 issuers).
- Common Crawl: scratch/cc-cluster.py -> scratch/cc-index-raw.json (42 crawls, 1,851 captures);
  scratch/cc-fetch.py (one capture per URL per year) -> scratch/cc-raw/ (623 to read; running at kickoff+30m).

## Done since (2026-09-29, to 02:15 UTC)
- cc-fetch + parse-cc-iconiq.py -> sources/wayback/parsed/<year>.json (2020:75 .. 2026:156); roster curated (17 people);
  coinvest-decode.json (14 confirmed); collect + build (199 rows) + prepare; queue backup scratch/queue-v0.json.
- Judged: batch-001..005, fixes-1, caps-1, valuation-1 (all recorded). Ledger 199 (172 member, 27 not_member awaiting rebuild).
- valuation-1: signed sales kept private at the agreed price (Airtable $2.25B, Miro $1.79B, Altruist $4.6B, Fin/Intercom $3.6B);
  Oura $11B (IPO terms set, not listed); HeadSpin and Highspot acquired; Smartling private (Vitruvian majority recap);
  GoFundMe OUT as control_position (June 2015 control deal, flag for Erik); GoodRx kept member, T3 timing open for Erik;
  rule-6 country citations; Wikidata claims confirmed (hcs wikidata); alibaba/groww band fix (fixes-1 status-only line bug).
- emit.py: `cf` clears work flags, `hcc` country citation, explicit vr=None keeps the band, stale auto on marks < 2024-09,
  city_unknown only where no city is on disk.
- WebSearch used: about 45 of 200.

## CLOSED 2026-09-29 ~14:15 UTC (resumed at 14:00 after the usage-limit pause)
- IA CDX read once after the cooldown: earliest growth portfolio page iconiqcapital.com/growth 2020-09-25 (73 logos),
  all in the base or excluded; no Wayback pull needed.
- Second rebuild: 169 rows, 30 excluded (24 not_member, 6 control_position), no rename; prepare re-run; verify clean.
- names.published set (11); profile focus/geo/stage filled; builder passes; duty 7 blind 5%: 51/54 cells agree,
  Fastly -> DevTools & APIs, Side -> SaaS, Sanity kept; 3 rows `unstable`.
- report.md written; run.py close; pathspec commit; Linear comment; closing message with the ingest request.
- NOT INGESTED: waits on Erik. At ingest: upload the icon (fetch-investor-icon.ts with the webclip URL), ingest the
  investor row + 169 companies, and align the accepted sibling rows (report section 9, item 6) with read-back.

## STATE AT PAUSE (2026-09-29 ~02:50 UTC, usage limit reached; prompt count still 1)
Done since the last entry:
- Web passes recorded: valuation-1, momentum-1 (17 rows), pass-b-1 (29), stage-1 (34). cite_pending left on 11:
  alibaba, anduril, bill-com, crowdstrike, goodrx, notion, openai, physical-intelligence, stripe, uber, zoom.
  Open T3 timing for Erik: goodrx, bill-com, crowdstrike, zoom (13F Class A from the listing quarter). Uber flagged boundary (X6).
- decisions.md R1-R6 written. cross-rulings.json written (13 distinct, 29 accepted). Recall probe done (FTS third-party,
  13F, Wikipedia, press-sweep.py, growth-page logo track = the 172 grid rows): nothing new. Wayback NOT pulled (CC covers
  2020-2026; iconiqcapital.com was a splash page in 2013/2017; anchors 84 cos Jan 2021 / 120+ Sept 2022 match the captures).
- Profile: investor.json + sources.json written; build-firm-profile.py passes (15 funds asserted, 15 people from
  sources/site/team-curated.json); offices.json = San Francisco, CA. Icon: webclip PNG, dry run passes; upload at ingest.
  STILL TO DO in profile: investment_scope.focus (sectors >= 12 members from the focus column; now SaaS, Fintech, AI,
  Healthcare, Consumer, Data Infrastructure), investment_geo (from hq_country), recheck investment_stage; rerun builder.
- Standing duties 3, 6, 8 done (weak joins, unicorn re-intersect, float collisions). Duty 7 blind 5%: an agent was
  re-judging captivateiq, sanity, miro, motorway, dialpad, fastly, side, docusign, dx (sample in scratchpad
  blind-sample.txt); it was stopped at the pause, so RE-RUN it (seed 168 sample) and compare cells; flag `unstable`.
- REBUILD 1 done 02:41 UTC (build4.log): 172 rows, 27 excluded (23 not_member, 4 control), merges nintex->skuid,
  intercom->fin, people-ai->backstory applied. Known builder issue hit: blackline-systems/truckstop-com verdicts were
  re-keyed onto the 2022 page variants 'blackline'/'truckstop'; restored on the site slugs (both slugs now carry
  control_position) and 'tme' came back (identity group skipped because tencent-music is excluded): tme judged
  not_member (rebuild-1). queue-v1.json = pre-rebuild queue; prepare-3 queued only tme.
- WebSearch used: about 142 of 200 (me ~48, agents 94).

## Pending (in order)
1. SECOND REBUILD (allowed: the delta produced not_member verdicts): `python3 scripts/build-company-base.py iconiq-growth`;
   expect 169 rows, blackline/truckstop/tme excluded; read the rename list; remove leftover classification keys of
   merged/renamed rows if verify complains.
2. Re-run the blind 5% duty; profile focus/geo; `python3 scripts/build-firm-profile.py iconiq-growth`.
3. Plain `python3 scripts/run.py verify --investor iconiq-growth` (Tiger Global's 8 None/None rows: its session has no
   in-flight marker; I messaged it); `export`, `review` (serve on 8931, check), report.md (usage kickoff 23% weekly /
   6% Fable; $1B+ share; open rulings: GoFundMe control minority, GoodRx/Bill.com/CrowdStrike/Zoom T3, Uber boundary,
   X6, unresolved co-invest codes KC/BD/ES/N/PR; Red Ventures below $1B by Rule A), `run.py close --investor iconiq-growth`,
   pathspec commit, Linear PRO-168 comment, memory, closing message with the ingest request. NO INGEST without Erik.

## Facts worth keeping
- Wikipedia: founded Dec 2011 (Makan, Anders, Boeding); ICONIQ Growth launched 2013, Will Griffith from TCV; Boeding left 2018;
  Blue Owl took 6% of ICONIQ in 2020. Flipkart Series D Aug 2012 names "ICONIQ Capital" (client era, D3).
- First-party round statements in posts: Snowflake Series D 2017 led; Datadog initial investment 2015; Adyen 2015 (first in Europe);
  Coupa "first invested" ~2015; Roy Luo boards (FloQast, Restaurant365, Enfusion, HighRadius, Primer, Truckstop, Conexiom).
- ICONIQ Strategic Partners, L.P. first sale 2013-06-07 ($393M + $102M -B); II 2014-10-27 ($551M + $449M); III 2016-08-01 ($570M + $547M).
