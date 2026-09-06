# COLLECTION.md write-back proposal — PRO-86 (Union Square Ventures), 2026-09-05

Proposed only; nothing here is committed to COLLECTION.md or scripts/ from this session (§12). For the tooling session.

1. **§8 record: make rejection unmissable.** `record` prints "REJECTED — n problem(s), nothing recorded" followed by
   bullets; a truncated read (`tail -2`) shows only bullets, which read like warnings. Twice in this run a rejected file
   passed as recorded until verify showed `valuation_range None`. Proposal: exit non-zero on rejection (so `&&` chains
   stop) and print the header again as the last line.
2. **§8 record: document the merge semantics of `note`.** `note` is appended (" | ") when the new text is not contained in
   the old, otherwise the field is left as is; explicit `null` in a line overrides the deterministic layer (that is how an
   acquired row sheds its unicorn pre-fill). A fix script that re-emits the old note plus a suffix duplicates it. One
   sentence in §8 saves the next run the dedupe pass.
3. **§8 record: `graduation set but entry_stage=None`** is judged on the line, not the merged row; a graduation-only fix
   must restate the row's `entry_stage`. Say so next to the C2A rules.
4. **§3/§6 recall additions vs the name-variant prefix merge.** The build merges "Brilliant" into "Brilliant Planet" unless
   one listing snapshot names both; a recall addition never appears in a snapshot, so it is always merged away. Proposal:
   exempt recall additions from the prefix rule (or warn loudly when one is absorbed), and add R12's naming rule to §3.
5. **§11 exempt reporting advisers.** USV is the first ERA in the set: no Item 5.F RAUM exists; Schedule D 7.B.(1) gross
   asset values are the sworn substitute (26 funds, $3,235,446,464). Write the rule into §11 next to the RIA text, with
   the parse method (first-appearance sequences over page-repeated PDF text).
6. **LANDED 2026-09-06 as Rule A (Erik's ruling, written into §7 valuation by the USV session).** §7 valuation: name the aggregator rule (R11). PitchBook/CB Insights/Tracxn/Contrary/Sacra marks go to the note and
   never band a row; a `1b_plus` band needs a priced round, tender or float with a citable figure. Spark's Justworks row
   banded on a PitchBook mark; USV and Thrive did not — the wave needs one rule.
7. **§7 acquired rows (R8).** Make explicit what every run already does: `acquired` carries no figure and bands
   `below_1b`; the exit price goes in the note. `record` enforces the first half only.
8. **§11 icons: extend `--discover` with the WordPress media library** (`/wp-json/wp/v2/media?search=logo|<acronym>`);
   USV's only ≥256px source was the site-icon original there (512x512), invisible to the link/manifest scan. Also decide
   what the contrast floor means for brand plates: USV's white-on-green mark measures 2.70:1 and cannot be re-plated
   without recolouring the glyph.
9. **§10 invariant 10 and slug variants (R13).** The comparison is by CIK and name key, so same-company rows under
   different slugs (matter-labs-zksync / matter-labs, sift-science / sift, dapper-labs / dapper, foursquare / four-square,
   granola-inc / granola, zerion-inc / zerion, koko / koko-labs, dia / dia-co, stacks / stacks-ai, sidecar / sidecar-
   technologies-inc, assembly vs assembly-ai is distinct) agree in verify but would be distinct rows in the companies
   table. Proposal: a wave-alignment step that picks one slug per company (the first-ingested) and records the mapping in
   the shared cross-investor.json.
10. **§12 review surface.** With two sessions the shared 8931 port was busy; `preview_start` fell back to 54160 and the
    playbook's fixed URL was wrong for this session. Note that the port is per instance and the path is what matters.
