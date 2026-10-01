"""Duty 9 (a duty 7 hit is a class): the two classes the blind sample surfaced, swept over the whole base.

Class A, from chargepoint: an early Form D band (Seed or Series A, source formd_band) that rides a round which is
not the company's first. The PRO-157 guard reads a numeric year of incorporation; a Form D that ticks "over five
years ago" carries none, so the guard never fired on those rows.
Class B, from everlane: member rows with no focus.

Run: NQ_TAG=du python3 judgments-dub.py"""
import judge_lib as jl
from judge_lib import cls, rnd

D = ("stage_disputes_band",)


def fd(slug, sale_date):
    rs = jl.FORMD_ROUNDS(slug)
    i = [k for k, r in enumerate(rs) if r.get("sale_date") == sale_date]
    if len(i) != 1:
        raise SystemExit(f"fd({slug!r}, {sale_date!r}) matched {len(i)}")
    return jl.FORMD_CITE(slug, i[0])


TC = {
    "datameer": "https://techcrunch.com/2011/05/16/kleiner-perkins-leads-9m-round-in-apache-hadoop-based-analytics-platform-datameer/",
    "rtr": "https://techcrunch.com/2011/05/23/kleiner-perkins-invests-15m-in-rent-the-runway/",
    "alienvault_b": "https://techcrunch.com/2012/01/31/on-the-heels-of-nabbing-7-hp-execs-cyber-security-startup-alienvault-raises-8-million/",
    "alienvault_c": "https://techcrunch.com/2012/07/09/alienvault-series-c/",
    "agilyx": "https://techcrunch.com/2011/04/01/agilyx-22-million-seriesb/",
    "uship": "https://techcrunch.com/2012/12/19/shipping-and-transportation-marketplace-uship-raises-18m-from-kleiner-perkins/",
    "booyah_a": "https://techcrunch.com/2009/07/28/booyah-society-level-up-in-life-via-the-iphone/",
    "booyah_b": "https://techcrunch.com/2010/05/16/booyah-raises-20-million-from-accel-expects-6-million-users-by-the-end-of-this-summer/",
    "dust_seed": "https://techcrunch.com/2018/11/14/this-startup-got-2-3m-to-identify-physical-objects-using-diamond-dust/",
    "dust_a": "https://techcrunch.com/2019/07/17/dust-identity-secures-10m-series-a-to-identify-objects-with-diamond-dust/",
    "spruce": "https://techcrunch.com/2014/09/25/spruce-gets-2-million-in-seed-from-kleiner-perkins-baseline-and-cowboy-ventures-to-put-a-doctor-in-the-palm-of-your-hand/",
}
AREA1_SEED = "https://venturebeat.com/2014/05/05/former-nsa-teammates-launch-area-1-security-snag-2-5-million"
AREA1_A = ("https://www.globenewswire.com/news-release/2014/12/10/1187523/0/en/Area-1-Security-Announces-8-Million-"
           "Funding-Round-Led-by-Kleiner-Perkins-Caufield-Byers.html")
LIVONGO_S1 = jl.FTS("Livongo", "S-1")
NO_GRAD = {"seed_to_a_graduation": None, "graduation_source": None, "graduation_citation": None,
           "graduation_confidence": None}

OLD = ("Duty 9 sweep (early Form D band on an older company): the band's Series A rests on the row's first "
       "electronically filed Form D, which ticks 'over five years ago' for the year of incorporation, so the "
       "company was at least five years old at that round and had raised before it; the older-company rule "
       "(PRO-157) gives such a band no early stage, and its guard missed the row only because the filing carries "
       "no numeric year. ")

