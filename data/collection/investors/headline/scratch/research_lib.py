"""Turn the research agents' rows (scratch/research/stage-N.json) into the §6
funding_rounds form. Non-USD amounts convert at the ECB reference rate of the round's
date (scripts/fx-convert.py, COLLECTION.md s6); a currency or date the ECB series does
not cover leaves amount_usd null and the native figure in the note."""
import json, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
ECB = {"EUR", "GBP", "SEK", "DKK", "NOK", "CHF", "JPY", "BRL", "PLN", "CZK", "HUF", "AUD", "CAD", "HKD", "CNY", "ILS", "INR", "SGD", "NZD"}


def research(n):
    return {r["slug"]: r for r in json.loads((HERE / "research" / f"stage-{n}.json").read_text())}


def usd(amount, ccy, date):
    if amount in (None, ""):
        return None
    ccy = (ccy or "USD").upper()
    if ccy == "USD":
        return int(amount)
    if ccy not in ECB or not date or date[:4] < "1999":
        return None
    d = date if len(date) == 10 else (date + "-15" if len(date) == 7 else date + "-06-30")
    r = subprocess.run(["python3", "scripts/fx-convert.py", str(int(amount)), ccy, d, "--json"],
                       cwd=ROOT, capture_output=True, text=True)
    try:
        return int(round(json.loads(r.stdout)["usd"]))
    except Exception:
        m = re.search(r"^([\d,]+)", r.stdout.strip())
        return int(m.group(1).replace(",", "")) if m else None


def rounds_of(row):
    out = []
    for x in row.get("rounds") or []:
        st = x.get("source_type") or "press"
        if st not in ("firm", "company", "press", "filing", "vendor"):
            st = "press"
        out.append({"date": x.get("date"), "round": x.get("round"),
                    "amount_usd": usd(x.get("amount"), x.get("currency"), x.get("date") or ""),
                    "lead": x.get("lead"), "firm_in_round": x.get("firm_in_round"),
                    "source": x.get("url"), "source_type": st})
    return out
