"""Momentum slice (COLLECTION.md s6): one recorded web check per recent hot-sector private row (PRO-104)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, rnd, write, EXPORT  # noqa: E402

D = "2026-09-29"
CHK = {
    "beyond-presence": ("https://www.finsmes.com/2024/10/beyond-presence-raises-3-1m-in-pre-seed-funding.html",
                        "latest round the $3.1M pre-seed of Oct 2024; nothing later"),
    "doorfeed": ("https://www.eu-startups.com/2023/11/paris-based-doorfeed-extends-seed-funding-to-e12-million-to-institutionalize-residential-real-estate-investments/",
                 "latest round the EUR 12M seed extension of Nov 2023; the Dec 2024 Ikory purchase carries no valuation"),
    "igent": ("https://tech.eu/2024/10/30/igent-ai-emerges-from-stealth-with-6-3m-for-engineering-ai/",
              "latest round the GBP 6.3M seed of Oct 2024; nothing later"),
    "impossible-cloud": ("https://games.gg/news/impossible-cloud-raises-34-million/",
                         "the only later raise is the sister entity ICN's, at $470M post-money; no $1B+ mark"),
    "kennek": ("https://www.osborneclarke.com/news/osborne-clarke-advises-albion-capital-kennek-solutions-raises-ps102m-seed-funding",
               "latest round the GBP 10.2M seed of Jan 2024; nothing later"),
    "kipu-quantum": ("https://thequantuminsider.com/2023/12/19/german-quantum-software-company-kipu-quantum-announces-e10-5-million-seed-round/",
                     "latest round the EUR 10.5M seed of Dec 2023; the July 2024 PlanQK purchase carries no valuation"),
    "one-data": ("https://www.finsmes.com/2024/07/one-data-closes-eur-32m-series-b-extension.html",
                 "latest round the EUR 32M Series B extension of July 2024; nothing later"),
    "payrails": ("https://ibsintelligence.com/ibsi-news/payrails-raises-32m-series-a-to-help-global-enterprises-maximise-payment-performance/",
                 "latest round the $32M Series A of June 2025; no valuation published"),
    "qontext": ("https://tech.eu/2026/02/05/qontext-closes-27m-pre-seed-round-to-develop-a-context-layer-for-ai/",
                "latest round the $2.7M pre-seed of Feb 2026"),
    "spread": ("https://tech.eu/2026/04/29/spread-ai-raises-30m-series-b-for-industrial-ai/",
               "latest round the $30M Series B of April 2026; no valuation published"),
    "tzafon": ("https://tech.eu/2025/07/30/tzafon-raises-9-7m-pre-seed-to-scale-ai-compute-and-launch-lightcone/",
               "latest round the $9.7M pre-seed of July 2025; no press source for anything later"),
    "visionai": ("https://tech.eu/2023/10/23/visionai-raises-eur5m-to-help-e-commerce-merchants-take-on-amazon/",
                 "latest round the EUR 5M round of Oct 2023; nothing later"),
    "wasp": ("https://techcrunch.com/2021/10/04/yc-grads-wasp-land-1-5m-seed-to-help-developers-build-web-apps-faster/",
             "latest round the $1.5M seed of Oct 2021; every later hit is a namesake"),
    "super-ai": ("https://nordic9.com/news/super-ai-in-a-12-million-investment-round-backed-by-hv-capital-nfx-mosaic-ventures-and-psl-ventures/",
                 "latest round the $12M raise of June 2021 (HV, NFX, Mosaic, PSL; $21.6M in total); nothing later"),
    "cogny": (EXPORT, "no round, valuation or exit found on the press surfaces or Google News ('\"Cogny\" AI Excel')"),
    "comet": (EXPORT, "no round, valuation or exit found for comet.rocks; the press hits are namesakes"),
    "informed": (EXPORT, "no round, valuation or exit found for informed.so; the press hits are namesakes (Informed.IQ)"),
    "reiner-ai": (EXPORT, "no round, valuation or exit found on the press surfaces or Google News"),
}
L = []
for slug, (cite, finding) in CHK.items():
    L.append(cls(slug, rng="below_1b",
                 extra={"valuation_range_source": "web_verified", "valuation_citation": cite, "valuation_asof": D,
                        "valuation_check": f"momentum slice {D}: {finding}; below_1b stands"}))
# super.AI: the round HV entered, found by the check
L.append(cls("super-ai", rounds=[rnd("2021-06-14", None, 12_000_000, None, True,
                                     "https://nordic9.com/news/super-ai-in-a-12-million-investment-round-backed-by-hv-capital-nfx-mosaic-ventures-and-psl-ventures/")]))
write("momentum-001", L)