lines = [
    # ---- Class A: a documented round replaces the band
    cls("datameer", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC["datameer"],
        entry_date="2011-04-22", flags=D,
        rounds=[rnd("2010-04", "first round", 2500000, "Redpoint Ventures", False,
                    "https://techcrunch.com/2010/04/13/datameer-raises-2-5-million-for-apache-hadoop-based-analytics-platform/", "press"),
                rnd("2011-04-22", "Series B", 9250000, "Kleiner Perkins", True, TC["datameer"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2011-05-16) reports $9.25M 'led by Kleiner Perkins with "
             "participation from Redpoint Ventures', after Redpoint's $2.5M of 2010, and the company's own Form D "
             "for the round (first sale 2011-04-22) reads 'Offering of Series B Preferred Stock'. The entry is the "
             "Series B: Growth, not the band's Series A."),
    cls("rent-the-runway", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC["rtr"],
        entry_date="2011-05-13", focus="Consumer & Marketplaces", flags=D,
        rounds=[rnd("2009-07-08", "unnamed (Form D)", 1750000, None, False, fd("rent-the-runway", "2009-07-08"), "filing"),
                rnd("2010-02-16", "unnamed (Form D)", 15000175, None, False, fd("rent-the-runway", "2010-02-16"), "filing"),
                rnd("2011-05-13", "Series B preferred (Form D)", 15000003, "Kleiner Perkins", True, TC["rtr"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2011-05-23) reports Kleiner Perkins investing $15M after "
             "$16M from Highland and Bain Capital, and the company's own Form D for the round (first sale "
             "2011-05-13) covers Series B preferred, its third filed round. Growth, not the band's Series A. Focus "
             "was missing: clothing rental is Consumer & Marketplaces, as the Bain Capital Ventures and TCV rows."),
    cls("alienvault", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC["alienvault_c"],
        entry_date="2012-06-29", flags=D,
        rounds=[rnd("2012-01-31", "Series B", 8000000, "Trident Capital", False, TC["alienvault_b"], "press"),
                rnd("2012-06-29", "Series C", 22400000, "Kleiner Perkins; Sigma Partners", True, TC["alienvault_c"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2012-07-09) reports 'a $22.4 million series C round, led "
             "by Kleiner Perkins Caufield & Byers (KPCB) and Sigma Partners', with Trident and Adara as the existing "
             "investors; the January 2012 Series B was Trident's and does not name the firm. The entry is the "
             "Series C: Growth, not the band's Series A."),
    cls("agilyx", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC["agilyx"],
        entry_date="2011-04", flags=D,
        rounds=[rnd("2011-04", "Series B", 22000000, "Kleiner Perkins", True, TC["agilyx"], "press"),
                rnd("2011-12-16", "unnamed (Form D)", 25000000, None, None, fd("agilyx", "2011-12-16"), "filing")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2011-04-01) reports a $22M Series B in which 'Kleiner "
             "Perkins Caufield & Byers (KPCB) ... led the round' beside the original backer Chrysalix. The entry is "
             "the Series B of spring 2011: Growth, not the band's Series A, and it predates the December 2011 "
             "Form D the band read."),
    cls("uship", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC["uship"],
        entry_date="2012-12-18", flags=D,
        rounds=[rnd("2012-12-18", "Series C", 18000000, "Kleiner Perkins", True, TC["uship"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2012-12-19) reports an $18M Series C led by Kleiner "
             "Perkins as a new investor, 'Benchmark Capital and DAG Ventures invested in earlier rounds'. Growth, "
             "not the band's Series A."),
    cls("awarepoint", stage="Growth", stage_src="model", stage_conf="medium",
        stage_cite=fd("awarepoint", "2009-04-16"), flags=D,
        rounds=[rnd("2009-04-16", "Series D warrant (Form D)", 140000, None, None, fd("awarepoint", "2009-04-16"), "filing"),
                rnd("2011-08-08", "unnamed (Form D)", 19920372, None, True, fd("awarepoint", "2011-08-08"), "filing")],
        note="Duty 9 sweep (early Form D band): the company's own Form D of April 2009 covers a warrant for Series D "
             "preferred, and four more rounds are on file before the August 2011 round that first names the firm's "
             "partner, so the entry is the Series D or later: Growth, not the band's Series A. The 2011 round "
             "itself is not named in a source read (medium)."),
    cls("livongo", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=LIVONGO_S1, flags=D,
        rounds=[rnd("2015-03-25", "Series B (by sequence)", 19999999, None, True, fd("livongo", "2015-03-25"), "filing"),
                rnd("2016-04", "Series C", None, None, True, LIVONGO_S1, "filing")],
        note="Duty 9 sweep (early Form D band): the S-1 names the April 2016 financing Series C and the March 2017 "
             "one Series D, with KPCB Holdings a 5% holder adding only $1.0M and $0.1M in them, so its position "
             "comes from the $20M round first sold 2015-03-25 (Beth Seidenberg a director on that Form D), the "
             "round before the Series C; General Catalyst's row records the founding $10M Series A of 2014. The "
             "entry is the Series B: Growth, not the band's Series A. The 2015 round's name is read off the "
             "sequence, not a source (medium)."),
    # ---- Class A: the band named the wrong side of the Seed line
    cls("booyah", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC["booyah_a"],
        entry_date="2009", flags=D, extra=NO_GRAD,
        rounds=[rnd("2009", "Series A", 4500000, "Kleiner Perkins (iFund)", True, TC["booyah_a"], "press"),
                rnd("2010-05-14", "unnamed (Form D)", 20000000, "Accel", True, TC["booyah_b"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2009-07-28) says Booyah 'was recently awarded $4.5 "
             "million in Series A funding through Kleiner Perkins Caufield and Byers iFund'. The entry is a named "
             "Series A, not the band's Seed, so the row leaves the S2A cohort and its graduation is removed."),
    cls("dust-identity", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC["dust_seed"],
        entry_date="2018-11", grad="graduated", grad_src="web_verified", grad_cite=TC["dust_a"], grad_conf="high",
        flags=D,
        rounds=[rnd("2018-11", "Seed", 2300000, "Kleiner Perkins", True, TC["dust_seed"], "press"),
                rnd("2019-07", "Series A", 10000000, "Kleiner Perkins", True, TC["dust_a"], "press")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2018-11-14) reports a $2.3M seed led by Kleiner Perkins, "
             "and (2019-07-17) 'a $10 million Series A round led by Kleiner Perkins, which also led its $2.3 million "
             "seed round last year'. The entry is the Seed of 2018, as the firm's 2018 listing has it, not the "
             "band's Series A read off the 2019 filing. S2A: graduated on the named Series A."),
    cls("area-1-security", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=AREA1_SEED,
        entry_date="2014-05-05", grad="graduated", grad_src="web_verified", grad_cite=AREA1_A, grad_conf="high",
        flags=D,
        rounds=[rnd("2014-05-05", "Seed", 2500000, None, True, AREA1_SEED, "press"),
                rnd("2014-12-10", "Series A", 8000000, "Kleiner Perkins", True, AREA1_A, "company")],
        note="Duty 9 sweep (early Form D band): VentureBeat (2014-05-05) reports a $2.5M seed whose investors "
             "'include Kleiner Perkins Caufield & Byers, Cowboy Ventures, Data Collective Venture Capital, First "
             "Round Capital, Allegis Capital'; the company's release of 2014-12-10 announces the $8M round led by "
             "Ted Schlein of KPCB. The entry is the Seed, not the band's Series A read off the second filing, as "
             "the First Round row has it. S2A: graduated on the $8M Series A."),
    cls("spruce-health", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC["spruce"],
        entry_date="2013", grad="graduated", grad_src="web_verified", grad_cite=fd("spruce-health", "2014-09-17"),
        grad_conf="medium", flags=D,
        rounds=[rnd("2013", "Seed", 2000000, "Kleiner Perkins", True, TC["spruce"], "press"),
                rnd("2014-09-17", "unnamed (Form D, filed 2015-04-21)", 15000000, None, None,
                    fd("spruce-health", "2014-09-17"), "filing")],
        note="Duty 9 sweep (early Form D band): TechCrunch (2014-09-25) reports '$2 million in seed money for "
             "Spruce, led by his former firm', Kleiner Perkins, with Baseline and Cowboy; the firm dates its entry "
             "2013. The entry is the Seed, not the band's Series A read off the company's one Form D. S2A: "
             "graduated on that filing, $15M of equity first sold 2014-09-17, more than seven times the seed and "
             "above the $5M floor; the round is unnamed in a source read, so medium."),
    # ---- Class A: no documented round; the older-company rule withholds the band
    cls("corthera", stage="undetermined", flags=D,
        note=OLD + "Corthera listed with the firm in 2008, before the April 2009 filing. No source read names the "
                   "round the firm entered, so the stage is undetermined."),
    cls("icontrol-networks", stage="undetermined", flags=D,
        note=OLD + "The firm dates its entry 2008, before the June 2009 filing, and TechCrunch (2010-11-04) says "
                   "the company 'was first backed by Charles River Ventures'. No source read names the round the "
                   "firm entered, so the stage is undetermined."),
    cls("juvaris-biotherapeutics-inc", stage="undetermined", flags=D,
        note=OLD + "No source read names the round the firm entered, so the stage is undetermined."),
    cls("nodality", stage="undetermined", flags=D,
        note=OLD + "The firm listed it in 2008, before the October 2009 filing. No source read names the round the "
                   "firm entered, so the stage is undetermined."),
    cls("stoke", stage="undetermined", flags=D,
        note=OLD + "The $24.5M round of June 2008 is not a first round (the Sequoia row puts the first round in "
                   "2004-05). No source read names the round the firm entered, so the stage is undetermined."),
    cls("lilliputian-systems", stage="undetermined", flags=D,
        note=OLD + "The March 2009 filing's 'Series A Convertible Preferred' is a $27.9M round of a recapitalised "
                   "company the firm already listed in 2008. No source read names the round the firm entered, so "
                   "the stage is undetermined."),
    # ---- Class B: member rows with no focus
    cls("etched", focus="Industrial & Robotics",
        note="Duty 9 sweep (missing focus): AI inference chips; chips read Industrial & Robotics, as the Sequoia, "
             "Ribbit and Bain Capital Ventures rows."),
    cls("flextronics-international", focus="Industrial & Robotics",
        note="Duty 9 sweep (missing focus): contract electronics manufacturing, Industrial & Robotics."),
    cls("friendster", focus="Consumer & Marketplaces",
        note="Duty 9 sweep (missing focus): social network, Consumer & Marketplaces, as the Benchmark and Battery rows."),
    cls("granola", focus="AI & Applied AI",
        note="Duty 9 sweep (missing focus): AI meeting notes, AI & Applied AI, as the Lightspeed and Spark rows."),
    cls("graphiq", focus="Consumer & Marketplaces",
        note="Duty 9 sweep (missing focus): consumer comparison engine, Consumer & Marketplaces, as the findthebest "
             "row. This row and findthebest are one company (FindTheBest was renamed Graphiq in 2015)."),
    cls("greatpoint-energy", focus="Climate & Energy",
        note="Duty 9 sweep (missing focus): coal and biomass gasification, Climate & Energy, as the Khosla row."),
    cls("groupon", focus="Consumer & Marketplaces",
        note="Duty 9 sweep (missing focus): local deals marketplace, Consumer & Marketplaces, as five sibling rows."),
    cls("home-network", focus="Data Infrastructure",
        note="Duty 9 sweep (missing focus): broadband internet access over cable networks; networking reads Data "
             "Infrastructure (the Excite portal row stays Media, Gaming & Advertising)."),
    cls("houzz", focus="Consumer & Marketplaces",
        note="Duty 9 sweep (missing focus): home design marketplace, Consumer & Marketplaces, as the Sequoia, NEA and "
             "ICONIQ rows."),
    cls("pulmonx", focus="Healthcare & Bio",
        note="Duty 9 sweep (missing focus): lung valve devices, Healthcare & Bio."),
    cls("rapid-micro-biosystems", focus="Healthcare & Bio",
        note="Duty 9 sweep (missing focus): microbial quality control for drug manufacturing, Healthcare & Bio."),
    cls("shyp", focus="Consumer & Marketplaces",
        note="Duty 9 sweep (missing focus): on-demand shipping for consumers, Consumer & Marketplaces."),
    cls("silver-spring-networks", focus="Climate & Energy",
        note="Duty 9 sweep (missing focus): smart-grid networking for utilities, Climate & Energy, as the GV row."),
]

jl.write("dub", lines)
