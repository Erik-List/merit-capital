"""PRO-100 NEA, judge m1, first half of queue/m1.json (38 rows): the 16 recall additions and the Form D
name-match clusters of Robert Croce, Perry Wallack, Jimmy Treybig, Krishna Kolluri and Richard Whitney (part).
Run: NQ_TAG=m1 python3 judgments-m1a.py"""
import json
import re

import judge_lib as jl

B = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def NOTE_URL(slug):
    """The filing URL the recall note on the base row cites (read from disk, never typed)."""
    m = re.findall(r"\((https://www\.sec\.gov/[^)]+)\)\s*$", B[slug]["notes"])
    if len(m) != 1:
        raise SystemExit(f"NOTE_URL({slug!r}) matched {len(m)}")
    return m[0]


def FD(slug, i=0):
    """The row's own Form D link (base.json formd_links)."""
    return [x.strip() for x in B[slug]["formd_links"].split(";") if x.strip()][i]


V, C = jl.verdict, jl.cls
rnd = jl.rnd
L = []

# ---------------------------------------------------------------- recall additions (ec none)

s = "airspan-networks"
S4 = NOTE_URL(s)
L += [V(s, "member", "The New Beginnings SPAC S-4 (2021) lists New Enterprise Associates 14, L.P. ($1,820,031) and "
        "NEA 15 Opportunity Fund ($180,072) buying Airspan's private Series H Senior Preferred, issued in December "
        "2020; NEA's earlier Airspan stock was the consideration for its 2018 sale of Mimosa (D8), so the member "
        "entry is the funds' own Series H money.", ec="fund_filing", conf="high", cite=S4),
      C(s, stage="Growth", stage_src="web_verified", stage_cite=S4, stage_conf="high", entry_date="2020-12",
        country="US", city="Boca Raton", rng="below_1b", focus="Data Infrastructure",
        rounds=[rnd("2020-12", "Series H Senior Preferred", 10400000, None, True, S4, "filing")],
        note="Entry is NEA 14 and NEA 15 Opportunity buying Series H in December 2020 (S-4 certain-transactions "
             "table), not the 2018 Mimosa sale stock. Status stays as prefilled.")]

s = "clearcommerce"
u = NOTE_URL(s)
L += [V(s, "member", "The January 2005 asset purchase agreement by which eFunds bought ClearCommerce is signed as "
        "stockholders by New Enterprise Associates VIII, L.P. and New Enterprise Associates 8A, L.P. beside "
        "Austin Ventures VII: NEA funds held the private company.", ec="fund_filing", conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="Austin", stage="undetermined",
        focus="Fintech & Payments", rounds=[],
        note="eFunds bought ClearCommerce's business under the January 11, 2005 asset purchase agreement. The "
             "filing names no series NEA bought, so the stage is undetermined.")]

s = "creekpath-systems"
HC = "https://hedgeco.net/news/04/2003/creekpath-takes-the-reins-in-vc-search.html"
L += [V(s, "member", "An April 2003 report says CreekPath closed $16.8 million of second-round financing in November "
        "(2002) 'led by investment firm New Enterprise Associates'; Opsware's July 2006 merger agreement sends the "
        "holders' representative notices care of New Enterprise Associates.", ec="web", conf="high", cite=HC),
      C(s, status="acquired", rng="below_1b", country="US", city="Longmont", stage="Growth",
        stage_src="web_verified", stage_cite=HC, stage_conf="high", entry_date="2002-11",
        focus="Data Infrastructure",
        rounds=[rnd("2002-11", "second round (Series B preferred)", 16800000, "New Enterprise Associates", True,
                    HC, "press")],
        note="NEA led the second round (November 2002, $16.8M) with original investors TeleSoft and Sequel "
             "following; the merger agreement's capital stock is Series A and Series B preferred, so NEA's entry "
             "is the Series B. Acquired by Opsware (agreement July 7, 2006).")]

