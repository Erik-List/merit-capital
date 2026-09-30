"""PRO-100 NEA delta judge g1: queue batch 1 (44 items; glacier-bay-inc is the lead's).

The graduation pass on the Seed rows (DELTA-BRIEF.md s1, COLLECTION.md s6 S2A), two stage corrections the pass
turned up (1bog, catalytic), one open stage (expanse), and the leftovers (agni-corporation; the country-only rows).

Evidence read 2026-09-30: the queue items (show.py), graduation-surfaces.json, the Form D rescan (FORMD_ROUNDS),
nq.py queries (news-extra-g1.json), TechCrunch's own search (the graduation-surfaces wordpress helper), curl and
WebFetch of the cited pages, and 4 WebSearch calls (Qadium 2016 round, Catalytic 2016 rounds, Evalve rounds, Agni).
URLs that are not read through a judge_lib helper were printed by a tool run this session and the page was read:
they are marked where they are defined.

Run: NQ_TAG=g1 python3 judgments-g1.py
"""
import judge_lib as jl

cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
GRADLINES, GNEWS, NEWS, FC, W, POST = jl.GRADLINES, jl.GNEWS, jl.NEWS, jl.FORMD_CITE, jl.W, jl.POST
ASOF = "2026-09-30"

# URLs printed by a tool this session (WebSearch result list, or the TechCrunch search helper) and read before citing.
TC_IFTTT_2018 = "https://techcrunch.com/2018/04/26/ifttt-raises-24m-led-by-salesforce-to-expand-its-platform-to-connect-everything/"  # TechCrunch search helper; page read with curl
CD_QADIUM_A = "https://convergedigest.com/qadium-raises-20m-for-indexing/"  # WebSearch; page read with WebFetch
FIERCE_EVALVE_D = "https://www.fiercebiotech.com/biotech/updated-evalve-r-completes-60-million-series-d-financing"  # WebSearch; read with WebFetch
TC_CATALYTIC_B = "https://techcrunch.com/2019/02/04/chicago-rpa-startup-catalytic-hauls-in-30m-series-b/"  # WebSearch; read with curl
TC_NARRATIV_2017 = "https://techcrunch.com/2017/08/15/narrativ/"  # TechCrunch search helper; read with curl

L = []


def no(slug, src, note, cite=None, extra=(), **kw):
    """A not_graduated line with the full absence record."""
    L.append(cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf="high" if src == "formd" else "medium",
                 grad_asof=ASOF, surfaces=GRADLINES(slug, extra=list(extra), **kw), note=note))


# ======================================================================= Form D layer: graduated (agree with the layer)
L.append(cls("beachmint", grad="graduated", grad_src="formd", grad_cite=FC("beachmint", 2), grad_conf="high",
             rounds=[rnd("2011-06-17", "unnamed (Form D)", 27704026, None, None, FC("beachmint", 2), "filing")],
             note="S2A: graduated on the company's own Form D sequence: after the $2.5M entry of November 2010 (its "
                  "December close of $10.1M is the same round), a $27.7M offering sold in June 2011, above twice the "
                  "entry round."))
L.append(cls("everactive", grad="graduated", grad_src="formd", grad_cite=FC("everactive", 6), grad_conf="high",
             rounds=[rnd("2015-09-24", "unnamed (Form D)", 16903119, None, None, FC("everactive", 6), "filing")],
             note="S2A: graduated on the company's own Form D sequence: the $16.9M offering of September 2015 follows "
                  "the $5.2M entry of March 2014 (PsiKick, now Everactive)."))
L.append(cls("graphite-systems", grad="graduated", grad_src="formd", grad_cite=FC("graphite-systems", 1), grad_conf="high",
             rounds=[rnd("2012-12-21", "unnamed (Form D)", 10399999, None, None, FC("graphite-systems", 1), "filing")],
             note="S2A: graduated on the company's own Form D sequence: a $10.4M offering in December 2012, seven "
                  "months after the $2.0M entry of May 2012."))

# ======================================================================= Form D layer: not graduated (agree with the layer)
no("cartiva", "formd", cite=FC("cartiva", 0),
   note="S2A: not graduated on the company's own Form D sequence: after the $4.5M entry of July 2013 the later offerings "
        "($1.5M in 2014, $8.5M in 2015 and 2016) all sit below twice the entry, no press names a later round, and Wright "
        "Medical bought the company in 2018. The firm dates its first investment to 2011, before the first Form D.",
   extra=["googlenews: judge's query, the company's name with financing, series, raises and investment -> 9 "
          "headlines, the FDA approval (2016), the Wright Medical sale (2018) and implant lawsuits; no named round"])
