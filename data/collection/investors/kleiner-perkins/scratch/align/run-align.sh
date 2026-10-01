#!/bin/bash
# Align the stale sibling rows found by the Kleiner Perkins run (PRO-99) and re-ingest each book through the
# COLLECTION.md s9 gate, one book at a time. A book is SKIPPED (nothing written to the database) when: it is in flight,
# its company files are uncommitted, its own verify is not clean before or after the lines, the readback before is not
# exact, record rejects a line, or the dry run would remove a row. Every outcome is one line in results.txt.
ROOT=/Users/erik/Developer/merit-capital; cd "$ROOT" || exit 1
HERE=data/collection/investors/kleiner-perkins/scratch/align
RB=data/collection/investors/20vc/scratch/align/readback.ts
: > $HERE/results.txt
for kit in $HERE/*.jsonl; do
  book=$(basename "$kit" .jsonl); B=data/collection/investors/$book; n=$(grep -c . "$kit")
  log=$HERE/$book.log; : > "$log"
  skip() { echo "SKIPPED $book ($n rows): $1" | tee -a $HERE/results.txt; }
  [ -f $B/scratch/in-flight.json ] && { skip "in flight"; continue; }
  [ -n "$(git status --short -- $B/companies/classification.json $B/companies/base.csv $B/companies/review.html)" ] && { skip "uncommitted company files"; continue; }
  python3 scripts/run.py verify --investor $book >> "$log" 2>&1 || { skip "its own verify is not clean before the lines"; continue; }
  npx tsx $RB $book >> "$log" 2>&1; tail -1 "$log" | grep -q "missing 0, extra 0, differing cells 0" || { skip "readback before is not exact: $(tail -1 "$log")"; continue; }
  cp $B/companies/classification.json /tmp/kp-align-$book-classification.json; cp $B/companies/base.csv /tmp/kp-align-$book-base.csv; cp $B/companies/review.html /tmp/kp-align-$book-review.html
  restore() { cp /tmp/kp-align-$book-classification.json $B/companies/classification.json; cp /tmp/kp-align-$book-base.csv $B/companies/base.csv; cp /tmp/kp-align-$book-review.html $B/companies/review.html; }
  python3 scripts/run.py record --investor $book "$kit" >> "$log" 2>&1
  if grep -qi "REJECTED\|refus" "$log"; then restore; skip "record rejected a line (see $book.log)"; continue; fi
  python3 scripts/run.py export --investor $book >> "$log" 2>&1 || { restore; skip "export refused"; continue; }
  python3 scripts/run.py review --investor $book >> "$log" 2>&1
  python3 scripts/run.py verify --investor $book >> "$log" 2>&1 || { restore; skip "verify not clean after the lines (see $book.log)"; continue; }
  npx tsx scripts/ingest-companies.ts $book --dry-run > $HERE/$book.dry 2>&1
  grep -q ", 0 removed" $HERE/$book.dry || { restore; skip "dry run would remove rows: $(grep Plan $HERE/$book.dry)"; continue; }
  npx tsx scripts/ingest-companies.ts $book >> "$log" 2>&1 || { skip "INGEST FAILED after local changes (files left changed; see $book.log)"; continue; }
  npx tsx $RB $book >> "$log" 2>&1
  if tail -1 "$log" | grep -q "missing 0, extra 0, differing cells 0"; then
    git commit -q -m "PRO-99: $book aligned to the Kleiner Perkins run's cited evidence ($n row(s), rule 10), re-ingested

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- $B/companies/classification.json $B/companies/base.csv $B/companies/review.html >> "$log" 2>&1
    echo "ALIGNED $book ($n rows): re-ingested, readback exact, commit $(git log --oneline -1 | cut -c1-8)" | tee -a $HERE/results.txt
  else
    echo "STOP $book: readback after is not exact: $(tail -1 "$log")" | tee -a $HERE/results.txt; break
  fi
done
echo "done" >> $HERE/results.txt
