#!/bin/sh
# Commit one book's company files (explicit pathspec; cross-rulings.json and graduation-surfaces.json only when this
# pass changed them), ingest, read back after (COLLECTION.md 9).  Usage: sh write.sh <book> "<what changed>"
set -e
b="$1"; D=data/collection/investors/$b; P="$D/companies/classification.json $D/companies/base.csv $D/companies/review.html"
git status --porcelain -- $D/companies/cross-rulings.json | grep -q . && P="$P $D/companies/cross-rulings.json"
git status --porcelain -- $D/scratch/graduation-surfaces.json | grep -q . && P="$P $D/scratch/graduation-surfaces.json"
git add -- $P
git commit -q -m "Verify-all pass after the NEA run (PRO-100): $b ($2)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- $P
git log --oneline -1
npx tsx scripts/ingest-companies.ts "$b" 2>&1 | tail -1
npx tsx data/collection/investors/20vc/scratch/align/readback.ts "$b" 2>&1 | tail -1
