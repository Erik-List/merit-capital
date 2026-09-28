#!/usr/bin/env python3
"""Membership pass 1 (PRO-161): the 18 Form D-only rows the queue asks about, and
the site-listed rows a standing test puts out (D2 token rule, D4/T3 public
positions). Every basis names the test and the fact."""
from judge_lib import verdict, write, SITE, ARCH, LISTING

F13 = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1836733&type=13F-HR"
MELI4 = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1571355&type=4"


def fd(slug, why, conf="high"):
    return verdict(slug, "not_member", why, ec="formd_adjudicated", conf=conf)


L = [
    # ---- D2: base-layer assets (Erik's a16z ruling 7)
    verdict("bitcoin", "not_member",
            "Listed on the Rebels list with founder 'Satoshi Nakamoto' and no company link: a base-layer asset with no "
            "issuing organisation, held through the treasury vehicle Ribbit BTC Holdings, LP (ADV Section 7.B). Token rule "
            "(COLLECTION.md s1; Erik's a16z ruling 7: Bitcoin out); decisions.md D2.", cite=SITE("bitcoin")),
    verdict("ethereum", "not_member",
            "Listed (Rebels list; archived Our Bets page 2022-2025 linking ethereum.org): a protocol asset with no "
            "investable issuing entity. Erik's a16z ruling 7 (2026-08-30) put Ethereum out; decisions.md D2.",
            cite=SITE("ethereum")),
    # ---- D4 / T3: positions in companies already listed on an exchange
    verdict("mercado-libre", "not_member",
            "Listed by the firm, but MercadoLibre has traded on Nasdaq since August 2007, five years before Ribbit's "
            "first fund (2012), so no Ribbit fund could enter it through a venture round. The record shows two "
            "non-venture ties: Meyer Malka's own board seat (Forms 3, 4 and 5 he filed personally, 2013-2020; T4, a "
            "person's filing locates the person) and the adviser's 13F holding of MELI from 2023 (a public-market "
            "position, T3). Post-listing public purchase with no venture entry: out.", cite=F13),
    verdict("sea", "not_member",
            "Listed on the archived Our Bets page 2022-2025 (sea.com, Singapore), but Sea Limited listed on the NYSE in "
            "October 2017 and the adviser's 13F carries SEA from 2023; no source names Ribbit in a Sea private round. "
            "A position first appearing as a public-market holding is out (T3; decisions.md D4).", cite=F13),
    verdict("futu", "not_member",
            "Listed on the archived Our Bets page from 2022 (futuholdings.com) and on the Rebels list, but Futu Holdings "
            "listed on Nasdaq in March 2019 and no filing, prospectus or press item names Ribbit in a Futu private round "
            "(the EDGAR full-text sweep of every Ribbit entity name returns no Futu document). First Ribbit sighting "
            "three years after the IPO: a public-market position, out under T3 (decisions.md D4).", conf="medium",
            cite=ARCH("futu")),
    verdict("tinkoff", "not_member",
            "Listed on the archived Our Bets page in 2022 only (tinkoff.ru, Russia), but TCS Group (Tinkoff) has been "
            "listed in London since October 2013 and no source names Ribbit in a private round. A public-market "
            "position, out under T3 (decisions.md D4).", conf="medium", cite=ARCH("tinkoff")),
    # ---- Form D-only rows: personal, founder and namesake seats (T2, T4; Erik 2026-09-28 on BCV)
    fd("craize-snacks-inc",
       "Meyer Malka is a director on Craize Snacks' 2024 Form D (a Miami snack maker); no round, post or listing names a "
       "Ribbit fund, and the firm has never listed it. A partner's board seat alone is not a verified venture "
       "investment (Erik, 2026-09-28): a personal position (T2, T4)."),
    fd("lemon-inc",
       "Lemon, Inc. (Lemon Wallet, Wences Casares's company, sold to LifeLock in 2013) filed a $5M Form D in 2012 with "
       "Meyer Malka as director and Cynthia McAdam as an executive officer, at 364 University Ave, the firm's own "
       "address. No round announcement, post or listing names a Ribbit fund (the firm's 2012-2014 Bets pages never "
       "listed Lemon), so the seat is unverified as a fund position (Erik, 2026-09-28: board seat alone is out).",
       conf="medium"),
    fd("osix-corp",
       "OSIX Corp (Woodside, then Redwood City; officers Cary and Staci Cole) filed in 2011 and 2012 with Meyer Malka as "
       "director; the first filing predates Ribbit's first fund (Form D 2012-Q2), and nothing ties a Ribbit fund to "
       "either round. A personal seat (T2, T4)."),
    fd("brellium-inc",
       "Zachary Rosen is an executive officer and director of Brellium (New York) on its 2024 Form D: the issuer's own "
       "officer, not a Ribbit seat. Brellium's 2025 Series A press names no Ribbit fund (T4)."),
    fd("pantheon-systems-inc",
       "Zachary Rosen co-founded Pantheon Systems; the 2010-2019 Form Ds list him as the issuer's own officer, years "
       "before he appears on Ribbit's team page (2023). A founder's own company is not a firm position (T4)."),
    fd("mission-bicycles-inc",
       "Zachary Rosen is Mission Bicycles' executive officer on its 2011 Form D (San Francisco): the issuer's own "
       "officer, a decade before his Ribbit tenure (T4)."),
    fd("polyops-inc",
       "Manav Kohli is PolyOps' executive officer and promoter on its 2020, 2021 and 2025 Form Ds: his own company, "
       "before he appears on Ribbit's team page (2026). Not a firm position (T4)."),
    fd("guarnerix-inc",
       "Matthew Wong is Guarnerix's executive officer and promoter (New York, with Lisa Wong) on its 2015-2019 Form Ds: "
       "a namesake or the person's own company, before Matt Wong appears on Ribbit's team page (2023) (T4)."),
    fd("green-central-holdings-inc",
       "Matched on 'Nancy Nguyen', a 2011 related person; no Ribbit team member carries that name. Namesake noise."),
    fd("nexalin-technology-inc",
       "Matched on 'Nancy Nguyen', a 2011 related person of a medical-device issuer; no Ribbit team member carries that "
       "name. Namesake noise."),
    fd("kalobios-pharmaceuticals-inc",
       "Denise Gilbert is a director of KaloBios Pharmaceuticals (South San Francisco) on its 2012 Form D: a personal "
       "directorship at a listed biotech, no Ribbit fund named (T4)."),
    fd("maitri-holdings-llc",
       "Jessica Brooks is Maitri Holdings' executive officer in Pittsburgh on its 2022 Form D: a namesake of Ribbit's "
       "chief compliance officer (T4)."),
    fd("pest-force-llc",
       "Nicholas Huber is Pest Force's executive officer (St. George, Utah) on its 2025 Form D: the self-storage and "
       "pest-control operator of that name, not Ribbit's former Nick Huber (namesake; T4)."),
    fd("smwr-t1-llc",
       "Nicholas Huber is the promoter of SMWR T1 LLC (Athens, Georgia), a 2024 real-estate vehicle of the "
       "self-storage operator of that name, not Ribbit's former Nick Huber (namesake; T4)."),
    fd("smwr-t2-llc",
       "Nicholas Huber is the promoter of SMWR T2 LLC (Athens, Georgia), a 2024 real-estate vehicle of the "
       "self-storage operator of that name (namesake; T4)."),
    fd("harbor-national-inc",
       "Nick Shalek is a director of Harbor National, Inc. (New York insurance startup, officers Luke Cohler and "
       "Michael Rudoy) on its 2016 Form D; the firm never listed it and no round or press item names a Ribbit fund. A "
       "partner's board seat alone is not a verified venture investment (Erik, 2026-09-28).", conf="medium"),
    # ---- a second legal entity of a listed member
    verdict("ibod-company-inc", "member",
            "IBOD Company, Inc. is Root Insurance's original legal entity (Columbus, Ohio; Alexander Timm and Dan "
            "Manges its officers, Nick Shalek a director) on its 2018 Form D. Root is on the firm's list (ROOT); the row "
            "folds into root at the rebuild (identity-merges.json).", ec="formd_adjudicated"),
]
write("members-1", L)
