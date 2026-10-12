#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
while IFS=$'\t' read -r slug q; do
  echo "### $slug | $q"
  NQ_TAG=j04 python3 nq.py "$slug" "$q" --all 2>&1 | tail -18
done < scratchpad/j04/queries.tsv
echo DONE
