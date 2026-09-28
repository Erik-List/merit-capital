"""PRO-76, the S2A pass (COLLECTION.md s6, seed_to_a_graduation): every Seed
entry decided. Surfaces: scratch/graduation-surfaces.json (run 2026-09-28, two
passes, every lookup answered), the targeted Google News reads in
scratch/research/gap.json (queries quoted below where the standard query used
the wrong spelling or drowned in namesakes), sibling rows, and the Form D bulk
data for the US companies (scratch/formd-name-scan.py). Graduations cite the
round's own announcement or a headline naming it (the paywall rule); nos cite
a terminal event or carry the full absence test. Also re-records Papaya's
stage at low confidence (a decided no on an uncited seed) and AgentSync's
Series A amount ($25M, not $35M)."""
import importlib.util, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", HERE / "judge_lib.py")
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd = jl.cls, jl.rnd
G = json.loads((HERE / "graduation-surfaces.json").read_text())
ASOF = "2026-09-28"
W = "web_verified"
L = []
FIRM = ("firm: 20vc.fund's portfolio collection (79 cards, read 2026-09-28; name, one-liner, sectors, "
        "exit flag, no round words) and the podcast site's archived portfolio pages (2022-2024) -> the "
        "company listed, no later round named")


def surf(slug, finding, skip=(), extra=()):
    """One line per standard surface from graduation-surfaces.json, then extra lines."""
    out = [FIRM]
    for name, sv in G[slug]["surfaces"].items():
        if name in skip:
            continue
        named = sum(1 for i in sv.get("items", []) if i.get("names"))
        out.append(f"{name}: {sv['query']} -> {sv.get('n', 0)} results, {named} naming the company; {finding}")
    return out + list(extra)


def grad(slug, cite, conf="high", note=None, **kw):
    L.append(cls(slug, grad="graduated", grad_src=W, grad_cite=cite, grad_conf=conf, note=note, **kw))


def no_end(slug, cite, surfaces, note=None, **kw):
    L.append(cls(slug, grad="not_graduated", grad_src=W, grad_cite=cite, grad_conf="medium",
                 grad_asof=ASOF, surfaces=surfaces, note=note, **kw))


def no_abs(slug, surfaces, note=None, **kw):
    L.append(cls(slug, grad="not_graduated", grad_src="absence_check", grad_conf="medium",
                 grad_asof=ASOF, surfaces=surfaces, note=note, **kw))


# ================= graduated: a later round named Series A or later =================
grad("agent-sync", "https://www.bizjournals.com/denver/news/2021/03/08/denver-insurtech-startup-agentsync-series-a.html",
     rounds=[rnd("2020-08", "seed", 4400000, "Elad Gil, Caffeinated Capital", True, "https://techcrunch.com/2020/08/04/agentsync-raises-4-4m-for-its-insurtech-compliance-service/"),
             rnd("2021-03", "Series A", 25000000, "Andreessen Horowitz", None, "https://www.bizjournals.com/denver/news/2021/03/08/denver-insurtech-startup-agentsync-series-a.html"),
             rnd("2021-12", "Series B", 75000000, "Valor Equity Partners", None, "https://www.prnewswire.com/news-releases/agentsync-secures-75m-at-a-1-2b-unicorn-valuation-to-power-growth-across-the-insurance-industry-301439043.html"),
             rnd("2023-10", "Series B extension", 50000000, None, None, "https://techcrunch.com/2023/10/26/agentsync-raises-50m-more-in-a-massive-series-b-extension/")])
grad("junction", "https://hlth.com/insights/news/junction-raises-18m-series-a-funding-to-modernize-healthcare-infrastructure-2025-03-12")
grad("pomelo", "https://latamlist.com/fintech-pomelo-raises-35m-to-expand-its-payments-infrastructure-throughout-latam/")
grad("bridgelinx", "https://www.allenandgledhill.com/perspectives/articles/28132/series-a-financing-of-bridgelinx-logistics-pte-ltd")
grad("deblock", "https://techfundingnews.com/crypto-banking-fintech-deblock-secures-30m-series-a-to-expand-fully-on-chain-banking-across-europe/")
grad("payflows", "https://tech.eu/2024/04/22/saas-payflows-raises-25m-series-a/")
grad("firmable", "https://www.prnewswire.com/news-releases/firmable-raises-14m-series-a-to-take-ai-native-sales-platform-global-302700754.html")
grad("slay", "https://techcrunch.com/2025/09/10/born-maker-of-virtual-pet-pengu-raises-15m-to-launch-a-new-wave-of-social-ai-companions/")
grad("poolside", "https://news.crunchbase.com/ai/coding-startup-poolside-raises-massive-series-b-bain/")
grad("allo", "https://www.hospitalitynet.org/news/4132593/allo-raises-14m-series-a-led-by-zigg-capital-to-scale-the-first-ai-native-operating-system-for-restaurants")
grad("peec-ai", "https://techcrunch.com/2025/11/17/as-consumers-ditch-google-for-chatgpt-peec-ai-raises-21m-to-help-brands-adapt/")

# ================= not graduated: a cited end before any Series A =================
no_end("spiketrap", "https://techcrunch.com/2022/09/01/reddit-acquires-contextualization-company-spiketrap-to-boost-its-ads-business/",
       surf("spiketrap", "the 2020 seed and the Reddit acquisition (2022-09) only, no later round",
            extra=["formd: Form D 2020-Q2 (Spiketrap Inc., San Francisco, $3,655,000 sold, first sale 2020-06-15) -> no later filing as of 2026-09-28",
                   "company: 'Spiketrap raised $3.5 million in a seed round in 2020' (TechCrunch, 2022-09-01, on the Reddit acquisition): the seed was the last round"]))
