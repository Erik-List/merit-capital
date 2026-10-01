"""Grind helpers for PRO-82 on top of judge_lib: C() emits one classification line with only the keys the
queue asked for (COLLECTION.md s8: extra keys clobber filing-grade facts), unless the key is named in
`dispute` (a deliberate override of a pre-filled value). focus, flags, note and funding_rounds always pass."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", H / "judge_lib.py")
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
Q = {i["slug"]: i for i in json.load(open(H / "queue" / "queue.json"))}
NEED_OF = {"status": "status", "rng": "valuation_range", "usd": "valuation_range", "stage": "entry_stage",
           "country": "hq_country", "city": "hq_city", "grad": "seed_to_a_graduation"}
DEP = {"stage": ("stage_src", "stage_cite", "stage_conf"), "usd": ("val_src", "val_cite", "asof", "val_conf"),
       "rng": ("val_conf",), "country": ("country_src", "country_cite"), "city": ("city_src",),
       "grad": ("grad_src", "grad_cite", "grad_conf", "grad_asof", "surfaces")}
post, postdate, page, arch, narch, sib, news, gsurl, rnd, verdict, ev, nqurl = (jl.post, jl.postdate, jl.page, jl.arch, jl.narch,
                                                                               jl.sib, jl.news, jl.gsurl, jl.rnd, jl.verdict, jl.ev, jl.nqurl)
DROPPED = []
ERRORS = []


def _safe(fn):
    def w(*a, **k):
        try:
            return fn(*a, **k)
        except (KeyError, StopIteration) as e:
            ERRORS.append(f"{fn.__name__}{a}: {str(e)[:260]}")
            return "MISSING"
    return w


post, postdate, page, arch, narch, sib, news, gsurl, nqurl = (_safe(f) for f in (post, postdate, page, arch, narch, sib, news, gsurl, nqurl))


def C(slug, dispute=(), **kw):
    need = set(Q[slug]["need"]) if slug in Q else set()
    known = (Q.get(slug) or {}).get("known") or {}
    for k, n in NEED_OF.items():
        if k in kw and n not in need and k not in dispute and not (k == "grad" and "stage" in dispute):
            # entry_date rides with the graduation / stage; a pre-filled column is left alone
            DROPPED.append((slug, k, kw[k], known.get(n)))
            kw.pop(k)
            for d in DEP.get(k, ()):
                kw.pop(d, None)
    if "usd" not in kw and "rng" not in kw:
        for d in DEP["usd"]:
            kw.pop(d, None)
    if dispute:
        fl = set(kw.get("flags") or ())
        if any(d in ("status", "country", "rng", "usd") for d in dispute):
            fl.add("model_disputes_source")
        if "stage" in dispute and known.get("entry_stage_source") in ("formd_band", "formd_structural"):
            fl.add("stage_disputes_band")
        kw["flags"] = sorted(fl)
    return jl.cls(slug, **kw)


def write(name, lines):
    if ERRORS:
        print(f"{len(ERRORS)} lookup error(s), nothing written:")
        for e in ERRORS:
            print("  -", e)
        return
    if DROPPED:
        print("dropped (not asked, not disputed):", [(s, k, v, f"known={kn}") for s, k, v, kn in DROPPED if str(v) != str(kn)][:40])
    jl.write(name, lines)
