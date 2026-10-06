"""A/B pass, judge ab4 (PRO-80): the momentum slice's four unchecked rows and the duty 6 hits.

Run once: NQ_TAG=ab4 python3 judgments-ab4a.py
"""
import judge_lib as jl
from judge_lib import cls, verdict, NEWS

L = []

# ---- momentum slice: the four rows whose note carried no dated check (Google News through nq.py, 2026-10-06)
L.append(cls("lithic", note="Checked 2026-10-06 for a priced round at $1B or more: none found (Google News); "
             "the newest priced round is the $60M Series C of July 2021 at $800M (Bloomberg headline)."))
L.append(cls("zopper", note="Checked 2026-10-06 for a priced round at $1B or more: none found (Google News); "
             "the newest round is the $25M Series D of November 2024 (Moneycontrol headline), no valuation at $1B reported."))
L.append(cls("oper", note="Checked 2026-10-06 for a priced round at $1B or more: none found (Google News); "
             "the EUR 11M Series A of July 2022 is the newest round reported."))
L.append(cls("dlthub", note="Checked 2026-10-06 for a priced round at $1B or more: none found (Google News); "
             "the $8M seed of November 2025 is the newest round reported."))

# ---- duty 6: unicorn-list hits on member rows that were neither banded nor exited
# Intercom (list: $1.2B, 2018) is this company, renamed Fin, and it exited: the stored status still read private.
FIN_CLOSE = NEWS("intercom", "Completes Acquisition of Fin - Salesforce")
L.append(cls("intercom", status="acquired", rng="below_1b",
             extra={"valuation_source": "web_verified", "valuation_range_source": "web_verified",
                    "valuation_citation": FIN_CLOSE, "valuation_asof": "2026-09-10"},
             note="Duty 6 (unicorn list re-intersected 2026-10-06): the list's Intercom is this company and it has exited; "
                  "acq. by Salesforce, 2026: Salesforce's own release of 2026-09-10 says it 'has completed its acquisition "
                  "of Fin', formerly Intercom (agreed 2026-06-15 at $3.6B, CMSWire headline), so the status reads acquired "
                  "as the fin row and the ICONIQ, Kleiner Perkins and GV books do."))

# VTS (list: $1B, 2019) is the company the firm's live listing 'View The Space (Fmr Hightower)' names. The base row
# vts was ruled not_member on 2026-10-06 (sale consideration) with the remark that the same reading applies here.
L.append(verdict("view-the-space-fmr-hightower", "not_member",
                 "Sale consideration (decisions.md R6, Erik 2026-09-22), the reading already recorded on the base row "
                 "vts, which is the same company: the firm's live listing 'View The Space (Fmr Hightower)' is VTS, "
                 "which absorbed Hightower in the all-stock merger announced 2016-11-29 (The Real Deal, 'VTS, Hightower "
                 "merge in landmark CRE tech deal'), and the listing dates the position 2013, the year of the Hightower "
                 "seed; Hightower is the row (acquired). No VTS round read names Bessemer: the $90M Series D of May 2019 "
                 "at $1B (The Real Deal and WSJ headlines) and the Series E of 2022-09-06, over $125M at about $1.7B led "
                 "by CBRE (FinLedger, read: CBRE, BentallGreenOak, AmTrust, Brookfield, Insight). Ethan Kurzweil's "
                 "director seat on VTS's 2017 and 2019 Form Ds is a seat, not a round naming a Bessemer fund. Found by "
                 "duty 6 (the unicorn list's VTS against the listing's alias, 2026-10-06).",
                 ec="web", conf="medium",
                 cite=NEWS("view-the-space-fmr-hightower", "VTS, Hightower merge in landmark")))

if __name__ == "__main__":
    jl.write("ab4a", L)
