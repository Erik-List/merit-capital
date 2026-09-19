# Lux Capital — investor-specific decisions

Derived from the standing rule set in `data/collection/COLLECTION.md` §1 under
the derivation protocol: one line per category, the facts found, the test
applied, the outcome, the precedent. Derivations need no confirmation — they
are listed in PRO-95 and PRO-87 for Erik to veto before kickoff; silence means
they apply. Only the deltas in §2 needed Erik, and PRO-95 states them.

Run: PRO-95, one session, started 2026-09-06.

## 0. The facts this file rests on (verified at kickoff, not assumed)

| Fact | Source |
|---|---|
| One adviser: **Lux Capital Management, LLC**, exempt reporting adviser, SEC file 802-75425, CRD 163026, CIK 1592843, 920 Broadway 11th Floor, New York NY 10010 | Form ADV annual amendment filed 2026-03-31 (`sources/adv/lux-capital-adv-163026.pdf`), IAPD firm search |
| No relying adviser, no second registration under the brand | IAPD firm record CRD 163026 lists no relying advisers and no other CRD; no other "Lux Capital" adviser exists in IAPD (Luxor Capital Group, Fiat Lux, Luxe Capital, Lux Aeterna are unrelated firms) |
| **No 13F filer**: the adviser reports no public-market holdings | EDGAR submissions for CIK 1592843 — 14 filings, all SC 13D/G and Forms 3/4 on portfolio issuers, no 13F-HR ever |
| 17 private funds, **$11,237,733,247** gross assets | ADV Section 7.B, 2026-03-31 |
| Firm founded 2000 by Josh Wolfe, Peter Hébert and Robert Paull; nanotech research and venture from the start | luxcapital.com captures from 2000-04; 2001 `industryfocus.htm` ("Information Technology and Nanotechnology", "start-up capital, or the first outside funds a company raises") |
| Lux incubates and co-founds companies | The firm's own 2012 portfolio page: "Genocea was founded by Lux in 2006 as a spin-out of Harvard Medical School", "Kala Pharmaceuticals was founded by Lux as a spin-out of Johns Hopkins", "Lux ideated and helped lead the spinout of Everspin from Freescale" |

The vehicle family, all at 920 Broadway (EDGAR company search + ADV 7.B):
Lux Ventures II–IX flagships (II CIK 1592755, III 1534238, IV 1633331,
V 1698008, VI 1783918, VII 1864660, VIII 1970486, VIII-B 2144228, IX 2090925),
Lux Ventures Cayman III (1569760), the sleeves (II Sidecar 1343943, Sidecar II
1603613, II Partners Fund I 1603613, III Special Founders Fund 1534241, VI
Sidecar 1783917, VII/VIII/IX Entrepreneurs Funds 1864659, 1970485, 2101310),
the co-invest vehicles (Lux Co-Invest Opportunities 1722022, II 1783916, Lux
Co-Invest Partners LLC 1722021), **Lux Defense Leaders, L.P.** (2059472),
**Lux Total Opportunities, L.P.** (1864658), **Pioneer Pier Investments, L.P.**
(2009624) and Lux Health Tech Acquisition Corp (1823767, the 2020 SPAC).

## 1. Derivations

**D1 — T1, same adviser. Every Lux vehicle above is IN.** One exempt reporting
adviser with no relying adviser and no brand-sharing registrant: the
Accel-KKR / Meritech / Lightspeed India pattern was checked in IAPD and does
not exist here. The lettered, sidecar, entrepreneurs', co-invest, Cayman and
single-strategy vehicles are sleeves of that one adviser and are named in its
own Section 7.B table. Precedent: a16z's vertical families, Thrive's umbrella,
Creandum's four ERAs.

**D1a — T1 strategy desks: not reached.** Lux runs one strategy (venture) from
one adviser. `Lux Defense Leaders` and `Lux Total Opportunities` are venture
sleeves of the same adviser at the same address, not a buyout, credit or
public-equities desk, so the strategy-desk partition does not fire and no
`other_desk` exists on this run. The profile is therefore sliced to the same
boundary as the base with no parent/child AUM problem: the $11.24B 7.B
composite is the whole firm.

