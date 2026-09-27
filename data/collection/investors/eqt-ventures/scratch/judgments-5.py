"""A/B pass on the visible slice and the momentum slice (COLLECTION.md s6, s7), PRO-163, 2026-09-27.
Pass A = the recorded source still confirms the value; pass B = a Google News search on the name for a
newer round, sale, down round or shutdown (scratch/momentum.py, scratch/news.py). Also the weak-join
corrections found on the way (Paid, Meridian) and Billhop's sale."""
import importlib.util, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from judge_lib import cls, write
ROOT = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("fxc", ROOT / "scripts" / "fx-convert.py"); fxc = importlib.util.module_from_spec(spec); spec.loader.exec_module(fxc)
D = "2026-09-27"
C = json.load(open(Path(__file__).parents[1] / "companies/classification.json"))
PASS_B = "Google News on the name with raise, valuation, unicorn, acquisition and shutdown words"

def add(slug, text):
    n = C[slug]["note"]
    return n if text in n else f"{n} {text}"

L = []
# ---- visible slice ($1B+ or public): both passes, one line each
AB = {
 "beamery": "pass A: the company's Series D release (Dec 2022, $1B) still stands; pass B: no priced round since (2024-2026 headlines are product and partnership news; unleash.ai's 'becomes a talent tech unicorn' is the Dec 2022 article). Stale mark kept.",
 "handshake": "pass A: the $200M Series F release (Jan 2022, $3.5B); pass B: no priced round since (2026 headlines under the name are other Handshakes). Stale mark kept.",
 "netlify": "pass A: the $105M Series D at $2B (Nov 2021); pass B: no round, sale or down round since. Stale mark kept.",
 "nothing": "pass A: the $200M Series C at $1.3B (Sep 2025; Financial Express, ArcticStartup); pass B: only the Dec 2025 community rounds ($5M to $8M, no new price).",
 "parloa": "pass A: TechCrunch 2026-01-15 ($3B); pass B: no round since (Sep 2026 headlines are product events).",
 "standard-ai": "pass A: the firm's post on the 2021 round at $1B; pass B: no round or sale found since. Stale mark kept.",
 "the-exploration-company": "pass A: the July 2026 report of $2B (The Next Web); pass B: the $450M Series C closed 2026-09-08 (TechCrunch, Tech.eu) without a disclosed price (TechCrunch's article states none), so the $2B stays at low confidence.",
 "ineffable-intelligence": "pass A: Bloomberg 2026-04-27 ($1.1B seed at $5.1B); pass B: no round since (Jun 2026 Google Cloud deal, Sep 2026 cofounder hires).",
 "odyssey": "pass A: TechCrunch 2026-06-17 ($310M Series B at $1.45B; Air Street); pass B: no round since (Odyssey-3 launch, Sep 2026).",
 "einride": "pass A: market cap $607.29M on Nasdaq (ENRD) as of 2026-09-25 (StockAnalysis); pass B: listed since 2026-06-10, no sale or delisting.",
}
for s, t in AB.items():
    L.append(cls(s, note=add(s, f"A/B pass {D}: {t}"), clear=("needs_web_value",) if "needs_web_value" in (json.load(open(Path(__file__).parents[1] / 'companies/resolved.json')).get(s, {}).get('flags') or []) else ()))
L.append(cls("starcloud", rng="1b_plus", usd=2300000000, val_src="web_verified",
    val_cite="https://pulse2.com/starcloud-raises-250-million-at-2-3-billion-valuation-to-build-20-gigawatt-orbital-ai-data-center-network/",
    asof="2026-08-21", clear=("needs_web_value",),
    note=add("starcloud", f"A/B pass {D}: pass B found the $250M Series A extension at a $2.3B valuation (2026-08-21; Pulse 2.0, BNN Bloomberg, Data Center Dynamics 2026-08-25), which replaces the $1.1B of March 2026.")))
