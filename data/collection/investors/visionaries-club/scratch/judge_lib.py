"""Helpers for the Visionaries Club grind (PRO-103): build `run.py record` lines
from the research files in scratch/research/ plus the judge's own decisions.

The research files are evidence, not answers: every value written here is the
judge's call, and a call that departs from the research file says so in the
row's note. Non-USD round amounts convert at the ECB reference rate of the
round's own date (COLLECTION.md s6; scripts/fx-convert.py): a full date uses
that day, a month uses its last day, a bare year is not converted.
"""
import calendar
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "scripts"))
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("fx_convert", ROOT / "scripts" / "fx-convert.py")
fx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fx)

WHO = "agent-judge-pro103"
TODAY = "2026-09-30"


def research(slug: str) -> dict:
    return json.loads((HERE / "research" / f"{slug}.json").read_text())


def fx_date(d: str) -> str | None:
    import re
    d = (d or "").strip()
    if not re.fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", d):
        return None
    if len(d) >= 10:
        return d[:10]
    if len(d) == 7:
        y, m = int(d[:4]), int(d[5:7])
        return f"{d}-{calendar.monthrange(y, m)[1]:02d}"
    return None


def usd(amount, ccy: str, on: str):
    """(usd, detail) or (None, reason)."""
    if amount in (None, "", 0):
        return None, ""
    ccy = (ccy or "USD").upper()
    if ccy == "USD":
        return int(round(float(amount))), ""
    day = fx_date(on)
    if not day:
        return None, f"{ccy} {amount:,.0f} (undated, not converted)"
    v, detail = fx.to_usd(float(amount), ccy, day)
    return int(round(v)), detail


def rounds(slug: str, keep=None) -> list[dict]:
    """The research file's rounds in the COLLECTION.md s6 form."""
    out = []
    for r in research(slug).get("funding_rounds", []):
        if keep and not keep(r):
            continue
        a, _ = usd(r.get("amount"), r.get("currency"), r.get("date"))
        dt = r.get("date") or None
        if dt and not __import__("re").fullmatch(r"\d{4}(-\d{2}(-\d{2})?)?", dt):
            dt = None  # a range or prose date stays in the round text, not the date field
        out.append({"date": dt, "round": r.get("round"),
                    "amount_usd": a, "lead": r.get("lead") or None,
                    "firm_in_round": r.get("firm_in_round"),
                    "source": r.get("source") or None,
                    "source_type": r.get("source_type") or "press"})
    return out


def line(slug: str, **kw) -> dict:
    rec = {"slug": slug, "who": WHO}
    rec.update({k: v for k, v in kw.items() if v is not None or k == "valuation_usd"})
    return rec


def write(path: str, recs: list[dict]) -> None:
    p = HERE / "queue" / path
    p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in recs))
    print(f"wrote {p.relative_to(HERE)}: {len(recs)} lines")
