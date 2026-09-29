#!/usr/bin/env python3
"""Expand compact judgments into gate-valid output lines for `run.py record`
(adapted from ICONIQ's and Coatue's emit.py for TCV, PRO-169; no TCV surface carries a stage label, so
no stage is ever read off the listing).

A judgments file (scratch/judgments/<name>.py) defines J, a list of dicts with
short keys; this writes scratch/queue/<name>.out.jsonl. The judgment is the
judge's; the expansion is mechanical: it adds the source and confidence keys
each claim needs, emits only the keys the queue asked for (plus a deliberate
dispute of a pre-filled value, flagged model_disputes_source), and writes a
member's verdict line and classification line separately (COLLECTION.md 8).

Short keys: s slug | m verdict, mb basis, me evidence class, mc citation,
mconf | st status | v usd, va as-of, vc citation (a priced event), vr band |
es stage, esc citation, ess source, econf, ed entry date | hc country, city |
f focus | g graduation, gs source, gc citation | fl flags | cf flags to clear | n note |
hcc country citation (rule 6) | vr=None on a status-only line keeps the band |
fr funding rounds [(date, round, amount_usd, lead, firm_in_round, source, source_type)]
Usage: python3 .../scratch/emit.py <name>
"""
import json, sys, runpy
from pathlib import Path
INV = Path(__file__).resolve().parents[1]
LISTING = "https://www.tcv.com/all-companies"
name = sys.argv[1]
J = runpy.run_path(str(INV / f"scratch/judgments/{name}.py"))["J"]
Q = {it["slug"]: it for it in json.load(open(INV / "scratch/queue/queue.json"))}
SIB = json.load(open(INV / "scratch/siblings.json")) if (INV / "scratch/siblings.json").exists() else {}
SURF = json.load(open(INV / "scratch/graduation-surfaces.json")) if (INV / "scratch/graduation-surfaces.json").exists() else {}
NEWSI = json.load(open(INV / "scratch/news-tcv.json")) if (INV / "scratch/news-tcv.json").exists() else {}
CL_ = json.load(open(INV / "companies/classification.json")) if (INV / "companies/classification.json").exists() else {}
RES_ = json.load(open(INV / "companies/resolved.json"))
CUR = lambda slug, k: (CL_.get(slug) or {}).get(k) or (RES_.get(slug) or {}).get(k)   # the value on disk now
GID = INV / "scratch/gid-cache.json"
GIDC = json.load(open(GID)) if GID.exists() else {}
def headline_url(slug, needle):
    """The URL of the headline containing `needle` among this row's news items;
    a Google News id is decoded once through graduation-surfaces.py and cached."""
    import subprocess, re
    groups = list(((SURF.get(slug) or {}).get("surfaces") or {}).values()) + [NEWSI.get(slug) or {}]
    for sv in groups:
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
    if j.get("mcn") and not j.get("mc"):
        u = headline_url(s, j["mcn"])
        if u: j["mc"] = u
        else: problems.append(f"{s}: no headline matches '{j['mcn']}' (membership citation)")
    if j.get("m"):
        v = {"slug": s, "verdict": j["m"], "who": "agent", "evidence_class": j.get("me", "site_listing"),
             "confidence": j.get("mconf", "high"), "basis": j["mb"]}
        if j.get("mc"): v["citation"] = j["mc"]
        if j.get("mx"): v["exclusion"] = j["mx"]   # e.g. control_position (the Insight builder change)
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
        if (j.get("va") or "9999")[:7] < "2024-09" and "stale" not in flags:
            flags.append("stale")    # a mark older than two years (the sibling path's cut-off)
        c.update({"valuation_usd": float(j["v"]), "valuation_source": j.get("vs", "web_verified"), "valuation_citation": j["vc"],
                  "valuation_asof": j["va"], "valuation_confidence": j.get("vconf", "high"), "valuation_range": vr,
                  "valuation_range_source": "web_verified"})
    else:
        # an explicit vr=None means "leave the band alone" (a status-only fix line);
        # only an absent key defaults a judged status to below_1b
        vr = j["vr"] if "vr" in j else ("below_1b" if j.get("st") else None)
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
        comp = {"hq_country_source": j.get("hcs", "web_verified" if j.get("hcc") else "model_knowledge"), "hq_country_confidence": j.get("hconf", "high")}
        if j.get("hcc"): comp["hq_country_citation"] = j["hcc"]   # rule 6: a non-US country on a $1B+ row
        put("hq_country", j["hc"], comp)
    if j.get("city"):
        put("hq_city", j["city"], {"hq_city_source": "model_knowledge", "hq_city_confidence": j.get("cconf", "high")})
    elif "hq_city" in need and j.get("st") and not CUR(s, "hq_city"):
        flags.append("city_unknown")   # only where no earlier line placed the company
    if j.get("f"): c.update({"focus": j["f"], "focus_source": "model"})
    if j.get("fr"):
        c["funding_rounds"] = [{"date": d, "round": r, "amount_usd": a, "lead": l, "firm_in_round": fi, "source": src, "source_type": t}
                               for d, r, a, l, fi, src, t in j["fr"]]
    if j.get("v") or (j.get("vr") and j.get("vr") != "later"): c["clear_flags"] = ["needs_web_value"]
    if j.get("cf"): c["clear_flags"] = sorted(set(c.get("clear_flags") or []) | set(j["cf"]))   # work flags the line settles
    c["flags"] = sorted(set(flags))
    if notes: c["note"] = " | ".join(notes)   # never send "": record writes an empty note over the stored one
    out.append(c)
dest = INV / f"scratch/queue/{name}.out.jsonl"
dest.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out))
print(f"{dest.name}: {len(out)} lines from {len(J)} judgments"); [print("  PROBLEM", p) for p in problems]
