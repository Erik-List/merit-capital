"""PRO-106 A/B pass and momentum slice (COLLECTION.md s6, s7): every $1B+ or public row pinned to a priced event
or a market cap with its citation, every status change since the judge's knowledge, and one dated web check on
each recent private row in a hot sector (scratch/momentum.json holds the searches)."""
import importlib.util, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", HERE / "judge_lib.py")
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
NEWS = "https://www.balderton.com/news/"
TODAY = "2026-09-26"
L = []
def mark(slug, rng, usd, asof, cite, note, flags=(), clear=("needs_web_value",), conf=None, **kw):
    return cls(slug, rng=rng, usd=usd, val_src="web_verified", asof=asof, val_cite=cite, val_conf=conf, flags=list(flags), clear=list(clear), note=note, **kw)

L.append(mark("aircall", "1b_plus", 1000000000, "2021-06-23", "https://aircall.io/blog/news/series-d-funding/",
    "A/B 2026-09-26: last priced round the $120M Series D of Jun 2021 at a valuation over $1B (the company's own post); no later priced event found; stale", flags=["stale"]))
L.append(mark("merama", "1b_plus", 1000000000, "2025-04-02", "https://www.bloomberg.com/news/articles/2025-04-02/3g-founder-telles-among-investor-in-215-million-investment-round-for-merama",
    "A/B 2026-09-26: the $215M equity-and-debt round of Apr 2025 ($45M equity; Balderton in) valued the company at more than $1B (Bloomberg); recorded at the $1B floor", conf="medium"))
L.append(mark("sophia-genetics", "below_1b", 700000000, TODAY, "https://companiesmarketcap.com/sophia-genetics/marketcap/",
    "A/B 2026-09-26: Nasdaq SOPH, market cap about $0.70B"))
L.append(mark("zopa", "1b_plus", 1000000000, "2024-12", "https://finovate.com/zopa-caps-off-2024-with-87-million-in-funding/",
    "A/B 2026-09-26: the $87M equity round of Dec 2024 led by A.P. Moller Holding, at a valuation above $1B (Finovate); recorded at the $1B floor", conf="medium"))
L.append(mark("workhuman", "1b_plus", 1200000000, "2020-06-22", "https://www.businesswire.com/news/home/20200622005717/en/Workhuman-Announces-New-Strategic-Investor-Continues-Strong-Growth-Trajectory-in-1H-2020",
    "A/B 2026-09-26: Intermediate Capital Group bought a minority stake from existing shareholders in Jun 2020 at a $1.2B valuation (company release), the sale in which the early funds exited; no later priced event found; stale", flags=["stale"]))
L.append(cls("gocardless", status="acquired", rng="below_1b", clear=["needs_web_value"],
    note="A/B 2026-09-26: Mollie completed its acquisition of GoCardless on 2026-09-01, about EUR 1.05-1.1B, over 90% in Mollie shares (Finextra, The Paypers); the Accel and Y Combinator books still read private at $2.1B, the stale side for the wave alignment"))
L.append(cls("contentful", note="A/B 2026-09-26: Salesforce completed the acquisition on 2026-09-01, about $1.5B in cash (Salesforce's 10-Q for the quarter to 2026-07-31 and its release)"))
L.append(cls("prior-labs", status="acquired", note="A/B 2026-09-26: SAP completed the acquisition on 2026-07-17 (SAP News Center)"))
L.append(cls("lyst", note="A/B 2026-09-26: sold to Zozo for $154M, Apr 2025 (TechCrunch 2025-04-09)"))
L.append(cls("housecall-pro", rng="below_1b", clear=["needs_web_value"],
    extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY, "valuation_citation": "https://www.housecallpro.com/resources/news-press/press/housecall-pro-secures-new-funding/"},
    note="A/B 2026-09-26: last round the $125M of Jun 2022 (company release), no price disclosed; the $1.1B figure in circulation is a vendor mark (Forge, PitchBook) and does not band the row (Rule A)"))
L.append(cls("jokr", rng="below_1b", clear=["needs_web_value"],
    extra={"valuation_range_source": "web_verified", "valuation_asof": "2023-09", "valuation_citation": "https://www.pymnts.com/news/investment-tracker/2023/jokr-valued-at-800-million-post-money-in-latest-funding-round/"},
    note="A/B 2026-09-26: the $50M Series D of Sep 2023 priced the company at $800M post-money, down from $1.3B in Feb 2023 and $1.2B in Dec 2021 (PYMNTS; Balderton in the round); documented collapse, below $1B"))
