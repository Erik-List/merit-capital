"""Erik's ruling on R2 (2026-09-27, with the ingest approval): Docly is not a member. Its shares
reached the fund only through Min Doktor's demerger, the same class as stock received when a
company buys a portfolio company (the sale-consideration ruling, 2026-09-22)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from judge_lib import verdict, write
L = [verdict("docly", "not_member",
    "Docly's shares reached EQT Ventures I only because Min Doktor, a Fund I company, split Docly off in Aug 2018; "
    "the fund never bought into a Docly round ('EQT Ventures declined to make a follow-up investment in Docly', Sifted). "
    "Stock received through a portfolio company's corporate event is not membership (Erik 2026-09-27 on decisions.md R2, "
    "the same class as the 2026-09-22 sale-consideration ruling); the investment is Min Doktor, which keeps its row.",
    ec="site_listing", conf="high", cite="https://sifted.eu/articles/min-doktor-startup-failure")]
write("docly-ruling", L)
