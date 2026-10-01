"""Apply the stage second pass (scratch/research/stage2-*.json): where it found a page
naming the round Speedinvest first joined, record the stage with that citation
(first_party for the firm's own post, web_verified otherwise, medium confidence), and for
a Seed entry decide the graduation on the pass's finding. Only rows whose stage is
`undetermined` or was banded under R1 (`model`) are touched; a cited round overrides a band.
  python3 apply_stage2.py <file-stem> [--dry]"""
import datetime, json, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J
import convert as C
TODAY = datetime.date(2026, 9, 30)
stem = sys.argv[1]
data = json.loads((H / "research" / f"{stem}.json").read_text())
cls = json.loads((J.INV / "companies/classification.json").read_text())
L = []
for slug, r in data.items():
    c = cls.get(slug)
    if not c or slug not in J.BASE:
        continue
    en = r.get("entry") or {}
    st = C.stage_of(en.get("round")) if en.get("round") else None
    cite = en.get("citation")
    if not (st and C.is_url(cite) and not C.VENDOR.match(cite)):
        continue
    if c.get("entry_stage") not in ("undetermined", None) and c.get("entry_stage_source") != "model":
        continue
    firm = "speedinvest.com" in cite or "medium.com/speedinvest" in cite
    d = str(en.get("date") or "")
    m = re.match(r"\d{4}(-\d{2}){0,2}", d)
    edate = m.group(0) if m else None
    rec = {"slug": slug, "who": J.WHO, "entry_stage": st, "entry_stage_source": "first_party" if firm else "web_verified",
           "entry_stage_confidence": "medium", "entry_stage_citation": cite,
           "note": f"Stage second pass 2026-09-30: {en.get('round')} ({d}) named on the cited page; {(en.get('how_first') or '')[:260]}"}
    if c.get("entry_stage_source") == "model":
        rec["clear_flags"] = ["stage_uncited"]
    if edate:
        rec["entry_date"] = edate
    if st == "Seed":
        g = r.get("graduation") or {}
        later = C.stage_of(g.get("later_round")) if g.get("later_round") else None
        ld = C.latest_day(edate)
        stt, st_cite = c.get("status"), c.get("status_citation")
        if not edate:
            continue
        if later in ("Series A", "Growth") and C.is_url(g.get("citation")) and not C.VENDOR.match(g["citation"]):
            rec.update(seed_to_a_graduation="graduated", graduation_source=C.src_of(g["citation"]), graduation_citation=g["citation"])
        elif stt in ("acquired", "defunct") and C.is_url(st_cite):
            rec.update(seed_to_a_graduation="not_graduated", graduation_source=C.src_of(st_cite), graduation_citation=st_cite,
                       graduation_asof=TODAY.isoformat(),
                       graduation_surfaces=J.surfaces_lines(slug, "no later round found before the sale or shutdown"))
        elif C.months_between(ld, TODAY) < 24:
            rec["seed_to_a_graduation"] = "censored"
        else:
            rec.update(seed_to_a_graduation="not_graduated", graduation_source="absence_check", graduation_asof=TODAY.isoformat(),
                       graduation_surfaces=J.surfaces_lines(slug, "no later round named"))
        if rec.get("seed_to_a_graduation") == "not_graduated" and c.get("hq_country") == "US":
            rec["graduation_surfaces"].append("formd: EDGAR company search for the name -> no Form D sequence after the entry")
    elif c.get("seed_to_a_graduation"):
        rec["seed_to_a_graduation"] = None
    L.append(rec)
for x in L:
    print(" ", x["slug"], x["entry_stage"], x.get("entry_date"), x["entry_stage_source"], x.get("seed_to_a_graduation"))
J.write(f"apply-{stem}", L, record="--dry" not in sys.argv)
