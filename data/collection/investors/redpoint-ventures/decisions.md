# Redpoint Ventures — investor-specific decisions (PRO-90)

The derivation of the standing rule set (`../../COLLECTION.md` §1, tests T1–T5)
against Redpoint's own facts, plus the deltas those tests do not cover. The
judge cites the rulings here per line. Everything in §1 binds unless a
confirmed delta below says otherwise.

**Membership definition** (unchanged): a row belongs in the base iff a firm
representative, acting on behalf of the firm, made an investment with fund
money in it, and it is a venture-outcome operating company.

---

## Part 1 — Derivations (no confirmation needed; §1's derivation protocol)

Each line: the facts found, the test applied, the outcome, the precedent.
Facts are verified at kickoff, not model priors. A wrong fact re-derives under
the same test and is recorded here, not escalated.

### D1 — One adviser, every sleeve (T1) → IN

**Facts.** `Redpoint Management, LLC`, doing business as **Redpoint Ventures**,
is an **exempt reporting adviser**: CRD **161680**, SEC file **802-75525**,
principal office 2969 Woodside Road, Woodside CA (annual amendment filed
2026-04-01, `sources/registers/adv-161680.pdf`). IAPD carries no second
Redpoint adviser under that brand. The ADV's Item 1.D(3) CIK list and its
Schedule D Section 7.A related-person list together name exactly the
Redpoint Ventures III–X and Redpoint Omega I–V general-partner LLCs plus the
lettered Omega co-invest vehicles (III-MC, IV-C, IV-F, IV-I, IV-R, IV-Y), each
an exempt "venture capital fund adviser" under common control. EDGAR's
name search returns the matching fund L.P.s — Redpoint Ventures I–X, Redpoint
Omega I–V, Redpoint Omega Entrepreneurs Fund IV and V, Redpoint Ventures VII
Annex Fund, Redpoint Technology Partners A-1 and Q-1, Redpoint Associates
I–IV — all filing from 3000 Sand Hill Road, Menlo Park (1999–2022) or 2969
Woodside Road, Woodside (2022–).

**Test T1** (same adviser). **Outcome: all IN, one desk (`us`).** The early
funds (Ventures I–X), the growth sleeve (Omega I–V), the entrepreneurs' and
annex vehicles and the lettered co-invest LLCs are one adviser's fund
families. Precedent: a16z's crypto / bio / games families under one adviser;
Thrive's umbrella with its lettered LLCs; Creandum's flagship, Select and SPV
vehicles.

**No non-venture strategy exists**, so the strategy-desk addendum does not
bite. `Redpoint Management, LLC` (CIK 1689508) does file **13F-HR** reports
from 2022, but a 13F reports post-IPO holdings of positions the venture funds
already hold; it is not a public-equities strategy and it is never membership
evidence (T3, below).

**Namesakes ruled external on the entity registry** (address-checked, not
name-checked): Redpoint Bio Corp (NJ), Redpoint Global Inc (MA), REDpoint
International (WA), Redpoint Investment Management Pty (Australia), Redpoint
Partners LP (c/o Kern Capital Partners, Madison NJ), Redpoint Storage Partners
LLC (Camarillo CA, a self-storage syndication), Redpoint Investment Advisors
and Redpoint Asset Management (IAPD, unrelated).

### D2 — Redpoint China (T1) → the post-2015 vehicles are OUT; the home funds' Chinese positions are IN

**Facts.** Redpoint began investing in China in 2005 as **its own effort**: the
firm's site carried a `/redpoint-in-china/` page ("At Redpoint, our interest
in China began through our extensive experience with consumer Internet,
wireless and semiconductor components companies"), and Chinese companies sat
**undifferentiated in the firm's own portfolio table** — AMEC, 51.com,
Innofidei, iDreamSky, Qihoo 360, Trip.com are in the 2007–2012 listing, and
the live CMS still carries 17 rows located in China. The China team **spun out
in 2015** and raised its own funds from 2016 (TechCrunch, 2019-01-17; Forbes,
2019-01-20), operating as `rpvchina.com` under **ACE Redpoint Management
Company, Ltd.** — a separate adviser, IAPD CRD **288086**. Redpoint
Management LLC's 2026 ADV names no China entity in Item 1.D or Section 7.A,
and EDGAR carries no Redpoint China filer.

