"""PRO-161, 2026-09-29: the first questions of the new hq_country claim guard (a non-US Wikidata country on a one-word
name, COLLECTION.md s5). Each join was checked against the company the row's note names; all ten are the right
entity, so each is recorded as the judge's value with its Wikidata provenance."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)

CONFIRMED = {"ajaib": "ID", "bharatpe": "IN", "clip": "MX", "cred": "IN", "kavak": "MX", "monzo": "GB",
             "nubank": "BR", "phonepe": "IN", "razorpay": "IN", "borro": "GB"}
jl.write("country-claims-1", [jl.cls(s, country=c, country_src="wikidata") for s, c in CONFIRMED.items()])