no("curisium", "formd", cite=FC("curisium", 0),
   note="S2A: not graduated on the company's own Form D sequence: the $1.2M entry of October 2017 and its November "
        "close are one round, no later offering follows, and HealthVerity bought the company in July 2020 (PR Newswire).")
no("eegeo", "formd", cite=FC("eegeo", 0),
   note="S2A: not graduated on the company's own Form D sequence (Kimble, Inc., eeGeo's US parent): the $4.6M entry of "
        "October 2010 and the $4.7M offering of 2011 are the only filings (TechCrunch's 2012 launch story reports the $4M "
        "from NEA), and WRLD3D was liquidated by June 2023 (NetSol's 10-K).",
   extra=["googlenews: judge's query, eeGeo or WRLD3D with raises, funding, investment or crowdfunding -> 1 headline "
          "(NetSol wins a UK contract, 2016); no later round. The Recce headlines on the standard surfaces name "
          "Recce Pharmaceuticals and a TV series, namesakes"])

# ======================================================================= graduated on a cited later round
L.append(cls("appsheet", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("appsheet", "Seattle startup AppSheet raises $15M"), grad_conf="high",
             rounds=[rnd("2019-04", "unnamed", 15000000, None, None,
                         GNEWS("appsheet", "Seattle startup AppSheet raises $15M"), "press")],
             note="S2A: graduated, the $15M round of April 2019 (GeekWire headline; the company's $19.3M Form D of April "
                  "2019 is the same round), above the $8M era ceiling that stands in for the unknown 2015 seed amount."))

L.append(cls("cardioxyl-pharmaceuticals", grad="graduated", grad_src="web_verified",
             grad_cite=FC("cardioxyl-pharmaceuticals", 0), grad_conf="high",
             rounds=[rnd("2009-08-05", "unnamed (Form D)", 9000000, None, None, FC("cardioxyl-pharmaceuticals", 0), "filing"),
                     rnd("2010-07-15", "unnamed (Form D)", 15000000, None, None, FC("cardioxyl-pharmaceuticals", 1), "filing"),
                     rnd("2012-10-24", "unnamed (Form D)", 28050000, None, None, FC("cardioxyl-pharmaceuticals", 2), "filing")],
             note="S2A: graduated, the company's own $9M Form D offering of August 2009 (then $15M in 2010 and $28M in "
                  "2012), above the $5M test for a 2006 seed of unknown amount; the Form D layer abstains because the "
                  "2006 entry predates electronic filing."))

L.append(cls("clearmetal", country="US", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("clearmetal", "ClearMetal gets $9M from Prelude"), grad_conf="high",
             rounds=[rnd("2017-09-20", "Series A", 9000000, "Prelude Ventures, Innovation Endeavors", None,
                         GNEWS("clearmetal", "ClearMetal gets $9M from Prelude"), "press")],
             note="S2A: graduated, the $9M Series A of September 2017 led by Prelude Ventures and Innovation Endeavors "
                  "(TechCrunch, which also reports the earlier $3M seed). HQ San Francisco, US."))

L.append(cls("dandelion", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("dandelion", "raises another $16M"), grad_conf="high",
             rounds=[rnd("2018-03", "Seed", 4500000, None, True, GNEWS("dandelion", "raises another $16M"), "press"),
                     rnd("2019-02-12", "Series A", 16000000, "Comcast Ventures", True,
                         GNEWS("dandelion", "raises another $16M"), "press")],
             note="S2A: graduated, the $16M Series A of February 2019 led by Comcast Ventures with GV, NEA a previous "
                  "backer (TechCrunch, which dates the $4.5M seed to March 2018)."))

DD_W = W("Dell EMC Data Domain")
L.append(cls("data-domain", grad="graduated", grad_src="web_verified", grad_cite=DD_W, grad_conf="high",
             rounds=[rnd("2002", "Series A", 9300000, "NEA and Greylock", True, DD_W, "press"),
                     rnd("2003", "Series B", 17000000, "Sutter Hill Ventures", True, DD_W, "press")],
             note="S2A: graduated; Wikipedia records the $9.3M Series A of 2002 led by NEA and Greylock and the $17M "
                  "Series B of 2003 led by Sutter Hill, both after the firm's 2001 seed. The stage score reads the 2001 "
                  "round as the S-1's Series A-1, which the lead may prefer (then the row is not a Seed entry)."))

