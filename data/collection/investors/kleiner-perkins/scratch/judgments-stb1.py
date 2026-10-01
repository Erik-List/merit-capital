#!/usr/bin/env python3
"""Stage and R7 pass, tag stb, first block of rows 65-129 of queue/st.json (PRO-99).
Run: NQ_TAG=stb python3 judgments-stb1.py

Stage keys, rounds and flags only (valuation and status belong to the A/B agents). A not_member row gets its verdict
line and nothing else. Rows the ab1 agents also hold (private $1B+) get no verdict here: an R7 case among them is
written into the note and reported.
"""
import json

import judge_lib as jl
from judge_lib import cls, verdict, rnd, NEWS, POST, FTS, SITE

L = []
_CLS = json.loads((jl.INV / "companies/classification.json").read_text())


def old(slug, *subs):
    """The rounds already stored on the row whose `round` label contains one of `subs` (all of them when none given)."""
    rs = (_CLS.get(slug) or {}).get("funding_rounds") or []
    return [r for r in rs if not subs or any(s.lower() in (r.get("round") or "").lower() for s in subs)]


# URLs read in this pass with curl, secget or the TechCrunch search (each says what is cited).
TC_PB_A = "https://techcrunch.com/2018/07/12/as-product-development-incorporates-more-feedback-development-toolkit-productboard-raises-8m/"
TC_PB_EXT = "https://techcrunch.com/2019/02/04/productboard/"
TC_REMIND_B = "https://techcrunch.com/2014/02/04/remind101-gets-15m-from-john-doerr-to-bring-free-secure-text-messaging-to-teachers/"
TC_RIQ_C = "https://techcrunch.com/2014/03/25/enterprise-relationship-manager-relateiq-raises-40m/"
TC_RIQ_B = "https://techcrunch.com/2013/06/12/relateiq-launches-with-29m-from-formation-8-dustin-moskovitz-and-more-to-be-your-next-gen-relationship-manager/"
TC_NETSKOPE = "https://techcrunch.com/2013/10/03/netskope-comes-out-of-stealth-with-21m-from-socialcapital-and-lightspeed-and-a-dream-team-of-enterprise-vets/"
TC_NETSKOPE_C = "https://techcrunch.com/2014/05/15/netskope-brings-in-35-million-more-as-cloud-security-competition-heats-up/"
VC_ONELOGIN_B = "https://www.vcnewsdaily.com/onelogin/venture-capital-funding/kcnfympydz"
SA_MIST_C = "https://siliconangle.com/2018/02/28/wireless-lan-startup-mist-systems-closes-oversubscribed-46m-series-c-round/"
ES_NEWSELA_B = "https://www.edsurge.com/news/2015-10-06-newsela-makes-more-news-with-15m-round-led-by-kleiner-perkins"
TC_NEWSELA_C = "https://techcrunch.com/2019/03/13/newsela-tcv/"
TC_PILOT_C = "https://techcrunch.com/2021/03/27/jeff-bezos-investment-fund-is-backing-a-startup-hoping-to-be-the-aws-for-smb-accounting/"
TC_PILOT_IDX = "https://techcrunch.com/2021/11/24/how-pilot-convinced-index-ventures-to-think-long-term-about-margins/"
CB_NURX = "https://news.crunchbase.com/startups/telehealth-startup-nurx-raises-22-5m-series-c-extension/"
TC_NEWLIMIT_B = "https://techcrunch.com/2025/05/06/newlimit-founded-by-coinbase-ceo-brian-armstrong-raises-130m-to-develop-age-reversing-therapies/"

# 65 luxcreo: the Series B the firm led in August 2019, the site's year.
LX = NEWS("luxcreo", "series B round")
L.append(cls("luxcreo", stage="Growth", stage_src="web_verified", stage_cite=LX, stage_conf="high",
             entry_date="2019-08-20",
             rounds=[rnd("2019-08-20", "Series B", 30000000, "Kleiner Perkins", True, LX, "press")],
             note="Stage pass: VoxelMatters (2019-08-20) reports the $30M Series B led by Kleiner Perkins with Shunwei "
                  "Capital and Northern Light, in the site's 2019 year; a Series B reads Growth. No R7 case, a "
                  "Kleiner Perkins fund led the round."))

