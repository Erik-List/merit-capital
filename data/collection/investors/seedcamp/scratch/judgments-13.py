"""PRO-83 grind, batch-013 (traity .. zuko); the Form D rows at its tail and all of batch-014 were ruled
not_member in judgments-formd.py. Whispr renamed itself Lua (re-judged here with Whispr's own post)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"
FII14 = ("first listed on the firm's /companies/ list captured 2014-03-12, inside the Fund II years, when the programme's "
         "standard cheque was the firm's only instrument (decisions.md D3)")
FII = ("first listed on the firm's 2012-2014 /companies/ list, inside the Fund II years, when the programme's standard cheque "
       "was the firm's only instrument (decisions.md D3)")


def fp(slug, stage, url, date, country, city, cite=None, **kw):
    kw.setdefault("stage_conf", "high")
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, entry_date=date,
             **loc(country, city, cite), **kw)


def und(slug, year, country, city, note, cite=None, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city, cite), note=note, **kw)


L = []
L.append(c("traity", prog_at="2012", **loc("ES", "Madrid"), status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    stage_conf="medium",
    note="Online reputation and trust scores ('amazing teams like Traity ... joined the family', the firm's post of 2012-09-13; 'Traity - Seedcamp "
         "Winner'); traity.com does not answer; " + FII))
L.append(c("try-com", prog_at="2012-08", **loc("GB", "London"), status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    stage_conf="medium",
    note="Try clothes at home before buying (try.com, now a domain for sale); the firm's logo for it was uploaded 2012-08, inside the Fund II years "
         "(decisions.md D3), though the archived lists read carry it only from 2018"))
L.append(und("twine", 2015, "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Marketplace for creative freelancers ('Seedcamp-backed company Twine', 2016-11-17; twine.net live); on the firm's lists under a 2015-02 logo; "
         "no round named"))
L.append(und("txt", 2023, "US", None, status="private", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown"],
    note="Structured outputs for LLMs (.txt, dottxt, Inc., makers of Outlines); site live; the 2023 entry round is not named"))
L.append(pc("uberblic-labs", "Uberblic Labs", "DE", "Berlin", status="unknown", rng="below_1b", focus="DevTools & APIs",
    note="Data integration service (Seedcamp Week 2010 winner); no later trace found"))
L.append(und("umony", 2024, "GB", "London", cite=V + "umony-announces-15m-series-a-and-powerhouse-advisory-board/", status="private",
    rng="below_1b", focus="Fintech & Payments",
    note="Capture and AI monitoring of regulated communications ('the London, UK-based company'); the firm's post of 2025-09-30: 'supporting Umony "
         "since the very first round' (no round word), then its $15M Series A"))
L.append(fp("uncovr", "Seed", "uncovr-raises-7-million-to-build-the-system-of-intelligence-for-surgery/", "2025", "FR", "Paris",
    status="private", rng="below_1b", focus="Healthcare & Bio", stage_conf="medium",
    note="Surgical video to operative reports (engineering in Paris, an office in San Francisco); the firm's post of 2026-06-10: 'we're so proud to "
         "participate in Uncovr's $7 million seed round, led by Index Ventures' and 'believer since day one'; the firm's investment year is 2025, "
         "hence medium"))
L.append(c("unifiedcrm", stage="undetermined", entry_date="2023", status="private", rng="below_1b", focus="SaaS", flags=["city_unknown"],
    note="Unified sales hub for remote and hybrid teams (unifiedcrm.ai, live); the 2023 entry round is not named; the country is not established"))
L.append(pc("unlease", "Unlease", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Flexible medium-term sublets (January 2016 cohort); no later trace found"))
L.append(c("unmanned-systems", prog_at=jl.coh("Unmanned Systems")["post_date"][:7], cohort=jl.coh("Unmanned Systems")["url"],
    country="BE", country_src="web_verified", country_cite=jl.coh("Unmanned Systems")["url"], flags=["city_unknown"],
    status="unknown", rng="below_1b", focus="AI & Applied AI",
    note="Drone-as-a-service platform (January 2016 cohort, Belgium); no later trace found"))
L.append(c("utopia", stage="undetermined", entry_date="2020", status="private", rng="below_1b", focus="DevTools & APIs",
    flags=["model_disputes_source", "city_unknown"],
    note="Design-and-code platform for building applications (utopia.app, live; the firm's 2021 devtools post); the pre-filled DE is a one-word "
         "Wikidata join and is not confirmed; the country is not established; the 2020 entry round is not named"))
L.append(fp("vaire", "Seed", "vaire-computing-secures-4-5m-to-create-near-zero-energy-silicon-chips-using-reversible-computing/", "2024-07-02",
    "GB", "London", V + "vaire-computing-secures-4-5m-to-create-near-zero-energy-silicon-chips-using-reversible-computing/", status="private",
    rng="below_1b", focus="AI & Applied AI",
    note="Reversible-computing chips ('a London- and Seattle-based company'); the firm's post of 2024-07-02: 'excited to participate in Vaire's $4 million "
         "Seed funding round co-led by 7percent Ventures and Jude Gomila'"))
L.append(fp("vance", "Pre-Seed", "vance-raises-1-5m-to-free-businesses-from-back-office-admin-using-generative-ai/", "2024-07-11",
    "GB", "London", status="private", rng="below_1b", focus="AI & Applied AI",
    note="AI back-office service for startups and SMBs (Vance, renamed Vera; founder Simon Holland); the firm's post of 2024-07-11: 'participate in "
         "Vance's $1.5 million oversubscribed pre-seed funding round'"))
L.append(und("vantik", "2018-04", "DE", "Berlin", cite=V + "vantik-the-worlds-first-fully-digital-private-pension-for-milennials/",
    status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Digital private pension ('A new investment from us out of Berlin'); the firm's post of 2018-04-24 joins an 850k round with Atlantic Labs "
         "(no round word); insolvent Jun 2022, customer accounts sold Aug 2022 (Business Insider, Yahoo Finanzen)"))
L.append(und("vespucci", 2021, "US", None, status="private", rng="below_1b", focus="SaaS", flags=["model_disputes_source", "city_unknown"],
    note="Product analytics from customer data (Vespucci Technologies, Inc.; site live); the pre-filled acquired/IT is a one-word Wikidata join and "
         "is disputed; the 2021 entry round is not named"))
L.append(c("viewshound", prog_at="2012-05", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising", stage_conf="medium",
    flags=["city_unknown"],
    note="ViewsHound; on the firm's lists only 2012-2014, on no post read; no later trace found; the country is not established; " + FII))
L.append(und("visibly", 2022, "GB", "London", status="private", rng="below_1b", focus="Climate & Energy",
    note="Certification-as-a-service for infrastructure trades ('the UK-based company', founder Kane St Quintin); the firm's post of 2024-06-10: "
         "'participate in Visibly's $7.5 million funding round led by ... Creandum' (no round word); the 2022 entry round is not named"))
L.append(fp("vitesse", "Seed", "full-speed-automation-raises-3-2m-to-accelerate-the-transition-to-industry-4-0/", "2021-03-04",
    "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Automation operating system for industrial machines (Full Speed Automation, product and now name VITESSE); the firm's post of 2021-03-04: "
         "'We're excited to join Full Speed Automation on their journey in a $3.2m seed round led by ... HCVC'; the Vitesse payments company in "
         "the news pack is a namesake; the firm's investment year is 2020"))
L.append(fp("volter", "Pre-Seed", "volter-raises-3-2-million-to-power-up-solar-energy-generation-for-real-estate/", "2024-11-28",
    "GB", "London", V + "volter-raises-3-2-million-to-power-up-solar-energy-generation-for-real-estate/", status="private", rng="below_1b",
    focus="Climate & Energy", flags=["model_disputes_source"],
    note="Operating system for commercial rooftop solar ('a London-based company'); the firm's post of 2024-11-28: 'participate in Volter's $3.2 million "
         "pre-seed funding'; the pre-filled PL is a one-word Wikidata join and is corrected"))
L.append(c("voyage-control", prog_at="2014-09", **loc("GB", "London"), status="private", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Construction and freight delivery logistics (voyagecontrol.com, live); 'Voyage Control joined Seedcamp in September 2014 and like all Seedcamp "
         "companies, participated in Onboarding Week' (the firm's post of 2014-12-08), the Seedcamp Week programme on its standard deal"))
L.append(und("waniwani", 2026, "FR", "Paris", status="private", rng="below_1b", focus="AI & Applied AI",
    note="Revenue and compliance infrastructure for selling financial services inside AI apps (FrenchWeb, 2026-06-15); the firm's post of 2026-06-15: "
         "'thrilled to lead Waniwani's $8m round' (no round word)"))
L.append(c("we-are-colony", prog_at="2014-03", **loc("GB", "London"), status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    stage_conf="medium",
    note="VOD platform for independent film ('We first invested in Colony in 2014 when the business was pre-launch'); acq. by Fantastec, Mar 2018 (the "
         "firm's post); " + FII14))
L.append(und("webstudio", 2022, "DE", "Berlin", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Open-source visual development platform (founder Oleg Isonen); the site sits behind a bot check; the 2022 entry round is not named"))
L.append(fp("weengs", "Seed", "weengs-raises-2-2m-seed-round/", "2016-10-24", "GB", "London", status="defunct", rng="below_1b",
    focus="Consumer & Marketplaces",
    note="Collect, pack and ship for small sellers; the firm's post of 2016-10-24: 'Weengs Raises GBP 2.2M Seed Round ... investing in their GBP 2.2M "
         "seed'; WEENGS LIMITED 09433283 dissolved 2024-11-01 after insolvency (Companies House)"))
L.append(fp("wexler", "Seed", "wexler-raises-5-3m-to-transform-complex-litigation/", "2025-09-23", "GB", "London", CH + "14460752",
    status="acquired", rng="below_1b", focus="AI & Applied AI",
    note="AI fact analysis for litigation (Wexler AI Ltd, London); the firm's post of 2025-09-23: 'We are excited to participate in wexler.ai's $5.3 "
         "million seed round alongside Pear VC'; acq. by Legora, Jul 2026 (Law.com)"))
for s in ("lua", "whispr"):
    L.append(fp(s, "Pre-Seed", "our-investment-in-whispr-using-voice-technology-to-empower-billions-of-underserved-workers/", "2019-03-14",
        "DK", "Copenhagen", status="acquired", rng="below_1b", focus="SaaS",
        note="Voice guidance for frontline workers (Whispr, 'the Irish/Danish startup', renamed Lua, lua.work; same line on the firm's lists); the "
             "firm's post of 2019-03-14: 'We lead $750,000 pre-seed investment in ... Whispr' with PreSeed Ventures and Bose Ventures; "
             f"{EXIT} (2022-2024, acquirer not named there); the 2026 'Lua' seed led by Norrsken22 is a namesake"
             + ("" if s == "lua" else "; duplicate of lua (identity-merges.json)")))
L.append(und("wluper", 2018, "GB", "London", status="defunct", rng="below_1b", focus="AI & Applied AI",
    note="Knowledge for conversational AI (logo 2018-11); WLUPER LTD. 10195181 dissolved 2025-06-20 (Companies House); no round named"))
L.append(c("wombo", stage="undetermined", entry_date="2015", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    flags=["city_unknown"],
    note="Live-streaming for gaming and esports (logo 2015-10); wombo.gg does not answer; on no post read; the country is not established"))
L.append(fp("zenline-ai", "Pre-Seed", "zenline-ai-raises-1-6m-to-help-european-retailers-regain-competitiveness/", "2025-08-26",
    "CH", "Zurich", V + "zenline-ai-raises-1-6m-to-help-european-retailers-regain-competitiveness/", status="private", rng="below_1b",
    focus="AI & Applied AI",
    note="AI assortment decisions for retail category teams ('Based in Zurich, Switzerland'); the firm's post of 2025-08-26: 'We are excited to lead "
         "Zenline's $1.6 million Pre-Seed round'; the firm's investment year is 2024"))
L.append(und("zero1", "2018-12", "GB", "London", status="defunct", rng="below_1b", focus="Fintech & Payments",
    note="Purchase-order financing for suppliers (founders from Spain); 'Welcoming Zero1 to the Seedcamp Nation' (the firm's post of 2018-12-07, no "
         "round word); ZERO1 TECHNOLOGY LTD 11243291 dissolved 2021-01-05 (Companies House)"))
L.append(c("zuko", prog_at="2014-03", **loc("GB", "Manchester"), status="private", rng="below_1b", focus="SaaS", stage_conf="medium",
    note="Form analytics (Formisimo, Manchester, renamed Zuko; 'Formisimo - Seedcamp Winner', the firm's post of 2014-05-29); zuko.io live; " + FII14))

if __name__ == "__main__":
    jl.write("batch-013", L)
