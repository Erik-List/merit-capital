#!/usr/bin/env python3
"""Turn the research files into record lines (PRO-108), one row at a time.

The research agents re-loaded every URL they cite (scratch/research-g*.json,
brief in row-research-brief.md). This script applies the record contract of
COLLECTION.md s6/s8 to each entry mechanically, so every row is judged by the
same rules, and OVERRIDES (scratch/judge-overrides.json, written by the judge
after reading the table this prints) corrects a row where the research and the
rules disagree. It emits only the keys a row's queue item asks for, plus a
deliberate dispute where a deterministic pre-fill is wrong (flagged
`model_disputes_source` or `stage_disputes_band`).

Usage: python3 judge_research.py g0 [g1 ...] [--dry]     (groups from research-groups.json)
       python3 judge_research.py --slugs a,b,c [--dry]
"""
import importlib.util
import json
import re
import sys
from datetime import date
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J  # noqa: E402

sys.path.insert(0, str(J.ROOT / "scripts"))
from stage_words import earliest_round  # noqa: E402

_spec = importlib.util.spec_from_file_location("fx_convert", J.ROOT / "scripts" / "fx-convert.py")
fx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fx)

TODAY = date(2026, 10, 1)
import glob as _glob
import pack as _pack  # noqa: E402
R2 = {}
for _f in sorted(_glob.glob(str(H / "research2-s*.json"))):
    R2.update(json.loads(open(_f).read()))
VIS = json.loads((H / "visible-research.json").read_text()) if (H / "visible-research.json").exists() else {}
R1_NOTE = ("The firm's own 2022-2026 portfolio page files the company under {label} (its stage field; scored against the "
           "book's documented entry rounds, decisions.md R1).")
GROUPS = json.loads((H / "research-groups.json").read_text())
OVR = json.loads((H / "judge-overrides.json").read_text()) if (H / "judge-overrides.json").exists() else {}
_q = json.loads((H / "queue" / "queue.json").read_text())
ITEMS = {i["slug"]: i for i in (_q.get("items", _q) if isinstance(_q, dict) else _q)}
RESOLVED = json.loads((J.INV / "companies" / "resolved.json").read_text())
FOCUS = {"AI & Applied AI", "Data Infrastructure", "DevTools & APIs", "SaaS", "Security", "Fintech & Payments",
         "Crypto & Web3", "Industrial & Robotics", "Climate & Energy", "Healthcare & Bio",
         "Consumer & Marketplaces", "Media, Gaming & Advertising"}
VENDOR = re.compile(r"(?<!news\.)crunchbase\.com|pitchbook\.com|tracxn\.com|dealroom\.co|cbinsights\.com|getlatka|"
                    r"owler\.com|zoominfo|craft\.co|growjo|golden\.com|seedtable|sacra\.com|contrary\.com", re.I)
CCY = {"EUR": "EUR", "€": "EUR", "GBP": "GBP", "£": "GBP", "SEK": "SEK", "CHF": "CHF", "DKK": "DKK", "NOK": "NOK",
       "USD": "USD", "$": "USD"}


def stage_of(round_word):
    if not round_word:
        return None
    w = str(round_word).strip()
    lab = earliest_round(w)
    if not lab:
        lw = w.lower()
        if re.search(r"pre[- ]?seed|angel|friends", lw):
            lab = "Pre-Seed"
        elif re.search(r"\bseed\b", lw):
            lab = "Seed"
        elif re.search(r"series a\b", lw):
            lab = "Series A"
        elif re.search(r"series [b-k]\b|growth|late|secondary|tender|pre-ipo|pipe|convertible|venture debt|"
                       r"extension of series [b-k]", lw):
            lab = "Growth"
    return lab


def _site_label(slug):
    """The first value of the firm's stage field for this row (before any Exit/IPO switch)."""
    ev = _pack.ev_for(slug, (J.BASE.get(slug) or {}).get("name") or slug)
    st = list((ev.get("stages") or {}).keys())
    return st[0] if st else None


