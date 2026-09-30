# Visionaries Club run log (PRO-103)

Kickoff 2026-09-30 ~11:38 EDT (prompt 1: "please collect visionaries club").
Usage at kickoff (read 12:08): weekly all models 15%, weekly Fable 1%, 5-hour 11%.

## Done
- COLLECTION.md read in full; PRO-103 -> In Progress.
- Live site (Kirby) 59 rows -> sources/site/companies-2026.json (site-live.py); team 15 (site-team.py).
- tomorrow.vc 10 rows -> sources/site/companies-tomorrow-2026.json (site-tomorrow.py).
- IA: cooldown hit 11:43 (60 min, machine-wide). CC index 2019-2026 (72 crawls, 2023-06 failed) + tomorrow.vc; 149 + 28 bodies.
- WordPress /portfolio/ 2023-2025 parsed (archive-parse.py): 32/38/44 rows; gone: Tactic, Uify, Sustained, Loxo; Zigguratum=Ziggiz merge.
- EDGAR: 3 own Form Ds, 0 portfolio; FTS 3 own hits; ADV CRD 317147 7.B 11 funds $193.1M.
- North Data: fund KGs on shareholder lists (Seed I: Tacto, Superlist, Acapela, GetMomo; counts 14/21/12/8 for 2021-24; Growth I: Rows, Choco, Vay, Taxdoo, Xentral, arculus, Leapsome; Late Growth I: Xentral; Seed II: Tytan, ContextFab; Growth II: n8n; Tomorrow I: Proxima, Hades).
- Press sweep (sources/web/press-sweep.json); recall candidates: Tytan, ContextFab, Acapela, Causal Labs, Roboat, Conveo (Series A 2026-09, "participation from Visionaries").
- decisions.md D1-D7; config traps (8).
- Research agents x4 launched on 78 companies -> scratch/research/<slug>.json.
- ia-pass.py queued (Gatsby page-data, WP portfolio, team, sitemap, js).

## Next
- Gatsby era parse -> extras -> research group 5 (with Conveo).
- prepare, grind, recall, rebuild, verify, profile, report, ingest.

## Write-back candidates (collected during the run)
1. North Data's free fund-KG pages list "Mentions": portfolio GmbHs whose shareholder lists (Gesellschafterliste) name the fund, named individually up to ~3 per year and counted beyond. A forward enumeration for German funds that the s5 table calls "aggregator only"; filing-grade (fund on the register filing) -> fund_filing, as Balderton classed UK share registers. Counts per year are a recall check (Seed Fund I: 14/21/12/8 GmbHs 2021-24).
2. A firm's domain can have belonged to someone else before the firm (visionaries.vc = Japanese Toastmasters club until 2019): read the earliest captures' titles before parsing any era.
3. Gatsby sites can hard-code the portfolio in the page component bundle (page-data.json has no query data, staticQueryHashes empty); Common Crawl rarely holds JS, so only the IA can recover it: fetch the bundle first.
4. IA blocked this machine twice in one session (60 min at 11:43, 120 min at 12:43) after <10 requests each: order an IA pass by what no other source holds.
5. Stage by construction: a firm founded after a company's Series A closed can only have entered at Growth (every later round or secondary is Growth). Used on Miro (entry uncited) with cite_pending; propose as a standing rule (a lower bound from the fund's inception date, the opposite direction to the capture-date reading PRO-143 refused).
6. Rebrands: the press writes "Visionaries" (2026) and "Visionaries Club"; phrase sweeps need both, and "Visionaries" alone is too common for FTS/Wikipedia (namesakes everywhere).

## State at 13:30 (after the grind)
- prepare run (in-flight marker written); 72 base rows; 70 classified (uify awaits the rebuild merge into turian; personio not_member).
- Recorded: batch-g24, batch-g3, batch-g1, batch-g1b, batch-grad, batch-patch1/2/3, batch-momentum.
- Pending for the delta after the rebuild: queue/delta-g24.out.jsonl (tytan, contextfab, acapela) and queue/delta-recall.out.jsonl (conveo, fina, trana). Ledger recall_additions holds all six.
- Profile: investor.json + sources.json built (build-firm-profile.py ok), icon dry run ok (favicon-new.svg).
- decisions.md R1-R10 written. Linear milestone comment posted.
- Waiting: IA cooldown until ~14:45 (ia-pass.py restarted, JS bundle first -> ia-pass2.log); blind duty-7 agent on tendrils-compute, solve-intelligence, leapsome, pallery.
- At ingest: align Rows (accel, cherry: acquired) and Two (sequoia: private) if those books pass the gate; else accept the pairs in cross-rulings.json.
