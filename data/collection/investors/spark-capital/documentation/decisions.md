# Spark Capital — investor-specific decisions

Applies the membership rules of `../../COLLECTION.md` to Spark Capital (slug
`spark-capital`, display name always **Spark Capital**). The judge cites these
rulings per line. Phase 0 (PRO-85) was researched 2026-09-05 and **confirmed by
Erik 2026-09-05** ("phase 0 is confirmed"); the facts under it were re-verified at
kickoff the same day against IAPD, the ADV PDF, EDGAR and the live and archived
site, and this file records the verified facts. Written under the derivation
protocol of COLLECTION.md §1: **derivations** (a standing test applied to verified
facts, vetoable, no confirmation needed), **deltas** (Erik's) and **run-time
standing rulings** (dated, flagged for review).

**The structural fact of this run:** Spark Capital is a 2005-vintage US
early-stage firm that added a growth strategy in 2014, under one exempt reporting
adviser and one team. Its live site is a **selected** list — 45 companies in six
tabs (the 124 rendered cards repeat them), ten of them carrying an exit marker —
while the archived site is the recall layer: the 2021 and 2023 Webflow listings
carried 135 and 164 distinct companies, the 2015–2019 WordPress `/companies/`
namespace 127 per-company pages with sector, geography and a seed / venture /
growth class per card, the 2012–2015 WordPress `/portfolio/` namespace 116 pages,
the 2008–2012 ExpressionEngine `/company/` namespace 74 pages with a rendered
listing (25 companies in 2009, 41 in 2011), and the 2006–2008 static site a dozen
per-company pages. The SEC footprint is full: 27 private funds in the ADV's
Section 7.B ($15.57B gross asset value), every fund family filing Form D, and the
fund vehicles filing 13G/13D and Forms 3/4 on the public winners; the EDGAR
full-text phrase "Spark Capital" returns ~900 documents.

## Derivations (T1–T5 applied to verified facts; vetoable, no confirmation needed)

- **D1 — The firm (T1, same adviser).** Spark Capital = the adviser filing as
  **Spark Capital** (other name **Spark Capital Partners, LLC**; CIK 2098748),
  SEC exempt reporting adviser 802-75412, **CRD 161231**, ERA since 2012-03-29
  (state ERA filings: Massachusetts 2012-08-01, California 2017-03-16, New York
  withdrawn 2020-03-26), Form ADV annual amendment filed 2026-03-27. Principal
  office **200 Clarendon Street, 59th Floor, Boston, MA 02116**; other offices
  **165 Mercer Street, 3rd Floor, New York, NY 10012** and **600 Montgomery
  Street, 25th Floor, San Francisco, CA 94111** (ADV Section 1.F). Website
  sparkcapital.com (ADV Section 1.I). Founded 2005 (Spark Capital, L.P., CIK
  1334932; the 2007 site: "a venture fund based in Boston, Massachusetts … the
  conflux of the media, entertainment and technology industries"). Verified
  vehicle set (ADV 7.B as of 2026-03-27, EDGAR company search 2026-09-05):
  flagship **Spark Capital, L.P. (2005) through Spark Capital VIII, L.P.**
  (7.B GAV: I $9.7M residual, II $252.7M, III $874.8M, IV $609.4M, V $882.0M,
  VI $678.6M, VII $1.19B, VIII $777.4M) and **Spark Capital IX, L.P.** (CIK
  2123887, Form D 2026, not yet in 7.B); **Spark Capital Growth Fund, L.P.
  (2014) through Growth Fund V** (GAV $1.76B, $538.3M, $2.34B, $3.75B, $1.75B)
  and **Growth Fund VI, L.P. / VI-A, L.P.** (CIKs 2123891 / 2140721, Form Ds
  2026); **Spark Capital Founders' Fund, L.P. through IX** and **Spark Capital
  Growth Founders' Fund, L.P. through VI** — partner and GP co-investment
  sidecars (related-person ownership 53–93 %, GAV $0.2M–$38.7M each); **Spark
  Member Fund, L.P.** (100 % related persons, GAV $0.5M, an employee vehicle);
  general partners **Spark Management Partners (I–VIII), LLC**, **Spark
  Management Partners III (AIV I), LLC** and **Spark Growth Management
  Partners (I–V), LLC**. All under one adviser and one investment team (the
  site's Early / Growth / Emeritus tabs are one roster) → **IN**: primaries,
  follow-ons, secondaries and tenders from any of these vehicles. A position
  held only through a Founders' Fund is still fund money under the adviser
  (T2) → IN, never a separate desk. Precedent: a16z's crypto / bio families
  under one adviser; Thrive's lettered LLCs; Creandum's Select and SPV
  vehicles.
- **D2 — Early and growth are one desk (T1 strategy-desk rule).** Spark Growth
  is a venture-growth strategy of the same adviser and team, not a buyout,
  credit or public-equities strategy, so it is not `other_desk`; a row's
  `entry_stage` is the round in which the firm first put fund money in, never
  the vehicle (the 2018 site's Slack story: "partner with Slack through Spark
  Growth in 2015" is a Growth entry by the record; Twitter's 2008 Series B a
  Growth entry by taxonomy even though it came from the flagship fund).
  Precedent: Lightspeed's US/Europe/Israel under one CRD; the Accel London
  desk inside the umbrella.
- **D3 — Namesakes OUT (T1), verified by CRD, CIK and address, never by name.**
  Spark Growth Ventures (CRD 330397), Sparkline Capital LP (CRD 314364),
  Sparks Capital Management (CRD 311222), Blue Spark Capital Advisors (CRD
  159025), Sparks Capital Corporation (CRD 36683), SparkChain Capital, L.P.
  (CIK 1770470), Spark Networks (NYSE: LOV), SparkLabs (accelerator), Spark
  Ventures (Chicago), Spark Therapeutics, SparkCognition, Spark Energy /
  Power / Infrastructure, and "Spark" as a product word in issuer names.
  Encoded as `desks.classify[0]` external patterns (the external rule runs
  before the home-desk rule so a "Spark Capital Management / Advisors / Group"
  namesake cannot be claimed by the `^spark capital` prefix) and reviewed per
  CIK in `entities.json` after `collect`. The bare phrase "Spark Capital" on
  EDGAR full-text search is read once for noise (the funds' own 13G/13D and
  the third-party S-1 / 424B hits are the signal).
- **D4 — Programs (T2, fund money).** One program exists and it is fund money:
  **Start@Spark** (launched 2009-03, Wired 2009-03-26 as archived on the
  firm's own news page: "up to $250,000 in jump start money" for Boston and
  New York entrepreneurs, alongside the firm's own seed checks such as
  "$300,000 in Tumblr"). Start@Spark checks came from the flagship fund, so
  its companies are members with `entry_stage` Seed (precedent: Sequoia Arc,
  a16z speedrun, Accel Atoms per cohort company where fund money was
  deployed). No scout program, angel network or accelerator was found on any
  site era (2006–2026), the ADV or the Form D record; a partner's personal
  angel check with no fund position stays out (Kushner precedent).
- **D5 — Instruments (T3).** Primaries, follow-ons, secondaries and tenders
  IN; secondaries and tenders are Growth entries by the policy constant;
  control positions out (none expected: no vehicle makes buyouts). LP stakes
  out; the Founders' Funds' and Member Fund's own LP positions in the
  flagship or growth funds are plumbing, not rows (T5).
- **D6 — Post-RIA public or secondary purchases with no venture entry — OUT**
  (standing rule since 2026-09-03). The fund vehicles file 13G/13D and Forms
  3/4 on public rows (Twitter, Wayfair, Affirm, Flywire, eToro, Coinbase,
  Snap …); every such row is checked for the venture entry that made it a
  member, and a position that first appears as a 13G/13F holding with no
  documented pre-IPO round is `not_member` (crossover treasury), raised as an
  Accel-arista-class case only if the record is genuinely silent.
- **D7 — Carried verbatim from §1.** Ex-partner filings out (a seat is dated
  against the person's firm at filing time); personal Section 16 out; LP
  stakes out; evidence sufficiency (a listing on any era of the firm's own
  site suffices alone, a fund vehicle's SEC filing suffices alone, a Form D
  related-person name-match never); fund-shaped list entries and token
  positions under the standing rules; a site-listed acquirer of a portfolio
  company is checked for sale consideration before it seeds member.
- **D8 — The roster (T4 seat dating).** Investing staff over time from the
  archived people pages with capture-year tenure windows: 2006–2007 static
  `/team/<first>_<last>.html` (Todd Dagres, Santo Politi, Paul Conway, Bijan
  Sabet, Alex Finkelstein, Dennis Miller, Scott Borenstein), 2008–2011
  ExpressionEngine `/team/bio/<firstlast>` (plus Mo Koyfman, Robert Go,
  Andrew Parker, Charles Huang, David Haber), 2012–2019 WordPress
  `/team/<first>-<last>/` (plus Nabeel Hyatt, Jeremy Philips, Kevin Thau,
  Megan Quinn, John Melas-Kyriazi, Alex Clayton, Will Reed, Yasmin Razavi,
  James Kuklinski …), 2020–2023 Webflow `/team-profiles/` and 2024+
  `/team-members/` (the live site: Early — Ashwill, Finkelstein, Hyatt,
  Kelton, Politi, Thau, Vais; Growth — Armstrong, Dendekuri, Fisher,
  Kuklinski, Philips, Razavi, Reed, Talwar; Emeritus — Sabet, Conway,
  Dagres). The 2006–2011 slugs carry no dash and are **curated** into
  `sources/wayback/partner-roster.json` by `scratch/roster-curate.py` from
  the CDX capture years of their bio pages; Operations staff are excluded
  from the Form D sweep (they sit no issuer boards for the firm). Common
  names (Dennis Miller, Andrew Parker, Paul Conway, Will Reed, Kevin Thau,
  Charles Huang, David Haber, Robert Go) are judged cluster-first; a roster
  name on a filing outside its window, or on an issuer with no Spark
  listing, announcement or vehicle, is a homonym or another firm's seat.
- **D9 — The archived Webflow exit marker is status evidence, not a label.**
  The 2020–2026 cards carry "NYSE: TWTR in 2013" / "Acquired by Facebook in
  2014" lines; they corroborate `status` (public → acquired for Twitter's 2022
  take-private is decided by the record, not the 2013 marker) and are never
  the sole source of a status. The 2015–2019 WordPress seed / venture /
  growth class is the firm's own stage label for the company **as listed**
  and is scored on the gate (§4) before it may corroborate `entry_stage`;
  "venture" is not a taxonomy value and maps to Series A only where the
  record agrees.
- **D10 — Policy constants.** Window opens 2006: Spark Capital, L.P. closed in
  2005 and the first deals (thePlatform, Veoh, KickApps, Twistbox) are on the
  2006 site; an entry documented in 2005 is pre-window (`entry_stage` and
  graduation null). Secondaries and tenders are Growth; a private mark is
  `stale` beyond 24 months; non-USD figures convert at the ECB reference rate
  of their own date (`scripts/fx-convert.py`); a listing outside SEC
  registration (eToro on Nasdaq is SEC-registered; a Tel Aviv or London
  listing would not be) takes a web-cited market cap.
- **D11 — Co-issued Form Ds (§11 trap).** The Founders' Funds and Growth
  Founders' Funds file beside their main funds; a per-accession issuer scan
  keeps the last co-issuer row and cross-wires names to CIKs. Fund sizes are
  read per documented close with `co_issuers` recorded; the Founders' Funds
  are described in the profile's funds basis, never listed as flagship
  vehicles.
- **D12 — Expected shape (verify.shape).** `one_b_share_max` 0.30 (default
  0.20): a 2005-vintage firm with a growth strategy whose live list is a
  winners' selection and whose fund vehicles file on the public winners
  carries a large visible slice (Twitter, Slack, Snap, Coinbase, Affirm,
  Wayfair, Anthropic, Discord, Scale AI, Deel, Ramp, Plaid, Kalshi, Niantic,
  Marqeta, Carta …) even after the archive and Form D layers add the long
  tail; the guard still fires above 30 %. `c2a_rate_max` stays 0.80.

## Deltas (Erik's; none raised at kickoff)

No fact verified at kickoff falls outside a standing test or satisfies two tests
with opposite outcomes. Erik confirmed the Phase 0 set on 2026-09-05. Two facts
in the issue were corrected mechanically (facts flip derivations, they do not
reopen rulings): the live list holds **45** companies, not ~120 (the 124 cards
repeat across tabs), so recall rests on the archive and filings even more than
the issue expected; and a seed **program did exist** (Start@Spark, 2009), ruled
IN under T2 as fund money (D4).

**String and namesake traps** (PRO-85): "Spark" is a common product and fund
word — Spark Networks, Spark Therapeutics, SparkCognition, Spark Energy, Spark
New Zealand, Apache Spark (Databricks is not a Spark Capital row on that
account), SparkLabs, Spark Ventures, Sparkline, Sparks Capital, Blue Spark;
the standard "Spark Capital, Union Square Ventures and …" co-investment
sentence (USV is a frequent co-investor: Twitter, Tumblr, Foursquare, Kik —
a USV row is not a Spark row and vice versa); "Spark-backed" applied to
companies the firm never held. Encoded as `desks.classify[0]` and the
entity-qualified `edgar.fts_own_pattern`.

## Run-time standing rulings (dated, class-wide, flagged for Erik's review)

(none yet — added during the run)

13. **Layer calibration on the gate** (agent, 2026-09-05, before the grind; scores in
    `golden.json` `_layer_scores`). The 2015–2020 listings' stage class is
    corroboration for `seed` (5/5) and `growth` (8/8) and no stage claim for
    `venture` (an A-or-later bucket: 8 Growth entries carry it); the Form D band
    scored 15/24 and stays a ceiling on entry recency, re-judged on every
    pre-filled row; the firm's 2006–2016 news archive names the entry round on
    a quarter of the golden rows and is a class-1 citation where it does; the
    judge's blind pass scored 44/44 with six rows where the evidence pack alone
    would have taken a later partner-anchored filing for the entry (Carta,
    Flywire, Lightmatter, Abridge, eToro, AdMeld) — the §6 rule that the first
    filed round is a ceiling, not the entry, applied throughout the grind.
14. **Two site-listed rows are not members** (agent, 2026-09-05, flagged for
    Erik). **CNET**: the Spark funds' Forms 3/4 on CNET Networks (January 2008)
    are the activist stake Spark took beside JANA Partners and Sandell in the
    CNET proxy contest, sold into the CBS acquisition that year; CNET was
    public since 1996 and never raised a venture round from the firm, so the
    Webflow alumni card (2021–2025, "Acquired by CBS in 2008") records a public
    purchase with no venture entry — `not_member` under the standing rule (T3,
    D6), the seed-evidence verdict overridden. **Mandalay Media**: listed
    2008–2011 as the successor of Twistbox (acquired by Mediavest/Mandalay
    Media in February 2008; Spark Management Partners' 13D on Mandalay Media is
    the sale consideration) — `not_member` under the consideration rule (D7);
    Twistbox (2006 entry) stays the member row, `acquired` 2008.

15. **At-scale first rounds keep the record's label** (agent, 2026-09-05, class-wide,
    for Erik). A venture round the firm and the press call "Series A" is keyed
    Series A whatever its size (Antithesis $105M A 2025, The Bot Company $150M A
    2024, Perch's $8M A 2020 before the SoftBank round); Growth is kept only for
    growth equity into mature businesses (Wayfair's $165M 2011 round into a nine-
    year-old profitable company, Harmonix, IPWireless). The alternative reading
    (Growth for any at-scale first check) would move three rows.
16. **Stale primary marks and the A/B pass** (agent, 2026-09-05, for Erik). Every
    $1B+ band now carries a web-verified figure and citation (66 rows; public caps
    as of 2026-09-04). Two judgement calls: **Sift** was ruled DOWN to below_1b —
    the $1B mark is the April 2021 round and 2026 secondary marks sit near $142M
    (premieralts), documented collapse evidence under the stale-primary rule;
    **MatX** carries a $1.0B *floor* (Caplight estimate) because the company
    states "several billion" for its $500M Series B (Feb 2026) without a figure
    and the schema needs one for a 1b_plus band. Twenty-two rows keep `stale`
    with their last priced mark named in the note.
17. **Cross-investor alignments** (agent, 2026-09-05; invariant 10). Aligned to the
    sibling's evidence: Careship → `acquired` (Creandum), Sesame → 1b_plus $1.0B
    (the a16z and Sequoia bases' figure; the Oct 2025 Series B's valuation was
    not disclosed, premieralts' $862M noted). Accepted pending the wave
    alignment: Justworks (Spark 1b_plus on aggregator marks vs Thrive below_1b
    without a figure — Erik picks the band), Catalyst (merged into Totango Feb
    2024; Accel's `private` is stale), InVision (Accel's `unknown` stale).
    Distinct: Beam, Parallel (Sequoia = Parallel Finance), Convex, Relay, Lola,
    Mirror, Post, Handshake ×2.
18. **Registrant twins after the exclusion of their canonical** (agent, 2026-09-05,
    write-back candidate). CNET Networks Inc, Imperfect Foods SPC and Papa Inc.
    resurfaced as unjudged rows at the scheduled rebuild because the ledger
    exclusion of `cnet`, `imperfect-foods` and `papa-technologies-llc` runs before
    the identity merge (the Accel 2tor case). They were judged `not_member` in
    the delta batch and retired with a second, retire-only rebuild (no other row
    changed: 328 → 325). The rule "every slug of a merge group needs its own
    verdict when the canonical is not_member" should be applied *before* the
    scheduled rebuild, from the merge file, not discovered after it.
19. **West Co's legal entity** (agent, 2026-09-05). Workshop for Emotional &
    Spiritual Technology Corp (Form D, $29.16M, May 2024; Evan Sharp CEO,
    Christopher Stone CFO) is West Co — the press sweep's "Jan 2026 $29M seed"
    was the public reveal of that financing. Both rows are classified identically
    (Seed 2024, San Francisco, Consumer), the corp row carries `duplicate`, and the
    merge is queued for the next rebuild (`scratch/rebuild-queue.md`).
20. **Nomad's entry** (agent, 2026-09-05). Spark was an existing investor when
    Tiger led the $61M Series B (Aug 2023, ~$365M); the entry is the 2022 round
    with Stripes and Monashees — Growth 2022, below_1b (web-verified), replacing
    the pack's 2023 reading.

Ruling 14 addendum: **KIT digital** (KickApps' acquirer, 2011) and **Mandalay
Digital** (Mandalay Media's later name) are consideration rows under D7 and were
ruled `not_member` in the grind on the same basis.

## Post-close ruling, 2026-09-06 (Erik)

- **Rule A — vendor marks never band a row** (uniform for USV, Spark and every further investor; written into COLLECTION.md §7 valuation): a `1b_plus` band needs a priced round, tender or public float with a citable figure from the company, a filing or the press; PitchBook, CB Insights, Tracxn, Dealroom, Sacra, GetLatka, Contrary, Forge, Caplight, PremierAlts and UpMarket figures go to the note. Applied to nine rows (report.md addendum): six re-cited to the priced event, Capitolis re-dated, Justworks and MatX re-banded `below_1b`, Enfabrica's figure to the note. Supersedes the run's ruling 3 (aggregator figures at low confidence).
