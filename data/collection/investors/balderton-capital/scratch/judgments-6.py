"""PRO-106 grind, batch-006 (video-island .. yassir-inc), and one correction to batch-005 (scytl).
The Form D-only rows are judged cluster-first (COLLECTION.md s3): one ruling per roster person."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd = jl.cls, jl.verdict, jl.rnd
LIST = "https://www.balderton.com/companies/"
NEWS = "https://www.balderton.com/news/"
L = []
def fp(slug, stage, conf="medium", **kw):
    return cls(slug, stage=stage, stage_src="first_party", stage_cite=LIST, stage_conf=conf, **kw)
def wv(slug, stage, cite, **kw):
    return cls(slug, stage=stage, stage_src="web_verified", stage_cite=cite, stage_conf="high", **kw)
def und(slug, **kw):
    return cls(slug, stage="undetermined", **kw)
def out(slug, basis, conf="high", cite=None, ec="formd_adjudicated"):
    return verdict(slug, "not_member", basis, ec=ec, conf=conf, cite=cite)

# correction: the 2010 round is the entry (TechCrunch 2010-07-13), so the card's label stands
L.append(fp("scytl", "Growth", clear=[], note="CORRECTION to batch-005: TechCrunch of 2010-07-13 reports the $9.2M round from Balderton, Nauta and Spinnaker, the entry the card calls 'Series B in 2010'; Wikipedia's 2006 date for the same round is wrong"))

L.append(fp("violet", "Seed", status="private", country="DE", country_src="web_verified", country_cite=LIST, city="Berlin", entry_date="2023",
    rng="below_1b", focus="Crypto & Web3", flags=["model_disputes_source"],
    note="On-chain compliance and identity; card 'Seed in 2023'; the pre-filled country HR is a wrong join (Felicis's Violet is a different company)"))
L.append(fp("virtuo", "Series A", status="private", country="FR", city="Paris", rng="below_1b", focus="Consumer & Marketplaces",
    note="App-based car rental; card 'Series A in 2017' (the firm's post of 2017-09-14, EUR 7.5M led by Balderton); EUR 20M Series B 2019"))
L.append(wv("vivenu", "Series A", NEWS + "vivenu-secures-e12-6m-series-a-to-empower-ticket-sellers-worldwide/", status="private", country="DE", city="Düsseldorf",
    rng="below_1b", focus="SaaS", note="API-first ticketing platform; the firm's post of 2020-12-01 announces the EUR 12.6M Series A Balderton led; $50M Series B 2021"))
L.append(fp("voi", "Series A", status="private", country="SE", country_src="web_verified", country_cite=LIST, city="Stockholm", rng="below_1b",
    focus="Consumer & Marketplaces", flags=["model_disputes_source"],
    note="E-scooter sharing; card 'Series A in 2018' (Balderton led the $50M Series A of Nov 2018); below $1B as in the Creandum and Felicis books (the 2021 mark collapsed); the pre-filled country CH is a wrong join"))
L.append(wv("voize", "Series A", NEWS + "voize-raises-50-million-to-power-the-ai-companion-transforming-nursing-care/", status="private", country="DE", city="Berlin",
    rng="below_1b", focus="AI & Applied AI", note="AI documentation companion for nurses; the firm's post of 2025-11-17 announces the $50M Series A Balderton led (Form D of 2025-Q4 under the legal name anyvoice Inc., Waterhouse director); band re-checked in the momentum pass"))
L.append(wv("wayve", "Series A", NEWS + "wayve-secures-20m-series-a-to-facilitate-self-driving-car-trials-in-london/", status="private", city="London",
    focus="AI & Applied AI", flags=["needs_web_value"],
    note="Embodied AI for driving; Balderton joined the $20M Series A of Nov 2019 led by Eclipse (the firm's post; Wikipedia); $1.05B Series C May 2024; mark pinned in the A/B pass"))
L.append(und("weeworld", status="unknown", city="Glasgow", rng="below_1b", focus="Consumer & Marketplaces",
    note="Avatar-based social network (Saw-You until 2006); on Benchmark's worldwide list 2005-08 (Europe lineage); neither the entry round nor the company's fate is on any surface read"))
L.append(fp("wooga", "Series A", status="acquired", city="Berlin", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Casual games; card 'Series A in 2009' (the EUR 5M round of Nov 2009 led by Balderton, Wikipedia); acq. by Playtika, 2018"))
L.append(fp("workable", "Growth", status="private", country="US", city="Boston", rng="below_1b", focus="SaaS",
    note="Recruiting software (founded in Athens); card 'Series B in 2015' (the $27M Series B of Oct 2015 led by Balderton, Wikipedia); Evans has been a director of the UK holding company since 2014-12, ten months before the announcement; $50M Series C 2018"))
L.append(fp("workhuman", "Series A", status="private", country="IE", city="Dublin", focus="SaaS", flags=["needs_web_value"],
    note="Employee recognition software (Globoforce until 2019, the same row as the Benchmark-era listing); card 'Series A in 2002'; its S-1 of 2013-14 says Barry Maloney joined the board in December 2001 and names Benchmark Europe I, L.P., later Balderton Capital I, L.P., among the shareholders; the card says Exited (the firm sold), the company remains private; mark pinned in the A/B pass"))
L.append(wv("writer", "Growth", NEWS + "writer-announces-100-million-series-b-to-help-deliver-generative-ai-to-the-enterprise/", status="private", country="US",
    city="San Francisco", focus="AI & Applied AI", flags=["needs_web_value"],
    note="Enterprise generative AI platform; Balderton joined the $100M Series B of Sep 2023 led by ICONIQ (the firm's post; card 'Series B, 2023'); $200M Series C Nov 2024; mark pinned in the A/B pass"))
L.append(und("xignal", status="acquired", country="DE", city="Munich", rng="below_1b", focus="Industrial & Robotics",
    note="Analog-to-digital converter chips; on the Benchmark Europe desk page 2003-07; the entry round is not named on any surface read; acq. by National Semiconductor, 2007; Benchmark's book carries the same row"))
L.append(cls("yingli-solar", status="acquired", country="CN", city="Baoding", stage="Growth", stage_src="model", stage_conf="medium", rng="below_1b",
    focus="Climate & Energy",
    note="Solar panel maker (founded 1998); card gives the year 2006 only: the pre-IPO preferred financing of 2006 (the 2007 F-1 files the agreements naming the fund), a growth entry; NYSE IPO 2007, delisted 2018, taken over in its 2020 restructuring; aligned to Benchmark's book"))
L.append(fp("yokoy", "Series A", status="acquired", country="CH", city="Zurich", rng="below_1b", focus="Fintech & Payments",
    note="Spend management platform; card 'Series A in 2021' (the firm's post of 2021-10-26, $26M led by Balderton); acq. by TravelPerk, 2025"))
L.append(wv("zego", "Series A", "https://techcrunch.com/2017/11/18/zego/", status="private", country="GB", city="London", focus="Fintech & Payments",
    flags=["needs_web_value"],
    note="Commercial motor insurance for gig workers; Balderton led the GBP 6M Series A of Nov 2017 (TechCrunch; Moffat director of Extracover 2017-19); $150M Series C at $1.1B Mar 2021; mark pinned or killed in the A/B pass"))
L.append(wv("zoe", "Growth", NEWS + "zoe-secures-additional-series-b-funding-in-preparation-for-uk-launch/", status="private", country="GB", city="London",
    rng="below_1b", focus="Healthcare & Bio", note="Personalised nutrition; the firm's post of 2021-12-17 announces the Series B extension Balderton joined (card 'Series B in 2021')"))

# ---- Form D-only rows, by roster person
L.append(verdict("abiquo-group-inc", "member", "Balderton led the $10M Series B of Nov 2010 and Bernard Liautaud joined the board (TechCrunch 2010-11-30); he signs the Form Ds of 2010-13 as director, inside his tenure",
    ec="web", conf="high", cite="https://techcrunch.com/2010/11/30/enterprise-cloud-management-software-maker-abiquo-raises-10-million/"))
L.append(wv("abiquo-group-inc", "Growth", "https://techcrunch.com/2010/11/30/enterprise-cloud-management-software-maker-abiquo-raises-10-million/", status="private",
    city="Redwood City", rng="below_1b", focus="Data Infrastructure", flags=["stage_disputes_band"],
    note="Cloud management software (founded in Barcelona, US HQ at the time of the filings); Series B led by Balderton, Nov 2010; status low confidence (the company was still trading in the 2020s)"))
L.append(out("dashlane-inc", "Bernard Liautaud co-founded Dashlane and chairs it: TechCrunch of 2014-05-19 names him as the founder of Business Objects who 'is currently a general partner at Balderton', not Balderton as an investor; no Balderton list, post or fund filing carries the company. A partner's own company is personal (T2, T4).",
    cite="https://techcrunch.com/2014/05/19/dashlane-raises-record-22m-for-its-cloud-based-password-manager-after-clocking-2m-users/", ec="web"))
L.append(verdict("daylife-inc", "member", "Wikipedia: 'Daylife was funded by Balderton Capital, Arts Alliance, The New York Times, and Getty Images'; Roberto Bonanzinga signs the 2009 Form D as director, inside his tenure",
    ec="web", conf="medium", cite="https://en.wikipedia.org/wiki/Daylife"))
L.append(und("daylife-inc", status="acquired", country="US", city="New York", rng="below_1b", focus="Media, Gaming & Advertising",
    note="News content platform for publishers; the round Balderton entered is not named on any surface read; acq. by NewsCred, 2012 (TechCrunch)"))
for s, n in [("digital-reasoning-systems-inc", "Digital Reasoning"), ("lookingglass-cyber-solutions-inc", "LookingGlass"), ("nav-technologies-inc", "Nav"),
             ("new-york-shipping-exchange-inc", "NYSHEX")]:
    L.append(out(s, f"{n}: Rana Yared's Goldman Sachs board seat, on filings of 2014-18 before she joined Balderton in February 2020; the firm's own welcome post lists it among the boards she sat on from Goldman (seat dated against the person's firm, T4; partner-carried, Erik 2026-09-17)",
        cite=NEWS + "press-release-balderton-capital-europes-most-active-series-a-investor-welcomes-two-new-general-partners/", ec="web"))
L.append(verdict("ewise-group-inc", "member", "Balderton led eWise's $12.1M round of Jul 2010 and joined the $14M round of Jun 2011 led by Wellington (TechCrunch); Dharmash Mistry signs the 2011 Form Ds as director, inside his tenure",
    ec="web", conf="high", cite="https://techcrunch.com/2010/07/28/ewise-raises-12-million-for-online-payments-technology/"))
L.append(cls("ewise-group-inc", status="unknown", city="Denver", stage="Growth", stage_src="model", stage_conf="medium", rng="below_1b", focus="Fintech & Payments",
    flags=["stage_disputes_band"],
    note="Online banking payments (founded 2000); Balderton led the $12.1M round of Jul 2010, an unnamed round in a ten-year-old company; the Form D band read the 2011 filing as a Series A; the company's later fate is not on any surface read"))
for s, n in [("fairway-energy-partners-llc", "Fairway Energy Partners (Houston)"), ("northworks-automation-inc", "Northworks Automation (Houston)")]:
    L.append(out(s, f"{n}: 'Jim / James Wise' on the filing is a Houston energy investor, a homonym of Balderton's James Wise (London; his only US filing is 3D Hubs); no Balderton surface carries the company", conf="high"))
for s, n in [("glamour-the-squalor-production-llc", "a Tacoma film production LLC"), ("mammoth-universal-inc", "Mammoth Universal (Denver)"),
             ("tellurian-investments-inc", "Tellurian Investments (Houston)")]:
    L.append(out(s, f"{n}: the 'Mark Evans' on the filing is a homonym; Balderton's Mark Evans sat on European boards (NaturalMotion, Figleaves, Depop, Workable) and no Balderton surface carries the company", conf="high"))
L.append(verdict("gemvara-inc", "member", "TechCrunch of 2012-06-04 names Balderton Capital among Gemvara's existing investors in the $25M Series D; the 2011 Form D names the firm and Mark Evans signs as director, inside his tenure",
    ec="web", conf="high", cite="https://techcrunch.com/2012/06/04/custom-jewlery-gemvara-25m-series-d/"))
L.append(und("gemvara-inc", status="acquired", city="Boston", rng="below_1b", focus="Consumer & Marketplaces", flags=["stage_disputes_band"],
    note="Custom jewellery retailer; Balderton was an existing investor by the Series D of Jun 2012; which earlier round it entered is not named on any surface read (the Form D band's Pre-Seed reads a $0.1M filing of 2009); acq. by Richline Group (Berkshire Hathaway), 2016"))
L.append(out("lemonade-inc", "David Thevenon's SoftBank seat: the 2018 filing predates his joining Balderton in 2020 (the firm's welcome post: a partner at SoftBank's Vision Fund for five years); no Balderton surface carries Lemonade (T4)",
    cite=NEWS + "press-release-balderton-capital-europes-most-active-series-a-investor-welcomes-two-new-general-partners/", ec="web"))
L.append(out("power-assure-inc", "George Coelho left the LLP on 2008-04-30 (Companies House OC306910); the filings of 2009-11 are seats of his next firm (T4)", conf="high"))
L.append(out("rainstor-inc", "Peter Malcolm appears only on the 2001-02 Benchmark Europe desk pages; the 2011-12 filings are his own later role at RainStor (formerly Clearpace); no Balderton surface carries the company (T4)", conf="high"))
L.append(verdict("saatchi-online-inc", "member", "Roberto Bonanzinga signs the April 2013 Form D as director, inside his tenure, and Demand Media's 2014 resale prospectus for the shares issued in its purchase of Saatchi Online names the Balderton fund among the selling stockholders",
    ec="fund_filing", conf="high", cite="https://www.sec.gov/Archives/edgar/data/1365038/000110465914064026/a14-20115_1s3.htm"))
L.append(und("saatchi-online-inc", status="acquired", city="Santa Monica", rng="below_1b", focus="Consumer & Marketplaces",
    note="Online art gallery (Saatchi Art); the round Balderton entered is not named on any surface read; acq. by Demand Media, 2014 (the Demand Media shares Balderton then held are sale consideration, not a row)"))
L.append(out("yassir-inc", "Lars Fjeldsoe-Nielsen left the LLP on 2020-12-31 (Companies House OC306910); the filing of 2021-Q4 is a seat from his next role (T4); no Balderton surface carries Yassir", conf="high"))
jl.write("batch-006", L)
