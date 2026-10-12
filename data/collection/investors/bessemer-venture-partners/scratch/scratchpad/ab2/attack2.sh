#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=ab2
W='(valuation OR acquired OR acquisition OR raises OR funding OR IPO OR tender OR shuts)'
run() { echo "=== $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run legora "\"Legora\" (raises OR closes OR valuation) after:2026-09-20"
run mambu "\"Mambu\" $W after:2022-01-01"
run netlify "\"Netlify\" $W after:2022-01-01"
run optibus "\"Optibus\" $W after:2022-06-01"
run pave "\"Pave\" compensation $W after:2022-07-01"
run perplexity "\"Perplexity\" valuation (raises OR round OR funding OR tender) after:2025-10-01"
run ramp "\"Ramp\" fintech valuation (raises OR round OR tender) after:2026-06-10"
run restaurant365 "\"Restaurant365\" $W after:2023-06-01"
run sarvam "\"Sarvam\" valuation after:2026-08-01"
run shippo "\"Shippo\" $W after:2021-01-01"
run sila-nanotechnologies "\"Sila\" battery valuation after:2026-07-01"
run snapdeal "\"Snapdeal\" OR \"AceVector\" (IPO OR valuation OR listing OR acquired) after:2025-01-01"
run teleport "\"Teleport\" infrastructure OR identity OR access $W after:2022-06-01"
run torq "\"Torq\" security (valuation OR raises OR acquired) after:2026-01-01"
run trm-labs "\"TRM Labs\" (valuation OR raises OR acquired) after:2026-09-01"
run upside "\"Upside\" cash back OR cashback $W after:2022-05-01"
run viva-republica-toss "\"Toss\" \"Viva Republica\" (valuation OR IPO OR listing OR raises) after:2022-01-01"
run wildlife-studios "\"Wildlife Studios\" $W after:2020-06-01"
run yotpo "\"Yotpo\" $W after:2021-01-01"
run zopa "\"Zopa\" (valuation OR raises OR IPO OR acquired OR acquisition) after:2025-01-01"
