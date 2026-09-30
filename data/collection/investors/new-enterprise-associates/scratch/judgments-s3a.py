"""PRO-100 NEA, stage pass s3, first half of queue/s3.json (52 rows): the entry round NEA first invested in,
with the funding history found (COLLECTION.md s6, PRO-143). Run: NQ_TAG=s3 python3 judgments-s3a.py"""
import json

import judge_lib as jl

C = json.loads((jl.INV / "companies/classification.json").read_text())
Q = json.loads((jl.Q / "s3.json").read_text())["slugs"]
rnd = jl.rnd
L = []


def R(slug, *new, drop=()):
    """The rounds already on the row (minus any named in `drop`) plus the ones found here, date order."""
    out = [r for r in (C.get(slug, {}).get("funding_rounds") or []) if r.get("round") not in drop]
    for r in new:
        if not any(o.get("date") == r["date"] and o.get("round") == r["round"] for o in out):
            out.append(r)
    return sorted(out, key=lambda r: str(r.get("date") or ""))


def U(slug, note, *new, drop=(), entry_date=None):
    """An undetermined stage with the rounds found and what was searched."""
    L.append(jl.cls(slug, stage="undetermined", rounds=R(slug, *new, drop=drop), entry_date=entry_date, note=note))


def S(slug, stage, src, cite, conf, entry_date, note, *new, drop=(), flags=()):
    L.append(jl.cls(slug, stage=stage, stage_src=src, stage_cite=cite, stage_conf=conf, entry_date=entry_date,
                    rounds=R(slug, *new, drop=drop), note=note, flags=flags))


NQ = "Google News (nq.py)"

# ---------------------------------------------------------------- $1B+ rows
U("iobeam", f"Stage pass 2026-09-30: {NQ} for iobeam and Timescale with NEA, and one web search, found no source "
  "naming the round NEA entered in 2015 (the 2018 Series A of $12.4M is a later round); stage stays undetermined.",
  rnd("2018-01-24", "Series A", 12400000, None, None, None, "press"))

HZ = "https://www.vcnewsdaily.com/access/getarticle.php?aid=svbfgypndf"
VB = "https://venturebeat.com/2013/01/29/houzz-raises-35m-to-inspire-better-homes-and-gardens/"
S("houzz", "Growth", "web_verified", HZ, "high", "2013-01-29",
  "NEA and GGV Capital co-led Houzz's $35M Series C announced 2013-01-29 (VC News Daily); VentureBeat calls it the "
  "third round, after the Series B Sequoia led in December 2011. The firm's 2012 year rules out the earlier rounds "
  "and reads as this round's close. The sibling Sequoia row calls the 2011 round a Series A, against VentureBeat's "
  "Series B.",
  rnd("2011-12", "Series B", None, "Sequoia Capital", None, VB, "press"),
  rnd("2013-01-29", "Series C", 35000000, "New Enterprise Associates; GGV Capital", True, HZ, "press"),
  drop=("Series A",))

U("sitime", f"Stage pass 2026-09-30: {NQ} and one web search for SiTime's early rounds with NEA and Greylock found "
  "no source naming NEA's 2004 round (the company dates its founding to 2005; the Form D filings of 2009 and 2011 "
  "are later rounds); stage stays undetermined.")

U("vertex-pharmaceuticals", "Stage pass 2026-09-30: Vertex's 1989 founding round predates EDGAR and no press item "
  "or Wikipedia sentence names NEA's round; stage stays undetermined.")

# ---------------------------------------------------------------- public rows
FB = "https://www.fiercebiotech.com/biotech/3-v-biosciences-raises-30-million"
S("sagimet-biosciences", "Growth", "web_verified", FB, "high", "2009-08-06",
  "3-V Biosciences (now Sagimet) closed a $30M Series B on 2009-08-06 led by new investor NEA, with existing "
  "investors Kleiner Perkins and The Column Group (FierceBiotech); this matches the firm's 2009 year and the NEA 13 "
  "and NEA Ventures 2009 holders in the S-1.",
  rnd("2009-08-06", "Series B", 30000000, "New Enterprise Associates", True, FB, "press"),
  rnd("2020-12", "Series F", None, None, None,
      "https://www.sec.gov/Archives/edgar/data/1400118/000110465921051413/tm218447-3_drs.htm", "filing"))

