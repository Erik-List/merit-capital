"""PRO-100 NEA, stage pass s1, first half of queue/s1.json (50 rows): the round NEA first entered, with the
funding history found (COLLECTION.md s6, PRO-143). Run: NQ_TAG=s1 python3 judgments-s1a.py"""
import json

import judge_lib as jl

C, rnd = jl.cls, jl.rnd
CLS = json.loads((jl.INV / "companies/classification.json").read_text())
Q = json.loads((jl.Q / "s1.json").read_text())["slugs"][:50]


def OLD(slug):
    """The funding rounds already on the row (kept: a new list replaces the key)."""
    return list((CLS.get(slug) or {}).get("funding_rounds") or [])


def FD(slug, firm=None):
    """The row's own Form D sequence as unnamed rounds, each cited to its filing index."""
    out = []
    rs = jl.FORMD_ROUNDS(slug)
    for i, r in enumerate(rs):
        out.append(rnd((r.get("sale_date") or r.get("quarter") or "")[:10], "unnamed (Form D)",
                       r.get("offering_usd") or r.get("sold_usd"), None, firm, jl.FORMD_CITE(slug, i), "filing"))
    return out


def MERGE(*lists):
    seen, out = set(), []
    for lst in lists:
        for x in lst:
            k = (x.get("date"), x.get("round"), x.get("amount_usd"))
            if k not in seen:
                seen.add(k)
                out.append(x)
    return out


SRCH = "Stage pass 2026-09-30: Google News, TechCrunch's own search and EDGAR full text"
L = []

# ---------------------------------------------------------------- $1B+ rows
s = "world-labs"
TC_A = "https://techcrunch.com/2024/08/14/nea-led-a-100m-round-into-fei-fei-lis-new-ai-startup-now-valued-at-over-1b/"
TC_S = "https://techcrunch.com/2024/09/13/fei-fei-lis-world-labs-comes-out-of-stealth-with-230m-in-funding/"
L.append(C(s, stage="undetermined", rounds=MERGE(OLD(s), [
    rnd("2024-09-13", "two rounds totalling $230M (launch report)", 230000000, None, True, TC_S, "press")]),
    note="Stage pass 2026-09-30: TechCrunch's August and September 2024 reports name neither the April first round "
         "nor the $100M round NEA led, so the stage stays undetermined; the a16z book's Series A cites the September "
         "report, which names no round."))

s = "genies"
TC_BLEND = "https://techcrunch.com/2014/03/05/blend-lands-2-7m-in-seed-funding-led-by-nea/"
TC_G18 = "https://techcrunch.com/2018/11/19/genies-avatars/"
TC_G21 = "https://techcrunch.com/2021/05/03/avatar-startup-genies-scores-65-million-in-funding-round-led-by-mary-meekers-bond/"
TC_G22 = "https://techcrunch.com/2022/04/12/avatar-startup-genies-hits-1-billion-valuation-in-latest-raise/"
L.append(C(s, stage="Seed", stage_src="web_verified", stage_cite=TC_BLEND, stage_conf="high", entry_date="2014-03-05",
           grad="graduated", grad_src="web_verified", grad_cite=TC_G22, grad_conf="high",
           rounds=[rnd("2013", "accelerator funding (Digital Catalyst)", 1300000, None, False, TC_BLEND, "press"),
                   rnd("2014-01-30", "unnamed (Form D)", 2400000, None, None, None, "filing"),
                   rnd("2014-03-05", "Seed", 2700000, "New Enterprise Associates", True, TC_BLEND, "press"),
                   rnd("2015-04-23", "unnamed (Form D)", 6341383, None, None, None, "filing"),
                   rnd("2018-11-19", "unnamed", 10000000, None, None, TC_G18, "press"),
                   rnd("2021-05", "Series B", 65000000, "Bond", True, TC_G22, "press"),
                   rnd("2022-04-12", "unnamed ($1B valuation)", 150000000, "Silver Lake", True, TC_G22, "press")],
           note="Genies is Blend renamed (EDGAR lists the issuer, CIK 1560253, as formerly Blend Systems, Inc.): NEA "
                "led Blend's $2.7M seed in March 2014 (TechCrunch), after $1.3M from the Digital Catalyst accelerator. "
                "TechCrunch's 2022 report names the May 2021 $65M round a Series B, so the row graduated."))

