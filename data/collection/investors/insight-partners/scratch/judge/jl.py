"""Tiny helpers for writing judged lines: keeps key names and shapes right."""
import json

IDEAS = "https://www.insightpartners.com/ideas/"


def city(c, src="model_knowledge", conf="high"):
    return {"hq_city": c, "hq_city_source": src, "hq_city_confidence": conf}


def country(cc, src="model_knowledge", conf="high"):
    return {"hq_country": cc, "hq_country_source": src, "hq_country_confidence": conf}


def stage(st, src, cite=None, conf="high"):
    d = {"entry_stage": st, "entry_stage_source": src, "entry_stage_confidence": conf}
    if cite:
        d["entry_stage_citation"] = cite
    return d


def post(slug):
    return IDEAS + slug.strip("/") + "/"


def value(usd, cite, asof, rng, src="web_verified", conf="high"):
    return {"valuation_usd": usd, "valuation_source": src, "valuation_citation": cite,
            "valuation_asof": asof, "valuation_range": rng, "valuation_confidence": conf}


def rnd(date, round_, amount=None, lead=None, firm=True, source=None, stype="firm"):
    return {"date": date, "round": round_, "amount_usd": amount, "lead": lead,
            "firm_in_round": firm, "source": source, "source_type": stype}


def write(path, lines):
    with open(path, "w") as f:
        for l in lines:
            f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(f"wrote {len(lines)} lines to {path}")
