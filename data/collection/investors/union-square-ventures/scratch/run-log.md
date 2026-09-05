# PRO-86 run log (scratch, regenerable narrative)

2026-09-05, single session, merged shape (PRO-71), slot 1 of the two-session test wave (Spark Capital is slot 2).
Prompt count so far: 1 (kickoff "please collect USV; phase 0 confirmed").

## Kickoff facts pinned
- usv.com: one live list (/companies/, 216 rows, server-rendered; the firm's own entry-round label + year, exit detail,
  Sector/Status/Entry Point terms read off the filtered pages); no REST route for the company post type; 3,807 posts
  pulled via REST (the firm's announcement archive). Five archived listing eras 2005-2024 (unionsquareventures.com
  /portfolio.html; usv.com/investments; /portfolio attribute cards 2013-2015; /portfolio Airtable cards 2016-2019, no
  names -> resolved via the 2019 title map + a domain hand map; /companies/ 2019+), parsed by hand from replay captures
  during the IA partial outage (CDX rc=7 all day) and merged with wayback-pull's partial years; Common Crawl: 41 people
  slugs, no company namespace.
- ADV: the firm is an ERA (802-75126, CRD 162375), 817 Broadway; 26 Section 7.B funds, GAV $3.235B (scratch/adv-7b-funds.json).
- EDGAR: 42 own entities (core 2004-2026, Opportunity 2010-2026, Climate, Bundled, Investors vehicles, GPs, Principals 2004);
  8 ownership-filing companies (Coinbase, Duolingo, Etsy, MongoDB, Tucows, Twilio, Twitter, Zynga); roster Form D sweep
  417 accessions / 205 issuers; fund Form Ds 25 filings (2022+ vintages file the target as offering with $0 sold).
- Roster: CURATED 33 names (31 investing) from the live people page, WP author tenure (first/last post) and the
  hiring/farewell posts; namesake filers external; four partners have personal CIKs (Section 16 as directors).

