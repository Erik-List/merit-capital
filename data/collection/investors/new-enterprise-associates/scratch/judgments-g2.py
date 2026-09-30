"""PRO-100 NEA delta, judge g2: queue batch 2 (graduation pass on Seed rows, plus country/city/status/stage leftovers).
Run once: NQ_TAG=g2 python3 judgments-g2.py"""
import judge_lib as jl

ASOF = "2026-09-30"
L = []


def lines(slug, fix=None, extra=(), firm_note=None, formd_note=None):
    """The absence test's surface lines: GRADLINES read, with the lines that summarise a homonym replaced by what the
    headlines actually show (fix: surface -> text after 'surface: '), plus the judge's own searches."""
    out = []
    for ln in jl.GRADLINES(slug, firm_note=firm_note, formd_note=formd_note):
        k = ln.split(":", 1)[0]
        out.append(f"{k}: {fix[k]}" if fix and k in fix else ln)
    return out + list(extra)


def no(slug, src, note, surfaces, cite=None, conf="medium", **kw):
    L.append(jl.cls(slug, grad="not_graduated", grad_src=src, grad_cite=cite, grad_conf=conf, grad_asof=ASOF,
                    surfaces=surfaces, note=note, **kw))


def yes(slug, src, cite, note, rounds, conf="high", **kw):
    L.append(jl.cls(slug, grad="graduated", grad_src=src, grad_cite=cite, grad_conf=conf, note=note, rounds=rounds, **kw))


# ---------------- graduated ----------------
u = jl.GNEWS("landit", "Landit lands $13 million")
yes("landit", "web_verified", u,
    "S2A: graduated, the $13M Series A led by WeWork with NEA in February 2019 (ImpactAlpha), after the firm's 2014 seed.",
    [jl.rnd("2019-02-28", "Series A", 13000000, "WeWork", True, u)])

u = jl.GNEWS("learnup", "Raises $8M From NEA")
yes("learnup", "web_verified", u,
    "S2A: graduated, the $8M round with NEA and Shasta in September 2015 (TechCrunch; Form D sale 2015-08-18), more than "
    "twice the $1.9M 2012 seed and above $5M.",
    [jl.rnd("2012-08-03", "Seed", 1875075, None, True, jl.FORMD_CITE("learnup", 0), "filing"),
     jl.rnd("2015-09-16", "unnamed", 8000000, None, True, u)])

u = jl.FORMD_CITE("modyfi", 0)
yes("modyfi", "web_verified", u,
    "S2A: graduated, a $14.65M round sold from 2024-04-26 (Form D, with a new outside director beside NEA's Luke Pappas), "
    "more than twice the $7M seed of 2023 and unnamed, so the step-up decides it; close to the line, since the seed's own "
    "Form D ($8.2M sold) includes converted notes. Figma bought the company in May 2025.",
    [jl.rnd("2023-08-23", "Seed", 7000000, "New Enterprise Associates", True,
            "https://www.prnewswire.com/news-releases/modyfi-launches-full-public-beta-for-ai-design-platform-announces-7m-in-seed-funding-led-by-nea-301907141.html"),
     jl.rnd("2024-04-26", "unnamed (Form D)", 14649959, None, None, u, "filing")], conf="medium")

u = jl.FORMD_CITE("neotract", 0)
yes("neotract", "web_verified", u,
    "S2A: graduated, a $28.1M round sold from 2009-07-17 (Form D, NEA's Frank Torti and Josh Makower among the directors), "
    "far above the $5M step-up for a 2005 seed of unknown size; more rounds followed in 2011 and 2012 before Teleflex bought it.",
    [jl.rnd("2009-07-17", "unnamed (Form D)", 28108160, None, True, u, "filing")])

u = jl.GNEWS("saferide-health", "Series B Funding")
u2 = jl.GNEWS("saferide-health", "Series C Funding")
yes("saferide-health", "web_verified", u,
    "S2A: graduated, SafeRide Health announced its Series B in November 2021 and a Series C in October 2023 (Business Wire), "
    "after the firm's 2017 seed.",
    [jl.rnd("2021-11-08", "Series B", None, None, None, u), jl.rnd("2023-10-05", "Series C", None, None, None, u2)])

