# Batch o02 (PRO-169): the 1996-2012 book, C to E (the companies the judge can place now; the rest wait
# for the 2000-2012 archive lists). Judge: this session, 2026-09-29.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post
U = "undetermined"
J = [
 {"s": "charitableway", "st": "defunct", "es": U, "hc": "US", "city": "Palo Alto", "f": "Fintech & Payments",
  "n": "Online charitable giving, Palo Alto (the firm's 2000 list). Defunct, aligned with Benchmark. Round not named."},
 {"s": "claremont-technology", "st": "acquired", "es": U, "hc": "US", "city": "Portland", "f": None,
  "n": "IT consulting (Claremont Technology Group), Portland OR (the firm's 2000 list). acq. by Complete Business Solutions, 1998. IT services are outside the focus taxonomy. Round not named."},
 {"s": "cnet", "st": "acquired", "es": U, "hc": "US", "city": "San Francisco", "f": "Media, Gaming & Advertising",
  "n": "Technology media (C|NET, later CNET Networks), San Francisco. acq. by CBS, 2008. Round not named."},
 {"s": "continuous-computing", "st": "acquired", "es": U, "city": "San Diego", "f": "Data Infrastructure",
  "n": "Telecom platforms, San Diego. acq. by RadiSys, 2011 (the RadiSys stock in TCV's 13F 2011-2012 is the consideration). Round not named."},
 {"s": "copper-mountain-networks", "st": "acquired", "es": U, "hc": "US", "city": "San Diego", "f": "Data Infrastructure",
  "n": "DSL equipment, San Diego. Listed 1999; its assets were sold to Tut Systems in 2005. Round not named."},
 {"s": "coreexpress", "st": "defunct", "es": U, "hc": "US", "city": "Linthicum", "f": "Data Infrastructure",
  "n": "Network services, Linthicum MD. Defunct, aligned with Benchmark. Round not named."},
 {"s": "cosine-communications", "st": "defunct", "es": U, "hc": "US", "city": "Redwood City", "f": "Data Infrastructure",
  "n": "Network service platforms, Redwood City. Listed 2000; ceased operations in 2004 and remained only as a shell. Round not named."},
 {"s": "digital-generation-systems", "es": U, "hc": "US", "city": "Irving", "f": "Media, Gaming & Advertising", "vr": "below_1b",
  "n": "Ad distribution (DG Systems, later DG FastChannel and Digital Generation), San Francisco then Irving TX. Its TV business was sold to Extreme Reach and Sizmek spun off in 2014: acquired. Round not named."},
 {"s": "ebags", "st": "acquired", "es": U, "hc": "US", "city": "Greenwood Village", "f": "Consumer & Marketplaces",
  "n": "Online luggage retailer, Greenwood Village CO. acq. by Samsonite, 2017. Round not named."},
 {"s": "egenera", "st": "private", "vr": "below_1b", "es": U, "city": "Boxborough", "f": "Data Infrastructure",
  "n": "Data-centre and cloud management software, Boxborough MA; operating and private. Round not named."},
 {"s": "eladian-partners", "m": "not_member", "me": "site_listing", "mconf": "medium",
  "mb": "fund-shaped list entry (T5, the fund-shaped rule; decisions.md D8): 'Eladian Partners LP' is a limited partnership named like an investment vehicle and nothing identifies it as an operating company (the firm's own lists carry the name only), so the line reads as a stake in an investment partnership; the verdict is amended if identification lands."},
 {"s": "elevate-credit", "es": U, "hc": "US", "city": "Fort Worth", "f": "Fintech & Payments", "vr": "below_1b",
  "n": "Online consumer lending, Fort Worth; spun out of TCV-backed Think Finance in 2014, listed 2017, taken private by Park Cities Asset Management in 2023: acquired. TCV's position came through Think Finance; the round is not named."},
 {"s": "emachines", "es": U, "city": "Irvine", "f": "Consumer & Marketplaces", "vr": "below_1b",
  "n": "Consumer PCs, Irvine CA. acq. by Gateway, 2004. Round not named."},
 {"s": "everyday-health", "es": "Growth", "esc": post("everyday-health-inc-closes-growth-financing"), "ess": "first_party", "econf": "medium",
  "city": "New York", "f": "Media, Gaming & Advertising", "vr": "below_1b",
  "n": "Consumer health media, New York. acq. by Ziff Davis (j2 Global), 2016. TCV led a growth financing (the firm's own post) in a company that had already raised earlier rounds: Growth."},
 {"s": "evite", "st": "acquired", "es": U, "hc": "US", "city": "Los Angeles", "f": "Consumer & Marketplaces",
  "n": "Online invitations, Los Angeles. acq., aligned with Greylock. Round not named."},
]