L.append(cls("deltastream", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("deltastream", "Raises $15M in Series A"), grad_conf="high",
             rounds=[rnd("2020-12-23", "Seed", 10000000, "New Enterprise Associates", True,
                         GNEWS("deltastream", "DeltaStream secures cash"), "press"),
                     rnd("2024-09-17", "Series A", 15000000, None, None,
                         GNEWS("deltastream", "Raises $15M in Series A"), "press")],
             note="S2A: graduated, the $15M Series A of September 2024 (Business Wire), after the $10M NEA-led seed "
                  "(TechCrunch 2022; its Form D sold from December 2020)."))

L.append(cls("evalve", grad="graduated", grad_src="web_verified", grad_cite=FIERCE_EVALVE_D, grad_conf="high",
             rounds=[rnd("2007-12-04", "Series D", 60000000, "BBT Fund", True, FIERCE_EVALVE_D, "press")],
             note="S2A: graduated, the $60M Series D of December 2007 with New Enterprise Associates among the investors "
                  "(Fierce Biotech), long after the firm's 1999 seed."))

L.append(cls("fyusion", grad="graduated", grad_src="web_verified", grad_cite=FC("fyusion", 3), grad_conf="high",
             rounds=[rnd("2015-03-03", "unnamed (Form D)", 12999984, None, None, FC("fyusion", 3), "filing")],
             note="S2A: graduated, the company's own $13.0M Form D offering of March 2015, more than twice the $3.35M "
                  "seed of May 2014; the Form D layer returned no verdict on this row."))

L.append(cls("goodguide", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("goodguide", "GoodGuide And Geni Land New Funding"), grad_conf="medium",
             rounds=[rnd("2009-01", "Series A", 3730000, None, True,
                         GNEWS("goodguide", "GoodGuide And Geni Land New Funding"), "press")],
             note="S2A: graduated, a $3.73M Series A with Draper Fisher Jurvetson and New Enterprise Associates reported "
                  "from SEC filings in January 2009 (TechCrunch), after the firm's 2007 seed. The Form D layer's no reads "
                  "the 2011 filing as the entry and does not see this paper-era round."))

L.append(cls("granica", grad="graduated", grad_src="first_party", grad_cite=POST("granica-catalyzing"), grad_conf="high",
             rounds=[rnd("2023-06", "Series A", None, "New Enterprise Associates", True, POST("granica-catalyzing"), "firm")],
             note="S2A: graduated; the firm's own post of June 2023 says NEA led Granica's Series A, after its 2020 "
                  "seed (the company reported $45M raised in all)."))

L.append(cls("gravel", status="defunct", rng="below_1b",
             grad="graduated", grad_src="web_verified",
             grad_cite=NEWS("gravel", "raises US$14 million funding round"), grad_conf="medium",
             rounds=[rnd("2023-12-04", "unnamed", 14000000, "New Enterprise Associates", True,
                         NEWS("gravel", "raises US$14 million funding round"), "press")],
             note="S2A: graduated, the US$14M funding round of December 2023 with NEA (Business Times), over twice the $5M "
                  "entry of April 2021; one Indonesian report reads the $14M as the total to date, so medium. Status "
                  "defunct: after founder conflict and layoffs Gravel dismissed its remaining staff and closed "
                  "(youngster.id, 2025-10-27, " + NEWS("gravel", "Runtuhnya Startup Gravel") + ")."))

L.append(cls("grubwithus", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("grubwithus", "Served $5M"), grad_conf="high",
             rounds=[rnd("2012-05-30", "Series A", 5000000, "GRP Partners", None, GNEWS("grubwithus", "Served $5M"), "press")],
             note="S2A: graduated, the $5M round of May 2012 led by GRP Partners (TechCrunch), aligned with the a16z and "
                  "First Round books."))

L.append(cls("ifttt", grad="graduated", grad_src="web_verified", grad_cite=TC_IFTTT_2018, grad_conf="high",
             rounds=[rnd("2018-04-26", "unnamed", 24000000, "Salesforce Ventures", None, TC_IFTTT_2018, "press")],
             note="S2A: graduated; TechCrunch (April 2018) reports a $24M round led by Salesforce, its first announced "
                  "funding in four years after an August 2014 round, NEA among the earlier investors."))

