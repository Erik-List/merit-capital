#!/usr/bin/env python3
"""Hydrate the bulk SEC source material that is deliberately not in git.

Downloads into place:
  data/filings/form-d/                       quarterly Form D bulk ZIPs, 2008q1 -> now
  data/collection/shared/sec/cik-lookup-data.txt

Both are verbatim SEC publications, so the repo tracks neither: a fresh clone
runs this once and ends up byte-identical with what the pipeline scripts
expect. Already-downloaded files are skipped, so re-running is cheap and
picks up only the newest quarter.

data/filings/edgar-headers/ needs no hydration: it is a per-filing cache that
edgar_common.py fills on demand.

Usage: python3 scripts/fetch-filings.py
"""
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paths import ROOT, SEC_CACHE as SEC_DIR  # noqa: E402

FORM_D_DIR = ROOT / "data" / "filings" / "form-d"

# SEC blocks anonymous bulk clients; they ask for a contact in the UA.
UA = "MeritCapital research erik@meritcapit.al"

DERA_BASE = "https://www.sec.gov/files/dera/data/form-d"
CIK_LOOKUP_URL = "https://www.sec.gov/Archives/edgar/cik-lookup-data.txt"


def quarters(start_year: int = 2008):
    # Up to the last *completed* quarter: the SEC publishes a quarter's bulk
    # file only after the quarter ends.
    today = date.today()
    year, q = today.year, (today.month - 1) // 3  # 0 means Q4 of last year
    if q == 0:
        year, q = year - 1, 4
    for y in range(start_year, year + 1):
        for quarter in range(1, 5):
            if (y, quarter) > (year, q):
                return
            yield f"{y}q{quarter}"


def fetch(url: str, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["curl", "-sf", "--max-time", "300", "-H", f"User-Agent: {UA}",
         "-o", str(dest), url],
    )
    if result.returncode != 0 and dest.exists():
        dest.unlink()  # no partial files
    return result.returncode == 0


def main() -> int:
    missing = []

    for quarter in quarters():
        # SEC's own naming is inconsistent: most quarters are <q>_d_0.zip,
        # the earliest are <q>_d.zip. Skip if either variant is on disk.
        names = [f"{quarter}_d_0.zip", f"{quarter}_d.zip"]
        if any((FORM_D_DIR / n).exists() for n in names):
            continue
        for name in names:
            if fetch(f"{DERA_BASE}/{name}", FORM_D_DIR / name):
                print(f"  fetched {name}")
                break
        else:
            missing.append(quarter)
            print(f"  ! no bulk file for {quarter}", file=sys.stderr)

    cik_lookup = SEC_DIR / "cik-lookup-data.txt"
    if not cik_lookup.exists():
        if fetch(CIK_LOOKUP_URL, cik_lookup):
            print("  fetched cik-lookup-data.txt")
        else:
            missing.append("cik-lookup-data.txt")
            print("  ! cik-lookup-data.txt failed", file=sys.stderr)

    if missing:
        # The newest quarter legitimately lags a few weeks after quarter end;
        # anything older failing is worth a look.
        print(f"\n{len(missing)} item(s) not fetched: {', '.join(missing)}",
              file=sys.stderr)
        return 1
    print("\nAll bulk source material present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
