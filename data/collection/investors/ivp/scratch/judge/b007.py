from jl import *
L=[]; V=[]
def row(slug, **k):
    d={"slug":slug}
    for x in k.pop("parts",[]): d.update(x)
    d.update(k); L.append(d)
def old(slug, city_, st="acquired", note="", cc_="US", conf="high", **extra):
    parts=[]
    if cc_: parts.append(country(cc_))
    if city_: parts.append(city(city_,"model_knowledge",conf))
    parts.append(stage("undetermined","model",None,"low"))
    row(slug, status=st, parts=parts, valuation_range="below_1b", note=note, **extra)
def v(slug, verdict, cls, conf, basis, cite=None):
    d={"slug":slug,"verdict":verdict,"evidence_class":cls,"confidence":conf,"who":"agent","basis":basis}
    if cite: d["citation"]=cite
    V.append(d)
FD="https://www.sec.gov/Archives/edgar/data/"
# ---- membership (Form D name-matches)
v("coverhound-inc","not_member","formd_adjudicated","high","T4 seat dating: Tom Loverro's 2013 director seat predates his IVP tenure (he joined IVP in 2015 per the firm's own news); no IVP listing, fund filing or announcement names CoverHound.")
v("creative-market-labs-inc","not_member","formd_adjudicated","high","T4: Cack Wilhelm's 2018 seat predates her IVP tenure (first on IVP's site in 2020, on its fund Form Ds from 2022); a prior-firm deal. Pre-registered trap.")
v("elder-technologies-inc","member","formd_adjudicated","high","Elder Technologies, Inc. is Sage (hellosage.com), whose $35M Series B IVP led (IVP post 2024-12-05); Eric Liaw, the deal partner on IVP's Sage page, is director of record on the 2024 and 2026 filings. Same investment as the sage row: merge recorded.", "https://www.ivp.com/content/sage-bringing-caregiving-into-the-21st-century/")
v("energy-power-solutions-inc","not_member","formd_adjudicated","high","'Jim Newell' homonym: the Houston energy investor (Houston Ventures / SMH Private Equity), not IVP's James Newell (on IVP's site 2013-2016). Pre-registered trap.")
v("exclusive-resorts-llc","member","formd_adjudicated","medium","Director-of-record pattern: Todd Chaffee, an IVP managing director in tenure (on IVP's fund Form Ds 2010-2020), is director of record on Exclusive Resorts LLC's 2009 Form D ($6.7M sold), and the issuer resolves to a real operating company (the Denver luxury destination club). No IVP listing names it: an unannounced position, flagged for the A/B pass.")
v("fieldlevel-inc","not_member","formd_adjudicated","high","Reid Dennis's personal seat on FieldLevel's 2017 filings, decades into his emeritus years, with no IVP fund, listing or announcement (T2, T4). Pre-registered trap.")
v("liquidframeworks-inc","not_member","formd_adjudicated","high","'James Newell' homonym (Houston Ventures). Pre-registered trap.")
v("oseberg-inc","not_member","formd_adjudicated","high","'James Newell' homonym (Houston Ventures / Oklahoma City issuer). Pre-registered trap.")
v("renaissance-lighting-inc","not_member","formd_adjudicated","high","'James / Jim Newell' homonym, 2009 energy filings, before IVP's James Newell appears on IVP's site. Pre-registered trap.")
v("safecorp-financial-corp","member","formd_adjudicated","high","SafeCorp Financial Corporation (Redwood City, incorporated 2009) was Personal Capital's original legal name; Steve Harrick, IVP's deal partner on Personal Capital, is director of record on its 2010 Form D. Same investment as the personal-capital row: merge recorded.", "https://www.ivp.com/portfolio/personal-capital/")
v("snyk-ltd","not_member","formd_adjudicated","high","T4: Tamar Yehoshua's Snyk seat (2021-2022 filings) is an independent directorship held before she joined IVP as a venture partner; IVP has no Snyk listing, fund filing or announcement.")
v("southwest-windpower-inc","not_member","formd_adjudicated","high","'Jim Newell' homonym (the Houston energy investor), 2009. Pre-registered trap.")
v("spekit-inc","not_member","formd_adjudicated","high","Roseanne Wincek left IVP in 2019 to co-found Renegade Partners; Spekit's 2022 filing is a Renegade seat (T4). Pre-registered trap.")
v("spinez","not_member","formd_adjudicated","high","'Kevin Egan' on SpineZ's 2013 Form D is an executive officer of the Atlanta medical-device issuer, an operator homonym, not IVP's Kevin Egan (a venture partner who joined IVP recently); no IVP evidence.")
# ---- classification
row("elder-technologies-inc", status="private", parts=[city("New York")], valuation_range="below_1b", flags=["identity_conflated"],
    note="Elder Technologies, Inc. is Sage's legal name; the sage row is this company (merge recorded, applies at the rebuild).")
