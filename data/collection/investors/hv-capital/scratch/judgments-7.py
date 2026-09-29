"""Batch 7 (PRO-104 grind, pass 1)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, verdict, rnd, write, gn, hq, EXPORT, firm_cite  # noqa: E402

L = []


def geo(slug, city=None, country=None):
    c, ci, cite = hq(slug)
    return dict(country=country or c, country_cite=cite, city=city or ci)


def old(slug, status, note, focus, stage="undetermined", rounds=None, extra=None, **kw):
    g = geo(slug)
    g.update(kw.pop("geo", {}))
    return cls(slug, status=status, rng="below_1b", stage=stage, focus=focus, note=note, rounds=rounds or [],
               extra=extra, **{**g, **kw})


def bare(slug, status, note, focus):
    return cls(slug, status=status, rng="below_1b", stage="undetermined", focus=focus, country="DE",
               country_src="model_knowledge", flags=["city_unknown"], note=note, rounds=[])


ZENMATE = ("https://web.archive.org/web/20141028015617/http://www.holtzbrinck-ventures.com:80/index.php?news_en"
           "&newsdetail=20141002-292_zenmate-scores-32m-series-a-for-its-vpn-style-private-browsing-service")

L.append(old("trustyou", "private", "Hotel reputation and guest-feedback software, Munich (founded 2008). HV entered 2008-04; the "
             "firm's 2011 post reports a $5M financing, and HV's own entry round is not named. Recruit took a majority in "
             "2017; TrustYou bought itself back in 2023 and operates independently.", "SaaS",
             extra={"status_citation": gn("trustyou", "OVNTcFlFbw")}))
L.append(old("tutoria", "unknown", "Tutoring marketplace, Munich (founded 2007). HV entered 2007-05; former portfolio from 2011. "
             "Its later state was not found.", "Consumer & Marketplaces"))
L.append(cls("tzafon", status="private", rng="below_1b", stage="Pre-Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("tzafon", "2tjZ0d6WWM"), entry_date="2025-07", focus="AI & Applied AI", **geo("tzafon"),
             note="AI lab for foundation models and agents, Stockholm (founded 2023). HV's entry (HV Entry 2025) is the $9.7M "
                  "pre-seed of July 2025 (tech.eu, FinSMEs, found by the firm-name search).",
             rounds=[rnd("2025-07-30", "Pre-Seed", 9_700_000, None, True, gn("tzafon", "2tjZ0d6WWM"))]))
L.append(old("urban-sports-club", "acquired", "Multi-sport and fitness membership, Berlin (founded 2012). HV entered 2015 (Fund "
             "VI). acq. by Wellhub (formerly Gympass), 2025 (Handelsblatt; Fitt Insider 2025-03-25); HV's export now files "
             "the position under 'Wellhub', which is not a member (D4). The round is not named.", "Consumer & Marketplaces",
             extra={"status_citation": gn("wellhub", "HNLUE5WZWU")}))
L.append(old("vaha", "acquired", "Interactive home-fitness mirror, Berlin (founded 2019). HV entered 2019-05-24; the round is not "
             "named. acq. by Bioniq, 2022 (endurance.biz, 2022-12-06); HV later financed Bioniq on its own (a member on that "
             "entry).", "Consumer & Marketplaces", extra={"status_citation": gn("vaha", "3YwVXVRM1I")}))
L.append(old("vaniday", "acquired", "Beauty and wellness booking (a Rocket Internet company; Berlin, later Singapore; founded 2015). "
             "HV entered 2015-06; sold in 2020 to a user of the app (Vulcan Post). The round is not named.",
             "Consumer & Marketplaces", extra={"status_citation": gn("vaniday", "s2el9CZkdB")}))
L.append(bare("virtual-nights", "unknown", "Virtual Nights, a nightlife community on the unit's 2007 portfolio pages. Its later "
              "state was not established.", "Media, Gaming & Advertising"))
L.append(cls("voize", status="private", rng="below_1b", stage="Seed", stage_src="web_verified", stage_conf="high",
             stage_cite=gn("voize", "d3cGd0S0Zn"), entry_date="2025-03",
             grad="graduated", grad_src="web_verified", grad_cite=gn("voize", "E03cXlGZUE"),
             focus="Healthcare & Bio", **geo("voize"),
             note="Voice AI documentation for nursing, Berlin (founded 2020; YC Winter 2022). HV's entry (HV Entry 2024, the "
                  "close) is the $9M seed announced 2025-03-31 (FinSMEs, tech.eu, found by the firm-name search); the $50M "
                  "Series A of Nov 2025 led by Balderton graduates the row (a cited later round decides inside the window).",
             rounds=[rnd("2025-03-31", "Seed", 9_000_000, None, True, gn("voize", "d3cGd0S0Zn")),
                     rnd("2025-11-17", "Series A", 50_000_000, "Balderton Capital", True, gn("voize", "E03cXlGZUE"))]))
L.append(old("webnews", "unknown", "News portal webnews.de, Unterfoehring (founded 2007). HV entered 2007-02; former portfolio "
             "from 2011. Its later state was not found.", "Media, Gaming & Advertising"))
L.append(verdict("wellhub", "not_member",
                 "Sale consideration (decisions.md D4): Wellhub (formerly Gympass) bought HV's Urban Sports Club in March "
                 "2025 (Handelsblatt, Fitt Insider); HV's export files the position under 'Wellhub' with USC's entry "
                 "(HV Entry 2015, Fund VI) and describes it as Urban Sports Club. No financing of Wellhub naming HV was "
                 "found. Urban Sports Club is the member.", ec="site_listing", conf="high", cite=gn("wellhub", "HNLUE5WZWU")))
L.append(old("wind", "unknown", "Wind Mobility, shared e-scooters, Berlin (founded 2018). HV entered at the EUR 19.2M round of "
             "Nov 2018 (EU-Startups, found by the firm-name search), not named as a series in the headline. Its later "
             "state was not found.", "Consumer & Marketplaces",
             rounds=[rnd("2018-11-22", None, 22_000_000, None, True, gn("wind", "FlKSVN3Tmc"))]))
L.append(bare("worldwidegames", "unknown", "worldwidegames, an online games company on the 2011 current list. Its later state "
              "was not established.", "Media, Gaming & Advertising"))
L.append(old("youtailor", "unknown", "Made-to-measure shirts online (YOUTAILOR, later volkshemd.de), Berlin (founded 2008). HV "
             "entered 2009-09; an exit on the 2022-25 lists. Its later state was not found.", "Consumer & Marketplaces"))
L.append(old("zeitgold", "acquired", "AI bookkeeping for small businesses, Berlin (founded 2015). HV entered 2016-04; a $29.2M "
             "Series B in May 2020 (TechCrunch). acq. by Deel, 2021 (Business Wire, 2021-08-04); HV's resulting Deel stake "
             "is not a member (D4). HV's entry round is not named.", "Fintech & Payments",
             extra={"status_citation": gn("zeitgold", "xRN283QkRR")}))
L.append(cls("zenmate", status="acquired", rng="below_1b", stage="Series A", stage_src="first_party", stage_conf="high",
             stage_cite=ZENMATE, entry_date="2014-10", focus="Security", **geo("zenmate"),
             note="Browser VPN, Berlin (founded 2013). The firm's own post of 2014-10-02, 'ZenMate scores $3.2M Series A for "
                  "its VPN-style private browsing service', is HV's entry (HV Entry 2014-08, the close). acq. by Kape "
                  "(CyberGhost's parent), 2018.",
             rounds=[rnd("2014-10-01", "Series A", 3_200_000, None, True, ZENMATE, "firm")],
             extra={"status_citation": gn("zenmate", "Ylo3aVpUZw")}))
L.append(old("zeuz", "acquired", "Managed game-server hosting, Munich (founded 2018). HV entered 2018-11; the round is not named. "
             "acq. by Improbable, 2020 (mcv/develop).", "Media, Gaming & Advertising",
             extra={"status_citation": gn("zeuz", "WTFDRFJQZw")}))
L.append(verdict("zopa", "not_member",
                 "Sale consideration (decisions.md D4): Zopa bought HV's Rvvup in Sept 2025 (Financial IT, 2025-09-02); HV's "
                 "export files the position under 'Zopa' with Rvvup's entry (HV Entry 2021, Fund VIII) and describes it as "
                 "'Rvvup developed an embedded finance and payments platform for merchants, acquired in ...'. No financing "
                 "of Zopa naming HV was found. Rvvup is the member.", ec="site_listing", conf="high", cite=EXPORT))

for slug, who in (("meemo-media-inc", "LINA CHONG (director)"), ("opkix-inc", "JOHN MCGUINNESS (director)"),
                  ("shape-up-inc", "JOHN MCGUINNESS (executive officer)"),
                  ("threatquotient-inc", "MARTIN WEBER (executive officer)")):
    L.append(verdict(slug, "not_member",
                     f"Form D name-match only (decisions.md D8): the related person {who} is a homonym of an HV team member, "
                     "not HV's partner (John McGuinness and Martin Weber of US companies; a Lina Chong at IvyCap); the "
                     "company is on no HV surface and no announcement ties it to HV. A name-match without corroboration is "
                     "not_member (COLLECTION.md s1).", ec="formd_adjudicated", conf="high"))
write("batch-007", L)
