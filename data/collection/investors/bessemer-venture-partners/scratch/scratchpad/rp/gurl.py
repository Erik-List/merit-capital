#!/usr/bin/env python3
"""gurl.py <title-fragment>...: decode the Google News gid of matching titles in news-extra-rp.json to the article URL."""
import importlib.util, json, sys
from pathlib import Path
H = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("gs", H.parents[4] / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv[1:], sys.argv[:1]
spec.loader.exec_module(gs)
d = json.load(open(H / "news-extra-rp.json"))
seen = set()
for frag in argv:
    for k, v in d.items():
        for i in v:
            if frag.lower() in i["title"].lower() and i["gid"] not in seen:
                seen.add(i["gid"])
                print(i["date"], "|", i["title"][:110], "|", gs.decode(i["gid"]))