def months_old(d):
    """Months between the LATEST day a coarse date can mean and today."""
    d = str(d)
    y = int(d[:4])
    m = int(d[5:7]) if len(d) >= 7 else 12
    return (TODAY.year - y) * 12 + (TODAY.month - m)


def ok_cite(u):
    return bool(u) and str(u).startswith("http") and not VENDOR.search(str(u))


def native_to_usd(native, asof):
    """'EUR 1.2B' at a date -> (usd, fx note). None when not parseable."""
    m = re.match(r"\s*(EUR|GBP|SEK|CHF|DKK|NOK|USD|€|£|\$)\s*([\d.,]+)\s*(B|bn|billion|M|m|million)?", str(native or ""), re.I)
    if not m or not asof:
        return None, None
    ccy = CCY[m.group(1).upper() if m.group(1).isalpha() else m.group(1)]
    val = float(m.group(2).replace(",", ""))
    unit = (m.group(3) or "").lower()
    val *= 1e9 if unit in ("b", "bn", "billion") else 1e6 if unit in ("m", "million") else 1
    if ccy == "USD":
        return int(val), None
    d = str(asof)
    d = d if len(d) == 10 else (d + "-28" if len(d) == 7 else d + "-12-31")
    usd, detail = fx.to_usd(val, ccy, d)
    return int(round(usd)), detail.get("note") if isinstance(detail, dict) else str(detail)


def rng_of(usd):
    return "100b_plus" if usd >= 100e9 else "10b_plus" if usd >= 10e9 else "1b_plus" if usd >= 1e9 else "below_1b"


