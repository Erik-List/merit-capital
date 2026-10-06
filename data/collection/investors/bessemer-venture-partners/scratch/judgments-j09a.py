import sys; sys.path.insert(0, "scratchpad/j09")
from h import *
L = []
L.append(C("james-river", "acquired", "US", "Richmond", flags=["pre_spinout", "model_disputes_source"], date="1978", extra={"valuation_usd": None},
  note="Archive: BVP invested in 1978 as the company began an acquisition program, held the stock after its 1980 IPO until 1983; it became Fort James, later acquired by Georgia Pacific (archive). The prefilled public status and $230M figure look like a join to a different James River (the insurer) and are disputed. The archive names no round."))
L.append(C("k-health", "private", "US", "New York", "Healthcare & Bio",
  note="Last priced mark is the July 2024 $50M round at $900M (Globes, Bloomberg), below the $1.4B Jan 2021 mark; the 2023 round was a down round. Momentum check done 2026-10-01 via news search. No source ties Bessemer to a named round.",
  rng="below_1b", rounds=[rnd("2021-01","Series E",132000000,None,None,NEWS("k-health","Raises $132M"),"press"), rnd("2024-07","Equity round",50000000,None,None,NEWS("k-health","raises $50 million at $900M"),"press")]))
L.append(C("k2-intelligence","private","US","New York",focus="NONE",date="2010-09-03",
  note="Risk and investigations consultancy; BVP (Rob Stavis) invested Sept 2010 per the archive, which names no round. No sale or shutdown found in the record; reads private."))
L.append(C("kajeet","private","US","McLean",focus="Data Infrastructure",date="2005",
  note="Mobile broadband and connectivity services company (fka Integrated Mobile); archive lists a 2005 BVP investment with no round named. City from recall (Washington DC area, McLean); no sale found."))
L.append(verdict("kcm-biomedical","not_member","Fund-shaped entry: the firm's own description says KCM Biomedical 'invested in biotech companies', so it is a vehicle, not an operating company (decisions.md D7).",cite=ARCH("kcm-biomedical")))
L.append(C("kiran-energy","acquired","IN","Mumbai","Climate & Energy",date="2010-07",
  note="Mumbai-based grid-connected solar producer; acquired by Hinduja Power Corporation in 2018 (archive). Archive names no round."))
L.append(C("knowme","unknown","US",None,"Consumer & Marketplaces",date="2015-09-17",
  note="Video creation and sharing platform; archive shows a 2015 BVP investment and a 2016 exit year but no acquirer or shutdown, and no source found for what became of it. City not established."))
L.append(C("kovio","acquired","US","San Jose","Industrial & Robotics",date="2002",
  note="Printed-electronics maker; the sibling Kleiner Perkins book reads acquired (assets to Thin Film Electronics, recalled, not verified here). Aligned to the sibling. Archive names no round."))
L.append(C("kroll-bond-ratings","private","US","New York",focus="NONE",date="2010-08-23",
  note="Credit ratings agency (Kroll Bond Rating Agency, KBRA); BVP (Rob Stavis) invested Aug 2010, exit listed 2015. The firm still operates as KBRA. No round named."))
L.append(C("kronos","acquired","US","Lowell","SaaS",flags=["pre_spinout"],date="1979",
  note="Time clock maker (Kronos Inc.), listed by BVP with a 1979 investment and a 1984 exit; recalled that it went public in 1992, was bought by Hellman and Friedman in 2007 and merged into UKG in 2020 (from knowledge, not verified here). No round named."))
L.append(C("kupivip","defunct","RU","Moscow","Consumer & Marketplaces",date="2011-04-12",
  note="Russian private sale club (archive description places it in Russia, so RU is confirmed). Siblings Accel and Balderton read defunct; aligned to them. Archive names no round."))
L.append(C("lbms","acquired","GB","London","SaaS",date="1994",
  ccite=ARCH("lbms"),flags=["model_disputes_source"],
  note="LBMS (Learmonth and Burchett Management Systems), a process-management software developer; the archive places it in Europe and says it was acquired by Platinum in 1995. London from recall. The prefilled CZ came from a one-word name join and is disputed."))
L.append(C("life-bot","unknown",None,None,"AI & Applied AI",
  note="Voice app listed 2019 to 2022 with no year, partner or place; nothing found on what became of it."))
L.append(C("lifeharbor","acquired","US",None,"Fintech & Payments",date="2002",
  note="Listed as acquired by Vestmark (archive); no year or round given. City not established."))
L.append(C("light","acquired","US","Palo Alto","Industrial & Robotics",stage="Series A",src="web_verified",conf="high",cite=W("Light (company)"),date="2014-06",
  rounds=[rnd("2014-06","Series A",9700000,None,True,W("Light (company)"),"press")],flags=["model_disputes_source"],
  note="Light (multi-lens camera maker): June 2014 Series A of $9.7M from a group including Bessemer (Wikipedia). May 2022 John Deere acquired parts of Light and hired staff, so the business continued under an acquirer; aligned to the GV sibling. The prefilled JP and the DK siblings are other companies named Light (name collision)."))
L.append(C("lightlogic","acquired","US","San Jose","Industrial & Robotics",date="1999",
  note="WDM laser component maker acquired by Intel in 2001 (archive). The firm 'first invested' in 1999 but names no round."))
L.append(C("magnuson-computer-systems","unknown","US",None,"Industrial & Robotics",flags=["pre_spinout"],date="1979",
  note="IBM-compatible personal computer maker; archive shows a 1979 investment and a 1980 exit but no acquirer, and no source found for its fate."))
L.append(C("mainbancorp","unknown","US",None,focus="NONE",date="1996",
  note="Bank holding company with a 1996 BVP investment and a 2003 exit; the place and fate are not established."))
L.append(C("makersplace","private","US","San Francisco","Crypto & Web3",date="2021",
  note="NFT marketplace; Aug 2021 $30M funding with Sony Music participation reported, no $1B+ priced round found on the 2026-10-01 news check. No source names Bessemer's round."))
L.append(C("malachyte","private","US","New York","AI & Applied AI",date="2024",
  rounds=[rnd("2026-08","Seed",10000000,None,None,NEWS("malachyte","Raises $10 Million Seed"),"press")],
  note="Early-stage enterprise AI company, firm partnered 2024. A $10M seed round was reported Aug 2026; momentum check 2026-10-01 found no $1B round. Which round Bessemer entered is not stated."))
L.append(C("maxim-integrated-products",None,"US","San Jose","Industrial & Robotics",date="1983",
  note="Archive: BVP invested in Maxim's first three rounds, starting in 1983; the rounds are not named, so no stage is taken. Status acquired (Analog Devices) as prefilled."))
L.append(verdict("medi-assist","not_member","Control position: the firm's own memo recommends $16M 'to finance the management buyout of Medi Assist' (decisions.md D5, control addendum).",ec="web",cite=POST("memos/medi-assist")))
L.append(C("mellanox-technologies",None,None,"Yokneam","Data Infrastructure",stage="Growth",src="web_verified",conf="high",cite=FTS("Mellanox","S-1"),date="2001-10",
  rounds=[rnd("2001-10","Series D",None,"Bessemer Venture Partners",True,FTS("Mellanox","S-1"),"filing")],
  note="Archive: Rob Chandra led the financing in late 2001. Mellanox's investor rights agreement (S-1 exhibit) gives BVP the Series D Redeemable Preferred board seat, so the entry round is the Series D. Acquired by NVIDIA in 2020 (status prefilled)."))
jl.write("j09a", L)
