#!/bin/zsh
# Before any alignment write (COLLECTION.md 9): each sibling book's verify as it stands, and its live rows read back
# against the committed base.csv (the tree is clean, so the working CSV is HEAD).
cd /Users/erik/Developer/merit-capital
for b in "$@"; do
  v=$(python3 scripts/run.py verify --investor $b 2>&1 | tail -1)
  r=$(npx tsx data/collection/investors/20vc/scratch/align/readback.ts $b 2>&1 | tail -1)
  echo "$b | $v | $r"
done
