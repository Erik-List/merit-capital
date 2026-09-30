#!/bin/zsh
cd /Users/erik/Developer/merit-capital
for b in "$@"; do
  o=$(python3 scripts/run.py verify --investor $b 2>&1)
  echo "=== $b: $(echo "$o" | tail -1)"
  echo "$o" | grep -E "^\s+- " | head -12
done
