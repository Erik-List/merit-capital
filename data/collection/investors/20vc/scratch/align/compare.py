"""Every 20VC row shared with another book (the cross-investor join: the
loose name key or a shared CIK, minus pairs ruled distinct), with status,
band, figure, as-of and source on both sides; prints the pairs that differ in
any of them. Read-only."""
import csv, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[6]
INV = ROOT / "data" / "collection" / "investors"
STRIP = re.compile(r"\b(inc|corp|corporation|co|ltd|llc|plc|labs|technologies|technology|ai|io|com|software|holdings|group)\b")
CIK = re.compile(r"/edgar/data/(\d+)/")
def key(n):
    n = re.sub(r"[.,'’]", "", (n or "").lower()); n = STRIP.sub("", n)
    return re.sub(r"[^a-z0-9]+", " ", n).strip()
def ciks(r):
    s = set(CIK.findall(r.get("formd_links") or ""))
    if "cik_weak" not in (r.get("flags") or ""):
        s |= set(CIK.findall(r.get("edgar_links") or ""))
    return s
distinct, accepted = set(), {}
shared = json.loads((ROOT / "data" / "collection" / "cross-investor.json").read_text())
ents = {k: list(shared.get(k, [])) for k in ("distinct", "accepted")}
for f in INV.glob("*/companies/cross-rulings.json"):
    d = json.loads(f.read_text())
    for k in ents: ents[k] += d.get(k, [])
distinct = {frozenset(e["rows"]) for e in ents["distinct"]}
accepted = {frozenset(e["rows"]) for e in ents["accepted"]}
def rows(inv):
    p = INV / inv / "companies" / "base.csv"
    return list(csv.DictReader(open(p))) if p.exists() else []
mine = [r for r in rows("20vc") if r["valuation_range"] != "undetermined"]
others = {}
for d in sorted(INV.iterdir()):
    if d.name == "20vc" or not d.is_dir() or re.search(r" \d+$", d.name): continue
    others[d.name] = rows(d.name)
F = ("status", "valuation_range", "valuation_usd", "valuation_asof", "valuation_source")
out = []
for m in mine:
    for inv, rs in others.items():
        for o in rs:
            if o["valuation_range"] == "undetermined": continue
            if not ((key(m["name"]) and key(m["name"]) == key(o["name"])) or (ciks(m) & ciks(o))): continue
            pair = frozenset((f"20vc:{m['slug']}", f"{inv}:{o['slug']}"))
            if pair in distinct: continue
            diff = [f for f in F if (m[f] or "") != (o[f] or "") and not (f == "valuation_usd" and m[f] and o[f] and abs(float(m[f]) - float(o[f])) < 1)]
            if not diff: continue
            if diff == ["valuation_source"]: continue
            out.append((m["name"], inv, o["slug"], diff, {f: m[f] for f in F}, {f: o[f] for f in F}, o["valuation_citation"], pair in accepted))
for n, inv, s, diff, a, b, cite, acc in out:
    print(f"## {n} vs {inv}:{s} {'[accepted]' if acc else ''} differs in {diff}")
    print(f"   20vc : {a['status']} {a['valuation_range']} {a['valuation_usd']} asof {a['valuation_asof']} ({a['valuation_source']})")
    print(f"   other: {b['status']} {b['valuation_range']} {b['valuation_usd']} asof {b['valuation_asof']} ({b['valuation_source']}) {cite[:110]}")
print(len(out), "differing pairs")
