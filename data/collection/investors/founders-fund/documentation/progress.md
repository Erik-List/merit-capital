# Founders Fund run progress (PRO-81)

Resume point for any session. Read COLLECTION.md, then this file, then
`python3 scripts/run.py status --investor founders-fund`.

## Who ran what

- 2026-09-27 to 2026-10-02: a Codex session. Provisional 170-row base, 72 verdicts, 54 classified rows (the live-site list, well cited).
- 2026-10-06 on: a Claude Code session (kickoff by Erik, prompt count 1). Usage at kickoff: weekly 1%, Fable 0%. At 20:00 EDT on 2026-10-06: weekly 18%, Fable 4%.

## State at 2026-10-06 20:00 EDT

- Base rebuilt twice on 2026-10-06 (build-2, build-3 logs in scratch/): **298 rows**. Ledger: **235 member, 63 not_member**, 0 unjudged. Classification holds 230 rows.
- Layers on disk: live site (64), archive index of /company/ pages (218 slugs, written by scratch/wb/parsed_from_inventory.py), 2006-2011 listing years (wayback-pull), roster of 35 (scratch/build-roster.py), Form D sweep (466 accessions), EDGAR full-text hits, Wikipedia sweep, ADV 7.B roster with gross asset values (sources/edgar/adv-7b-roster.json, total $58.93B), SPV Form Ds and fingerprint (sources/edgar/spv-*.json).
- Judgments are in scratch/judgments-*.py, each writing scratch/queue/<tag>.out.jsonl, all recorded: m1, m2 (membership), c1 to c6 (classification).
- Helpers in scratch/: jl.py (V, NM, C, R with need-awareness and sibling_val), view.py (compact queue view), sib.py (sibling books' values), cap.py (StockAnalysis market caps), cite.py and news.py (Google News headlines and URL decode), press_sweep.py (recall press layer, output scratch/recall-press.json), decode_press.py.

## Blocked services on 2026-10-06

- Internet Archive: machine-wide cooldown until about 21:35 EDT (firewall block, doubled twice). Still owed from it: page bodies of the /company/ slugs (scratch/wb/company_pages.py, resumable, writes sources/wayback/company-pages.json and names), thefoundersfund.com news releases 2005-2007, the /company/ era of wayback-pull. Names for 80 unread slugs are provisional (scratch/wb/slug_names.py).
- Google News: HTTP 503 after the press sweep (about 19:40 EDT). Needed for decode_press.py (publisher URLs of the recall headlines) and scripts/graduation-surfaces.py.

## Next steps, in order

1. Recall additions into `membership-ledger.json` `recall_additions` (schema: name, slug, basis, citation, first_seen, on_site_now, sector, source). Candidates, all judged member unless noted:
   - Wikipedia sweep (cite the article): AI Foundation, AirGarage, BitPay, Bonfire Studios, Brave, Carbyne, Circles.Life, Citizen, Declara, Even Healthcare, Flo, Hermeus, HyperTrack, IfOnly, June, Magdrive, Nucleus Genomics, Physical Intelligence, Porch, Prime Intellect, Privateer Holdings (Tilray's parent, one row), Quince, Skillz, StarkWare, Tbh, Transatomic Power, Unbound, Upstart, Ultima Genomics, Urbit (Tlon), Run The World (EventMobi article), Hooked.
   - Exit-side SEC filings (fund_filing, URLs printed from sources/edgar/fts-hits.json): 3VR Security (Identiv S-3 2018), Hims & Hers (S-1 2021, Fund VI), Pulley (Prolific Labs TA-1, Fund VII; also PR Newswire 2022-07-13), Notable Labs (Vascular Biogenics S-4/A 2023, FF Science V and VI), Strive (8-K 2025-09-12, Fund VII). CipherTrust is a namesake (Clarion Ventures' fund): rejected, trap in config.
   - Press sweep (scratch/recall-press.json; URLs still to decode): Primer, Ondo Finance, Huspy, Mudafy, Giraffe360, The Mirror, Maverick Protocol, Opal Camera, Campus, Lagrange Labs, Layup Parts, Avail, AfterHour, Sentient, Igloo (Pudgy Penguins), Caldera, Avantis, Anthropic (Bloomberg 2026-02-11, co-lead of the Series G; matches the ADV vehicle Founders ANT), Halter ($220M at $2B, 2026-03), Roadrunner, Endurance Energy, Stark Defence, Gamgee, Anvil (token purchase, 2026-10-06, token_funded). Also to cite: Erebor (bank), Bullish, Zenefits, Nerd Street Gamers, Sentient.
   - Set aside (OGE report only, see decisions.md): about ten names; not added.
2. One more rebuild (lands additions, removes 63 not_member rows, applies 21 identity merges in companies/identity-merges.json), then `run.py prepare founders-fund`, classify the delta with jl.R().
3. Seed-to-A second pass: `python3 scripts/graduation-surfaces.py founders-fund`, `prepare`, decide every Seed row (76 seed entries, 63 open). Royal is decided.
4. A/B pass on the visible slice (64 rows at $1B+): rows flagged `cite_pending` and `needs_web_value` (hampton-creek, material), momentum slice.
5. Cross-investor: write `companies/cross-rulings.json` (distinct: Cloud9/Balderton, Wave/Seedcamp, Glow/Index+Redpoint, Hubble/Accel+YC+Seedcamp, Cover/First Round+Spark+YC, Ramp/Balderton+Seedcamp, Cedar/a16z+YC, Hadrian/Cherry+HV, Branch/8VC+YC, Compass/NEA, Harbor/YC, Lore/YC, Radius/YC, Neon/Thrive, Ritual, Gowalla new company/GV+Spark, Eight Sleep check). Align stale siblings and re-ingest them (COLLECTION.md s9): Synthego (8VC, Menlo), Calibrate (Tiger), Enter (Coatue, Sequoia), Lighter (a16z), Instacanvas (First Round), Eight Sleep (YC), Gowalla (Greylock), Plethora (Lux: Form D filings of 2020-21 contradict a 2019 sale).
6. Firm profile (`build-firm-profile.py`): AUM both ends the 7.B composite $58.9B (exempt reporting adviser), HQ San Francisco with a Miami office, thesis from the homepage, team from sources/site/team.json, icon via `fetch-investor-icon.ts --discover`.
7. verify (plain), export, review (serve and check), report.md (SPV findings, recall gap, OGE item, usage line, prompt count), COLLECTION.md write-back proposal, `run.py close`, commit with pathspec `data/collection/investors/founders-fund`, ingest through the s9 gate.

## Findings to carry into report.md

- The firm publishes a list (PRO-81's prior was wrong): 64 live, 218 archived company pages, listings back to 2006. Its 2012-13 menu carries an "FF Angel" group (36 companies), a first-party seed-vehicle label (sources/wayback/site-menu-2013.json), used as corroboration, not yet scored.
- SPV fingerprinting: 17 deal vehicles on the ADV. One names its company outright (Founders Fund SpaceX Fund, 2009), ten carry an abbreviation (AND x6 = Anduril, OPEN x2 = OpenAI, SPC = SpaceX, ANT = Anthropic), six are opaque (Gopher E, Erebor, Mirian, Miruvor, Lembas II and its Series F). Only five filed a Form D. Date-and-size fingerprint against the Form D universe: SpaceX Fund 2009 -> SpaceX (right, by name), Lembas III 2010 -> SpaceX's $50M round (only known position that fits), Mirian 2023 -> Stripe's Series I (only one), Erebor 2019 -> Stripe's September 2019 round nearest of three, Miruvor 2019 -> three candidates (Stripe, Reddit, SpaceX), undecided. Every decoded vehicle points at a company already on the firm's list except Anthropic, which the press confirms. Verdict: corroboration for entry dating, never a membership instrument at this firm; zero rows rest on it.
- Namesake noise in the exit-side sweep: Kleiner Perkins' "KPCB ... Founders Fund" side funds (86 of 139 third-party registrants) and Clarion Ventures' "Founders Fund, LP" (CipherTrust).
- Four build-seeded "fund filing" members were Mithril's and Clarium's filings co-filed by Peter Thiel (Adagio, BlackSky, Fractyl, PEMCO): ruled out.
- Recall gap: about 65 members the firm's own lists never carried.
