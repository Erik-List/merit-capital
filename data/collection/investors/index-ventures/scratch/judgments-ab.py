"""PRO-82 A/B pass on the visible slice (COLLECTION.md s7; standing duties 1, 4, 5, 8): every $1B+ or public row
defended with a citation and attacked with a 2026 news search (scratch/ab-sweep.py -> ab-news.json), public rows
re-read at their market cap of 2026-10-06. Values are aligned to a sibling book's cited mark where one is on disk
(the same event, the same figure), otherwise cited to a headline on disk or a page in scratch/web-finds.json.
Patch lines; a note is added only where the row's own note would otherwise mislead."""
import importlib.util, json, glob
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
jl = gl.jl; cls, post, nqurl = jl.cls, gl.post, gl.nqurl
WEB = json.loads((H / "web-finds.json").read_text()); web = lambda k: WEB[k]["url"]
AB = json.loads((H / "ab-news.json").read_text())
FACTS = json.loads((H.parent / "sources/wayback/archive-facts.json").read_text())["cc"]
NEWS = {}
for f in glob.glob(str(H / "news-bulk*.json")):
    for k, v in json.load(open(f)).items():
        if v.get("status") == "ok": NEWS.setdefault(k, []).extend(v["items"])
def _decode(it):
    u = it.get("url") or it.get("link") or jl._gs().decode(it["gid"])
    if not u: gl.ERRORS.append(f"decode failed: {it['title'][:60]}"); return "MISSING"
    return u
def abn(slug, sub):
    hits = sorted([i for i in AB[slug]["items"] if sub.lower() in i["title"].lower()], key=lambda i: (i["date"], i["source"]))
    if not hits or len({h["title"][:40].lower() for h in hits}) != 1:
        gl.ERRORS.append(f"abn({slug}, {sub}): {len(hits)} hits {[h['title'][:50] for h in hits][:4]}"); return "MISSING"
    return _decode(hits[0])
def nws(name, sub):
    hits = sorted([i for i in NEWS.get(name, []) if sub.lower() in i["title"].lower()], key=lambda i: (i["date"], i["source"]))
    if not hits or len({h["title"][:40].lower() for h in hits}) != 1:
        gl.ERRORS.append(f"nws({name}, {sub}): {len(hits)} hits {[h['title'][:50] for h in hits][:4]}"); return "MISSING"
    return _decode(hits[0])
def sx(slug, inv, skey=None):
    """Align to a sibling book's cited mark: (usd, asof, citation)."""
    c = json.loads((H.parents[1] / inv / "companies" / "classification.json").read_text()).get(skey or slug) or {}
    if not c.get("valuation_usd") or not str(c.get("valuation_citation") or "").startswith("http"):
        gl.ERRORS.append(f"sx({slug}, {inv})"); return dict(usd=None)
    return dict(usd=int(c["valuation_usd"]), val_src="web_verified", val_cite=c["valuation_citation"], asof=str(c.get("valuation_asof")))
def band(usd): return "100b_plus" if usd >= 1e11 else "10b_plus" if usd >= 1e10 else "1b_plus" if usd >= 1e9 else "below_1b"
L = []
def val(slug, usd=None, cite=None, asof=None, flags=(), clear=(), note=None, sib=None, **kw):
    k = dict(sib) if sib else dict(usd=int(usd), val_src="web_verified", val_cite=cite, asof=asof)
    if k.get("usd") is None: return
    L.append(cls(slug, rng=band(k["usd"]), flags=flags, clear=clear, note=note, **k, **kw))

