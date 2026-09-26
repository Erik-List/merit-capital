"""PRO-106 grind: the rows deferred from the batches (unidentified desk-era names, Spodradio, Opbeat)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls = jl.cls
L = []
TRIED = "searched 2026-09-26 (web search on the name with the desk's name, TechCrunch's archive, Google News): nothing names the company"
for s, n, dom in [("activiti", "Activiti", "activiti.com"), ("cas-services", "Cas Services", "casservicesltd.com"), ("i-cue", "i-Cue", "i-cue.co.uk"),
                  ("visual-media", "Visual Media", "vmfx.com")]:
    L.append(cls(s, status="unknown", country="GB", city=None, stage="undetermined", rng="undetermined", grad="undetermined",
        flags=["identity_unresolved", "country_prior", "city_unknown"], extra={"hq_city": None, "focus": None},
        note=f"Listed on the Benchmark Europe desk page with the link {dom} and nothing else; {TRIED}, so the company cannot be described; country inferred from the London desk"))
L.append(cls("spodradio", status="unknown", country="DE", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://venturebeat.com/business/spodradio-a-radio-and-podcast-hub-gets-10m-from-benchmark/", rng="below_1b",
    focus="Media, Gaming & Advertising", flags=["city_unknown", "country_prior"], extra={"hq_city": None},
    note="Mobile radio and podcast software for carriers; Benchmark Capital Europe and Baytech put $10M into its second round, Oct 2006 (VentureBeat; Baytech alone backed the $2.4M first round in 2005); the company's later fate and its city are not on any surface read",
    rounds=[jl.rnd("2005", "first round", 2400000, "Baytech", False, "https://venturebeat.com/business/spodradio-a-radio-and-podcast-hub-gets-10m-from-benchmark/"),
            jl.rnd("2006-10", "second round", 10000000, "Benchmark Capital Europe", True, "https://venturebeat.com/business/spodradio-a-radio-and-podcast-hub-gets-10m-from-benchmark/")]))
L.append(cls("opbeat", status="acquired", city="Copenhagen", rng="below_1b", focus="DevTools & APIs",
    note="Application performance monitoring; the $2.9M round of 2013 with Creandum (Form D Jun 2013, Maloney), a seed by the band and in Creandum's book; the card says 'Series A in 2013', which no dated source repeats; acq. by Elastic, 2017 (the firm's post of 2017-06-22)"))
jl.write("batch-008", L)
