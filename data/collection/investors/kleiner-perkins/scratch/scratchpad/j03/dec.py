import judge_lib as jl
for slug, sub in [("inworld", "joins metaverse"), ("inworld", "raises $50M"), ("juna-ai", "raises $7.5M in seed")]:
    try:
        print(slug, sub, jl.NEWS(slug, sub), flush=True)
    except SystemExit as e:
        print("ERR", slug, sub, e, flush=True)
