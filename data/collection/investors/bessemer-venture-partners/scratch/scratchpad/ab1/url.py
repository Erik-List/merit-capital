import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import judge_lib as jl
slug = sys.argv[1]
for sub in sys.argv[2:]:
    try:
        print(sub, "->", jl.NEWS(slug, sub))
    except SystemExit as e:
        print(sub, "-> ERR", e)
