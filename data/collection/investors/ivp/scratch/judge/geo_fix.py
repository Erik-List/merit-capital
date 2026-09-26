"""Geography sweep (2026-09-26): the Wikidata-sourced countries read against
their cities (two incoherent pairs), and a citation for every visible non-US
row whose country rests on model knowledge (COLLECTION.md 6 hq_country)."""
from jl import *
L = []
def row(slug, **k):
    d = {"slug": slug}; d.update(k); L.append(d)
row("seagate-technology", hq_city="Fremont", hq_city_source="web_verified", hq_city_confidence="high",
    note="Geo sweep: the pair read US + Dublin. Seagate's operating headquarters is Fremont CA and Dublin is only its legal domicile (https://en.wikipedia.org/wiki/Seagate_Technology), so the city is Fremont and the country stays US.")
row("shazam", hq_country="GB", hq_country_source="model_knowledge", hq_country_confidence="high", flags=["model_disputes_source"],
    note="Geo sweep: Wikidata's US is the acquirer's (Apple); Shazam Entertainment was a London company when Apple bought it in 2018, so GB with London.")
row("deepl", hq_country_citation="https://www.deepl.com/en/press-release/deepl-announces-300-million-investment-at-2-billion-valuation-fueled-by-global-demand-for-ai-language-solutions",
    note="Geo sweep: Cologne, Germany, per the company's own release.")
row("pigment", hq_country_citation="https://techcrunch.com/2024/04/04/business-planning-startup-pigment-raises-145-million-round-in-rare-french-tech-megaround/",
    note="Geo sweep: Paris-founded French company per the Series D coverage.")
row("papaya-global", hq_country="US", hq_country_source="web_verified", hq_country_confidence="medium",
    hq_country_citation="https://en.wikipedia.org/wiki/Papaya_Global",
    hq_city="New York", hq_city_source="web_verified", hq_city_confidence="medium", clear_flags=["model_disputes_source"],
    note="Geo sweep: the column is current HQ, and Papaya now gives New York as its headquarters (Wikipedia infobox); founded in Tel Aviv, where R&D stays. Wikidata's 'Israel / United States' named both.")
row("wonderful", hq_country="NL", hq_country_source="web_verified", hq_country_confidence="high",
    hq_country_citation="https://siliconangle.com/2026/09/02/wonderful-raises-550m-at-5b-valuation-for-its-ai-automation-platform/",
    hq_city="Amsterdam", hq_city_source="web_verified", hq_city_confidence="high", clear_flags=["model_disputes_source"],
    note="Geo sweep: founded in Tel Aviv in 2025 but headquartered in Amsterdam (legal and commercial HQ; R&D in Tel Aviv), per the Series C coverage ('Amsterdam-based Wonderful').")
write("../queue/geo-fix.out.jsonl", L)
