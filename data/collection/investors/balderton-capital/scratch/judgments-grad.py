"""PRO-106 graduation pass (COLLECTION.md s6, PRO-132): every Seed entry decided. Post URLs are read from
evidence-pack.json by key and press URLs from the decoded surfaces, never typed (run-log, citation audit)."""
import importlib.util, json
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("jl", HERE / "judge_lib.py")
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
pack = json.loads((HERE / "evidence-pack.json").read_text())
G = json.loads((HERE / "graduation-surfaces.json").read_text())
TODAY = "2026-09-26"
def post(slug, frag):
    hits = [p["url"] for p in pack[slug]["posts"] if frag in p["url"]]
    assert len(hits) == 1, (slug, frag, hits)
    return hits[0]
L = []
def grad(slug, cite, note, src="first_party", **kw):
    L.append(cls(slug, grad="graduated", grad_src=src, grad_cite=cite, grad_conf="high", note=note, **kw))

grad("01health", "https://pulse2.com/01health-raises-15-million-series-a-to-expand-specialist-healthcare-platform-across-the-uk-and-us/",
     "Graduated: $15M Series A, Jun 2026 (Pulse 2.0; UKTN; Tech.eu)", src="web_verified")
grad("agave-games", post("agave-games", "series-a"), "Graduated: $18M Series A, Dec 2024 (the firm's post)")
grad("arive", post("arive", "series-a"), "Graduated: $20M Series A, Jan 2022 (the firm's post; TechCrunch)")
grad("attio", post("attio", "series-a"), "Graduated: $23.5M Series A, Mar 2023 (the firm's post)")
grad("carwow", "https://techcrunch.com/2014/12/14/carwow-fuel-injection/", "Graduated: GBP 4.6M Series A, Dec 2014 (TechCrunch)", src="web_verified")
grad("contentful", post("contentful", "raises-28m"), "Graduated: the $28M Series C of Dec 2017 is the earliest later round the firm's archive names (the Series A and B preceded it)")
grad("depop", post("depop", "raises-20m"), "Graduated: $20M Series B, Jan 2018 (the firm's post), after the $8M round of Jan 2015")
grad("dream-games", post("dream-games", "series-a"), "Graduated: $50M Series A, Mar 2021 (the firm's post)")
grad("fuse-energy", post("fuse-energy", "5bn"), "Graduated: the round of Dec 2025 at a $5B valuation (the firm's post)")
grad("mytomorrows", post("mytomorrows", "10m"), "Graduated: EUR 10M round of Jan 2017 (the firm's post; TechCrunch), unnamed and above the $5M bar for a 2014 seed")
grad("ory", "https://www.prnewswire.com/news-releases/cloud-security-provider-ory-corp-raises-22-million-in-series-a-round-led-by-insight-partners-301446521.html",
     "Graduated: $22M Series A led by Insight Partners, Dec 2021 (company release)", src="web_verified")
grad("primer", post("primer", "series-a"), "Graduated: GBP 14M Series A, Nov 2020 (the firm's post); $100M Series C May 2026 led by Sofina, no price disclosed (company release), so the band stays below_1b",
     extra={"valuation_range_source": "web_verified", "valuation_asof": TODAY,
            "valuation_citation": "https://www.businesswire.com/news/home/20260519989278/en/Primer-Raises-$100M-Series-C-to-Bring-AI-to-Every-Payment-and-Accelerate-US-Expansion"})
grad("revolut", post("revolut", "7-75m"), "Graduated: the Series A of Jul 2016 Balderton led (the firm's post)")
grad("sava", post("sava", "series-a"), "Graduated: $19M Series A, Jul 2025 (the firm's post)")
grad("sketchfab", post("sketchfab", "raise-7m"), "Graduated: $7M Series A, Jun 2015 (Form D 2015-Q2; the firm's post of 2016-06-16); the seed Balderton led was Dec 2013 (Wikipedia; Form D 2013-Q4 $1.9M)",
     entry_date="2013-12")
grad("tictail", post("tictail", "series-a"), "Graduated: $8M Series A led by Thrive, Feb 2014 (the firm's post)")
grad("trawa", post("trawa", "24m"), "Graduated: EUR 24M Series A, May 2025 (the firm's post)")

for s, d in [("cino", "2025-03-04"), ("mozart", "2026-02-11")]:
    L.append(cls(s, grad="censored", entry_date=d, note=f"Censored: the seed of {d} is under 24 months old on {TODAY}"))

FIRM = "firm: balderton.com/companies card and the news archive (552 posts to 2026-09-23) for the name"
def lines(slug, firm, gn, tc, cb, local=None, formd=None, company=None):
    s = G[slug]["surfaces"]
    out = [f"{FIRM} -> {firm}",
           f"googlenews: {s['googlenews']['query']} -> {s['googlenews']['n']} results, {gn}",
           f"techcrunch: {s['techcrunch']['query']} -> {s['techcrunch']['n']} results, {tc}",
           f"crunchbase_news: {s['crunchbase_news']['query']} -> {s['crunchbase_news']['n']} results, {cb}"]
    if local and "googlenews_local" in s:
        out.append(f"googlenews_local: {s['googlenews_local']['query']} -> {s['googlenews_local']['n']} results, {local}")
    if formd:
        out.append(f"formd: {formd}")
    return out
def no(slug, surf, note, src="absence_check", cite=None, **kw):
    L.append(cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf="medium", grad_asof=TODAY, surfaces=surf, note=note, **kw))

