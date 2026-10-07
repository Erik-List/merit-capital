"""Seed-to-Series-A decisions for every open Seed row, and stage/citation fixes found on the way.
Evidence: scratch/graduation-surfaces.json (run 2026-10-06, 268 lookups, none failed), sibling books, six web searches."""
from jl import *
import importlib.util, sys, json
ROOT = H.parents[4]
spec = importlib.util.spec_from_file_location("gs", ROOT / "scripts" / "graduation-surfaces.py")
gs = importlib.util.module_from_spec(spec); _a = sys.argv; sys.argv = sys.argv[:1]; spec.loader.exec_module(gs); sys.argv = _a
G = json.loads((H / "graduation-surfaces.json").read_text())
ASOF = "2026-10-06"
CACHE_P = H / "grad-urls.json"; CACHE = json.loads(CACHE_P.read_text()) if CACHE_P.exists() else {}
def head(slug, sub):
    key = f"{slug}|{sub}"
    if CACHE.get(key): return CACHE[key]
    for v in G[slug]["surfaces"].values():
        for i in v.get("items") or []:
            if sub.lower() in i["title"].lower():
                u = i.get("link") or i.get("url") or (gs.decode(i["gid"]) if i.get("gid") else None)
                if u:
                    CACHE[key] = u; CACHE_P.write_text(json.dumps(CACHE, indent=1)); return u
    raise SystemExit(f"no URL for {slug}: {sub}")
def surf(slug, finding, us=True):
    g = G[slug]; out = ["firm: foundersfund.com live list, the archived /company/ pages (2009-2026) and the firm's 24 posts, read for a later round -> " + finding]
    if us: out.append("formd: the company's Form D sequence in the bulk data through 2026 (sources/edgar/formd-issuer-rounds.json) -> no later priced round meeting the step-up")
    for svc in ("googlenews", "googlenews_firm", "techcrunch", "crunchbase_news", "googlenews_local"):
        v = g["surfaces"].get(svc)
        if not v: continue
        assert v.get("status") == "ok", (slug, svc)
        n = v.get("n", len(v.get("items") or [])); named = sum(1 for i in v.get("items") or [] if i.get("names"))
        out.append(f"{svc}: {v.get('query') or g.get('query_name')} -> {n} results, {named} naming the company; {finding}")
    return out
def grad(slug, cite, note=None, **kw):
    C(slug, seed_to_a_graduation="graduated", graduation_source="web_verified", graduation_confidence="high", graduation_citation=cite, **({"note": note} if note else {}), **kw)
def sib_grad(slug, inv, sslug=None):
    c = json.loads((H.parents[1] / inv / "companies/classification.json").read_text())[sslug or slug]
    assert c.get("seed_to_a_graduation") == "graduated" and c.get("graduation_citation"), (slug, inv)
    C(slug, seed_to_a_graduation="graduated", graduation_source=c["graduation_source"] if c["graduation_source"] != "formd" else "web_verified", graduation_confidence="high", graduation_citation=c["graduation_citation"])
def no(slug, finding, src="absence_check", cite=None, us=True, **kw):
    d = dict(seed_to_a_graduation="not_graduated", graduation_source=src, graduation_confidence="medium", graduation_asof=ASOF, graduation_surfaces=surf(slug, finding, us))
    if cite: d["graduation_citation"] = cite
    C(slug, **d, **kw)
# --- graduated on a cited later round
grad("backplane", head("backplane", "Raises Over $4M"))
grad("billguard", head("billguard", "Put $10 Million Into BillGuard"))
grad("bitpay", head("bitpay", "Series A Led By Index"))
grad("brit-co", "https://techcrunch.com/2013/06/25/brit-and-co-morin-6-5m-series-a-funding-oak-investment-partners")
grad("compass", head("compass", "Raises $370M"))
grad("crowdflower", head("crowdflower", "CrowdFlower raises $10M"))
grad("fanbridge", head("fanbridge", "$2 Million In Fresh Funding"))
grad("homee-interiors-inc", "https://www.housingwire.com/articles/40667-zillow-invests-10-million-in-virtual-interior-design-app-hutch/", entry_date="2016-06",
     note="Homee, renamed Hutch in 2017: interior-design app. 'Homee raises $5M from Founders Fund' (TechCrunch, July 2016); Zillow led the $10M Series A of July 2017. No trace of the app after about 2020.")
