#!/usr/bin/env python3
"""UK share-register backtrace: does a fund of the firm appear on a company's
shareholder list? (COLLECTION.md s5 country table, UK: "inside filed documents".)

For each company number: the filing history's confirmation statements (CS01,
"with updates") and annual returns (AR01, pre-2016), newest first; each PDF is
read with pypdf, and a scanned one through the macOS Vision text recognition
(scratch/ocr.swift, compiled once). Lines naming the firm are kept with the
filing's own URL, which is the citation. A PDF that cannot be fetched or read
is recorded as FAILED, never as "not a holder".

Usage: python3 ch-shareholders.py <number> [<number> ...]   (--max N filings per company, default 4;
       --years 2005-2012 reads only lists filed in those years)
Output: ../sources/registers/companies-house/shareholders.json (merged per number)
"""
import json, os, re, subprocess, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import companies_house as ch  # noqa: E402
from pypdf import PdfReader  # noqa: E402
OUT = HERE.parent / "sources" / "registers" / "companies-house" / "shareholders.json"
PDFS = HERE.parent / "sources" / "registers" / "companies-house" / "filings"
TMP = Path(os.environ.get("CH_TMP", "/tmp")) / "ch-ocr"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
FIRM = re.compile(r"(?i)balderton|benchmark (capital )?europe|benchmark capital|gaia investments")
OCR = HERE / "ocr"

def ocr_pdf(pdf: Path) -> str:
    if not OCR.exists():
        subprocess.run(["swiftc", "-O", str(HERE / "ocr.swift"), "-o", str(OCR)], check=True)
    d = TMP / pdf.stem
    d.mkdir(parents=True, exist_ok=True)
    files = []
    for i, p in enumerate(PdfReader(str(pdf)).pages):
        for im in p.images:
            f = d / f"p{i+1:03d}.{im.name.split('.')[-1]}"
            f.write_bytes(im.data)
            files.append(str(f))
            break
    if not files:
        return ""
    r = subprocess.run([str(OCR)] + files, capture_output=True, text=True)
    return r.stdout

def read(pdf: Path) -> tuple[str, str]:
    try:
        txt = "\n".join((p.extract_text() or "") for p in PdfReader(str(pdf)).pages)
    except Exception:
        txt = ""
    if len(txt) > 400:
        return txt, "text"
    return ocr_pdf(pdf), "ocr"

def main():
    args = sys.argv[1:]
    mx = 4
    if "--max" in args:
        i = args.index("--max"); mx = int(args[i + 1]); del args[i:i + 2]
    yrs = None
    if "--years" in args:
        i = args.index("--years"); a, b = args[i + 1].split("-"); yrs = (a, b + "-12-31"); del args[i:i + 2]
    data = json.loads(OUT.read_text()) if OUT.exists() else {"_readme": __doc__.strip().splitlines()[0], "companies": {}}
    PDFS.mkdir(parents=True, exist_ok=True)
    for num in args:
        prof = ch.company(num)
        fl = ch.filings(num)
        cand = [f for f in fl if f["type"] in ("CS01", "AR01", "363a", "363s", "363") and f.get("pdf")
                and "no updates" not in f["description"].lower()
                and (yrs is None or yrs[0] <= f["date"] <= yrs[1])]
        prev = data["companies"].get(num, {})
        rec = {"name": prof.get("name"), "status": prof.get("status"), "dissolved": prof.get("dissolved"),
               "filings_total": len(fl), "lists_read": [], "firm_lines": []}
        for f in cand[:mx]:
            pdf = PDFS / f"{num}-{f['type']}-{f['date']}.pdf"
            if not pdf.exists() or pdf.stat().st_size < 2000:
                r = subprocess.run(["curl", "-sL", "--max-time", "120", "-A", UA, "-o", str(pdf), "-w", "%{http_code}", f["pdf"]],
                                   capture_output=True, text=True)
                time.sleep(1.2)
                if r.stdout.strip() != "200":
                    rec["lists_read"].append({"date": f["date"], "type": f["type"], "url": f["pdf"], "read": "FAILED http " + r.stdout.strip()})
                    continue
            txt, how = read(pdf)
            if len(txt) < 200:
                rec["lists_read"].append({"date": f["date"], "type": f["type"], "url": f["pdf"], "read": "FAILED unreadable"})
                continue
            lines = [l.strip() for l in txt.splitlines()]
            hits = []
            for k, l in enumerate(lines):
                if FIRM.search(l):
                    hits.append(" | ".join(x for x in lines[max(0, k - 2):k + 4] if x))
            rec["lists_read"].append({"date": f["date"], "type": f["type"], "description": f["description"], "url": f["pdf"],
                                      "read": how, "chars": len(txt), "firm_hits": len(hits)})
            for h in hits:
                rec["firm_lines"].append({"filing_date": f["date"], "type": f["type"], "url": f["pdf"], "context": h[:400]})
        seen = {x["url"] for x in rec["lists_read"]}
        rec["lists_read"] += [x for x in prev.get("lists_read", []) if x["url"] not in seen]
        rec["firm_lines"] += [x for x in prev.get("firm_lines", []) if x["url"] not in seen]
        rec["previous_names"] = prof.get("previous_names")
        data["companies"][num] = rec
        print(num, rec["name"], rec["status"], "| lists read:", [(x["date"], x["read"], x.get("firm_hits")) for x in rec["lists_read"]])
        for h in rec["firm_lines"][:6]:
            print("     ", h["filing_date"], h["context"][:260])
        OUT.write_text(json.dumps(data, indent=1) + "\n")

if __name__ == "__main__":
    main()
