#!/usr/bin/env python3
"""TechCrunch own-search for a list of names (through the shared throttle). Prints titles + links + excerpts."""
import importlib.util, sys, json
from pathlib import Path
HERE = Path("/Users/erik/Developer/merit-capital/data/collection/investors/bessemer-venture-partners/scratch")
spec = importlib.util.spec_from_file_location("gs", HERE.parents[4] / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
ALL = "--all" in argv
argv = [a for a in argv if a != "--all"]
for name in argv:
    r = gs.wordpress("techcrunch", "https://techcrunch.com", name)
    print("###", name, r.get("status"), r.get("n"))
    for i in r.get("items", []):
        if i["names"] or ALL:
            print("  ", i["date"], "|", i["title"][:140], "|", i["link"])
            print("       ", i["excerpt"][:260])
