"""PRO-106 grind, batch-007 and the Form D rows batch-006's rendering skipped."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
verdict = jl.verdict
NEWS = "https://www.balderton.com/news/"
W = NEWS + "press-release-balderton-capital-europes-most-active-series-a-investor-welcomes-two-new-general-partners/"
L = []
for s, n in [("zoomdata-inc", "Zoomdata"), ("context-relevant-inc", "Context Relevant")]:
    L.append(verdict(s, "not_member", f"{n}: Rana Yared's Goldman Sachs board seat, on filings of 2014-16 before she joined Balderton in February 2020 (the firm's welcome post: a partner on the Goldman Sachs growth equity team); no Balderton surface carries the company (T4; partner-carried, Erik 2026-09-17)", ec="web", conf="high", cite=W))
L.append(verdict("civic-science-inc", "not_member", "Civic Science (Pittsburgh): the 'Mark Evans' on the 2011 filing is a homonym; Balderton's Mark Evans sat on European boards and no Balderton surface carries the company", ec="formd_adjudicated", conf="high"))
L.append(verdict("clear-pace-software-inc", "not_member", "Clear Pace Software (renamed RainStor): Peter Malcolm appears only on the 2001-02 Benchmark Europe desk pages; the 2010 filing is his own later role; no Balderton surface carries the company (T4)", ec="formd_adjudicated", conf="high"))
jl.write("batch-007", L)
