# 8VC — investor-specific decisions

The rulings the judge cites per line for `8vc`. Not a restatement of
`data/collection/COLLECTION.md` §1 — its **derivation** for 8VC's facts, plus
the **deltas** the standing tests do not settle. Run issue: PRO-96
(sub-issue of PRO-87, Archetype A). Run opened 2026-09-06.

**Firm identity, verified at kickoff.** 8VC is the trading name of **Eight
Partners VC, LLC**, an SEC-registered investment adviser, CRD 283031 /
801-134666, principal office 907 South Congress Avenue, Austin TX, with one
other office (Pier 5, Suite 101, San Francisco, 16 advisory employees). Its
2026-04-16 Form ADV reports Item 5.F regulatory assets under management of
**$13,379,484,700** across 65 discretionary accounts, and a Section 7.B roster
of 65 private funds plus one advised by its single relying adviser. Founded
2015 in the breakup of Formation 8; first fund family filed under the legal
name (**Eight Partners VC Fund I, L.P.**, CIK 1667762), later ones under the
brand (8VC Fund II–VII).

---

## Part 1 — Derivations (no confirmation needed)

Each line is: the facts found, the test applied, the outcome, the precedent.
Listed in PRO-96 so they can be vetoed before kickoff; silence means they apply.

### D1 — The Formation 8 lineage: three sister firms, all external (T1) → `external`

**Facts.** Formation 8 was founded in 2011–12 by Joe Lonsdale, Jim Kim and
Brian Koo and raised two funds ($448M in 2013, $500M in 2014). It broke up in
2015 into three successors, and each successor registered separately:

| Successor | Adviser | Vehicles |
|---|---|---|
| **8VC** (Lonsdale) | Eight Partners VC, LLC — RIA, CRD 283031 | 8VC / Eight Partners funds |
| **Formation Group** (Koo, Asia) | — | Formation Group Fund I (CIK 1640249), Cayman Fund I, SPV Cayman |
| **Eclipse Ventures** (Lior Susan, hardware) | Eclipse — ERA 802-101492, Palo Alto | Eclipse Fund III, Continuity, Early Growth |

The legacy manager itself survives all three: **Formation8 Partners, LLC**,
CRD 163046 / **802-74921**, an exempt reporting adviser at 4962 El Camino Real,
Los Altos, filed its annual amendment on 2026-03-30. Its Schedule A still lists
**all three founders — Kim, Koo and Lonsdale — each as Managing Director,
ownership code C (25–50%) and each a Control Person**. Its Section 7.B carries
Formation8 Partners Fund I ($572,491,960 gross assets), Fund II
($1,226,530,550), Entrepreneurs Fund II ($37,279,786) and the F8 Bluelight /
Lumelight / Mindlight / Openframe SPVs. Its execution page is signed by Ian M.
Shannon, General Counsel; 8VC's is signed by Sallie S. Kim, CCO. **Not one
Formation8 vehicle appears in 8VC's Section 7.B.**

**Test T1** (same adviser: OUT for an entity with its own RIA or ERA, its own
fund family, or its own disclosure of independent operation). **Outcome:** every
Formation8, Formation Group and Eclipse vehicle is **`external`** — a separate
adviser, separately registered, jointly controlled, whose funds 8VC does not
advise. `config.json` `desks.classify[0]` matches all three by name, and the
external rule runs first. Precedent: Accel-KKR and IDG-Accel (own RIA / historical
JV), Lightspeed India and Lightspeed Faction (own ERA), Meritech.

One fact this does **not** decide, and it is Delta A below: Joe Lonsdale signs
**Formation8 GP, LLC**'s 13F-HRs as Managing Member from Austin (CIK 1835718,
2020–2024), so 8VC's principal still runs a legacy Formation 8 GP — and 8VC's
own site lists Formation 8-era companies as its portfolio.

### D2 — Kodiak, the relying adviser (T1) → `us`, in the base

**Facts.** 8VC files an umbrella registration with one relying adviser,
**Kodiak Holdings Capital Management, LP**, which sponsors **Kodiak Fund I,
L.P.** (CIK 2107620). Kodiak Fund I's Form D of 2026-03-05 declares
`industryGroupType: Pooled Investment Fund`, `investmentFundType: **Venture
Capital Fund**`, a $50,000,000 offering, and Joseph Lonsdale as Executive
Officer, filed from 907 South Congress Avenue, Austin — 8VC's own address.

**Test T1**, default IN for every sleeve of the one adviser and its relying
advisers; the **strategy-desk** addendum (Erik, 2026-09-04) does not fire,
because the sworn fund type is venture, not buyout, credit or real assets.
**Outcome: `us` desk, in the base.** Precedent: Thrive's relying adviser and
lettered LLCs; a16z's vertical fund families under one adviser.

