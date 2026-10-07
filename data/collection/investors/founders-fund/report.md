# Founders Fund: collection report (PRO-81)

Run 2026-09-27 to 2026-10-07. Started by a Codex session (provisional base, 54 rows classified), taken over and finished by a Claude Code session on 2026-10-06 at Erik's kickoff. Prompt count for the finishing session: 3 (the kickoff, one "continue" after the app was quit mid-run, and Erik's two rulings).

## 1. Result

- **299 companies** after Erik's rulings of 2026-10-07 (293 at the first ingest), every one a ruled member; `verify` clean in full mode with only flagged debt.
- Status: 148 private, 73 acquired, 28 public, 24 unknown, 20 defunct.
- **75 at $1B or more** (51 at $1B+, 17 at $10B+, 7 at $100B+: SpaceX, Facebook, Anthropic, OpenAI, Palantir, Stripe, Spotify).
- Entry stage: Seed 80, Series A 78, Growth 71, Pre-Seed 2; 59 nameable rows undetermined, 3 rows unnameable.
- **Seed to Series A: of 80 seed entries, 3 were too recent to count; of the 77 that remain, 55.8% raised a later round (43).** Of the 34 that did not, 5 rest on the filings, 7 on a cited end and 22 on a dated search of the named surfaces. 51 decided rows rest on an uncited seed (flagged `stage_uncited`).
- Firm profile built: San Francisco, founded 2005, assets $58.9B (the sworn fund total), 13 funds, 29 people.

## 2. The scoping prior was wrong: the firm publishes a list

PRO-81 expected a firm that publishes little. It publishes 64 companies today and has listed its portfolio since 2006: thefoundersfund.com/portfolio.html (2006 to 2009), foundersfund.com/portfolio.php (2009 to 2011) and per-company pages from 2011 (218 distinct pages in the archive index). 215 of the 293 members were on one of those lists.

**The recall gap, as a number: 78 of 293 members (27%) were never on any list of the firm.** They came from the Wikipedia sweep (32), the press sweep for rounds the firm led (27), the exit-side SEC sweep (5), Form D director seats that resolved (14, six of them unannounced) and identity work. The live list is a showcase: it carries 64 of 293.

## 3. SPV fingerprinting: corroboration, not a membership instrument

The 2026 ADV lists 48 private funds, 17 of them deal vehicles.

| What the name gives | Vehicles | Decodes to |
| -- | -- | -- |
| The company, outright | Founders Fund SpaceX Fund (2009) | SpaceX |
| An abbreviation | Founders AND, AND2 to AND6; OPEN, OPEN II; SPC; ANT | Anduril, OpenAI, SpaceX, Anthropic |
| Nothing | Gopher E, Erebor, Mirian, Miruvor, Lembas II and its Series F | not decodable from the name |

- **Name parsing**: 11 of 17 vehicles decode. Ten point at companies already on the firm's own list. The eleventh, Founders ANT, points at Anthropic, which the press confirms (co-lead of the February 2026 round) and which is in the book on that press evidence. False positives against the list: 0 of 11, on a sample too small to promote.
- **Date and size fingerprint** (a vehicle's Form D against the Form D universe, 45 days): only 5 of the 17 vehicles ever filed. Two resolve to one known position (the 2009 SpaceX fund; Mirian 2023 to Stripe's Series I), Lembas III 2010 to SpaceX's $50M round, Erebor 2019 to Stripe as the nearest of three, Miruvor 2019 to three candidates and stays open.
- **Verdict**: at this firm the layer adds no member a list or the press does not already give, so no row rests on it. It is useful for dating follow-on money. Config shape if it is ever promoted: `edgar.deal_vehicles: [{name, cik, decodes_to, basis}]`, each entry scored against a documented round before it corroborates. Files: `sources/edgar/adv-7b-roster.json`, `spv-formd.json`, `spv-fingerprint.json`.

## 4. Method notes worth keeping

- **Namesakes in the exit-side sweep**: 86 of 139 third-party registrants naming "Founders Fund" are Kleiner Perkins' "KPCB ... Founders Fund" side funds; Clarion Ventures' "Founders Fund, LP" put CipherTrust in front of the judge (rejected, trap in config).
- **Thiel as co-filer**: four rows the build seeded as fund filings were Mithril's and Clarium's filings co-filed by Peter Thiel (Adagio, BlackSky, Fractyl, PEMCO). All out.
- **Name-match rows**: 75 judged by person. 19 members (five were legal names of listed companies: Careportal is Cedar, Indie Technologies is Found, Miami Labs is OpenStore, Orgio is The Org, Virtual Kitchen is All Day Kitchens), 56 out on seat dating.
- **"FF Angel"**: the 2012-13 site menu files 36 companies under the firm's angel vehicle. Checked against documented rounds it held on 14 of 15 (Cherry was a Series A entry), so it is used as corroboration only.
- **Archive**: the Internet Archive blocked this machine four times on 2026-10-06 (cooldown doubled to four hours). The base was built from the index and from captures already on disk; 64 of 218 company pages were read. Debt: the remaining page bodies, and the 2005-07 press releases on thefoundersfund.com.

