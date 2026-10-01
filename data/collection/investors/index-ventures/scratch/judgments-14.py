"""PRO-82 grind, batch-014: zendesk and the Form D rows adjudicated as members (the others were ruled out in
judgments-formd.py; dahlia-labs-inc and kiosk-inc are name variants of daydream and parallel, merged at the rebuild).
A Form D member needs both lines: the verdict (formd_adjudicated: the firm's partner sat as a director of the issuer
while at the firm, T4) and the classification."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, narch, sib, news, rnd, nqurl, verdict, arch = gl.C, gl.post, gl.narch, gl.sib, gl.news, gl.rnd, gl.nqurl, gl.verdict, gl.arch
L = []
def fd(slug):
    return (gl.Q[slug].get("formd_links") or "").split("; ")[0] or None
def member(slug, basis):
    L.append(verdict(slug, "member", basis, ec="formd_adjudicated", conf="high", cite=fd(slug)))

u = narch("Zendesk announces $60 Million")
L.append(C("zendesk", city="San Francisco", stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=u, entry_date="2012-09", rng="below_1b", focus="SaaS",
    note="Customer service software (San Francisco; founded in Copenhagen); 'Redpoint Ventures led the $45 million equity financing with participation by Index Ventures, GGV Capital, Goldman Sachs and the company's existing venture capital investors' (the firm's own news item, 2012-09-12): the Series D, the firm's entry; NYSE IPO May 2014; taken private by Hellman & Friedman and Permira, 2022",
    rounds=[rnd("2012-09-12", "Series D", 45000000, "Redpoint Ventures", True, u, "firm")]))

member("fleetsmith-inc", "T4 (decisions.md D5): Ilya Fushman, an Index partner 2015-2018, is a director on the issuer's Form D of 2016, inside his seat at the firm; the firm backed the seed with Harrison Metal")
L.append(C("fleetsmith-inc", status="acquired", city="San Francisco", rng="below_1b", grad="graduated", grad_src="formd", focus="DevTools & APIs",
    note="Apple device management for small and mid-size companies (San Francisco); Index was in the $3.1M seed, Ilya Fushman on the board (Form D 2016), then a $6.7M Series A in 2018 and a $30M Series B led by Menlo in 2019 (Form Ds); acq. by Apple, June 2020 (CNBC)",
    extra={"status_citation": nqurl('"Fleetsmith" Apple acquires', "Apple buys Fleetsmith")}))

u = post("optimizely-raises-58m")
member("optimizely-inc", "T4 (decisions.md D5): Ilya Fushman and Mike Volpi, Index partners, are directors on the issuer's Form D of 2015, the Series C that Index led (the firm's post 'Optimizely Raises $58M', 2015-10-13)")
L.append(C("optimizely-inc", status="acquired", city="San Francisco", rng="below_1b", focus="SaaS",
    note="Website A/B testing and experimentation platform (San Francisco); Index led the $58M Series C of October 2015 (the firm's post; Form D 2015 with Ilya Fushman and Mike Volpi as directors), after Benchmark, Bain Capital Ventures, Battery and a16z; acq. by Episerver, 2020, which took the Optimizely name",
    rounds=[rnd("2015-10-13", "Series C", 58000000, "Index Ventures", True, u, "firm")]))

member("skyport-systems-inc", "T4 (decisions.md D5): Mike Volpi, an Index partner since 2009, is a director on the issuer's Form Ds of 2017; the firm led the $30M Series B of 2015")
L.append(C("skyport-systems-inc", dispute=("stage",), status="acquired", city="Mountain View", stage="Growth", stage_src="model", stage_conf="high", entry_date="2015", rng="below_1b",
    focus="Security", note="Secure hyper-converged servers for critical infrastructure (Mountain View); Index led the $30M Series B of 2015, Mike Volpi on the board (director on the 2017 Form Ds), after a 2013 Series A from Sutter Hill and Intel Capital; acq. by Cisco, 2018; the Form D band reads the company's first sale in 2013, which was not the firm's round"))

member("zesty-inc", "T4 (decisions.md D5): Danny Rimer, an Index partner, is a director on the issuer's Form D of 2015, the $17M-$20M Series A that Index led")
L.append(C("zesty-inc", status="acquired", city="San Francisco", stage="Series A", stage_src="model", stage_conf="high", entry_date="2015-06", rng="below_1b", focus="Consumer & Marketplaces",
    note="Healthy office catering marketplace (San Francisco; YC W14); Index led the Series A of June 2015, Danny Rimer on the board (Form D 2015, $20.4M); acq. by Square, 2018, for Caviar"))

member("saurus-inc", "T4 (decisions.md D5): Danny Rimer, an Index partner, is a director on the issuer's Form D of 2016, the $8M round that Index led; Saurus, Inc. is the company behind Imzy")
L.append(C("saurus-inc", status="defunct", city="Salt Lake City", rng="below_1b", focus="Consumer & Marketplaces",
    note="Imzy, a community platform founded by former Reddit staff (Saurus, Inc., Salt Lake City); Index led the $8M Series A of 2016, Danny Rimer on the board (Form D 2016); shut down in 2017 (Axios)",
    extra={"status_citation": nqurl('"Imzy" raises Index Ventures', "Imzy, a Reddit challenger, is shutting down")}))

member("pomsg-ai-inc", "T4 (decisions.md D5): Danny Rimer, an Index partner, is a director on the issuer's Form D of 2017, the $5.1M round that Index led; POMSG AI, Inc. traded as msg.ai and is now Netomi")
L.append(C("pomsg-ai-inc", status="private", city="San Francisco", rng="below_1b", grad="graduated", grad_src="formd", focus="AI & Applied AI",
    note="AI customer-service agents, founded as msg.ai and now Netomi (POMSG AI, Inc., San Francisco area; YC W16); Index led the $5.1M round of March 2017, Danny Rimer on the board (Form D 2017); later Form Ds of $15M (2020), $30M (2021) and $55M (2025)"))
gl.write("batch-014", L)
