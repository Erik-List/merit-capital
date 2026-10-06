"""PRO-80 Bessemer Venture Partners, boundary judge bd, list B: possible purchases of companies that were already
listed (COLLECTION.md s1 T3, decisions.md R3), plus one control position found while reading (Harman, R1) and three
entry-stage corrections on rows that stay. Verdict lines only for the rows that leave."""
import json

import judge_lib as jl
from judge_lib import cls, verdict

INV = jl.INV
P2005 = {r["slug"]: r for r in json.loads((INV / "sources/wayback/parsed/2005.json").read_text())}
HIST = json.loads((INV / "sources/site/history-narrative.json").read_text())
assert any("11 growth equity investments in firms such as Motilal Oswal and Shriram EPC" in p
           for p in map(str, HIST["paragraphs"]))
assert "second round in April 1988" in P2005["allscripts"]["about"]
assert "participated in the 1980 transaction that spun Harco" in P2005["harman-international-industries"]["about"]
FIRM_2005 = P2005["allscripts"]["capture_url"]            # the firm's own list with a sentence per exit, 2005-02-05
assert FIRM_2005 == P2005["harman-international-industries"]["capture_url"]
FIRM_HIST_2008 = HIST["capture_url"]                      # the firm's own history page, capture of 2008-11-20

# URLs read in this session (WebFetch and direct reads)
FU_CENTOCOR = "http://www.fundinguniverse.com/company-histories/centocor-inc-history/"
FU_COMFED = "http://www.fundinguniverse.com/company-histories/commercial-federal-corporation-history/"
EB_GANESH = "https://equitybulls.com/category.php?id=8008"
FX_AIT = "https://www.finextra.com/newsarticle/6357/ait-hammers-out-refinancing-agreement"
IIFL_RIDDHI = "https://www.indiainfoline.com/company/riddhi-siddhi-gluco-biols-ltd/summary"
CH_TULIP = "https://www.chittorgarh.com/ipo/tulip-it-services-ipo/3072/"

T3 = "Purchase of a company that was already listed, with no Bessemer round before the listing (COLLECTION.md s1 T3, decisions.md R3): "

lines = [
    verdict("centocor", "not_member",
            T3 + "Centocor offered 'its stock to the public in 1982' (International Directory of Company Histories, "
            "on FundingUniverse) and the firm's own list dates its investment 1989, seven years after the listing, "
            "with no description of an earlier round.",
            ec="web", conf="medium", cite=FU_CENTOCOR),

    verdict("commercial-federal", "not_member",
            T3 + "Commercial Federal became 'a publicly traded, investor-owned institution' in 1984, with a national "
            "public offering completed that year (International Directory of Company Histories, on FundingUniverse), "
            "and the firm's own list dates its investment 1992, the year the holding company offered about $40M of "
            "new equity; no earlier round is recorded.",
            ec="web", conf="medium", cite=FU_COMFED),

    verdict("ganesh-housing", "not_member",
            T3 + "Ganesh Housing Corporation was a listed company by February 2007, when it allotted 7,000,000 "
            "shares to qualified institutional buyers under a QIP and awaited listing approval for them (Equity "
            "Bulls, 2007-02-14); the firm's own list dates the BVP India investment 2008-06-04.",
            ec="web", conf="high", cite=EB_GANESH),

    verdict("portrait-software", "not_member",
            T3 + "the row is AIT Group plc, later Portrait Software. AIT's shares were suspended in June 2002 and on "
            "2002-08-01 it agreed a secured rescue loan of 6M pounds 'provided by a combination of Bessemer Venture "
            "Partners', local private investors and its founder, with 'an option to convert the full amount of the "
            "loan into ordinary shares of AIT following shareholder approval' (Finextra, read in its archived copy); "
            "the firm's own list dates its investment 2002. A rescue financing of a listed company is not a venture "
            "round.",
            ec="web", conf="high", cite=FX_AIT),

    verdict("riddhi-siddhi-gluco-biols", "not_member",
            T3 + "Riddhi Siddhi Gluco Biols 'came out with a public issue in Nov.93' (India Infoline company "
            "summary) and the firm's own list dates the BVP India investment 2006-12-29, thirteen years after the "
            "listing.",
            ec="web", conf="high", cite=IIFL_RIDDHI),

    verdict("tulip-telecom", "not_member",
            T3 + "Tulip IT Services, later Tulip Telecom, closed its IPO in December 2005 and was 'Listed on Thu, "
            "Jan 5, 2006' on the BSE and NSE (Chittorgarh IPO record); the firm's own list, in its one capture of "
            "the row, dates the BVP India investment 2007.",
            ec="web", conf="medium", cite=CH_TULIP),

    verdict("harman-international-industries", "not_member",
            "Control position (COLLECTION.md s1 control positions, decisions.md R1; the Medi Assist and GTS "
            "precedents): the firm's own archived description says 'BVP participated in the 1980 transaction that "
            "spun Harco ... out of its corporate parent Beatrice Foods'. That transaction was the purchase of the "
            "business from Beatrice: 'In 1980 Sidney Harman and a group of investors paid $55 million' for it "
            "(International Directory of Company Histories, on FundingUniverse). The firm was in the group that "
            "bought the company, so there is no venture round. The listing check itself is clean: the company was "
            "private from 1980 to its 1986 IPO.",
            ec="site_listing", conf="medium", cite=FIRM_2005),

    # ---- rows that stay, stage corrected on what was read
    cls("onmobile", stage="Growth", stage_src="model", stage_conf="medium", clear=("listed_purchase_check",),
        note="Listed-purchase check closed: OnMobile's IPO ran 24 to 29 January 2008 and the shares listed on "
             "2008-02-19 (Chittorgarh IPO record), eight weeks after the firm's own investment date of 2007-12-27, so "
             "the entry is a pre-IPO placement in a company founded in 2000, a member at Growth (decisions.md R3)."),

    cls("shriram-epc", stage="Growth", stage_src="first_party", stage_cite=FIRM_HIST_2008, stage_conf="medium",
        note="Listed-purchase check closed: Shriram EPC listed on 2008-02-20 (Chittorgarh IPO record), two years "
             "after the firm's own investment date of 2006-03-27, and the firm's 2008 history page counts it among "
             "its India practice's 'growth equity investments in firms such as Motilal Oswal and Shriram EPC', so "
             "Growth."),

    cls("allscripts", stage="Growth", stage_src="first_party", stage_cite=FIRM_2005, stage_conf="high",
        entry_date="1988-04",
        note="The firm's own 2005 list: 'BVP's Chris Gabrieli invested in Allscript's second round in April 1988. The "
             "company went public in July 1999', so a private entry eleven years before the listing; a second round "
             "reads Growth and the date replaces the list's bare 1987."),
]
jl.write("bdb", lines)
