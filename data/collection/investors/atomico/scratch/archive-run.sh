#!/bin/zsh
# Archive pulls in priority order; each waits on the machine-wide IA throttle.
cd /Users/erik/Developer/merit-capital
S=data/collection/investors/atomico/scratch
echo "== cms-pull $(date -u)"; python3 $S/cms-pull.py 2>&1 | tail -3
echo "== team-pull $(date -u)"; python3 $S/team-pull.py 2>&1 | tail -12
echo "== partner-roster $(date -u)"; python3 scripts/partner-roster.py atomico 2>&1 | tail -8
echo "== wayback-pull $(date -u)"; python3 scripts/wayback-pull.py atomico 2>&1 | tail -40
echo "== insights-pull $(date -u)"; python3 $S/insights-pull.py 2>&1 | tail -3
echo "== done $(date -u)"
