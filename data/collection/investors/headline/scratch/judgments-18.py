"""Momentum slice (COLLECTION.md s6, s7): every private hot-sector row first seen since
2021 got one dated Google News check (scratch/momentum.py, 2026-09-27) for a priced mark
at or above $1B. None found; each check is recorded with the latest round on record as
its citation. Fonoa's HQ is Dublin in the 2026 coverage (and the Coatue row)."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus, post_url  # noqa: E402

ASOF = "2026-09-27"
U = {k: v["url"] for k, v in json.loads((Path(__file__).resolve().parent / "momentum-urls.json").read_text()).items()}
LATEST = {
    "helcim": "C$53M Series C, August 2026, reported at a C$250M valuation",
    "finom": "EUR 115M Series C led by AVP, June 2025, valuation undisclosed",
    "deepip": "$25M Series B, March 2026",
    "didero": "$30M Series A, February 2026",
    "mithrl": "$20M Series A, September 2026",
    "netbox-labs": "$35M Series B, July 2025",
    "payflows": "EUR 25M Series A, April 2024",
    "first-aml": "GBP 15.6M Series B, March 2025",
    "skalar": "EUR 12M pre-seed and seed, July 2026",
    "vox-ai": "$8.7M seed, August 2025",
    "aiprise": "$12.5M Series A, October 2025",
    "defacto": "EUR 16M, September 2025",
    "braavo": "$5M Series B, May 2024",
    "fonoa": "$110M Series C led by Headline, May 2026, valuation undisclosed",
    "replicated": "$50M Series C, 2021 (Business Insider)",
    "adapt": "$10M seed, January 2026",
    "heard": "the round Headline led in June 2023 (the firm's post)",
    "sqldbm": "the 2024 round Headline led (the firm's post)",
    "weavr": "$40M Series A led by Tiger Global, February 2022",
    "plumery": "a $3.3M pre-Series A",
    "pragli-inc": "Gentrace's $8M Series A, December 2024",
    "brite-payments": "$60M Series A, October 2023 (the firm's post)",
    "dbeaver": "$6M seed, April 2023",
    "lucidlink": "$75M Series C including secondaries, November 2023 (the firm's post)",
}
U.update({
    "replicated": "https://www.businessinsider.com/replicated-software-series-c-pitch-deck-blue-owl-2021-7",
    "adapt": "https://adapt.com/blog/pitch-deck",
    "heard": post_url("heard", "Investing in Heard"),
    "sqldbm": post_url("sqldbm", "SqlDBM"),
    "weavr": "https://techfundingnews.com/era-of-plug-and-play-finance-baas-disruptor-weavr-secures-40m-for-international-expansion/",
    "pragli-inc": "https://siliconangle.com/2024/12/10/generative-ai-app-testing-platform-gentrace-raises-8m-make-llm-development-accessible/",
    "brite-payments": post_url("brite-payments", "Investing in Brite"),
    "dbeaver": "https://techcrunch.com/2023/04/11/dbeaver-takes-6m-seed-investment-to-build-on-growing-popularity/",
    "lucidlink": post_url("lucidlink", "LucidLink"),
})
PL = json.loads((Path(__file__).resolve().parent / "research" / "stage-4.json").read_text())
U["plumery"] = [r for r in PL if r["slug"] == "plumery"][0]["rounds"][0]["url"]
L = []
for slug, latest in LATEST.items():
    extra = {"valuation_range_source": "web_verified", "valuation_citation": U[slug], "valuation_asof": ASOF}
    L.append(cls(slug, extra=extra, note=note_plus(slug,
        f"Momentum-slice check {ASOF} (Google News on the name with valuation, valued, unicorn, billion, raises, Series B/C): latest round on record {latest}; no priced mark at or above $1B.")))
for x in L:
    if x["slug"] == "fonoa":
        x.update({"hq_country": "IE", "hq_country_source": "web_verified", "hq_country_citation": U["fonoa"],
                  "hq_city": "Dublin", "hq_city_source": "web_verified"})
if __name__ == "__main__":
    write("momentum-001", L, record="--dry" not in sys.argv)
