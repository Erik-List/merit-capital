"""Duty 7 (blind self-consistency, seed 99, 45 member rows): the corrections where the blind answer held.
Every line carries the flag `unstable`. Run: NQ_TAG=du python3 judgments-dua.py"""
import judge_lib as jl
from judge_lib import cls, rnd

U = ("unstable",)


def fd(slug, sale_date):
    """The SEC index URL of the row's own Form D round first sold on `sale_date`."""
    rs = jl.FORMD_ROUNDS(slug)
    i = [k for k, r in enumerate(rs) if r.get("sale_date") == sale_date]
    if len(i) != 1:
        raise SystemExit(f"fd({slug!r}, {sale_date!r}) matched {len(i)}")
    return jl.FORMD_CITE(slug, i[0])


DRUGSTORE_S1 = "https://www.sec.gov/Archives/edgar/data/1086467/0001032210-99-000833.txt"
CARE_10Q = "https://www.sec.gov/Archives/edgar/data/1412270/000141227018000037/fy18q210-q.htm"
JUST_ENERGY_6K = "https://www.sec.gov/Archives/edgar/data/1538789/000110262415001285/exh99_1.htm"

lines = [
    # chargepoint: the band read the 2014 filing that first names Michael Linse; the company's own 2009 and 2010
    # Form Ds name Series B and Series C preferred, and the firm listed the company in 2013.
    cls("chargepoint", stage="Growth", stage_src="model", stage_conf="medium",
        stage_cite=fd("chargepoint", "2010-09-07"), entry_date="2012-04-20",
        flags=U + ("stage_disputes_band",),
        rounds=[rnd("2009-12-21", "Series B", 9550597, None, None, fd("chargepoint", "2009-12-21"), "filing"),
                rnd("2010-09-07", "Series C", 16416000, None, None, fd("chargepoint", "2010-09-07"), "filing"),
                rnd("2012-04-20", "unnamed (Form D)", 52511929, None, None, fd("chargepoint", "2012-04-20"), "filing"),
                rnd("2014-04-23", "unnamed (Form D)", 27000000, None, True, fd("chargepoint", "2014-04-23"), "filing")],
        note="Duty 7 (blind re-judgment): the Form D band's Series A is wrong. The company's own Form D of "
             "2010-09-07 covers Series C preferred and the one of 2009-12-21 Series B, so any later entry is Growth; "
             "the band rode the April 2014 filing, the first to name Michael Linse, although the firm's archived "
             "page already lists the company in 2013. The entry date is inferred as the $52.5M round first sold "
             "2012-04-20, the only round on file between the Series C and that listing; no source read names "
             "Kleiner Perkins in it, so the stage is medium."),
    # drugstore-com: the 1999 S-1 carries the Series A purchase agreement signed by the KP funds.
    cls("drugstore-com", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=DRUGSTORE_S1,
        entry_date="1998-06", flags=U,
        rounds=[rnd("1998-06", "Series A", 8000000, None, True, DRUGSTORE_S1, "filing")],
        note="Duty 7 (blind re-judgment): the S-1 of 1999-05-19 records Series A preferred sold in June and August "
             "1998 for $8.0M to five investors, and its Series A Preferred Stock Purchase Agreement is signed by "
             "Kleiner Perkins Caufield & Byers VIII, KPCB VIII Founders Fund and KPCB Life Sciences Zaibatsu Fund "
             "II; the voting agreement gives KPCB two board seats on its Series A holding. The entry is the "
             "Series A."),
    # elcomax: Freudenberg bought parts of Elcore and its sister Elcomax, Munich, in early 2018.
    cls("elcomax", status="acquired", rng="below_1b", city="Munich", city_src="web_verified", flags=U,
        note="Duty 7 (blind re-judgment): German Wikipedia's article on Freudenberg Sealing Technologies says that "
             "at the start of 2018 it took over parts of the fuel cell maker Elcore and its sister company Elcomax, "
             "based in Munich; the row reads acquired (a business sale) and the city is Munich. The round is still "
             "not named."),
    # kilowatt-financial: merged with Clean Power Finance in 2015 to form Spruce Finance.
    cls("kilowatt-financial", status="acquired", rng="below_1b", flags=U,
        note="Duty 7 (blind re-judgment): Kilowatt Financial merged with Clean Power Finance in 2015 to form Spruce "
             "Finance (Wikipedia, Spruce Finance; Just Energy's report on Form 6-K of 2015-08-13 calls it 'the "
             "merger of Clean Power Finance and Kilowatt Financial'), so the row reads acquired, as GV's Spruce "
             "Finance row does. No source read places its head office; the city stays unknown. "
             + JUST_ENERGY_6K),
    # med-zenith: the name is a Beijing cardiovascular device maker with a live site.
    cls("med-zenith", status="private", rng="below_1b", country="CN", country_src="web_verified",
        country_cite="https://www.med-zenith.com/", city="Beijing", city_src="web_verified",
        focus="Healthcare & Bio", flags=U, clear=("identity_unresolved",),
        note="Duty 7 (blind re-judgment): the company can be named. Med-Zenith (med-zenith.com, live in 2026) says "
             "it was founded in 2005, is headquartered in Beijing (Tianzhu Free Trade Zone, Shunyi) and makes "
             "devices for congenital, valvular and arrhythmic heart disease; the firm's 2021-24 tile linked a "
             "site-builder address under the same hyphenated name. The site names no investor, so the tie to the "
             "firm rests on the exact name and the China listing (medium). Private, below $1B; the round is not "
             "on record, so the stage and S2A stay undetermined."),
    # trusted: the firm's own 2017 page describes the child care company, not Trusted Health.
    cls("trusted", status="acquired", rng="below_1b", focus="Consumer & Marketplaces", city="San Francisco",
        flags=U + ("model_disputes_source",),
        note="Duty 7 (blind re-judgment): the identity was wrong. The firm's own archived page (kpcb.com/companies/"
             "trusted, captured 2017-10-20) reads 'Trusted allows parents to review and select a same-day child "
             "care provider' and links usetrusted.com, with San Francisco job openings: Trusted Labs, not the "
             "nurse staffing company Trusted Health in the Felicis book (a name collision). Care.com's 10-Q for "
             "the second quarter of 2018 records the purchase of Trusted Labs, 'an on-demand child care provider', "
             "on 2018-07-12 for up to $8.0M, and usetrusted.com now redirects to care.com: acquired. No source "
             "read names the round the firm entered. " + CARE_10Q),
    # everlane: the focus was missing.
    cls("everlane", focus="Consumer & Marketplaces", flags=U,
        note="Duty 7: the row carried no focus; direct-to-consumer apparel is Consumer & Marketplaces, as the "
             "Khosla row reads."),
]

jl.write("dua", lines)
