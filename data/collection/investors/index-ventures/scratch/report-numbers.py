#!/usr/bin/env python3
"""Every number report.md quotes, read from the MERGED view over the live base (COLLECTION.md s8: a measurement reads
the merged view or it is wrong). Prints rows, not just totals, where a number will be quoted."""
import json, sys, collections
from pathlib import Path
H = Path(__file__).resolve().parent; sys.path.insert(0, str(H))
from merged import view
R = H.parent
V = view(); led = json.loads((R / "companies/membership-ledger.json").read_text())["index-ventures"]
M = {s: r for s, r in V.items() if r["verdict"] == "member"}
C = collections.Counter
n = len(M)
print("base rows", len(V), "members", n, "not_member", sum(1 for r in V.values() if r["verdict"] == "not_member"), "no verdict", [s for s, r in V.items() if not r["verdict"]])
print("ledger verdicts", C(v["verdict"] for v in led["verdicts"].values()), "recall additions", len(led["recall_additions"]))
st = C(r.get("status") for r in M.values()); print("status", [(k, v, f"{v/n:.1%}") for k, v in st.most_common()])
print("unknown rows:", sorted(r["name"] for r in M.values() if r.get("status") == "unknown"))
band = C(r.get("valuation_range") for r in M.values()); print("band", band.most_common())
big = sorted([r for r in M.values() if r.get("valuation_range") in ("1b_plus", "10b_plus", "100b_plus")], key=lambda r: -(float(r.get("valuation_usd") or 0)))
print("$1B+ rows", len(big), f"{len(big)/n:.1%}")
for b in ("100b_plus", "10b_plus", "1b_plus"):
    print(" ", b, "; ".join(f"{r['name']} ${float(r.get('valuation_usd') or 0)/1e9:.2f}B{' (public)' if r.get('status') == 'public' else ''}{' (' + r['status'] + ')' if r.get('status') not in ('public', 'private') else ''}" for r in big if r["valuation_range"] == b))
print("public rows", sorted((r["name"], r.get("valuation_range")) for r in M.values() if r.get("status") == "public"))
print("visible band sources", C(r.get("valuation_source") for r in big))
stage = C(r.get("entry_stage") for r in M.values()); print("entry stage", stage.most_common())
print("stage sources (decided)", C(r.get("entry_stage_source") for r in M.values() if r.get("entry_stage") not in (None, "undetermined")).most_common())
print("stage confidence", C(r.get("entry_stage_confidence") for r in M.values() if r.get("entry_stage") not in (None, "undetermined")).most_common())
cty = C(r.get("hq_country") for r in M.values()); print("countries", cty.most_common(14), "distinct", len(cty))
city = C(r.get("hq_city") for r in M.values() if r.get("hq_city")); print("cities filled", sum(city.values()), "top", city.most_common(10))
print("focus", C(r.get("focus") for r in M.values()).most_common())
print("membership evidence", C((led["verdicts"].get(s) or {}).get("evidence_class") for s in M).most_common())
seeds = {s: r for s, r in M.items() if r.get("entry_stage") == "Seed"}
g = C(r.get("seed_to_a_graduation") for r in seeds.values()); coh = g["graduated"] + g["not_graduated"]
print("S2A: seed", len(seeds), "censored", g["censored"], "cohort", coh, "graduated", g["graduated"], "not", g["not_graduated"], "rate", f"{g['graduated']/coh:.1%}" if coh else "-", "other", {k: v for k, v in g.items() if k not in ("graduated", "not_graduated", "censored")})
nos = [r for r in seeds.values() if r.get("seed_to_a_graduation") == "not_graduated"]
print("  nos by source", C(r.get("graduation_source") for r in nos).most_common(), "| by status", C(r.get("status") for r in nos).most_common())
print("  nos:", sorted(r["name"] for r in nos))
print("  yes by source", C(r.get("graduation_source") for r in seeds.values() if r.get("seed_to_a_graduation") == "graduated").most_common())
def period(d):
    y = int(str(d)[:4]) if d and str(d)[:4].isdigit() else None
    return "no date" if y is None else "to 2011" if y <= 2011 else "2012-2015" if y <= 2015 else "2016-2019" if y <= 2019 else "2020-2022" if y <= 2022 else "2023 on"
per = collections.defaultdict(C)
for r in seeds.values(): per[period(r.get("entry_date"))][r.get("seed_to_a_graduation")] += 1
for k in ("to 2011", "2012-2015", "2016-2019", "2020-2022", "2023 on", "no date"):
    c = per[k]; t = c["graduated"] + c["not_graduated"]
    print(f"  {k}: {c['graduated']} of {t}" + (f" ({c['graduated']/t:.0%})" if t else "") + f", censored {c['censored']}")
fl = C(f for r in M.values() for f in (r.get("flags") or [])); print("flags", fl.most_common())
print("undetermined stage rows", sum(1 for r in M.values() if r.get("entry_stage") in (None, "undetermined")))
ent = C(period(r.get("entry_date")) for r in M.values()); print("entry period, all members", ent.most_common())
