q() { echo "=== $1 :: $2"; NQ_TAG=stb python3 nq.py "$1" "$2" $3 2>&1 | tail -${4:-10}; }
q segment '"Segment.io" raises' --all
q segment '"Segment" $15 million Series A Accel Kleiner' --all
q ujet '"UJET" "Series A"' --all
q stripe '"Stripe" Visa American Express Kleiner 2015'
q watershed '"Watershed" Sequoia Kleiner Perkins 2021 climate startup' 
q rebellion-defense '"Rebellion Defense" Series A'
q turo '"RelayRides" $47 million Kleiner'
q veem '"Align Commerce" $12.5 million' --all
q remind '"Remind" $15 million Kleiner Perkins John Doerr' --all
q servicemax '"ServiceMax" $71 million' --all
q sessionm '"SessionM" Kleiner' --all
q onelogin '"OneLogin" $13 million' --all
q onelogin '"OneLogin" Charles River Ventures' --all
q plex '"Plex" media Kleiner Perkins investment' --all
q relateiq '"RelateIQ" Series B Kleiner' --all
q mist-systems '"Mist" Kleiner Perkins wireless $46 million' --all
q mist-systems '"Mist Systems" Series C' --all
q mindbloom '"Mindbloom" funding' --all
q stackbit '"Stackbit" seed' --all
q trace-data '"Trace" Netskope acquires' --all
q visly '"Visly"' --all
q willo '"Willo" Kleiner Perkins' --all
q xendit '"Xendit" Series B Accel' 
q productboard '"productboard" Series A Kleiner Perkins leads'
q newsela '"Newsela" $15 million'
q transmedics '"TransMedics" $36 million'
q pinterest '"Pinterest" Kleiner Perkins investor stake'