# 66 magic-leap (ab1): the October 2014 Series B names KPCB.
ML = NEWS("magic-leap", "Closes $542m Series B")
L.append(cls("magic-leap", stage="Growth", stage_src="web_verified", stage_cite=ML, stage_conf="high",
             entry_date="2014-10-21",
             rounds=[rnd("2014-10-21", "Series B", 542000000, "Google", True, ML, "press")]
                    + old("magic-leap", "Series C", "Series D"),
             note="Stage pass: Road to VR (2014-10-21) lists Kleiner Perkins Caufield & Byers among the investors of "
                  "the $542M Series B led by Google, the firm's 2014 year; Vox (2014-10-20) names it as an addition "
                  "to that round. Cited, so the stage is no longer model."))

# 67 mashgin (ab1): the record names no Kleiner Perkins fund and no partner link; the listing stands.
MG = NEWS("mashgin", "Raises $62.5M Series B Funding")
L.append(cls("mashgin", stage="undetermined",
             rounds=[rnd("2022-05-09", "Series B", 62500000, "NEA", False, MG, "company")],
             note="Stage pass: the company's Series B release (2022-05-09) names NEA, Matrix Partners, Susa Ventures "
                  "and Y Combinator as its backers and no Kleiner Perkins fund; the firm listed it on its 2017-18 "
                  "company pages only, no partner's previous firm explains it, so the listing stands and the entry "
                  "round stays undetermined."))

# 71 mobcrush: the September 2015 Series A the firm led.
MC = NEWS("mobcrush", "confirms $11m")
MC_LAT = NEWS("mobcrush", "Mobcrush raises $11 million")
L.append(cls("mobcrush", stage="Series A", stage_src="web_verified", stage_cite=MC, stage_conf="high",
             entry_date="2015-09-01",
             rounds=[rnd("2015-05", "seed funding", 4900000, None, None, MC_LAT, "press"),
                     rnd("2015-09-01", "Series A", 11000000, "Kleiner Perkins Caufield & Byers", True, MC, "press")],
             note="Stage pass: GamesIndustry.biz (2015-09) reports the $11M Series A led by Kleiner Perkins Caufield "
                  "& Byers, with Mike Abbott joining the board (Los Angeles Times, 2015-09-01), after $4.9M announced "
                  "in May 2015; the firm's 2015 year. No R7 case."))

# 73 netlify (ab1): the firm's own welcome post names the Series B it led.
NL = POST("netlify-modernizing-the-web")
L.append(cls("netlify", stage="Growth", stage_src="first_party", stage_cite=NL, stage_conf="high",
             entry_date="2018-10-09",
             rounds=[rnd("2017", "Series A", None, None, False, NL, "firm"),
                     rnd("2018-10-09", "Series B", 30000000, "Kleiner Perkins", True, NL, "firm")],
             note="Stage pass: the firm's post 'Welcome Netlify' (2018-10-09) announces the $30M Series B led by "
                  "Kleiner Perkins and says it was convinced by the progress 'less than a year since raising their "
                  "Series A', so the Series B is the entry; it agrees with the Growth band."))

# 74 netskope: R7, Mamoon Hamid's Social+Capital deal; no Kleiner Perkins fund in any round or filing.
L.append(verdict("netskope", "not_member",
                 "partner-carried (R7): Mamoon Hamid backed it at The Social+Capital Partnership in 2012; no round "
                 "names a Kleiner Perkins fund. TechCrunch (2013-10-03) reports the $5.5M seed from Social+Capital and "
                 "the $15.9M round from Lightspeed, and the 2014 Series C led by Accel names only those two as "
                 "previous investors; the investors' rights agreement filed with the 2025 IPO prospectus is signed by "
                 "Social+Capital funds and by no Kleiner Perkins entity, and EDGAR full-text search finds no Netskope "
                 "filing naming Kleiner; the firm's own page for Hamid lists Netskope among his companies and he "
                 "joined Kleiner Perkins in 2017, after the site's 2012 year; the row is on the live list only, never "
                 "on the kpcb.com archive (Erik 2026-09-17 partner-carried rule; decisions.md R7).",
                 ec="web", conf="medium", cite=TC_NETSKOPE))

# 70 mist-systems: the Series C the firm led.
L.append(cls("mist-systems", stage="Growth", stage_src="web_verified", stage_cite=SA_MIST_C, stage_conf="high",
             entry_date="2018-02-28",
             rounds=[rnd("2016", "Series A", 14400000, "Lightspeed Venture Partners; Norwest Venture Partners", False,
                         NEWS("mist-systems", "Not Your Father"), "press"),
                     rnd("2018-02-28", "Series C", 46000000, "Kleiner Perkins", True, SA_MIST_C, "press")],
             note="Stage pass: SiliconANGLE (2018-02-28) reports the $46M Series C led by Kleiner Perkins, Mamoon "
                  "Hamid joining the board as an observer; the site's 2017 year is the firm's own (the round was "
                  "announced in February 2018). No R7 case, a Kleiner Perkins fund led the round."))

