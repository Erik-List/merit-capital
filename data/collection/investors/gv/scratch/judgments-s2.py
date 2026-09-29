#!/usr/bin/env python3
"""Stage sweep s2 (COLLECTION.md s8 duty 9; PRO-75, 2026-09-29): the undetermined-stage and unknown-status class,
50 rows (SWEEP-BRIEF.md). Sixteen rows get a named entry round, six of them Seed entries decided for S2A; the other
rows keep their stage or status (no source names GV's round or the company's fate) and get no line. Notes carry only
the new sentences (record appends). Every URL below was printed by a tool run in this session (TechCrunch's own
search, Google News decoding, the Wayback CDX index, EDGAR) and read before it is cited.

Run ONCE from the scratch directory: NQ_TAG=s2 python3 judgments-s2.py. `record` replaces a stored note with the new
sentence when that sentence is already in it, so a second successful run would drop the older note text."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

S = "Stage sweep 2026-09-29: "
ASOF = "2026-09-29"
C = json.loads((jl.INV / "companies" / "classification.json").read_text())


def R(slug, fix=None, add=()):
    """The row's stored funding_rounds, entry i updated with fix[i], the new rounds appended, sorted by date."""
    out = [dict(r) for r in (C.get(slug, {}).get("funding_rounds") or [])]
    for i, f in (fix or {}).items():
        out[i].update(f)
    out += list(add)
    return sorted(out, key=lambda r: str(r.get("date") or ""))


rnd = jl.rnd

# ---- citations (printed by the tools, read before use)
TC_99 = "https://techcrunch.com/2022/02/22/99-counties-regenerative-agriculture-meat-marketplace/"
FIERCE_GV17 = "https://www.fiercebiotech.com/biotech/b-for-biotech-alphabet-and-its-search-for-life-science-glory"
TC_BT19 = ("https://techcrunch.com/2019/06/13/gv-joins-in-another-76-million-for-neurobehavioral-health-company-"
           "blackthorns-plan-to-treat-mental-disorders/")
TC_COZY12 = "https://techcrunch.com/2012/10/04/cozy-funding/"
TC_COZY14 = "https://techcrunch.com/2014/02/11/cozy-credit-reporting/"
HN_FAUNA = "https://hackernoon.com/founder-interveiws-evan-weaver-of-fauna-73f9e220ea91"
TC_HIRED14 = "https://techcrunch.com/2014/03/24/hired-raises-15m-series-a/"
FORBES_KENSHO = ("http://web.archive.org/web/20141127194020/http://www.forbes.com:80/sites/stevenbertoni/2014/11/24/"
                 "goldman-sachs-leads-15-million-investment-in-tech-start-up-kensho/")
TC_KENSHO18 = "https://techcrunch.com/2018/03/07/sp-global-snares-kensho-for-550-million/"
FD_NEURA17 = "https://www.sec.gov/Archives/edgar/data/1708503/000170850317000001/0001708503-17-000001-index.htm"
FD_NEURA19 = "https://www.sec.gov/Archives/edgar/data/1708503/000170850319000001/0001708503-19-000001-index.htm"
W_NGMOCO = jl.W("Ngmoco")
W_GV = jl.W("GV (company)")
FIERCE_OBS = "https://www.fiercebiotech.com/biotech/biotech-vet-gilman-back-heading-up-next-gen-car-t-startup-obsidian"
TC_POCKET12 = ("https://techcrunch.com/2012/07/19/pocket-raises-5m-series-b-plans-to-bring-its-save-for-later-app-to-"
               "more-devices-and-platforms/")
TC_RES14 = ("https://techcrunch.com/2014/10/28/reserve-from-startup-studio-expa-makes-restaurant-reservations-easier-"
            "than-ever/")