### D3 — Sleeves, SPVs and the AI fund series (T1, T5) → in, at their entry

**Facts.** The 65-fund 7.B roster is one venture strategy expressed in many
wrappers: flagships (8VC Fund I–VII), Entrepreneurs Funds I–VII, Opportunities
Fund II, Co-Invest Fund I, Angel Fund I, an **8VC AI Fund I–VIII** series of
LLCs, Access / Allocate Access feeders, and ~30 four-letter single-company SPVs
(ADSF, ANSD, CHSB, EPSD, ERSB, LBSD, ORSE, PAIC, PSE, SESN, STSD, TSC …) plus
named ones (8VC Build Saronic SPV I/II, 8VC Build NRI, Anduin Opportunities SPV
II, 8VC HighLight II/III).

**Tests T1** (every sleeve of the one adviser is IN) and **T5** (positions moved
through plumbing stay rows through their original entries; a new commitment made
through such a vehicle enters at that stage). **Outcome:** every one of them is
a home-desk vehicle; the SPVs and Access feeders are plumbing, never rows, and an
SPV that funds a *new* commitment sets that row's entry stage. Precedent:
Lightspeed's Project Mercury; Creandum's Select funds and SPV TR; Thrive IX
Access as a third-party feeder (external) versus the firm's own feeders (in).

### D4 — 8VC Build: incubation and from-inception positions (T2, T3) → in

**Facts.** 8VC runs an incubation practice ("Build", 8vc.com/build) and names it
in its vehicles — 8VC Build Saronic SPV, 8VC Build Saronic SPV II / II-A, 8VC
Build NRI. Saronic, Base Power and other rows began as 8VC-built companies with
the firm's people on the founding cap table.

**Test T2** (fund money: IN where a fund of the firm held the position, whatever
the channel) and **T3** (venture entry). **Outcome:** an incubation is a member
where an 8VC fund held the position, exactly as Thrive's incubations including
pre-spin-out ones are. Where the position was held **from company formation**,
`entry_stage` is the first priced round the fund participated in; where the record
establishes no round at all, the row carries `stage_prior` at low confidence and
is reported. PRO-96 flags this as the Sutter Hill question in milder form: if the
taxonomy has no valid value for a from-inception position, that is a §9 trigger-3
contract question raised once at close, never an invented label.

### D5 — The advisors and fellows directories are people, not portfolio (T2, T5)

**Facts.** 8vc.com publishes **three** people namespaces: `/team/` (53 live
pages, the firm's own roster, with a site group per person — Investment Team 22,
Operations 11, Portfolio Support 8, Finance/Legal/IR 8), `/advisors/` (73 pages,
the *Advisor Upside* network: outside domain experts including Aaron Levie and
Ambassador Kenneth Braithwaite, who hold 8VC equity for advising portfolio
companies) and `/fellows/` (249 pages, the 8VC Fellowship — students and early
founders). robots.txt disallows `/advisors`, and the advisor pages render no
content server-side: the pull returns names only, recorded as a negative result
in `sources/site/advisors.json`.

**Tests T2** (OUT where the only connection is a person, a program listing or an
association) and **T5** (natural persons are not rows). **Outcome:** the roster
sweep is `/team/` only (`config.json` `roster.cdx_patterns`, plus the 2016
`/team-members/` alias). Advisors and fellows are **not** roster input and their
Form D related-person seats are not 8VC evidence. Precedent: the First Round
lesson — a people namespace holding a directory of outside founders poisons the
Form D sweep with filing-grade-looking false members; Lightspeed's Extreme
Entrepreneurs (no funding) and Accel's Atoms per-company test.

### D6 — Pre-2015 rows in a 2015-vintage book (policy constant) → no pre-window class

**Facts.** The base window opens 2006. 8VC's own first fund closed in 2016 and
its earliest archived listing is June 2016. Every entry the firm can claim in its
own name postdates 2015, and the oldest companies on its list (Addepar 2009,
OpenGov 2012) were entered by Formation 8 or by Lonsdale personally, which D1 and
Delta A govern.

**Outcome:** 8VC carries **no pre-window class**. `entry_stage` and
`seed_to_a_graduation` are expected at full fill with no `pre_window` flags, and a
`pre_window` flag on this base is a defect to investigate, not a policy null.
Precedent: the constant itself (Erik, 2026-09-07, on Lux); contrast Menlo and
Benchmark.

### D7 — Palantir is not a row (T2, T4) — **re-derived on corrected facts**

