"""Post-rebuild delta: the 69 recall additions (the e.ventures logo wall, the press sweep,
Deposit Solutions) and two merged rows. Identity, status and rounds come from the four
logo research packets (scratch/research/recall-*.json; quotes verified) and the press
sweep; each row keeps its researched rounds under funding_rounds."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402
from research_lib import usd  # noqa: E402

H = Path(__file__).resolve().parents[1]
R = {}
for n in (1, 2, 3, 4):
    for r in json.loads((H / "scratch" / "research" / f"recall-{n}.json").read_text()):
        if r.get("logo"):
            R[r["logo"]] = r
src = (H / "scratch" / "recall-write.py").read_text()
HOME = eval(src[src.index("HOME = {") + 7:src.index("}\nALSO") + 1])
S2L = {v[0]: k for k, v in HOME.items()}

def rounds(slug):
    r = R[S2L[slug]]
    out = []
    for x in r.get("rounds") or []:
        st = x.get("source_type") if x.get("source_type") in ("firm", "company", "press", "filing") else "press"
        out.append({"date": x.get("date"), "round": x.get("round"), "amount_usd": usd(x.get("amount"), x.get("currency"), x.get("date") or ""),
                    "lead": x.get("lead"), "firm_in_round": x.get("firm_in_round"), "source": x.get("url"), "source_type": st})
    return out
def ent(slug): return R[S2L[slug]].get("entry") or {}
def rurl(slug, word):
    return [x["url"] for x in R[S2L[slug]]["rounds"] if word.lower() in (x.get("round") or "").lower() or word in (x.get("date") or "")][0]
def note(slug, extra=""):
    r = R[S2L[slug]]
    return (f"{r.get('company')}: {r.get('description') or ''} Status: {r.get('status_detail') or r.get('status')}. {extra} "
            f"Recall addition from the e.ventures logo wall (decisions.md R6); desk {r.get('desk')}.").replace("  ", " ").strip()

# slug: (status, country, city, stage, how, grad, focus, extra-note)   how: W=web_verified entry, M=model medium, U=undetermined
T = {
 "backops": ("acquired", "US", "San Francisco", "Series A", "W", None, "SaaS", "Merged into the founder's Scalus in 2016."),
 "causebox": ("acquired", "US", "Los Angeles", "undetermined", "U", None, "Consumer & Marketplaces", "Shut in April 2022 and taken over by new owners (acquired out of shutdown)."),
 "everything-but-the-house": ("private", "US", "Cincinnati", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "friendbuy": ("private", "US", "San Francisco", "undetermined", "U", None, "SaaS", "BV Capital's February 2012 portfolio page lists it."),
 "gettacar": ("defunct", "US", "Philadelphia", "Seed", "M", "grad:2021-02", "Consumer & Marketplaces", "The quoted 'Seed A' is the firm's seed entry; the $25M 2021 round clears the step-up."),
 "hashgo": ("unknown", "US", "San Francisco", "undetermined", "U", None, "Media, Gaming & Advertising", "The company's site names e.ventures as an investor without the round."),
 "huckleberry": ("acquired", "US", "San Francisco", "undetermined", "U", None, "Fintech & Payments", "Ownership by Paychex reported only by Coverager (2023)."),
 "jw-player": ("acquired", "US", "New York", "Growth", "W", None, "Media, Gaming & Advertising", "Merged with Connatix in October 2024 (JWP Connatix): acquired with a successor note."),
 "lastline": ("acquired", "US", "Redwood City", "Growth", "W", None, "Security", ""),
 "layer": ("defunct", "US", "San Francisco", "Seed", "W", "grad:Series A", "DevTools & APIs", ""),
 "mighty-networks": ("private", "US", "Palo Alto", "undetermined", "U", None, "SaaS", "Formerly Mightybell."),
 "mira": ("acquired", "US", None, "Seed", "W", "term", "Consumer & Marketplaces", ""),
 "nativo": ("acquired", "US", "El Segundo", "Series A", "W", None, "Media, Gaming & Advertising", ""),
 "openbucks": ("acquired", "US", None, "Series A", "W", None, "Fintech & Payments", ""),
 "pie-insurance": ("private", "US", "Washington", "undetermined", "U", None, "Fintech & Payments", "Series D $315M (2022) with no valuation disclosed (TechCrunch)."),
 "plain-vanilla-games": ("acquired", "IS", "Reykjavik", "Series A", "M", None, "Media, Gaming & Advertising", "The firm entered the November 2013 extension of the April 2013 Series A."),
 "plated": ("acquired", "US", "New York", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "playbook": ("private", "US", None, "Series A", "W", None, "Consumer & Marketplaces", "e.ventures led the $9.3M Series A (October 2020); Porsche Ventures co-invested (decisions.md D5 does not reach a round the firm led)."),
 "playhaven": ("acquired", "US", "San Francisco", "Growth", "W", None, "Media, Gaming & Advertising", "Merged with Kontagent into Upsight (December 2013)."),
 "pulse": ("acquired", "US", "Palo Alto", "undetermined", "U", None, "Media, Gaming & Advertising", "The BG country pre-fill is a wrong join."),
 "saatchi-art": ("acquired", "US", "Los Angeles", "undetermined", "U", None, "Consumer & Marketplaces", "BV eVenture Fund II, LP is among the selling stockholders in Demand Media's 2014 S-3."),
 "spothero": ("private", "US", "Chicago", "Seed", "W", "grad:Series B", "Consumer & Marketplaces", "Uber agreed to acquire SpotHero (2026-02-23, Uber investor relations); no close confirmed, so private until it closes."),
 "stackshare": ("acquired", "US", "San Francisco", "Series A", "W", None, "DevTools & APIs", ""),
 "streamlabs": ("acquired", "US", "San Francisco", "undetermined", "U", None, "Media, Gaming & Advertising", ""),
 "stylesaint": ("unknown", "US", "New York", "Series A", "W", None, "Consumer & Marketplaces", ""),
 "tonebase": ("private", "US", "Los Angeles", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "trippy": ("private", "US", None, "Series A", "W", None, "Consumer & Marketplaces", ""),
 "vulcun": ("defunct", "US", None, "undetermined", "U", None, "Media, Gaming & Advertising", ""),
 "solid": ("defunct", "US", "Palo Alto", "Series A", "W", None, "Fintech & Payments", "Formerly Wise; Chapter 11 (subchapter V) in April 2025 reads defunct."),
 "wonderschool": ("private", "US", "San Francisco", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "asap54": ("defunct", "GB", "London", "Seed", "W", None, "Consumer & Marketplaces", ""),
 "auctionata": ("defunct", "DE", "Berlin", "Seed", "W", "grad:Series A", "Consumer & Marketplaces", ""),
 "cornerjob": ("unknown", "ES", "Barcelona", "Growth", "W", None, "Consumer & Marketplaces", ""),
 "cuponation": ("private", "DE", "Munich", "Seed", "W", None, "Consumer & Marketplaces", "As DropGifts (Rocket Internet, Berlin), pivoted into CupoNation, now Global Savings Group; the investors' pages, e.ventures' included, swapped the DropGifts logo for CupoNation's (deutsche-startups 2013-11-18)."),
 "deadhappy": ("defunct", "GB", "Leicester", "Series A", "W", None, "Fintech & Payments", ""),
 "deltamethod": ("acquired", "DE", "Berlin", "Series A", "M", None, "SaaS", "The unnamed mid-seven-figure EUR round of July 2014, the firm's first, sits in the Series A band."),
 "fight-my-monster": ("defunct", "GB", "London", "Seed", "W", None, "Media, Gaming & Advertising", ""),
 "flux": ("defunct", "GB", "London", "Series A", "W", None, "Fintech & Payments", "The public CZ pre-fill is a wrong join."),
 "futrli": ("acquired", "GB", "Bournemouth", "Series A", "W", None, "SaaS", ""),
 "kenbi": ("defunct", "DE", "Berlin", "Seed", "W", "grad:Series A", "Healthcare & Bio", ""),
 "layerise": ("unknown", "DK", "Copenhagen", "undetermined", "U", None, "SaaS", ""),
 "mydeco": ("defunct", "GB", "London", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "paykey": ("unknown", "IL", "Tel Aviv", "undetermined", "U", None, "Fintech & Payments", ""),
 "tvsmiles": ("unknown", "DE", "Berlin", "Series A", "W", None, "Media, Gaming & Advertising", ""),
 "verse": ("acquired", "ES", "Barcelona", "Series A", "W", None, "Fintech & Payments", ""),
 "wine-in-black": ("acquired", "DE", "Berlin", "Seed", "W", "grad:Series A", "Consumer & Marketplaces", ""),
 "mapia": ("private", "UA", "Kyiv", "Seed", "W", None, "Consumer & Marketplaces", "Held through eVenture Capital Partners, Hamburg (decisions.md R5)."),
 "sapato": ("acquired", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", "acq. by Ozon, February 2012 (Ozon is the consideration, not a member); eVenture Capital Partners a backer before the November 2010 round (R5)."),
 "heverest": ("defunct", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "lokata": ("defunct", "RU", "Moscow", "Series A", "M", None, "Media, Gaming & Advertising", "The firm's first round, the unlabelled several-million-EUR follow-on of September 2012, sits in the Series A band."),
 "domgeo": ("defunct", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "pinme": ("unknown", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "onlinetours": ("private", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "carprice": ("private", "RU", "Moscow", "Seed", "W", "grad:Series B", "Consumer & Marketplaces", "Seized by the Russian state in 2026 and still operating."),
 "teamo": ("acquired", "RU", "Moscow", "undetermined", "U", None, "Consumer & Marketplaces", ""),
 "admoment": ("unknown", "RU", "Moscow", "Seed", "M", None, "Media, Gaming & Advertising", "Backed by the firm from its creation (seed, unlabelled)."),
 "bird": ("acquired", "US", "Miami", "Growth", "W", None, "Consumer & Marketplaces", "SPAC listing (NYSE: BRDS) 2021, Chapter 11 December 2023, assets bought by Third Lane Mobility (2024): acquired out of insolvency. The NL country pre-fill is a wrong join."),
 "bright-health": ("acquired", "US", "Minneapolis", "Growth", "W", None, "Healthcare & Bio", "e.ventures Growth II, L.P. signed the Series C registration rights agreement (S-1 exhibit, 2018-11-15). IPO 2021 as Bright Health Group, renamed NeueHealth, taken private by NEA (October 2025)."),
 "unbabel": ("acquired", "PT", "Lisbon", "Growth", "W", None, "AI & Applied AI", "acq. by TransPerfect, August 2025. The US country pre-fill is a wrong join."),
}
PRESS = {
 "ahara": dict(status="private", country="US", city="Los Angeles", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite="https://labusinessjournal.com/healthcare/wellness/ahara-garners-10-8-million/", entry_date="2023-07", focus="Healthcare & Bio"),
 "all-def-digital": dict(status="unknown", country="US", city="Los Angeles", stage="undetermined", focus="Media, Gaming & Advertising"),
 "candid": dict(status="defunct", country="US", city="New York", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2017-11", focus="Healthcare & Bio"),
 "deposit-solutions": dict(status="acquired", country="DE", city="Hamburg", stage="undetermined", focus="Fintech & Payments"),
 "exporo": dict(status="private", country="DE", city="Hamburg", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2016-07", focus="Fintech & Payments"),
 "flowhub": dict(status="private", country="US", city="Denver", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2021-10", focus="SaaS"),
 "soldsie": dict(status="unknown", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite="https://betakit.com/soldsie-raises-1m-to-let-merchants-sell-through-facebook-comments/", entry_date="2013-03", focus="SaaS"),
 "test-ai": dict(status="unknown", country="US", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite="https://www.prnewswire.com/news-releases/testai-raises-11m-series-a-to-test-every-app-in-the-world-300689694.html", entry_date="2018-07", focus="DevTools & APIs"),
 "the-young-turks": dict(status="private", country="US", city="Los Angeles", stage="Growth", stage_src="model", stage_conf="medium", entry_date="2017-08", focus="Media, Gaming & Advertising"),
 "zeller": dict(status="private", country="AU", city="Melbourne", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite="https://www.itnews.com.au/news/aussie-fintech-zeller-closes-100m-series-b-reaches-1billion-valuation-576855", entry_date="2022-03", focus="Fintech & Payments"),
}
PNOTE = {
 "ahara": "Ahara (Century City, Los Angeles), personalised nutrition: $10.8M seed led by Greycroft with Headline (July 2023). Recall addition (press sweep).",
 "all-def-digital": "All Def Digital (Russell Simmons' media company, Los Angeles): e.ventures was a previous investor at the $10M round of June 2016 (Variety), so its entry, probably the earlier $5M Series A, is not named. Recall addition (press sweep).",
 "candid": "Candid (clear aligners, New York): $15M from Greycroft, Bessemer, e.ventures and Arena (November 2017), its first round after about $2M: Series A by sequence. Shut down in December 2024. Recall addition (press sweep).",
 "deposit-solutions": "Deposit Solutions (Hamburg, open banking deposits; founded 2011 as Comonea): e.ventures in the EUR 15M round of July 2016 and the $100M round of August 2018 (at a $500M valuation); the firm's CMS dates its entry 2012 (unnamed). Merged into Raisin, June 2021 (decisions.md R2).",
 "exporo": "Exporo (Hamburg, real-estate crowdinvesting): EUR 8.2M Series A (July 2016, FinSMEs), e.ventures named a previous investor at the EUR 43M round of June 2019 (Hamburg Business). Recall addition (press sweep).",
 "flowhub": "Flowhub (Denver, cannabis retail software): $19M strategic round led by Headline, Poseidon and Shawn Carter (October 2021), after an earlier Series A: Growth by sequence. Recall addition (press sweep).",
 "soldsie": "Soldsie (social commerce): $1M seed from 500 Startups, e.ventures and FundersClub (March 2013). Recall addition (press sweep).",
 "test-ai": "Test.ai (formerly Appdiff; AI app testing): $11M Series A led by Gradient Ventures with e.ventures (July 2018). Recall addition (press sweep and the logo wall).",
 "the-young-turks": "The Young Turks (TYT Network, Los Angeles): $20M round led by 3L Capital with Greycroft, e.ventures and WndrCo (August 2017), after a 2014 raise: Growth by sequence. Recall addition (press sweep).",
 "zeller": "Zeller (Melbourne payments): A$100M Series B led by Headline and Hostplus at an A$1B valuation (March 2022); AUD 1.00B @ ECB 2022-03-02 (AUD/EUR 1.5272, EUR/USD 1.1106) = $727.2M. Recall addition (press sweep).",
}
L = []
for slug, (st, co, ci, stg, how, grad, focus, extra) in T.items():
    e = ent(slug)
    kw = dict(status=st, country=co, country_src="web_verified" if co != "US" else "model_knowledge", rng="below_1b", focus=focus, focus_src="model",
              rounds=rounds(slug), note=note(slug, extra))
    if co != "US":
        kw["country_cite"] = e.get("url") or R[S2L[slug]].get("status_url")
        if not kw["country_cite"]:
            kw["country_src"] = "model_knowledge"
    if ci:
        kw["city"] = ci
    else:
        kw["flags"] = ["city_unknown"]
    if how == "W":
        kw.update(stage=stg, stage_src="web_verified", stage_conf="high", stage_cite=e["url"], entry_date=str(e.get("date") or "")[:10] or None)
    elif how == "M":
        kw.update(stage=stg, stage_src="model", stage_conf="medium", entry_date=str(e.get("date") or "")[:10] or None)
    else:
        kw.update(stage="undetermined")
    if kw.get("entry_date") is None:
        kw.pop("entry_date", None)
    if grad and grad.startswith("grad:"):
        kw.update(grad="graduated", grad_src="web_verified", grad_cite=rurl(slug, grad[5:]))
    if slug in ("flux", "pulse", "bird", "unbabel"):
        kw["flags"] = sorted(set(kw.get("flags", [])) | {"model_disputes_source"})
        kw["extra"] = {"valuation_source": "model_knowledge", "valuation_range_source": "model_knowledge", "valuation_usd": None, "valuation_asof": None}
    L.append(cls(slug, **kw))
for slug, kw in PRESS.items():
    L.append(cls(slug, rng="below_1b", focus_src="model", note=PNOTE[slug], **kw))
if __name__ == "__main__":
    write("delta-001", L, record="--dry" not in sys.argv)
