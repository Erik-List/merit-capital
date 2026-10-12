#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=jm
q() { echo "=== $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -12; }
q birch-solutions-inc '"Fern" SDK Postman acquires'
q birch-solutions-inc '"Fern" Series A Bessemer SDK'
q every-neighbor-deserves-kindness-inc '"Mural Health" raises'
q pinpt-inc '"Pinpoint" engineering Austin Series A Bessemer'
q hellorelish-inc '"Relish" relationship app shuts down OR acquired'
q tiz-inc '"Provi" raises Bessemer alcohol marketplace'
q make-cents-technologies-inc '"Cents" raises Series A laundromat'
q dyn365-inc '"Restaurant365" Bessemer Tiger Global 2018'
q recover-together-inc '"Groups" opioid Bessemer Series A'
q reputationdefender-inc '"ReputationDefender" Bessemer Kleiner Series B'
q 2tor-inc '"2tor" Bessemer $32.5 million'
q dolores-labs-inc '"CrowdFlower" "Series A" Trinity Bessemer'
q dolores-labs-inc '"Figure Eight" Appen acquires'
q flexcorp-inc '"FlexFactor" Bessemer'
q strala-group-inc '"Strala" claims Series B'
q k2-global-consulting-inc '"K2 Intelligence" Bessemer Kroll investment'
q adaptive-planning-inc '"Adaptive Planning" $45 million Bessemer'
q hyper-labs-inc '"Hyperscience" valuation'
