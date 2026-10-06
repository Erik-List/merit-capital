"""PRO-82 delta after the one rebuild (571 rows): the 22 recall additions (decisions.md R3), the 1999-2002 Internet
Archive rows (R2: the fund's group in, the 'Prior investments' group out), and the two rows the rebuild resurfaced
(oxyplus-inc = NormOxys, life desk D3; opentest-inc = Loom's first legal name, T4). Citations come from files on disk:
the ledger's recall entries, scratch/web-finds.json, the surfaces file, sibling rows, archive-facts.json."""
import importlib.util, json, re
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, rnd, verdict, post, nqurl = gl.C, gl.rnd, gl.verdict, gl.post, gl.nqurl
WEB = json.loads((H / "web-finds.json").read_text()); web = lambda k: WEB[k]["url"]
LED = json.loads((H.parent / "companies/membership-ledger.json").read_text())["index-ventures"]
REC = {r["slug"]: r for r in LED["recall_additions"]}
G = json.loads((H / "graduation-surfaces.json").read_text())
IA = json.loads((H.parent / "sources/wayback/archive-facts.json").read_text())["ia"]
FD = json.loads((H / "formd-lookup.json").read_text())
def gsib(slug, investor, key):
    for sb in G[slug].get("siblings") or []:
        if sb["investor"] == investor and str(sb.get(key) or "").startswith("http"): return sb[key]
    gl.ERRORS.append(f"gsib({slug}, {investor}, {key})"); return "MISSING"
def gitem(slug, surface, sub):
    """The decoded link of a headline in the surfaces file."""
    hits = [i for i in G[slug]["surfaces"][surface].get("items", []) if sub.lower() in i.get("title", "").lower()]
    if not hits: gl.ERRORS.append(f"gitem({slug}, {surface}, {sub})"); return "MISSING"
    it = sorted(hits, key=lambda h: (not h.get("link"), h.get("date") or ""))[0]
    return it.get("link") or gl.gsurl(slug, sub)
def cap(slug, group=None):
    es = IA[slug].get("group") or IA[slug]["name"]
    if group: es = [e for e in es if e["value"] == group]
    return es[0]["capture_url"]
LATER = re.compile(r"series [a-f]\b|rais|fund|secure|lands|closes|acqui|shut|bought|buys|sold|merge|\$\d|€\d|£\d", re.I)
FIRM = "firm: the company page on indexventures.com, the Perspectives archive (586 posts to 2026-09-30) and the firm's archived news 2002-2019 for {n} -> {f}"
def surf(slug, firm, formd=None):
    e = G[slug]; name = (e.get("query_name") or e["name"])
    out = [FIRM.format(n=e["name"], f=firm)]
    if formd: out.append(formd)
    for sn, sf in sorted(e["surfaces"].items()):
        assert sf["status"] == "ok", (slug, sn)
        its = sf.get("items", []); named = [i for i in its if name.lower() in i.get("title", "").lower()]
        fund = sorted([i for i in named if LATER.search(i["title"])], key=lambda i: i.get("date") or "")[-2:]
        out.append(f"{sn}: {sf['query']} -> {sf.get('n', len(its))} items, {len(named)} naming the company; "
                   + ("; ".join(f"{i.get('date')} {i['title'][:75]}" for i in fund) + "; none names a later round that meets the rule" if fund else "no headline naming a later round"))
    return out
def formd_none(*names):
    assert all(n in FD and not FD[n]["entities"] for n in names), names
    return "formd: EDGAR's entity-name table (cik-lookup-data.txt, 2026-08-10) for " + " / ".join(f"'{n}'" for n in names) + " -> no filer under the company's name, so no Form D sequence"
ASOF = "2026-10-06"
L = []
def member(slug, ec="web", conf="high"):
    r = REC[slug]; L.append(verdict(slug, "member", "recall addition (decisions.md R3): " + r["basis"], ec=ec, conf=conf, cite=r["citation"]))