usd, det = fxc.to_usd(1.6e9, "EUR", "2022-09-19")
L.append(cls("instabee", rng="1b_plus", usd=round(usd), val_src="web_verified",
    val_cite="https://techcrunch.com/2022/09/19/swedish-last-mile-delivery-companies-instabox-and-budbee-to-become-instabee-in-1-7b-merger/",
    asof="2022-09-19", flags=("stale",), clear=("needs_web_value",),
    note=C["instabee"]["note"].replace("the band is pinned in the A/B pass.",
      f"A/B pass {D}: the last priced event is the Sep 2022 combination at EUR 1.6B (the firm's post; TechCrunch 2022-09-19: '$1.7B merger'), {det['note']}; "
      "a holder's write-down of about a quarter (Tech.eu 2023-01-27, Creades) and the unpriced 2024 round do not replace it, so the stale mark stands.")))

# ---- momentum slice: private, hot sector, first seen 2021 or later; one dated web check each
MOM = {
 "argil": ("https://www.eu-startups.com/2024/11/paris-based-argil-raises-e4-9-million-to-develop-ai-video-creation-for-the-creator-economy/", "EUR 4.9M pre-seed and seed, Nov 2024"),
 "depict-ai": ("https://techcrunch.com/2022/02/24/depict-ai-raises-17m-to-give-e-commerce-sites-amazon-level-product-recommendation-muscle/", "$17M Series A, Feb 2022"),
 "dottxt": ("https://www.eu-startups.com/2024/10/paris-based-dottxt-raises-e11-million-to-make-llms-speak-the-language-of-every-application/", "$11.9M pre-seed and seed, Oct 2024"),
 "evroc": ("https://tech.eu/2025/03/20/european-cloud-infrastructure-startup-evroc-raises-largest-tech-series-a-in-the-nordics/", "EUR 50M ($55M) Series A, Mar 2025"),
 "fly-io": ("https://www.finsmes.com/2026/08/fly-io-raises-25m-in-series-d-funding.html", "$25M Series D, Aug 2026 (with a new CEO); the last reported price is $467M at the 2023 Series C"),
 "hume-ai": ("https://www.finsmes.com/2024/03/hume-ai-raises-50m-in-series-b-funding.html", "$50M Series B, Mar 2024; Google DeepMind hired its team under a licence in Jan 2026"),
 "juni": ("https://fintechmagazine.com/articles/juni-secures-us-206mn-funding-for-its-e-commerce-platform", "$206M of equity and debt, Jun 2022; layoffs since"),
 "kaiber": ("https://www.businesswire.com/news/home/20241016279399/en/Kaiber-Launches-Superstudio-a-New-Creative-AI-Platform-for-Seamless-Image-and-Video-Generation", "the seed announced Oct 2024; nothing later"),
 "kota": ("https://tech.eu/2025/05/22/kota-raises-145m-series-a-to-fix-broken-employee-benefits-system/", "the $14.5M Series A led by Eurazeo, May 2025"),
 "moonscale": ("https://stories.eqtventures.com/articles/using-ai-to-close-sales", "the EUR 3.5M seed of Sep 2024; nothing later under either name"),
 "payrails": ("https://tech.eu/2025/06/12/payrails-raises-32m-series-a-to-boost-payment-performance-for-global-enterprises/", "$32M Series A, Jun 2025"),
 "pruna-ai": ("https://www.businessinsider.com/pruna-ai-models-compress-funding-pitch-deck-2024-11", "$6.5M seed, Nov 2024"),
 "sifflet": ("https://www.prnewswire.com/news-releases/sifflet-confirms-momentum-with-18m-in-funding-302486300.html", "$18M, Jun 2025"),
 "talentium": ("https://www.staffingindustry.com/news/global-daily-news/ai-recruitment-platform-talentium-secures-new-funding-round", "a further round, Jan 2025"),
 "timeless": ("https://www.eu-startups.com/2021/11/berlin-based-timeless-secures-e12-million-in-mission-to-democratise-investment-in-luxury-assets/", "the EUR 12M round of Nov 2021; nothing later"),
 "volt": ("https://www.businesswire.com/news/home/20230621292901/en/UK-founded-Fintech-Volt-Raises-%2460m-Series-B-Round-Led-By-Silicon-Valley-investor-IVP", "the $60M Series B led by IVP, Jun 2023; nothing later"),
 "wildhero": ("https://www.fintechfutures.com/bankingtech/uk-challengers-monument-pockit-and-treecard-bank-funding", "new funding reported Apr 2025, after the $23M of Nov 2022"),
 "beside": ("https://fortune.com/2025/11/11/beside-ai-voice-startup-raises-32-million-ai-receptionist-for-small-business/", "$32M, Nov 2025"),
 "clarifeye": ("https://tech.eu/2025/10/01/clarifeye-raises-eur4m-to-transform-expert-knowledge-into-scalable-ai-agents/", "EUR 4M pre-seed, Oct 2025"),
 "infinit": (None, "no funding report at all beyond the fund's 2022 entry"),
 "marvelx": ("https://www.eu-startups.com/2025/05/insurance-services-are-at-a-pivotal-moment-amsterdam-based-marvelx-raises-e5-4-million-for-ai-platform/", "$6M pre-seed, May 2025"),
 "pactio": ("https://fintech.global/2024/04/11/fintech-startup-pactio-raises-14m-from-eqt-ventures-to-enhance-private-capital-workflows/", "$14M Series A, Apr 2024"),
 "stacks": ("https://fintech.global/2026/02/20/stacks-raises-23m-series-a-to-scale-agentic-ai/", "$23M Series A, Feb 2026"),
 "strawberry": ("https://tech.eu/2025/10/14/strawberry-raises-6m-to-make-advanced-ai-automation-intuitive/", "$6M, Oct 2025"),
 "ylookup": ("https://nordic9.com/news/ylookup-closed-a-3-million-pre-seed-round-led-by-eqt-ventures/", "$3M pre-seed, Jan 2026"),
 "bluebook": ("https://tech.eu/2025/02/13/y-combinator-alumni-bluebook-raises-3m-to-build-ai-agents-for-accounting-firms/", "$3M pre-seed, Feb 2025"),
}
for s, (cite, latest) in MOM.items():
    ext = {"valuation_range_source": "web_verified", "valuation_asof": D}
    if cite:
        ext["valuation_citation"] = cite
    L.append(cls(s, note=add(s, f"Momentum-slice check {D} ({PASS_B}): latest round on record {latest}; no priced mark at or above $1B."), extra=ext))

