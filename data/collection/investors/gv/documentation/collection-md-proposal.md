# Proposed COLLECTION.md write-backs from the GV run (PRO-75)

Not applied: `COLLECTION.md` and `scripts/` belong to the tooling session during a wave (§12). Each item says
where it goes, the rule, and the evidence from this run. Item 1 answers the question PRO-75 was opened to ask.

## 1. §11: the profile of a manager that files no Form ADV (a corporate venture arm)

**Where:** §11, a new paragraph after "Profile without a site", and one line in §1 T1.

**Rule proposed.** A corporate venture arm invests its parent's balance sheet through vehicles with one limited
partner, so it has no adviser registration, no Section 7.B, no Item 5.F and no fund offering. Recognise it at
kickoff by three checks: IAPD returns nothing under the brand, the legal names on EDGAR and the parent's name; the
vehicles file ownership forms (13D/G, Forms 3/4) but no Form D (at most a general-partner or carry vehicle files
one); and the management company files 13F notices whose holdings sit inside the parent's 13F. Then:

- `aum` publishes `{bottom: null, top: null}` with the flag `no_sworn_source`. The firm's own stated figure goes
  into the sidecar basis with its page and date, never into the value, because every other profile's range is
  anchored on a sworn number and a firm's marketing figure is not comparable to it.
  *Alternative for Erik (delta 1 in decisions.md):* publish the firm's own figure as both ends, flagged
  `firm_stated`. It is what the firm says and a reader expects a number; the cost is a column that mixes sworn and
  unsworn figures with nothing on the page to tell them apart.
- `hq_location`: `config.json profile.adv_crd: null`, and the firm's own site decides through
  `profile.site_office`. The vehicles' filing address is the parent's headquarters (GV: 1600 Amphitheatre
  Parkway, Mountain View), not the firm's office, and must not decide.
- `funds`: the vehicles by name and vintage from EDGAR, `size: null`, sourced to each vehicle's EDGAR page; press
  allocations ("$125 million for Europe", 2014) go in the basis.
- `investment_range`: unaffected; the entry-round distribution is read from the portfolio's own rounds.
- **Boundary (T1).** The parent's other investing units are separate firms under T1 when they carry their own
  vehicles and team (CapitalG with its CapitalG 20xx L.P. family; Gradient with its own funds), and the parent's
  strategic balance-sheet stakes are not the arm's positions (T2). The parent and its holding companies co-file
  the arm's 13D/G and must be `external` in the entity registry, or the crawl imports every position the parent
  holds.
- **The parent's own companies on the arm's list** (GV: Waymo, Isomorphic Labs) are members as minority
  financings: the control addendum excludes a transaction in which the firm acquires control, and the arm acquired
  none (decisions.md D4). Worth a line under T3's control addendum so the next corporate arm does not re-derive it.

**Evidence.** IAPD: no firm under GV, GV Management, Google Ventures, Google or Alphabet (2026-09-29). GV
Management Company, L.L.C. (CIK 1940173) files 13F-NT and N-PX only. Vehicles Google Ventures 2011, L.P. and GV
2013 to GV 2023, L.P. file 13D/G and Forms 3/4; the only Form D is GV 2025 GP, L.P. (84 investors, $0 sold).
`build-firm-profile.py` refuses a literal `null` for `aum` (it reads a missing field), so the null range is
written as an object; a tooling line saying so would save the next run a failed build. And `firm-offices.py` words the HQ basis for a manager with no ADV as "The firm's own site disagrees with the Form ADV principal office, None."; with `adv_crd: null` it should say that no ADV exists and the site decides.

## 2. §5: archived Nuxt payloads are listings

**Where:** §5 layer 1, beside the Nuxt 2 full-static paragraph.

**Rule proposed.** A server-rendered Nuxt 2 page carries its CMS rows in `window.__NUXT__`, a minified function
whose result is a cyclic object graph (a company links its partners, a partner links her companies); it cannot be
JSON-serialised, so evaluate it in node and walk it with a visited set, emitting only the entries of the content
type that is the listing. Nuxt 3 pages carry `__NUXT_DATA__`, a flat devalue array whose objects hold indices; a
twenty-line reviver reads it. On gv.com the portfolio names appear nowhere in the rendered markup from September
2022 on: without the payload those years read as empty. `scratch/js/nuxt2-companies.js` and `parse_e` in
`scratch/cc-parse.py` are the generic versions; both belong in `wayback-pull.py` as era parsers.