# ---- the 22 recall additions
member("instinct"); u = REC["instinct"]["citation"]; v = web("instinct-series-c")
L.append(C("instinct", dispute=("usd", "rng"), city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2026-08",
    rng="10b_plus", usd=10000000000, val_src="web_verified", val_cite=v, asof="2026-09-28", focus="AI & Applied AI",
    note="Personal AI agent that works by text and phone (Noah Shinn; Spear Street Technology Inc., registered in California in April 2026, reported as San Francisco); Index co-led the $250M Series B at $2.5B with Benchmark, announced 2026-08-26 (Tech Funding News), three weeks after Kleiner Perkins led the Series A; the $1B Series C at $10B closed on 2026-09-28 (the company's release, PYMNTS), the same mark Kleiner Perkins' row carries; not on the firm's list as read 2026-10-01; YC's Instinct (London) is another company",
    rounds=[rnd("2026-08", "Series A", 75000000, "Kleiner Perkins", False, u), rnd("2026-08-26", "Series B", 250000000, "Index Ventures and Benchmark", True, u), rnd("2026-09-28", "Series C", 1000000000, "Sequoia, Benchmark and Coatue", None, v)]))

member("uncovr"); u = REC["uncovr"]["citation"]
L.append(C("uncovr", status="private", country="FR", city="Paris", stage="Seed", stage_src="first_party", stage_conf="high", stage_cite=u, entry_date="2026-06", rng="below_1b",
    grad="censored", focus="Healthcare & Bio",
    note="Surgical AI: operative reports and coding from surgical video (Ines Iraki, Johann Diep, Prof. Eric Vibert; engineering in Paris, as Seedcamp's row has it); 'has raised $7 million in seed funding led by Index Ventures', with Seedcamp, Frst and Entrepreneurs First (the firm's post, 2026-06-10); inside the 24-month window",
    rounds=[rnd("2026-06-10", "Seed", 7000000, "Index Ventures", True, u, "firm")]))

member("less"); u = REC["less"]["citation"]
L.append(C("less", status="acquired", country="FR", city="Paris", stage="Series A", stage_src="first_party", stage_conf="high", stage_cite=u, entry_date="2017-11", rng="below_1b", focus="Consumer & Marketplaces",
    note="Real-time urban carpooling app from Criteo's founder Jean-Baptiste Rudelle (Paris); 'has secured 16 million Euros in its first round of fundraising (\"Series A\"). This round was led by Index Ventures and Daphni' (the firm's post, 2017-11-14; $18.8M at the ECB rate of the day), Dominique Vidal on the board; 'BlaBlaCar ... is acquiring Less' (TechCrunch, 2018-04-27)",
    rounds=[rnd("2017-11-14", "Series A", 18792000, "Index Ventures and Daphni", True, u, "firm")], extra={"status_citation": web("less-acquired")}))

member("cyngn", ec="fund_filing"); u = web("cyngn-ira")
L.append(C("cyngn", dispute=("usd",), country="US", city="Mountain View", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2014-12",
    rng="below_1b", usd=8770000, val_src="web_verified", val_cite=web("cap-cyn"), asof="2026-10-06", focus="Industrial & Robotics",
    note="Cyanogen Inc., the commercial Android distribution (Palo Alto and Seattle), renamed Cyngn in 2017 and rebuilt as an autonomous industrial vehicle company (Mountain View; NASDAQ: CYN, IPO October 2021); Index Ventures VII holds 152,150 shares of Series C Preferred Stock on the schedule of the Investors' Rights Agreement of 2014-12-24 (exhibit to the S-1), so the entry is the Series C; one legal entity, so one row under today's name; market cap $8.77M on 2026-10-06 (stockanalysis.com)",
    rounds=[rnd("2014-12-24", "Series C", None, None, True, u, "filing")]))

member("familiar"); u = web("familiar-seed")
L.append(C("familiar", dispute=("country",), status="acquired", country="US", city="Seattle", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2012", rng="below_1b",
    grad="not_graduated", grad_src="web_verified", grad_cite=REC["familiar"]["citation"], grad_asof=ASOF,
    surfaces=surf("familiar", "no post, page or news item on the firm's site", formd_none("Familiar Inc", "Familiar, Inc", "Familiar Labs")), focus="Consumer & Marketplaces",
    note="Private photo sharing to the screens of family and friends (Seattle; Marcus Womack); 'closed a $1.3 million round of seed funding earlier this year. Investors in the round include Greylock Partners, Redpoint Ventures, Index Ventures' (TechCrunch, 2012-09-18); bought by TASER's Evidence.com in October 2013, the app shut down (TASER's 8-K of 2013-10-10; GeekWire): sold before any Series A, a cited end. The pre-filled country JP is a name collision. YC's Familiar (Toronto, 2026) is another company",
    rounds=[rnd("2012", "Seed", 1300000, None, True, u)], extra={"status_citation": REC["familiar"]["citation"]}))

