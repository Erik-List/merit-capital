import sys; sys.path.insert(0, "scratchpad/j09")
from h import *
L = []
L.append(C("obsidian","acquired","US",None,"Industrial & Robotics",date="1997",
  note="Chemical mechanical polishing equipment maker acquired by Applied Materials (archive, 1999). City not established. No round named."))
L.append(C("oclassen-pharmaceuticals","acquired","US","San Rafael","Healthcare & Bio",date="1990",
  note="Therapeutics developer, exit 1997 in the archive; recalled as acquired by Watson Pharmaceuticals (from knowledge, not verified here). No round named."))
L.append(C("octave-communications","acquired","US",None,"Data Infrastructure",date="1999",
  note="Listed as acquired by Voyant, itself bought by Polycom (archive). Country from the firm's region-less listing and recall; city not established. No round named."))
L.append(C("ocular-networks","acquired","US",None,"Data Infrastructure",date="2000-01-11",
  note="Optical access equipment maker acquired by Tellabs (archive, 2002); the archive places it in the East region. City not established. No round named."))
L.append(C("omnia-communications","acquired","US",None,"Data Infrastructure",date="1996",
  note="Voice and data access multiplexers maker acquired by Ciena in 1999 (archive). City not established. No round named."))
L.append(C("on-technology","acquired","US","Waltham","SaaS",date="1994",
  note="LAN applications vendor that went public and was acquired by Symantec in 2002 (archive). City from recall. No round named."))
L.append(C("onecloud-labs","unknown","US",None,"Data Infrastructure",date="2013-10-28",
  note="Disaster recovery as a service on public cloud; archive shows an Oct 2013 investment, listed to 2016, with no source found for its fate."))
L.append(C("onestop-internet","unknown","US",None,"Consumer & Marketplaces",date="2008-10-16",
  note="Outsourced e-commerce technology and distribution; archive shows an Oct 2008 investment (Jeremy Levine) and a listing to 2018, no source found for its fate."))
L.append(C("onmobile","public","IN","Bangalore","Media, Gaming & Advertising",flags=["listed_purchase_check"],date="2007-12-27",
  note="Indian mobile value-added services company listed on the Indian exchanges in 2008 (archive); the Dec 2007 investment looks pre-listing, but that sequence and the round are not verified here, so the stage is left open. Reads below $1B on a small-cap listing, no figure cited."))
L.append(C("onx","private","US","Missoula","Consumer & Marketplaces",stage="Growth",src="web_verified",conf="high",cite=NEWS("onx","onX Closes"),date="2018-02",
  rounds=[rnd("2018-02","Growth equity",20300000,"Summit Partners",True,NEWS("onx","onX Closes"),"press")],
  note="Summit Partners' release of the $20.3M growth equity round (Feb 2018) lists Bessemer among additional investors; that matches the firm's own Feb 15, 2018 date. No $1B mark found; the TCV sibling reads below $1B."))
L.append(C("opta-food-ingredients","acquired","US","Bedford",focus="NONE",date="1990",
  note="Food additive maker, listed with a 1992 exit (IPO); siblings Menlo and NEA read acquired and Bedford, aligned. No round named."))
L.append(C("orient-green-power","public","IN","Chennai","Climate & Energy",date="2007-09-14",
  note="Wind, hydro and biomass power operator listed in October 2010 (archive), so the Sept 2007 BVP investment was before listing. The round is not named. Small-cap listing, reads below $1B with no figure cited."))
L.append(C("oryx-vision","defunct","IL",None,"Industrial & Robotics",date="2016",
  ccite=NEWS("oryx-vision","Shuts Down"),
  note="Depth-sensing lidar startup; Calcalist (Aug 2019) reports it shut down, which also places it in Israel. City not established. Which round Bessemer entered is not named."))
L.append(C("oxagen","unknown","GB","Abingdon","Healthcare & Bio",date="2005-05-09",
  note="Biopharma developer of asthma drugs; the archive places it in Europe and Rob Chandra led. City from recall (Abingdon, UK). No source found for its later fate. No round named."))
L.append(C("oximetrix","acquired","US",None,"Healthcare & Bio",flags=["pre_spinout"],date="1978",
  note="Medical device maker acquired by Abbott (archive, exit 1985). City not established. No round named."))
L.append(C("p-a-semi",None,"US","Santa Clara","Industrial & Robotics",date="2004-09-13",
  note="Microprocessor maker acquired by Apple in 2008 (archive, status prefilled). No round named."))
L.append(C("palogix-infrastructure","unknown","IN",None,focus="NONE",date="2010-08-18",
  note="Developer and operator of private freight terminals in India; archive shows an Aug 2010 investment and a listing to 2019, no source found for its fate."))
L.append(C("parametric-technology",None,"US","Boston","SaaS",rng=None,date="1987",
  rounds=[rnd("1987","First institutional round",None,"Bessemer Venture Partners",True,ARCH("parametric-technology"),"firm")],
  note="Archive: BVP led the company's first institutional round in 1987; the round is not given a stage name, so the stage stays open. Public status and mark prefilled."))
L.append(C("perseptive-biosystems","acquired","US","Framingham","Healthcare & Bio",date="1989-12",
  note="Archive: BVP's Chris Gabrieli invested in December 1989; public in 1992, bought by Perkin Elmer in 1998. No round named."))
L.append(C("pillar","acquired","US",None,"SaaS",date="1987",flags=["model_disputes_source"],
  note="Budgeting software maker acquired by IMRS in 1994 (archive, West region). The prefilled JP is a one-word name join and is disputed; the sibling rows reading unknown are older and lack this archive line."))
L.append(C("pinnacle-engines-fmr-cleeves-engines-inc","unknown","US","San Carlos","Climate & Energy",date="2007-12-21",
  note="Engine architecture developer (fka Cleeves Engines); archive shows a Dec 2007 investment and a listing to 2019, no source found for its fate. City from recall."))
L.append(C("pinpoint","unknown","US","Austin","DevTools & APIs",stage="Series A",src="first_party",conf="high",cite=POST("bessemer-series-a-investment-pinpoint"),date="2019-02",
  rounds=[rnd("2019-02","Series A",13500000,"Bessemer Venture Partners",True,POST("bessemer-series-a-investment-pinpoint"),"firm")],flags=["model_disputes_source"],
  note="The firm's own post says Bessemer led the $13.5M Series A (Feb 2019). Engineering analytics company in Austin; the prefilled RO is a one-word join and is disputed. Current status not established."))
L.append(C("pirus-networks","acquired","US","Acton","Data Infrastructure",date="2000-01-18",
  note="Storage networking developer acquired by Sun Microsystems (archive, 2002). City from recall. No round named."))
jl.write("j09c", L)