**Test T1.** **Outcome:** post-spin-out Redpoint China vehicles are a
brand-sharing entity with its own adviser and its own fund family →
**OUT (`external`)**. Positions a **home fund** took in Chinese companies
before the spin-out — the ones the firm lists on its own surfaces — stay
**IN**: the vehicle was a home fund, which is what T1 asks. Resolve per
vehicle by CRD or CIK, never by the brand that announced the deal.
Precedent: HongShan / Peak XV, Lightspeed China, Lightspeed India.

**Operational consequence.** No desk partition is configured, because no
Redpoint China vehicle files with the SEC and none can therefore reach the
entity registry. The separation is carried by the layers themselves: the home
firm's own listing surfaces stop carrying new Chinese rows after the spin-out,
and a Chinese company whose only evidence is `rpvchina.com` is `not_member`
with this ruling cited.

### D3 — The crypto slice (T1, T5) → IN, with the token rule binding

**Facts.** The firm's own sector vocabulary carries **Blockchain** (8 live
rows: Alchemy, BitGo, Dune Analytics, Mysten Labs, Offchain Labs, XMTP,
Scale3, Dragonfly). No crypto-specific vehicle exists on EDGAR under the
firm's name; IAPD carries no crypto adviser for it; the ADV names none.

**Test T1** → there is no separate registration, so crypto positions are home
fund positions, **IN**. **Test T5** then binds unchanged: a listed token
position is in only when it maps to an operating or issuing organisation, and
where a token and its company are both listed they are one row under the
company. Precedent: a16z's crypto family under one adviser; the standing
token rule.

### D4 — Redpoint eventures, the Brazil joint venture (T1, T2) → the JV vehicle is OUT; a listed row is judged on whether a home fund held it

