"""PRO-162 fixes from the in-flight verify after the rebuild (2026-09-27): focus on the rows that had none, the public
rows' market caps (stockanalysis.com, as of 2026-09-25), the stage citations verify asks for, and Symphony Commerce, which
absorbs the sneakpeeq row (one SEC issuer, CIK 1517646)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, NEWS = jl.cls, jl.rnd, jl.NEWS
V = {"valuation_range_source": "web_verified"}
L = []
FOCUS = {"avidxchange": "Fintech & Payments", "clari": "SaaS", "docusign": "SaaS", "dynatrace": "Data Infrastructure",
         "flywire": "Fintech & Payments", "forescout-technologies-inc": "Security", "join-the-company": "Media, Gaming & Advertising",
         "mirakl": "SaaS", "pleo": "Fintech & Payments", "quanterix": "Healthcare & Bio", "rapid7": "Security",
         "rave-mobile-safety": "SaaS", "redis": "Data Infrastructure", "rent-the-runway": "Consumer & Marketplaces",
         "rubrik": "Security", "smartrent": "SaaS", "socure": "Security", "startree-cortexdata": "Data Infrastructure",
         "synapdx": "Healthcare & Bio", "sysdig": "Security", "taleo": "SaaS", "tellapart-acquired-by-twitter-in-2015":
         "Media, Gaming & Advertising", "tengion": "Healthcare & Bio", "tracelytics": "DevTools & APIs",
         "turbonomic-ibm": "Data Infrastructure", "txvia-google": "Fintech & Payments", "unstructured": "AI & Applied AI",
         "vention": "Industrial & Robotics", "vonage": "Consumer & Marketplaces", "wonolo": "Consumer & Marketplaces",
         "zero-turnaround": "DevTools & APIs", "symphony-commerce": "SaaS"}
for s, f in FOCUS.items():
    if s in ("docusign", "flywire", "rubrik", "symphony-commerce"):
        continue
    L.append(cls(s, focus=f))
L.append(cls("docusign", status="public", rng="10b_plus", usd=12620000000, val_src="web_verified", asof="2026-09-25",
    val_cite="https://stockanalysis.com/stocks/docu/market-cap/", extra=V, focus="SaaS"))
L.append(cls("flywire", status="public", rng="1b_plus", usd=2120000000, val_src="web_verified", asof="2026-09-25",
    val_cite="https://stockanalysis.com/stocks/flyw/market-cap/", extra=V, focus="Fintech & Payments"))
L.append(cls("rubrik", status="public", rng="10b_plus", usd=22710000000, val_src="web_verified", asof="2026-09-25",
    val_cite="https://stockanalysis.com/stocks/rbrk/market-cap/", extra=V, focus="Security"))
L.append(cls("acv", stage="Growth", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://www.sec.gov/Archives/edgar/data/1637873/000119312521060598/d34258dex101.htm"))
L.append(cls("cube-js", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=NEWS("cube-js", "Cube Dev raises $6.2M"), clear=["cite_pending"]))
L.append(cls("truemotion", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"]))
TC_SEED = "https://techcrunch.com/2012/02/10/social-shopping-site-sneakpeeq-raises-2-7m-from-bain-capital-ventures-keith-rabois-and-others/"
TC_A = "https://techcrunch.com/2012/03/29/firstmark-capital-leads-7-5m-round-in-social-shopping-startup-sneakpeeq/"
L.append(cls("symphony-commerce", focus="SaaS", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SEED,
    entry_date="2011-03-25", grad="graduated", grad_src="web_verified", grad_cite=TC_A, grad_conf="high",
    rounds=[rnd("2012-03", "Series A", 7500000, "FirstMark Capital", None, TC_A, "press")],
    note="Commerce-as-a-service for brands (San Francisco), which began as the social shopping site sneakpeeq (one SEC issuer, CIK "
         "1517646; the sneakpeeq row folds in here). 'Social Shopping Site Sneakpeeq Raises $2.7M From Bain Capital Ventures, Keith "
         "Rabois And Others' (TechCrunch, 2012-02-10), the $2.67M seed the March 2011 Form D records (Ajay Agarwal); 'FirstMark "
         "Capital Leads $7.5M Round' (TechCrunch, 2012-03-29), its Series A, graduates it. The firm lists it as acquired."))
if __name__ == "__main__":
    jl.write("fix-3", L)
