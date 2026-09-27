#!/usr/bin/env python3
"""Expand compact judgments into gate-valid output lines for `run.py record`.

A judgments file (scratch/judgments/<name>.py) defines J, a list of dicts with
short keys; this writes scratch/queue/<name>.out.jsonl. The judgment is the
judge's; the expansion is mechanical: it adds the source and confidence keys
each claim needs, emits only the keys the queue asked for (plus a deliberate
dispute of a pre-filled value, flagged model_disputes_source), and writes a
member's verdict line and classification line separately (COLLECTION.md 8).

Short keys: s slug | m verdict, mb basis, me evidence class, mc citation,
mconf | st status | v usd, va as-of, vc citation (a priced event), vr band |
es stage, esc citation, ess source, econf, ed entry date | hc country, city |
f focus | g graduation, gs source, gc citation | fl flags | n note |
fr funding rounds [(date, round, amount_usd, lead, firm_in_round, source, source_type)]
Usage: python3 .../scratch/emit.py <name>
"""
import json, sys, runpy
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
LISTING = "https://www.coatue.com/portfolio"
name = sys.argv[1]
J = runpy.run_path(str(INV / f"scratch/judgments/{name}.py"))["J"]
Q = {it["slug"]: it for it in json.load(open(INV / "scratch/queue/queue.json"))}
SIB = json.load(open(INV / "scratch/siblings.json"))
SURF = json.load(open(INV / "scratch/graduation-surfaces.json")) if (INV / "scratch/graduation-surfaces.json").exists() else {}
GID = INV / "scratch/gid-cache.json"
GIDC = json.load(open(GID)) if GID.exists() else {}
def headline_url(slug, needle):
    """The URL of the headline containing `needle` among this row's news items;
    a Google News id is decoded once through graduation-surfaces.py and cached."""
    import subprocess, re
    for sname, sv in ((SURF.get(slug) or {}).get("surfaces") or {}).items():
        for i in sv.get("items") or []:
            norm_ = lambda x: x.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
            if norm_(needle) in norm_(i.get("title") or ""):
                if i.get("link"): return i["link"]
                g = i.get("gid")
                if g and g not in GIDC:
                    r = subprocess.run([sys.executable, str(INV.parents[3] / "scripts/graduation-surfaces.py"), "decode", g], capture_output=True, text=True)
                    m = re.search(r"https?://\S+", r.stdout)
                    GIDC[g] = m.group(0) if m else None
                    GID.write_text(json.dumps(GIDC, indent=1))
                if g and GIDC.get(g): return GIDC[g]
    return None
def band(v):
    return "100b_plus" if v >= 1e11 else "10b_plus" if v >= 1e10 else "1b_plus" if v >= 1e9 else "below_1b"