s = "egreetings"
u = NOTE_URL(s)
L += [V(s, "member", "The IPO prospectus (S-1/A, 1999) shows New Enterprise Associates VIII, NEA Presidents Fund "
        "and NEA Ventures 1999 holding Egreetings stock, bought in its private Series F (March to April 1999) and "
        "Series G (October 1999) rounds; Stewart Alsop (NEA general partner) director since March 1999.",
        ec="fund_filing", conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="San Francisco", stage="Growth",
        stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="1999-03",
        focus="Consumer & Marketplaces",
        rounds=[rnd("1997-12", "Series D", 5900000, None, False, u, "filing"),
                rnd("1999-03", "Series F", 26100000, None, True, u, "filing"),
                rnd("1999-10", "Series G", 23600000, None, True, u, "filing")],
        note="The certain-transactions table shows NEA with Series F and G shares and none of Series B to D, so "
             "NEA entered at the Series F. Egreetings listed in December 1999 and was taken private by "
             "AmericanGreetings.com's tender offer in 2001.")]

s = "emphasys-medical"
u = NOTE_URL(s)
DS1 = "https://www.sec.gov/Archives/edgar/data/1411380/000119312507205152/ds1.htm"
L += [V(s, "member", "Emphasys Medical's Fourth Amended and Restated Investors' Rights Agreement (June 29, 2006, an "
        "S-1 exhibit) lists New Enterprise Associates VIII and New Enterprise Associates 8A among its Series B, C, "
        "D and E investors and has both funds sign as investors.", ec="fund_filing", conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="Redwood City", stage="Growth",
        stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="2001-07",
        focus="Healthcare & Bio",
        rounds=[rnd("2001-07", "Series B", 8900000, None, True, DS1, "filing")],
        note="NEA's funds appear first among the Series B investors (none in the Series A list); the S-1 dates the "
             "Series B to July and August 2001 at $1.50 a share. The 2007 IPO was withdrawn; Pulmonx bought all of "
             "Emphasys's assets on May 13, 2009 after its failure, an asset sale out of insolvency.")]

s = "entevo"
u = NOTE_URL(s)
L += [V(s, "member", "BindView's 2001 resale prospectus lists the shares it issued in its acquisition of Entevo "
        "Corporation (February 2000), and the selling holders include New Enterprise Associates VII L.P. (45,484), "
        "NEA Presidents Fund and NEA Ventures 1998: NEA funds held the private company.", ec="fund_filing",
        conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="Arlington", stage="undetermined",
        focus="Security", rounds=[],
        note="Acquired by BindView in February 2000. The filing names no round NEA bought, so the stage is "
             "undetermined; city from knowledge (a Northern Virginia directory-administration software maker).")]

s = "home-account-network"
u = NOTE_URL(s)
L += [V(s, "member", "InteliData's 2001 resale prospectus covers shares issued for its January 2001 acquisition of "
        "Home Account Holdings, and the selling holders include 'NEA Enterprise Associates VIII Limited Partnership' "
        "(1,041,138 shares), NEA Presidents Fund and NEA Ventures 1999.", ec="fund_filing", conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", stage="undetermined", focus="Fintech & Payments",
        flags=["city_unknown"], rounds=[],
        note="Acquired by InteliData on January 11, 2001 for about $320,000 cash and 6.9 million shares. No source "
             "on disk places the company's city, and no round NEA bought is named.")]

s = "linkdoc"
u = NOTE_URL(s)
L += [V(s, "member", "LinkDoc's F-1 (2021) shows New Enterprise Associates 15 and NEA Ventures 2015 holding Series A "
        "preference shares and designating the Series A director, with NEA 15 also buying Series D (June 2018, "
        "$8.8M) and Series D+ (September 2020, $3.0M); China desk.", ec="fund_filing", conf="high", cite=u),
      C(s, status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_cite=u,
        stage_conf="high", entry_date="2015", country="CN", country_src="web_verified", country_cite=u,
        city="Beijing", focus="Healthcare & Bio",
        rounds=[rnd("2015", "Series A preference", None, None, True, u, "filing"),
                rnd("2018-06-08", "Series D preference", 8800000, None, True, u, "filing"),
                rnd("2020-09-04", "Series D+ preference", 3000000, None, True, u, "filing")],
        note="NEA holds Series A shares and names the Series A director, so NEA entered at the Series A; the "
             "company began operating in December 2014 and the co-investing vehicle is NEA Ventures 2015, which "
             "dates the entry to 2015. The last priced round, Series D+ at about $2.54 a share on 311.6M "
             "as-converted shares, implies roughly $0.8B, below $1B; the 2021 US IPO was withdrawn.")]