no_end("shoppinggives", "https://www.prnewswire.com/news-releases/cpgio-expands-market-reach-with-shoppinggives-acquisition-and-strategic-leadership-appointment-302355666.html",
       surf("shoppinggives", "the 2020 seeds (Caffeinated Capital in September, Serena Ventures in December) and the CPGIO acquisition (2025-01) only, no Series A",
            extra=["formd: no Form D filings on record for the company (issuer-name scan of the 2019-2026 bulk data for 'ShoppingGives')"]))
no_end("atlantic-money", "https://finovate.com/deel-acquires-atlantic-money-for-undisclosed-sum/",
       surf("atlantic-money", "the March 2022 seed and the Deel acquisition (2024-12) only, no later round",
            extra=["sibling:ribbit-capital: not graduated, 'the $4.5M seed of March 2022 was the last round; Deel bought the company in December 2024'"]))
no_end("bonnet", "https://company.ovo.com/ovo-announces-acquisition-of-bonnet-to-bring-accessible-public-charging-to-millions-of-customers/",
       surf("bonnet", "the March 2022 seed, a 2023 crowdfunding and the OVO acquisition (2023-11) only, no Series A",
            extra=["sibling:lightspeed: not graduated, cited to OVO's announcement of the acquisition"]))

# ================= not graduated: the absence test =================
no_abs("athenian", surf("athenian", "only namesakes (the Athenian Riviera, schools), no round of the engineering-metrics company after its March 2022 seed",
       extra=["sibling:point-nine: not graduated; the $6M seed of March 2022 was the last round and the company went to the Linux Foundation",
              "googlenews: \"Athenian\" \"Linux Foundation\" acquires OR acquisition -> 0 results"]))
no_abs("courtcorrect", surf("courtcorrect", "the November 2021 seed (GBP 2.2M) only, no later round",
       extra=["googlenews: \"CourtCorrect\" raises OR funding OR investment -> 4 results, 3 read: the 2021 seed (Artificial Lawyer, Business Insider) and a 2020 profile, no later round"]))
no_abs("cryptotax-calculator", surf("cryptotax-calculator", "the March 2022 seed only, no later round",
       extra=["googlenews: \"Crypto Tax Calculator\" OR \"CryptoTaxCalculator\" OR \"Summ\" crypto tax raises -> 40 results, none naming a round after the March 2022 seed ('How Crypto Tax Calculator survived market collapse - twice', Capital Brief, 2025-01-31)"]))
no_abs("ellis", surf("ellis", "namesakes only (Ellis County, Tracee Ellis Ross, Ellis Brooklyn), no round of the immigration company after its April 2022 seed",
       extra=["googlenews: \"Ellis\" immigration startup raises OR \"Series A\" -> 3 results, 2 read: the April 2022 seed (TechCrunch) and a 2025 profile (LA Weekly, 2025-05-22), no later round",
              "formd: Form D 2022-Q2 (Ellis Technologies, Inc., New York, $5,554,988 sold, first sale 2022-04-14) -> no later filing as of 2026-09-28",
              "sibling:first-round-capital and sibling:thrive-capital: a different company of the same name (ruled distinct), not read as this one"]))
no_abs("lottielabs", surf("lottielabs", "no result under the base spelling 'LottieLabs'; the company's spelling was searched below",
       extra=["googlenews: \"Lottielab\" raises OR funding OR \"Series A\" -> 6 results, 3 read: the April 2022 seed ($4M led by Point Nine; Business Insider, EU-Startups, UK Tech Investment News), no later round"]))
no_abs("rollee", surf("rollee", "the April 2022 seed (EUR 4M) only, no later round"))
no_abs("papaya", surf("papaya", "fruit and namesakes only, no round of the delivery-fleet company after its September 2022 first round",
       extra=["googlenews: \"Papaya\" electric delivery fleets raises OR \"Series A\" -> 1 result, not the company"]),
       stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"])
no_abs("noh-payments", surf("noh-payments", "no result under the base name 'Noh Payments'; the company's own name was searched below",
       extra=["googlenews: \"Noh\" fintech casais rodada OR investimento OR \"Series A\" -> 0 results",
              "press: 'uma rodada semente de R$ 17 milhoes captada em 2021 com os fundos Kindred Ventures, Future Positive, Propel e 20VC' (O Globo, 2025-02-21, a profile on its first billion in transactions): the 2021 seed is the round on record"]))
no_abs("omada", surf("omada", "the September 2023 seed only for the sports game; the 2025 investment from GRO and Kirk Kapital is Omada A/S, the Danish identity-governance company, a namesake",
       skip=("techcrunch",)))
no_abs("roam", surf("roam", "namesakes only under 'Roam' (ROAM Africa, ro.am); Roam Research searched below",
       extra=["googlenews: \"Roam Research\" raises OR funding OR crowdfunding -> 8 results, 2 read: the September 2020 seed ($9M at $200M; The Hustle) and a 2021 crowdfunding of more than $1.6M 'from hundreds of individuals' (Business Insider, 2021-04-27), unnamed and under the step-up (2x the seed), no later round",
              "formd: Form D 2020-Q3 (Roam Research, Inc., Oakland, $11,389,216 sold, first sale 2020-08-28) -> no later filing as of 2026-09-28"]),
       city="Oakland", city_src="formd_address", clear=["city_unknown"])

# ================= censored: entry inside the 24-month window, no later named round =================
for s in ["handly", "zekju", "delos", "altertable", "slashwork", "requesty", "trig", "vesence", "superme",
          "bottlecap", "entire", "ami-labs", "denki", "zalos", "lua", "uplane", "xo-market", "corvera",
          "moritz", "archestra-ai", "fonio-ai"]:
    L.append(cls(s, grad="censored"))

if __name__ == "__main__":
    jl.write("batch-s2a", L)
