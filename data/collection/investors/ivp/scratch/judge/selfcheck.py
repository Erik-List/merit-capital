"""Duty 7, blind 5% self-consistency (15 rows drawn with seed 92 from the
pre-rebuild evidence view, scratch/selfcheck-slugs.json): 3 of 15 disagreed,
each adjudicated and flagged unstable; the Datalogix hit was a class
(deterministic Wikidata `defunct` on an acquired company) and the sweep found
one more (Sequent)."""
from jl import *
L = []
def row(slug, **k):
    d = {"slug": slug}; d.update(k); L.append(d)
row("datalogix", status="acquired", hq_city="Westminster", hq_city_source="model_knowledge", hq_city_confidence="high",
    flags=["unstable"],
    note="Self-consistency (2026-09-26): the deterministic Wikidata 'defunct' read the 2015 merger into Oracle as a dissolution; Oracle bought Datalogix (announced Dec 2014, closed Jan 2015), so acquired. City is Westminster CO, the municipality, not the Denver metro.")
row("sequent-computer-systems", status="acquired",
    note="Class sweep after the Datalogix hit: the deterministic Wikidata 'defunct' read IBM's 1999 purchase as a dissolution, so acquired.")
row("qubole", **stage("Growth", "web_verified", "https://www.avcj.com/avcj/news/49692/ivp-leads-usd30m-series-c-for-india-us-based-qubole", "high"),
    flags=["unstable"], clear_flags=["stage_uncited"],
    note="Self-consistency: the blind pass could not name the round; IVP led the $30M Series C (Jan 2016, Somesh Dash to the board), so the recorded Growth stands, now cited.")
row("surf-air-global-ltd", entry_stage="undetermined", entry_stage_source="model", entry_stage_confidence="low",
    flags=["unstable"],
    note="Self-consistency: the Form D band read the 2018 Surf Air Global Ltd raise as a Series A by amount, but Surf Air was seven years old with earlier institutional rounds and the round IVP bought is not named anywhere, so the stage is undetermined.")
write("../queue/selfcheck.out.jsonl", L)
