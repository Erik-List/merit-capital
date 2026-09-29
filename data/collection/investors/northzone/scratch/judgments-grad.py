"""PRO-105 graduation pass on base v1's Seed rows (COLLECTION.md s6, PRO-132), from
scratch/graduation-surfaces.json (run 2026-09-29, 0 failed lookups), the firm's posts, and three web
searches (Goals, 3Box, Yonder). A no carries the full absence test: asof, the surfaces searched, the
entry past the window. Also: Fishbrain's stage moves to undetermined (the record conflicts)."""
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, rnd, post, news, gsurl = jl.cls, jl.rnd, jl.post, jl.news, jl.gsurl
G = json.load(open(Path(__file__).with_name("graduation-surfaces.json")))
ASOF = "2026-09-29"
def surf(slug, firm_line, formd_line=None):
    lines = [firm_line]
    if formd_line: lines.append(formd_line)
    for name, sf in G[slug]["surfaces"].items():
        its = [i for i in sf.get("items", []) if i.get("names")]
        shown = "; ".join(f"{i['date']} {i['title'][:70]}" for i in its[:2]) or "no headline naming a later round"
        lines.append(f"{name}: {sf.get('query')} -> {sf.get('n')} items, {len(its)} naming the company; {shown}")
    return lines
def yes(slug, cite, src="web_verified", note=None):
    return cls(slug, grad="graduated", grad_src=src, grad_cite=cite, grad_conf="high", note=note)
def no(slug, lines, note):
    return cls(slug, grad="not_graduated", grad_src="absence_check", grad_asof=ASOF, surfaces=lines, grad_conf="medium", note=note)
L = []
L.append(yes("aidence", gsurl("aidence", "Aidence Raises €10M in Series A"),
    note="Graduated: EUR 10M Series A, Feb 2019 (FinSMEs), after the EUR 2.25M seed of 2017"))
L.append(yes("cusp-ai", post("material-revolution-a-portrait-of-cuspais-chad-edwards"), src="first_party",
    note="Graduated: the $100M Series A of Sept 2025 ('Last year, they closed their $100M Series A', the firm's portrait post; Bloomberg 2025-09-11)"))
L.append(yes("flink", gsurl("flink", "Flink Inks $240M"),
    note="Graduated: the $240M round of June 2021, over twice the ~$52M seed (Crunchbase News briefing 2021-06-04)"))
L.append(yes("goals", "https://gamesbeat.com/goals-scores-20m-series-a-to-develop-esports-ready-soccer-game/",
    note="Graduated: $20M Series A of April 2023 led by Seven Seven Six with Northzone, Moonfire and Cassius (GamesBeat; FinSMEs)"))
L.append(yes("hopin", news("Hopin", "Hopin Raises $40M As Demand"),
    note="Graduated: $40M round of June 2020, the Series A after the $6.5M seed (Crunchbase News 2020-06-25)"))
L.append(yes("ravio", news("Ravio", "Series A to modernise"),
    note="Graduated: $12M Series A of May 2025 (Business Wire)"))
L.append(yes("rayon", news("Rayon", "Series A"),
    note="Graduated: EUR 10M Series A of Sept 2026 (tech.eu, 2026-09-29)"))
L.append(yes("recall-labs", "https://www.coindesk.com/business/2022/02/16/usv-multicoin-lead-30m-raise-for-3boxs-ceramic-data-network",
    note="Graduated: 3Box Labs' $30M Series A co-led by Multicoin and USV, Feb 2022 (CoinDesk; Ceramic's blog)"))
L.append(yes("spektr", news("Spektr", "Business Wire"),
    note="Graduated: $20M Series A of April 2026 led by NEA (Business Wire; Crunchbase News)"))
L.append(yes("stockeld-dreamery", news("Stockeld Dreamery", "Series A"), note="Graduated: $20M Series A of Sept 2021 (AgFunderNews); the company shut in Oct 2025 (AgFunderNews, vegconomist) and Bettani Farms bought the brand in Dec 2025 (Green Queen)"))
L.append(yes("tandem-health", news("Tandem Health", "raises $50M Series A to scale"),
    note="Graduated: $50M Series A of July 2025 (tech.eu; FinSMEs)"))
L.append(yes("yonder", "https://www.uktech.news/fintech/yonder-series-a-20230417",
    note="Graduated: GBP 62.5m Series A of April 2023 (GBP 12.5m equity, GBP 50m debt) co-led by Northzone and RTP Global (UKTN; TechCrunch)"))
L.append(cls("fishbrain", stage="undetermined", clear=[], grad=None,
    note="Social network and app for anglers (Stockholm); the July 2014 round Northzone and Active Venture Partners led ($2.4M) is tagged Series A by TechCrunch (2014-07-08) while the firm's post calls the 2015 $8M round its 'A-round' (2015-07-22), after a 2013 seed (TechCrunch 2013-09-05): the record gives two readings of the entry round, so the stage is undetermined; Series B $13.5M 2018",
    extra={"entry_stage_source": None, "entry_stage_confidence": None}))
L.append(no("era", surf("era", "firm: the firm's posts and page for Era -> the $3.1M seed of Nov 2023 only",
    "formd: EDGAR entity search 'Era' / 'Era Technologies' -> no filer matching Era the wealth platform"),
    "Not graduated: after the $3.1M seed (Nov 2023) the only later round is the unnamed $6M of Feb 2025 (Business Wire; Coverager), below the step-up of max(2 x $3.1M, $5M) = $6.2M; no Series A named on any surface; entry 30 months before the check"))
L.append(no("fiberplane", surf("fiberplane", "firm: the firm's page and posts for Fiberplane -> no later round"),
    "Not graduated: no round after the EUR 7.5M seed of Sept 2021 on any surface searched; entry 60 months before the check"))
L.append(no("mimo", surf("mimo", "firm: the firm's posts for Mimo -> the EUR 18M seed of April 2024 (post 2024-04-11)"),
    "Not graduated: after the EUR 18M seed (April 2024) the only later round is the unnamed GBP 6m of March 2025 led by Project A (UKTN), far below twice the seed; no Series A named; entry 29 months before the check"))
L.append(no("solvimon", surf("solvimon", "firm: the firm's posts for Solvimon -> the EUR 9M seed of Nov 2023 only"),
    "Not graduated: no round after the EUR 9M seed (Nov 2023) on any surface searched; entry 34 months before the check"))
L.append(no("troop", surf("troop", "firm: the firm's posts for Troop -> the $4.3M seed of Nov 2022 only",
    "formd: EDGAR entity search 'Troop' / 'Troop Technologies' -> no filer"),
    "Not graduated: no round after the $4.3M seed (Nov 2022) on any surface searched; entry 46 months before the check"))
jl.write("batch-grad1", L)
