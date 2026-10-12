import sys,os
sys.path.insert(0,'.')
import judge_lib as jl
for a in sys.argv[1:]:
    slug,sub=a.split('::')
    try: print(slug,'|',sub,'|',jl.NEWS(slug,sub))
    except SystemExit as e: print('ERR',slug,sub,e)
