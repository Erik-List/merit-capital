"""PRO-80 Bessemer, second pass s21, file c: two cities, and the rows whose entry round stays undetermined after
a real search, with what was searched and the rounds found."""
import json
from pathlib import Path

import judge_lib as jl

CL = json.loads((jl.INV / "companies/classification.json").read_text())
CL = CL.get("bessemer-venture-partners", CL)

TC_KH = "https://techcrunch.com/2018/12/17/k-health-raises-25m-for-its-ai-powered-primary-care-platform/"
TC_ENDECA08 = "https://techcrunch.com/2008/01/23/intel-and-sap-put-15-million-into-enterprise-search-company-endeca/"
TC_ENDECA11 = "https://techcrunch.com/2011/10/18/oracle-buys-enterprise-search-and-data-management-company-endeca/"
TC_LIFEBOT = "https://techcrunch.com/2017/07/28/life-bots-new-alexa-app-can-text-you-reminders-help-with-daily-activities/"
SEARCHED = "2026-10-06"

kh_rounds = list((CL.get("k-health") or {}).get("funding_rounds") or []) + [
    jl.rnd("2018-12-17", "Series B", amount_usd=25000000, lead="14W; Comcast Ventures; Mangrove Capital Partners",
           firm_in_round=None, source=TC_KH, source_type="press")]

lines = [
    jl.cls("smart-machines", city="San Jose",
           note="Second pass: city (San Jose, California) from memory; Brooks Automation bought the company in "
                "1999 per the firm. The firm's sentence 'BVP led an investment round' in 1997 names no round."),
    jl.cls("resonext", city="San Jose",
           note="Second pass: city (San Jose, California) from memory of the RF Micro Devices acquisition "
                "coverage. No round named."),
    jl.cls("endeca",
           rounds=[jl.rnd("2008-01-23", "Later round", amount_usd=15000000, lead="Intel; SAP", firm_in_round=None,
                          source=TC_ENDECA08, source_type="press")],
           note="Second pass: TechCrunch (2011-10-18) lists Bessemer and Venrock first among the investors in "
                "Endeca's $65M total but names no first round. A web search summary of a vendor page (not read, "
                "not citable) dates a $10M Series A from Bessemer and Venrock to December 2000, ten months after "
                "the firm's own date 2000-02-24, which suggests an earlier seed; with the two dates in conflict "
                "the stage stays undetermined."),
    jl.cls("k-health", rounds=kh_rounds,
           note="Second pass: TechCrunch (2018-12-17) reports the $25M Series B and adds 'Other previous investors "
                "include Primary Ventures and Bessemer Venture Partners', so Bessemer entered at the seed or the "
                "Series A before December 2018; which of the two is not stated, so the stage stays undetermined."),
    jl.cls("life-bot", rounds=[],
           note="Second pass: TechCrunch (2017-07-28) describes Life Bot as a Y Combinator Summer 2017 voice-app "
                "startup of Jess Williams and Oscar Merry, then bootstrapped and planning a seed round. Google News "
                "and TechCrunch searches on " + SEARCHED + " found no report tying Bessemer to a round or saying "
                "what became of it."),
    jl.cls("kiran-energy", rounds=[],
           note="Second pass: Google News (two queries) and TechCrunch searches on " + SEARCHED + " returned the "
                "2018 Hinduja acquisition and a 2017 Amplus approach but no report naming the 2010 round."),
    jl.cls("goal-com", rounds=[],
           note="Second pass: Wikipedia says Perform Group paid 18 million pounds for Goal.com, and TechCrunch "
                "(2011-02-23) says it was bought from 'a consortium of investors, which includes Bessemer Venture "
                "Partners'; neither names the 2008 round, and Google News searches on " + SEARCHED + " found none."),
    jl.cls("pinnacle-engines-fmr-cleeves-engines-inc", rounds=[],
           note="Second pass: Google News on " + SEARCHED + " shows coverage of Pinnacle Engines from 2011 to 2016 "
                "(The New York Times, CNET, Autocar Professional) and nothing later; no headline names the round of "
                "the firm's December 2007 date or the company's fate, so stage and status stay open."),
    jl.cls("speakeasy", rounds=[],
           note="Second pass: Google News (two queries) and TechCrunch searches on " + SEARCHED + " found no report "
                "of this conference-calling app's funding or fate."),
    jl.cls("datadistillr", rounds=[],
           note="Second pass: Google News (two queries), TechCrunch and Crunchbase News searches on " + SEARCHED
                + " found no funding report; one 2021 trade item ties the company to the Apache Drill project."),
    jl.cls("dcortex", rounds=[],
           note="Second pass: Google News (two queries) and TechCrunch searches on " + SEARCHED + " found no "
                "report of the round or the company's city."),
    jl.cls("spanco-power-distribution", rounds=[],
           note="Second pass: three Google News queries on " + SEARCHED + " found no report of the 2011 round or "
                "of what became of the company."),
]

jl.write("s21c", lines)
