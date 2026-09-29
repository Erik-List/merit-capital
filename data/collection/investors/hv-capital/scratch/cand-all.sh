#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/hv-capital
for b in 1 2 3 4 5 6 7; do python3 scratch/candidates.py $b > scratch/cand-b$b.txt 2>&1; echo "batch $b done"; done
