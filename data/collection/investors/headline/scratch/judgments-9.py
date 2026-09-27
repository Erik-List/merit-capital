"""Valuation pass: the $1B+ candidates and every public row (COLLECTION.md s6: a public
row's mark is its web-cited market cap, the SEC float corroboration only; a private
row's mark is its last priced primary round with a citable figure, `stale` beyond 24
months; aggregators never mark). Shared companies take the sibling books' cited marks
where those are the freshest (verify rule 10). Caps: StockAnalysis, read 2026-09-27
(last close Friday 2026-09-25)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402

CAP = "2026-09-25"
def v(slug, rng, usd, cite, asof, text, flags=(), status=None, conf="high"):
    return cls(slug, status=status, rng=rng, usd=usd, val_src="web_verified", val_cite=cite, asof=asof,
               val_conf=conf, flags=flags, note=note_plus(slug, text))

L = [
    v("acorns", "1b_plus", 1900000000, "https://techcrunch.com/2022/03/09/acorns-squirrels-away-300m/", "2022-03-09",
      "Mark: $300M Series F led by TPG at $1.9B (March 2022), after the $2.2B SPAC merger was abandoned; no priced round since.", flags=["stale"]),
    v("black-forest-labs", "1b_plus", 3250000000, "https://tech.eu/2025/12/01/black-forest-labs-secures-300m-series-b-at-325b-valuation/", "2025-12-01",
      "Mark: $300M Series B at $3.25B post-money (December 2025), as in the a16z, Creandum and Cherry rows."),
    v("creditas", "1b_plus", 3300000000, "https://www.stblaw.com/about-us/news/view/2025/12/04/creditas-to-receive-$108-million-in-series-g-funding-round-at-$3.3-billion-valuation", "2025-12-01",
      "Mark: $108M Series G led by Andbank at $3.3B (closed December 2025), down from the Series F's $4.5B."),
    v("fetch", "1b_plus", 2500000000, "https://siliconangle.com/2022/04/07/mobile-shopping-rewards-startup-fetch-rewards-raises-240m-2-5b-valuation/", "2022-04-07",
      "Mark: $240M round led by Hamilton Lane with Headline participating, at a valuation 'greater than $2.5 billion' (April 2022); floor figure.", flags=["stale", "valuation_floor"]),
    v("flutterwave", "1b_plus", 3000000000, "https://techcrunch.com/2022/02/16/flutterwave-triples-valuation-to-over-3b-after-250m-series-d/", "2022-02-16",
      "Mark: $250M Series D at over $3B (February 2022), as in the Y Combinator row; floor figure.", flags=["stale", "valuation_floor"]),
    v("fundamental", "1b_plus", 1200000000, "https://www.calcalistech.com/ctechnews/article/hktlfm7vbx", "2026-02-05",
      "Mark: emerged from stealth with $255M ($30M seed plus $225M Series A led by Oak HC/FT) at a $1.2B valuation (February 2026). The Battery row still reads below_1b from before the announcement: cross-investor alignment item."),
    v("gopuff", "1b_plus", 8500000000, "https://www.bloomberg.com/news/articles/2025-11-13/delivery-startup-gopuff-value-drops-to-8-5-billion-in-new-deal", "2025-11",
      "Mark: $250M at $8.5B (November 2025), as in the Accel and Creandum rows."),
    v("icertis", "1b_plus", 2800000000, "https://www.enterprisetimes.co.uk/2021/03/12/icertis-valued-at-2-8-billion-as-it-raises-80-million/", "2021-03-12",
      "Mark: $80M Series F led by B Capital at $2.8B (March 2021); SoftBank's later purchase from Eight Roads near $5B was a secondary (note only); $150M debt in 2022.", flags=["stale"]),
    v("lightricks", "1b_plus", 1800000000, "https://www.businesswire.com/news/home/20210922005119/en/Lightricks-Award-winning-App-Developer-Raises-$130M-Series-D-to-Power-Expansion-and-Champion-Creator-Economy-Users", "2021-09-22",
      "Mark: $130M Series D ($100M primary) co-led by Insight Partners and Hanaco at $1.8B (September 2021).", flags=["stale"]),
    v("mistral", "10b_plus", 24389400000, "https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/", "2026-09-08",
      "Mark: EUR 3B Series D led by Samsung at a post-money of more than EUR 21B (2026-09-08). EUR 21.00B @ ECB 2026-09-08 (EUR/USD 1.1614) = $24.39B; floor figure. The Lightspeed row carries the September 2025 $14B mark (same band).", flags=["valuation_floor"]),
    v("owner", "1b_plus", 2300000000, "https://www.prnewswire.com/news-releases/owner-raises-240m-led-by-goldman-sachs-alternatives-to-build-the-ai-native-platform-for-every-local-business-302862420.html", "2026-08-28",
      "Mark: $240M Series D led by Goldman Sachs Alternatives at $2.3B, Headline participating (2026-08-28). The Redpoint row carries the $1B Series C with a dead citation: cross-investor alignment item."),
    v("raisin", "1b_plus", 1631850000, "https://financefwd.com/de/raisin-secondary/", "2023-03-23",
      "Mark: the EUR 60M Series E (March 2023) at about EUR 1.5B (Finance Forward). EUR 1.50B @ ECB 2023-03-23 (EUR/USD 1.0879) = $1.63B. A December 2024 secondary to Tencent, Hedosophia and Vitruvian implied more than EUR 2B (note only).", flags=["stale"]),
    v("recursive", "1b_plus", 4650000000, "https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding", "2026-05-13",
      "Recursive Superintelligence (Richard Socher, Tim Rocktäschel and others; San Francisco and London). Mark: $650M led by GV and Greycroft at $4.65B (May 2026)."),
    v("sorare", "1b_plus", 4300000000, "https://www.prnewswire.com/news-releases/sorare-raises-680m-series-b-to-create-the-next-sports-entertainment-giant-leveraging-nfts-301380764.html", "2021-09-20",
      "Mark: $680M Series B led by SoftBank at $4.3B (September 2021), as in the Atomico and IVP rows. The Accel row reads below_1b on layoffs (November 2025), which are not the priced collapse evidence s6 requires: cross-investor item for Erik.", flags=["stale"]),
    v("staffbase", "1b_plus", 1100000000, "https://techcrunch.com/2022/03/15/staffbase-raises-115m-at-a-1-1b-valuation-to-help-internal-comms-teams-get-their-message-across/", "2022-03-15",
      "Mark: $115M Series E led by General Atlantic at $1.1B (March 2022).", flags=["stale"]),
    v("swile", "1b_plus", 1000000000, "https://techcrunch.com/2021/10/11/swile-raises-200-million-for-its-employee-benefits-card-and-app/", "2021-10-11",
      "Mark: $200M Series D led by SoftBank, valued at more than $1B (October 2021), Headline investing for the first time; floor figure, no priced round since.", flags=["stale", "valuation_floor"]),
    # public rows: market cap governs
    v("appfolio", "1b_plus", 7230000000, "https://stockanalysis.com/stocks/appf/", CAP, "Market cap $7.23B (Nasdaq APPF)."),
    v("the-realreal", "1b_plus", 1070000000, "https://stockanalysis.com/stocks/real/", CAP, "Market cap $1.07B (Nasdaq REAL), 7% above the $1B edge."),
    v("sonos", "1b_plus", 2150000000, "https://stockanalysis.com/stocks/sono/", CAP,
      "Market cap $2.15B (Nasdaq SONO); the SEC float ($818M, March 2025) had read below_1b.", flags=["model_disputes_source"]),
    v("bumble", "below_1b", 407560000, "https://stockanalysis.com/stocks/bmbl/", CAP, "Market cap $407.6M (Nasdaq BMBL)."),
    v("sonim-technologies", "below_1b", 5830000, "https://stockanalysis.com/stocks/sonm/", CAP, "Market cap $5.8M (Nasdaq SONM)."),
    v("yeahka", "below_1b", 218001342, "https://stockanalysis.com/quote/hkg/9923/", CAP,
      "Market cap HKD 1.71B (HKEX 9923). HKD 1.71B @ ECB 2026-09-25 (HKD/EUR 8.9445, EUR/USD 1.1403) = $218.0M."),
    cls("semrush", status="acquired", rng="below_1b",
        note=note_plus("semrush", "acq. by Adobe, closed 2026-04-28 (Adobe newsroom, https://news.adobe.com/news/2026/04/adobe-completes-semrush-acquisition); IPO'd then acquired reads acquired.")),
    cls("attio", rng="below_1b", note=note_plus("attio", "Band as in the Balderton, Point Nine and Redpoint rows: the $52M Series B (August 2025) disclosed no valuation.")),
]
if __name__ == "__main__":
    write("valuation-001", L, record="--dry" not in sys.argv)
