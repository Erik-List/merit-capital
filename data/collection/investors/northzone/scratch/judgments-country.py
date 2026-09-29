"""PRO-105 fix after the rebuild's prepare (2026-09-29 ~22:40 UTC): my batch helpers passed the country's
source and citation but not the country itself, so 114 judged rows carried no hq_country (and the one-word
Wikidata claims stayed unconfirmed). Countries now come from the city each row was judged to, checked
against the firm's own location field: equal -> web_verified, cited to the firm's company page; different
-> model_knowledge with the reason in the note."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, page = jl.cls, jl.page
todo = json.load(open("/private/tmp/claude-501/-Users-erik-Developer-merit-capital/10f04a40-cbf8-46db-b66c-aeceb2e15a21/scratchpad/nz/country-todo.json"))
L = []
for s, final, city, sc, kn in todo:
    if s == "alphora":
        final = "DE"; sc = "DE"
    if s == "behaviosec":
        L.append(cls(s, country="SE", country_src="web_verified", country_cite=page(s), city=None, flags=["city_unknown"],
                     extra={"hq_city": None}, note="HQ read as the firm's Sweden (founded in Luleå 2008; the acquirer's release names a presence in the US, Canada and EMEA); the San Francisco city first recorded is not confirmed by the surfaces read, so no city is asserted"))
        continue
    if final == sc:
        L.append(cls(s, country=final, country_src="web_verified", country_cite=page(s)))
    else:
        L.append(cls(s, country=final, country_src="model_knowledge",
                     note={"avito": "Country RU: Avito operated from Moscow; the firm's page lists Sweden, its founders' home",
                           "cusp-ai": "Country GB: Cambridge, UK (the firm's page gives no location)"}.get(s)))
jl.write("batch-country", L)