def judge(slug):
    """-> (lines, summary row, problems)"""
    r = dict(J.RS.get(slug) or {})
    o = OVR.get(slug) or {}
    r2 = R2.get(slug) or {}
    if isinstance(r2.get("entry"), dict) and str(r2["entry"].get("citation") or "").startswith("http"):
        r["entry"] = r2["entry"]
        if r2.get("graduation") is not None:
            r["graduation"] = r2["graduation"]
    vis = VIS.get(slug) or {}
    for k in ("status", "status_detail", "status_citation", "hq_city", "hq_country"):
        if vis.get(k):
            r[k] = vis[k]
    if isinstance(vis.get("valuation"), dict) and vis["valuation"].get("range") in ("below_1b", "1b_plus", "10b_plus", "100b_plus"):
        r["valuation"] = vis["valuation"]
    if isinstance(vis.get("entry"), dict) and str(vis["entry"].get("citation") or "").startswith("http"):
        r["entry"] = vis["entry"]
        r["graduation"] = vis.get("graduation") or r.get("graduation")
    if o.get("skip"):
        return [], f"{slug:28s} SKIP ({o['skip']})", []
    for k, v in o.items():
        if k in ("entry", "graduation", "valuation") and isinstance(v, dict) and isinstance(r.get(k), dict):
            r[k] = {**r[k], **v}
        else:
            r[k] = v
    item = ITEMS.get(slug) or {}
    need = set(item.get("need") or [])
    if "--force" in sys.argv:              # a re-judged row (the A/B pass): every column is re-emitted
        need = {"status", "valuation_range", "entry_stage", "seed_to_a_graduation", "hq_country", "hq_city"}
    known = item.get("known") or {}
    res = RESOLVED.get(slug) or {}
    probs = []
    if not r or r.get("identity") == "unresolved":
        return [], f"{slug:28s} NO RESEARCH / unresolved", [f"{slug}: no usable research"]
    kw = {"flags": set(o.get("flags") or []), "clear": set(o.get("clear_flags") or [])}
    extra = {}
    notes = []
    what = (r.get("what") or "").strip().rstrip(".")
    if what:
        notes.append(what + ".")

    # ---- status
    status = r.get("status")
    if status not in ("private", "public", "acquired", "defunct", "unknown"):
        probs.append(f"{slug}: status {status!r}")
        status = None
    sc = r.get("status_citation") if ok_cite(r.get("status_citation")) else None
    pre_status = res.get("status")
    if status and ("status" in need or (pre_status and pre_status != status)):
        kw["status"] = status
        if pre_status and pre_status != status:
            kw["flags"].add("model_disputes_source")
            notes.append(f"The pre-filled status '{pre_status}' ({res.get('valuation_source') or 'deterministic layer'}) is a wrong join.")
    if status in ("acquired", "defunct") and sc:
        extra["status_citation"] = sc
    if r.get("status_detail") and status in ("acquired", "defunct", "public"):
        notes.append(str(r["status_detail"]).strip().rstrip(".") + ".")

    # ---- valuation
    v = r.get("valuation") or {}
    vr = v.get("range") or "below_1b"
    pre_rng, pre_usd = res.get("valuation_range"), res.get("valuation_usd")
    if status in ("acquired", "defunct", "unknown"):
        if "valuation_range" in need or pre_usd or (pre_rng and pre_rng != "below_1b"):
            kw["rng"] = "below_1b"
            if pre_usd:
                kw["flags"].add("model_disputes_source")
                extra["valuation_source"] = None
                extra["valuation_asof"] = None
    elif vr != "below_1b":
        usd = v.get("usd")
        fxnote = None
        if v.get("native") and not re.match(r"\s*(USD|\$)", str(v["native"])):
            conv, fxnote = native_to_usd(v["native"], v.get("asof"))
            if conv:
                usd = conv
        if not usd or not ok_cite(v.get("citation")) or not v.get("asof"):
            probs.append(f"{slug}: {vr} without usd/citation/asof ({usd}, {v.get('citation')}, {v.get('asof')})")
            if "valuation_range" in need:
                kw["rng"] = "below_1b"
                kw["flags"].add("needs_web_value")
        else:
            usd = int(usd)
            kw.update(rng=rng_of(usd), usd=usd, val_src="web_verified", val_cite=v["citation"],
                      asof=str(v["asof"]), val_conf="high" if r.get("confidence") == "high" else "medium")
            if rng_of(usd) != vr:
                probs.append(f"{slug}: research said {vr}, figure gives {rng_of(usd)}")
            notes.append((f"{v.get('event', '').strip().rstrip('.')}. " if v.get("event") else "")
                         + (f"{fxnote}." if fxnote else ""))
            if status == "private" and months_old(v["asof"]) > 24:
                kw["flags"].add("stale")
            if pre_usd and pre_usd != usd:
                kw["clear"].update({"unicorn_name_match", "needs_web_value"})
    else:
        if "valuation_range" in need or pre_usd or (pre_rng and pre_rng != "below_1b"):
            kw["rng"] = "below_1b"
            if pre_usd or (pre_rng and pre_rng != "below_1b"):
                kw["flags"].add("model_disputes_source")
                kw["clear"].update({"unicorn_name_match", "needs_web_value"})
                extra["valuation_source"] = None
                extra["valuation_asof"] = None
                notes.append(f"The pre-filled mark ({res.get('valuation_source')}, ${pre_usd}) does not hold: "
                             f"{(v.get('searched') or v.get('event') or 'no priced event at $1B or more found').strip().rstrip('.')}.")
        if ok_cite(v.get("citation")) or (v.get("searched") and sc):
            extra["valuation_range_source"] = "web_verified"
            extra["valuation_citation"] = v.get("citation") if ok_cite(v.get("citation")) else sc
            extra["valuation_asof"] = J.ASOF

    # ---- entry stage
    e = r.get("entry") or {}
    stage = stage_of(e.get("round")) if e else None
    pre_stage = known.get("entry_stage") or res.get("entry_stage")
    entry_date = (e.get("date") or "").strip() if e else ""
    if stage and e.get("lakestar_named") and ok_cite(e.get("citation")):
        kw.update(stage=stage, stage_src="first_party" if "lakestar.com" in e["citation"] else "web_verified",
                  stage_cite=e["citation"], stage_conf=e.get("confidence") or r.get("confidence") or "medium")
        if entry_date:
            kw["entry_date"] = entry_date
        if pre_stage and pre_stage != stage:
            kw["flags"].add("stage_disputes_band")
        q = (e.get("quote") or "").strip()
        notes.append(f"Entry: {e.get('round')}{' (' + e['amount'] + ')' if e.get('amount') else ''}, {entry_date or 'date not given'}"
                     + (f": '{q[:180]}'" if q else "") + ".")
    elif o.get("force_stage"):
        fs = o["force_stage"]
        stage = fs["stage"]
        kw.update(stage=stage, stage_src=fs["src"], stage_conf=fs.get("conf", "medium"))
        if fs.get("cite"):
            kw["stage_cite"] = fs["cite"]
        notes.append(fs["note"])
    elif (_site_label(slug) == "Growth") and not o.get("no_first_party"):
        ev = _pack.ev_for(slug, J.BASE[slug]["name"])
        stage = "Growth"
        kw.update(stage="Growth", stage_src="first_party", stage_cite=ev["stage_urls"]["Growth"], stage_conf="medium")
        notes.append(R1_NOTE.format(label="Growth") + " No round announcement naming Lakestar's first round was found.")
        if pre_stage and pre_stage != "Growth":
            kw["flags"].add("stage_disputes_band")
    else:
        kw["stage"] = "undetermined"
        stage = "undetermined"
        if pre_stage and pre_stage != "undetermined":
            kw["flags"].add("stage_disputes_band")
        notes.append("No source names the round in which a Lakestar fund entered"
                     + (f" ({e.get('round')} {entry_date} is named without Lakestar)" if e and e.get("round") else "") + ".")

    # ---- graduation
    g = r.get("graduation") or {}
    if stage == "Seed":
        if not entry_date:
            probs.append(f"{slug}: Seed without entry_date")
        elif g.get("later_round") and ok_cite(g.get("citation")):
            kw.update(grad="graduated", grad_cite=g["citation"],
                      grad_src="first_party" if "lakestar.com" in g["citation"] else "web_verified")
            notes.append(f"Graduated: {g['later_round']}{' (' + str(g['amount']) + ')' if g.get('amount') else ''}, {g.get('date')}.")
        elif months_old(entry_date) < 24 and status not in ("acquired", "defunct"):
            kw["grad"] = "censored"
        elif months_old(entry_date) < 24 and not sc:
            kw["grad"] = "censored"
        else:
            finding = o.get("absence_finding") or "no later round named or sized after the seed"
            if status in ("acquired", "defunct") and sc:
                kw.update(grad="not_graduated", grad_src="web_verified", grad_cite=sc, grad_asof=J.ASOF)
                finding = (f"{status} ({r.get('status_date') or 'date in the note'}) with the seed as the last round"
                           if not o.get("absence_finding") else o["absence_finding"])
            else:
                kw.update(grad="not_graduated", grad_src="absence_check", grad_asof=J.ASOF)
            lines = J.surfaces_lines(slug, finding)
            searched = [s for s in (g.get("searched") or []) if isinstance(s, str)]
            co = next((s for s in searched if "company" in s.lower() or "site" in s.lower()), None)
            if co:
                lines.append("company: " + re.sub(r"^[^:]*:\s*", "", co)[:200] + " -> no later round")
            if (r.get("hq_country") == "US") and not any(l.startswith("formd:") for l in lines):
                fd = item.get("formd_graduation") or {}
                lines.append("formd: the company's Form D sequence on EDGAR (issuer-rounds rescan as of 2026-10-01) -> "
                             + ("no filing after the entry round" if not fd else f"layer says {fd.get('seed_to_a_graduation')}"))
            kw["surfaces"] = lines
            notes.append("No later round found: " + finding + ".")
    elif "seed_to_a_graduation" in need and stage and stage != "Seed":
        pass  # a judged non-Seed stage closes the need

    # ---- HQ
    country, city = r.get("hq_country"), r.get("hq_city")
    hc = r.get("hq_citation") if ok_cite(r.get("hq_citation")) else (sc or (e.get("citation") if ok_cite(e.get("citation")) else None))
    pre_c = known.get("hq_country") or res.get("hq_country")
    if country and ("hq_country" in need or (pre_c and pre_c != country)):
        kw["country"] = country
        kw["country_src"] = "web_verified" if hc else "model_knowledge"
        if hc:
            kw["country_cite"] = hc
        if pre_c and pre_c != country:
            kw["flags"].add("model_disputes_source")
            notes.append(f"The pre-filled country {pre_c} ({res.get('hq_country_source')}) is wrong for this company.")
    if city and "hq_city" in need:
        kw["city"] = city
        kw["city_src"] = "web_verified" if hc else "model_knowledge"
    elif "hq_city" in need:
        kw["flags"].add("city_unknown")

    # ---- focus
    if r.get("focus") in FOCUS:
        kw["focus"] = r["focus"]
    elif r.get("focus"):
        probs.append(f"{slug}: focus {r['focus']!r} outside the taxonomy")

    if r.get("notes"):
        notes.append(str(r["notes"]).strip())
    if o.get("note"):
        notes = [o["note"]]
    note = re.sub(r"\s+", " ", " ".join(n for n in notes if n)).strip()
    rounds = J.rrounds(slug) + [J.rnd(x.get("date"), x.get("round"), x.get("amount_usd"), x.get("lead"), x.get("firm_in_round"),
                                       x.get("source") if str(x.get("source") or "").startswith("http") else None,
                                       x.get("source_type") or "press") for x in (r2.get("rounds_added") or [])]
    line = J.cls(slug, status=kw.get("status"), rng=kw.get("rng"), usd=kw.get("usd"), val_src=kw.get("val_src"),
                 val_cite=kw.get("val_cite"), asof=kw.get("asof"), val_conf=kw.get("val_conf"),
                 stage=kw.get("stage"), stage_src=kw.get("stage_src"), stage_cite=kw.get("stage_cite"),
                 stage_conf=kw.get("stage_conf"), entry_date=kw.get("entry_date"), grad=kw.get("grad"),
                 grad_src=kw.get("grad_src"), grad_cite=kw.get("grad_cite"), grad_asof=kw.get("grad_asof"),
                 surfaces=kw.get("surfaces"), country=kw.get("country"), country_src=kw.get("country_src", "web_verified"),
                 country_cite=kw.get("country_cite"), city=kw.get("city"), city_src=kw.get("city_src", "web_verified"),
                 focus=kw.get("focus"), flags=kw["flags"], clear=kw["clear"], note=note, rounds=rounds, extra=extra)
    summ = (f"{slug[:26]:26s} {status or '-':8s} {kw.get('rng') or res.get('valuation_range') or '-':9s} "
            f"{('$%.1fB' % (kw['usd'] / 1e9)) if kw.get('usd') else '':8s} {kw.get('stage') or '-':12s} {kw.get('entry_date') or '':8s} "
            f"{kw.get('grad') or '':14s} {kw.get('city') or '-'}, {kw.get('country') or pre_c or '-'} | {kw.get('focus') or '-'} | "
            f"{','.join(sorted(kw['flags']))}")
    return [line], summ, probs


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    if "--slugs" in sys.argv:
        slugs = sys.argv[sys.argv.index("--slugs") + 1].split(",")
        name = "research-" + slugs[0]
        args = []
    else:
        slugs = [s for g in args for s in GROUPS[g]]
        name = "research-" + "-".join(args)
    L, allp = [], []
    for s in slugs:
        lines, summ, probs = judge(s)
        print(summ)
        L += lines
        allp += probs
    print(f"\n{len(L)} lines; {len(allp)} problems")
    for p in allp:
        print("  !!", p)
    if not dry:
        J.write(name, L)


if __name__ == "__main__":
    main()
