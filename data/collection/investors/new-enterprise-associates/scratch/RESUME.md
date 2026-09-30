# NEA run (PRO-100): where to resume (updated 2026-09-30, after the scheduled rebuild)
Done: evidence layers, base, full grind, fix passes F1-F6, stage pass s1-s5, A/B ab1-ab3, caps, recall probe,
the scheduled rebuild (1,126 rows), delta prepare (153 rows, 4 batches), lead rows (judgments-lead1.py: Glacier Bay,
Viracta not_member, Cohere Technologies stage), NeueHealth control check (judgments-nh.py), profile files written and
built once (investor/*.json; icon uploaded to storage, investors/new-enterprise-associates-bbcae460c3.png).
Rebuild findings fixed by hand: rename step moved Serious Materials' answers onto glacier-bay-inc (removed); merge
canonicals re-pointed (sunesis-pharmaceuticals, trivascular-technologies-inc); wrong merges corrected (cohere-networks
is Gainspeed; the 2017-19 'Blend' is Genies, Blend Therapeutics is Tarveda; never_merge pairs added); pooled Form D
cache entries split (blend -> genies/tarveda-therapeutics; cohere-networks -> gainspeed); northern-power-systems
ledger entry tagged exclusion=control_position.
In flight: delta judges g1, g2, g3a, g3b, g4 (DELTA-BRIEF.md). Then, in order:
1. Read their reports; fix anything they left. 2. The SECOND, final rebuild (delta has membership verdicts); read its
rename lines; re-run prepare if it re-queues anything. 3. `python3 scratchpad/cross.py` style capture of rule-10
disagreements -> scratch/cross-list.txt; run the cross pass (CROSS-BRIEF.md); apply distinct/accepted to
companies/cross-rulings.json; keep the sibling_stale list for ingest. 4. Verify clean-ups (mode stale stage keys;
stash unicorn_list source). 5. build-firm-profile.py again (asserts notables, recomputes focus). 6. verify clean,
export, review (port 8931), report.md, write-back, close, commit (explicit pathspec), section 9 ingest + sibling
alignments, Linear PRO-100, memory file.
WebSearch used: 127 of 200 before the delta judges (their cap: 32).
