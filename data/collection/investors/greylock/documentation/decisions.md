# Greylock Partners — investor decisions

Derived from the standing rule set in `data/collection/COLLECTION.md` §1 under
the derivation protocol: **derive, and confirm only the delta.** The judge
cites a line from this file per ruling. Run: PRO-89, kicked off 2026-09-07.

Firm facts verified at kickoff (not model priors):

- Legal name **Greylock Management Corporation**, business name **Greylock
  Partners**, CRD **161537**, SEC file **802-74573**, an **exempt reporting
  adviser** (no Item 5.F RAUM; Section 7.B gross assets are the sworn
  substitute, §11). Principal office 140 New Montgomery Street, Suite 2600,
  San Francisco. ADV annual amendment filed 2026-03-31.
- 57 EDGAR filer entities carry the word; 39 resolve to the home desk
  (`entities.json`). The venture partnerships run Greylock Ltd Partnership,
  Greylock Ventures, Greylock Capital LP, Greylock Investments LP, Greylock
  Equity, Greylock IX through XIV with their -A and GP entities, and Greylock
  15 through 18 with -A and Principals vehicles, plus Greylock Discovery Fund
  LLC and Greylock Management Corp.
- Founded 1965 (Bill Elfers, Dan Gregory, Charlie Waite), Boston. Live site
  lists 158 companies; the 1999 archive says "some of the 250 companies we
  have helped build … over 105 … publicly held … another 80 … merged".

## 1. Derivations (no confirmation needed; vetoable before kickoff)

