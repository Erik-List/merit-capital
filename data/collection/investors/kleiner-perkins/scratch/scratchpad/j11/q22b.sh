cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j11
q(){ echo "=== $1 :: $2"; python3 nq.py "$1" "$2" --all 2>&1 | tail -14; }
q galy-co '"Galy" cotton raises'
q eridu-corp '"Eridu" AI networking raises'
q epiodyne-inc '"Epiodyne" funding'
q gruns-nutrition-inc '"Gruns" gummies raises'
q heartflow-inc '"HeartFlow" "Kleiner Perkins"'
q erecycling-group-inc '"eRecyclingCorps"'
q femtosense-inc '"Femtosense" Series A led'
echo DONE22
