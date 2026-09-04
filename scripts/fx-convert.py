#!/usr/bin/env python3
"""Convert a non-USD figure to USD at the ECB euro reference rate of a date.

The EU collection rule (COLLECTION.md §6, Creandum decisions.md ruling 5):
every EUR / SEK / DKK / NOK / GBP / CHF figure — a round size, a private
mark, a market cap — converts at the ECB euro reference rate of the figure's
own date, cross-rated through EUR, with the original figure and currency
preserved in the row's note. The ECB publishes one reference rate per
currency per TARGET business day; a weekend or holiday date takes the last
published rate before it (the rate in force), and the note names the date
actually used.

Data: the ECB Data Portal (data-api.ecb.europa.eu, keyless, CC-BY), series
EXR.D.<CCY>.EUR.SP00.A — units of <CCY> per EUR. Cached per currency and
year under data/collection/shared/fx/ so a re-run costs nothing.

Usage:
  python3 scripts/fx-convert.py <amount> <ccy> <YYYY-MM-DD>        # -> USD
  python3 scripts/fx-convert.py 1.0e9 EUR 2025-06-30
  python3 scripts/fx-convert.py 12500000000 SEK 2026-08-29 --json
  python3 scripts/fx-convert.py --rate SEK 2026-08-29             # SEK per USD

Library:
  from fx_convert import to_usd
  usd, detail = to_usd(1.0e9, "EUR", "2025-06-30")
"""
import argparse
import csv
import io
import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "collection" / "shared" / "fx"
API = "https://data-api.ecb.europa.eu/service/data/EXR/D.{ccy}.EUR.SP00.A"
UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
SUPPORTED = ("USD", "EUR", "SEK", "DKK", "NOK", "GBP", "CHF", "PLN", "CZK",
             "HUF", "ISK", "JPY", "CAD", "AUD", "CNY", "INR", "BRL", "ILS",
             "TRY", "KRW", "SGD", "HKD", "MXN", "ZAR", "NZD")


def _fetch_year(ccy: str, year: int) -> dict[str, float]:
    """{YYYY-MM-DD: units of ccy per EUR} for one calendar year, cached."""
    CACHE.mkdir(parents=True, exist_ok=True)
    dest = CACHE / f"ecb-{ccy}-{year}.json"
    if dest.exists():
        return json.loads(dest.read_text())
    url = (API.format(ccy=ccy) + f"?startPeriod={year}-01-01&endPeriod={year}-12-31"
           "&format=csvdata")
    r = subprocess.run(["curl", "-s", "--max-time", "60", "-A", UA, url],
                       capture_output=True, check=False)
    rates: dict[str, float] = {}
    for row in csv.DictReader(io.StringIO(r.stdout.decode("utf-8", "replace"))):
        if row.get("OBS_VALUE"):
            rates[row["TIME_PERIOD"]] = float(row["OBS_VALUE"])
    if not rates:
        raise SystemExit(f"ECB returned no {ccy} rates for {year} ({url})")
    # the current year is still growing: cache it only through the last
    # published day, and refetch if a later date is requested
    dest.write_text(json.dumps(rates, indent=0))
    return rates


def rate_per_eur(ccy: str, on: str) -> tuple[float, str]:
    """(units of ccy per EUR, date of the rate used) — the rate in force on
    `on`: the ECB rate of that day, else the last published rate before it."""
    ccy = ccy.upper()
    if ccy == "EUR":
        return 1.0, on
    if ccy not in SUPPORTED:
        raise SystemExit(f"{ccy}: not an ECB reference currency")
    d = date.fromisoformat(on)
    for back in range(0, 10):
        day = d - timedelta(days=back)
        rates = _fetch_year(ccy, day.year)
        iso = day.isoformat()
        if iso in rates:
            return rates[iso], iso
        if back == 0 and iso > max(rates):
            # date after the last published rate of the year file: refresh
            (CACHE / f"ecb-{ccy}-{day.year}.json").unlink(missing_ok=True)
            rates = _fetch_year(ccy, day.year)
            if iso in rates:
                return rates[iso], iso
    raise SystemExit(f"no ECB {ccy} rate within 10 days before {on}")


def to_usd(amount: float, ccy: str, on: str) -> tuple[float, dict]:
    """USD value of `amount` in `ccy` on `on`, plus the conversion detail
    (rates used, date used) for the row's note."""
    ccy = ccy.upper()
    if ccy == "USD":
        return float(amount), {"ccy": "USD", "amount": amount, "usd": float(amount),
                               "rate_date": on, "basis": "already USD"}
    usd_per_eur, d1 = rate_per_eur("USD", on)
    ccy_per_eur, d2 = rate_per_eur(ccy, on)
    usd = float(amount) / ccy_per_eur * usd_per_eur
    return usd, {"ccy": ccy, "amount": amount, "usd": usd,
                 "usd_per_eur": usd_per_eur, "ccy_per_eur": ccy_per_eur,
                 "rate_date": max(d1, d2),
                 "note": f"{ccy} {_fmt(amount)} @ ECB {max(d1, d2)} "
                         f"({'EUR/USD ' + str(usd_per_eur) if ccy == 'EUR' else f'{ccy}/EUR {ccy_per_eur}, EUR/USD {usd_per_eur}'}) = ${_fmt(usd)}"}


def _fmt(v: float) -> str:
    v = float(v)
    if abs(v) >= 1e9:
        return f"{v / 1e9:.2f}B"
    if abs(v) >= 1e6:
        return f"{v / 1e6:.1f}M"
    return f"{v:,.0f}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("amount", nargs="?", help="figure in the source currency (1.0e9, 12500000000)")
    ap.add_argument("ccy", nargs="?", help="ISO currency code")
    ap.add_argument("on", nargs="?", help="date of the figure, YYYY-MM-DD")
    ap.add_argument("--rate", nargs=2, metavar=("CCY", "DATE"),
                    help="print units of CCY per USD on DATE and exit")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.rate:
        ccy, on = a.rate
        usd_per_eur, d1 = rate_per_eur("USD", on)
        ccy_per_eur, d2 = rate_per_eur(ccy, on)
        print(f"{ccy.upper()} per USD on {max(d1, d2)}: {ccy_per_eur / usd_per_eur:.6f} "
              f"(ECB {ccy.upper()}/EUR {ccy_per_eur}, USD/EUR {usd_per_eur})")
        return
    if not (a.amount and a.ccy and a.on):
        ap.error("amount, ccy and date are required (or --rate CCY DATE)")
    usd, detail = to_usd(float(a.amount), a.ccy, a.on)
    if a.json:
        print(json.dumps(detail, indent=1))
    else:
        print(f"{usd:,.0f}")
        print(detail.get("note") or detail.get("basis"))


if __name__ == "__main__":
    main()
