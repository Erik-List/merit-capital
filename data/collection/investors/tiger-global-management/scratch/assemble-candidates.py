#!/usr/bin/env python3
"""Union every recall layer into one candidate table, keyed by company (PRO-167).

Inputs (each optional; a missing file is reported, not treated as empty evidence):
  press headlines   recall/headlines-*.out.jsonl  (extraction agents: company, cls T/F/P/O)
                    + recall/headlines-all.json    (gid, date, source, title per index)
  parametric lists  recall/param-*.json            (model memory: LEADS, never evidence)
  full-text triage  recall/fts-triage.json         (portfolio / target / public / noise)
  Wikipedia         sources/web/wikipedia-insource.json (company articles naming Tiger)
  base rows         companies/base.json            (site, EDGAR filer, Form D layers)

Output: recall/candidates.json {key: {name, names, in_base, press_T, press_F, press_P,
param, fts, wiki}} and a count summary. The key is a loose name (legal suffixes and
generic words dropped), the same normalisation the sibling lookup uses, so a company the
base already holds is marked `in_base` instead of becoming a second row.
"""
import glob, json, re
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
INV = HERE.parent

GENERIC = r"\b(inc|incorporated|ltd|limited|pvt|private|gmbh|ab|sa|s\.a|plc|llc|l\.l\.c|corp|corporation|co|company|group|holdings?|technologies|technology|tech|labs|the|app|com|ai|india|global|international|pte|bv|nv|ag|oy|as)\b\.?"


def loose(s):
    s = (s or "").lower().replace("&", " and ")
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"\.(com|io|ai|co|in|app|net|org)\b", " ", s)
    s = re.sub(GENERIC, " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)


C = defaultdict(lambda: {"names": Counter(), "press_T": [], "press_F": [], "press_P": [],
                         "param": [], "fts": [], "wiki": [], "in_base": None})
missing = []

base = json.loads((INV / "companies/base.json").read_text())
base_keys = {}
for r in base:
    k = loose(r["name"])
    if k:
        base_keys.setdefault(k, r["slug"])

allh = HERE / "recall/headlines-all.json"
rows = json.loads(allh.read_text()) if allh.exists() else []
outs = sorted(glob.glob(str(HERE / "recall/headlines-*.out.jsonl")))
if not outs:
    missing.append("headline extraction")
for f in outs:
    for line in open(f):
        line = line.strip()
        if not line:
            continue
        try:
            x = json.loads(line)
        except ValueError:
            continue
        comp, cls = x.get("company"), x.get("cls")
        if not comp or cls not in ("T", "F", "P"):
            continue
        i = int(x["i"])
        if i >= len(rows):
            continue
        h = rows[i]
        k = loose(comp)
        if len(k) < 2:
            continue
        C[k]["names"][comp] += 1
        C[k][f"press_{cls}"].append({"gid": h["gid"], "date": h["date"], "source": h.get("source"),
                                    "title": h["title"], "round": x.get("round"), "amount": x.get("amount"),
                                    "tiger_led": x.get("tiger_led"), "valuation": x.get("valuation")})

pfiles = sorted(glob.glob(str(HERE / "recall/param-*.json")))
if not pfiles:
    missing.append("parametric lists")
for f in pfiles:
    try:
        L = json.loads(Path(f).read_text())
    except ValueError:
        missing.append(f"unreadable {Path(f).name}")
        continue
    for x in L:
        k = loose(x.get("name"))
        if len(k) < 2:
            continue
        C[k]["names"][x["name"]] += 1
        C[k]["param"].append({**x, "file": Path(f).stem})

ft = HERE / "recall/fts-triage.json"
if ft.exists():
    for x in json.loads(ft.read_text()):
        if x.get("class") not in ("portfolio", "target") or not x.get("company"):
            continue
        k = loose(x["company"])
        if len(k) < 2:
            continue
        C[k]["names"][x["company"]] += 1
        C[k]["fts"].append(x)
else:
    missing.append("fts triage")

wf = INV / "sources/web/wikipedia-insource.json"
if wf.exists():
    for a in json.loads(wf.read_text()).get("articles", []):
        if not a.get("is_company"):
            continue
        sents = [s for s in (a.get("sentences") or []) if "Tiger" in s]
        if not sents:
            continue
        nm = re.sub(r"\s*\(.*?\)\s*", "", a["title"]).strip()
        k = loose(nm)
        if len(k) < 2:
            continue
        C[k]["names"][nm] += 1
        C[k]["wiki"].append({"title": a["title"], "url": a.get("url"), "sentences": sents[:3]})

# one company under two keys: fold the alias's evidence into the canonical key
AL = {}
alf = HERE / "recall/aliases.json"
if alf.exists():
    AL = json.loads(alf.read_text()).get("aliases", {})
for a, canon in AL.items():
    if a in C and a != canon:
        src = C.pop(a)
        dst = C[canon]
        dst["names"].update(src["names"])
        for f in ("press_T", "press_F", "press_P", "param", "fts", "wiki"):
            dst[f].extend(src[f])
base_keys.update({a: base_keys[canon] for a, canon in AL.items() if canon in base_keys})
for a, canon in AL.items():
    if a in base_keys and canon not in base_keys:
        base_keys[canon] = base_keys[a]

out = {}
for k, v in C.items():
    name = v["names"].most_common(1)[0][0]
    v["in_base"] = base_keys.get(k)
    out[k] = {"name": name, "names": dict(v["names"]), **{x: v[x] for x in
              ("in_base", "press_T", "press_F", "press_P", "param", "fts", "wiki")}}
(HERE / "recall/candidates.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")


def has(v, *fields):
    return any(v[f] for f in fields)


print(f"{len(out)} candidate companies ({sum(1 for v in out.values() if v['in_base'])} already in the base)")
print("  with a Tiger-naming headline:", sum(1 for v in out.values() if v["press_T"]))
print("  with a filing (fts portfolio/target):", sum(1 for v in out.values() if v["fts"]))
print("  with a Wikipedia sentence:", sum(1 for v in out.values() if v["wiki"]))
print("  press F only (article matched, title silent):", sum(1 for v in out.values() if v["press_F"] and not has(v, "press_T", "fts", "wiki")))
print("  parametric only:", sum(1 for v in out.values() if v["param"] and not has(v, "press_T", "press_F", "fts", "wiki")))
print("  public-trade headlines only:", sum(1 for v in out.values() if v["press_P"] and not has(v, "press_T", "press_F", "fts", "wiki", "param")))
if missing:
    print("MISSING inputs:", missing)
