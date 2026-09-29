#!/usr/bin/env python3
"""Parse Tiger Global Management's Form ADV (CRD 160318; data/filings/adv/160318.pdf,
untracked bulk, 277 pages, annual amendment of 2026-03-27) into
sources/registers/adv-160318.json: Item 1.F principal office and Section 1.F other
offices, Item 5.F RAUM, the relying advisers of the umbrella registration (Schedule R),
Schedule A owners and officers, and the Section 7.B.(1) private-fund roster (name,
805-ID, domicile, general partner, gross asset value, minimum investment, number of
beneficial owners, master/feeder). Adapted from coatue/scratch/parse-adv.py (PRO-78).

pypdf's per-page text is cumulative within a run of pages, so each fund is kept at its
first complete reading per ID (the IVP parser's rule), and a regex over the full text
reads each section once."""
import json, re, sys
from pathlib import Path
import pypdf

ROOT = Path(__file__).resolve().parents[5]
INV = ROOT / "data/collection/investors/tiger-global-management"
PDF = ROOT / "data/filings/adv/160318.pdf"
CACHE = Path("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/e4102706-b045-419d-94c7-a1402905b586/scratchpad/adv-160318-pages.jsonl")
if CACHE.exists():
    pages = [json.loads(l)["text"] for l in CACHE.open()]
else:
    pages = [p.extract_text() or "" for p in pypdf.PdfReader(str(PDF)).pages]
full = "\n".join(pages)
out = {"_readme": __doc__.strip(), "crd": 160318, "adviser": "TIGER GLOBAL MANAGEMENT, LLC",
       "source": "https://reports.adviserinfo.sec.gov/reports/ADV/160318/PDF/160318.pdf"}
m = re.search(r"(Annual Amendment|Other-Than-Annual Amendment|Initial Application)[^\n]*\n(\d+/\d+/\d{4})", pages[0])
out["filing"] = {"kind": m.group(1), "date": m.group(2)} if m else None
m = re.search(r"F\. Principal Office and Place of Business\s*\n\(1\) Address[^\n]*\n(.*?)If this address is a private residence", full, re.S)
out["principal_office_raw"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
m = re.search(r"Discretionary: \(a\) \$ ([\d,]+) \(d\) (\d+)\s*\nNon-Discretionary: \(b\) \$ ([\d,]+) \(e\) (\d+)\s*\nTotal: \(c\) \$ ([\d,]+) \(f\) (\d+)", full)
out["raum"] = {"discretionary": int(m.group(1).replace(",", "")), "accounts": int(m.group(6)),
               "total": int(m.group(5).replace(",", ""))} if m else None
m = re.search(r"attributable to clients who\s*\nare non- United States persons\?\s*\n\$ ([\d,]+)", full)
out["raum_non_us"] = int(m.group(1).replace(",", "")) if m else None

# other offices (Section 1.F), first reading of each street; each match reads a bounded
# window after its anchor (a full-text re.S scan over the cumulative page text took minutes)
offices, seen_o = [], set()
OFF = re.compile(r"Number and Street 1:\n(.*?)\nNumber and Street 2:\n(.*?)\nCity:\n(.*?)\nState:(.*?)Country:\n?(.*?)\nZIP\+4/Postal Code:\n?(.*?)\n.*?How many employees perform investment advisory functions from this office location\?\s*\n(\d+)", re.S)
for a in re.finditer(r"Number and Street 1:", full):
    mo = OFF.match(full, a.start(), a.start() + 2500)
    if not mo:
        continue
    k = (mo.group(1).strip(), mo.group(3).strip())
    if k in seen_o or not mo.group(3).strip():
        continue
    seen_o.add(k)
    offices.append({"street": (mo.group(1) + " " + mo.group(2)).strip(), "city": mo.group(3).strip(),
                    "state": mo.group(4).strip().strip("\n"), "country": mo.group(5).strip(),
                    "postal": mo.group(6).strip(), "advisory_staff": int(mo.group(7))})
out["other_offices"] = offices

# relying advisers (Schedule R): legal names, first reading each
rel = []
for mo in re.finditer(r"A\.  Your full legal name: \n(.*?)\n", full):
    n = mo.group(1).strip()
    if n and n not in rel and n != "TIGER GLOBAL MANAGEMENT, LLC":
        rel.append(n)
out["relying_advisers_raw"] = rel[:20]

# Schedule A: direct owners and executive officers, read from the last page (the
# cumulative text of the final run carries the whole schedule)
last = pages[-1]
i = last.find("FULL LEGAL NAME (Individuals: Last")
j = last.find("Schedule B", i)
out["schedule_a_raw"] = last[i:j] if i >= 0 else None
sa = []
if i >= 0:
    body = re.sub(r"\s*\n\s*", " ", last[i:j])
    for mo in re.finditer(r"([A-Za-z' .-]+?, [A-Za-z' .,-]+?) (I|DE|FE) (.+?) (\d{2}/\d{4}) (NA|[A-F]) (Y|N) (Y|N) (\d+)", body):
        sa.append({"name": mo.group(1).strip(), "entity": mo.group(2), "title": mo.group(3).strip(),
                   "since": mo.group(4), "ownership_code": mo.group(5), "control": mo.group(6),
                   "crd": mo.group(8)})
out["schedule_a"] = sa

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
               "gav": int(gav.group(1).replace(",", "")),
               "min_investment": int(mininv.group(1).replace(",", "")) if mininv else None,
               "beneficial_owners": int(owners.group(1)) if owners else None,
               "pct_related": int(pct.group(1)) if pct else None,
               "master_fund": feeder.group(1).strip() if feeder and feeder.group(1).strip() else None,
               "page": pi + 1}
        seen[fid.group(1)] = rec
        funds.append(rec)
out["funds_7b1"] = funds
out["funds_7b1_total_gav"] = sum(r["gav"] for r in funds)
(INV / "sources/registers").mkdir(parents=True, exist_ok=True)
(INV / "sources/registers/adv-160318.json").write_text(json.dumps(out, indent=1) + "\n")
print("filing", out["filing"], "| principal", out["principal_office_raw"])
print("raum", out["raum"], "non-US", out["raum_non_us"])
print("offices", out["other_offices"])
print("relying", out["relying_advisers_raw"])
print("schedule A", len(sa))
for r in sa:
    print("  ", r)
print("funds", len(funds), "total GAV", f"{out['funds_7b1_total_gav']:,}")
for r in sorted(funds, key=lambda r: -r["gav"]):
    print(f"  ${r['gav']:>16,} owners={r['beneficial_owners']!s:5} {r['name'][:62]:62} gp={str(r['gp'])[:40]} master={str(r['master_fund'])[:40]}")
