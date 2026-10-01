"""Parse Form ADV Schedule D Section 7.B.(1) private-fund rosters from Kleiner Perkins' ADV (CRD 161035) and
KPCB China's (CRD 161470), sources/adv/<CRD>.pdf, into sources/adv/adv-7b-funds.json. pypdf's per-page text is
cumulative within runs of pages and a fund's gross asset value can sit a page or more below its name, so each fund
takes the value from the first page on which its OWN block (from its name to the next fund name, or the page end)
carries line 11. Section 7.B.(2) funds (reported by another adviser) carry no value and are listed separately.
Deduped by private fund ID. (Adapted from ivp/scratch/parse-adv-7b.py, whose pairing misread this layout: six
Select-family funds all read $18,659,493.)"""
import json, re
from pathlib import Path
import pypdf
REG = Path(__file__).resolve().parents[1] / "sources" / "adv"
PDFS = Path(__file__).resolve().parents[5] / "data" / "filings" / "adv"  # the ADV PDFs (gitignored, re-downloadable from reports.adviserinfo.sec.gov)
NAME = re.compile(r"Name of the private fund:\s*\n(.*?)\n")
GAV = re.compile(r"11\. Current gross asset value of the private fund:\s*\n\$\s*([\d,]+)")
out = {"_readme": __doc__, "advisers": {}, "funds": []}
for crd in ("161035", "161470"):
    r = pypdf.PdfReader(str(PDFS / f"{crd}.pdf"))
    pages = [p.extract_text() or "" for p in r.pages]
    first = pages[0]
    nm = re.search(r"Primary Business Name:(.*?) CRD Number", first)
    funds, ids, sec2 = {}, {}, {}
    for t in pages:
        cut = t.find("SECTION 7.B.(2)")
        ms = list(NAME.finditer(t))
        for k, m in enumerate(ms):
            name = m.group(1).strip()
            end = ms[k + 1].start() if k + 1 < len(ms) else len(t)
            blk = t[m.end():end]
            if cut >= 0 and m.start() > cut:
                fid = re.search(r"(805-\d+)", blk)
                sec2.setdefault(name, fid.group(1) if fid else None)
                continue
            fid = re.search(r"(805-\d{10})", blk)
            if fid:
                ids.setdefault(name, fid.group(1))
            g = GAV.search(blk)
            if g and name not in funds:
                funds[name] = int(g.group(1).replace(",", ""))
    adv = {"crd": crd, "adviser": nm.group(1).strip() if nm else None,
           "funds_7b1": [{"name": n, "id": ids.get(n), "gav": funds.get(n)} for n in sorted(set(ids) | set(funds))],
           "funds_7b2": [{"name": n, "id": i} for n, i in sorted(sec2.items()) if n not in ids]}
    out["advisers"][crd] = adv
    for f in adv["funds_7b1"]:
        out["funds"].append({**f, "reported_by": crd})
out["sum_by_adviser"] = {c: sum(f["gav"] or 0 for f in a["funds_7b1"]) for c, a in out["advisers"].items()}
out["sum_gross_asset_value_usd"] = sum(out["sum_by_adviser"].values())
(REG / "adv-7b-funds.json").write_text(json.dumps(out, indent=1) + "\n")
for f in out["funds"]:
    print(f["reported_by"], f["id"], f"{f['gav']:,}" if f["gav"] else None, f["name"])
print(out["sum_by_adviser"], f"{out['sum_gross_asset_value_usd']:,}")
print("7B2:", [(a["crd"], [x["name"] for x in a["funds_7b2"]]) for a in out["advisers"].values()])