row("exclusive-resorts-llc", status="private", parts=[country("US"), city("Denver")], valuation_range="below_1b", flags=["needs_review"],
    note="Exclusive Resorts, luxury destination club, Denver. Member on the director-of-record pattern (Todd Chaffee, 2009); still operating privately (majority owner Revolution). To be confirmed in the A/B pass.")
row("safecorp-financial-corp", status="acquired", parts=[city("Redwood City")], valuation_range="below_1b", flags=["identity_conflated"],
    note="SafeCorp Financial Corporation was Personal Capital's original legal name; the personal-capital row is this company (merge recorded, applies at the rebuild).")
row("twyla", status="unknown", parts=[country("US"), city("Austin"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Twyla, online art marketplace, Austin TX. IVP's page: Year Invested 2016; last listed by IVP in 2019 and dark since; fate not established. Round not named.")
row("unify", status="acquired", parts=[country("US"), city("Sacramento","model_knowledge","medium"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["identity_homonym"],
    note="Unify Corporation, database tools, Sacramento CA. IPO (UNFY), renamed Daegis in 2010 and sold to Open Text in 2015. Not Battery's or Thrive's 'Unify' rows (different companies). Entry round not on record.")
row("uproxx", status="acquired", parts=[country("US"), city("Culver City"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Uproxx Media Group (formerly Woven Digital), pop-culture publisher, Culver City CA. IVP's page: Year Invested 2014; acquired by Warner Music Group in 2018. The woven row is this company (merge recorded).")
old("varolii","Seattle",note="Varolii (formerly PAR3), outbound communications, Seattle. Acquired by Nuance in 2013. Entry round not on record.")
row("venice", status="private", parts=[stage("Series A","web_verified",post("privileged-access-is-broken-venice-fixes-it"))], valuation_range="below_1b",
    funding_rounds=[rnd("2026-02","Series A",33000000,None,True,post("privileged-access-is-broken-venice-fixes-it"))],
    note="Venice (venice.io), privileged access security. IVP invests in the $33M Series A (IVP post 2026-02-18). Country and city to be placed in the web pass. Not Insight Venture Partners' 'IVP (Venice)' vehicle, which is external.")
old("verisity","Mountain View",conf="medium",note="Verisity, chip verification software, Mountain View CA. IPO 2001; acquired by Cadence in 2005. Entry round not on record.")
row("vessel", status="acquired", parts=[city("San Francisco"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Vessel, premium short-form video, San Francisco (Jason Kilar). IVP's page: Year Invested 2015, a round after the 2014 Series A; acquired by Verizon in 2016 and shut down.")
row("walker-company", parts=[city("Palo Alto"), stage("Growth","model",None,"low")], valuation_range="below_1b", flags=["stage_uncited"],
    note="Walker & Company Brands, grooming products, Palo Alto (later Atlanta). IVP's page: Year Invested 2014, a round after a16z's Series A; acquired by Procter & Gamble in 2018.")
old("webex-communications","Santa Clara",conf="medium",note="WebEx, web conferencing, Santa Clara CA. IPO 2000; acquired by Cisco in 2007. On IVP's 2014 list; entry round not on record.")
row("websense", parts=[country("US"), city("San Diego"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Websense, web security, San Diego. IPO 2000 (WBSN); taken private by Vista in 2013 (now Forcepoint). Entry round not on record.")
row("whisper", status="unknown", parts=[country("US"), city("San Francisco"), stage("undetermined","model",None,"low")], valuation_range="below_1b", flags=["identity_homonym"],
    note="Whisper.ai, AI hearing aids, San Francisco (Dwight Crow). IVP's page: Year Invested 2020; listed to 2023, then dark; fate not established. Not the anonymous-app Whisper that Sequoia, Thrive and Lightspeed hold (a homonym).")
old("whistle-communications","Foster City",conf="low",note="Whistle Communications, small-business internet appliances, Foster City CA. Acquired by IBM in 1999. Entry round not on record.")
row("wonderful", parts=[country("IL"), city("Tel Aviv"), stage("Series A","web_verified",post("wonderful-agents-for-the-international-enterprise"))], flags=["model_disputes_source"],
    funding_rounds=[rnd("2025-11","Series A",100000000,"IVP (co-lead)",True,post("wonderful-agents-for-the-international-enterprise"))],
    note="Wonderful (wonderful.ai), enterprise AI agents, Tel Aviv. IVP co-leads the Series A (IVP post 2025-11-11). The Wikidata 'Israel/ Netherlands' is not a country code; the unicorn-list mark is left to the A/B pass.")
old("argonaut-technologies-inc","Foster City",conf="medium",note="Argonaut Technologies, chemistry instruments, Foster City CA. IPO 2000; acquired by Biotage in 2005. IVP funds filed 13Gs and Form 4s 2001-2004 (fund filing); entry round not on record.")
old("arthrocare-corp","Austin",conf="medium",note="ArthroCare, surgical devices, Austin TX (Sunnyvale at IPO). IPO 1996; acquired by Smith & Nephew in 2014. IVP funds filed 13Gs 1997-2000; entry round not on record.")
old("aviron","Mountain View",note="Aviron, vaccines (FluMist), Mountain View CA. IPO 1996; acquired by MedImmune in 2002. IVP funds filed 13Gs 1997-1998; entry round not on record.")
old("biopsys-medical-inc","Irvine",conf="medium",note="Biopsys Medical, breast biopsy devices, Irvine CA. IPO 1996; acquired by Johnson & Johnson in 1997. IVP fund 13G 1997; entry round not on record.")
old("cardiac-pathways-corp","Sunnyvale",conf="medium",note="Cardiac Pathways, cardiac ablation, Sunnyvale CA. IPO 1996; acquired by Boston Scientific in 2001. IVP funds filed 13Gs 1997-2000; entry round not on record.")
old("cv-therapeutics-inc","Palo Alto",note="CV Therapeutics, cardiovascular drugs, Palo Alto. IPO 1996; acquired by Gilead in 2009. IVP funds filed 13Gs 1997-1998; entry round not on record.")
old("endosonics-corp","Rancho Cordova",conf="medium",note="EndoSonics, intravascular ultrasound, Rancho Cordova CA. Acquired by Jomed in 2000. IVP fund 13G 1997; entry round not on record.")
old("genta-incorporated-de","Berkeley Heights",st="defunct",conf="medium",note="Genta Incorporated, oncology drugs, Berkeley Heights NJ (San Diego at founding). Filed for Chapter 7 liquidation in 2012: defunct. IVP fund 13G 1998; entry round not on record.")
old("iasiaworks-inc","San Mateo",st="defunct",conf="low",note="iAsiaWorks, Asian data centers, San Mateo CA. IPO 2000; collapsed in 2001-2002. IVP fund 13G 2001; entry round not on record.")
old("igo-corp","Reno",conf="medium",note="iGo (iGo.com), mobile power accessories, Reno NV. IPO 1999 (IGOC); merged into Mobility Electronics in 2002 (which took the iGo name and was bought by Steel Excel in 2013). IVP fund 13G 2000; entry round not on record.")
old("imagyn-medical-inc","Laguna Niguel",st="defunct",conf="low",note="Imagyn Medical, minimally invasive gynecology devices, Laguna Niguel CA. Merged into Urohealth in 1997 (Imagyn Medical Technologies), which went through Chapter 11 in 1998. IVP fund 13G 1997; entry round not on record.")
row("integrated-medical-resources-inc", status="unknown", parts=[country("US"), city("Lenexa","model_knowledge","low"), stage("undetermined","model",None,"low")], valuation_range="below_1b",
    note="Integrated Medical Resources, men's health clinics, Lenexa KS. IPO 1996; fate after the late 1990s not established. IVP fund 13G 1997; entry round not on record.")
old("metra-biosystems-inc","Mountain View",conf="medium",note="Metra Biosystems, bone-disease diagnostics, Mountain View CA. IPO 1995; acquired by Quidel in 1999. IVP fund 13G 1997; entry round not on record.")
old("microcide-pharmaceuticals-inc","Mountain View",st="defunct",conf="medium",note="Microcide Pharmaceuticals, antibiotics, Mountain View CA. IPO 1996; renamed Essential Therapeutics, which filed for bankruptcy in 2003. IVP funds filed 13Gs 1997-1998; entry round not on record.")
old("onyx-pharmaceuticals-inc","South San Francisco",note="Onyx Pharmaceuticals, oncology, South San Francisco. IPO 1996; acquired by Amgen in 2013. IVP funds filed 13Gs 1997-2001; entry round not on record.")
old("pharmacopeia-inc","Princeton",conf="medium",note="Pharmacopeia, combinatorial chemistry, Princeton NJ. IPO 1995; acquired by Ligand in 2008. IVP funds filed 13Gs 1997-1998; entry round not on record.")
old("solta-medical-inc","Hayward",note="Solta Medical (formerly Thermage), aesthetic devices, Hayward CA. IPO 2006; acquired by Valeant in 2014. IVP funds filed Forms 3/4 at the 2006 IPO and 13Gs to 2010, so IVP held pre-IPO shares; entry round not on record.")
old("storm-technology-inc","Mountain View",st="defunct",conf="medium",note="Storm Technology, digital imaging, Mountain View CA. IPO 1996; ceased operations in 1998. IVP funds filed 13Gs 1997-1998; entry round not on record.")
write("../queue/batch-007.out.jsonl", L+V)