member("nauto"); u = web("nauto-series-a")
L.append(C("nauto", status="private", country="US", city="Palo Alto", stage="Series A", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2016-04", rng="below_1b", focus="AI & Applied AI",
    note="Driver-safety AI for commercial fleets (Palo Alto); a $12M Series A in April 2016 led by Playground Global, 'Draper Nexus and Index Ventures also participated' (the company's release, read in the search result: the page now redirects); 'backers include Playground Global, Draper Nexus and Index Ventures' (Sierra Wireless 6-K, 2017-02-24); status and band as Greylock's row has them",
    rounds=[rnd("2016-04", "Series A", 12000000, "Playground Global", True, u)]))

member("sourceclear"); u = REC["sourceclear"]["citation"]
L.append(C("sourceclear", status="acquired", country="US", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2015-10", rng="below_1b", focus="Security",
    note="Open-source software composition analysis for developers (founded in Seattle in 2013, then San Francisco; Mark Curphey); '$10 million in Series A funding led by Index Ventures with participation from Storm Ventures', Shardul Shah on the board (the company's release, 2015-10-27); 'CA Technologies is buying SourceClear' (Fortune, 2018-04-09), folded into Veracode",
    rounds=[rnd("2015-10-27", "Series A", 10000000, "Index Ventures", True, u)], extra={"status_citation": web("sourceclear-acquired")}))

member("snapguide"); u = web("snapguide-series-a")
L.append(C("snapguide", status="acquired", country="US", city="San Francisco", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2012-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="How-to guides made and read on the phone (San Francisco); 'announcing a $5 million Series A raise this morning, from investors Atlas Venture, Index Ventures and Michael Arrington's CrunchFund' (TechCrunch, 2012-06-18); the $2M seed before it names Mike Volpi in person beside his firm (The Next Web), which locates a person, so the entry is the round that names the firm; bought by Brit + Co in June 2015 (TechCrunch)",
    rounds=[rnd("2012-06-18", "Series A", 5000000, None, True, u)], extra={"status_citation": gitem("snapguide", "techcrunch", "Acquires How-To App Snapguide")}))

member("sphere"); u = web("sphere-2017")
L.append(C("sphere", dispute=("country",), status="acquired", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2016", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=u, focus="Consumer & Marketplaces",
    note="Sphere Knowledge, Nick D'Aloisio's question-and-answer app that became a group chat app (London; founded November 2015); 'London VC firm Index Ventures is in the frame, having participated in both the seed and Series A' (TechCrunch, 2017-10-05, on a combined round a Companies House filing put at about $11.8M): seed entry, graduated on that Series A; the seed's own date is not on record, so the year is the first full year of the company; bought by Twitter in October 2021 (CNBC). The pre-filled country JP is a name collision; the other books' Sphere rows are the tax compliance company",
    rounds=[rnd("2017-10", "Series A", None, None, True, u)], extra={"status_citation": REC["sphere"]["citation"]}))

member("italic"); u = REC["italic"]["citation"]
L.append(C("italic", status="private", country="US", city="Los Angeles", stage="undetermined", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace selling unbranded goods from the factories of luxury brands (Los Angeles; Jeremy Cai; launched November 2018); 'has raised $13 million in funding from Comcast Ventures, Global Founders Capital, Index Ventures, Ludlow Ventures, Kindred Ventures and others' (PYMNTS, 2018-12-10): the sum of its early rounds, with no round named for the firm, so the round is not on record",
    rounds=[]))

member("gojimo"); u = REC["gojimo"]["citation"]
L.append(C("gojimo", status="acquired", city="London", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2014-01", rng="below_1b",
    grad="not_graduated", grad_src="web_verified", grad_cite=web("gojimo-acquired"), grad_asof=ASOF,
    surfaces=surf("gojimo", "no post, page or news item on the firm's site"), focus="Consumer & Marketplaces",
    note="Exam revision app for UK school students (London; George Burgess); 'Index Ventures Joins $1M+ Seed Round' (TechCrunch, 2014-01-30); a further $1.8M in December 2015, below the step-up an unnamed round needs (R5); 'has been acquired by Telegraph Media Group' with about $3M raised in total (TechCrunch, 2017-04-26): sold before any Series A, a cited end",
    rounds=[rnd("2014-01-30", "Seed", 1000000, None, True, u), rnd("2015-12-22", "unnamed", 1800000, None, None, gitem("gojimo", "techcrunch", "Picks Up Further $1.8M"))],
    extra={"status_citation": web("gojimo-acquired")}))