u = "https://techcrunch.com/2018/11/13/meditation-app-simple-habit-raises-10-million-series-a"
yes("simple-habit", "web_verified", u,
    "S2A: graduated, the $10M Series A led by Foundation Capital in November 2018 (TechCrunch), after the $2.5M seed of "
    "2017 that the firm's listing dates.",
    [jl.rnd("2017", "Seed", 2500000, None, True, u), jl.rnd("2018-11-13", "Series A", 10000000, "Foundation Capital", None, u)])

u = jl.W("Surf Air")
yes("surf-air", "web_verified", u,
    "S2A: graduated, the Series A completed in June 2013 with Anthem Venture Partners, NEA and others (Wikipedia), after the "
    "firm's 2012 seed entry; the company is now listed (NYSE SRFM).",
    [jl.rnd("2013-06", "Series A", None, None, True, u)], conf="medium")

u = jl.NEWS("terrajoule", "Solar storage below")
yes("terrajoule", "web_verified", u,
    "S2A: graduated, a $11.5M round with Air Liquide and NEA in 2013 (RenewEconomy; Form D sale 2013-06-07, $10.0M), far "
    "above the $5M step-up for the 2009 seed of unknown size; VC Post calls that round seed funding too, so no Series A "
    "name is on record and the step-up decides it.",
    [jl.rnd("2013-06-07", "unnamed", 11500000, None, True, u)], conf="medium")

u = jl.GNEWS("transifex", "Series A, Led by Toba")
yes("transifex", "web_verified", u,
    "S2A: graduated, the $4M Series A led by Toba Capital in July 2015, which TechCrunch says NEA joined as a seed investor.",
    [jl.rnd("2015-07-07", "Series A", 4000000, "Toba Capital", True, u)])

yes("retrieve", "formd", jl.FORMD_CITE("retrieve", 3),
    "S2A: graduated on the Form D layer, a $10M offering from 2022-01-14 against the $4M entry of 2018-04-20.",
    [jl.rnd("2022-01-14", "unnamed (Form D)", 10000000, None, None, jl.FORMD_CITE("retrieve", 3), "filing")])

yes("rocket-chat", "formd", jl.FORMD_CITE("rocket-chat", 1),
    "S2A: graduated on the Form D layer, a $19.0M round from 2021-01-27 against the $5M entry of 2016 (TechCrunch reported "
    "the $19M raise on 2021-02-03).",
    [jl.rnd("2021-01-27", "unnamed (Form D)", 18974979, None, None, jl.FORMD_CITE("rocket-chat", 1), "filing")])

yes("sentons", "formd", jl.FORMD_CITE("sentons", 1),
    "S2A: graduated on the Form D layer, a $10.0M round from 2012-12-20 against the $4.4M entry of 2011-12-06; a $23.5M "
    "round followed a year later.",
    [jl.rnd("2012-12-20", "unnamed (Form D)", 10000001, None, None, jl.FORMD_CITE("sentons", 1), "filing")])

# ---------------- not graduated: a cited end ----------------
no("intrinsic", "web_verified",
   "S2A: not graduated; VMware bought Intrinsic in August 2019 with the August 2016 seed as its last round (CRN), and the "
   "absence test found no later round (surfaces listed). Aligned with the First Round row.",
   lines("intrinsic",
         firm_note="the firm's listing for this slug joins Intrinsic Therapeutics, a different company; no firm post names "
                   "a round of the security startup",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 72 headlines on the word "
                            "'Intrinsic'; the only ones on this company report VMware's acquisition (CNBC, 2019-08-20); the "
                            "funding headlines name Intrinsic Therapeutics, Intrinsic Power and others; no later round",
              "techcrunch": "TechCrunch's own search -> 30 results, the named ones on Alphabet's Intrinsic and a 2023 YC "
                            "company of the same name; none reports a round of this company"}),
   cite="https://www.crn.com/news/security/vmware-acquires-intrinsic-for-application-security-expertise-report", conf="high")

no("iopipe", "web_verified",
   "S2A: not graduated; New Relic bought IOpipe in November 2019 (TechCrunch, 'early-stage'), with the $2.5M seed of "
   "2017 as the last round found (surfaces listed).",
   lines("iopipe"), cite=jl.GNEWS("iopipe", "New Relic snags"), conf="high")

