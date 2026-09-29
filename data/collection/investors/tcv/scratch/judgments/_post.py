"""post(*words) -> the capture URL of TCV's own post whose slug contains every word (earliest capture).
Raises if none or several distinct slugs match, so a judgment can never cite the wrong post silently."""
import json
from pathlib import Path
_P = json.load(open(Path(__file__).resolve().parents[1] / "tcv-posts.json"))
def post(*words):
    hits = sorted((p["ts"], s, p["capture"]) for s, p in _P.items() if all(w in s for w in words))
    if not hits:
        raise KeyError(f"no TCV post for {words}")
    slugs = {h[1] for h in hits}
    if len(slugs) > 1:
        raise KeyError(f"several TCV posts for {words}: {sorted(slugs)[:4]}")
    return hits[0][2]
