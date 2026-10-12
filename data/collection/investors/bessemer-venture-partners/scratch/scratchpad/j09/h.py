import judge_lib as jl
from judge_lib import ARCH, SITE, POST, W, FTS, NEWS, rnd, verdict
def C(slug, status=None, country=None, city=None, focus="NONE", note="", stage="undetermined", date=None,
      rounds=None, rng="below_1b", flags=(), src=None, cite=None, conf=None, ccite=None, extra=None, usd=None, **kw):
    fl = set(flags)
    ex = dict(extra or {})
    if focus == "NONE":
        ex["focus"] = None; focus = None
        note += " Outside the focus taxonomy."
    if city is None:
        fl.add("city_unknown")
    csrc = "model_knowledge"
    if country and country != "US":
        csrc = "web_verified"; ccite = ccite or ARCH(slug)
    return jl.cls(slug, status=status, rng=rng, usd=usd, stage=stage, stage_src=src, stage_cite=cite, stage_conf=conf,
                  entry_date=date, country=country, country_src=csrc, country_cite=ccite if csrc=="web_verified" else None,
                  city=city, focus=focus, flags=fl, note=note.strip(), rounds=[] if rounds is None else rounds,
                  extra=ex or None, **kw)
