"""Print publisher URLs for (slug, headline substring) pairs: NQ_TAG=j05 python3 scratchpad/j05/dec.py slug 'sub' [slug 'sub' ...]"""
import sys
sys.path.insert(0, ".")
import judge_lib as jl
a = sys.argv[1:]
for s, sub in zip(a[::2], a[1::2]):
    try:
        print(s, "|", sub, "->", jl.NEWS(s, sub))
    except SystemExit as e:
        print(s, "|", sub, "-> ERR", e)
