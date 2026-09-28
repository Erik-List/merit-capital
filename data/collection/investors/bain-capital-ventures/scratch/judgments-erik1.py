"""PRO-162, Erik's ruling of 2026-09-28: 'rm Mynd, Boon, Swift, daVinci, Onbe if not verified to be a venture investment'.
None of the five is verified as a venture investment: Mynd and Boon rest only on a venture or operating partner's board seat
(director-of-record pattern, no round naming BCV); the Syncapay lineage reached the business through a holding company whose
ownership split no source states. All five are out."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
RULE = "Erik 2026-09-28: removed because it is not verified to be a venture investment. "
L = [
    jl.verdict("mynd-management-inc", "not_member", RULE + "The only evidence is Clelia Peters (BCV Venture Partner 2020-2021) as a "
               "director on Mynd's 2021 Form D; no round, post or listing names BCV, and a venture partner's seat can be personal.",
               ec="formd_adjudicated", conf="high"),
    jl.verdict("boon-business-solutions-inc", "not_member", RULE + "The only evidence is Noah Breslow (BCV Operating Partner) as a "
               "director on Boon's 2025 Form D; no round, post or listing names BCV, and an operating partner's seat can be personal.",
               ec="formd_adjudicated", conf="high"),
]
SYNC = "https://www.prnewswire.com/news-releases/payments-industry-veterans-launch-syncapay-to-maximize-the-success-of-disruptor-payments-companies-300641028.html"
for s, what in [("swift-prepaid-solutions", "Swift Prepaid Solutions"), ("davinci-payments", "daVinci Payments (Swift Prepaid renamed)"),
                ("onbe", "Onbe (daVinci Payments after its merger with North Lane)")]:
    L.append(jl.verdict(s, "not_member", RULE + what + ": BCV's money reached the business through Syncapay, a holding company "
        "formed with Silversmith, MissionOG and Nyca to buy it outright (PR Newswire, 2018-05-02); no source shows a venture round "
        "in the company or states the group's share of the holding company.", ec="site_listing", conf="high", cite=SYNC))
for x in L:
    x["who"] = "erik"
if __name__ == "__main__":
    jl.write("erik-1", L)