**D1b — T1: `Lux Defense - Allocate Access, L.P.` (CIK 2067895) is external.**
It files from 1300 El Camino Real, Suite 100, Menlo Park — Allocate's address,
not Lux's — and is a third-party feeder that raises into Lux Defense Leaders.
Precedent: Thrive IX Access (a third-party feeder into a fund is external;
agent, flagged). Its own filings are not Lux membership evidence, and it is
configured `external` in `desks.classify[0]`.

**D2 — T2, fund money. Lux's incubations and spin-outs are IN where a fund
held the position.** Lux is a company creator (Genocea 2006, Kala, Everspin's
spin-out from Freescale, Lux Research), and the firm's own listings say so.
A company Lux ideated and funded is a portfolio company on the same test as
one it met cold: the question is only whether fund money entered. Precedent:
Thrive's incubations, including pre-spin-out ones where a fund held the
position. The corollary binds too — a Lux-founded entity that no fund ever
held (a research product, a conference, a publication brand) is not a row.

**D3 — T2. Scout checks with no main-fund follow-on, partners' personal angel
books and the Riskgaming / Securities newsletter's subject companies are OUT.**
Standing rule, ruled on Sequoia, a16z, Accel, Lightspeed and Cherry. Lux
publishes a large media surface (the Securities newsletter, the Riskgaming
podcast and scenario archive) which names hundreds of companies it does not
hold; a naming there is editorial, never a listing. This is the recurring
false-positive class for this investor and the trap set is built to catch it.

**D4 — T3, venture entry. De-SPAC rows are members; the SPAC shell is not.**
Lux's holdings that went public by SPAC merger (Desktop Metal, Matterport,
Aeva, Rigetti, Evolv, Shapeways, Planet and others to be resolved on the
evidence) entered through venture rounds years earlier and stay members after
listing — the standing rule that a row entering through a venture round stays
in after it goes public. `Lux Health Tech Acquisition Corp.` itself is **not a
row**: a blank-check shell is not a venture-outcome operating company (T5), it
is the vehicle, and it is a Lux vehicle besides. Its own outcome (it
deregistered without completing a business combination — 15-12G and 25-NSE on
CIK 1823767) is reported in the firm profile's fund ladder, not in the base.

**D5 — T3. Positions first appearing as a 13F holding or a post-IPO 13G are
`not_member`.** Standing rule generalized 2026-09-03. Lux files no 13F at all,
so the crossover-treasury class is expected to be empty here; the 13D/G
filings by Lux Capital Management and the funds are post-IPO reports of
venture positions, which stay in. Each 13G subject is still checked for a
documented pre-IPO round rather than assumed.

**D6 — T4, person or firm. Standard seat dating, with four named clusters.**
A seat is dated against the person's firm at filing time. The roster spans
2000–2026 and its departures are the sweep's main noise source: Renata
Quintini (Lux 2015–2017, then Renegade Partners), Zavain Dar (Lux to 2022,
then Dimension Capital), Adam Goulburn (to 2022), Bilal Zuberi (Partner from
2013, on `/advisors/` by 2025), plus the 2005–2008 people (Sasha Blaug, Nick
Wachtel, Carl Barrelet) whose later careers are elsewhere. Name-match rows are
judged cluster-first (§3), and the live site's per-company partner attribution
(`company_partner-slugs`, 210 of 215 rows) is the reference graph.

**D7 — T5, operating company. Lux Research Inc and Angstrom Publishing are
rows; the funds, the SPAC and the newsletter are not.** Lux Research (the
nanotech research and advisory firm Lux spun out in 2004) and Angstrom
Publishing (the Forbes/Wolfe Nanotech Report joint venture with Forbes) are
operating companies with employees, customers and revenue, and both sat on the
firm's own portfolio page for a decade — a site listing suffices for
membership. That they were founded by the firm is D2's case, not an exclusion.
Fund-shaped list entries, feeders, the SPAC shell and natural persons are not
rows.

**D8 — Policy constants apply unchanged.** Window opens 2006 (Lux's 2001–2005
nanotech entries are pre-window: `entry_stage` and graduation null, the row
still a member); secondaries and tenders are Growth; a private mark is stale
beyond 24 months; ECB conversion on the figure's own date; a listing outside
SEC registration takes a web-cited market cap. Rule A binds: vendor marks
never band a row.

