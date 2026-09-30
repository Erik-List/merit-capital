"""Cross-book judge cx1 (PRO-100, rule 10): NEA row changes from cross-list-cx1.txt.
Every other pair is a namesake or a stale sibling row; see cross-plan-cx1.json."""
import judge_lib as jl

JIGSAW = "https://jigsawinteractive.com/jigsaw-interactive-acquires-influtive/"
NAVER_CLOSE = jl.NEWS("wallapop", "South Korea's Naver completes acquisition")
SEMTECH_8K = "https://www.sec.gov/Archives/edgar/data/88941/000115752315000104/a51019686ex99_1.htm"

L = [
    jl.cls("influitive", status="acquired",
           note=f"Jigsaw Interactive announced on 2023-12-21 that it had acquired Influitive ({JIGSAW}), so the row "
                "reads acquired as in the First Round book; the Lightspeed row, which still reads private, should align."),
    jl.cls("wallapop",
           note=f"Naver received all regulatory approvals and completed the acquisition on 2026-01-30 (Catalan News, "
                f"{NAVER_CLOSE}), so the sale is closed, not only signed."),
    jl.cls("enverv",
           note=f"Semtech's 8-K of 2015-01-14 announces it completed the acquisition of EnVerv's assets, with the team "
                f"joining Semtech ({SEMTECH_8K}), which confirms the firm's exit line."),
]

jl.write("cx1", L)