grad("instacanvas", head("instacanvas", "Twenty20 Raises $8M"))
grad("isocket", head("isocket", "Nabs $8M"))
grad("layup-parts", head("layup-parts", "Ex-Anduril engineer raises $42M"))
grad("leap-motion", head("leap-motion", "nabs $50M"))
grad("life360", "https://www.life360.com/press/angellist-with-expansion-vc-join-50-million-series-c-investment-in-life360")
grad("lore", "https://www.techlearning.com/news/academic-social-network-raises-5-million",
     note="Coursekit, later Lore. Founders Fund was in the $1M seed of June 2011; the $5M Series A of January 2012 was led by The Social+Capital Partnership. Acq. by Noodle, 2013.")
grad("ostrovok", head("ostrovok", "Takes $25M"))
grad("oyster", "https://techcrunch.com/2014/01/14/oyster-raises-14-million-to-build-a-comprehensive-netflix-for-books")
grad("primer", "https://www.notboring.co/p/primer-the-ambitious-home-for-ambitious")
grad("quince", head("quince", "$50 million Series A"))
grad("ritual", head("ritual", "$10.5M Series A"))
grad("sendgrid", "https://www.sec.gov/Archives/edgar/data/1477425/000104746917006437/a2233508zex-4_3.htm")
grad("tagomi", head("tagomi", "$12 Million in Second Funding Round"))
grad("ubeam", head("ubeam", "$10 Million In Funding From Upfront"))
grad("vicarious-systems", "https://techcrunch.com/2012/08/21/vicarious-good-ventures-funding")
for slug, inv in [("betable", "atomico"), ("carwoo", "felicis"), ("moat", "first-round-capital"), ("path", "first-round-capital"), ("ripple", "a16z"), ("styleseat", "point-nine")]:
    sib_grad(slug, inv)
C("tachyus", seed_to_a_graduation="graduated", graduation_source="formd", graduation_confidence="high")
# --- not graduated: a cited end
for slug, sub, what in [("atavist", "acquires Atavist", "acquired by Automattic in June 2018 with the seed its last round"),
                        ("booshaka", "Sprinklr Acquires Booshaka", "acquired by Sprinklr in November 2015 after seed-size rounds only"),
                        ("tbh", "Facebook Acquires Anonymous", "acquired by Facebook in October 2017, weeks after launch"),
                        ("topguest", "Topguest Acquired By EzRez", "acquired by ezRez (Switchfly) in December 2011"),
                        ("votizen", "Causes Acquires Votizen To", "acquired by Causes in January 2013"),
                        ("wallaby", "Acquired by Bankrate", "acquired by Bankrate in December 2014 with the seed its last round")]:
    no(slug, what, src="web_verified", cite=head(slug, sub))
no("readyforce", "acquired by LookSharp in December 2014; no Series A is reported", src="web_verified", cite=head("readyforce", "Acquires Readyforce"), status="acquired",
   note="College recruiting network listed under FF Angel. Acq. by LookSharp, December 2014.")
# --- not graduated: the filings
for slug in ("azumio", "emerald-therapeutics", "inigral", "prior-knowledge", "tribogenics-inc"):
    C(slug, seed_to_a_graduation="not_graduated", graduation_source="formd", graduation_confidence="medium", graduation_asof=ASOF, graduation_surfaces=surf(slug, "no later round named"))