# 76 neuron23: the Series A, with Westlake, from the founding in October 2018.
N23 = NEWS("neuron23", "Closes $113.5 Million")
L.append(cls("neuron23", stage="Series A", stage_src="web_verified", stage_cite=N23, stage_conf="high",
             entry_date="2018",
             rounds=[rnd("2018", "Series A", 33500000, "Westlake Village BioPartners; Kleiner Perkins", True, N23,
                         "company"),
                     rnd("2020-12-16", "Series B", 80000000, "Redmile Group", True, N23, "company")],
             note="Stage pass: the company's release (2020-12-16) says the $33.5M Series A came from Westlake Village "
                  "BioPartners and Kleiner Perkins, that Beth Seidenberg led it, and that the company was founded in "
                  "October 2018 with Kleiner Perkins, the site's year (the Series A is not dated more closely). The "
                  "release names the firm itself beside Westlake, so this is fund money (D5 does not apply)."))

# 77 newlimit (ab1): the firm's Series B post reads as a follow-on to the 2023 Series A.
NW = POST("new-limit-series-b")
L.append(cls("newlimit", stage="Series A", stage_src="first_party", stage_cite=NW, stage_conf="medium",
             entry_date="2023",
             rounds=[rnd("2023", "Series A", 40000000, None, True, NW, "firm"),
                     rnd("2025-05-06", "Series B", 130000000, "Kleiner Perkins", True, TC_NEWLIMIT_B, "press")]
                    + old("newlimit", "Series C"),
             note="Stage pass: the firm's post (2025-05-06) says it will 'double-down on our partnership and lead "
                  "their Series B' and looks back to 'the Series A', the only earlier priced round (TechCrunch: $40M, "
                  "two years before), in the site's 2023 year; first-party, medium because the post does not say "
                  "'we invested in the Series A' in so many words."))

# 78 newsela (ab1): the firm led the Series B; the Series A band is disputed.
L.append(cls("newsela", stage="Growth", stage_src="web_verified", stage_cite=ES_NEWSELA_B, stage_conf="high",
             flags=["stage_disputes_band"],
             rounds=[rnd("2015-10-06", "Series B", 15000000, "Kleiner Perkins Caufield & Byers", True, ES_NEWSELA_B,
                         "press"),
                     rnd("2019-03-13", "Series C", 50000000, "TCV", None, TC_NEWSELA_C, "press")],
             note="Stage pass: EdSurge (2015-10-06) reports the $15M Series B led by Kleiner Perkins Caufield & Byers "
                  "($10M of it), Brook Byers joining the board; the Form D dates the first sale 2015-05-27. The round "
                  "is named Series B, so the Series A band read off the Form D amounts is disputed: Growth."))

# 79 nuna: Kleiner Perkins led the funding, the round is not named.
NU = NEWS("nuna", "takes Medicaid")
L.append(cls("nuna", stage="undetermined", entry_date="2014",
             rounds=[rnd("2017-01", "venture funding to date, $90M (rounds not named)", 90000000,
                         "Kleiner Perkins Caufield & Byers", True, NU, "press")],
             note="Stage pass: Healthcare Dive (2017-01-12) says Nuna has raised $90M in venture funding led by "
                  "Kleiner Perkins Caufield & Byers and individual investors, so the listing is the firm's own money "
                  "(no R7 case); no source read names or dates the 2014 round, so the stage stays undetermined."))

# 80 nurx: the $36M round the firm led in July 2018, the round between the Series A and the Series C.
NX = NEWS("nurx", "Launches in Georgia")
L.append(cls("nurx", stage="Growth", stage_src="web_verified", stage_cite=NX, stage_conf="medium",
             entry_date="2018-07",
             rounds=[rnd("2018-07", "$36M round (the round between the Series A and the Series C)", 36000000,
                         "Kleiner Perkins", True, NX, "press"),
                     rnd("2019-08", "Series C", 32000000, None, None, CB_NURX, "press"),
                     rnd("2020-08-11", "Series C extension", 22500000, None, True, CB_NURX, "press")],
             note="Stage pass: Hypepotamus (2018-08-14) says Nurx closed a $36M round led by Kleiner Perkins in July "
                  "2018; Crunchbase News (2020-08-11) names Kleiner Perkins an existing investor at the Series C "
                  "extension and dates the Series C to August 2019. The $36M round follows the Union Square "
                  "Ventures Series A and precedes the Series C, so Growth; medium because the source does not "
                  "print 'Series B' and the site's year is 2017. No R7 case."))

