import sys; sys.path.insert(0, "scratchpad/j09")
from h import *
L = []
PV = "https://www.uktech.news/news/investment-news/fintech-startup-previse-closes-7m-series-a-20180820"
L.append(C("polaris-petroleum","acquired","CA",None,focus="NONE",flags=["pre_spinout"],date="1978",
  note="Oil and gas explorer in western Canada (archive), acquired by Cabre Exploration (exit 1993). City not established. No round named."))
L.append(C("portrait-software","acquired","GB","Reading","SaaS",flags=["listed_purchase_check"],date="2002",
  note="UK customer analytics software plc (fka AIT Group), recalled as acquired by Pitney Bowes in 2010 (not verified here). AIT Group was already listed on the London exchange, so whether the 2002 BVP investment was a purchase of a listed company (decisions.md D5) is not shown by the archive; kept as listed, flagged for review."))
L.append(C("powergenix","unknown","US","San Diego","Climate & Energy",date="2008",
  note="Nickel-zinc battery maker; archive shows a 2008 investment (Justin Label), listed in 2010 only, no source found for its fate. City from recall."))
L.append(C("powertel-pcs-partners","acquired","US",None,"Data Infrastructure",date="1994",
  note="Southeastern PCS wireless network operator acquired by Deutsche Telekom (archive, 2001). City not established. No round named."))
L.append(C("previse","private","GB","London","Fintech & Payments",stage="Series A",src="web_verified",conf="high",cite=PV,date="2018-08",
  ccite=ARCH("previse"),
  rounds=[rnd("2017","Seed",2580000,"Hambro Perks",False,"https://www.pymnts.com/news/b2b-payments/2017/previse-lands-millions-for-ai-powered-invoice-financing-platform/","press"),
          rnd("2018-08","Series A",7000000,"Augmentum Fintech; Bessemer Venture Partners",True,PV,"press")],
  note="Series A of $7M led by Augmentum Fintech and Bessemer (Aug 2018, UK Tech News); the earlier seed was Hambro Perks, not Bessemer. A later $11M round led by Mastercard and Reefknot had Bessemer participating. Momentum check 2026-10-01: no $1B round found. Graduation not applicable."))
L.append(C("proteon-therapeutics",None,"US","New York","Healthcare & Bio",rng=None,date="2009-04-17",
  note="Archive: Chris Gabrieli invested April 2009; the 2014 S-1 draft lists Bessemer VII among holders with convertible notes. The same registrant became Protara Therapeutics (New York) after a 2020 merger, so the current city is used. Round not named."))
L.append(C("psinet","defunct","US","Herndon","Data Infrastructure",date="1993",flags=["model_disputes_source"],
  note="First venture-backed internet service provider; BVP invested in its early rounds from 1993 (archive), IPO 1995. The prefilled CN is a one-word name join and is disputed. The rounds are not named."))
L.append(C("quantor","acquired","US",None,focus="NONE",flags=["pre_spinout"],date="1970",
  note="Listed with a 1970 investment and as acquired by NCR (archive); the line of business is not stated and no further source was found."))
L.append(C("quantum-effect-devices",None,"US","Santa Clara","Industrial & Robotics",stage="Growth",src="first_party",conf="medium",cite=ARCH("quantum-effect-devices"),date="1998",
  note="Archive: Rob Chandra led BVP's investment in the company's later rounds, so the entry was a later round. IPO and PMC-Sierra acquisition in 2000. City matches the Lightspeed sibling."))
L.append(C("qwilt","private","US","Redwood City","Data Infrastructure",date="2013-05-31",
  rounds=[rnd("2021-09","Series E",70000000,"Cisco",None,NEWS("qwilt","Series E led by Cisco"),"press")],
  note="Last priced mark is the Sept 2021 Series E at $800M (Calcalist), below $1B; Calcalist (July 2025) reports the CEO left as it weighs mergers. Which round Bessemer entered in 2013 is not named. City matches the Accel sibling; Redpoint's IL country is the R&D base, not the headquarters."))
L.append(C("rabbit","unknown","US",None,"Consumer & Marketplaces",date="2015-05-21",
  note="Rabbit (watch-together service); the GV sibling reads acquired, other siblings unknown, and no source was read here for its fate, so unknown stays. Aligned later if a source is found."))
L.append(C("radiation-dynamics","acquired","US",None,"Industrial & Robotics",flags=["pre_spinout"],date="1974",
  note="Listed as acquired by Monsanto (archive); a 1974 investment. City not established. No round named."))
L.append(C("register-com","acquired","US","New York","SaaS",date="1998",
  note="Domain registration company, IPO 2000 per the archive exit; recalled as bought by Vector Capital in 2005 (not verified here). The 1998 or 1999 round is not named."))
L.append(C("relish","unknown","US",None,"Consumer & Marketplaces",
  note="Relationship coaching app listed 2020 to 2022 with no year or partner; no source found for its place or fate."))
L.append(C("remedinet","private","IN",None,"Healthcare & Bio",date="2013-03-14",
  note="Healthcare information exchange and claims software (fka HealthSprint); still named as a board seat in the firm's June 2021 post. Duplicate of the row remidinet, which is the later spelling. No round named."))
L.append(C("remidinet","private","IN",None,"Healthcare & Bio",
  note="India-based cashless healthcare software; same company as the row remedinet (later spelling on the 2022 list), classified alike. No round named."))
L.append(C("resonext","acquired","US",None,"Industrial & Robotics",date="1998",
  note="CMOS high-frequency communications chips maker acquired by RF Microdevices (archive, 2002). City not established. No round named."))
L.append(C("revver","acquired","US","Los Angeles","Media, Gaming & Advertising",date="2005",
  note="Video sharing site launched in 2005 with Bessemer among its investors (Wikipedia); acquired by LiveUniverse (archive). City from recall. The round is not named."))
L.append(C("riddhi-siddhi-gluco-biols","unknown","IN",None,focus="NONE",flags=["listed_purchase_check"],date="2006-12-29",
  note="Indian starch maker with an end-2006 BVP India investment and a 2014 exit. It may have been a listed company at the time (a purchase, decisions.md D5), which this pass could not check; flagged for review. Present status not established."))
L.append(C("rilla","private","US","New York","AI & Applied AI",date="2023",
  rounds=[rnd("2025-06","Series B",68500000,"GV",True,"https://sacra.com/c/rilla/","vendor")],
  note="Vendor pages put the June 2025 Series B (led by GV, Bessemer participating) at about $757M post-money, so below $1B; momentum check 2026-10-01 found no $1B round. The firm partnered in 2023; the round of entry is not named (the site stage field is a default and is not used)."))
L.append(verdict("rockhealth","not_member","Fund-shaped entry: the firm's own description says Rock Health is a seed fund and startup accelerator, so it is another manager's vehicle (decisions.md D7).",cite=ARCH("rockhealth")))
L.append(C("sagence","unknown","US",None,"SaaS",date="2010-12-21",
  note="Competency-based education technology for colleges; archive shows a Dec 2010 investment and a 2017 listing only, no source found for its fate."))
jl.write("j09d", L)
