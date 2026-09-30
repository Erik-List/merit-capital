#!/bin/sh
# Pre-write gate for one book in the verify-all pass (COLLECTION.md 9): record the book's gathered lines once
# (apply.py), export, review, plain verify, the cell diff against HEAD, the ingest dry run, the readback before.
# Usage: sh gate.sh <book>        (run from the repo root)
set -e
b="$1"; K=data/collection/investors/new-enterprise-associates/scratch/verify-all
python3 $K/apply.py "$@" | grep -v "^   " | tail -4
python3 scripts/run.py export --investor "$b" | tail -1
python3 scripts/run.py review --investor "$b" | tail -1
python3 scripts/run.py verify --investor "$b" --skip-links 2>&1 | grep -E "^verify|problem\(s\)|^  - " | head -8
python3 data/collection/investors/tcv/scratch/align/csvdiff.py "$b"
npx tsx scripts/ingest-companies.ts "$b" --dry-run 2>&1 | grep -E "Plan|remov|Refus|Error" | head -6
npx tsx data/collection/investors/20vc/scratch/align/readback.ts "$b" 2>&1 | tail -8