## 2. The deltas (PRO-95, confirmed by Erik in the issue)

**Δ1 — SPAC-listed holdings carry more `status` and valuation weight than a
typical archetype-A base.** A de-SPAC is a public row from its listing date and
its mark is the **cited market cap**, never the merger's announced enterprise
value or the pre-deal PIPE valuation — the class of figure that is a promise
rather than a price. Several Lux de-SPACs trade far below their merger
valuations, so an uncorrected EV would mis-band a whole cohort upward.

**Δ2 — deep-tech and defense holdings are quiet, so the exit-side EDGAR
full-text sweep runs as a primary recall layer**, not a late check: government-
funded, classified-adjacent and hardware companies raise without press, and
Lux's own announcement surface is a newsletter rather than a deal blog. Run
`edgar-fts-sweep.py` before the recall probe, alongside the Wikipedia insource
sweep.

**Δ3 — check for a separately advised vehicle under T1.** Done at kickoff and
answered negative: no second registration, no 13F, no crossover sleeve
(see D1/D1a and §0). The check is recorded rather than left implicit.

## 3. Run-time standing rulings

Dated, class-wide, flagged for Erik's review. Added as the run makes them.

**R1 (2026-09-06) — the site's `Lux investment: <year>` is an entry-year anchor,
not a round label.** Scored on the 26-row stage golden set: 17 exact, 4 wrong,
5 uncovered. The four misses are systematic rather than random — the field
slips to the company's own first-round year (Chronosphere reads 2019, the year
of a Series A Lux did not lead, while Lux's own post is titled "Our Series B
Investment In Chronosphere", January 2021) or lags the announcement by a year
(Phonic, Waymark, Maven AGI). So the year feeds `first_seen` and corroborates,
and a dated announcement naming the round overrides it with
`stage_disputes_band` plus the citation. Class-wide, flagged for review.

**R2 (2026-09-06) — the job board's `stage` field is refused as a stage label.**
Scored 3/19 on the same set: it reports the company's current stage, not the
round Lux entered (Recursion "ipo", SteadyMD "acquisition", Shiru "series_b"
against a documented $3.5M seed). Same finding as Thrive's 0/10. It stays in
the evidence pack as an unscored extra and may not label a row. Class-wide.

**R3 (Erik, 2026-09-07) — a Chapter 11 filing reads `defunct`.** The closed
status vocabulary had no value for a company in reorganisation, and this run
carried Carbon Health as `unknown` pending a ruling. Erik's reading: Chapter 11
means the business goes defunct afterwards, so the row is `defunct`. This does
not disturb the standing insolvency rule for the case where a sale follows —
insolvency **followed by an asset sale** is still `acquired` with a successor
note (Shapeways, Tempo Automation), because there the business continues under
an acquirer. Class-wide and investor-agnostic; written back to COLLECTION.md §6
the same day under the ratchet rule.

### D-S2A — Seed-to-A graduation re-judged; the stage leg, not the graduation, is what limits this book (2026-09-17, agent, class-wide)

Under the 2026-09-16 contract (COLLECTION.md §6) all 133 in-window Seed rows
were re-judged: 130 seed entries, 9 censored, 94 undetermined, cohort 27,
graduated 24, not graduated 3, rate 88.9%, **coverage 22%** — the thinnest of
the wave, and for a reason worth recording.

**The binding constraint is the entry-stage leg.** Only 25 of the 133 rows
arrive with a verified stage (17 `formd_band`, 8 with an on-disk citation).
Deciding any of the other 108 needs a page naming the *seed round with Lux in
it*, and Lux's announcement surface is a newsletter rather than a deal blog,
exactly as Δ2 predicted. So the common shape of an `undetermined` here is not
a missing graduation: it is a well-cited later round in which Lux appears only
as a participant, or a company whose seed no publisher attributed. Of the 94
undetermined, 26 have a cited later round and fail only on the seed leg, 31
have nothing but the site's own year, 34 have neither leg, and 3 have a
settled stage whose graduation source refuses automated fetching.

`verify.shape.c2a_rate_max` is restated from 0.80 to 0.90: what survives the
stage filter is a remnant of well-covered companies, so the rate sits high on
very thin coverage, and the coverage is published beside it.

