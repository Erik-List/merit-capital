cd /Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch/
export NQ_TAG=j07
q(){ echo "=== $1 :: $2"; python3 nq.py "$1" "$2" 2>&1 | head -10; }
q voxel51 '"Voxel51" valuation billion funding'
q verse '"Verse" battery dispatch energy Series B valuation'
q zenzap '"ZenZap" Bessemer seed'
q wonderful '"Wonderful" AI agents Series C valuation headquarters'
q zoomin '"Zoomin" Bessemer seed 2018 Series A'
