import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import judge_lib as jl
args = sys.argv[1:]
for i in range(0, len(args), 2):
    try:
        print(args[i], "|", args[i+1], "->", jl.NEWS(args[i], args[i+1]))
    except SystemExit as e:
        print(args[i], "|", args[i+1], "ERR", e)
