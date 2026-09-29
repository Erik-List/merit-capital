# Web pass 4 (PRO-169): citation debt on the visible slice and three public caps. Judge: this session, 2026-09-29.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post
U = "undetermined"
J = [
 {"s": "exlservice", "st": "public", "v": 5240000000, "va": "2026-09-29", "vc": "https://stockanalysis.com/stocks/exls/market-cap/",
  "es": "Growth", "esc": "https://www.sec.gov/Archives/edgar/data/1297989/000119312505015669/dex1024.htm", "ess": "web_verified", "econf": "high", "ed": "2004-12",
  "cf": ["cite_pending", "stage_uncited"],
  "n": "TCV V and TCV V Member Fund bought shares from the founders Vikram Talwar and Rohit Kapoor under a Supplemental Stockholders Agreement of 2004-12-03 (exhibit 10.24 to the 2005 S-1/A): a secondary purchase, Growth by the policy constant. Market cap $5.24B on 2026-09-29 (StockAnalysis)."},
 {"s": "rent-the-runway", "st": "public", "v": 56400000, "va": "2026-09-29", "vc": "https://stockanalysis.com/stocks/rent/market-cap/",
  "n": "Market cap $56.4M on 2026-09-29 (StockAnalysis), replacing the 2025 float figure."},
 {"s": "oak-pacific-interactive", "st": "public", "v": 10840000, "va": "2026-09-29", "vc": "https://stockanalysis.com/stocks/mtbl/market-cap/",
  "n": "Renren Inc. renamed itself Moatable (NYSE: MTBL); market cap $10.8M on 2026-09-29 (StockAnalysis)."},
 {"s": "anthropic", "es": U, "cf": ["cite_pending", "stage_uncited"],
  "n": "No source names the round TCV entered: Anthropic's own releases of the Series G (February 2026) and Series H (May 2026) and the reports of the 2026 employee tender do not list TCV. The grid carries it from 2026, so every round it could be (Series F or later, or the tender) is Growth-sized, but the round itself is not named: undetermined."},
 {"s": "hinge-health", "es": U, "cf": ["cite_pending", "stage_uncited"],
  "n": "No primary source names the round TCV entered: the October 2021 Series E coverage (Bloomberg, HIT Consultant, pharmaphorum) names Tiger Global and Coatue as leads and not TCV, and the 2025 S-1 does not list TCV among 5% holders. The grid carries it from 2022 with the 'minority' label; the round is not named: undetermined."},
 {"s": "nourish", "es": "Series A", "esc": "https://www.citybiz.co/article/537462/nourish-raises-35m-series-a/", "ess": "web_verified", "econf": "high", "ed": "2024-03",
  "cf": ["cite_pending", "stage_uncited"],
  "n": "Correction: TCV entered at the $35M Series A of March 2024, led by Index Ventures 'with participation from Maverick Ventures, TCV, Y Combinator, Thrive Capital and BoxGroup' (citybiz, 2024-03-28); the compliance list only carried it from 2025. Series A."},
 {"s": "klook", "es": "Growth", "esc": post("klook-gears-up"), "ess": "first_party", "econf": "high", "ed": "2018-08",
  "cf": ["cite_pending", "stage_uncited"],
  "n": "The firm's own copy of Klook's release of 2018-08-07: the $200M Series D, 'Investors in this round include Sequoia China, Matrix Partners, Goldman Sachs, Boyu Capital, TCV', with a quote from TCV's David Yuan. Series D: Growth."},
 {"s": "zillow", "es": "Series A", "esc": "https://www.sec.gov/Archives/edgar/data/1334814/000119312511188823/ds1a.htm", "ess": "web_verified", "econf": "medium", "ed": "2005-11",
  "cf": ["cite_pending", "stage_uncited", "stage_disputes_band"],
  "n": "Real estate marketplace, Seattle; listed July 2011 (Nasdaq: Z), operating and public: the pre-filled 'acquired' was wrong. TCV came in at the $26.0M Series A private placement of November 2005 (the S-1 of 2011: 'In November 2005, we completed a private placement of $26.0 million ... Series A convertible preferred stock'), when Jay Hoag joined the board (October 2005) beside Benchmark's Bill Gurley, matching the firm's own 2005 release (tcv.com/news/zillow.html); TCV V and TCV Member Fund held over 5% at the IPO. Series A. The 2011 Form D ($5.5M) is the concurrent private placement at the listing, not the entry. Market cap $6.2B on 2026-09-29 (StockAnalysis)."},
]
