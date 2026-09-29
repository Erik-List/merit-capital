#!/usr/bin/env python3
"""PRO-167 Tiger Global, adversarial A/B pass (COLLECTION.md 7), slice 1, chunk a: the public rows.

Pass A defends each recorded market cap; pass B refreshes it to a September 2026 as-of and looks for a sale,
de-listing or signed deal. Caps come from the StockAnalysis market-cap pages, fetched 2026-09-29 by this pass's own
tool and saved as ab1-mcap.json (Meta and Cerebras cross-checked on companiesmarketcap.com); news from Bing News
(bq.py storage, NQ_TAG=ab1) and WebFetch of the companies' releases. Non-USD caps convert with
scripts/fx-convert.py at the ECB rate of the as-of date.
Rows of the slice whose cap is already dated September 2026 and whose news shows no deal need no line.
Run: NQ_TAG=ab1 python3 ab1a.py"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl
from judge_lib import cls

HERE = Path(__file__).resolve().parent
MCAP = json.loads((HERE / "ab1-mcap.json").read_text())
WV = {"valuation_range_source": "web_verified"}
ASOF = "2026-09-29"


def MC(slug):
    """The market-cap page this pass fetched for the row (ab1-mcap.json), refusing a page with no cap."""
    r = MCAP.get(slug) or {}
    if not r.get("cap") or r.get("asof") != "September 29, 2026":
        raise SystemExit(f"MC({slug!r}): no September 29 cap on disk")
    return r["url"]


L = []

# ---------------------------------------------------------------- 17 Education & Technology (cap added)
L.append(cls("17-education-and-technology", rng="below_1b", usd=38_430_000, val_src="web_verified",
             val_cite=MC("17-education-and-technology"), asof=ASOF, extra=WV,
             note="A/B 2026-09-29: market cap $38.43M on 2026-09-29 (StockAnalysis), below $1B; still listed on "
                  "Nasdaq (YQ), with second-quarter 2026 results out in September 2026 and no sale on record."))

# ---------------------------------------------------------------- Allbirds (business sold: acquired)
L.append(cls("allbirds", status="acquired", rng="below_1b",
             note="A/B 2026-09-29: Allbirds agreed on 2026-03-30 to sell its brand, intellectual property and other "
                  "assets to American Exchange Group, the owner of Aerosoles, for about $39M (Reuters; Pulse 2.0), "
                  "and the sale closed on 2026-06-17 (MSN: 'Allbirds rebrands as Smartbird, completes IP sale to "
                  "American Exchange'), so the footwear business Tiger backed continues under the buyer: acquired, "
                  "below $1B, under the asset-sale rule (COLLECTION.md 6). The emptied listed company renamed itself "
                  "Smartbird, Inc. (Nasdaq: BIRD, about $27M on 2026-09-29) and is a new AI infrastructure business, "
                  "not the company in this row; a reading for Erik to confirm."))

# ---------------------------------------------------------------- Asana (cap refreshed)
L.append(cls("asana", rng="1b_plus", usd=1_920_000_000, val_src="web_verified", val_cite=MC("asana"),
             asof=ASOF, extra=WV,
             note="A/B 2026-09-29: market cap $1.92B on 2026-09-29 (StockAnalysis), replacing the August figure; "
                  "still 1b_plus. No sale of Asana is on record (it bought StackAI in May 2026). The 8VC, a16z and "
                  "Benchmark rows carry older figures ($2.02B to $2.35B, July 2025 to August 2026)."))

# ---------------------------------------------------------------- Blend Labs (cap refreshed, cited)
L.append(cls("blend-labs-inc", rng="below_1b", usd=248_340_000, val_src="web_verified",
             val_cite=MC("blend-labs-inc"), asof=ASOF, extra=WV,
             note="A/B 2026-09-29: market cap $248.34M on 2026-09-29 (StockAnalysis), replacing the uncited 2025 "
                  "float; below $1B, still listed on the NYSE (BLND) and no sale on record. The 8VC, Greylock and "
                  "Lightspeed rows still carry figures from the float of 2025-06-30."))

# ---------------------------------------------------------------- Carma (cap added, AUD converted)
L.append(cls("carma", rng="below_1b", usd=71_712_103, val_src="web_verified", val_cite=MC("carma"),
             asof=ASOF, extra=WV,
             note="A/B 2026-09-29: market cap AUD 102.38M on 2026-09-29 (StockAnalysis, ASX: CMA): AUD 102.4M @ ECB "
                  "2026-09-29 (AUD/EUR 1.6211, EUR/USD 1.1355) = $71.7M, below $1B. The General Catalyst row still "
                  "reads private; Carma has traded on the ASX since 2025-11-05, so this row holds the fresher "
                  "evidence."))

# ---------------------------------------------------------------- Cerebras (cap refreshed)
L.append(cls("cerebras", rng="10b_plus", usd=49_700_000_000, val_src="web_verified", val_cite=MC("cerebras"),
             asof=ASOF, extra=WV,
             note="A/B 2026-09-29: market cap $49.7B on 2026-09-29 (StockAnalysis; companiesmarketcap.com reads "
                  "$49.76B), replacing the first-day figure of May 2026; still 10b_plus."))

# ---------------------------------------------------------------- Facebook / Meta (cap refreshed, cited)
L.append(cls("facebook", rng="100b_plus", usd=1_830_000_000_000, val_src="web_verified", val_cite=MC("facebook"),
             asof=ASOF, extra=WV,
             note="A/B 2026-09-29: Meta Platforms market cap $1.83T on 2026-09-29 (StockAnalysis; "
                  "companiesmarketcap.com reads $1.834T), replacing the uncited 2025 float. The a16z and Accel rows "
                  "($1.46T to $1.47T, August 2026) and the Greylock row (2025-06-30) carry older figures, same "
                  "band."))

# ---------------------------------------------------------------- Dingdong (signed, unclosed sale of the core)
L.append(cls("dingdong-cayman-ltd",
             note="A/B 2026-09-29: on 2026-02-05 Dingdong signed a definitive agreement to sell its whole China "
                  "business (Dingdong Fresh) to a Meituan subsidiary for up to $717M (the company's release); its "
                  "second-quarter release of 2026-08-20 says the sale is still pending anti-monopoly approval from "
                  "SAMR, and the company keeps its overseas business. Signed, not closed, so the row stays public at "
                  "its market cap ($470.83M on 2026-09-29, StockAnalysis); once the sale closes, the business Tiger "
                  "backed passes to Meituan and the row should read acquired."))

# ---------------------------------------------------------------- DoubleVerify (signed take-private)
L.append(cls("doubleverify-holdings-inc",
             note="A/B 2026-09-29: Nielsen agreed on 2026-08-06 to buy DoubleVerify for $13.60 a share in cash, an "
                  "enterprise value of about $2.15B, expected to close by the first quarter of 2027 subject to "
                  "shareholder and regulatory approval (the companies' release). Signed, not closed: the row stays "
                  "public at its market cap ($2.08B on 2026-09-29, StockAnalysis), the same band as the deal "
                  "price."))

if __name__ == "__main__":
    jl.write("ab-1a", L)