s = "splashtop"
VB = "https://venturebeat.com/business/devicevms-instant-on-software-get-another-15m/"
L.append(C(s, stage="Growth", stage_src="model", stage_cite=VB, stage_conf="medium", entry_date="2008-08-19",
           rounds=[rnd("2008", "unnamed", 1000000, "Merus Capital", False, VB, "press"),
                   rnd("2008-08-19", "Series C (the company's release title)", 15000000, "New Enterprise Associates",
                       True, VB, "press")],
           note="DeviceVM (renamed Splashtop in 2010) raised $15M on 2008-08-19 in a round NEA led, with existing "
                "investors Storm Ventures, DFJ Dragon, Tim Draper and Larry Augustin, taking the total to about $36M "
                "(VentureBeat); the company's release is titled Series C (vmblog, page blocked when read), so NEA "
                "entered at Growth."))

# ---------------------------------------------------------------- public rows
s = "progress-software"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round; the 1991 IPO prospectus predates EDGAR's electronic filings."))

s = "champions-oncology"
CH = jl.FTS("CHAMPIONS", "8-K")
L.append(C(s, stage="Growth", stage_src="web_verified", stage_cite=CH, stage_conf="high", entry_date="2015-03-11",
           rounds=[rnd("2015-03-11", "private placement into the listed company (2015 Securities Purchase Agreement)",
                       None, None, True, CH, "filing")],
           note="NEA 14 entered through the March 2015 securities purchase agreement with Battery, a placement into "
                "an already listed company: Growth. The X1 membership question stands."))

s = "lianlian"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round of the firm's 2006 entry; the 2025 Hong Kong prospectus was not read."))

s = "iridex-corporation"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round; the February 1996 IPO prospectus predates the company's first EDGAR filing "
                "(August 1996)."))

s = "corxel"
SITE_C = jl.SITE(s)
D1 = next(x["source"] for x in OLD(s) if x.get("round") == "Series D-1")
L.append(C(s, stage="Seed", stage_src="first_party", stage_cite=SITE_C, stage_conf="medium", entry_date="2024",
           grad="graduated", grad_src="web_verified", grad_cite=D1, grad_conf="high",
           rounds=MERGE([rnd("2024", "Seed (the firm's own label)", None, None, True, SITE_C, "firm")], OLD(s)),
           note="Stage pass 2026-09-30: no release, press item or filing documents the round NEA entered in 2024, so "
                "the firm's own Seed label stands at medium; the company's January 2026 Series D-1 release is a later "
                "named round, so the row graduated."))

s = "corestory"
L.append(C(s, stage="undetermined", rounds=OLD(s),
           note=SRCH + " and Crunchbase News name no round before the 2025 Series A that NEA co-led."))

s = "incarey"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " return nothing on InCarey's rounds."))

s = "inventiva-s-a"
F1 = jl.FTS("Inventiva", "F-1")
L.append(C(s, stage="undetermined",
           rounds=[rnd("2020-06", "holding in the listed company (a 5% holder named in the F-1)", None, None, True,
                       F1, "filing")],
           note="NEA appears only as a 5% holder of a company listed on Euronext Paris since 2017 (the 2020 F-1 for "
                "its Nasdaq offering); no private round is on record, so membership should be re-judged under X1."))

s = "comprehensive-pharmacy-services"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " and Crunchbase News name no transaction for NEA's 2019 entry."))

s = "recludix-pharma"
L.append(C(s, stage="undetermined", rounds=OLD(s),
           note="Stage pass 2026-09-30: Fierce Biotech names NEA among the November 2021 Series A investors, but the "
                "firm dates its entry to 2019 and no earlier round is on record."))

s = "erytech"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " show no private round; NEA's 2020 purchase was into a listed company (X1)."))

s = "strive-health"
CBN = ("https://news.crunchbase.com/health-wellness-biotech/"
       "capitalg-backed-strive-health-lands-140m-to-develop-kidney-care-technology/")
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=CBN, stage_conf="high", entry_date="2018",
           rounds=MERGE([rnd("2018", "Series A", 80000000, "NEA", True, CBN, "press")], OLD(s)),
           note="Crunchbase News (2021-03-16) quotes the CEO: $80M of Series A funding led by NEA in 2018, the year "
                "NEA incubated the company; the $140M 2021 round was the Series B."))

s = "evident-id"
L.append(C(s, stage="undetermined", rounds=OLD(s),
           note=SRCH + " and Crunchbase News name none of Evident's rounds."))

s = "rocket"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " return nothing on this Rocket's rounds."))