no("lemonade-io", "first_party",
   "S2A: not graduated; the firm's own page records the sale to Evernote, and every surface searched is empty of any round "
   "after the 2015 seed (surfaces listed).",
   lines("lemonade-io"), cite=jl.SITE("lemonade-io"))

no("liveloop", "web_verified",
   "S2A: not graduated; Microsoft bought and shut LiveLoop in March 2015 (VentureBeat), and the absence test found no round "
   "after the 2010 seed (surfaces listed).",
   lines("liveloop"), cite=jl.GNEWS("liveloop", "Microsoft acquires and shutters"), conf="high")

no("lxa", "web_verified",
   "S2A: not graduated; CapitaLand bought LXA Capital (KrASIA, 2025-12-02; the firm's exit line names CLI PE), and the $10M "
   "seed of November 2023 is the only round found (surfaces listed).",
   lines("lxa"), cite=jl.GNEWS("lxa", "LXA Capital, new China investments, and more - kr-asia.com"), conf="high")

no("minimum", "web_verified",
   "S2A: not graduated; Novisto bought Minimum on 2026-03-31 (BetaKit), and no round after the firm's 2022 seed was found "
   "(surfaces listed; the name searches return minimum-wage news, so the judge's own searches carry the check).",
   lines("minimum",
         firm_note="the firm's own listing for Minimum (Seed, 2022); no firm post names the company",
         fix={"crunchbase_news": "Crunchbase News's own search -> 30 results, none on this company",
              "googlenews": "Google News, the company's name with round and exit words -> 94 headlines on minimum wages "
                            "and funding floors, none on this company",
              "googlenews_firm": "Google News, the company's name beside the firm's -> 8 headlines, none on this company",
              "googlenews_local": "Google News in the company's own edition and language -> 93 headlines on minimum "
                                  "wages, none on this company"},
         extra=["news_search: Google News '\"Minimum\" carbon accounting' and '\"Minimum\" Novisto', run 2026-09-30 -> a "
                "Pulse 2.0 profile (2023-09-21) and Novisto's acquisition (BetaKit, ESG Today, newswire.ca, 2026-03-31); "
                "no round after the 2022 seed"]),
   cite=jl.GNEWS("minimum", "Novisto acquires UK-based Minimum"),
   conf="high")

no("simsolid", "web_verified",
   "S2A: not graduated; Altair bought SimSolid on 2018-10-17 (its release, on the Siemens newsroom), and no round after "
   "the 2015 seed was found (surfaces listed). Country and city: Mississauga, Ontario (Magnetics Magazine, carrying the "
   "acquisition release).",
   lines("simsolid"), cite=jl.GNEWS("simsolid", "Altair Acquires SimSolid - Siemens"), conf="high",
   country="CA", country_src="web_verified",
   country_cite="https://magneticsmag.com/altair-acquires-simsolid-game-changing-simulation-technology-for-designers-design-engineers-and-simulation-analysts/",
   city="Mississauga", city_src="web_verified", clear=("city_unknown",))

no("subtext", "first_party",
   "S2A: not graduated; the firm's own page records the sale to Renaissance Learning (2013), and no round after the $3M "
   "seed of October 2011 was found (surfaces listed). Aligned with the GV row.",
   lines("subtext",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 61 headlines on the word "
                            "'subtext', none on this company"}),
   cite=jl.SITE("subtext"))

# ---------------- not graduated: the Form D layer ----------------
no("more-health", "formd",
   "S2A: not graduated; the Form D layer finds no later priced round at twice the $3.3M entry of 2015-04-30 (the 2018 "
   "notice is an indefinite offering with nothing sold), and the news finds only hospital partnerships.",
   lines("more-health",
         formd_note="the company's Form D filings on EDGAR -> $0.4M sold from 2014-06-30, the $3.33M entry round from "
                    "2015-04-30, and a 2018-08-01 notice of an indefinite offering with nothing sold at filing; no later "
                    "priced round at twice the entry",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 7 headlines on the phrase "
                            "'more health', none on this company"},
         extra=["news_search: Google News '\"MORE Health\" second opinion', run 2026-09-30 -> hospital partnerships "
                "(PR Newswire, 2017 to 2019) and a Forbes profile (2024-08-15); no funding round"]),
   cite=jl.FORMD_CITE("more-health", 1), conf="high")

