# Felicis — investor-specific decisions (PRO-94)

The derivation of the standing rule set (COLLECTION.md §1, T1–T5) for
Felicis's facts, plus the deltas those tests do not cover. This file is not a
restatement of the playbook; the judge cites its rulings per line.

Archetype A (US venture, SEC nexus on both sides). The shared derivation is
PRO-87's and applies unchanged; what follows is that derivation carried out
against **verified** Felicis facts, per §1's derivation protocol. Facts were
verified at kickoff on 2026-09-06, not taken as model priors.

---

## Part 1 — Derivations (no confirmation needed; §1 protocol)

**D-T1. One adviser, one desk, no partition.**
*Facts.* IAPD firm search returns **exactly one** registrant for "felicis":
FELICIS VENTURES MANAGEMENT COMPANY, LLC, CRD **162301**, SEC **802-74738**,
2460 Sand Hill Road Suite 100, Menlo Park CA 94025. The `802-` prefix makes it
an **exempt reporting adviser**, so no Item 5.F regulatory AUM exists and
Schedule D Section 7.B gross assets is the sworn substitute (§11, the First
Round / Creandum shape). EDGAR company search for "felicis" returns sixteen
filers and **all sixteen share that one address**: flagships Felicis Ventures
II (CIK 1493916), III (1548506), IV (1614817), V (1669524), VI (1745992),
VII (1805025), VIII (1875660), IX (1964181), X (2070105); the parallel and
employee vehicles Felicis Associates Fund VI (1746049), VII (1810544),
VIII (1884330) and Felicis Associates Focus Fund I (1884491); Felicis Focus
Fund I (1876390); Felicis Side Fund V (1672620); and the GP entity Felicis
Ventures GP II, LLC (1644840).
*Test.* T1, same adviser.
*Outcome.* **IN** for every one of those vehicles — flagships, Associates
parallel funds, Side Fund, Focus Funds and the GP entity. There is **no**
brand-sharing entity with its own RIA or ERA, so the Accel-KKR / Meritech /
Lightspeed India pattern PRO-87 requires each run to check for does not exist
here; that is a checked fact, not an assumption. There is no second geography
and **no non-venture strategy**, so neither the desk partition nor the
strategy-desk addendum applies, and `desks.partition` is empty.
*Precedent.* a16z (one adviser, many fund families, all IN); Creandum
(ERA-only firm, 7.B as the sworn AUM substitute).

