#!/bin/sh
# Commit one sibling book's three company files (explicit pathspec), ingest, read back after (COLLECTION.md 9).
# Usage: sh write.sh <book> "<rows changed>"     (run from the repo root, after gate.sh passed)
set -e
b="$1"; C=data/collection/investors/$b/companies
git commit -q -m "PRO-100: $b aligned from the NEA run ($2), rule 10

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- $C/classification.json $C/base.csv $C/review.html
git log --oneline -1
npx tsx scripts/ingest-companies.ts "$b" 2>&1 | tail -1
npx tsx data/collection/investors/20vc/scratch/align/readback.ts "$b" 2>&1 | tail -1
