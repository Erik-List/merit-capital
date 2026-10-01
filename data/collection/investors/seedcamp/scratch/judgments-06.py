"""PRO-83 grind, batch-006 (repositive .. sweatcoin)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, pc, sc, rnd, V = jl.c, jl.loc, jl.pc, jl.sc, jl.rnd, jl.V
EXIT = "the firm's list marks it exited"
CH = "https://find-and-update.company-information.service.gov.uk/company/"


def fp(slug, stage, url, date, country, city, **kw):
    return c(slug, stage=stage, stage_src="first_party", stage_cite=V + url, stage_conf="high", entry_date=date,
             **loc(country, city), **kw)


def und(slug, year, country, city, note, **kw):
    return c(slug, stage="undetermined", entry_date=str(year), **loc(country, city), note=note, **kw)


L = []
L.append(pc("repositive", "Repositive", "GB", "Cambridge", status="defunct", rng="below_1b", focus="Healthcare & Bio",
    note="Genomic data access platform; REPOSITIVE LIMITED (08820538) dissolved 2024-09-05 (Companies House), the domain is for sale"))
L.append(c("rerun", status="private", **loc("SE", "Stockholm"), rng="below_1b", focus="DevTools & APIs",
    stage="Pre-Seed", stage_src="model", stage_conf="medium", entry_date="2022-06-21",
    note="Data layer for physical AI (visualisation for computer vision); the firm's post of 2022-06-21 announces the $3.2M round it backed (the June 2022 pre-seed); TechCrunch calls the $17M round of Mar 2025 its seed"))
L.append(und("resistant-ai", 2019, "CZ", "Prague", status="private", rng="below_1b", focus="Security",
    note="AI document fraud detection for financial services; $25M Series B Oct 2025 (SecurityWeek); the 2019 entry round is not named"))
L.append(pc("revision-app", "Revision App", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Mobile revision app by teachers (2013); the related UK entities are dissolved and the site is blank"))
L.append(c("revolut", prog_at="2015-02", cohort=jl.coh("Revolut")["url"], status="private",
    **loc("GB", "London", "https://seedcamp.com/views/seedcamp-family-grows-to-over-150-as-11-new-startups-join/"),
    rng="100b_plus", usd=115000000000, val_src="web_verified", asof="2026-07-22",
    val_cite="https://www.bloomberg.com/news/articles/2026-07-22/revolut-confirms-115-billion-valuation-in-secondary-share-sale",
    focus="Fintech & Payments", flags=["model_disputes_source"],
    note="Digital bank; joined from Seedcamp Week London Feb 2015 on the programme deal ('we wrote their first check before doubling down alongside Balderton', the firm's post of 2025-11-24); seed of Jul 2015 led by Balderton; marked at the company-run secondary of Jul 2026 at $115B (Bloomberg), as in the Balderton and Point Nine books; last primary the 2021 Series E at $33B; the pre-filled LT is the Lithuanian bank entity"))
L.append(pc("rialto", "Rialto", "GB", "London", status="private", rng="below_1b", focus="SaaS", flags=["model_disputes_source"],
    note="Leasing and portfolio software for commercial landlords (rial.to, live); the pre-filled NL is a name collision"))
L.append(und("risk-ledger", 2018, "GB", "London", status="private", rng="below_1b", focus="Security",
    note="Supply-chain security network; GBP 2.1M 2021 (Forbes), GBP 24M Series B Jul 2026; the 2018 entry round is not named"))
L.append(und("rollee", 2021, "FR", "Paris", status="private", rng="below_1b", focus="DevTools & APIs",
    note="Employment and income data API; site live; the 2021 entry round is not named"))
L.append(und("rosita", 2020, "ES", "Madrid", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Longevity coaching app for over-60s; rositalongevity.com does not answer; the 2020 entry round is not named"))
L.append(und("rossum", 2019, "CZ", "Prague", status="acquired", rng="below_1b", focus="AI & Applied AI", flags=["model_disputes_source"],
    note="AI document processing; $100M Series A led by General Catalyst Oct 2021; acq. by Coupa, May 2026 (FinTech Futures); the pre-filled GB is its UK entity; the 2019 entry round is not named"))
L.append(pc("saberr", "Saberr", "GB", "London", status="defunct", rng="below_1b", focus="SaaS",
    note="Team-building and hiring analytics; SABERR LIMITED (08388093) dissolved 2025-02-14 (Companies House)"))
L.append(und("salv", 2019, "EE", "Tallinn", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Anti-money-laundering platform with intelligence sharing; EUR 1.5M 2020, EUR 4M 2023; the 2019 entry round is not named"))
L.append(fp("sano", "Seed", "sano-raises-500000-to-make-personalised-medicine-a-reality/", "2019-04-09", "GB", "Cambridge",
    status="private", rng="below_1b", focus="Healthcare & Bio", flags=["model_disputes_source"],
    note="Sano Genetics, genetic research participant platform; the firm's post of 2019-04-09: 'thrilled to back ... as they close GBP 500,000 seed funding'; $11.4M 2024; the pre-filled US is a name collision"))
L.append(pc("satago", "Satago", "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note=f"Credit control and invoice finance for SMBs; acq. by Oxygen Finance, Feb 2017 (the firm's /acquirer/oxygen-finance page); {EXIT}"))
L.append(pc("sayduck", "SayDuck", "FI", "Helsinki", status="acquired", rng="below_1b", focus="SaaS",
    note="3D and AR product visualisation; acq. by Bublar Group, Jul 2019 (Cision)"))
L.append(c("scoville", prog_at="2009", **loc("GB", "London"), status="acquired", rng="below_1b", focus="Consumer & Marketplaces", stage_conf="medium",
    note="'A Flipboard for Places' (Mobile, London, per the firm's 2014 company page); acq. by Rundavoo (the same page); the live list gives 2009 and the firm's 2012-2014 lists carry it; "
         + "a Fund II-era entry on the programme's standard cheque (decisions.md D3)"))
L.append(und("seedlegals", 2017, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Legal automation for startup fundraising; site live; the 2017 entry round is not named"))
L.append(pc("server-density", "Server Density", "GB", "London", status="acquired", rng="below_1b", focus="DevTools & APIs",
    note="Server monitoring (Boxed Ice, Birmingham; Seedcamp Week 2009 winner); acq. by StackPath, 2018; SERVER DENSITY LIMITED dissolved Feb 2026"))
L.append(pc("sharelatex", "ShareLaTeX", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note=f"Online collaborative LaTeX editor; merged into Overleaf, 2017 (the firm's /acquirer/overleaf page; sharelatex.com redirects to Overleaf); {EXIT}"))
L.append(pc("shoprocket", "Shoprocket", "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Embeddable e-commerce; site live"))
L.append(fp("sikoia", "Pre-Seed", "our-investment-in-sikoias-2-3m-seed-round-to-cut-through-the-noise-in-fintech-with-a-plug-and-play-data-and-api-platform/",
    "2021-08-31", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Customer verification data platform for financial services; the firm's post of 2021-08-31: 'Our investment in Sikoia's $2.3M pre-seed round'; $6M 2023 (Finextra)"))
L.append(pc("simpletax", "SimpleTax", "GB", "London", status="acquired", rng="below_1b", focus="Fintech & Payments",
    note=f"UK self-assessment tax software (gosimpletax.com); {EXIT} (2018-2021, acquirer not named there); the Canadian SimpleTax bought by Wealthsimple in 2019 is a namesake"))
L.append(fp("skew", "Seed", "skew-raises-2m-to-reinvent-capital-markets/", "2019-09-27", "GB", "London",
    status="acquired", rng="below_1b", focus="Crypto & Web3",
    note="Crypto derivatives analytics; the firm's post of 2019-09-27: 'delighted to invest in London-based startup Skew ... as they close a $2M seed round led by ... FirstMinute Capital'; acq. by Coinbase, Apr 2021"))
L.append(pc("smartward", "SmartWard", "GB", "London", status="unknown", rng="below_1b", focus="Healthcare & Bio",
    note="Hospital ward management app (Seedcamp Week Berlin 2013); no later trace found"))
for s in ("audiense", "socialbro"):
    L.append(pc(s, "SocialBro", "GB", "London", status="private", rng="below_1b", focus="Media, Gaming & Advertising",
        note="SocialBro (Barcelona; Seedcamp Barcelona 2011), renamed Audiense in 2016, audience intelligence (London and Barcelona)"
             + ("" if s == "audiense" else "; duplicate of audiense (identity-merges.json)")))
L.append(c("sorare", status="private", **loc("FR", "Paris"), focus="Crypto & Web3", stage="undetermined", entry_date="2019-05-15",
    note="Fantasy football with digital cards; the firm's post of 2019-05-15 names Sorare 'our latest investment' in a round of 'over EUR 500k' without a round word; $680M Series B at $4.3B Sep 2021; a new round from existing investors 2026 (Maddyness); the mark is pinned in the A/B pass",
    rounds=[rnd("2019-05-15", None, None, None, True, V + "sorare-raises-over-e500k-to-transform-the-beautiful-game-into-the-first-mass-blockhain-based-football-game/", "firm")]))
L.append(pc("soup", "Soup", "AT", "Vienna", status="defunct", rng="below_1b", focus="Media, Gaming & Advertising",
    note="soup.io microblogging (Seedcamp Week 2008 winner; 'received an investment during Seedcamp 2008', Wikipedia); the service shut down in 2020"))
L.append(pc("sparkeo", "Sparkeo", "IL", "Tel Aviv", status="unknown", rng="below_1b", focus="Media, Gaming & Advertising",
    note="Video monetisation for experts (Seedcamp Week 2010 winner); no later trace found"))
L.append(und("speechly", 2018, "FI", "Helsinki", status="acquired", rng="below_1b", focus="AI & Applied AI",
    note="Spoken-language understanding API; acq. by Roblox, Sep 2023 (TechCrunch); the 2018 entry round is not named"))
L.append(fp("spill", "Seed", "our-investment-in-spill-out-to-make-therapy-a-default-workplace-benefit/", "2019-03-07", "GB", "London",
    status="private", rng="below_1b", focus="Healthcare & Bio", flags=["model_disputes_source"],
    note="Workplace therapy app (EAP); the firm's post of 2019-03-07: 'thrilled to invest in Spill ... as part of their GBP 650,000 seed round alongside Passion Capital'; the pre-filled US is a name collision"))
L.append(sc("spoke", "Spoke", "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Made-to-fit menswear; on the firm's Fund III seed list (2015-09-21); site live"))
L.append(pc("sportlyzer", "Sportlyzer", "EE", "Tallinn", status="private", rng="below_1b", focus="SaaS",
    note="Team management for youth and amateur sports (Mini Seedcamp Ljubljana 2011); site live"))
L.append(pc("spreddit", "Spreddit", "GB", "London", status="unknown", rng="below_1b", focus="Fintech & Payments",
    note="Interest-free instalments for online shoppers (2013); no later trace found"))
L.append(pc("squadmail", "SquadMail", "DE", "Berlin", status="unknown", rng="below_1b", focus="SaaS",
    note="Shared email folders (Seedcamp Week Berlin 2013); no later trace found"))
L.append(pc("stamplay", "Stamplay", "GB", "London", status="acquired", rng="below_1b", focus="DevTools & APIs",
    note=f"API integration platform (Italian founders, London); acq. by Claris (Apple), 2019 (stamplay.com now redirects to Claris); {EXIT} (2020-2023)"))
L.append(fp("stepladder", "Pre-Seed", "introducing-stepladder-the-collaborative-solution-to-get-first-time-buyers-on-the-property-ladder/",
    "2018-03-15", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Collaborative savings circles for home deposits; the firm's post of 2018-03-15: 'We're thrilled to lead their GBP 250,000 pre-seed round'; site live"))
L.append(und("stotles", 2019, "GB", "London", status="private", rng="below_1b", focus="SaaS",
    note="Public-sector sales intelligence; the firm's post of 2019-11-06 calls it 'This first round of funding' without a round word; GBP 9.6M Series A led by Headline May 2025"))
L.append(pc("stowga", "Stowga", "GB", "London", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Pay-as-you-go warehousing marketplace (January 2017 cohort); stowga.com does not answer"))
L.append(fp("studentfinance", "Seed", "studentfinance-raises-a-e1-15m-to-reshape-education-financing-through-ai-powered-isas/",
    "2019-12-03", "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Income-share tuition financing (Lisbon and London); the firm's post of 2019-12-03: 'We're thrilled to invest in their seed round' (EUR 1.15m); EUR 39M Series A 2023"))
L.append(pc("stupeflix", "stupeflix", "FR", "Paris", status="acquired", rng="below_1b", focus="Media, Gaming & Advertising",
    note=f"Online video creation (Seedcamp Week 2008 winner); acq. by GoPro, 2016 (the firm's /acquirer/gopro page); {EXIT}"))
L.append(pc("sunlight", "Sunlight", "GB", "London", status="unknown", rng="below_1b", focus="SaaS",
    note="Employee learning wallet and marketplace (2016); sunlight.is does not answer"))
L.append(und("superscript", 2018, "GB", "London", status="private", rng="below_1b", focus="Fintech & Payments",
    note="Insurance for digital businesses; $10M 2021 backed by Seedcamp (Business Insider), GBP 45M Series B Jan 2023; the 2018 entry round is not named"))
L.append(und("surfboard", "2021", "GB", "London", status="acquired", rng="below_1b", focus="SaaS",
    note="Workforce management for support teams; 'since we wrote their first cheque in early 2021' (the firm's post of 2022-11-21, no round word); $5M 2022 (Speedinvest); acq. by Dialpad, Oct 2024 (Tech.eu)"))
L.append(pc("sush-io", "Sush.io", "FR", "Paris", status="unknown", rng="below_1b", focus="Consumer & Marketplaces",
    note="Joined from Seedcamp Paris 2011 (the firm's 2012 post); no later trace found"))
L.append(fp("sweatcoin", "Seed", "our-investment-in-sweatcoin-the-new-digital-currency-powered-by-physical-movement/", "2018-01-17",
    "GB", "London", status="private", rng="below_1b", focus="Consumer & Marketplaces",
    note="Rewards for walking; the firm's post of 2018-01-17: 'our first investment of 2018 in Sweatcoin as part of their $5,7m Seed round' (Tech.eu)"))

if __name__ == "__main__":
    jl.write("batch-006", L)
