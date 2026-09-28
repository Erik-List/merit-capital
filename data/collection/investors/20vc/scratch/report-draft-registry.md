## The vehicle registry: what PRO-76 asked, and the answer

**Five of the firm's seventeen vehicles, its first fund among them, were
invisible to every route the registry had, and the registry said nothing.**

| Route in `edgar-entities.py` | What it found | Why it missed the rest |
|---|---|---|
| EDGAR company search, `seed_queries: ["20vc"]` | 12 filers named "20VC ..." | The search matches name PREFIXES: "Fund I, a series of 20VC, LP" starts with the administrator's pattern, and `fund i, a series of 20...` returns nothing because the search stops at the comma |
| Co-filer closure | nothing new | The platform funds co-file with nothing the seed found |
| Own pooled Form D issuers (partner-matched sweep) | 2 Stride funds (Harry Stebbings is an officer), 20VC's own | The platform funds' Form Ds name AngelList's Belltower Fund Group and "Fund GP, LLC", never a partner |
| IAPD firm search, "20VC" | nothing | The adviser files as Twenty VC LLP (CRD 316359) |

What found them: the adviser's own sworn fund list. Form ADV Section 7.B.(1)
names six funds and 7.B.(2) three more (the 20Growth, 20Product and 20Sales
series funds, reported by AngelList Advisors); EDGAR full-text search on each
name's distinctive tail ("a series of 20VC") resolves it to a CIK with an
exact match on the conformed name. Two vehicles are on no ADV and were found
by the full-text phrase alone: Fund I (it predates the 2021 registration) and
20Sales Fund II (it postdates the 2025 amendment).

### Proposed config shape

```json
"edgar": {
  "seed_queries": ["20vc"],
  "adviser_crds": [316359],
  "vehicle_phrases": ["a series of 20VC", "a series of 20Growth", "a series of 20Product", "a series of 20Sales"],
  "gp_entities": ["20VC GP II", "20VC GP III"]
}
```

- `adviser_crds`: the registry reads each adviser's newest ADV (the IAPD PDF,
  already fetched by `firm-offices.py`) and resolves every 7.B.(1) and 7.B.(2)
  fund name, source `adv-7b`. The adviser is found by the Form D filing
  address in the SEC's monthly roster CSV when IAPD's search fails (the First
  Round method), and its CRD is written here once.
- `vehicle_phrases`: EDGAR full-text phrases whose Form D hits are the firm's
  vehicles when the conformed name contains the phrase; catches funds no ADV
  lists yet.
- `gp_entities`: Form D related-person names of the firm's GP entities; a
  vehicle of any name whose Form D names the firm's GP is the firm's (every
  S-series SPV names 20VC GP II). The bulk Form D files already carry these
  rows; the sweep today only matches roster PEOPLE.

### Proposed verify signal (a new invariant)

**Registry completeness: the registry resolves at least as many own vehicles
as the adviser's sworn fund count.** `verify` reads the adviser's 7.B.(1) and
7.B.(2) counts from the SEC's monthly roster (columns "Count of Private Funds
- 7B(1)" and "- 7B(2)"; one CSV, no fetch per run beyond the monthly file) and
compares them with the registry's rows carrying source `adv-7b`:

- ADV count N > 0, registry resolves N: OK.
- ADV count N > 0, registry resolves fewer: **fail**: "the name-pattern
  registry missed K of N sworn funds" (this run before the fix: 3 of 9, the three 7.B.(2) series funds; Fund I and 20Sales Fund II are on no ADV and are the full-text phrases' job).
- ADV count 0 and registry empty: OK, printed as "no private funds reported"
  (the only state in which an empty registry is clean).
- No adviser resolved at all: **fail** unless config states
  `edgar.no_adviser: "<reason>"` (a firm below the SEC's thresholds, say).

The counts are what separate "empty because there are no vehicles" from
"empty because the pattern missed": the first is an adviser swearing to zero
funds, the second an adviser swearing to N while the registry holds fewer.