# ---- public rows: market cap read 2026-10-06 (stockanalysis.com; companiesmarketcap.com for Ozon)
D = "2026-10-06"
val("facebook", 1.89e12, web("cap-meta"), D, flags=["model_disputes_source", "cite_pending"])
val("arista-networks", 270.14e9, web("cap-anet"), D, flags=["model_disputes_source"])
val("dropbox", 7.25e9, web("cap-dbx"), D, flags=["model_disputes_source", "cite_pending"])
val("criteo", 713.89e6, web("cap-crto"), D, flags=["model_disputes_source"])
val("outbrain", 56.02e6, web("cap-tead"), D, flags=["model_disputes_source"], note="the listed company is now Teads Holding Co. (NASDAQ: TEAD): Outbrain bought Teads in February 2025 and took its name; market cap read 2026-10-06")
val("scm-microsystems", 56.83e6, web("cap-inve"), D, flags=["model_disputes_source"], note="the listed company is now INVE Technologies (NASDAQ: INVE), formerly Identiv; market cap read 2026-10-06")
val("boku", 534082625, web("cap-boku"), D, note="market cap GBP 402.3M @ ECB 2026-10-06 (GBP/EUR 0.8488, EUR/USD 1.1269) = $534.1M")
val("gruppo-mutuionline", 1307204000, web("cap-mol"), D, clear=["needs_web_value"], note="market cap EUR 1.16B @ ECB 2026-10-06 (EUR/USD 1.1269) = $1.31B")
val("ozon-ru", 7.99e9, web("cap-ozon"), "2026-10", clear=["needs_web_value"])

# ---- private rows: a newer priced event found by the attack search
val("cohere", 20e9, abn("cohere", "Cohere merges with Aleph Alpha at $20B valuation"), "2026-04-24", flags=["model_disputes_source"],
    note="April 2026: merged with Aleph Alpha and raised $600M at a $20B valuation (Tech Funding News, 2026-04-24); in talks for more at the same mark in September 2026")
val("capitolis", 1.9e9, nqurl('"Capitolis" $1.9 billion valuation after:2026-10-01', "Capitolis raises $220 million from Wall Street giants at $1.9 billion valuation"), D, clear=["stale"],
    note="$220M announced 2026-10-06, including a $120M Series E at $1.9B (CTech)")
val("flapping-airplanes", 1.5e9, web("flapping-valuation"), "2026-01-28", clear=["needs_web_value"],
    note="the $180M seed of 2026-01-28 valued the lab at $1.5B (TechCrunch, 2026-02-17): the mark is the seed's own, so no later round is implied")
val("revel", 1.0e9, web("revel-valuation"), "2026-02-26", clear=["needs_web_value"],
    stage="Growth", stage_src="web_verified", stage_cite=web("revel-series-b"), stage_conf="high",
    note="'Index Ventures led the Series B round' of $150M (SiliconANGLE, 2026-02-26), 'at a $1+ billion valuation' (Sourcery, same day); the figure is the floor the source gives")
# ---- private rows: the deterministic mark confirmed against a sibling book's citation or a headline
val("anthropic", sib=sx("anthropic", "sequoia-capital"))
val("wonderful", sib=sx("wonderful", "ivp"))
val("simile", sib=sx("simile", "bain-capital-ventures"))
val("granola", sib=sx("granola", "kleiner-perkins"))
val("thatch", sib=sx("thatch", "gv"))
val("plaid", sib=sx("plaid", "kleiner-perkins"), flags=["model_disputes_source"])
val("multiverse", sib=sx("multiverse", "gv"))
val("discord", sib=sx("discord", "ivp"), flags=["stale"])
val("patreon", sib=sx("patreon", "thrive-capital"), flags=["stale"])
val("gong", sib=sx("gong", "thrive-capital"))
val("safetyculture", sib=sx("safetyculture", "tiger-global-management"))
val("instabase", sib=sx("instabase", "new-enterprise-associates"), flags=["model_disputes_source"],
    note="$100M Series D in January 2025 at $1.24B (TechCrunch, 2025-01-17), below the $2B of 2023: the newer priced round is the mark")
val("productboard", sib=sx("productboard", "kleiner-perkins"), flags=["stale"])
val("spendesk", sib=sx("spendesk", "tiger-global-management"), flags=["stale"])
val("swile", sib=sx("swile", "headline"), flags=["stale"])
val("ankorstore", sib=sx("ankorstore", "tcv"), flags=["stale"])
val("pilot", 1.2e9, nqurl('"Pilot" bookkeeping startup $1.2 billion valuation Bezos Expeditions', "Pilot's Valuation Soars To $1.2 Billion"), "2021-03-26", flags=["stale"])
val("motive", 2.85e9, nqurl('"Motive" $2.85 billion valuation Series F', "Motive raises valuation to $2.85B after closing $150M funding round"), "2022-05-25", flags=["stale"],
    note="September 2026: $1.3B of growth financing from General Catalyst and the IPO filing withdrawn (Business Wire, 2026-09-10); no new valuation given, so the 2022 mark stands")
