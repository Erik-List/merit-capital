# Headline run log (PRO-164)

Kickoff 2026-09-27 ~19:05 UTC (15:05 EDT local) on Erik's "please collect Headline" (prompt 1).
Usage at kickoff: 5-hour 5%, weekly all models 80%, weekly Fable 82% (resets 2026-09-29 17:59 UTC).
Siblings running at kickoff: Bain Capital Ventures, General Catalyst. Atomico's in-flight marker is still on disk (its run is ingested; not ours to touch).

## RESUME NOTES

- Re-read COLLECTION.md, then `python3 scripts/run.py status --investor headline`.
- Site layer: `python3 data/collection/investors/headline/scratch/build-site-layer.py` rebuilds sources/site/companies.json and team-cards.json from sources/site/sanity/*.json.
- ADV 7.B: `scratch/parse-adv-7b.py` (PDFs in data/filings/headline/adv/, gitignored).
- Own-vehicle Form D persons: `scratch/fund-formd-persons.py` -> sources/edgar/fund-formd-persons.json.
- entities.json: edgar-entities.py DROPS entities its company search cannot see (EDGAR returns a single company page, not a list, for a unique match; the seed step does not parse it). After any run of edgar-entities.py (incl. via `run.py collect`), re-run `scratch/add-entities.py` and then `python3 scripts/edgar-companies.py headline`.
- Common Crawl: `scratch/cc-index.py <domain>` -> sources/wayback/cc-index-<domain>.json.

## DEFECTS FOUND (for write-back / tooling session)

1. edgar-entities.py: a seed query with exactly one EDGAR match returns the company page, which `seed_from_company_search` does not parse, and entries added by hand are dropped on the next run (only the desk of a prior entry is preserved). Headline lost Headline US VII, Global Growth IV, Lion SPV, Wombat SPV, BV Capital Fund II / II-A / IV (Asia), the KG No. 1 and BV Capital Management.

2. run.py record, note merge (cmd_record ~l.1705): a new note is joined as "old | new" unless it is already inside the old one, and then it REPLACES the stored note with itself, so re-recording a line whose note is a fragment of the stored note truncates the note silently. Judge helpers that pre-join the old note (ours did) duplicate every earlier note instead. Fix proposed: keep the old note when the new one is inside it. Headline's 74 duplicated notes were de-duplicated directly (note key only; backup scratch/classification.before-note-dedupe.json).

## STATE

- 15:05 kickoff; COLLECTION.md read in full; PRO-164 In Progress.
- Sanity dataset dumped (293 companies, 83 team, 60 posts, 5 fund pages).
- IAPD: six Headline ERAs + BV Capital Management (inactive). 7.B parsed (29 funds incl. two unrelated Infinity advisers, excluded).
- IA machine-wide cooldown 15:19-16:19 local; scratch/cdx-enum.py waiting on it (bvcapital.com, eventures.vc, eventures.com, headline.vc).
- Common Crawl: bvcapital.com has /portfolio/show/<slug> 2008-2010 and /team/show/<person>.
- 15:20-16:30 EDT: pass 1 of the grind recorded for all six batches (judgments-1..6.py): membership, status, country, city, band where below_1b, and stage where the firm's own posts, filings or press name the round. Left open on purpose: stage for rows with no named round (stage pass), S2A (graduation pass, needs graduation-surfaces), marks for $1B+ candidates (valuation pass), a few cities.
- Context was compacted once mid-run (~16:05); COLLECTION.md s1-s3 and s6 re-read before batch 5.
- Disk: the Mac hit 100% (144 MB free) at ~16:00; back to 6.9 GB free by 16:05 (freed outside this session).
- Hidden CMS docs: the seed step counted them as site listings; each was re-judged on corroboration (thrive-market, flutterwave, friendsurance member; wawa not_member). roadrunner still open.
- Merges added (identity-merges.json): codefied->housecall-pro, brainfights->codesignal, ixtens->merchantry-inc, rizio->voicea, superintelligence->recursive (+ hound, nomnomnow, blossom, angi, gotomeeting, homa-games, saymine earlier). Desk move: vital-signals (Asia).
- names.published still to write: baron-app-inc Cameo, pragli-inc Gentrace, clyde-technologies-inc Clyde, daily-secret-inc Daily Secret, fanhattan-inc Fanhattan, merchantry-inc Merchantry, munchery-inc Munchery, reelio-inc Reelio, viavia-corp ViaVia, zumper-inc Zumper, gr-ns Grüns, trawa (check), etc.
- Cross-investor items: Clyde (Spark says Spark led and sale 2024; press: Headline led, assets to Cover Genius 2023-03), Fanhattan (Redpoint dates the Rovi sale 2016; it closed 2014-11).
- 16:10-16:45 EDT: stage pass launched as five research agents (packets scratch/research/packet-1..5.json -> stage-1..5.json; Google News + WebFetch only, no WebSearch); CMS 'Growth' label scored 3/3 and applied (stage-001); valuation pass (valuation-001: marks cited, public caps from StockAnalysis 2026-09-25); focus pass (focus-001); verify --in-flight follow-ups (fix-001/002); distinct same-name pairs added to data/collection/cross-investor.json; names.published and verify traps written to config.json.
- Archives: IA machine-wide cooldown until ~18:20 EDT; Common Crawl index refused connections (curl rc=7) for eventures.vc / eventures.com / headline.vc, job stopped at 16:42. The e.ventures/Headline site eras are STILL TO PULL (Wayback, after the cooldown).
- Cross-investor alignment to apply in sibling books at close (ingest gated): Redpoint sonos -> public/1b_plus $2.15B; Battery fundamental -> 1b_plus $1.2B; Redpoint owner citation dead (band same); YC flutterwave citation dead (band same); Spark clyde (lead + sale date); Redpoint fanhattan (sale 2014 not 2016). Sorare (Accel below_1b vs Atomico/IVP/Headline 1b_plus): for Erik.
- 17:05 EDT: group 2 (BV era) recorded as stage-002 (5 cited entries: Shopping.com via Epinions Series C, Cranite C, Pronto B, myfab A (model), Fotolog A (model); Sonos A (model, cite_pending); rest undetermined with rounds persisted). Alignment list += Khosla k2-network ('acquired' vs a 2012 merger into its own subsidiary). Group 2's agent fetched web.archive.org directly during the IA cooldown (so did verify-urls.py once); both stopped: agents told, verify-urls SKIPs the archive.
- 18:00 EDT: stage pass complete (stage-002..006); graduation pass on the open seeds (grad-001; graduation-surfaces.py got a FIRM_TERMS entry for headline); momentum slice running (scratch/momentum.py, 24 rows). ADV 7.B: Headline US VI's GAV was mis-parsed as Growth III's value (page-spanning); corrected to $417,397,831 in sources/registers/adv-7b-funds.json. In-boundary 7.B now ~$4.02B.
- 18:20-18:45 EDT: IA cleared at 18:20; eventures.vc CDX enumerated (1,758 URLs) and then the next CDX call hit the firewall again: machine-wide cooldown now ~7.5 h (to ~02:20). Common Crawl's index host still refuses (rc=7); data.commoncrawl.org answers. So: eventures.vc read through the firm's own upload filenames (sources/wayback/eventures-uploads.json, 166 non-people logos, 46 known, 119 researched by four agents -> scratch/research/recall-*.json). NOT pulled, debt for the report: headline.com / headline.vc eras, bvcapital.com 2000-2007 (IA), per-year snapshot parses of eventures.vc.
- Recall press sweep (scratch/recall-press.json): nine confirmed additions (scratch/recall-candidates.json): Soldsie, All Def Digital, Candid, Test.ai, Flowhub, Zeller, Ahara, The Young Turks, Exporo; plus Deposit Solutions (R2).
- 19:25-20:00 EDT: rebuild 1 (89 recall additions injected; the name-variant pass merged Verse into Verse Medical) -> never_merge + rebuild 2 (268 rows, all judged); prepare delta (71 rows) -> delta-001, grad-002, fix-005. Alignment list += Accel bettercloud (acquired, CoreStack 2026-03), GC coya (acquired, Luko 2022), 8VC plated (acquired first; its own note argues it), Sequoia bird (insolvency + asset sale reads acquired). Distinct pairs added for candid, thread, trellis x2, verse x2, flux x2, mira, bird x2.
- 19:30-20:10 EDT: A/B pass recorded (ab-001: Creditas BR, Sonim stage source, notes; no band moved); 21 distinct rulings moved from the shared cross-investor.json to companies/cross-rulings.json (shared file restored to HEAD, s12) + 8 accepted (sibling side stale); city-001 (5 rows); duties-001 (Pronto/Flux/Pulse is_public from wrong joins cleared), duties-002 (unicorn flags cleared); 59 double periods in notes fixed. Profile: investor.json + sources.json, firm-offices (San Francisco, ADV principal), build-firm-profile (83 people, focus via fixed crosswalk casing), icon dry run clean. Plain verify CLEAN; export 268 rows; review.html checked on 8931. report.md drafted; blind 5% (14 rows) running in a subagent -> scratch/blind-rejudge.json.
