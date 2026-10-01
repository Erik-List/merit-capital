"""PRO-83 post-rebuild delta: the eight recall additions (membership + classification) and the S2A pass on
every Seed entry (graduation-surfaces.json of 2026-09-30 + the firm's archive + sibling books)."""
import importlib.util
import json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, V = jl.c, jl.loc, jl.V
HERE = Path(__file__).resolve().parent
SURF = json.loads((HERE / "graduation-surfaces.json").read_text())
ASOF = "2026-09-30"
FIRM = ("firm: seedcamp.com Views archive (1,337 posts, 2007 to 2026-09-30), the live portfolio list and the archived "
        "2008-2024 lists read for the name -> {}")


def surf_lines(slug, finding, sib=None):
    g = SURF.get(slug) or {}
    out = [FIRM.format(finding)]
    for svc in ("googlenews", "googlenews_firm", "techcrunch", "crunchbase_news", "googlenews_local"):
        v = (g.get("surfaces") or {}).get(svc)
        if not v:
            continue
        if v.get("status") != "ok":
            raise RuntimeError(f"{slug}: surface {svc} not ok; re-run surfaces before a no")
        items = v.get("items") or []
        named = sum(1 for i in items if i.get("names"))
        out.append(f"{svc}: {v.get('query') or g.get('query_name')} -> {v.get('n', len(items))} results, {named} naming "
                   f"the name; {finding}")
    if sib:
        out.append(sib)
    return out


def no(slug, finding, sib=None, note=None):
    """not_graduated by the absence test."""
    return c(slug, grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
             surfaces=surf_lines(slug, finding, sib), note=note)


FD = {
    "teleport": "formd: the local Form D issuer data 2008Q1-2026Q2 for the name -> Teleport, Inc. (CA) filed once, 2014Q3 (0001608746-14-000001, the seed); no later filing",
    "legit-patents": "formd: the local Form D issuer data 2008Q1-2026Q2 for Legit Patents / Legit.ai -> no filing",
    "membrane": "formd: the local Form D issuer data 2008Q1-2026Q2 for Membrane and Integration.app -> no filing by this company",
    "podo-labs": "formd: the local Form D issuer data 2008Q1-2026Q2 for Podo Labs -> no filing",
}


def end(slug, cite, what, note=None):
    """not_graduated on a cited terminal event (an acquisition or shutdown with no later round before it)."""
    return c(slug, grad="not_graduated", grad_src="web_verified", grad_cite=cite, grad_asof=ASOF,
             surfaces=surf_lines(slug, "no later round before the end: " + what, FD.get(slug)), note=note)


def yes(slug, cite, src="web_verified"):
    return c(slug, grad="graduated", grad_src=src, grad_cite=cite, grad_asof=ASOF)


def cens(slug):
    return c(slug, grad="censored", grad_asof=ASOF)


NOTHING = "no later priced round found"
L = []

# ---- recall additions (the firm's own posts; decisions.md D10 reading)
def member(slug, basis, cite):
    return jl.verdict(slug, "member", "Recall probe: " + basis, ec="site_listing", cite=cite)

