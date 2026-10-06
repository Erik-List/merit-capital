"""Lead judgments 5 (2026-10-06): the four rows the final prepare left open."""
import json
import judge_lib as jl
ASOF = "2026-10-06"
_CLS = json.loads((jl.INV / "companies" / "classification.json").read_text())
_CLS = _CLS.get("bessemer-venture-partners", _CLS)


def SURF(slug, fix=None, **kw):
    out = jl.GRADLINES(slug, **kw)
    fix = dict(fix or {})
    for i, l in enumerate(out):
        k = l.split(":", 1)[0]
        if k in fix:
            out[i] = l.split(" -> ")[0] + " -> " + fix.pop(k)
    if fix:
        raise SystemExit(f"SURF({slug!r}): no line for {sorted(fix)}")
    return out


lines = [
    jl.cls("earthly", grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
           entry_date="2020-10",
           surfaces=SURF("earthly",
                         firm_note="the firm's own posts and listings -> no post or listing names Earthly (the row rests on the seed "
                                   "announcement); no later round named by the firm",
                         fix={"googlenews": "71 results on a common word; none reports a round of Earthly Technologies after the 2021 seed-plus",
                              "googlenews_firm": "1 result, the $6.5M seed-plus report of 2023-02-23 (a round closed in 2021 and named a seed extension); no Series A or later round",
                              "techcrunch": "30 results on a common word; the company's own is the 2023-02-23 report of the $6.5M seed-plus; no later round",
                              "crunchbase_news": "2 results, neither on a round of the company"}),
           note="S2A: not graduated. The only financing after the October 2020 seed is the $6.5M round closed in 2021 that "
                "TechCrunch (2023-02-23) calls a seed plus, led by Innovation Endeavors: a named seed extension, and below "
                "the $12M an unnamed round of that year needs; the absence test of 2026-10-06 found no Series A since."),
    jl.cls("synergy-computer-graphics", grad="not_graduated", grad_src="first_party",
           grad_cite=_CLS["synergy-computer-graphics"]["entry_stage_citation"], grad_conf="low", grad_asof=ASOF,
           entry_date="1984",
           surfaces=SURF("synergy-computer-graphics",
                         firm_note="the firm's archived listing for Synergy Computer Graphics (2005 to 2007) -> names the 1984 seed "
                                   "and the sale to Nippon Steel four years later, and no round between them",
                         formd_note="not applicable, a company sold in 1988, before electronic filing"),
           note="S2A: not graduated, at low confidence. The firm's own sentence names the 1984 seed and the sale of the "
                "operation to Nippon Steel four years later and no round between them, and no other source on the company "
                "was found; a financing the record does not give is possible."),
    jl.cls("m4-financial", country="US", flags=["country_prior"], clear=["country_unknown"],
           extra={"hq_country_confidence": "low"},
           note="Country inferred: the firm listed it in 2000 on its US e-commerce practice page with David Cowan as the "
                "deal partner; no source places the company."),
    jl.cls("utmost-technologies", country="US", flags=["country_prior"], clear=["country_unknown"],
           extra={"hq_country_confidence": "low"},
           note="Country inferred: the firm listed it in 2002 among its US optical companies with Rob Soni as the deal "
                "partner; no source places the company."),
]
jl.write("lead5", lines)
