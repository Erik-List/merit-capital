# Batch o06 (PRO-169): the 1996-2012 book, T to Z (companies the judge can place now). Judge: this session, 2026-09-29.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post
U = "undetermined"
J = [
 {"s": "thinkorswim", "es": U, "hc": "US", "city": "Chicago", "f": "Fintech & Payments", "vr": "below_1b",
  "n": "Online options brokerage, Chicago. TCV invested in the private thinkorswim in 2004 (the firm's own release, tcv.com/news/thinkorswim.html) and received INVESTools shares when INVESTools bought it in February 2007 (TCV V's 4.27M shares in INVESTools' 2007 resale S-3; the firm's thinkorswim_merger release); the combined company renamed itself thinkorswim Group and was acquired by TD Ameritrade in 2009. Round not named."},
 {"s": "timesten", "st": "acquired", "es": U, "hc": "US", "city": "Mountain View", "f": "Data Infrastructure",
  "n": "In-memory database, Mountain View. acq. by Oracle, 2005; aligned with Lightspeed. Round not named."},
 {"s": "tinyprints", "st": "acquired", "es": U, "hc": "US", "city": "Sunnyvale", "f": "Consumer & Marketplaces",
  "n": "Online stationery, Sunnyvale. acq. by Shutterfly, 2011 (the Shutterfly stock in TCV's 13F 2011-2012 is the consideration). Round not named."},
 {"s": "top-layer-networks", "st": "acquired", "es": U, "hc": "US", "city": "Westborough", "f": "Security",
  "n": "Network intrusion prevention, Westborough MA. acq. by Corero, 2011. Round not named."},
 {"s": "total-sports", "st": "acquired", "es": U, "hc": "US", "city": "Raleigh", "f": "Media, Gaming & Advertising",
  "n": "Online sports content, Raleigh NC. acq. by Quokka Sports, 2000. Round not named."},
 {"s": "triversity", "st": "acquired", "es": U, "hc": "CA", "city": "Toronto", "f": "SaaS",
  "n": "Retail store software, Toronto. acq. by SAP, 2004. Round not named."},
 {"s": "vacationspot-com", "st": "acquired", "es": U, "hc": "US", "city": "Seattle", "f": "Consumer & Marketplaces",
  "n": "Vacation rental bookings, Seattle. acq. by Expedia, 2000. Round not named."},
 {"s": "vastera", "st": "acquired", "es": U, "hc": "US", "city": "Dulles", "f": "SaaS",
  "n": "Global trade management software, Dulles VA. Listed 2000; acq. by JPMorgan Chase, 2005; aligned with Battery. Round not named."},
 {"s": "vertical-networks", "st": "acquired", "es": U, "hc": "US", "city": "Sunnyvale", "f": "Data Infrastructure",
  "n": "IP telephony systems, Sunnyvale. acq. by Artisoft, 2004. Round not named."},
 {"s": "viant", "st": "acquired", "es": U, "city": "Boston", "f": None, "vr": "below_1b",
  "n": "Internet consulting, Boston. Listed 1999; merged into divine in 2002: acquired (divine itself later failed). The pre-filled 'defunct' reads divine's end. Consulting is outside the focus taxonomy. Round not named."},
 {"s": "vice", "st": "acquired", "es": "Growth", "esn": "Vice Media Gets $250 Million Investment From Venture Capital Firm", "ess": "web_verified", "econf": "high", "ed": "2014-09",
  "hc": "US", "city": "New York", "f": "Media, Gaming & Advertising",
  "n": "Youth media (Vice Group Holding), New York. TCV invested $250M in September 2014 (The Hollywood Reporter), after A&E and Hearst: Growth. Vice filed for Chapter 11 in 2023 and its business was bought by a lender group led by Fortress: acquired out of insolvency."},
 {"s": "whitepages", "st": "private", "vr": "below_1b", "es": U, "hc": "US", "city": "Seattle", "f": "Consumer & Marketplaces",
  "n": "People search, Seattle. WhitePages bought out its venture investors, TCV among them, for $80M in 2013 (GeekWire) and operates privately. TCV's round is not named."},
 {"s": "xacct-technologies", "st": "acquired", "es": U, "hc": "US", "city": "Santa Clara", "f": "SaaS",
  "n": "Billing mediation software, Santa Clara (R&D in Israel). acq. by Amdocs, 2004. Round not named."},
 {"s": "xiotech", "st": "acquired", "es": U, "hc": "US", "city": "Eden Prairie", "f": "Data Infrastructure",
  "n": "Storage systems, Eden Prairie MN. acq. by Seagate, 2000 (later spun out again). Round not named."},
 {"s": "xrs", "m": "not_member", "me": "fund_filing", "mconf": "high",
  "mc": "https://www.sec.gov/Archives/edgar/data/854398/000095012309069897/c55044exv99w1.htm",
  "mb": "bought into a listed company (T3, decisions.md D6, delta X1): XATA Corporation (renamed XRS in 2012) was listed on Nasdaq, and TCV's money came in December 2009, when 'XATA Corporation (Nasdaq: XATA) ... received $30 million in funding from Technology Crossover Ventures (TCV) and Trident Capital' (the 8-K exhibit of 2009-12-10). Christopher Marshall's seat from 2003 was Trident's (he joined TCV in May 2008, per the 2008 proxy). A PIPE is read as a listed purchase, flagged."},
 {"s": "xylan", "st": "acquired", "es": U, "hc": "US", "city": "Calabasas", "f": "Data Infrastructure",
  "n": "LAN switching, Calabasas CA. Listed 1996; acq. by Alcatel, 1999. Round not named."},
 {"s": "youcentric", "st": "acquired", "es": U, "hc": "US", "city": "Charlotte", "f": "SaaS",
  "n": "CRM software, Charlotte NC. acq. by J.D. Edwards, 2001. Round not named."},
]
