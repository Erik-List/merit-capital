#!/usr/bin/env python3
"""A/B pass (COLLECTION.md 7), slice 3, chunk a: public rows. PRO-167, 2026-09-29.

Market caps read from stockanalysis.com on 2026-09-29 (each page fetched and its
'has a market cap or net worth of ... as of September 29, 2026' sentence read);
non-USD caps converted with scripts/fx-convert.py at the ECB rate of 2026-09-29.
Run: NQ_TAG=ab3 python3 ab3a.py
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls

L = []
WV = {"valuation_range_source": "web_verified"}
ASOF = "2026-09-29"


def SA(path):
    """The stockanalysis.com market-cap page fetched for this pass (scratchpad sa.py)."""
    return "https://stockanalysis.com/" + path.strip("/") + "/market-cap/"


def BURL(slug, title_sub, url_sub):
    """A Bing News item from this pass's cache (news-extra-bing-ab3.json) whose title and
    publisher URL both match; refuses a missing or ambiguous match."""
    d = json.loads((Path(__file__).resolve().parent / "news-extra-bing-ab3.json").read_text())
    m = {i["url"] for i in d.get(slug, [])
         if title_sub.lower() in i["title"].lower() and url_sub in i["url"]}
    if len(m) != 1:
        raise SystemExit(f"BURL({slug!r}, {title_sub!r}, {url_sub!r}) matched {len(m)}")
    return m.pop()


# ---------------------------------------------------------------- samsara
L.append(cls("samsara", rng="10b_plus", usd=21_930_000_000, val_src="web_verified",
             val_cite=SA("stocks/iot"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap $21.93B (stockanalysis.com, 2026-09-29) replaces the SEC "
                  "float of $12.69B (2025-08-01), which is corroboration only; 10b_plus, as the a16z and "
                  "General Catalyst rows read."))

# ---------------------------------------------------------------- sentinelone
L.append(cls("sentinelone", rng="1b_plus", usd=7_960_000_000, val_src="web_verified",
             val_cite=SA("stocks/s"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap $7.96B (stockanalysis.com, 2026-09-29) replaces the SEC "
                  "float of $5.10B (2025-07-31); no pending sale of the company found (Bing News). Insight's "
                  "row reads the same band; Redpoint's row still carries the IL country join."))

# ---------------------------------------------------------------- servicetitan
L.append(cls("servicetitan", rng="1b_plus", usd=6_130_000_000, val_src="web_verified",
             val_cite=SA("stocks/ttan"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap $6.13B (stockanalysis.com, 2026-09-29) replaces the SEC "
                  "float of $6.05B (2025-07-31); the Battery, Coatue and ICONIQ rows read the same band."))

# ---------------------------------------------------------------- shein
L.append(cls("shein", rng="10b_plus", usd=19_004_658_720, val_src="web_verified",
             val_cite=SA("quote/hkg/0625"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: SHEIN Global Holdings trades in Hong Kong (HKEX: 0625) since the "
                  "2026-09-01 listing. Market cap HKD 149.11B @ ECB 2026-09-29 (HKD/EUR 8.9091, EUR/USD 1.1355) "
                  "= $19.00B (stockanalysis.com), replacing the debut-day $24B (Forbes); the shares hit a record "
                  "low on 2026-09-29 after the first results (Bloomberg). Still 10b_plus, 90% above the band edge."))

# ---------------------------------------------------------------- spotify
L.append(cls("spotify", rng="100b_plus", usd=101_380_000_000, val_src="web_verified",
             val_cite=SA("stocks/spot"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap $101.38B (stockanalysis.com, 2026-09-29), within 5% of the "
                  "$100B band edge (1.4% above it; the 2026-09-25 figure was 4.9% above). 100b_plus holds "
                  "today, the band of the Accel, Coatue, Creandum and Thrive rows."))

# ---------------------------------------------------------------- toast
L.append(cls("toast", rng="10b_plus", usd=17_360_000_000, val_src="web_verified",
             val_cite=SA("stocks/tost"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap $17.36B (stockanalysis.com, 2026-09-29) gives the figure a "
                  "dated as-of (companiesmarketcap.com reads $17.37B 'as of September 2026'); GV's row reads "
                  "the same band."))

# ---------------------------------------------------------------- unicommerce
L.append(cls("unicommerce", rng="below_1b", usd=96_577_561, val_src="web_verified",
             val_cite=SA("quote/nse/UNIECOM"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: market cap INR 9.27B @ ECB 2026-09-29 (INR/EUR 108.991, EUR/USD "
                  "1.1355) = $96.6M (stockanalysis.com, NSE: UNIECOM); the below_1b row now carries its figure."))

# ---------------------------------------------------------------- warby-parker-inc
L.append(cls("warby-parker-inc", rng="1b_plus", usd=3_360_000_000, val_src="web_verified",
             val_cite=SA("stocks/wrby"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: Warby Parker (NYSE: WRBY), New York; market cap $3.36B "
                  "(stockanalysis.com, 2026-09-29) replaces the SEC float of $2.17B (2025-06-30). The Felicis, "
                  "First Round, General Catalyst, ICONIQ, Menlo, Spark and Thrive rows read the same band."))

# ---------------------------------------------------------------- weave-communications-inc
WEAVE_REL = BURL("weave-communications-inc", "Weave Announces Acquisition by Francisco Partners", "morningstar.com")
L.append(cls("weave-communications-inc", rng="below_1b", usd=588_790_000, val_src="web_verified",
             val_cite=SA("stocks/weav"), asof=ASOF, extra=WV,
             note="A/B pass 2026-09-29: Francisco Partners signed a definitive agreement on 2026-08-18 to take "
                  "Weave private at $7.40 a share in cash, an equity value of about $650M, expected to close in "
                  f"the fourth quarter of 2026 subject to the stockholder vote ({WEAVE_REL}). Signed, not closed, "
                  "so the row stays public; market cap $588.79M (stockanalysis.com, 2026-09-29) replaces the "
                  "SEC float of $532.1M (2025-06-30). below_1b either way."))

# ---------------------------------------------------------------- zkh-group-ltd (focus left empty by the grind)
L.append(cls("zkh-group-ltd", focus="Consumer & Marketplaces",
             note="Focus filled in the A/B pass (the grind left it empty): a B2B marketplace for industrial "
                  "supplies, read as Consumer & Marketplaces as this book reads Moglix and OfBusiness. Market "
                  "cap $435.44M on 2026-09-29 (stockanalysis.com), below_1b as recorded."))

# ---------------------------------------------------------------- zomato (focus left empty by the grind)
L.append(cls("zomato", focus="Consumer & Marketplaces",
             note="Focus filled in the A/B pass (the grind left it empty): food delivery and quick commerce. "
                  "Market cap unchanged at INR 3.04 trillion on 2026-09-29 (stockanalysis.com)."))

if __name__ == "__main__":
    jl.write("ab-3a", L)
