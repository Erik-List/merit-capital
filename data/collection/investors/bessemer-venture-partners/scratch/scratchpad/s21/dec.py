import sys
sys.path.insert(0, '.')
import judge_lib as jl
slug, sub = sys.argv[1], sys.argv[2]
print(jl.NEWS(slug, sub))
