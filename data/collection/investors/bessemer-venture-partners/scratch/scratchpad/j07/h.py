import re, json
import judge_lib as jl
N = {}
for f in ("b13", "b14"):
    for l in open(f"scratchpad/j07/{f}.txt"):
        m = re.match(r"### (\S+) \| .*? \| need=(\S+)", l)
        if m: N[m.group(1)] = set(m.group(2).split(","))
PRE = {"businessland"} - {"businessland"}
def cite_for(slug):
    for f in (jl.ARCH, jl.SITE):
        try: return f(slug)
        except SystemExit: pass
    raise SystemExit("no citation for "+slug)
def C(slug, note, status=None, city=None, country=None, focus="SaaS", stage=None, ed=None, cite=None, conf="medium",
      src=None, rng=None, usd=None, vcite=None, asof=None, flags=(), rounds=None, ccite=None, csrc=None, extra=None, unres=False,
      grad=None, gsrc=None, gcite=None, gconf=None, dispute_country=False):
    n = N[slug]; fl = set(flags)
    kw = {}
    if "status" in n: kw["status"] = status
    if "valuation_range" in n or rng:
        kw["rng"] = rng or ("undetermined" if unres else "below_1b")
        if usd: kw.update(usd=usd, val_src="web_verified", val_cite=vcite, asof=asof, val_conf="high")
        if usd and asof and asof < "2024-10-01": fl.add("stale")
    if ("hq_country" in n or dispute_country) and country:
        kw["country"] = country
        if country != "US":
            kw["country_src"] = csrc or "web_verified"; kw["country_cite"] = ccite or cite_for(slug)
        if dispute_country: fl.add("model_disputes_source")
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
    if grad:
        kw.update(grad=grad, grad_src=gsrc, grad_cite=gcite, grad_conf=gconf)
        if rounds is not None: kw["rounds"] = rounds
    e = dict(extra or {})
    if focus is None: e["focus"] = None
    return jl.cls(slug, focus=focus, flags=fl, note=note, extra=e or None, **kw)