**D-T1a. No Fund I on EDGAR is a coverage fact, not a boundary question.**
*Facts.* The vehicle ladder starts at Felicis Ventures **II** (first filing
2010). Felicis was founded in 2006 and its first years were Aydin Senkut's
angel and first-fund era, below the electronic Form D window.
*Test.* T1 (the vehicles are the adviser's), read with the §1 policy constant
that the base window opens 2006.
*Outcome.* The 2006–2009 book is **IN scope** and is carried by the
felicisventures.com captures, which are its only first-party record. It is
**not** carried by Form D, so those rows will be `site_listing`-classed and
the report states the coverage regime rather than blending it (PRO-94's
second delta, below).

**D-T2. Fellows, VC Fellows and Scholars are not membership.**
*Facts.* felicis.com/fellows runs three programs: AI Fellows (a week-long
student programme awarding "non-dilutive cash prizes"), VC Fellows (a campus
community and education programme, no capital) and Scholars ("$200,000 for
two years" as a **research grant** to named AI researchers, with
commercialisation support only as a later possibility).
*Test.* T2, fund money.
*Outcome.* **OUT.** None of the three deploys a fund position: a prize and a
non-dilutive research grant are not investments, and a programme listing is
not evidence under T2 in any case. A fellow's or scholar's company enters the
base only where a Felicis **fund** later held a position, on that position's
own evidence.
*Precedent.* Lightspeed's Extreme Entrepreneurs (no funding, OUT); Accel
Atoms (IN only per cohort company where Accel money was deployed).

**D-T2a. The angel-era book is IN where a Felicis vehicle held it, OUT where
it was Aydin Senkut's personal position.**
*Facts.* Felicis presents its own history as beginning in 2006, and the
2006–2010 felicisventures.com portfolio pages are published by the firm under
the firm's name.
*Test.* T2, fund money, read with the §1 evidence rule that a listing on the
investor's own site (any era) suffices alone.
*Outcome.* **IN** for every company on the firm's own 2006–2010 portfolio
pages: the firm published them as its portfolio, which is site-listing
evidence. Positions evidenced **only** as Senkut's personal angel cheques,
never listed by the firm, are **OUT** under the partners'-personal-angel-book
precedent (Kushner; Cherry's founder-angel positions).
*Precedent.* First Round D-T2a (the founders' pre-firm angel book, which the
firm itself published separately, excluded) — note the **inversion**: First
Round's firm published that book as *"investments made prior to First Round
Capital"*, i.e. explicitly not the firm's; Felicis publishes its 2006-era
rows as the firm's own portfolio with no such disclaimer.

**D-T3. Venture entry; one common-stock row; no control practice.**
*Facts.* The fund ladder is nine flagships plus side, focus and associates
sleeves — all venture. The firm runs **no** buyout, credit or public-equities
practice, so the control-position addendum has nothing to reach. The live CMS
carries one row at stage **"Common"** (The Climate Corporation, acquired by
Monsanto in 2013), against 129 Seed, 99 Series A, 34 Series B and 14 Series C.
*Test.* T3, venture entry.
*Outcome.* Primaries, follow-ons, secondaries and tenders **IN**, tenders and
secondaries as Growth. A position first appearing as a public-market purchase,
a 13F holding or a post-IPO 13G is **OUT**. The single "Common" row is a
common-stock position in a private company; it is IN as a venture entry, and
its `entry_stage` is **Growth** by the secondaries rule unless the record
names an earlier priced round Felicis joined.

**D-T4. Standard person-level attribution and seat dating.**
*Facts.* The roster is 109 people across the archived `/team/` namespace and
the live CMS (2011–2026), with real churn.
*Test.* T4, person or firm.
*Outcome.* Standard: a Form D related-person name-match never suffices alone;
a seat is dated against the person's firm **at filing time**, not against the
roster; Section 16 filings by a natural person locate the person, never a firm
position. Name-match rows are judged cluster-first.

**D-T4a. The `/founder/` namespace is a portfolio-founder directory and is
never swept.**
*Facts.* felicis.com carries **two** people namespaces: `/team/<first-last>`
(113 archived slugs, the firm's own people) and `/founder/<first-last>` (153
archived slugs — Aaron Patzer, Adrian Aoun, Aza Raskin, Auren Hoffman, Brad
Gerstner and so on), a directory of the founders Felicis backed. The live
Sanity CMS carries the same shape as 620 `founder` documents.
*Test.* T4, and §5.2's First Round rule.
*Outcome.* `roster.slug_re` is constrained to `/team/`, so the directory
cannot reach the Form D sweep. This is the First Round trap in its **cleanest**
form: there the two lived in one namespace and only a case rule separated
them; here they are separate paths, so no case rule is needed. A founder is a
related person on their own company's Form D, so sweeping them would confirm
hundreds of false members with filing-grade-looking evidence.
*Read the other way round, the directory is a first-party company list* and is
pulled deliberately as a recall layer, never as roster evidence.

**D-T5. Standard operating-company test.**
*Outcome.* Fund vehicles, SPVs, feeders, fund-shaped list entries, tokens with
no issuing organisation, filter labels, scrape artifacts and natural persons
are not rows. Two scrape-artifact classes are expected on this book
specifically and are handled at parse time, not by the judge: the 2008–2010
ASP.NET captures carry **injected comment spam** ("buy valium" anchors), and
the 2011–2019 WordPress era is **logo-only**, so a mis-anchored pattern would
publish theme asset names as companies.

---

## Part 2 — Deltas for Erik

PRO-94 lists three, each flagged there as "a model prior to verify at kickoff,
not a finding". All three were verified against the run's own evidence at
kickoff. **None of them turned out to need a ruling**: each is a property of
the base that changes how the run reports, not a boundary question that
changes what is in it. They are recorded here as confirmed facts, and the
run proceeds under them per the protocol's "silence means they apply".

**Δ1 — Non-US rows: CONFIRMED, smaller than expected on the live surface.**
The live CMS states an HQ for only 50 of 277 rows, of which seven are non-US:
Amsterdam (Adyen), Sydney (Canva), Ottawa (Shopify), Dublin, Berlin, Finland,
and one literal "Global". The true non-US share will be larger once the judge
fills `hq_country` on the rest. The two Creandum policy constants therefore
bind on an archetype-A base as PRO-94 predicted: **ECB reference rate on the
figure's own date** (Adyen is Euronext-listed in EUR — a large public row that
cannot take a `sec_public_float`), and **a web-cited market cap for any
listing outside SEC registration**. Neither is new machinery. No ruling needed.

**Δ2 — Partial Form D visibility: CONFIRMED and structural, with a second
cause PRO-94 did not name.** Coverage is uneven for two independent reasons,
not one. (a) Non-US portfolio companies file no Form D, as PRO-94 says.
(b) **The 2006–2009 book predates the firm's own first EDGAR vehicle**
(D-T1a): there is no Felicis Ventures I, so the angel-era rows have no
fund-side filing either. The report therefore breaks coverage down **by
evidence regime** — pre-2010 site-only, US Form D era, non-US — rather than
publishing one blended number. No ruling needed.

**Δ3 — Multi-stage entries: CONFIRMED by the firm's own data.** The CMS's own
per-company stage field is Seed 129 / Series A 99 / Series B 34 / Series C 14
/ Common 1 — genuinely broad, so a narrow published distribution would be the
signal to re-check that PRO-94 describes. Recorded as an expectation to test
the landed distribution against, not as a label: **the field is scored on the
golden set before the grind may use it** (§4), and this note is not a licence
to trust it. No ruling needed.

---

## Part 3 — Run-time standing rulings

Dated, class-wide, flagged for Erik's review. Added as the run makes them.

**R1 (2026-09-06) — The CMS `stage` field and the archived `circles` ladder
are two independent first-party entry-round claims, and both are scored
before either labels.** Felicis publishes its entry round twice: the live
Sanity `stage` reference (all 277 rows) and, on the 2011–2019 WordPress
listings, a `<p class="circles">` per company naming **every round Felicis
joined** ("Seed a b", "a b c", "c"), whose first element is the entry. §4
requires a candidate layer to be scored against the golden set before the
grind trusts it, and §6 records the precedent both ways: Accel's CMS label
scored 30/31 and was promoted to class 1, Accel's own *socure* class showed a
CMS describing the company when listed rather than the deal. Both layers are
therefore measured blind on the stage golden set, and each is promoted or
demoted on its own score. Where they disagree with each other or with the
record, **the label follows the record** with `stage_disputes_band` and a
citation.

**R2 (2026-09-06) — Operator Venture Partners are firm people whose own
executive filings are not firm positions.** Felicis's team CMS has a real
group taxonomy (Investors 12, Venture Partners 9, Finance 9, Operations 8,
Founder Success 6), and the Venture Partner tier is drawn from operators who
run or ran portfolio companies: Harley Finkelstein (President of Shopify),
Thijn Lamers (Adyen), Alex Stamos, Sonia Arrison, Jack Abraham (Atomic),
Javier Soltero (Acompli). Two consequences, both class-wide. First, §5.2's
`site_team_groups` constraint applies and is set to Investors + Venture
Partners; Finance, Operations and Founder Success staff are dropped from the
swept roster, and because a person's group is a fact about the PERSON it
drops their archived `/team/` slugs too (Ryan Thompson 29 sweep rows, Beth
Steinberg 8, Tyler Wilson 6). The sweep went from 101 names / 477 accessions
to 78 / 442. Second, an operator Venture Partner is a related person on their
OWN company's Form D by virtue of running it, so that filing locates the
person's executive seat and never a Felicis position — the T4 question "whose
money sat behind the seat" answers *the company's own*, not Felicis's. Rows in
this class must rest on the site listing or the round's press, and two of them
(Shopify, Acompli) are in the trap set precisely because the right verdict is
`member` for the wrong-evidence reason.

**R3 (2026-09-06) — Gate result: the evidence order for `entry_stage`.**
Both first-party layers were scored blind against the 18-row stage key
(golden.json), mapped into the published taxonomy first:

- **circles ladder — 5/5**, and it won the one diagnostic row outright.
- **CMS `stage` enum — 17/18 (94%)**.

The single CMS miss decomposes cleanly and is the known failure mode, not
noise: Ginkgo Bioworks reads `Seed` in the enum, but the seed was Y
Combinator's (S14) and Felicis entered at the $9M Series A of March 2015. The
enum is describing **the company's stage when it was listed**, which is
Accel's *socure* class in §6 — and the circles layer, which records the rounds
Felicis actually joined, is immune to it by construction. Across the full
57-company overlap the two layers agree on 54.

Evidence order for the grind, in force from here:

1. Both layers present and agreeing → **class 1**, publishes.
2. Circles only → **class 1** (the firm's own record of the rounds it joined).
3. CMS only → **class 1 at medium confidence**, with §8's guard live: a $1B+
   or post-2020 row goes back through the judge with the press check rather
   than past it, because this is where the socure class hides.
4. Layers disagree → **neither labels**. The row is judged with a citation
   attempt and carries `stage_disputes_band` where it overrides. Three rows
   are in this state (BrightRoll, Ginkgo Bioworks, Opendoor); Ginkgo is
   already settled by the key, the other two are in golden.json `unresolved`.

**R4 (2026-09-06, RAISED FOR ERIK — does not block the run) — the 2006-2009
angel era is published as member under D-T2a, and the fact that decided it is
newly verified.** Felicis was founded in 2006, but the record now says Aydin
Senkut "began angel investing in 2005" and "raised the firm's first
institutional fund in 2010" — which the EDGAR ladder corroborates exactly, as
the first vehicle to file is Felicis Ventures **II** in 2010 and no Fund I
files at all. So for roughly four years the capital behind the Felicis book
was its founder's own. That satisfies **two standing tests with opposite
outcomes**, which is the §1 definition of a delta rather than a derivation:
T2 asks whether a fund of the firm held the position and the answer is no,
while §1's evidence rule says a listing on the investor's own site in any era
suffices alone — and Felicis published these companies as its portfolio, on
its own domain, under its own name, and still counts them in its public track
record.

This run publishes them as **members**, on the reading that a solo-GP firm
deploying its founder's capital through its own branded vehicle is the firm,
not a partner's personal angel book taken on the side while employed
elsewhere (Kushner; Cherry's founder-angel positions). The nearest precedent
cuts the other way on its facts and confirms the distinction: First Round's
D-T2a excluded its founders' pre-firm book **because the firm itself published
it separately** as "investments made prior to First Round Capital". Felicis
makes no such separation.

It moves a class of rows (roughly 50-80 across the 2006-2010 captures,
including Mint, Meraki, Dogster, Freewebs and BrightRoll), so it is raised
under §9 trigger 2 rather than settled here. The base ships with them IN and
the report names them, so reversing it is a re-export and not a re-run.

**R5 (2026-09-06) — the Wikidata `hq_country` layer is demoted to
corroboration for single-token names, and every value it wrote is re-judged.**
`prepare` filled `hq_country` on 226 rows, of which 104 came from Wikidata,
and the split is stark: **all 14 multi-token labels are right** (Clear Labs,
Guardant Health, Warby Parker …) while the **90 single-token labels are wrong
at a rate no layer survives** — Gusto→Netherlands, Wish→Japan, Guild→Japan,
Cedar→Japan, Planet→Greece, Mercor→Latvia, Alloy→Australia, Chalk→Czech
Republic, Proton→Ukraine (that is Proton AG, the Swiss privacy company),
Karma and Milo→"Czechoslovakia" (not an ISO code, and not a state), and
Survios→a raw `wikidata.org/.well-known/genid/…` URL. This is exactly the
First Round finding, on a book even more exposed to it: Felicis names its
companies Key, Origin, Sphere, Stream, Arena, Feel, Depot, Condor.

The failure is silent in the way §8 warns about — `prepare` fills the column,
the queue then asks only about EMPTY fields, and the row never reaches the
judge. So the demotion is not enough on its own: **every Wikidata-written
country is re-judged and disputed on the row with `model_disputes_source`**,
which is §8's one licensed exception to "emit only the keys the queue asked
for". Where the company cannot be identified the row takes the US desk prior
at low confidence with `country_prior`, never a silent Wikidata value.

**R6 (2026-09-06) — 43 slug artifacts are fixed in the parsed source, not by
merging.** The base carried 44 rows whose slug is a file name rather than a
company: the 2007-2010 logo eras publish identity as the image file
(`bumplogocurrent2`, `justintvlogo`, `midomi-small`, `optrip-logo-small`,
`loomia-latest`, `dogster-new-2`), and the current Sanity CMS re-creates a
company document with a disambiguator that is sometimes a raw UUID
(`disco-2-0e261ea1-b126-4fb0-9346-e0faee3720f5`, `walnut-2-<uuid>`,
`xilis-2-<uuid>`). Left alone the base publishes a row named "Dig 2 7869de28
2b5e 4634 A24a C5a487f3a955".

§5's First Round rule says the fix belongs in the parsed sources rather than
in `identity-merges.json`, "because a merge keeps the junk name on the
surviving row" — and here that matters twice over, since for most of these the
canonical row does **not** separately exist, so the correction is a RENAME
that gives the company's only row its real name. `scratch/fix-slug-variants.py`
carries the curated map, keyed case- and separator-insensitively. Three are
deliberately left unresolved and reported rather than guessed:
`go-2-<uuid>` (the base holds both `go-maps` and `go-insurance`, and the UUID
row could be either) and the two-letter logo files `pf-logo` and `rr-logo`.
`room-77` is a real company name that merely looks like a variant.

**R7 (2026-09-07) — site chrome parsed as portfolio companies.** The 2011
`/portfolio/` capture renders the site's SOCIAL FOOTER through the same
`images/logos/` path as its portfolio cards, so `linkedin.png`, `groupon.png`
and `twitter-small.jpg` were parsed as companies and published as Felicis
positions. This is §5's First Round class — "the same page carries marks that
are not members" — in a form the playbook does not name: not acquirer logos
beside exits, but the site's own chrome. The discriminator is exact and is now
in the era pattern: portfolio cards carry a **relative** `src`
(`/wp-content/themes/felicis/images/logos/...`) while the chrome carries an
absolute `http://www.felicisvc.com/...` host. The three rows are removed from
the parsed source rather than ruled `not_member`, because they were never
companies; `scratch/fix-slug-variants.py` records them under `REJECTS`.
Checked across every listing year: 2011 is the only affected capture.
