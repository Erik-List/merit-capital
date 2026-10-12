import sys; sys.path.insert(0, "/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch")
import judge_lib as jl, time
for slug, sub in [("mirendil", "SiliconANGLE"), ("mirendil", "Unite.AI"), ("mirendil", "Pulse 2.0")]:
    t = time.time()
    try:
        print(slug, sub, jl.NEWS(slug, sub), round(time.time() - t), flush=True)
    except SystemExit as e:
        print(slug, sub, "ERR", e, flush=True)
