import re, json
import judge_lib as jl
N = {}
for f in ("b15", "b16"):
    for l in open(f"scratchpad/j08/{f}.txt"):
        m = re.match(r"### (\S+) \| .*? \| need=(\S+)", l)
        if m: N[m.group(1)] = set(m.group(2).split(","))
PRE = {"circadian","compumotor","dysan","galileo-electro-optics","gartner-group","harman-international-industries","four-phase-systems","icot","intersil-advanced-memory-systems"}
def C(slug, note, status=None, city=None, country=None, focus="SaaS", stage=None, ed=None, cite=None, conf="medium",
      src=None, rng=None, usd=None, vcite=None, asof=None, flags=(), rounds=None, ccite=None, csrc=None, extra=None, unres=False):
    n = N[slug]; fl = set(flags)
    if slug in PRE: fl.add("pre_spinout")
    kw = {}
    if "status" in n: kw["status"] = status
    if "valuation_range" in n or rng:
        kw["rng"] = rng or ("undetermined" if unres else "below_1b")
        if usd: kw.update(usd=usd, val_src="web_verified", val_cite=vcite, asof=asof, val_conf="high")
    if "hq_country" in n and country:
        kw["country"] = country
        if country != "US":
            kw["country_src"] = csrc or "web_verified"; kw["country_cite"] = ccite or jl.ARCH(slug)
    elif "hq_country" in n and not country: fl.add("country_unknown")
    if "hq_city" in n:
        if city: kw["city"] = city
        else: fl.add("city_unknown")
    if "entry_stage" in n:
        st = stage or "undetermined"
        kw["stage"] = st
        if st != "undetermined":
            kw.update(stage_src=src or "first_party", stage_cite=cite, stage_conf=conf)
        if ed: kw["entry_date"] = ed
        kw["rounds"] = rounds if rounds is not None else []
    e = dict(extra or {})
    if focus is None: e["focus"] = None
    return jl.cls(slug, focus=focus, flags=fl, note=note, extra=e or None, **kw)
