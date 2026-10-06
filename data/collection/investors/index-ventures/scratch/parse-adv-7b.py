"""Parse Form ADV Schedule D Section 7.B.(1) private-fund rosters from the
Index Ventures and Medicxi adviser PDFs (data/filings/index-ventures/adv/<CRD>.pdf, gitignored; IAPD reports.adviserinfo.sec.gov/reports/ADV/<CRD>/PDF/<CRD>.pdf) into
sources/registers/adv-7b-funds.json. Per-page extraction (pypdf's whole-document
text repeats pages), one record per fund: name, 805- ID, GAV, filing adviser.
Deduped by private fund ID across advisers (COLLECTION.md 11: co-advisers of
one desk report identical rosters). Section 7.B.(2) (sub-advised funds reported
by another adviser) carries no GAV and is recorded as a reference list."""
import json, re, sys
from pathlib import Path
import pypdf
REG = Path(__file__).resolve().parents[1] / "sources" / "registers"
RAW = Path(__file__).resolve().parents[5] / "data" / "filings" / "index-ventures" / "adv"
out = {"_readme": __doc__, "advisers": {}, "funds": []}
seen = {}
for pdf in sorted(RAW.glob("*.pdf")):
    crd = pdf.stem
    r = pypdf.PdfReader(str(pdf))
    pages = [p.extract_text() or "" for p in r.pages]
    first = pages[0]
    name = re.search(r"Primary Business Name:(.*?) CRD Number", first)
    filed = re.search(r"(Annual Amendment|Other-Than-Annual Amendment|Initial Application)[^\n]*\n(\d+/\d+/\d{4})", first)
    adv = {"crd": crd, "adviser": name.group(1).strip() if name else None,
           "filed": filed.group(2) if filed else None, "funds_7b1": [], "funds_7b2": []}
    # pypdf's per-page text is cumulative within a run of pages (each page repeats the run so far), and a fund
    # block can straddle two runs. So read the LAST page of every run, join them into one linear text, and pair
    # each fund name with the ID and the gross asset value that follow it before the next name. (The first
    # version paired within a page and carried one pending fund forward; on this PDF four funds then took the
    # same carried value. Fixed 2026-10-06; the sum is re-proved below against the per-fund list.)
    NAME = re.compile(r"1\. \(a\) Name of the private fund:\s*\n(.*?)\n")
    GAV = re.compile(r"11\. Current gross asset value of the private fund:\s*\n\$\s*([\d,]+)")
    runs = [t for i, t in enumerate(pages) if i + 1 == len(pages) or len(pages[i + 1]) < len(t)]
    linear = "\n".join(runs)
    sec2 = linear.find("SECTION 7.B.(2)")
    names = [m for m in NAME.finditer(linear) if sec2 < 0 or m.start() < sec2]
    for k, m in enumerate(names):
        end = names[k + 1].start() if k + 1 < len(names) else (sec2 if sec2 >= 0 else len(linear))
        block = linear[m.end():end]
        fid = re.search(r"(805-\d+)", block); g = GAV.search(block)
        if not fid or any(f["id"] == fid.group(1) for f in adv["funds_7b1"]):
            continue
        adv["funds_7b1"].append({"name": m.group(1).strip(), "id": fid.group(1),
                                 "gav": int(g.group(1).replace(",", "")) if g else None})
    for t in pages:
        i = t.find("SECTION 7.B.(2)")
        if i < 0:
            continue
        for m in re.finditer(r"Name of the private fund:?\s*\n(.*?)\n(?:.*?\n)*?.*?(805-\d+)", t[i:]):
            if not any(f["id"] == m.group(2) for f in adv["funds_7b2"]):
                adv["funds_7b2"].append({"name": m.group(1).strip(), "id": m.group(2)})
    out["advisers"][crd] = adv
    for f in adv["funds_7b1"]:
        if f["id"] in seen:
            seen[f["id"]]["also_reported_by"].append(crd); continue
        rec = {**f, "reported_by": crd, "also_reported_by": []}
        seen[f["id"]] = rec; out["funds"].append(rec)
out["count"] = len(out["funds"])
out["sum_gross_asset_value_usd"] = sum(f["gav"] or 0 for f in out["funds"])
(REG / "adv-7b-funds.json").write_text(json.dumps(out, indent=1) + "\n")
for crd, a in out["advisers"].items():
    print(crd, a["adviser"], a["filed"], "7B1:", len(a["funds_7b1"]), "7B2:", len(a["funds_7b2"]),
          "sum:", sum(f["gav"] or 0 for f in a["funds_7b1"]))
print("deduped funds:", out["count"], "sum:", out["sum_gross_asset_value_usd"])
for f in out["funds"]: print("  ", f["reported_by"], f["id"], f["gav"], f["name"])