val("taxfix", 1.0e9, nqurl('"Taxfix" $1 billion valuation 2022 unicorn', "joining the unicorn club with $220 million funding"), "2022-04-28", flags=["stale"])
val("rohlik", 1.2e9, nqurl('"Rohlik" unicorn valuation 2021 OR 2024 raises', "raises $119m to join unicorn club"), "2021-07-01", flags=["stale"],
    note="Reuters reported it 'valued at nearly $2 billion' from a document in December 2024; no priced round gives a figure, so the 2021 mark stands")
val("iterable", 2.0e9, nqurl('"Iterable" $2 billion valuation Series E 2021', "Iterable Announces $2 Billion Valuation"), "2021-06-15", flags=["stale"])
val("applyboard-inc", 3.2e9, nqurl('"ApplyBoard" valuation $3.2 billion OR "C$4 billion" 2021', "ApplyBoard Triples Valuation To $3.2 Billion"), "2021-06-15", flags=["stale"])
# ---- flags the attack search closes without a change
for s, why in (("physical-intelligence", None), ("oratomic", None), ("brinc", None), ("sublime-security", None), ("twelve-labs", None)):
    L.append(cls(s, clear=["needs_web_value"], flags=["cite_pending"] if s == "physical-intelligence" else ()))
# ---- entry-stage provenance on $1B+ rows
L.append(cls("kong", stage="Seed", stage_src="first_party", stage_cite="https://www.indexventures.com/companies/", stage_conf="medium", clear=["stage_uncited"]))
L.append(cls("algolia", flags=["cite_pending"]))
u = post("solving-the-ai-reasoning-gap")
L.append(cls("harmonic", stage="Series A", stage_src="web_verified", stage_cite=u, stage_conf="medium", entry_date="2024-09"))
L.append(cls("class-companion", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"]))
L.append(cls("ideogram-ai", stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"]))
L.append(cls("acutus-medical", rng="below_1b"))
# ---- rule 6: the country of every non-US $1B+ row cited (the firm's own archived page, a sibling's citation, or a headline)
def hq(slug): return [e for e in FACTS[slug]["hq"]][0]["capture_url"]
def sc(slug, inv, skey=None):
    c = json.loads((H.parents[1] / inv / "companies" / "classification.json").read_text()).get(skey or slug) or {}
    u = c.get("hq_country_citation")
    if not str(u or "").startswith("http"): gl.ERRORS.append(f"sc({slug}, {inv})"); return "MISSING"
    return u
CC = {"alan": hq("alan"), "beamery": hq("beamery"), "culture-amp": hq("culture-amp"), "kry-livi": hq("kry-livi"), "revolut": hq("revolut"),
      "datasnipper": sc("datasnipper", "insight-partners"), "linktree": sc("linktree", "20vc"), "mistral": sc("mistral", "headline"),
      "motorway": sc("motorway", "iconiq-growth"), "multiverse": nws("Multiverse", "Edtech unicorn Multiverse raises £50m") if "Multiverse" in NEWS else abn("multiverse", "Edtech unicorn Multiverse raises £50m"),
      "wonderful": sc("wonderful", "ivp"), "deepl": sc("deepl", "bessemer-venture-partners"), "elastic": nws("Elastic", "Elastic, a Dutch software startup"),
      "glow": abn("glow", "Israeli startup Glow raises $180m"), "granola": abn("granola", "becomes latest UK unicorn after fundraising"),
      "ineffable": nqurl('"Ineffable Intelligence" seed Index Ventures', "for London AI startup Ineffable Intelligence")}
for s, u in CC.items():
    L.append({"slug": s, "who": jl.WHO, "hq_country_citation": u})
for s in ("gruppo-mutuionline", "ozon-ru", "cohere"):
    pass
print(len(L), "lines")
gl.write("ab-pass", L)