## Build 1 (20:3x) + prepare (20:41)
270 rows: 184 A / 39 B / 47 C; 216 site-listed; 53 pooled fund issuers dropped; 22 ex-partner-only rows removed
(Parker/O'Donnell/Friedman/Watson later seats); 21 name-variant + 16 identity merges. prepare: 223 site_listing seeds,
47 for the judge; layer A 12 public floats (two collisions to dispute: ghost, tapestry), unicorn pre-fills incl. two
collisions (bolt = Bolt.Earth vs Estonian Bolt; odyssey = the energy platform vs the AI company); 261 queued in 6 batches.

## Gate (scratch/gate-blind-pass.json) — PASS
Membership 0 false members (12 blind not_member recorded: six LP fund stakes, Tucows + Marley Spoon public purchases,
GroupMe, three Lightspeed-era Mignano seats). Stage layers: live label 51/52 -> class 1; archived labels 87/89; Form D
band 8/25 -> ceiling. Zemanta: the label's one error (press: $650K seed, Sep 2008).
Merges added from the pack: splice <- distributed-creation-inc (Splice's legal name), bolt <- revos, plus wattpad,
nova-labs, leap, shopshops legal names; sift canonical flipped to the build's rendering.

## Recall candidates queued for the probe
Uniswap (USV in the $11M Series A, Aug 2020 — Uniswap's own blog + press; never on the site), Libra/Diem (the firm's
own 2019-06-18 posts: USV joined the Libra Association; a16z/Thrive precedent -> member, defunct). Noise read once:
Host Hotels S-4 chain ("Union Square" hotel), SPAC/director-bio mentions (Eucrates, Tribe, Trajectory, KRAK, DeepGreenX,
TeraWulf, W Technologies), Comscore/ITXC/CarMax bios, Reg A sports-team issuers, Form C crowdfunding pitches, Rally (no
USV link found).

## A/B pass (21:0x–21:5x)
~46 web checks + 14 fetches (companiesmarketcap/stockanalysis/ECB, usv.com media). Public floats pinned at the 2026-09-04
close (Cloudflare $99.31B, Coinbase $48.71B, Twilio $35.77B, MongoDB $29.65B, Duolingo $7.19B, Etsy $7.02B, LendingClub
$2.21B, Funding Circle £669.67M -> $906M at ECB 1.1622/0.85898, Teamshares $454M). Unicorn slice: Abridge $5.3B (2026-04),
Suno $5.4B (2026-06), Generalist $3B reported (2026-08-25, medium), Upgrade $6.28B, Sift $1B, Shippo $1B, Quizlet $1B, Dune
$1B, Outschool $3B, Nova Labs $1.2B, Carta $7.4B (+$3.5B secondaries in the note), Dapper $7.6B, Polygon $2B (company
statement, R9), Uniswap $1.66B. Status moves: Farcaster and Stash -> acquired (R8), Veniam acquirer Nexar, Odyssey unicorn
mark disputed (collision). Momentum rows (addi, alife, anon, consensus, hume-ai, karat, mundi, slope, doctronic,
general-intelligence, tutor-intelligence, zanskar, viam, c2fo, clarifai, payjoy, top-hat, protocol-labs, matter-labs): all
below_1b with the check cited. Recall probe: Uniswap, Diem, Brilliant.org, Chamber, Glif, Tasklet, Alqem.

LESSON: `record` prints "REJECTED — n problem(s), nothing recorded" above its bullet list; `tail -2` hid the header twice
(align-002, align-003) and the rows read as recorded until verify showed range None / focus None. Read the whole output.

## Rebuild (21:2x) + corrective rebuild (21:3x) + delta
Build 2: 219 rows (43 not_member -> excluded.csv; 6 of 7 recall additions landed — Brilliant merged into Brilliant Planet by
the name-variant prefix rule). Renamed Brilliant.org, build 3: 220 rows, tiers A 177 / B 35 / C 8; prepare: 213/220
deterministic, 7 queued (batch-001, delta). Judged: all 7 members (Uniswap 1b_plus $1.66B aligned with a16z; Diem defunct;
Glif/Alqem/Chamber/Tasklet/Brilliant.org below_1b). fix-005 (mongodb/twilio graduation nulled after align-002 landed),
fix-006 (16 judge notes restored — the scratch fix script's note had replaced them; buglabs graduated on its 2010 Form D
$4M round). Standing duties: $1B+ all web_verified; graduation-false rows vetted (13 stand, buglabs flipped); weak CIK
joins 0 (cik_weak flag on 7 rows from the layer); unicorn loose re-intersection: bolt/odyssey/polygon/kik/stash/twitter/
zynga explained (collisions, acquired, token); blind sample 11 rows x 58 fields: 3 disagreements (props status/focus, supper
graduation None vs False).

## Verify, export, review, profile (21:4x–22:0x)
verify --in-flight clean; plain verify (links) clean at 21:52. Cross-investor: 4 gaps -> 3 accepted (a16z human-dx, pascal,
kiosk), justworks aligned with Thrive; after Spark closed (77 shared): buglabs and justworks accepted pairs (R11). Export
220 rows; review.html rendered on the review-surface server (port 54160, 8931 busy). Profile: investor.json + sources
authored (ERA: ADV 7.B $3,235,446,464 as AUM; 26 vehicles, 2004 fund from the site; range $750K / $5M / $50M), built by
build-firm-profile.py (hq 25/25 filings, 13 people, focus recomputed from site tags). Icon: --discover found only sub-100px
favicons; the WP media library holds cropped-usv_logo.jpg 512x512 (white USV on green) — dry-run refused at 2.70:1
contrast (3:1 floor); raised in report.md §7.

## Close (22:1x)
Standing audits: cik_weak 7 (3 fit, 4 disputed collisions), unicorn_name_match 9 (all verified). report.md written with computed
counts; Linear milestone + closing comments on PRO-86; scratch/collection-writeback.md handed to the tooling session;
run.py close (in-flight marker removed); commit with the investor pathspec. Ingest gated on Erik's approval. Prompt count 1.
