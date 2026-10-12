cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
while IFS=$'\t' read -r slug q; do
  echo "=== $slug :: $q"
  NQ_TAG=ab1b python3 nq.py "$slug" "$q" 2>&1 | tail -16
done < scratchpad/ab1b/queries.tsv