# --- not graduated: the dated search found no later round
for slug, finding in [("100plus", "no later round; acquired by Practice Fusion in February 2013 (the 2021 headlines are another company that took the name)"),
    ("affordit", "no later round"), ("afterhour", "no round after the June 2024 seed"), ("amicus", "no later round for the non-profit fundraising company (the headlines are namesakes)"),
    ("brave", "a 2019 report of a planned Series A 'per sources' and no announced close; the 2017 token sale is not a priced round"), ("coolchip", "no later round"),
    ("estately", "no later round"), ("frogmetrics", "no later round"), ("geckogo", "no later round"), ("hipchat", "no later round; acquired by Atlassian in March 2012"),
    ("hipswap", "no later round"), ("immunepath", "no later round; wound down in 2012"), ("lagrange-labs", "no round after the May 2024 seed"), ("networkedblogs", "no later round"),
    ("portalarium", "no named later round"), ("retel-technologies", "no later round"), ("ringadoc", "no round after the $1.9M seed of 2012-13; acquired by Practice Fusion in 2015"),
    ("sentient", "no priced round after the July 2024 seed"), ("tlon", "no named later round"), ("transatomic-power", "a $2.5M extension in 2015 and no Series A; closed in September 2018"),
    ("unbound", "no later round"), ("uservoice", "no later round")]:
    no(slug, finding)
C("ringadoc", entry_date="2013-01", note="After-hours telemedicine. 'Ringadoc Raises $1.2M From Founders Fund's FF Angel' (TechCrunch, January 2013), part of its $1.9M seed. Acq. by Practice Fusion, 2015.")
for slug in ("endurance-energy", "gamgee"):
    C(slug, seed_to_a_graduation="censored")
# --- stage and citation fixes
C("cherry", entry_stage="Series A", entry_stage_source="web_verified", entry_stage_confidence="high", entry_stage_citation="https://techcrunch.com/?p=536687", entry_date="2012", seed_to_a_graduation=None, clear_flags=["stage_uncited"],
  note="On-demand car wash. The $750K seed came from Max Levchin, David Sacks and Keith Rabois personally; Founders Fund entered in the $4.5M Series A of 2012 led by Shasta (TechCrunch), though the firm lists it under FF Angel. Closed in December 2012; Lyft took the team in 2013.")
C("sword-health", entry_stage="Series A", entry_stage_source="web_verified", entry_stage_confidence="high", entry_date="2020-02",
  entry_stage_citation="https://www.prnewswire.com/news-releases/sword-health-extends-series-a-to-17m-with-investment-from-khosla-ventures-and-founders-fund-301012225.html", clear_flags=["cite_pending"],
  note="Digital musculoskeletal care, founded in Porto, run from New York. 'SWORD Health Extends Series A to $17M With Investment From Khosla Ventures and Founders Fund' (PR Newswire, 2020-02-27). The Wikidata country string was malformed.")
C("gecko-robotics", entry_stage_source="web_verified", entry_stage_citation="https://techcrunch.com/2018/08/20/safety-and-inspection-bot-startup-gecko-robotics-adds-7-million-to-the-coffers/", entry_date="2018-08", clear_flags=["cite_pending"])
C("newlimit", entry_stage_source="web_verified", entry_stage_confidence="high", entry_stage_citation="https://www.axios.com/2023/05/16/coinbase-ceo-startup-newlimit-40-million-reverse-aging", clear_flags=["cite_pending"])
C("material", valuation_usd=1_100_000_000, valuation_range="1b_plus", valuation_source="web_verified", valuation_confidence="high", valuation_asof="2022-05-11",
  valuation_citation="https://siliconangle.com/2022/05/11/email-security-startup-material-security-raises-100m-unicorn-valuation-1-1b/", entry_stage_source="web_verified",
  entry_stage_citation="https://siliconangle.com/2022/05/11/email-security-startup-material-security-raises-100m-unicorn-valuation-1-1b/", entry_stage_confidence="high", clear_flags=["needs_web_value"], flags=["stale"],
  note="Material Security, email security. Founders Fund led the $100M Series C of May 2022 at $1.1B; no priced round since.")
write("g1-graduation")
