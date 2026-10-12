cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j11
until grep -q "=== gruns" scratchpad/j11/q22.log; do sleep 3; done
pkill -f "scratchpad/j11/q22b.sh"; pkill -f 'nq.py gruns-nutrition-inc'
q(){ echo "=== $1 :: $2"; python3 nq.py "$1" "$2" --all 2>&1 | tail -14; }
q erecycling-group-inc '"eRecyclingCorps"'
q gruns-nutrition-inc '"Gruns" gummies raises'
echo DONE22C