# 81 onelogin: R7, Mamoon Hamid's Social+Capital Series B.
L.append(verdict("onelogin", "not_member",
                 "partner-carried (R7): Mamoon Hamid backed it at The Social+Capital Partnership in 2013; no round "
                 "names a Kleiner Perkins fund. The company's release (VC News Daily, October 2013) announces the "
                 "$13M Series B led by Social+Capital alongside Charles River Ventures, with Hamid, 'general partner "
                 "at The Social+Capital Partnership', joining the board; the Series A was Charles River's $1.5M "
                 "(TechCrunch 2011-06-24) and TechCrunch's report of the $100M round of 2019-01-10 names "
                 "Greenspring, Silver Lake Waterman, CRV and Scale as the investors; Hamid joined Kleiner Perkins in "
                 "2017, after the site's 2013 year; the row is on the live list only, never on the kpcb.com archive "
                 "(Erik 2026-09-17 partner-carried rule; decisions.md R7).",
                 ec="web", conf="medium", cite=VC_ONELOGIN_B))

# 82 peloton: the 2017 Series E names Kleiner Perkins.
PE = NEWS("peloton", "raise $325 million")
L.append(cls("peloton", stage="Growth", stage_src="web_verified", stage_cite=PE, stage_conf="high",
             entry_date="2017-05-24",
             rounds=[rnd("2017-05-24", "Series E", 325000000, None, True, PE, "press")],
             note="Stage pass: Business Insider (2017-05-24) names Kleiner Perkins among the investors of the $325M "
                  "Series E (with Wellington, Fidelity and Comcast NBCUniversal) and quotes Mary Meeker, the firm's "
                  "2017 year. Cited, so the stage is no longer model."))

# 83 persona (ab1): R7 candidate, written up for the main session; no verdict from this pass.
PS = NEWS("persona", "Raises $150M in Series C")
L.append(cls("persona", stage="undetermined",
             rounds=old("persona", "Series A", "Series B and", "Series D")
                    + [rnd("2021-09-15", "Series C", 150000000, "Founders Fund", None, PS, "press")],
             note="Stage pass: R7 candidate, left to the main session because the row is also in the A/B pass. The "
                  "firm's post welcoming Leigh Marie Braswell (2023-05-24) counts Persona among the investments she "
                  "led before joining; the site dates a Growth entry to 2021 and first lists the company in 2023; "
                  "the September 2021 Series C headlines name Founders Fund and Index, and no source read names a "
                  "Kleiner Perkins fund in a Persona round. The stage is undetermined until membership is ruled."))

# 84 pilot (ab1): R7 candidate; the Form D that set the band is Ilya Fushman's Index seat.
PI = NEWS("pilot", "closes $15m Series A")
L.append(cls("pilot", stage="undetermined", flags=["stage_disputes_band"],
             rounds=[rnd("2018-03-16", "Series A", 15000000, "Index Ventures", False, PI, "press"),
                     rnd("2019-04", "Series B", 40000000, "Stripe; Index Ventures", False, TC_PILOT_C, "press"),
                     rnd("2021-03-26", "Series C", 100000000, "Bezos Expeditions; Whale Rock Capital", None,
                         TC_PILOT_C, "press")],
             note="Stage pass: R7 candidate, left to the main session because the row is also in the A/B pass. The "
                  "Series A band rests on the February 2018 Form D naming Ilya Fushman a director, but that round "
                  "was the $15M Series A led by Index Ventures (FinTech Global, 2018-03-16), Fushman's firm until he "
                  "joined Kleiner Perkins later in 2018; TechCrunch has Index leading the Series A and co-leading "
                  "the Series B with Stripe, and names Bezos Expeditions, Whale Rock, Sequoia, Index and Authentic "
                  "in the Series C. No source read names a Kleiner Perkins fund in a Pilot round, so the band is "
                  "disputed and the stage is undetermined until membership is ruled."))

# 85 pinterest: no round names the firm; the label stays model and the citation is owed.
L.append(cls("pinterest", flags=["cite_pending"],
             note="Stage pass: no source read names a Kleiner Perkins fund in a Pinterest round, and EDGAR full-text "
                  "search finds no Pinterest filing naming the firm; the Growth label rests on the site's 2015 year "
                  "alone (any 2015 entry was at an $11B valuation), so the citation stays owed. No partner's "
                  "previous firm explains the listing."))