s = "aveo-pharmaceuticals-inc"
AV = jl.FTS("AVEO PHARMACEUTICALS INC", "8-K")
L.append(C(s, stage="Growth", stage_src="web_verified", stage_cite=AV, stage_conf="high", entry_date="2016-05-13",
           rounds=[rnd("2016-05-13", "PIPE (units of shares and warrants)", 17024995, "New Enterprise Associates", True,
                       AV, "filing")],
           note="NEA led AVEO's May 2016 PIPE (8-K), a placement into a company listed since 2010: Growth. No earlier "
                "NEA private round is on record, so membership should be re-judged under X1."))

s = "greythr"
L.append(C(s, stage="undetermined", rounds=OLD(s), note=SRCH + " name no round of NEA's 2016 entry."))

s = "pilot-ai"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Pilot AI Labs."))

s = "broadly"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Broadly."))

s = "guideline"
TC_GL = "https://techcrunch.com/2017/08/08/guideline-15-million/"
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd(None, "earlier financing, $9M in total (unnamed)", 9000000, None, True, TC_GL, "press"),
    rnd("2017-08-08", "unnamed", 15000000, "Felicis Ventures", None, TC_GL, "press")], OLD(s)),
    note="Stage pass 2026-09-30: TechCrunch (2017) lists NEA among the investors in the $9M Guideline raised before "
         "the Felicis round, without naming the round."))

s = "nightstar"
PRN = ("https://www.prnewswire.com/news-releases/"
       "nightstarx-closes-35-million-series-b-funding-to-advance-inherited-retinal-disease-pipeline-300174913.html")
NS = "https://www.sec.gov/Archives/edgar/data/1711675/000119312517297974/d401686d424b4.htm"
L.append(C(s, stage="Growth", stage_src="web_verified", stage_cite=PRN, stage_conf="high", entry_date="2015-11-09",
           rounds=[rnd("2014-05", "Class A ordinary shares (founding financing)", None, "Syncona", False, NS, "filing"),
                   rnd("2015-11-09", "Series B", 35000000, "New Enterprise Associates", True, PRN, "company"),
                   rnd("2017-06", "private placement (Class A ordinary shares)", 45000000, None, True, NS, "filing")],
           note="NightstaRx's release (2015-11-09): NEA, a new investor, led the $35M Series B and David Mott joined "
                "the board; Syncona had founded the company."))

s = "the-players-tribune"
TC_PT = "https://techcrunch.com/2015/06/15/derek-jeters-players-club-raises-9-5-million-led-by-nea/"
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd("2014", "first outside financing", 3000000, None, None, TC_PT, "press"),
    rnd("2015-06-15", "unnamed", 9500000, "NEA", True, TC_PT, "press")],
    [x for x in OLD(s) if x.get("date") != "2015-06-15"]),
    note="Stage pass 2026-09-30: TechCrunch says NEA led a $9.5M close of a planned $15M round, after $3M of first "
         "outside financing, but names neither round."))

s = "51offer"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of 51offer."))

s = "console"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of this Console."))

s = "omio"
GE = jl.POST("goeuro")
SK = "https://skift.com/2015/12/08/goeuro-gets-45-million-in-funding-round-led-by-goldman-sachs/"
L.append(C(s, stage="Series A", stage_src="first_party", stage_cite=GE, stage_conf="high", entry_date="2014-08-27",
           rounds=[rnd("2014-08-27", "Series A", None, "NEA", True, GE, "firm"),
                   rnd("2015-12-08", "Series B", 45000000, "Goldman Sachs", None, SK, "press")],
           note="The firm's own post (2014-08-27) announces its Series A investment in GoEuro, in the year the firm "
                "gives as its first; Omio is GoEuro renamed."))

s = "upskill"
TC_A1 = "https://techcrunch.com/2014/04/22/apx-labs-gets-10m-from-nea-for-enterprise-friendly-wearables/"
TC_A2 = "https://techcrunch.com/2015/11/18/apx-labs-grabs-13-million-for-enterprise-smart-glasses-platform/"
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd("2014-04-22", "first institutional round", 10000000, "NEA", True, TC_A1, "press"),
    rnd("2015-11-18", "unnamed", 13000000, "NEA", True, TC_A2, "press")], FD(s)),
    note="Stage pass 2026-09-30: TechCrunch calls NEA's $10M of April 2014 APX Labs' first institutional round but "
         "names no series, and the $15.6M Form D of that quarter sits above the era's Series A band, so the stage "
         "stays undetermined."))

