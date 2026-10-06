"""PRO-82 graduation pass (COLLECTION.md s6, PRO-132): every Seed entry decided. Citations are read from files on disk
(the surfaces file, the news files, the firm's posts, sibling rows, scratch/web-finds.json), never typed.
Patch lines carry no note; the later round goes into funding_rounds beside what the grind stored.
Entry dates of label rows (decisions.md R1): the seed's own dated announcement where one is on disk, a sibling's cited
entry for the same round, else the year the firm first lists the company (an upper bound, said so in decisions.md)."""
import importlib.util, json, re
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
jl = gl.jl
post, narch, sib, news, nqurl, gs, arch, rnd, cls = gl.post, gl.narch, gl.sib, gl.news, gl.nqurl, gl.gsurl, gl.arch, gl.rnd, jl.cls
G = json.loads((H / "graduation-surfaces.json").read_text())
CL = json.loads((H.parent / "companies" / "classification.json").read_text())
WEB = json.loads((H / "web-finds.json").read_text())
FD = json.loads((H / "formd-lookup.json").read_text())
web = lambda k: WEB[k]["url"]
def gsib(slug, investor, key):
    """A sibling book's citation for the same company, read from the surfaces file (graduation_citation / entry_stage_citation)."""
    for sb in G[slug].get("siblings") or []:
        if sb["investor"] == investor and str(sb.get(key) or "").startswith("http"):
            return sb[key]
    gl.ERRORS.append(f"gsib({slug}, {investor}, {key})"); return "MISSING"
L = []

def rounds(slug, *new):
    old = list((CL.get(slug) or {}).get("funding_rounds") or [])
    have = {(r.get("date"), r.get("round")) for r in old}
    return old + [r for r in new if (r["date"], r["round"]) not in have]

def yes(slug, src, cite, entry=None, later=None, **kw):
    """graduated on a cited later round; `later` = (date, round, amount_usd, lead, source_type)."""
    k = dict(grad="graduated", grad_src=src, grad_cite=cite)
    if entry: k["entry_date"] = entry
    if later: k["rounds"] = rounds(slug, rnd(later[0], later[1], later[2], later[3], None, cite, later[4] if len(later) > 4 else "press"))
    k.update(kw)
    L.append(cls(slug, **k))

LATER = re.compile(r"series [a-f]\b|rais|fund|secure|lands|closes|acqui|shut|bought|buys|sold|merge|lève|\$\d|€\d|£\d", re.I)
FIRM = "firm: the company page on indexventures.com, the Perspectives archive (586 posts to 2026-09-30) and the firm's archived news 2002-2019 for {n} -> {f}"
TABLE = "EDGAR's entity-name table (cik-lookup-data.txt, 2026-08-10) for {q}"
def formd_none(*names):
    assert all(n in FD and not FD[n]["entities"] for n in names), names
    return "formd: " + TABLE.format(q=" / ".join(f"'{n}'" for n in names)) + " -> no filer under the company's name, so no Form D sequence"
def surf(slug, firm, formd=None, shows=None, extra=()):
    e = G[slug]; name = (e.get("query_name") or e["name"])
    out = [FIRM.format(n=e["name"], f=firm)]
    if formd: out.append(formd)
    for sn, sf in sorted(e["surfaces"].items()):
        assert sf["status"] == "ok", (slug, sn)
        its = sf.get("items", [])
        named = [i for i in its if name.lower() in i.get("title", "").lower()]
        if shows:
            out.append(f"{sn}: {sf['query']} -> {sf.get('n', len(its))} items; {shows}")
            continue
        fund = sorted([i for i in named if LATER.search(i["title"])], key=lambda i: i.get("date") or "")[-2:]
        out.append(f"{sn}: {sf['query']} -> {sf.get('n', len(its))} items, {len(named)} naming the company; "
                   + ("; ".join(f"{i.get('date')} {i['title'][:75]}" for i in fund) + "; none names a later round" if fund else "no headline naming a later round"))
    for sb in e.get("siblings") or []:
        if sb.get("seed_to_a_graduation"):
            out.append(f"sibling:{sb['investor']}: its row for {sb.get('name')} -> S2A {sb['seed_to_a_graduation']} ({sb.get('graduation_source')}), entry {sb.get('entry_date')}")
    return out + list(extra)
def no(slug, surfaces, src="absence_check", cite=None, entry=None, **kw):
    k = dict(grad="not_graduated", grad_src=src, grad_asof=G[slug]["asof"], surfaces=surfaces)
    if cite: k["grad_cite"] = cite
    if entry: k["entry_date"] = entry
    k.update(kw)
    L.append(cls(slug, **k))

