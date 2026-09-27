"""PRO-162 follow-ups from batches 6, 7 and 11.
(1) Heritage by Bain Capital Private Equity's own portfolio list (read 2026-09-27): it carries Stream, EPOCH Holdings,
eCredit.com (SR Research) and DexterUs, beside the generalist names (Staples, Bright Horizons, DoubleClick, Ameritrade), while the
venture fund's positions of the same years (Taleo, Vonage, Tengion, aPriori) are absent from it. Rows the firm listed only in its
2006-2013 archive and that sit on the private-equity list are the generalist funds' (decisions.md D2, R1).
(2) The Syncapay lineage (Swift Prepaid -> daVinci Payments -> Onbe): a holding company the investor group formed to buy the
business outright, so the canonical row and Onbe follow the Swift ruling (control position, medium, open for Erik)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
PE = "https://www.baincapitalprivateequity.com/portfolio/current-and-former-portfolio-companies"
TAG = "[bain_capital_heritage] "
L = []


def heritage(slug, why, conf="medium"):
    L.append(jl.verdict(slug, "not_member",
        TAG + "Another desk (decisions.md D1, D2, R1): " + why + " Bain Capital Private Equity's own portfolio list carries it beside "
        "the generalist-fund names (Staples, Bright Horizons, DoubleClick, Ameritrade), while the venture fund's positions of the same "
        "years (Taleo, Vonage, Tengion, aPriori) are absent from that list; no record names a Bain Capital venture vehicle as a holder.",
        ec="site_listing", conf=conf, cite=PE))


heritage("stream", "Stream International (technical-support outsourcing, Richardson, TX), 'acquired by Solectron (NYSE: SLR) in October "
         "2001' (the firm's 2012 page), listed by the firm only in 2006-2013 under 'Expansion/Growth Buyout'; the private-equity list "
         "carries 'Stream'. This replaces its earlier classification as a member.")
heritage("epoch", "EPOCH Senior Living (the firm's 2006 page, Brewster, MA, 'Expansion/Growth Buyout'); the private-equity list carries "
         "'EPOCH Holdings', and Bain Capital managing directors sat on its board.")
heritage("ecredit-com", "eCredit.com (Dedham, MA; the firm's 2003-2010 pages), with Bain Capital managing director Mark Nunnelly on its "
         "board (CTC Communications' 2001 proxy); the private-equity list carries 'eCredit.com (SR Research)'.")
heritage("dexterus", "DexterUs (the firm's 2006 page, 'Early', Acquired), with Bain Capital managing director Stephen Pagliuca on its "
         "board around 2000-2001 (Gartner's and IOS Brands' 2001 proxies); the private-equity list carries 'DexterUs'.")
SYNC = "https://www.prnewswire.com/news-releases/payments-industry-veterans-launch-syncapay-to-maximize-the-success-of-disruptor-payments-companies-300641028.html"
for s, what in [("davinci-payments", "daVinci Payments, the renamed Swift Prepaid Solutions (the firm's 2020-2021 page /portfolio/swift-prepaid-solutions)"),
                ("onbe", "Onbe, the 2021 name of daVinci Payments after its merger with North Lane on Centerbridge's majority investment")]:
    L.append(jl.verdict(s, "not_member",
        what + ": 'Syncapay, a new holding company focused on high-potential payments solutions has launched with the backing of Bain "
        "Capital Ventures, Silversmith Capital Partners, MissionOG, Nyca Partners' and 'Syncapay's first acquisition, Swift Prepaid "
        "Services, was made late last year' (PR Newswire, 2018-05-02). BCV's money reached the business through a holding company its "
        "investor group formed to buy it outright, the same ruling as swift-prepaid-solutions (COLLECTION.md s1 T3 control positions; "
        "decisions.md D4). OPEN for Erik: the release does not state the group's share of Syncapay.",
        ec="site_listing", conf="medium", cite=SYNC) | {"exclusion": "control_position"})
if __name__ == "__main__":
    jl.write("fix-2", L)