# ---- weak joins: a public float on a private company (another issuer under the same name)
for s, latest, cite in (
  ("paid", "$21M seed led by Lightspeed, Sep 2025 (after the EUR 10M pre-seed)", "https://techcrunch.com/2025/09/28/paid-the-ai-agent-results-based-billing-startup-from-manny-medina-raises-huge-21m-seed/"),
  ("meridian", "the $15M seed of Feb 2025; operating (BPI stablecoin pilot, Jul 2026)", None)):
    ext = {"valuation_usd": None, "valuation_source": None, "valuation_range_source": "web_verified", "valuation_asof": D, "is_public": False}
    if cite:
        ext["valuation_citation"] = cite
    L.append(cls(s, clear=("cik_weak",), note=add(s, f"Weak-join audit {D}: the SEC public float the filings layer joined belongs to another issuer of the same name (cik_weak), so it is cleared. Momentum-slice check {D}: latest round on record {latest}; no priced mark at or above $1B."), extra=ext))

# ---- a sale found by the momentum check
L.append(cls("billhop", status="acquired", note=add("billhop", f"Acquired by Ramp, 2026-03-16 (Finextra; FinTech Global). Momentum-slice check {D}: no priced mark at or above $1B."),
    extra={"valuation_range_source": "web_verified", "valuation_asof": D, "valuation_citation": "https://www.finextra.com/newsarticle/47440/ramp-acquires-billhop-to-expand-across-eu-and-uk"}))
print(len(L), "lines")
write("ab-momentum", L)
