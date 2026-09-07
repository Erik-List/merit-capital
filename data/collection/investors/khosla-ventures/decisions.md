# Khosla Ventures — investor-specific decisions

Derived from the standing rule set in `data/collection/COLLECTION.md` §1 under
the derivation protocol: one line per category, the facts found, the test
applied, the outcome, the precedent. Derivations need no confirmation — they
are listed in the run's Linear issue for Erik to veto before kickoff; silence
means they apply. Only the deltas in §2 need Erik.

Run: one session, started 2026-09-07.

## 0. The facts this file rests on (verified at kickoff, not assumed)

| Fact | Source |
|---|---|
| One adviser: **Khosla Ventures, LLC**, **exempt reporting adviser**, SEC file 802-76280, CRD 162910, 2128 Sand Hill Road, Menlo Park CA 94025 | IAPD firm search 2026-09-07 (`firm_source_id` 162910, `firm_ia_full_sec_number` 802-76280, scope ACTIVE, one branch) |
| No second registration under the brand, and no separate Khosla Impact adviser | IAPD returns zero hits for "Khosla Impact", "Khosla Labs" and "Khosla Ventures Management"; the only Khosla adviser in IAPD is CRD 162910 |
| An ERA files no Item 5.F RAUM; Section 7.B private-fund gross assets is the sworn substitute | COLLECTION.md §11 AUM recipe, the Creandum/Cherry ERA shape |
| Every vehicle files from **3000 Sand Hill Road** (funds I–III, Seed) or **2128 Sand Hill Road** (IV onward), Menlo Park | EDGAR submissions API per CIK, 2026-09-07 |
| Firm founded 2004 by Vinod Khosla after leaving Kleiner Perkins; the base window opens 2006 | COLLECTION.md §1 policy constant |
| Five natural persons named Khosla hold their own EDGAR CIKs, one of them an unrelated investor | Vinod Khosla 1032453, Chaitan Khosla 1135139, Rachna Khosla 1881332, Rajiv Khosla 1537095, Victor Khosla 1473996 (Strategic Value Partners, distressed debt) |

The vehicle family (EDGAR company search 2026-09-07, 66 registrants under
"khosla", filtered to the firm's own):

- **Flagships** — Khosla Ventures I (CIK 1501935), II (1501949), III (1471809),
  IV (1521016), IV (CF) (1685550), V (1611146), VI (1734961), VI (AIV)
  (1778468), VI (AIV) Holding (1778470), VII (1828214), VIII (1958968),
  VIII Strategic (2006738), IX (2074230), IX Strategic (2097668).
- **Seed funds** — Khosla Ventures Seed (1471810), Seed B (1551426), Seed B
  (CF) (1551427), Seed C (1627897), Seed D (1734977), Seed E (1828213),
  Seed F (1959515), Seed G (2074203), Seed Side Fund (1501948).
- **Growth sleeve** — Khosla Ventures Opportunity I (1837715), II (1959115),
  III (2074231).
- **SPVs and single-deal vehicles** — CFS SPV (1894352), GI SPV (2109620),
  GI SPV II (2153384), IFSPV I (1802299), II (1891166), II-A (1891165),
  II-B (1892357), MM SPV (2148181), OAI (2039800), Moonshot (2152350),
  Excelsior (1969723).
- **General partners** — the Khosla Ventures Associates I–VII LLCs, Seed
  Associates / B / C / D, Seed Side Fund Associates, Opportunity Associates
  I–II.
- **The 2021 SPAC programme** — Khosla Ventures Acquisition Co. (1841873),
  III (1846068), IV (1847037), the four Sponsor LLCs, and **Khosla Ventures
  Acquisition Co. II, which became Nextdoor Holdings, Inc.** (1846069) — the
  programme's only completed de-SPAC. KVSA I and III wound up (last filings
  SC 13G/A, Feb 2024); KVSA IV was deregistered by SEC staff action (Jul 2022).
- **Third-party feeders, NOT the firm's** — Khosla Ventures 2023 Allocate
  Access Fund (1977905, 1300 El Camino Real Suite 100, Menlo Park) and
  KV 2025 - Allocate Access (2068411, 502 Waverley Street Suite 2, Palo Alto),
  both filing from Allocate Inc's addresses.

## 1. Derivations

**D1 — T1, same adviser. Every Khosla Ventures vehicle above is IN.** One
exempt reporting adviser, one office, no relying adviser and no brand-sharing
registrant: the Accel-KKR / Meritech / Lightspeed India pattern was checked in
IAPD and does not exist here. The flagship, Seed, Opportunity, AIV, CF,
Strategic, SPV and Associates vehicles all file from the adviser's own
addresses and are sleeves of the one adviser. Precedent: a16z's vertical
families under one adviser, Thrive's umbrella with its sleeves and lettered
LLCs, LSVP's offices under one CRD.

