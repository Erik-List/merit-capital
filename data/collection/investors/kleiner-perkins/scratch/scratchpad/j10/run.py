import subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor
os.chdir("/Users/erik/Developer/merit-capital/data/collection/investors/kleiner-perkins/scratch")
rows = [l.rstrip("\n").split("\t") for l in open(sys.argv[1]) if l.strip()]
def go(r):
    slug, q = r
    out = subprocess.run(["python3", "nq.py", slug, q, "--all"], capture_output=True, text=True,
                         env={**os.environ, "NQ_TAG": "j10"}).stdout
    with open("scratchpad/j10/nq.log", "a") as f:
        f.write(f"=== {slug} | {q}\n{out}\n")
with ThreadPoolExecutor(int(sys.argv[2]) if len(sys.argv)>2 else 3) as ex:
    list(ex.map(go, rows))
with open("scratchpad/j10/nq.log", "a") as f:
    f.write(f"DONE {sys.argv[1]}\n")
