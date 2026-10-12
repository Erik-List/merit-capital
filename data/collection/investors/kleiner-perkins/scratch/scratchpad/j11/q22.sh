cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j11
until grep -q DONE21 scratchpad/j11/q21.log; do sleep 5; done
q(){ echo "=== $1 :: $2"; python3 nq.py "$1" "$2" --all 2>&1 | tail -14; }
q eridu-corp '"Eridu" AI networking raises'
q epiodyne-inc '"Epiodyne" funding'
q galy-co '"Galy" cotton raises'
q gruns-nutrition-inc '"Grüns" gummies raises'
q heartflow-inc '"HeartFlow" "Kleiner Perkins"'
q grail-inc '"Grail" "Kleiner Perkins" Series'
q erecycling-group-inc '"eRecyclingCorps"'
q femtosense-inc '"Femtosense" Series A led'
echo DONE22
