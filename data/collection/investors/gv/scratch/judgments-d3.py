"""PRO-75 GV delta pass, judge d3: the S2A (seed_to_a_graduation) column for 19 Seed rows.

Rows: bonnet, cliqr-technologies, cord, daydream, emergent-vr, hipster, meltano, mitro, polar-signals, snowball,
ubersense, vocode, airy-labs, buttercoin, datapad, humanoid, nifti, shelf, studio.

Method per row (DELTA-BRIEF.md, COLLECTION.md s6): gradview.py and show.py; the publisher surfaces on disk; nq.py
(Google News) for targeted queries; TechCrunch's own search API; the company's own pages; EDGAR company search and
submissions (the repo's SEC user agent and throttle) for each company's own Form D sequence, because the Form D layer
on disk holds no rounds for these rows. Every page cited was read with curl on 2026-09-29.

Surfaces start from jl.GRADLINES; where a generic name (Bonnet, Cord, Hipster, Snowball, Humanoid, Shelf, Studio,
Daydream, DataPad) made a surface line quote another company's headline as "the newest funding report", or where the
Form D line said "no filing" for a company that does file, the line is rewritten to say what the surface showed.

Notes: record appends a line's note to the stored note with " | " (and a note that repeats the stored note plus a
sentence would store the old note twice), so each line carries only its S2A sentence; the stored result is the
existing note followed by "| S2A: ...". Rounds: record replaces funding_rounds whole, so a line that touches them
carries the row's existing list with the change applied."""
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, rnd, NEWS, GNEWS = jl.cls, jl.rnd, jl.NEWS, jl.GNEWS

CHECK = "2026-09-29"
L = []
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())
_PACK = json.loads((Path(__file__).with_name("evidence-pack.json")).read_text())


def S(slug, firm=None, formd=None, fix=None, extra=()):
    """GRADLINES for the row, with the lines named in `fix` ({prefix: text}) rewritten to what the surface showed."""
    lines = jl.GRADLINES(slug, firm_note=firm, formd_note=formd, extra=list(extra))
    fix = dict(fix or {})
    out = []
    for ln in lines:
        key = next((k for k in fix if ln.startswith(k + ":")), None)
        out.append(f"{key}: {fix.pop(key)}" if key else ln)
    if fix:
        raise SystemExit(f"S({slug}): no line to rewrite for {sorted(fix)}")
    return out


def R(slug, change=None, add=()):
    """The row's existing funding_rounds, with entries replaced by index ({i: {key: value}}) and new ones added."""
    rs = [dict(r) for r in (_CLS.get(slug, {}).get("funding_rounds") or [])]
    for i, kv in (change or {}).items():
        rs[i].update(kv)
    return rs + list(add)


def NO(slug, cite, conf, entry, surfaces, note, src="web_verified", **kw):
    return cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf, grad_asof=CHECK,
               surfaces=surfaces, entry_date=entry, note=note, **kw)


def ABS(slug, entry, surfaces, note, **kw):
    return cls(slug, grad="not_graduated", grad_src="absence_check", grad_conf="medium", grad_asof=CHECK,
               surfaces=surfaces, entry_date=entry, note=note, **kw)