s = "luxn"
u = NOTE_URL(s)
L += [V(s, "member", "Sorrento Networks' 2003 S-3 resale table lists New Enterprise Associates VIII, 10 and 8A among "
        "the holders paid in shares at the closing of its acquisition of LuxN, Inc., a private company.",
        ec="fund_filing", conf="high", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="Sunnyvale", stage="undetermined",
        focus="Data Infrastructure", rounds=[],
        note="Acquired by Sorrento Networks on August 8, 2003; the filing names no round NEA bought. Status, city "
             "and focus agree with the Menlo row.")]

s = "mayan-networks"
u = NOTE_URL(s)
L += [V(s, "member", "Ariel's 2001 S-4 for its merger with MAYAN Networks lists New Enterprise Associates VII and "
        "VIII, NEA Presidents Fund and NEA Ventures 1998 among MAYAN's preferred holders, and states the August "
        "1998 Series B went to 'entities affiliated with New Enterprise Associates and U.S. Venture Partners'.",
        ec="fund_filing", conf="high", cite=u),
      C(s, status="unknown", rng="below_1b", country="US", city="San Jose", stage="Growth",
        stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="1998-08",
        focus="Data Infrastructure",
        rounds=[rnd(None, "Series A", 1526000, None, False, u, "filing"),
                rnd("1998-08", "Series B", 8000000, None, True, u, "filing"),
                rnd("1999-04", "Series C", None, None, True, u, "filing")],
        note="NEA co-bought the Series B (August 1998, 7,843,137 shares at $1.02) with USVP; the Series A was "
             "individuals only. Status stays unknown as in the TCV row: the 2001 Ariel merger's completion is not "
             "on record.")]

s = "nanoopto"
u = NOTE_URL(s)
L += [V(s, "member", "Excelsior Venture Partners III's report for the year to October 2001 says it invested $2 "
        "million in NanoOpto and that 'Bessemer Venture Partners, Morgenthaler and New Enterprise Associates are "
        "co-investors in NanoOpto'.", ec="web", conf="medium", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="Somerset", stage="undetermined",
        focus="Industrial & Robotics", rounds=[],
        note="A co-investor's SEC report names NEA as an investor; no round NEA bought is named. API Nanotronics "
             "bought all of NanoOpto's assets for $4 million on July 19, 2007 (API's 8-K press release).")]

s = "northern-power-systems"
u = NOTE_URL(s)
L += [V(s, "not_member", "R1 control test: under the June 4, 2008 asset purchase agreement, NEA Wind Acquisition "
        "Corp. and NEA Management Company bought substantially all of Northern Power Systems' assets out of its "
        "parent Distributed Energy Systems' bankruptcy sale. NEA acquired the business outright rather than taking "
        "a minority in a financing, so the row is out as a control_position.", ec="fund_filing", conf="high",
        cite=u)]

s = "pathnet"
u = NOTE_URL(s)
L += [V(s, "member", "Pathnet's 2001 10-K holder table shows New Enterprise Associates VI holding its private Series "
        "A, B and C preferred (41.7% of the class), with NEA VI an initial designee of the Series A holders and "
        "Peter Barris (NEA) a director since August 1995; the equity never listed.", ec="fund_filing",
        conf="high", cite=u),
      C(s, status="defunct", rng="below_1b", country="US", city="Reston", stage="Series A",
        stage_src="web_verified", stage_cite=u, stage_conf="high", entry_date="1995",
        focus="Data Infrastructure",
        rounds=[rnd("1995", "Series A preferred", None, None, True, u, "filing")],
        note="NEA VI held Series A from the start and named one of its two board designees; Barris joined the "
             "board in August 1995. Pathnet and its subsidiaries filed Chapter 11 in Delaware on April 2, 2001, "
             "with no going-concern sale on record, so defunct.")]

