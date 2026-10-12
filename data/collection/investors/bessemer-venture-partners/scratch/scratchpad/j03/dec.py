import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import judge_lib as jl
for a in sys.argv[1:]:
    slug, sub = a.split("|", 1)
    try:
        print(slug, "|", sub, "->", jl.NEWS(slug, sub))
    except SystemExit as e:
        print(slug, "|", sub, "!!", e)
