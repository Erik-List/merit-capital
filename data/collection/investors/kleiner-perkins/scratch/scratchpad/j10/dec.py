import sys, os
os.chdir("/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch")
sys.path.insert(0, ".")
import judge_lib as jl
for line in open(sys.argv[1]):
    if not line.strip(): continue
    slug, sub = line.rstrip("\n").split("\t")
    try:
        u = jl.NEWS(slug, sub)
    except SystemExit as e:
        u = f"ERR {e}"
    with open("scratchpad/j10/dec.log", "a") as f:
        f.write(f"{slug}\t{sub}\t{u}\n")