s = "stx-entertainment"
u = NOTE_URL(s)
HR = jl.NEWS(s, "Carmen Chang Added")
L += [V(s, "member", "Eros STX's 2020 F-3 lists New Enterprise Associates 16, L.P. among the 'STX Holders', the "
        "holders of the private STX Entertainment before the July 2020 merger, and Carmen Chang (NEA general "
        "partner) joined STX's board in November 2015 (NEA's own 2016 and 2018 releases list the seat). D8 does "
        "not apply: NEA held STX itself; the Eros STX shares are what it received for STX.", ec="fund_filing",
        conf="medium", cite=u),
      C(s, status="acquired", rng="below_1b", city="Burbank", stage="undetermined",
        focus="Media, Gaming & Advertising", rounds=[],
        note=f"No round NEA bought is named; NEA's board seat dates from November 2015 ({HR}). STX merged into "
             "Eros in July 2020 and was sold to The Najafi Companies in April 2022.")]

s = "visual-sciences"
u = NOTE_URL(s)
L += [V(s, "not_member", "In the February 2006 WebSideStory merger agreement, New Enterprise Associates 10 and NEA "
        "Ventures 2000 sign only as 'AVIVO INVESTOR', holders of WebSideStory stock received when WebSideStory "
        "bought Avivo in 2005, not as Visual Sciences unitholders; no NEA holding of Visual Sciences, LLC is shown "
        "(D8).", ec="fund_filing", conf="high", cite=u)]

s = "yipes-communications"
u = NOTE_URL(s)
L += [V(s, "member", "Jyra Research's 10-K (2001) says 'Yipes has received $291 million in funding from more than "
        "30 investors including Norwest Venture Partners, New Enterprise Associates (NEA)'.", ec="web",
        conf="medium", cite=u),
      C(s, status="acquired", rng="below_1b", country="US", city="San Francisco", stage="undetermined",
        focus="Data Infrastructure", rounds=[],
        note="A partner's SEC filing names NEA among Yipes' investors; no round NEA bought is named. Yipes went "
             "through Chapter 11 in 2002 and was bought by Reliance Globalcom in 2007.")]

# ---------------------------------------------------------------- Robert Croce (NEA venture partner 2008-14,
# venture advisor 2017-19). His seats sit with the Lewis Pell and David Auth group, the Fischell family and
# individual angels; no NEA listing, filing or press names an NEA fund in any of these companies.
CROCE = ("Robert Croce (NEA venture partner, later venture advisor) is a director of record, {x}; no NEA listing, "
         "NEA vehicle filing or press source names an NEA fund in the company, so the name match stands "
         "uncorroborated (D2, D4).")