TC_RES15 = "https://techcrunch.com/2015/02/11/reserve-series-a/"
TC_ST11 = "https://techcrunch.com/2011/03/11/soundtracking/"
TC_ST_A = ("https://techcrunch.com/2011/11/08/accel-true-ventures-and-softbank-plunk-4-75m-into-music-sharing-app-"
           "soundtracking/")
TC_OC10 = ("https://techcrunch.com/2010/04/21/opencandy-raises-5-million-series-b-for-bundled-software-you-might-"
           "actually-want/")
TC_SL11 = ("https://techcrunch.com/2011/09/29/sweetlabs-raises-13-million-from-intel-google-and-others-for-pokki-app-"
           "platform/")
TC_TN = "https://techcrunch.com/2011/07/26/thinknear-1-6-million-launches/"
TC_TP = ("https://techcrunch.com/2011/02/23/energy-efficiency-startup-transphorm-emerges-from-stealth-raises-20-"
         "million-from-google-ventures/")
TC_WUT = "https://techcrunch.com/2014/06/11/wut-round/"

L = [
 # ---------------------------------------------------------------- Pre-Seed
 jl.cls("99-counties", stage="Pre-Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_99,
        entry_date="2022-02",
        rounds=R("99-counties", fix={0: {"round": "Pre-Seed", "lead": "OMERS Ventures", "firm_in_round": True}}),
        note=S + "TechCrunch (2022-02-22) reports 'the recent closure of $3.8 million of pre-seed funding in a round "
                 "led by OMERS Ventures, with participation from Union Labs, GV and Supply Change Capital': GV entered "
                 "at the pre-seed, the round on the company's one Form D (first sale 2022-02-08, $3.72M sold). A "
                 "Pre-Seed entry is outside the S2A cohort."),

 # ---------------------------------------------------------------- Seed, decided for S2A
 jl.cls("cozy", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=TC_COZY12,
        entry_date="2012-10-04",
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_COZY14,
        rounds=R("cozy", fix={2: {"firm_in_round": True}},
                 add=[rnd("2012-10-04", "Seed", 1500000, "Social+Capital Partnership", True, TC_COZY12, "press")]),
        note=S + "TechCrunch (2012-10-04): Cozy 'has raised $1.5 million in seed funding', led by the Social+Capital "
                 "Partnership, with 'Google Ventures (Kevin Rose is Google's partner on the deal)': GV entered at the "
                 "seed. Medium, because TechCrunch's 2016 Series B story calls the same round 'the company's $1.5 "
                 "million Series A in 2012', against the 2012 report and TechCrunch's 2014 statement that Cozy 'raised "
                 "a Series A led by General Catalyst last year'. S2A: graduated on that named 2013 Series A "
                 "(TechCrunch, 2014-02-11); every investor in the 2012 round joined the $8.5M Series B of August 2016."),
 jl.cls("hired", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_HIRED14,
        entry_date="2013-03-14",
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_HIRED14,
        rounds=R("hired", fix={0: {"round": "Seed"}, 1: {"round": "Series B (Form D, $14.98M sold)"}},
                 add=[rnd("2014-03-24", "Series A", 15000000, "Crosslink Capital and Sierra Ventures", None,
                          TC_HIRED14, "press")]),
        note=S + "TechCrunch (2014-03-24): Hired, formerly DeveloperAuction, 'previously raised $2.7 million in seed "
                 "funding from SoftTech, New Enterprise Associates, Google Ventures, Sierra Ventures, Crosslink "
                 "Capital, and Haystack', the round TechCrunch reported on 2013-03-14: GV entered at the seed. S2A: "
                 "graduated on the named $15M Series A led by Crosslink and Sierra Ventures (the same story); the "
                 "November 2014 Form D ($14.98M sold) is the $15M Series B TechCrunch reported on 2014-12-09."),
 jl.cls("kensho", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=FORBES_KENSHO,
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_KENSHO18,
        rounds=R("kensho", fix={0: {"round": "Seed", "amount_usd": 10000000, "source": FORBES_KENSHO,
                                    "source_type": "press"}},
                 add=[rnd("2017-02", "unnamed", 50000000, "S&P Global", None, TC_KENSHO18, "press")]),
        note=S + "Forbes (2014-11-24, read from its archived copy): 'Kensho had previously raised a $10 million seed "
                 "round from the likes of Accel Partners, Breyer Capital, General Catalyst, Google Ventures and NEA', "
                 "the round on the company's first Form D (convertible notes, first sale 2013-11-07; $10.08M sold by "
                 "March 2014) and the firm's own '2013': GV entered at the seed. S2A: graduated; after Goldman Sachs "
                 "led $15M in November 2014, S&P Global led a $50M round in February 2017 (TechCrunch, 2018-03-07), "
                 "more than twice the $10M seed."),
 jl.cls("reserve", stage="Seed", stage_src="web_verified", stage_conf="medium", stage_cite=TC_RES14,
        entry_date="2014",
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_RES15,
        rounds=R("reserve", fix={0: {"date": "2014", "round": "pre-Series A (seed)", "firm_in_round": True,
                                     "source": TC_RES14}}),
        note=S + "TechCrunch (2014-10-28): the company was 'pre-Series A', with investors including Expa, First Round "
                 "Capital, Lowercase Capital, Sherpa Ventures, Advancit Capital, Homebrew, Box Group and Google "
                 "Ventures: GV entered at the seed (about $2.3M, the $17.3M raised by February 2015 less the $15M "
                 "Series A). Medium: the article neither dates nor sizes that funding. S2A: graduated on the named "
                 "$15M Series A led by Human Ventures and Expa (TechCrunch, 2015-02-11)."),
 jl.cls("schematic-labs", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_ST11,
        entry_date="2010",
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_ST_A,
        rounds=[rnd("2010", "Seed", 1100000, None, True, TC_ST_A, "press"),
                rnd("2011-11-08", "Series A", 4750000, "Accel Partners, True Ventures and SoftBank Capital", None,
                    TC_ST_A, "press")],
        note=S + "TechCrunch (2011-03-11): 'Schematic Labs raised a seed round late last year. Investors include True "
                 "Ventures, Google Ventures, AOL Ventures', a $1.1M seed (TechCrunch, 2011-11-08): GV entered at the "
                 "seed. S2A: graduated on the named $4.75M Series A led by Accel Partners, True Ventures and SoftBank "
                 "Capital (TechCrunch, 2011-11-08)."),
 jl.cls("wut", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_WUT,
        entry_date="2014-06-11",
        grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=ASOF,
        surfaces=jl.GRADLINES(
            "wut",
            firm_note="the firm's own listings for WUT (2014 to 2016 captures, partner M.G. Siegler) -> no post "
                      "names the company or a later round",
            formd_note="EDGAR company search for 'WUT, Inc' and 'Wut Inc' -> no filing by the company",
            extra=["techcrunch: TechCrunch's own search ('Wut app', 2014 on) -> the 2014-02-07 launch story, the "
                   "2014-06-11 seed and a 2014-12-18 roundup that lists WUT among anonymous apps 'no longer "
                   "ranked'; no later round",
                   "googlenews: Google News ('\"Wut\" app anonymous (raises OR funding OR seed)') -> one result, a "
                   "2014-06-13 New York Magazine guide to anonymous apps; no later round",
                   "company: wutwut.com -> a registrar's suspension page (read 2026-09-29); no newsroom and no later "
                   "news"]),
        rounds=[rnd("2014-06-11", "Seed", None, "Foundation Capital", True, TC_WUT, "press")],
        note=S + "TechCrunch (2014-06-11): WUT 'has raised seed funding from Foundation Capital with participation "
                 "from Google Ventures': GV entered at the seed. S2A: not graduated on the absence test (searched "
                 "2026-09-29): no later round on any surface; TechCrunch's 2014-12-18 roundup lists WUT among "
                 "anonymous apps 'no longer ranked', and wutwut.com shows a registrar's suspension page. Status left "
                 "unknown: no source reports a shutdown."),

 # ---------------------------------------------------------------- Series A
 jl.cls("blackthorn-therapeutics", stage="Series A", stage_src="web_verified", stage_conf="medium",
        stage_cite=FIERCE_GV17, entry_date="2017-01",
        rounds=R("blackthorn-therapeutics", fix={0: {"round": "Series B", "source": TC_BT19}},
                 add=[rnd("2017-01", "Series A (extension)", None, None, True, FIERCE_GV17, "press")]),
        note=S + "Fierce Biotech (2017-05-03) reports GV 'starting off in January with funding for an extended Series "
                 "A for BlackThorn Therapeutics'; the firm lists BlackThorn from 2017, and GV was already an investor "
                 "when the $76M Series B closed (TechCrunch, 2019-06-13). GV entered at the Series A, in its January "
                 "2017 extension (medium: the extension's own release was not found)."),
 jl.cls("fauna", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=HN_FAUNA,
        entry_date="2017-08-31",
        rounds=R("fauna", fix={0: {"round": "Seed ($3.1M sold)", "firm_in_round": False},
                               1: {"firm_in_round": True}}),
        note=S + "CEO Evan Weaver (HackerNoon, 2018-09-07): 'In 2016, we raised our seed round from CRV' and, about a "
                 "year before the interview, 'our A round from Point72 and Google Ventures': GV entered at the Series "
                 "A, the $25M round on the company's Form D (first sale 2017-08-31, $21.75M sold, Point72's Daniel "
                 "Gwak a director)."),
 jl.cls("obsidian-therapeutics", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FIERCE_OBS,
        entry_date="2017-11-29",
        rounds=R("obsidian-therapeutics", fix={0: {"date": "2017-11-29", "round": "Series A", "amount_usd": 49500000,
                                                   "lead": "GV", "firm_in_round": True, "source": FIERCE_OBS}}),
        note=S + "Fierce Biotech (2017-12-06): Obsidian 'just came out of stealth with a $49.5 million series A' and "
                 "'the series A financing was led by GV, with participation from Atlas Ventures, Takeda Ventures, "
                 "Vertex Ventures HC, Amgen Ventures, Alexandria Venture Investments and ShangPharma Investment "
                 "Group'; the firm lists it from its January 2018 capture: GV entered at the Series A (the company's "
                 "Form D, first sale 2017-11-29, $32.4M sold of $49.9M)."),
 jl.cls("pocket", stage="Series A", stage_src="model", stage_conf="medium", stage_cite=TC_POCKET12,
        entry_date="2011-07-26",
        rounds=R("pocket", fix={0: {"round": "unnamed (first external funding); the Series A by position"},
                                1: {"date": "2012-07-19", "round": "Series B", "lead": "Foundation Capital",
                                    "firm_in_round": True, "source": TC_POCKET12}}),
        note=S + "TechCrunch (2012-07-19) calls the $5M round led by Foundation Capital, with Baseline Ventures and "
                 "Google Ventures, a 'series B', following 'a previous funding round of $2.5m, which all three VC firms "
                 "participated in'; that July 2011 round was the company's first external funding (TechCrunch, "
                 "2011-07-26). The round GV entered is therefore the Series A (model, medium: named from the company's "
                 "later naming of the B)."),
 jl.cls("thinknear", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_TN,
        entry_date="2011-07-26",
        rounds=[rnd("2011-07-26", "Series A", 1630000, "IA Ventures", True, TC_TN, "press")],
        note=S + "TechCrunch (2011-07-26): ThinkNear 'raised $1.63 million in a series A', led by IA Ventures and "
                 "including Google Ventures: GV entered at the Series A (the label follows the record, not the check "
                 "size)."),

 # ---------------------------------------------------------------- Growth
 jl.cls("sweetlabs", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_OC10,
        entry_date="2010-04-21",
        rounds=[rnd("2008", "Series A", 3500000, None, False, TC_OC10, "press"),
                rnd("2010-04-21", "Series B", 5000000, "Google Ventures", True, TC_OC10, "press"),
                rnd("2011-09-29", "Series C", 13000000, "Intel Capital", True, TC_SL11, "press")],
        note=S + "OpenCandy is SweetLabs' earlier name (TechCrunch 2011-06-28, 'OpenCandy's Pokki'; 2011-09-29, "
                 "'SweetLabs, the San Diego company behind the Pokki app platform and the OpenCandy advertising "
                 "network'). TechCrunch (2010-04-21): OpenCandy 'closed a $5 million Series B funding round led by "
                 "Google Ventures, with existing investors Bessemer Venture Partners and O'Reilly Alpha Tech', after "
                 "'a $3.5 million Series A round in 2008': GV entered at the Series B, which reads Growth; it followed "
                 "in the $13M Series C of 2011 (TechCrunch, 2011-09-29)."),
 jl.cls("transphorm", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=TC_TP,
        rounds=R("transphorm", fix={0: {"round": "Series C", "lead": "Google Ventures"}}),
        note=S + "TechCrunch (2011-02-23): Transphorm 'has just closed a $20 million Series C funding round led by "
                 "Google Ventures, with participation from existing investors Kleiner Perkins Caufield & Byers, "
                 "Foundation Capital, and Lux Capital', bringing its total to $38M: GV entered at the Series C, which "
                 "reads Growth. It is the April 2010 Form D ($20.2M, Wesley Chan a director) whose date the row "
                 "already carries."),
 jl.cls("neuralink", stage="Growth", stage_src="model", stage_conf="medium", stage_cite=FD_NEURA19,
        rounds=R("neuralink", fix={0: {"round": "unnamed; the Series B by position ($39.31M sold on its Form D)"}},
                 add=[rnd("2017-08-15", "unnamed (Form D, $26.96M sold)", 26958000, None, None, FD_NEURA17,
                          "filing")]),
        note=S + "The firm's own /ai list dates GV's first investment to May 2019 and its second to July 2021. "
                 "Neuralink's Form Ds show one round per financing: August 2017 ($26.96M sold), April 2019 ($39.31M "
                 "sold of $51.31M, filed 2019-05-10), 2021 ($205.9M, the round the company named its Series C, which "
                 "included GV: 9to5Google, 2021-07-29), 2023, and 2025 (the $650M Series E, TechCrunch, 2025-06-02). "
                 "GV's May 2019 round is therefore the Series B, and one earlier filing with $39.3M above the era's "
                 "$30M Series A ceiling reads Growth on the structural rule too: Growth (model, medium; no page names "
                 "the 2019 round)."),
 jl.cls("ngmoco", stage="Growth", stage_src="model", stage_conf="low",
        rounds=R("ngmoco", add=[rnd("2008-06", "first round (iFund)", None, "Kleiner Perkins Caufield & Byers", False,
                                    W_NGMOCO, "press"),
                                rnd("2008-10", "second round", 10000000, "Norwest Venture Partners", False, W_NGMOCO,
                                    "press")]),
        note=S + "Google Ventures was founded on 31 March 2009 (Wikipedia, " + W_GV + "), after ngmoco's first two "
                 "rounds, June 2008 from Kleiner Perkins' iFund and October 2008, Norwest's $10M second round "
                 "(Wikipedia, " + W_NGMOCO + "); the next was the $25M Series C led by Institutional Venture Partners "
                 "without GV, and DeNA bought the company in October 2010. Any GV money therefore went in at the "
                 "Series B or later, which reads Growth (model, low: no source names GV's round, and its date is not "
                 "on record)."),
]
jl.write("s2", L)