RA = {
    "arcane": ("the firm's post of 2023-12-18: 'a previously unannounced $1 million pre-seed round led by us'; listed in the firm's 2024 review "
               "as 'Arcane (GB)'", V + "arcane-raises-6m-to-give-every-marketer-the-power-of-a-team-via-its-ai-powered-co-pilot/"),
    "kern-ai": ("the firm's post of 2023-02-16: 'We are excited to co-lead Kern AI's EUR 2.7 million seed round alongside Faber'",
                V + "open-source-platform-kern-ai-raises-e2-7-million-in-seed-funding-to-power-data-centric-natural-language-processing/"),
    "mindlabs": ("'New to the Nation ... MindLabs - A live mental health platform' (the firm's 2020 review)", V + "seedcamp-2020-year-in-review/"),
    "ourspace": ("the firm's post of 2022-10-25: 'We are excited to join Ourspace's $2.5M pre-seed round led by Connect Ventures'",
                 V + "ourspace-raises-2-5-million-to-redesign-cross-functional-teams/"),
    "recurse-ml": ("the firm's post of 2024-07-10: 'We are excited to co-lead Recurse ML's GBP 2.5 million funding round alongside Playfair'",
                   V + "recurse-ml-raises-2-5m-to-build-machine-learning-models-for-large-codebase-maintenance/"),
    "salesroom": ("the firm's post of 2022-06-22: 'We are excited to participate in Salesroom's $8 million seed round'",
                  V + "salesroom-brings-smart-video-to-sales-meetings-with-8m-in-funding/"),
    "specify": ("listed in 'Seedcamp's Developer Footprint (so far...)' (the firm's post of 2021-11-30)",
                V + "the-future-of-developer-tools-and-the-tech-companies-out-to-improve-it/"),
    "troop": ("'We are excited to support Troop' among the firm's portfolio companies (its post of 2021-09-29)",
              V + "the-future-of-sustainability-and-the-tech-companies-out-to-improve-it/"),
}
for s, (b, u) in RA.items():
    L.append(member(s, b, u))
L += [
    c("arcane", stage="Pre-Seed", stage_src="first_party", stage_conf="high", stage_cite=RA["arcane"][1], entry_date="2023",
      **loc("GB", "London"), status="unknown", rng="below_1b", focus="AI & Applied AI",
      note="AI co-pilot for marketing content workflows; the firm's post of 2023-12-18: 'a previously unannounced $1 million pre-seed round led by us', "
           "then $5M seed led by Accel (AdExchanger, 2023-12-13); absent from the firm's live list in 2026"),
    c("kern-ai", stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=RA["kern-ai"][1], entry_date="2023-02-16",
      **loc("DE", "Bonn"), status="unknown", rng="below_1b", focus="AI & Applied AI",
      note="Data-centric NLP developer platform ('the Germany-based company', founded Nov 2020 by Johannes Hoetter and Henrik Wenck); the firm's "
           "post of 2023-02-16: co-led the EUR 2.7 million seed; absent from the firm's live list in 2026"),
    c("mindlabs", stage="undetermined", entry_date="2020", **loc("GB", "London"), status="unknown", rng="below_1b", focus="Healthcare & Bio",
      note="Live mental health classes ('New to the Nation', the firm's 2020 review); GBP 1.4M Oct 2020 and a $3.5M seed Oct 2021 (Yahoo), "
           "neither tied to the firm; absent from the firm's live list in 2026"),
    c("ourspace", stage="Pre-Seed", stage_src="first_party", stage_conf="high", stage_cite=RA["ourspace"][1], entry_date="2022-10-25",
      **loc("GB", "London"), status="unknown", rng="below_1b", focus="SaaS",
      note="Team design for product and engineering leaders; the firm's post of 2022-10-25: 'join Ourspace's $2.5M pre-seed round led by Connect "
           "Ventures'; absent from the firm's live list in 2026"),
    c("recurse-ml", stage="undetermined", entry_date="2024-07", **loc("GB", "London"), status="unknown", rng="below_1b", focus="DevTools & APIs",
      note="ML models for large-codebase maintenance ('a UK-based startup'); the firm's post of 2024-07-10: 'co-lead Recurse ML's GBP 2.5 million "
           "funding round' (no round word); absent from the firm's live list in 2026"),
    c("salesroom", stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=RA["salesroom"][1], entry_date="2022-06-22",
      **loc("US", None), flags=["city_unknown"], status="private", rng="below_1b", focus="SaaS",
      note="Video conferencing built for sales (founders Roy Solomon of Applause and Daria Danilina); the firm's post of 2022-06-22: 'participate in "
           "Salesroom's $8 million seed round' ($8.5M, Business Wire); Creatio partnership Dec 2024; absent from the firm's live list in 2026"),
    c("specify", stage="undetermined", entry_date="2021", **loc("FR", None), flags=["city_unknown"], status="unknown", rng="below_1b",
      focus="DevTools & APIs",
      note="Design-token and asset management for design systems (TechCrunch, 2022-02-24); in the firm's 2021 developer footprint; no round tied "
           "to the firm; absent from the firm's live list in 2026"),
    c("troop", stage="undetermined", entry_date="2021", **loc("GB", "London"), status="unknown", rng="below_1b", focus="Fintech & Payments",
      note="Pools retail shareholders' votes on ESG questions (TechCrunch, 2022-11-02); 'We are excited to support Troop' (the firm's 2021 post), "
           "no round named; absent from the firm's live list in 2026"),
]

