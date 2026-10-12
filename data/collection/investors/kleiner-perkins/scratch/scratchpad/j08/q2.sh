#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j08
run(){ echo "######## $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run inrix '"INRIX" Kleiner Perkins'
run insidesales '"InsideSales.com" Kleiner Perkins'
run insidesales '"XANT" acquired'
run ip-unity '"IP Unity"'
run izon-formerly-ophthonix '"Ophthonix"'
run izumi '"iZumi Bio"'
run jawbone '"Jawbone" Kleiner Perkins'
run jhl-biotech '"JHL Biotech"'
run jiangsu-yangtze-river-delta-fine-chemical '"Delta Technology Holdings"'
run kaiima '"Kaiima"'
run kingnet '"KingNet" game'
run kilowatt-financial '"Kilowatt Financial"'
run lifesquare '"Lifesquare"'
run instart-logic '"Instart Logic" Kleiner'
