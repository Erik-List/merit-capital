# Batch 5 (19 rows): the filings-only name-match cluster, judged person by person (COLLECTION.md 3), 2026-09-29.
T4 = ("Name-match on a Form D with no growth-fund evidence: the filing predates the partner's time at ICONIQ, so the seat was his "
      "earlier firm's (T4: a seat is dated against the person's firm at filing time).")
HOMONYM = ("Name-match only: no ICONIQ listing, post, fund filing or press ties this issuer to the firm, and the issuer (its place, "
           "sector and stage) does not fit the growth desk. A name-match never suffices alone; unsupported, it is not_member (COLLECTION.md 1).")
PEPPER = " Doug Pepper was a partner at InterWest Partners (to 2014) and Shasta Ventures before joining ICONIQ Growth around 2020."
J = [
 dict(s="bronco-1-2-joint-venture", m="not_member", me="formd_adjudicated", mb=HOMONYM + " 'Bill Griffith' on an oil and gas joint venture in Dallas (2016) is not Will Griffith of ICONIQ."),
 dict(s="circle-pharma-inc", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A San Francisco biotech seed (2016); the Matthew Jacobson on it is a namesake or a personal seat."),
 dict(s="diameter-credit-co", m="not_member", me="fund_filing", mconf="high", mc="https://www.sec.gov/Archives/edgar/data/1916099/000119312524026841/d547408d1012ga.htm",
      mb="Not an operating company (T5): Diameter Credit Company is a closed-end credit fund; ICONIQ Capital, LLC's 20.9% (its 2024 registration statement) and later 13G stakes are client-platform allocations reported by the umbrella adviser (decisions.md D2)."),
 dict(s="doximity-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2011."),
 dict(s="flurry-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " These filings run from 2009 to 2014."),
 dict(s="good-bad-ugly-llc", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A Portland, Oregon seed of 2016."),
 dict(s="gravy-analytics-inc", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A location-data company in Sterling, Virginia (2018)."),
 dict(s="invidi-technologies-corp", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2010."),
 dict(s="libremax-asset-backed-income-fund", m="not_member", me="fund_filing", mconf="high", mc="https://www.sec.gov/Archives/edgar/data/2074612/000101143826000261/primary_doc.xml",
      mb="Not an operating company (T5): LibreMax Asset-Backed Income Fund is a registered credit fund; ICONIQ Capital, LLC's 49.4% (Schedule 13D of 2026-05-04) is a client-platform allocation reported by the umbrella adviser (decisions.md D2)."),
 dict(s="marketo-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2010."),
 dict(s="medallia-inc", m="not_member", me="formd_adjudicated", mb="Rob Bernshteyn's independent directorship at Medallia (2019) was personal and from his years as Coupa's chief executive; he joined ICONIQ Growth in 2024 (decisions.md D8, T4). No ICONIQ listing or fund filing names Medallia."),
 dict(s="newscred-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2014."),
 dict(s="nine-square-therapeutics-inc", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A New York biotech of 2020."),
 dict(s="oxford-county-telephone-telegraph-co", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A telephone company in Lewiston, Maine (2012)."),
 dict(s="sls-breeze-holdings-inc", m="not_member", mx="control_position", me="formd_adjudicated", mconf="high", mc="https://www.sec.gov/Archives/edgar/data/1666134/000095012316014567/filename10.htm",
      mb="SLS Breeze Holdings, Inc. is BlackLine, Inc. under its name at the September 2013 acquisition ('BlackLine, Inc. (f/k/a SLS Breeze Holdings, Inc.)', the draft S-1's exhibits); its $200M Form D is Silver Lake's and ICONIQ's control investment, out as a control position with the BlackLine row (ruling R1)."),
 dict(s="spredfast-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2011."),
 dict(s="tapjoy-inc", m="not_member", me="formd_adjudicated", mb=T4 + PEPPER + " This filing is from 2011."),
 dict(s="the-people-s-movement-inc", m="not_member", me="formd_adjudicated", mb=HOMONYM + " A Solana Beach, California seed of 2013."),
 dict(s="xylos-corp", m="not_member", me="formd_adjudicated", mb=T4 + " Seth Pierrepont joined ICONIQ Growth from Accel in 2022; this filing is from 2010."),
]