L.append(cls("influitive", grad="graduated", grad_src="web_verified",
             grad_cite=GNEWS("influitive", "Marketing Startup Influitive Raises $30.5M"), grad_conf="high",
             rounds=[rnd("2015-07-09", "Series B", 30500000, None, None,
                         GNEWS("influitive", "Marketing Startup Influitive Raises $30.5M"), "press")],
             note="S2A: graduated, the $30.5M Series B of July 2015 (TechCrunch), aligned with the First Round and "
                  "Lightspeed books."))

# ======================================================================= not graduated: the absence test
no("ajax-vascular", "absence_check",
   note="S2A: not graduated; the absence test found no later round of the 2013 seed on any surface (listed), and no "
        "Form D by the company.")
no("blockcypher", "absence_check",
   note="S2A: not graduated; the absence test found only the $3M first round TechCrunch reported in January 2015 and no "
        "later round (surfaces listed).",
   extra=["googlenews: judge's query, BlockCypher with raises, Series A, funding or acquired -> 1 headline (the Payza "
          "integration, 2018); no later round"])
no("boxc", "absence_check",
   note="S2A: not graduated; the absence test found no round of BoxC after the 2014 seed (the boxC.in headlines are "
        "Chai Point's, a namesake).",
   extra=["googlenews: judge's query, BoxC with logistics or ecommerce and raises, funding or series -> 0 results"])
no("change-io", "absence_check",
   note="S2A: not graduated; the absence test found no round of Change (getchange.io) after the 2022 seed (surfaces "
        "listed).",
   extra=["googlenews: judge's query, Change with donation API or GetChange and raises, funding or seed -> 2 "
          "headlines (TechCrunch 2022-07-11 on its crypto donations, and a namesake); no later round"])
no("coedition", "absence_check",
   note="S2A: not graduated; the $4M seed of March 2018 (TechCrunch, AlleyWatch) is the only round reported, and no "
        "later round or sale announcement was found (the site now points to City Chic's CoEdition store).",
   extra=["googlenews: judge's query, CoEdition with City Chic, acquired, acquires or raises -> 6 headlines, the 2018 "
          "launch and seed, swimwear lists and a City Chic results story; no later round"])
no("crowdmed", "absence_check",
   note="S2A: not graduated; the absence test found no round after the seed (surfaces listed), aligned with the a16z and "
        "Khosla books.")
no("element3-health", "absence_check",
   note="S2A: not graduated; the absence test found no round of Element3 Health, renamed Grouper in January 2024, after "
        "the 2018 seed (surfaces listed).",
   extra=["googlenews: judge's queries, Element3 Health or Grouper with raises, funding, Series A or seed, and Grouper "
          "with health plan or Medicare -> no headline naming the company"])
no("elion", "absence_check",
   note="S2A: not graduated; the $9.3M NEA-led round of August 2025 is named a seed round by AlleyWatch, so no Series A "
        "or later round followed the October 2022 seed (surfaces listed).",
   extra=["alleywatch: the August 2025 interview (" + GNEWS("elion", "Help Health Systems Navigate") + ") -> 'an "
          "oversubscribed $9.3M seed round led by existing investor NEA', total funding $12.6M; no Series A"])
no("enceladus", "absence_check",
   note="S2A: not graduated; the absence test found no round of the genome-editing company after the 2022 seed (the "
        "Enceladus headlines are the Saturn moon and namesakes).")
no("eventup", "absence_check",
   note="S2A: not graduated; the $1.8M seed of June 2012 (TechCrunch) is the only round reported, and the company is now "
        "part of Tripleseat (surfaces listed).",
   extra=["googlenews: judge's query, EventUp with Tripleseat, acquired, acquires or raises -> 8 headlines, Los "
          "Angeles startup features (2012-13) and Tripleseat's own news; no later round"])
no("functional-finance", "absence_check",
   note="S2A: not graduated; the $8M seed of August 2023 (PR Newswire, citybiz) is the latest round found (surfaces "
        "listed).")
no("geistm", "absence_check",
   note="S2A: not graduated; the absence test found no round of GeistM after the 2011 seed (surfaces listed).",
   extra=["googlenews: judge's query, GeistM or Geist Media with raises, funding or acquired -> 1 headline (a 2018 "
          "fastest-growing award); no round"])
