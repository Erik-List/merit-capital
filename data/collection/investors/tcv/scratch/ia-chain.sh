#!/bin/zsh
# PRO-169: the Internet Archive leg, run once the machine-wide cooldown has ended.
cd /Users/erik/Developer/merit-capital
python3 scripts/partner-roster.py tcv
python3 data/collection/investors/tcv/scratch/roster-old-pages.py
python3 data/collection/investors/tcv/scratch/parse-cc-tcv.py
python3 data/collection/investors/tcv/scratch/roster-curate.py
python3 data/collection/investors/tcv/scratch/pull-archive-tcv.py alpha2000 sector2003 idx2007 all2012
python3 data/collection/investors/tcv/scratch/news-layer.py
echo "ia-chain done"
