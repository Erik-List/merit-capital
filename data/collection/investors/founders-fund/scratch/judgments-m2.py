"""Membership: four rows the build seeded from ownership filings whose fund filers are not Founders Fund vehicles."""
from jl import *
M = "D3/T1: the ownership filings on this issuer are Mithril's (Mithril LP, Mithril II LP and their general partners, with Ajay Royan), co-filed by Peter Thiel as a Mithril principal. No Founders Fund vehicle is on any of them; Mithril is a separate firm."
NM("adagio-therapeutics-inc", M, cls="fund_filing", cite="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1832038&type=3&dateb=&owner=include&count=40")
NM("blacksky-technology-inc", M, cls="fund_filing", cite="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1753539&type=3&dateb=&owner=include&count=40")
NM("fractyl-health-inc", M, cls="fund_filing", cite="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1572616&type=3&dateb=&owner=include&count=40")
NM("pemco-aviation-group-inc", "D3/T1: the 2002 to 2004 filings are Clarium Capital's (Clarium Capital Ltd and Clarium Capital Management LLC, Thiel's hedge fund), three years before Founders Fund existed.", cls="fund_filing", cite="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=771729&type=SC&dateb=&owner=include&count=40")
write("m2-membership")