member("strikingly"); u = REC["strikingly"]["citation"]; g = gsib("strikingly", "headline", "graduation_citation")
L.append(C("strikingly", status="private", country="CN", city="Shanghai", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2013-04", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="SaaS",
    note="Mobile-first website builder (Shanghai; Y Combinator Winter 2013); 'Strikingly (YC W13) raises $1.5M from SV Angel, Index Ventures, FundersClub' (Y Combinator's blog, 2013-04-26); a $6M Series A in August 2017 (TechCrunch, the citation Headline's row carries); status and band as Headline's and YC's rows have them",
    rounds=[rnd("2013-04-26", "Seed", 1500000, None, True, u), rnd("2017-08-31", "Series A", 6000000, None, None, g)]))

member("yup"); u = REC["yup"]["citation"]; g = web("yup-formd-2018")
L.append(C("yup", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2015-05", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="Consumer & Marketplaces",
    note="On-demand tutoring by chat, founded as MathCrunch (San Francisco; Naguib Sawiris; legal entity Yup Technologies Inc., formerly Dwellers, Inc.); the company's release of 2016-04-14 names Index Ventures among the backers of the $3.5M seed of May 2015, extended by $4M in 2016 (EdSurge); its Form D of 2018-04-30 reports $16.0M sold in a round first sold on 2018-04-16, unnamed, above twice the $7.5M of seed money and above $5M, so it graduates by the step-up rule; shut down in late 2024 or early 2025 (Wikipedia; yup.com no longer serves a site)",
    rounds=[rnd("2015-05", "Seed", 3500000, None, True, u), rnd("2016-04-14", "Seed extension", 4000000, None, None, web("yup-edsurge")), rnd("2018-04-16", "unnamed", 16032545, None, None, g, "filing")],
    extra={"status_citation": web("yup-wikipedia")}))

member("leap-transit"); u = REC["leap-transit"]["citation"]; g = gsib("leap-transit", "a16z", "graduation_citation")
L.append(C("leap-transit", status="defunct", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2013-05", rng="below_1b",
    grad="not_graduated", grad_src="web_verified", grad_cite=g, grad_asof=ASOF,
    surfaces=surf("leap-transit", "no post, page or news item on the firm's site", formd_none("Leap Transit")), focus="Consumer & Marketplaces",
    note="Private commuter buses in San Francisco; 'Leap is backed with $2.5 million from Andreessen Horowitz, Index Ventures, Slow Ventures and Salesforce CEO Marc Benioff' (TechCrunch, 2015-03-17), the seed of May 2013 as a16z's row dates it; ordered off the road by the state regulator in May 2015 and bankrupt in July 2015 (Wikipedia, the citation a16z's row carries): ended before any Series A, a cited end",
    rounds=[rnd("2013-05", "Seed", 2500000, None, True, u)], extra={"status_citation": g}))

member("djz"); u = REC["djz"]["citation"]
L.append(C("djz", status="unknown", country="US", city="San Francisco", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2012-09", rng="below_1b",
    grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
    surfaces=surf("djz", "no post, page or news item on the firm's site", formd_none("DJZ")), focus="Media, Gaming & Advertising",
    note="Electronic dance music media site and DJ apps from Seth Goldstein (San Francisco; launched October 2012); the $1M seed led by Google Ventures, 'Other investors in DJZ are: Troy Carter ..., Index Ventures ...' (Global Venturing, 2012-09-15); no later round on any surface and no trace of the company today, so the status reads unknown, as GV's and Kleiner Perkins' rows have it",
    rounds=[rnd("2012-09-12", "Seed", 1000000, "Google Ventures", True, u)]))

member("dazz"); u = web("dazz-2021")
L.append(C("dazz", status="acquired", country="US", city="Palo Alto", stage="undetermined", rng="below_1b", focus="Security",
    note="Cloud security remediation (Palo Alto, engineering in Tel Aviv; Merav Bahat); the December 2021 announcement covers a $10M seed and a $50M Series A together and names Insight, Greylock, Index Ventures and Cyberstarts without splitting them by round (SiliconANGLE, 2021-12-14), so the round Index entered in is not on record; it joined the $50M round of July 2024 (SiliconANGLE); bought by Wiz in November 2024 (Greylock's and Insight's rows)",
    rounds=[rnd("2024-07-24", "unnamed", 50000000, "Greylock", True, REC["dazz"]["citation"])]))