# ---------------------------------------------------------------- bonnet (cited end: OVO; stage uncited)
OVO = GNEWS("bonnet", "OVO announces acquisition of Bonnet")
MADDY = NEWS("bonnet", "Maddymoney")
L.append(NO(
    "bonnet", OVO, "medium", "2022-03",
    S("bonnet",
      firm="the firm's own posts and its portfolio listing for Bonnet (Consumer, Tom Hulme) -> no post names the "
           "company; the listing carries no round words",
      formd="EDGAR company search for Bonnet -> no Form D filing (a London company)",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 70 results, 48 containing the "
                         "word; this company's are the OVO acquisition reports (2023-11-24 to 2023-11-28) and a 2025 "
                         "product item; the rest are Easter bonnets, Lac du Bonnet and namesakes; no later round",
           "googlenews_local": "Google News in the UK edition -> 71 results, 49 containing the word; the same OVO "
                               "acquisition reports among namesakes; no later round"},
      extra=["googlenews_targeted: '\"Bonnet\" EV charging app raises', '\"Bonnet\" \"Patrick Reich\"', '\"Bonnet\" "
             "crowdfunding EV' (nq.py, 2026-09-29) -> a GBP 920,000 raise reported in 2021 (Imperial, 2021-10-12), a "
             "March 2023 top-up of GBP 3M from existing investors plus a crowdfunding (Business Cloud 2023-03-06, Maddyness 2023-03-31) and "
             "the OVO acquisition; no Series A",
             "company: OVO's release of 2023-11-24 (read 2026-09-29) -> acquisition completed that day; Bonnet had "
             "'recently raised' GBP 3.7m from investors and its drivers"]),
    "S2A: not graduated. After the $5.5M round of March 2022 that GV joined, the only money was an unnamed top-up in "
    "March 2023 (GBP 3M from existing investors plus a crowdfunding, Maddyness; GBP 3.7m in all per OVO, about "
    "$4.6M), under twice the seed, and OVO's release of 24 November 2023 says it completed the acquisition that day, "
    "so no Series A or qualifying round came before the sale; aligned with the 20VC and Lightspeed rows. The stage "
    "stays an uncited model reading (Lightspeed's own card labels its 2022 entry Seed, but no page names GV's round "
    "as one), hence stage_uncited at low confidence.",
    stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"],
    rounds=R("bonnet", add=[rnd("2023-03-31", "unnamed top-up (GBP 3M from existing investors plus a crowdfunding; "
                                "GBP 3.7M in all per OVO)", 4580000, None, None, MADDY, "press")])))

# ---------------------------------------------------------------- cliqr-technologies (graduated: named Series C)
CLIQR_C = NEWS("cliqr-technologies", "Capital Gains: LinkedIn Goes to School")
L.append(cls(
    "cliqr-technologies", grad="graduated", grad_src="web_verified", grad_cite=CLIQR_C, grad_conf="high",
    entry_date="2012-06",
    note="S2A: graduated. CliQr raised a $20M Series C with Polaris Partners, Foundation Capital, Google Ventures and "
         "TransLink Capital (Re/code's funding roundup of 2015-04-12, citing Forbes), a named later round after the "
         "sub-$1M seed of 2012; the 'just over $38 million' TechCrunch gave at the 2016 Cisco sale agrees.",
    rounds=R("cliqr-technologies", add=[rnd("2015-04", "Series C", 20000000, None, True, CLIQR_C, "press")])))

# ---------------------------------------------------------------- cord (cited end: Spotify)
CORD_ACQ = GNEWS("cord", "Spotify Acquires Cord Project")
L.append(NO(
    "cord", CORD_ACQ, "high", "2014-12-15",
    S("cord",
      firm="the firm's own posts (none names Cord; the default substring match hit words like 'record') and its "
           "portfolio listing -> exit line 'Acquired by Spotify, 2016'",
      formd="the company's Form D filings on EDGAR (Cord Project Inc., Brooklyn, CIK 1612384) -> one, a $1.8M offering "
            "first sold 2014-06-18 ($1.715M sold), the seed; no later filing",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 100 results, 87 containing the "
                         "word (cord blood, spinal cord, cord cutting); this company's only one is Variety's report of "
                         "the Spotify acquisition (2016-01-20); no later round"},
      extra=["googlenews_targeted: '\"Cord Project\"' (nq.py, 2026-09-29) -> 13 results: Business Insider's 2015 "
             "profile, Variety and Business Insider on the Spotify sale (2016-01-20/21; Business Insider names one "
             "seed round), the rest the Linux Foundation's CORD project and namesakes; no later round"]),
    "S2A: not graduated. The $1.8M seed (TechCrunch, 2014-12-15; the company's only Form D, first sale 2014-06-18) was "
    "its only round: Spotify acquired The Cord Project in January 2016 (Variety, 2016-01-20), and Business Insider's "
    "account of the sale names only the seed."))