no("poggled", "formd",
   "S2A: not graduated; the Form D layer finds only a $3M round in 2014 after the $5.6M entry of 2011-03-24, and no press "
   "reports a later round.",
   lines("poggled"), cite=jl.FORMD_CITE("poggled", 0), conf="high")

no("waltz-networks", "formd",
   "S2A: not graduated; the Form D layer finds no filing after the $6.75M entry of 2015-10-26, and no press reports a "
   "later round.",
   lines("waltz-networks"), cite=jl.FORMD_CITE("waltz-networks", 0), conf="high")

# ---------------- not graduated: the absence test ----------------
no("ledge", "absence_check",
   "S2A: not graduated; the absence test found no round after the $9M seed of February 2023 (surfaces listed).",
   lines("ledge",
         firm_note="the firm's own post on Ledge (2023-02-16, the $9M seed) and its listing -> neither names a later round",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 38 headlines on the word "
                            "'ledge'; the company's own is only the February 2023 seed; no later round"},
         extra=["news_search: Google News '\"Ledge\" AI accounting close' and '\"Ledge\" finance automation raises Series "
                "A', run 2026-09-30 -> only the February 2023 seed (TechCrunch, FF News, Calcalist); no later round"]))

no("martian", "absence_check",
   "S2A: not graduated; the absence test found no priced round after the $9M seed of November 2023; Accenture's "
   "September 2024 strategic investment was unpriced and undisclosed (surfaces listed). Aligned with the General Catalyst row.",
   lines("martian",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 48 headlines, mostly on Mars and "
                            "the film; the company's own are the November 2023 seed and Accenture's investment "
                            "(2024-09-17); no later priced round",
              "techcrunch": "TechCrunch's own search -> 4 headlines, the company's own the 2023-11-15 launch ('Martian "
                            "Lawyers Club' is a different company); no later round"},
         extra=["news_search: Google News '\"Martian\" model router', run 2026-09-30 -> the 2023 seed coverage, "
                "Accenture's investment (2024-09-17) and a CB Insights list (2025-01-25); no later round"]))

no("neo-cybernetica", "absence_check",
   "S2A: not graduated; the absence test found nothing after the $30M seed of February 2022 (surfaces listed).",
   lines("neo-cybernetica"))

no("nimble-collective", "absence_check",
   "S2A: not graduated; NEA led the $8.5M round of the firm's 2015 entry (Variety, Cartoon Brew, 2016-02-18), and the only "
   "later round, $16M offered and $9.2M sold from 2018-01-18 (Form D), is below twice it; Amazon Web Services later took "
   "over the platform (surfaces listed).",
   lines("nimble-collective",
         formd_note="one filing, a round first sold 2018-01-18 ($16.0M offered, $9.2M sold), below twice the $8.5M "
                    "NEA-led round announced 2016-02-18"))

no("nth-round", "absence_check",
   "S2A: not graduated; the absence test found no round after the firm's 2018 seed (a GetLatka vendor estimate is the "
   "only item) (surfaces listed).",
   lines("nth-round",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 1 headline, a GetLatka vendor "
                            "estimate (2026-08-10) that reports no round; no later round",
              "googlenews_firm": "Google News, the company's name beside the firm's -> the same GetLatka item; no round"},
         extra=["news_search: Google News '\"Nth Round\" liquidity', run 2026-09-30 -> the same GetLatka item only"]))

for s in ("ohai", "proof-of-learn"):
    no(s, "absence_check",
       "S2A: not graduated; Proof of Learn and Ohai are one issuer (CIK 1904393, ProofOfLearn, Inc. renamed Ohai.ai, Inc.), "
       "whose seed from 2021-12-31 sold $18.95M; the only later rounds are a $4.0M sale from 2023-12-01 and an undisclosed "
       "strategic investment led by Muse Capital in August 2025, neither at twice the entry (surfaces listed).",
       lines(s,
             formd_note="the issuer's Form D filings on EDGAR (CIK 1904393, ProofOfLearn, Inc., now Ohai.ai, Inc.) -> a "
                        "round first sold 2021-12-31, $14.9M offered then amended to $26.7M offered with $18.95M sold; "
                        "$6.0M offered from 2023-12-01 with $4.0M sold; no later round at twice the entry",
             extra=["press: Ohai.ai's strategic investment led by Muse Capital (Yahoo Finance, FinSMEs, 2025-08-19), "
                    "amount and price undisclosed"]))

