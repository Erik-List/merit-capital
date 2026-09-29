# Batch m06 (PRO-169): grid companies U to Z. Judge: this session, 2026-09-29.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post

J = [
 {"s": "upwind-security", "st": "private", "v": 1.6e9, "va": "2026-03-24", "vc": "https://en.globes.co.il/en/article-salesforce-invests-in-upwind-security-at-16b-valuation-1001538345",
  "es": "Growth", "esc": post("upwind"), "ess": "first_party", "econf": "medium", "ed": "2024-12",
  "hc": "US", "city": "San Francisco", "f": "Security",
  "n": "Cloud runtime security, San Francisco (R&D in Israel). TCV's own post of January 2025 announces its investment, the $100M Series B of December 2024 at $900M (Globes). Mark: Salesforce Ventures' investment at $1.6B (Globes, 2026-03-24), after the $250M Series C at $1.5B of January 2026 (Yahoo Finance); a reported raise at $3.8B (Pulse 2.0, 2026-09) has not closed."},
 {"s": "vectra-ai", "st": "private", "sib": "accel", "city": "San Jose", "f": "Security",
  "es": "Growth", "esc": post("vectra-raises"), "ess": "first_party", "econf": "high", "ed": "2019-06",
  "n": "Network detection and response, San Jose. TCV led the $100M round of June 2019 (the firm's own post), the entry; the Form D band dated the Blackstone-led $130M round of April 2021 at $1.2B, the current mark (aligned with Accel)."},
 {"s": "venafi", "st": "acquired", "es": "Growth", "esc": post("venafi-secures"), "ess": "first_party", "econf": "high", "ed": "2018-12",
  "city": "Salt Lake City", "f": "Security",
  "n": "acq. by CyberArk, 2024, from Thoma Bravo (majority owner since 2020, hence 'Venafi Parent, L.P.' on the compliance list). TCV led the $100M financing of December 2018 (the firm's own post) in a company founded in 2000: Growth."},
 {"s": "wealthsimple", "st": "private", "sib": "greylock", "es": "Growth", "esc": post("wealthsimple-announces"), "ess": "first_party", "econf": "high", "ed": "2020-10",
  "hc": "CA", "hcc": "https://en.wikipedia.org/wiki/Wealthsimple", "city": "Toronto", "f": "Fintech & Payments",
  "n": "Consumer investing and banking, Toronto. TCV led the C$114M round of October 2020 at C$1.4B (the firm's own copy of the release). Mark aligned with Greylock."},
 {"s": "zepz", "st": "private", "sib": "accel", "es": "Growth", "esc": post("worldremit-raises-100m"), "ess": "first_party", "econf": "high", "ed": "2015",
  "hc": "GB", "hcc": "https://en.wikipedia.org/wiki/Zepz", "city": "London", "f": "Fintech & Payments",
  "n": "Cross-border payments (WorldRemit and Sendwave), London. TCV led WorldRemit's $100M round of 2015, the Series B (the firm's own post), after Accel's Series A. Mark aligned with Accel's $5B (August 2021); the $267M raise of October 2024 (World Bank, Accel, TCV) carried no published valuation."},
 {"s": "zillow", "st": "public", "vr": "later", "city": "Seattle", "f": "Consumer & Marketplaces",
  "es": "Growth", "econf": "medium", "ed": "2005",
  "n": "Real estate marketplace, Seattle; listed July 2011. TCV invested in 2005, after Benchmark's first round, and Jay Hoag has been a director since 2005: Growth. The Form D band's 'Seed' and its graduation read a 2011 filing, not the entry. The pre-filled 'acquired' was a Wikidata artefact (Benchmark's row carries the same error, to align). Market cap pinned in the web pass."},
]
