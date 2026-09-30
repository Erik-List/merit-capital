"""f3a: canonical-row corrections other judges found (FIX-CANON-BRIEF.md Part A), verified and recorded.
Classification lines only, only the keys that change. Rows already correct on the canonical row get no line:
fusion-io (Series A 2008-03 with stage_disputes_band), willow (US, Mountain View), super (private, ID, Surabaya),
element3-health (private as Grouper; hellogrouper.com shows Element3 Health, Inc. d/b/a Grouper operating, 2025
copyright), erytech (defunct, and F1 has since ruled it not_member under X1).
Skipped because F2 settled them first: elements-behavioral-health (F2: not_member, control position) and
grubwithus (F2 recorded private at GOAT's $3.7B June 2021 mark, Culver City from the Form D; the same reading
this pass reached from the First Round Review account of the pivot).
Run: NQ_TAG=f3 python3 judgments-f3a.py"""
import judge_lib as jl
from judge_lib import cls

WING = jl.W("The Wing (workspace)")
LOT18 = jl.W("Lot18")
DAZN_PR = jl.NEWS("viewlift-inc", "GLOBAL SPORTS ENTERTAINMENT LEADER DAZN")
DAZN_DONE = jl.NEWS("snagfilms", "Nashville Predators Tap ViewLift")
MODE_PR = ("https://www.prnewswire.com/news-releases/mode-emerges-from-stealth-with-24-million-in-venture-funding-"
           "and-a-new-class-of-private-network-for-enterprise-300660534.html")

L = [
    cls("the-wing", flags=["stage_disputes_band"],
        note="The merged Refresh Club, Inc. Form D reads Growth, but NEA led the April 2017 Series A "
             f"({WING}), so the stored Series A stands against the band."),
    cls("lot18", flags=["stage_disputes_band"],
        note="The merged L18 Holdings Form D band reads Series A, but NEA's entry is the $10M Series B it led in "
             f"May 2011 after FirstMark's Series A ({LOT18}), so Growth stands against the band."),
    cls("snagfilms", status="acquired", rng="below_1b",
        note="Correction: the issuer, renamed ViewLift, was acq. by DAZN, 2026 (agreement announced 2026-04-30, "
             f"{DAZN_PR}; completed in August 2026 per Sports Video Group, {DAZN_DONE}), so the 2020 end of the "
             "SnagFilms service no longer decides the status."),
    cls("exent-technologies", status="unknown", rng="below_1b", flags=["model_disputes_source"],
        note="The prefilled acquired status comes from a weak SEC join to a listed issuer (public since 2018), "
             "which is not this private Israeli games-on-demand company; Google News (2026-09-30) and the news on "
             "disk show no sale after 2012 and exent.com carries no company page, so the state is unknown."),
    cls("mode", stage="Series A", stage_src="web_verified", stage_cite=MODE_PR, stage_conf="medium",
        entry_date="2017",
        note="No earlier NEA round was found: the company's only Form D is its 2018 filing (CIK 1744501, San "
             "Mateo, a CIK issued in 2018), no post of the firm names Mode, and the company's release says it closed "
             "an $8M Series A led by NEA the year before, so the entry is that Series A; the firm's 2015 year stays "
             "unexplained, hence medium."),
]

jl.write("f3a", L)
