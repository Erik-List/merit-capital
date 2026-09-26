"""PRO-79 grind, batch-004 part a: the 2008-2014 listing eras and two 2026
board companies (research agent C, citations re-fetched by verify-urls.py)."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
INS = "https://atomico.com/insights/"

L = []
L.append(cls("cinemaki", status="unknown", rng="below_1b", country="AR", city="Buenos Aires",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Argentine movie-recommendation social site across Latin America; on the 2011-2012 listings, and TNW (Feb 2012) names it among the companies Atomico backed before its first Brazil deals ('the Argentine movie recommendation site Cinemaki'); the round is unnamed and undated on every surface; no press after 2012 - status unknown"))
L.append(cls("cmune", status="defunct", rng="below_1b", country="CN", city="Beijing",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Maker of the UberStrike browser shooter (founded Seoul 2007, Beijing team); 'it has just announced that it has raised money from Atomico' (GamesBeat, May 2012) - Atomico was the initial funder, round unnamed and undisclosed; DCM's A-Fund led the next round Feb 2013 (TNW); shut down 2020 (Wikipedia)",
             rounds=[rnd("2012-05-11", "unnamed", None, None, True, "https://gamesbeat.com/cmune-spreads-uberstrike-to-new-platforms-and-raises-funds-from-skype-founder/")]))
L.append(cls("deca", status="private", rng="below_1b", country="US", city="Los Angeles",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Digital entertainment production house (founded 2007 by Michael Wayne and Chris Kimbell; created the Kin Community network in 2011, now the company's name); 'Mayfiled, General Catalyst Partners, and Atomico Investments have put $5 million into Deca.tv' (TechCrunch, Sep 2007; the firm's 2008 page: 'DECA is funded by Mayfield, Atomico, and General Catalyst Partners') - the round is unnamed; still operating as Kin Community (Playa Vista), only its Canadian arm sold to Corus 2019",
             rounds=[rnd("2007-09-27", "unnamed", 5000000, None, True, "https://techcrunch.com/2007/09/27/decatv-vcs-invest-new-media-production-house/")]))
L.append(cls("electric-twin", status="private", rng="below_1b", country="GB", city="London",
             focus="AI & Applied AI", stage="undetermined",
             note="Synthetic-audience simulation (Alex Cooper, Ben Warner, ex-No 10); 'The total includes a $10 million round led by Atomico' (Tech.eu, Feb 2026; the firm's own post the same day; Ben Blume director from Sep 2025, register) - the round's name conflicts across sources (FinSMEs 'Pre-Seed and Seed', deal counsel 'Series A', no article body names it) -> undetermined",
             rounds=[rnd("2026-02-12", "unnamed", 10000000, "Atomico", True, "https://tech.eu/2026/02/12/electric-twin-expands-ai-audience-platform-with-14m-round/")]))
L.append(cls("equal-media", status="defunct", rng="below_1b", country="GB", city="London",
             focus="Media, Gaming & Advertising",
             stage="Seed", stage_src="web_verified", stage_conf="medium",
             stage_cite="https://en.wikipedia.org/wiki/State_(website)",
             entry_date="2012-05",
             note="The company behind State (state.com), an opinion network (Alex and Mark Asseily); 'raised $14 million in seed financing in May 2012 from funders such as Atomico' (Wikipedia, citing TechCrunch, which lists 'Niklas Zennstrom of Atomico' but does not name the round - hence medium); on the firm's 2014-2020 listings; inactive by 2020 and Equal Media Ltd dissolved 2024; graduation decided in the S2A pass",
             rounds=[rnd("2012-05", "seed", 14000000, None, True, "https://en.wikipedia.org/wiki/State_(website)")]))
L.append(cls("fab", status="acquired", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces",
             stage="Growth", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2012/07/18/fab-seals-the-deal-on-105-million-in-new-funding",
             note="Design e-commerce (Jason Goldberg); 'This round serves as Fab's Series C ... was indeed led by London-based VC Atomico Ventures' (TechCrunch, Jul 2012; the firm's own release 'Atomico Leads $105 Million Series C Funding for Fab'); Atomico was not in the a16z-led Series B of Dec 2011; the Fab brand's US assets were sold to PCH International Mar 2015 and the Hem business (Fab's pivot, merged into this row) Feb 2016 -> acquired",
             rounds=[rnd("2012-07-18", "Series C", 105000000, "Atomico", True, "https://techcrunch.com/2012/07/18/fab-seals-the-deal-on-105-million-in-new-funding")]))
L.append(cls("fabricly", status="unknown", rng="below_1b", country="US", city="New York",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Crowdsourced independent-designer fashion (Y Combinator 2010; founders Ari Helgason and Tom Riley); filed under the firm's /portfolios/atomico-ii/ pages 2011-2012; a $400K round of Nov 2010 (Vator headline, page gone) is the likely Atomico round but no fetchable source confirms it -> undetermined; no press after 2012 - status unknown"))
L.append(cls("frontier-health", status="private", rng="below_1b", country="GB", city="London",
             focus="Healthcare & Bio",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://thenextweb.com/news/frontier-health-16m-seed-atomico-nhs-admin-ai-juno",
             entry_date="2026-06-18", grad="censored",
             note="AI agent for NHS administration (Rachel Finegold, ex-Palantir); 'The London startup announced a $16M seed round led by Atomico ... the first institutional money into the company' (TNW, Jun 2026; Tech.eu gives GBP 9.7M for the round; the firm's own post; Andreas Helbig director of Frontier AI Ltd from Mar 2026, register); censored",
             rounds=[rnd("2026-06-18", "Seed", 16000000, "Atomico", True, "https://thenextweb.com/news/frontier-health-16m-seed-atomico-nhs-admin-ai-juno")]))
L.append(cls("grows-up", status="unknown", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces", stage="undetermined",
             note="Online marketplace/community for mothers (founded 2010, San Francisco); filed under the firm's /portfolios/atomico-ii/ pages 2010-2011; the only round record is a vendor listing (not citable) -> undetermined; no press - status unknown"))
L.append(cls("heysan", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Consumer & Marketplaces",
             stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite="https://www.ycombinator.com/companies/heysan",
             entry_date="2007-07",
             note="Free mobile messaging (YC W07, Swedish founders, San Francisco); 'In the summer of 2007 Heysan raised a seed round from Khosla Ventures and Atomico' (YC's company page); on the firm's 2008-2012 listings; acquired by Good Technology May 2009; graduation decided in the S2A pass",
             rounds=[rnd("2007-07", "seed", None, None, True, "https://www.ycombinator.com/companies/heysan")]))
L.append(cls("jolicloud", status="defunct", rng="below_1b", country="FR", city="Paris",
             focus="SaaS",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2009/07/08/jolicloud-raises-42m-from-atomico-mangrove-zennstrom-takes-board-seat/",
             note="Cloud netbook OS, then personal cloud (Tariq Krim); 'has just raised $4.2 million in Series A funding from Atomico Ventures and Mangrove Capital Partners' (TechCrunch, Jul 2009; Zennstrom joined the board); discontinued 2016-04-01 (Wikipedia)",
             rounds=[rnd("2009-07-08", "Series A", 4200000, None, True, "https://techcrunch.com/2009/07/08/jolicloud-raises-42m-from-atomico-mangrove-zennstrom-takes-board-seat/")]))
L.append(verdict("joost", "not_member",
                 "D2 (the founders' own companies, T4): Zennstrom and Friis created Joost in 2006; a founder's company is a member only where an Atomico vehicle held it, and no surface shows one - the only outside round (the $45M of May 2007: Sequoia, Index, CBS, Viacom, Li Ka-shing) had no Atomico, and TechCrunch notes the seed 'presumably ... came directly from them'; the 2008 listing is the founders' history, as with Skype",
                 "site_listing", "medium", "https://techcrunch.com/2007/05/09/6022"))
L.append(cls("jott", status="acquired", rng="below_1b", country="US", city="Seattle",
             focus="SaaS", stage="undetermined",
             note="Voice-to-text messaging (founded 2006 by ex-Microsoft staff); 'The round was led by Bain Capital Ventures, which was joined by Draper Richards, Ackerley Partners and Atomico Investments (UK)' - the company's 'first equity financing' of $5.4M, May 2007 (Light Reading), unnamed; acquired by Nuance Jul 2009",
             rounds=[rnd("2007-05-14", "unnamed (first equity financing)", 5400000, "Bain Capital Ventures", True, "https://www.lightreading.com/network-technology/jott-com-raises-5-4m")]))
L.append(cls("kyte", status="acquired", rng="below_1b", country="US", city="San Francisco",
             focus="Media, Gaming & Advertising", stage="undetermined",
             note="Live and mobile video platform (decentral.tv); 'had raised $2.25 million earlier from investors that include Atomico ... Draper Fisher Jurveston and Draper Richards' (GigaOm, May 2007; Light Reading: Atomico among the founding investors) - unnamed; acquired by KIT digital Feb 2011 (Global Venturing)",
             rounds=[rnd("2007", "unnamed (founding round)", 2250000, None, True, "https://om.co/gigaom/kyte-tv-vc-cash/")]))
L.append(cls("madbid", status="defunct", rng="below_1b", country="GB", city="London",
             focus="Consumer & Marketplaces",
             stage="Series A", stage_src="web_verified", stage_conf="high",
             stage_cite="https://techcrunch.com/2010/07/26/penny-auction-site-madbid-secures-4m-from-atomico/",
             note="Pay-to-bid auction site; 'has secured GBP 4 million in a Series A funding from Atomico Ventures' (TechCrunch, Jul 2010; $6.2M at the ECB rate of 2010-07-26; Ljungman joined the board); administration 2018-06-28, service ceased Aug 2018 (Wikipedia)",
             rounds=[rnd("2010-07-26", "Series A", 6200060, "Atomico", True, "https://techcrunch.com/2010/07/26/penny-auction-site-madbid-secures-4m-from-atomico/")]))

if __name__ == "__main__":
    jl.write("batch-004a", L)