**Facts (corrected 2026-09-06).** The first version of this derivation asserted
that 8vc.com carries no Palantir page. That was wrong: **`8vc.com/companies/palantir`
exists on the live site** (Government & Defense, with the firm's own description)
and has 13 captures in the archive. Joe Lonsdale co-founded Palantir in 2003 —
twelve years before 8VC and eight before Formation 8 — and the firm's own content
cites it as founder track record. Palantir has been public (NYSE: PLTR) since
September 2020, so a fund position would appear on a 13F: **8VC GP I, LLC's 13F-HR
for Q2 2026 reports exactly one holding, Joby Aviation** — no PLTR, in that filing
or any other 8VC one.

**Tests T2** (OUT where the only connection is a person) and **T4** (whose money
sat behind the seat). **Outcome unchanged: `not_member`** — but on a different and
stronger basis. Not "the firm never listed it", which was false, but "no 8VC
vehicle has ever held it, and the connection is the founder's". Per §1 a wrong
fact re-derives under the same test; the flip is clean, recorded here and reported,
not escalated.

Palantir is therefore the oldest and most visible member of the Delta A class: a
row 8VC publishes as its portfolio that no 8VC fund bought. The same reading
applies to any company a partner founded before the firm's own fund backed it.
Precedent: the standing rule that companies founded by the firm's alumni that no
fund backed are out; Accel's Erasmic-era deals.

---

## Part 2 — Deltas (Erik confirms these, and only these)

### Delta A — The legacy book: 8VC lists Formation 8-era companies as its own

**The collision.** Two rules point opposite ways on the same rows.

*Out* — D1 above under **T1** and **T2**: Formation8 Partners, LLC is a separate
adviser, jointly controlled by three people, whose funds 8VC does not advise. A
company whose only position sits in Formation8 Partners Fund I or II was never
bought with 8VC fund money.

*In* — COLLECTION.md §1's evidence-sufficiency rule: **"a listing on the
investor's own site (any era) … suffices alone."** 8vc.com lists these companies
in its own `/companies/` collection, formatted exactly like every other row, with
no predecessor label anywhere on the page or the listing.

**The rows it moves.** Nine are on the live site today — **Addepar, Blend, Color,
Guardant Health, Illumio, Joby, OpenGov, Oscar, Wish** — and the archive adds
Formation 8-era names since removed (RelateIQ, acquired by Salesforce in July
2014, a year before 8VC existed; Zenreach, BuildZoom, Radius, Progressly, Castle
Global, Kiwi). Order of 10–20 rows, and they are disproportionately the book's
famous ones, so the ruling moves the published `$1B+` share and the notable-
investments list, not just a row count.

**The firm's own words, found after the delta was written.** The `/companies/`
list carries no predecessor label — but 8VC's own 2016 team page does. Joe
Lonsdale's bio there reads: "Most recently, he was a founding partner at
**Formation 8, the precursor fund to 8VC**, which manages over 1.5 billion USD"
(web.archive.org/web/20160627182109). The same bio lists his board seats —
"Addepar, OpenGov, Oscar, Illumio, Radius, Hyperloop-One and Wish" — as *his*,
which is T4's question answered by the firm itself. So this **is** the Redpoint
D5 shape after all: the firm's own surface distinguishes the predecessor book
from its own, just on a different page than the one that lists the rows. What
8VC has that Redpoint did not is a genuine continuity fact on the other side:
**Joe Lonsdale signs Formation8 GP, LLC's 13F-HRs as Managing Member from Austin
(2020–2024)**, so 8VC's principal still operates a legacy Formation 8 GP. That
is why this stays a delta rather than collapsing into a derivation.

**Recommended ruling (argued, for Erik to confirm or reject).** *Split the class
by fund money, not by era.* A legacy row is a **member** where an 8VC vehicle
took a position — a follow-on, an SPV, a secondary — and that is what the Form D
issuer histories, the 13F/13G filings and the 8VC SPV names are read for. A
legacy row whose only evidence is a Formation 8 round plus the 8VC site listing
is **`not_member`**, evidence class `site_listing`, basis: the position is
Formation8 Partners Fund I/II's and Formation8 Partners, LLC is a separate
adviser under T1. Rationale: T1 and T2 are the tests that define the base, the
site-listing rule is an *evidence-sufficiency* rule about how a membership claim
is proved, and where a firm's own list demonstrably includes another adviser's
positions the listing stops being sufficient — the same structural reading that
made Redpoint's D5 correct, reached through the filings instead of through the
page's wording. The alternative (take the site at face value) publishes
Formation 8 Fund I and II's track record as 8VC's, which is the defect the
membership definition exists to prevent.

**Either way**, every row in the class gets a recorded verdict with its
Formation-8-versus-8VC evidence written out, so the recall probe does not
re-find them and a later reversal is a re-run of one ledger class, not a
re-collection. The base ships under whichever ruling lands; if the ruling
arrives after export, the affected rows are re-judged and the base re-exported
before any ingest.

---

## Part 3 — Run-time standing rulings

Dated, class-wide, flagged for review. Raised once at the end with the results (§9).

*(none yet)*