U("inhale-therapeutic-systems", "Stage pass 2026-09-30: NEA's filings on Inhale are 1997-98 13G ownership reports "
  "after the 1994 listing; EDGAR's record for the company (now Nektar) starts later and names no NEA round, so the "
  "stage is undetermined.")

U("samaya-ai", "Stage pass 2026-09-30: Fortune and the company release say NEA led the $43.5M financing but name no "
  "round, and the firm's post calls it a financing; stage stays undetermined.")

U("singularity", f"Stage pass 2026-09-30: {NQ} finds only the July 2026 $80M Series A at a $400M valuation "
  "(FinSMEs and others), which postdates NEA's 2024 entry; the earlier round is not named.",
  rnd("2026-07-14", "Series A", 80000000, None, None, None, "press"))

U("heliogen-inc", "Stage pass 2026-09-30: the Heliogen Forms 3 and 4 behind this row (July and August 2022) are filed "
  "by Krishna Kolluri and NeoTribe Ventures I, his post-NEA firm, with no NEA entity among the reporting persons, so "
  "the filings do not show NEA money and the membership should be re-judged; no stage is given.")

SAT = jl.FTS("Satsuma", "8-K")
S("satsuma-pharmaceuticals-inc", "Growth", "web_verified", SAT, "high", "2021-03",
  "NEA's entry is the $80M private placement of common stock Satsuma closed in March 2021, led by Commodore Capital "
  "and NEA (company 8-K), bought through Growth Equity Opportunities 17 into a company listed since 2019. No earlier "
  "NEA private round is on record, so under decisions X1 the membership should be re-judged.",
  rnd("2021-03", "Private placement of common stock (listed company)", 80000000,
      "Commodore Capital; New Enterprise Associates", True, SAT, "company"))

GWO = jl.NEWS("theorycraft-games", "Riot, Bungie, Blizzard, and Valve veterans")
S("theorycraft-games", "Series A", "model", GWO, "medium", "2021-03",
  "The studio's launch round of $37.5M (March 2021) was led by NetEase with money from NEA, Bitkraft and Griffin "
  "(Game World Observer); GamesIndustry.biz's headline names it the Series A. The firm's 2020 year is the close; no "
  "earlier round is reported. The round was not led by a16z as the earlier line had it.",
  rnd("2021-03-04", "Series A", 37500000, "NetEase", True, GWO, "press"),
  rnd("2022-09-22", "Series B", 50000000, None, None, None, "press"),
  drop=("Series A",))

U("evenly", f"Stage pass 2026-09-30: {NQ} for Evenly orthodontics finds no funding report naming NEA's 2019 round.")

U("the-well", f"Stage pass 2026-09-30: {NQ} for THE WELL with its founders and round words returns namesakes only; "
  "NEA's 2020 round is not named.")

U("logikcull", f"Stage pass 2026-09-30: {NQ} finds Business Insider's 2018 report of a $25M raise but no source read "
  "names the round or its lead (the page could not be fetched); NEA's 2018 round stays undetermined.",
  rnd("2018", "financing (round not named)", 25000000, None, None, None, "press"))

U("unite-genomics-inc", f"Stage pass 2026-09-30: {NQ} has nothing on Unite Genomics; the November 2018 Form D "
  "(Pete Sonsini a director) names no round.")

U("missmalini", f"Stage pass 2026-09-30: {NQ} finds the August 2018 INR 104M pre-Series A (exchange4media; the page "
  "could not be read) after NEA's 2017 entry; NEA's own round is not named.",
  rnd("2018-08-28", "Pre-Series A", None, None, None, None, "press"))

U("some-spider-studios", f"Stage pass 2026-09-30: {NQ} finds the 2021 sale of Scary Mommy's parent to Bustle "
  "Digital for $150M in stock but no report of NEA's 2017 round.")

CAS = jl.FTS("Cascadian", "SC 13D")
S("cascadian-therapeutics", "Growth", "web_verified", CAS, "high", "2016-06-28",
  "NEA's Growth Equity Opportunities IV bought 10.75M shares for $8.6M in Cascadian's underwritten public offering "
  "closed 2016-06-28 (NEA's 13D, Item 3): a purchase into a listed company, which the firm labels Public/PIPES. "
  "No earlier NEA private round is on record, so the membership should be re-judged under decisions X1.",
  rnd("2016-06-28", "Underwritten public offering (listed company)", 28000000, None, True, CAS, "filing"))

