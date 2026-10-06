#!/usr/bin/env python3
"""French register sweep (decisions.md D10): for FR rows that read private or unknown, the state's open company search
(recherche-entreprises.api.gouv.fr, the Sirene register, no key) gives the legal unit, its creation date, its
administrative state (A = active, C = ceased) and closing date, and its officers. Writes
sources/registers/sirene/fr-sweep.json. Identity is the judge's call; the script lists the top candidates.
    python3 scratch/register-fr.py [slug=Query ...]"""
import csv, json, subprocess, sys, time, urllib.parse
from pathlib import Path
H = Path(__file__).resolve().parent; R = H.parent
OUT = R / "sources/registers/sirene/fr-sweep.json"; OUT.parent.mkdir(parents=True, exist_ok=True)
out = json.loads(OUT.read_text()) if OUT.exists() else {}
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
def search(q):
    u = "https://recherche-entreprises.api.gouv.fr/search?per_page=6&q=" + urllib.parse.quote(q)
    for attempt in range(3):
        r = subprocess.run(["curl", "-s", "-m", "30", "-A", UA, "-w", "\n%{http_code}", u], capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code == "200": return json.loads(body)
        time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"{q}: http {code}")
rows = {r["slug"]: r for r in csv.DictReader(open(R / "companies/base.csv")) if r["hq_country"] == "FR" and r["status"] in ("private", "unknown")}
alt = dict(a.split("=", 1) for a in sys.argv[1:] if "=" in a)
for s, r in rows.items():
    if alt and s not in alt: continue
    if s in out and not alt: continue
    q = alt.get(s, r["name"])
    try: d = search(q)
    except Exception as e: print("FAILED", s, e); continue
    cands = []
    for x in d.get("results", [])[:6]:
        sg = x.get("siege") or {}
        cands.append({"siren": x.get("siren"), "name": x.get("nom_complet"), "created": x.get("date_creation"), "state": x.get("etat_administratif"),
                      "closed": x.get("date_fermeture"), "city": sg.get("libelle_commune"), "naf": x.get("activite_principale"), "category": x.get("categorie_entreprise"),
                      "employees": x.get("tranche_effectif_salarie"), "officers": [((o.get("prenoms") or "") + " " + (o.get("nom") or o.get("denomination") or "")).strip() for o in (x.get("dirigeants") or [])][:6],
                      "url": f"https://annuaire-entreprises.data.gouv.fr/entreprise/{x.get('siren')}"})
    out[s] = {"name": r["name"], "query": q, "status_before": r["status"], "total": d.get("total_results"), "candidates": cands, "checked": "2026-10-06"}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(f"{s:14s} {r['status']:8s} q={q!r} total {d.get('total_results')} | " + " || ".join(f"{c['name']} [{c['siren']}] {c['state']} cr {c['created']}{' closed ' + c['closed'] if c['closed'] else ''} {c['city']} naf {c['naf']} off {', '.join(c['officers'][:2])}" for c in cands[:3])[:420], flush=True)
    time.sleep(0.6)