**D1a — T1 strategy desks: not reached.** Every Khosla strategy is venture —
seed (Seed A–G), early (the flagships) and growth (Opportunity I–III). There
is no buyout, credit, infrastructure, real-assets or public-equities fund
under CRD 162910, so the 2026-09-04 strategy-desk partition does not fire and
no `other_desk` exists on this run. The profile is therefore sliced to the same
boundary as the base and the 7.B composite is the whole firm, with no
parent/child AUM problem.

**D1b — T1/T5: the two Allocate feeders are external.** `Khosla Ventures 2023
Allocate Access Fund, L.P.` and `KV 2025 - Allocate Access, L.P.` file from
Allocate Inc's addresses, not the firm's, and are third-party feeders that
raise into Khosla funds. Precedent: Thrive IX Access (a third-party feeder into
a fund is external; agent, flagged). Their own filings are not membership
evidence, and both are configured `external` in `desks.classify[0]`.

**D2 — T4/T5: the five natural persons named Khosla are external, and Vinod
Khosla's own filings locate the person, never a firm position.** Vinod Khosla
(CIK 1032453) has filed 98 Form 4s, 22 Form 3s and six 13G/As in his own name.
Standing rule (COLLECTION.md §1, person-level attribution): Forms 3/4/5 filed
by a natural person are dropped as sole evidence; the genuine EDGAR signal is a
fund vehicle on the filing. Victor Khosla (Strategic Value Partners), Chaitan
Khosla (a Stanford professor with biotech board seats), Rachna and Rajiv Khosla
are unrelated namesakes caught by CIK and address, never by name.

