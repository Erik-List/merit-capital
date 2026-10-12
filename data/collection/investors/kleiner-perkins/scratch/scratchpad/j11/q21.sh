cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j11
q(){ echo "=== $1 :: $2"; python3 nq.py "$1" "$2" --all 2>&1 | tail -16; }
q counsel-ai-corp '"Harvey" legal AI valuation billion'
q baron-app-inc '"Cameo" Galanis valuation'
q arsenal-biosciences-inc '"ArsenalBio" Kleiner Perkins'
q beam-technologies-inc '"Beam Dental" Kleiner Perkins'
q asapp-inc '"ASAPP" "Kleiner Perkins"'
q alpha-design-ai-inc '"Alpha Design AI"'
q biomine-inc '"BioMine" Kleiner'
q borderx-lab-inc '"BorderX" funding'
q cellpro-incorporated '"CellPro" Baxter bankruptcy'
echo DONE21
