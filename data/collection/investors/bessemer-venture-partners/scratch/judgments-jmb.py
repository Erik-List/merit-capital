"""PRO-80 Bessemer, judge jm, file b: Peter Lee (one row), Jeff Epstein, Michael Segal, Sheel Tyle, Aran Ron, Jay Po
and the Robert Goodman homonyms (batches 21 to 25). All not_member: none of these issuers is on the firm's own list
(live or archived) or its deal-partner map, and no source ties a Bessemer fund to any of them.
"""
import judge_lib as jl

NM = "not_member"
EC = "formd_adjudicated"
lines = []


def nm(slug, basis, conf="high"):
    lines.append(jl.verdict(slug, NM, basis, ec=EC, conf=conf))


# ---- Peter Lee (senior associate, Menlo Park, team pages 2012 to 2015)
nm("steel-house-inc", "Form D name match only: Bessemer's Peter Lee was a senior associate on the team pages of 2012 to 2015, a "
   "common name (homonym trap, decisions.md D6); this 2011 director seat of a Los Angeles ad-tech company predates his "
   "window and belongs to a Los Angeles investor of the same name; the issuer is not on the firm's list or deal-partner map.")

# ---- Jeff Epstein: Operating Partner since 2011 (the firm's own team page; AvePoint's and Booking's proxies say so).
# An operating partner's own board seats are not fund positions (decisions.md D4 and D6).
JE = ("Jeff Epstein is a Bessemer Operating Partner (the former Oracle CFO), and an operating partner's own board seat "
      "is not a fund position (decisions.md D4, D6); the issuer is not on the firm's own list or deal-partner map and "
      "no Bessemer fund appears in any round. ")
nm("appirio-inc", JE + "Appirio's backers were Sequoia, GGV and General Atlantic; he sat on its board as an independent director.")
nm("monsoon-commerce-inc", JE + "He is an independent director on the 2013 filing.")
nm("metamarkets-group-inc", JE + "He is an independent director on the 2013 and 2015 filings.")
nm("avepoint-inc", JE + "He reached AvePoint's board as co-chief executive of the blank-check company Apex Technology "
   "Acquisition, which merged with AvePoint in 2021 (AvePoint's S-1); a sponsor seat, not a venture round (D5).")
nm("global-eagle-entertainment-inc", JE + "He joined the board of the listed company in January 2013 at its blank-check "
   "merger (the company's own 8-K); a public-company directorship.")
nm("return-path-inc", JE + "He is an independent director on the 2013 to 2016 filings; Return Path's venture backers were "
   "Union Square, Sutter Hill and others.")
nm("booking-holdings-inc", JE + "He was an independent director of the listed company (its 2018 proxy names him as a "
   "Bessemer Operating Partner); a public-company directorship, T3.")
nm("vendr-inc", JE + "He is an independent director on the 2021 and 2022 filings; the rounds were led by Tiger Global, "
   "Craft and others.")
nm("us-patent-innovations-llc", "Form D name match only: the director of this Lakeland, Florida medical device LLC "
   "(2010 to 2013) is another Jeffrey Epstein, a homonym (decisions.md D6: Jeff Epstein is a named homonym trap); the "
   "issuer is not on the firm's list and no source ties Bessemer to it.")
nm("zferral-inc", "Form D name match only: the executive officer of Zferral (Ambassador, Royal Oak, Michigan) is its own "
   "founder Jeffrey Epstein, a homonym of the Bessemer operating partner (decisions.md D6); the issuer is not on the "
   "firm's list and no source ties Bessemer to it.")

# ---- Michael Segal: analyst in Larchmont (team page 2010), senior associate in San Francisco (2017 to 2018)
MS = ("Form D name match only: Bessemer's Michael Segal was an analyst and later a senior associate (team pages 2010 and "
      "2017 to 2018), a common name (homonym trap, decisions.md D6); the issuer is not on the firm's own list or "
      "deal-partner map and no source ties a Bessemer fund to it. ")
nm("biostar-pharmaceuticals-inc", MS + "The 2009 filings name a director of a Shaanxi, China drug maker listed through a "
   "reverse merger, another person.")
nm("china-power-equipment-inc", MS + "The 2009 filing names a director of a Xi'an, China reverse-merger company, another person.")
nm("asia-carbon-industries-inc", MS + "The 2010 filings name a director of a China reverse-merger company, another person.")
nm("simulconsult-inc", MS + "The executive officer of SimulConsult (Brookline, Massachusetts, 2010 to 2023) is its founder, "
   "a physician of the same name.")
nm("wonderhop-inc", MS + "The 2012 filing names him as an executive officer of the issuer, an operator job, not an investor seat.")
nm("boston-materials-inc", MS + "The 2018 to 2025 filings name a co-founder and officer of Boston Materials, an operator "
   "job, not an investor seat.")

