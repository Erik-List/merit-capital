#!/bin/zsh
# Waits for the Internet Archive to answer again, then runs the two IA layers.
# COLLECTION.md §5: an outage is a delay, not a gap -- the pulls are idempotent.
cd /Users/erik/Developer/merit-capital
D=data/collection/investors/greylock/scratch
for i in $(seq 1 240); do
  code=$(curl -sS --max-time 20 -o /dev/null -w "%{http_code}" \
    "https://web.archive.org/cdx/search/cdx?url=greylock.com&limit=1&output=json" 2>/dev/null)
  if [ "$code" = "200" ]; then
    echo "IA back at $(date -u +%FT%TZ) after $i probes" >> $D/ia-resume.log
    python3 scripts/partner-roster.py greylock >> $D/roster.log 2>&1
    python3 scripts/wayback-pull.py greylock >> $D/wayback.log 2>&1
    echo "IA layers done at $(date -u +%FT%TZ)" >> $D/ia-resume.log
    exit 0
  fi
  sleep 30
done
echo "IA never recovered in 120 min (last code $code)" >> $D/ia-resume.log
exit 1
