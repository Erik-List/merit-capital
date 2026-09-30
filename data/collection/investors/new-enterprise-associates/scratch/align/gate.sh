#!/bin/sh
# Pre-write gate for one sibling book (COLLECTION.md 9): record the NEA alignment lines once, export, review,
# plain verify, the cell diff against HEAD, the ingest dry run and the readback before. Writes nothing to the DB.
# Usage: sh gate.sh <book>        (run from the repo root)
set -e
b="$1"; K=data/collection/investors/new-enterprise-associates/scratch/align
python3 $K/align.py --record "$b"
python3 scripts/run.py export --investor "$b" | tail -1
python3 scripts/run.py review --investor "$b" | tail -1
python3 scripts/run.py verify --investor "$b" --skip-links 2>&1 | grep -E "^verify|problem\(s\)|^  - " | head -8
python3 data/collection/investors/tcv/scratch/align/csvdiff.py "$b"
npx tsx scripts/ingest-companies.ts "$b" --dry-run 2>&1 | grep -E "Plan|remov|Refus|Error" | head -6
npx tsx data/collection/investors/20vc/scratch/align/readback.ts "$b" 2>&1 | tail -6