# ---- S2A: graduated (a later round the record names, or an unnamed one past the era's threshold)
G = {
    "curve": "https://www.fintechfutures.com/2019/07/curve-raises-55m-in-series-b-round/",
    "cymmetria": "https://www.darkreading.com/cyberattacks-data-breaches/cymmetria-adds-9-million-in-funding",
    "fluidstack": "https://www.forbes.com/sites/iainmartin/2026/09/03/a-tiny-startup-helping-google-take-on-nvidia-is-now-worth-18-billion/",
    "hubble": "https://www.finsmes.com/2019/01/hubble-raises-4m-in-series-a-funding.html",
    "marcopolo-learning": "https://venturebeat.com/business/marcopolo-learning-raises-8-5-million-and-cuts-deal-with-boat-rocker-media",
    "nodes-and-links": "https://www.cbn.com.cy/article/106190/cyprus-based-nodes-links-raises-12m-to-transform-construction-industry-with-ai",
    "pento": "https://techcrunch.com/2021/12/07/londons-pento-raises-35m/",
    "pointy": "https://www.siliconrepublic.com/start-ups/pointy-funding-series-a",
    "portalone": "https://techcrunch.com/2022/01/27/portalone-raises-60m-as-it-gears-up-to-launch-of-its-hybrid-immersive-gaming-platform-later-this-year/",
    "property-partner": "https://www.businessinsider.com/property-partner-16-million-series-b-proptech-2016-3",
    "questdb": "https://techcrunch.com/2021/11/03/questdb-snares-12m-series-a-with-hosted-version-on-the-horizon/",
    "sano": "https://mmc.vc/mmc-leads-11-milllion-series-a-for-genetic-disease-research-platform-sano-genetics/",
    "studentfinance": "https://techcrunch.com/2023/02/28/studentfinance-nabs-41m-to-help-europeans-upskill-for-in-demand-jobs/",
    "taxscouts": "https://www.uktechnews.info/2020/08/04/positron-technologies-t-a-taxscouts-secures-5-million-series-a-investment-led-by-octopus-ventures/",
    "this": "https://sifted.eu/articles/plant-based-this-20m-series-c-news",
    "trussle": "https://fintech.global/2020/01/22/digital-broker-trussle-secures-7-5m-in-funding-round/",
    "wave": "https://www.gamesindustry.biz/virtual-concert-firm-wave-raises-usd30m-in-funding",
    "weavr": "https://www.businessinsider.com/exclusive-fintech-startup-raises-40m-tiger-global-for-us-expansion-2022-2",
    "appwrite": "https://www.calcalistech.com/ctechnews/article/bj60000nyq5",
    "buynomics": "https://www.businessinsider.com/series-a-pitch-deck-buynomics-raises-13-million-from-insight-2022-11",
    "weengs": "https://www.eu-startups.com/2019/04/london-based-weengs-a-logistics-startup-for-e-commerce-retailers-raises-e7-5-million/",
}
for s, u in G.items():
    L.append(yes(s, u))