# ---------------------------------------------------------------- daydream (absence)
L.append(ABS(
    "daydream", "2024-06-20",
    S("daydream",
      formd="EDGAR company search for Daydream and Daydream Factory -> no filing by this company (daydream Labs, Inc. "
            "of San Francisco is the SEO agency in the First Round book, a different company)",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 44 results, 30 containing the "
                         "name; this company's are the $50M seed (2024-06-20), the June 2025 launch and product news; "
                         "the $15M Series A headlines of April 2026 are daydream Labs, a different company; no later "
                         "round of this company"},
      extra=["googlenews_targeted: '\"Daydream\" Bornstein' and the same with funding words (nq.py, 2026-09-29) -> "
             "11 results, 2024-06 to 2026-03: the seed, the 2025 launch and Puck's March 2026 profile, which recounts "
             "only the $50M; no later round",
             "techcrunch_read: TechCrunch 2025-06-25 ('nearly a year after raising a mega seed round of $50 million') "
             "and 2026-09-14 (a product feature, no funding) read 2026-09-29 -> no later round"]),
    "S2A: not graduated on the absence test (2026-09-29): the $50M seed of June 2024 is past the 24-month window, and "
    "no later round appears in Google News, TechCrunch or Crunchbase News through September 2026; TechCrunch's June "
    "2025 launch piece still cites the seed and its September 2026 piece names no new funding."))

# ---------------------------------------------------------------- emergent-vr (absence; stage uncited)
L.append(ABS(
    "emergent-vr", "2015",
    S("emergent-vr",
      firm="the firm's own posts and its portfolio listing for Emergent VR -> no post names the company; the listing's "
           "exit line reads 'Acquired by River Studios, 2018'",
      formd="the company's Form D filings on EDGAR (EMERGENT VR, INC., San Jose, CIK 1632809) -> one, a $2M debt "
            "offering first sold 2015-01-21 ($1M sold at filing, 2015-02-04), the seed notes; no later filing",
      extra=["googlenews_targeted: '\"Emergent VR\"', '\"Emergent VR\" seed', '\"Mobius\" \"Emergent VR\"', "
             "'\"River Studios\" VR acquires' (nq.py, 2026-09-29) -> Road to VR's October 2015 report of the $2.2M is "
             "the only financing; the other hits are a 2018 Texas VR arcade of the same name and unrelated pages; no "
             "later round and no report of the sale"]),
    "S2A: not graduated on the absence test (2026-09-29): the $2.2M from Accel, Google Ventures and Rothenberg "
    "Ventures (Road to VR, October 2015; the company's only Form D, first sale January 2015) is its only financing on "
    "record, and the firm's exit line has River Studios acquiring it in 2018; no search found a later round. The "
    "stage is an uncited model reading (no page names the round), hence stage_uncited at low confidence.",
    stage="Seed", stage_src="model", stage_conf="low", flags=["stage_uncited"]))

# ---------------------------------------------------------------- hipster (cited end: AOL)
HIP_ACQ = _PACK["hipster"]["site"]["more_info"]  # the firm's own exit link: TechCrunch 2012-03-15
L.append(NO(
    "hipster", HIP_ACQ, "high", "2011-05-16",
    S("hipster",
      firm="the firm's own posts and its portfolio listing for Hipster -> no post names the company; exit line "
           "'Acquired by AOL, 2012', linking TechCrunch's report of the sale",
      formd="EDGAR company search for Hipster -> no Form D filing",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 53 results, 45 containing the "
                         "word; all are hipster culture, Hipster Whale and namesakes; none about this company",
           "techcrunch": "TechCrunch's own search -> 30 results; the three containing the word are unrelated "
                         "(2019-2024); none reports a later round of the company"}),
    "S2A: not graduated. The $1M seed of May 2011 was the company's only round: AOL bought Hipster and its "
    "five-person team for a low seven-figure sum in March 2012 (TechCrunch, 2012-03-15, the firm's own exit link), "
    "ten months after the seed."))

