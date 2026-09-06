# Lux Capital — collection report (PRO-95)

Run: one session, 2026-09-06, under the merged shape of `data/collection/COLLECTION.md`.
Archetype A (US venture, SEC nexus on both sides), sub-issue of PRO-87.

**Result: 271 published members, 79 excluded, `verify` green in plain mode.**
Firm profile built and through the taxonomy gate; `review.html` rendered and
checked in the browser. **Ingest is gated and has not run.**

**Usage line:** Erik reads Settings > Usage — kickoff percentages were not
given for this session; the line is filled at ingest (weekly %, Fable %,
base rows 271). Web searches used: 13. Prompt count: 2 at the time of
writing (kickoff, plus the mid-run request to collect Felicis, which was
routed to its own session rather than run here).

## 1. What the base looks like

| | |
|---|---|
| Published members | **271** |
| Excluded (`not_member`) | 79 |
| Identity merges applied | 34 duplicate slugs into 33 canonicals |
| Recall additions | 1 (DoNotPay) |
| Tiers | A 206 · B 63 · C 2 |
| Status | private 184 · acquired 52 · defunct 21 · public 13 · unknown 1 |
| Entry stage | Seed 136 · Series A 92 · Growth 42 · Pre-Seed 1 |
| Valuation | below_1b 240 · 1b_plus 25 · 10b_plus 5 · 100b_plus 1 |
| C2A cohort | 90 rows, 30 graduated, 33.3% |
| Focus (base-derived) | Healthcare & Bio 75 · Industrial & Robotics 64 · SaaS 34 · AI & Applied AI 24 · Data Infrastructure 15 |
| Geography | US 249 of 271 (92%) |
| First seen | 2005–2026 |

The shape is a deep-tech seed book: 84% of entries are Seed or Series A, the
median Form D entry round is $6.5M, and the winners are concentrated and
large — Anduril at $30.5B, Applied Intuition at $15B, Hugging Face at the
$12.93B NVIDIA agreement, Cognition at $10.2B, Databricks at $190B.

## 2. The method delta — five renderings of one book, and a firm that publishes no deal blog

Lux has been online since April 2000 and has changed site technology five
times. Each era renders the portfolio differently and the base is the union:

| Era | Surface | What it gave |
|---|---|---|
| 2000–2004 | static `.htm` | no portfolio listing existed — checked, not assumed |
| 2005–2008 | `/portfolio.php` | 11 companies with the firm's own sector, location and description |
| 2010–2011 | Flash | logo-only, deliberately unparsed; bracketed by the eras either side |
| 2012–2016 | `/portfolio` logo grid | 44 companies; the only stable slug is the `/importfolio/<slug>_logo.jpg` filename |
| 2016–2022 | WordPress `/companies/<slug>` | per-company pages |
| 2023–2026 | Webflow `/companies/<slug>` | 215 live companies with the firm's own investment year |
| 2019–2026 | `jobs.luxcapital.com` (Getro) | 190 live + 312 archived board slugs |

**The 2005–2008 era needed curating, and the site's own alt text lies.**
`LOGO_ACCELERGY.gif` carries `alt="Angstrom Publishing - Nanotechnology"` and
`LOGO_CIS.gif` (Crystal IS) carries `alt="Cambrios Technologies Corp."` — the
firm's own copy-paste errors. A parser that trusts the alt drops Accelergy and
Crystal IS from the era entirely. The row's own anchor text owns the name;
`scratch/php-era-curate.py` reads it that way and recovered 11 companies where
the alt-first pass found 6.

**The archive is the survivorship layer.** 246 archived `/companies` slugs
against 215 live ones: 50 companies are gone from the current site, including
Accelergy, AltspaceVR, Aria Insights, Arraiy, Blockstack, Common Networks,
CyPhy Works, Gridco Systems, Hometeam, Mousera, New Knowledge and Subspace.

**The firm's own announcement archive is the class-1 stage layer.** Lux
publishes no deal blog; it publishes a newsletter (*Securities*) and 194 `/news`
posts, 34 of which name a base company and a round. Those posts are the
citations behind the strongest `entry_stage` values in this run
(`scratch/news-pull.py` → `sources/site/news-archive.json`).

## 3. The calibration gate

Both sets were pre-registered in `golden.json` before any verdict wrote.

**Membership trap set — 21 rows, 14 of them asking for a membership verdict.
Result: 14/14 agreement with the key, zero false members at high confidence.
Gate passed.** The traps were real: the Welsh-Carson homonym (Sean M. Traynor,
whose firm page names K2M as his investment), Zavain Dar's post-Lux NewLimit
seat, Nat Turner's own Flatiron Health, Michelle Fang as Turo's own Chief Legal
Officer, and Intel Corp arriving on an "Andrew Wilson" name-match.

