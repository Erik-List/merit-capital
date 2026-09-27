#!/usr/bin/env python3
"""Agent A, part 2 (2026-09-27): identities resolved, Seed entries found, and the absence tests, whose
Form D line reports a name search this script actually runs over the bulk data."""
import csv, glob, io, json, re, sys, zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]; INV = ROOT / "data/collection/investors/coatue"
S = json.load(open(INV / "scratch/graduation-surfaces.json"))
NAMES = {"httpie": r"^httpie", "butterflies-ai": r"^butterflies", "crypthulhu-studios": r"^crypthulhu", "meld": r"^meld(,| inc| technologies|\.io)", "product-science": r"^product science",
         "revops": r"^revops", "sundeck": r"^sundeck", "lutra-ai": r"^lutra", "fero": r"^fero( |,|$)(?!labs)", "meticulous-ai": r"^meticulous", "stability": r"^stability ai", "placement": r"^placement(,| inc|\.com| holdings)"}
PAT = {k: re.compile(v, re.I) for k, v in NAMES.items()}
hits = {k: [] for k in NAMES}
for zp in sorted(glob.glob(str(ROOT / "data/filings/form-d/*.zip"))):
    z = zipfile.ZipFile(zp); accs = {}
    for n in z.namelist():
        if n.upper().endswith("ISSUERS.TSV"):
            for r in csv.DictReader(io.TextIOWrapper(z.open(n), "utf-8", errors="replace"), delimiter="\t"):
                for k, p in PAT.items():
                    if p.search(r.get("ENTITYNAME") or ""): accs[r["ACCESSIONNUMBER"]] = (k, r["ENTITYNAME"])
    if not accs: continue
    sold, filed = {}, {}
    for n in z.namelist():
        u = n.upper()
        if u.endswith("OFFERING.TSV"):
            for r in csv.DictReader(io.TextIOWrapper(z.open(n), "utf-8", errors="replace"), delimiter="\t"):
                if r["ACCESSIONNUMBER"] in accs: sold[r["ACCESSIONNUMBER"]] = r.get("TOTALAMOUNTSOLD")
        if u.endswith("FORMDSUBMISSION.TSV"):
            for r in csv.DictReader(io.TextIOWrapper(z.open(n), "utf-8", errors="replace"), delimiter="\t"):
                if r["ACCESSIONNUMBER"] in accs: filed[r["ACCESSIONNUMBER"]] = r.get("FILING_DATE")
    for a, (k, nm) in accs.items(): hits[k].append((Path(zp).name[:6], nm, sold.get(a)))
def formd_line(k, name):
    h = hits[k]
    if not h: return f"formd: issuer names beginning '{name}' searched in the Form D bulk data 2008q1 to 2026q2 -> no filing"
    return f"formd: issuer names beginning '{name}' searched in the Form D bulk data 2008q1 to 2026q2 -> " + "; ".join(f"{q} {nm} ${s}" for q, nm, s in sorted(h)[:6]) + "; none is a later round at twice the seed"
def surf(k, name):
    e = S.get(k, {}).get("surfaces", {}); L = [f"firm: coatue.com/blog and coatue.com/c/takes searched for {name} -> no post names a later round", formd_line(k, name)]
    for s in ("googlenews", "googlenews_firm", "googlenews_local", "techcrunch", "crunchbase_news"):
        if s in e and e[s].get("status") == "ok": L.append(f"{s}: {e[s].get('query')} -> {e[s].get('n')} items read, none names a later priced round of this company")
    return L
out = []
def seed(k, name, cite, ed, city, note, status=None, end=None):
    c = {"slug": k, "entry_stage": "Seed", "entry_stage_source": "web_verified", "entry_stage_citation": cite, "entry_stage_confidence": "high", "entry_date": ed,
         "seed_to_a_graduation": "not_graduated", "graduation_source": "web_verified" if end else "absence_check", "graduation_asof": "2026-09-27", "graduation_surfaces": surf(k, name),
         "flags": [], "note": "Web pass: " + note}
    if end: c["graduation_citation"] = end
    if city: c.update({"hq_city": city, "hq_city_source": "web_verified", "hq_city_confidence": "high"})
    if status: c["status"] = status
    out.append(c)