## 5. Decided in the run (decisions.md)

- Deal vehicles and Growth funds are the same firm (D7, D8); partners' own vehicles are not (D9); FF Angel and FF Science positions are fund money (D10); PIPE and public-market positions are out: Opendoor, BitMine, ETHZilla (D11); acquirers are out, the company they bought is the row (D12).
- Out though listed by the firm: Friendster (Thiel's personal 2003 angel round), fbFund (a fund), Vittana (a non-profit).
- Homevest and SpotMap (Keith Rabois director in tenure, issuer never identified): out under the unresolved-issuer rule.

## 6. Other books aligned

13 stale rows in 11 books written from this run's evidence and re-exported: Calibrate (Tiger), Eight Sleep (YC), Enter (Coatue, Sequoia), Instacanvas and Readyforce (First Round), Lighter (a16z), Plethora (Lux), Porch (Battery), Readyforce and Synthego (Menlo), Synthego (8VC), Gowalla (Greylock). 34 namesake pairs ruled distinct in `companies/cross-rulings.json`.

## 7. Debt behind the flags

`stage_uncited` 65, `cite_pending` 20 (visible rows whose entry round still wants a citation), `city_unknown` 16, `country_prior` 16, `stale` 13, `needs_web_value` 2 (Eat Just, Flo Health: reported above $1B, not yet pinned), `identity_unresolved` 3 (Lava, Navia, Top Fans: page bodies unread), status `unknown` 24.

## 8. Rulings (Erik, 2026-10-07) and what is still open

- **Howery's financial disclosure is in.** Six companies added (AppCard, Five Apes, Indigo Technologies, Instapray, Neurotrack, theAudience); four acquirers it names stay out as sale consideration (Sabse, Freethink Media, NetBase, Higher Ground Education); 23 rows it names were already in the book and are now corroborated by a sworn fund-level list. The book went from 293 to **299 companies**.
- **Avalanche is below $1B** in this book and in a16z's (a token's market value is not a mark on the company). $1B+ rows: 74.
- Still open, one: **Brave.** A 2019 report said a Series A was planned; no close was announced. Read as not graduated; the other reading would move one row.

## 9. Proposed playbook write-backs

- §5: a firm's 13F-filing growth arm and a partner who co-files for another firm are two recurring sources of false fund filings; check the filer names against the entity registry before seeding a member.
- §5: the site menu of an old WordPress site can carry the whole list with the firm's own groups on every captured page; one page capture replaces a listing era.
- §5: SPV names at a code-naming firm (section 3 above): corroboration only.
- §9: sworn government disclosures (OGE Form 278e) carry a statutory use restriction; ask before using one.
- Tooling: `graduation-surfaces.py` fails without `investor/investor.json`, so the profile has to exist before the seed-to-A pass.

## 10. Ingest (2026-10-07, through the s9 gate)

- Closing commit 9f13091a, then icon, investor row, dry run (293 new, 0 removed, from 0 live), write, readback: **293 live, 0 differing cells**.
- The icon is the firm's four-band square mark, redrawn as a vector from the site's 152 px image (the site declares no vector of it); provenance in `investor/sources.json`.
- Eleven sibling books re-ingested after their alignment (Tiger, Coatue, Sequoia, First Round, a16z, Lux, Battery, Menlo, 8VC, Greylock, Y Combinator): each readback before the write showed exactly the aligned cells (1 to 3), each dry run 0 new and 0 removed, each readback after 0 differing cells. Y Combinator shows its known one-row name artefact (a leading space the readback tool does not trim).

- **Re-ingest of 2026-10-07 after Erik's rulings** (commits 4a734eae, 83a5f4d2): readback before showed the six new rows and Avalanche's cells, dry run 6 new and 0 removed, readback after **299 live, 0 differing cells**; a16z re-ingested for Avalanche, readback exact.

## 11. Usage

Finishing session: weekly 1% and Fable 0% at kickoff; weekly 22% and Fable 5% at close; 293 rows.
