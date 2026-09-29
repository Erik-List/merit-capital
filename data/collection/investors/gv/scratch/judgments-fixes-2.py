#!/usr/bin/env python3
"""Lead's fixes after rebuild 3 (PRO-75, 2026-09-29): canonical rows that absorbed a duplicate at the rebuild carry
the earliest GV entry of the merged company. Apteligent takes Crittercism's 2011 seed (GV was in it, then the
Series A); myLaurel takes Ready's Series C; Beamable's note gains Disruptor Beam's 2013-19 listings; nChroma Bio's
note records why its entry is read through Chroma."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import judge_lib as jl  # noqa: E402

cls_now = json.loads((jl.INV / "companies/classification.json").read_text())
L = []
cr = cls_now["crittercism"]
L.append(jl.cls("apteligent", stage="Seed", stage_src="web_verified", stage_cite=cr["entry_stage_citation"],
                stage_conf="high", entry_date="2011-07", grad="graduated", grad_src="web_verified",
                grad_cite="https://techcrunch.com/2012/06/01/crittercism-series-a/", grad_conf="high",
                flags=["stage_disputes_band"],
                note="Mobile app performance monitoring (San Francisco), Crittercism until its 2015 rename to "
                     "Apteligent; the base carried both names and they are one row since the rebuild. Google "
                     "Ventures was in the $1.2M seed announced 2011-07-13 with Kleiner Perkins, Opus, Shasta and AOL "
                     "Ventures (TechCrunch), re-upped in the $5.5M Series A of June 2012 (TechCrunch, 2012-06-01) and "
                     "led the $12M Series B of March 2013 (TechCrunch, 2013-03-12), so the entry is the seed, not the "
                     "B the Apteligent row had read; the named Series A graduates it. A $30M round with Accenture "
                     "followed in April 2014. Acquired by VMware in 2017 (the firm's own exit line; VMware "
                     "announced it on 2017-05-15).",
                rounds=cr.get("funding_rounds")))
rd = cls_now["ready"]
ml = cls_now["mylaurel"]
L.append(jl.cls("mylaurel", stage="Growth", stage_src="web_verified", stage_cite=rd["entry_stage_citation"],
                stage_conf="high", entry_date="2020-09-16",
                note="Acute and transitional care at home, founded in New Orleans in 2016 as Ready Responders "
                     "(readyresponders.com, the firm's 2020-23 listing, same partner) and operating as myLaurel since "
                     "2023; the base carried both names and they are one row since the rebuild. GV was among the "
                     "investors in Ready's $54M Series C (Home Health Care News, 2020-09-16), which says GV, Deerfield "
                     "and City Light put over $100M in across two rounds in under a year, so GV may have entered in "
                     "the preceding round, also Growth; the entry date is the Series C's. The $12M initial closing of "
                     "June 2025 was 'led by Deerfield Management and GV' (the company's release) and SteelSky Ventures "
                     "led a further round in November 2025 with GV a previous investor. Headquarters New York (the "
                     "company's release).",
                rounds=(rd.get("funding_rounds") or [])[:1] + (ml.get("funding_rounds") or [])
                       + (rd.get("funding_rounds") or [])[1:]))
bm = cls_now["beamable"]
L.append(jl.cls("beamable",
                note=bm["note"].replace("which the firm's archive lists from 2020, so undetermined.",
                                        "so undetermined; the firm listed the company as Disruptor Beam from 2013 "
                                        "(under Rich Miner) and as Beamable from 2020, one row since the rebuild.")))
nc = cls_now["nchroma-bio"]
L.append(jl.cls("nchroma-bio",
                note=nc["note"].replace("The base also carries chroma-medicine (batch 15) and nvelop-therapeutics "
                                        "(batch 17), the two predecessors of this company.",
                                        "The two predecessors are one row with this company since the rebuild. The "
                                        "firm's live list files nChroma Bio under Issi Rozen, Chroma's GV partner, "
                                        "which is why the entry is read through Chroma; GV's other predecessor "
                                        "position, Nvelop's $100M seed of about 2022 (GEN, 2024-04), is recorded "
                                        "here, not as a second entry.")))
for x in L:
    assert x.get("note") and "—" not in x["note"], x["slug"]
jl.write("fixes-2", L)
