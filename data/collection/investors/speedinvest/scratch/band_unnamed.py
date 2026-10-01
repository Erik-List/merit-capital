#!/usr/bin/env python3
"""Run-time ruling R1 (decisions.md): a cited, UNNAMED entry round with a stated
amount is banded by the era ceilings of COLLECTION.md s6, exactly as an
electronic Form D round is (which also carries an amount and never a name).

Scope: rows whose stage reads `undetermined`, where the research found the round
Speedinvest first joined on a non-vendor page that names Speedinvest, with a
date and an amount, but no round word. Source `model` (rung 3: a named deal in
the note), the citation kept in the note and in funding_rounds. A Seed band puts
the row in the S2A cohort on an uncited stage, so it carries `stage_uncited` at
low confidence and its graduation is decided on its own evidence (PRO-131 b).
No amount -> the row stays undetermined.

  python3 band_unnamed.py [--dry]
"""
import datetime
import glob
import importlib.util
import json
import re
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H))
import judge_lib as J  # noqa: E402
import convert as C  # noqa: E402

spec = importlib.util.spec_from_file_location("fx", J.ROOT / "scripts" / "fx-convert.py")
fx = importlib.util.module_from_spec(spec)
_argv, sys.argv = sys.argv, sys.argv[:1]
spec.loader.exec_module(fx)
sys.argv = _argv

TODAY = datetime.date(2026, 9, 30)
CEIL = [(2010, 1.5e6, 12e6), (2014, 2.5e6, 15e6), (2018, 4e6, 20e6), (2021, 6e6, 30e6), (9999, 8e6, 40e6)]
MULT = {"k": 1e3, "m": 1e6, "mio": 1e6, "million": 1e6, "bn": 1e9, "b": 1e9}


def parse_amount(s):
    """('EUR', 5300000.0) from 'EUR 5.3M', 'GBP 1.5M', 'USD 3M', 'DKK 20M (~USD 3.2M)', '~NOK 30M', 'about EUR 1M'."""
    m = re.search(r"(EUR|USD|GBP|DKK|NOK|SEK|CHF|PLN|€|\$|£)\s?([\d.,]+)\s?(k|m|mio|million|bn|b)?\b", s or "", re.I)
    if not m:
        return None
    ccy = {"€": "EUR", "$": "USD", "£": "GBP"}.get(m.group(1), m.group(1).upper())
    num = float(m.group(2).replace(",", ""))
    return ccy, num * MULT.get((m.group(3) or "").lower(), 1.0)


def band(usd, year):
    for last, seed, a in CEIL:
        if year <= last:
            if usd < seed / 4:
                return "Pre-Seed"
            if usd <= seed:
                return "Seed"
            if usd <= a:
                return "Series A"
            return "Growth"


def founded_year(slug, r):
    """The company's founding year from the firm's board, the home register, the firm's
    card or the research text; None when the record gives none."""
    for f2 in ("stage2-s2a.json", "stage2-s2b.json"):
        p2 = H / "research" / f2
        if p2.exists():
            v = json.loads(p2.read_text()).get(slug) or {}
            if str(v.get("founded") or "")[:4].isdigit():
                return int(str(v["founded"])[:4]), "second pass: " + str(v.get("founded_source") or "")[:80]
    bo = J.board(slug) or {}
    y = str(bo.get("founded_board") or "")[:4]
    if y.isdigit():
        return int(y), "board"
    rg = J.REG.get(slug) or {}
    if rg.get("status") == "matched" and str(rg.get("founded") or "")[:4].isdigit():
        return int(rg["founded"][:4]), "register"
    card = J.live(slug) or {}
    blob = " ".join([card.get("description") or "", (r.get("identity") or {}).get("what") or "", r.get("notes") or ""])
    m = re.search(r"(?i)\b(?:founded|launched|incorporated|established|spin-?out)\b[^.]{0,40}?\b((?:19|20)\d\d)\b", blob)
    if m:
        return int(m.group(1)), "text"
    return None, None