no("regression-games", "absence_check",
   "S2A: not graduated; the absence test found no round after the $4.2M seed of August 2022 (surfaces listed). Aligned "
   "with the a16z row.",
   lines("regression-games"))

no("scratch-music-group", "absence_check",
   "S2A: not graduated; the absence test found no round after the firm's 2013 seed (surfaces listed).",
   lines("scratch-music-group",
         extra=["news_search: Google News '\"Scratch DJ Academy\"' and '\"Scratch Music Group\"', run 2026-09-30 -> academy "
                "news from 2009 to 2023 (the Miami location closed in 2023); no funding round"]))

no("spokn", "absence_check",
   "S2A: not graduated; the absence test found no round after the $4M seed of May 2021 (AlleyWatch) (surfaces listed).",
   lines("spokn"))

no("sundeck", "absence_check",
   "S2A: not graduated; the absence test found no round after the $20M seed of May 2023 (surfaces listed). Aligned with the "
   "Coatue row.",
   lines("sundeck",
         extra=["news_search: Google News '\"Sundeck\" Snowflake', run 2026-09-30 -> the June 2023 product launches only"]))

no("swirlds", "absence_check",
   "S2A: not graduated; the absence test found no priced round of Swirlds after the firm's 2016 seed (surfaces listed).",
   lines("swirlds",
         extra=["news_search: Google News '\"Swirlds\"' and '\"Swirlds\" raises funding', run 2026-09-30 -> the 2022 move "
                "of the teams to Swirlds Labs (Hedera) and Hedera news; no funding round of Swirlds"]))

no("teal", "absence_check",
   "S2A: not graduated; Teal Drones raised $6.05M in all by 2017 ($150K in 2014, the $2.8M seed of December 2015, $3M more "
   "in 2016; BYU Daily Universe), below the $8M step-up, and Red Cat bought it in 2021 (surfaces listed).",
   lines("teal",
         firm_note="the firm's own listing for Teal (Seed, 2015, exit line Red Cat Holdings); no firm post names a round of "
                   "Teal Drones",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 88 headlines on the word 'teal'; "
                            "Teal Drones' own report the Red Cat acquisition (2021-07) and later contracts; the funding "
                            "headlines name Teal Communications and Teal Health; no later round of Teal Drones",
              "techcrunch": "TechCrunch's own search -> 3 headlines, all on Teal Health, a different company"},
         extra=["news_search: Google News '\"Teal\" drone raises before:2020' and '\"Teal Drones\"', run 2026-09-30 -> the "
                "$2.8M seed (Dronelife, 2016-07-20) and $6.05M raised in all (BYU Daily Universe, 2017-02-09); no round "
                "at the step-up before the 2021 sale"]))

no("wiith", "absence_check",
   "S2A: not graduated; the absence test found no round after the firm's 2022 seed (surfaces listed).",
   lines("wiith",
         fix={"googlenews": "Google News, the company's name with round and exit words -> 4 headlines on the misspelling "
                            "'wiith', none on this company"}))

no("apropose", "absence_check",
   "S2A: not graduated; the absence test found no round after the $1.875M seed of July 2016 (surfaces listed). Aligned with "
   "the a16z row.",
   lines("apropose"))

u = jl.GNEWS("blispay", "raises $12.75M")
no("blispay", "absence_check",
   "S2A: not graduated; the seed that names NEA is the $12.75M round led by FirstMark (TechCrunch, 2016-03-31; no trace of "
   "the company before 2016, so the firm's archived 2014 year is not used), and the only later round, a further $12M "
   "(TechCrunch, 2017-05-23, unnamed), is below twice it; Alliance Data bought Blispay in May 2019.",
   lines("blispay",
         extra=["press: TechCrunch (2016-03-31) the $12.75M seed led by FirstMark with NEA; TechCrunch (2017-05-23) a "
                "further $12M, round not named; Business Journals (2019-05-22) the sale to Alliance Data"]),
   stage="Seed", stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2016-03-31",
   rounds=[jl.rnd("2016-03-31", "Seed", 12750000, "FirstMark Capital", True, u),
           jl.rnd("2017-05-23", "unnamed", 12000000, None, True, jl.GNEWS("blispay", "raises $12 million"))])

