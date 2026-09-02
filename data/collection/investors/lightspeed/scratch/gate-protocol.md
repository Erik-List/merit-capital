# Checkpoint-1 blind pass protocol (COLLECTION.md §4)

Order, run after build + prepare + seed, before ANY verdict records:

1. `python3 scripts/run.py status --investor lightspeed` — confirm 0 recorded
   agent verdicts beyond evidence-class seeds.
2. For each of the 22 golden slugs: pull the BUILT row (base.json), its queue
   item if queued, and its evidence links. Judge fresh through decisions.md +
   COLLECTION.md §1-3 only — golden.json stays closed (single-session caveat
   as Accel: same session wrote the key; honesty = document-anchored key,
   registered pre-build in commit 9efb036).
3. Structural falses first: lightspeed-technologies, lightspeed-microscopy,
   select-iv, ppdai, rong360, flock-io, pharos, apna, zolve must have NO
   published base row (grep base.json + excluded.csv reasons).
4. Judged rows (oyster-travel, arrikto, popupbagels if built; all 10 trues):
   write blind verdicts to scratch/gate-blind-pass.json.
5. Score vs golden.json membership key; decompose misses BY LAYER; fix the
   layer, re-run the blind pass on affected rows; record PASS in run-log +
   checkpoint-1 paragraph in chat. Zero false members at high confidence.
