#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j08
run(){ echo "######## $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run intercom '"Intercom" raises Kleiner Perkins 2018'
run k2-space '"K2 Space" Series D'
run instinct '"Instinct" Noah Shinn'
run mirendil '"Mirendil"'
run lotus-health-ai '"Lotus Health" raises'
run mind-robotics '"Mind Robotics" raises'
run nexthop-ai '"Nexthop AI" raises'
run manifest-os '"Manifest" immigration Dan Mishin'
run mindbloom '"Mindbloom" raises'
run nearside '"Nearside" raises'
run mai '"MAI" performance marketing AI agents seed'
run mashgin '"Mashgin" Kleiner Perkins'
run kapwing '"Kapwing" raises'
run leanplum '"Leanplum" raises'
run noteworth '"Noteworth" raises'
run mason-finance '"Mason Finance"'
run knack '"Knack" Halfteck'
run kuark-finance '"Kuark"'
