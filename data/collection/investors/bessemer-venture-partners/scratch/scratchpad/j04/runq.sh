#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
while IFS='|' read -r slug q; do
  echo "##### $slug :: $q"
  NQ_TAG=j04 python3 nq.py "$slug" "$q" 2>&1 | tail -16
done < scratchpad/j04/queries.txt
echo "##### DONE"