def main():
    dry = "--dry" in sys.argv
    cls = json.loads((J.INV / "companies/classification.json").read_text())
    cls = cls.get("speedinvest", cls)
    cls = cls.get("rows", cls) if "rows" in cls else cls
    R = {}
    for f in glob.glob(str(H / "research" / "g*.json")):
        if "groups" not in f:
            R.update(json.load(open(f)))
    L, skipped = [], []
    for slug in J.BASE:
        c = cls.get(slug) or {}
        if c.get("entry_stage") != "undetermined" or "identity_unresolved" in (c.get("flags") or []):
            continue
        r = R.get(slug) or {}
        en = r.get("entry") or {}
        cite = en.get("citation")
        if not (en and en.get("date") and C.is_url(cite) and not C.VENDOR.match(cite) and en.get("speedinvest_named")):
            continue
        if C.stage_of(en.get("round")):
            continue
        pa = parse_amount(str(en.get("amount") or ""))
        if not pa:
            skipped.append((slug, "no amount"))
            continue
        d = str(en["date"])
        m = re.match(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", d)
        on = f"{m.group(1)}-{m.group(2) or '06'}-{m.group(3) or '15'}"
        usd = pa[1] if pa[0] == "USD" else fx.to_usd(pa[1], pa[0], on)[0]
        fy, fsrc = founded_year(slug, r)
        if fy is None:
            skipped.append((slug, "no founding year on record; the older-company guard cannot run"))
            continue
        if int(m.group(1)) - fy >= 3:
            skipped.append((slug, f"founded {fy}, entry {m.group(1)}: three or more years old, no early band (PRO-157)"))
            continue
        stage = band(usd, int(m.group(1)))
        edate = m.group(0)
        note = (f"Entry banded (decisions.md R1): Speedinvest's first round is cited but unnamed, {en.get('amount')} "
                f"({d}; about ${usd/1e6:.2f}M), which the s6 era ceilings read as {stage}; company founded {fy} ({fsrc}) ({cite}).")
        rec = {"slug": slug, "who": J.WHO, "entry_stage": stage, "entry_stage_source": "model",
               "entry_stage_confidence": "medium", "entry_date": edate, "note": note}
        if stage == "Seed":
            rec["entry_stage_confidence"] = "low"
            rec["flags"] = ["stage_uncited"]
            g = r.get("graduation") or {}
            later = C.stage_of(g.get("later_round")) if g.get("later_round") else None
            st, st_cite = c.get("status"), c.get("status_citation")
            ld = C.latest_day(edate)
            if later in ("Series A", "Growth") and C.is_url(g.get("citation")) and not C.VENDOR.match(g["citation"]):
                rec.update(seed_to_a_graduation="graduated", graduation_source=C.src_of(g["citation"]),
                           graduation_citation=g["citation"])
            elif st in ("acquired", "defunct") and C.is_url(st_cite) and ld:
                rec.update(seed_to_a_graduation="not_graduated", graduation_source=C.src_of(st_cite),
                           graduation_citation=st_cite, graduation_asof=TODAY.isoformat(),
                           graduation_surfaces=J.surfaces_lines(slug, "no later round found before the sale or shutdown"))
            elif ld and C.months_between(ld, TODAY) < 24:
                rec["seed_to_a_graduation"] = "censored"
            elif ld:
                rec.update(seed_to_a_graduation="not_graduated", graduation_source="absence_check",
                           graduation_asof=TODAY.isoformat(),
                           graduation_surfaces=J.surfaces_lines(slug, "no later round named"))
            if rec.get("seed_to_a_graduation") == "not_graduated" and c.get("hq_country") == "US":
                rec["graduation_surfaces"].append("formd: EDGAR company search for the name -> no Form D sequence after the entry")
        L.append(rec)
    for s in skipped:
        print("SKIP", s)
    from collections import Counter
    print(Counter(x["entry_stage"] for x in L), Counter(x.get("seed_to_a_graduation") for x in L))
    for x in L:
        print(" ", x["slug"], x["entry_stage"], x["entry_date"], x.get("seed_to_a_graduation"))
    J.write("band-unnamed", L, record=not dry)


if __name__ == "__main__":
    main()