Three Form D verdicts were overturned with citations (**aeva**, a $45M Series
A of Oct 2018 the filings miss and which invariant 7 forbade calling a no on a
public row; **flex-logix**, a named $55M Series D of Mar 2021; **sols-systems**,
an $11.1M Series B of Feb 2015); fourteen were confirmed. Three rows left the
cohort, each on evidence that forces it rather than merely suggests it:
**applied-intuition** and **mos** on Lux's own posts naming the round a Series
A, and **echodyne** on arithmetic (the May 2017 $29M is explicitly the Series
B and total raised is $44M, so the Dec 2014 $15M that names Lux is the A).
The standing line: a re-stage needs the firm's own post naming the round or
arithmetic that forces it; a citation merely naming Lux inside a later round
is not enough, and those rows stay `undetermined`.

**Open for Erik — five entry-stage questions**, each a row where Lux is named
in a later round and the site year points earlier:
1. **cajal-neuroscience** — Lux co-led the $96M Series A (2022-11-29); the site dates the investment 2020.
2. **impulse-space** — Founders Fund led the $20M seed in early 2022, and TechCrunch says Lux "previously supported the company with a $10 million funding deal last summer" (FinSMEs dates it 2022-06-20); the round Lux entered has no name.
3. **summer-health** — Lux co-led the $11.65M Series A (2024-04-23), and the report lists the returning investors without Lux, against a 2022 site year.
4. **lightform** — Lux led the unnamed $5M round of 2017-11-22, which followed a $2.6M seed that does not name Lux.
5. **sols-systems** — the structural `formd_band` Seed was kept, but if the Feb 2015 round is the Series B then the Lux-led April 2014 round is the Series A and the band is wrong.

**R4 (2026-09-19, PRO-135) — this book's 188 sourceless stages are decided by
what their own notes say, and 137 of them read `undetermined`.** Lux carried
every one of the repo's 214 stages with an empty `entry_stage_source`, and the
reason is structural rather than an oversight: the firm publishes no round word
anywhere. Its site gives `lux_investment_year` and a milestone line ("Lux
investment: 2021"), which R1 already ruled an anchor and not a label; its Getro
job board gives a `stage` field, which R2 already refused as the company's
current stage; and neither is eligible under PRO-135's first-party harvest, so
Lux is the one book of twenty where that harvest yields nothing. What it does
have is the firm's own **announcement archive**, and that is where five rows
came back: auris-health ("Lux co-led Auris Health's Series A financing in
2012"), matterport ("Lux led Matterport's Series A financing"), steadymd ("Lux
Capital is leading SteadyMD's $25M Series B", so the B is the entry and the row
is Growth), plus hugging-face and fiddler on the firm's own 2019 posts. Those
are class-1 `first_party` with the post as the citation.

For the rest the row's own note is the record of what the earlier pass knew, and
it decides:

- **45 rows take `model`.** The note names the company's own round pinned to one
  transaction by an amount or a date — "launched 2023 with a $193M Series A",
  "Ahana's $2.25M seed of 2020-06-02" — which is rung 3 of the evidence order.
  The empty source field was a recording omission, not an absent source.
- **137 rows read `undetermined`.** The note names no round, or says outright
  that none could be found: "entry round not documented on any Lux surface", "no
  Pinscreen round announcement could be retrieved at all", "pre-window entry so
  entry_stage is null by policy" — and PRO-137 has since retired the date policy
  the last phrasing rested on. An absence phrase outranks a round word mentioned
  in passing in the same note.
- **`Growth` is the one stage a note establishes without a round word**, because
  it is the whole ladder from Series B up: eleven rows say the entry came after
  the company's earlier rounds ("Lux entered in 2020 at a later round, not at
  formation"; "a decade after founding and at one of the late private rounds")
  and that sentence settles Growth whatever the round was called. The same
  sentence would not settle Seed or Series A, so the rule is gated on the value.

The published effect is large and intended: 137 of 270 rows leave the stage
distribution, the S2A cohort drops to 26 decided rows, and the rate moves to
88.5% over that cohort. They keep their band, their status and their focus —
an unknown round is not an unknown company (§6) — and `verify` now says so on
its own `stage unknown` line instead of folding them in with the unnameable.
