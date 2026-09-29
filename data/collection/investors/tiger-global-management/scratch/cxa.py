"""Cross-investor alignment of Tiger's own rows (COLLECTION.md rule 10), PRO-167, 2026-09-29.

Where a sibling book cites a fresher event than this book's row, this book's row is
the stale side and is aligned here. Run: NQ_TAG=cx python3 cxa.py (from scratch/).
Only the keys given are written; status acquired carries no figure (COLLECTION.md 6).
"""
import judge_lib as jl
from judge_lib import cls

L = [
    cls("alkira", status="acquired", rng="below_1b",
        note="Cross-investor 2026-09-29: Lumen Technologies completed its acquisition of Alkira on "
             "2026-07-07 (citybiz, https://www.citybiz.co/article/870607/lumen-completes-alkira-acquisition-"
             "to-expand-ai-ready-network-platform/; press reports put the price at $475M), as the GV row "
             "reads: acquired, below $1B, no standalone figure. The Sequoia row still reads private."),
    cls("heavy-ai", status="acquired", rng="below_1b",
        note="Cross-investor 2026-09-29: Nvidia acquired HEAVY.AI in 2025 (Wikipedia, "
             "https://en.wikipedia.org/wiki/HEAVY.AI: 'In 2025, the company was acquired by Nvidia'; "
             "GV's portfolio exit line reads 'Acquired by NVIDIA, 2025'), as the GV row reads: acquired, "
             "below $1B, no figure disclosed."),
]

if __name__ == "__main__":
    jl.write("cross-a", L)
