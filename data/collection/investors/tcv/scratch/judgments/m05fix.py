import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post
J = [
 {"s": "razorpay", "hc": "IN", "hcc": post("razorpay-raises"), "cf": [],
  "n": "Payments, Bengaluru. TCV co-led the $375M Series F of December 2021 at $7.5B with Lone Pine and Alkeon (the firm's own post, datelined Bengaluru, which is also the country citation). Mark aligned with Tiger Global."},
 {"s": "strava", "st": "private", "v": 2.2e9, "va": "2025-05", "vn": "Strava Valuation Powers Up To $2.2B",
  "n": "Social fitness app, San Francisco. TCV and Sequoia led the $110M financing of November 2020 (the firm's own post). Mark: $2.2B in the round of May 2025 (Crunchbase News), the figure Sequoia's row carries."},
]