# ---------------------------------------------------------------- meltano (cited end: Arch shut, project sold)
MELT_END = "https://meltano.com/blog/looking-for-arch"
L.append(NO(
    "meltano", MELT_END, "high", "2021-06",
    S("meltano",
      firm="the firm's own posts and its /ai listing (Invested 2021-06, Re-invested 2022-04) -> no post names Meltano; "
           "the re-investment matches the seed extension announced in June 2022",
      formd="EDGAR company search for Meltano -> no Form D filing",
      extra=["techcrunch_read: TechCrunch 2022-06-08 read 2026-09-29 -> the $8.2M led by Venrock was raised 'to extend "
             "its seed round to $12.4 million', a seed extension, not a later round",
             "googlenews_targeted: '\"Meltano\"', '\"Arch\" \"Meltano\"', '\"Douwe Maan\"' (nq.py, 2026-09-29) -> the "
             "2021 spin-out and articles on data tooling; no round after June 2022",
             "company: meltano.com/blog/looking-for-arch (Matatika, 2026-03-01, read 2026-09-29) -> 'Arch has "
             "officially shut down' and Matatika has acquired the Meltano open source project"]),
    "S2A: not graduated. The $8.2M of June 2022, led by Venrock with GV, extended the seed round to $12.4M "
    "(TechCrunch, 2022-06-08), so it is not a later round; nothing followed before the company's Arch platform shut "
    "down and Matatika acquired the Meltano open source project (meltano.com, 2026-03-01).",
    rounds=R("meltano", change={1: {"round": "Seed extension"}})))

# ---------------------------------------------------------------- mitro (cited end: Twitter)
MITRO_ACQ = GNEWS("mitro", "Twitter Acquires Password Security Startup Mitro")
L.append(NO(
    "mitro", MITRO_ACQ, "high", "2013-09",
    S("mitro",
      firm="the firm's own posts and its portfolio listing for Mitro -> no post names the company; exit line "
           "'Acquired by Twitter, 2014'",
      formd="EDGAR company search for Mitro -> no Form D filing",
      extra=["venturebeat: VentureBeat 2015-07-11 (Google News) -> Twitter to shut Mitro down on 31 August 2015, a "
             "year after buying it; no round"]),
    "S2A: not graduated. The $1.2M seed from Google Ventures and Matrix Partners, announced with the launch "
    "(TechCrunch, 2013-09-05, the entry date), was its only round: Twitter acquired Mitro in July 2014, and "
    "TechCrunch's report of the deal still gives the seed as its backing (2014-07-31).",
    rounds=R("mitro", change={0: {"date": "2013-09-05"}})))

# ---------------------------------------------------------------- polar-signals (cited end: Dash0)
PS_ACQ = NEWS("polar-signals", "Dash0 Acquires Berlin Tech Company")
PS_SEED = "https://www.polarsignals.com/blog/posts/2021/10/08/introducing-parca-we-got-funded"
L.append(NO(
    "polar-signals", PS_ACQ, "high", "2021-10-08",
    S("polar-signals",
      firm="the firm's own posts and its portfolio listing for Polar Signals -> one post (a 2021-11-23 podcast with "
           "the founder), no round named; exit line 'Acquired by Dash0, 2026'",
      formd="the company's Form D filings on EDGAR (Polar Signals Inc., CIK 1869910) -> two: $4.14M first sold "
            "2021-06-10 (the seed) and $6.78M first sold 2024-01-05 (the seed's close), under twice the entry; no "
            "later filing",
      extra=["company: polarsignals.com blog (sitemap read 2026-09-29) -> 'We raised a $4M seed from GV & Lightspeed' "
             "(2021-10-08) and 'Polar Signals is being acquired by Dash0' (2026-08-17); no other funding post",
             "techcrunch_read: TechCrunch 2024-03-12 read 2026-09-29 -> the $6.8M closes the seed round at $10.8M"]),
    "S2A: not graduated. The company's own post of 2021-10-08 announced the $4M seed from GV and Lightspeed (the entry "
    "date; its Form D gives the first sale as 2021-06-10); the $6.8M of 2024 closed that same seed round at $10.8M "
    "(TechCrunch, 2024-03-12), and Dash0 announced its acquisition of Polar Signals on 2026-08-17 (Business Insider; "
    "the company's own post), so the seed was the last round. Aligned with the Lightspeed and Spark rows.",
    rounds=R("polar-signals", change={
        0: {"date": "2021-10-08", "source": PS_SEED, "source_type": "company", "lead": None},
        1: {"round": "Seed (the close of the round at $10.8M)"}})))