**Stage golden set — 26 rows, every answer anchored to a citation** (Lux's own
announcements and Wikipedia sentences naming the round and Lux's participation).
Two candidate layers were scored before the grind trusted either:

| Layer | Score | Verdict |
|---|---|---|
| Site `Lux investment: <year>` | 17 exact / 4 wrong / 5 uncovered | **Promoted** to entry-year anchor and corroboration; **refused** as a round label |
| Job board `stage` | 3 right / 16 wrong | **Refused** — same finding as Thrive's 0/10 |

The site-year misses are systematic, not random: the field slips to the
company's own first-round year (Chronosphere reads 2019, the year of a Series A
Lux did not lead, while Lux's own post is titled "Our Series B Investment In
Chronosphere", January 2021) or lags the announcement by a year (Phonic,
Waymark, Maven AGI). Both rulings are recorded in `decisions.md` as R1 and R2.

## 4. Membership: 79 exclusions, almost all of them one of fifteen clusters

Judged cluster-first (§3). Fifteen people explain 66 of the 79 exclusions:

- **Sean Traynor** (11 rows) — Welsh, Carson, Anderson & Stowe's healthcare GP, not Lux's Sean Traynor. Cited.
- **Andrew / Andy Wilson** (13) — irrigation controllers, Australian coal-to-liquids, pickleball courts, a listed telecom, and Intel Corp itself.
- **Richard Foster** (6), **Jeffrey Kindler** (6), **Thomas Reardon** (3), **Tuvia Barak** (2), **Zachary Iscol** (2) — venture partners and advisers holding their own board seats.
- **Michelle Lee** (4), **Nat Turner** (2), **Alex/Alexa/Alexander Nguyen** (4), **Christopher/Christian Gates** (2), **Anthony Thomas** (2) — seats dated against the person's firm at filing time.
- **Uncorroborated in-tenure name-matches** (7) — the person is in tenure but the company appears on no Lux surface in any era. §1 makes that a `not_member` verdict, not an `uncertain` one.

Two vehicles left the base under decisions.md D4: **Lux Health Tech Acquisition
Corp**, Lux's own 2020 SPAC (which deregistered without completing a business
combination), and **Gores Holdings VI**, the shell that took Matterport public.
The member row is the operating company, never the shell.

Two rows were removed by the build's tenure rule before judgment: Flock Homes
(Renata Quintini, filing five years after she left) and Terns Pharmaceuticals
(Jeffrey Kindler, four years after).

## 5. Evidence layers, including the ones that returned nothing