no("hireguide", "absence_check",
   note="S2A: not graduated; no round of Hireguide after the 2022 seed was found, and Hirevue bought its technology and "
        "team in March 2026 (GlobeNewswire).",
   extra=["globenewswire: " + GNEWS("hireguide", "Hirevue Acquires Hireguide Technology") + " -> Hirevue acquired the "
          "technology behind Hireguide and its team (2026-03-10); no funding named"])
no("hos", "absence_check",
   firm_note="the firm's own listing for hOS (Seed, first invested 2022) -> no post names a round of the company",
   note="S2A: not graduated; no round of hOS after the 2022 seed was found (the HoS and HOS headlines on the standard "
        "surfaces are namesakes).",
   extra=["googlenews: judge's query, hOS beside Jeremy Achin -> 1 headline (Forbes 2022-02-09, the launch); no round"])
no("howl", "absence_check",
   note="S2A: not graduated; TechCrunch (2017) reports $3M raised by Narrativ (Howl's former name) from Talis Capital "
        "and NEA, and no later round was found (the Howl headlines on the standard surfaces are namesakes).",
   extra=["techcrunch: TechCrunch's own search for Narrativ -> 7 results, the 2017 profile (" + TC_NARRATIV_2017 + ": "
          "$3M from Talis Capital and NEA); no later round",
          "googlenews: judge's queries, Narrativ with raises, funding or Series, and Narrativ with Shirley Chen -> "
          "profiles (Forbes 2018, Medium 2018, Business Insider 2020); no round"])
no("hyperfair", "absence_check",
   note="S2A: not graduated; the $1.2M convertible round of February 2014 (Intesa Sanpaolo) is the latest found after "
        "the 2012 seed (surfaces listed).",
   extra=["googlenews_local: judge's query in the Italian edition, Hyperfair with round, finanziamento, milioni, "
          "investimento or Series A -> 0 results"])

# ======================================================================= stage corrections and the open stage
L.append(cls("1bog", stage="Series A", stage_src="web_verified",
             stage_cite=GNEWS("1bog", "One Block Off the Grid Raises"), stage_conf="high",
             flags=["stage_disputes_band"],
             rounds=[rnd("2010-02-10", "Series A", 5000000, "New Enterprise Associates", True,
                         GNEWS("1bog", "One Block Off the Grid Raises"), "press")],
             note="Stage: TechCrunch (2010-02-10) reports a $5M Series A from New Enterprise Associates, the round of the "
                  "company's February 2010 Form D, so the entry is Series A, not the band's Seed, and no S2A applies."))

L.append(cls("catalytic", stage="undetermined", entry_date="2016", flags=["stage_disputes_band"],
             rounds=[rnd("2016-09-06", "unnamed (Form D)", 11129988, None, None, FC("catalytic", 0), "filing"),
                     rnd("2019-01", "Series B", 30000000, "Intel Capital", True, TC_CATALYTIC_B, "press")],
             note="Stage: the firm dates its first investment to 2016 and its June 2017 release names Blake Wu a board "
                  "observer, so the 2018 Form D the band read as a seed is not the entry. A web search reports a 2016 "
                  "seed and an $11.1M 2016 Series A (the company's September 2016 Form D gives $11.1M) without naming "
                  "NEA in either, so NEA's round is not named; NEA was an existing investor at the 2019 Series B "
                  "(TechCrunch)."))

L.append(cls("expanse", stage="Series A", stage_src="web_verified", stage_cite=CD_QADIUM_A, stage_conf="high",
             rounds=[rnd("2016-06-06", "Series A", 20000000, "New Enterprise Associates", True, CD_QADIUM_A, "press")],
             note="Stage: Qadium (renamed Expanse) announced a $20M Series A in June 2016 led by Scott Sandell of NEA "
                  "(Converge Digest), the firm's 2016 first investment; not a Seed entry. The Y Combinator book's "
                  "Expanse (Spring 2026 batch) is a different company."))

# ======================================================================= leftovers
L.append(cls("agni-corporation", status="unknown", rng="below_1b", country="US", focus="Climate & Energy",
             flags=["city_unknown"],
             note="Biofuels developer (Agni Corp, a Cayman holding company whose March 2011 Form D gives its officers "
                  "c/o Inventus Law, Palo Alto; the founder describes operations focused on India). No news, filing or "
                  "site shows it operating, sold or closed after the firm's 2013 listing, so the state is unknown and "
                  "the city is not established."))
for s in ("clarifai", "clarify", "coda", "collective-health"):
    L.append(cls(s, country="US", note="HQ country US, as in every sibling book for the same company."))

jl.write("g1", L)
