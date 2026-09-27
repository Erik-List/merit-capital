#!/usr/bin/env python3
"""Parse Coatue Management's Form ADV (CRD 157910; data/filings/adv/157910.pdf,
untracked bulk, 35 MB / 790 pages) into sources/registers/adv-157910.json:
Item 1.F principal office and Section 1.F other offices, Item 5.F RAUM,
Schedule A / B owners, and the Section 7.B.(1) private-fund roster (name, 805-
ID, domicile, general partner, gross asset value, minimum investment, number
of beneficial owners, master/feeder). The fund-type checkboxes of question 10
do not survive text extraction; the type is joined from each vehicle's own
Form D (sources/edgar/formd-own-issuers.json) by name. pypdf's per-page text is
cumulative within a run of pages, so each fund is kept at its first complete
reading per ID (the IVP parser's rule)."""
import json, re, sys
from pathlib import Path
import pypdf
ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/coatue"
PDF = ROOT / "data/filings/adv/157910.pdf"
CACHE = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e46af375-7462-4261-959d-b43f6f66e864/scratchpad/adv-157910-pages.jsonl")
if CACHE.exists():
    pages = [json.loads(l)["text"] for l in CACHE.open()]
else:
    pages = [p.extract_text() or "" for p in pypdf.PdfReader(str(PDF)).pages]
full = "\n".join(pages)
out = {"_readme": __doc__.strip(), "crd": 157910, "adviser": "COATUE MANAGEMENT, L.L.C."}
m = re.search(r"(Annual Amendment|Other-Than-Annual Amendment|Initial Application)[^\n]*\n(\d+/\d+/\d{4})", pages[0])
out["filing"] = {"kind": m.group(1), "date": m.group(2)} if m else None
m = re.search(r"F\. Principal Office and Place of Business\s*\n\(1\) Address[^\n]*\n(.*?)If this address is a private residence", full, re.S)
out["principal_office_raw"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
m = re.search(r"Discretionary: \(a\) \$ ([\d,]+) \(d\) (\d+)\s*\nNon-Discretionary: \(b\) \$ ([\d,]+) \(e\) (\d+)\s*\nTotal: \(c\) \$ ([\d,]+) \(f\) (\d+)", full)
out["raum"] = {"discretionary": int(m.group(1).replace(",", "")), "accounts": int(m.group(6)), "total": int(m.group(5).replace(",", ""))} if m else None
m = re.search(r"attributable to clients who\s*\nare non- United States persons\?\s*\n\$ ([\d,]+)", full)
out["raum_non_us"] = int(m.group(1).replace(",", "")) if m else None
# other offices
offices = []
for mo in re.finditer(r"Number and Street 1:\n(.*?)\nNumber and Street 2:\n(.*?)\nCity:\n(.*?)\nState:(.*?)Country:\n?(.*?)\nZIP\+4/Postal Code:\n?(.*?)\n.*?How many employees perform investment advisory functions from this office location\?\s*\n(\d+)", full, re.S):
    offices.append({"street": (mo.group(1) + " " + mo.group(2)).strip(), "city": mo.group(3).strip(), "state": mo.group(4).strip().strip("\n"),
                    "country": mo.group(5).strip(), "postal": mo.group(6).strip(), "advisory_staff": int(mo.group(7))})
out["other_offices"] = [o for o in offices if o["city"]]
# Schedule A / B
i = full.find("Schedule A"); j = full.find("Schedule B", i); k = full.find("Schedule C", j)
out["schedule_a_raw"] = full[i:j][:6000] if i >= 0 else None
out["schedule_b_raw"] = full[j:k][:6000] if j >= 0 else None
# 7.B.(1) funds
NAME = re.compile(r"1\. \(a\) Name of the private fund:\s*\n(.*?)\n")
funds, seen = [], {}
for pi, t in enumerate(pages):
    sec2 = t.find("SECTION 7.B.(2)")
    names = list(NAME.finditer(t))
    for k2, mm in enumerate(names):
        end = names[k2 + 1].start() if k2 + 1 < len(names) else len(t)
        block = t[mm.end():end]
        fid = re.search(r"(805-\d+)", block)
        gav = re.search(r"11\. Current gross asset value of the private fund:\s*\n\$\s*([\d,]+)", block)
        if not fid or not gav or (sec2 >= 0 and mm.start() > sec2):
            continue
        if fid.group(1) in seen:
            continue
        gp = re.search(r"Name of General Partner, Manager, Trustee, or Director\n(.*?)\n", block)
        dom = re.search(r"2\. Under the laws of what state or country is the private fund organized:\s*\nState:\s*(.*?)\n?Country:\s*\n?(.*?)\n", block)
        mininv = re.search(r"12\. Minimum investment commitment required of an investor in the private fund:\s*\n\$\s*([\d,]+)", block)
        owners = re.search(r"13\. Approximate number of the private fund's beneficial owners:\s*\n(\d+)", block)
        pct = re.search(r"14\. What is the approximate percentage of the private fund beneficially owned by you and your related persons:\s*\n(\d+)%", block)
        feeder = re.search(r"\(d\) If yes, what is the name and private fund identification number \(if any\) of the master fund in which this private fund invests\?\s*\nName of private fund:\s*\n(.*?)\n", block)
        rec = {"name": mm.group(1).strip(), "id": fid.group(1), "gp": gp.group(1).strip() if gp else None,
               "state": dom.group(1).strip() if dom else None, "country": dom.group(2).strip() if dom else None,
               "gav": int(gav.group(1).replace(",", "")), "min_investment": int(mininv.group(1).replace(",", "")) if mininv else None,
               "beneficial_owners": int(owners.group(1)) if owners else None, "pct_related": int(pct.group(1)) if pct else None,
               "master_fund": feeder.group(1).strip() if feeder and feeder.group(1).strip() else None, "page": pi + 1}
        seen[fid.group(1)] = rec; funds.append(rec)
# join Form D types by name
fd = json.load(open(INV / "sources/edgar/formd-own-issuers.json"))["filings"]
types = {}
for f in fd:
    types.setdefault(re.sub(r"[^a-z0-9]+", " ", f["issuer"].lower()).strip(), set()).add(f.get("fund_type") or "")
for r in funds:
    key = re.sub(r"[^a-z0-9]+", " ", r["name"].lower()).strip()
    r["formd_type"] = sorted(t for t in types.get(key, set()) if t) or None
out["funds_7b1"] = funds
out["funds_7b1_total_gav"] = sum(r["gav"] for r in funds)
(INV / "sources/registers").mkdir(parents=True, exist_ok=True)
(INV / "sources/registers/adv-157910.json").write_text(json.dumps(out, indent=1))
print("raum", out["raum"], "non-US", out["raum_non_us"]); print("offices", out["other_offices"])
print("funds", len(funds), "total GAV", f"{out['funds_7b1_total_gav']:,}")
for r in sorted(funds, key=lambda r: -r["gav"])[:60]:
    print(f"  ${r['gav']:>16,} owners={r['beneficial_owners']!s:5} min=${r['min_investment'] or 0:>10,} {r['name'][:55]:55} gp={str(r['gp'])[:35]} type={r['formd_type']} master={str(r['master_fund'])[:30]}")
print("=== Schedule A raw:\n", (out["schedule_a_raw"] or "")[:3500])