L += [V("ancora-heart-inc", "not_member", CROCE.format(
          x="beside Lewis Pell and David Auth, the individual backers of the Pell companies; Ancora Heart is "
            "Guided Delivery Systems renamed (same CIK 1253687)"), ec="formd_adjudicated", conf="medium"),
      V("guided-delivery-systems-inc", "not_member", CROCE.format(
          x="beside Lewis Pell, David Auth and Glen Nelson (individual investors); the same company as the "
            "ancora-heart-inc row (CIK 1253687)"), ec="formd_adjudicated", conf="medium"),
      V("arstasis-inc", "not_member", CROCE.format(
          x="beside Lewis Pell, David Auth, Glen Nelson (GDN Holdings) and Samuel Navarro (Fractal Holdings), "
            "a Pell-backed company"), ec="formd_adjudicated", conf="medium"),
      V("svelte-medical-systems-inc", "not_member", CROCE.format(
          x="later also an executive officer, of the Fischell family's New Jersey stent company"),
        ec="formd_adjudicated", conf="medium"),
      V("vascular-therapies-llc", "not_member", CROCE.format(
          x="listed at his home address in Stuart, Florida among individual directors: a personal seat"),
        ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Perry Wallack: a homonym. The Form D seats
# belong to Perry A. Wallack, Cornerstone OnDemand's CFO (executive officer on its 2010 Form D) and later an
# independent director; NEA's Perry Wallack is an associate whose team page dates from 2025 and whose deals are
# Anterior, Curana Health, Habitat Health, In-House Health, Marathon Health and NeueHealth.
WAL = ("Homonym: the Perry Wallack on this Form D is {x}; NEA's Perry Wallack is an associate listed on the team "
       "page from 2025, and no NEA listing, filing or press source names an NEA fund in the company.")
L += [V("cornerstone-ondemand-inc", "not_member", WAL.format(
          x="Perry A. Wallack, Cornerstone OnDemand's own executive officer (CFO) in 2010, an operator job"),
        ec="formd_adjudicated", conf="high"),
      V("kareo-inc", "not_member", WAL.format(
          x="the former Cornerstone OnDemand CFO sitting as a director (2018) beside Kareo's investors; Kareo "
            "became Tebra (same CIK 1327870)"), ec="formd_adjudicated", conf="high"),
      V("tebra-technologies-inc", "not_member", WAL.format(
          x="the former Cornerstone OnDemand CFO continuing as a director after Kareo became Tebra (same CIK "
            "1327870, 2022)"), ec="formd_adjudicated", conf="high"),
      V("procore-technologies-inc", "not_member", WAL.format(
          x="the former Cornerstone OnDemand CFO as an independent director (2016-18) beside Bessemer and "
            "ICONIQ; NEA is not among Procore's holders"), ec="formd_adjudicated", conf="high"),
      V("arine-inc", "not_member", WAL.format(
          x="a director on Arine's May 2025 round, before NEA's associate joined (team page June 2025); Arine is "
            "not on NEA's list or its associate's deals"), ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Jimmy Treybig (NEA venture partner from 2002,
# venture advisor 2017-19), Austin. His Austin seats are personal: WhiteGlove's S-1 shows him an option-
# compensated director with no NEA fund among its holders.
TRE = ("Jimmy Treybig (NEA venture partner, Austin) is a director of record{x}; no NEA listing, NEA vehicle filing "
       "or press source names an NEA fund in the company, so the name match stands uncorroborated (D2, D4).")
WG = "https://www.sec.gov/Archives/edgar/data/1429664/000119312511225759/ds1a.htm"
L += [V("whiteglove-health-inc", "not_member", "WhiteGlove Health's S-1/A (2011) names Treybig's NEA role only in "
        "his biography, pays him director options, and lists no NEA fund among its holders; a personal board seat "
        "(D2). Same company as the whiteglove-house-call-health-inc row (CIK 1429664, renamed 2011).",
        ec="formd_adjudicated", conf="high", cite=WG),
      V("whiteglove-house-call-health-inc", "not_member", "WhiteGlove House Call Health's S-1 (2011) names Treybig's "
        "NEA role only in his biography, pays him director options, and lists no NEA fund among its holders; a "
        "personal board seat (D2). Same company as the whiteglove-health-inc row (CIK 1429664).",
        ec="formd_adjudicated", conf="high", cite=WG),
      V("erelevance-corporation-inc", "not_member", TRE.format(
          x=" of eRelevance (Austin), founded by WhiteGlove's Robert Fabbio, whose WhiteGlove seat was personal"),
        ec="formd_adjudicated", conf="medium"),
      V("naturallycurly-com-inc", "not_member", TRE.format(
          x=" of NaturallyCurly (Austin) on a $1.02M 2011 raise"), ec="formd_adjudicated", conf="medium"),
      V("olea-networks-inc", "not_member", TRE.format(
          x=" of Olea Networks (Bee Cave, Texas) on a $3.1M 2018 raise, after his NEA venture-advisor listing"),
        ec="formd_adjudicated", conf="medium")]

# ---------------------------------------------------------------- Krishna 'Kittu' Kolluri (NEA general partner
# to 2016, then Neotribe Ventures).
TCC = jl.SITE("the-climate-corporation")
SEEDPOST = jl.POST("vcs-and-angels-take-aim")
L += [V("climate-corp", "member", "Climate Corp (formerly WeatherBill, CIK 1380313) is The Climate Corporation, "
        "which the firm lists with a 2006 first investment; Kolluri, NEA general partner, sits as director at NEA's "
        "2855 Sand Hill Road address. Duplicate of the-climate-corporation.", ec="site_listing", conf="high",
        cite=TCC),
      C("climate-corp", status="acquired", rng="below_1b", city="San Francisco", focus="Climate & Energy",
        stage="Seed", stage_src="first_party", stage_cite=SEEDPOST, stage_conf="medium", entry_date="2006",
        flags=["identity_conflated", "stage_disputes_band"],
        note="Same company as the-climate-corporation and weatherbill-inc (CIK 1380313). NEA's own post names The "
             "Climate Corporation among its seed investments and the firm's first-invested year is 2006, so the "
             "2012 Form D is a follow-on, not the entry. Acquired by Monsanto (2013). Graduation left for the "
             "graduation pass."),
      V("weatherbill-inc", "member", "WeatherBill is The Climate Corporation's earlier name (same CIK 1380313), "
        "listed by the firm with a 2006 first investment; Kolluri sits as director at NEA's 2855 Sand Hill Road "
        "address. Duplicate of the-climate-corporation.", ec="site_listing", conf="high", cite=TCC),
      C("weatherbill-inc", status="acquired", rng="below_1b", city="San Francisco", focus="Climate & Energy",
        stage="Seed", stage_src="first_party", stage_cite=SEEDPOST, stage_conf="medium", entry_date="2006",
        flags=["identity_conflated"],
        note="Same company as the-climate-corporation and climate-corp (CIK 1380313). NEA's own post names The "
             "Climate Corporation among its seed investments; first invested 2006. Acquired by Monsanto (2013). "
             "Graduation left for the graduation pass."),
      V("fortanix-inc", "not_member", "Kolluri's Fortanix seat (2017-19, beside Foundation Capital's Ashu Garg) "
        "postdates his NEA years (the team pages show him to 2016; he then founded Neotribe Ventures, a Fortanix "
        "backer); no NEA listing, filing or press source names an NEA fund in Fortanix.",
        ec="formd_adjudicated", conf="medium")]
VU = jl.SITE("vuclip")
L += [V("xinlab-inc", "member", "XinLab Inc. (Milpitas) is Vuclip: founders Nickhil Jakatdar and Xinhui Niu, with "
        "Kolluri (NEA) and Nick Sturiale (JAFCO) as directors; the firm lists Vuclip with a 2008 first investment "
        "and Wikipedia names NEA and JAFCO as its venture investors. Duplicate of vuclip.", ec="site_listing",
        conf="medium", cite=VU),
      C("xinlab-inc", status="acquired", rng="below_1b", city="Milpitas", focus="Media, Gaming & Advertising",
        stage="undetermined", entry_date="2008", flags=["identity_conflated", "stage_disputes_band"],
        note="Same company as the vuclip row. The firm's first-invested year (2008) precedes this 2009 Form D, so "
             "the filing is not NEA's entry and the entry round is not named. Acquired by PCCW.")]

# ---------------------------------------------------------------- Richard Whitney (NEA venture partner 2008-10,
# venture advisor to 2022).
L += [V("light-sciences-oncology-inc", "not_member", "Richard K. Whitney is one of eleven directors on Light "
        "Sciences Oncology's 2009 Form D, beside individual Seattle-area backers; no NEA listing, NEA vehicle "
        "filing or press source names an NEA fund in the company, so the name match stands uncorroborated.",
        ec="formd_adjudicated", conf="medium"),
      V("miles-ahead-holdings-llc", "not_member", "Homonym: Richard Christopher Whitney is an executive officer of "
        "Miles Ahead Holdings (formerly Whitney Logistics Holdings, Riverview, Florida), whose 2025 raise repaid his "
        "own note; not NEA's venture advisor.", ec="formd_adjudicated", conf="high"),
      V("rp-redwood-holdco-llc", "not_member", "A Richard Whitney is director of RP Redwood Holdco, LLC, an El "
        "Segundo healthcare holding LLC (2021); no NEA listing, filing or press source ties an NEA fund to it, and "
        "a holdco LLC is fund-shaped until shown to be an operating company (D5).", ec="formd_adjudicated",
        conf="medium")]

jl.write("m1a", L)