L.append(yes("emoov", V + "2017-year-in-review/", "first_party"))
L.append(yes("monese", V + "mobile-banking-service-monese-closes-10m-series-a/", "first_party"))
# Cymmetria's end: Stage Fund bought it in Sep 2019 (the YC book says acquired, the Felicis book defunct)
L.append(c("cymmetria", status="acquired",
           note="Cyber deception platform; on the firm's Fund III seed list (2015-09-21) and its 2015-06-29 post 'Cymmetria exits stealth, having "
                "raised a seed round with Seedcamp' (alongside Felicis and Y Combinator); $9M Series A led by Sherpa Capital (Dark Reading); "
                "acq. by Stage Fund, Sep 2019 (Calcalist), employees then filed for liquidation, Dec 2019 (Calcalist); the Felicis book reads "
                "defunct, the YC book acquired"))

# ---- S2A: not graduated on a cited end
L += [
    end("back", "https://www.handelsblatt.com/technik/it-internet/start-up-fuer-personalsoftware-personio-stemmt-naechste-uebernahme-und-kauft-software-spezialisten-back-technologies/28357636.html",
        "acq. by Personio, May 2022 (Handelsblatt)"),
    end("helloflow", "https://www.businesswire.com/news/home/20220208005237/en/Trulioo-Acquires-No-Code-Orchestration-Solution-HelloFlow-to-Accelerate-Digital-Onboarding-and-Advance-its-End-to-End-Global-Identity-Platform",
        "acq. by Trulioo, Feb 2022 (Business Wire)"),
    end("incrediblue", "https://news.gtp.gr/2018/01/24/spains-nautal-acquires-greek-yachting-startup-incrediblue/", "acq. by Nautal, Jan 2018 (GTP)"),
    end("skew", "https://www.coinbase.com/blog/coinbase-to-acquire-leading-institutional-data-analytics-platform-skew", "acq. by Coinbase, Apr 2021"),
    end("pace", "https://skift.com/2022/09/20/airline-software-startup-flyr-buys-pace-revenue-to-expand-into-serving-hotels/", "acq. by FLYR, Sep 2022 (Skift)"),
    end("teleport", "https://estonianworld.com/business/estonian-startup-teleport-acquired-move-guides/",
        "acq. by MoveGuides, Apr 2017 (Estonian World), as in the a16z book"),
    end("wexler", "https://www.uktech.news/legal/wexler-acquired-by-swedish-legal-unicorn-legora-20260730",
        "acq. by Legora, Jul 2026 (UKTN), inside the window, which a cited end decides"),
    end("kukimi", "https://www.deutsche-startups.de/2016/12/20/kukimi-noch-ein-food-startup-schlittert-die-inolvenz/",
        "insolvent Dec 2016 (Deutsche Startups)"),
    end("heresy", "https://find-and-update.company-information.service.gov.uk/company/10309713",
        "HERESY SOFTWARE LTD dissolved 2025-09-30 (Companies House)"),
]

# ---- S2A: not graduated by the absence test
for s in ("askui", "charlie-hr", "edgefolio", "findify", "fractal-labs", "gameye", "getagent", "klasha", "land-insight", "legit-patents",
          "mailcloud", "membrane", "podo-labs", "priori-data", "spill", "spoke", "arcjet", "botika", "homie", "pixie", "pronto",
          "splittable", "vaire", "vitesse"):
    L.append(no(s, NOTHING, FD.get(s)))
L.append(no("sweatcoin", NOTHING + " (the $13M of Jul 2022 was the SWEAT token sale by Sweat Economy, not a priced round of the company)"))
L.append(no("papaya", NOTHING, "sibling:20vc: its row reads not_graduated on the same absence test (2026-09-27)"))
L.append(no("riff", NOTHING + " (the Norwegian Riff's $16M Series A of Oct 2025 is a namesake)",
            "sibling:balderton-capital: its row reads not_graduated (Riff Technologies, Companies House 12611399 active)"))

# ---- S2A: censored (entry inside 24 months, or a bare 2025)
for s in ("bioorbit", "catch", "dalton", "eversettled", "opereit", "opio", "pair", "stackfix", "topograph", "uncovr"):
    L.append(cens(s))

if __name__ == "__main__":
    jl.write("delta-01", L)
