import sys; sys.path.insert(0, "scratchpad/j09")
from h import *
L = []
L.append(C("metapath","acquired","US",None,"Data Infrastructure",date="1994",
  note="Wireless network planning software; archive says acquired by Mobile Systems International (itself a row, acquired by Marconi in 2000). Place not established. No round named."))
L.append(C("miasol","acquired","US","Santa Clara","Climate & Energy",date="2005",
  note="CIGS thin-film solar maker; recalled that Hanergy bought it in 2012 (from knowledge, not verified here). No round named."))
L.append(C("micro-peripherals","acquired","US","Chatsworth","Industrial & Robotics",flags=["pre_spinout"],date="1978",
  note="Early 5.25-inch disk drive maker, listed as acquired by CTS (archive, exit 1983). City from recall. No round named."))
L.append(C("microacquire","private","US",None,"Consumer & Marketplaces",stage="Seed",src="first_party",conf="high",cite=POST("microacquire-helps-startups-find-buyers"),date="2021-07",
  rounds=[rnd("2021-07","Seed",2800000,"Bessemer Venture Partners",True,POST("microacquire-helps-startups-find-buyers"),"firm")],
  note="The firm's own news post says Bessemer led the $2.8M seed round (July 2021). Marketplace for startup buyers and sellers (now Acquire.com); no $1B round found. Graduation left for the graduation pass."))
L.append(C("mind-pirate","unknown","US",None,"Media, Gaming & Advertising",date="2012-12-28",
  note="Augmented reality mobile games developer; archive shows a Dec 2012 BVP investment, listed to 2016, and nothing found on its fate."))
L.append(C("mobile-systems-international","acquired",None,"Cambridge",date="1998",
  note="Wireless telecom design services and software; acquired by Marconi plc in 2000 (archive). City from recall (Cambridge, UK). No round named."))
L.append(C("mobilian","acquired","US","Research Triangle Park","Industrial & Robotics",date="2000",
  note="Listed as acquired by Intel (archive, 2002 recalled); wireless chip maker. City from recall. No round named."))
L.append(C("mojave-networks","acquired","US",None,"Security",date="2013-03-12",
  note="Cloud mobile security; acquired by Sophos in October 2014 (archive). City not established. No round named."))
L.append(C("multiflow-computers","defunct","US","Branford","Data Infrastructure",date="1985",
  note="Minisupercomputer maker that ceased trading around 1990 (from knowledge, assets to other companies; not verified here). No round named."))
L.append(C("myco-pharmaceuticals","acquired","US","Cambridge","Healthcare & Bio",date="1990",
  note="Anti-viral and anti-cancer compound developer; acquired by Millennium in 1996 (archive). No round named."))
L.append(C("myglamm",None,"IN","Mumbai","Consumer & Marketplaces",rng=None,ccite=ARCH("myglamm"),
  note="Indian beauty brand (Good Glamm Group); the partner is on the India desk (Anant Vidur Puri board observer), so IN is confirmed. Prefilled status and mark kept; the sibling Accel row reads defunct, which this pass could not verify, so it is left for a later check. No Bessemer round named."))
L.append(C("nbx","acquired","US","Boston",flags=[],focus="Data Infrastructure",date="1996",
  note="Voice and data network product maker acquired by 3Com in 1999 (archive). City from recall. No round named."))
L.append(C("netambit","unknown","IN",None,"Fintech & Payments",date="2007-09-07",
  note="Indian outsourced sales and financial services distribution firm; archive shows a Sept 2007 investment, exit 2016, no acquirer. City not established. No round named."))
L.append(C("netframe-systems","acquired","US","Milpitas","Data Infrastructure",date="1988",
  note="Fault-tolerant superserver maker; recalled as acquired by Micron Electronics in 1997. City matches the Menlo sibling. No round named."))
L.append(C("netgenesis","acquired","US","Cambridge","SaaS",date="1996",
  note="Web analytics software; recalled as acquired by SPSS in 2001 (from knowledge, not verified here). No round named."))
L.append(C("netli","acquired","US","Mountain View","Data Infrastructure",date="2002-05-23",
  note="Web application acceleration service acquired by Akamai in 2007 (archive). No round named."))
L.append(C("netsys","acquired","US","Mountain View","Data Infrastructure",date="1994",
  note="Network management and simulation software acquired by Cisco in 1996 (archive). City from recall. No round named."))
L.append(verdict("new-vernon-capital","not_member","Fund-shaped entry: the firm's own description says New Vernon Capital 'makes investments in India', so it is an investing vehicle, not an operating company (decisions.md D7).",cite=ARCH("new-vernon-capital")))
L.append(C("newport-communications","acquired","US","Irvine","Industrial & Robotics",date="1998",
  note="Optical communications chip maker acquired by Broadcom in 2000 (archive). City from recall. No round named."))
L.append(C("nistevo","acquired","US","Eden Prairie","SaaS",date="1999",
  note="Collaborative logistics software acquired by Sterling (Sterling Commerce, archive). City matches the Insight sibling. No round named."))
L.append(C("nitrous-io","unknown","US",None,"DevTools & APIs",date="2012-08-09",
  note="Cloud development environment platform; archive shows an Aug 2012 investment and a listing to 2018, with no source found for its fate."))
L.append(C("numerax","unknown","US",None,focus="NONE",flags=["pre_spinout"],date="1974",
  note="Computerized freight tariff database company, 1974 investment and 1983 exit in the archive; no source found for its fate."))
jl.write("j09b", L)