# ---------------------------------------------------------------- snowball (cited end: Credit Karma)
SNOW_ACQ = "https://techcrunch.com/2015/12/30/credit-karma-acquires-innovative-mobile-notifications-startup-snowball/"
L.append(NO(
    "snowball", SNOW_ACQ, "high", "2014-10-08",
    S("snowball",
      firm="the firm's own posts and its portfolio listing for Snowball -> no post names the company; exit line "
           "'Acquired by Credit Karma, 2015'",
      formd="EDGAR company search for Snowball -> no filing by this company (the 2014 filer Snowball, Inc. of San "
            "Francisco names other officers than founders Anish Acharya and Jeson Patel)",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 61 results, 46 containing the "
                         "word; this company's are TechCrunch's seed and launch piece (2014-10-08) and BetaKit's "
                         "report of the Credit Karma acquisition (2015-12-30); the rest are galas, dough balls and "
                         "namesakes; no later round",
           "techcrunch": "TechCrunch's own search -> 30 results; the two containing the word are unrelated (2023, "
                         "2026); TechCrunch's report of the acquisition (2015-12-30) gives the $2.3M seed as the "
                         "company's earlier raise"},
      extra=["googlenews_targeted: '\"Snowball\" Android messaging app' and '\"Snowball\" \"Credit Karma\"' (nq.py, "
             "2026-09-29) -> the 2014 launch, a February 2015 BetaKit profile and the December 2015 acquisition; no "
             "later round"]),
    "S2A: not graduated. TechCrunch's report of the Credit Karma acquisition (2015-12-30) says Snowball had previously "
    "raised the $2.3M seed round, so the seed was its last round; aligned with the Felicis and First Round rows."))

# ---------------------------------------------------------------- ubersense (cited end: Hudl)
UBER_ACQ = GNEWS("ubersense", "Hudl Acquires Ubersense")
L.append(NO(
    "ubersense", UBER_ACQ, "high", "2012-09",
    S("ubersense",
      firm="the firm's own posts and its portfolio listing for UberSense -> no post names the company; exit line "
           "'Acquired by Hudl, 2014'",
      formd="the company's Form D filings on EDGAR (UberSense Inc, CIK 1552594) -> one, a $1.14M equity offering "
            "first sold 2012-06-12, the seed; no later filing"),
    "S2A: not graduated. Hudl acquired Ubersense in September 2014 (Re/code, 2014-09-17), when it had raised $2.5M in "
    "all from Google Ventures, Atlas Venture and Boston Seed Capital: beyond the $1.1M seed that leaves about $1.4M, "
    "unnamed and far below the $5M a 2012 entry needs, and no Series A was named."))

# ---------------------------------------------------------------- vocode (absence)
L.append(ABS(
    "vocode", "2023-04",
    S("vocode",
      formd="EDGAR company search for Vocode -> no Form D filing",
      extra=["googlenews_targeted: '\"Vocode\"' and '\"Vocode\" acquired OR acquires OR acquisition' (nq.py, "
             "2026-09-29) -> the February 2024 seed reports (Business Insider, Tech Funding News) only; no later "
             "round and no buyer named",
             "yc_directory: ycombinator.com/companies/vocode (read 2026-09-29) -> status Acquired with no buyer "
             "named, a founder 'working on something new'; its latest news item is the seed report"]),
    "S2A: not graduated on the absence test (2026-09-29): the $3.25M seed of April 2023 is past the window, and no "
    "later round appears in Google News, TechCrunch or Crunchbase News; YC's directory lists Vocode as acquired "
    "without naming a buyer."))

# ---------------------------------------------------------------- airy-labs (absence)
L.append(ABS(
    "airy-labs", "2011-08-03",
    S("airy-labs",
      firm="the firm's archived listings for Airy Labs (2012-2015, Joe Kraus) -> the company listed with no exit line; "
           "no post names it",
      formd="EDGAR company search for Airy Labs -> no Form D filing",
      extra=["googlenews_targeted: '\"Airy Labs\"' and '\"Airy Labs\" \"Andrew Hsu\"' (nq.py, 2026-09-29) -> 2011-2013 "
             "coverage of the seed and the founder; the Mercury News (2012-02-21) reports layoffs and office space "
             "for rent; no later round"]),
    "S2A: not graduated on the absence test (2026-09-29): after the $1.5M seed of August 2011 the only later coverage "
    "is of layoffs (TechCrunch 2012-02-11; the Mercury News 2012-02-21, with office space in Palo Alto for rent); no "
    "later round was found."))