L.append(mark("lendable", "1b_plus", 4608731809, "2022-03-10", NEWS + "lendable-raises-210m-funding-round-to-accelerate-growth/",
    "A/B 2026-09-26: the GBP 210M round of Mar 2022 led by Ontario Teachers' 'values Lendable at GBP 3.5bn' (the firm's post): GBP 3.50B @ ECB 2022-03-10 (GBP/EUR 0.84175, EUR/USD 1.1084) = $4.61B; the $670M of Jul 2026 was asset-backed debt, not equity; stale", flags=["stale"]))
L.append(mark("quantum-systems", "1b_plus", 8000000000, "2026-07-02", "https://quantum-systems.com/news/quantum-systems-raises-1-2bn-series-d-to-accelerate-growth-and-scale-software-defined-autonomous-systems-across-air-land-and-sea/",
    "A/B 2026-09-26: $1.2B Series D signed 2026-07-02 at about $8B post-money (company release; Bloomberg), after the Series C extension of Nov 2025 above EUR 3B"))
L.append(mark("scalable-capital", "1b_plus", 1400000000, "2023-12-07", "https://en.wikipedia.org/wiki/Scalable_Capital",
    "A/B 2026-09-26: the EUR 60M Series E extension Balderton led in Dec 2023 was priced at an unchanged $1.4B (Wikipedia, citing the announcement); the EUR 155M round of Jun 2025 (Sofina, Noteus) disclosed no price; stale", flags=["stale"], conf="medium"))
L.append(mark("thg-the-hut-group", "below_1b", 550000000, TODAY, "https://companiesmarketcap.com/the-hut-group/marketcap/",
    "A/B 2026-09-26: LSE THG, market cap about $0.55B"))
L.append(mark("wayve", "1b_plus", 8600000000, "2026-02-25", NEWS + "wayve-secures-1-5b-to-deploy-its-global-autonomy-platform/",
    "A/B 2026-09-26: $1.2B Series D of Feb 2026 'bringing its post-money valuation to $8.6 billion' (the firm's post)"))
L.append(mark("writer", "1b_plus", 1900000000, "2024-11-12", "https://techcrunch.com/2024/11/12/generative-ai-startup-writer-raises-200m-at-a-1-9b-valuation/",
    "A/B 2026-09-26: $200M Series C of Nov 2024 at a $1.9B valuation (TechCrunch; the firm's post); no later priced event found"))
L.append(cls("dream-games", status="acquired", rng="below_1b", clear=["needs_web_value"],
    note="A/B 2026-09-26: CVC bought the venture investors' stakes in 2025, a majority, at about $5B (CVC release; Bloomberg 2025-05-01); the firm's own post of 2025-10-01 looks back 'following the completion of CVC's acquisition of the VC stakes'; recorded acquired; IVP's book still reads private at $2.75B, the stale side for the wave alignment"))
L.append(mark("zego", "1b_plus", 1100000000, "2021-03-10", "https://www.fintechfutures.com/insurtech/insurtech-zego-lands-150m-series-c-to-join-unicorn-club",
    "A/B 2026-09-26: last priced round the $150M Series C of Mar 2021 at $1.1B (FinTech Futures; the firm's post); no later priced event found; stale", flags=["stale"]))
L.append(mark("vestiaire-collective", "1b_plus", 1195920000, "2024-01-23", "https://www.pymnts.com/news/investment-tracker/2024/vestiaire-collective-targets-1-million-dollars-crowdfunding/",
    "A/B 2026-09-26: the crowdfunding of Jan 2024 was priced at EUR 1.1B, the valuation of the Nov 2023 round (PYMNTS): EUR 1.10B @ ECB 2024-01-23 (EUR/USD 1.0872) = $1.20B; it supersedes the $1.7B of Sep 2021; stale", flags=["stale"]))
L.append(mark("flywire", "1b_plus", 2110000000, TODAY, "https://companiesmarketcap.com/flywire/marketcap/",
    "A/B 2026-09-26: Nasdaq FLYW, market cap about $2.11B (the SEC float of the pre-fill is corroboration only)", clear=[]))
L.append(mark("exein", "1b_plus", 1700000000, "2026-09-15", "https://techcrunch.com/2026/09/15/new-italian-unicorn-exein-rides-the-physical-ai-wave/",
    "Momentum-slice check 2026-09-26: $270M round led by Headline at a $1.7B valuation, 2026-09-15 (TechCrunch), eleven days before the check", clear=[]))