MJ = jl.NEWS("mojo-vision", "$58 Million Funding Round")
U("mojo-vision", "Stage pass 2026-09-30: next.reality.news reports a $58M Series B in March 2019 after a $50M Series "
  "A, but no source read ties NEA to the Series A or dates it; NEA's 2016 round stays undetermined.",
  rnd(None, "Series A (date not given)", 50000000, None, None, MJ, "press"),
  rnd("2019-03-19", "Series B", 58000000, None, None, MJ, "press"))

U("tigera", f"Stage pass 2026-09-30: {NQ} for Tigera's seed and Series A finds only the January 2018 $10M and the "
  "December 2018 Series B; NEA's 2016 round is not named.")

U("dots-technology-corp", f"Stage pass 2026-09-30: {NQ} for DOTS Technology returns namesakes only; the Form D "
  "filings of 2015, 2017 and 2021 name no round.")

U("lytmus", f"Stage pass 2026-09-30: {NQ} returns only the 2026 Indian namesake Lytmus AI; NEA's 2015 round is not "
  "on record.")

GV = jl.NEWS("pager", "Pager calls in $33m")
U("pager", "Stage pass 2026-09-30: Global Venturing (2020-03-09) lists NEA in Pager's early-2018 round led by Horizon "
  "and the March 2020 $33M round led by Health Catalyst Capital, after $29.6M from Sound Ventures, Montage and "
  "Summation; none of these names the round NEA entered in 2015.",
  rnd("2018", "financing (round not named)", None, "Horizon Healthcare Services", True, GV, "press"),
  rnd("2020-03-06", "equity and debt financing", 33000000, "Health Catalyst Capital", True, GV, "press"))

U("travelbank", f"Stage pass 2026-09-30: {NQ} finds only PhocusWire's October 2016 $10M report (the page could not be "
  "read); NEA's 2015 round is not named.")

U("betterdoctor", f"Stage pass 2026-09-30: {NQ} has no funding report for BetterDoctor; the one Form D ($10.4M, 2014, "
  "Mohamad Makhzoumi a director) names no round.")

U("epix-therapeutics", f"Stage pass 2026-09-30: {NQ} under both names finds the 2017 $45M raise of Advanced Cardiac "
  "Therapeutics and Medtronic's 2019 purchase but no report of NEA's 2014 round.",
  rnd("2017-05-02", "financing (round not named)", 45000000, None, None, None, "press"))

PW = jl.W("Pocket (service)")
U("pocket", "Stage pass 2026-09-30: Wikipedia gives Read It Later's $2.5M (2011) and $5.0M (2012) raises, both before "
  "NEA's 2014 year; no source names the round NEA entered.",
  rnd("2011", "venture financing", 2500000, None, None, PW, "press"),
  rnd("2012", "venture financing", 5000000, None, None, PW, "press"))

WH = jl.NEWS("wheelhouse", "spins out of Lyric with $16M")
U("wheelhouse", "Stage pass 2026-09-30: Wheelhouse was built inside Lyric and spun out in April 2022 with $16M co-led "
  "by Highgate Ventures and NEA (TechCrunch), round not named. The firm's 2014 year predates the product and appears "
  "to carry NEA's Lyric history, so the entry is not dated here.",
  rnd("2022-04-20", "spin-out financing (round not named)", 16000000, "Highgate Ventures; New Enterprise Associates",
      True, WH, "press"))

U("british-bio-technology-limited", "Stage pass 2026-09-30: a 1980s UK private round; nothing on EDGAR, Google News "
  "or Wikipedia names NEA's round.")
U("corvita-corporation", "Stage pass 2026-09-30: no filing, press item or Wikipedia sentence names NEA's round in "
  "Corvita (Donald Murfin, an NEA special partner, sat on its board by 1996, per the Diatide S-1).")

