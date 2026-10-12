#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=jm
q() { echo "=== $1 :: $2"; python3 nq.py "$1" "$2" --all 2>&1 | tail -9; }
q tiz-inc '"Provi" "$15 million" Series A'
q make-cents-technologies-inc '"Cents" laundromat "seed" Bessemer 2020'
q make-cents-technologies-inc '"Cents" laundromat "Series A"'
q dyn365-inc '"Restaurant365" "$20 million"'
q 2tor-inc '"2tor" "$32.5 million"'
q reputationdefender-inc '"ReputationDefender" million funding Bessemer'
q dolores-labs-inc '"CrowdFlower" "$5 million" Bessemer'
q every-neighbor-deserves-kindness-inc '"Mural Health" seed "$7.5 million"'
q every-neighbor-deserves-kindness-inc '"Mural Health" "Series A"'
q hellorelish-inc '"Relish" app Eccles acquired'
q pinpt-inc '"Pinpoint" Haynie engineering analytics shut'
q strala-group-inc '"Strala" Bessemer'
