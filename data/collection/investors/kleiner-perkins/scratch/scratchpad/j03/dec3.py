import judge_lib as jl
for slug, sub in [
                  ("nooks", "announces $43M Series B"), ("maxima", "Seed and Series A to Transform")]:
    try:
        print(slug, sub, jl.NEWS(slug, sub), flush=True)
    except SystemExit as e:
        print("ERR", slug, sub, e, flush=True)
