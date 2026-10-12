#!/bin/bash
export NQ_TAG=j10
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
while IFS='|' read -r s q; do [ -z "$s" ] && continue; echo "== $s"; python3 nq.py "$s" "$q" --all 2>&1 | head -9 | cut -c1-200; done