s = "agenebio-inc"
L.append(C(s, stage="undetermined", rounds=FD(s), note=SRCH + " name none of the Form D rounds."))

s = "citic-pharmaceuticals"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round. The row and china-health-citic carry the same description and the same "
                "acquirer (Shanghai Pharmaceuticals): one company."))

s = "envisia-therapeutics"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Envisia."))

s = "koozoo"
TC_K = ("https://techcrunch.com/2012/12/12/"
        "koozoo-raises-2-5m-seed-round-led-by-nea-and-tugboat-to-cover-the-world-with-24-hour-mobile-video/")
L.append(C(s, stage="Seed", stage_src="web_verified", stage_cite=TC_K, stage_conf="high", entry_date="2012-12-12",
           country="US", country_src="web_verified", country_cite=TC_K, city="San Francisco", city_src="web_verified",
           rounds=[rnd("2012-12-12", "Seed", 2500000, "New Enterprise Associates and Tugboat Ventures", True, TC_K,
                       "press")],
           note="TechCrunch: San Francisco-based Koozoo's $2.5M seed round was led by NEA and Tugboat Ventures. "
                "Graduation left for the graduation pass."))

s = "medisys-edutech"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of MediSys EduTech."))

s = "nordic-windpower"
L.append(C(s, stage="undetermined", rounds=OLD(s),
           note=SRCH + " name no NEA round before the May 2010 Series C."))

s = "primary-health-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Primary Health."))

s = "sibeam-inc"
WS = jl.W("SiBEAM")
L.append(C(s, stage="undetermined",
           rounds=[rnd(y, "unnamed venture round", None, None, None, WS, "press") for y in
                   ("2004", "2005", "2006", "2008", "2010")],
           note="Stage pass 2026-09-30: Wikipedia gives financing from USVP, NEA, Foundation and Lux in 2004, 2005, "
                "2006, 2008 and 2010 (over $112M) without round names or NEA's first year."))

s = "the-spectranetics-corporation"
L.append(C(s, stage="undetermined", rounds=[],
           note=SRCH + " name no round; the holding traces to Advanced Interventional Systems (D8 question stands)."))

s = "visual-edge-technology-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Visual Edge Technology."))

s = "clarvista-medical"
L.append(C(s, stage="undetermined", rounds=FD(s),
           note=SRCH + " name no round of the firm's 2012 entry; the 2015 Form D is later."))

s = "legato-medical"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of Legato Medical."))

s = "sonatype"
ATD = "https://allthingsd.com/20120710/sonatype-manager-of-grown-up-open-source-software-lands-25-million-from-nea/"
TC_S16 = "https://techcrunch.com/2016/02/04/sonatype-snares-30-million-investment-led-by-goldman-sachs/"
TC_S18 = "https://techcrunch.com/2018/09/07/sonatype-raises-80-million-to-build-out-nexus-platform/"
L.append(C(s, stage="Growth", stage_src="model", stage_cite=ATD, stage_conf="medium", entry_date="2012-07-10",
           rounds=MERGE([rnd("2012-07-10", "unnamed (Series C in Crunchbase, vendor)", 25000000,
                             "New Enterprise Associates", True, ATD, "press"),
                         rnd("2016-02-04", "unnamed", 30000000, "Goldman Sachs", None, TC_S16, "press"),
                         rnd("2018-09-07", "unnamed", 80000000, None, None, TC_S18, "press")], FD(s)),
           note="AllThingsD (2012-07-10): NEA led the $25M round with existing investors Accel, Hummer Winblad, "
                "Morgenthaler and Bay Partners following, after a $10M 2010 Form D round; Crunchbase (vendor, not "
                "cited) calls it the Series C, so NEA entered at Growth."))

s = "blue-jeans-network"
TC_B12 = "https://techcrunch.com/2012/06/27/blue-jeans-nea/"
TC_B15 = "https://techcrunch.com/2015/09/23/blue-jeans-network-raises-76-5m-to-bring-video-conferencing-beyond-the-office/"
L.append(C(s, stage="undetermined", rounds=MERGE(OLD(s), [
    rnd("2012-06-27", "unnamed", 25000000, None, True, TC_B12, "press"),
    rnd("2015-09-23", "unnamed", 76500000, None, None, TC_B15, "press")]),
    note="Stage pass 2026-09-30: TechCrunch's 2012 and 2015 reports name no series, and no source names the "
         "pre-launch round of 2011 that NEA joined."))

