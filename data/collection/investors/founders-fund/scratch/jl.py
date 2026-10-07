"""Judgment-file helpers: V() a membership verdict line, C() a classification line.
Each judgments-*.py file imports these, states its rulings, and writes one
queue/<tag>.out.jsonl that `run.py record` validates and merges."""
import json
from pathlib import Path
H = Path(__file__).resolve().parent
LINES = []
def V(slug, verdict, cls, conf, basis, cite=None):
    r = {"slug": slug, "verdict": verdict, "who": "agent", "evidence_class": cls, "confidence": conf, "basis": basis}
    if cite: r["citation"] = cite
    LINES.append(r)
def NM(slug, basis, cls="knowledge", conf="high", cite=None): V(slug, "not_member", cls, conf, basis, cite)
def C(slug, **kw):
    kw = {k: v for k, v in kw.items() if v is not None or k in ("valuation_usd", "seed_to_a_graduation", "hq_city")}
    LINES.append({"slug": slug, **kw})
def write(tag):
    p = H / "queue" / f"{tag}.out.jsonl"
    p.write_text("".join(json.dumps(l, ensure_ascii=False) + "\n" for l in LINES))
    print(f"{p.name}: {len(LINES)} lines ({sum(1 for l in LINES if 'verdict' in l)} verdicts)")

# ---- need-aware row helper -------------------------------------------------
import csv, re
_Q = {i["slug"]: i for i in (lambda q: q if isinstance(q, list) else q["items"])(json.loads((H / "queue/queue.json").read_text()))}
_INV = H.parents[1]
def sibling_val(investor, slug):
    c = json.loads((_INV / investor / "companies/classification.json").read_text()).get(slug) or {}
    r = json.loads((_INV / investor / "companies/resolved.json").read_text()).get(slug) or {}
    m = {**r, **c}
    return {k: m.get(k) for k in ("valuation_usd", "valuation_range", "valuation_source", "valuation_citation", "valuation_asof", "valuation_confidence") if m.get(k) is not None}
def R(slug, st=None, city=None, focus=None, stage=None, src="model", conf="medium", note=None, co=None, vr=None,
      usd=None, vcite=None, vasof=None, val_from=None, edate=None, scite=None, flags=None, dispute=(), stale=False,
      co_src="model_knowledge", city_src="model_knowledge", rounds=None, **extra):
    need = set(_Q[slug]["need"]) if slug in _Q else set()
    d = set(dispute)
    out, fl = {}, list(flags or [])
    if st and ("status" in need or "status" in d): out["status"] = st
    if city is not None or "hq_city" in need:
        if city: out.update(hq_city=city, hq_city_source=city_src)
        else: fl.append("city_unknown")
    if co and ("hq_country" in need or "hq_country" in d): out.update(hq_country=co, hq_country_source=co_src)
    if stage and ("entry_stage" in need or "entry_stage" in d):
        out.update(entry_stage=stage)
        if stage != "undetermined":
            out.update(entry_stage_source=src, entry_stage_confidence=conf)
            if scite: out["entry_stage_citation"] = scite
        if "entry_stage" in d and "entry_stage" not in need: fl.append("stage_disputes_band")
    if edate: out["entry_date"] = edate
    if "valuation_range" in need or "valuation_range" in d or usd or val_from:
        if val_from:
            out.update(sibling_val(*val_from))
        elif usd:
            rng = "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"
            out.update(valuation_usd=usd, valuation_range=rng, valuation_source="web_verified", valuation_citation=vcite, valuation_asof=vasof, valuation_confidence="high")
        else:
            out.update(valuation_range=vr or "below_1b")
            if (st or "") in ("acquired", "defunct", "unknown"): out["valuation_usd"] = None
    if stale: fl.append("stale")
    if focus: out.update(focus=focus, focus_source="model")
    if note: out["note"] = note
    if rounds: out["funding_rounds"] = rounds
    if fl: out["flags"] = sorted(set(fl))
    out.update(extra)
    C(slug, **out)
CON, IND, FIN, AI, HB, SAAS, CRY, DATA, MED, CLI, SEC, DEV = ("Consumer & Marketplaces", "Industrial & Robotics", "Fintech & Payments", "AI & Applied AI",
    "Healthcare & Bio", "SaaS", "Crypto & Web3", "Data Infrastructure", "Media, Gaming & Advertising", "Climate & Energy", "Security", "DevTools & APIs")
