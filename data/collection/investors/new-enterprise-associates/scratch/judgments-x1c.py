"""X1 pass x1c (PRO-100 NEA): five member rows that rested only on NEA's post-listing Schedule 13G filings of
1997-2000. Each row was checked for an NEA holding from before the listing: the 13Gs themselves, the company's
earliest proxy and 10-K on EDGAR (director biographies, principal stockholders), EDGAR full text, Google News
(nq.py) and web search. Every SEC document cited below was read in this pass through secget.py."""
import json

import judge_lib as jl

_B = {r["slug"]: r for r in json.loads((jl.INV / "companies/base.json").read_text())}


def edgar(slug, i=0):
    return [u.strip() for u in _B[slug]["edgar_links"].split(";") if u.strip()][i]


NETRIX_PROXY = "https://www.sec.gov/Archives/edgar/data/889237/0000928385-97-001035.txt"
LUMISYS_PROXY = "https://www.sec.gov/Archives/edgar/data/1001289/0001001289-97-000003.txt"
SEQUANA_PROXY = "https://www.sec.gov/Archives/edgar/data/946736/0000936392-97-000569.txt"

L = []

L.append(jl.verdict("netrix-corp", "member",
    "Not X1: NEA held Netrix before its 1992 listing. The 1997 proxy lists New Enterprise Associates IV with 582,009 "
    "shares (5.9%) beside 200,000 held by NEA V, and says director Arthur J. Marks, a general partner of New Enterprise "
    "Associates since 1984, had been on the board since 1987, five years before the IPO (the 10-K cites the company's "
    "1992 S-1). NEA's 13G/A of 1999 was filed under Rule 13d-1(d), the route for holders from before registration.",
    ec="fund_filing", conf="high", cite=NETRIX_PROXY))
L.append(jl.cls("netrix-corp",
    note="X1 pass x1c: NEA's Arthur Marks sat on the Netrix board from 1987 and NEA IV held 582,009 shares in 1997 "
         "(1997 proxy), so the position predates the 1992 listing; no round is named, so the stage stays undetermined."))

L.append(jl.verdict("lumisys-inc-de", "member",
    "Not X1: NEA held Lumisys before its listing (IPO effective November 14, 1995, per the 1996 10-K). The 1997 proxy "
    "says C. Richard Kramlich, managing general partner of New Enterprise Associates, had been a Lumisys director since "
    "October 1987, and that his holding includes 199,736 shares owned by New Enterprise Associates IV. NEA's 13G/A of "
    "February 1997 was not filed under Rule 13d-1(b), the exempt route for holders from before registration.",
    ec="fund_filing", conf="high", cite=LUMISYS_PROXY))
L.append(jl.cls("lumisys-inc-de",
    note="X1 pass x1c: NEA's Richard Kramlich sat on the Lumisys board from October 1987 and NEA IV held 199,736 shares "
         "in 1997 (1997 proxy), eight years before the November 1995 IPO; no round is named, so the stage stays "
         "undetermined."))

L.append(jl.verdict("sequana-therapeutics-inc", "member",
    "Not X1: NEA held Sequana before its July 1995 IPO (10-K for 1996). The 1997 proxy lists New Enterprise Associates "
    "VI with 464,017 shares (4.6%) and says director Thomas C. McConnell, a general partner of New Enterprise "
    "Associates since 1989, had served on the board since December 1993, a year and a half before the listing.",
    ec="fund_filing", conf="high", cite=SEQUANA_PROXY))
L.append(jl.cls("sequana-therapeutics-inc",
    note="X1 pass x1c: NEA's Thomas McConnell joined the Sequana board in December 1993 and NEA VI held 464,017 shares "
         "in 1997 (1997 proxy), so the position predates the July 1995 IPO; no round is named, so the stage stays "
         "undetermined."))

L.append(jl.verdict("genemedicine-inc", "not_member",
    "X1: no source shows NEA in GeneMedicine before its July 12, 1994 IPO (10-K405 for 1996). NEA V's only electronic "
    "filing is this 13G/A (Amendment No. 1, February 1997) reporting it had fallen below 5%, and it describes no "
    "purchase. The 1997 proxy names no NEA director or holder (the board carries Abingworth, Cahill Warnock and "
    "industry directors), the IPO prospectus predates EDGAR, and EDGAR full text, Google News and web search found no "
    "NEA mention beyond a vendor profile (PitchBook, unreadable). The 13G's filing route (not Rule 13d-1(b), no 13D) "
    "points to a stake held from before the listing; if Erik reads that route as evidence, the row is a member with "
    "the stage undetermined. If Erik rules such a purchase a venture entry, the row enters at Growth.",
    ec="fund_filing", conf="medium", cite=edgar("genemedicine-inc")))

L.append(jl.verdict("penederm-inc", "not_member",
    "X1: no source shows NEA IV in Penederm before its November 3, 1993 IPO (1997 proxy). NEA's only electronic filing "
    "is this group 13G/A (Amendment No. 3, February 1997) by NEA IV with ONSET Enterprise Associates, an affiliate fund "
    "run from ONSET's Palo Alto office, reporting the group below 5% and describing no purchase. The 1997 proxy and the "
    "1996 10-K/A name no NEA director or holder (Terry Opdendyk, the 1996 chairman, is ONSET's), the IPO prospectus "
    "predates EDGAR, and EDGAR full text, Google News and web search found nothing beyond a vendor profile (PitchBook, "
    "unreadable). The group's original 13G, filed by early 1994 at the latest and not under Rule 13d-1(b), points to a "
    "stake held from before the listing, but it does not split NEA IV from ONSET. If Erik rules such a purchase a "
    "venture entry, the row enters at Growth.",
    ec="fund_filing", conf="medium", cite=edgar("penederm-inc")))

jl.write("x1c", L)
