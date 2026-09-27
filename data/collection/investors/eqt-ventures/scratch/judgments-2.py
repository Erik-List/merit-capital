"""PRO-163 grind, batch-002 (let-s-do-this .. unomaly). Same evidence and conventions as judgments-1.py:
the firm's own posts (stories 2016-2026, the 2017-2020 articles by capture URL), the eqtgroup.com Key Facts,
Wikipedia raw text, sibling rows, and web checks of 2026-09-27 whose URLs are copied from the search results.
Rounds that no citable source names take `model` at low confidence where the size and sequence place them
(flagged stage_uncited) and `undetermined` where they do not. Seed graduations that need the absence test are
judged in their own pass."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, S, A, W, SITE = jl.cls, jl.verdict, jl.rnd, jl.S, jl.A, jl.W, jl.SITE
L = []

def site_c(slug, code, **kw):
    return dict(country=code, country_src="web_verified", country_cite=SITE(slug), **kw)

L.append(cls("let-s-do-this", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2019/11/13/lets-do-this-raises-15-million-series-a-led-by-eqt-ventures-to-grow-endurance-sport-events-platform/",
    entry_date="2019-11", **site_c("let-s-do-this", "GB"), city="London", focus="Consumer & Marketplaces",
    note="Marketplace for endurance events. EQT Ventures led the $15M Series A (Nov 2019, Tech.eu; Lyle Fong to the board); EUR 60M Series B 2022 (the firm's post)."))

L.append(cls("linearity", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.dlapiper.com/en-pt/news/2021/09/dla-piper-advises-eqt-ventures-in-tech-start-up-linearity",
    entry_date="2021-09", **site_c("linearity", "DE"), city="Berlin", focus="SaaS",
    note="Vector design software (Vectornator, renamed Linearity 2022). EQT Ventures led the $20M round with 468 Capital (Sep 2021; the firm's post; TechCrunch); "
         "EQT's counsel DLA Piper names it the Series A (a database calls it a Series B)."))

L.append(cls("min-doktor", status="private", rng="below_1b", stage="undetermined", **site_c("min-doktor", "SE"), city="Malmö",
    focus="Healthcare & Bio",
    note="Digital primary care. One of EQT Ventures' first five investments (2016-05-26 release; site: EQT Ventures I, 2016; Lars Jornow chairman 2017). The first round "
         "is named by no citable source: the Dec 2016 EUR 4.7M came 'primarily from existing investors including EQT Ventures' (Tech.eu, 2016-12-21), so EQT entered "
         "earlier that year in an unnamed round; the stage is undetermined. The firm lists it as current."))

L.append(cls("moralis", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("founders-story-moralis"), entry_date="2021-10",
    grad="graduated", grad_src="web_verified", grad_cite=S("founders-story-moralis"),
    **site_c("moralis", "SE"), city="Stockholm", focus="Crypto & Web3",
    note="Web3 developer APIs. 'Two things led EQT Ventures to lead the EUR 11.5 million seed round in Moralis in October 2021' and 'an additional $40 million in a Series A "
         "funding round, announced last week' (the firm's post, 2022-05-18): the named Series A graduates the row.",
    rounds=[rnd("2021-10", "Seed", 13400000, "EQT Ventures", True, S("founders-story-moralis"), "firm"),
            rnd("2022-05", "Series A", 40000000, None, None, S("founders-story-moralis"), "firm")]))

L.append(cls("natural-cycles", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite=W("Natural_Cycles"), entry_date="2017-11", **site_c("natural-cycles", "SE"), city="Stockholm", focus="Healthcare & Bio",
    note="Digital contraceptive (FDA-cleared). 'In November 2017 Natural Cycles received a $30M investment in series B round led by EQT Ventures fund' (Wikipedia; "
         "the firm's post 2017-11-09); no disclosed $1B mark."))

L.append(cls("netlify", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified", val_cite=W("Netlify"), asof="2021-11",
    city="San Francisco", focus="DevTools & APIs", flags=["stale"],
    note="Web development platform. EQT Ventures led the $53M Series C (Mar 2020, Wikipedia; the Form D band agrees: Growth); the $105M Series D led by Bessemer valued it "
         "at $2B (Nov 2021, Wikipedia), the last priced round, older than 24 months."))

L.append(cls("nothing", status="private", rng="1b_plus", usd=1300000000, val_src="web_verified", val_cite=S("2025-in-review"), asof="2025-09",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=S("2022-at-eqt-ventures"), entry_date="2022-03",
    **site_c("nothing", "GB"), city="London", focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="Consumer electronics (Carl Pei). 'We ... co-led Nothing's EUR 63.4m Series B' (the firm's post, 2022-12-20; site: EQT Ventures III, 2022). "
         "'Nothing's $200M Series C at a $1.3B valuation' (the firm's 2025 review, Sep 2025). London-based; the Wikidata FR is a wrong join."))

L.append(cls("oden-technologies", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite=A("oden-technologies-raises-seed"), entry_date="2015", country="US", country_src="web_verified", country_cite=SITE("oden-technologies"),
    city="New York", focus="Industrial & Robotics",
    note="Industrial IoT analytics for manufacturers. The fund entered in 2015 (site Entry 2015; one of the five investments of the 2016-05-26 release) and led the $3.5M "
         "round of May 2017, which 'brings Oden's total seed funding to $5.9M' ('we've partnered again with EQT Ventures', the firm's post 2017-05-08): every round to "
         "then was seed. Graduation judged in the surfaces pass."))

L.append(cls("onramper", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2022/01/onramper-raises-6m-in-seed-funding.html", entry_date="2022-01",
    **site_c("onramper", "NL"), city="Amsterdam", focus="Crypto & Web3",
    note="Fiat-to-crypto on-ramp aggregator. $6M seed led by EQT Ventures (Jan 2022, FinSMEs). The firm's Exit 2024 is its own sale of the stake; the company is independent. "
         "Graduation judged in the surfaces pass."))

L.append(cls("owwn", status="defunct", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.eu-startups.com/2021/06/berlin-based-wajve-secures-e5-million-seed-funding-to-accelerate-its-financial-advisory-app-for-gen-z/",
    entry_date="2021-06", **site_c("owwn", "DE"), city="Berlin", focus="Fintech & Payments",
    note="Gen-Z banking app, wajve until its 2022 rebrand as OWWN. EUR 5M seed led by EQT Ventures with 468 Capital (Jun 2021, EU-Startups). The banking product never left "
         "beta and the company gave up in Mar 2023 ('Berliner Banking-Fintech Owwn gibt auf', Finanz-Szene), pointing users to N26. Graduation judged in the surfaces pass."))

L.append(cls("packmatic", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2024/01/25/packmatics-dgital-one-stop-shop-for-packaging-supplies-raises-eur15m/", entry_date="2024-01",
    **site_c("packmatic", "DE"), city="Berlin", focus="Consumer & Marketplaces",
    note="B2B marketplace for packaging. EQT Ventures led the EUR 15M Series A (Jan 2024; Tech.eu; FYB)."))

L.append(cls("parloa", status="private", rng="1b_plus", usd=3000000000, val_src="web_verified",
    val_cite="https://techcrunch.com/2026/01/15/parloa-triples-its-valuation-in-8-months-to-3b-with-350m-raise/", asof="2026-01-15",
    stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.dlapiper.com/en-bh/news/2023/04/dla-piper-advises-eqt-ventures-on-series-a-financing-round-in-ai-company-parloa",
    entry_date="2023-03", **site_c("parloa", "DE"), city="Berlin", focus="AI & Applied AI",
    note="Conversational AI for contact centres. EQT Ventures led the EUR 20M Series A (Mar 2023; TechCrunch; EQT's counsel DLA Piper), the fund's first check (the firm's "
         "2023 review lists Parloa among that year's new investments; the page's Entry 2021 is not the deal year). $120M Series C at $1B (May 2025), $350M Series D led "
         "by General Catalyst at $3B (TechCrunch, 2026-01-15)."))

L.append(cls("payrails", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2023/06/07/payrails-scaling-its-payment-operating-system-for-global-platforms-with-144-million-seed-extension/",
    entry_date="2023-06", city="Berlin", focus="Fintech & Payments",
    note="Payments operating system. EQT Ventures led the $14.4M seed extension (Jun 2023, Tech.eu; after a16z's $6.4M seed). Graduation judged in the surfaces pass."))

L.append(cls("peakon", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("662-year-over-year"), entry_date="2017-03", **site_c("peakon", "DK"), city="Copenhagen", focus="SaaS",
    note="Employee engagement analytics. 'just 10 months after EQT Ventures led the EUR 6.1m Series A' (the firm's post, 2018-02-28; announced 2017-03-27). "
         "acq. by Workday, 2021 (the firm's post on Workday's intent to acquire)."))

L.append(cls("peanut", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2020/05/05/social-network-for-women-peanut-raises-12m-series-a-amid-pandemic/", entry_date="2020-05",
    **site_c("peanut", "GB"), city="London", focus="Consumer & Marketplaces",
    note="Social network for women. $12M Series A led by EQT Ventures (May 2020, TechCrunch; Naza Metghalchi to the board)."))

L.append(cls("pelago", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2018-05",
    grad="graduated", grad_src="web_verified", grad_cite="https://www.uktech.news/news/quit-genius-closes-$11m-series-a-funding-20200319",
    country="US", country_src="web_verified", country_cite="https://www.pelagohealth.com/company/news/remeet-pelago-well-funded-quit-genius-rebrands-to-make-addiction-treatment-more-accessible/",
    city="New York", focus="Healthcare & Bio", flags=["stage_uncited"],
    note="Virtual addiction care (Quit Genius until its 2023 rebrand; YC). The fund's entry (site: EQT Ventures I, 2018; the archive's announcement date 2018-05-23) falls in "
         "the seed of 2018, which no citable source ties to EQT, so Seed by position at low confidence; the named $11M Series A led by Octopus (Mar 2020, UKTN) graduates "
         "it; $64M Series B 2021, $58M Series C. New York-headquartered; the firm's Key Facts say United Kingdom, where it was founded."))

L.append(cls("peltarion", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2016-10",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://www.eu-startups.com/2019/02/stockholm-based-peltarion-secures-e18-million-series-a-funding-to-advance-humankind-through-ai/",
    **site_c("peltarion", "SE"), city="Stockholm", focus="AI & Applied AI", flags=["stage_uncited"],
    note="Deep-learning platform. EQT Ventures put in SEK 30M (about $3.5M) at the end of 2016 (Nordic9; site Entry 2016), a round no source names; the company's named "
         "EUR 18M Series A led by Euclidean Capital (Feb 2019, EU-Startups) came later, so Seed by position at low confidence and graduated. acq. by King, 2022 (Wikipedia)."))

L.append(cls("permutive", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2018-01",
    city="London", focus="Media, Gaming & Advertising", flags=["stage_uncited"],
    note="Audience data platform for publishers. The fund's entry is the $10M round of Jan 2018 led by EQT Ventures (the Form D of 2018 lists Alastair Mitchell as director; "
         "the archive's announcement date 2018-01-02), which the databases name the Series A; TechCrunch's 2020 Series B story cites only Crunchbase for it, so model at medium. "
         "$18.5M Series B led by Octopus (Jul 2020, EQT participating)."))

L.append(cls("playsome", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-03",
    **site_c("playsome", "FI"), city="Helsinki", focus="Media, Gaming & Advertising", flags=["stage_uncited"],
    note="Mobile game studio (founded 2019). EQT Ventures II entered in 2021 (the archive's announcement date 2021-03-02) with Play Ventures; the databases call the round a "
         "seed and no press names it, so model at low. Graduation judged in the surfaces pass."))

L.append(cls("popcore", status="acquired", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2019-04",
    **site_c("popcore", "DE"), city="Berlin", focus="Media, Gaming & Advertising", flags=["stage_uncited"],
    note="Hyper-casual mobile games (founded 2018). 'EQT Ventures backs the Popcore team ... through an early stage investment' with Makers Fund and David Helgason (the "
         "firm's post, 2019-04-09), the company's first institutional round, which no source names: Seed by position at low confidence. acq. by Rollic (Zynga), 2022 "
         "(the firm's post 2022-11-17). Graduation judged in the surfaces pass."))

L.append(cls("pruna-ai", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://nordic9.com/news/pruna-ai-in-a-65-million-seed-round-led-by-eqt-ventures-joined-by-daphni-motier-kima-ventures-and-angel-investors/",
    entry_date="2024-11", grad="censored", city="Munich", country="DE", country_src="web_verified", country_cite="https://www.munich-startup.de/en/106164/pruna-ai-seed-round/",
    focus="AI & Applied AI",
    note="Model compression and inference optimisation (Munich and Paris). $6.5M seed led by EQT Ventures with Daphni, Motier and Kima (Nov 2024); inside the window."))

L.append(cls("qevlar-ai", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2023/11/16/taking-ai-to-the-ai-fight-eqt-ventures-leads-seed-round-for-ai-cybersecurity-firm-qevlar-ai/",
    entry_date="2023-11", grad="graduated", grad_src="web_verified",
    grad_cite="https://www.businesswire.com/news/home/20250408264298/en/Qevlar-AI-Raises-$14M-to-Supercharge-Security-Operations-Centres-with-Agentic-AI",
    **site_c("qevlar-ai", "FR"), city="Paris", focus="Security",
    note="Autonomous SOC investigations. EQT Ventures led the EUR 4.5M seed (Nov 2023, Tech.eu) and the $14M round of Apr 2025 (Business Wire; the firm's post: 'double down "
         "... following the initial round in November 2023'); an unnamed later round of $14M clears 2x the seed and $5M, so the row graduates; $30M round Mar 2026."))

L.append(cls("reworks", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-eqt-ventures-investment-in-reworks"), entry_date="2020-04", city="Helsinki", focus="Media, Gaming & Advertising",
    note="Mobile games (Redecor). 'EQT Ventures led the seed round in the company' (the firm's post, 2020-04-23). acq. by Playtika, 2021 (Playtika's 8-K lists 'EQT Ventures "
         "Investments S.a r.l.' among the selling venture holders). Graduation judged in the surfaces pass."))

L.append(cls("risk-methods", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.eu-startups.com/2016/02/munich-based-riskmethods-secures-6-million-in-a-series-a-funding-round-led-by-eqt-ventures/",
    entry_date="2016-02", **site_c("risk-methods", "DE"), city="Munich", focus="SaaS",
    note="Supply-chain risk management. EQT Ventures led the $6M Series A (Feb 2016, EU-Startups), one of the fund's first five investments. acq. by Sphera, 2022 (the firm's post)."))

L.append(cls("sana-labs", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("on-sana-s-34m-series-b"), entry_date="2020", **site_c("sana-labs", "SE"), city="Stockholm", focus="AI & Applied AI",
    note="AI knowledge and learning platform. 'After leading the Series A in 2020, we also joined the round' (the firm's post on Sana's $34M Series B led by Menlo, "
         "2022-12-13). acq. by Workday, 2025 (the firm's Exit 2025)."))

L.append(cls("seeqc", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.businesswire.com/news/home/20200916005167/en/Seeqc-Secures-%2422.4-Million-In-Series-A-Round-Strategic-Investment-Led-By-EQT-Ventures",
    entry_date="2020-09", city="Elmsford", focus="Industrial & Robotics",
    note="Digital quantum computing chips. $22.4M Series A led by EQT Ventures (Sep 2020, Business Wire; Ted Persson to the board). The Jan-2026 merger agreement with Allegro "
         "Merger Corp. ('approximately $1 billion') was terminated by a Settlement, Termination and Release Agreement of 2026-08-25 (SEEQC's 10-Q of 2026-08-28); an S-1 for a "
         "conventional IPO was amended 2026-09-11 and no shares trade yet, so there is no priced event at $1B+. The prospectus names EQT Ventures II Investments S.a r.l. as holder."))

L.append(cls("service-partner-one", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2016/07/06/service-partner-one/", entry_date="2016-07", **site_c("service-partner-one", "DE"),
    city="Berlin", focus="Consumer & Marketplaces",
    note="Online office-management services. EQT Ventures led the $10M Series A (Jul 2016, TechCrunch; the firm's post). acq. by Kaercher, 2019 (the firm's Exit 2019)."))

L.append(cls("sifflet", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=W("Sifflet"), entry_date="2023-03", **site_c("sifflet", "FR"), city="Paris", focus="Data Infrastructure",
    note="Data observability. 'In March 2023, Sifflet received EUR 12 million in Series A funding led by EQT Ventures' (Wikipedia; the firm's post 2024-04-18)."))

L.append(cls("silexica", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2018/06/21/silexica-which-optimises-how-disparate-applications-work-together-on-autonomous-cars-raises-18m/",
    entry_date="2018-06", **site_c("silexica", "DE"), city="Cologne", focus="DevTools & APIs",
    note="Software tools for multicore embedded systems. EQT Ventures led the $18M Series B (Jun 2018, TechCrunch), after the $8M Series A of 2016. acq. by Xilinx, 2020."))

L.append(cls("small-giant-games", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=S("congratulations-to-small-giant-games"), entry_date="2017-03", city="Helsinki", focus="Media, Gaming & Advertising",
    note="Mobile games (Empires & Puzzles). EQT Ventures led the $5.7M Series A (Mar 2017) and the $41M round of Jan 2018 (the firm's post, 2018-12-20). "
         "acq. by Zynga, 2018 ($700M implied value), the fund's first exit."))

L.append(cls("sonantic", status="acquired", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://tech.eu/2020/03/03/sonantic-funding/", entry_date="2020-03", city="London", country="GB", country_src="web_verified",
    country_cite=SITE("sonantic"), focus="AI & Applied AI",
    note="Expressive AI voices for games. EUR 2.3M seed led by EQT Ventures (Mar 2020, Tech.eu). acq. by Spotify, 2022 (the firm's 2022 review). "
         "Graduation judged in the surfaces pass."))

L.append(cls("standard-ai", status="private", rng="1b_plus", usd=1000000000, val_src="web_verified", val_cite=S("standard-cognition-how"), asof="2021-02",
    city="San Francisco", focus="AI & Applied AI", flags=["stale"],
    note="Autonomous checkout, now retail vision analytics (Standard Cognition until 2021). EQT Ventures led the Series B ('after leading the Series B', the firm's post; "
         "the Form D band agrees). The $150M round of Feb 2021 from SoftBank Vision and TI Platform made it 'the first unicorn in autonomous checkout' (the firm's post, "
         "2021-02-19): $1B, at the band edge, the last priced round and older than 24 months; bought Pathr.ai in Jan 2026."))

L.append(cls("superlist", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite=S("superlist-10m-series-seed"), entry_date="2022-04", **site_c("superlist", "DE"), city="Berlin", focus="SaaS",
    note="Task and project management. 'EQT Ventures is leading a EUR 10m round of seed funding alongside Cherry Ventures' (the firm's post, 2022-04-11). "
         "Graduation judged in the surfaces pass."))

L.append(cls("supernormal", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.finsmes.com/2020/12/supernormal-raises-2m-in-seed-funding.html", entry_date="2020-12",
    **site_c("supernormal", "SE"), city="Stockholm", focus="AI & Applied AI",
    note="AI meeting notes. $2M seed led by EQT Ventures (Dec 2020, FinSMEs); a $10M round in Jan 2023 led by Balderton, itself named a seed. Graduation judged in the surfaces pass."))

L.append(cls("supernova", status="private", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2021-03",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://therecursive.com/supernova-raises-series-a-investment-portal-vibe-coding-for-entire-teams/",
    city="San Francisco", focus="SaaS", flags=["stage_uncited"],
    note="Design-system platform (Czech-founded, YC; headquartered in San Francisco). The fund entered in 2021 (site: EQT Ventures I; the archive's announcement date 2021-03-01), "
         "ahead of the Wing-led $4.8M seed of Nov 2022 in which it also joined; no source names the 2021 round, so Seed by position at low confidence; the company's named "
         "Series A (The Recursive) graduates it."))

L.append(cls("supplant", status="defunct", rng="below_1b", stage="Seed", stage_src="model", stage_conf="low", entry_date="2018-10",
    grad="graduated", grad_src="web_verified", grad_cite="https://news.crunchbase.com/briefing/briefing-2-26-21/",
    **site_c("supplant", "GB"), city="Cambridge", focus="Healthcare & Bio", flags=["stage_uncited"],
    note="Sugars made from plant fibre (Cambridge Glycoscience until its rebrand). EQT Ventures I entered in 2018 (the archive's announcement date 2018-10-01), a round no source "
         "names; the $15M Series A led by Manta Ray with EQT among existing investors (Crunchbase News, Feb 2021) graduates it. Entered administration and was put up for sale "
         "in Aug 2025 (City AM): no sale cited, so defunct (the bankruptcy-without-sale rule); the firm's Exit 2025."))

L.append(cls("syntetica", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
    stage_cite="https://www.vestbee.com/insights/articles/syntetica-raises-4-2-m", entry_date="2024-07",
    grad="graduated", grad_src="web_verified",
    grad_cite="https://www.eu-startups.com/2026/07/paris-based-syntetica-raises-e26-1-million-to-industrialise-process-that-cracks-a-major-nylon-recycling-barrier/",
    **site_c("syntetica", "FR"), city="Paris", focus="Climate & Energy",
    note="Nylon textile recycling. EQT Ventures led the EUR 4.2M seed (Jul 2024, Vestbee; the firm's post); EUR 26.1M raised Jul 2026 (EU-Startups; Sifted: $30M with Lululemon), "
         "an unnamed round well past 2x the seed and $5M, so graduated."))

L.append(cls("talentium", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="medium",
    stage_cite="https://siliconcanals.com/hiring-platform-talentium-bags-e3-5m/", entry_date="2024-12",
    **site_c("talentium", "SE"), city="Stockholm", focus="AI & Applied AI",
    note="AI recruitment search engine. EQT Ventures led the EUR 3.5M round of Dec 2024, a pre-seed in Silicon Canals and a seed in Nordic9; a second tranche took it to SEK 121M."))

L.append(cls("the-exploration-company", status="private", rng="1b_plus", usd=2000000000, val_src="web_verified",
    val_cite="https://thenextweb.com/news/exploration-company-300m-raise-spacex-rival", asof="2026-07-27", val_conf="low",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=S("exploration-behind-the-exploration-company"), entry_date="2023-02",
    city="Munich", focus="Industrial & Robotics",
    note="Reusable space capsule Nyx. 'EUR 40.5 Million Series A, co-led by EQT Ventures and Red River West' (the firm's post, 2023-02-07; site: EQT Ventures III, 2023). "
         "The $450M Series C of Sep 2026 was co-led by Bessemer, Atomico and the Scaleup Europe Fund (an EQT fund of another desk, decisions.md D3) with no price disclosed; "
         "the $2B figure is the July 2026 press report on that round (The Next Web), aligned to the Atomico and Balderton rows at low confidence; Cherry's row reads below $1B."))

L.append(cls("timeless", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="low", entry_date="2021-11",
    **site_c("timeless", "DE"), city="Berlin", focus="Fintech & Payments", flags=["stage_uncited"],
    note="Fractional investing in collectibles. EQT Ventures led the EUR 12M round of Nov 2021 with existing investors C3 EOS, La Roca and Porsche Ventures (C3's release; the "
         "firm's post): the first round after the seed, which no source names; Series A by position at low confidence."))

L.append(cls("tinyclues", status="acquired", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2018/02/22/tinyclues-series-b/", entry_date="2018-02", **site_c("tinyclues", "FR"), city="Paris",
    focus="SaaS",
    note="AI campaign targeting for marketers. EQT Ventures led the $18M Series B (Feb 2018, TechCrunch). acq. by Amplitude, 2024 (the firm's Exit 2024)."))

L.append(cls("token", status="private", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=A("enables-banks-to-generate"), entry_date="2017-04", city="London", country="GB", country_src="web_verified",
    country_cite=A("enables-banks-to-generate"), focus="Fintech & Payments",
    note="Open-banking payments (Token.io). 'Token has announced its Series A funding from major investors including Octopus Ventures, EQT Ventures and OP Financial Group' "
         "(the firm's post, 2017-04-24). Founded in Silicon Valley; operated from London since opening its European office (the firm's Key Facts still say United States)."))

L.append(cls("traplight", status="private", rng="below_1b", stage="Series A", stage_src="model", stage_conf="low", entry_date="2020-07",
    **site_c("traplight", "FI"), city="Tampere", focus="Media, Gaming & Advertising", flags=["stage_uncited"],
    note="Mobile games (Battle Legion). 'the EUR 8m investment round that the EQT Ventures fund lead' with Play Ventures and existing investors Initial Capital and Heartcore "
         "(the firm's post, 2020-07-09; Tech.eu): the first round after the studio's seed, which no source names; Series A by position at low confidence. The firm's Exit 2022 "
         "is its own sale; no sale or closure of the studio was found."))

L.append(cls("unmind", status="private", rng="below_1b", stage="Growth", stage_src="web_verified", stage_conf="high",
    stage_cite="https://techcrunch.com/2021/05/12/unmind-raises-47m-for-a-platform-to-provide-mental-health-support-in-your-workplace",
    entry_date="2021-05", **site_c("unmind", "GB"), city="London", focus="Healthcare & Bio",
    note="Workplace mental health platform. EQT Ventures led the $47M Series B (May 2021, TechCrunch)."))

L.append(cls("unomaly", status="acquired", rng="below_1b", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=A("partners-with-unomaly"), entry_date="2016-06", **site_c("unomaly", "SE"), city="Stockholm", focus="Data Infrastructure",
    note="Log anomaly detection. 'EQT Ventures leads the EUR 4 M A-round of Unomaly' (the firm's post, 2016-06-21), after a EUR 1.9M seed in 2013. acq. by Datadog, 2020 "
         "(the firm's Exit 2020)."))

jl.write("batch-002", L)
