"""SPV fingerprinting: a deal vehicle's own Form D (first sale date, amount sold)
against the bulk Form D universe. Candidates are operating issuers whose round
has a first-sale date within WINDOW days of the vehicle's and sold at least the
vehicle's amount; the list is then cut to companies the firm is otherwise known
to hold (live site, archive slugs, base). Writes sources/edgar/spv-fingerprint.json."""
import csv, io, json, re, sys, zipfile, datetime as dt
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from paths import Paths, write_atomic
p = Paths("founders-fund")
WINDOW = 45
spv = [r for r in json.loads((p.root / "sources/edgar/spv-formd.json").read_text()) if r["form"] == "D"]
def d(s):
    s = (s or "")[:10]
    try: return dt.date.fromisoformat(s)
    except ValueError: return None
targets = [(r["issuer"], d(r["first_sale"]), float(r["sold"])) for r in spv]
known = set()
def nk(s): return re.sub(r"[^a-z0-9]", "", re.sub(r"\b(inc|corp|corporation|llc|ltd|co|technologies|labs|holdings)\b\.?", "", s.lower()))
for r in json.loads(p.base_json.read_text()): known.add(nk(r["name"]))
for f in (p.wayback / "parsed").glob("*.json"):
    for r in json.loads(f.read_text()): known.add(nk(r.get("name") or r["slug"].replace("-", " ")))
for r in json.loads((p.root / "sources/site/companies.json").read_text()): known.add(nk(r.get("name", "")))
known.discard("")
csv.field_size_limit(10**9)
out = {t[0]: [] for t in targets}
for z in sorted((ROOT / "data/filings/form-d").glob("*.zip")):
    yr = int(z.stem[:4])
    if not any(t[1] and abs(t[1].year - yr) <= 1 for t in targets): continue
    with zipfile.ZipFile(z) as zf:
        names = {n.split("/")[-1].upper(): n for n in zf.namelist()}
        def rows(key):
            with zf.open(names[key]) as f:
                yield from csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"), delimiter="\t")
        off = {}
        for r in rows("OFFERING.TSV"):
            sd = d(r.get("SALE_DATE"))
            try: sold = float(r.get("TOTALAMOUNTSOLD") or 0)
            except ValueError: sold = 0
            if not sd or r.get("INDUSTRYGROUPTYPE") == "Pooled Investment Fund": continue
            for name, tdate, tamt in targets:
                if tdate and abs((sd - tdate).days) <= WINDOW and sold >= tamt:
                    off.setdefault(r["ACCESSIONNUMBER"], []).append((name, sd.isoformat(), sold))
        if not off: continue
        for r in rows("ISSUERS.TSV"):
            a = r["ACCESSIONNUMBER"]
            if a in off and r.get("IS_PRIMARYISSUER_FLAG", "YES").upper() != "NO":
                for name, sd, sold in off[a]:
                    out[name].append({"issuer": r.get("ENTITYNAME"), "cik": r.get("CIK"), "accession": a, "first_sale": sd,
                                      "sold": sold, "known_position": nk(r.get("ENTITYNAME") or "") in known})
res = {}
for name, tdate, tamt in targets:
    c = out[name]; k = [x for x in c if x["known_position"]]
    res[name] = {"vehicle_first_sale": tdate.isoformat(), "vehicle_sold": tamt, "window_days": WINDOW,
                 "candidates_all": len(c), "candidates_known": sorted(k, key=lambda x: x["first_sale"])}
    print(f"{name} | {tdate} ${tamt/1e6:.1f}M | all candidates {len(c)} | known positions:",
          "; ".join(f"{x['issuer']} ({x['first_sale']}, ${x['sold']/1e6:.0f}M)" for x in res[name]["candidates_known"]) or "none")
write_atomic(p.root / "sources/edgar/spv-fingerprint.json", json.dumps(res, indent=1) + "\n")
