import judge_lib as jl
for slug, sub in [("mirage", "Mirage raises $75M to continue"), ("mirage", "Captions rebrands as Mirage, expands")]:
    try:
        print(slug, sub, jl.NEWS(slug, sub), flush=True)
    except SystemExit as e:
        print("ERR", slug, sub, e, flush=True)
