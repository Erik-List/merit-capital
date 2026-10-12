"""Shared by judgments-ab3a/b/c: the market caps read on 2026-10-06 (scratchpad/ab3/caps.json, fx.json), never typed."""
import json
import re
import sys
from pathlib import Path

H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parent.parent))
import judge_lib as jl  # noqa: E402

CAPS = json.loads((H / "caps.json").read_text())
FX = json.loads((H / "fx.json").read_text())
ASOF = "2026-10-06"
MULT = {"trillion": 1e12, "billion": 1e9, "million": 1e6}
SHORT = {"trillion": "T", "billion": "B", "million": "M"}


def usd(slug):
    c = CAPS[slug]
    assert c["asof"] == "October 6, 2026" and c["http"] == "200", (slug, c)
    if slug in FX:
        return FX[slug]["usd"]
    m = re.fullmatch(r"\$([\d.,]+) (trillion|billion|million)", c["cap"])
    assert m, (slug, c["cap"])
    return int(round(float(m.group(1).replace(",", "")) * MULT[m.group(2)]))


def fig(slug):
    """The figure as the note carries it: '$1.78B on 2026-10-06', or the FX helper's own line."""
    if slug in FX:
        return FX[slug]["line"]
    m = re.fullmatch(r"\$([\d.,]+) (trillion|billion|million)", CAPS[slug]["cap"])
    return f"${m.group(1)}{SHORT[m.group(2)]} on {ASOF}"


def band(u):
    return "100b_plus" if u >= 1e11 else "10b_plus" if u >= 1e10 else "1b_plus" if u >= 1e9 else "below_1b"


def P(slug, ticker, tail, **kw):
    """One priced line: the cap, its page, its date and the band it implies, with a one-sentence note."""
    u = usd(slug)
    note = f"A/B {ASOF}: {ticker}, market cap {fig(slug)} (StockAnalysis){tail}"
    assert "—" not in note
    return jl.cls(slug, rng=band(u), usd=u, val_src="web_verified", val_cite=CAPS[slug]["url"], asof=ASOF, note=note, **kw)
