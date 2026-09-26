"""PRO-79 post-rebuild delta (the one re-prepare): the six rows the firm's own
'Growth' label now stages (config.site_api.entry_stage_fields, medium: 25/26
on the book's cited rows, below the 30-row bar), and the three recall
additions. iqube and wunderloop keep no country: the company cannot be named."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
SITE = "https://atomico.com/partners/"
LABEL = ("the firm's own CMS files it under Stage 'Growth' (investment year {y}): the site label, "
         "eligible and scored 25/26 against the book's cited entry rounds (medium, under the 30-row bar)")

L = []
for slug, y in [("compass", 2016), ("deepl", 2023), ("klarna", 2012), ("stripe", 2015),
                ("viagogo", 2007), ("zocdoc", 2014)]:
    L.append(cls(slug, stage="Growth", stage_src="first_party", stage_conf="medium",
                 stage_cite=SITE + slug, clear=["cite_pending"],
                 note="Stage: " + LABEL.format(y=y)))

L.append(verdict("coderabbit", "member",
                 "Recall addition (press layer): 'Atomico and Smash Capital co-led the round' - CodeRabbit's $143M Series C of Aug 2026, with Atomico partner Luca Eisenstecken joining the board (the company's own release); after every site capture",
                 "web", "high", "https://www.coderabbit.ai/newsroom/coderabbit-series-c-agentic-change-management"))
L.append(cls("coderabbit", status="private", rng="1b_plus", usd=1500000000, val_src="web_verified", asof="2026-08-12",
             val_cite="https://www.coderabbit.ai/newsroom/coderabbit-series-c-agentic-change-management", val_conf="high",
             country="US", city="San Francisco", focus="DevTools & APIs",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.coderabbit.ai/newsroom/coderabbit-series-c-agentic-change-management",
             note="AI code review; 'We raised $143 million in a Series C funding round at a $1.5 billion valuation. Atomico and Smash Capital co-led the round' (the company's own release, Aug 2026; Business Wire) - Atomico's first round; Luca Eisenstecken to the board",
             rounds=[rnd("2026-08-12", "Series C", 143000000, "Atomico; Smash Capital", True, "https://www.coderabbit.ai/newsroom/coderabbit-series-c-agentic-change-management", "company")]))
L.append(verdict("the-exploration-company", "member",
                 "Recall addition: the firm's own post 'Our investment in The Exploration Company: building Europe's way to orbit and back' (2026-09-08) and the $450M Series C co-led by Bessemer, Atomico and the Scaleup Europe Fund (the company's own release); after every site capture",
                 "site_listing", "high", "https://atomico.com/insights/our-investment-in-the-exploration-company-building-europes-way-to-orbit-and-back"))
L.append(cls("the-exploration-company", status="private", rng="below_1b", city="Munich",
             focus="Industrial & Robotics",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.exploration.space/blog/the-exploration-company-series-c-450-million",
             note="Reusable space capsules (Nyx) and engines (Hélène Huby; Munich, with teams in France, Luxembourg, Spain and Italy); 'Landmark financing co-led by Bessemer Venture Partners, Atomico, and the Scaleup Europe Fund' - the $450M Series C of Sep 2026 (the company's own release; TechCrunch) - Atomico's first round; no valuation was disclosed, so the band reads below $1B for want of a citable figure (Rule A)",
             rounds=[rnd("2026-09-08", "Series C", 450000000, "Bessemer; Atomico; Scaleup Europe Fund", True, "https://www.exploration.space/blog/the-exploration-company-series-c-450-million", "company")]))
L.append(verdict("visualdna", "member",
                 "Recall addition (UK register layer): Imagini Holdings Ltd (05730835), VisualDNA's parent, lists Atomico Investment Holdings Ltd - the firm's BVI vehicle, decisions.md D1 - as a shareholder in its annual returns to March 2008 and 2009 (276,321 ordinary shares); Mattias Ljungman was a director 2007-05-30 to 2010-03-17. A fund vehicle on the register suffices alone",
                 "fund_filing", "high", "https://find-and-update.company-information.service.gov.uk/company/05730835/filing-history/MjAwMTcyMjY4NGFkaXF6a2N4/document?format=pdf&download=0"))
L.append(cls("visualdna", status="acquired", rng="below_1b", country="GB", city="London",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Personality-based audience data for advertisers (Imagini Holdings Ltd, CEO Alex Willcock); Atomico entered between the Mar 2007 annual return (no Atomico holder) and the Mar 2008 one (Atomico Investment Holdings Ltd, 276,321 ordinary shares) - an unnamed round -> undetermined; 'Israeli billionaire and Playtech founder Teddy Sagi acquires ad tech startup VisualDNA' (Business Insider, May 2015), later part of Nielsen; the holding company dissolved 2017 -> acquired",
             rounds=[rnd("2007", "unnamed (register: holder by 2008-03)", None, None, True, "https://find-and-update.company-information.service.gov.uk/company/05730835/filing-history/MjAwMTcyMjY4NGFkaXF6a2N4/document?format=pdf&download=0", "filing")]))

if __name__ == "__main__":
    jl.write("delta-001", L)