L.append(cls("premialab", country="AE", country_src="web_verified", country_cite="https://www.wamda.com/2025/12/uae-headquartered-premialab-raises-220-million-led-kkr", city="Dubai",
    extra={"hq_city_confidence": "low", "valuation_range_source": "web_verified", "valuation_asof": TODAY,
           "valuation_citation": "https://www.businesswire.com/news/home/20251215372814/en/KKR-and-Premialab-Announce-A-$220m-Strategic-Investment-To-Power-Next-Phase-Of-Global-Growth"},
    note="Momentum-slice check 2026-09-26: KKR led a $220M investment in Dec 2025 with Balderton returning (company and KKR release), no price disclosed; below_1b; the company now describes itself as UAE-headquartered (Wamda), the card's Paris is older"))

# ---- momentum slice: below_1b results, each with its dated check
PRESS = {
 "deepip": ("https://legaltechnology.com/legal-tech-latest-husch-blackwell-rolls-out-legora-big-name-hires-for-harvey-spellbook-partners-with-cba-deepip-raises-25m/", "$25M Series B, Mar 2026"),
 "geordie-ai": ("https://www.uktech.news/ai/geordie-ai-raises-22-3m-for-security-and-governance-platform-for-ai-agents-20260601", "$30M Series A, May 2026"),
 "lawhive": ("https://www.globallegalpost.com/news/uk-new-law-start-up-lawhive-secures-fresh-funding-for-us-expansion-1810357469", "$60M round, Feb 2026"),
 "taktile": ("https://fortune.com/2026/06/24/exclusive-taktile-goldman-sachs-ai-bank-insurance-funding/", "$110M Series C led by Goldman Sachs, Jun 2026 (Balderton in), the founder declining to give the valuation"),
 "huspy": ("https://cairoscene.com/Business/UAE-s-Huspy-Acquires-Integra-Finance-With-86-Million-Italy-Expansion", "$59M Series B, Jul 2025; Integra Finance bought Sep 2026"),
 "lindus-health": ("https://pulse2.com/lindus-health-anti-cro-company-raises-55-million-series-b/", "$55M Series B, Jan 2025"),
 "tinybird": ("https://techcrunch.com/2024/06/17/tinybird-raises-another-30-million-to-transform-data-into-real-time-apis/", "$30M Series B, Jun 2024"),
 "checkly": ("https://tech.eu/2024/08/01/checkly-secures-20m-series-b-for-code-error-detection/", "$20M Series B, Jul 2024"),
 "cino": ("https://techcrunch.com/2025/03/04/cino-has-cracked-bill-splitting-at-the-moment-of-payment-raises-seed/", "EUR 3.5M seed, Mar 2025"),
 "davis": ("https://www.eu-startups.com/2026/05/french-ai-real-estate-startup-davis-raises-e4-6-million-and-unveils-gaudi-1-for-automated-architectural-generation/", "$5.5M pre-seed, May 2026"),
 "reson8": ("https://slator.com/reson8-build-europe-centric-speech-ai-platform/", "EUR 5M pre-seed, Mar 2026"),
 "payflows": ("https://www.eu-startups.com/2024/04/paris-based-payflows-raises-e25-million-series-a-to-build-the-command-centre-for-finance-teams/", "EUR 25M Series A, Apr 2024"),
 "attio": ("https://www.businesspost.ie/tech/irish-tech-startup-inconvo-acquired-by-uk-platform-attio/", "$52M Series B, Aug 2025; Inconvo bought Jul 2026"),
 "grand-games": ("https://www.bloomberg.com/news/articles/2026-05-11/turkey-s-grand-games-raises-70-million-in-funding-round", "$70M Series B, May 2026, the firm describing the valuation as 'closing in on unicorn status'"),
 "lassie": ("https://www.siliconrepublic.com/start-ups/europes-love-for-pets-fuels-swedish-insurtech-lassie-as-it-raises-75m-series-c", "$75M Series C, Feb 2026, no price disclosed"),
 "voize": ("https://www.eu-startups.com/2025/11/berlins-voize-raises-e43-million-to-use-their-ai-companion-to-give-nurses-time-for-what-matters-most-care/", "$50M Series A, Nov 2025"),
 "gitguardian": ("https://blog.gitguardian.com/series-c-pr/", "$50M Series C, Feb 2026"),
 "healx": ("https://techcrunch.com/2024/08/01/healx-an-ai-enabled-drug-discovery-platform-for-rare-diseases-raises-47m/", "$47M Series C, Aug 2024"),
 "coro": ("https://techcrunch.com/2024/03/28/coro-cybersecurity-smb-100m-series-d/", "$100M Series D at a $750M valuation, Mar 2024 (TechCrunch)"),
 "cleo": ("https://www.fintechfutures.com/fintech-innovation/gen-z-financial-assistant-app-cleo-raises-80m-at-500m-valuation", "$80M Series C at a $500M valuation, 2022, the last priced round; the 'unicorn' figures in circulation are vendor estimates and do not band the row (Rule A)"),
 "photoroom": ("https://techcrunch.com/2024/02/27/photoroom-ai-image-editor-raises-43m-at-a-500m-valuation/", "$43M Series B at a $500M valuation, Feb 2024 (TechCrunch)"),
 "conveo": (NEWS + "conveo-raises-50m-to-help-fortune-500-brands-understand-what-consumers-want-next/", "$50M Series A, Sep 2026"),
 "escape": (NEWS + "escape-raises-18m-series-a-to-fight-ai-powered-cyberattacks-with-ai-agents/", "$18M Series A, Mar 2026"),
 "mozart": (NEWS + "mozart-ai-scores-6m-from-balderton-to-put-artists-at-the-centre-of-ai-powered-music-making/", "$6M seed, Feb 2026"),
 "light": (NEWS + "light-raises-30m-series-a-to-replace-legacy-finance-systems-with-ai-native-platform/", "$30M Series A, Sep 2025"),
 "stream": (NEWS + "stream-raises-90m-series-d-to-redefine-workplace-finance-and-drive-global-expansion/", "$90M Series D led by Sofina, Jan 2026, no price disclosed"),
 "grasp": ("https://www.uktech.news/education/grasp-3m-20230731", "GBP 3.1M seed, Jul 2023 (the Oct 2025 'Grasp' Series A is a different, Swedish company)"),
 "sylvera": (NEWS + "sylvera-raises-57-million-series-b-to-incentivise-investment-in-real-climate-impact/", "$57M Series B, Jul 2023"),
 "treasuryspring": (NEWS + "treasuryspring-raises-29-million-to-transform-the-future-of-cash-investment-for-businesses/", "$29M Series B, Jun 2023"),
 "kili-technology": (NEWS + "kili-technology-raises-25m-to-speed-up-ai-adoption/", "$25M Series A, Jul 2021"),
 "levity": (NEWS + "levity-raises-8-3m-to-bring-the-power-of-ai-to-businesses-of-all-sizes/", "$8.3M seed, Oct 2022"),
 "itoflow": (NEWS + "itoflow-raises-2-5-million-to-bring-institutional-grade-portfolio-management-to-every-investor/", "$2.5M pre-seed, Aug 2026"),
 "deepset": ("https://en.wikipedia.org/wiki/Deepset", "$30M Series B, Aug 2023"),
 "supernormal": (NEWS + "supernormal-raises-10-million-to-transform-worker-productivity-and-transparency-with-ai-generated-meeting-notes/", "$10M seed, Jan 2023"),
 "ory": ("https://www.balderton.com/companies/", "the 2021 Series A and a $5M filing of 2024"),
 "testgorilla": (NEWS + "testgorilla-secures-70m-series-a-to-help-companies-eliminate-hiring-bias/", "$70M Series A, Jun 2022"),
 "tibber": (NEWS + "tibber-raises-a-100m-series-c-to-revolutionise-the-energy-industry/", "$100M Series C, Mar 2022"),
 "taptap-send": ("https://www.balderton.com/companies/", "the Series B the card dates to 2025"),
 "finoa": (NEWS + "finoa-announces-15m-in-strategic-funding/", "$15M strategic round, Jan 2024"),
 "request-finance": (NEWS + "request-finance-raises-5-5m-to-simplify-enterprise-crypto-payments/", "$5.5M seed, Jun 2022"),
 "ramp": (NEWS + "ramp-closes-70m-series-b-fundraise/", "$70M Series B, Nov 2022"),
 "primer": (NEWS + "primer-hits-425m-valuation-after-50m-series-b/", "$50M Series B at a $425M valuation, Oct 2021"),
 "violet": ("https://www.balderton.com/companies/", "the 2023 seed"),
}
for s, (cite, latest) in PRESS.items():
    L.append(cls(s, rng="below_1b",
        extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY, "valuation_citation": cite},
        note=f"Momentum-slice check 2026-09-26 (Google News on the name with valuation, raises, unicorn, acquired; the firm's news archive to 2026-09-23): latest round on record {latest}; no priced mark at or above $1B"))
jl.write("batch-ab", L)
