"""PRO-82 grind, the life sciences desk (decisions.md D3): every company the firm's own site classed as Life
Sciences (2008-2013 /portfolio/index/industry_id/2 listings), every company whose only Index Team on the
2014-2015 pages is the Life Sciences team, and the Life VI positions. Verdict not_member, preserved in
excluded.json; the basis carries `life_sciences_desk` so the class is countable and reversible in one pass."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
H = Path(__file__).resolve().parent
q = json.load(open(H / "queue" / "queue.json"))
LIFE_TEAM = {"Francesco De Rubertis", "Kevin Johnson", "Michèle Ollier", "David Grainger", "Roman Fleck", "Mark de Boer", "Mark De Boer"}
# rows the archive captures give no desk for, named here with the reason (each a biotech or medical-device
# company on the firm's 2008-2014 lists or a Life VI / Medicxi filing)
EXTRA = {
 "micromet": "the firm's own news item of 2008-10-03, 'Index Growth makes first biotech investment in Micromet'; the funds' 13D/G filings",
 "minerva-neurosciences": "formed in 2013 from Cyrenaic and Mind-NRG, both on the Life Sciences list; the Index funds' 13D filings from the 2014 IPO",
 "profibrix": "a biotech (fibrinogen haemostat, Leiden) on the firm's 2008-2013 list beside the Life Sciences companies; sold to The Medicines Company in 2013",
 "sgx-pharma": "SGX Pharmaceuticals (San Diego), a biotech on the firm's 2008-2012 list; its 2005 S-1 names the Index funds",
 "medicentrix": "a healthcare services company on the 2008 list tagged '(Galenica)', the Swiss pharma group that bought it",
 "epsilon-3-bio": "Epsilon 3 Bio, an asset-centric biotech of the life sciences practice (the firm's 2014 page)",
 "centessa-pharmaceuticals-plc": "formed in 2021 from Medicxi's asset-centric companies; the holder of record is Index Ventures Life VI (Jersey) L.P., sub-advised by Medicxi (13G filings 2021-2026)",
}
L = []
for i in q:
    s = i["slug"]
    a = (jl.ev(s).get("archive") or {})
    desk = {x["value"] for x in a.get("desk", [])}
    team = {n for x in a.get("partners", []) for n in x["value"]}
    if "life" in desk:
        basis = "life_sciences_desk (decisions.md D3): on the firm's own Life Sciences list (industry_id/2), a practice that became Medicxi in 2016 with its whole book"
        cite = jl.arch(s, "desk", "life")
    elif team and team <= LIFE_TEAM:
        basis = f"life_sciences_desk (decisions.md D3): the firm's 2014-2015 page names only the Life Sciences team ({', '.join(sorted(team))}); the practice became Medicxi in 2016 with its whole book"
        cite = jl.arch(s, "partners")
    elif s in EXTRA:
        basis = f"life_sciences_desk (decisions.md D3): {EXTRA[s]}; the practice became Medicxi in 2016 with its whole book"
        cite = i.get("wayback_first_link") or (i.get("edgar_links") or "").split("; ")[0] or None
    else:
        continue
    L.append(jl.verdict(s, "not_member", basis, ec="site_listing" if i.get("wayback_years") else "fund_filing", conf="medium", cite=cite))
print(len(L), [x["slug"] for x in L])
jl.write("life-desk", L)