| # | Category | Facts found | Test | Outcome | Precedent |
|---|---|---|---|---|---|
| D1 | Fund families and sleeves | One ERA (CRD 161537) over Greylock I–XVIII, the -A parallel funds, the Principals/Discovery vehicles and the GP entities; one filing address per era (One Federal Street Boston → 880 Winter Street Waltham → 2550 Sand Hill Road → 140 New Montgomery Street) | T1 | **IN** — every numbered fund, -A parallel, Principals and Discovery vehicle | a16z's crypto/bio families; Thrive's lettered LLCs |
| D2 | Greylock Israel | **GREYLOCK ISRAEL GLOBAL MANAGEMENT LTD. has its own exempt reporting adviser registration, CRD 162176, SEC file 802-75092** — a separate registration from CRD 161537, not a relying adviser on it. GREYLOCK ISRAEL L P (CIK 1370903) files from Ugland House, Grand Cayman | T1 | **OUT** | Lightspeed India (own ERA and separate disclosure); Lightspeed Faction (own RIA) |
| D3 | 83North | 83North is the 2015 rebrand of the Greylock Israel practice as an independent firm; **83NORTH MANAGEMENT, LTD. (CRD 283471) and 83NORTH 2017, LTD. (CRD 294729) hold their own registrations**, and 83North II LP / GP / Manager file separately | T1 | **OUT** | HongShan and Peak XV; IDG-Accel China |
| D4 | Greylock Capital Management (New York) | A different firm — Hans Humes' distressed-debt and emerging-markets manager, CRD 137825, with its own relying adviser and its own fund family (Greylock Global / Emerging Markets / Distressed Debt / Global Focus) | T1 | **OUT** — namesake, not a desk | Accel-KKR (own RIA) |
| D5 | Other namesakes | Greylock Investments SLP (Aztec Group House, St Helier, Jersey; related persons Richard Phillips, Liam Jones), Greylock Ventures LP – IAI-1 Series (Burlington MA; GP "Greylock Ventures GP LLC – Series IAI-1"; related person Donald Sullivan), Greylock Marketing Inc and Greylock Inc (Florida) — no address, person or fund overlap with CRD 161537 | T1/T5 | **OUT** | Menlo's namesake list |
| D6 | Scout checks, angel books, programs | No scout program or accelerator is disclosed; partners' personal board seats appear on Forms 3/4 | T2 | **OUT** where no fund of the firm held the position | Ruled on Sequoia, a16z, Accel, Lightspeed; Cherry's founder-angel positions |
| D7 | Secondaries and tenders | No dedicated crossover or public vehicle in the registry; the Discovery Fund is a venture vehicle | T3 | **IN** as Growth entries; positions first appearing as 13F holdings or post-IPO 13Gs **OUT** | The standing post-RIA rule (§1) |
| D8 | Control positions | No buyout or credit strategy under CRD 161537; the 1999 site's "management buyouts and recapitalizations" page is the 1980s–90s book and each such row is tested individually | T3 | **OUT** where the firm and its co-investor group take 50%+ or the company reports a change of control; `excluded.json` reason `control_position` | Erik, 2026-09-04 |
| D9 | Seat dating and person attribution | Greylock partners move (Aneel Bhusri to Workday as CEO; Reid Hoffman's LinkedIn and OpenAI seats; David Sze, Asheem Chandna, Josh Elman) | T4 | Standard: a seat is dated against the person's firm at filing time, never against the roster | Accel's Jonathan Turner; Ethan Choi at Khosla |
| D10 | Fund-shaped and token rows, scrape artifacts | The archive eras yield logo-filename slugs (`accel-chip`, `athoc_65`) and nav junk | T5 | Standard: fund-shaped entries `not_member` until identified; artifacts filtered in `non_company_slugs` | a16z rulings 6–7 |

## 2. Deltas (Erik's call)

**None raised at kickoff.** PRO-89's three delta candidates all resolved under
a standing test against verified facts, so each is a derivation above, not a
delta:

- *"Check Greylock Israel and any separately advised affiliate under T1 on
  IAPD by CRD"* — done, and it resolves cleanly: D2 and D3. This is the
  Lightspeed India pattern, ruled by the test.
- *"Founded 1965, so a large slice lands pre-window"* — a policy constant, not
  a ruling. **The constant moved after PRO-89 was written**: COLLECTION.md §1
  now reads (Erik, 2026-09-07, on Lux) that a pre-window entry carries the
  best-supported `entry_stage` at low confidence behind a `pre_window_entry`
  flag rather than a null. The issue's text ("entry_stage and graduation
  null") is the older rule. This run follows the playbook: graduation null,
  `entry_stage` filled and flagged. Reported, not escalated.
- *"A long-running site with many eras … check for a pre-rebrand domain"* —
  done: greylock.com carries every era from 1998 to 2026, no pre-rebrand
  domain exists, and six markup eras are configured.

## 3. Run-time standing rulings

*(dated, class-wide, flagged for review — added as the run makes them)*

- **R1 (2026-09-07) — a "Greylock Capital" vehicle is home or namesake by
  ADDRESS, never by name.** GREYLOCK CAPITAL LIMITED PARTNERSHIP (CIK 940543)
  files a 1997 13G/A from One Federal Street, Boston — Greylock's own office —
  while Greylock Capital Management LLC (CRD 137825) is the unrelated New York
  manager. The first desk pass classed the Boston fund `external` on the
  shared word and would have dropped its 13G subject from the base. Class-wide:
  every vehicle carrying a contested word resolves by CIK and filing address.

- **R2 (2026-09-07) — the site's own entry-round field publishes only when it
  says Series B or later.** Scored on the stage golden set before the grind
  (§4): `firstPartnered` is 12/17 overall and the misses are ONE class.
  6/6 where it claims Series B or later, 4/4 where it claims Series A and
  **2/7 where it claims Seed**. (The single Series A "miss" was my own
  recognition failure rather than the layer's: that key row was written against
  Joinhandshake, the campus recruiting company, while Greylock's Handshake is
  handshake.org, the naming protocol. Corrected in `golden.json` before the
  grind, under §4's rule that a golden label can itself be wrong.) Where Greylock was the first institutional money
  the field reads "Seed" whatever the record calls the round (AppDynamics'
  $5.5M Series A, Sumo Logic's $5.8M Series A, TellApart's $4.75M first round,
  Abnormal's $24M Series A — whose first Form D *is* that Series A, so no
  earlier priced round exists), and it fails by two buckets in the other
  direction on Cribl, which Greylock entered at the $200M Series C. The field
  is not a round name; it is the firm's own sense of how early it felt.
  Class-wide: a Series-B-or-later claim is class 1 and publishes as Growth; a
  Seed or Series A claim is corroboration only, and the round is established
  from the record.
- **R3 (2026-09-07) — Greylock's announcement archive is a thesis archive and
  is refused for `entry_stage`.** Creandum's finding was that a firm's own
  announcement archive scores class 1 for the round; Menlo's was that it
  inverts where the firm leads later rounds into companies it seeded quietly.
  Greylock is a third case: the posts name no round and no amount, only ~14 of
  207 are investment announcements, and the archive starts in 2015. It stays
  in the evidence pack as dated first-party evidence THAT the firm invested —
  membership evidence and a `first_seen` ceiling — and nothing more.
- **R4 (2026-09-07) — GoFundMe is a control position and leaves the published
  base.** In June 2015 an investor group led by Accel and TCV, with Greylock,
  Iconiq, Meritech and Stripes, bought a controlling stake from the founders at
  a ~$600M valuation; both founders stepped back from day-to-day roles. Under
  T3's control-position addendum (Erik, 2026-09-04) that is not a venture
  round, so `entry_stage`, entry valuation and the C2A cohort are meaningless
  for it. `excluded.json`, reason `control_position`. Greylock has no earlier
  position in the company, so nothing survives the exclusion. Raised for the
  wave alignment because Accel's published base holds the same row.
- **R5 (2026-09-07) — the Israel book is out for its whole life, not only after
  the 2015 rebrand, and the archived listings are a shared-brand surface.**
  D2 ruled Greylock Israel out on its separate ERA. Its own Form ADV closes the
  question of what that entity is: **GREYLOCK ISRAEL GLOBAL MANAGEMENT LTD.
  (CRD 162176) gives its website as 83north.com** and advises GREYLOCK ISRAEL
  LIMITED PARTNERSHIP (Cayman) — the Israeli adviser simply renamed, so the
  Israel funds were never advised by Greylock Management Corporation (CRD
  161537) at any point. The firm's 2005–2013 listings nonetheless carried the
  Israeli companies, which is the Lightspeed shared-brand case: archived
  listing years from a shared-brand surface are not, alone, home-firm listing
  evidence, and membership resolves by the current attribution plus independent
  vehicle or partner evidence. Class-wide: a row whose only Greylock
  attribution is an Israel-desk partner — **Moshe Mor (2001–2013, 8 attributed
  deals), Erez Ofer (2004–2007), Yoram Snir (2005)** — and which the current
  site does not list is `not_member`, reason external desk. A row those
  partners share with a home-desk partner, or that a Greylock (not Greylock
  Israel) fund vehicle filed on, stays.

### D-S2A — Seed-to-A graduation re-judged under the status contract (2026-09-17, agent, class-wide)

Under the 2026-09-16 contract (COLLECTION.md §6) every in-window Seed row was
re-judged with both legs cited: 71 seed entries, 10 censored, 22
undetermined, cohort 39, graduated 37, rate 94.9%, coverage 64%. No Form D
verdict was disputed, because no row in the delta carried one. Two rows left
the cohort: **upwind** re-staged to Series A (SiliconANGLE dates Greylock's
entry to the $50M Series A it co-led at the 2023 stealth exit, with $80M
already raised, so an earlier round exists that no page puts Greylock in),
and **workday** takes `pre_window_entry` at low confidence under the 2006
constant, keeping its `cite_pending` flag, which is what satisfies the
public-$1B+ market-cap invariant. **wisetack**'s entry date was moved off the
Form D layer's $15M filing to the 2019 seed, since TechCrunch describes the
$19M as spanning "its seed and Series A rounds, which were both led by
Greylock" and the firm's own post says it incubated the company.

`verify.shape.c2a_rate_max` stays at 0.98, but its note is re-derived: the
old reasoning counted a cohort of unverified rows, and the shape it described
survives the harder instrument.

**Open — three identity questions for a rebuild.**
1. **`ailens-inc` is almost certainly TruEra before its rebrand**, not a
   separate company: its single 2019 Menlo Park filing is $5,099,988, exactly
   the 2019q2 round the `truera` row already carries, with the same Jerry Chen
   director signature, and FinSMEs reports that $5.1M as TruEra's first round
   led by Greylock. Left `undetermined`, because that is an identity ruling
   and not an S2A answer.
2. **`greenlite` and `bretton-ai` are one company** (Greenlite AI rebranded to
   Bretton AI in February 2026), judged identically on both rows.
3. **`bedrock-data` and `bedrock-security` are one company**, likewise.

**Two traps recorded for the next run.** `greylock.com/blog/bedrock-security/`
serves the Kodem announcement body under a Bedrock title, so it is not a
Bedrock citation. And "Airspeed" is a name collision: the $20M Series A of
June 2026 belongs to a different London/New York go-to-market company, not
Greylock's Slack-based Airspeed.
