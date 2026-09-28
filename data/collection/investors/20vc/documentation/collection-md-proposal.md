# Proposed COLLECTION.md diff (PRO-76, not applied)

Proposed by the 20VC run on 2026-09-28 for the tooling session to land at the
next wave boundary (COLLECTION.md s12: the playbook is edited by the tooling
session only). Rationale and measurements: `documentation/report.md` s3 and
s11.

## 1. s5 layer 3, after "Two registry rules." paragraph

```diff
@@ s5 Evidence layers, 3. EDGAR (after the two registry rules)
+   **A name-pattern registry can be empty without being clean** (20VC,
+   2026-09-28, PRO-76). Five of 20VC's seventeen vehicles, its first fund
+   among them, were invisible to every route: EDGAR's company search matches
+   name PREFIXES ("Fund I, a series of 20VC, LP" never matches "20vc"), the
+   administered platform funds' Form Ds name the administrator's GP
+   (Belltower Fund Group) and never a partner, and IAPD's search found no
+   adviser because it files as Twenty VC LLP. Three more routes close it,
+   all in `config.json edgar`:
+   - `adviser_crds`: every Section 7.B(1) and 7.B(2) fund name on each
+     adviser's newest Form ADV (the IAPD PDF firm-offices.py already reads)
+     is resolved to a CIK by EDGAR full-text search on the name's
+     distinctive tail, source `adv-7b`. Find the adviser by the Form D
+     filing address in the SEC's monthly roster CSV when IAPD's search fails
+     (First Round's method), and record the CRD here once.
+   - `vehicle_phrases`: EDGAR full-text phrases ("a series of 20VC") whose
+     Form D hits are the firm's vehicles when the conformed name contains the
+     phrase: catches the funds no ADV lists yet (a first fund older than the
+     registration, a vehicle newer than the last amendment).
+   - `gp_entities`: a Form D whose related persons name the firm's GP entity
+     ("20VC GP II") is the firm's vehicle, whatever its name (every 20VC
+     S-series single-deal fund). The bulk files already carry these rows;
+     the sweep today matches roster people only.
```

## 2. s10 Verify invariants, a new invariant

```diff
@@ s10 after invariant 11
+12. Registry completeness: the vehicle registry resolves at least as many
+    own vehicles as the firm's advisers swear to on Form ADV (Section 7.B(1)
+    and 7.B(2) private-fund counts, read from the SEC's monthly roster CSV).
+    A sworn count N > 0 with fewer resolved fails ("the registry missed K of
+    N sworn funds"); a sworn count of 0 with an empty registry is clean and
+    printed as "no private funds reported", the only state in which an
+    empty registry is clean; no adviser resolved at all fails unless
+    `edgar.no_adviser` states why (a firm below the SEC's thresholds). The
+    sworn count is what tells "no vehicles" apart from "the pattern missed".
+    Added 2026-09-28 after 20VC (PRO-76): the registry held 12 of 17
+    vehicles and said nothing.
```

## 3. s6 S2A, the surfaces paragraph

```diff
@@ s6 seed_to_a_graduation, after "scripts/graduation-surfaces.py runs the standard surfaces"
+  **The surfaces search the published name**, `config.json names.published`
+  where one exists, else the base name. The 20VC run's standard queries went
+  out as "LottieLabs", "Noh Payments" and "Roam" (the base renderings of
+  Lottielab, Noh and Roam Research), so three absence tests needed a
+  hand-run query named on the row.
```

## 4. s5, the site layer: Framer CMS

```diff
@@ s5 layer 1 (the firm's own site), escalation ladder
+  **Framer sites** ship a CMS collection as a binary data chunk
+  (`<module path under /cms/>-chunk-default-0.framercms`) behind a client-side
+  "Load More"; `scripts/framercms.py` (promoted from the 20VC run's scratch)
+  decodes it to name, one-liner, sector enums, website and exit flag. The
+  Internet Archive keeps older chunks under the project's `/modules/` prefix
+  on framerusercontent.com (a CDX prefix query finds them); the 2026 format
+  pairs an index chunk with a dictionary chunk whose strings carry every
+  card, which is how the 20VC run resolved Alloy (alloy.capital) from a card
+  the live list had dropped.
```

## 5. s1, the podcast-brand reading (a standing rule)

```diff
@@ s1 Evidence rules
+- **A firm that is also a media brand is named far more often as the medium
+  than as the investor** (20VC, PRO-76): "told 20VC", "on the 20VC podcast"
+  and a guest's own remarks never count as membership; the firm's own
+  statement about its holding, on its own show, is first-party evidence of
+  that position (20VC's R2, Poolside).
```
