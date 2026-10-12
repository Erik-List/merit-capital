import sys, os
sys.path.insert(0, '/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch')
os.environ.setdefault('NQ_TAG','j04')
import judge_lib as jl
L = [
 ("mind-robotics","for industrial AI-powered robots"),
 ("mind-robotics","Mind Robotics raises Series A to develop"),
 ("nala","NALA raises $10M seed to build Revolut"),
 ("nala","NALA raises $40m series A funding"),
 ("luxury-presence","Luxury Presence Raises $22M Series C"),
 ("luxury-presence","raises $19.2M"),
 ("manychat","Manychat taps $140M"),
 ("miter","Miter, the AI Platform for Construction, Raises $40 Million"),
 ("moonvalley","Moonvalley Raises Additional $84 Million to Scale Ambitious Vision for Licensed AI Video Model - Business Wire"),
 ("lentra","HDFC Bank writes cheque"),
 ("omsignal","OMsignal announces $13 million"),
 ("modelcode","Modelcode.ai founder Michael Fertik expands"),
 ("onyx-security","New York-based Onyx Security lands"),
 ("neo","Neo Launches with $100M"),
]
for s, sub in L:
    try:
        print(s, '|', sub, '|', jl.NEWS(s, sub), flush=True)
    except SystemExit as e:
        print(s, '|', sub, '| ERR', e, flush=True)