## 3. §5 layer 2: a people page's own title dates the window, not the page's existence

**Where:** §5 layer 2 (partner roster).

**Rule proposed.** Read the title on every capture of a person's page, and count a year only when that year's
title is an investing title. Firms keep departed partners' pages up under a new title (GV: Kevin Rose "General
Partner" 2013-14, "Advisor to Google Ventures" from 2015 with "Previously, he was a general partner"; Rich Miner
General Partner to 2016, "GV Advisor" from 2017), so the page's capture span over-reports tenure by years. Platform
staff whose later pages carry a bare "Partner" are identified by their first title (marketing, portfolio programs,
data). And a listing era that keeps a departed partner attached to his companies (GV's 2022+ CMS) must not extend
his window.

## 4. §5 layer 3 and §3: read the Form D's other related persons before judging a name-match

**Where:** §3 "Name-match rows are judged cluster-first", and §5.3.

**Rule proposed.** A partner's Form D row whose issuer name matches nothing is often a listed company under its
legal name, and the co-filers say which: the founder as executive officer names the company. On GV four "unknown"
issuers were listed companies (Rosa Foods = Soylent via Robert Rhinehart, Denver Technologies = Warp via Zachary
Lloyd, NoHo Dental = Tend via Larson Hudson, Asset Blue Pharmacy Services = Waltz Health via Mark Thierer). And the
partner's own filed address is the firm's office where it is one: Ben Robbins filed Synapse Health's 2023 Form D
from 1600 Amphitheatre Parkway, and Asset Blue's from Google's Cambridge building, 355 Main Street. This is the
Sutter Hill address finding (its proposal 1) from a second firm; `formd-query.py` should keep every related person
and address on a matched filing.

## 5. §1 T5: an investment company on the firm's own list

**Where:** §1, "Fund-shaped list entries".

**Rule proposed.** The fund-shaped rule keys on a name; the firm's own description can decide it where the name
does not. GV lists Oxford Science Enterprises, whose name is not fund-shaped; the firm's own 2015 listing called
it "a fund that provides capital and business expertise to companies developed in Oxford University". Read the
firm's own words for every entry that is an investment company, holding company or university IP vehicle.

## 6. §12: a machine-wide bucket needs a per-session cap on clients

**Where:** §12, "One budget per external service".

**Rule proposed.** `shared_throttle.py` keeps each service's total rate right but gives every waiting process an
equal chance at each slot, so a session's share of a service is its number of waiting clients. GV ran 17 parallel
judges plus a news sweep against Google News (1 request/s machine-wide) and took about 15 of every 16 slots; the
Tiger Global session's queries fell to under 25 in 20 minutes and it asked, correctly, for a cap. A session that fans
out to parallel agents caps its own clients per service (GV: two local slot locks taken before the shared bucket,
`scratch/gvslot.py`); better still, `shared_throttle.wait()` could take a per-session key and serve sessions round
robin, which would make the cap unnecessary.

## 7. §8: the rebuild's re-key must refuse a fingerprint that is not unique on both sides

**Where:** §8, "A rebuild that renames a row carries the row's answers with it", and `scripts/rekey_overlays.py`.

**Rule proposed.** `rename_map` keeps a fingerprint only when one ARRIVED row holds it, but never checks the
DEPARTED side. On GV that moved two answers onto the wrong rows in the one rebuild: Curie.Bio's `not_member`
verdict (the row left as excluded) landed on the newly split Spruce Health because both carried the same
`site_url`, which on gv.com is the listing page itself (`https://www.gv.com/portfolio`, shared by all 648 live
rows); and Place's member verdict landed on Oxford Sciences Innovation because both were first seen on the same
Common Crawl capture of the listing page. Had it gone unread, the next rebuild would have excluded Spruce Health and
resurrected Curie.Bio unjudged. Fix: a fingerprint identifies only when it is unique among the departed rows AND
among the arrived rows; and a `site_url` or `wayback_first_link` that points at a listing index (shared by more
than one row of the old base) is not an identity key at all. Until then, the run reads the rename list after every
rebuild (the memory note of 2026-09-28 says so) and moves wrong keys back by hand, as this run did.

## 8. §5 / §8: a curated same-name split must also be a never-merge pair

**Where:** §5, the curated renames in a parsed source, and §8, identity duplicates.

**Rule proposed.** A split made in the parsed source by giving the second company its domain in brackets
("Bowery (bowery.io)", "Basis (basis.io)") is folded straight back by the builder's name-variant rule, which reads
"Bowery (bowery.io)" as a rendering of "Bowery" whenever no single capture lists both. Every bracketed split
therefore needs its `never_merge` pair in `identity-merges.json` in the same edit; GV found both of its splits
re-merged only after the first rebuild. A one-line check in `verify` would catch it: a parsed-source name of the
form "X (domain)" whose slug is absent from the base.

## 9. §8: every slug of an automatic name-variant group needs its own verdict too

**Where:** §8, the paragraph ending "Every slug of a merge group needs its own verdict when the canonical's verdict
is `not_member`."

**Rule proposed.** The same holds for the builder's automatic name-variant merges, not only for `identity-merges.json`
groups. The build excludes by slug before it merges variants, so excluding the canonical resurfaces the variant
(Oxford Sciences Innovation after Oxford Science Enterprises), and a Form D-only pair filed under two issuer names
(Culture Amp Pty Ltd and Culture Amp Inc.; Qadium and Expanse; Vise Technologies and Vise) flips its rendering
between builds, so the verdict lands on whichever name the last build chose and the other name comes back
unjudged. GV needed two extra verdict passes and two extra rebuilds for it. Fix: when a row is ruled `not_member`,
`record` writes the same verdict under every slug the row's evidence carries (its variant names), or the build
excludes by the evidence keys rather than the slug.

## 10. §6 / §8: a disputed layer join must not leave its source and date behind

**Where:** §8, standing duty 3 (weak CIK joins) and duty 8 (the float quarantine).

**Rule proposed.** When the judge disputes a status or figure that a wrong-entity join supplied, the join's
`valuation_source` and `valuation_asof` still ride on the row and publish: GV's Mill read "wikidata, as of
1788-01-01", Courier "sec_public_float, 2014-03-29" (another registrant's float), and Lattice Data carried a
Lattice Inc. float date. Fifteen rows were cleared by hand (`scratch/judgments-fixes-3.py`). Fix: `record` clears
`valuation_source` and `valuation_asof` whenever a line disputes the layer's `status` or figure without giving its
own, and `verify` fails a row whose `valuation_source` names a layer the row's flags say was disputed.

## 11. §8: `record` appends a note; say so where the merge rule is stated

**Where:** §8, "`record` is the gate" ("answers merge per key into existing records; flags union; only
`clear_flags` removes").

**Rule proposed.** One key does not merge per key: `note`. `record` stores "old | new" unless the new text is
already inside the old, so a judge who passes the stored note plus a sentence doubles the note, and a lead who
passes a rewritten note keeps both versions. GV's delta brief told judges to do the former and 22 notes doubled
before a judge noticed (`scratch/repair-notes.py` repaired them). Say it in the paragraph: a line's `note` is the
new sentences only; a note is replaced only by editing the file under the record lock. The same test has a second
face (found by sweep judge s2): when a file is recorded twice, its note is already inside the stored one, so `record`
skips the append but has already overwritten the stored note with the line's, and a line that carried only a new
sentence wipes the row's description. A re-run should be a no-op for the note.

## 12. §6: the Form D band in code is flat; the playbook's structural rule is era-adjusted

**Where:** `scripts/run.py` `STAGE_BANDS` / `band_stage()`, against §6 "Structural rules" (entry_stage).

**Rule proposed.** §6 labels a first filed round by era-adjusted ceilings (seed / A: $1.5M / $12M up to 2010,
$2.5M / $15M 2011-14, $4M / $20M 2015-18, $6M / $30M 2019-21, $8M / $40M from 2022; Pre-Seed below a quarter of
the seed ceiling), but `band_stage()` uses one flat ladder for every year ($1M Pre-Seed, $7.5M Seed, $30M Series
A). An old round between the era's seed ceiling and $7.5M is therefore banded Seed and enters the S2A cohort:
GV's Corduro (a $3.3M first round in 2010, no prior filing) read Seed and not graduated; by the playbook it is a
Series A and outside the cohort (re-staged in `scratch/judgments-fixes-7.py`, found by judge d4). On GV only one
band-staged row changed, because the grind had replaced most bands with named rounds, but a book whose older
entries still rest on the band will carry the same error at every era. Fix: `band_stage(offering, year)` with the
§6 table, then re-run `prepare` on the landed books and read which Seed rows move.
