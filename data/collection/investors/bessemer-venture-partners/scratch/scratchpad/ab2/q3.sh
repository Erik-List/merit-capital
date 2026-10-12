#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=ab2
run() { echo "=== $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -14; }
run klook "\"Klook\" (unicorn OR \"valuation\" OR \"valued at\") before:2020-01-01"
run klook "\"Klook\" valuation (IPO OR \"valued at\" OR funding) after:2023-11-01 before:2025-12-31"
run devo "\"Devo Technology\" OR \"Devo\" SIEM (merger OR merges OR acquired OR acquires OR Strike48 OR layoffs) after:2024-01-01"
run upside "\"GetUpside\" (raises OR funding OR Series OR Bessemer)"
run betterment "\"Betterment\" \"Series A\" Bessemer before:2012-01-01"
run claroty "\"Claroty\" (stealth OR \"Series A\" OR Bessemer) before:2017-06-01"
run trm-labs "\"TRM Labs\" (\"Series A\" OR Bessemer) before:2021-12-01"
run viva-republica-toss "\"Viva Republica\" OR \"Toss\" PayPal Bessemer 48 million before:2017-12-31"
run boom-supersonic "\"Boom Supersonic\" (\"Series B\" OR raises OR funding OR Bessemer) before:2021-12-31"
run captivateiq "\"CaptivateIQ\" Bessemer"
run wildlife-studios "\"Wildlife Studios\" OR \"Top Free Games\" Bessemer"
run electric "\"Electric\" electric.ai OR \"Electric AI\" (acquired OR acquisition OR layoffs OR valuation OR raises) after:2022-06-01"