out, problems = [], []
for j in J:
    s = j["s"]; it = Q.get(s)
    if it is None:
        problems.append(f"{s}: not in the queue"); continue
    need, known = set(it["need"]), it.get("known") or {}
    if j.get("sib"):
        cand = [x for x in SIB.get(s, []) if x["valuation_usd"] and x["valuation_citation"] and x["valuation_source"] == "web_verified"
                and (j["sib"] == "*" or x["investor"] == j["sib"])]
        cand.sort(key=lambda x: (x["valuation_asof"] or "", not x["in_flight"]), reverse=True)
        sb = cand[0] if cand else None
        if sb is None:
            problems.append(f"{s}: sibling {j['sib']} has no cited figure; band left open for the web pass")
            j["vr"] = "later"
        else:
            j.update({"v": float(sb["valuation_usd"]), "va": sb["valuation_asof"] or j.get("va"), "vc": sb["valuation_citation"], "vs": sb["valuation_source"]})
            if not j.get("va"): problems.append(f"{s}: sibling {sb['investor']} figure has no as-of date")
            elif j["va"][:7] < "2024-09" and "stale" not in (j.get("fl") or []): j.setdefault("fl", []).append("stale")
    for nk, ck in (("esn", "esc"), ("vn", "vc"), ("gn", "gc")):
        if j.get(nk) and not j.get(ck):
            u = headline_url(s, j[nk])
            if u: j[ck] = u
            else:
                problems.append(f"{s}: no headline matches '{j[nk]}'")
                if nk == "vn": j.pop("v", None); j.pop("vlocal", None); j["vr"] = "later"
    if j.get("m"):
        v = {"slug": s, "verdict": j["m"], "who": "agent", "evidence_class": j.get("me", "site_listing"),
             "confidence": j.get("mconf", "high"), "basis": j["mb"]}
        if j.get("mc"): v["citation"] = j["mc"]
        out.append(v)
        if j["m"] == "not_member": continue
    c = {"slug": s}; flags = list(j.get("fl") or []); notes = [j["n"]] if j.get("n") else []
    def put(key, val, companions=None):
        """Emit when asked, or as a flagged dispute of a pre-filled value."""
        if val is None: return
        asked = key in need or (key == "seed_to_a_graduation" and "seed_to_a_graduation" in need)
        pre = known.get(key)
        if asked or pre is None:
            c[key] = val; c.update(companions or {})
        elif pre != val:
            c[key] = val; c.update(companions or {})
            if "model_disputes_source" not in flags: flags.append("model_disputes_source")
            notes.append(f"disputes the pre-filled {key} '{pre}'")
    put("status", j.get("st"))
    if j.get("vlocal"):
        import subprocess
        amt, ccy, on = j["vlocal"]
        fx = json.loads(subprocess.run([sys.executable, str(INV.parents[3] / "scripts/fx-convert.py"), str(amt), ccy, on, "--json"], capture_output=True, text=True).stdout)
        j["v"] = round(fx["usd"]); notes.append(fx["note"] + (f" (rate of {fx['rate_date']})" if fx.get("rate_date") != on else ""))
    if j.get("v"):
        vr = band(j["v"])
        for e_ in (1e9, 1e10, 1e11):
            if 0 < abs(j["v"] - e_) / e_ <= 0.05: notes.append(f"Within 5% of the ${e_/1e9:.0f}B band edge.")
        c.update({"valuation_usd": float(j["v"]), "valuation_source": j.get("vs", "web_verified"), "valuation_citation": j["vc"],
                  "valuation_asof": j["va"], "valuation_confidence": j.get("vconf", "high"), "valuation_range": vr,
                  "valuation_range_source": "web_verified"})
    else:
        vr = j.get("vr") or ("below_1b" if j.get("st") else None)
        if vr == "later":
            if "needs_web_value" not in flags: flags.append("needs_web_value")
        elif vr:
            put("valuation_range", vr)
            if j.get("vc"):        # a recorded web check on a below_1b row (momentum slice, collapse evidence)
                c["valuation_range"] = vr
                c.update({"valuation_range_source": "web_verified", "valuation_citation": j["vc"], "valuation_asof": j.get("va")})
            if known.get("valuation_usd") and vr == "below_1b" or (j.get("st") in ("acquired", "defunct", "unknown") and known.get("valuation_usd")):
                c["valuation_usd"] = None
    es = j.get("es")
    if es:
        comp = {}
        if es == "undetermined":
            comp = {"entry_stage_source": "model", "entry_stage_confidence": "low"}
        elif j.get("esc"):
            comp = {"entry_stage_source": j.get("ess", "web_verified"), "entry_stage_citation": j["esc"], "entry_stage_confidence": j.get("econf", "high")}
        elif es == "Growth" and it.get("site_entry_stage") == "Growth" and not j.get("ess"):
            comp = {"entry_stage_source": "first_party", "entry_stage_citation": LISTING, "entry_stage_confidence": "medium"}
        else:
            comp = {"entry_stage_source": j.get("ess", "model"), "entry_stage_confidence": j.get("econf", "medium")}
            if "stage_uncited" not in flags: flags.append("stage_uncited")
        pre = known.get("entry_stage")
        if pre and pre != es and "stage_disputes_band" not in flags and (known.get("entry_stage_source") or "").startswith("formd"):
            flags.append("stage_disputes_band")
        c["entry_stage"] = es; c.update(comp)
        if j.get("ed"): c["entry_date"] = j["ed"]
        if es != "Seed" and "seed_to_a_graduation" in need and not j.get("g"):
            pass   # a judged non-Seed stage closes the graduation need
    if j.get("g"):
        c["seed_to_a_graduation"] = j["g"]
        if j["g"] == "graduated" and j.get("gc") and not j.get("gs"): j["gs"] = "web_verified"
        for k_, kk in (("gs", "graduation_source"), ("gc", "graduation_citation"), ("ga", "graduation_asof"), ("gsurf", "graduation_surfaces")):
            if j.get(k_): c[kk] = j[k_]
    if j.get("hc"):
        put("hq_country", j["hc"], {"hq_country_source": j.get("hcs", "model_knowledge"), "hq_country_confidence": j.get("hconf", "high")})
    if j.get("city"):
        put("hq_city", j["city"], {"hq_city_source": "model_knowledge", "hq_city_confidence": j.get("cconf", "high")})
    elif "hq_city" in need and j.get("st"):
        flags.append("city_unknown")
    if j.get("f"): c.update({"focus": j["f"], "focus_source": "model"})
    if j.get("fr"):
        c["funding_rounds"] = [{"date": d, "round": r, "amount_usd": a, "lead": l, "firm_in_round": fi, "source": src, "source_type": t}
                               for d, r, a, l, fi, src, t in j["fr"]]
    if j.get("v") or (j.get("vr") and j.get("vr") != "later"): c["clear_flags"] = ["needs_web_value"]
    c["flags"] = sorted(set(flags)); c["note"] = " | ".join(notes)
    out.append(c)
dest = INV / f"scratch/queue/{name}.out.jsonl"
dest.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out))
print(f"{dest.name}: {len(out)} lines from {len(J)} judgments"); [print("  PROBLEM", p) for p in problems]
