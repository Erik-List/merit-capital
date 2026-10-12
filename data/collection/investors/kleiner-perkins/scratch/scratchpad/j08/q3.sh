#!/bin/bash
cd /Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch
export NQ_TAG=j08
run(){ echo "######## $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run level '"Level Money"'
run kingnet '"Kingnet" Kleiner'
run limei '"Limei" mobile advertising'
run madhouse '"Madhouse" mobile advertising China'
run manzuo '"Manzuo"'
run meican '"Meican"'
run nearside '"Nearside" acquired'
run n3twork '"N3TWORK"'
run neos-geosolutions '"NEOS GeoSolutions"'
run new-vine-logistics '"New Vine Logistics"'
run next-autoworks '"Next Autoworks"'
run miaozhen-systems '"Miaozhen"'
run leo '"Leo" app Kleiner Perkins Megan Quinn'