- **Wayback**: 18 years across three era parsers, 301 distinct slugs. CDX answered every query; no outage this run.
- **Common Crawl**: 127 indexes, 267 company slugs and 64 people slugs — an independent capture set converging on the same book.
- **EDGAR**: 455 Form D accessions over 243 issuers from a 73-name roster sweep; 33 entities; 132 companies with a Form D round history (438 rounds).
- **Exit-side EDGAR full-text sweep** (promoted to a primary recall layer by the issue's Δ2): 91 registrants, 44 third-party. It surfaced the whole de-SPAC cohort from the shell side (Trine → Desktop Metal, InterPrivate → Aeva, TS Innovation → Latch, NewHold → Evolv, Gores VI → Matterport, ACE Convergence → Tempo, LifeSci II → Science 37, Dynamics → Senti) and **produced exactly one membership candidate, Myriant Corp, which was rejected**: the phrase hit sits inside R. James Woolsey's director biography ("a Venture Partner with Lux Capital Management"). A person-level mention locates the person, never a firm position.
- **Wikipedia insource sweep**: 57 articles, 22 already in the base, 12 company candidates of which one landed (DoNotPay) and the rest were noise or LP positions (Breakout Ventures names Lux among its own financial partners — an LP stake, not a portfolio company).
- **Roster**: `partner-roster.py` reaches only 2016+, because the dash-separated people namespaces start then. The 2005–2015 people live in `/team_<lastname>.php` pages and in `/imteam/<initials>.jpg` image filenames. `scratch/roster-curate.py` added 15 pre-2016 investment-side names with capture-evidenced windows; without them the Form D sweep is blind to every deal whose only Lux seat was held by someone who left before 2016.

**Negative results worth recording.** The per-deal partner attribution that
made Accel's CMS a judge instrument is *published* by Lux but not reachable:
`company_partner-slugs` appears only inside the "Similar companies" cards, never
on a company's own page, and `/companies` renders a curated 28 of 215 rows with
no pagination to load the rest (confirmed in the browser pane, eight scroll
passes, count stayed 28). The union of every related card across all 215 pages
covers 40 companies. The remaining rows' Form D clusters were resolved by roster
tenure windows instead.

## 6. The visible slice

24 rows are $1B+ or public. Every one carries a sourced figure with an as-of
date and a citation. Findings that changed rows:

- **Hugging Face** — NVIDIA signed a definitive agreement on 2026-09-02 to acquire it for **$12,930,300,000** (NVIDIA's own SEC filing). **The deal has not closed** (expected first half of next year), so under the status rule the row stays `private` with the agreed price as its mark and flips to `acquired` on closing.
- **Eikon Therapeutics** — IPO'd 2026-02-05; status corrected from private to public.
- **Carbon Health** — filed Chapter 11 on 2026-02-02 against a $1.4B pre-bankruptcy mark. See the open ruling in §7.
- **Genocea** — the deterministic layer read it `acquired`; it wound down in 2022 after its 2014 IPO. Corrected with `model_disputes_source`.
- **Resilience** — reported winding down manufacturing operations; documented collapse evidence rules it out of the higher bands regardless of the old mark.
- **Anduril** — pinned at the **$30.5B** June 2025 Series G (TechCrunch, CNBC). Figures of $60–61B circulate on vendor pages and a July 2026 report has the company in talks at ~$100B; **Rule A** keeps the last priced event with a citable figure. The band is `10b_plus` either way.
- **Sakana AI** — ¥400B post-money converted under the policy constant: JPY 400.00B @ ECB 2025-11-20 (JPY/EUR 181.47, EUR/USD 1.1514) = **$2.54B**.

**Rule A cost four rows a band, knowingly**: Aurora Solar, Everly Health,
Saildrone and OpenStore are each believed larger than `below_1b` but the only
figures found are vendor and secondary-marketplace marks (Tracxn, CB Insights,
Forge, GetLatka). Each reads `below_1b` with the check recorded and dated, the
Justworks precedent applied.

## 7. Open rulings for Erik

1. **Carbon Health and the status vocabulary.** The closed vocabulary
   (`private | public | acquired | defunct | unknown`) has no value for "in
   Chapter 11". The business has not ended, so `defunct` is wrong; it is not
   safely `private` at a $1.4B mark either. The row is recorded `unknown` with
   the filing in the note. If you want a different mapping — or a sixth value —
   it is a taxonomy decision, not a row fix.
2. **The pre-window entry_stage tension.** The policy constant nulls
   `entry_stage` for entries before 2006; verify invariant 1 requires the column
   at 100% fill. Seven rows sit in that gap (Angstrom, Atair, Cambrios, Kereos,
   Lux Research, Molecular Imprints, Nanosys). They carry the best-supported
   label at low confidence with a `pre_window_entry` flag. Confirm that reading
   or tell me to publish nulls and relax the invariant.
3. **Lux Research and Angstrom Publishing as rows** (decisions.md D7). Both are
   operating companies Lux created and listed on its own portfolio pages for a
   decade. They are in. Flagged because a firm's own research arm and its own
   media joint venture are the kind of row you may want out of a *portfolio*
   track record.
4. **`ftx`.** A `/companies/ftx` path appears in the archived site index. The
   row is published as a member on that site-listing evidence with
   `identity_uncertain`, status `defunct`. Whether Lux ever held FTX is not
   settled by the evidence in hand, and given the name it is worth your eye.
5. **Two director-of-record members at medium confidence**: `system-inc`
   (Josh Wolfe, 2021) is in; `rivington-holdings-inc` (Peter Hebert, 2024) is
   out as an unidentifiable "Holdings" entity. Both are flagged `needs_review`.
6. **Bilal Zuberi's tenure boundary.** He appears as a Lux partner from 2013 and
   on `/advisors` by 2025. Kinetic Automation (2024) and Frontera Health (2025)
   name him on their Form Ds and appear on no Lux surface; both are ruled
   `not_member` under the uncorroborated-name-match rule. If he was still
   investing the funds in 2024–25, those two flip.

## 8. Debt behind the green verify

| Flag | Rows | What it means |
|---|---|---|
| `stage_uncited` | 133 | entry stage carried at low confidence with no citation — the long tail of a 271-row book with one announcement surface |
| `cohort_unverified` | 73 | C2A cohort rows whose graduation legs are not both verified |
| `suspected_duplicate` | 37 | flagged before the identity overlay merged 34 of them; the flags remain on the merged rows |
| `cite_pending` | 24 | the resumable citation queue |
| `model_disputes_source` | 13 | deterministic layers overridden with a reason (10 of them Wikidata country name-matches) |
| `identity_uncertain` | 9 | one-word names that did not resolve |
| `pre_window_entry` | 7 | open ruling 2 |
| `stale` | 4 | marks older than 24 months |

**`hq_city` is 0/271 filled.** It is not a verify invariant and no queue item
asked for it, so this run did not author it; the Form D issuer city is on every
row that has a filing and the column can be filled cheaply in a follow-up.
Worth deciding whether the pipeline should ask for it, since prior runs filled
it and this one did not.

**`defunct` is undercounted by construction** (7.7% here). Quiet shutdowns
present as `private` or `unknown`; no mortality rate may be read off this column.

**The C2A rate carries its selection bias in the sentence**: of the seed entries
where the record could be established, 33.3% graduated — and the establishable
set skews toward visible successes, with 73 of 90 cohort rows carrying
`cohort_unverified`.

## 9. Cross-investor (invariant 10)

85 rows shared with other published investors: **74 agree, 10 accepted, 0
disagree.** Five pairs are ruled `distinct` — genuine namesakes: Lux's Galileo
(virtual care) against Accel's Galileo Financial and Lightspeed's Galileo
Technology; Lux's Osmo (digital olfaction) against Accel's Osmo/Tangible Play;
Lux's Rivet (healthcare payments) against a16z's Rivet (game servers); and the
two unresolved one-word `neo` rows.

**Five rows were aligned onto this base from published siblings** where their
mark was sourced and mine was not: Ironclad ($3.2B, Accel and Sequoia),
LangChain ($1.25B, Sequoia), Modal ($1.1B, Accel and Creandum — whose note
records Lux joining that round), Nominal ($1B, Lightspeed and Sequoia) and
Unconventional AI ($4.5B, a16z and Lightspeed, which also fixed the entry as a
seed). **Ten pairs are `accepted` because the stale side is another investor's
file** and §12 forbids editing it from this session — they belong to the wave
alignment: Applied Intuition (a16z at $1.25B as of 2020), Hugging Face (Sequoia
at $4.5B), Runway (a16z and Lightspeed at below_1b), Together (Cherry), Hadrian
(Cherry), plus four status disagreements.

Three siblings were in flight and skipped by name: first-round-capital,
menlo-ventures, redpoint-ventures.

## 10. Firm profile

- **AUM $11,237,733,247**, both ends of the range, from Form ADV Section 7.B (annual amendment 2026-03-31): 17 private funds. Lux Capital Management is an **exempt reporting adviser** (802-75425, CRD 163026) and files no Item 5.F, so the 7.B composite is the sworn substitute. TechCrunch reported "$7 billion" at the Lux Ventures IX close — *below* the sworn number, so it sits in the flag, not the range.
- **12 funds** with Form D sizes, eight of them asserted against the filing at build time. Lux Ventures IX's $1.5B Form D matches the reported January 2026 close to the dollar. Lux Ventures I and II predate electronic Form D (REGDEX paper filings).
- **Three vehicles the EDGAR name search cannot reach** came out of the ADV: Lux Defense Leaders, Lux Total Opportunities and **Pioneer Pier Investments**, which carries no "Lux" in its name at all. This is the §11 reason the fund sweep is name-swept rather than partner-matched, and it is why the config's seed queries were widened mid-run.
- **A third-party feeder was caught and excluded**: `Lux Defense - Allocate Access, L.P.` files from Allocate's Menlo Park address, not Lux's — the Thrive IX Access pattern (decisions.md D1b).
- **Icon**: both declared assets fail the measured rules — the 32×32 shortcut icon would be upscaled and the 256×256 apple-touch webclip is pre-blurred (edge ramp 6.09px against a 2px limit). The mark ships as an **inline SVG** in the page; extracted to `sources/site/lux-mark.svg` and normalized from the vector at ramp 0.97px, contrast 17.9:1, box 52%, radius 55% — inside every rule with no override flags. Upload runs at ingest.
- **Positioning-versus-behaviour gap, flagged not corrected**: Lux's own five industry phrases contain **no AI category**, while the base carries 24 AI & Applied AI rows including Hugging Face, Cognition, Runway, Sakana AI, Physical Intelligence, EvolutionaryScale, LangChain, Together and Modal — several of them the largest marks in the book. The Lightspeed/Security finding in its strongest form.

## 11. Deviations from the playbook

- **Two rebuilds, not one.** The scheduled rebuild ran after the recall probe. A second ran at the end, because the delta pass produced one more `not_member` verdict (`centrexion-corp`) and a `not_member` row must not sit in the published base. Nothing was re-judged between them; the grind was complete.
- **The momentum slice was not fully web-checked.** 73 private rows with an entry inside the last five years qualify. The believed-$1B rows among them were checked and pinned; the remainder were checked against the unicorn snapshot (which matched 10 rows and, tellingly, does not carry Anduril at all) rather than one web search each. The unchecked rows are the ones carrying `stage_uncited` without `valuation_range_source`, and the search budget needed for a full slice on a book this size is ~70 calls.

## 12. Playbook write-back — proposed, not applied

Three siblings are in flight and §12 reserves `COLLECTION.md` and `scripts/`
to the designated tooling session during a wave, so these are proposed here
rather than committed. Each is investor-agnostic and paid for by this run.

1. **§5, era parsers — the row's own anchor text owns the name, not the image
   alt.** Lux's `LOGO_ACCELERGY.gif` carries `alt="Angstrom Publishing"` and
   `LOGO_CIS.gif` carries `alt="Cambrios Technologies Corp."`. An alt-first
   parser silently drops both companies, because the wrong name collides with a
   row already seen. Where a listing renders both, prefer the anchor text and
   keep the alt as a fallback. (Generalises the existing "the site's own
   rendering owns name and slug" rule to the case where the site renders the
   same row twice, inconsistently.)

2. **§5 / §4 — a firm job board's `stage` field is refused as a label
   standing, without re-scoring.** Thrive scored it 0/10; Lux scored it 3/19,
   and the misses have the same cause both times: the field describes the
   company's current stage (`ipo`, `acquisition`, `series_f`), not the round
   the firm entered. Two independent measurements on two different boards is
   enough to make it a standing rule rather than a per-run gate item. Keep it
   in the evidence pack as an unscored extra.

3. **§6 status/valuation — a signed but unclosed acquisition agreement is a
   priced event, and it does not flip status.** NVIDIA's definitive agreement
   to buy Hugging Face for $12.93B (2026-09-02, in NVIDIA's own SEC filing) is
   a better mark than the 2023 round it supersedes, and stronger than any
   vendor estimate — but the status rule turns on the *closing*, so the row
   stays `private` until then and flips on close. Proposed wording: "an agreed
   transaction price in a definitive agreement is a valid `web_verified` mark
   for the target while the deal is pending; the row's status changes only at
   closing, and the note carries the expected close."

4. **§6 status vocabulary — there is no value for a company in Chapter 11.**
   Carbon Health is neither `defunct` (the business has not ended) nor safely
   `private` at its old mark. This run recorded `unknown` with the filing in
   the note, which is the least-wrong mapping but not a good one. Raised as
   open ruling 1; it needs Erik's decision before another run hits it.

5. **§11 icon rules — check the page for an inline logo SVG before accepting a
   soft raster.** Lux's two declared assets both fail the measured rules (the
   favicon would be upscaled; the apple-touch webclip has a 6.09px edge ramp),
   and `--discover` therefore offers nothing publishable. The mark itself ships
   as an inline `<svg viewBox="0 0 64 64">` in the page markup and normalizes at
   ramp 0.97px and contrast 17.9:1. Proposed: `--discover` should also list
   inline logo SVGs found in the page source, which is where a Webflow site
   often keeps the real mark.

6. **§11 — `build-firm-profile.py` has two undocumented required inputs with no
   generator.** It reads `sources/edgar/fund-formds.json` and
   `sources/site/team-members.json`, and refuses to run without them, but
   nothing in the pipeline writes either; every run so far has hand-built them.
   `fund-formds.json` is a mechanical filter of `formd-sweep.json` by
   `config.profile.own_vehicle_pattern` and should be emitted by `run.py
   collect` (or by the profile build itself). `team-members.json` is the site
   team pull in a fixed shape. Two schema traps cost time here: the file's
   `_readme` must be a **dict**, not a string, because the fund verifier
   iterates every value; and a fund entry carrying an `accession` is asserted
   against `TOTALAMOUNTSOLD` on that filing, so a fund whose latest Form D
   reports `$0 sold` must carry no accession.

7. **§1 / §10 — the pre-window rule and invariant 1 contradict each other.**
   The policy constant says entries before 2006 carry `entry_stage` null;
   invariant 1 requires the column at 100% fill. Seven Lux rows sit in the gap.
   Whichever way Erik rules (open ruling 2), one of the two sentences needs
   editing so the next pre-2006 book does not re-derive the conflict.