member("bonify"); u = REC["bonify"]["citation"]
L.append(C("bonify", status="acquired", country="DE", city="Berlin", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2017-02", rng="below_1b", focus="Fintech & Payments",
    note="Consumer credit-score and personal finance app (Forteil GmbH, Berlin); the EUR 5.5M Series A 'was led by London's Mosaic Ventures and Ribbit Capital, with participation from Index Ventures' (Tech.eu, 2017-02-21); 'has been acquired by credit bureau company Schufa' (Tech.eu, 2022-12-21)",
    rounds=[rnd("2017-02-21", "Series A", 5800000, "Mosaic Ventures and Ribbit Capital", True, u)], extra={"status_citation": web("bonify-acquired")}))

member("flipagram"); u = REC["flipagram"]["citation"]
L.append(C("flipagram", status="acquired", country="US", city="Los Angeles", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2015-07", rng="below_1b", focus="Consumer & Marketplaces",
    note="Photo-and-music video stories app (Los Angeles); 'a $70 million B round of funding led by Sequoia and including Kleiner Perkins and Index Ventures' (TechCrunch, 2015-07-15); bought by Toutiao (ByteDance) in 2017, as the Kleiner Perkins and Sequoia rows have it",
    rounds=[rnd("2015-07-15", "Series B", 70000000, "Sequoia", True, u)]))

member("little-borrowed-dress"); u = REC["little-borrowed-dress"]["citation"]
L.append(C("little-borrowed-dress", status="defunct", country="US", city="New York", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2014-02", rng="below_1b",
    grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
    surfaces=surf("little-borrowed-dress", "no post, page or news item on the firm's site", "formd: Little Borrowed Dress, Inc. (CIK 1581819) filed five Form Ds 2013-2017; the largest reports $1,750,954 sold of a $3,050,000 offering (D/A 2017-08-16): no round reaches twice the seed and $5M"), focus="Consumer & Marketplaces",
    note="Bridesmaid dress rental (New York; Corinne Hardee); '$1.25M From Index Ventures, A16Z' (TechCrunch, 2014-02-27); its Form Ds to 2017 show only small follow-ons; the company's domain now carries an unrelated wedding blog (read 2026-10-06), so the business is gone, as a16z's row has it",
    rounds=[rnd("2014-02-27", "Seed", 1250000, None, True, u)], extra={"status_citation": web("lbd-site")}))

member("lookback"); u = REC["lookback"]["citation"]; g = gsib("lookback", "lakestar", "graduation_citation")
L.append(C("lookback", status="private", country="SE", city="Stockholm", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2014-03", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=g, focus="SaaS",
    note="Remote user-research recording for apps and websites, founded by former Spotify engineers (Stockholm); the $2.2M seed of March 2014 led by Lakestar with Index Ventures (TechCrunch, 2014-03-27); a $6M round in December 2016 (Tech.eu, the citation Lakestar's row carries); status and band as Lakestar's row has them",
    rounds=[rnd("2014-03-27", "Seed", 2200000, "Lakestar", True, u), rnd("2016-12-13", "Series A", 6000000, None, None, g)]))

member("pets-deli"); u = REC["pets-deli"]["citation"]
L.append(C("pets-deli", status="acquired", country="DE", city="Berlin", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2015", rng="below_1b",
    grad="graduated", grad_src="web_verified", grad_cite=u, focus="Consumer & Marketplaces",
    note="Fresh pet food sold direct (Berlin; founded 2014); Global Founders Capital joined 'existing investors Index Ventures and Project A' in the eight-figure Series A of February 2016 (Tech.eu), so Index was in before the Series A, in the 2015 seed Project A's row dates; bought by VAFO Group in August 2026 (Pet Business World)",
    rounds=[rnd("2016-02", "Series A", None, None, True, u)], extra={"status_citation": gitem("pets-deli", "googlenews", "VAFO Group acquires Pets Deli")}))

member("cue-labs"); u = REC["cue-labs"]["citation"]
L.append(C("cue-labs", country="US", city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012-11", rng="below_1b", focus="Consumer & Marketplaces",
    note="Personal search and daily-agenda app, founded as Greplin (San Francisco; Y Combinator Winter 2010); 'Cue had previously raised a $10 million round in November of 2012 from Index Ventures, which the startup chose not to announce' (TechCrunch, 2013-10-03), after the $4M Series A Sequoia led in 2011, so the entry is the round after the Series A (Growth); bought by Apple in October 2013. Not the calendar app Cue the firm listed in 2020, which is its own row",
    rounds=[rnd("2012-11", "Series B", 10000000, "Index Ventures", True, u)], extra={"status_citation": u}))