s = "gumgum"
TC_G11 = "https://techcrunch.com/2011/10/24/in-image-ad-network-gumgum-raises-7-million-from-nea-first-round-and-grp/"
TC_G15 = "https://techcrunch.com/2015/05/28/gumgum-series-c/"
L.append(C(s, stage="Growth", stage_src="model", stage_cite=TC_G11, stage_conf="medium", entry_date="2011-10-24",
           rounds=MERGE(OLD(s), [rnd("2011-10-24", "unnamed", 7000000, "NEA", True, TC_G11, "press"),
                                 rnd("2015-05-28", "Series C", 26000000, "Morgan Stanley Expansion Capital", True,
                                     TC_G15, "press")]),
           note="TechCrunch: NEA led GumGum's $7M round of October 2011 (total raised $11M, after a 2009 second round), "
                "and the next round, $26M in May 2015 with NEA following, was the Series C (total over $36M), so "
                "NEA's entry was the Series B: Growth."))

s = "netcitadel"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of NetCitadel."))

s = "azuray-technologies-inc"
L.append(C(s, stage="undetermined", rounds=FD(s), note=SRCH + " name no round of Azuray."))

s = "everfi"
TC_E10 = "https://techcrunch.com/2010/09/02/everfi-raises-11-million-for-financial-literacy-education-application/"
TC_E12 = ("https://techcrunch.com/2012/08/14/"
          "critical-skills-education-saas-everfi-raises-10m-from-jeff-bezos-eric-schmidt-ev-williams-and-others/")
TC_E17 = "https://techcrunch.com/2017/04/26/everfi-raises-190-million-to-teach-life-skills-and-touchy-subjects-online/"
L.append(C(s, stage="Series A", stage_src="web_verified", stage_cite=TC_E10, stage_conf="high", entry_date="2010-09-02",
           rounds=[rnd("2010-09-02", "Series A", 11000000, "New Enterprise Associates", True, TC_E10, "press"),
                   rnd("2012-08-14", "unnamed", 10000000, None, None, TC_E12, "press"),
                   rnd("2017-04-26", "unnamed", 190000000, None, None, TC_E17, "press")],
           note="TechCrunch (2010-09-02): EverFi raised $11M in Series A funding from NEA, with TomorrowVentures "
                "participating, in the year the firm gives as its first."))

s = "suvolta"
TC_SV = "https://techcrunch.com/2012/01/05/semiconductor-startup-suvolta-collects-17-6m-in-second-funding-round/"
L.append(C(s, stage="undetermined", rounds=MERGE(OLD(s), [
    rnd("2010", "original funding (unnamed)", 22000000, None, True, TC_SV, "press"),
    rnd("2012-01-05", "second funding round (unnamed)", 17600000, None, None, TC_SV, "press")]),
    note="Stage pass 2026-09-30: TechCrunch calls the $22M of 2010 from Kleiner Perkins, August Capital and NEA the "
         "original funding but names no series, and it sits above the era's Series A band."))

s = "brightkite"
TC_BK = ("https://techcrunch.com/2009/04/07/"
         "mobile-socializing-limbo-merges-with-brightkite-and-announces-9-million-funding-round/")
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd("2009-04-07", "unnamed (at the Limbo merger)", 9000000, "Nexit Ventures", True, TC_BK, "press")], FD(s)),
    note="NEA's stake came through Limbo: TechCrunch names NEA an existing Limbo investor in the $9M round of the "
         "April 2009 merger, and EDGAR lists Brightkite, Inc. as formerly Limbo Inc. Limbo's earlier rounds are not "
         "named."))

s = "mashlogic-inc"
TC_ML = "https://techcrunch.com/2009/06/01/mashlogic-launches-adds-high-powered-angels-to-investor-list/"
L.append(C(s, stage="undetermined", rounds=MERGE([
    rnd(None, "seed (Bessemer incubation)", 900000, "Bessemer Venture Partners", False, TC_ML, "press"),
    rnd("2009-06-01", "second seed", 500000, None, False, TC_ML, "press")], FD(s)),
    note="Stage pass 2026-09-30: TechCrunch (June 2009) lists Bessemer's seed and a $500K second seed without NEA; "
         "NEA's round is the unnamed $2.5M Form D of August 2009."))

s = "3jam-inc"
L.append(C(s, stage="undetermined", rounds=[], note=SRCH + " name no round of 3Jam."))

got = [x["slug"] for x in L]
assert got == Q, [a for a in Q if a not in got] + [b for b in got if b not in Q]
jl.write("s1a", L)