no("anytype", lines("anytype", "the $13.4M round of Aug 2023 and nothing after it", "the 2023 round only", "none naming a round", "none", "the 2023 round and product coverage only"),
   "Not graduated: no round after the seed of Aug 2023 on any surface, 37 months on")
no("delli", lines("delli", "the $7.2M seed of Sep 2022 and the $6M extension of Sep 2024", "the seed and its 2024 extension ('Seed Extension', Pulse 2.0), no Series A", "none naming Delli", "none", "the same two rounds"),
   "Not graduated: the only later money is the $6M seed extension of Sep 2024, which counts as the seed")
no("furhat-robotics", lines("furhat-robotics", "the $2.5M seed of Sep 2017 and nothing after it", "the seed and the purchase of Misty Robotics (2022), no later round", "the Misty purchase only", "none", "none naming a round"),
   "Not graduated: no round after the seed of Sep 2017 on any surface")
no("grasp", lines("grasp", "the card (Seed 2023), no post names a round", "the Series A headlines of Oct 2025 are a different, Swedish company (Point Nine's book records the same reading)", "none naming this company", "none", "the same Swedish company only"),
   "Not graduated: no round after the GBP 3.1M seed of Jul 2023; aligned to Point Nine's book", entry_date="2023-07")
no("levity", lines("levity", "the $8.3M seed of Oct 2022 and nothing after it", "the seed only (the rest are an entertainment company of the same name)", "none naming a round", "none", "the seed only"),
   "Not graduated: no round after the seed of Oct 2022 on any surface, 47 months on")
no("request-finance", lines("request-finance", "the $5.5M seed of Jun 2022 and nothing after it", "the seed, two acquisitions and 'strategic funding' of undisclosed size (Mar 2025), no named or sized later round", "none naming a round", "none naming a round", "the seed only"),
   "Not graduated: the only later money is an undisclosed 'strategic funding' of Mar 2025, neither named nor sized")
no("riff", lines("riff", "the $1.5M seed of Aug 2020 and nothing after it (Chandratillake left the board 2026-03)", "none about the company (the word is a common one)", "none naming the company", "none naming the company", "none about the company"),
   "Not graduated: no round after the seed of Aug 2020 on any surface")
no("supernormal", lines("supernormal", "the $10M seed of Jan 2023 and nothing after it", "the seed only", "the seed only", "none", "the seed only", formd="Form D 2023-Q1 ($10.0M, Hanna) -> no later filing as of 2026-09-26"),
   "Not graduated: no round after the seed of Jan 2023 on any surface, 44 months on")
no("violet", lines("violet", "the card (Seed 2023), no post names a round", "none about the company (the word is a common one)", "none about the company", "none about the company", "none about the company"),
   "Not graduated: no round after the 2023 seed on any surface; the entry is read at its latest day, 2023-12-31, 33 months before the check")
# cited ends
no("adludio", lines("adludio", "the card (Seed 2013) and no post naming a round", "the closure (Sep 2024) and a 2023 profile, no round", "none naming the company", "none", "the same two items"),
   "Not graduated: no later round on any surface; the company closed in Sep 2024 (Performance Marketing World) and Adludio Limited is in liquidation (Companies House 08227542)",
   src="web_verified", cite="https://www.performancemarketingworld.com/article/1887634/industry-moves-adludio-closes-its-doors-omnicom-creates-centralised-hub")
no("dinghy", lines("dinghy", "the $1.2M seed of Jan 2018 and nothing after it", "the shutdown (Coverager, Feb 2023), no round", "none naming the company", "none", "the same"),
   "Not graduated: the seed was the last round; the company announced its shutdown in Feb 2023 (Coverager)", src="web_verified",
   cite="https://coverager.com/freelancer-insurance-agency-dinghy-to-shut-down/", status="defunct")
no("numeral", lines("numeral", "the EUR 13M seed of Dec 2021 and nothing after it", "the $100M Series C headlines of Sep 2026 are Numeral the US sales-tax company, a homonym; none names a later round of the Paris company", "none naming this company", "none naming this company", "the seed only"),
   "Not graduated: the seed of Dec 2021 was the last round; acq. by Mambu, announced Dec 2024 (Finextra)", src="web_verified",
   cite="https://www.finextra.com/newsarticle/45175/mambu-acquires-french-payments-player-numeral")
no("opbeat", ["firm: balderton.com/companies card and the news archive (552 posts to 2026-09-23) for the name -> the 2017 post on the sale to Elastic, no round",
              "formd: Form D 2013-Q3 ($2.9M, Maloney) -> no later filing as of 2026-09-26",
              "techcrunch: Opbeat -> 6 results, the sale to Elastic (2017-06-22) and no round after 2013",
              "googlenews: \"Opbeat\" -> 26 results, one naming the company (2015), no round"],
   "Not graduated: the 2013 round was the last; acq. by Elastic, Jun 2017 (the firm's post)", src="first_party", cite=post("opbeat", "elastic"), entry_date="2013-06-24")
no("rahko", lines("rahko", "the GBP 1.3M seed of Oct 2019 and the sale to Odyssey", "the seed and the sale (PR Newswire, Jan 2022), no later round", "the seed only", "none", "the same"),
   "Not graduated: the seed of Oct 2019 was the last round; acq. by Odyssey Therapeutics, agreement Oct 2021, announced Jan 2022 (the firm's post; PR Newswire)",
   src="first_party", cite=post("rahko", "acquired"))
jl.write("batch-grad", L)
