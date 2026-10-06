"""PRO-80 Bessemer Venture Partners, boundary judge bd, list A: possible control positions (COLLECTION.md s1 T3
"Control positions", decisions.md R1, R7, D2). Verdict lines only for the rows that leave; rows that stay are
untouched and listed in the report."""
import json

import judge_lib as jl
from judge_lib import verdict, W, NEWS

INV = jl.INV
LED = json.loads((INV / "companies/membership-ledger.json").read_text())["bessemer-venture-partners"]["verdicts"]
TEAM = json.loads((INV / "sources/site/team-pages.json").read_text())
TEAM = TEAM if isinstance(TEAM, list) else (TEAM.get("rows") or TEAM.get("pages"))
FEINSTEIN = next(p["url"] for p in TEAM if p.get("slug") == "brian-feinstein")
assert "growth buyout investments in Litify, LiveAuctioneers (acq), Beyond, Current, and CRI" in \
    next(p["bio"] for p in TEAM if p.get("slug") == "brian-feinstein")

# URLs read in this session (WebFetch and direct reads), the helpers' own where one exists
WS_VCJ = LED["ws-holdco-pbc"]["citation"]          # the citation of the legal-entity row, headline re-read 2026-10-06
SYNCSORT_W = W("Syncsort")
METALOGIX_NVBC = "https://www.newventuresbc.com/where-are-they-now-metalogix-inc/"
CRI_AT = NEWS("cri", "CRI and PKFOD")

BIO = ("the firm's own partner page (bvp.com/team/brian-feinstein): 'Brian also led growth buyout investments in "
       "Litify, LiveAuctioneers (acq), Beyond, Current, and CRI', set apart from his 'early-stage investments' and "
       "'growth investments'")

lines = [
    verdict("syncsort", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1): in April 2008 'Insight Venture "
            "Partners, Bessemer Venture Partners, Georgian Partners, Goldman Sachs, and other investors bought a "
            "majority interest in Syncsort' (Wikipedia), the year its long-time chief executive and majority "
            "shareholder 'sold a large portion of his stake'; the firm's listed date is 2008-03-31. The firm with "
            "its co-investor group acquired control, so there is no venture round.",
            ec="web", conf="medium", cite=SYNCSORT_W),

    verdict("wiredscore", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1): Bessemer's first entry, in "
            "October 2017, was the acquisition of WiredScore by an investor group led by Bessemer Venture Partners "
            "and Fifth Wall (Venture Capital Journal, 2017-10-12, 'Bessemer and Fifth Wall-led investor group "
            "acquires WiredScore'; Forbes, 2017-10-10, 'Jared Kushner Sells Majority Stake In Real Estate Tech Firm "
            "WiredScore'); the Series A of October 2018, where the two are named as previous backers (FinTech "
            "Global), came after it. Same transaction and citation as the legal-entity row ws-holdco-pbc, already "
            "ruled out; only the two headlines could be read, the articles are behind registration walls.",
            ec="web", conf="medium", cite=WS_VCJ),

    verdict("metalogix", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1): Metalogix 'was acquired in 2008 "
            "by Insight Venture Partners, a private equity firm' (New Ventures BC), with an outside chief executive "
            "installed, and the firm's own date for its investment is 2008-09-30, the same transaction; at the 2014 "
            "sale to Permira 'the current owners, Insight Venture Partners and Bessemer Venture Partners', were "
            "bought out (Washington Technology, 'Metalogix bought by another private equity firm'). The firm with "
            "its co-investor acquired the company, so there is no venture round.",
            ec="web", conf="medium", cite=METALOGIX_NVBC),

    verdict("cri", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1, the exception R7 names): in the "
            "transaction of 2024-11-18 'Centerbridge and Bessemer are taking a combined 51% voting interest in the "
            "firm' (Accounting Today), and " + BIO + ". The firm with its co-investor acquired control of Carr, Riggs "
            "& Ingram's advisory business, so there is no venture round.",
            ec="web", conf="high", cite=CRI_AT),

    verdict("liveauctioneers", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1): a buyout by the firm's own "
            "account. " + BIO[0].upper() + BIO[1:] + "; its Forge launch post names LiveAuctioneers beside NetSmart "
            "and TeamViewer (both ruled out as buyouts) among its companies with 'a growth buyout investment "
            "structure'. The transaction is the $47.6M of November 2014, the first outside money in a company "
            "founded in 2002; EDGAR's company search returns no filer under the company's name, so no Form D "
            "records it as a financing. The releases read do not state the stake, so the ruling rests on the "
            "firm's own label.",
            ec="web", conf="medium", cite=FEINSTEIN),

    verdict("beyond", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1): a buyout by the firm's own "
            "account. " + BIO[0].upper() + BIO[1:] + "; of the five, Litify (a majority stake, February 2023) and "
            "CRI (a combined 51% voting interest, November 2024) are confirmed as control by their own "
            "announcements. The transaction is the $42.5M of September 2019, which TechCrunch and Crunchbase News "
            "called a Series A without stating the stake; EDGAR's company search returns no filer named Beyond "
            "Pricing, so no Form D records it as a financing. The ruling rests on the firm's own label.",
            ec="web", conf="medium", cite=FEINSTEIN),

    verdict("current", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1, the exception R7 names; D2 in "
            "the alternative): a buyout by the firm's own account. " + BIO[0].upper() + BIO[1:] + "; the firm calls "
            "BVP Forge its 'growth buyout platform', and this 2024 position sits on the Forge grid. Current "
            "(formerly Crete Professionals Alliance) was founded in 2023 and buys accounting firms with Thrive "
            "Capital's money (Accounting Today, 2025-06-20). The press read does not state the stake, so the "
            "ruling rests on the firm's own label.",
            ec="web", conf="medium", cite=FEINSTEIN),
]
jl.write("bda", lines)