# ---------------- graduated: a cited later round ----------------
yes("adzuna", "web_verified", gs("adzuna", "Series C from Smedvig"), entry="2012", later=("2018-05-18", "Series C", None, "Smedvig Capital"))
u = gs("argent", "raises $4M from Euro VCs")
yes("argent", "web_verified", gs("argent", "raises $40m Series B to build Web3"), entry="2018-11", later=("2022-05-03", "Series B", 40000000, None),
    rounds=rounds("argent", rnd("2018-11-20", "Seed", 4000000, None, True, u, "press")))
yes("cartesia", "web_verified", gs("cartesia", "Advises Cartesia in US$64 Million Series A"), entry="2024-12", later=("2025-03-11", "Series A", 64000000, "Kleiner Perkins"))
yes("citymapper", "web_verified", gs("citymapper", "CityMapper Raises $40M in Series B"), entry="2014", later=("2016-01-23", "Series B", 40000000, "Index Ventures"))
yes("common-room", "web_verified", gs("common-room", "Launches With $52 Million In Funding"), entry="2020", later=("2021-03-31", "Series A and Series B (announced together with the seed)", 52000000, None))
yes("cowboy", "first_party", post("cowboy-the-electric-bike-start-up-raises"), entry="2017", later=("2018-10-23", "Series A", None, "Tiger Global", "firm"))
yes("creative-juice", "web_verified", gs("creative-juice", "flowing with a $15 million Series A"), entry="2021", later=("2022-04-05", "Series A", 15000000, None))
yes("double", "web_verified", gs("double", "Double Raises Series A To Grow Flexible Assistant Platform"), entry="2019", later=("2021-10-26", "Series A", None, None))
u = post("duffel-raises-215m")
yes("duffel", "first_party", u, entry="2018", later=("2019-06-18", "Series A", 21500000, "Benchmark", "firm"),
    stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high")
yes("duna", "first_party", post("duna-built-by"), entry="2025-05", later=("2026-02-05", "Series A", None, "CapitalG", "firm"))
u = web("eisen-funding")
yes("eisen", "web_verified", gs("eisen", "Eisen Raises $10M in Series A"), entry="2026", later=("2026-05-19", "Series A", 10000000, "MissionOG"),
    stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high",
    rounds=rounds("eisen", rnd(None, "Seed", 8500000, "Index Ventures", True, u, "company"), rnd("2026-05-19", "Series A", 10000000, "MissionOG", None, u, "company")))
yes("goody", "web_verified", gsib("goody", "new-enterprise-associates", "entry_stage_citation"), entry="2021", later=("2021-11-16", "Series A", 15000000, "SoftBank"))
yes("lightning-ai", "web_verified", gsib("lightning-ai", "bain-capital-ventures", "graduation_citation"), entry="2020", later=("2022-06", "Series B", 40000000, None))
yes("hutch-games", "web_verified", gs("hutch-games", "Index-backed Hutch puts $5.5M"), entry="2014", later=("2017-02-02", "undisclosed", 5500000, None))
yes("immersive-gamebox", "web_verified", gsib("immersive-gamebox", "project-a-ventures", "entry_stage_citation"), entry="2019", later=("2021-06-11", "Series A follow-on", None, None))
yes("lever", "web_verified", gs("lever", "Lever Raises $50 Million in Series D"), entry="2014", later=("2021-11-01", "Series D", 50000000, None))
yes("linear", "web_verified", gsib("linear", "sequoia-capital", "graduation_citation"), entry="2019-11", later=("2023-09-14", "Series B", 35000000, "Accel"))
yes("lithic", "web_verified", gs("lithic", "Closes $43 Million in Series B Round"), entry="2020", later=("2021-05-20", "Series B", 43000000, "Bessemer Venture Partners"))
yes("nacelle", "web_verified", gs("nacelle", "closes $18M Series A"), entry="2020", later=("2021-01-12", "Series A", 18000000, None))
yes("newfront", "web_verified", gs("newfront", "Hits $2.2 Billion Valuation in Latest Funding Round"), entry="2020", later=("2022-04-12", "undisclosed", 200000000, "Goldman Sachs Asset Management, B Capital"))
yes("nuvo", "web_verified", nqurl('"Nuvo" seed Index Ventures B2B trade', "nabbed $34M from Sequoia and Spark Capital"), entry="2025", later=("2025-04-30", "Series A", 34000000, "Sequoia, Spark Capital"))
u = post("peanut-leading-social-network")
yes("peanut", "web_verified", gs("peanut", "Mishcon de Reya advises"), entry="2019-11", later=("2020-05-13", "Series A", 12000000, "EQT Ventures"),
    rounds=rounds("peanut", rnd("2019-11-14", "undisclosed", 5000000, "Index Ventures", True, u, "firm")))
yes("roli", "web_verified", gs("roli", "raises $27 million in Series B led by Foundry"), entry="2014", later=("2016-05-04", "Series B", 27000000, "Foundry Group"))
yes("scoop", "first_party", post("scoop-announces"), entry="2016", later=("2017-11-09", "Series A (Index led; announced with the Series B)", 11000000, "Index Ventures", "firm"))
yes("second-home", "web_verified", gs("second-home", "Has Raised £7.5 Million"), entry="2014", later=("2016-01-18", "undisclosed", None, None))
yes("stytch", "web_verified", gs("stytch", "Stytch Raises $30 Million in Series A Led by Thrive"), entry="2020", later=("2021-07-14", "Series A", 30000000, "Thrive Capital"))
yes("supersolid", "first_party", post("supersolid-raises-4-million-series-a"), entry="2014", later=("2017-10-12", "Series A", 4000000, "Index Ventures", "firm"))
yes("tiney", "web_verified", gs("tiney", "raises €8.3 million Series A"), entry="2022", later=("2024-05-13", "Series A", None, None))
yes("wise", "first_party", narch("$6 million investment round in London start-up"), entry="2012", later=("2013-05-15", "undisclosed", 6000000, "Valar Ventures", "firm"))
u = gs("twelve-labs", "propelled by $5M seed round")
yes("twelve-labs", "web_verified", gs("twelve-labs", "Earns $50 Million Series A"), entry="2022-03", later=("2024-06-04", "Series A", 50000000, "NEA, NVentures"),
    stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high",
    rounds=rounds("twelve-labs", rnd("2022-03-16", "Seed", 5000000, "Index Ventures", True, u, "press")))
yes("wetravel", "web_verified", gs("wetravel", "raises $27m in Series B"), entry="2023", later=("2025-03-29", "Series B", 27000000, None))
yes("edited", "web_verified", news("Edited", "Edited Raises $29M In New Round Led By Wavecrest"), entry="2012", later=("2020-04-15", "undisclosed", 29000000, "Wavecrest Growth, Beringea"),
    stage="Seed", stage_src="first_party", stage_cite=arch("edited", "stage_filter", "Seed stage"), stage_conf="low")
yes("bigger-games", "web_verified", gs("bigger-games", "secures $25m in Series A"), later=("2025-06-17", "Series A", 25000000, None))
yes("sanlo", "web_verified", gs("sanlo", "raises $10M"), later=("2022-06-02", "undisclosed", 10000000, None))
yes("the-business-of-fashion", "web_verified", gs("the-business-of-fashion", "SERIES B INVESTMENT IN BUSINESS OF FASHION"), later=("2019-09-20", "Series B", None, "Financial Times"))
yes("tofu", "web_verified", nqurl('"Tofu" B2B marketing AI raises $12M', "Tofu Raises $12M Series A"), later=("2025-02-13", "Series A", 12000000, None))
yes("albert", "web_verified", gs("albert", "Announces $22.5 Million Series A"), later=("2024-12-11", "Series A", 22500000, "Coatue"))
yes("algolia", "web_verified", gsib("algolia", "point-nine", "graduation_citation"), later=("2015-05", "Series A", 18300000, "Accel"))
yes("captain-train", "web_verified", web("captain-train-2014"), later=("2014-12-02", "undisclosed", 6300000, "Alven Capital"))
yes("fast", "web_verified", gs("fast", "$102 Million in Series B"), later=("2021-01-26", "Series B", 102000000, "Stripe"))
yes("ideogram-ai", "web_verified", gsib("ideogram-ai", "a16z", "graduation_citation"), later=("2024-02", "Series A", 80000000, "Andreessen Horowitz"))
yes("move-loot", "web_verified", gsib("move-loot", "gv", "graduation_citation"), later=("2015-02-12", "Series A", 9000000, "Index Ventures"))
yes("thread-ai", "web_verified", gs("thread-ai", "Secures $20M Series A"), later=("2025-06-05", "Series A", 20000000, None))
yes("venice", "web_verified", gs("venice", "raises $25 million Series A for Venice"), later=("2026-02-18", "Series A", 25000000, "IVP"))
u = web("marvel-series-a")
yes("marvel", "web_verified", u, later=("2016-12-08", "Series A", None, "BGF Ventures"),
    stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="medium", clear=["stage_uncited"])
u = web("abes-market-series-a")
yes("abe-s-market", "web_verified", u, entry="2010", later=("2011-02-10", "Series A", 3400000, "Accel"),
    stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="medium")

# ---------------- not graduated: a cited end (acquired or shut before any later round) ----------------
END = "the seed is the last round the firm records before the {e}"
no("adaptive-ml", surf("adaptive-ml", END.format(e="sale to Datadog (2026-06-30)")), "web_verified", gs("adaptive-ml", "Datadog Acquires Adaptive ML to Accelerate"))
no("apex", surf("apex", END.format(e="sale to Tenable (2025-05)"), shows="the $7M seed of May 2024 and the sale to Tenable; the Series A and C headlines are Apex the satellite maker and Apex Fintech, other companies"),
   "web_verified", gsib("apex", "sequoia-capital", "graduation_citation"))
no("atlantic-money", surf("atlantic-money", END.format(e="sale to Deel (2024-12)")), "web_verified", gs("atlantic-money", "Deel Acquires Atlantic Money for Undisclosed Sum"), entry="2022-03")
no("class-companion", surf("class-companion", END.format(e="sale to Panorama Education (2025-04)"), formd=formd_none("Class Companion")),
   "web_verified", gs("class-companion", "Panorama Education Acquires Class Companion"))
no("otterize", surf("otterize", END.format(e="sale to Cyera (2025-06)")), "web_verified", gs("otterize", "Cyera acquires Otterize"))
no("dija", surf("dija", END.format(e="sale to Gopuff (2021-08), eight months after the seed")), "web_verified", gs("dija", "Gopuff Doubles Down on European Expansion With Acquisition of Dija"))
e8 = FD["8tracks"]["entities"][0]
no("8tracks", surf("8tracks", "listed 2012-2016; no post or news item names a round after the seed",
                   formd="formd: EDGAR filing index of 8tracks, Inc. (CIK %s) -> %s; no later priced round at twice the seed, then Regulation A filings from 2016" % (
                       e8["cik"], "; ".join(f"{f['date']} {f['form']} ${int(f['sold_usd']):,} sold of ${int(f['offering_usd']):,}" for f in e8["formd"]))),
   "web_verified", gs("8tracks", "8tracks Is Shutting Down"))
no("frontback", surf("frontback", "listed 2014-2016; no post names a round", formd=formd_none("Frontback")), "web_verified", gs("frontback", "Frontback Shutting Down After Attracting $4M"))
no("humanloop", surf("humanloop", "the firm's post of 2022-07-28 on the product launch; no later round named"), "web_verified",
   gs("humanloop", "Anthropic snapping up Humanloop team"), entry="2021")
no("the-gifts-project", surf("the-gifts-project", "on the 2012-2014 lists as an exit, tagged eBay"), "web_verified", gs("the-gifts-project", "eBay Buys The Gifts Project for $20 Million"), entry="2010")
u = gs("wool-and-the-gang", "Wool and the Gang sold to Lion Capital")
no("wool-and-the-gang", surf("wool-and-the-gang", "listed 2014-2015; no post names a round"), "web_verified", u,
   stage="Seed", stage_src="web_verified", stage_cite=gs("wool-and-the-gang", "Raises $2.8M Seed Round To Rethink Fashion"), stage_conf="medium", clear=["stage_uncited"],
   status="acquired", extra={"status_citation": u})

# ---------------- not graduated: the absence test ----------------
NONE = "no post or news item names a round after the seed"
no("atlar", surf("atlar", "the EUR 5M seed post of 2022-11-08 and nothing after it",
                 extra=["company: atlar.com/company (read 2026-10-06) -> 'backed by world-leading investors including Index Ventures and General Catalyst'; no round named",
                        "googlenews_note: Breakit 2024-04-23 reports a later round of SEK 90M (about $8.3M), unnamed in the headline and below twice the SEK 52M seed, so it does not graduate the row by the step-up test; only vendor databases call it a Series A (Rule A)"]))
no("brightgo", surf("brightgo", "the seed post of 2023-11-13 and nothing after it", formd=formd_none("BrightGo")))
no("catch", surf("catch", "listed 2022; no post names a round", formd=formd_none("Catch Commerce"),
                 shows="none about getcatch.com; the Series A headline of 2021-07-30 is Catch the benefits platform, another company"), entry="2022")
d = FD["Dahlia Labs"]["entities"][0]
no("daydream", surf("daydream", "the $50M seed post of 2024-06-20 and nothing after it",
                    formd="formd: EDGAR filing index of Dahlia Labs, Inc. (CIK %s), the company's legal name -> %s; both are the seed, no later filing" % (
                        d["cik"], "; ".join(f"{f['date']} D ${int(f['offering_usd']):,} (first sale {f['first_sale']})" for f in d["formd"])),
                    shows="the $50M seed of June 2024 only; the '$15M Series A' headlines of 2026-04 are daydream the SEO agency, another company"))
no("greg", surf("greg", "the $5m seed post of 2021-05-27 and nothing after it", formd=formd_none("Gregarious"), shows="none about the plant-care app (the name is a common first name)"))
no("hoop", surf("hoop", "the $5M seed post of 2024-06-05 and nothing after it", formd="formd: " + TABLE.format(q="'Hoop'") + " -> five filers of that name (a person, two sports venues, a real-estate issuer, a drinks maker), none the productivity app; no Form D sequence",
                shows="the $5M seed of 2024-06-05 only; the rest are basketball and unrelated companies"))
no("superlinked", surf("superlinked", "the $9.5M seed post of 2024-03-18 and nothing after it", formd=formd_none("Superlinked")))
t = FD["Tema ETFs"]["entities"][0]
no("tema", surf("tema", "the launch post of 2023-05 and nothing after it",
                formd="formd: " + TABLE.format(q="'Tema ETFs' / 'Tema Global'") + f" -> Tema ETFs LLC (CIK {t['cik']}) files as a fund adviser (13F-HR, 40-APP, N-PX) and has filed no Form D",
                shows="none about the ETF issuer's own financing (the headlines are the port city of Tema, Ghana)"))
no("solvo", surf("solvo", "the $3.5M seed post of 2022-09-29 and nothing after it", shows="none about solvo.finance; the headlines are Solvo the cloud-security company (sold to CYE, 2025) and Solvo.ai, other companies"))
no("upollo", surf("upollo", "listed with Mike Volpi; no post names a round"))
no("workbounce", surf("workbounce", "the $2.7M seed post of 2022-03-09 and nothing after it"))
no("worldover", surf("worldover", "the GBP 3M seed post of 2023-09-05 and nothing after it"))
no("tactic", surf("tactic", "listed 2023 with Jan Hammer; no post names a round", shows="none about tactic.fyi; the 2022-2023 headlines are Tactic the crypto-accounting company (sold to TaxBit), another company"), entry="2022-03")
no("hyperline", surf("hyperline", "the seed post of 2023-06-20 and the post of 2025-01-16, 'leading an additional $10m of seed funding': the later money is named seed"))
no("the-garden", surf("the-garden", "the launch post of 2022-07-13 (GBP 3M) and nothing after it", shows="none about the learning platform (the name is a common phrase)"))
no("fontself", surf("fontself", "on the 2010-2013 lists under the Seed stage filter; no news item names a round"), entry="2010")
no("geckoboard", surf("geckoboard", "on the 2012-2017 lists; no post names a round"), entry="2012-09",
   rounds=rounds("geckoboard", rnd("2012-09-28", "Seed", 1500000, None, True, gs("geckoboard", "Geckoboard Gets $1.5M From Top Investors"), "press")))
no("rjdj", surf("rjdj", "on the 2012-2013 lists under the Seed stage filter; no news item names a round"), entry="2012")
no("groupspaces", surf("groupspaces", "the firm's news item of 2010-07-01 on the $1.3M seed and nothing after it"))
no("futurelytics", surf("futurelytics", "on the 2014-2015 pages; no post names a round"))
no("loveshark", surf("loveshark", "on the 2021-2022 pages; no post names a round"))
no("sproutl", surf("sproutl", "on the 2022 page; no post names a round"))
no("beryl", surf("beryl", "listed as Blaze 2014-2016 and Beryl 2019-2020; no post names a round",
                 shows="Tech.eu 2023-02-20, 'Beryl raises GBP 2 million to open factory in Poole': unnamed and under the $5M bar for a 2014 seed; the rest are unrelated (a hurricane, a solar farm)"))
no("cruisewise", surf("cruisewise", "on the 2012 list under the Seed stage filter; no news item names a round", formd=formd_none("CruiseWise")), entry="2011")
no("amen", surf("amen", "on the 2012-2013 lists; no news item names a round", shows="none about the Berlin app (the name is a common word)"))

gl.write("graduation", L)
