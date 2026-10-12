q() { echo "### $1 :: $2"; NQ_TAG=ab1a python3 nq.py "$1" "$2" 2>&1 | tail -${3:-10}; }
q inmobi '"InMobi" SoftBank stake buyback founders'
q front '"Front" "Social Capital" Series A "$10 million"'
q front 'Front shared inbox raises $10 million Series A' 8
q cultureamp '"Culture Amp" "Index Ventures"'
q handshake '"Handshake" "Garrett Lord" valuation'
q built '"Built Technologies" "Kleiner Perkins"'
q built '"Built" "Ilya Fushman"'
q cultureamp '"Culture Amp" "Ilya Fushman"'
q dji '"DJI" "$15 billion" valuation'
q anthropic '"Kleiner Perkins" Anthropic stake invested' 8
