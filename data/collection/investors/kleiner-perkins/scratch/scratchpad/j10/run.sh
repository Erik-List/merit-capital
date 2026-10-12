#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
f=$1
while IFS=$'\t' read -r slug q; do
  echo "$slug	$q"
done < "$f" | xargs -P 3 -d '\n' -I{} bash -c 'slug=$(echo "{}" | cut -f1); q=$(echo "{}" | cut -f2); out=$(NQ_TAG=j10 python3 nq.py "$slug" "$q" --all 2>&1); printf "=== %s | %s\n%s\n" "$slug" "$q" "$out" >> scratchpad/j10/nq.log'
echo DONE $f >> scratchpad/j10/nq.log