**D3 — T2/T4: Vinod Khosla's Kleiner Perkins record and his personal angel book
are OUT.** Vinod Khosla was a KPCB general partner from 1986 and founded Khosla
Ventures in 2004; his KPCB-era positions (Juniper, Cerent, Siara, NexGen and the
rest) are a prior firm's, dated against the person's firm at filing time.
Precedent: the seat-dating rule in full (Accel's Jonathan Turner e.ventures-era
boards; Ethan Choi leading Anrok at Khosla months after leaving Accel — the
playbook's own example, and Choi is on this roster). Personal angel cheques with
no Khosla fund behind them are out on the same test as Kushner and Cherry's
founder-angel positions. **A named class here**: Khosla's roster is unusually
full of founder-operators — Evan Moore (DoorDash), Nikita Shamgunov
(SingleStore), Tim Westergren (Pandora), Benny Buller (Velo3D), Uri Lopatin,
Ari Zilka (Terracotta) — and a founder is a related person on their own
company's Form D, so the roster sweep will confirm their founder-era companies
with filing-grade-looking evidence. Those are personal/founder seats unless a
Khosla fund held. This class is pre-registered in the membership trap set (§4).

**D4 — T2: the 2004–2009 book, funded by Vinod Khosla's own capital through the
firm's own fund vehicles, is IN.** Khosla Ventures took no outside limited
partners until Khosla Ventures III and the Seed fund closed in 2009; Funds I and
II were Vinod's own money. The membership definition asks whether a firm
representative, acting on behalf of the firm, invested **fund money** — and
Khosla Ventures I, L.P. and II, L.P. are funds of the firm under its own
adviser, staffed by its partners and listed on its own portfolio pages. A fund's
LP composition is an LP-side fact the base never looks at; a single-LP fund is
still a fund, which is what separates this class from a partner's personal angel
book (D3, where there is no firm vehicle at all). This derivation moves a large
class of rows — most of the 2004–2009 cleantech book — so it is called out in
the issue for veto rather than buried.

**D5 — T3: standard venture entry, with no control positions expected.** Khosla
is a minority venture investor across seed, early and growth; primaries,
follow-ons, secondaries and tenders are IN, and a secondary or tender entry is
Growth by the policy constant. The 2026-09-04 control-position rule is recorded
as applicable but no Khosla LBO or majority recapitalisation is known; any that
the grind surfaces lands in `excluded.csv` under `control_position` and the
profile says so.

**D6 — T3: post-RIA public and secondary purchases with no venture entry are
`not_member`.** Standing rule (generalized 2026-09-03). Khosla files 13Gs on
issuers it took public; a row that entered through a venture round stays in
after the IPO, and a position that first appears as a 13F holding or a post-IPO
13G does not.

**D7 — T5: the SPAC shells themselves are not rows.** Khosla Ventures
Acquisition Co. I, III and IV are blank-check vehicles with no operating
business; two wound up and one was deregistered. Fund-shaped list entries and
shell vehicles are not venture-outcome operating companies. The *target* of the
one completed de-SPAC is a different question and is delta **X1** below.

**D8 — T5: the SPVs and single-deal vehicles are plumbing, not rows, and a
commitment made through one enters at that stage.** CFS SPV, GI SPV I/II,
IFSPV I/II/II-A/II-B, MM SPV, OAI, Moonshot and Excelsior are Khosla vehicles
whose positions are rows through their underlying companies. Precedent:
Lightspeed's Project Mercury; Creandum's Select funds and SPV TR as follow-ons
with entry stage unchanged.

**D9 — evidence sufficiency and the site's own fund label.** A listing on any
era of khoslaventures.com suffices alone, as does an SEC filing by a fund
vehicle. The live Webflow cards additionally carry the firm's **own fund label**
(`Seed` / `Early` / `Growth`, on 88 of 114 rows). That label is a candidate
class-1 `entry_stage` layer and is **scored blind on the golden set before it is
allowed to label anything** (COLLECTION.md §4, the Accel CMS label promoted
30/31 versus Thrive's job board refused 0/10). Note the specific risk it
carries: the label names the *fund* that holds the position, which is a proxy
for the entry round and not the round itself, and the firm re-lists companies it
followed on into. Until scored it is corroboration only.

**D10 — the roster's two-spellings trap is fixed before the base is built.**
`partner-roster.py` returned 116 people and five of them are one person under
two slugs — `kanu-gulati`/`kanupriya-gulati` (2025–2026 and 2019–2025),
`avisha-mehra`/`avisha-mehra-naganath` (2020–2025 and 2022–2026),
`kathy-chan`/`kathy-h-chan`, `tamara-tompkins`/`tamara-l-tompkins`, and
`qa-irene-au`, a staging artifact of `irene-au`. Left alone,
`build-company-base.py`'s ex-partner rule reads each as departed years before
they left. Collapsed to one entry per person with the union window before the
build, per COLLECTION.md §8 (First Round, 2026-09-06).

**D11 — the roster is curated back past 2014.** The CDX roster covers 2014–2026
only, because the pre-2014 site used people namespaces the dash pattern cannot
reach: `/<lastname>.html` in 2006–2009 (vinod, kaul, weiden, lamond, kim,
kinnier, tamer, yu, cameron, white, adeeb) and `/people_<initials>.html` in
2010–2013. A 2014+ roster structurally misses the partner-anchored Form D
filings of the firm's first decade — the same defect Lightspeed found in its
2012+ window — and Khosla's first decade is most of the cleantech book. Those
names are curated by hand from the captures into the roster with their capture
windows and a recorded basis.

## 2. Deltas — these need Erik

**X1 — Is Nextdoor a member on the strength of the KVSA II de-SPAC alone?**

The facts. Khosla Ventures sponsored four blank-check companies in 2021.
Exactly one completed a deal: Khosla Ventures Acquisition Co. II merged with
Nextdoor in November 2021 and the registrant is now Nextdoor Holdings, Inc.
(CIK 1846069). The sponsor vehicle, Khosla Ventures SPAC Sponsor II LLC, is the
firm's own, so the position is unambiguously the firm's and unambiguously in an
operating company — T1, T2 and T5 all say yes.

Why no test decides it. T3 asks whether the position entered **through a venture
round — a primary, a secondary or a tender in a private company**. A sponsor
promote is none of the three: the sponsor's founder shares are issued by the
shell at nominal cost when the shell is formed, and the position in the operating
business arises from a reverse merger into a public listing, not from a
financing of Nextdoor. It is also not the T3 OUT limb, which names public-market
purchases, 13F holdings and post-IPO 13Gs — the shares are not bought on the
market and the entry is contemporaneous with the listing rather than after it.
The sponsor PIPE, if a Khosla fund took one, is a different instrument again and
would be a purchase into a company at the moment it becomes public.

The recommendation. **Out, unless a Khosla fund held Nextdoor through a venture
round before the merger** — in which case the row is a member on that earlier
round and the SPAC is irrelevant to its membership. The reasoning: T3 exists to
keep the base to positions taken through venture financings of private
companies, and a sponsor promote is a fee for assembling a listing vehicle, not
a venture entry. Ruling it in would also make `entry_stage` meaningless for the
row in the way the control-position rule describes — there is no round to label.
The grind checks the pre-merger cap table first; whichever way this lands it is
a boundary ruling of the kind COLLECTION.md §9 trigger 2 reserves for Erik,
because it decides how every future sponsor-vehicle position is read.

## 3. Run-time standing rulings

_(dated, class-wide, flagged for review; added during the run)_
