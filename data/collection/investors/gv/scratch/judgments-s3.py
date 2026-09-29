#!/usr/bin/env python3
"""Stage sweep s3 (COLLECTION.md s8 duty 9; PRO-75, 2026-09-29): the undetermined-stage and unknown-status class,
50 rows. Settled here: 17 rows (stage on 13, status on 5; rodin, scout, kibits+collaborate carry both kinds of
evidence). Rows no source settles get no line. Notes carry only the new sentences (record appends).

Citations are read, never typed: press URLs come from jl.NEWS (decoded Google News items) or from a tool's printed
search result (TechCrunch's own search, lifescivc.com's month listing); SEC URLs are assembled from the accession and
document a full-text search printed (SEC()); Internet Archive captures from the timestamp and original URL a CDX
listing or a capture redirect printed (IA()). Every page cited was read in this session."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

S = "Stage sweep 2026-09-29: "
ASOF = "2026-09-29"


def SEC(cik, acc, doc=None):
    """An EDGAR document (or the filing index) from a CIK and an accession printed by a full-text search."""
    base = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/"
    return base + (doc if doc else f"{acc}-index.htm")


def IA(ts, url):
    """An Internet Archive capture from a timestamp and original URL printed by a CDX listing or redirect."""
    return f"http://web.archive.org/web/{ts}/{url}"


# ---- citations
LSVC_RODIN = "https://lifescivc.com/2019/11/thinking-boldly-alkermes-acquires-rodin-therapeutics/"
BPD_RODIN = jl.NEWS("rodin-therapeutics", "Alkermes follows up")
TC_BENTO = "https://techcrunch.com/2015/03/11/bento-labs/"
SCOUT_SHUT = IA("20160527025303", "https://medium.com/@BentoApp/scout-launcher-is-shutting-down-19d6cf7b88")
SCOUT_RENAME = IA("20150911194645", "https://medium.com/@BentoApp/bento-is-now-scout-afe7394cc868")
TC_JET = "https://techcrunch.com/2023/02/01/jetpack-io-helps-developers-focus-on-applications-instead-of-infrastructure/"
LAW_JET = jl.NEWS("jetify", "GC AI Acquires Backend Software Company Jetify")
BW_GS = jl.NEWS("groundswell", "Groundswell Announces A Total of")
BW_GS_IA = IA("20260314223450", "https://www.businesswire.com/news/home/20211130005365/en/"
                                 "Groundswell-Announces-A-Total-of-%2415M-in-Seed-Funding-To-Democratize-Philanthropy")
FD_GS = SEC(1899820, "0001899820-21-000001")
WIRED_PAGER = jl.NEWS("pager", "This App Gives Screenshots Superpowers")
FD_PAGER = SEC(1939419, "0001493152-22-020911")
TC_KIBITS = "https://techcrunch.com/2012/03/29/google-backed-kibits-lets-you-share-with-real-world-micro-networks-raises-1m/"
CISCO_S8 = SEC(858877, "0000858877-14-000004", "forms-8xkibits.htm")
CISCO_BLOG = jl.NEWS("collaborate", "Cisco Announces Acquisition of Collaborate.com")
COLLAB_2013 = IA("20130621071141", "http://www.collaborate.com:80/")
KIBITS_FWD = IA("20131120122856", "http://www.kibits.com/")
EFF_ORDRX = jl.NEWS("ordr-in", "Alice Arrives Too Late")
ORDRIN_FWD = IA("20150314141133", "http://www.ordrx.com/")
TINYRX_END = IA("20160530231213", "https://www.tinyrx.com/")
WEOTTA_END = IA("20170507105028", "http://www.weotta.com:80/?")
CRN_FLETCH = jl.NEWS("weotta", "F5 Buys Cybersecurity Upstart Fletch")
FIERCE_RANI = jl.NEWS("rani-therapeutics", "B is for biotech")
TC_SIGNOS_A = "https://techcrunch.com/2021/11/10/signos-series-a/"
TC_SIGNOS_B = "https://techcrunch.com/2023/10/24/signos-series-b/"
TC_CLUSTER = ("https://techcrunch.com/2013/08/22/photo-sharing-app-cluster-snags-instagram-seed-investor-steve-"
              "anderson-others-to-lead-1-6m-round-launches-version-1-0/")
TC_LAUNCHKIT = ("https://techcrunch.com/2016/07/27/launchkit-team-heads-to-google-and-open-sources-its-tools-for-"
                "helping-devs-launch-their-apps/")
TC_SUBTEXT = ("https://techcrunch.com/2011/10/25/subtext-raises-3-million-from-google-ventures-more-to-make-ebook-"
              "reading-social/")
VOX_SUBTEXT = jl.NEWS("subtext", "Google Capital Invests")
GVN_YUGA = jl.NEWS("yuga-labs", "Yuga Labs pulls in")
MBW_YUGA = jl.NEWS("yuga-labs", "Snoop Dogg, Google Ventures and Samsung")
FD_YUGA = SEC(1917607, "0001917607-22-000003")
TC_TRAVELJOY = ("https://techcrunch.com/2024/03/01/backed-by-10m-series-a-traveljoy-is-riding-the-post-covid-demand-"
                "for-expert-travel-planning/")
PRN_RESILIENCE = jl.NEWS("resilience", "RESILIENCE Launches to Change the Future")
FD_RESILIENCE = SEC(1834819, "0001567619-21-000473")

L = [
 # ---------------- stage: Growth / Series A from a page naming GV's round
 jl.cls("rodin-therapeutics", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=LSVC_RODIN,
        entry_date="2017",
        rounds=[jl.rnd("2013", "Seed", None, "Atlas Venture", False, LSVC_RODIN, "press"),
                jl.rnd("2014", "Series A", None, "Atlas Venture", False, LSVC_RODIN, "press"),
                jl.rnd("2016", "equity investment (Atlas Venture and Biogen)", 17300000, None, False, BPD_RODIN,
                       "press"),
                jl.rnd("2017", "Series B", 27000000, None, True, LSVC_RODIN, "press")],
        note=S + "Atlas's own blog (LifeSciVC, 2019-11-18, read 2026-09-29) confirms the lead: ending the Biogen "
                 "agreement in 2017 'enabled us to raise a Series B financing, bringing several great co-investors "
                 "to the story, including GV, Hatteras Venture Partners, Remeditex Ventures, and Third Point "
                 "Ventures', after the Atlas seed of 2013 and a Series A in 2014, and it names Ben Robbins at GV "
                 f"({LSVC_RODIN}). BioPharma Dive (2019-11-18) puts that round at $27 million in 2017, after a "
                 "$17.3 million equity investment by Atlas and Biogen in 2016. GV entered at the Series B: Growth "
                 "(web_verified)."),
 jl.cls("rani-therapeutics", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=FIERCE_RANI,
        entry_date="2013",
        rounds=[jl.rnd("2013", "Series B", None, None, True, FIERCE_RANI, "press")],
        note=S + "Fierce Biotech (2017-05-03) on GV's life-science record: 'In 2013, it also joined a Series B "
                 "round for Rani Therapeutics', the year the firm first lists Rani: GV entered at the Series B, "
                 "so Growth (web_verified, medium: a later summary, not the round's own announcement)."),
 jl.cls("resilience", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=PRN_RESILIENCE,
        entry_date="2020-10",
        rounds=[jl.rnd("2020-10-23", "Series B", 750000000, "ARCH Venture Partners and 8VC", True, PRN_RESILIENCE,
                       "company")],
        note=S + "The company's launch release (PR Newswire, 2020-11-23): 'RESILIENCE has raised over $800 million "
                 "of capital following the recent Series B raise of approximately $750 million ... Led by ARCH "
                 "Venture Partners and 8VC with participation by GV and NEA', with GV's David Schenkein a board "
                 "observer. The round's Form D (National Resilience, Inc., CIK 1834819, "
                 f"{FD_RESILIENCE}) reports $755,000,062 sold from 2020-10-23, the entry date. No source read puts "
                 "GV in the earlier money and the firm lists the company from 2021: Growth (web_verified, medium)."),
 jl.cls("signos", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=TC_SIGNOS_A,
        entry_date="2021-11-10",
        rounds=[jl.rnd("2021-01", "Seed", 4000000, "Courtside Ventures, 1984 Ventures and Tau Ventures", False,
                       TC_SIGNOS_A, "press"),
                jl.rnd("2021-11-10", "Series A", 13000000, "GV", True, TC_SIGNOS_A, "press"),
                jl.rnd("2023-10-24", "Series B", 20000000, "Cheyenne Ventures and GV", True, TC_SIGNOS_B, "press")],
        note=S + "TechCrunch (2021-11-10): Signos raised 'a $4 million seed funding led by Courtside Ventures, 1984 "
                 "Ventures and Tau Ventures back in January' and then 'a $13 million Series A led by GV': GV entered "
                 "at the Series A (web_verified); it co-led the $20M Series B of October 2023 (TechCrunch)."),

 # ---------------- stage: Seed from a page naming GV's round, with S2A
 jl.cls("scout", status="defunct", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_BENTO,
        entry_date="2015-03",
        grad="not_graduated", grad_src="first_party", grad_conf="high", grad_cite=SCOUT_SHUT, grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Scout -> archived 2015 to 2016 (Rich Miner); no post names the "
                  "company",
                  "formd: EDGAR full-text search for Bento Labs and the founder Nikhil Chandhok -> no Form D by the "
                  "company",
                  "techcrunch: TechCrunch's own search (Bento Labs, Scout launcher, Chandhok) -> only the "
                  "2015-03-11 seed story; no later round",
                  "googlenews: Google News ('Scout launcher'; Scout launcher shutting down; 2026-09-29) -> only "
                  "Notebookcheck's 2016-02-26 'Scout Android launcher shuts down'; no later round",
                  "company: the company's own blog (medium.com/@BentoApp in its Internet Archive captures) -> "
                  "'Introducing Bento', 'Bento is now Scout', a feature update and the 2016-02-23 shutdown post; no "
                  "funding news"],
        rounds=[jl.rnd("2015-03-11", "Seed", 2000000, None, True, TC_BENTO, "press")],
        note=S + "Scout is Bento Labs renamed: the company's post 'Bento is now Scout!' (2015-08-27, "
                 f"{SCOUT_RENAME}) says 'We are rebranding today as Scout', and its site linked the Play Store app "
                 "com.bento.launcher. TechCrunch (2015-03-11): the founders 'had raised $2 million in seed funding "
                 "from investors that include First Round Capital, Social+Capital, Google Ventures, Susa Ventures' "
                 "and angels: Seed (web_verified), dated by that article. The company's own post of 2016-02-23 "
                 f"({SCOUT_SHUT}): 'Scout Launcher will cease operations on March 2, 2016 ... all our servers will "
                 "be shut down': defunct. S2A: not graduated on a cited end; the seed was its last round."),
 jl.cls("jetify", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_JET, entry_date="2022",
        grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_cite=LAW_JET, grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Jetify (2025-2026, Erik Nordlander) -> no post names the company",
                  "formd: EDGAR full-text search for Jetpack Technologies, Jetify and the founder Daniel Loreto -> "
                  "no Form D by the company",
                  "techcrunch: TechCrunch's own search (Jetpack.io; Jetify) -> the 2023-02-01 seed story and the "
                  "2025-01-28 Testpilot launch; no later round",
                  "googlenews: Google News (Jetify and Jetpack.io with round and sale words, 2026-09-29) -> the "
                  "Testpilot launch and Law.com's 2026-08-10 report of the GC AI purchase; no later round",
                  "sibling:coatue: its row for Jetify -> acquired by GC AI in 2026; no later round in its note"],
        rounds=[jl.rnd("2022", "Seed", 10000000, "Coatue and GV", True, TC_JET, "press")],
        note=S + "TechCrunch (2023-02-01): Jetpack.io 'revealed a $10 million seed investment, which closed a year "
                 "ago, but was previously unannounced', and 'The $10 million seed was co-led by Coatue and GV': GV "
                 "entered at the seed (web_verified), which that article dates to 2022. 'GC AI quietly acquired "
                 "Jetify ... in June' 2026 (Law.com, 2026-08-10), with no round after the seed on any surface: not "
                 "graduated on a cited end. The GV row jetpack-technologies is the same company (Jetify Inc., "
                 "formerly Jetpack Technologies Inc.); it dates the seed 2023-02, the announcement."),
 jl.cls("groundswell", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=BW_GS,
        entry_date="2021-11-30",
        grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Groundswell -> listed from 2022 (M.G. Siegler); no post names "
                  "the company",
                  "formd: EDGAR for Groundswell Giving, Inc. (CIK 1899820) -> one Form D, $13,214,985 sold from "
                  "2021-11-23 (the seed); no later filing",
                  "googlenews: Google News (Groundswell with philanthropy, round and sale words, 2026-09-29) -> the "
                  "2021-11-30 seed release and a 2023-02-14 customer release; no later round",
                  "techcrunch: TechCrunch's own search (Groundswell, 2021-2026) -> nothing about this company",
                  "company: groundswell.io (read 2026-09-29) -> the operating product site; no funding news",
                  "sibling:felicis: its row for Groundswell -> S2A not_graduated (absence_check, 2026-09-20)"],
        rounds=[jl.rnd("2021-11-30", "Seed", 15000000, "GV", True, BW_GS, "company")],
        note=S + "Groundswell's release (Business Wire, 2021-11-30, read in its Internet Archive capture "
                 f"{BW_GS_IA}): it 'raised a total of $15M in seed investment funding. The round was led by GV "
                 "(formerly Google Ventures), with participation from Human Ventures, Moonshots Capital, Felicis "
                 "Ventures, and Core Innovation Capital': Seed (web_verified). Groundswell Giving, Inc. (CIK "
                 f"1899820, Redondo Beach) filed one Form D, $13.2M sold from 2021-11-23 ({FD_GS}), and none since. "
                 "S2A: not graduated on the absence test (2026-09-29), aligned with the Felicis row."),
 jl.cls("pager", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=WIRED_PAGER,
        entry_date="2022-11",
        grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Pager (2023-2026, M.G. Siegler) -> no post names the company",
                  "formd: EDGAR for Pager Technologies, Inc (CIK 1939419, New York) -> one Form D, $6,088,855 sold "
                  "from 2022-06-02 (the seed); no later filing",
                  "googlenews: Google News (Pager with screenshots, seed and GV, 2026-09-29) -> only WIRED's "
                  "2022-11-18 story on the seed; no later round",
                  "techcrunch: TechCrunch's own search (Pager, 2022-2023) -> nothing about this company",
                  "company: pager.xyz (checked 2026-09-29) -> no longer resolves; no later round announced"],
        rounds=[jl.rnd("2022-11-18", "Seed", 5200000, "GV (M.G. Siegler)", True, WIRED_PAGER, "press")],
        note=S + "WIRED (2022-11-18): 'M. G. Siegler, a general partner at GV (formerly known as Google Ventures) "
                 "who invested in Pager' and 'Pager has raised $5.2 million in seed funding, with Siegler leading "
                 "the funding round': GV led the seed (web_verified). The company is Pager Technologies, Inc (CIK "
                 f"1939419, New York; CEO Alexander Mahedy), whose only Form D ({FD_PAGER}) reports $6.09M sold from "
                 "2022-06-02. S2A: not graduated on the absence test (2026-09-29). Status stays unknown: no source "
                 "read gives the fate."),
 jl.cls("collaborate", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_KIBITS,
        entry_date="2011",
        grad="not_graduated", grad_src="web_verified", grad_conf="high", grad_cite=CISCO_S8, grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Collaborate -> 2013 to 2015 (Rich Miner) with the exit line "
                  "'Acquired by Cisco, 2013'; no post names a round",
                  "formd: EDGAR full-text search for Kibits and Collaborate.com -> no Form D by the company; Cisco's "
                  "S-8 of 2014-01-07 for the assumed Kibits Corp. 2011 plan",
                  "techcrunch: TechCrunch's own search (Kibits; Collaborate.com) -> only the 2012-03-29 seed story; "
                  "no later round",
                  "googlenews: Google News (Kibits with sale and round words; Collaborate.com with Kibits, Boston "
                  "and the founders; 2026-09-29) -> Cisco's 2013-12-17 acquisition post; no later round",
                  "company: collaborate.com in its 2013 Internet Archive captures (footer '© 2013 Kibits Corp.') -> "
                  "no funding news",
                  "sibling:general-catalyst: its row for Collaborate.com -> no later round in its note"],
        rounds=[jl.rnd("2011", "Seed", 1000000, None, True, TC_KIBITS, "press")],
        note=S + "Collaborate.com was Kibits Corp.: its 2013 pages carry '© 2013 Kibits Corp.' "
                 f"({COLLAB_2013}), kibits.com forwarded there from November 2013 ({KIBITS_FWD}), and Cisco's S-8 "
                 f"of 2014-01-07 ({CISCO_S8}) registers options 'under the Kibits Corp. 2011 Equity Incentive Plan, "
                 "and assumed by the Registrant on December 16, 2013 pursuant to an Agreement and Plan of Merger by "
                 "and among the Registrant, Cougar Acquisition Corp., Kibits Corp.'. TechCrunch (2012-03-29) names "
                 "Kibits' investors as 'including Google Ventures and Charles River Ventures' and its '$1 million "
                 "round of seed funding from Google, CRV, General Catalyst' and others, 'raised near the beginning "
                 "of the company's one-year history': Seed (web_verified), entry 2011. Cisco bought it in December "
                 "2013 (its blog post of 2013-12-17) with no later round on any surface: not graduated on a cited "
                 "end. The GV row kibits is the same company; its entry date reads 2012-03, the announcement."),
 jl.cls("launchkit", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_CLUSTER,
        entry_date="2013-08-22",
        grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for LaunchKit (2016-2026, exit line 'Acquired by Google, 2016') -> "
                  "no post names a later round",
                  "formd: EDGAR full-text search for Cluster Labs and LaunchKit -> no Form D by the company",
                  "techcrunch: TechCrunch's own search (Cluster; LaunchKit) -> the $1.6M seed (2013-08-22), product "
                  "stories 2013-2015 and the 2016-07-27 story on the team joining Google ('raised a total of $2.2 "
                  "million', $1.6M for Cluster and $600,000 after the pivot); no Series A",
                  "googlenews: Google News (Cluster with its founders' names and round words, 2026-09-29) -> no "
                  "later round",
                  "sibling:first-round-capital: its row for LaunchKit -> S2A not_graduated (web_verified); no priced "
                  "round before the 2016 wind-down in its note"],
        rounds=[jl.rnd("2013-08-22", "Seed", 1600000, "Baseline Ventures (Steve Anderson)", True, TC_CLUSTER,
                       "press")],
        note=S + "LaunchKit is Cluster's company after its pivot: 'The team raised a total of $2.2 million ($1.6 "
                 "million for Cluster and an additional $600,000 after it decided to focus on LaunchKit)', GV among "
                 f"the investors (TechCrunch, 2016-07-27, {TC_LAUNCHKIT}). TechCrunch (2013-08-22): Cluster "
                 "announced '$1.6 million in seed funding in a round led by ... Steve Anderson of Baseline "
                 "Ventures. Also participating were Freestyle Capital, First Round Capital, Google Ventures, and "
                 "Sherpa Ventures', its 'first outside investment': Seed (web_verified). S2A: not graduated on the "
                 "absence test (2026-09-29); the $600,000 after the pivot is far below the $5M step-up. The GV row "
                 "cluster is the same company and reads private (the app runs on under its makers' Fotoloce) while "
                 "this row reads defunct; the two need one status."),
 jl.cls("subtext", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=TC_SUBTEXT,
        entry_date="2011-10",
        grad="not_graduated", grad_src="web_verified", grad_conf="medium", grad_cite=VOX_SUBTEXT, grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Subtext (2012-2026, Karim Faris) -> the exit line 'Acquired by "
                  "Renaissance Learning, 2013'; no post names a round",
                  "formd: EDGAR full-text search for Subtext (2009-2014) -> no Form D by the company",
                  "techcrunch: TechCrunch's own search (Subtext ebook) -> only the 2011-10-25 seed story; no later "
                  "round",
                  "googlenews: Google News (Subtext with Renaissance Learning; with ebook round and sale words; "
                  "2026-09-29) -> only Vox's 2014-02-19 note of the purchase; no later round"],
        rounds=[jl.rnd("2011-10-25", "Seed", 3000000, None, True, TC_SUBTEXT, "press")],
        note=S + "TechCrunch (2011-10-25): Subtext's investors 'now includes Google Ventures, Mayfield Fund, New "
                 "Enterprise Associates (NEA) and Omidyar Network, which have collectively poured $3 million of "
                 "seed funding into the startup': Seed (web_verified). Renaissance Learning bought it (Vox, "
                 "2014-02-19: 'the company bought e-reading tool Subtext, a Google Ventures investment'; the firm's "
                 "exit line dates it 2013) with no round after the seed on any surface: not graduated on a cited "
                 "end (medium: the sale is reported in passing)."),
 jl.cls("yuga-labs", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=GVN_YUGA,
        entry_date="2022-03-22",
        grad="not_graduated", grad_src="absence_check", grad_asof=ASOF,
        surfaces=["firm: the firm's own listing for Yuga Labs (2022-2026, David Krane, Tom Hulme) -> no post names "
                  "the company",
                  "formd: EDGAR for Yuga Labs, Inc. (CIK 1917607, Coral Gables) -> one Form D, $424,091,159 sold of "
                  "$450M from 2022-03-07 (the seed); no later filing",
                  "googlenews: Google News (Yuga Labs with round and valuation words, 2026-09-29) -> the March 2022 "
                  "seed, a CEO change, layoffs, IP sales and a 2026 report of an SEC probe; no later priced round",
                  "techcrunch: TechCrunch's own search (Yuga Labs, 2023-2026) -> no later round",
                  "sibling:a16z: its row for Yuga Labs -> S2A not_graduated (absence_check, 2026-09-20)",
                  "sibling:lightspeed: its row for Yuga Labs -> S2A not_graduated (absence_check, 2026-09-20)"],
        rounds=[jl.rnd("2022-03-22", "Seed", 450000000, "a16z crypto", True, GVN_YUGA, "press")],
        note=S + "Global Venturing (2022-03-23): Yuga Labs 'secured $450m yesterday in a seed round' at a $4bn "
                 "post-money valuation, and 'FTX, Alphabet and Adidas invested through FTX Ventures, GV and Adidas "
                 f"Ventures respectively'; Music Business Worldwide's headline of 2022-03-22 ({MBW_YUGA}) also puts "
                 "Google Ventures in the $450m seed: Seed (web_verified). Yuga Labs, Inc. (CIK 1917607) filed one "
                 f"Form D ({FD_YUGA}). The $4B mark was set by that seed (s6's exception to rule 7). S2A: not "
                 "graduated on the absence test (2026-09-29), aligned with the a16z and Lightspeed rows."),

 # ---------------- stage: Seed by the listing bound (lead's rule of 2026-09-29), with S2A
 jl.cls("traveljoy", stage="Seed", stage_src="model", stage_conf="low", entry_date="2019",
        grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=TC_TRAVELJOY,
        flags=["stage_uncited"],
        rounds=[jl.rnd("2019", "Seed", None, None, None, TC_TRAVELJOY, "press"),
                jl.rnd("2023", "Series A", 10000000, "Acrew Capital", None, TC_TRAVELJOY, "press")],
        note=S + "the firm listed TravelJoy from its May 2019 capture, and the only financing on record by then is "
                 "the 2019 round TechCrunch (2024-03-01) calls its seed ('just getting off the ground in 2019, "
                 "raising its seed round'), so GV entered at the seed (model, low: no page names GV in it). The same "
                 "article reports 'a $10 million Series A' raised 'a little over a year ago', led by Acrew Capital's "
                 "Theresia Gouw: graduated."),

 # ---------------- status only
 jl.cls("kibits", status="acquired",
        note=S + "Kibits became Collaborate.com: the collaborate.com pages of 2013 carry '© 2013 Kibits Corp.' "
                 f"({COLLAB_2013}) and kibits.com forwarded there from November 2013 ({KIBITS_FWD}). Cisco bought "
                 f"it: Cisco's S-8 of 2014-01-07 ({CISCO_S8}) registers options under the Kibits Corp. 2011 Equity "
                 "Incentive Plan assumed under a merger agreement with Kibits Corp. dated 2013-12-16, and Cisco "
                 f"announced the Collaborate.com acquisition on 2013-12-17 ({CISCO_BLOG}): acquired. The GV row "
                 "collaborate is the same company."),
 jl.cls("ordr-in", status="defunct",
        note=S + "Ordr.in became Ordrx: by 2015 ordr.in forwarded to ordrx.com ('Copyright © 2015 Ordrx', 79 "
                 f"Madison Avenue, New York; {ORDRIN_FWD}), and the EFF (2017-09-07, {EFF_ORDRX}) writes that "
                 "David Bloom, Ordr.in's CEO in TechCrunch's 2011 seed story, founded Ordrx in 2011, that patent "
                 "litigation drained it and that 'Growth stalled, and then Ordrx folded', before November 2016: "
                 "defunct. The Ordrx name shows no later round either (Google News, TechCrunch, EDGAR)."),
 jl.cls("tinyrx", status="defunct", city="San Francisco", city_src="web_verified",
        note=S + f"the company's own site ({TINYRX_END}): 'As of Friday May 6th, the TinyRx home delivery service "
                 "will no longer be operational', signed by the TinyRx team at 525 Brannan Street, San Francisco; "
                 "tinyrx.com had expired by April 2017: defunct, San Francisco."),
 jl.cls("weotta", status="defunct",
        note=S + f"the company's own site ({WEOTTA_END}): 'Goodbye. Weotta is no more. After many years the team "
                 "has decided to focus their time on solving other hard things', pointing to its team's later "
                 "projects: defunct. Its CEO Grant Wernick later led Fletch, which F5 bought in June 2025 (CRN, "
                 f"{CRN_FLETCH}); no source read says Fletch continues Weotta's company."),
]
jl.write("s3", L)
