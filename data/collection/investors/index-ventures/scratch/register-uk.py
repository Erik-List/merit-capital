#!/usr/bin/env python3
"""UK register sweep (decisions.md D10, 'status first'): for every GB row whose status is private or unknown, search
Companies House (the public register website, through scratch/companies_house.py) for the legal entity and read its
status. Writes sources/registers/companies-house/uk-sweep.json: per row the query names tried and the candidates with
status, incorporation date, dissolution date, SIC codes and previous names. Identity is the judge's call, never the
script's: the script only ranks candidates (name match first, then incorporation before the firm first listed the row).
    python3 scratch/register-uk.py [slug ...]"""
import csv, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent
sys.path.insert(0, str(H))
import companies_house as ch
OUT = R / "sources/registers/companies-house/uk-sweep.json"; OUT.parent.mkdir(parents=True, exist_ok=True)
out = json.loads(OUT.read_text()) if OUT.exists() else {}
ALT = json.loads((H / "register-uk-names.json").read_text()) if (H / "register-uk-names.json").exists() else {}
norm = lambda s: re.sub(r"[^a-z0-9]+", "", re.sub(r"\b(limited|ltd|plc|llp|uk|group|holdings|technologies|technology|labs|the)\b", "", s.lower()))
rows = [r for r in csv.DictReader(open(R / "companies/base.csv")) if r["hq_country"] == "GB" and r["status"] in ("private", "unknown")]
want = set(sys.argv[1:])
for r in rows:
    s = r["slug"]
    if want and s not in want: continue
    if s in out and not want: continue
    names = [r["name"]] + ALT.get(s, [])
    cands = {}
    for q in names:
        try: res = ch.search_companies(q)
        except ch.Unavailable as e: print("UNAVAILABLE", s, q, e); res = None
        if res is None: continue
        nq = norm(q)
        for i, c in enumerate(res[:20]):
            nc = norm(c["name"])
            score = 3 if nc == nq else 2 if nc.startswith(nq) or nq.startswith(nc) else 1 if nq in nc else 0
            if score and (c["number"] not in cands or score > cands[c["number"]]["score"]): cands[c["number"]] = {**c, "score": score, "rank": i, "query": q, "qi": names.index(q)}
    # an exact hit on a legal name the judge supplied outranks an exact hit on the brand name (a namesake more often than not)
    top = sorted(cands.values(), key=lambda c: (-c["score"], -min(c.get("qi", 0), 1), c["rank"]))[:5]
    for c in top:
        try: c["profile"] = ch.company(c["number"])
        except ch.Unavailable as e: c["profile"] = {"error": str(e)}
    out[s] = {"name": r["name"], "status_before": r["status"], "first_seen": r["first_seen"], "queries": names, "candidates": top}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"{s:22s} {r['status']:8s} fs {r['first_seen']} | " + " || ".join(f"{c['name']} [{c['number']}] {c.get('profile',{}).get('status','?')} inc {c.get('profile',{}).get('incorporated','?')}" + (f" diss {c['profile']['dissolved']}" if c.get('profile',{}).get('dissolved') else "") for c in top)[:330], flush=True)
