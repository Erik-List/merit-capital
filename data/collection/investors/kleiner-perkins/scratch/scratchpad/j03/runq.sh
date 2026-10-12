#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
while IFS='|' read -r slug q; do
  echo "=== $slug | $q"
  NQ_TAG=j03 python3 nq.py "$slug" "$q"
done < "$1"
echo DONE
