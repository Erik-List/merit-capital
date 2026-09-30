"""Rebuild delta (PRO-102): the duplicates of two excluded merge groups resurfaced as their own rows
(COLLECTION.md s8: a merge whose canonical is not_member never runs, so every slug of the group needs a verdict).
GartenHaus = YDEON Group and Lampenwelt = LUQOM Group, both control positions under R1 (judgments-pe.py)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import verdict, write  # noqa: E402

R = json.loads((Path(__file__).resolve().parent / "pe-research.json").read_text())["companies"]
L = [
    verdict("gartenhaus", "not_member",
            "The same company as ydeon-group (A-Z Gartenhaus, renamed YDEON Group): 3i agreed in September 2020 to buy "
            "the majority, and Project A's October 2020 investment 'was made as a co-investment with the private equity "
            "firm 3i Group' (Deutsche Startups dealmonitor). Control position (decisions.md D3, R1; COLLECTION.md s1 T3); "
            "the merge into ydeon-group cannot run because that row is excluded.",
            ec="web", conf="high", cite=R["GartenHaus / YDEON Group"]["sources"][0]["url"], exclusion="control_position"),
    verdict("lampenwelt", "not_member",
            "The same company as luqom-group (Lampenwelt, now LUQOM Group): 3i bought the majority in March 2017 and "
            "Project A agreed with 3i to invest in October 2017, 'the third private equity co-investment' (Private "
            "Equity News); 3i still holds the majority. Control position (decisions.md D3, R1; COLLECTION.md s1 T3); the "
            "merge into luqom-group cannot run because that row is excluded.",
            ec="web", conf="high", cite=R["Lampenwelt / LUQOM Group"]["sources"][0]["url"], exclusion="control_position"),
]
if __name__ == "__main__":
    write("delta-verdicts", L)