SR = "https://www.siliconrepublic.com/start-ups/fire1-medical-devices-funding-series-b-ucd"
SR2 = jl.NEWS("fire1", "Dublin’s FIRE1 raises")
U("fire1", "Stage pass 2026-09-30: NEA was already an investor at FIRE1's $7.5M Series B in 2016 and its EUR 40M "
  "Series C in 2018 (Silicon Republic), so it entered earlier, but no source names that 2013 round.",
  rnd("2016-04", "Series B", 7500000, None, True, SR, "press"),
  rnd("2018-01-30", "Series C", None, "Gilde Healthcare", True, SR2, "press"))

U("luminate-wireless", f"Stage pass 2026-09-30: {NQ} has nothing on Luminate Wireless; no round on record.")
U("nephrolife", f"Stage pass 2026-09-30: {NQ} for NephroLife finds only other Indian dialysis chains; NEA's round is "
  "not named.")
U("peptimmune-inc", f"Stage pass 2026-09-30: {NQ} has nothing on Peptimmune's financings; no round on record.")
U("rapid-mobile-media-limited", "Stage pass 2026-09-30: the company could not be found in any source; no round on "
  "record.")
U("t-ram-semiconductor-inc", f"Stage pass 2026-09-30: {NQ} has nothing on T-RAM's financings; no round on record.")
U("triquint-semiconductor-inc", "Stage pass 2026-09-30: TriQuint's venture rounds of the 1980s predate EDGAR and no "
  "source names NEA's round.")
U("ym-biosciences-inc", "Stage pass 2026-09-30: no filing or press item names NEA's round in YM Biosciences.")
U("datrium", f"Stage pass 2026-09-30: {NQ} for Datrium's Series A and launch funding returned nothing naming NEA's "
  "2012 round; Wikipedia has no article.")
U("pure-energies", f"Stage pass 2026-09-30: {NQ} has no funding report for Pure Energies; NEA's 2012 round is not "
  "named.")
U("stormpath", f"Stage pass 2026-09-30: {NQ} finds the $15M Series B of October 2015 (FinSMEs, page not readable) "
  "but nothing on the 2012 round the firm's own post dates; stage stays undetermined.",
  rnd("2015-10-01", "Series B", 15000000, None, None, None, "press"))
U("davita-nephrolife", "Stage pass 2026-09-30: no source names NEA's 2011 round in NephroLife.")
U("intellisys", f"Stage pass 2026-09-30: {NQ} for Intellisys and its Vennfer product finds nothing; the live Early "
  "and archived growth labels still conflict.")
U("tagkast", f"Stage pass 2026-09-30: {NQ} has nothing on Tagkast's funding.")
U("causes", f"Stage pass 2026-09-30: {NQ} for Causes returns namesakes; Wikipedia lists NEA among investors without "
  "a round.")
U("nova-fertility", f"Stage pass 2026-09-30: {NQ} for Nova IVI Fertility finds no report naming NEA's 2010 round.")
U("antenna-software", f"Stage pass 2026-09-30: {NQ} finds only the 2013 Pegasystems purchase; NEA's 2009 round is "
  "not named.")
U("cyren-call-communications-corp", "Stage pass 2026-09-30: nothing beyond the 2009 $165K Form D names a Cyren Call "
  "round.")

NM = jl.FTS("NeuroMetrix", "8-K")
S("neurometrix-inc", "Growth", "web_verified", NM, "high", "2009-09",
  "NEA's entry is NeuroMetrix's September 2009 private placement of common stock and warrants, led by Deerfield with "
  "NEA participating (company 8-K), bought through Growth Equity Opportunities into a company listed since 2004. "
  "No earlier NEA private round is on record, so under decisions X1 the membership should be re-judged.",
  rnd("2009-09", "Private placement of common stock and warrants (listed company)", None, "Deerfield Management",
      True, NM, "company"))

U("acoustic-imaging-technologies-corp", "Stage pass 2026-09-30: no source names NEA's round in Acoustic Imaging "
  "Technologies.")
U("agami-systems-inc", f"Stage pass 2026-09-30: {NQ} under Agami and its former name Zambeel finds no report naming "
  "NEA's round.")
U("alsius-corporation", "Stage pass 2026-09-30: the 2006 S-1 already read shows NEA VII in Series C-D, E and F after a "
  "recapitalisation; the first series NEA bought is not established.")

want = set(Q[:52])
got = {x["slug"] for x in L}
assert got == want, (sorted(want - got), sorted(got - want))
jl.write("s3a", L)