**Facts.** "Redpoint eventures" is a co-branded joint venture with e.ventures,
formed 2012 for Brazil. **No eventures entity appears** in Redpoint
Management LLC's ADV Item 1.D CIK list or Section 7.A related persons.
`eVentures Growth, L.P.` (CIK 1611943, Form D 2014) is **e.ventures' own**
vehicle: its related persons are Mathias Schilling and Thomas Gieselmann at
600 Montgomery Street, San Francisco, with no Redpoint person on the filing.
Redpoint's live site nevertheless lists three Brazilian rows as its own —
Nubank ("We first partnered for their Series D in 2016"), Viajanet ("their
Series A in 2010") and Xango.

**Test T1** on the vehicle: the JV's funds are not under the home adviser →
the JV **as a vehicle is external**. **Test T2** on the row: where a home fund
held the position, the row is IN, and the firm's own listing plus a dated
entry claim is the seed evidence. **Outcome:** the three listed rows are
judged individually, with the exit-side EDGAR full-text sweep (Nubank is
NYSE-listed and files) as the corroboration. A row whose only support is the
JV's participation is `not_member` with this ruling cited.

### D5 — "Previous Investments by Redpoint Partners" (T2, T4) → not_member

**Facts.** Redpoint was founded in 1999 by partners from **Brentwood Venture
Capital** and **Institutional Venture Partners**. Its own first site
(2000–2002) renders the portfolio in **two labelled sections**: *Current
Investments* (19–31 rows, the firm's own logo table with description,
location and status) and **"Previous Investments by Redpoint Partners"**
(57 text names in the November 2000 capture: 3Com, Ask Jeeves, Bay Networks,
Documentum, Excite, FileNet, Foundry Networks, Juniper Networks, NetFlix,
Polycom, Sybase, TiVo, WebTV Networks and the rest). The 2002–2006 CMS keeps
the same split (`oid=152` current, `oid=157` previous). The partners' own
bios say whose deals those were: "Prior to founding Redpoint, Geoff was a
general partner with IVP … He was responsible for **the firm's** investments
in Ask Jeeves, Excite, Foundry Networks, Juniper Networks, MMC Networks, TiVo
and Wellfleet" — "the firm" there is IVP.

**Tests T2** (fund money: OUT where the only connection is a person) **and T4**
(whose money sat behind the seat on that date). **Outcome:** a row whose only
evidence is the "Previous Investments by Redpoint Partners" section is
**`not_member`** — it is a founding partner's predecessor-firm track record,
not a Redpoint fund position. A row is IN where a Redpoint fund took a
position, including a follow-on into a company first backed at Brentwood or
IVP; the current-investments table, the fund vehicles' own filings and the
later eras are that evidence. Precedent: Accel's Erasmic-era India deals with
no Accel listing; the standing rule that companies founded by the firm's
alumni that no fund backed are out.

**This is the one place where the "a listing on the investor's own site
suffices" rule must not be applied mechanically**: the firm's own page is
explicit that the section is a *predecessor* book, so reading it as a
membership claim would contradict the page. The section is preserved in
`sources/web/previous-by-partners.json` and every name in it gets a recorded
`not_member` verdict, so the recall probe does not re-find it as a miss.

### D6 — Pre-window entries (policy constant) → in the base, columns null

The base window opens **2006**. Redpoint is a 1999-vintage firm, so a large
share of the base entered before the window: those rows are members with
`entry_stage` and `seed_to_a_graduation` null by rule, and the report says what
share they are. Precedent: Benchmark (1995 vintage, 284 members).

### D7 — Standing rules applied unchanged

Fund-shaped list entries, token positions, and post-RIA public or secondary
purchases with no venture entry (T3) all apply as written in §1. The firm's
13F-HR filings (CIK 1689508, from 2022) are the concrete case for the third:
a 13F holding is never membership evidence and never an entry.

---

## Part 2 — Deltas (Erik confirms these, and only these)

**None raised at kickoff.** Every question the issue flagged — the sleeves,
the China independence check, the crypto vehicle, and the Brazil JV found
alongside them — resolved on the sworn record under T1 and T2 (D1–D4), and
the predecessor-book question resolved under T2 and T4 (D5). The derivations
above are listed so they can be vetoed; silence means they apply.

Open questions that arise **during** the run are recorded in Part 3 and raised
once, at the end, with the results (§9).

---

## Part 3 — Run-time standing rulings

Dated, class-wide, flagged for review. Each was made during the run under the
tests above, recorded here, and raised in `report.md` §7.

**R1 (2026-09-06) — the previous-by-partners rule is evidence-based, not
mechanical.** D5 says a row appearing only in "Previous Investments by Redpoint
Partners" is `not_member`. The operational form: a row leaves the base only when
it appears in NO current-investments section of any era AND carries no Redpoint
fund filing and no announcement. Santera appears in both sections and stays a
member on the current listing; 60 rows appear only in the previous section and
left. Four rows (Ask.com, Concur, Juniper, MMC Networks) appear only in the
previous section of the old site but are claimed by the LIVE site and were kept
as members, flagged `identity_uncertain`, pending Erik's ruling.

**R2 (2026-09-06) — a logo-only era names its rows from the company's own
domain.** The 2002-2006 site rendered every company as an image with no alt
text. Rather than leave the decade unparsed, `scratch/build-early-eras.py` reads
the company URL out of the anchor that wraps the logo and names the row from its
host, then joins on that host across eras to adopt whichever surface renders a
name. On an ACQUIRED row the logo's anchor points at the ACQUIRER, so the URL is
recorded as `acquirer_url` and never names the company.

**R3 (2026-09-06) — a deterministic pre-fill on a key the queue did not ask
about may still be disputed.** Twenty rows carried wrong Wikidata or public-float
values on `status` and `hq_country` — keys absent from their `need` list, so the
queue never put them to the judge. They were flagged `model_disputes_source` in
the grind and corrected in a dispute pass before verify. Proposed as a §8
write-back.

**R4 (2026-09-06) — the firm's own announcement archive is a ceiling, not a
label.** Scored on the golden set: four of 34 key rows had their earliest
announcement postdate the entry (LifeSize listed 2003, announced at its 2004
Series B). The archive cites and dates a round; it never labels an entry alone.

**R5 (2026-09-06) — a merger of two portfolio companies is one row.** Couchbase
arrived as a recall-probe addition, but Membase — already a member — is the
company that merged into it. Under T5 a position that moves through plumbing
stays a row through its original entry, so Couchbase is `not_member` as a
duplicate identity and the Couchbase outcome is written onto the membase row.
