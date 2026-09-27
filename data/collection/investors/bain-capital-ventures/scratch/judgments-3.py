"""PRO-162 grind, batch-003 (hazelcast .. national-cardiovascular-partners). Evidence as in judgments-1.py,
plus the firm's own 2012 company pages (Common Crawl captures, judge_lib.CCPAGE)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
cls, verdict, rnd, POST, SITE, W, NEWS, CCPAGE = jl.cls, jl.verdict, jl.rnd, jl.POST, jl.SITE, jl.W, jl.NEWS, jl.CCPAGE
L = []


def site_stage(slug):
    return dict(stage_src="first_party", stage_conf="medium", stage_cite=SITE(slug))


L.append(cls("hazelcast", status="private", rng="below_1b", city="Palo Alto", focus="Data Infrastructure",
    note="In-memory computing platform (Palo Alto). BCV (Salil Deshpande) entered with the 2013 seed the filings give. Graduation left for "
         "the graduation pass."))
L.append(cls("hightouch", status="private", rng="1b_plus", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Data Infrastructure", usd=2750000000, val_src="web_verified", asof="2026-04-29",
    val_cite=NEWS("hightouch", "$150 Million Series D At $2.75 Billion"), extra={"valuation_range_source": "web_verified"},
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("putting-data-in-the-hands"), entry_date="2021-07",
    note="Reverse-ETL and data activation (San Francisco). 'Bain Capital Ventures' participation in a $12M Series A financing for Hightouch' "
         "(the firm's post, 2021-07-21). Mark: the $150M Series D of April 2026 at $2.75B (Pulse 2.0)."))
L.append(cls("hireology", status="private", rng="below_1b", city="Chicago", focus="SaaS",
    note="Hiring platform (Chicago); $27M round in 2019. Operating; entry from the filings (Michael Krupka, 2014)."))
L.append(cls("homebase", status="private", rng="below_1b", city="San Francisco", focus="SaaS",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=W("Homebase (software company)"), entry_date="2018",
    note="Hourly-team management (San Francisco). 'In 2018, Homebase raised $20 million in a series B round led by Bain Capital Ventures' "
         "(Wikipedia); BCV's listing gives 2017 (the close). Series C $71M (2021) and D $60M (2024) followed."))
L.append(cls("hooklogic-criteo", status="acquired", rng="below_1b", city="New York", focus="Media, Gaming & Advertising",
    note="Retail search advertising (New York). Acquired by Criteo in 2016 (the firm's listing)."))
L.append(cls("humedica-unitedhealth-group", status="acquired", rng="below_1b", city="Boston", focus="Healthcare & Bio",
    note="Clinical analytics (Boston). Acquired by UnitedHealth Group's Optum in 2013 (the firm's archive)."))
L.append(cls("hycu", status="private", rng="below_1b", city="Boston", focus="Data Infrastructure",
    stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("data-backup-in-a-hybrid"), entry_date="2021-03",
    flags=["stage_disputes_band"],
    note="Multi-cloud backup (Boston). 'BCV Leads $87.5 Million Series A In HYCU' (the firm's post, 2021-03-30): a Series A by name, whatever "
         "its size (COLLECTION.md s6: the label follows what the record calls the round), so the band's Growth and the listing's Growth tag "
         "are overruled (decisions.md R2 names this case)."))
L.append(cls("iex", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="Fintech & Payments", stage="Growth", **site_stage("iex"), entry_date="2014",
    note="Stock exchange (IEX Group, New York). BCV's listing: 2014, Growth (Matt Harris), the $75M 2014 raise (Traders Magazine); a $75M "
         "Series C followed in 2018."))
L.append(cls("ike-robotics-nuro", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="Industrial & Robotics", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("we-like-ike"),
    entry_date="2019-02",
    note="Autonomous trucking (San Francisco). BCV led Ike's $52M Series A (the firm's post 'We Like Ike: Investing In Autonomous Freight', "
         "2019-02-05). Acquired by Nuro in December 2020."))
L.append(cls("inauth-american-express", status="acquired", rng="below_1b", city="Boston", focus="Security",
    note="Device identity and fraud risk (Boston). Acquired by American Express (the firm's listing)."))
L.append(cls("infoscout-acquired-by-numerator-in-2017", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="San Francisco", focus="Consumer & Marketplaces", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("backedbybcv-infoscout"), entry_date="2013",
    note="Shopper receipt panel (San Francisco). 'We were fortunate to lead the Series A for InfoScout in early 2013' (the firm's post, "
         "2017-06-19); merged into Numerator in 2017."))
L.append(cls("inrix", status="private", rng="below_1b", city="Kirkland", focus="Data Infrastructure",
    note="Traffic and mobility data (Kirkland, WA). BCV listed it from 2006; operating and private."))
L.append(cls("invoke-solutions", status="unknown", rng="below_1b", city="Waltham", focus="SaaS", stage="undetermined",
    note="Market-research software (Waltham, MA), listed by the firm 2003-2013 (Michael Krupka). No sale or later trace found; state unknown. "
         "BCV's first round (by 2003) is not named."))
L.append(cls("iodine-software-waystar", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Austin",
    focus="Healthcare & Bio", stage="Growth", **site_stage("iodine-software-waystar"), entry_date="2018",
    note="Clinical documentation AI (Austin). BCV's listing: 2018, Growth. Acquired by Waystar in 2025."))
L.append(cls("jet-walmart", status="acquired", rng="below_1b", city="Hoboken", focus="Consumer & Marketplaces",
    note="E-commerce (Jet.com, Hoboken). Walmart bought it for $3B in 2016 (TechCrunch). BCV's listing gives 2014, before the $140M round of "
         "February 2015 the filings give; the entry round is taken from the filings pending a source for the 2014 round."))
L.append(cls("join-the-company", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", flags=["city_unknown"],
    note="Social game developer; 'Join the company was acquired by GSN (Game Show Network) in December 2011' (the firm's archived page). "
         "The filing carries no address and no source read places it."))
L.append(cls("justworks", status="private", rng="below_1b", city="New York", focus="SaaS",
    note="PEO and payroll (New York). Filed for an IPO in 2021 and withdrew; private. Its only reported unicorn figures are vendor estimates "
         "(COLLECTION.md s6 Rule A, ruled on this company), so below_1b. Entry from the filings (Matt Harris on the board since July 2015)."))
L.append(cls("kalderos", status="private", rng="below_1b", city="Chicago", focus="Healthcare & Bio",
    note="Drug-discount management (Chicago); $28M Series B in June 2020, the round the filings give."))
L.append(cls("keap", status="acquired", rng="below_1b", city="Chandler", focus="SaaS",
    stage="Growth", stage_src="model", stage_conf="medium", entry_date="2014",
    note="Small-business CRM (Keap, formerly Infusionsoft; Chandler, AZ). BCV listed Infusionsoft from 2014, the year of its $110M growth round, "
         "well past its early rounds; the 2018 Form D (Indranil Guha, Merritt Hummer) is a later round. Thryv acquired Keap in 2024 (Thryv's "
         "2025 10-K names BCV's funds)."))
L.append(cls("kiva-systems-amazon-robotics-since-2012", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="Woburn", focus="Industrial & Robotics", stage="Series A", stage_src="web_verified", stage_conf="high",
    stage_cite=POST("hot-off-the-assembly"), entry_date="2004",
    note="Warehouse robots (Woburn, MA). 'Bain Capital Ventures led the first institutional investment in Kiva Systems' (the firm's post, "
         "2019-01-15), in 2004. Amazon bought Kiva for $775M in 2012."))
L.append(cls("leapyear-technologies", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Berkeley",
    focus="Security", stage="undetermined",
    note="Privacy-preserving analytics (Berkeley). Acquired by Snowflake in 2022. BCV's listing gives 2016 (Enrique Salem); the round is not named."))
L.append(cls("liazon", status="acquired", rng="below_1b", city="Buffalo", focus="Healthcare & Bio", stage="undetermined",
    note="Private benefits exchange (Buffalo). 'Bain Capital Leads $12.6 Million Financing in Liazon' (2011, the round Jeff Crisan's Form D "
         "records, in a company incorporated in 2007); Towers Watson bought it in 2013. The round is not named."))
L.append(cls("liberty-dialysis", status="acquired", rng="below_1b", city="Mercer Island", focus="Healthcare & Bio",
    stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=CCPAGE("/portfolio/company/liberty-dialysis"), entry_date="2002",
    flags=["stage_disputes_band"],
    note="Dialysis provider (Mercer Island, WA). 'Bain Capital Ventures seeded and co-founded Liberty Dialysis alongside management in 2002' "
         "(the firm's own company page, 2012 capture); the Form D band read a 2010 filing. Merged with Renal Advantage and sold to Fresenius "
         "for $1.7B in 2012. Graduation left for the graduation pass."))
L.append(cls("lightbend", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="San Francisco",
    focus="DevTools & APIs", stage="undetermined",
    note="Reactive application platform (Lightbend, formerly Typesafe; San Francisco); a $25M round led by Dell in 2020. BCV's listing gives "
         "2013; the round is not named."))
L.append(cls("lightning-ai", status="private", rng="below_1b", country="US", country_src="model_knowledge", city="New York",
    focus="AI & Applied AI", stage="Seed", **site_stage("lightning-ai"), entry_date="2020",
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("lightning-ai", "Raises $40M"),
    note="ML development platform (Lightning AI, formerly Grid.ai; New York). BCV's listing: 2020, Seed; the $40M Series B of June 2022 "
         "(AlleyWatch) followed the 2021 Series A.",
    rounds=[rnd("2022-06", "Series B", 40000000, None, None, NEWS("lightning-ai", "Raises $40M"), "press")]))
L.append(cls("lime", status="public", city="San Francisco", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="medium", stage_cite=W("Lime (transportation company)"),
    note="Shared e-bikes and scooters (Neutron Holdings; San Francisco). BCV's listing gives 2019 (Sarah Smith); Wikipedia records BCV in the "
         "$170M Uber-led round of May 2020; both are late rounds, so Growth. IPO on Nasdaq (LIME) in June 2026; market cap pinned in the "
         "A/B pass."))
L.append(cls("linkable-networks-collinson-group", status="acquired", rng="below_1b", city="Boston", focus="Media, Gaming & Advertising",
    stage="undetermined",
    note="Card-linked offers (Boston). Acquired by Collinson Group (the firm's listing). BCV's 2011 round is not named."))
L.append(cls("linkedin", country="US", country_src="model_knowledge", city="Sunnyvale", rng="below_1b", focus="Consumer & Marketplaces",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=CCPAGE("/portfolio/company/linkedin"), entry_date="2008",
    note="Professional network (Sunnyvale). 'In 2008, Bain Capital Ventures and our affiliates provided a substantial investment to LinkedIn' "
         "(the firm's own company page, 2012 capture): the $53M Series D of June 2008 that BCV led. IPO 2011; Microsoft bought it in 2016."))
L.append(cls("logicsource", status="private", rng="below_1b", city="Norwalk", focus="SaaS",
    note="Procurement services (Norwalk, CT); FTV Capital invested $180M in 2022 (WSJ). Operating; entry from the filings (2009)."))
L.append(cls("magicschool", status="private", rng="below_1b", city="Denver", focus="AI & Applied AI",
    note="AI tools for teachers (Denver). BCV led the $15M Series A (the firm's post, 2024-06-27), as the filings give."))
L.append(cls("manicube-elizabeth-arden-red-door", status="acquired", rng="below_1b", country="US", country_src="model_knowledge",
    city="New York", focus="Consumer & Marketplaces", stage="undetermined",
    note="Office manicure service (New York). Acquired by Elizabeth Arden Red Door Spas (the firm's listing). BCV's 2014 round is not named."))
L.append(cls("material-bank", status="private", rng="1b_plus", country="US", country_src="model_knowledge", city="Boca Raton",
    focus="Consumer & Marketplaces", usd=1900000000, val_src="web_verified", asof="2022-05-09",
    val_cite=NEWS("material-bank", "now valued at $1.9B"), extra={"valuation_range_source": "web_verified"},
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-rise-of-the-b2b-marketplace"), entry_date="2020-04",
    flags=["stale"],
    note="Materials-sample marketplace (Boca Raton, FL; the firm lists New York). 'We are leading a Series B investment in Material Bank' "
         "(the firm's post, 2020-04-30). Mark: the $175M round of May 2022 at $1.9B (Refresh Miami); stale beyond 24 months."))
L.append(cls("mathison", status="private", rng="below_1b", city="Los Angeles", focus="SaaS", stage="undetermined",
    note="Diversity hiring software (Los Angeles). BCV's archive lists it from 2021 (Sarah Smith); the 2022 filing is in a company incorporated "
         "in 2017, so the band is withheld and the round is not named."))
L.append(cls("medeanalytics-jll-partners", status="acquired", rng="below_1b", city="Emeryville", focus="Healthcare & Bio",
    note="Healthcare analytics (Emeryville). BCV listed it from 2008 under 'Expansion/Growth Buyout'; JLL Partners acquired it (the firm's "
         "listing). Entry taken from the filings as Growth."))
L.append(cls("medhok-hearst-communications", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Tampa",
    focus="Healthcare & Bio", stage="Growth", stage_src="model", stage_conf="medium",
    note="Care-management software (Tampa). Acquired by Hearst (the firm's listing). The firm's WordPress-era page tags the 2013 entry "
         "'Growth' (a field not scored for labelling), read as a growth round."))
L.append(cls("media-radar", status="acquired", rng="below_1b", city="New York", focus="Media, Gaming & Advertising", stage="undetermined",
    note="Ad sales intelligence (MediaRadar, New York); the firm lists it as Acquired. BCV's listing gives 2008, six years before the 2014 "
         "filing the band read, so the band is withheld; the round is not named."))
L.append(cls("memento", status="acquired", rng="below_1b", city="Concord", focus="Fintech & Payments", stage="undetermined",
    note="Fraud management for banks (Concord, MA). 'Acquired by FIS' (the firm's archive). BCV listed it from 2006; the round is not named."))
L.append(cls("mirakl", city="Paris", stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=POST("the-mirakl-of-marketplaces"),
    entry_date="2019-02",
    note="Marketplace software (Paris). 'We are joining forces with Mirakl to lead its $70 million Series C' (the firm's post, 2019-02-28); "
         "'BCV first invested in Mirakl in 2019'."))
L.append(cls("moov-financial", status="private", rng="below_1b", city="Cedar Falls", focus="Fintech & Payments",
    stage="Seed", **site_stage("moov-financial"), entry_date="2019", flags=["stage_disputes_band"],
    grad="graduated", grad_src="web_verified", grad_conf="high", grad_cite=NEWS("moov-financial", "Secures $45M in Series B"),
    note="Payments infrastructure (Cedar Falls, IA). BCV's listing: 2019, Seed; the first partner-anchored Form D (2020) is a later round. "
         "The $45M Series B of January 2023 graduates the seed.",
    rounds=[rnd("2023-01", "Series B", 45000000, "Commerce Ventures", None, NEWS("moov-financial", "Secures $45M in Series B"), "press")]))
L.append(cls("moveworks-servicenow", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Mountain View",
    focus="AI & Applied AI", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=POST("moveworks-moves-work"),
    entry_date="2019",
    note="AI assistant for enterprise IT (Mountain View). 'When Bain Capital Ventures led Moveworks' Series A in 2019' (the firm's post, "
         "2025-02-24; the listing's 2017 is earlier than any named round). ServiceNow bought Moveworks for $2.85B, closing in December 2025."))
L.append(cls("mparticle", status="acquired", rng="below_1b", city="New York", focus="Data Infrastructure",
    stage="Growth", stage_src="web_verified", stage_conf="high", stage_cite=NEWS("mparticle", "Leads MParticle"), entry_date="2016-10",
    note="Customer data platform (New York). 'Bain Capital Ventures Leads mParticle's $17.5M Series B' (WSJ, 2016-10-13). Rokt acquired it "
         "in January 2025."))
L.append(cls("myedu", status="acquired", rng="below_1b", country="US", country_src="model_knowledge", city="Austin",
    focus="Consumer & Marketplaces",
    note="College planning platform (Austin). Acquired by Blackboard in 2014 (the firm lists it as Acquired). Graduation left for the "
         "graduation pass."))
L.append(cls("nanosphere", country="US", country_src="model_knowledge", city="Northbrook", rng="below_1b", focus="Healthcare & Bio",
    stage="undetermined",
    note="Molecular diagnostics (Northbrook, IL). Bain Capital Venture Fund 2005 was a pre-IPO holder (its 2007 S-1); IPO November 2007; "
         "Luminex bought it in 2016. The round is not named."))
L.append(cls("national-cardiovascular-partners-fresenius-medical-care", status="acquired", rng="below_1b", country="US",
    country_src="model_knowledge", city="Houston", focus="Healthcare & Bio", stage="undetermined",
    note="Outpatient cardiology and vascular centres (Houston). Acquired by Fresenius Medical Care (the firm's listing). BCV's listing gives "
         "2012; whether the position was a minority round is not established and the round is not named."))

if __name__ == "__main__":
    jl.write("batch-003", L)
