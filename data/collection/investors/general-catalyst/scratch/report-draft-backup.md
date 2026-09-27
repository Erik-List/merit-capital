# General Catalyst: Build & Reconciliation Report (PRO-166)

**Linear issue** PRO-166 · **slug** `general-catalyst` · one run under the merged shape of
`data/collection/COLLECTION.md`, in two sessions (a context restart mid-grind) · report written
2026-09-27. **Not ingested**: the ingest waits on Erik's approval (section 14).

---

## 1. The answer PRO-166 asked for

{{SUMMARY}}

## 2. Results

{{RESULTS}}

## 3. The boundary: control positions, Creation, the Customer Value Fund

The firm runs venture and growth funds, a Creation strategy (hatches and AI-enabled roll-ups),
the Customer Value Fund (revenue-sharing growth financing), GC Wealth and a SPAC. The page's
track record covers the venture investments only (decisions.md D3 to D8, R1 to R4):

- **Control positions out** (D4, R4): Athletes First (the MASTRY and GC majority purchase, 2023),
  the roll-ups Beacon, Dwelly, Long Lake and Zero RFI, Aura and Intersections (the consortium
  take-private of 2018/19 is the entry), BBN (the 2004 purchase from Verizon), and eleven list
  entries named as buyout or holding vehicles (Ulysses Buyer, Fino Topco, Raven TopCo, Dynamo
  Topco, Logicbroker TopCo, RW-2023 HoldCo, Build Holdco I, ReInvent Commerce Holdings, XFIT
  Holdings, Ponto Meridian Rollup, Beacon Acquisition). HATCo's Summa Health purchase is not a
  row. {{CONTROL_COUNT}}
- **Creation hatches in** (D3.1): Commure, Hippocratic AI, Homeward, HealthEx, Maribel, Kayak,
  Demandware, Datalogix, Datto, Livongo, Transcarent, Tendo, Paradigm, Pacific Fusion and others,
  each entered on its founding capital. **X1, the Creation companies that build and buy**, were
  ruled on the entry: Accrual, Crescendo, Eudia and Titan are IN (a product company when the firm
  came in, acquisitions after); Zero RFI is OUT (it launched on its seed with three acquisitions).
  These five are the ones to move if the line should sit elsewhere.
- **Customer Value Fund** (D6, R3): ten companies whose only tie is CVF money are out
  (Beautiful.ai, Chainguard, CookUnity, Function Health, IM8, Ladder, Mirage, Quo, Relay, Rylo).
  Where a venture fund also bought equity the company stays, entered on the first equity round
  (Factorial's 2026 Series D; Iru's 2024 round). Dandy is `uncertain`.
- **La Famiglia and Venture Highway** (D8): 41 La Famiglia companies backed before the October
  2023 combination are out as the earlier firm's deals (Personio, Forto, SoSafe, Y42, Vay, Stoke
  and others); Mistral AI stays, entered on the firm's own December 2023 Series A.
- **Sale consideration** (R1): Teladoc (Livongo), Millennial Media (Jumptap), Xero (Melio),
  WW International (Weilos) and Starco Brands are out.
- **The SPACs** (D7) and the firm's own fund-shaped list entries are out.

## 4. Coverage per evidence regime

{{COVERAGE}}

## 5. Method deltas

- **The firm's /list page is the recall layer.** 1,896 legal names "as of June 30th, 2026", joined
  to the 607-company grid by name, reverse prefix and 12 judged pairs (Maplebear to Instacart,
  Exafunction to Windsurf, Blockratize to Polymarket and others). About 1,300 list rows name
  companies no other source identifies; they carry `status: unknown` and `city_unknown` rather
  than a guess.
- **Form D rows are adjudicated by who sat, not by the name.** 21 Form D registrants are the list's
  companies under a legal or former name and were folded in (JAND is Warby Parker, Mulberry Health
  is Oscar, Coopkanics is Wildcard, Unlimited Labs is B12, Emerging Travel is Ostrovok, DC Devices
  is Corvia, ParElastic is Tesora); the rest were namesakes or pre-GC seats (R2).
- **The research that did not fit the grind ran as three agents**: the CVF equity check, the
  Creation hatch-or-buy check and the valuation pins, each writing one findings file under
  `scratch/research/` that the judge applied row by row.
- **S2A from a converter**: `scratch/judge/s2a.py` turns one line per row into the record and
  builds the absence test from `scratch/graduation-surfaces.json`, the firm's own posts and the
  Form D sequence, so every no names its surfaces.

## 6. Flags and debt behind `verify`

{{DEBT}}

## 7. Standing duties and the A/B pass

- **Duty 1** ($1B+ claims): {{DUTY1}}
- **Duty 2**: every `not_graduated` is below $1B and private or dead; every `censored` entry is
  inside 24 months at the check.
- **Duties 3 and 4** (weak CIK joins, stale floats): the float layer's "acquired" on four rows
  whose registrant is another company is disputed (Cicero Technologies, Faro Health, Sprint Labs,
  Shyft; R5). The other stale-float rows are genuinely acquired.
- **Duty 5**: OvaScience's float belongs to its successor (merged into Millendo, 2018): acquired.
- **Duty 6**: a loose re-intersection of the unicorn list finds only name collisions, and Thatch,
  which the Wikipedia list shows at $1B (2026) with no citable round; it stays below $1B,
  aligned with Lux.
- **Duty 7**: a blind 5% re-classification (88 rows, seed 20260927) disagreed on 12; three were
  errors and are fixed (autone Series A, Mainspring Growth, Landbase private).
- **Duty 9**: the India-team region pattern was swept as a class and holds.
- **Momentum slice**: {{MOMENTUM}}

## 8. Firm profile

{{PROFILE}}

## 9. Open rulings for Erik

{{OPEN}}

## 10. Rebuilds and deltas

{{REBUILDS}}

## 11. Playbook write-backs proposed (not applied mid-wave)

{{WRITEBACKS}}

## 12. Usage line

{{USAGE}}

## 13. Prompt count

{{PROMPTS}}

## 14. Ingest request (not run)

{{INGEST}}

## 15. Incident: a personal address in a request header

One research subagent (the Creation check) sent one EDGAR full-text-search request with Erik's
personal Gmail address in its User-Agent header, contrary to the rule that the address is used
only to identify him. The repo's own scripts send the Merit Capital research address
(`scripts/edgar_common.py`); every later agent prompt in this run forbade personal identifiers
in requests, and no other request carried it.
