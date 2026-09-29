#!/usr/bin/env python3
"""Decode Google News article ids to publisher URLs in batches (PRO-167).

graduation-surfaces.decode() makes two throttled requests per article: the article
page (for its signature and timestamp) and one batchexecute call. The batchexecute
endpoint takes several RPCs in one request, each tagged with its own id, so this makes
one page request per article and ONE batchexecute per group of up to 20: about 1.05
requests per article instead of 2. Same throttle (shared_throttle "googlenews", 1/s
machine-wide), same cache format as judge_lib.NEWS ({gid: url}).

    from decode_batch import decode_many
    urls = decode_many(gids)          # {gid: url or None}

Cache: scratch/news-decoded.json (merged with any news-decoded*.json on read).
"""
import json, re, sys, urllib.parse
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import write_atomic  # noqa: E402
from shared_throttle import wait  # noqa: E402
import importlib.util
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(gs)
sys.argv = _argv

CACHE = HERE / "news-decoded.json"


def load_cache():
    d = {}
    for f in sorted(HERE.glob("news-decoded*.json")):
        try:
            d.update(json.loads(f.read_text()))
        except ValueError:
            pass
    return d


def _sig(gid):
    wait("googlenews", gs.RATES["googlenews"])
    code, page = gs.curl(f"https://news.google.com/rss/articles/{gid}?oc=5&hl=en-US&gl=US&ceid=US:en")
    sg = re.search(r'data-n-a-sg="([^"]+)"', page)
    ts = re.search(r'data-n-a-ts="([^"]+)"', page)
    if code != 200 or not (sg and ts):
        return None
    return int(ts.group(1)), sg.group(1)


def _batch(group):
    """group: [(gid, ts, sg)] -> {gid: url}"""
    reqs = []
    for k, (gid, ts, sg) in enumerate(group):
        inner = ["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1,
                                 None, None, None, None, None, 0, 1],
                                "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
                 gid, ts, sg]
        reqs.append(["Fbv4je", json.dumps(inner), None, str(k + 1)])
    body = urllib.parse.urlencode({"f.req": json.dumps([reqs])})
    wait("googlenews", gs.RATES["googlenews"])
    code, resp = gs.curl("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body,
                         headers=("Content-Type: application/x-www-form-urlencoded;charset=UTF-8",))
    out = {}
    if code != 200:
        return out
    # each response line: ["wrb.fr","Fbv4je","[\"garturlres\",\"<url>\",1]",null,null,null,"<id>"]
    for m in re.finditer(r'\["wrb\.fr","Fbv4je","(.*?)",null,null,null,"(\d+)"\]', resp):
        payload, rid = m.group(1), int(m.group(2))
        u = re.search(r'\\"garturlres\\",\\"(.*?)\\"', payload)
        if u and 1 <= rid <= len(group):
            out[group[rid - 1][0]] = u.group(1).encode().decode("unicode_escape")
    return out


def decode_many(gids, group_size=20, verbose=False):
    cache = load_cache()
    mine = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    res = {g: cache[g] for g in gids if g in cache}
    todo = [g for g in dict.fromkeys(gids) if g not in cache]
    pend = []
    for i, g in enumerate(todo):
        s = _sig(g)
        if s:
            pend.append((g, s[0], s[1]))
        if len(pend) >= group_size or (i == len(todo) - 1 and pend):
            got = _batch(pend)
            for gid, _, _ in pend:
                u = got.get(gid)
                if u is None:           # retry singly through the reference decoder
                    u = gs.decode(gid)
                res[gid] = u
                if u:
                    mine[gid] = u
            write_atomic(CACHE, json.dumps(mine, indent=1) + "\n")
            if verbose:
                print(f"decoded {len(res)}/{len(gids)}", flush=True)
            pend = []
    for g in gids:
        res.setdefault(g, None)
    return res


if __name__ == "__main__":
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    r = decode_many(ids, verbose=True)
    print(sum(1 for v in r.values() if v), "of", len(ids), "decoded")