# ---------------------------------------------------------------- buttercoin (cited end: shut down)
BUTTER_END = GNEWS("buttercoin", "Google Ventures-Backed Bitcoin Exchange Buttercoin")
L.append(NO(
    "buttercoin", BUTTER_END, "high", "2013",
    S("buttercoin",
      firm="the firm's archived listings for Buttercoin (2013-2015, Kevin Rose, then Blake Byers and Chris Hutchins) "
           "-> the company listed; no post names it",
      formd="EDGAR company search for Buttercoin -> no Form D filing"),
    "S2A: not graduated. Buttercoin shut its service on 10 April 2015 'after failing to raise new investment' "
    "(TechCrunch, 2015-04-06), so the 2013 seed (about $1M with Google Ventures, then Centralway's $250k on the same "
    "terms) was its last round; CoinDesk put its total at $2.1M."))

# ---------------------------------------------------------------- datapad (cited end: Cloudera)
DP_ACQ = GNEWS("datapad", "Cloudera acquires business-intelligence startup DataPad")
L.append(NO(
    "datapad", DP_ACQ, "high", "2014-05",
    S("datapad",
      firm="the firm's archived listing for DataPad (2014, Dave Munichiello) -> the company listed; no post names it",
      formd="the company's Form D filings on EDGAR (DataPad Inc., Brooklyn, CIK 1571800) -> one, $1.68M of debt "
            "first sold 2013-03-06 and all sold, the notes behind the $1.7M TechCrunch reported; no later filing",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 18 results, 6 containing the "
                         "name; this company's only one is VentureBeat's report of the Cloudera acquisition "
                         "(2014-09-30); 'Datapad raises $500K' (Tech.eu, 2024-12-05) is a different, European KPI "
                         "startup; the rest are game items; no later round of this company"}),
    "S2A: not graduated. Cloudera bought DataPad and shut the service in September 2014 (VentureBeat, 2014-09-30), "
    "four months after TechCrunch reported the $1.7M, so the seed was its only round; aligned with the a16z row."))

# ---------------------------------------------------------------- humanoid (cited end: CloudFactory)
HUM_ACQ = ("https://techcrunch.com/2013/03/03/cloudfactory-launches-cloudfactory-2-0-platform-after-acquiring-"
           "speakertext-humanoid/")
L.append(NO(
    "humanoid", HUM_ACQ, "high", "2011-11",
    S("humanoid",
      firm="the firm's own posts (none names this Humanoid; the default match hit a 2026 post on humanoid robots) and "
           "its archived listing (2012-2014) -> the company listed, no exit line",
      formd="EDGAR company search for Humanoid and SpeakerText -> SpeakerText, Inc. (New York, CIK 1496316) filed one "
            "Form D, a $250K offering on 2010-07-12, before GV's seed; no later filing; no Humanoid filer is this "
            "company",
      fix={"crunchbase_news": "Crunchbase News's own search -> 30 results, all about humanoid robots (Apptronik and "
                              "others); none about this company",
           "googlenews": "Google News, the company's name with round and exit words -> 100 results, 81 containing "
                         "the word, all about humanoid robots and their makers (the 2026 UK robot maker Humanoid is a "
                         "different company); none about this company",
           "techcrunch": "TechCrunch's own search -> 30 results; the five containing the word are 2026 robot stories; "
                         "none about this company"},
      extra=["techcrunch_targeted: TechCrunch's own search for SpeakerText and CloudFactory (2026-09-29) -> the 2011 "
             "angel and seed posts and the 2013-03-03 report of the acquisition; no later round"]),
    "S2A: not graduated. CloudFactory acquired SpeakerText and Humanoid in October 2012 (TechCrunch, 2013-03-03), a "
    "year after GV's seed of November 2011, with no later round in between."))

