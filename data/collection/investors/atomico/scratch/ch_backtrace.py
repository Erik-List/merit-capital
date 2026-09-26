#!/usr/bin/env python3
"""Companies House backtrace: does the register name the firm's funds as holders?

The register's backtrace (COLLECTION.md §5 country table, UK row: "inside
filed documents, not the API"). For one UK company:

  1. the company profile: status (Active / Dissolved / Liquidation /
     In Administration ...), incorporation and dissolution dates, previous
     names — `status` evidence for every UK row;
  2. the shareholder statements, oldest first: annual returns "with full list
     of shareholders" (to 2016) and confirmation statements "with updates"
     (2016 on). Each is read for the firm's vehicle names (config
     registers.uk.holder_pattern); a text PDF is read directly, a scanned one
     through macOS Vision OCR (scratch/pdf-ocr.swift, compiled on first use).
     The first statement naming a firm vehicle bounds the entry from above,
     the statement before it (naming none) bounds it from below;
  3. the share-capital filings (SH01 allotments, SH08/SH10 class changes)
     inside that window: the allotment dates and the class names they carry
     ("SERIES A PREFERRED", "B PREFERRED ORDINARY") are the round's dating
     and, where a class names a round, a candidate round word — a new layer,
     scored before it may label (COLLECTION.md §5, "measure it before you
     trust it"). An SH01 never names the allottee.

Cost is recorded per company (requests, documents, OCR pages) so the report
can state the layer's cost per row.

Usage: python3 ch_backtrace.py <investor-slug> <company-number> [...]
       python3 ch_backtrace.py <investor-slug> --from <json list of {slug, number}>
Writes: sources/registers/companies-house/backtrace.json (merged per number)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "scripts"))
import companies_house as ch  # noqa: E402
from paths import Paths, write_atomic  # noqa: E402

DOCS = ch.CACHE.parent / "docs"
OCR_BIN = ch.CACHE.parent / "pdf-ocr"


def ocr_bin() -> Path:
    if not OCR_BIN.exists():
        subprocess.run(["swiftc", "-O", str(HERE / "pdf-ocr.swift"), "-o", str(OCR_BIN)],
                       check=True, capture_output=True)
    return OCR_BIN


def doc_text(url: str, key: str, stats: dict) -> tuple[str, str]:
    """(text, how) for one filed document; cached as .pdf and .txt."""
    DOCS.mkdir(parents=True, exist_ok=True)
    pdf, txt = DOCS / f"{key}.pdf", DOCS / f"{key}.txt"
    if txt.exists():
        t = txt.read_text()
        return t, t[:4] == "OCR\n" and "ocr" or "text"
    if not pdf.exists():
        time.sleep(ch.PACE)
        r = subprocess.run(["curl", "-sSL", "--max-time", "120", "-A", ch.UA, "-o", str(pdf), url],
                           capture_output=True)
        stats["requests"] += 1
        if r.returncode != 0 or not pdf.exists() or pdf.read_bytes()[:4] != b"%PDF":
            pdf.unlink(missing_ok=True)
            raise ch.Unavailable(f"document {url[:80]}: rc={r.returncode}")
    stats["documents"] += 1
    import pypdf
    try:
        rd = pypdf.PdfReader(str(pdf))
        t = "\n".join((p.extract_text() or "") for p in rd.pages)
        pages = len(rd.pages)
    except Exception:  # noqa: BLE001 — a damaged PDF falls through to OCR
        t, pages = "", 0
    how = "text"
    if len(t.strip()) < 200:
        r = subprocess.run([str(ocr_bin()), str(pdf)], capture_output=True, timeout=600)
        t = "OCR\n" + r.stdout.decode("utf-8", errors="replace")
        stats["ocr_pages"] += pages
        how = "ocr"
    txt.write_text(t)
    return t, how


def holder_lines(text: str, rx: re.Pattern) -> list[str]:
    lines = [ln.strip() for ln in text.splitlines()]
    out = []
    for i, ln in enumerate(lines):
        if rx.search(ln):
            ctx = " | ".join(x for x in lines[max(0, i - 2): i + 3] if x)
            out.append(ctx[:300])
    return out


def backtrace(number: str, rx: re.Pattern, max_docs: int = 6, since: str = "") -> dict:
    stats = {"requests": 0, "documents": 0, "ocr_pages": 0}
    t0 = time.time()
    prof = ch.company(number)
    stats["requests"] += 1
    # The website ignores the category filter on a plain GET, so the whole
    # history is read once (25 rows a page) and split here.
    try:
        history = ch.filings(number, pages=20)
    except ch.Unavailable:
        history = []
    stats["requests"] += max(1, (len(history) + 24) // 25)
    stmts = []
    for f in history:
        if f["type"] in ("AR01", "CS01", "363a", "363s", "RP04CS01", "RP04AR01"):
            d = f["description"].lower()
            full = ("full list of shareholders" in d or "with updates" in d
                    or f["type"] in ("363a", "363s"))
            stmts.append({**f, "full_list": full})
    stmts.sort(key=lambda f: f["date"])
    # Read the statements that carry a holder list, oldest first; stop once a
    # firm vehicle has been seen twice (entry bracketed and still holding).
    read, first_hit, last_miss = [], None, None
    cands = [s for s in stmts if s["full_list"] and s["pdf"]]
    if since:
        # Start one statement before the year the firm's own record gives for
        # its entry (the site's investment year, or the first seat), so the
        # document budget is spent where the entry is, not on the company's
        # pre-history (Pharmacy2U's statements run from 2005).
        idx = next((i for i, c in enumerate(cands) if c["date"][:4] >= since[:4]), len(cands))
        cands = cands[max(0, idx - 1):]
    for f in cands[:max_docs * 3]:
        if len(read) >= max_docs:
            break
        key = f"{number}-{f['type']}-{f['date']}"
        try:
            text, how = doc_text(f["pdf"], key, stats)
        except ch.Unavailable as e:
            read.append({"date": f["date"], "type": f["type"], "error": str(e)[:120]})
            continue
        hits = holder_lines(text, rx)
        # How many holdings the statement lists: an annual return carried the
        # FULL list only every third year (changes otherwise), and a statement
        # listing a handful of holders says nothing about an absent one. Only
        # a statement with a real list bounds the entry from below.
        n_holders = len(re.findall(r"(?i)shareholding\s*\d+", text))
        read.append({"date": f["date"], "type": f["type"], "description": f["description"],
                     "pdf": f["pdf"], "how": how, "holders_listed": n_holders,
                     "firm_holders": hits[:8]})
        if hits and not first_hit:
            first_hit = f["date"]
        elif not hits and not first_hit and n_holders >= 5:
            last_miss = f["date"]
        if first_hit and len([r for r in read if r.get("firm_holders")]) >= 2:
            break
    capital = [{"date": f["date"], "type": f["type"], "description": f["description"],
                "pdf": f["pdf"]} for f in history
               if f["type"] in ("SH01", "88(2)", "88(2)R", "SH02", "SH08", "SH10", "SH19",
                                "RES01", "RESOLUTIONS", "MEM/ARTS", "123", "122")]
    stats["seconds"] = round(time.time() - t0, 1)
    return {"number": number, "profile": prof, "statements_read": read,
            "first_named": first_hit, "last_not_named": last_miss,
            "capital_filings": capital, "cost": stats,
            "checked": time.strftime("%Y-%m-%d")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("investor")
    ap.add_argument("numbers", nargs="*")
    ap.add_argument("--from", dest="src")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    p = Paths(args.investor)
    cfg = p.config().get("registers", {}).get("uk", {})
    rx = re.compile(cfg.get("holder_pattern") or r"(?i)\batomico\b")
    out = p.sources / "registers" / "companies-house" / "backtrace.json"
    data = json.loads(out.read_text()) if out.exists() else {"companies": {}}
    targets = [{"number": n, "slug": ""} for n in args.numbers]
    if args.src:
        targets += json.loads(Path(args.src).read_text())
    for t in targets:
        n = t["number"]
        if n in data["companies"] and not args.refresh:
            continue
        try:
            rec = backtrace(n, rx, since=str(t.get("since") or ""))
        except ch.Unavailable as e:
            rec = {"number": n, "error": str(e)[:200], "checked": time.strftime("%Y-%m-%d")}
        rec["slug"] = t.get("slug") or rec.get("slug", "")
        data["companies"][n] = rec
        write_atomic(out, json.dumps({
            "_readme": ("Companies House backtrace (scratch/ch_backtrace.py): per UK company the "
                        "register profile (status), the shareholder statements read for the firm's "
                        "vehicle names (text or Vision OCR), the entry bracket they give "
                        "(last_not_named < entry <= first_named), and the share-capital filings for "
                        "round dating. Per-company cost recorded."),
            "holder_pattern": rx.pattern, **data}, indent=1, ensure_ascii=False) + "\n")
        prof = rec.get("profile", {})
        print(f"{n} {prof.get('name', '')[:40]:40} {prof.get('status', rec.get('error', ''))[:14]:14} "
              f"named {rec.get('first_named')} (after {rec.get('last_not_named')}) "
              f"cost {rec.get('cost')}", flush=True)


if __name__ == "__main__":
    main()
