"""Helpers for writing batch .out.jsonl lines (PRO-73 grind)."""
import json
from pathlib import Path
WHO = "agent-judge-pro73"
NEWS = "https://cherry.vc/news/"

def row(slug, status, city, country, stage, stage_src, focus, *, stage_cite=None, stage_conf="medium",
        rng="below_1b", usd=None, asof=None, val_src=None, val_cite=None, val_conf="high", public=None,
        grad=None, grad_src=None, grad_conf=None, flags=(), note="", city_src="model_knowledge",
        country_src="model_knowledge", country_cite=None, focus_src="model", rng_src=None, rng_cite=None, extra=None):
    r = {"slug": slug, "who": WHO, "status": status, "valuation_confidence": val_conf, "note": note,
         "flags": sorted(set(flags)), "valuation_range": rng, "valuation_usd": usd,
         "entry_stage": stage, "entry_stage_source": stage_src, "entry_stage_confidence": stage_conf,
         "hq_city": city, "hq_city_source": city_src if city else None,
         "hq_country": country, "hq_country_source": country_src,
         "focus": focus, "focus_source": focus_src}
    if city is None:
        r.pop("hq_city"); r.pop("hq_city_source")
    if stage_cite: r["entry_stage_citation"] = stage_cite
    if usd is not None:
        r.update({"valuation_asof": asof, "valuation_source": val_src, "valuation_range_source": val_src})
        if val_cite: r["valuation_citation"] = val_cite
    if rng_src: r["valuation_range_source"] = rng_src
    if rng_cite: r["valuation_range_citation"] = rng_cite
    if public is not None: r["is_public"] = public
    if country_cite: r["hq_country_citation"] = country_cite
    if stage == "Seed":
        r["seed_to_a_graduation"] = grad
        if grad_src: r["graduation_source"] = grad_src
        if grad_conf: r["graduation_confidence"] = grad_conf
    if extra: r.update(extra)
    return r

def verdict(slug, v, basis, ec, conf="high", cite=None):
    d = {"slug": slug, "verdict": v, "who": WHO, "evidence_class": ec, "basis": basis, "confidence": conf}
    if cite: d["citation"] = cite
    return d

def write(path, lines):
    Path(path).write_text("\n".join(json.dumps(l, ensure_ascii=False) for l in lines) + "\n")
    print(f"wrote {path}: {len(lines)} lines")
