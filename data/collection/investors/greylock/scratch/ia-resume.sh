#!/bin/zsh
# Waits for the Internet Archive's CDX endpoint and then runs the two IA layers,
# re-trying while the eras are still thin. COLLECTION.md §5: an outage is a
# delay, not a gap; the pulls are idempotent and multi-pass.
cd /Users/erik/Developer/merit-capital
D=data/collection/investors/greylock/scratch
P=data/collection/investors/greylock/sources/wayback/parsed
for round in 1 2 3 4 5 6; do
  ok=0
  for i in $(seq 1 120); do
    code=$(curl -sS --max-time 20 -o /dev/null -w "%{http_code}" \
      "https://web.archive.org/cdx/search/cdx?url=greylock.com&limit=1&output=json" 2>/dev/null)
    if [ "$code" = "200" ]; then ok=1; break; fi
    sleep 30
  done
  [ "$ok" = "1" ] || { echo "round $round: IA never answered" >> $D/ia-resume.log; exit 1; }
  echo "round $round: IA answering at $(date -u +%FT%TZ)" >> $D/ia-resume.log
  python3 scripts/partner-roster.py greylock >> $D/roster.log 2>&1
  python3 scripts/wayback-pull.py greylock >> $D/wayback.log 2>&1
  n=$(ls $P 2>/dev/null | wc -l | tr -d ' ')
  echo "round $round done: $n parsed year files" >> $D/ia-resume.log
  [ "$n" -ge 18 ] && exit 0
  sleep 120
done