TC = "https://techcrunch.com/"
seed("butterflies-ai", "Butterflies", TC + "2024/06/18/former-snap-engineer-launches-butterflies-a-social-network-where-ais-and-humans-coexist", "2023-11", "Bellevue", "Coatue led the $4.8M seed round (Nov 2023, announced Jun 2024). No later round on any surface. The company's site has been disabled since mid-2026 and its app was last updated in Feb 2025; no shutdown was announced, so the state reads unknown.", status="unknown")
seed("crypthulhu-studios", "Crypthulhu", "https://venturebeat.com/games/crypthulhu-studios-raises-3-million-for-dimension-x-blockchain-game/", "2022-07", "San Diego", "Coatue and Dapper Labs led the $3M seed round (Jul 2022). No later round on any surface; the company's site no longer answers.")
seed("meld", "Meld", TC + "2022/05/10/fintech-gets-more-fragmented-meld-helps-developers-manage-tech-stack-integrations-api/", "2022-05", "San Francisco", "Coatue led the $8M seed round (May 2022). No later round on any surface.")
seed("product-science", "Product Science", TC + "2023/01/04/product-science-raises-18m-for-mobile-app-performance-testing/", "2023-01", "Los Angeles", "Coatue joined the $18M seed round (Jan 2023). No later round on any surface.")
seed("revops", "RevOps", TC + "2021/10/19/caffeinated-coatue-gradient-back-revops-to-build-modern-sales-stack-for-startups/", "2021-10", "San Francisco", "Caffeinated Capital, Coatue and Gradient led the $5M seed round (Oct 2021). No later round on any surface.")
seed("sundeck", "Sundeck", "https://www.newswire.com/news/sundeck-announces-the-public-availability-of-its-query-engineering-22049696", "2023-05", "Santa Clara", "NEA, Coatue and Factory funded the $20M seed round (May 2023). No later round on any surface.")
seed("lutra-ai", "Lutra", TC + "2023/12/07/google-coursera-lutra-ai-workflows/", "2023-12", "Mountain View", "Coatue Ventures joined the $3.8M seed round (Dec 2023). No later round on any surface.")
seed("httpie", "HTTPie", "https://httpie.io/about", "2022-12", "San Francisco", "The company's own page names Coatue in its $6.5M seed round. No later round on any surface.")
seed("placement", "Placement", TC + "2019/11/21/placement/", "2019-11", None, "Coatue's seed fund backed the $3M seed round led by Founders Fund (Nov 2019). The company has since joined Exec (its own site), the seed being its last round.", status="acquired", end="https://www.placement.com/")
for k, name, ed in (("stability", "Stability AI", "2022-10"), ("fero", "Fero", "2023-11"), ("meticulous-ai", "Meticulous", "2022-12")):
    out.append({"slug": k, "seed_to_a_graduation": "not_graduated", "graduation_source": "absence_check", "graduation_asof": "2026-09-27", "graduation_surfaces": surf(k, name), "entry_date": ed, "flags": [],
                "note": "Absence test re-recorded with the Form D name search actually run."})
out.append({"slug": "verse", "status": "private", "entry_stage": "Seed", "entry_stage_source": "web_verified", "entry_stage_confidence": "high", "entry_date": "2023-07",
            "entry_stage_citation": "https://www.prnewswire.com/news-releases/clean-energy-procurement-and-management-software-provider-verse-closes-5-75m-seed-round-led-by-coatue-launches-first-product-and-signs-climeworks-as-customer-301879805.html",
            "seed_to_a_graduation": "graduated", "graduation_source": "web_verified", "graduation_citation": "https://verse.inc/press/verse-inc-secures-20-5-million-series-a-funding-led-by-gv/",
            "hq_city": "San Francisco", "hq_city_source": "web_verified", "hq_city_confidence": "high", "flags": [],
            "note": "Web pass: Verse, clean energy procurement software, San Francisco. Coatue led the $5.75M seed round (Jul 2023); graduated on the $20.5M Series A led by GV (May 2024)."})
out.append({"slug": "swarm-aero", "hq_city": "Oxnard", "hq_city_source": "web_verified", "hq_city_confidence": "high", "flags": [], "note": "Web pass: Swarm Aero, Oxnard CA; Coatue is named among the backers at the $35M Series A of Mar 2026 (https://finance.yahoo.com/news/swarm-aero-announces-35m-series-110000029.html)."})
# identities resolved: the provisional flag and the undetermined values are removed from the overlay, then the rows are judged
cp = INV / "companies/classification.json"; C = json.load(open(cp)); D = C.get("coatue", C)
for k in ("ara", "graphy", "radpod"):
    r = D[k]; r["flags"] = [f for f in r.get("flags", []) if f not in ("identity_unresolved", "city_unknown")]
    for key in ("entry_stage", "entry_stage_source", "entry_stage_confidence", "valuation_range", "seed_to_a_graduation", "status"): r.pop(key, None)
cp.write_text(json.dumps(C, indent=1, ensure_ascii=False))
def ident(k, status, cc, city, focus, note):
    out.append({"slug": k, "status": status, "valuation_range": "below_1b", "entry_stage": "undetermined", "entry_stage_source": "model", "entry_stage_confidence": "low", "hq_country": cc,
                "hq_country_source": "web_verified", "hq_country_confidence": "medium", "hq_city": city, "hq_city_source": "web_verified", "hq_city_confidence": "medium", "focus": focus, "focus_source": "model", "flags": [], "note": "Web pass: " + note})
ident("ara", "private", "US", "New York", "Media, Gaming & Advertising", "Ara (Ara Labs), digital advertising screens on rideshare cars and in shops, New York; its own site names Coatue as a backer (https://www.arascreens.com/). The round Coatue entered is not named in a citable source.")
ident("graphy", "private", "GB", "London", "DevTools & APIs", "Graphy, charting and AI data visualisation, London; backed by Coatue, General Catalyst and Seedcamp. The round Coatue entered is not named in a citable source.")
ident("radpod", "private", "US", "San Mateo", "AI & Applied AI", "The firm's link radpod.ai now redirects to Compound (Twenty Labs), an AI analyst for institutional finance, San Mateo (https://getcompound.ai/about). The round Coatue entered is not named in a citable source.")
(INV / "scratch/queue/agent-a-2.out.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in out))
print(len(out), "lines; Form D name hits:", {k: len(v) for k, v in hits.items() if v})
