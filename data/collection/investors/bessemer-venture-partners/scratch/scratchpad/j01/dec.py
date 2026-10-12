import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import judge_lib as jl
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('#'): continue
    slug, sub = line.split('|', 1)
    try:
        print(slug, '|', sub, '|', jl.NEWS(slug.strip(), sub.strip()))
    except SystemExit as e:
        print(slug, '|', sub, '| ERR', e)