# 88 productboard (ab1): the July 2018 Series A the firm led.
L.append(cls("productboard", stage="Series A", stage_src="web_verified", stage_cite=TC_PB_A, stage_conf="high",
             entry_date="2018-07-12",
             rounds=[rnd("2018-07-12", "Series A", 8000000, "Kleiner Perkins Caufield & Byers", True, TC_PB_A, "press"),
                     rnd("2019-02-04", "Series A extension", 10000000, "Index Ventures", True, TC_PB_EXT, "press")],
             note="Stage pass: TechCrunch (2018-07-12) reports the $8M commitment from Kleiner Perkins Caufield & "
                  "Byers with Index, Credo, Reflex and Rockaway, Ilya Fushman joining the board as the firm's new "
                  "general partner; TechCrunch (2019-02-04) calls it the Series A of July 2018 and Kleiner Perkins a "
                  "previous backer. Fushman had done the seed at Index, but the Series A is the firm's own money, "
                  "so no R7 case."))

# 89 progyny: the IPO prospectus has KPCB XIII holding Series A preferred; the firm dates its entry May 2010.
PG = FTS("Progyny", "S-1")
L.append(cls("progyny", stage="Series A", stage_src="web_verified", stage_cite=PG, stage_conf="high",
             entry_date="2010-05",
             rounds=[rnd("2010-05", "Series A", None, None, True, PG, "filing"),
                     rnd(None, "Series B", None, None, True, PG, "filing")],
             note="Stage pass: the 2019 prospectus's principal-stockholders note has Kleiner Perkins Caufield & "
                  "Byers XIII holding 27,950,050 shares of Series A preferred and 48,880,248 of Series B, with Beth "
                  "Seidenberg on the board since May 2010, the month the firm's own post gives for its first "
                  "investment (then Auxogyn). The Series A is the entry."))

# 90 propel: the December 2018 Series A.
PR = NEWS("propel", "Raises $12.8 Million")
L.append(cls("propel", stage="Series A", stage_src="web_verified", stage_cite=PR, stage_conf="medium",
             entry_date="2018-12-18",
             rounds=[rnd("2018-12-18", "Series A", 12800000, "Nyca Partners", True, PR, "press")],
             note="Stage pass: Pulse 2.0 (2018-12-18) reports the $12.8M Series A led by Nyca Partners with "
                  "Andreessen Horowitz, Kleiner Perkins and Omidyar Network, in the site's 2018 year; medium because "
                  "the report does not say which of them were new. No R7 case."))

# 95 relateiq: the March 2014 round, after the Series A and B.
L.append(cls("relateiq", stage="Growth", stage_src="web_verified", stage_cite=TC_RIQ_C, stage_conf="high",
             entry_date="2014-03-25",
             rounds=[rnd("2012", "Series A", 9000000, "Accel", False, TC_RIQ_B, "press"),
                     rnd("2013-06-12", "Series B", 20000000, "Formation 8; Accel", False, TC_RIQ_B, "press"),
                     rnd("2014-03-25", "$40M round (Series C)", 40000000, None, True, TC_RIQ_C, "press")],
             note="Stage pass: TechCrunch (2014-03-25) reports $40M of new funding from Redpoint, KPCB, Felicis and "
                  "News Corp at a $245M valuation and lists the previous investors without the firm; it follows the "
                  "$9M Series A and the $20M Series B (TechCrunch 2013-06-12), so Growth. Cited, no longer model; "
                  "no R7 case."))

# 96 remind: the Series B the firm led in February 2014.
L.append(cls("remind", stage="Growth", stage_src="web_verified", stage_cite=TC_REMIND_B, stage_conf="high",
             entry_date="2014-02-04",
             rounds=old("remind", "Series A")
                    + [rnd("2014-02-04", "Series B", 15000000, "Kleiner Perkins Caufield & Byers", True, TC_REMIND_B,
                           "press")],
             note="Stage pass: TechCrunch (2014-02-04) reports the $15M Series B led by Kleiner Perkins Caufield & "
                  "Byers, John Doerr joining the board, four months after the $3.5M Series A from Social+Capital. "
                  "Social+Capital's Series A was Chamath Palihapitiya's deal, and the Series B is the firm's own "
                  "money, so no R7 case."))

# 97 ring: the March 2016 Series C.
RG = NEWS("ring", "Kleiner Perkins Joins Richard Branson")
L.append(cls("ring", stage="Growth", stage_src="web_verified", stage_cite=RG, stage_conf="high",
             entry_date="2016-03-16",
             rounds=old("ring") + [rnd("2016-03-16", "Series C", 61200000, None, True, RG, "press")],
             note="Stage pass: Fox Business (2016-03-16) reports Kleiner Perkins Caufield & Byers joining the $61.2M "
                  "Series C, the site's 2016 year. Cited, no longer model; no R7 case."))

jl.write("stb1", L)
