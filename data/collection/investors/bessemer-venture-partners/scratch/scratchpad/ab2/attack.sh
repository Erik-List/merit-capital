#!/bin/zsh
cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=ab2
W='(valuation OR acquired OR acquisition OR raises OR funding OR IPO OR tender OR shuts)'
run() { echo "=== $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | tail -16; }
run ada "\"Ada\" chatbot OR \"customer service\" $W after:2024-01-01"
run anthropic "\"Anthropic\" valuation (round OR tender OR funding) after:2026-05-01"
run betterment "\"Betterment\" $W after:2024-06-01"
run boom-supersonic "\"Boom Supersonic\" (valuation OR raises OR funding) after:2026-01-01"
run captivateiq "\"CaptivateIQ\" $W after:2023-01-01"
run claroty "\"Claroty\" (valuation OR acquired OR IPO OR raises) after:2026-02-01"
run clio "\"Clio\" legal (valuation OR raises OR IPO OR tender) after:2025-10-01"
run cognition "\"Cognition\" Devin (valuation OR raises OR tender) after:2026-08-15"
run devo "\"Devo\" security $W after:2022-01-01"
run doubleai "\"doubleAI\" (valuation OR raises OR funding OR Series)"
run electric "\"Electric\" \"IT support\" OR \"IT management\" $W after:2022-06-01"
run evenup "\"EvenUp\" (valuation OR raises OR acquired OR tender) after:2025-11-01"
run farther "\"Farther\" wealth (valuation OR raises OR acquired) after:2026-05-01"
run fireworks "\"Fireworks AI\" (valuation OR raises OR acquired OR tender) after:2026-07-01"
run glossgenius "\"GlossGenius\" OR \"Genius\" beauty (valuation OR raises OR Series D) after:2026-06-01"
run halter "\"Halter\" cow OR collar (valuation OR raises OR IPO) after:2026-04-01"
run imply "\"Imply\" Druid $W after:2022-06-01"
run klook "\"Klook\" (IPO OR NYSE OR shares OR debut OR valuation) after:2025-11-20"
run legora "\"Legora\" (valuation OR raises OR tender OR acquired) after:2026-03-01"