# ---------------------------------------------------------------- nifti (absence)
L.append(ABS(
    "nifti", "2013-07",
    S("nifti",
      firm="the firm's archived listings for Nifti (2013-2015, Rich Miner) -> the company listed with no exit line; no "
           "post names it",
      formd="EDGAR company search for Nifti -> no Form D filing",
      extra=["googlenews_targeted: '\"Nifti\" price tracking', '\"Nifti\" \"Google Ventures\"', '\"Nifti\" Tuck "
             "startup', '\"Cinch\" polling app Nifti' (nq.py, 2026-09-29) -> only Tuck's article of 2013-07-24 and "
             "namesakes; no later round",
             "techcrunch_read: TechCrunch 2014-09-25 read 2026-09-29 -> the $1.2M of December 2013 was 'additional "
             "seed funding' and the company turned to its Cinch polling app; no later round"]),
    "S2A: not graduated on the absence test (2026-09-29): the $800K seed of July 2013 was followed only by $1.2M more "
    "seed funding in December 2013 (TechCrunch, 2014-09-25), part of the seed, not a later round; no later round of "
    "Nifti or its Cinch app was found."))

# ---------------------------------------------------------------- shelf (cited end: wind-down; status defunct)
SHELF_END = NEWS("shelf", "Backed by $10M Series A, TravelJoy")
L.append(NO(
    "shelf", SHELF_END, "medium", "2014",
    S("shelf",
      firm="the firm's own posts (none names this Shelf; the default match hit 'off the shelf' phrases) and its "
           "archived listings (2016-2019) -> the company listed with no exit line",
      formd="the company's Form D filings on EDGAR (Shelf.com, Inc., Pacifica, CIK 1601267; Dayo Esho, Chris Kline) "
            "-> one offering, $1.25M first sold 2013-09-04 and filed 2014-03-05 (amended 2014-03-07), the seed; no "
            "later filing",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 100 results, 63 containing the "
                         "word; all are food shelves, shelf registrations and other companies (Shelf Engine, "
                         "Shelf.io); none about this company",
           "sibling:insight-partners": "its row named Shelf is Shelf.io, a different company (a name collision); it "
                                       "says nothing about this one"},
      extra=["googlenews_targeted: '\"Shelf.com\"', '\"Shelf\" \"Dayo Esho\"', '\"Dayo Esho\"' (nq.py, 2026-09-29) -> "
             "the founder's later company TravelJoy (TechCrunch 2024-03-01, which places it after the wind-down of "
             "Shelf) and namesakes; no round of Shelf after the seed"]),
    "S2A: not graduated. TechCrunch (2024-03-01) says the founders, Dayo Esho and Chris Kline, built TravelJoy in the "
    "years following the wind-down of their earlier product discovery startup Shelf, so the $1.2M seed (Shelf.com, "
    "Inc.'s only Form D: $1.25M first sold in September 2013, filed in March 2014) was its last round. Status set to "
    "defunct on that wind-down, replacing unknown.",
    status="defunct"))

# ---------------------------------------------------------------- studio (absence)
L.append(ABS(
    "studio", "2022-09-29",
    S("studio",
      firm="the firm's own posts (none names this Studio; the default match hit a 2026 post using the word) and its "
           "archived listings (2022-2026, M.G. Siegler) -> the company listed, no round named",
      formd="EDGAR company search for Studio of America -> no Form D filing",
      fix={"googlenews": "Google News, the company's name with round and exit words -> 100 results, 94 containing the "
                         "word; all are other studios (film, games, design, venture); none about this company",
           "googlenews_firm": "Google News, the company's name beside the firm's -> 48 results, 20 containing the "
                              "word; none about this company",
           "sibling:y-combinator": "its row named Studio is a different company (a name collision); it says nothing "
                                   "about this one"},
      extra=["googlenews_targeted: '\"Matt Hidalgo\"', '\"Studio\" app \"Matt Hidalgo\"', '\"Studio\" group video app "
             "friends episodes' (nq.py, 2026-09-29) -> only TechCrunch's seed and launch piece (2022-09-29) names the "
             "company; no later round",
             "techcrunch_targeted: TechCrunch's own search for Hidalgo and Studio (2026-09-29) -> the same 2022 piece "
             "only",
             "company: s-tud.io (2026-09-29) -> the domain does not resolve"]),
    "S2A: not graduated on the absence test (2026-09-29): the $3.3M seed of September 2022 is four years old, and "
    "searches on the company and its CEO Matt Hidalgo find only TechCrunch's seed and launch piece; no later round."))

jl.write("d3", L)
