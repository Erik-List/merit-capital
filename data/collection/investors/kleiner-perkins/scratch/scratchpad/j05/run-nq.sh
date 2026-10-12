#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
while IFS='|' read -r slug q; do
  [ -z "$slug" ] && continue
  echo "##### $slug :: $q"
  NQ_TAG=j05 python3 nq.py "$slug" "$q" 2>&1 | tail -16
done < "$1"