# ---- Sheel Tyle: on the team page in 2012 only; then New Enterprise Associates, then his own firm Amplo
ST = ("Seat outside the person's Bessemer window (decisions.md D6): Sheel Tyle appears on the firm's team page in 2012 "
      "only, then worked at New Enterprise Associates and founded Amplo; the issuer is not on the firm's own list or "
      "deal-partner map and no Bessemer fund appears in its rounds. ")
nm("andela-inc", ST + "His Andela board seat (2015 to 2021) came with his own and later Amplo's money.")
nm("blend-systems-inc", ST + "His Blend seat (2015 to 2017) dates from his New Enterprise Associates years.")
nm("learnup-inc", ST + "His LearnUp seat (2015 to 2016) dates from his New Enterprise Associates years.")
nm("freightwalla-inc", ST + "The 2019 filing dates from his Amplo years.")
nm("locale-hospitality-inc", ST + "The 2020 filing dates from his Amplo years.")
nm("collectable-technologies-inc", ST + "The 2021 filing dates from his Amplo years.")

# ---- Aran Ron: Operating Partner specialising in healthcare (team pages 2010 and 2012); then a founder
AR = ("Aran Ron was a Bessemer Operating Partner in healthcare (team pages 2010 to 2012) who went on to found and run "
      "hospital-services companies; an operating partner's own company is not a fund position (decisions.md D4, D6). "
      "The issuer is not on the firm's own list or deal-partner map and no Bessemer fund appears in its rounds. ")
nm("data-driven-delivery-systems-llc", AR + "He is a director of this New York LLC in 2012 to 2014, one of the hospital-services companies he built after his operating-partner years.")
nm("accuity-delivery-systems-llc", AR + "He is a director of Accuity in 2016 to 2017, one of his own hospital-services companies; it was "
   "sold to Frazier Healthcare Partners in 2020.")
nm("kaden-health-inc", AR + "He is an executive officer of the issuer in 2020, an operator job.")
nm("second-wave-delivery-systems-llc", AR + "He is a director of this Las Vegas LLC in 2020 to 2021, one of his own ventures.")
nm("third-wave-recovery-systems-llc", AR + "He is a director of this Las Vegas LLC in 2022, one of his own ventures.")

# ---- Jay Po: joined Bessemer in 2014 (team pages 2017 to 2018); then Stage 2 Capital
JP = ("Seat outside the person's Bessemer window (decisions.md D6): Jay Po joined Bessemer in 2014 and is last on the "
      "team page in 2018; he then became a partner at Stage 2 Capital. The issuer is not on the firm's own list or "
      "deal-partner map and no Bessemer fund appears in its rounds. ")
nm("listreports-inc", JP + "The 2020 filing dates from his Stage 2 Capital years.")
nm("arcade-solutions-inc", JP + "The 2021 filing dates from his Stage 2 Capital years.")
nm("negotiatus-corp", JP + "The 2021 to 2026 filings of Negotiatus (Order.co) date from his Stage 2 Capital years.")
nm("gigpro-inc", JP + "The 2022 to 2024 filings date from his Stage 2 Capital years.")
nm("steelhead-technologies-inc", JP + "The 2023 to 2024 filings date from his Stage 2 Capital years.")

# ---- Robert (Bob) Goodman: partner since 1998, New York; a common name
RG = ("Form D name match only: Bessemer's Bob Goodman is a New York partner (since 1998) with a common name (decisions.md "
      "D6); the issuer is not on the firm's own list or deal-partner map and no source ties a Bessemer fund to it. ")
nm("convoke-media-inc", RG + "The 2010 filings name a Robert Goodman as an executive officer of the issuer, an operator, "
   "and later as its director; another person.")
nm("sagacity-media-inc", RG + "The director of this Portland, Oregon magazine publisher (2010 to 2012) is another "
   "person of the same name (an Oregon issuer).")
nm("crosscurrent-inc", RG + "The director of this Portland, Oregon health company (2013) is another person of the same name (an Oregon issuer).")
nm("ni-q-llc", RG + "The director of this Wilsonville, Oregon LLC (2017 to 2020) is another person of the same name (an Oregon issuer).")
nm("physicians-surgery-center-llc", RG + "The director of this Durango, Colorado surgery centre (2009 to 2012) is another person.")
nm("good-earth-minerals-llc", RG + "The executive officer of this Denver minerals LLC (2024) is another person.")
nm("designed-technology-inc", RG + "The 2020 filing is a $250,000 raise by a Sudbury, Massachusetts company; nothing "
   "identifies the director as the Bessemer partner, and a seat on a raise of that size would be personal in any case (D4).",
   conf="medium")

assert len(lines) == 40, len(lines)
jl.write("jmb", lines)
