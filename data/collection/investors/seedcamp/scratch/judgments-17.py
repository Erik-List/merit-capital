"""PRO-83 delta: S2A for the two Seed recall additions (surfaces run 2026-09-30)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("j16", Path(__file__).with_name("judgments-16.py"))
j = importlib.util.module_from_spec(spec); spec.loader.exec_module(j)
jl, c = j.jl, j.c
U = ("https://www.braunschweiger-zeitung.de/wirtschaft/Presseportal/article409071953/"
     "next-level-it-accompio-uebernimmt-kern-ai-und-verankert-kuenstliche-intelligenz-im-kern-der-unternehmensgruppe.html")
L = [
    j.end("kern-ai", U, "acq. by Accompio, May 2025 (press release)"),
    c("kern-ai", status="acquired",
      note="Data-centric NLP developer platform ('the Germany-based company', founded Nov 2020 by Johannes Hoetter and Henrik Wenck); the firm's "
           "post of 2023-02-16: co-led the EUR 2.7 million seed; acq. by Accompio, May 2025 ('Accompio uebernimmt Kern AI', press release); "
           "absent from the firm's live list in 2026"),
    j.no("salesroom", j.NOTHING, "formd: the local Form D issuer data 2008Q1-2026Q2 for Salesroom -> no filing"),
]
if __name__ == "__main__":
    jl.write("delta-02", L)
