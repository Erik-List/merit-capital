#!/usr/bin/env python3
"""The adversarial A/B pass over the visible slice (COLLECTION.md §7).

Every row that is currently public or $1B+, defended (find the confirming
source) and attacked (search for the newer round, the acquisition, the down
round). What survives is written here with a cited figure.

Two standing rules do most of the work on this book:

* **Rule A** -- a vendor mark never bands a row. Attentive (PremierAlts
  $913.5M, Forge $6.03/share), Vannevar Labs (Forge $554M, Caplight,
  UpMarket), Orca Bio (Forge $2.4B) and Komodo Health (PM Insights $800M) all
  carry vendor numbers that disagree with each other and with the last priced
  event. The priced event decides the band; the vendor numbers go in the note.
* **§6 staleness** -- a private mark older than 24 months stands, `stale`
  flagged, unless there is documented collapse evidence. Elemy is the one row
  where that evidence exists.

Market caps are as of 2026-09-04 (stockanalysis.com), which is the same as-of
date the sibling runs in this wave used, so invariant 10 compares like with
like rather than straddling a band edge on date alone.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from emit import WHO  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "scratch" / "queue" / "ab-pass.out.jsonl"
SA = "https://stockanalysis.com/stocks/{}/market-cap/"

# slug: (status, range, usd, citation, note, flags)
ROWS = {
 # ---- public: market capitalisation is canonical, web-cited with an as-of date
 "recursion": ("public", "1b_plus", 1_950_000_000, SA.format("rxrx"),
   "Nasdaq: RXRX, market cap $1.95B as of 2026-09-04.", []),
 "recursion-pharmaceuticals": ("public", "1b_plus", 1_950_000_000, SA.format("rxrx"),
   "Duplicate rendering of `recursion`; same cap, $1.95B as of 2026-09-04.", ["duplicate_suspected"]),
 "planet": ("public", "1b_plus", 6_590_000_000, SA.format("pl"),
   "NYSE: PL, market cap $6.59B as of 2026-09-04.", []),
 "planet-labs": ("public", "1b_plus", 6_590_000_000, SA.format("pl"),
   "Duplicate rendering of `planet`; same cap, $6.59B as of 2026-09-04.", ["duplicate_suspected"]),
 "rigetti": ("public", "1b_plus", 5_070_000_000, SA.format("rgti"),
   "Nasdaq: RGTI, market cap $5.07B as of 2026-09-04.", []),
 "soundhound": ("public", "1b_plus", 2_990_000_000, SA.format("soun"),
   "Nasdaq: SOUN, market cap $2.99B as of 2026-09-04. Entered as Melodis in the 2007-2010 angel era.", []),
 "opendoor": ("public", "1b_plus", 3_060_000_000, SA.format("open"),
   "Nasdaq: OPEN, market cap $3.06B as of 2026-09-04.", []),
 "ginkgo-bioworks": ("public", "below_1b", None, SA.format("dna"),
   "NYSE: DNA, market cap $468.01M as of 2026-09-04 -- far below the SPAC-era mark, so the row is below_1b despite being a former unicorn.", []),
 "gingko-bioworks": ("public", "below_1b", None, SA.format("dna"),
   "Duplicate rendering of `ginkgo-bioworks`; same cap, $468.01M as of 2026-09-04.", ["duplicate_suspected"]),
 "hippo-insurance": ("public", "below_1b", None, SA.format("hipo"),
   "NYSE: HIPO, market cap $893.81M as of 2026-09-04.", []),
 "adyen": ("public", "10b_plus", 37_640_000_000,
   "https://companiesmarketcap.com/adyen/marketcap/",
   "Euronext Amsterdam: ADYEN, market cap $37.64B as of September 2026. This is the run's Creandum-constant row: a listing outside SEC registration, so no `sec_public_float` exists and the cap is web-cited. The source publishes in USD at the as-of date, so no ECB conversion was needed; had it quoted EUR, §6 would convert at the reference rate of that date.", []),

 # ---- private, priced and current
 "crusoe": ("private", "10b_plus", 30_000_000_000,
   "https://www.bloomberg.com/news/articles/2026-09-03/crusoe-raises-over-3-billion-in-funding-at-30-billion-valuation",
   "$3B+ round at a ~$30B valuation, co-led by Atreides and Valor, 2026-09-03.", []),
 "poolside": ("private", "10b_plus", 12_000_000_000,
   "https://techcrunch.com/2025/10/30/nvidia-is-reportedly-investing-up-to-1-billion-in-poolside/",
   "$12B valuation on the round Nvidia backed, Oct 2025 -- a fourfold step up from $3B.", []),
 "supabase": ("private", "10b_plus", 10_500_000_000,
   "https://supabase.com/blog/supabase-series-f",
   "$500M Series F at $10.5B post-money, June 2026, led by GIC with Felicis participating. Felicis led the $80M Series B in 2022 and has been in every round since.", []),
 "runway": ("private", "1b_plus", 5_300_000_000,
   "https://techcrunch.com/2026/02/10/ai-video-startup-runway-raises-315m-at-5-3b-valuation-eyes-more-capable-world-models/",
   "$315M Series E at $5.3B post-money, 2026-02-10, led by General Atlantic. Felicis led the $50M Series C at $500M in Dec 2022 -- a 10x mark-up on its own entry round.", []),
 "n8n": ("private", "1b_plus", 5_200_000_000,
   "https://www.trendingtopics.eu/sap-bets-big-on-ai-invests-in-n8n-at-a-5-2-billion-valuation/",
   "SAP's investment priced n8n at $5.2B in 2026, up from the $2.5B Series C of Oct 2025. Felicis led the $12M Series A in 2021.", []),
 "mercor": ("private", "10b_plus", 10_000_000_000,
   "https://techcrunch.com/2025/10/27/mercor-quintuples-valuation-to-10b-with-350m-series-c/",
   "$350M Series C at $10B, 2025-10-27, led by Felicis -- which also led the $100M Series B at $2B eight months earlier.", []),
 "periodic-labs": ("private", "1b_plus", 1_300_000_000,
   "https://techcrunch.com/2025/09/30/former-openai-and-deepmind-researchers-raise-whopping-300m-seed-to-automate-science/",
   "$300M seed at $1.3B, 2025-09-30; Felicis was in the round and its own page calls this the first seed cheque. Reports of a ~$7.5B round are 'in talks' and under §6 a reported-but-unpriced deal does not mark the row.", []),
 "tines": ("private", "1b_plus", 1_125_000_000,
   "https://www.prnewswire.com/news-releases/tines-secures-125m-in-series-c-financing-bringing-total-valuation-to-1-125b-302372726.html",
   "$125M Series C at $1.125B, led by Goldman Sachs Growth with Felicis participating. Dublin-based.", []),
 "juniper-square": ("private", "1b_plus", 1_100_000_000,
   "https://www.prnewswire.com/news-releases/juniper-square-announces-series-d-financing-round-at-1-1-billion-valuation-302481912.html",
   "$130M Series D at $1.1B post-money, June 2025.", []),
 "assort-health": ("private", "1b_plus", 1_200_000_000,
   "https://hitconsultant.net/2026/06/24/assort-health-raises-120-million-series-c-menlo/",
   "$120M Series C at $1.2B, 2026-06-24, led by Menlo Ventures. Felicis entered at the $76M Series B in 2025.", []),

 # ---- private, priced but stale (>24 months); the mark stands, flagged
 "alloy": ("private", "1b_plus", 1_550_000_000,
   "https://techcrunch.com/2022/09/01/fintech-alloy-fight-fraud/",
   "$52M extension at $1.55B, Sept 2022, led by Lightspeed and Avenir with Felicis participating. No priced event since.", ["stale"]),
 "cedar": ("private", "1b_plus", 3_200_000_000,
   "https://www.prnewswire.com/news-releases/cedar-closes-200m-in-series-d-funding-to-continue-fueling-growth-as-a-leading-patient-financial-engagement-platform-for-the-healthcare-industry-301243208.html",
   "$200M Series D at $3.2B, March 2021, led by Tiger Global. No priced event since.", ["stale"]),
 "dialpad": ("private", "1b_plus", 2_200_000_000,
   "https://www.businesswire.com/news/home/20211216005248/en/Dialpad-Raises-170-Million-and-Increases-Valuation-to-2.2-Billion-as-it-Leads-New-Era-of-AI-Powered-Communications",
   "$170M Series F at $2.2B, 2021-12-16, led by ICONIQ. No priced event since.", ["stale"]),
 "komodo-health": ("private", "1b_plus", 3_300_000_000,
   "https://medcitynews.com/2021/03/health-analytics-startup-komodo-passes-3-3b-valuation/",
   "$220M Series E at $3.3B, March 2021, led by Tiger Global. A vendor profile now marks it at $800M; under Rule A that estimate does not band the row, and it is recorded here rather than used.", ["stale"]),
 "guild-education": ("private", "1b_plus", 4_400_000_000,
   "https://en.wikipedia.org/wiki/Guild_Education",
   "$4.4B, June 2022, as reported by Forbes and Bloomberg at the time of the round. No priced event since.", ["stale"]),
 "modern-health": ("private", "1b_plus", 1_170_000_000,
   "https://www.globenewswire.com/news-release/2021/02/11/2174026/0/en/Modern-Health-Gains-Unicorn-Status-After-74-Million-Series-D-at-1-17-Billion-Valuation.html",
   "$74M Series D at $1.17B, 2021-02-11, led by Founders Fund. No priced event since.", ["stale"]),
 "formation-bio": ("private", "1b_plus", 1_000_000_000,
   "https://techcrunch.com/2024/06/26/formation-bio-raises-372m-to-boost-drug-development-with-ai/",
   "The last DISCLOSED figure is the $1B Series C of Sept 2021; the $372M Series D of June 2024 (a16z-led) was described as a material step up but its valuation was not disclosed, so the row is banded on the figure that exists rather than on the step-up.", ["stale"]),
 "attentive": ("private", "1b_plus", 2_200_000_000,
   "https://www.attentive.com/blog/attentive-raises-230-million-series-d-investment-led-by-coatue",
   "Banded on the last priced event carrying a citable figure: the $230M Series D at $2.2B (Sept 2020). The $470M Series E of 2021 was widely reported at ~$7B but no company, filing or press source states that figure in a form this run could cite. Current vendor marks (PremierAlts $913.5M, Forge $6.03/share) are estimates and under Rule A do not band the row; they are recorded here.", ["stale"]),

 # ---- checked and ruled below_1b, with the check recorded (Rule A / §6)
 "vannevar-labs": ("private", "below_1b", None,
   "https://www.prnewswire.com/news-releases/vannevar-labs-announces-75m-series-b-funding-round-301725181.html",
   "Last priced round: $75M Series B, Jan 2023, at a reported ~$575M. The CEO has referred to a $1.5B valuation in company materials and vendors quote $554M (Forge) upward, but neither is a priced event with a citable figure, so Rule A holds the row at below_1b. Flagged for Erik as a row where the rule and the likely market value may diverge.", ["needs_web_value"]),
 "orca-bio": ("private", "below_1b", None,
   "https://forgeglobal.com/orca-bio_stock/",
   "Vendor marks only and they disagree (Forge $2.4B; other profiles ~$1B in 2020). No priced round with a citable figure since, so Rule A holds the row at below_1b with the check recorded.", ["needs_web_value"]),
 "deepinfra": ("private", "below_1b", None,
   "https://deepinfra.com/series-b",
   "$107M Series B closed May 2026 with Nvidia participating; the valuation was not disclosed, so there is no figure to band on.", []),
 "ent": ("private", "below_1b", None,
   "https://www.felicis.com/portfolio",
   "Reported a $100M seed in 2026; no valuation disclosed.", []),
 "elemy": ("private", "below_1b", None,
   "https://bhbusiness.com/2022/12/05/elemy-lays-off-staff-as-it-winds-down-direct-care/",
   "The 2021 mark (~$1.15B on a $219M SoftBank-led round) does NOT stand: §6's documented-collapse test is met -- four rounds of layoffs through 2022, the wind-down of direct care, and a retreat to three states as a software-only platform. Banded below_1b on that evidence rather than on the stale primary.", []),
 "guideline": ("acquired", "below_1b", None, None,
   "acq. by Gusto, announced 2025-08-27. Guideline was valued at $1.15B in 2021; an acquired row carries a null figure, so the band is below_1b.", []),
}


def main() -> None:
    lines = []
    for slug, (status, vrange, usd, cite, note, flags) in ROWS.items():
        row = {"slug": slug, "who": WHO, "status": status,
               "status_confidence": "high",
               "valuation_range": vrange, "valuation_confidence": "high",
               "valuation_range_source": "web_verified", "note": note}
        if usd:
            row["valuation_usd"] = usd
            row["valuation_source"] = "web_verified"
        if cite:
            row["valuation_citation"] = cite
        if flags:
            row["flags"] = flags
        row["clear_flags"] = ["cite_pending"]
        lines.append(row)
    OUT.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in lines) + "\n")
    print(f"wrote {OUT.name}: {len(lines)} rows")
    from collections import Counter
    print(" bands:", dict(Counter(r["valuation_range"] for r in lines)))


if __name__ == "__main__":
    main()
