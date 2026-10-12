#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j08
run(){ echo "######## $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run nearside '"Nearside" OR "Hatch" Thomson Nguyen'
run manifest-os '"Manifest" immigration law AI raises'
run mindbloom '"Mindbloom" raises'
run mai '"MAI" performance marketing AI'
run noteworth '"Noteworth"'
run mason-finance '"Mason Finance"'
run mashgin '"Mashgin" Kleiner'