# ---------------- stage disputes (the entry was a Series A, so the S2A column does not apply) ----------------
s1 = "https://www.sec.gov/Archives/edgar/data/1088825/0001012870-99-002461-index.html"
L.append(jl.cls("tivo", stage="Series A", stage_src="web_verified", stage_cite=s1, stage_conf="high",
                entry_date="1997-09-24", flags=("stage_disputes_band",),
                rounds=[jl.rnd("1997-09-24", "Series A preferred", 3000000, None, True, s1, "filing"),
                        jl.rnd("1998-05-29", "Series B preferred", 4612752, None, None, s1, "filing")],
                note="Stage dispute: TiVo's S-1 (1999-07-22) says NEA entities bought 2,000,000 of the 5,000,000 Series A "
                     "preferred shares sold at $0.60 on 1997-09-24 and 1997-10-22, so the 1997 entry is a Series A, not the "
                     "firm's Seed label (a D6 miss); S2A does not apply. Aligns with the IVP row."))

t1 = jl.GNEWS("trackmaven", "TrackMaven Lands $6.5M")
L.append(jl.cls("trackmaven", stage="Series A", stage_src="web_verified", stage_cite=t1, stage_conf="high",
                flags=("stage_disputes_band",),
                rounds=[jl.rnd("2013-03", "Seed", 1250000, None, False, t1),
                        jl.rnd("2014-02-04", "Series A", 6500000, "New Enterprise Associates", True, t1),
                        jl.rnd("2014-12-09", "unnamed", 8000000, None, True,
                               jl.GNEWS("trackmaven", "Raises $14 Million"))],
                note="Stage dispute: TechCrunch (2014-02-04) calls NEA's $6.5M lead the Series A, after a $1.25M seed from "
                     "AOL Ventures and angels in 2013, so the Form D band's Seed does not hold; S2A does not apply."))

# ---------------- country, city and status leftovers ----------------
L.append(jl.cls("isgn-technologies-ltd", country="US", country_src="web_verified",
                country_cite="https://www.mpamag.com/us/news/general/sagent-lending-technologies-acquires-mortgage-tech-firm/195669",
                city="Melbourne", city_src="web_verified",
                note="Country and city: 'Melbourne-based ISGN', serving the US residential mortgage market (MPA, on the "
                     "2019 Sagent deal); the Melbourne is Florida, where the company's US office stood (1333 Gateway "
                     "Drive); the listed Ltd. entity is its Indian arm."))

L.append(jl.cls("lizzyai", country="US", country_src="web_verified",
                country_cite="https://pulse2.com/lizzyai-5-million-seed-funding/",
                city="New York", city_src="web_verified", clear=("city_unknown",),
                note="Country and city: 'a New York-based AI-native interviewing platform' (Pulse 2.0, on the December 2025 "
                     "seed)."))

L.append(jl.cls("medisys-edutech", country="IN", country_src="web_verified",
                country_cite=jl.POST("nea-names-josh-makower-general-partner"),
                flags=("city_unknown",),
                note="Country: the firm's own release (2015-06-11) names NEA India's Ruchir Lahoty (New Enterprise "
                     "Associates (India) Pvt. Ltd.) a director of MEdRC EduTech, and the company's own page lists Indian "
                     "medical-college faculty; no source gives its city."))

L.append(jl.cls("telebit-corp", status="acquired", rng="below_1b", country="US", country_src="web_verified",
                country_cite=jl.W("Telebit"), city="Chelmsford", city_src="web_verified", focus="Data Infrastructure",
                note="Cisco Systems bought Telebit in July 1996 for $200M (Wikipedia). Headquarters: Sunnyvale until the "
                     "1993 Octocom merger moved the corporate office to Chelmsford, Massachusetts, where it stayed to the "
                     "sale."))


# plain prose: no em or en dashes anywhere on a line
def _clean(x):
    if isinstance(x, str):
        return x.replace("—", ",").replace("–", "-")
    if isinstance(x, list):
        return [_clean(i) for i in x]
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    return x


L = [_clean(x) for x in L]
jl.write("g2", L)
