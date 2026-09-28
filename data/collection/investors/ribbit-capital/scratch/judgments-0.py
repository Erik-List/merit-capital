"""PRO-161 grind, exemplar rows (the pattern every batch file follows): Robinhood and Brex.
Evidence: the judge view (show.py), Wikipedia (wikifetch.py), the Google News sweep and nq.py."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, SITE, ARCH, W, NEWS, SPV = jl.cls, jl.verdict, jl.rnd, jl.SITE, jl.ARCH, jl.W, jl.NEWS, jl.SPV
L = []

L.append(cls("robinhood", city="Menlo Park", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Robinhood Markets"), entry_date="2014-09",
    note="Commission-free brokerage (Menlo Park since 2018, Wikipedia). Ribbit came in as a new investor in the $13M Series A of "
         "September 2014 led by returning investor Index Ventures (Wikipedia), and followed through its deal vehicles in the Series C "
         "(2017), D (2018) and E (2019) and the February 2021 notes (RH, RH-D, RH-E, RH-N Form Ds). Public since July 2021; the "
         "market cap is pinned in the A/B pass.",
    rounds=[rnd("2014-09", "Series A", 13000000, "Index Ventures", True, W("Robinhood Markets"), "press"),
            rnd("2018-05", "Series D", None, None, True, SPV("RH-D"), "filing")]))
L.append(cls("brex", status="acquired", rng="below_1b", city="San Francisco", focus="Fintech & Payments",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=W("Brex"), entry_date="2017",
    note="Corporate cards and spend management (San Francisco). 'Micky Malka's Ribbit Capital led Brex's $7 million Series A shortly "
         "after its founding in 2017' (Wikipedia); Ribbit also joined the June 2018 Series B and, through its deal vehicles, the 2021 "
         "Series D and its extension (BX-D, BX-DX). Capital One completed its $5.15B cash-and-stock acquisition on 2026-04-08 ("
         + NEWS("brex", "Capital One Completes Brex Deal") + ").",
    rounds=[rnd("2017", "Series A", 7000000, "Ribbit Capital", True, W("Brex"), "press"),
            rnd("2018-06", "Series B", 50000000, None, True, W("Brex"), "press"),
            rnd("2021-04", "Series D", None, None, True, SPV("BX-D"), "filing")]))
jl.write("exemplar-0", L)