# ---- the 1999-2002 Internet Archive rows
R2 = ("T2, pre-fund position (decisions.md R2): the firm's 1999-2002 portfolio page lists it under its own heading 'Prior investments', apart from the "
      "group 'Index Ventures I, L.P.'; a position that began before the fund stays out even where the firm lists it later, unless a fund held it "
      "(Erik, 2026-09-26). No fund of the firm is on record in it")
for s in ("aptix", "arraycomm", "biocom", "calico-commerce", "optimer"):
    L.append(verdict(s, "not_member", R2, ec="site_listing", conf="medium", cite=cap(s, "team_prior")))
L.append(verdict("oxyplus-inc", "not_member", "life_sciences_desk (decisions.md D3): Oxyplus is NormOxys, a drug developer on the firm's Life Sciences list, a practice that became Medicxi in 2016 with its whole book; the canonical row normoxys is already out", ec="site_listing", conf="medium"))
L.append(verdict("opentest-inc", "not_member", "Opentest, Inc. is the first legal name of Loom, whose row is already out: Ilya Fushman's seat, taken after he left Index for Kleiner Perkins in 2018 (T4: the money behind the seat is Kleiner's); Form D 2018-11-27", ec="formd_adjudicated", conf="medium"))

def ia_row(slug, country, city, status, focus, note, cite=None, status_cite=None):
    c = cap(slug, "fund")
    L.append(verdict(slug, "member", f"On the firm's own portfolio page of 1999-2002 in the group of the fund, 'Index Ventures I, L.P.' (Internet Archive)", ec="site_listing", conf="high", cite=c))
    L.append(C(slug, status=status, country=country, city=city, stage="undetermined", rng="below_1b", focus=focus, note=note, rounds=[],
               extra=({"status_citation": status_cite} if status_cite else {})))
ia_row("evolve-software", "US", "San Francisco", "acquired", "SaaS",
    "Service resource planning software for professional services firms (San Francisco, later Emeryville; NASDAQ: EVLV, IPO August 2000); under 'Prior investments' on the firm's 1999 page and in the fund's group from 2001, so a fund held it; Primavera Systems bought the business in 2003 (Wikipedia); the round the fund entered in is not on record",
    status_cite=web("evolve-primavera"))
ia_row("lane15", "US", "Austin", "acquired", "Data Infrastructure",
    "InfiniBand management software (Lane15 Software, Austin); on the firm's list 2002; merged with InfiniSwitch in March 2003, and the merged company, renamed Fabric Networks, closed in September 2003 (Network Computing); the round is not on record",
    status_cite=web("lane15-2003"))
ia_row("lasercomm", "IL", "Tel Aviv", "unknown", "Industrial & Robotics",
    "Optical components for managing chromatic dispersion in fibre networks (founded in Israel in 1998, plant in Plano, Texas); on the firm's list 2001-2002; three rounds of layoffs by April 2002 (Light Reading) and no trace afterwards; no source read gives the end, so the status reads unknown; the round is not on record")
ia_row("pulsent", "US", "Milpitas", "unknown", "Media, Gaming & Advertising",
    "Object-based video compression (Pulsent Corp., Milpitas); on the firm's list 2002, the year it showed its technology (Computerworld); no source read gives what became of it, so the status reads unknown; the round is not on record")
ia_row("respond-com", "US", "Redwood City", "acquired", "Consumer & Marketplaces",
    "Online marketplace matching buyers' requests to merchants, later lead generation (Redwood City, then Palo Alto); on the firm's list 2000-2002; renamed Respond Networks in May 2002 (ClickZ) and bought by TEOCO of Fairfax, Virginia, in December 2002 (company profiles only, so the status is held at medium); the round is not on record",
    status_cite=web("respond-2002"))
ia_row("smarterwork-com", "GB", "London", "unknown", "Consumer & Marketplaces",
    "Online marketplace for freelance business services (London); on the firm's list 2001-2002 as 'Business community software' in the fund's group; no source read gives what became of it, so the status reads unknown; the round is not on record")
ia_row("webfair", "DE", "Munich", "unknown", "SaaS",
    "Software for virtual trade fairs (Webfair AG, Munich; founded 1997); on the firm's list 2001-2002; it built the online platform of Messe München's SYSTEMS fair in 2001; no source read gives what became of it, so the status reads unknown; the round is not on record")
gl.write("delta-1", L)
