#!/bin/sh
# Wait for the Common Crawl data host to stop refusing (403), then index, then fetch.
until [ "$(curl -s -o /dev/null -w '%{http_code}' -r 0-100 https://data.commoncrawl.org/cc-index/collections/CC-MAIN-2017-26/indexes/cluster.idx)" = "206" ]; do sleep 60; done
echo "data host answering $(date)"
python3 cc-cluster.py >> cc-cluster.log 2>&1
python3 cc-fetch.py '^kpcb:/+(portfolio|china/english/portfolio)' > cc-fetch-listings.log 2>&1
python3 cc-fetch.py '^(kpcb|kp):/+(china/)?(companies|company|portfolio|partnerships)' --first-per-path-year > cc-fetch-portfolio.log 2>&1
python3 cc-fetch.py '^(kpcb|kp):/+(team|partner|people|teams|china/(english/)?(team|partner))' --first-per-path-year > cc-fetch-team.log 2>&1
echo "all done $(date)"
