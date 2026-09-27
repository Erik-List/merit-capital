#!/bin/zsh
# Wait for the machine-wide IA cooldown to clear, then enumerate captures per domain
# through the shared throttle (scripts/ia_fetch.py). Never fetches during a cooldown.
cd /Users/erik/Developer/merit-capital/data/collection/investors/headline
until python3 -c "import sys; sys.path.insert(0,'/Users/erik/Developer/merit-capital/scripts'); import ia_fetch; sys.exit(0 if ia_fetch.blocked()<=0 else 1)"; do sleep 30; done
echo "IA clear at $(date)"
for d in eventures.vc headline.com eventures.com headline.vc bvcapital.com; do
  python3 scratch/cdx-enum.py $d
done
echo "done at $(date)"
